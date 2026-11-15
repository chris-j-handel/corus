"""A reader's match beside part one: each living line having 17 as a 1 by any of its wordings, and whether a living string of the part is in it.
A locating, deciding nothing. Usage: python3 -I part_one_reach.py <repo root>"""
import re, sys, glob, os
root = sys.argv[1]
part = open(os.path.join(root, 'incoming/v401mgr/parts/Part_one_17_no_next_1.md'), encoding='utf-8').read()
strings = []
for line in part.split('\n'):
    if line.startswith('| ') and not line.startswith('| The living file') and not line.startswith('|---'):
        cells = re.split(r'(?<!\\)\|', line)[1:-1]
        if len(cells) >= 4:
            strings.append(cells[2].strip().replace('\\|', '|'))
pat = re.compile(r"next('s)? 1(?!\d)|1-now-existing again|as its 1-now-existing|as 1-now-existing|opens again|second 1\b|1 of (2nd|3rd|[4-9]th)|1, a next momentary")
files = sorted(glob.glob(os.path.join(root, 'Natural_Intelligence_v*.md')) + glob.glob(os.path.join(root, 'Exhibit_*_v*.md')) + glob.glob(os.path.join(root, 'Natural_Intelligence_Corus_v*.md')))
tot = cov = 0; out = []
for f in files:
    head = ''; name = os.path.basename(f).split('_v')[0].replace('Exhibit_', '').replace('_', ' ')
    for line in open(f, encoding='utf-8').read().split('\n'):
        if line.startswith('#'): head = line.lstrip('# ').strip()[:40]; continue
        for m in pat.finditer(line):
            tot += 1
            if any(s and s in line for s in strings): cov += 1
            else: out.append(f"{name} · {head} · [{m.group(0)}] …{line[max(0, m.start()-70):m.end()+50].strip()}…")
print(len(strings), 'living strings in the part;', tot, 'living places by the match;', cov, 'having a string of the part;', tot - cov, 'having none:')
seen = set()
for o in out:
    if o not in seen: seen.add(o); print(' ', o[:300])
