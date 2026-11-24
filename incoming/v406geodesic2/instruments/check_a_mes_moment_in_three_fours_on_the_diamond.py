"""v406geodesic2 · the check of the 24th drawing: a me's moment as three fours and a one on the diamond of nine, with rigor.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_a_mes_moment_in_three_fours_on_the_diamond.py \
      Exhibit_ONE_Natural_Resolver_v402mgr.md incoming/v403mgr/The_seventeen_names_in_one_table.csv \
      incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py

A partner's saying of 24 November is its ground, as said in the transcripts, pared. Re-said: in place of observes and gives, on the
23rd drawing's diamond: 1, 2, 4, 5 co-observing; 3, 5, 7, 5 co-possibling; 5, 8, 6, 9 co-discovering; and 9 bi-neutralling. To be
gone through with rigor: it is possibly off, beside, or of no value.
Four ways, all or none: the diamond's own form; the living code's own lines; the seventeen names' own roots; and the cell by nand.
A line says what is and what is not, and the line is is with both said as they are.
It opens Exhibit ONE Natural Resolver for its code, the seventeen names' one table, and v406Reiman's cell, and writes none.
"""
import ast, csv, importlib.util, re, sys
from itertools import product
from pathlib import Path
exhibit_one, table, its_file = (Path(a) for a in sys.argv[1:4])
results = []
def line(name, ok): results.append((name, bool(ok)))

FRONT, MIDDLE, BACK, ONE_MORE = [1, 2, 4, 5], [3, 5, 7, 5], [5, 8, 6, 9], [9]      # a partner's three fours and a one, as said
NINE = set(range(1, 10))
# ---------------- the diamond's own form ----------------
line("a partner's three fours and a one are all the diamond's nine; the 5 is in all three fours, and no other number is in two",
     set(FRONT) | set(MIDDLE) | set(BACK) | set(ONE_MORE) == NINE and set(FRONT) & set(MIDDLE) & set(BACK) == {5} and (set(FRONT) & set(BACK)) | (set(FRONT) & set(MIDDLE)) | (set(MIDDLE) & set(BACK)) == {5})
grid = {(a, b): a + 3 * b for a in (1, 2, 3) for b in (0, 1, 2)}
square = lambda a0, b0: sorted(grid[(a, b)] for a in (a0, a0 + 1) for b in (b0, b0 + 1))
line("the front four is the three by three's square at its opening corner and the back four the square at its far corner, the front 4 on and its podal about 5; as said, the front is two arcs of a step of 1, the middle steps of 2 and 5 again, and the back two arcs of a step of 3",
     square(1, 0) == sorted(FRONT) and square(2, 1) == sorted(BACK) and sorted(n + 4 for n in FRONT) == sorted(BACK) == sorted(10 - n for n in FRONT)
     and (FRONT[1] - FRONT[0], FRONT[3] - FRONT[2]) == (1, 1) and (MIDDLE[1] - MIDDLE[0], MIDDLE[2] - MIDDLE[1], MIDDLE[3]) == (2, 2, 5) and (BACK[1] - BACK[0], BACK[3] - BACK[2]) == (3, 3))
line("added, the three fours are 12, 20 and 28, 8 on and 8 on, and 60 together, a pair of cones; a fourth of them is 3, 5 and 7, the diamond's widest row",
     [sum(FRONT), sum(MIDDLE), sum(BACK)] == [12, 20, 28] and sum(FRONT) + sum(MIDDLE) + sum(BACK) == 60 and [sum(f) // 4 for f in (FRONT, MIDDLE, BACK)] == [3, 5, 7] and all(sum(f) % 4 == 0 for f in (FRONT, MIDDLE, BACK)))

# ---------------- the living code's own lines ----------------
code = re.search(r"```python\n(.*?)```", exhibit_one.read_text(encoding="utf-8"), flags=re.S).group(1)
tree = ast.parse(code)
number = lambda name: int(re.match(r"_(\d+)_", name).group(1)) if re.match(r"_(\d+)_", name) else None
def numbers(node):
    return ({number(n.id) for n in ast.walk(node) if isinstance(n, ast.Name) and number(n.id)} | {number(a.arg) for a in ast.walk(node) if isinstance(a, ast.arg) and number(a.arg)})
fns = {number(f.name): f for f in tree.body if isinstance(f, ast.FunctionDef)}
a_moment = fns[1]                                                                     # a me's own moment: the code's 1-now-existing
in_a_moment = numbers(a_moment) | {1}
going_on = numbers(fns[9]) | numbers(fns[17]) | {9, 17}
line("the living code is three, named 1, 9 and 17; of the nine names, the ones in no line of a me's own moment, its 1, are 5, 6, 8 and 9: a partner's back four, all four and no other",
     sorted(fns) == [1, 9, 17] and NINE - in_a_moment == set(BACK) and set(BACK) <= going_on)
loops = [st for st in a_moment.body if isinstance(st, ast.For)]
over = lambda loop: number(loop.iter.id)
line("a me's own moment has 1, its own name, and 2, 3, 4 and 7 in its lines: a partner's front four and middle four less their 5s; its opening loop, over 2, what it observes, has 2, 4 and 7, and its next, over 3, its prior, has 3, 4 and 7: 2 with the front and 3 with the middle as said, and 4 and 7 in both",
     in_a_moment & NINE == (set(FRONT) | set(MIDDLE)) - {5} and [over(l) for l in loops[:2]] == [2, 3] and numbers(loops[0]) & NINE == {2, 4, 7} and numbers(loops[1]) & NINE == {3, 4, 7})
line("the 5 of a partner's front and middle fours is not of a me's own moment by the code: 5, the bi-couplings, is in its going on alone, with 9 and with 17",
     5 not in in_a_moment and 5 in numbers(fns[9]) and 5 in numbers(fns[17]))
choosing = lambda f: sum(isinstance(n, (ast.If, ast.Compare, ast.IfExp)) for n in ast.walk(f))
line("the 9, by the code, has no is-or-is-not in its lines, no comparing and no choosing: a giving carried to the me a coupling names, between two; a me's own moment has them; and by numbers 9 alone of 1 to 17 is its own podal about 9, in both diamonds",
     choosing(fns[9]) == 0 and choosing(a_moment) > 0 and [n for n in range(1, 18) if 18 - n == n] == [9] and set(range(1, 10)) & set(range(9, 18)) == {9})
line("8 up, the back diamond's names: of 10 to 17 a me's own moment has 10, 11, 12, 14 and 15; a partner's fours 8 up have 10, 12, 11 and 15 of them the same way, and 14 with the going on: one name of the eight is other than the fours 8 up",
     in_a_moment & set(range(10, 18)) == {10, 11, 12, 14, 15} and {n + 8 for n in (set(FRONT) | set(MIDDLE)) - {1, 5}} == {10, 11, 12, 15} and 14 in {n + 8 for n in BACK})

# ---------------- the seventeen names' own roots ----------------
rows = list(csv.reader(table.open(encoding="utf-8")))
name_of = {int(r[0]): r[1] for r in rows[1:]}
root = {n: re.sub(r"^\d+-(now|next)-(co-)?", "", name_of[n]) for n in name_of}
co = {n for n in name_of if "-co-" in name_of[n]}
word_at = lambda word: sorted(n for n in NINE if n in co and root[n] == word)
line("by the names' own roots, on the diamond a root is a line along: 2 and 6 possibling, 4 and 8 same-existing, 3 and 7 observing, 1 and 5 existing and 9 discovering; and the co names of a partner's three words are 3, 6 and 9, co-observing, co-possibling and co-discovering, one arc of a step of 3",
     [root[n] for n in range(1, 10)] == ["existing", "possibling", "observing", "same-existing", "existing", "possibling", "observing", "same-existing", "discovering"]
     and all(root[n] == root[n + 4] for n in range(1, 5)) and (word_at("observing"), word_at("possibling"), word_at("discovering")) == ([3], [6], [9]) and (6 - 3, 9 - 6) == (3, 3))
line("of a partner's three words, by the names: co-discovering is at its own name, 9 in its four; co-possibling is not, 6 being in the back four; co-observing is not, 3 being in the middle four: the fours' own co names are none of the three in the front, co-observing in the middle, and co-possibling with co-discovering in the back",
     9 in BACK and 6 not in MIDDLE and 6 in BACK and 3 not in FRONT and 3 in MIDDLE and not (set(FRONT) & {3, 6, 9}))
line("by its root the front four has 2, now-possibling, the code's own name of what a me observes; by its root the middle has 3 and 7, now-co-observing and now-observing, the code's own names of a me's prior and of a parity",
     name_of[2] == "2-now-possibling" and 2 in FRONT and (name_of[3], name_of[7]) == ("3-now-co-observing", "7-now-observing") and {3, 7} <= set(MIDDLE)
     and [number(a.arg) for a in a_moment.args.args] == [3, 2])

# ---------------- the cell by nand ----------------
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", its_file)
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
TWO, ONE = its.TWO, its.ONE
def a_me(prior, observed):
    gives, its_next, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed])
    return ONE[gives], ONE[its_next]
def surfacing(observed):                                                              # a + among them and no -, a - and no +, or a 0
    return 1 if (1 in observed and -1 not in observed) else (-1 if (-1 in observed and 1 not in observed) else 0)
observings = [list(o) for k in range(4) for o in product((1, -1, 0), repeat=k)]
line("a me's moment by nand is three steps in a row: what it observes, to its surfacing, one of three; its surfacing with its prior, same-existing or not; and its giving with its next prior. What it observes enters by its surfacing alone: all observings of none to three with one surfacing have one giving and one next prior, with all priors",
     all(a_me(p, o) == a_me(p, [surfacing(o)]) for p in (0, 1, -1) for o in observings) and len(observings) == 40
     and all(a_me(p, [s]) == ((0, p) if (p and s == p) else ((-p, -p) if p else (s, s))) for p in (0, 1, -1) for s in (0, 1, -1)))
line("a 0 surfaces two ways, with none observed and with a + and a - observed together, parting; and a me gives none a third way, same-existing: neutral is more than one thing in a me's moment",
     surfacing([]) == 0 == surfacing([1, -1]) and all(a_me(p, []) == a_me(p, [1, -1]) for p in (0, 1, -1)) and all(a_me(p, [p])[0] == 0 for p in (1, -1)))
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
