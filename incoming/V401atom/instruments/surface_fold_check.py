"""On a surface: six around one, and a fold of three, right from left and left from right, a thread straight along. All or none.

By whole numbers only: no measuring. Two steps a and b of one length, sixty apart: each has 2 of itself, and the two have 1.
Run: python3 incoming/V401atom/instruments/surface_fold_check.py
"""
from fractions import Fraction as F
dot = lambda u, v: 2 * u[0] * v[0] + 2 * u[1] * v[1] + u[0] * v[1] + u[1] * v[0]
side = lambda along, v: along[0] * v[1] - along[1] * v[0]            # which side of a line along a point is: +, - or on it
add = lambda u, v: (u[0] + v[0], u[1] + v[1]); sub = lambda u, v: (u[0] - v[0], u[1] - v[1])
six = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
print("1 six same ones around one, on a surface, each touching it:")
print("  each is the same far from the one, and sixty from its next around, full around in six:",
      all(dot(v, v) == 2 for v in six) and all(dot(six[i], six[(i + 1) % 6]) == 1 for i in range(6)))
print("  each touches its two next to it around, and no other of the six:", all(sum(1 for w in six if dot(sub(v, w), sub(v, w)) == 2) == 2 for v in six))
ok = True
for a in six:                                                        # each of the six as the line along
    on = [v for v in six if side(a, v) == 0]; one = [v for v in six if side(a, v) > 0]; other = [v for v in six if side(a, v) < 0]
    ok = ok and len(on) == 2 and on[0] == tuple(-x for x in on[1]) and len(one) == 2 and len(other) == 2
print("  by a line along through the one: two of the six are on it, each straight across its other; two are on its one side, and two on its other:", ok)
print("  six ways: co, along, two; and across, two of the side before and two of the side after")
N = 240
c = [(0, 0), (0, 1), (1, 0)]                                         # three same ones, each touching each
zeros = []
for i in range(N):
    d, a, b = c[-3], c[-2], c[-1]
    zeros.append((F(a[0] + b[0], 2), F(a[1] + b[1], 2)))             # the middle of the two
    c.append(sub(add(a, b), d))                                      # the oldest through it, the same far on the other side
print("2 a fold on a surface, each of", N, ": the oldest of three through the middle of its two others")
print("  the middle of the two is the middle of the prior and its next: one point, a 0:", all((F(c[i][0] + c[i + 3][0], 2), F(c[i][1] + c[i + 3][1], 2)) == zeros[i] for i in range(N)))
print("  the next is touching each of the two, as the prior was:", all(dot(sub(c[i + 3], c[i + j]), sub(c[i + 3], c[i + j])) == 2 for i in range(N) for j in (1, 2)))
along = sub(c[2], c[0])
print("3 folds one after one:")
print("  each second one is one same step along from the one two before it: two lines along, each straight:", all(sub(c[i + 2], c[i]) == along for i in range(len(c) - 2)))
s = [side(along, sub(c[i + 3], c[i])) for i in range(N)]
print("  each fold goes across from the one line to the other, and the next fold from the other to the one: right from left, and left from right, in turn:",
      all(x != 0 for x in s) and all(s[i] == -s[i + 1] for i in range(N - 1)))
zs = [(zeros[i + 1][0] - zeros[i][0], zeros[i + 1][1] - zeros[i][1]) for i in range(N - 1)]
print("  the 0s, one by each fold, are on one line along, between the two lines, each the same step from the 0 before it: a thread:",
      len(set(zs)) == 1 and zs[0] == (F(along[0], 2), F(along[1], 2)))
print("  no centre is a centre a second time, and no 0 a 0 a second time: it closes at none:", len(set(c)) == len(c) and len(set(zeros)) == len(zeros))
print("  each one touches four of the co-chaining: the two before it and the two after it; and of them two are along, its own line's:",
      all(sum(1 for j in range(len(c)) if j != i and dot(sub(c[i], c[j]), sub(c[i], c[j])) == 2) == 4 for i in range(2, len(c) - 2)))

# a fold's line, and the thread's line: a cone of thirty. Thirty is 3 of 4 the same, of the squares; sixty is 1 of 2.
def folds(first, n):
    c = list(first); f = []
    for i in range(n):
        d, a, b = c[-3], c[-2], c[-1]
        c.append(sub(add(a, b), d)); f.append(sub(c[-1], d))
    return c, f
print("4 each fold's line, a prior through its 0 to its next; and the thread's line, the 0s' line along:")
allok = True; n = 0
for a in six:                                                    # each of six lines along, and each side first
    for b in (six[(six.index(a) + 1) % 6], six[(six.index(a) - 1) % 6]):
        n += 1
        c, f = folds([(0, 0), b, a], 60)
        thr = sub(c[2], c[0])
        thirty = all(F(dot(x, thr) ** 2, dot(x, x) * dot(thr, thr)) == F(3, 4) and dot(x, thr) > 0 for x in f)
        turn = all(side(thr, f[i]) == -side(thr, f[i + 1]) != 0 for i in range(len(f) - 1))
        sixty = all(F(dot(f[i], f[i + 1]), dot(f[i], f[i])) == F(1, 2) for i in range(len(f) - 1))
        two = all(F(dot(sub(c[i + 1], c[i]), f[i]) ** 2, 2 * dot(f[i], f[i])) == F(3, 4) and F(dot(sub(c[i + 2], c[i]), f[i]) ** 2, 2 * dot(f[i], f[i])) == F(3, 4) for i in range(len(f)))
        allok = allok and thirty and turn and sixty and two
print("  cases, each of six lines along and each side first:", n)
print("  each fold's line is thirty from the thread's line, and has the same way along it as each other fold: each fold is in the one cone of thirty about the thread's line;")
print("  folds one after one are its one edge and its other, in turn, sixty apart, one half the same;")
print("  and from a fold's prior, its two others are thirty each side of the fold's line: the fold's own cone's two edges:", allok)
