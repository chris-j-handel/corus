"""v406geodesic2 · the logic of this window in its order, executed: podaling, routing and orienting, a turn beside stepping, and resolving.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v406geodesic2/instruments/the_logic_of_podaling_routing_and_orienting_executed.py \
      incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py

By a partner's asking of 23 November: the learning of the logical work, beside the learning of the drawings by an eye.
A line here is a sentence of the session's page for Exhibit THIRTY-TWO Natural Prime Numbering, by its number, and no drawing is
opened. It opens v406Reiman's cell from its own file for the lines by nand alone, and writes that cell in no second place.
Whole numbers alone. All or none: with one line not is, the logic is not. The drawings' own checks execute more of a sentence, apart.
"""
import importlib.util, sys
from itertools import permutations, product
from math import gcd
from pathlib import Path
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", Path(sys.argv[1]))
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
nand, other_than, both, either, adding = its.nand, its.other_than, its.both, its.either, its.adding_with_nand
results = []
def line(n, name, ok): results.append((n, name, bool(ok)))
IS, NOT = True, False
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
about = lambda st: (lambda n: 2 * st - n)                               # a podaling about a station
def by(n, stations):
    for st in stations: n = about(st)(n)
    return n
SPAN = range(-240, 241)

# ---------------- podaling ----------------
line(1, "a podaling about a station carries a number to twice the station less the number, and twice it is the number again",
     all(about(s)(n) == 2 * s - n and about(s)(about(s)(n)) == n for s in range(0, 241, 15) for n in SPAN))
line(2, "two podalings in a row are a going on, by twice the way from the one station to the other",
     all(by(n, (s, t)) == n + 2 * (t - s) for s in range(0, 241, 15) for t in range(0, 241, 15) for n in range(0, 61)))
STATIONS = (30, 60, 90, 120, 150, 180)
line(3, "three in a row are one podaling, about the one station less the next with the third: an even number of podalings in a row is a going on, and an odd number is one podaling",
     all(by(n, (s, t, u)) == about(s - t + u)(n) for s in STATIONS for t in STATIONS for u in STATIONS for n in range(0, 61))
     and all(by(n, STATIONS[:k]) == (n + 30 * k if k % 2 == 0 else about(15 * (k + 1))(n)) for k in range(1, 7) for n in range(0, 61)))
line(4, "on a line of stations 30 apart, a podaling about 30 carries a number of 0 to 60 to a number of 0 to 60, and about 90 to a number of 120 to 180; about 30 and then about 90 it is 120 on",
     all(0 <= about(30)(n) <= 60 and 120 <= about(90)(n) <= 180 and by(n, (30, 90)) == n + 120 for n in range(0, 61)))
PLACES = [n for n in range(1, 60) if gcd(n, 30) == 1]
place = {k + 1: p for k, p in enumerate(PLACES)}; name = {p: k for k, p in place.items()}
line(5, "the sixteen places of a pair of cones no spiral of 2, 3 or 5 crosses are the names 1 to 16 in their order, and the living files' three moves are the line's own: 8 up is 30 on, 9 less a podaling about 15, 17 less a podaling about 30, and 9 less and then 17 less is 8 up",
     len(PLACES) == 16 and all(place[k + 8] == place[k] + 30 and place[9 - k] == about(15)(place[k]) for k in range(1, 9)) and all(place[17 - k] == about(30)(place[k]) for k in range(1, 17))
     and all(17 - (9 - k) == k + 8 and by(place[k], (15, 30)) == place[k] + 30 for k in range(1, 9)))
def places_of(n, wide): return [bool((n >> i) & 1) for i in range(wide)]
def same(a, b):
    ok = IS
    for one, other in zip(a, b): ok = both(ok, other_than(both(either(one, other), nand(one, other))))
    return ok
others = lambda a: [other_than(x) for x in a]
def moved(n, which):
    m = places_of(n - 1, 4)
    return {"8 up": m[:3] + [other_than(m[3])], "17 less": others(m), "9 less": others(m[:3]) + [m[3]]}[which]
line(6, "by nand alone, a name less one, in four places, has the three moves as other-thans of its places: 8 up of its top place, 17 less of all four, and 9 less of its three low places",
     all(same(moved(n, "8 up"), places_of((n + 8 if n <= 8 else n - 8) - 1, 4)) and same(moved(n, "17 less"), places_of(17 - n - 1, 4)) for n in range(1, 17))
     and all(same(moved(n, "9 less"), places_of(9 - n - 1, 4)) for n in range(1, 9)))
WIDE = 10
def less(a, b): return adding(adding(a, others(b))[:WIDE], places_of(1, WIDE))[:WIDE]
def podaling(n, s): return less([NOT] + places_of(s, WIDE)[:WIDE - 1], places_of(n, WIDE))
def in_a_row(x, k):
    for _ in range(k): x = other_than(x)
    return x
line(7, "by nand alone, a podaling is the nand's adding, twice its station less a number, and two in a row are a going on; and an other-than twice is the same again, an even number of them a me and an odd number an other",
     all(same(podaling(n, s), places_of(2 * s - n, WIDE)) for s in range(0, 241, 30) for n in range(0, 2 * s + 1))
     and all(same(podaling(int(sum(v << i for i, v in enumerate(podaling(n, 30)))), 60), places_of(n + 60, WIDE)) for n in range(0, 61))
     and all(in_a_row(x, k) == (x if k % 2 == 0 else other_than(x)) for x in (IS, NOT) for k in range(9)))

# ---------------- routing ----------------
FOUR = (30, 60, 90, 120)
route = [37]
for st in FOUR: route.append(about(st)(route[-1]))
line(8, "a me-now at 37 goes by four moments, a podaling about 30, 60, 90 and 120, a cone on with a moment: to 23, 97, 83 and 157; its second is 60 on and its fourth 120 on, and all five are primes",
     route == [37, 23, 97, 83, 157] and route[2] == 37 + 60 and route[4] == 37 + 120 and all(map(prime, route)))
rows = [FOUR[a:b] for a in range(4) for b in range(a + 1, 5)]
line(9, "the rows of the four moments, one after an other, are ten: four of one, three of two, two of three and one of four; four of the ten are a going on, by 60, 60, 60 and 120, and six are one podaling",
     len(rows) == 10 and [sum(len(r) == k for r in rows) for k in (1, 2, 3, 4)] == [4, 3, 2, 1]
     and sorted(by(0, r) for r in rows if len(r) % 2 == 0) == [60, 60, 60, 120] and sum(len(r) % 2 for r in rows) == 6)
line(10, "prior, now and next are three pairs of cones, 0 to 60, 60 to 120 and 120 to 180: a me at its prime scale p passes through as p, 60 less p, 60 and p, 120 less p, 120 and p and 180 less p, two in a pair",
     all([p] + [by(p, (30, 60, 90, 120, 150)[:k]) for k in range(1, 6)] == [p, 60 - p, 60 + p, 120 - p, 120 + p, 180 - p] for p in PLACES)
     and all([n // 60 for n in (p, 60 - p, 60 + p, 120 - p, 120 + p, 180 - p)] == [0, 0, 1, 1, 2, 2] for p in PLACES))
DIAMOND = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
grid = {(a, b): a + 3 * b for a in (1, 2, 3) for b in (0, 1, 2)}
podal = lambda n: 10 - n
line(11, "ten in an order, 0124357689, its 0 apart, is a diamond of nine, the three by three of 1 to 9: an arc a step of 1 one way and of 3 the other, a row odd or even all through; the podaling about 5 carries its upper triangle to its lower, a row to a row",
     [d for r in DIAMOND for d in r] == [1, 2, 4, 3, 5, 7, 6, 8, 9] and all(sorted(n for (a, b), n in grid.items() if (a - 1) + b == r) == DIAMOND[r] for r in range(5))
     and all(len({d % 2 for d in r}) == 1 for r in DIAMOND) and [sorted(podal(d) for d in r) for r in DIAMOND] == DIAMOND[::-1])
wide = lambda n: (n % 60) if (n % 60) <= 30 else 60 - (n % 60)
line(12, "a pair of cones observed across is that diamond: at 0, 15, 30, 45 and 60 a row's numbers are one more than the cone's width in fifteens",
     [1 + wide(n) // 15 for n in (0, 15, 30, 45, 60)] == [len(r) for r in DIAMOND])
walk = [(0, 1)]
while len(walk) < 60: walk.append((walk[-1][1], sum(walk[-1]) % 10))
line(13, "prior two added, round ten, is a route of sixty moments and no fewer, a pair of cones, its 0s at 0, 15, 30 and 45, the diamond's rows",
     (walk[59][1], sum(walk[59]) % 10) == (0, 1) and len(set(walk)) == 60 and [k for k, w in enumerate(walk) if w[0] == 0] == [0, 15, 30, 45])

# ---------------- orienting ----------------
PAIRS = [(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1)]
by3 = {(x, y): 5 + x + 3 * y for (x, y) in PAIRS}; by7 = {(x, y): (5 + x + 7 * y) % 10 for (x, y) in PAIRS}
line(14, "a right spiral step, a pair (x, y) to (y, -x), is multiplying by 7 round ten, a number of the diamond 5 with x and with three ys, a place to a place; with the mirror it is multiplying by 3; and two steps are multiplying by 9, the podaling about 5",
     all(by3[(y, -x)] == by3[(x, y)] * 7 % 10 for (x, y) in PAIRS) and all(by7[(y, -x)] == by7[(x, y)] * 3 % 10 for (x, y) in PAIRS) and all(n * 49 % 10 == podal(n) == n * 9 % 10 for n in range(1, 10)))
def square(k):
    N = k * k + 1; g = {(a, b): a + k * b for a in range(1, k + 1) for b in range(k)}
    return all(g[(k - b, a - 1)] == n * k % N for (a, b), n in g.items()) and all(n * k * k % N == N - n for n in g.values())
line(15, "in a square in a square it is the same step: 1 to 4 round 5, 1 to 9 round 10 and 1 to 16 round 17; one way it is multiplying by the side, and two are the podaling, the next number less, 17 less with the sixteen names",
     all(square(k) for k in (2, 3, 4)) and [2 ** k % 5 for k in (1, 2, 3, 4)] == [2, 4, 3, 1] and all(n * 16 % 17 == 17 - n for n in range(1, 17)))
line(16, "fifteen moments of prior two added, round ten, are one right spiral step of the diamond, all its pairs multiplied by 7, with all moments",
     all(walk[(k + 15) % 60] == tuple(v * 7 % 10 for v in walk[k]) for k in range(60)))
line(17, "a number past 5 ending at 0, 2, 4, 5, 6 or 8 has 2 or 5 a part, a prime past 5 at a corner of the diamond, 1, 3, 7 or 9, by one turn of ten; and 2, 4 and 6, 8 are one short and one past of 3, and of 7, the places of a prime's two closings",
     all((10 * t + e) % (5 if e == 5 else 2) == 0 for t in range(1, 1000) for e in (0, 2, 4, 5, 6, 8)) and all(p % 10 in (1, 3, 7, 9) for p in range(7, 100_000) if prime(p))
     and (3 - 1, 3 + 1, 7 - 1, 7 + 1) == (2, 4, 6, 8))
ONE_LINE, OTHER_LINE = ["357", "573", "735"], ["753", "537", "375"]
SIX = ONE_LINE + OTHER_LINE
carry = lambda t: [[1 if "357"[c] == t[r] else 0 for c in range(3)] for r in range(3)]
hand2 = lambda m: m[0][0] * m[1][1] - m[0][1] * m[1][0]
def hand(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
line(18, "six orders of three are three turns and three folds: a turn has the hand as it is and a fold inverts it; a pair's exchange, (x, y) to (y, x), is a fold, and with one inverting, to (y, -x), it is the right spiral step; a three's step, (x, y, z) to (y, z, x), is a turn with none inverting",
     sorted(SIX) == sorted("".join(p) for p in permutations("357")) and [hand(carry(t)) for t in SIX] == [1, 1, 1, -1, -1, -1]
     and hand2([[0, 1], [1, 0]]) == -1 and hand2([[0, 1], [-1, 0]]) == 1 and hand(carry("573")) == 1 and all(carry("573")[r][c] >= 0 for r in range(3) for c in range(3)))
X, Y, Z = (1, -1, -1), (-1, 1, -1), (-1, -1, 1)
mult = lambda a, b: tuple(p * q for p, q in zip(a, b))
alike = lambda t, group, n: all(dict(zip("357", t)).get(str(a * b % n), str(a * b % n)) == str(int(dict(zip("357", t)).get(str(a), str(a))) * int(dict(zip("357", t)).get(str(b), str(b))) % n) for a in group for b in group)
line(19, "round eight 3, 5 and 7 are alike, two of them multiplied the third, the same with all six orders, as the three bi-inversionings of three lines at right angles; round ten it is with two orders alone, 357 and 753, the 5 at its place",
     (3 * 5 % 8, 5 * 7 % 8, 7 * 3 % 8) == (7, 3, 5) and all(alike(t, (1, 3, 5, 7), 8) for t in SIX) and mult(X, Y) == Z and mult(Y, Z) == X and mult(Z, X) == Y
     and [t for t in SIX if alike(t, (1, 3, 5, 7, 9), 10)] == ["357", "753"])
order = lambda h: "".join(c for _, c in sorted(zip(h, "357"), reverse=True)) if len(set(h)) == 3 else None
line(20, "a horizon is a line, and the three are across in the order of its own three numbers along 3, 5 and 7; with two of its numbers the same, two of the three are at one place, a fold's plane; with all three the same, all three are, the corner's line",
     sorted(order(h) for h in permutations((2, 1, 0))) == sorted(SIX) and order((5, 5, 6)) is None and order((1, 1, 1)) is None)
beside = lambda a, b: sum(x != y for x, y in zip(a, b)) == 2 and (a[0] == b[0] or a[2] == b[2])
N = 1000
line(21, "across, a horizon's numbers adding to none, the six orders are a round, and from an order two are next; one quarter on, along the corner's line, it is a snap, a hair from the line all six, and from an order all five others are next",
     all(sum(beside(a, b) for b in SIX if b != a) == 2 for a in SIX) and sorted(order(tuple(N + d for d in p)) for p in permutations((2, 1, 0))) == sorted(SIX)
     and all(order(tuple(a * x + b for x in h)) == order(h) for h in permutations((1, 0, -1)) for a in (1, 9) for b in (0, 5, 10 ** 9)))
turnings = [m for p in permutations(range(3)) for ways in product((1, -1), repeat=3) for m in [[[ways[c] if p[c] == r else 0 for c in range(3)] for r in range(3)]] if hand(m) == 1]
line(22, "the turnings of three lines at right angles onto the three, the hand as it is, are 24, four with an order of the six",
     len(turnings) == 24 and all(sum("".join("357"[[abs(m[r][c]) for r in range(3)].index(1)] for c in range(3)) == t for m in turnings) == 4 for t in SIX))

# ---------------- a turn, and stepping ----------------
def far(k, n=10):
    a, b = 0, 1
    for bit in bin(k)[2:]:
        a, b = a * (2 * b - a) % n, (a * a + b * b) % n
        if bit == "1": a, b = b, (a + b) % n
    return a, b
line(23, "a turn says a thing with all numbers: a number however far is on the diamond by its ending, and prior two added with a moment however far, 10 to the 100th, has the pair the round of sixty says, found a second way by doubling the moment",
     all(((10 ** 100 + r) * (10 ** 50 + 7)) % 10 == r * 7 % 10 for r in range(1, 10)) and all(far(10 ** 100 + k) == walk[(10 ** 100 + k) % 60] for k in range(60)))
both_closings = lambda n: pow(2, n - 1, n) == 1 and far(n + 1, n)[0] == 0
stepped = [n for n in range(3, 1_000_000, 2) if n % 10 in (3, 7)]
found = [n for n in stepped if both_closings(n) != prime(n)]                    # a prime with one closing alone or none, or a number of no prime with both
line(24, "stepping says a thing to its horizon: of the odd numbers ending in 3 or 7, to 1,000,000, all stepped, the primes have both closings, doubling's one short and prior two added's one past, and no other number has; past the stepping it is not said",
     found == [] and len(stepped) == 200_000 and sum(map(both_closings, stepped)) == 39_286)
# ---------------- resolving: a me's moment, and two front to back ----------------
TWO, ONE = its.TWO, its.ONE
def a_me(prior, observed):                                             # one me, one moment, by the cell: its giving and its next prior
    gives, its_next, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed])
    return ONE[gives], ONE[its_next]
THREE = (0, 1, -1)
line(25, "a me, observing the same as its prior, is same-existing: it gives none and is as it was; observing its other-than, or none, it inverts and gives its inverting; with no prior it gives what it observes and has it",
     all(a_me(p, [o]) == ((0, p) if o == p else (-p, -p)) for p in (1, -1) for o in THREE) and all(a_me(0, [o]) == (o, o) for o in THREE))
def front_to_back(front, back, observed):
    g_front, n_front = a_me(front, [observed]); g_back, n_back = a_me(back, [g_front])
    return n_front, n_back, g_back
line(26, "two mes front to back, the front me's giving the back me's observing, their priors one the other's other-than: one of the two alone inverts with a moment, and what is same-existing at the front goes through the two",
     all((nf == f) != (nb == -f) and gb == (o if o == f else 0) for f in (1, -1) for o in THREE for nf, nb, gb in [front_to_back(f, -f, o)]))
one_giving = lambda prior, plus, minus: its.a_cell(prior, [(plus, minus)])[0][0]
line(27, "two mes in a row, with one more observed at the back me, are a nand, all the logic a me's lines have; one me with a prior a - is an other-than of what it observes",
     all(one_giving((NOT, IS), one_giving((NOT, IS), NOT, y), x) == nand(x, y) for x in (IS, NOT) for y in (IS, NOT)) and all(one_giving((NOT, IS), NOT, x) == other_than(x) for x in (IS, NOT)))
FRONT_ROWS = DIAMOND; BACK_ROWS = [[n + 8 for n in r] for r in DIAMOND]
line(28, "two diamonds of nine with one vertex of both are 1 to 17, the back's rows the front's 8 up: a podaling about 5 and then about 9; and 9 less and then 17 less on the names is that same 8 up",
     sorted(n for r in FRONT_ROWS + BACK_ROWS[1:] for n in r) == list(range(1, 18)) and all(18 - (10 - n) == n + 8 for n in range(1, 10)) and all(17 - (9 - n) == n + 8 for n in range(1, 9))
     and [sorted(18 - n for n in r) for r in FRONT_ROWS] == BACK_ROWS[::-1])
for n, name_, ok in results: print(("is       " if ok else "is not   ") + f"{n}. " + name_)
print(f"\n{sum(ok for _, _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, _, ok in results) else ": the logic is not, all or none"))
sys.exit(0 if all(ok for _, _, ok in results) else 1)
