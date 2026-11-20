#!/usr/bin/env python3
"""The threads of Exhibit THIRTY's co-chaining.

A thread is a word or a concept of the chain, tied back to the step naming it
and forward to the later steps needing it. It runs through the sentences
using it, between them in their order, and around the chain into the files
citing its steps.

Usage:
  python3 -I threads.py EXHIBIT_THIRTY.md [FROM [TO]] [--json OUT.json] [--csv OUT.csv] [--open]

Three kinds of thread, each the chain's own:
  a name    a word in bold in a step's sentence names a concept at that step
  an adding a step's *Adding* line opens with the concept it adds; a head of
            one to three words, before its first comma, is taken as a name
  a cite    *step N*, *steps N and M*, *steps N to M* in a step's sentence

What it finds, for a reader to go through, deciding nothing:
  back      a named concept a step uses, tied to the step naming it
  forward   the later steps using a concept a step names
  ahead     a concept a step uses before the step naming it
  twice     a concept named at two steps or more
  unneeded  a concept named at a step and used by no later step
  cite      a cite of a later step, or a cite whose own words meet nothing
            of the cited step's sentence or Adding line
With --open, only the steps with an ahead, a twice, an unneeded or a cite
are printed.
"""
import json, re, sys

args = sys.argv[1:]
out_json, out_csv, only_open = None, None, False
if '--csv' in args:
    i = args.index('--csv'); out_csv = args[i + 1]; del args[i:i + 2]
if '--json' in args:
    i = args.index('--json'); out_json = args[i + 1]; del args[i:i + 2]
if '--open' in args:
    args.remove('--open'); only_open = True
path = args[0]
lo = int(args[1]) if len(args) > 1 else 1
hi = int(args[2]) if len(args) > 2 else 10 ** 6

lines = open(path, encoding='utf-8').read().split('\n')
steps, group, cur = {}, None, None
for line in lines:
    g = re.match(r'^## (\d+) ', line)
    if g:
        group = int(g.group(1)); continue
    m = re.match(r'^(\d+)\. (.*)', line)
    if m and group:
        cur = int(m.group(1))
        steps[cur] = {'group': group, 'sentence': m.group(2).strip(), 'adding': ''}
        continue
    a = re.match(r'^\s*\*Adding: (.*?)\.?\*\s*$', line)
    if a and cur:
        steps[cur]['adding'] = a.group(1).strip()

IRREGULAR = {'self': ['selves'], 'me': [], 'society': ['societies']}
ARTICLES = ('a ', 'an ', 'the ')

def forms(c):
    f = {c}
    last = c.split(' ')[-1]
    head = c[: len(c) - len(last)]
    if last in IRREGULAR:
        f.update(head + x for x in IRREGULAR[last])
    elif re.search(r'[^aeiou]y$', last):
        f.add(head + last[:-1] + 'ies')
    elif last[-1:].isalpha():
        f.update({c + 's', c + 'es'})
    return f

def pattern(c):
    alts = '|'.join(re.escape(x) for x in sorted(forms(c), key=len, reverse=True))
    return re.compile(r'(?<![\w-])(?:' + alts + r')(?![\w-])', re.I)

def adding_head(text):
    h = re.split(r'[,;:]', text)[0].strip().lower()
    for art in ARTICLES:
        if h.startswith(art):
            h = h[len(art):]
    return h

namings = {}  # concept -> [(step, kind)]
for n in sorted(steps):
    for b in re.findall(r'\*\*([^*]+)\*\*', steps[n]['sentence']):
        c = b.strip().lower()
        namings.setdefault(c, []).append((n, 'name'))
    h = adding_head(steps[n]['adding'])
    if h and 1 <= len(h.split()) <= 3 and not re.match(r'^[\d+−-]', h) and len(h) > 2:
        if not any(s == n for s, _ in namings.get(h, [])):
            namings.setdefault(h, []).append((n, 'adding'))

named = {c: v[0][0] for c, v in namings.items()}
pats = {c: pattern(c) for c in named}
order = sorted(named, key=len, reverse=True)

def concepts_in(sentence):
    t = re.sub(r'\*\*', '', sentence).replace("'s", '')
    found = []
    for c in order:
        if pats[c].search(t):
            found.append(c)
            t = pats[c].sub(' ', t)
    return found

STOP = set('''a an the of and or is are to it its as with by for from at on in be
its their this that these those one two no not each all any other than own which
who whose while when then there here so same step steps both one's itself'''.split())

def words(text):
    ws = {w for w in re.findall(r"[a-z][a-z'-]+", text.lower().replace("'s", '')) if w not in STOP}
    return {('self' if w == 'selves' else w) for w in ws}

def stems(ws):
    out = set()
    for w in ws:
        for part in w.split('-'):
            if len(part) > 3:
                out.add(part[:4])
    return out

CITE = re.compile(r'(steps?) (\d+)((?:(?:, | and | to |, and )\d+(?=[,.;:)]| and|$))*)')

def cites_in(sentence):
    out = []
    for m in CITE.finditer(sentence):
        if m.group(1) == 'step' and m.group(3).startswith(' to '):
            continue  # a walk of numbers, step 1 to 3 to 5, and no cite
        nums = [int(m.group(2))] + [int(x) for x in re.findall(r'\d+', m.group(3))]
        if m.group(3).startswith(' to ') and len(nums) == 2:
            nums = list(range(nums[0], nums[1] + 1))
        before = sentence[max(0, m.start() - 110): m.start()]
        before = re.split(r'[:;(]', before)[-1] + ' ' + sentence[m.end(): m.end() + 50]
        out.append({'nums': nums, 'before': before.strip(' ,')})
    return out

uses = {c: [] for c in named}
rows = []
for n in sorted(steps):
    s = steps[n]
    found = concepts_in(s['sentence'])
    own = sorted(c for c, v in namings.items() if any(k == n for k, _ in v))
    back = sorted((named[c], c) for c in found if named[c] < n and c not in own)
    ahead = sorted((named[c], c) for c in found if named[c] > n)
    for c in found:
        if named[c] != n:
            uses[c].append(n)
    cites = []
    for ci in cites_in(s['sentence']):
        for k in ci['nums']:
            if k >= n:
                cites.append({'cite': k, 'words': ci['before'], 'open': 'a cite of a step at or after its own'})
                continue
            if k not in steps:
                cites.append({'cite': k, 'words': ci['before'], 'open': 'a cite of no step'})
                continue
            meet = stems(words(ci['before'])) & stems(words(steps[k]['sentence'] + ' ' + steps[k]['adding']))
            cites.append({'cite': k, 'words': ci['before'], 'open': '' if meet or not words(ci['before']) else 'its words meet nothing of the cited step'})
    rows.append({'step': n, 'group': s['group'], 'sentence': s['sentence'], 'adding': s['adding'],
                 'names': own, 'back': back, 'ahead': ahead, 'cites': cites})

for r in rows:
    r['forward'] = {c: [m for m in uses[c] if m > r['step']] for c in r['names']}
    r['twice'] = [c for c in r['names'] if len(namings[c]) > 1 and namings[c][0][0] != r['step']]
    r['unneeded'] = [c for c in r['names'] if named[c] == r['step'] and not r['forward'][c]]
    r['open'] = bool(r['ahead'] or r['twice'] or r['unneeded'] or any(c['open'] for c in r['cites']))

if out_json:
    json.dump({'namings': namings, 'rows': rows}, open(out_json, 'w'), indent=1)

if out_csv:
    import csv
    with open(out_csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['step', 'group', 'sentence', 'names', 'back', 'ahead', 'forward', 'cites', 'open'])
        for r in rows:
            fwd = '; '.join(f"{c}: {fw[0]} to {fw[-1]}" if fw else f"{c}: ends at itself"
                            for c, fw in r['forward'].items())
            opens = (['ahead'] if r['ahead'] else []) + (['named again'] if r['twice'] else []) \
                + (['ends at itself'] if r['unneeded'] else []) + (['cite'] if any(c['open'] for c in r['cites']) else [])
            w.writerow([r['step'], r['group'], r['sentence'], '; '.join(r['names']),
                        '; '.join(f"{c} {k}" for k, c in r['back']),
                        '; '.join(f"{c} {k}" for k, c in r['ahead']), fwd,
                        '; '.join(str(c['cite']) for c in r['cites']), ', '.join(opens)])

for r in rows:
    if not lo <= r['step'] <= hi or (only_open and not r['open']):
        continue
    print(f"{r['step']}. [{r['group']}] {r['sentence']}")
    print(f"   adding   {r['adding']}")
    for k, c in r['back']:
        print(f"   back     {c} <- {k}")
    for k, c in r['ahead']:
        print(f"   ahead    {c} -> named at {k}")
    for c, fw in r['forward'].items():
        tag = ' (named first at %d)' % named[c] if named[c] != r['step'] else ''
        shown = ', '.join(map(str, fw[:10])) + (' and on' if len(fw) > 10 else '')
        print(f"   forward  {c}{tag} -> {shown if fw else 'no later step'}")
    for c in r['cites']:
        print(f"   cite     {c['cite']} by '{c['words'][-50:]}'" + (f"  OPEN: {c['open']}" if c['open'] else ''))
    print()
