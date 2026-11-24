"""v406geodesic2 · the check of the eleventh drawing: a me-now's four moments, other-than, all, other-than, all, and the prime scales of a me.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_a_me-now_four_moments_other-than_all_other-than_all.py .

A partner's saying of 23 November is the drawing's ground, as said in the transcripts, pared. Re-said:
  the all among two other-thans, at three places of them and by itself, a next-universing me-parity at the fourth moment of a me;
  and the method of moving the all through the prime scales of a me.
The candidate laid on the drawing:
  a podaling about a cone's widest, 30, 90, 150 or 210, is an other-than, and a podaling about a vertex, 60, 120, 180 or 240, is an all;
  a me-now among 0 to 60 goes by four moments, about 30, about 60, about 90 and about 120, one and then the next,
  a cone on with a moment, and the fourth is next-universing: 120 on;
  its four in its universe, one a cone, are its all-parity, and a me-now is set at a prime scale of a me, 5 to 53.
Whole numbers alone, and the figure's own geometry: the ninth drawing's winding going on to 240.
It opens the living files, v407primes' story and the drawing's own artboard, and writes none.
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
def by(n, stations):
    """A number carried by podalings about stations, one and then the next."""
    for mid in stations: n = about(mid)(n)
    return n
moments = lambda n: [n, 60 - n, 60 + n, 120 - n, 120 + n, 180 - n, 180 + n, 240 - n]   # a me-now, and seven moments on
ME = range(61)                                            # a me-now among 0 to 60
EIGHT = [k for k in range(30) if math.gcd(k, 30) == 1]
SCALES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

# ---------- four moments: other-than, all, other-than, all ----------
line("podalings about 30, about 60, about 90 and about 120, one and then the next, carry a me-now among 0 to 60 to 60 less it, 60 on, 120 less it and 120 on",
     all([by(n, (30, 60, 90, 120)[:i]) for i in range(5)] == [n, 60 - n, 60 + n, 120 - n, 120 + n] for n in ME))
line("the fourth moment is next-universing, 120 on, and four moments more, about 150, 180, 210 and 240, are 240 on: a universe on with four moments",
     all(by(n, (30, 60, 90, 120)) == n + 120 and by(n + 120, (150, 180, 210, 240)) == n + 240 for n in ME)
     and all([by(n, (30, 60, 90, 120, 150, 180, 210)[:i]) for i in range(8)] == moments(n) for n in ME))
cone_of = lambda m: m // 30                               # 0 to 30 a cone opening, 30 to 60 a cone closing, and on
line("a me-now and its four moments are in five cones, one in a cone: among 0 to 30 a cone on with a moment, and among 30 to 60 a cone back, three on, a cone back and three on",
     all([cone_of(m) for m in moments(n)[:5]] == [0, 1, 2, 3, 4] for n in range(1, 30)) and all([cone_of(m) for m in moments(n)[:5]] == [1, 0, 3, 2, 5] for n in range(31, 60)))
line("a me-now's four in its universe, itself, 60 less it, 60 on and 120 less it, are one a cone, an all-parity: four places for a me-now not at 0, 30 or 60",
     all(sorted(cone_of(m) for m in moments(n)[:4]) == [0, 1, 2, 3] and len(set(moments(n)[:4])) == 4 for n in ME if n not in (0, 30, 60)))
line("two podalings, one and then the next, are a going on by twice their stations' distance: a widest and the vertex after it, 60 on, and two widests or two vertices, 120 on",
     all(by(n, (30, 60)) == n + 60 and by(n, (60, 90)) == n + 60 and by(n, (30, 90)) == n + 120 and by(n, (60, 120)) == n + 120 for n in range(-240, 241)))

# ---------- the all among the two other-thans ----------
station = lambda order: {(by(n, order) + n) // 2 for n in range(-240, 241)}
line("three podalings in a row are one podaling: the all, about 60, between the two other-thans, about 30 and about 90, is the all itself, about 60, by both orders of doing",
     station((30, 60, 90)) == {60} and station((90, 60, 30)) == {60} and all(by(n, (30, 60, 90)) == about(60)(n) for n in ME))
line("the all ahead of the two other-thans or after them is a podaling about 0 or about 120, by the order of doing: the all's three places are the universe's three vertices, 0, 60 and 120",
     station((60, 30, 90)) == {120} and station((30, 90, 60)) == {0} and station((60, 90, 30)) == {0} and station((90, 30, 60)) == {120})

# ---------- the winding, going on to 240 ----------
def wide(n):
    """A cone's distance from the co-linear at n: opening from a vertex to 30, closing to the next vertex."""
    m = n % 60
    return m if m <= 30 else 60 - m
def at(n):
    """A number's place: along the co-linear, and about it by the right-hand turn, 12 degrees a number."""
    t = math.radians(12 * n)
    return np.array([n, -wide(n) * math.sin(t), wide(n) * math.cos(t)])      # along; toward the far viewer; up
line("the winding goes on to 240, eight cones of 30: at a vertex, 0, 60, 120, 180 and 240, a cone's lines are all at one place, the co-linear's own, and at a widest, 30, 90, 150 and 210, they are at their widest apart",
     [wide(n) for n in range(0, 241, 30)] == [0, 30, 0, 30, 0, 30, 0, 30, 0] and all(wide(n) < 30 for n in range(241) if n % 60 != 30) and all(wide(n) > 0 for n in range(241) if n % 60))
def podal_is_two_folds(mid, lo, hi):
    """n with twice mid less n: one fold about the plane across the co-linear at mid, and one about the co-linear's upright plane."""
    fold = np.diag([-1.0, -1.0, 1.0])
    return all(np.allclose(fold @ (at(n) - np.array([mid, 0, 0])), at(2 * mid - n) - np.array([mid, 0, 0])) for n in range(lo, hi + 1))
line("a podaling about a widest and about a vertex is the figure's own, two folds: about 30, 60, 90, 120, 150, 180 and 210, on the winding from 0 to 240",
     all(podal_is_two_folds(mid, max(0, 2 * mid - 240), min(240, 2 * mid)) for mid in range(30, 211, 30)))
line("observed along the co-linear a me-now's all-parity is two places, one fold apart: a me-now with 60 on, and 60 less it with 120 less it",
     all(np.allclose(at(n)[1:], at(60 + n)[1:]) and np.allclose(at(60 - n)[1:], at(120 - n)[1:]) and np.allclose(at(60 - n)[1:], at(n)[1:] * np.array([-1, 1])) for n in ME))

# ---------- all-parity on the turn's eight places, and the prime scales of a me ----------
fours = {k: [k, 60 - k, 60 + k, 120 - k] for k in EIGHT}
line("the all-parities of the turn's eight places, 1, 7, 11, 13, 17, 19, 23 and 29, are eight fours, and they are the 32 places of 0 to 120 no spiral of 2, 3 or 5 crosses, a place in one four alone",
     sorted(m for f in fours.values() for m in f) == [m for m in range(120) if math.gcd(m, 30) == 1])
line("four of the eight fours are four primes, of 7, 13, 19 and 23; of 1, 1 and 119 are no primes, and of 11, 17 and 29 one is crossed by the spiral of 7, 49, 77 and 91: 27 primes in all",
     {k: [m for m in f if not prime(m)] for k, f in fours.items()} == {1: [1, 119], 7: [], 11: [49], 13: [], 17: [77], 19: [], 23: [], 29: [91]}
     and sum(prime(m) for f in fours.values() for m in f) == 27 and all(m % 7 == 0 for m in (49, 77, 91, 119)))
line("the fourteen prime scales, 5 to 53, are among 0 to 60, a me-now's own two cones, and thirteen of them are in seven of the eight fours, two and two but 11, with 49",
     all(0 < p < 60 and prime(p) for p in SCALES) and len(SCALES) == 14
     and {k: [m for m in f[:2] if m in SCALES] for k, f in fours.items()} == {1: [], 7: [7, 53], 11: [11], 13: [13, 47], 17: [17, 43], 19: [19, 41], 23: [23, 37], 29: [29, 31]})
all_primes = [p for p in SCALES if all(prime(m) for m in moments(p)[:4])]
line("eight prime scales have an all-parity of four primes, 7, 13, 19, 23, 37, 41, 47 and 53, and six have a crossed number in it, 5, 11, 17, 29, 31 and 43",
     all_primes == [7, 13, 19, 23, 37, 41, 47, 53] and [p for p in SCALES if p not in all_primes] == [5, 11, 17, 29, 31, 43])
line("a me-now at 37 goes by 23, 97, 83 and 157, primes all five; in its next universe 143, 217 and 203 are crossed, by 11 and 13, 7 and 31, and 7 and 29",
     moments(37) == [37, 23, 97, 83, 157, 143, 217, 203] and all(prime(m) for m in moments(37)[:5]) and [parts(m) for m in moments(37)[5:]] == [[11, 13], [7, 31], [7, 29]])
line("a me-now at 17 or at 43 has a crossed number, 77, in its universe and four primes in its next universe, 137, 163, 197 and 223",
     all(sorted(moments(p)[4:8]) == [137, 163, 197, 223] and all(prime(m) for m in moments(p)[4:8]) and 77 in moments(p)[:4] for p in (17, 43))
     and [p for p in SCALES if all(prime(m) for m in moments(p)[4:8])] == [17, 43])

# ---------- the device's own rows ----------
board = root / "incoming" / "v406geodesic2" / "illustrations" / "artboards" / "Draft11.dc.html"
rows = json.loads(re.search(r"/\*rows\*/(.*?)/\*rows end\*/", board.read_text(encoding="utf-8"), flags=re.S).group(1))
line("the device's rows in its artboard, one for a me-now of 0 to 60, are these moments with their words",
     len(rows) == 61 and all([int(rows[n][f"n{i}"]) for i in range(8)] == moments(n) and [rows[n][f"w{i}"] for i in range(5)] == [what(m) for m in moments(n)[:5]] for n in ME))

# ---------- word for word, living, and a partner's saying in v407primes' story ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
SOCIETIES, NAMING, ME_FILE, NI, STORY = (text("Exhibit_SEVEN_*.md"), text("Exhibit_TWENTY_Natural_Naming_*.md"), text("Exhibit_THIRTY-ONE_*.md"),
                                         text("Natural_Intelligence_v*.md"), text("incoming/v407primes/The_prime_numbers_story.md"))
quotes = [
    (SOCIETIES, "Fourteen rungs go with fourteen primes, five to fifty-three, and they part eight and six."),
    (SOCIETIES, "four moments of six one-way recursionings"),
    (NAMING, "one of fourteen, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 and 53"),
    (NAMING, "each existing thing is living with one prime scale and non-living with each other scale"),
    (ME_FILE, "A me is a self's universal set."),
    (NI, "Each number is its podaling"),
    (STORY, "Four cones of 30 are an all-parity universal now me-parity."),
]
line("six living sentences beside the drawing, and a partner's saying in v407primes' story, are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
