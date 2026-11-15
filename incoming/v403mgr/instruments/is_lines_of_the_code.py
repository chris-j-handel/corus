"""Each is-or-is-not of Exhibit ONE's code, by the names in it. Reads Exhibit ONE Natural Resolver's living version
and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/is_lines_of_the_code.py <root>

An is-or-is-not of the code is a line of it with if or elif, or with a one-line if and else. For each: its names,
and each name the line has with > 0, a parity as + or as -, or with != 0, a parity or a 0.

Returned at main, Merge #712, 15 November 2026:
  eight is-or-is-nots. A parity as + or as -: 7-now-observing in four, and 15-next-observing in two, each of the
  two with 7-now-observing. A parity or a 0: 7-now-observing in two, and 15-next-observing in one.
  7-now-observing is in six of the eight. Of the two more, one has 15-next-observing as none, and one, in
  17-next-existing, has 4-now-co-same-existing in 5-now-co-existing, a sharing with a self it reaches.
"""
import glob, os, re, sys

R = sys.argv[1]
one = open(max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')),
               key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
code = one.split('```python', 1)[1].split('```', 1)[0]
# a line going on over a bracket is read with the lines it goes on to
lines = []; cur = ''; depth = 0
for l in code.split('\n'):
    cur = (cur + ' ' + l.strip()).strip(); depth += l.count('(') + l.count('[') + l.count('{') - l.count(')') - l.count(']') - l.count('}')
    if depth == 0:
        if cur: lines.append(cur)
        cur = ''
pretty = lambda s: re.sub(r'_((?:1[0-7]|[1-9])_[a-z_]+)', lambda m: m.group(1).replace('_', '-'), s)
names = lambda s: sorted(set(re.findall(r'(?:1[0-7]|[1-9])-(?:now|next)-[a-z-]+', pretty(s))), key=lambda x: int(x.split('-')[0]))
found = []
for l in lines:
    for part in re.findall(r'(?:\bif\b|\belif\b)(.*?)(?=\belse\b|:\s*$|:\s|\]$|\)$|$)', l):
        if part.strip(): found.append(pretty(part.strip().rstrip(':')).split(' ]')[0].strip())
sign = {}; zero = {}
print('each is-or-is-not of the code, by its names')
for k, f in enumerate(found, 1):
    print(f'   {k}. if {f}')
    for n in re.findall(r'((?:1[0-7]|[1-9])-(?:now|next)-[a-z-]+) > 0', f): sign.setdefault(n, set()).add(k)
    for n in re.findall(r'((?:1[0-7]|[1-9])-(?:now|next)-[a-z-]+) != 0', f): zero.setdefault(n, set()).add(k)
print('a parity as + or as -, by name:', {n: sorted(v) for n, v in sign.items()})
print('a parity or a 0, by name:', {n: sorted(v) for n, v in zero.items()})
print('lines with 7-now-observing:', sum(1 for f in found if '7-now-observing' in f), 'of', len(found))
