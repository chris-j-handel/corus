"""Session v383Op, at its improving: the stable forms a small torus comes to, from every opening.

Runs from the repository root: python3 incoming/v383Op/stable_forms.py
The plain rule of plain_rule.py, matched to the resolver in torus_rule.py. A torus of p along and
q across, each self releasing along to the next along and sharing across to the next across, the
last to the first; begun at EVERY opening, each self carrying + or -, none offered at the first
momentary and none from beyond; the selves stepped together. A stable form here is one coming
again: the carryings and the changings shared, in sequence, that the torus comes to and is at from
then on. Two that are one carried a self on, or one inverted, are told apart here and reckoned as
two. Reported: how many, and at how many momentaries each is again.
"""
import collections, itertools


def step(c, o, p, q):
    c2, o2 = {}, {}
    for (i, j) in c:
        arrived = [x for x in (o[((i - 1) % p, j)], o[(i, (j - 1) % q)]) if x]
        s = arrived[0] if arrived and len(set(arrived)) == 1 else 0
        n = s if s else -c[(i, j)]
        c2[(i, j)] = n
        o2[(i, j)] = n if n != c[(i, j)] else 0
    return c2, o2


for p, q in ((1, 3), (2, 2), (2, 3), (3, 3), (3, 4), (3, 5)):
    selves = [(i, j) for i in range(p) for j in range(q)]
    forms = {}
    for opening in itertools.product((1, -1), repeat=p * q):
        c, o = dict(zip(selves, opening)), {s: 0 for s in selves}
        seen = set()
        while True:
            k = (tuple(c.values()), tuple(o.values()))
            if k in seen:
                break
            seen.add(k)
            c, o = step(c, o, p, q)
        cycle, k0 = [], k
        while True:
            cycle.append(k)
            c, o = step(c, o, p, q)
            k = (tuple(c.values()), tuple(o.values()))
            if k == k0:
                break
        forms[min(cycle)] = len(cycle)
    again = collections.Counter(forms.values())
    print('torus %d by %d: %5d openings come to %3d stable forms; again at: %s'
          % (p, q, 2 ** (p * q), len(forms), ', '.join('%d at %d' % (again[t], t) for t in sorted(again))))
