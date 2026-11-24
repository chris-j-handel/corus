"""v406geodesic2 · the check of the 22nd drawing: six orientations, across a round of six, and a quarter on all six at one.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_six_orientations_a_snap_by_the_corners_line.py .

A partner's saying of 23 November is the drawing's ground, as said in the transcripts, pared. Re-said: the going from one to an other of the six
orientations is a snap, with the angle of the horizon turning one quarter, and from one of the six all five others are next; it is
of the six parity balancing method of cones as universes, three universes with all moments. The saying goes on, and its end is not
yet said.
All or none, both ways: by the corner's line, a quarter from across to along; and by a quarter turn about one of the three lines.
Whole numbers alone. It opens no file and writes none. All or none: with one line not is, the check is not.
"""
import sys
from itertools import permutations, product
results = []
def line(name, ok): results.append((name, bool(ok)))

ONE_LINE, OTHER_LINE = ["357", "573", "735"], ["753", "537", "375"]
SIX = ONE_LINE + OTHER_LINE
def order(h):                                                          # a horizon, a line: its own three numbers along 3, 5 and 7; the three across, in their order
    return "".join(c for _, c in sorted(zip(h, "357"), reverse=True)) if len(set(h)) == 3 else None
ALONG = (1, 1, 1)                                                      # the corner's line
dot = lambda a, b: sum(p * q for p, q in zip(a, b))
sixth = lambda u: (-u[1], -u[2], -u[0])
across, u = [], (1, 0, -1)
for _ in range(6): across.append(u); u = sixth(u)

line("the three are across in the order of a horizon's own three numbers along 3, 5 and 7: with three other-than numbers, one of the six, and all six; the 21st drawing's round of six is that, its horizons' numbers adding to none",
     sorted(order(h) for h in permutations((2, 1, 0))) == sorted(SIX) and [order(h) for h in across] == ["357", "537", "573", "753", "735", "375"] and all(dot(h, ALONG) == 0 for h in across))
PLANES = {"7": (1, -1, 0), "3": (0, 1, -1), "5": (1, 0, -1)}           # the plane with a line of the three in it: a horizon in it has its two other numbers the same
LINES = {"3": (1, 0, 0), "5": (0, 1, 0), "7": (0, 0, 1)}
line("on a fold's plane two of the three are at one place across, with no order of the two: three planes, a plane with one of the three lines in it and the corner's line in it; on the corner's line all three are at one place, with no order of the three",
     all(dot(PLANES[k], LINES[k]) == 0 and dot(PLANES[k], ALONG) == 0 for k in "357") and all(order(tuple(a + b for a, b in zip(LINES[k], (5, 5, 5)))) is None for k in "357") and order(ALONG) is None)
beside = lambda a, b: sum(x != y for x, y in zip(a, b)) == 2 and (a[0] == b[0] or a[2] == b[2])
line("across is one quarter from along: a horizon across has its three numbers adding to none; going on across it passes one plane with a step, and from an order two of the five others are next, the 21st drawing's round of six",
     all(dot(h, ALONG) == 0 for h in across) and all(sum(beside(a, b) for b in SIX if b != a) == 2 for a in SIX))
N = 1000
near_along = {order(tuple(N + d for d in p)): tuple(N + d for d in p) for p in permutations((2, 1, 0))}
line("one quarter on, a horizon along the corner's line has the three at one place; a hair from it are all six orders: from one of the six, by the corner's line, all five others are next, thirty goings of six by five",
     sorted(near_along) == sorted(SIX) and all(dot(h, ALONG) ** 2 * 1_000_000 > 999_999 * dot(h, h) * 3 for h in near_along.values()) and len([(a, b) for a in SIX for b in SIX if a != b]) == 30 == 6 * 5)
line("a snap: a horizon turning steady from an order's middle, across, to the corner's line has that one order all the way, and none at the line; no other order is between",
     all(order(tuple(a * x + b for x in h)) == order(h) for h in across for a in (1, 2, 50) for b in (0, 1, 7, 10 ** 9)) and all(order(tuple(0 * x + b for x in h)) is None for h in across for b in (1, 7)))
def exchanges(a, b):
    seen, n = list(a), 0
    for i in range(3):
        if seen[i] != b[i]:
            j = seen.index(b[i]); seen[i], seen[j] = seen[j], seen[i]; n += 1
    return n
pairs = [(a, b) for i, a in enumerate(SIX) for b in SIX[i + 1:]]
folds = [(a, b) for a, b in pairs if exchanges(a, b) == 1]; turns = [(a, b) for a, b in pairs if exchanges(a, b) == 2]
line("the joinings of the six, two and two, are fifteen: nine folds, an order of the one line with an order of the other, 3 by 3, and six turns, three in a line and three in the other",
     len(pairs) == 15 and len(folds) == 9 == 3 * 3 and len(turns) == 6 and all((a in ONE_LINE) != (b in ONE_LINE) for a, b in folds) and all((a in ONE_LINE) == (b in ONE_LINE) for a, b in turns))
ENDS = {"+3": (1, 0, 0), "+5": (0, 1, 0), "+7": (0, 0, 1), "-3": (-1, 0, 0), "-5": (0, -1, 0), "-7": (0, 0, -1)}
seen_along = {k: tuple(3 * x - dot(e, ALONG) for x in e) for k, e in ENDS.items()}       # an end as observed along the corner's line, three times over
name_of = {v: k for k, v in seen_along.items()}
hexagon, w = [], seen_along["+3"]
for _ in range(6): hexagon.append(name_of[w]); w = sixth(w)
line("three lines at right angles, a line with two ends, six ends: observed along the corner's line they are a hexagon, a sixth of a turn apart, in turn an end of one cone and an end of the other; three are one round about the corner's line and three its other, two cones of one vertex; and the six added are none",
     len(set(hexagon)) == 6 and [k[0] for k in hexagon] == ["+", "-", "+", "-", "+", "-"] and all(dot(ENDS[k], ALONG) == (1 if k[0] == "+" else -1) for k in ENDS)
     and tuple(map(sum, zip(*ENDS.values()))) == (0, 0, 0) and tuple(map(sum, zip(*(ENDS[k] for k in ("+3", "+5", "+7"))))) == ALONG)
def then(a, b): return [[sum(a[r][k] * b[k][c] for k in range(3)) for c in range(3)] for r in range(3)]
def hand(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
ABOUT = {"3": [[1, 0, 0], [0, 0, -1], [0, 1, 0]], "5": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], "7": [[0, -1, 0], [1, 0, 0], [0, 0, 1]]}   # one quarter turn about a line of the three
def order_of(m):                                                       # the three lines' order after a turning m, the lines with no ends
    return "".join("357"[[abs(m[r][c]) for r in range(3)].index(1)] for c in range(3))
line("both ways, one quarter turn about a line of the three: the two other lines are one for the other, one inverting, the right spiral step of that pair, and the order is a fold on; by one such turn three of the five are next, the folds, and the two turns are two such turns on, about two lines",
     sorted(order_of(ABOUT[k]) for k in "357") == sorted(OTHER_LINE) and all(hand(ABOUT[k]) == 1 for k in "357") and all(sum(ABOUT[k][r][c] == -1 for r in range(3) for c in range(3)) == 1 for k in "357")
     and sorted({order_of(then(ABOUT[a], ABOUT[b])) for a in "357" for b in "357" if a != b}) == ["573", "735"])
turnings = []
for p in permutations(range(3)):
    for ways in product((1, -1), repeat=3):
        m = [[ways[c] if p[c] == r else 0 for c in range(3)] for r in range(3)]
        if hand(m) == 1: turnings.append(m)
by_order = {t: sum(order_of(m) == t for m in turnings) for t in SIX}
line("the turnings of three lines at right angles onto the three, the hand as it is, are 24: four with an order of the six, no bi-inversioning and the three bi-inversionings of the 21st drawing",
     len(turnings) == 24 and all(v == 4 for v in by_order.values()) and sum(order_of(m) == "357" and m != [[1, 0, 0], [0, 1, 0], [0, 0, 1]] for m in turnings) == 3)
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
