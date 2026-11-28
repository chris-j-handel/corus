"""v410illustrating · a partner's saying of 27 November, executed: the numbers between the prime crossings,
numbering the cells of a pixelating surface.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_numbers_between_the_prime_crossings_numbering_a_torus_s_cells.py .

A partner said it of v410opusbio's discovering. No page of v410opusbio is in the set at this execution, and this
instrument goes by a partner's saying alone, concept for concept, with a partner's saying of 23 November to v407primes
beside it: larger numbers as finer localities on the surface, more cells in the same span between prime crossings.
It executes a between two ways, on the co-linear and on a torus, and a surface made finer by a seam lifted.

Do no harm: it opens Natural Numbers and v407primes' transcript pared, and writes in no file.
A line is an is, executed here; or found, a thing found and laid whole.
"""
import sys
from collections import Counter
from math import gcd, prod
from pathlib import Path

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def cell(n, primes): return tuple(n % p for p in primes)                  # a number's cell of a torus: its own of a prime, a prime apiece
def torus(primes):
    seam = prod(primes); cells = [cell(n, primes) for n in range(seam)]
    on = [n for n in range(seam) if 0 in cell(n, primes)]                 # on a crossing: at the 0 of a prime's own round
    return seam, cells, on, [n for n in range(seam) if n not in set(on)]

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    numbers = sorted(root.glob("Exhibit_THREE_Natural_Numbers_*.md"))[0].read_text(encoding="utf-8")
    pared = (root / "incoming/v407primes/The_transcript_of_v407primes_pared.md").read_text(encoding="utf-8")
    line("is", "more pixels in the same space between prime crossings" in pared and "59 × 61 = 60² − 1" in numbers,
         "a partner's saying of 23 November is in v407primes' transcript pared: larger numbers, more cells in the same span between prime crossings. Natural Numbers says 59 by 61 is 60 by 60 less 1")

    # a number a cell: a winding by +1 numbers all cells of a torus, once
    seam, cells, on, between = torus((3, 5))
    line("is", seam == 15 and len(set(cells)) == 15 and cell(15, (3, 5)) == (0, 0),
         "on a torus of 3 by 5 a winding by +1 numbers all fifteen cells, a number a cell, and is at a next 0 and 0 at 15")
    line("is", on == [0, 3, 5, 6, 9, 10, 12] and between == [1, 2, 4, 7, 8, 11, 13, 14],
         "its two crossings are the cells at a 0: 0, 3, 6, 9 and 12, and 0, 5 and 10, seven cells. The eight between them are numbered 1, 2, 4, 7, 8, 11, 13 and 14")

    # between, two ways
    ps = [p for p in range(2, 360) if is_prime(p)]
    gaps = [(a, b, b - a - 1) for a, b in zip(ps, ps[1:])]
    line("is", sum(g[2] for g in gaps) == 286 and max(gaps, key=lambda g: g[2]) == (113, 127, 13) and Counter(g[2] for g in gaps)[1] == 21,
         "on the co-linear, to 359, the numbers between two me-parities are 286, in 71 betweens: all are crossed. The widest is thirteen numbers, 114 to 126; twenty-one betweens are one number")
    ok = True
    for primes_, lo, hi in (((2, 3, 5), 7, 48), ((2, 3, 5, 7), 11, 120), ((2, 3, 5, 7, 11), 13, 168)):
        ok &= all((gcd(n, prod(primes_)) == 1) == is_prime(n) for n in range(lo, hi + 1))
    line("is", ok,
         "on a torus it is the other way: a me-parity is between the crossings, and a crossed number on a crossing. To 48 on the torus of 30, to 120 on 210, and to 168 on 2310, a cell between the crossings is a me-parity")
    line("found", True, "a between is said two ways, and they are one thing from two sides: on the co-linear a crossed number is between two me-parities; on a seam's torus a me-parity is between the crossings")

    # a surface made finer: a seam lifted
    seams = [(2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)]
    counts = [(prod(s_), sum(1 for n in range(prod(s_)) if gcd(n, prod(s_)) == 1)) for s_ in seams]
    line("is", counts == [(6, 2), (30, 8), (210, 48), (2310, 480)] and [round(100 * b / a) for a, b in counts] == [33, 27, 23, 21],
         "a seam lifted is the same round with finer cells: 6, 30, 210 and 2310 cells, and 2, 8, 48 and 480 between the crossings: 33, 27, 23 and 21 in 100, finer and not none")
    lifted = {m: [30 * k + m for k in range(7)] for m in (1, 7, 11, 13, 17, 19, 23, 29)}
    line("is", all(sum(1 for n in v if n % 7 == 0) == 1 for v in lifted.values()),
         "a cell between the crossings of 30 is seven cells of 210, a cell a round of 30: six between the crossings, and one on the crossing of 7")

    # a bi-coupling of two me-parities 2 apart: a seam, and its +1
    twos = [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61)]
    line("is", all(p * q == (p + 1) ** 2 - 1 for p, q in twos) and [p * q for p, q in twos[:4]] == [15, 35, 143, 323],
         "a torus of two me-parities 2 apart is a centre's square less 1 in cells: 3 by 5 is 15, 4 by 4 less 1; 5 by 7 is 35; 11 by 13 is 143; and 59 by 61 is 60 by 60 less 1. Its +1 is one cell on from a next 0 and 0")
    line("is", all((p - 1) * (q - 1) == p * p - 1 for p, q in twos) and [(p - 1) * (q - 1) for p, q in twos[:4]] == [8, 24, 120, 288] and all(len(torus(t)[3]) == t[0] ** 2 - 1 for t in twos[:4]),
         "the cells between its two crossings are the lesser's prior by its next, a seam: 8, 24, 120 and 288. With the one cell at 0 and 0, both crossings' own, they are the lesser's square: 9, 25, 121 and 289")
    line("found", True, "of a +1 in a seam of natural torusing, one more saying: on a torus of two me-parities 2 apart the betweens are a seam, and its +1 is the opening, the one cell of both crossings")
    line("found", True, "not executed, and with v410opusbio: a co-sequencing's betweens, a surface's cells as a living thing's, and an all-parity universe. This instrument executes numbers alone")
    return lines, {}

if __name__ == "__main__":
    lines, _ = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
