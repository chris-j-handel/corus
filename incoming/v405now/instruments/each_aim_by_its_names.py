#!/usr/bin/env python3
"""Each aim of the expedition by its names: the log's table, written from the aims page.

Usage: python3 -I each_aim_by_its_names.py AIMS.md NEXT_ROOT WORDS.py > Each_aim_by_its_names.csv
  AIMS.md   the aims page, read from its "# The aims, by cluster" heading if it has one, its bands as "## " headings and its aims as "- **Aim.** words *homes*" bullets
  NEXT_ROOT a checkout of the next version, its Natural Intelligence and gathering-value/
  WORDS.py  incoming/v404mgr/instruments/words_of_no_natural_naming_in_a_page.py

A row is an aim. Observing, of 7 and 15: the window's lines its words reach now, through the
opening's named concepts. Possibling, of 2 and 14: the open notes, possible explorings and possible
incoherings, at its homes' gathering sections, named by place. Discovering, of 13 and 9: the opening's concepts its
chain opens next, which no window line names yet, a name of the one list marked. A concept carried with no bold name of the opening
is missed; the table sizes a chain and decides nothing.
"""
import csv, glob, os, re, sys

aims_md, root, wordsmod = sys.argv[1:4]
import importlib.util
_spec = importlib.util.spec_from_file_location('w', wordsmod)
_w = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_w)
LISTED = [re.compile(p, re.I) for _, p in _w.WORDS]

def mark(k):
    return k + ' (of the one list)' if any(rx.search(k) for rx in LISTED) else k

WINDOW = {'now': '1', 'now-existing': '2', 'universe': '3', 'prior': '4', 'prior-existing': '5',
          'next': '6', 'next-existing': '7', 'same-existing': '8', 'same-named': '9',
          'universal set': '10', 'other-than': '12', 'nothing': '13', 'different things': '14',
          'own-parity': '15', 'bi-coupling': '16', 'moment': '1', 'is-or-is-not': 'live', 'observing': 'live',
          'possibling': 'live', 'discovering': 'live', 'self': 'live'}

ni = sorted(glob.glob(os.path.join(root, 'Natural_Intelligence_v*.md')))
ni = [p for p in ni if 'Corus' not in p][-1]
names, order = {}, []
for line in open(ni, encoding='utf-8').read().split('\n')[:80]:
    s = line.rstrip(' \\').strip()
    for b in re.findall(r'\*\*([^*]+)\*\*', s):
        k = b.strip().lower()
        if len(k) > 40 or k in names:
            continue
        names[k] = s
        order.append(k)
keys = sorted(set(names) | set(WINDOW), key=len, reverse=True)

def concepts(text):
    t = ' ' + text.lower() + ' '
    found = []
    for k in keys:
        pat = r'(?<![\w-])' + re.escape(k) + r's?(?![\w-])'
        if re.search(pat, t):
            found.append(k)
            t = re.sub(pat, ' ', t)
    return found

def chain(text):
    seen, todo = [], concepts(text)
    while todo:
        k = todo.pop(0)
        if k in seen:
            continue
        seen.append(k)
        if k in WINDOW or k not in names:
            continue
        todo += [c for c in concepts(names[k]) if c != k]
    return seen

def line_key(v):
    return (1, 0) if v == 'live' else (0, int(v))

# The gathering files and their sections.
gdir = os.path.join(root, 'gathering-value')
gath = {}
for p in glob.glob(os.path.join(gdir, '*.md')):
    title = os.path.basename(p)[:-3].replace('_', ' ')
    secs, cur = {}, 'Head'
    for l in open(p, encoding='utf-8'):
        m = re.match(r'^#{2,3} (.+)', l)
        if m:
            cur = m.group(1).strip()
            secs.setdefault(cur, 0)
            continue
        if re.match(r'^- \*\*(Possible exploring|Possible incohering)\*\*', l):
            secs[cur] = secs.get(cur, 0) + 1
    gath[title] = secs

thirty = sorted(glob.glob(os.path.join(root, 'Exhibit_THIRTY_*_v*.md')))[-1]
step_group, g = {}, None
for l in open(thirty, encoding='utf-8'):
    m = re.match(r'^## (\d+) ', l)
    if m:
        g = m.group(1)
    m = re.match(r'^(\d+)\. ', l)
    if m and g:
        step_group[int(m.group(1))] = g

ALIAS = {'Exhibit THIRTY': 'Co-Chaining Logic Registry', 'Natural Intelligence Corus': 'Natural Intelligence Corus'}
TITLES = sorted(gath, key=len, reverse=True)

def section_count(title, sec):
    secs = gath.get(title, {})
    hit = [h for h in secs if h == sec or h.startswith(sec + ' ')]
    return (hit[0], secs[hit[0]]) if hit else (None, 0)

def possibling(homes):
    found = []
    for part in re.split(r';', homes):
        part = part.strip()
        if 'gathering' in part:
            found.append(('a gathering note', None))
            continue
        m = re.match(r'Exhibit THIRTY, (steps?|group|groups) ([\d ,toand]+)', part)
        if m:
            nums = [int(n) for n in re.findall(r'\d+', m.group(2))]
            groups = sorted({str(n) for n in nums} if m.group(1).startswith('group') else
                            {step_group.get(n) for n in nums if step_group.get(n)}, key=int)
            for gr in groups:
                h, c = section_count('Co-Chaining Logic Registry', gr)
                if c:
                    found.append((f"Exhibit THIRTY's gathering, group {gr}", c))
            continue
        for t in TITLES:
            if part.startswith(t + ' '):
                for sec in re.findall(r'(\d+(?:\.\d+)?)', part[len(t):]):
                    h, c = section_count(t, sec)
                    if c:
                        found.append((f"{t}'s gathering, {sec}", c))
                break
    if not found:
        return 'an opportunity: a note at its home'
    return 'is: ' + '; '.join(dict.fromkeys(f for f, _ in found))

rows, band = [], None
_lines = open(aims_md, encoding='utf-8').read().split('\n')
_start = next((i for i, l in enumerate(_lines) if l.startswith('# The aims, by cluster')), -1)
for l in _lines[_start + 1:]:
    m = re.match(r'^## (.+)', l)
    if m:
        band = m.group(1).strip()
        continue
    m = re.match(r'^- \*\*(.+?)\*\*\s*(.*?)\s*(?:\*([^*]+)\*)?\s*$', l.strip())
    if m and band:
        aim, words, homes = m.group(1).rstrip('.,: '), m.group(2), m.group(3) or ''
        path = chain(aim + ' ' + words)
        lines = sorted({WINDOW[k] for k in path if k in WINDOW}, key=line_key)
        nxt = [k for k in order if k in path and k not in WINDOW][:4]
        nums = [x for x in lines if x != 'live']
        obs = (('is: line ' if len(nums) == 1 else 'is: lines ') + ', '.join(nums) if nums else 'is: its home') \
            + ('; the live lines' if 'live' in lines else '')
        disc = ', '.join(mark(k) for k in nxt) if nxt else "its own line, said with the window's words"
        rows.append([band, aim, words, homes, obs, possibling(homes), disc])

w = csv.writer(sys.stdout)
w.writerow(['band', 'aim', 'areas on its path', 'home', 'observing, 7 and 15', 'possibling, 2 and 14', 'discovering, 13 and 9'])
w.writerows(rows)
