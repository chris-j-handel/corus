"""The Living Society Registry's societies in one table: each society a line, each line of its entry a column, as it is.
Reads Exhibit TWENTY-FIVE Living Society Registry's second part; executes; writes no file; decides nothing.

Use: python3 -I incoming/v403mgr/instruments/living_societies_in_one_table.py <root>        each society, and each check
     python3 -I incoming/v403mgr/instruments/living_societies_in_one_table.py <root> csv    the table

Returned at main, 16 November 2026, each check is:
  22 societies. Each has its society, its members, its magnitude, its members agreeing and parting, its apex and
  its seam, its passing, a field's words and its stripping. Each society's standing among ten opens with one
  unchangeable, and each of the ten unchangeables is with a living society; a rate fixing as a value, 7 and 15,
  is with four: a membrane at one potential, a cosmos at one rate, a mixture at one constant, an enzyme at one
  turnover.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
t = open(max(glob.glob(os.path.join(R, 'Exhibit_TWENTY-FIVE_Living_Society_Registry_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
second = t.split('\n# 2 ', 1)[1].split('\n# 3 ', 1)[0]
parts = re.split(r'(?m)^## (2\.\d+) (.+)$', second); E = []; labels = []
for i in range(1, len(parts), 3):
    f = {}
    for l in parts[i + 2].split('\n'):
        m = re.match(r'\*\*(.+?)\.\*\* ?(.*)', l)
        if m:
            f[m.group(1)] = m.group(2)
            if m.group(1) not in labels: labels.append(m.group(1))
    E.append((parts[i], parts[i + 1].strip(), f))
hard = open(max(glob.glob(os.path.join(R, 'Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10
one = open(max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}
OPENS = {'A middle': 'as an end', 'An opening': 'as a place', 'A sequencing': 'to one beat', 'A between': 'as a cut', 'A magnitude': 'as a magnitude', 'A two-way': 'to one side',
         'An observing': 'from behind', 'A rate': 'as a value', 'A bound': 'as a last', 'A same-existing': 'as a store'}   # a society's standing opens with one of the ten
def among(f):
    s = f.get('Standing in ten') or f.get('Standing among ten') or ''
    k = next((k for k in OPENS if s.startswith(k + ',')), None)
    return next(u for u in SEAT if u.endswith(OPENS[k])) if k else None
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n'); w.writerow(['its place in the Living Society Registry', 'society', 'the unchangeable its standing opens with', 'seated with, now', 'and 8 up, next'] + [x[0].lower() + x[1:] for x in labels])
    w.writerows([n, title, among(f), NAME[SEAT[among(f)][0]], NAME[SEAT[among(f)][1]]] + [f.get(k, '') for k in labels] for n, title, f in E); sys.exit()
print(f'{len(E)} societies; {len(labels)} lines of an entry:', ', '.join(labels))
print('Each check, all or none at all:')
whole = [k for k in labels if all(k in f for _, _, f in E)]
print(f'  is · each society has each of these lines: {", ".join(whole)}')
for k in labels:
    if k not in whole: print(f'    {k}: with {sum(1 for _, _, f in E if k in f)} of {len(E)}')
say = lambda ok, label: print(f'  {"is" if ok else "is-not"} · {label}')
say(all(among(f) for _, _, f in E), 'each society\'s standing among ten opens with one unchangeable')
with_ = {u: [title for _, title, f in E if among(f) == u] for u in SEAT}
say(all(with_.values()), 'each of the ten unchangeables is with a living society')
for u, v in with_.items(): print(f'    {u}, {SEAT[u][0]} and {SEAT[u][1]}: {"; ".join(v)}')
