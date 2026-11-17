"""Each of the seventeen names, between selves across, between selves along, or of a self's own resolving: read
out of the living sentences of the seventeen and out of Exhibit ONE Natural Resolver's code executed, for the
is-or-is-not? *Each odd name is along, and each even name is across.*
Reads the newest at the root of Natural Intelligence, Exhibit THREE Natural Numbers and Exhibit ONE Natural
Resolver, and `incoming/v403mgr/The_seventeen_names_in_one_table.csv`; executes; decides nothing; writes nothing.

Use: python3 -I incoming/v404helping/instruments/each_name_between_selves_or_a_selfs_own.py <root>

What it reads, each all or none at all:
  1. Natural Intelligence's sentences, word for word: *One entry, six names between selves and ten names of a
     self's own resolving are seventeen.*, *Ten are 3, 4, 5, 7 and 8 with now and 11, 12, 13, 15 and 16 with
     next.*, *Of the names between selves, the four across are even, 2, 6, 10 and 14.* and *The two along are
     odd, 9 and 17.*; and Exhibit THREE Natural Numbers's *Of six, across names, 2, 6, 10 and 14, are each even
     and along names, 9 and 17, both odd.*
  2. The table of the seventeen names, its columns of a name, its root, its odd or even, and its one entry,
     six between selves and ten of a self's own resolving: each name by them.
  3. The code executed with three selves: a self's sharing reaches an other self by its 6, its 10 and its 9
     alone, each into its other's 14; with none of the three, no parity of a self reaches an other.

Returned at main, 16 November 2026, after Merge #855: each of five sentences word for word. Between selves
across, four names, each even and each of the root possibling: 2, 6, 10 and 14. Between selves along, two, each
odd: 9, of the root discovering, and 17, of the root existing. Of a self's own resolving, ten: six odd, 3, 5,
7, 11, 13 and 15, and four even, each of the root same-existing, 4, 8, 12 and 16. One entry, 1. The code:
with a self's 6, its 10 or its 9 to an other, that other's 14 has its sharing with the next moment, each of
three; with none of the three, each other self's 14 is empty, eight moments.
"""
import csv, glob, os, re, sys

R = sys.argv[1]
ver = lambda p: int(re.search(r'_v(\d+)', p).group(1))
newest = lambda stem: max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver)
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'[*`_\\]', '', s)).strip()
NI, THREE, ONE = (open(newest(s), encoding='utf-8').read() for s in ('Natural_Intelligence', 'Exhibit_THREE_Natural_Numbers', 'Exhibit_ONE_Natural_Resolver'))
SENT = [(NI, "One entry, six names between selves and ten names of a self's own resolving are seventeen."),
        (NI, 'Ten are 3, 4, 5, 7 and 8 with now and 11, 12, 13, 15 and 16 with next.'),
        (NI, 'Of the names between selves, the four across are even, 2, 6, 10 and 14.'),
        (NI, 'The two along are odd, 9 and 17.'),
        (THREE, 'Of six, across names, 2, 6, 10 and 14, are each even and along names, 9 and 17, both odd.')]
found = [norm(s) in norm(t) for t, s in SENT]
print(f'living sentences word for word: {sum(found)} of {len(SENT)}'); assert all(found)

T = list(csv.reader(open(os.path.join(R, 'incoming', 'v403mgr', 'The_seventeen_names_in_one_table.csv'), encoding='utf-8'))); H = T[0]
col = lambda start: next(i for i, h in enumerate(H) if h.startswith(start))
c_name, c_root, c_odd, c_kind = col('name ['), col('root ['), col('odd or even ['), col('one entry, six between selves')
kinds = {}
for r in T[1:]: kinds.setdefault(r[c_kind].split(',')[0] + (',' + r[c_kind].split(',')[1] if 'between' in r[c_kind] else ''), []).append((r[c_name], r[c_root], r[c_odd]))
for k, v in kinds.items():
    print(f"   {k}: {len(v)} · " + ', '.join(f'{n} ({o}, {root})' for n, root, o in v))
across = kinds['between selves, across']; along = kinds['between selves, along']; own = kinds["a self's own resolving"]
assert all(o == 'even' and root == 'possibling' for _, root, o in across) and all(o == 'odd' for _, _, o in along)
even_own = [n for n, root, o in own if o == 'even']; assert all(root == 'same-existing' for n, root, o in own if o == 'even')
print(f"   each even name across: {len(across)} of {len(across) + len(even_own)} even names; the even names of a self's own resolving: {', '.join(even_own)}")

code = {}; exec(ONE.split('```python', 1)[1].split('```', 1)[0], code)
world = code['_17_next_existing']
def reached(routes, moments=8):
    S = {'a': ([('s', 1)], []), 'b': ([], []), 'c': ([], [])}
    got = False
    for m in range(moments):
        S = world(S, routes); got = got or bool(S['b'][1]) or bool(S['c'][1])
    return got
for n in (6, 10, 9):
    print(f"   the code: a self's {n} to an other, that other's 14 has its sharing: {reached({('a', n): 'b'})}"); assert reached({('a', n): 'b'})
print(f"   the code: with none of 6, 10 and 9, an other's 14 has a sharing: {reached({})}"); assert not reached({})
print('nothing written')
