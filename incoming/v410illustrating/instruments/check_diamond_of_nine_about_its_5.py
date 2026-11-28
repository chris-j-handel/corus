"""v410illustrating · the check of the 62nd drawing: a diamond of nine about its 5.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_diamond_of_nine_about_its_5.py .

The 62nd is the fourth figure of the reduced set, the diamond of nine, one drawing beside the seven it gathers, the
18th to the 24th. By a partner's aiming of 27 November it goes on showing how the +1s are living in the seams of
natural torusing. This check executes what the 62nd says, ahead of its laying: the three by three of 1 to 9 on its
corner; a podaling about its 5; multiplying round ten by 3 as a right spiral step; a seam of ten as a torus of 2 by 5;
nine as eight and one more; its middle row's three centres, a centre's square a seam's +1; a square's rounds beside a
cube's shells; diamonds on the co-linear, a vertex 8 on a diamond; and Exhibit ONE's names by their cells.

Do no harm: it opens Natural Numbers, Natural Illustrating, Natural Naming and v403mgr's one table, and writes in no
file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, re, sys
from collections import Counter
from math import gcd
from pathlib import Path

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def cell(n): return ((n - 1) // 3, (n - 1) % 3)                     # a number's own of the three by three, its row and its column
def number(rc): return 3 * rc[0] + rc[1] + 1
def quarter(rc): return (rc[1], 2 - rc[0])                           # a right spiral step of the three by three about its middle
def across(rc): return (2 - rc[0], 2 - rc[1])                        # two steps: across its middle
DIAMOND = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]                      # a partner's order after its 0, as the 19th drawing lays it
def round_ten(k, n): return (k * n) % 10
def at_a_seam_of_8(n): return "its +1" if n % 8 == 1 else "the seam" if n % 8 == 0 else "its −1" if n % 8 == 7 else ""

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    lf = lambda pat: sorted(root.glob(pat))[0].read_text(encoding="utf-8")
    numbers, illus, naming = lf("Exhibit_THREE_Natural_Numbers_*.md"), lf("Exhibit_TWENTY-NINE_Natural_Illustrating_*.md"), lf("Exhibit_TWENTY_Natural_Naming_*.md")

    line("is", "eight its first seam" in numbers and "within 1 to 8 it is 9 less n" in numbers and "a right spiral step's quarter turn" in naming,
         "Natural Numbers says eight the opening seam, and a podal from 1 to 8 as 9 less; Natural Naming says a right spiral step a quarter round")

    # the diamond of nine
    rows = [sorted((n for n in range(1, 10) if sum(cell(n)) == k), key=lambda n: cell(n)[0]) for k in range(5)]
    line("is", rows == DIAMOND and all(len({n % 2 for n in r}) == 1 for r in rows) and [len(r) for r in rows] == [1, 2, 3, 2, 1],
         "the three by three of 1 to 9 on its corner is a diamond: 1; 2 and 4; 3, 5 and 7; 6 and 8; and 9: a row odd or even all through")
    line("is", all(number(across(cell(n))) == 10 - n for n in range(1, 10)) and across(cell(5)) == cell(5),
         "a podaling about its 5 is 10 less a number: 1 with 9, 2 with 8, 3 with 7, 4 with 6, and 5 as it was: the three by three across its middle")

    # multiplying round ten
    line("is", all(number(quarter(cell(n))) == round_ten(3, n) for n in range(1, 10)),
         "multiplying by 3 round ten is a right spiral step of the three by three about its 5: 1 onto 3, 3 onto 9, 9 onto 7, 7 onto 1; 2 onto 6, 6 onto 8, 8 onto 4, 4 onto 2; 5 onto 5")
    line("is", all(round_ten(9, n) == 10 - n == round_ten(3, round_ten(3, n)) for n in range(1, 10)) and all(round_ten(3, round_ten(7, n)) == n for n in range(1, 10))
         and [pow(3, k, 10) for k in range(5)] == [1, 3, 9, 7, 1],
         "by 9 is two steps, the podaling about 5; by 7 is three, a step the other way; by 1 all are as they were: four moves, 1, 3, 9 and 7")
    as_it_was = [n for n in range(1, 10) if round_ten(3, n) == n]
    def round_of(n):
        r = [n]
        while round_ten(3, r[-1]) != n: r.append(round_ten(3, r[-1]))
        return r
    line("is", as_it_was == [5] and round_of(1) == [1, 3, 9, 7] and round_of(2) == [2, 6, 8, 4],
         "a right spiral step leaves one cell as it was, its 5, and carries eight round it: two rounds of four, 1, 3, 9 and 7, and 2, 6, 8 and 4")
    corners = sorted(n for n in range(1, 10) if cell(n)[0] != 1 and cell(n)[1] != 1); sides = sorted(n for n in range(1, 10) if (cell(n)[0] == 1) != (cell(n)[1] == 1))
    line("is", corners == [1, 3, 7, 9] == [n for n in range(1, 10) if gcd(n, 10) == 1] and sides == [2, 4, 6, 8] and number((1, 1)) == 5,
         "its four corners are 1, 3, 7 and 9, crossed by none of 2 and 5; its four sides' middles 2, 4, 6 and 8, crossed by 2; and its middle 5, by 5: the four moves are the four corners' numbers")

    # the seam of ten, a torus of 2 by 5
    walk = [(n % 2, n % 5) for n in range(11)]
    line("is", len(set(walk[:10])) == 10 and walk[10] == walk[0] and walk[1] == (1, 1) and walk[9] == (1, 4),
         "ten is 2 by 5, a seam: on its torus a winding by +1 is through all ten cells, and at its opening again at 10; 1 is at the cell of ones, and 9 at the cell one before the opening")
    ends = Counter(p % 10 for p in range(7, 10000) if is_prime(p))
    line("is", sorted(ends) == [1, 3, 7, 9] and not is_prime(21) and not is_prime(27) and not is_prime(33) and not is_prime(39),
         "a prime past 5 ends at 1, 3, 7 or 9, the four cells crossed by none, at all primes to 10,000; 21, 27, 33 and 39 end at them too, and are no primes")

    # nine is eight and one more
    seams = [(2 * k + 1) ** 2 - 1 for k in range(1, 6)]
    line("is", 9 == 3 * 3 == 2 * 4 + 1 and seams == [8, 24, 48, 80, 120] and all(sm == 8 * (k * (k + 1) // 2) for k, sm in enumerate(seams, 1)),
         "nine is eight and one more: three by three is 2 by 4 and 1, a centre's square past its prior by its next; eight is the opening seam of 8, 24, 48, 80 and 120")
    centres = DIAMOND[2]
    line("is", centres == [3, 5, 7] and [(m - 1) * (m + 1) for m in centres] == seams[:3] == [8, 24, 48] and [m * m for m in centres] == [sm + 1 for sm in seams[:3]] == [9, 25, 49]
         and DIAMOND[1] == [2, 4] and DIAMOND[3] == [6, 8] and 4 + 6 == 10,
         "its middle row is 3, 5 and 7, three centres: a centre's prior by its next is a seam, 2 by 4, 4 by 6 and 6 by 8, at 8, 24 and 48; a centre's square is the seam's +1, 9, 25 and 49. Its rows 2, 4 and 6, 8 are the priors and the nexts")
    rounds = [sum(1 for x in range(-k, k + 1) for y in range(-k, k + 1) if max(abs(x), abs(y)) == k) for k in range(4)]
    line("is", rounds == [1, 8, 16, 24] and [sum(rounds[:k + 1]) for k in range(4)] == [1, 9, 25, 49] and [1 + 6 * (k * (k + 1) // 2) for k in range(5)] == [1, 7, 19, 37, 61],
         "a square's rounds about its middle are 8, 16 and 24, an eight more a round: one and its rounds are 1, 9, 25 and 49, as a cube's shells are 1, 7, 19, 37 and 61, a six more a round, the 60th")
    line("is", [(a * b) % 8 for a, b in ((3, 5), (5, 7), (7, 3))] == [7, 3, 5] and all((m * m) % 8 == 1 for m in centres) and [(a * b) % 10 for a, b in ((3, 3), (7, 7), (3, 7))] == [9, 9, 1],
         "round eight 3, 5 and 7 are alike: two of them multiplied are the third, and one by its own is 1, the seam's +1. Round ten 3 by 3 and 7 by 7 are at 9, its −1, and 3 by 7 at 1, its +1")
    line("is", all((9 - n) in range(1, 9) for n in range(1, 9)) and not any(9 - n == n for n in range(1, 9)) and [n for n in range(1, 10) if 10 - n == n] == [5],
         "two podalings: 9 less, from 1 to 8, leaves no number as it was; 10 less, from 1 to 9, leaves its 5")

    # two diamonds, one vertex of both, and the names at a seam of eight
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    names = {n: table[n][0] if re.match(r"\d+-", table[n][0]) else next(x for x in table[n] if re.match(rf"{n}-[a-z-]+$", x)) for n in range(1, 18)}
    first, second = list(range(1, 10)), list(range(9, 18))
    line("is", [n + 8 for n in first] == second and len(set(first) | set(second)) == 17 == 2 * 8 + 1 and set(first) & set(second) == {9},
         "two diamonds of nine with one vertex of both are 1 to 17: two eights and 1; 8 up lays a diamond onto its next, 1 onto 9 and 9 onto 17")
    vertices = [1 + 8 * j for j in range(7)]
    line("is", [vertices[j] for j in (1, 3, 6)] == [9, 25, 49] and [k * (k + 1) // 2 for k in (1, 2, 3)] == [1, 3, 6] and [v % 10 for v in vertices] == [1, 9, 7, 5, 3, 1, 9]
         and vertices[5] == 41 == 40 + 1 and 40 % 8 == 0 == 40 % 10 and is_prime(41) and all(v % 8 == 1 for v in vertices),
         "six diamonds on the co-linear are 1 to 49, a vertex 8 on a diamond: a centre's square is a vertex, 9 one diamond on, 25 three on, 49 six on; round ten the vertices are at 1, 9, 7, 5, 3, 1 and 9, and 41 is 40 and 1, one on from both seams")
    line("is", 9 == 8 + 1 == 10 - 1 and 49 == 48 + 1 == 50 - 1 and (8, 9, 10) == (2 * 4, 3 * 3, 2 * 5),
         "nine is between two seams, one on from eight and one before ten: even, odd, even; and 49 is one on from 48 and one before 50")
    kind = lambda n: {(0, 0): "on the co-linear", (2, 2): "on the co-linear", (1, 1): "its middle", (0, 2): "its widest", (2, 0): "its widest"}.get(cell(n if n <= 9 else n - 8), "a side")
    core = lambda n: re.sub(r"^\d+-(now|next)-", "", names[n])
    on_line, widest, a_side = [n for n in range(1, 18) if kind(n) in ("on the co-linear", "its middle")], [n for n in range(1, 18) if kind(n) == "its widest"], [n for n in range(1, 18) if kind(n) == "a side"]
    line("is", on_line == [1, 5, 9, 13, 17] and [core(n) for n in on_line] == ["existing", "co-existing", "co-discovering", "discovering", "existing"]
         and widest == [3, 7, 11, 15] and [core(n) for n in widest] == ["co-observing", "observing"] * 2
         and a_side == [2, 4, 6, 8, 10, 12, 14, 16] and all(core(n).endswith("possibling") for n in (2, 6, 10, 14)) and all(core(n).endswith("same-existing") for n in (4, 8, 12, 16)),
         "by Exhibit ONE's names: on the co-linear, 1, 5, 9, 13 and 17, are existing, co-existing, co-discovering, discovering and existing; at a diamond's widest, 3, 7, 11 and 15, the four of observing; on its sides, four of possibling and four of same-existing")
    line("is", [core(n) for n in (2, 3, 6)] == ["possibling", "co-observing", "co-possibling"] and [core(n) for n in (4, 7, 8)] == ["co-same-existing", "observing", "same-existing"],
         "from 1 to 9 are two paths, one on a side of its 5: by 2, 3 and 6, possibling about co-observing; and by 4, 7 and 8, same-existing about observing")
    plus, seam, less = [n for n in range(1, 18) if n % 8 == 1], [n for n in range(1, 18) if n % 8 == 0], [n for n in range(1, 18) if n % 8 == 7]
    root_of = lambda n: names[n].split("-")[-1]
    line("is", plus == [1, 9, 17] and seam == [8, 16] and less == [7, 15] and {root_of(n) for n in seam} == {"existing"} and all("same-existing" in names[n] for n in seam)
         and all(names[n].endswith("-observing") and "co-observing" not in names[n] for n in less) and names[1].endswith("now-existing") and names[17].endswith("next-existing") and names[9].endswith("co-discovering"),
         "by their own numbers the names at the me, 1, 9 and 17, are a seam of eight's +1; same-existing is at the seam, 8 and 16; and observing one before it, 7 and 15")
    line("found", "A local nine, centre one" in illus,
         "Natural Illustrating says a local nine with its middle 1; the seven drawings lay a partner's nine with its middle 5. The two numberings are laid side by side")
    line("found", True, "on a pair of cones the names at the me are at a seam of 30's +1, the 61st; by their own numbers, at a seam of eight's +1. 8 up is one round of both: 30 on, and 8 on")
    line("found", 1 + 2 + 3 + 4 == 10 == 5 * 4 // 2,
         "the 18th drawing's ten in four rows, of one, two, three and four, is a ten: the couplings among five, as the opening figure's ten corners are five with two sides")
    line("placing", True, "the diamond laid with 1 and 9 on the co-linear, its four moves as marks about it, and the tints of a corner, a side's middle and its 5 are the drawing's own placings")
    own = {"names": names, "plus": plus, "seam": seam, "less": less, "kind": kind, "vertices": vertices, "seams": seams, "rounds": rounds}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
