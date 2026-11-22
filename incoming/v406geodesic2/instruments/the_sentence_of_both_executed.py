"""v406geodesic2 · the sentence of both, of v406all2-2 and this session, executed, and the torus by the sheet's lines.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/the_sentence_of_both_executed.py \
      incoming/v403mgr/The_seventeen_names_in_one_table.csv \
      incoming/v406me/working_documents_as_a_partner_gave_them/The_seventeen_names_in_one_table_its_sheet_Surface.csv \
      Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md

The sentence: 8 up is two right spiral steps, 9 less and then 17 less, one parity inverting with each.
It opens the three pages and writes none. It decides nothing: a line is is, or is not.
"""
import csv, sys

table, sheet, thirty = sys.argv[1], sys.argv[2], sys.argv[3]
rows = list(csv.reader(open(table, encoding="utf-8")))
col = next(i for i, h in enumerate(rows[0]) if h.startswith("four parities, one changing"))
par = {}
for r in rows[1:]:
    try: par[int(r[0])] = r[col].strip()
    except ValueError: pass
assert sorted(par) == list(range(1, 18)), "seventeen names expected"

def parting(a, b):                      # which of a name's four parities part two names, the fourth at the far end
    return tuple(4 - i for i, (x, y) in enumerate(zip(par[a], par[b])) if x != y)
def less9(n): return 9 - n if n <= 8 else 25 - n          # 9 less, with its eight
def less17(n): return 17 - n

results = []
def line(name, ok): results.append((name, bool(ok)))

# ---- the sentence, by the table's four parities
line("9 less, with its eight, inverts one parity, the third, with all sixteen names", {parting(n, less9(n)) for n in range(1, 17)} == {(3,)})
line("17 less inverts one parity, the fourth, with all sixteen names", {parting(n, less17(n)) for n in range(1, 17)} == {(4,)})
line("9 less and then 17 less is 8 up with 1 to 8, and 8 down with 9 to 16",
     all(less17(less9(n)) == n + 8 for n in range(1, 9)) and all(less17(less9(n)) == n - 8 for n in range(9, 17)))
round_ = [1]
for step in (less9, less17, less9, less17): round_.append(step(round_[-1]))
line("the two, one and then its other, go 1 to 8 to 9 to 16 and to 1 with four steps", round_ == [1, 8, 9, 16, 1])
line("one parity inverting with a step of the four: the third, the fourth, the third, the fourth",
     [parting(round_[i], round_[i + 1]) for i in range(4)] == [(3,), (4,), (3,), (4,)])
text = open(thirty, encoding="utf-8").read()
line("Exhibit THIRTY, word for word: Two right spiral steps invert both parities", "Two right spiral steps invert both parities" in text)
line("Exhibit THIRTY, word for word: a right spiral step, one parity each step", "a right spiral step, one parity each step" in text)
line("4 up inverts two parities of a name's four with all of 1 to 12: the second and the third, and from 5 to 8 the second and the fourth",
     all(tuple(sorted(parting(n, n + 4))) == ((2, 4) if 5 <= n <= 8 else (2, 3)) for n in range(1, 13)))

# ---- the sheet Surface's lines, as a surface gone round its edges: a torus of sixteen names
cells = list(csv.reader(open(sheet, encoding="utf-8")))
head = next(i for i, r in enumerate(cells) if any(c.strip().startswith("first: lines") for c in r))
c0 = next(j for j, c in enumerate(cells[head]) if c.strip().startswith("first: lines"))
grid = [[int(cells[head + 1 + i][c0 + j]) for j in range(4)] for i in range(4)]
line("the sheet's lines: 1 2 3 4, 8 7 6 5, 9 10 11 12, 16 15 14 13", grid == [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12], [16, 15, 14, 13]])
pairs = [(grid[i][j], grid[i][(j + 1) % 4]) for i in range(4) for j in range(4)] + [(grid[i][j], grid[(i + 1) % 4][j]) for i in range(4) for j in range(4)]
line("on it, round its edges, two names beside one another are one parity apart, all thirty-two pairs", len(pairs) == 32 and all(len(parting(a, b)) == 1 for a, b in pairs))
down = [frozenset(grid[i][j] for i in range(4)) for j in range(4)]
line("a line down it is a bi-folding of the four: 1 8 9 16, 2 7 10 15, 3 6 11 14, 4 5 12 13",
     set(down) == {frozenset(b) for b in ([1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12])})
line("down a line a step is 9 less or 17 less, one and then its other, and two steps are 8 up or down",
     all(grid[(i + 1) % 4][j] == (less9 if i % 2 == 0 else less17)(grid[i][j]) and abs(grid[(i + 2) % 4][j] - grid[i][j]) == 8 for i in range(4) for j in range(4)))
line("the winding 1 to 17 goes along a line across and round an edge at a between, 4 to 5, 8 to 9, 12 to 13 and 16 to 17, one parity inverting with a step",
     all(len(parting(n, n + 1)) == 1 for n in range(1, 17)))
# ---- the third drawing's torus, by n - 1 in four binary digits, beside it
third = [[4 * i + j + 1 for j in range(4)] for i in range(4)]
line("the third drawing's torus parts from the sheet's lines in two of four: 5 to 8 and 13 to 16 go round the large opening the other way",
     [third[i] == grid[i] for i in range(4)] == [True, False, True, False] and all(third[i] == grid[i][::-1] for i in (1, 3)))
HEIGHT = ["outer top", "inner top", "inner bottom", "outer bottom"]
q = lambda n: (n - 1) // 4
kinds = {tuple(sorted({HEIGHT[q(n)], HEIGHT[q(n + 4)]})) for n in range(1, 13)}
line("on the third drawing's torus 4 up is outer with inner at one height with 1 to 4 and with 9 to 12, and inner with inner, upper with lower, with 5 to 8",
     kinds == {("inner top", "outer top"), ("inner bottom", "inner top"), ("inner bottom", "outer bottom")}
     and all({HEIGHT[q(n)], HEIGHT[q(n + 4)]} == {"inner top", "inner bottom"} for n in range(5, 9)))
line("the four betweens are the winding's passings from a height to its next, and no other two names one apart are of two heights",
     [n for n in range(1, 17) if q(n) != q(n % 16 + 1)] == [4, 8, 12, 16])
turn = lambda n: 90 if q(n) in (0, 3) else -90            # degrees, by the direction a place faces
line("by the direction a place faces, a bi-folding of the four is at nought and a middle bi-folding at 360 under it",
     all(sum(turn(n) for n in b) == 0 for b in ([1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12])) and all(sum(turn(n) for n in b) == -360 for b in ([9, 5, 12, 8], [7, 11, 6, 10])))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
sys.exit(0 if all(ok for _, ok in results) else 1)
