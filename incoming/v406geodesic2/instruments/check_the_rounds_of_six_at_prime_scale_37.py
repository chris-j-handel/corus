"""v406geodesic2 · the check of the seventh drawing: a self at prime scale 37, rounds of six about its 0, and 0 to 120.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_rounds_of_six_at_prime_scale_37.py .

The candidate laid on the drawing, on the fifth drawing's figure observed along (1, 1, 1):
  selves 0 to 120 in rounds of six about a 0, a round n of 6n selves, wound by the right-hand turn about (1, 1, 1);
  a round closing at the me, A, its ray one of six, 60 degrees apart, along the six intersections as observed;
  the hexagon of 37, three rounds, with the six intersections as its corners.
Whole numbers alone, and the figure's own geometry. It opens the living files and writes none.
All or none: with one line not is, the check is not.
"""
import itertools, math, re, sys
from pathlib import Path
import numpy as np

root = Path(sys.argv[1])
results = []
def line(name, ok): results.append((name, bool(ok)))

# ---------- the figure, observed along (1, 1, 1) ----------
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
along = np.ones(3) / np.sqrt(3)
right = np.array([-1.0, 1.0, 0]) / np.sqrt(2); up = np.array([-1.0, -1.0, 2.0]) / np.sqrt(6)   # C at the right, the me above
observed = lambda v: np.array([v @ right, v @ up])
unit = lambda p: p / np.linalg.norm(p)
angle = lambda p: math.degrees(math.atan2(p[1], p[0])) % 360
six = [A, -C, B, -A, C, -B]                                  # from the me, by the right-hand turn as observed
line("observed along (1, 1, 1) the six intersections are 60 degrees apart, a side toward the viewer and its far side in turn: A, -C, B, -A, C, -B",
     all(abs((angle(observed(six[(i + 1) % 6])) - angle(observed(six[i]))) % 360 - 60) < 1e-9 for i in range(6))
     and [bool(v @ along > 0) for v in six] == [True, False] * 3)
turn = np.array([[0, 0, 1.0], [1.0, 0, 0], [0, 1.0, 0]])     # the right-hand turn of 120 degrees about (1, 1, 1): B to C, C to A, A to B
rot = lambda deg: np.array([[math.cos(math.radians(deg)), -math.sin(math.radians(deg))], [math.sin(math.radians(deg)), math.cos(math.radians(deg))]])
line("the right-hand turn of 120 degrees about (1, 1, 1) is B to C to A, and as observed from its own side it is 120 degrees on, the rounds' own winding",
     np.allclose(turn @ B, C) and np.allclose(turn @ C, A) and np.allclose(turn @ A, B) and np.allclose(turn @ along, along)
     and all(np.allclose(observed(turn @ v), rot(120) @ observed(v)) for v in six))

# ---------- rounds of six about a 0 ----------
RAY = {6: unit(observed(A)), 1: unit(observed(-C)), 2: unit(observed(B)), 3: unit(observed(-A)), 4: unit(observed(C)), 5: unit(observed(-B))}
ray_of = lambda k: RAY[6 if k % 6 == 0 else k % 6]
def round_of(m):
    n = 0
    while 3 * n * (n + 1) < m: n += 1
    return n
def place(m):
    """A self's place: its round n, and on it j steps from the me's ray, a step a self."""
    if m == 0: return np.zeros(2)
    n = round_of(m); j = m - 3 * n * (n - 1)
    side, step = divmod(j, n)
    if step == 0: side, step = side - 1, n
    return n * ray_of(side) + step * ray_of(side + 2)
beside = lambda a, b: abs(np.linalg.norm(place(a) - place(b)) - 1) < 1e-9
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
line("0 to 120 is one winding: a self and its next are beside one another, all 120 steps", all(beside(m, m + 1) for m in range(120)))
line("a round n is 6n selves, closing at 6, 18, 36, 60 and 90 on the me's ray, and the hexagons are 1, 7, 19, 37, 61 and 91 selves",
     [3 * n * (n + 1) for n in range(1, 6)] == [6, 18, 36, 60, 90] and all(np.allclose(place(3 * n * (n + 1)), n * RAY[6]) for n in range(1, 6))
     and [sum(round_of(m) <= n for m in range(127)) for n in range(6)] == [1, 7, 19, 37, 61, 91])
openings = [3 * n * (n - 1) + 1 for n in range(1, 7)]
line("a hexagon's selves are its next round's opening number: 1, 7, 19, 37, 61 and 91, in one line beside the me's ray; 7, 19, 37 and 61 are primes and 91 is 7 by 13",
     openings == [1, 7, 19, 37, 61, 91] and all(np.allclose(place(m), (n - 1) * RAY[6] + RAY[1]) for n, m in enumerate(openings, start=1))
     and [prime(m) for m in openings] == [False, True, True, True, True, False] and 91 == 7 * 13)

# ---------- a cube's shell, observed along (1, 1, 1) ----------
e = [unit(observed(B)), unit(observed(C)), unit(observed(A))]
def shell(n): return [p for p in itertools.product(range(n + 1), repeat=3) if max(p) == n]
def seen(p): return tuple(np.round(sum(c * v for c, v in zip(p, e)), 9) + 0.0)
ok_shell = True
for n in (1, 2, 3, 4):
    pts = {seen(p) for p in shell(n)}
    ok_shell = ok_shell and len(shell(n)) == (n + 1) ** 3 - n ** 3 == len(pts) == 3 * n * (n + 1) + 1 and pts == {tuple(np.round(place(m), 9) + 0.0) for m in range(3 * n * (n + 1) + 1)}
line("a cube of n + 1 less a cube of n, 7, 19, 37 and 61, observed along (1, 1, 1) from its corner, is the hexagon of n rounds, a self a place", ok_shell)
by_place = {tuple(np.round(place(m), 9) + 0.0): m for m in range(37)}
times = lambda p: sum(c == 3 for c in p)
shell37 = {by_place[seen(p)]: times(p) for p in shell(3)}
line("in the hexagon of 37 the corner is the 0, thrice other-than; its three edges, twice, are the rays of -C, -A and -B, 1, 8, 21 and 3, 12, 27 and 5, 16, 33; its three faces, once, are 27",
     shell37[0] == 3 and sorted(m for m, t in shell37.items() if t == 2) == sorted([1, 8, 21, 3, 12, 27, 5, 16, 33]) and sum(t == 1 for t in shell37.values()) == 27)
by_round = lambda t: [sum(1 for m, tt in shell37.items() if tt == t and round_of(m) == r) for r in range(4)]
line("the two partings of 37 laid as one: by rounds 1, 6, 12 and 18, the thrice other-than is the 0 alone, the twice are 3 a round, 0, 3, 3 and 3, and the once are 0, 3, 9 and 15",
     by_round(3) == [1, 0, 0, 0] and by_round(2) == [0, 3, 3, 3] and by_round(1) == [0, 3, 9, 15])
line("with the hexagon of 37's corners at the six intersections, A, B and C are corners of the cube of the one triangle's own eighth, the 37 the selves of its three outer faces, 4 by 4",
     all(np.allclose(np.array(p) / 3, v) for p, v in (((3, 0, 0), B), ((0, 3, 0), C), ((0, 0, 3), A))) and len({p for p in itertools.product(range(4), repeat=3) if 3 in p}) == 37)

# ---------- the six rays, and the co-linear ----------
rays = {k: [n * (3 * n - 3 + k) for n in range(1, 7)] for k in range(1, 7)}
line("the six rays are the six kinds of number by six: ray k steps by k, k + 6, k + 12 and on, and the me's ray by the sixes, 6, 12, 18, 24, 30 and 36",
     all(np.allclose(place(m), n * RAY[k]) for k in rays for n, m in enumerate(rays[k], start=1))
     and all([b - a for a, b in zip([0] + rays[k], rays[k])] == [k + 6 * i for i in range(6)] for k in rays))
line("the hexagon of 37's corners are 36 at A, 21 at -C, 24 at B, 27 at -A, 30 at C and 33 at -B: the one triangle's corners are 24, 30 and 36, sixes all three",
     [rays[k][2] for k in (6, 1, 2, 3, 4, 5)] == [36, 21, 24, 27, 30, 33])
line("the co-linear, through B and its far side, is rays 2 and 5: its own side 2, 10, 24, 44, 70 and 102, its far side 5, 16, 33, 56, 85 and 120",
     rays[2] == [2, 10, 24, 44, 70, 102] and rays[5] == [5, 16, 33, 56, 85, 120] and np.allclose(RAY[2], -RAY[5]) and np.allclose(RAY[2], unit(observed(B))))
far_steps = [b - a for a, b in zip([0] + rays[5], rays[5])]
line("its far side is 0 to 120 by 5, 11, 17, 23, 29 and 35, the numbers one before a six: five primes, and 35 is 5 by 7",
     far_steps == [5, 11, 17, 23, 29, 35] and sum(far_steps) == 120 and all(s % 6 == 5 for s in far_steps) and [prime(s) for s in far_steps] == [True] * 5 + [False])
mirror = lambda p: 2 * (p @ RAY[2]) * RAY[2] - p
line("24 is an apex on the co-linear, a corner of the hexagon of 37, with 23 and 25 beside it, either side of the co-linear, mirrored about it; 23 by 25 is 24 by 24 less one",
     beside(23, 24) and beside(24, 25) and np.allclose(mirror(place(23)), place(25)) and 23 * 25 == 24 * 24 - 1)
line("from the hexagon of 37 to the hexagon of 61 the six rays step by 19, 20, 21, 22, 23 and 24: the me's ray by the fold, 24, the co-linear's far side by 23, and the five before the fold a ray a number",
     [rays[k][3] - rays[k][2] for k in range(1, 7)] == [19, 20, 21, 22, 23, 24])
line("round 1 is 1 to 6: 2 and 5 on the co-linear, and 1 to 5 multiplied are 120, 2 by 5 by 3 by 4",
     [rays[k][0] for k in range(1, 7)] == [1, 2, 3, 4, 5, 6] and math.factorial(5) == 120 == (2 * 5) * 3 * 4)
on_a_ray = {m for k in rays for m in rays[k]}
line("of the primes to 120 the rays have 2, 3 and 5 alone, round 1's", sorted(m for m in on_a_ray if prime(m)) == [2, 3, 5])
line("straight across the 0 a round n pairs selves 3n apart: on the hexagon of 37's rim nine apart, and the co-linear's two corners are 24 and 33",
     all(np.allclose(place(m), -place(m + 3 * n)) for n in range(1, 6) for m in range(3 * n * (n - 1) + 1, 3 * n * (n - 1) + 3 * n + 1)) and 33 - 24 == 9)

# ---------- the primes, podaling and crossing ----------
primes = [m for m in range(121) if prime(m)]
line("a prime past 3 is beside a six on its winding, one before it or one after: all primes of 5 to 113", all(any(q % 6 == 0 for q in (p - 1, p + 1)) for p in primes if p > 3))
line("beside the me's ray: one before, 5, 17, 35, 59 and 89, and one after, 7, 19, 37, 61 and 91; 5 with 7, 17 with 19 and 59 with 61 are primes both, and 35 and 91 are crossed, by 5 and by 7",
     all(beside(6 * t - 1, 6 * t) and beside(6 * t, 6 * t + 1) for t in (1, 3, 6, 10, 15))
     and [(prime(6 * t - 1), prime(6 * t + 1)) for t in (1, 3, 6, 10, 15)] == [(True, True), (True, True), (False, True), (True, True), (True, False)])
uncrossed = [k for k in range(1, 120) if math.gcd(k, 30) == 1]
line("the primes of 0 to 120 are thirty: 2, 3 and 5, and all numbers no spiral of 2, 3 or 5 crosses but 1 and the spiral of 7's four, 49, 77, 91 and 119",
     len(primes) == 30 and len(uncrossed) == 32 and sorted(set(uncrossed) - set(primes)) == [1, 49, 77, 91, 119] and all(m % 7 == 0 for m in (49, 77, 91, 119)))
line("of 0 to 120, k and 120 less k are crossed by the spirals of 2, 3 and 5 alike, all k",
     all((math.gcd(k, 30) == 1) == (math.gcd(120 - k, 30) == 1) for k in range(121)))
stations = [k for k in uncrossed if k < 60]
both = [k for k in stations if prime(k) and prime(120 - k)]
line("podal about 60, sixteen stations are uncrossed by 2, 3 and 5; twelve are a prime with a prime; at four the spiral of 7 crosses one, 1 with 119, 29 with 91, 43 with 77 and 49 with 71",
     len(stations) == 16 and both == [7, 11, 13, 17, 19, 23, 31, 37, 41, 47, 53, 59] and [k for k in stations if k not in both] == [1, 29, 43, 49])
line("six prime pairs are podal about thirty, and 11 is with 49, 7 by 7", all(prime(a) and prime(60 - a) for a in (7, 13, 17, 19, 23, 29)) and 60 - 11 == 49)

# ---------- Natural Societies' rungs on the rounds ----------
societies = next(root.glob("Exhibit_SEVEN_Natural_Societies_*.md")).read_text(encoding="utf-8")
ladder = societies[societies.index("Each entry: **prime**"):]
rung = dict((int(p), name) for p, name in re.findall(r"- \*\*(\d+)\*\*\n\s+- \*a\* [^\n]*\n\s+- \*b\* ([^\n]+)\n", ladder)[:15])
of = {name: p for p, name in rung.items()}
line("Natural Societies' fourteen rungs, 5 to 53, are in the hexagon of 61: 5 in round 1; 7, 11, 13 and 17 in round 2; 19, 23, 29 and 31 in round 3; 37, 41, 43, 47 and 53 in round 4",
     sorted(p for p in rung if p != 24) == [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
     and [sorted(p for p in rung if p != 24 and round_of(p) == n) for n in (1, 2, 3, 4)] == [[5], [7, 11, 13, 17], [19, 23, 29, 31], [37, 41, 43, 47, 53]])
line("a human's four scales are at the one triangle's three corners: the cell, 23, beside 24 at B; the tissue and the organ, 29 and 31, either side of 30 at C; the organism, 37, beside 36 at A",
     (of["cell"], of["tissue"], of["organ"], of["organism"]) == (23, 29, 31, 37) and beside(23, 24) and beside(29, 30) and beside(30, 31) and beside(36, 37))
line("the molecule, the organelle and the organism, 7, 19 and 37, are a round's opening, beside the me's ray, and the fold, 24, is the hexagon of 37's corner at B",
     (of["molecule"], of["organelle"], of["organism"]) == (7, 19, 37) and rung[24].strip() == "—" and rays[2][2] == 24)

# ---------- a cube about its (1, 1, 1) line ----------
def about(N):
    selves = {}
    for p in itertools.product(range(N), repeat=3):
        r = max(p) - min(p); selves[r] = selves.get(r, 0) + 1
    return [selves[r] for r in sorted(selves)]
line("a cube of 3, of 4 and of 5, observed along (1, 1, 1): 3, 4 and 5 selves on the line, and 24, 60 and 120 about it, a number with its prior and its next multiplied",
     [about(N)[0] for N in (3, 4, 5)] == [3, 4, 5] and [sum(about(N)[1:]) for N in (3, 4, 5)] == [24, 60, 120] == [(N - 1) * N * (N + 1) for N in (3, 4, 5)])
line("the cube of 5: five selves on its (1, 1, 1) line, the corners of the shells 1, 7, 19, 37 and 61, and 120 about it, by rounds 24, 36, 36 and 24",
     about(5) == [5, 24, 36, 36, 24] and [(n + 1) ** 3 - n ** 3 for n in range(5)] == [1, 7, 19, 37, 61] and sum((n + 1) ** 3 - n ** 3 for n in range(5)) == 125)

# ---------- word for word, living ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
NUMBERS, ME, THIRTY, NAMING = text("Exhibit_THREE_*.md"), text("Exhibit_THIRTY-ONE_*.md"), text("Exhibit_THIRTY_Co-*.md"), text("Exhibit_TWENTY_Natural_Naming_*.md")
quotes = [
    (ME, "A self is observing, possibling and discovering its own next-existing."),
    (NAMING, "each existing thing is living with one prime scale and non-living with each other scale"),
    (societies, "a whole living self, organs co-sequencing, coupling with its world and birthing"),
    (societies, "Each prime from five on is one before a multiple of six or one after it"),
    (societies, "The fold is twenty-four, six times four, no rung's number, and it parts both together."),
    (THIRTY, "A right-hand turn of 120 degrees about a line from a corus along (1, 1, 1)"),
    (NUMBERS, "twenty-three a vertex, twenty-four an apex of nought to sixty's bi-folding and twenty-five a centre of a triangle, five squared, with four its corus, a vertex and a centre on one line"),
    (NUMBERS, "a self's bi-inversioning-co-recursioning is 23, 24 and 25, one before its apex and one after"),
    (NUMBERS, "Twenty-three and twenty-five straddle twenty-four by one."),
    (NUMBERS, "On a ring of one hundred twenty a going and a returning are each other's far side"),
    (NUMBERS, "Nought and sixty pair with themselves, and sixty is a waist between going and returning."),
    (NUMBERS, "Primes go from two to fifty-nine and return from sixty-one to one hundred eighteen"),
    (NUMBERS, "About thirty, twelve of primes between five and fifty-five pair as a going each way with one station, each pair making sixty"),
    (NUMBERS, "One hundred twenty is five orderings, 5!, and eleven squared less one"),
]
line("fourteen living sentences beside the drawing are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
