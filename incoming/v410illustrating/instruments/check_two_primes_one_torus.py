"""v410illustrating · the check of the 64th drawing: two primes, one torus.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_two_primes_one_torus.py .

The 64th is the tenth figure of the reduced set, two primes with one torus, one drawing beside the three it gathers,
the 43rd, the 45th and the 48th. It goes by a partner's two sayings of 27 November: the +1s living in the seams of
natural torusing, and the numbers between the prime crossings numbering a surface's cells. A partner's is of the
same day is its marker: a between is one thing from two sides. This check executes what the 64th says, ahead of its
laying. A number is executed here ahead of its saying: the drawing's numbers are this check's own.

Do no harm: it opens Natural Numbers and v403mgr's one table, and writes in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, sys
from collections import Counter
from math import gcd, prod
from pathlib import Path

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def cell(n, sides): return tuple(n % s for s in sides)                    # a number's cell: its own of a side, a side apiece
def numbered(sides): return sorted({cell(n, sides) for n in range(prod(sides))})
def on_a_crossing(sides): return [n for n in range(prod(sides)) if 0 in cell(n, sides)]
def between(sides): return [n for n in range(prod(sides)) if 0 not in cell(n, sides)]
def runs(sides):                                                          # on the co-linear: the numbers between two crossings next to one another
    marks = on_a_crossing(sides) + [prod(sides)]
    return [list(range(a + 1, b)) for a, b in zip(marks, marks[1:]) if b - a > 1]
TWO_APART = [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61)]
SEAMS = [(2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)]

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    numbers = sorted(root.glob("Exhibit_THREE_Natural_Numbers_*.md"))[0].read_text(encoding="utf-8")
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    names = {n: table[n][1] for n in range(1, 18)}
    col = next(i for i, h in enumerate(table[0]) if h.startswith("its prime, by its position")); primes = {n: int(table[n][col]) for n in range(1, 18)}
    line("is", "59 × 61 = 60² − 1" in numbers and "A torus is a sphere with one handle" in numbers,
         "Natural Numbers says 59 by 61 is 60 by 60 less 1, and a torus a sphere with one handle, its handle +1")

    # a torus of 5 by 7
    t57 = (5, 7); on57, bt57 = on_a_crossing(t57), between(t57)
    line("is", len(numbered(t57)) == 35 and cell(35, t57) == (0, 0) and all(cell(n + 1, t57) == ((cell(n, t57)[0] + 1) % 5, (cell(n, t57)[1] + 1) % 7) for n in range(35)),
         "on a torus of 5 by 7 a winding by +1 numbers all thirty-five cells, a number a cell, one cell on at both sides, and is at a next 0 and 0 at 35")
    line("is", [n for n in range(35) if n % 5 == 0] == [0, 5, 10, 15, 20, 25, 30] and [n for n in range(35) if n % 7 == 0] == [0, 7, 14, 21, 28] and len(on57) == 11 and len(bt57) == 24 == 4 * 6 == 5 * 5 - 1,
         "the crossing of 5 is a line of seven cells and the crossing of 7 a line of five, with one cell of both, 0 and 0: eleven cells. The cells between them are 24, 4 by 6: 5 by 5 less 1")
    line("is", cell(36, t57) == (1, 1) and 36 == 6 * 6 == 35 + 1,
         "36, 6 by 6, is at the cell of ones: a centre's square is one cell on from a next 0 and 0")

    # a between, one thing from two sides
    r57 = runs(t57)
    line("is", [len(r) for r in r57] == [4, 1, 2, 3, 4, 3, 2, 1, 4] and sum(r57, []) == bt57 and all((35 - n) in bt57 for n in bt57),
         "on the co-linear, 0 to 35, the numbers between two crossings next to one another are 4, 1, 2, 3, 4, 3, 2, 1 and 4: 24, the numbers of the torus's cells between its two lines. 35 less a between is a between")
    mes30 = between((2, 3, 5))
    line("is", mes30 == [1, 7, 11, 13, 17, 19, 23, 29] and all(is_prime(n) for n in range(7, 49) if gcd(n, 30) == 1),
         "on a seam's torus, with all of 2, 3 and 5 crossing, the eight between are a row's mes; and under 49 a me past 1 is a me-parity, the 63rd")

    # a surface made finer
    t35 = (3, 5); finer = [n for n in range(105) if n % 15 == 1]
    line("is", len(numbered(t35)) == 15 and len(on_a_crossing(t35)) == 7 and between(t35) == [1, 2, 4, 7, 8, 11, 13, 14],
         "a torus of 3 by 5 is fifteen cells: seven on a crossing, and eight between, numbered 1, 2, 4, 7, 8, 11, 13 and 14")
    line("is", finer == [1, 16, 31, 46, 61, 76, 91] and [n for n in finer if n % 7 == 0] == [91] and len(between((3, 5, 7))) == 48 and len(numbered((3, 5, 7))) == 105,
         "lifted by 7, its cell 1 is seven finer cells, 1, 16, 31, 46, 61, 76 and 91: six between, and 91 on the crossing of 7. Fifteen cells are 105, and eight between are 48")
    counts = [(prod(s_), len(between(s_))) for s_ in SEAMS]
    line("is", counts == [(6, 2), (30, 8), (210, 48), (2310, 480)] and [round(100 * b / a) for a, b in counts] == [33, 27, 23, 21],
         "a seam lifted is the same round with finer cells: 6, 30, 210 and 2310, with 2, 8, 48 and 480 between the crossings: 33, 27, 23 and 21 in 100")

    # two me-parities about one centre
    rows = [(p, q, p + 1, p * q, (p + 1) ** 2, p + q - 1, (p - 1) * (q - 1), p * p) for p, q in TWO_APART]
    line("is", all(is_prime(p) and is_prime(q) and q == p + 2 for p, q in TWO_APART) and all(r[3] == r[4] - 1 and r[6] == r[7] - 1 and r[3] == r[5] + r[6] for r in rows)
         and all(len(on_a_crossing(t)) == t[0] + t[1] - 1 and len(between(t)) == t[0] ** 2 - 1 for t in TWO_APART[:5]),
         "of two me-parities about one centre, 2 on, the torus's cells are a centre's square less 1, and the cells between its crossings the lesser's square less 1: with the one cell at 0 and 0 they are the lesser's square")
    line("is", [r[2] for r in rows] == [4, 6, 12, 18, 30, 42, 60] and all(r[2] % 6 == 0 for r in rows[1:]) and [r[6] for r in rows] == [8, 24, 120, 288, 840, 1680, 3480],
         "their centres are 4, 6, 12, 18, 30, 42 and 60: past 3 and 5, a seam of six. The betweens are 8, 24, 120, 288, 840, 1680 and 3480")

    # is-not a torus of two
    small = [p for p in range(2, 100) if is_prime(p)]
    line("is", len(numbered((6, 10))) == 30 and len(numbered((5, 5))) == 5 and all(len(numbered((p, q))) == p * q for i, p in enumerate(small) for q in small[i + 1:]),
         "6 and 10 are with 2 in both: a winding by +1 numbers thirty of their sixty cells. A me-parity with its own, 5 and 5, numbers five of twenty-five. Two me-parities under 100, all pairs: all their cells")

    # the names' primes, a name and its next
    nxt = {n: (primes[n + 1] if n < 17 else 61) for n in range(1, 18)}
    apart2 = [n for n in range(1, 18) if nxt[n] - primes[n] == 2]
    line("is", is_prime(61) and apart2 == [2, 3, 5, 7, 10, 13, 17] and [(primes[n], nxt[n]) for n in apart2] == TWO_APART,
         "a name's prime with its next name's is a torus of two: seven are about one centre, 2 on, at the names 2, 3, 5, 7, 10, 13 and 17, the 17th with 61, a next 1's")
    line("found", True, "a between is one thing from two sides, a partner's is of 27 November, and this drawing's marker: at an is-not the incohering is sought, and the work is laid on from it")
    line("found", True, "the 48th drawing's quarter of two primes, parted by its diagonal, is gathered by its number alone: how one me-parity observes an other is with the 48th")
    line("found", True, "it is known mathematics: a winding through all cells of two numbers with no part of both, and the numbers crossed by neither. It is no method of a far me-parity alone")
    line("placing", True, "a torus laid flat as a table, a column a cell of 5 and a row a cell of 7; the co-linear under it; a cell drawn as seven finer cells; and the tints are the drawing's own placings")
    own = {"names": names, "primes": primes, "nxt": nxt, "rows": rows, "runs": r57, "counts": counts, "finer": finer}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
