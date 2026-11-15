"""Same-existing after, and a 0 between, by Exhibit ONE's table and code. Reads Exhibit ONE Natural Resolver's
living version, executes its code, and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/same_with_a_0_between.py <root>

It says five things:
  1. by the table of seventeen names: each same-existing name, with the root of the name it is after and the root
     of the name after it
  2. by the code executed, two selves alike, each with one sharing and a prior of +, bi-coupling in their pair:
     each moment, a self's prior-existing parity, the parity it is sharing, and its next-existing parity
  3. by the table: each same-existing name by its place in its four, and its three
  4. by the table: each name of the sixteen with no same-existing, by now or next, by its root and by co or of one
  5. by the code executed, the same two selves: each 0 in the society's next, by its place

Returned at main, Merge #703, 15 November 2026:
  1. 4-now-co-same-existing is after 3-now-co-observing, and 5-now-co-existing is after it;
     8-now-same-existing is after 7-now-observing, and 9-next-co-discovering is after it;
     12-next-co-same-existing is after 11-next-co-observing, and 13-next-discovering is after it;
     16-next-same-existing is after 15-next-observing, and 17-next-existing is after it.
     Each same-existing name is after an observing name, and an existing or a discovering name is after it.
  2. moments 1 to 8, each self the same as its other:
     odd moments, 1, 3, 5 and 7: its prior-existing parity inverting, + to - or - to +, and it is sharing its next
     even moments, 2, 4, 6 and 8: its prior-existing parity and its next-existing parity the same, and it is sharing 0
  3. each same-existing name is the fourth of its four, 4, 8, 12 and 16, and no other root is a fourth; its three has
     bi on both its outsides: bi-co-bi by 4 and 12, and bi-tri-bi by 8 and 16
  4. the twelve names of the sixteen with no same-existing: two by three by two, now and next, by existing or
     discovering, possibling and observing, by co and of one, each of the twelve once
  5. the same two selves: after each even moment the 0 a self is sharing is in its other's possibling within the
     society's next, the next 16-next-same-existing, and no prior has a 0
"""
import glob, os, re, sys

R = sys.argv[1]
one = open(max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')),
               key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
rows = re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \| ([a-z-]+)', one, re.M)
name = {int(n): nm for n, nm, _ in rows}; root = {int(n): r for n, _, r in rows}
assert sorted(name) == list(range(1, 18)), sorted(name)
print('1. by the table of seventeen names')
for n in sorted(name):
    if root[n] == 'same-existing':
        print(f'   {name[n]} is after {name[n - 1]}, and {name[n + 1]} is after it')
print('   the root of each name a same-existing name is after:', sorted({root[n - 1] for n in name if root[n] == 'same-existing'}),
      ' and of each name after it:', sorted({root[n + 1] for n in name if root[n] == 'same-existing'}))

ns = {}; exec(one.split('```python', 1)[1].split('```', 1)[0], ns)
resolve = ns['_1_now_existing']; society = ns['_17_next_existing']
five = {('A', 10): 'B', ('B', 10): 'A'}
state = {s: ([('k', 1)], []) for s in 'AB'}
mark = lambda p: {1: '+', -1: '-', 0: '0', None: 'none'}[p]
print('2. by the code executed, two selves alike, bi-coupling in their pair')
for m in range(1, 9):
    prior = {s: dict(state[s][0]).get('k') for s in state}
    sharing = {s: dict(resolve(*state[s])[0]).get('k') for s in state}
    state = society(state, five)
    nxt = {s: dict(state[s][0]).get('k') for s in state}
    assert prior['A'] == prior['B'] and sharing['A'] == sharing['B'] and nxt['A'] == nxt['B']
    same = prior['A'] == nxt['A']
    assert same == (sharing['A'] == 0) and same == (m % 2 == 0)
    print(f'   moment {m}: prior {mark(prior["A"])}, sharing {mark(sharing["A"])}, next {mark(nxt["A"])}   ' + ('the same on both outsides, a 0 between' if same else 'inverting, and sharing its next'))

full = re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \| ([a-z-]+)[^|]*\| [^|]*\| (co|one) \| ([a-z-]+) \|', one, re.M)
co = {int(n): c for n, _, _, c, _ in full}; three = {int(n): th for n, _, _, _, th in full}
assert sorted(co) == list(range(1, 18))
print('3. by the table, each same-existing name')
fourths = [n for n in range(1, 17) if n % 4 == 0]
assert fourths == [n for n in range(1, 17) if root[n] == 'same-existing']
for n in fourths:
    assert three[n].split('-')[0] == 'bi' and three[n].split('-')[2] == 'bi'
    print(f'   {name[n]}: the fourth of its four, its three {three[n]}')
print('4. by the table, the twelve names of the sixteen with no same-existing')
seen = {}
for n in range(1, 17):
    if root[n] == 'same-existing': continue
    key = ('now' if '-now-' in name[n] else 'next', 'existing or discovering' if root[n] in ('existing', 'discovering') else root[n], co[n])
    assert key not in seen, key; seen[key] = n
assert len(seen) == 12 and len({k[0] for k in seen}) == 2 and len({k[1] for k in seen}) == 3 and len({k[2] for k in seen}) == 2
for k, n in sorted(seen.items(), key=lambda x: x[1]): print(f'   {name[n]}: {k[0]}, {k[1]}, {"co" if k[2] == "co" else "of one"}')
print('   two by three by two, each of the twelve once')
print('5. by the code executed, the same two selves: each 0 in the society\'s next')
state = {s: ([('k', 1)], []) for s in 'AB'}
for m in range(1, 9):
    state = society(state, five)
    in_prior = any(p == 0 for s in state for _, p in state[s][0]); in_possibling = any(p == 0 for s in state for _, p in state[s][1])
    assert not in_prior and in_possibling == (m % 2 == 0)
    print(f'   after moment {m}: a 0 in a prior, {"is" if in_prior else "is-not"}; a 0 in a possibling, {"is" if in_possibling else "is-not"}')
