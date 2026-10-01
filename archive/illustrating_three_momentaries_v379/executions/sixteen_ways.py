"""The sixteen ways a next could follow from a prior and a now, Natural Intelligence 2.4, each run
through the momentaries from each of the four joint forms (prior, now) -> (now, next).
A way carries a joint form still where prior = now = next, a form named still; a way loses the prior
where the next is the same at both values of the prior. Run from the repository root:
    python3 incoming/illustrating_three_momentaries_v379/executions/sixteen_ways.py
"""
from itertools import product
P = (1, -1)
forms = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
s = lambda f: ''.join('+' if v > 0 else '-' for v in f)
rows = []
for bits in product(P, repeat=4):                      # next at (++), (+-), (-+), (--)
    way = dict(zip([(1, 1), (1, -1), (-1, 1), (-1, -1)], bits))
    nxt = lambda p, n: way[(p, n)]
    still = [f for f in forms if nxt(*f) == f[1] and f[0] == f[1]]          # prior = now = next
    uses_prior = any(nxt(1, n) != nxt(-1, n) for n in P)
    # the longest run from any form before a joint form comes again, and whether all four are met
    reach = set(); seen_cycle = None
    for f in forms:
        path = [f]; cur = f
        for _ in range(8):
            cur = (cur[1], nxt(*cur)); path.append(cur)
        reach |= set(path)
    cycle_len = None
    cur = (1, 1); path = [cur]
    for _ in range(8):
        cur = (cur[1], nxt(*cur))
        if cur in path: cycle_len = len(path) - path.index(cur); break
        path.append(cur)
    name = {(1,-1,1,-1): 'next as now', (-1,1,-1,1): 'next as now inverted',
            (1,1,-1,-1): 'next as prior', (-1,-1,1,1): 'next as prior inverted, the living step',
            (1,-1,-1,1): 'prior and now agreeing', (-1,1,1,-1): 'prior and now parting, the exclusive or',
            (1,1,1,1): 'next always +', (-1,-1,-1,-1): 'next always -'}.get(bits, '')
    rows.append((bits, name, still, uses_prior, len(reach), cycle_len))
print(f"{'next at ++ +- -+ --':<22}{'carries prior':<15}{'forms still':<14}{'forms reached':<15}{'cycle from ++':<14}way")
for bits, name, still, up, nreach, cyc in rows:
    print(f"{' '.join('+' if b>0 else '-' for b in bits):<22}{('yes' if up else 'no'):<15}{(' '.join(s(f) for f in still) or 'none'):<14}{nreach:<15}{str(cyc):<14}{name}")
