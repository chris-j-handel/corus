"""Same-existing after, and a 0 between, by Exhibit ONE's table and code. Reads Exhibit ONE Natural Resolver's
living version, executes its code, and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/same_with_a_0_between.py <root>

It says two things:
  1. by the table of seventeen names: each same-existing name, with the root of the name it is after and the root
     of the name after it
  2. by the code executed, two selves alike, each with one sharing and a prior of +, bi-coupling in their pair:
     each moment, a self's prior-existing parity, the parity it is sharing, and its next-existing parity

Returned at main, Merge #698, 15 November 2026:
  1. 4-now-co-same-existing is after 3-now-co-observing, and 5-now-co-existing is after it;
     8-now-same-existing is after 7-now-observing, and 9-next-co-discovering is after it;
     12-next-co-same-existing is after 11-next-co-observing, and 13-next-discovering is after it;
     16-next-same-existing is after 15-next-observing, and 17-next-existing is after it.
     Each same-existing name is after an observing name, and an existing or a discovering name is after it.
  2. moments 1 to 8, each self the same as its other:
     odd moments, 1, 3, 5 and 7: its prior-existing parity inverting, + to - or - to +, and it is sharing its next
     even moments, 2, 4, 6 and 8: its prior-existing parity and its next-existing parity the same, and it is sharing 0
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
