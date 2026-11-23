#!/usr/bin/env python3
"""All or none at all: the cell by nand alone and Exhibit ONE Natural Resolver's living code, as one method.

    python3 -I incoming/v406all2/instruments/the_two_codes_one_method_all_or_none.py .

The cell is `a_cell` of `incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py`, as it is.
Exhibit ONE Natural Resolver's code is the python block of its living file, as it is. No line of
either is written here, and no line of either moves. Of the exchange on 22 November.

The way: a finite all. By its own syntax the living cell goes through a value by its side of 0 alone,
and a name's observed list one value at a moment into one of four states. Four states, three sides of
a value and three priors are all of a cell: its steps and its cases are gone through, all of them, and
a moment of a society is the living code's own lines with the cell alone swapped. An all at the cell
is then an all at all societies, all couplings and all moments.

Two partings are a call's alone, and no line of the living code makes them: a prior 0 supplied, and a
value other-than a +, a - and a 0. They are shown at the foot, with what a session beginning found of
the prior 0 on 23 November.

It writes its lines to standard output. It writes no file and decides nothing.
"""
import ast
import itertools
import re
import sys
from pathlib import Path

REIMAN = Path(__file__).resolve().parents[2] / "v406Reiman" / "instruments"
sys.dont_write_bytecode = True
sys.path.insert(0, str(REIMAN))
from resolver_as_it_is import S, resolver
from the_resolver_with_nand_alone import now_with_nand as nand_cell

names, page_name = resolver(sys.argv[1])
page = Path(sys.argv[1]) / page_name
code = re.search(r"```python\n(.*?)```", page.read_text(encoding="utf-8"), re.S).group(1)
living = names
living_cell = living["_1_now_existing"]


def said(a_cell_s_answer):
    giving, next_prior = a_cell_s_answer
    return tuple(sorted(giving, key=str)), tuple(sorted(next_prior, key=str))


results = []
def all_or_none(what, pairs):
    pairs = list(pairs)
    parted = [p for p in pairs if p[1] != p[2]]
    results.append((what, len(pairs), len(parted)))
    print(f"{'ALL ' if not parted else 'NONE'} · {what}: {len(pairs)} gone through, {len(parted)} parting")
    for p in parted[:3]:
        print("        parts at", p[0], "| living:", p[1], "| by nand:", p[2])

# ---- 1. by syntax: the living cell goes through a value by its side of 0 alone
tree = ast.parse(code)
cell = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_1_now_existing")
def by_a_side_of_0(c):
    if len(c.ops) != 1: return False
    one_side, its_other = c.left, c.comparators[0]
    if isinstance(its_other, ast.Constant) and its_other.value in (0, None): return True
    return all(isinstance(x, ast.Compare) and isinstance(x.comparators[0], ast.Constant) and x.comparators[0].value == 0 for x in (one_side, its_other))
compares = [n for n in ast.walk(cell) if isinstance(n, ast.Compare)]
sums = [n for n in ast.walk(cell) if isinstance(n, (ast.BinOp, ast.AugAssign))]
all_or_none("the living cell's is-or-is-nots are of a value's side of 0 alone, by its own syntax",
            [(ast.unparse(c), True, by_a_side_of_0(c)) for c in compares] + [("no adding and no multiplying of a value", 0, len(sums))])
nand_src = ast.parse((REIMAN / "the_resolver_with_nand_alone.py").read_text(encoding="utf-8"))
nand_fn = next(n for n in nand_src.body if isinstance(n, ast.FunctionDef) and n.name == "a_cell")
others = [n for n in ast.walk(nand_fn) if isinstance(n, (ast.If, ast.IfExp, ast.BoolOp, ast.Compare, ast.BinOp)) or (isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.Not))]
all_or_none("the cell by nand alone has no and, no or, no not, no if and no comparing, by its own syntax", [("a_cell", 0, len(others))])

# ---- 2. a name's observed list: four states, three sides of a value, twelve steps, in both codes
STATES = {"none": [], "+": [1], "-": [-1], "both": [1, -1]}
def state_of(the_cell, observed):
    giving, _ = the_cell([], [(S, v) for v in observed])
    return {(): "none", ((S, 1),): "+", ((S, -1),): "-", ((S, 0),): "both"}[tuple(giving)]
STEP = {("none", 1): "+", ("none", -1): "-", ("none", 0): "none", ("+", 1): "+", ("+", -1): "both", ("+", 0): "+",
        ("-", 1): "both", ("-", -1): "-", ("-", 0): "-", ("both", 1): "both", ("both", -1): "both", ("both", 0): "both"}
all_or_none("a state with one value more, its twelve steps, living and by nand",
            [((s, v), state_of(living_cell, STATES[s] + [v]), state_of(nand_cell, STATES[s] + [v])) for s in STATES for v in (1, -1, 0)])
all_or_none("the twelve steps are the table's: a + among them, a − among them, both or none",
            [((s, v), STEP[(s, v)], state_of(living_cell, STATES[s] + [v])) for s in STATES for v in (1, -1, 0)])
all_or_none("two values in either order come to one state, with all states",
            [((s, x, y), state_of(living_cell, STATES[s] + [x, y]), state_of(living_cell, STATES[s] + [y, x])) for s in STATES for x in (1, -1, 0) for y in (1, -1, 0)])

# ---- 3. the cell: three priors with four states, twelve cases, all of a cell
PRIORS = {"none": [], "+": [(S, 1)], "-": [(S, -1)]}
all_or_none("a prior with a state, the twelve cases of a cell: its giving and its next prior",
            [((p, s), said(living_cell(PRIORS[p], [(S, v) for v in STATES[s]])), said(nand_cell(PRIORS[p], [(S, v) for v in STATES[s]]))) for p in PRIORS for s in STATES])
lists = [list(l) for n in range(0, 7) for l in itertools.product((1, -1, 0), repeat=n)]
all_or_none("beside it, all lists of none to six observed, with all three priors",
            [((p, tuple(l)), said(living_cell(PRIORS[p], [(S, v) for v in l])), said(nand_cell(PRIORS[p], [(S, v) for v in l]))) for p in PRIORS for l in lists])

# ---- 4. a name by itself: a second name beside it moves nothing of it
A, B = "a name", "an other name"
def of_a_name(answer, name):
    giving, next_prior = answer
    return tuple(v for k, v in giving if k == name), tuple(v for k, v in next_prior if k == name)
cases = [(p, s) for p in ("none", 1, -1) for s in STATES]
all_or_none("a name is resolved by itself, a second name beside it, in the living cell",
            [((pa, sa, pb, sb),
              of_a_name(living_cell([(A, pa)] if pa != "none" else [], [(A, v) for v in STATES[sa]]), A),
              of_a_name(living_cell(([(A, pa)] if pa != "none" else []) + ([(B, pb)] if pb != "none" else []), [(B, v) for v in STATES[sb]] + [(A, v) for v in STATES[sa]]), A))
             for pa, sa in cases for pb, sb in cases])

# ---- 5. a moment of a society: the living code's own lines of 17, the cell alone swapped
def frozen(society):
    return tuple((s, tuple(sorted(p, key=str)), tuple(sorted(o, key=str))) for s, (p, o) in sorted(society.items(), key=str))
by_nand = dict(living); exec(compile(code, str(page), "exec"), by_nand); by_nand["_1_now_existing"] = nand_cell
def societies():
    for n, names in ((1, (6, 9, 10)), (2, (6, 9, 10)), (3, (9, 10))):
        selves = list(range(n))
        keys = [(s, k) for s in selves for k in names]
        for to in itertools.product([None] + selves, repeat=len(keys)):
            couplings = {k: r for k, r in zip(keys, to) if r is not None}
            for priors in itertools.product((None, 1, -1), repeat=n):
                yield n, couplings, {s: ([(S, priors[s])] if priors[s] else [], []) for s in selves}
made_a_prior_0 = 0
def same_moments():
    global made_a_prior_0
    for n, couplings, opening in societies():
        a, b, parted = opening, opening, None
        for t in range(1, 13):
            a, b = living["_17_next_existing"](a, couplings), by_nand["_17_next_existing"](b, couplings)
            made_a_prior_0 += sum(1 for s in a for k, v in a[s][0] if v == 0)
            if frozen(a) != frozen(b):
                parted = t; break
        yield (n, tuple(sorted(couplings.items())), frozen(opening)), None, parted
all_or_none("societies of one to three selves, all their couplings and all their openings, twelve moments, the cell alone swapped", same_moments())
all_or_none("no line of the living code makes a prior 0, in all those moments", [("a prior 0 made", 0, made_a_prior_0)])

# ---- 6. the two places a call can supply and no line of the code makes
print("\nThe partings, a call's alone:")
print("   a prior 0 supplied: the living cell has it as a -, by its side of 0, and the cell by nand as no prior")
for state, observed in STATES.items():
    given = [(S, v) for v in observed]
    print(f"      {state:4} observed | living: {said(living_cell([(S, 0)], given))} | as a prior -: {said(living_cell([(S, -1)], given))} | by nand: {said(nand_cell([(S, 0)], given))}")
print("   a prior 2 supplied, a + observed | living:", said(living_cell([(S, 2)], [(S, 1)])), "| by nand: a 2 is no + and no -, and no line of the cell is of it")
all_is = all(parting == 0 for _, _, parting in results)
print(f"\n{len(results)} goings through, {sum(n for _, n, _ in results)} things gone through")
print("All is" if all_is else "NOT ALL")
