"""v406geodesic2 · the fourth drawing's fold, set beside the seventeen names.

Usage: python3 -I the_fold_beside_the_seventeen_names.py PATH_TO_The_seventeen_names_in_one_table.csv

The fourth drawing lays 8 up as one fold, a mirror through the me's line. This instrument executes what the
set's table of the seventeen names says of 8 up, 9 less and 17 less by its four parities, and what two folds
of the one triangle on lines at a right angle are. It decides nothing: it lays the two beside one another.
"""
import csv, math, sys
import numpy as np

rows = list(csv.reader(open(sys.argv[1], encoding="utf-8")))
head = rows[0]
col = next(i for i, h in enumerate(head) if h.startswith("four parities, one changing"))
par = {}
for r in rows[1:]:
    try: n = int(r[0])
    except ValueError: continue
    par[n] = r[col].strip()
assert sorted(par) == list(range(1, 18)), "seventeen names expected"
print("the table's column:", head[col])

def changing(a, b):                       # which of four parities part, the fourth said at the far end
    return [4 - i for i, (x, y) in enumerate(zip(par[a], par[b])) if x != y]

results = []
def line(name, ok): results.append((name, bool(ok)))

steps = [changing(n, n + 1) for n in range(1, 17)]
line("the table: one parity alone parts a name from its next, 1 to 17", all(len(s) == 1 for s in steps))
up8 = {tuple(sorted(changing(n, n + 8))) for n in range(1, 10)}
line("the table: 8 up parts two parities, the third and the fourth, with all of 1 to 9", up8 == {(3, 4)})
less9 = {tuple(changing(n, 9 - n)) for n in range(1, 9)}
line("the table: 9 less parts one parity, the third", less9 == {(3,)})
less17 = {tuple(changing(n, 17 - n)) for n in range(1, 17)}
line("the table: 17 less parts one parity, the fourth", less17 == {(4,)})
line("the table: 9 less and then 17 less is 8 up or 8 down, with all of 1 to 8", all(17 - (9 - n) == n + 8 for n in range(1, 9)))
line("the table: a move of one parity exchanges odd and even; 8 up does not", all((n + (9 - n)) % 2 == 1 for n in range(1, 9)) and all((n + 8 - n) % 2 == 0 for n in range(1, 10)))

# the one triangle: a me at A, tips B and C on the me's horizon, the far side's middle M
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0]); M = (B + C) / math.sqrt(2)
fold_me = np.array([[0, 1.0, 0], [1.0, 0, 0], [0, 0, 1.0]])      # about the me's line: one tip onto its other
fold_far = np.diag([1.0, 1.0, -1.0])                             # about the far side: the me onto its other
both = fold_far @ fold_me
line("the triangle: the me's line and the far side cross at a right angle, at the far side's middle",
     abs(np.cross(A, M) @ np.cross(B, C)) < 1e-12 and np.allclose(fold_me @ M, M) and np.allclose(fold_far @ M, M))
line("the triangle: one fold about the me's line is a mirror, tip B onto tip C, the me as it is",
     np.linalg.det(fold_me) < 0 and np.allclose(fold_me @ B, C) and np.allclose(fold_me @ A, A))
turn = 2 * np.outer(M, M) - np.eye(3)                            # two right spiral steps about the line through M
line("the triangle: the two folds, one and then its other, are two right spiral steps about the far side's middle, no mirror",
     np.allclose(both, turn) and np.linalg.det(both) > 0 and np.allclose(both, fold_me @ fold_far))
line("the triangle: by the two folds tip B is onto tip C and C onto B, and the me onto its other across its horizon",
     np.allclose(both @ B, C) and np.allclose(both @ C, B) and np.allclose(both @ A, -A))
line("the triangle: the two folds again, four right spiral steps: the triangle as it was, 1 as 17", np.allclose(both @ both, np.eye(3)))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
print("\nBeside one another, the move of 8 said two ways in the set, and the fourth drawing:")
print("  Exhibit ONE Natural Resolver, living: a bi-folding goes two folds in turn, 17 less and a move of 8 up or down.")
print("  The table's four parities and the workbook's sheet Surface: 8 up parts two parities, 9 less and then 17 less, through the centre.")
print("  The fourth drawing: 8 up is one fold, a mirror through the me's line.")
sys.exit(0 if all(ok for _, ok in results) else 1)
