"""window_scope_v366.py · exactly where the ring's keeping of its count stands, and where it does not.

Standard library only. Runs at the step beside it and changes nothing in the resolver.
Run:  python3 window_scope_v366.py

The keeping holds at the ten pairs and the 26 standings three long, at the one beat: every node taking its arriving
together. It does not carry unchanged to one node alone taking its turn from a standing the others still hold. Three
nodes each at +, carrying +, count three: the first node alone taking its turn leaves two; all three taking their turn
from the same standing leaves three.

This is not a breaking of own-turn resolving. It says that the count this identity keeps is the one-beat count, and that
what stands at a single node's turn is open. `own_turn_seam_v366.py` beside this one carries how far the two runnings
part.

This instrument arrived from the Natural Illustrating work and is re-laid at Exhibit ONE's version 366 naming. It
returns identically at the earlier naming and at this one.
"""
from ring_window_v366 import ST, step, density, joint, NAME
from itertools import product

pairs = {((1, 1), (1, 1)), ((-1, -1), (-1, -1)),
         ((1, 1), (-1, -1)), ((-1, -1), (1, 1)),
         ((1, 1), (0, -1)), ((-1, -1), (0, 1)),
         ((0, 1), (1, 1)), ((0, -1), (-1, -1)),
         ((0, 1), (0, 1)), ((0, -1), (0, -1))}
windows = [(a, b, c) for a, b, c in product(ST, repeat=3) if (a, b) in pairs and (b, c) in pairs]
assert len(windows) == 26
assert all(((s, s), (t, t)) in pairs for s, t in product((1, -1), repeat=2))
assert all((step(a, b), step(b, c)) in pairs for a, b, c in windows)
assert all(density(step(a, b), step(b, c)) - density(b, c) == joint(a, b) - joint(b, c) for a, b, c in windows)
print('26 standings three long: first beat within the ten, the step keeping the ten, and the local keeping, all hold.')

D = lambda x: sum(density(x[i], x[(i + 1) % len(x)]) for i in range(len(x)))
x = [(1, 1)] * 3
y = x.copy(); y[0] = step(x[-1], x[0])
assert all((x[i], x[(i + 1) % 3]) in pairs for i in range(3))
assert D(x) == 3 and D(y) == 2
print('One node alone taking its turn:', [NAME[a] for a in x], '->', [NAME[a] for a in y], 'count:', D(x), '->', D(y))
one_beat = [step(x[i - 1], x[i]) for i in range(3)]
assert D(one_beat) == 3
print('Every node at one beat:', [NAME[a] for a in one_beat], 'count:', D(one_beat))
print('The count is kept at the one beat; one node alone taking its turn does not carry it unchanged.')
