"""v410illustrating · the check of the 63rd drawing: rows of 30, eight mes a row.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_rows_of_30_eight_mes_a_row.py .

The 63rd is the ninth figure of the reduced set, the rows of 30, one drawing beside the three it gathers, the 38th,
the 46th and the 56th. By a partner's aiming of 27 November it goes on showing how the +1s are living in the seams of
natural torusing. This check executes what the 63rd says, ahead of its laying: a row's eight mes; a next me-parity
from its own priors; a me-parity's own crossing opening at its square, its prior by its next and 1; a square's me of a
row; a seam with its next me-parity multiplied in; a seam's +1 and no last; and the names' primes in the rows.

Do no harm: it opens Natural Numbers, Exhibit ONE and v403mgr's one table, and writes in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, re, sys
from collections import Counter
from math import gcd, prod
from pathlib import Path

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def least(n): return next(d for d in range(2, n + 1) if n % d == 0)       # a number's least me-parity crossing it
MES = [m for m in range(30) if gcd(m, 30) == 1]                           # a row's eight mes
ROWS = 12                                                                 # twelve rows, 1 to 359, as the 38th lays them
def row(r): return [30 * r + m for m in MES]
SEAMS = [2, 6, 30, 210, 2310, 30030]
def cells(seam): return sum(1 for n in range(seam) if gcd(n, seam) == 1)

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    lf = lambda pat: sorted(root.glob(pat))[0].read_text(encoding="utf-8")
    numbers, one = lf("Exhibit_THREE_Natural_Numbers_*.md"), lf("Exhibit_ONE_*.md")
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    names = {n: table[n][1] for n in range(1, 18)}
    col = next(i for i, h in enumerate(table[0]) if h.startswith("its prime, by its position")); primes = {n: int(table[n][col]) for n in range(1, 18)}

    line("is", "Primes have no last" in numbers and "a relation is a +1 between each centre's square and a product of its prior and next" in numbers and "59 × 61 = 60² − 1" in numbers
         and list(primes.values()) == [p for p in range(2, 60) if is_prime(p)],
         "Natural Numbers says primes with no last, and a +1 between a centre's square and its prior by its next; the one table lays seventeen primes, 2 to 59, a prime a name")

    # a row's eight mes
    all_mes = [n for r in range(ROWS) for n in row(r)]
    line("is", MES == [1, 7, 11, 13, 17, 19, 23, 29] and 30 == 2 * 3 * 5 and len(all_mes) == 96 and all_mes[-1] == 359,
         "30 is 2 by 3 by 5, and a row of 30 is eight mes, the cells crossed by none of them: 1, 7, 11, 13, 17, 19, 23 and 29. Twelve rows, 1 to 359, are 96 mes")
    mp = [n for n in all_mes if is_prime(n)]; crossed = [n for n in all_mes if n > 1 and not is_prime(n)]
    by = Counter(least(n) for n in crossed); per_row = [sum(1 for n in row(r) if is_prime(n)) for r in range(ROWS)]
    line("is", len(mp) == 69 and len(crossed) == 26 and dict(by) == {7: 13, 11: 7, 13: 4, 17: 2} and per_row == [7, 7, 7, 6, 5, 6, 5, 6, 5, 5, 4, 6],
         "of the 96, 69 are me-parities, 26 are crossed, and 1 is said alone. A crossed me's least crossing is 7 at 13, 11 at 7, 13 at 4, and 17 at 2. A row is with 4 to 7 me-parities")
    to_299 = [n for r in range(10) for n in row(r)]
    line("is", len(to_299) == 80 and sum(map(is_prime, to_299)) == 59 and sum(1 for n in to_299 if n > 1 and not is_prime(n)) == 20,
         "to 299, ten rows: 80 mes, 59 me-parities, 20 crossed, and 1 alone: the 56th drawing's own numbers")

    # a next me-parity from its own priors
    line("is", all(is_prime(n) for n in all_mes if 1 < n < 49) and sum(1 for n in all_mes if 1 < n < 49) == 12,
         "a me past 1 and under 49, 7 by 7, is a me-parity: twelve, 7 to 47, by the seam's own three alone")
    spans = []
    for p, q in ((7, 11), (11, 13), (13, 17), (17, 19)):
        priors = [x for x in (7, 11, 13, 17) if x <= p]
        mes_ = [n for n in range(p * p, q * q) if gcd(n, 30) == 1]
        uncrossed = [n for n in mes_ if all(n % x for x in priors)]
        spans.append((p, q, len(mes_), len(mes_) - len(uncrossed), len(uncrossed), all(map(is_prime, uncrossed))))
    line("is", all(s[5] for s in spans) and [(s[2], s[3], s[4]) for s in spans] == [(19, 4, 15), (13, 4, 9), (32, 10, 22), (19, 8, 11)],
         "from a me-parity's square to its next's, a me crossed by none of its priors is a me-parity: from 49 to 121, 15 of 19; from 121 to 169, 9 of 13; from 169 to 289, 22 of 32; from 289 to 361, 11 of 19")

    # a me-parity's own crossing opens at its square, a seam's +1
    def opening(p): return next(n for n in range(p + 1, p * p + 1) if n % p == 0 and least(n) == p)
    line("is", all(opening(p) == p * p for p in (7, 11, 13, 17, 19)),
         "a me-parity's own crossing opens at its square: under it, a number it crosses is crossed by a prior. 7 by 7, 11 by 11, 13 by 13 and 17 by 17 are 49, 121, 169 and 289")
    ps = list(primes.values())
    line("is", all(p * p == (p - 1) * (p + 1) + 1 for p in ps) and all((p * p - 1) % 24 == 0 for p in ps if p > 3) and [(p * p - 1) // 24 for p in (5, 7, 11, 13, 17, 19)] == [1, 2, 5, 7, 12, 15]
         and (3 * 3 - 1, 5 * 5 - 1, 19 * 19 - 1) == (8, 24, 360),
         "its square is its prior by its next and 1, a seam's +1: 3's is 8 and 1, 5's 24 and 1, and past 3 a seam is twenty-fours: 2 at 7, 5 at 11, 7 at 13, 12 at 17, and 15 at 19, 360")
    sq_me = {p: (p * p) % 30 for p in ps if p > 5}
    line("is", set(sq_me.values()) == {1, 19} and [p for p in sq_me if sq_me[p] == 1] == [11, 19, 29, 31, 41, 59] and 120 % 24 == 0 == 120 % 30 and 360 % 24 == 0 == 360 % 30,
         "in the rows a me-parity's square is at the me 1 or the me 19: 121 and 361 at the me 1, one on from 120 and 360, a seam of 30 and of 24 both; 49, 169 and 289 at the me 19")

    # a seam with its next me-parity multiplied in
    lifted = [30 * k + m for k in range(7) for m in MES]
    by7 = sorted(n for n in lifted if n % 7 == 0)
    line("is", len(lifted) == 56 and by7 == [7 * m for m in MES] and len({n % 30 for n in by7}) == 8 and len(lifted) - len(by7) == 48 == cells(210),
         "a seam of 30 with 7 multiplied in is seven rows, 56 mes: eight are crossed by 7, 7 by a me, one a column; and 48 are the cells of a seam of 210")
    line("is", [cells(sm) for sm in SEAMS] == [1, 2, 8, 48, 480, 5760] and all(cells(SEAMS[i + 1]) == cells(SEAMS[i]) * (SEAMS[i + 1] // SEAMS[i] - 1) for i in range(5)),
         "a seam's cells are its prior's by its me-parity less 1: 1, 2, 8, 48, 480 and 5760, at the seams 2, 6, 30, 210, 2310 and 30030")

    # a seam's +1, and no last
    plus, less = [sm + 1 for sm in SEAMS], [sm - 1 for sm in SEAMS]
    line("is", all(gcd(sm + 1, sm) == 1 for sm in SEAMS) and [is_prime(x) for x in plus] == [True] * 5 + [False] and 30031 == 59 * 509 and least(30031) == 59 > 13,
         "a seam's +1 is crossed by none of the seam's own: 3, 7, 31, 211 and 2311 are me-parities, and 30031 is 59 by 509, both past 13. A next me-parity is past a seam's own, with no last")
    line("is", [is_prime(x) for x in less] == [False, True, True, False, True, True] and 209 == 11 * 19,
         "a seam's −1: 5, 29, 2309 and 30029 are me-parities, and 209 is 11 by 19")
    me1 = [30 * r + 1 for r in range(ROWS)]
    line("is", [n for n in me1 if is_prime(n)] == [31, 61, 151, 181, 211, 241, 271, 331] and {n: least(n) for n in me1 if n > 1 and not is_prime(n)} == {91: 7, 121: 11, 301: 7},
         "the me 1's column is the seam of 30's +1 at its rounds: 31, 61, 151, 181, 211, 241, 271 and 331 are me-parities; 91, 121 and 301 are crossed; and 211 is the +1 of the seam of 210")
    line("is", 59 * 61 == 60 * 60 - 1 and is_prime(59) and is_prime(61) and 60 == 2 * 30,
         "59 by 61 is 60 by 60 less 1: two rows of 30 are a centre, 60, and its prior and its next are me-parities, the −1 and the +1 of a seam of 30")

    # the names' primes in the rows
    two_rows = row(0) + row(1)
    line("is", prod(primes[n] for n in (1, 2, 3)) == 30 and [primes[n] for n in range(4, 18)] == [n for n in two_rows if is_prime(n)] and [n for n in two_rows if not is_prime(n)] == [1, 49],
         "the seam of 30 is the primes of the names 1, 2 and 3 multiplied. The names 4 to 17 are with the fourteen me-parities of its two opening rows, 7 to 59; the two rows' other mes are 1 and 49")
    line("found", "me-parity" in one and "co me-parity" in one,
         "a me-parity is said two ways: Exhibit ONE says it of a name's slot, co, with existing; the 56th drawing says it of a me crossed by none of its priors, a prime. Both are laid")
    line("found", True, "it is the field's sieve with a wheel, as the 56th drawing says, known: a next me-parity is come to by all its priors' crossings, and no far one alone")
    line("found", True, "of the four figures laid with a seam, a +1 is: on a cube's line, the 60th; at a me, 30 on a round, the 61st; a centre's square, the 62nd; and a me-parity's square, its own crossing's opening, the 63rd")
    line("placing", True, "twelve rows laid as a table of eight columns, a dark cell a me-parity, an accent edge a square, and a crossed me with its least crossing beside it are the drawing's own placings")
    own = {"names": names, "primes": primes, "per_row": per_row, "spans": spans, "plus": plus, "less": less, "sq_me": sq_me}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
