"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/cells_by_society.py
"""
import itertools, sys
sys.argv = ['x']
exec(open('incoming/v383Op/records/cells.py').read().split("rules = [dict")[0])
rules = [dict(zip(S_VALUES, combo)) for combo in itertools.product(OUT, repeat=4)]

def D(r):
    # a sharing is a changing shared: the new parity where the carrying changed, and 0 where it did not
    return all((c2 == 1 and o == 0) or (c2 == -1 and o == -1) for c2, o in r.values())

def still(rule, selves, joins, T=60, cap=512):
    ops = list(itertools.product((1, -1), repeat=len(selves)))[:cap]
    for op in ops:
        C = run(rule, selves, joins, dict(zip(selves, op)), T)
        if any(len(set(C[s][T // 2:])) == 1 for s in selves):
            return True
    return False

def fed():   # two lone selves, each releasing to a third and to no other
    return ['a', 'b', 's'], {'a': ['s'], 'b': ['s'], 's': []}

def crossed(p, q):
    selves = [('P', i) for i in range(p)] + [('Q', i) for i in range(q)]
    joins = {('P', i): [('P', (i + 1) % p)] for i in range(p)}
    joins.update({('Q', i): [('Q', (i + 1) % q)] for i in range(q)})
    joins[('P', 0)].append(('Q', 0)); joins[('Q', 0)].append(('P', 0))
    return selves, joins

B = [r for r in rules if cond_B(r)]
print('living step at one other:', len(B))
soc = {'torus 3 by 3': torus(3, 3), 'torus 2 by 3': torus(2, 3), 'two lone selves releasing to a third': fed(), 'spirals of 3 and 4 crossed': crossed(3, 4), 'spirals of 2 and 3 crossed': crossed(2, 3)}
left = B
for name, (selves, joins) in soc.items():
    left = [r for r in left if not still(r, selves, joins)]
    print('  and no self still at', name, ':', len(left), '| files in:', FILES in left)
print('with a sharing a changing shared, alone:', sum(D(r) for r in rules))
print('living step at one other and a sharing a changing shared:', [r for r in B if D(r)])
print('all three:', [r for r in left if D(r)])
# behaviours of what is left without D
import collections
sig = collections.defaultdict(list)
for r in left:
    key = []
    for selves, joins in (ring(1), ring(2), ring(3), torus(2, 3), torus(3, 3), fed()):
        for op in list(itertools.product((1, -1), repeat=len(selves)))[:64]:
            C = run(r, selves, joins, dict(zip(selves, op)), 16)
            key.append(tuple(tuple(C[s]) for s in selves))
    sig[tuple(key)].append(r)
print('left without the sharing condition:', len(left), 'cells at', len(sig), 'distinct carryings')
