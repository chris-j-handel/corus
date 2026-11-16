"""Each of medicine's rows of Exhibit ELEVEN Natural Medicine, a field's naming whole as the field has it, with
the fixing the file has it of, that one of the ten as Exhibit TWENTY-TWO Resolving the Hard Problem Registry has
it, its two names eight apart, a now name with a next name, and the hard problem of the registry by its title.
Two living files read with each other: medicine's own sorting of its rows, and the registry's.
Reads Exhibit ELEVEN Natural Medicine, Exhibit TWENTY-TWO Resolving the Hard Problem Registry, Exhibit ONE
Natural Resolver, and the managing session's table of each hard problem, a file of `incoming/v403mgr` written by
its own instrument out of Exhibit TWENTY-TWO; executes; writes no file; decides nothing. All or none at all, by
each row. That table is found by its two columns, *hard problem* and *its unchangeable*, one table and no other,
and by no name of its file: its file's name is re-said with no change here.
No sentence of Exhibit ELEVEN Natural Medicine for a body is read, changed or said again by it: a row is a name.

Use: python3 -I incoming/v403cohering/instruments/medicines_rows_with_the_names.py <root>        each check, and each row
     python3 -I incoming/v403cohering/instruments/medicines_rows_with_the_names.py <root> csv    the table, one line with each row

What it reads. A fixing of Exhibit ELEVEN: a line opening in bold with its name, a dash, and one of the ten with
*fixed*, as *Forced-choosing — a two-way fixed to one side.*; its rows are after it, one after one with a middle
dot between, to the first full stop. One of the ten is found by its ending, as *to one side*. A hard problem by
its title: the row's words and the title's the same, a first *a*, *an* or *the* passed over, or one whole in the other.

Returned at main, 16 November 2026: six fixings of Exhibit ELEVEN, each one of the ten by its ending, and nineteen
rows. Sixteen are a hard problem of the registry by its title, and each of the sixteen is with the same one of
the ten in the two files. Three are no hard problem by their title: *cancer's somatic account and its rival*,
*Anaesthesia* and *Easterlin pairing*. Exhibit ELEVEN has each of the six with *fixed*, and one by an other first
word, *a bound* with the registry's *a completing*.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def ver(p):
    m = re.search(r'_v(\d+)', p); return int(m.group(1)) if m else 0
def newest(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver), encoding='utf-8').read()
one = newest('Exhibit_ONE_Natural_Resolver')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
hard = newest('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry')
ten_line = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
TEN = {t: (f'{h} fixing {t}', int(a), int(b)) for h, t, a, b in re.findall(r'(an? [a-z-]+) fixing ([a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', ten_line)}
assert len(TEN) == 10

FIXINGS = []                                   # (its name, as written, its ending, its rows)
for l in newest('Exhibit_ELEVEN_Natural_Medicine').split('\n'):
    m = re.match(r'^\*\*([A-Z][a-z]+-[a-z]+) — (an? [a-z-]+ fixed ([a-z ]+?))\.\*\* (.+)$', l)
    if m:
        first = re.split(r'(?<=[a-z\)])\. ', m.group(4), maxsplit=1)[0]
        FIXINGS.append((m.group(1), m.group(2), m.group(3), [x.strip().rstrip('.') for x in first.split(' · ')]))

def head(p):
    with open(p, encoding='utf-8', newline='') as f: return next(csv.reader(f), [])
TABLES = [p for p in sorted(glob.glob(os.path.join(R, 'incoming', 'v403mgr', '*.csv'))) if {'hard problem', 'its unchangeable'} <= set(head(p))]
assert len(TABLES) == 1, f'the table of each hard problem is one table by its two columns, and {len(TABLES)} are found'
H = list(csv.reader(open(TABLES[0], encoding='utf-8', newline='')))
ti, ui = H[0].index('hard problem'), H[0].index('its unchangeable')
def key(s): return re.sub(r'\s+', ' ', re.sub(r"[^a-z' ]", ' ', re.sub(r'^(a|an|the) ', '', s.lower()))).strip()
TITLES = [(key(h[ti]), h) for h in H[1:]]

ROWS = []
for name, written, ending, rows in FIXINGS:
    ten = TEN.get(ending)
    for row in rows:
        k = key(row)
        hits = [h for kk, h in TITLES if kk == k] or [h for kk, h in TITLES if re.search(r'\b' + re.escape(k) + r'\b', kk) or re.search(r'\b' + re.escape(kk) + r'\b', k)]
        h = hits[0] if len(hits) == 1 else None
        ROWS.append([row, f'{name} — {written}', ten[0] if ten else '', NAME[ten[1]] if ten else '', NAME[ten[2]] if ten else '',
                     f'{h[0]} · {h[ti]}' if h else ('' if not hits else f'{len(hits)} titles'), ('the same' if h[ui] == ten[0] else h[ui]) if h and ten else ''])
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(["medicine's row, a field's naming whole [living ELEVEN]", 'its fixing, as written [living ELEVEN]', 'its unchangeable [living TWENTY-TWO]',
                'its now name [living TWENTY-TWO]', 'its next name, 8 up [living TWENTY-TWO]',
                'the hard problem of the registry by its title, with its number [executed]', 'its unchangeable by the registry [executed]'])
    w.writerows(ROWS); sys.exit()

print(f"{len(FIXINGS)} fixings of Exhibit ELEVEN Natural Medicine with rows, {len(ROWS)} rows")
found = [r for r in ROWS if r[5] and not r[5].endswith('titles')]
checks = [
    ('each fixing of Exhibit ELEVEN is one of the ten by its ending', all(e in TEN for _, _, e, _ in FIXINGS)),
    ('each row found by its title is with the same one of the ten in the two files', all(r[6] == 'the same' for r in found)),
    ('no row is two titles of the registry', not any(r[5].endswith('titles') for r in ROWS)),
]
for what, ok in checks: print(('  is · ' if ok else '  is-not · ') + what)
print(f"  rows a hard problem of the registry by its title: {len(found)}; rows with no hard problem by its title: {len(ROWS) - len(found)}: " + '; '.join(r[0] for r in ROWS if not r[5]))
for name, written, ending, rows in FIXINGS:
    ten = TEN.get(ending)
    first_other = '' if not ten or written.split(' fixed ')[0] == ten[0].split(' fixing ')[0] else f" · an other first word: {written.split(' fixed ')[0]}, the registry's {ten[0].split(' fixing ')[0]}"
    print(f"    {name} — {written}: {len(rows)} rows · {ten[0] if ten else 'not of the ten'}, with {NAME[ten[1]]} and {NAME[ten[2]]}{first_other}")
print('each check is' if all(ok for _, ok in checks) else 'a check is-not')
