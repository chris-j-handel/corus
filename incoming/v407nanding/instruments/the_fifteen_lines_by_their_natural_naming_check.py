"""v407nanding · the fifteen lines by their natural naming, Exhibit ONE's own names, with no giving.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/the_fifteen_lines_by_their_natural_naming_check.py .

A partner's word of 24 November: giving is-not, as v406geodesic2 found with its drafts 25 to 30. NATURAL_CODE is
v406Reiman's fifteen lines with all their places named by Exhibit ONE Natural Resolver's living code, name 1's own
lines: the fifteen lines are 1-now-existing for one name. No line's logic is altered. All or none.
"""
import ast
import importlib.util
import itertools
import re
import sys
from pathlib import Path

NATURAL_CODE = '''
NAND = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def nand(a, b):
    return NAND[(a, b)]


def other_than(a):
    return nand(a, a)


def both(a, b):
    once = nand(a, b)
    return nand(once, once)


def either(a, b):
    return nand(nand(a, a), nand(b, b))


def now_existing(now_co_observing, now_possibling):
    next_observing_plus = next_observing_minus = False
    for now_observing_plus, now_observing_minus in now_possibling:
        next_observing_plus = either(next_observing_plus, now_observing_plus)
        next_observing_minus = either(next_observing_minus, now_observing_minus)
    next_possibling_plus = both(next_observing_plus, other_than(next_observing_minus))
    next_possibling_minus = both(next_observing_minus, other_than(next_observing_plus))
    now_co_observing_plus, now_co_observing_minus = now_co_observing
    no_now_co_observing = both(other_than(now_co_observing_plus), other_than(now_co_observing_minus))
    next_co_same_existing_plus = either(both(no_now_co_observing, next_possibling_plus),
                                        both(now_co_observing_minus, other_than(next_possibling_minus)))
    next_co_same_existing_minus = either(both(no_now_co_observing, next_possibling_minus),
                                         both(now_co_observing_plus, other_than(next_possibling_plus)))
    next_co_observing_plus = either(next_co_same_existing_plus, both(now_co_observing_plus, next_possibling_plus))
    next_co_observing_minus = either(next_co_same_existing_minus, both(now_co_observing_minus, next_possibling_minus))
    is_next_co_possibling = either(other_than(no_now_co_observing), either(next_observing_plus, next_observing_minus))
    is_next_co_observing = either(next_co_observing_plus, next_co_observing_minus)
    return ((next_co_same_existing_plus, next_co_same_existing_minus), (next_co_observing_plus, next_co_observing_minus),
            is_next_co_possibling, is_next_co_observing)
'''

root = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone",
                                              root / "incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py")
reiman = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reiman)
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


ns = {}
exec(NATURAL_CODE, ns)
now_existing = ns["now_existing"]
FOUR = ((True, False), (False, True), (False, False), (True, True))
THREE = FOUR[:3]


def lists(values, most):
    for k in range(most + 1):
        yield from itertools.product(values, repeat=k)


CASES = [(p, list(o)) for p in FOUR for o in lists(THREE, 4)] + [(p, list(o)) for p in FOUR for o in lists(FOUR, 3)]
say("L1. The fifteen lines by their natural naming are v406Reiman's fifteen lines, case with case: four priors, none to "
    "four others, and none to three with the vault among them",
    all(now_existing(p, o) == reiman.a_cell(p, o) for p, o in CASES))

tree = ast.parse(NATURAL_CODE)
fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "now_existing")
lines = [s for s in fn.body if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant))]
statements = sum(1 for s in ast.walk(fn) if isinstance(s, (ast.Assign, ast.For, ast.Return)))
say("L2. They are fifteen lines of code, written in eighteen rows for their width, and they call nand alone",
    statements == 15 and lines[-1].end_lineno - lines[0].lineno + 1 == 18 and not any(isinstance(n, (ast.BoolOp, ast.Not, ast.Compare, ast.If, ast.IfExp, ast.BinOp)) for n in ast.walk(fn)))

living = open(root / "Exhibit_ONE_Natural_Resolver_v402mgr.md", encoding="utf-8").read()
code = "\n".join(re.findall(r"```python\n(.*?)```", living, re.S))
names = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name)} | {a.arg for a in fn.args.args} | {fn.name}
logic = {"either", "both", "other_than"}
bases = {re.sub(r"_(plus|minus)$", "", re.sub(r"^(is_|no_)", "", n)) for n in names - logic}
say("L3. Its names are the living code's own: now-existing, now-co-observing, now-possibling, now-observing, next-observing, "
    "next-possibling, next-co-same-existing, next-co-observing and next-co-possibling, all in Exhibit ONE's code",
    all(re.search(rf"\b_\d+_{b}\b", code) for b in bases) and len(bases) == 9)
say("L4. No name of the lines is a giving", not any("giv" in n for n in names))

artboards = root / "incoming/v406geodesic2/illustrations/artboards"
givings = {k: len(re.findall(r"giv", re.sub(r"<[^>]+>", " ", (artboards / f"Draft{k}.dc.html").read_text(encoding="utf-8")), re.I))
           for k in range(25, 31)}
say("L5. v406geodesic2's drafts 25 to 27 say giving, and its drafts 28 to 30 say none",
    all(givings[k] > 0 for k in (25, 26, 27)) and all(givings[k] == 0 for k in (28, 29, 30)))
say("L6. Draft 25 has the four by the living code's numbers, 3 and 2 given, to 11 and 10",
    "the living code's 3 and 2, to 11 and 10" in re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", (artboards / "Draft25.dc.html").read_text(encoding="utf-8"))))

import io
import tokenize
comments = [k for k in tokenize.generate_tokens(io.StringIO(NATURAL_CODE).readline) if k.type == tokenize.COMMENT]
docstrings = [n for n in ast.walk(tree) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant)]
say("L7. The code carries no story: no docstring and no comment in its lines", not comments and not docstrings)

broken = {}
exec(NATURAL_CODE.replace("next_observing_plus = either(next_observing_plus, now_observing_plus)",
                          "next_observing_plus = both(next_observing_plus, now_observing_plus)"), broken)
say("M1. With line 3 saying both in the place of either, L1 says is-not",
    not all(broken["now_existing"](p, o) == reiman.a_cell(p, o) for p, o in CASES))

print("\nAll is." if all(results) else "\nNot all is.")
