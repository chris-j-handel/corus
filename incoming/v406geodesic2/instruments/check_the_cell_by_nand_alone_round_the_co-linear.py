"""v406geodesic2 · the check of the sixth drawing: the cell by nand alone, round the co-linear.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_cell_by_nand_alone_round_the_co-linear.py \
      incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py .

The cell is v406Reiman's, opened from its own file as it is: no line of it is written here.
Its named things are gone through a line at a moment, its own lines with their return widened to all of them.

The candidate laid on the drawing, on the fifth drawing's figure:
  a parity is two is-or-is-nots, a + and a -, and the two are the two folds' circles through the co-linear;
  the four quarters round the co-linear are a +, a + and a -, a -, and none, the one triangle's own quarter a +;
  a fold about a circle is an other-than, and two folds in a row, about the two circles, are through the co-linear;
  a prior is of the far side and a next prior of its own side, the circle between the two a moment's now.
It opens the pages and writes none. All or none: with one line not is, the check is not.
"""
import ast, copy, importlib.util, itertools, re, sys
from pathlib import Path
import numpy as np

results = []
def line(name, ok): results.append((name, bool(ok)))

# ---------- the cell, from its own file ----------
its_file, root = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", its_file)
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
tree = ast.parse(its_file.read_text(encoding="utf-8"))
cell = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "a_cell")
its_lines = [n for n in ast.walk(cell) if isinstance(n, (ast.Assign, ast.For, ast.Return))]
line("the cell's lines are fifteen", len(its_lines) == 15)
wide = copy.deepcopy(cell); wide.name = "a_cell_with_its_named_things"
wide.body[-1] = ast.parse("return dict(locals())").body[0]
space = dict(vars(its)); exec(compile(ast.fix_missing_locations(ast.Module([wide], [])), str(its_file), "exec"), space)
named = space["a_cell_with_its_named_things"]

TWO = (False, True)
PLUS, MINUS, NONE, BOTH = (True, False), (False, True), (False, False), (True, True)
lists = [list(o) for k in range(5) for o in itertools.product((PLUS, MINUS, NONE), repeat=k)]   # none to four observed
line("other-than is one nand, a thing with itself; both is two nands in a row; either is a nand of two other-thans",
     all(its.other_than(a) == its.nand(a, a) for a in TWO)
     and all(its.both(a, b) == its.nand(its.nand(a, b), its.nand(a, b)) and its.either(a, b) == its.nand(its.nand(a, a), its.nand(b, b)) for a in TWO for b in TWO))

# ---------- the fifth drawing's figure ----------
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
fold_of_a_plus = np.diag([1.0, 1.0, -1.0])       # about the horizon's circle, the second drawing's fold
fold_of_a_minus = np.diag([1.0, -1.0, 1.0])      # about the circle of the side from the me to B, its other fold
fold_of_the_between = np.diag([-1.0, 1.0, 1.0])  # about the circle between the far side and its own side
through_the_co_linear = fold_of_a_plus @ fold_of_a_minus
through_the_0 = fold_of_the_between @ through_the_co_linear
def quarter(parity):
    """A parity's quarter round the co-linear, by its sides of the two circles: (of C, of the me)."""
    plus, minus = parity
    return (-1 if minus else 1, 1 if plus else -1)
def folded(q, fold): return tuple(int(v) for v in (fold @ np.array([0.0, q[0], q[1]]))[1:])
def angle(q): return np.degrees(np.arctan2(q[1], q[0])) % 360
line("a fold twice is as it was, and an other-than twice: two in a row of one are the prior again",
     all(np.allclose(f @ f, np.eye(3)) for f in (fold_of_a_plus, fold_of_a_minus, fold_of_the_between)) and all(its.other_than(its.other_than(a)) == a for a in TWO))
line("the one triangle's own quarter is a +, and the four cases of a + and a - are the four quarters round the co-linear",
     quarter(PLUS) == (1, 1) and len({quarter(p) for p in (PLUS, BOTH, MINUS, NONE)}) == 4)
round_ = sorted((PLUS, BOTH, MINUS, NONE), key=lambda p: angle(quarter(p)))
line("round the co-linear the four are a +, a + and a -, a -, and none, in turn a parity and a 0",
     round_ == [PLUS, BOTH, MINUS, NONE] and [its.ONE[p] for p in round_] == [1, 0, -1, 0])
line("a step from a quarter to its next is one fold, one is-or-is-not inverting: an other-than",
     all(sum(a != b for a, b in zip(round_[i], round_[(i + 1) % 4])) == 1 for i in range(4))
     and all(folded(quarter(p), fold_of_a_plus) == quarter((its.other_than(p[0]), p[1])) and folded(quarter(p), fold_of_a_minus) == quarter((p[0], its.other_than(p[1]))) for p in round_))
turn = 2 * np.outer(B, B) - np.eye(3)
line("two folds in a row, about the two circles, are through the co-linear, two right spiral steps about it: a + with a -, and both with none",
     np.allclose(through_the_co_linear, turn) and folded(quarter(PLUS), through_the_co_linear) == quarter(MINUS) and folded(quarter(BOTH), through_the_co_linear) == quarter(NONE))

# ---------- lines 1 to 6: observing, and the parity surfacing ----------
def observed_by_folds(observing):
    """From none, a fold with a parity observed that its quarter is not yet of; the folds gone, one at a moment."""
    q, gone = quarter(NONE), []
    for plus, minus in observing:
        step = 0
        if plus and q[1] < 0: q, step = folded(q, fold_of_a_plus), step + 1
        if minus and q[0] > 0: q, step = folded(q, fold_of_a_minus), step + 1
        gone.append(step)
    return q, gone
ok_observing = ok_one_fold = True
for prior in (PLUS, MINUS, NONE):
    for observing in lists:
        things = named(prior, observing)
        q, gone = observed_by_folds(observing)
        ok_observing = ok_observing and q == quarter((things["a_plus"], things["a_minus"]))
        ok_one_fold = ok_one_fold and all(g in (0, 1) for g in gone) and sum(gone) <= 2
line("lines 1 to 4: observing is from none, and a parity observed is a fold or none: one fold to a + or to a -, and one more to a + and a -", ok_observing)
line("no fold of observing is back: a parity observed again is no fold, and two folds are the most", ok_one_fold)
def not_both(q): return folded(q, through_the_co_linear) if q == quarter(BOTH) else q
ok_surfacing = all(quarter((t["surfacing_plus"], t["surfacing_minus"])) == not_both(quarter((t["a_plus"], t["a_minus"])))
                   for prior in (PLUS, MINUS, NONE) for observing in lists for t in [named(prior, observing)])
line("lines 5 and 6, not both: a + and a - go through the co-linear to none, two folds in a row, and a +, a - and none are as they were", ok_surfacing)

# ---------- lines 7 to 12: its prior, and its one is-or-is-not ----------
line("lines 7 and 8: its prior is a +, a -, or none, and no prior is none",
     all(named(prior, [])["no_prior"] == (prior == NONE) for prior in (PLUS, MINUS, NONE)))
ok_cell = ok_one_of_four = ok_triangles = ok_given = True
for prior in (PLUS, MINUS):
    for observing in lists:
        things = named(prior, observing)
        gives, its_next, a_giving, a_next = its.a_cell(prior, observing)
        observed = quarter((things["a_plus"], things["a_minus"]))
        surfacing = quarter((things["surfacing_plus"], things["surfacing_minus"]))
        an_is = surfacing == quarter(prior)
        across = folded(quarter(prior), through_the_co_linear)
        ok_cell = ok_cell and quarter(its_next) == (quarter(prior) if an_is else across) and quarter(gives) == (quarter(NONE) if an_is else across)
        ok_one_of_four = ok_one_of_four and an_is == (observed == quarter(prior))
        from_far = np.array([-1.0, *quarter(prior)]); to_own = np.array([1.0, *quarter(its_next)])
        folds = int(sum(from_far != to_own))
        ok_triangles = ok_triangles and folds == (1 if an_is else 3) and (an_is or np.allclose(to_own, through_the_0 @ from_far)) and (not an_is or np.allclose(to_own, fold_of_the_between @ from_far))
        ok_given = ok_given and a_giving and a_next
line("lines 9 to 12, with a prior: with is, its giving is none, a 0, and its next prior is its prior; with is-not, its giving and its next prior are the quarter through the co-linear from its prior, one inversion", ok_cell)
line("its one is-or-is-not is of four quarters: with what it is observing in its prior's own quarter alone it is is, and with the three others is-not", ok_one_of_four)
line("from its prior, a triangle of the far side, to its next prior, a triangle of its own side: with is one fold, about the circle between, and with is-not three, through the 0, to the triangle opposite", ok_triangles)
line("with a prior + and is, its next prior is the one triangle itself",
     tuple(int(v) for v in fold_of_the_between @ np.array([-1.0, *quarter(PLUS)])) == (1, 1, 1))
ok_opening = True
for observing in lists:
    things = named(NONE, observing)
    gives, its_next, a_giving, a_next = its.a_cell(NONE, observing)
    surfacing = (things["surfacing_plus"], things["surfacing_minus"])
    ok_opening = ok_opening and gives == surfacing and its_next == surfacing and a_next == (surfacing != NONE)
line("with no prior, its giving and its next prior are the parity surfacing, and with none surfacing no next prior is", ok_opening)
line("lines 13 to 15: with a prior a giving is and a next prior is, to the cell again", ok_given)
swap = lambda p: (p[1], p[0])
between_the_two = np.array([[1.0, 0, 0], [0, 0, -1.0], [0, -1.0, 0]])     # a fold about a third circle through the co-linear, through the quarters of both and of none
ok_alike = all(folded(quarter(p), between_the_two) == quarter(swap(p)) for p in (PLUS, BOTH, MINUS, NONE))
for prior in (PLUS, MINUS, NONE):
    for observing in lists:
        g, n, _, _ = its.a_cell(prior, observing); g2, n2, _, _ = its.a_cell(swap(prior), [swap(o) for o in observing])
        ok_alike = ok_alike and g2 == swap(g) and n2 == swap(n)
line("a + and a - alike: with the two exchanged the cell is as it was, and the exchanging is one fold, about a third circle through the co-linear, through the quarter of both and the quarter of none", ok_alike)

# ---------- a nand, of the eight triangles ----------
def triangle(a, b, c): return (1 if c else -1, *quarter((a, b)))
its_four = lambda f: {triangle(a, b, f(a, b)) for a in TWO for b in TWO}
moved = lambda four, fold: {tuple(int(v) for v in fold @ np.array(t, float)) for t in four}
nand4 = its_four(its.nand)
line("a nand is four of the eight triangles: of the quarter of both the far side's, and of the three other quarters its own side's",
     nand4 == {(-1, *quarter(BOTH))} | {(1, *quarter(p)) for p in (PLUS, MINUS, NONE)})
line("both is that four folded about the circle between, and either is it gone through the co-linear",
     its_four(its.both) == moved(nand4, fold_of_the_between) and its_four(its.either) == moved(nand4, through_the_co_linear))
line("other-than is two of the four, opposite through the 0", {triangle(a, a, its.other_than(a)) for a in TWO} <= nand4
     and moved({triangle(True, True, its.other_than(True))}, through_the_0) == {triangle(False, False, its.other_than(False))})

# ---------- beside Exhibit ONE Natural Resolver, its code and its own cells ----------
names, page = its.resolver(str(root))
now = names["_1_now_existing"]
ok_living = True
for prior in ([(its.S, 1)], [(its.S, -1)], []):
    for k in range(5):
        for seen in itertools.product((1, -1, 0), repeat=k):
            observing = [(its.S, v) for v in seen]
            living, with_nand = now(list(prior), list(observing)), its.now_with_nand(list(prior), list(observing))
            ok_living = ok_living and its.as_observed(living[0]) == its.as_observed(with_nand[0]) and living[1] == with_nand[1]
line("the cell and Exhibit ONE Natural Resolver's 1-now-existing as it is, a prior +, a prior - and no prior with none to four observed: the same giving, a 0 passed over, and the same next prior", ok_living)
ONE_md = next(root.glob("Exhibit_ONE_Natural_Resolver_*.md")).read_text(encoding="utf-8")
PARITY_OF = {"+": PLUS, "−": MINUS, "0": NONE}
SEEN = {"empty": [], "+": [PLUS], "−": [MINUS], "+ and − together": [PLUS, MINUS]}
part = ONE_md[ONE_md.index("**One self, one moment.**"):ONE_md.index("**One cell, four receivings.**")]
cells, prior = [], None
for row in part.splitlines():
    head = re.match(r"- \*\*A prior, 3-now-co-observing, one sharing: (.)\*\*", row)
    if head: prior = PARITY_OF[head.group(1)]
    one = re.match(r"\s+- \*Surfacing, 14-next-possibling: (.+?)\*: (.) · (.)$", row)
    if one: cells.append((prior, SEEN[one.group(1)], PARITY_OF[one.group(2)], PARITY_OF[one.group(3)]))
line("Exhibit ONE Natural Resolver's own eight cells of One self, one moment, a prior + and a prior - with its four surfacings, are the cell's, giving and next prior",
     len(cells) == 8 and all(its.a_cell(p, seen)[:2] == (gives, nxt) for p, seen, gives, nxt in cells))

# ---------- word for word, living ----------
text = lambda pattern: next(root.glob(pattern)).read_text(encoding="utf-8")
NI, THREE, FOUR, THIRTY = text("Natural_Intelligence_v*.md"), text("Exhibit_THREE_*.md"), text("Exhibit_FOUR_*.md"), text("Exhibit_THIRTY_*.md")
quotes = [
    (ONE_md, "With a prior of one parity, four receivings come to one cell: an inverse parity surfacing, + and − together, an empty set surfacing, and a 0 a self passes over. In that cell its prior inverts."),
    (ONE_md, "One cell is alike for four receivings."),
    (ONE_md, "A sharing of 0 is its prior same-existing."),
    (ONE_md, "Each cell with + and − exchanging is that cell exchanging, with a prior and with an empty prior."),
    (ONE_md, "a 0 both with an empty set surfacing and with + and − parting"),
    (NI, "Its two meetings are co-parity, the same, sharing 0, and bi-parity, one inversion."),
    (NI, "With code each is-or-is-not is one test with both its outcomes"),
    (THREE, "a self's bi-inversioning-co-recursioning is 23, 24 and 25, one before its apex and one after"),
    (FOUR, "Bi-inversioning-co-recursioning is two consecutive inversions on different axes"),
    (THIRTY, "One inversion is other-than-prior"),
    (THIRTY, "an even number of them same-as its prior and an odd number other-than"),
]
line("eleven living sentences beside the drawing are word for word in their files", all(q in t for t, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
