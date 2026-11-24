"""v406geodesic2 · the check of the ninth drawing: four cones of 30 in one line, 0 to 120, and the staircase on its geodesic.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_four_cones_of_30.py .

The candidate laid on the drawing, by a partner's yes of its one sentence:
  four cones of 30 in one line, the co-linear, their ends at 0, 30, 60, 90 and 120, facing two and two:
  two crossing at 30 and two at 90, as the fifth drawing's two cones cross, and the two pairs through one vertex at 60;
  0 to 120 one right-hand winding about the co-linear, a turn a cone, a number 12 degrees on from the one before it.
The staircase and its geodesic are v407primes' story's sentence 84, executed here apart.
Whole numbers alone, and the figure's own geometry. It opens the living files and writes none.
All or none: with one line not is, the check is not.
"""
import math, sys
from pathlib import Path
import numpy as np

root = Path(sys.argv[1])
results = []
def line(name, ok): results.append((name, bool(ok)))
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))

# ---------- a cone's turn of 30, and its eight places ----------
eight = [k for k in range(30) if math.gcd(k, 30) == 1]
line("a turn of 30 has eight places no spiral of 2, 3 or 5 crosses, 1, 7, 11, 13, 17, 19, 23 and 29, the same on all four cones",
     eight == [1, 7, 11, 13, 17, 19, 23, 29] and all(sorted(n % 30 for n in range(30 * c, 30 * c + 30) if math.gcd(n, 30) == 1) == eight for c in range(4)))
line("the eight are podal about the turn's own line, k with 30 less k: 1 with 29, 7 with 23, 11 with 19 and 13 with 17", all(30 - k in eight for k in eight) and [(k, 30 - k) for k in eight[:4]] == [(1, 29), (7, 23), (11, 19), (13, 17)])
by_cone = [[n for n in range(30 * c, 30 * c + 30) if prime(n)] for c in range(4)]
line("the primes of the four cones are 10, 7, 7 and 6, 30 in all: the eight places' with 2, 3 and 5, less 1 and the spiral of 7's four, 49, 77, 91 and 119",
     [len(x) for x in by_cone] == [10, 7, 7, 6] and sorted(n for n in range(120) if math.gcd(n, 30) == 1 and not prime(n)) == [1, 49, 77, 91, 119])

# ---------- the four cones, one winding ----------
def wide(n):
    """A cone's distance from the co-linear at n: opening from a vertex to 30, closing to the next vertex."""
    m = n % 60
    return m if m <= 30 else 60 - m
def at(n):
    """A number's place: along the co-linear, and about it by the right-hand turn toward the co-linear's own side, the me's way up."""
    t = math.radians(12 * n)
    return np.array([n, -wide(n) * math.sin(t), wide(n) * math.cos(t)])      # along; toward the far viewer; up
line("four cones in one line: vertices at 0, 60 and 120, the widest at 30 and at 90, and a number is 12 degrees on from the one before it, a turn a cone",
     [wide(n) for n in (0, 30, 60, 90, 120)] == [0, 30, 0, 30, 0] and all(abs(np.linalg.norm(at(n)[1:]) - wide(n)) < 1e-9 for n in range(121)))
turn = lambda deg: np.array([[1, 0, 0], [0, math.cos(math.radians(deg)), -math.sin(math.radians(deg))], [0, math.sin(math.radians(deg)), math.cos(math.radians(deg))]])
line("the winding is by the right-hand turn about the co-linear toward its own side: a step is 12 degrees of it, with the cone's opening or closing",
     all(np.allclose(turn(12) @ (at(n) / max(wide(n), 1e-12))[[0, 1, 2]] * np.array([0, 1, 1]), (at(n + 1) / max(wide(n + 1), 1e-12)) * np.array([0, 1, 1])) for n in range(1, 59) if wide(n) and wide(n + 1)))
def podal_is_two_folds(mid, lo, hi):
    """n with twice mid less n: one fold about the plane across the co-linear at mid, and one about the co-linear's upright plane."""
    fold = np.diag([-1.0, -1.0, 1.0])
    return all(np.allclose(fold @ (at(n) - np.array([mid, 0, 0])), at(2 * mid - n) - np.array([mid, 0, 0])) for n in range(lo, hi + 1))
line("podal about 30, about 60 and about 90 are the figure's own: n with 60, 120 and 180 less n is two folds, about the plane across the co-linear and about its upright plane, a side toward the viewer with its far side",
     podal_is_two_folds(30, 0, 60) and podal_is_two_folds(60, 0, 120) and podal_is_two_folds(90, 60, 120))
line("observed across the co-linear a place and its podal place are on one line of a cone, one toward the viewer and one behind: the eight are four lines, of 1 and 29, of 7 and 23, of 11 and 19, and of 13 and 17",
     all(abs(math.cos(math.radians(12 * k)) - math.cos(math.radians(12 * (30 - k)))) < 1e-12 and math.sin(math.radians(12 * k)) > 0 > math.sin(math.radians(12 * (30 - k))) for k in eight[:4])
     and len({round(math.cos(math.radians(12 * k)), 9) for k in eight}) == 4)
line("observed along the co-linear the two cones of 0 to 60 and the two of 60 to 120 are one figure, n and n with 60 at one place: the 32 places of 120 are sixteen, on eight rays, two distances a ray, k and 30 less k",
     all(np.allclose(at(n)[1:], at(n + 60)[1:]) for n in range(61))
     and len({tuple(np.round(at(n)[1:], 9)) for n in range(120) if math.gcd(n, 30) == 1}) == 16
     and all(sorted({wide(n) for n in range(120) if n % 30 == k}) == sorted({k, 30 - k}) for k in eight))

# ---------- the primes' podaling on the cones ----------
pairs = lambda mid, lo: [(k, 2 * mid - k) for k in range(lo, mid) if prime(k) and prime(2 * mid - k)]
line("about 30 six prime pairs are podal, and 11 is with 49, 7 by 7", pairs(30, 0) == [(7, 53), (13, 47), (17, 43), (19, 41), (23, 37), (29, 31)] and 60 - 11 == 49)
line("about 90 five prime pairs are podal, 67 with 113, 71 with 109, 73 with 107, 79 with 101 and 83 with 97; and 61, 89 and 103 are with 119, 91 and 77, the spiral of 7's",
     pairs(90, 60) == [(67, 113), (71, 109), (73, 107), (79, 101), (83, 97)] and [180 - k for k in (61, 89, 103)] == [119, 91, 77] and all(m % 7 == 0 for m in (119, 91, 77)))
line("about 60, the vertex of the two pairs, twelve prime pairs are podal", len(pairs(60, 0)) == 12)
alone = lambda mid, lo, hi: sorted({2 * mid - p for p in range(lo, hi + 1) if prime(p) and math.gcd(p, 30) == 1 and not prime(2 * mid - p)})
line("a prime of the eight places with no prime across it, about 30, about 60 or about 90, is across from 1 or from the spiral of 7's crossing, 49, 77, 91 or 119",
     alone(30, 0, 60) == [1, 49] and alone(60, 0, 120) == [49, 77, 91] and alone(90, 60, 120) == [77, 91, 119])

# ---------- the staircase on its geodesic, four faces of 30 along and one across ----------
stair = [0]
for n in range(1, 100001): stair.append(stair[-1] + prime(n))
line("at the faces' corners, 30, 60, 90 and 120, the staircase is 10, 17, 24 and 30, and the geodesic, a rise of one face for the four along, a quarter of the four",
     [stair[n] for n in (30, 60, 90, 120)] == [10, 17, 24, 30] and 120 == 4 * 30)
on_it = [n for n in range(1, 121) if 4 * stair[n] == n]
above = [n for n in range(1, 121) if 4 * stair[n] > n]
line("from 2 to 120 the staircase is above its geodesic or on it, and on it at 96, 100 and 120 alone: with 24, 25 and 30 primes", on_it == [96, 100, 120] and above == [n for n in range(2, 121) if n not in on_it] and [stair[n] for n in on_it] == [24, 25, 30])
line("past 120 the staircase is under its geodesic, all numbers to 100,000: 120 is the last", all(4 * stair[n] < n for n in range(121, 100001)))
line("the eighth drawing's four rounds and the four cones are two partings of 0 to 120 in four, both podal about 60: their ends are 0, 24, 60, 96, 120 and 0, 30, 60, 90, 120, and at 96 the staircase is on its geodesic at 24",
     [120 - e for e in (0, 24, 60, 96, 120)] == [120, 96, 60, 24, 0] and [120 - e for e in (0, 30, 60, 90, 120)] == [120, 90, 60, 30, 0] and stair[96] == 24)

# ---------- word for word, living ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
PHYSICS, NUMBERS, NI = text("Exhibit_EIGHTEEN_*.md"), text("Exhibit_THREE_*.md"), text("Natural_Intelligence_v*.md")
quotes = [
    (PHYSICS, "Double-cone is two cones through a vertex"),
    (PHYSICS, "two facing through an unoccupied 24, a 0, not changing, two cones inversions of each other"),
    (PHYSICS, "a light-cone is an apex double-cone, its vertex a now, a 0, not changing"),
    (PHYSICS, "its four quarter-turns a cone closes through"),
    (NUMBERS, "About thirty, twelve of primes between five and fifty-five pair as a going each way with one station, each pair making sixty"),
    (NUMBERS, "Eleven pairs with forty-nine about thirty"),
    (NUMBERS, "Nought and sixty pair with themselves, and sixty is a waist between going and returning."),
    (NUMBERS, "a self's bi-inversioning-co-recursioning is 23, 24 and 25, one before its apex and one after"),
    (NI, "two odd numbers coprime, p and q, come again together first with moment 4pq"),
]
line("nine living sentences beside the drawing are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
