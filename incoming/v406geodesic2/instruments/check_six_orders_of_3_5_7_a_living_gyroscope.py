"""v406geodesic2 · the check of the 21st drawing: six orders of 3, 5 and 7, right spiraling, and a living gyroscope.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_six_orders_of_3_5_7_a_living_gyroscope.py .

Two sayings of a partner, 23 November, are the drawing's ground, as said in the transcripts, pared. Re-said:
the order in three parts, 0124, a three and 689, with its three as 357, 573 and 735, and as 753, 537 and 375, and it is right
spiraling; and the twentieth drawing is a living gyroscope for aiming over the horizon.
All or none, both ways: the three going round, and an observing going round three at their places.
Whole numbers alone. It opens no file and writes none. All or none: with one line not is, the check is not.
"""
import sys
from itertools import permutations
results = []
def line(name, ok): results.append((name, bool(ok)))

ONE_LINE, OTHER_LINE = ["357", "573", "735"], ["753", "537", "375"]          # a partner's two lines, as said
SIX = ONE_LINE + OTHER_LINE
DIAMOND = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
whole = lambda three: [int(c) for c in "0124" + three + "689"]
cut = lambda o: [sorted(o[1:2]), sorted(o[2:4]), sorted(o[4:7]), sorted(o[7:9]), sorted(o[9:10])]
podal = lambda n: 10 - n                                                      # the podaling about 5

line("a partner's six are all the orders of 3, 5 and 7, none twice, and with all six the order's rows are the diamond's: 1; 2, 4; the three; 6, 8; and 9, with 0 apart",
     sorted(SIX) == sorted("".join(p) for p in permutations("357")) and len(set(SIX)) == 6 and all(cut(whole(t)) == DIAMOND for t in SIX))
parts = [[0, 1, 2, 4], [3, 5, 7], [6, 8, 9]]
line("the three parts, 0124, the three and 689: of a pair of cones, before its widest, its widest and after it; the podaling about 5 carries 1, 2, 4 to 9, 8, 6; and the parts added are 7, 15 and 23, 8 on and 8 on, 45 together",
     parts[0][1:] == DIAMOND[0] + DIAMOND[1] and parts[1] == DIAMOND[2] and parts[2] == DIAMOND[3] + DIAMOND[4] and [len(r) for r in DIAMOND].index(3) == 2
     and [podal(n) for n in (1, 2, 4)] == [9, 8, 6] and sorted(podal(n) for n in parts[1]) == parts[1] and [sum(p) for p in parts] == [7, 15, 23] and 23 - 15 == 15 - 7 == 8 and sum(map(sum, parts)) == 45)
on = lambda t: t[1:] + t[0]                                                   # the opening number gone to its end
line("in a line of the two, a three is the one before it with its opening number gone to its end, and a third such step is the line's opening again: a round of three",
     all(on(a) == b for a, b in zip(ONE_LINE, ONE_LINE[1:])) and on(ONE_LINE[2]) == ONE_LINE[0] and all(on(a) == b for a, b in zip(OTHER_LINE, OTHER_LINE[1:])) and on(OTHER_LINE[2]) == OTHER_LINE[0])
swap37 = lambda t: "".join({"3": "7", "7": "3", "5": "5"}[c] for c in t)
line("the other line is the one line with 3 for 7, the podaling about 5, a three for a three in their places; gone the other way it is the same three threes, and not in their places",
     [swap37(t) for t in ONE_LINE] == OTHER_LINE and sorted(t[::-1] for t in ONE_LINE) == sorted(OTHER_LINE) and [t[::-1] for t in ONE_LINE] != OTHER_LINE)
def exchanges(t):                                                             # exchanges of two from 357, odd or even
    seen, n = list("357"), 0
    for i in range(3):
        if seen[i] != t[i]:
            j = seen.index(t[i]); seen[i], seen[j] = seen[j], seen[i]; n += 1
    return n
at_its_place = lambda t: [c for c, d in zip(t, "357") if c == d]
line("the one line is three turns, from 357 by no exchange of two or by two; the other line is three folds, by one exchange, a fold with one of the three at its place: 753 with 5, 537 with 7 and 375 with 3",
     [exchanges(t) for t in ONE_LINE] == [0, 2, 2] and [exchanges(t) for t in OTHER_LINE] == [1, 1, 1] and [at_its_place(t) for t in OTHER_LINE] == [["5"], ["7"], ["3"]] and [len(at_its_place(t)) for t in ONE_LINE] == [3, 0, 0])

# ---- three lines at right angles, the three-right-angle triangle's corners: 3, 5 and 7 at them
def carry(t):                                                                 # a three as a carrying of the corners: the corner of 357's k-th to the corner of t's k-th
    return [[1 if "357"[c] == t[r] else 0 for c in range(3)] for r in range(3)]
def hand(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
def then(a, b): return [[sum(a[r][k] * b[k][c] for k in range(len(b))) for c in range(len(b[0]))] for r in range(len(a))]
SAME = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
line_as_it_is = lambda m: all(sum(row) == 1 for row in m)                        # the line (1, 1, 1) to itself
line("on three lines at right angles the one line's three have the hand as it is: no turn and two thirds of a turn about the line (1, 1, 1), three of a step reaching the three again; the other line's three invert the hand, a fold twice no step; all six carry the three corners to the three corners",
     [hand(carry(t)) for t in ONE_LINE] == [1, 1, 1] and [hand(carry(t)) for t in OTHER_LINE] == [-1, -1, -1] and all(line_as_it_is(carry(t)) for t in SIX)
     and all(then(then(carry(t), carry(t)), carry(t)) == SAME for t in ONE_LINE) and all(then(carry(t), carry(t)) == SAME for t in OTHER_LINE)
     and [sum(carry(t)[k][k] for k in range(3)) for t in ONE_LINE] == [3, 0, 0])
EXCHANGE, STEP = [[0, 1], [1, 0]], [[0, 1], [-1, 0]]                          # (x, y) to (y, x); and to (y, -x), the right spiral step
hand2 = lambda m: m[0][0] * m[1][1] - m[0][1] * m[1][0]
line("a pair and a three: a pair's exchange inverts the hand, and with one inverting, (x, y) to (y, -x), it is the right spiral step, the hand as it was, four to its pair again; a three's step, (x, y, z) to (y, z, x), has the hand as it was with none inverting, three to its three again",
     hand2(EXCHANGE) == -1 and hand2(STEP) == 1 and then(then(STEP, STEP), then(STEP, STEP)) == [[1, 0], [0, 1]] and then(STEP, STEP) == [[-1, 0], [0, -1]]
     and hand(carry("573")) == 1 and then(then(carry("573"), carry("573")), carry("573")) == SAME)

# ---- an observing going round three at their places: 3, 5 and 7 a third of a turn apart about a line, observed across
order = lambda u: "".join(c for _, c in sorted(zip(u, "357"), reverse=True))  # across, by the observing's own line u, with u's three adding to none
sixth = lambda u: (-u[1], -u[2], -u[0])                                       # the observing a sixth of a turn on, about the line (1, 1, 1)
u, seen = (1, 0, -1), []
for _ in range(6): seen.append(order(u)); u = sixth(u)
side_by_side = lambda a, b: sum(x != y for x, y in zip(a, b)) == 2 and (a[0] == b[0] or a[2] == b[2])
line("both ways: with the three at their places a third of a turn apart and the observing going round, across, the six orders are one round of six, a sixth of a turn a three, 357, 537, 573, 753, 735 and 375, in turn of the one line and of the other, a step an exchange of two side by side",
     u == (1, 0, -1) and seen == ["357", "537", "573", "753", "735", "375"] and all((seen[k] in ONE_LINE) == (k % 2 == 0) for k in range(6)) and all(side_by_side(seen[k], seen[(k + 1) % 6]) for k in range(6)))
line("with it the one line goes a third of a turn on with a three, the other line a third of a turn the other way, counter-turning, and a three with the observing from behind, three sixths on, is that three gone the other way",
     [seen.index(t) for t in ONE_LINE] == [0, 2, 4] and [seen.index(t) for t in OTHER_LINE] == [3, 1, 5] and all(seen[(k + 3) % 6] == seen[k][::-1] for k in range(6)))

# ---- round eight and round ten
EIGHT = (1, 3, 5, 7)
alike = lambda t, group, n: all(dict(zip("357", t)).get(str(a * b % n), str(a * b % n)) == str(int(dict(zip("357", t)).get(str(a), str(a))) * int(dict(zip("357", t)).get(str(b), str(b))) % n) for a in group for b in group)
line("round eight, 3 by 5 is 7, 5 by 7 is 3 and 7 by 3 is 5, and a number of the three by its own is 1: the three are alike, and the multiplying is the same with all six orders",
     (3 * 5 % 8, 5 * 7 % 8, 7 * 3 % 8) == (7, 3, 5) and all(a * a % 8 == 1 for a in (3, 5, 7)) and all(alike(t, EIGHT, 8) for t in SIX))
line("round ten the three are not alike: 5 by an odd number is 5, and 3 by 7 is 1; with two of the six orders alone ten's multiplying is the same, 357 and 753, the 5 at its place",
     all(5 * a % 10 == 5 for a in (1, 3, 5, 7, 9)) and 3 * 7 % 10 == 1 and [t for t in SIX if alike(t, (1, 3, 5, 7, 9), 10)] == ["357", "753"])
X, Y, Z = (1, -1, -1), (-1, 1, -1), (-1, -1, 1)                               # two inversions on different lines of the three: the line as it is, the third
by = lambda a, b: tuple(p * q for p, q in zip(a, b))
line("the three bi-inversionings of three lines at right angles, two of the three inverting and the third as it is: one twice is no step, and two in a row are the third, the multiplying of 3, 5 and 7 round eight",
     all(by(a, a) == (1, 1, 1) for a in (X, Y, Z)) and by(X, Y) == Z and by(Y, Z) == X and by(Z, X) == Y and all(hand([[a[0], 0, 0], [0, a[1], 0], [0, 0, a[2]]]) == 1 for a in (X, Y, Z)))

# ---- the nine, laid by rows about its 5 and laid from its centre, 1
PAIRS = [(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1)]
by_rows = {(x, y): 5 + x + 3 * y for (x, y) in PAIRS}
ROUND = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
from_centre = {(0, 0): 1, **{p: 2 + k for k, p in enumerate(ROUND)}}
line("the nine laid two ways, and one right spiral step of both, (x, y) to (y, -x): by rows, the 5 at the centre, it is multiplying by 7 round ten; from the centre, 1 at the centre and 2 to 9 round it, it is 2 round the eight, one way; the centre is at its place with both",
     sorted(from_centre.values()) == list(range(1, 10)) and all(by_rows[(y, -x)] == by_rows[(x, y)] * 7 % 10 for (x, y) in PAIRS)
     and all(from_centre[(y, -x)] == 2 + (from_centre[(x, y)] - 2 - 2) % 8 for (x, y) in ROUND) and by_rows[(0, 0)] == 5 and from_centre[(0, 0)] == 1)

# ---- the twentieth drawing as a gyroscope
row = lambda m: "".join(str(int(c) * m % 10) for c in "357")
line("the twentieth drawing's turning reaches two of the six orders alone: by 9, two right spiral steps, 357 is 753; by 7 and by 3 the row is on the line 1, 5, 9; and with all its steps the 5 alone of the nine is at its place: the turning is about the 5, a line through it observed along",
     [row(m) for m in (1, 7, 9, 3)] == ["357", "159", "753", "951"] and [n for n in range(1, 10) if all(n * m % 10 == n for m in (1, 7, 9, 3))] == [5])
walk = [(0, 1)]
while len(walk) < 60: walk.append((walk[-1][1], sum(walk[-1]) % 10))
def far(k, n=10):                                                             # prior two added, the pair with moment k, by doubling the moment: a second way
    a, b = 0, 1
    for bit in bin(k)[2:]:
        a, b = a * (2 * b - a) % n, (a * a + b * b) % n
        if bit == "1": a, b = b, (a + b) % n
    return a, b
FAR = [10 ** 18, 10 ** 100, 7 ** 300]
line("living, and steady: prior two added turns the diamond one right spiral step with fifteen moments, the same with all moments; a moment far past all stepping, 10 to the 18th, to the 100th, and on, has the pair the round of sixty says, found a second way by doubling the moment",
     (walk[59][1], sum(walk[59]) % 10) == (0, 1) and all(walk[(k + 15) % 60] == tuple(v * 7 % 10 for v in walk[k]) for k in range(60))
     and all(far(m + k) == walk[(m + k) % 60] and far(m + k + 15) == tuple(v * 7 % 10 for v in far(m + k)) for m in FAR for k in range(60)))
line("over the horizon, by one turn, with all numbers: a number however far is on the diamond by its ending; multiplying by a number ending in 7 is one right spiral step; a number ending at 0, 2, 4, 6 or 8 has 2 a part and at 0 or 5 has 5, a prime past 5 at a corner; and one short and one past of an ending 3 are at 2 and 4, of 7 at 6 and 8",
     all(((m + r) * (10 ** 50 + 7)) % 10 == r * 7 % 10 for m in FAR[:2] for r in range(1, 10)) and all((m + e) % 2 == 0 for m in FAR[:2] for e in (0, 2, 4, 6, 8)) and all((m + e) % 5 == 0 for m in FAR[:2] for e in (0, 5))
     and all(((m + 3 - 1) % 10, (m + 3 + 1) % 10, (m + 7 - 1) % 10, (m + 7 + 1) % 10) == (2, 4, 6, 8) for m in FAR[:2]))
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
