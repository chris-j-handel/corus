"""v410illustrating · the check of the 61st drawing: cones of 30 on a co-linear; podaling a me-now about a seam of 30.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_cones_of_30_on_a_co-linear_podaling_about_a_seam_of_30.py .

The 61st is the third figure of the reduced set, cones of 30 on the co-linear, one drawing beside the nine it
gathers, the 9th to the 17th. By a partner's aiming of 27 November it goes on showing how the +1s are living in the
seams of natural torusing. This check executes what the 61st says, ahead of its laying: the seam of 30 as a torus of
2 by 3 by 5 and its eight cells crossed by none; four cones of 30 from 0 to 120; the sixteen names on a pair of
cones, with 17 a next 1; the living files' three moves as a going on by 30 and two podalings; a me-now's four
moments; and the +1 and the −1 of the seam at the names of the me and of same-existing.

Do no harm: it opens Exhibit ONE, Natural Numbers, v403mgr's one table and one drawing's words of v406geodesic2,
and writes in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, html, itertools, re, sys
from collections import Counter
from math import gcd
from pathlib import Path

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def parts(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out + ([n] if n > 1 else [])
SEAM = 30
EIGHT = [n for n in range(1, SEAM) if gcd(n, SEAM) == 1]                     # the cells of a cone's 30 no spiral of 2, 3 or 5 crosses
PLACES = [n for n in range(0, 121) if gcd(n, SEAM) == 1]                     # the cells of four cones, 0 to 120
ON_CONES = {k + 1: n for k, n in enumerate(x for x in range(1, 62) if gcd(x, SEAM) == 1)}   # a name's number on a pair of cones, 1 to 17
BI_FOLDINGS = [(1, 9, 8, 16), (2, 15, 7, 10), (3, 11, 6, 14), (4, 13, 5, 12)]
STATIONS = [0, 30, 60, 90, 120]
def about(s, x): return 2 * s - x                                            # a podaling about a station
def four_moments(x):
    """a me-now's four moments, a podaling about 30, about 60, about 90 and about 120, one and then the next"""
    out = []
    for s in (30, 60, 90, 120): x = about(s, x); out.append(x)
    return out

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    lf = lambda pat: sorted(root.glob(pat))[0].read_text(encoding="utf-8")
    one, numbers = lf("Exhibit_ONE_Natural_Resolver_*.md"), lf("Exhibit_THREE_Natural_Numbers_*.md")

    line("is", "8 up and down, keeping odd or even; 17 less, podal within 1 to 16, exchanging odd and even; and 9 less, podal within 1 to 8" in numbers
         and all(re.search(r"(?<![\d-])" + "-".join(map(str, b)) + r"(?![\d-])", one) for b in BI_FOLDINGS),
         "Natural Numbers says three moves, 8 up and down, 17 less a podal from 1 to 16, and 9 less a podal from 1 to 8; Exhibit ONE says the four bi-foldings")

    # the seam of 30, a torus of 2 by 3 by 5
    walk = [(n % 2, n % 3, n % 5) for n in range(0, 31)]
    line("is", len(set(walk[:30])) == 30 and walk[30] == walk[0] and walk[1] == (1, 1, 1) and walk[29] == (1, 2, 4),
         "30 is 2 by 3 by 5, a seam: on its torus a winding by +1 is through all thirty cells, and at a next opening at 30; 1 is at the cell of ones, and 29 at the cell one before the opening")
    line("is", EIGHT == [1, 7, 11, 13, 17, 19, 23, 29] and len(EIGHT) == 8 == 1 * 2 * 4 and all((n % 2, n % 3, n % 5).count(0) == 0 for n in EIGHT),
         "its cells crossed by none of 2, 3 and 5 are eight: 1, 7, 11, 13, 17, 19, 23 and 29, a cone's eight cells")
    six = {r: [n for n in range(30) if n % 6 == r] for r in range(6)}
    line("is", sorted(n for r in (1, 5) for n in six[r] if n % 5) == EIGHT and [n for r in (1, 5) for n in six[r] if n % 5 == 0] == [25, 5],
         "on the seam of six's own cells, the eight are at its +1 and at its −1, four and four; 25 and 5 are at them too, and the spiral of 5 crosses the two")

    # four cones of 30, 0 to 120
    by_cone = [[n for n in PLACES if 30 * k < n < 30 * (k + 1)] for k in range(4)]
    primes_by_cone = [sum(1 for n in range(30 * k + 1, 30 * k + 31) if is_prime(n)) for k in range(4)]
    line("is", [len(c) for c in by_cone] == [8, 8, 8, 8] and all([n - 30 * k for n in c] == EIGHT for k, c in enumerate(by_cone)) and primes_by_cone == [10, 7, 7, 6],
         "0 to 120 is four cones of 30, eight cells a cone, the same eight on all four; their primes are 10, 7, 7 and 6")
    not_prime = [n for n in PLACES if not is_prime(n)]
    line("is", not_prime == [1, 49, 77, 91, 119] and [parts(n) for n in not_prime[1:]] == [[7, 7], [7, 11], [7, 13], [7, 17]],
         "of the 32 cells, 27 are primes; 1 is no prime, and 49, 77, 91 and 119 are crossed by the spiral of 7")
    line("is", all(about(30, n) in PLACES for n in by_cone[0] + by_cone[1]) and all(about(60, n) in PLACES for n in PLACES) and all(about(90, n) in PLACES for n in by_cone[2] + by_cone[3]),
         "a cell's podal about 30, about 60 and about 90 is a cell: across the co-linear a cell and its podal are at one width of a cone")

    # the sixteen names on a pair of cones
    line("is", [ON_CONES[n] for n in range(1, 18)] == [1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61],
         "a pair of cones, 0 to 60, is sixteen cells: in their order the names 1 to 16, and 17 is at 61, a next 1")
    line("is", all(ON_CONES[n + 8] == ON_CONES[n] + 30 for n in range(1, 10)) and all(ON_CONES[17 - n] == about(30, ON_CONES[n]) for n in range(1, 17))
         and all(ON_CONES[9 - n] == about(15, ON_CONES[n]) for n in range(1, 9)),
         "the three moves on them: 8 up is 30 on; 17 less is a podaling about 30; and 9 less a podaling about 15")
    folds = [[ON_CONES[n] for n in b] for b in BI_FOLDINGS]
    line("is", folds == [[1, 31, 29, 59], [7, 53, 23, 37], [11, 41, 19, 49], [13, 47, 17, 43]] and all(is_prime(x) for b in (folds[1], folds[3]) for x in b) and parts(49) == [7, 7],
         "the four bi-foldings on them: 1, 31, 29 and 59; 7, 53, 23 and 37; 11, 41, 19 and 49; 13, 47, 17 and 43: two are four primes, and 49 is 7 by 7")
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    names = {n: table[n][0] if re.match(r"\d+-", table[n][0]) else next(x for x in table[n] if re.match(rf"{n}-[a-z-]+$", x)) for n in range(1, 18)}
    col = next(j for j, h in enumerate(table[0]) if h.startswith("its prime, by its position"))
    prime_of = {n: int(table[n][col]) for n in range(1, 18)}

    # the +1 and the −1 of the seam, at the names
    same = [n for n in range(1, 18) if "same-existing" in names[n]]
    line("is", [ON_CONES[n] for n in (1, 9, 17)] == [1, 31, 61] and [x % 30 for x in (1, 31, 61)] == [1, 1, 1] and is_prime(31) and is_prime(61),
         "the names at the me, 1, 9 and 17, are at 1, 31 and 61: the seam of 30's +1, at three rounds; 31 and 61 are primes")
    line("is", [ON_CONES[n] for n in (8, 16)] == [29, 59] and 8 in same and 16 in same and is_prime(29) and is_prime(59),
         "the 8th and the 16th names, two of same-existing, are at 29 and 59: its −1, one before the seams 30 and 60; both are primes")
    line("is", sorted(folds[0]) == [1, 29, 31, 59] and ON_CONES[17] == 61,
         "the bi-folding 1-9-8-16 is the four beside the seams: 29 and 31 about 30, 59 about 60 with 61, a next 1")
    plus = [30 * k + 1 for k in range(0, 8)]
    line("is", [is_prime(x) for x in plus] == [False, True, True, False, False, True, True, True] and parts(91) == [7, 13] and parts(121) == [11, 11] and plus[7] == 211 == 2 * 3 * 5 * 7 + 1,
         "the seam's +1 at its rounds on: 31 and 61 primes; 91 is 7 by 13, and 121 is 11 by 11; 151, 181 and 211 primes, and 211 is the +1 of the seam of 210")

    # a me-now's four moments
    m37 = four_moments(37)
    line("is", m37 == [23, 97, 83, 157] and all(four_moments(x) == [60 - x, x + 60, 120 - x, x + 120] for x in range(0, 61)) and all(is_prime(x) for x in m37) and parts(about(90, 37)) == [11, 13],
         "a me-now's four moments, a podaling about 30, 60, 90 and 120, one and then the next: 60 less it, 60 on, 120 less it and 120 on; a me-now at 37 is 23, 97, 83 and 157, four primes; and about 90 alone, 143, 11 by 13")
    fours = [(x, 60 - x, x + 120, 180 - x) for x in ON_CONES.values() if x < 30 and all(is_prime(y) for y in (x, 60 - x, x + 120, 180 - x))]
    line("is", fours == [(7, 53, 127, 173), (17, 43, 137, 163), (29, 31, 149, 151)],
         "podaling about 30 and about 90, three fours are four primes: 7, 53, 127 and 173; 17, 43, 137 and 163; 29, 31, 149 and 151: the last is two pairs about a seam")

    # a name with two numbers
    shift = [n for n in range(1, 16) if ON_CONES[n] == prime_of[n + 2]]
    line("found", shift == list(range(2, 14)) and ON_CONES[14] == 49 and prime_of[16] == 53 == ON_CONES[15] and prime_of[17] == 59 == ON_CONES[16],
         "a name is with two numbers, its number on a pair of cones and its prime by its position: from the 2nd name to the 13th its number on the cones is the prime of the name two on; the 14th is at 49, 7 by 7, and the 15th and 16th are at the primes of the name one on")
    line("found", ON_CONES[9] == 31 and prime_of[9] == 23 and ON_CONES[12] == 43 and prime_of[12] == 37,
         "the 9th name is at 31 on the cones and with 23 by position; the 12th at 43 and with 37. One saying of a name's number is not laid")

    # the nine drawings' own two sayings of a podaling
    def words_of(n):
        t = (root / f"incoming/v406geodesic2/illustrations/artboards/Draft{n}.dc.html").read_text(encoding="utf-8")
        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S); return html.unescape(re.sub(r"<[^>]+>", "\n", t))
    line("found", "A podaling is two folds, an other-than of an other-than" in words_of(10) and "A podaling about a cone's widest is an other-than, and a podaling about a vertex is an all" in words_of(11),
         "a podaling is said two ways in the nine: two folds, an other-than of an other-than, at the 10th; and an other-than about a cone's widest and an all about a vertex, at the 11th. Both are laid")
    line("placing", True, "a cone drawn as a width over the co-linear, a cell at its width; the tints of a seam, a +1 and a −1; and a name's chip over its cell are the drawing's own placings")
    own = {"names": names, "prime_of": prime_of, "by_cone": by_cone, "folds": folds, "m37": m37, "same": same}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
