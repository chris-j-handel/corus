"""Same atoms touching, as a doing: a prior folded through a 0 to its next, spiraling open, of one hand. All or none.

By whole numbers and their parts only: no measuring. A sphere is a field's picture of an atom, used for its centre only.
Four same ones, each touching each, have their centres as four corners, each two the same apart.
A fold: the oldest of four goes through the middle of its three others, to the same far on the other side.
Run: python3 incoming/V401atom/instruments/bi_folding_spiral_check.py
"""
from fractions import Fraction as F
import itertools
sub = lambda u, v: tuple(a - b for a, b in zip(u, v))
dot = lambda u, v: sum(a * b for a, b in zip(u, v))
cross = lambda u, v: (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
d2 = lambda u, v: dot(sub(u, v), sub(u, v))

def chain(first, n):
    c = [tuple(F(x) for x in p) for p in first]
    zeros = []
    for i in range(n):
        d, a, b, e = c[-4], c[-3], c[-2], c[-1]
        zero = tuple((x + y + z) / 3 for x, y, z in zip(a, b, e))        # the middle of the three
        c.append(tuple(2 * m - x for m, x in zip(zero, d)))              # the oldest, through it, the same far
        zeros.append(zero)
    return c, zeros

T = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
print("1 four same ones, each touching each: each two centres the same apart:", len({d2(u, v) for u, v in itertools.combinations(T, 2)}) == 1)
N = 240
R, Z = chain(T, N)
side = d2(T[0], T[1])
print("2 a fold, each of", N, ": the oldest of four through the middle of its three others, to the same far on the other side")
print("  the middle of the three is the middle of the prior and its next: one point, a 0, the three's own middle:",
      all(tuple((x + y) / 2 for x, y in zip(R[i], R[i + 4])) == Z[i] for i in range(N)))
print("  the prior, the 0 and the next are on one line, at a right angle to each line of the three:",
      all(dot(sub(R[i + 4], R[i]), sub(R[i + 1], R[i + 2])) == 0 and dot(sub(R[i + 4], R[i]), sub(R[i + 2], R[i + 3])) == 0 for i in range(N)))
print("  the next is touching each of the three it is folded through, as the prior was:", all(d2(R[i + 4], R[i + j]) == side for i in range(N) for j in (1, 2, 3)))
print("3 the folds, one after one: a co-chaining")
touch = [sum(1 for j in range(len(R)) if j != i and d2(R[i], R[j]) == side) for i in range(len(R))]
print("  each one, but the three at each end, is touching six: the three before it and the three after it:", all(t == 6 for t in touch[3:-3]))
print("  no centre is a centre a second time: the spiraling closes at none, in", N, "folds:", len(set(R)) == len(R))
far = [d2(R[i], R[0]) for i in range(len(R))]
print("  each fourth one is farther from the first than the fourth before it: it goes on along:", all(far[i + 4] > far[i] for i in range(4, len(R) - 4)))
hand = lambda c: [dot(sub(c[i + 1], c[i]), cross(sub(c[i + 2], c[i + 1]), sub(c[i + 3], c[i + 2]))) for i in range(len(c) - 3)]
hR = hand(R)
print("  its hand is one, the same by each four one after one:", len({h > 0 for h in hR}) == 1 and all(h != 0 for h in hR))
f = [sub(R[i + 4], R[i]) for i in range(N)]
turns = {dot(f[i], f[i + 1]) / dot(f[i], f[i]) for i in range(N - 1)}
print("  each fold's line and the next fold's line have 1 of 3 the same, each step:", turns == {F(1, 3)}, "· each fold the same long:", len({dot(x, x) for x in f}) == 1)
L, _ = chain([T[1], T[0], T[2], T[3]], N)
hL = hand(L)
print("4 the same four, its first two in the other order: the other hand, each step:", len({h > 0 for h in hL}) == 1 and (hL[0] > 0) != (hR[0] > 0))
back, _ = chain([R[7], R[6], R[5], R[4]], 4)
print("5 a fold taken from its next: through the same 0, to its prior: the one direction through a 0, and its other:", back[4:] == [R[3], R[2], R[1], R[0]])
