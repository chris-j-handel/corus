#!/usr/bin/env python3
"""The reach of the window's lines into Exhibit THIRTY's chain.

    python3 -I reach.py EXHIBIT_THIRTY.md WINDOW_LINES.md [--csv OUT.csv] [--md OUT.md]

WINDOW_LINES.md is the window's lines, one a line, "N. sentence", a name in
bold as the window names it. A step of the chain names its concepts in bold
and by its *Adding* head, as the threads instrument reads them, and uses the
concepts it names before it. For a step, by the window's names:

  said        the window names the concept the step names
  reachable   the window names all the concepts the step uses, and not yet its own;
              a step using no named concept is reachable with no named word
  not yet     a concept the step uses is in no line of the window: its missing

For a window line, the step of the chain naming its name, or none: a line
re-saying a step, or a name no step names. A missing name is sized by the
steps waiting on it. It sizes and decides nothing.
"""
import csv, re, sys

args = sys.argv[1:]
out_csv = out_md = None
if '--csv' in args:
    i = args.index('--csv'); out_csv = args[i + 1]; del args[i:i + 2]
if '--md' in args:
    i = args.index('--md'); out_md = args[i + 1]; del args[i:i + 2]
if len(args) < 2:
    sys.exit(__doc__)
thirty, window = args

steps, group, cur = {}, None, None
for line in open(thirty, encoding='utf-8').read().split('\n'):
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

namings = {}
for n in sorted(steps):
    for b in re.findall(r'\*\*([^*]+)\*\*', steps[n]['sentence']):
        namings.setdefault(b.strip().lower(), []).append(n)
    h = adding_head(steps[n]['adding'])
    if h and 1 <= len(h.split()) <= 3 and not re.match(r'^[\d+−-]', h) and len(h) > 2:
        if n not in namings.get(h, []):
            namings.setdefault(h, []).append(n)
named = {c: v[0] for c, v in namings.items()}
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

lines = []
for line in open(window, encoding='utf-8').read().split('\n'):
    m = re.match(r'^(\d+)\. (.*)', line.strip())
    if m:
        names = [b.strip().lower() for b in re.findall(r'\*\*([^*]+)\*\*', m.group(2))]
        lines.append((int(m.group(1)), m.group(2), names))
wnames = {}
for k, _, names in lines:
    for c in names:
        for f in forms(c):
            wnames.setdefault(f, k)

def in_window(c):
    return next((wnames[f] for f in forms(c) if f in wnames), None)

def first_use(c):
    p = pattern(c)
    return next((n for n in sorted(steps) if p.search(re.sub(r'\*\*', '', steps[n]['sentence']))), None)

rows, held = [], {}
for n in sorted(steps):
    s = steps[n]
    own = sorted(c for c, v in namings.items() if n in v)
    used = [c for c in concepts_in(s['sentence']) if named[c] < n and c not in own]
    missing = sorted({c for c in used if in_window(c) is None}, key=lambda c: (named[c], c))
    if own and all(in_window(c) is not None for c in own):
        status = 'said'
    elif not missing:
        status = 'reachable' if used else 'reachable, no named word'
    else:
        status = 'not yet'
    for c in missing:
        held.setdefault(c, []).append(n)
    rows.append({'step': n, 'group': s['group'], 'sentence': s['sentence'], 'names': own,
                 'status': status, 'missing': missing,
                 'lines': sorted({in_window(c) for c in own + used if in_window(c) is not None})})

def short(t, k=110):
    t = re.sub(r'\*\*', '', t)
    return t if len(t) <= k else t[:k].rsplit(' ', 1)[0] + ' ...'

said = [r for r in rows if r['status'] == 'said']
reach = [r for r in rows if r['status'] == 'reachable']
bare = [r for r in rows if r['status'] == 'reachable, no named word']
notyet = [r for r in rows if r['status'] == 'not yet']
out = []
out.append(f"Steps {len(rows)}: said {len(said)}, reachable {len(reach)} resting on the lines' names and {len(bare)} using no named word, not yet {len(notyet)}.")
out.append('')
out.append('The window\'s lines, a line with the step naming its name:')
for k, text, names in lines:
    at = [f"{c} {named[c]}" for c in names if c in named]
    alt = [f"{c} {named[f]}" for c in names if c not in named for f in forms(c) if f in named]
    if at or alt:
        at_step = '; '.join(at + alt)
    else:
        uses = [f"{c}, used from step {first_use(c)}" if first_use(c) else f"{c}, used at no step" for c in names]
        at_step = 'named at no step: ' + '; '.join(uses)
    out.append(f"  {k}. {short(text, 90)}  -> {at_step}")
out.append('')
out.append('Said, a step whose name the window names:')
for r in said:
    out.append(f"  {r['step']}. {short(r['sentence'])}")
out.append('')
out.append('Reachable, a step resting on the lines\' names, its own name not yet:')
for r in reach:
    out.append(f"  {r['step']}. {short(r['sentence'])}")
out.append('')
out.append('Missing, a name no line of the window names, by the steps waiting on it:')
for c, ns in sorted(held.items(), key=lambda kv: (-len(kv[1]), named[kv[0]], kv[0]))[:40]:
    out.append(f"  {c} (named at {named[c]}): {len(ns)} steps")
text = '\n'.join(out)
print(text)

if out_md:
    open(out_md, 'w', encoding='utf-8').write(text + '\n')
if out_csv:
    with open(out_csv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['step', 'group', 'sentence', 'names', 'status', 'missing', 'window lines'])
        for r in rows:
            w.writerow([r['step'], r['group'], r['sentence'], '; '.join(r['names']), r['status'],
                        '; '.join(f"{c} {named[c]}" for c in r['missing']),
                        '; '.join(map(str, r['lines']))])
