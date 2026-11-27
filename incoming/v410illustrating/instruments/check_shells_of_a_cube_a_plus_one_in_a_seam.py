"""v410illustrating · the check of the 60th drawing: shells of a cube, 1, 7, 19, 37 and 61; a +1 in a seam.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_shells_of_a_cube_a_plus_one_in_a_seam.py .

A partner's aiming of 27 November, as this session is with it: to show how the +1s are living in the seams of natural
torusing. The 60th is the second figure of the reduced set, a cube's shells, one drawing beside the five it gathers:
the 7th, the 8th, the 40th, the 41st and the 50th. This check executes what the 60th says, ahead of its laying:
rounds of six about a 0, a round closing at a seam and its next opening at a +1; a cube's shells as a seam and one
more, the one on the cube's line; a seam of six as a torus of 2 by 3; the seams of the primes multiplied and their
+1s; the seventeen names' primes beside a six; and the +1s of the opening figure.

Do no harm: it opens Natural Numbers, Exhibit THIRTY, Exhibit ONE and v403mgr's one table of the seventeen names,
and writes in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, itertools, re, sys
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
T = lambda k: k * (k + 1) // 2
SHELL = lambda n: n ** 3 - (n - 1) ** 3
SEVEN = [2, 3, 5, 7, 11, 13, 17]                              # the primes of the seams gone through, to 17

# ---- rounds of six about a 0: a cell's own on a flat laying of sixes, a round closing on the me's line
U = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]       # six ways from a cell, round one way; the me's line is the way U[0]
def cell_of(n):
    """the cell of the number n, wound round the 0: round k is 6k cells, opening beside the me's line and closing on it"""
    if n == 0: return (0, 0)
    k = 1
    while 6 * T(k) < n: k += 1
    m = n - 6 * T(k - 1)                                       # its step of its round, 1 to 6k
    i, step = divmod(m - 1, k); step += 1
    a, b = U[i], U[(i + 1) % 6]
    return (k * a[0] + step * (b[0] - a[0]), k * a[1] + step * (b[1] - a[1]))
def beside(p, q): return (q[0] - p[0], q[1] - p[1]) in U
def from_the_0(p): return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))

def side_of_a_six(p):
    if p in (2, 3): return "the seam's own"
    return f"{p + 1} less 1" if p % 6 == 5 else f"{p - 1} and 1"

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    lf = lambda pat: sorted(root.glob(pat))[0].read_text(encoding="utf-8")
    numbers, thirty = lf("Exhibit_THREE_Natural_Numbers_*.md"), lf("Exhibit_THIRTY_Co-Chaining_*.md")

    # the living files' own sayings of a +1 and of a seam
    line("is", "A torus is a sphere with one handle, and its handle is +1" in numbers and "a relation is a +1 between each centre's square and a product of its prior and next" in numbers,
         "Natural Numbers says a torus a sphere with one handle, its handle +1; and a +1 between a centre's square and its prior by its next")
    line("is", "a self of both seams" in thirty and "Seventeen primes, two to fifty-nine, and returning from sixty-one" in numbers,
         "Exhibit THIRTY says a torus of mes with its two seams, a me of both; Natural Numbers says seventeen primes, 2 to 59, and a returning from 61")

    # rounds of six about a 0
    cells = [cell_of(n) for n in range(0, 92)]
    line("is", len(set(cells)) == 92 and all(beside(cells[n], cells[n + 1]) for n in range(1, 91)) and all(from_the_0(cells[n]) == k for k in range(1, 6) for n in range(6 * T(k - 1) + 1, 6 * T(k) + 1)),
         "the numbers wound round a 0 are rounds of six: 6, 12, 18, 24 and 30 cells, a number beside its next")
    closing = [6 * T(k) for k in range(1, 6)]; opening = [6 * T(k) + 1 for k in range(0, 6)]
    line("is", closing == [6, 18, 36, 60, 90] and all(cells[c] == (0, k) for k, c in enumerate(closing, 1)),
         "a round closes on the me's line, at 6, 18, 36, 60 and 90: a seam")
    line("is", opening == [1, 7, 19, 37, 61, 91] and all(cells[o] == (1, k) for k, o in enumerate(opening)) and all(beside(cells[c], cells[c + 1]) and beside(cells[c - 1], cells[c]) for c in closing),
         "its next round opens one on, beside the me's line, at 1, 7, 19, 37, 61 and 91: a +1; and one before a seam is beside it too, its −1")
    twins = [(c - 1, c + 1) for c in closing if is_prime(c - 1) and is_prime(c + 1)]
    line("is", twins == [(5, 7), (17, 19), (59, 61)] and parts(35) == [5, 7] and parts(91) == [7, 13] and is_prime(37) and is_prime(89),
         "a seam's −1 and its +1 are two primes at 6, 18 and 60: 5 and 7, 17 and 19, 59 and 61; at 36, 35 is 5 by 7 and 37 a prime; at 90, 89 a prime and 91 is 7 by 13")

    # a cube's shells
    shells = [SHELL(n) for n in range(1, 7)]
    line("is", shells == [1, 7, 19, 37, 61, 91] and all(SHELL(n) == 6 * T(n - 1) + 1 for n in range(1, 200)) and sum(shells[:5]) == 125 == 5 ** 3 and 6 * sum(T(n - 1) for n in range(1, 6)) == 120,
         "a cube's shells are a seam and one more, 6 by 0, 1, 3, 6 and 10, and 1: 1, 7, 19, 37 and 61; five shells are a cube of 5, five ones and 120")
    def shell_cells(n): return [c for c in itertools.product(range(n), repeat=3) if max(c) == n - 1]
    on_line = [[c for c in shell_cells(n) if c[0] == c[1] == c[2]] for n in range(1, 6)]
    seen = [sorted({(c[0] - c[2], c[1] - c[2]) for c in shell_cells(n)}) for n in range(1, 6)]
    hexagon = lambda r: sorted((a, b) for a in range(-r, r + 1) for b in range(-r, r + 1) if max(abs(a), abs(b), abs(a - b)) <= r)
    line("is", all(len(x) == 1 for x in on_line) and all(len(shell_cells(n)) == SHELL(n) == len(seen[n - 1]) and seen[n - 1] == hexagon(n - 1) for n in range(1, 6)),
         "a shell's one more is its cell on the cube's line; observed along the line a shell is that cell and rounds of six about it, one cell deep")
    line("is", 37 == 1 + 6 + 12 + 18 == 4 ** 3 - 3 ** 3 == 27 + 9 + 1,
         "37 is one me and three rounds of six, 1, 6, 12 and 18; and a cube of 4 less its inner cube of 3, 27 and 9 and 1: as the 41st drawing says it")

    # a seam of six as a torus of 2 by 3
    walk = [(n % 2, n % 3) for n in range(0, 7)]
    line("is", len(set(walk[:6])) == 6 and walk[6] == walk[0] == (0, 0) and walk[1] == (1, 1) and walk[5] == (1, 2),
         "a torus of 2 by 3 is a seam of six: a winding by +1 is through all six cells, and at its opening again at 6; 1 is at the cell of ones, and 5 at the cell one before the opening")
    line("is", all((p % 2, p % 3) in ((1, 1), (1, 2)) for p in range(5, 10000) if is_prime(p)) and all((s % 2, s % 3) == (1, 1) for s in shells),
         "a prime past 3 is at the +1's cell or at the −1's, the two cells neither the spiral of 2 nor of 3 crosses, at all primes to 10,000; a cube's shells are all at the +1's cell")

    # the seams of the primes multiplied, and their +1s
    rows = []; seam = 1
    for p in SEVEN:
        seam *= p; ps = [q for q in SEVEN if q <= p]
        living = 1
        for q in ps: living *= q - 1
        rows.append((seam, p, living, seam + 1, parts(seam + 1)))
    line("is", [r[0] for r in rows] == [2, 6, 30, 210, 2310, 30030, 510510] and [r[2] for r in rows] == [1, 2, 8, 48, 480, 5760, 92160]
         and all(sum(1 for n in range(r[0]) if gcd(n, r[0]) == 1) == r[2] for r in rows[:5]),
         "the seams of the primes multiplied are 2, 6, 30, 210, 2,310, 30,030 and 510,510; their cells crossed by none of their primes are 1, 2, 8, 48, 480, 5,760 and 92,160")
    line("is", all(all((r[3] % q) == 1 for q in SEVEN if q <= r[1]) for r in rows),
         "a seam's +1 is at the cell of ones on its torus, one on along all its ways: no prime of its seam crosses it, at all seven seams")
    line("is", [len(r[4]) == 1 for r in rows] == [True] * 5 + [False] * 2 and rows[5][4] == [59, 509] and rows[6][4] == [19, 97, 277],
         "the +1 is a prime at five seams, 3, 7, 31, 211 and 2,311; 30,031 is 59 by 509, and 510,511 is 19 by 97 by 277: primes past their seam's")

    # the seventeen names' primes, beside a six, and the rounds of four
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    col = next(j for j, h in enumerate(table[0]) if h.startswith("its prime, by its position"))
    prime_of = {n: int(table[n][col]) for n in range(1, 18)}
    names = {n: table[n][0] if re.match(r"\d+-", table[n][0]) else next(x for x in table[n] if re.match(rf"{n}-[a-z-]+$", x)) for n in range(1, 18)}
    plus = [p for p in prime_of.values() if p % 6 == 1]; less = [p for p in prime_of.values() if p % 6 == 5]
    line("is", plus == [7, 13, 19, 31, 37, 43] and less == [5, 11, 17, 23, 29, 41, 47, 53, 59] and len(plus) + len(less) == 15,
         "of the seventeen primes, 2 and 3 are the seam of six's own; six are a six and 1, and nine a six less 1")
    same = [n for n in range(1, 18) if "same-existing" in names[n]]
    line("is", same == [4, 8, 12, 16] and [prime_of[n] for n in same[:3]] == shells[1:4] and prime_of[16] == 53 and shells[4] - prime_of[16] == 8,
         "the names of same-existing are the 4th, the 8th, the 12th and the 16th: three rounds of four primes close at a shell, 7, 19 and 37; the fourth is with 53, 8 short of 61")
    line("found", is_prime(61) and prime_of[17] == 59 and 61 == [p for p in range(2, 70) if is_prime(p)][17],
         "61, the fifth shell, is the 18th prime, one past the seventeen: Natural Numbers says a returning from 61")

    # the +1s of the opening figure, beside the 59th
    line("is", 16 + 1 == 17 and 59 + 1 == 60 and 35 + 1 == 36 == 6 * 6 and 5 * 7 == 35 and 36 + 1 == 37 and all(n * n == (n - 1) * (n + 1) + 1 for n in range(1, 500)),
         "16 and 1 is 17, at 1 again; 59 and 1 is sixty; 35 and 1 is 36, 5 by 7 and 6 by 6; 36 and 1 is 37: a centre's square is its prior by its next and one more, at all centres to 500")
    line("is", is_prime(23) and 25 == 5 * 5 and 24 == 4 * 6 == 5 * 5 - 1, "23 and 25 are beside 24, a prime and five fives; 24 is 4 by 6, five fives less 1")
    line("found", True, "a +1 is said five ways on the drawings: a round's opening; a shell's cell on the cube's line; the cell of ones on a seam's torus; a torus's handle; and a centre's square past its seam. One saying of the five is not laid")
    line("placing", True, "the rounds' flat laying, a shell drawn across its line, and the tints of a seam, a +1 and a −1 are the drawing's own placings")
    own = {"cells": cells, "closing": closing, "opening": opening, "shells": shells, "rows": rows, "prime_of": prime_of, "names": names, "same": same}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
