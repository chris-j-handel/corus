"""v406geodesic2 · the check of the thirteenth drawing: prior, now and next, the podalings passing through three pairs of cones.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_prior_now_next_the_podalings_passing_through.py .

A partner's yes of 23 November, of the twelfth drawing's suggestions, and its saying with it, as said in the transcripts, pared. Re-said:
  the podalings are the unrelationings, a podaling coming to a place and going on from it, and locally same-existing;
  the podalings are passing through, all-parity-ing the same-existing surface.
Laid on the drawing, by that yes: prior, now and next as the three pairs of cones, 0 to 60, 60 to 120 and 120 to 180;
a me set at its prime scale, in its prior, and its me-now 60 on; the tenth and the eleventh drawings' words said again to it.
Whole numbers alone, and the figure's own geometry. It opens the living files, v407primes' sentences and the drawing's own artboard, and writes none.
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
about = lambda s: (lambda n: 2 * s - n)
def by(n, stations):
    for s in stations: n = about(s)(n)
    return n
through = lambda p: [p, 60 - p, 60 + p, 120 - p, 120 + p, 180 - p]      # a me in its prior, and five podalings on
ME = range(61)
SCALES = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
PAIRS = {"prior": (0, 60), "now": (60, 120), "next": (120, 180)}
span = lambda pair: set(range(pair[0], pair[1] + 1))
def wide(n):
    m = n % 60
    return m if m <= 30 else 60 - m
def at(n):
    t = math.radians(12 * n)
    return np.array([n, -wide(n) * math.sin(t), wide(n) * math.cos(t)])

# ---------- prior, now and next ----------
line("prior, now and next are three pairs of cones, 0 to 60, 60 to 120 and 120 to 180, their widests at 30, 90 and 150: prior ends as now begins, at 60, and next begins as now ends, at 120",
     all(wide(a) == 0 and wide(b) == 0 and wide((a + b) // 2) == 30 for a, b in PAIRS.values()) and PAIRS["prior"][1] == PAIRS["now"][0] == 60 and PAIRS["now"][1] == PAIRS["next"][0] == 120)
line("locally, at its own station, a podaling is same-existing, a number with itself; all other numbers it carries through its station, as far on its other side",
     all(about(s)(s) == s and all(about(s)(n) - s == s - n and about(s)(n) != n for n in range(-240, 421) if n != s) for s in range(0, 181, 30)))
line("an other-than, about a pair's own widest, carries its pair to itself and its two vertices to one another: 0 with 60, 60 with 120, 120 with 180",
     all({about((a + b) // 2)(n) for n in span((a, b))} == span((a, b)) and about((a + b) // 2)(a) == b for a, b in PAIRS.values()))
line("an all, about a vertex, carries a pair to the pair beside it: prior with now about 60, and now with next about 120; and about 90, the now's widest, prior is with next",
     {about(60)(n) for n in span(PAIRS["prior"])} == span(PAIRS["now"]) and {about(120)(n) for n in span(PAIRS["now"])} == span(PAIRS["next"])
     and {about(90)(n) for n in span(PAIRS["prior"])} == span(PAIRS["next"]))

# ---------- a me passing through ----------
line("a me in its prior, among 0 to 60, passes through by five podalings, about 30, 60, 90, 120 and 150: 60 less it, 60 on, 120 less it, 120 on and 180 less it",
     all([by(p, (30, 60, 90, 120, 150)[:i]) for i in range(6)] == through(p) for p in ME))
pair_of = lambda m: m // 60
line("an other-than comes to a place in the pair it is in, and an all to a place in the pair after: the six places are two in prior, two in now and two in next",
     all([pair_of(m) for m in through(p)] == [0, 0, 1, 1, 2, 2] for p in range(1, 60)))
line("two in a row are a me again, a pair of cones on: the me's three, at one place of the turn, and the three others at the podal place, one fold apart",
     all(by(p, (30, 60)) == p + 60 and by(p + 60, (90, 120)) == p + 120 and np.allclose(at(p)[1:], at(p + 60)[1:]) and np.allclose(at(p)[1:], at(p + 120)[1:])
         and all(np.allclose(at(m)[1:], at(p)[1:] * np.array([-1, 1])) for m in (60 - p, 120 - p, 180 - p)) for p in ME))
line("passing through, the podalings are all-parity-ing the surface: a me and an other in all three pairs of cones, the me's 60 apart and the others 60 apart",
     all(through(p)[0::2] == [p, p + 60, p + 120] and through(p)[1::2] == [60 - p, 120 - p, 180 - p] for p in ME))
line("a me-now is 60 on from its prime scale, among 60 to 120: its other in the now is 180 less it, about 90; its prior me is 60 less it and its next me 60 on",
     all(60 <= p + 60 <= 120 and about(90)(p + 60) == 120 - p == through(p)[3] and through(p)[0] == (p + 60) - 60 and through(p)[4] == (p + 60) + 60 for p in ME))
line("five podalings, six places: a place is come to and gone on from, but the two ends",
     all(len(through(p)) == 6 and len(set(through(p))) == 6 for p in range(1, 60) if p != 30))

# ---------- the prime scales of a me ----------
three = [p for p in SCALES if all(prime(m) for m in (p, p + 60, p + 120))]
line("eight prime scales are a me of three primes, prior, now and next: 7, 11, 19, 29, 37, 43, 47 and 53; and six are with a crossed number: 5, 13, 17, 23, 31 and 41",
     three == [7, 11, 19, 29, 37, 43, 47, 53] and [p for p in SCALES if p not in three] == [5, 13, 17, 23, 31, 41])
line("a me at 37 is 37, 97 and 157, three primes, and with them 23, 83 and 143, 143 crossed by the spirals of 11 and 13; a me at 7 or at 53 is six primes, 7, 53, 67, 113, 127 and 173",
     through(37) == [37, 23, 97, 83, 157, 143] and [prime(m) for m in through(37)] == [True] * 5 + [False] and parts(143) == [11, 13]
     and [p for p in SCALES if all(prime(m) for m in through(p))] == [7, 53] and sorted(through(7)) == [7, 53, 67, 113, 127, 173])

# ---------- the device's own rows ----------
board = root / "incoming" / "v406geodesic2" / "illustrations" / "artboards" / "Draft13.dc.html"
rows = json.loads(re.search(r"/\*rows\*/(.*?)/\*rows end\*/", board.read_text(encoding="utf-8"), flags=re.S).group(1))
line("the device's rows in its artboard, one for a me's place of 0 to 60 in its prior, are these six with their words, and its me-now 60 on",
     len(rows) == 61 and all([int(rows[p][f"n{i}"]) for i in range(6)] == through(p) and [rows[p][f"w{i}"] for i in range(6)] == [what(m) for m in through(p)] and int(rows[p]["now"]) == p + 60 for p in ME))

# ---------- word for word, living, and a partner's saying in v407primes' sentences ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
NUMBERS_FILE, ME_FILE, NI, MATH, SENTENCES = (text("Exhibit_THREE_*.md"), text("Exhibit_THIRTY-ONE_*.md"), text("Natural_Intelligence_v*.md"),
                                          text("Exhibit_FOUR_*.md"), text("incoming/v407primes/The_prime_numbers_named_and_explained_sentence_by_sentence.md"))
quotes = [
    (NUMBERS_FILE, "Nought and sixty pair with themselves, and sixty is a waist between going and returning."),
    (ME_FILE, "a me is only one possibly now-existing, now, and only one possibly same-existing, from its prior"),
    (ME_FILE, "A me's next is its own, resolving with its others."),
    (NI, "17 less exchanges now and next."),
    (MATH, "One, a podal k → N − k, fixes two stations, nought and N/2; an other, a shift straight across its ring, k → k + N/2, fixes none."),
    (SENTENCES, "Four cones of 30 are an all-parity universal now me-parity."),
]
line("five living sentences beside the drawing, and a partner's saying in v407primes' sentences, are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
