"""v406geodesic2 · the check of the sixteenth drawing: parity, universe and me, one in an other.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_parity_universe_and_me_one_in_an_other.py .

A partner's saying of 23 November is the drawing's ground, as said in the transcripts, pared. Re-said: parity, universe and me are
fractal; my universe is my all-parities; an other-than is a third parity, from a me-parity and my all-parities; my universe is a
parity in my other universes; my universes and my parities are fractals, one in an other.
The candidate laid on the drawing: spans one twice the one before it, a cone, a pair of cones, a universe and two universes; a
span's own podaling about its middle; and a number's cone, and a name less one, as places, an is-or-is-not a place.
Whole numbers alone. It opens the living files and writes none. All or none: with one line not is, the check is not.
"""
import sys
from pathlib import Path
root = Path(sys.argv[1])
results = []
def line(name, ok): results.append((name, bool(ok)))
about = lambda st: (lambda n: 2 * st - n)
SPANS = (30, 60, 120, 240)                                # a cone, a pair of cones, a universe, two universes
places = lambda c, k: [(c >> i) & 1 for i in range(k)]    # a number in k places, the low place ahead
other = lambda bits: [1 - b for b in bits]

line("the spans are one twice the one before it, a cone, a pair of cones, a universe and two universes, and a span's own podaling, about its middle, carries it to itself and its two parts to one another",
     all(b == 2 * a for a, b in zip(SPANS, SPANS[1:])) and all({about(s // 2)(n) for n in range(s + 1)} == set(range(s + 1)) and all((about(s // 2)(n) < s / 2) == (n > s / 2) for n in range(s + 1) if 2 * n != s) for s in SPANS))
line("a span's own podaling and then the own podaling of the span twice it are a going on by that span: about 15 and then 30, 30 on; about 30 and then 60, 60 on; about 60 and then 120, 120 on",
     all(about(s)(about(s // 2)(n)) == n + s for s in SPANS[:3] for n in range(-240, 241)))
cone = lambda n: n // 30                                  # a number's cone, of the eight of 0 to 240
line("a number's cone of the eight is three places: a cone opening or closing, a pair prior or now, and a universe of two; the own podaling of a pair, of a universe and of two universes is the other-than of its one, two and three low places",
     all(places(cone(about(s // 2)(n)), 3)[:k] == other(places(cone(n), 3)[:k]) and places(cone(about(s // 2)(n)), 3)[k:] == places(cone(n), 3)[k:]
         for k, s in ((1, 60), (2, 120), (3, 240)) for n in range(s) if n % 30))
line("a universe is all the places under it, and one place of the span over it: a going on by a cone, a pair and a universe is the other-than of that one place alone, in the span twice it",
     all(places(cone(n + s), 3)[k] != places(cone(n), 3)[k] and places(cone(n + s), 3)[:k] == places(cone(n), 3)[:k] for k, s in ((0, 30), (1, 60), (2, 120)) for n in range(s)))
line("on the names it is one form: 3 less, 5 less, 9 less, 17 less and 33 less, podal in 1 to 2, 4, 8, 16 and 32, are the other-than of the one, two, three, four and five low places of a name less one",
     all(places((2 ** k + 1 - n) - 1, 5)[:k] == other(places(n - 1, 5)[:k]) and places((2 ** k + 1 - n) - 1, 5)[k:] == places(n - 1, 5)[k:] for k in (1, 2, 3, 4, 5) for n in range(1, 2 ** k + 1)))
line("and a going on by 1, 2, 4, 8 and 16 names is the other-than of one place alone: 8 up of the top place of the sixteen, and 16 up the place over it, a next sixteen",
     all(places(n - 1 + 2 ** k, 5)[k] != places(n - 1, 5)[k] and places(n - 1 + 2 ** k, 5)[:k] == places(n - 1, 5)[:k] for k in range(5) for n in range(1, 2 ** k + 1)))
line("a place is two, and a number of k places is k of them, one in an other: the eight cones are three and the sixteen names four",
     len({tuple(places(c, 3)) for c in range(8)}) == 8 and len({tuple(places(n - 1, 4)) for n in range(1, 17)}) == 16)

text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
NI, ME_FILE = text("Natural_Intelligence_v*.md"), text("Exhibit_THIRTY-ONE_*.md")
line("four living sentences beside the drawing are word for word in their files",
     all(q in t for t, q in ((NI, "It is one fractal method."), (NI, "Each number pairs with its far side on each ring it is on."),
                             (ME_FILE, "A me is a self's universal set."), (ME_FILE, "each scale's selves within a me, and a me within each scale's societies"))))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
