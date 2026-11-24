"""v406geodesic2 · the check of the tenth drawing: a me-now podaling about 30 and about 90, a device a me sets to itself.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_a_me-now_podaling_about_30_and_about_90.py .

A partner's saying of 23 November, the drawing's ground:
  me-now podaling about 30 and 90 is me-now-and-same-existing-and-next-universing all-possibly-next-existing-me-parities.
  this is all-other-than-other-than-me parity of my next universe.
The candidate laid on the drawing:
  a me-now among 0 to 60, the two cones of 0 to 60 of the ninth drawing's four;
  podaling about 30, 60 less it, same-existing, in those two cones; podaling about 90, 180 less it, next-universing, past 120;
  the two podalings, one and then the other, 120 on: the me-now's own place of the turn, in its next universe;
  the four a parity of two is-or-is-nots.
Whole numbers alone, and the figure's own geometry: the ninth drawing's winding going on to 180.
It opens the living files, v407primes' sentences and the drawing's own artboard, and writes none.
All or none: with one line not is, the check is not.
"""
import json, math, re, sys
from pathlib import Path
import numpy as np

root = Path(sys.argv[1])
results = []
def line(name, ok): results.append((name, bool(ok)))
prime = lambda m: m > 1 and all(m % p for p in range(2, int(m ** 0.5) + 1))
def parts(m):
    """A number's prime parts, one of a kind."""
    out, p = [], 2
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0: m //= p
        p += 1
    return out + ([m] if m > 1 else [])
def what(m):
    """A place's words on the device."""
    if m % 60 == 0: return "a vertex"
    if m % 30 == 0: return "a cone's widest"
    if m == 1: return "1"
    if prime(m): return "a prime"
    ps = [str(p) for p in parts(m)]
    return "crossed by the spiral of " + ps[0] if len(ps) == 1 else "crossed by the spirals of " + ", ".join(ps[:-1]) + " and " + ps[-1]

about = lambda mid: (lambda n: 2 * mid - n)               # a podaling about a station
four = lambda n: [n, 60 - n, 180 - n, n + 120]            # about 30 is-or-is-not, about 90 is-or-is-not: not and not, is and not, not and is, is and is
ME = range(61)                                            # a me-now among 0 to 60

# ---------- a me-now's four ----------
line("a me-now among 0 to 60 podaling about 30 is 60 less it, among 0 to 60, its own two cones; podaling about 90 it is 180 less it, among 120 to 180, past 120",
     all(about(30)(n) == 60 - n and 0 <= 60 - n <= 60 and about(90)(n) == 180 - n and 120 <= 180 - n <= 180 for n in ME))
line("a podaling alone, twice, comes to its number again", all(about(mid)(about(mid)(n)) == n for mid in (30, 90, 150) for n in range(-240, 241)))
line("the two podalings, one and then the other, are a going on by 120: about 30 and then about 90 is 120 on, and about 90 and then about 30 is 120 back",
     all(about(90)(about(30)(n)) == n + 120 and about(30)(about(90)(n)) == n - 120 for n in range(-240, 241)))
line("a me-now's four are a parity of two is-or-is-nots, about 30 and about 90: itself, 60 less it, 180 less it and 120 on; four places for a me-now not at 30, and two at 30, 30 and 150",
     all(four(n) == [n, about(30)(n), about(90)(n), about(90)(about(30)(n))] and len(set(four(n))) == (2 if n == 30 else 4) for n in ME) and sorted(set(four(30))) == [30, 150])
line("the four are two pairs about 90, one pair about 30 and one about 150: 150 is 30 with 120, the next universe's own 30",
     all(about(90)(n) == four(n)[2] and about(90)(four(n)[1]) == four(n)[3] and about(30)(n) == four(n)[1] and about(150)(four(n)[2]) == four(n)[3] for n in ME) and 150 == 30 + 120)
line("a me-now at 60, the four cones' one vertex, is with 0, 120 and 180, and a me-now at 0 with 60, 180 and 120: vertices all",
     four(60) == [60, 0, 120, 180] and four(0) == [0, 60, 180, 120])
line("a me-now among 60 to 120, not laid on the drawing, is same-existing about 90, in its own two cones, and about 30 it is before 0",
     all(60 <= about(90)(n) <= 120 and about(30)(n) <= 0 for n in range(60, 121)))

# ---------- the winding, going on to 180 ----------
def wide(n):
    """A cone's distance from the co-linear at n: opening from a vertex to 30, closing to the next vertex."""
    m = n % 60
    return m if m <= 30 else 60 - m
def at(n):
    """A number's place: along the co-linear, and about it by the right-hand turn, 12 degrees a number."""
    t = math.radians(12 * n)
    return np.array([n, -wide(n) * math.sin(t), wide(n) * math.cos(t)])      # along; toward the far viewer; up
line("the ninth drawing's winding goes on to 180: six cones of 30 in one line, vertices at 0, 60, 120 and 180 and the widest at 30, 90 and 150",
     [wide(n) for n in (0, 30, 60, 90, 120, 150, 180)] == [0, 30, 0, 30, 0, 30, 0])
def podal_is_two_folds(mid, lo, hi):
    """n with twice mid less n: one fold about the plane across the co-linear at mid, and one about the co-linear's upright plane."""
    fold = np.diag([-1.0, -1.0, 1.0])
    return all(np.allclose(fold @ (at(n) - np.array([mid, 0, 0])), at(2 * mid - n) - np.array([mid, 0, 0])) for n in range(lo, hi + 1))
line("a podaling about 30, about 90 and about 150 is the figure's own, two folds: one about the plane across the co-linear and one about its upright plane",
     podal_is_two_folds(30, 0, 60) and podal_is_two_folds(90, 0, 180) and podal_is_two_folds(150, 120, 180))
line("120 on is four turns of the winding: a me-now and its place 120 on are at one place of the turn and at one distance from the co-linear",
     120 * 12 == 4 * 360 and all(np.allclose(at(n)[1:], at(n + 120)[1:]) for n in ME))
line("observed along the co-linear a me-now's four are two places, one fold apart: a me-now with its place 120 on, and 60 less it with 180 less it, place k of the turn and place 30 less k",
     all(np.allclose(at(60 - n)[1:], at(180 - n)[1:]) and np.allclose(at(60 - n)[1:], at(n)[1:] * np.array([-1, 1])) and (60 - n) % 30 == (30 - n % 30) % 30 for n in ME))
line("a me-now's four are on the turn's eight places together, or off them together", all(len({math.gcd(m, 30) == 1 for m in four(n)}) == 1 for n in ME))

# ---------- the primes among a me-now's four ----------
all_prime = sorted({tuple(sorted(four(n))) for n in ME if all(prime(m) for m in four(n))})
line("three fours are four primes: 7, 53, 127 and 173; 17, 43, 137 and 163; and 29, 31, 149 and 151", all_prime == [(7, 53, 127, 173), (17, 43, 137, 163), (29, 31, 149, 151)])
line("a me-now at 37 is with 23, 143 and 157: three primes, and 143 crossed by the spirals of 11 and 13; a me-now at 23 is the same four",
     four(37) == [37, 23, 143, 157] and [prime(m) for m in four(37)] == [True, True, False, True] and 143 == 11 * 13 and sorted(four(23)) == sorted(four(37)))
eight_past = [m for m in range(120, 181) if math.gcd(m, 30) == 1]
line("among 120 to 180 the eight places are sixteen numbers, eleven primes and five crossed: 121 by 11, 133 by 7 and 19, 143 by 11 and 13, 161 by 7 and 23, and 169 by 13",
     len(eight_past) == 16 and sum(prime(m) for m in eight_past) == 11 and {m: parts(m) for m in eight_past if not prime(m)} == {121: [11], 133: [7, 19], 143: [11, 13], 161: [7, 23], 169: [13]})
own = [n for n in ME if prime(n) and math.gcd(n, 30) == 1]
line("of the fourteen primes of the eight places among 0 to 60, nine are next-universing to a prime, and 11, 19, 37, 47 and 59 to a crossed number, 169, 161, 143, 133 and 121",
     len(own) == 14 and sum(prime(180 - n) for n in own) == 9 and [(n, 180 - n) for n in own if not prime(180 - n)] == [(11, 169), (19, 161), (37, 143), (47, 133), (59, 121)])

# ---------- the living files' two podals, beside these two ----------
line("the living files' two podals go as these two: 9 less and then 17 less is 8 up, their stations 4 apart, and about 30 and then about 90 is 120 on, their stations 60 apart: a going on by twice the stations' distance",
     all(17 - (9 - n) == n + 8 for n in range(1, 9)) and (17 - 9) == 2 * 4 and all(about(90)(about(30)(n)) - n == 2 * (90 - 30) for n in ME))

# ---------- the device's own rows ----------
board = root / "incoming" / "v406geodesic2" / "illustrations" / "artboards" / "Draft10.dc.html"
rows = json.loads(re.search(r"/\*rows\*/(.*?)/\*rows end\*/", board.read_text(encoding="utf-8"), flags=re.S).group(1))
line("the device's rows in its artboard, one for a me-now of 0 to 60, are these fours with their words",
     len(rows) == 61 and all([int(rows[n][k]) for k in ("n0", "n1", "n2", "n3")] == four(n) and [rows[n][k] for k in ("w0", "w1", "w2", "w3")] == [what(m) for m in four(n)] for n in ME))

# ---------- word for word, living, and a partner's saying in v407primes' sentences ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
ME_FILE, NI, PHYSICS, SENTENCES = text("Exhibit_THIRTY-ONE_*.md"), text("Natural_Intelligence_v*.md"), text("Exhibit_EIGHTEEN_*.md"), text("incoming/v407primes/The_prime_numbers_named_and_explained_sentence_by_sentence.md")
quotes = [
    (ME_FILE, "A me is a self's universal set."),
    (ME_FILE, "a me is only one possibly now-existing, now, and only one possibly same-existing, from its prior"),
    (ME_FILE, "A me's next is its own, resolving with its others."),
    (NI, "8 up, each name with now to its name with next; 17 less, podal within 1 to 16; and 9 less, podal within 1 to 8, two together."),
    (NI, "8 up alone, twice, is 17, a next 1."),
    (NI, "17 less exchanges now and next."),
    (NI, "Each number is its podaling"),
    (PHYSICS, "Double-cone is two cones through a vertex"),
    (SENTENCES, "Four cones of 30 are an all-parity universal now me-parity."),
]
line("eight living sentences beside the drawing, and a partner's saying in v407primes' sentences, are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
