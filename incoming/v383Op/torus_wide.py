"""Session v383Op: Exhibit ONE's rule of the torus at more odd pairs. Asks numpy.

Runs from the repository root: python3 incoming/v383Op/torus_wide.py [largest p, default 45]
The plain rule of plain_rule.py, matched to the resolver itself in torus_rule.py, run at each odd
pair, p from 1 to the largest p and q from p to three times it. Arrangement and opening as
Exhibit ONE's table of the torus of selves says them. The rule: the parities come again at q at a
q more than twice p, and at 4p at each other q.
"""
import sys
import numpy as np


def period(p, q):
    i, j = np.indices((p, q))
    c = np.where((i + j) % 2 == 0, -1, 1).astype(np.int8)
    o = np.zeros((p, q), np.int8)
    seen, t = {}, 0
    while True:
        key = c.tobytes() + o.tobytes()
        if key in seen:
            return t - seen[key], seen[key]
        seen[key] = t
        a, b = np.roll(o, 1, axis=0), np.roll(o, 1, axis=1)      # from along, from across
        s = np.where((a != 0) & (b != 0), np.where(a == b, a, 0), a + b)
        n = np.where(s != 0, s, -c).astype(np.int8)
        o = np.where(n != c, n, 0).astype(np.int8)
        c = n
        t += 1


top = int(sys.argv[1]) if len(sys.argv) > 1 else 45
agree, part = 0, []
for p in range(1, top + 1, 2):
    for q in range(p, 3 * top + 1, 2):
        T, first = period(p, q)
        rule = q if q > 2 * p else 4 * p
        if T == rule:
            agree += 1
        else:
            part.append((p, q, T, rule))
print('odd pairs, p to %d and q to %d: agreeing with the rule at %d of %d' % (top, 3 * top, agree, agree + len(part)))
for p, q, T, rule in part:
    print('  parting: %d by %d comes again at %d, the rule says %d' % (p, q, T, rule))
