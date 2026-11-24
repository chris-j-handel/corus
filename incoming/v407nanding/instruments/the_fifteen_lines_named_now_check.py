"""v407nanding · the fifteen lines named now, executed beside the fifteen lines as they are.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/the_fifteen_lines_named_now_check.py .

A partner's asking of 24 November: the nand code with the best replacement for cell in its opening line, and the
universality in the parities traveling through same-existing now. NOW_CODE is v406Reiman's fifteen lines with five names
said again: a_cell as now, a_plus and a_minus as others_plus and others_minus, gives as giving, a_giving as is_giving and
a_next as is_next. No line's logic is altered. v406Reiman's lines are opened from their own file, and its society of
cells from its own file. All or none: with one line not is, the check is not.
"""
import ast
import importlib.util
import itertools
import sys
from pathlib import Path

NOW_CODE = '''
NAND = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def nand(a, b):
    """Not both: is-not with both alone, and is with all else."""
    return NAND[(a, b)]


def other_than(a):
    """One nand: a thing with itself."""
    return nand(a, a)


def both(a, b):
    """Two nands in a row."""
    once = nand(a, b)
    return nand(once, once)


def either(a, b):
    """A nand of two other-thans."""
    return nand(nand(a, a), nand(b, b))


def now(prior, observing):
    """A me-parity's now: its prior and what it observes, to its giving and its next prior, by nand alone."""
    others_plus = others_minus = False                     # 14 next-possibling, opening with none
    for plus, minus in observing:                          # 2 now-possibling, with 4 and 7
        others_plus = either(others_plus, plus)            # 15 next-observing
        others_minus = either(others_minus, minus)         # 15 next-observing
    surfacing_plus = both(others_plus, other_than(others_minus))      # 14 next-possibling
    surfacing_minus = both(others_minus, other_than(others_plus))     # 14 next-possibling
    prior_plus, prior_minus = prior                        # 3 now-co-observing
    no_prior = both(other_than(prior_plus), other_than(prior_minus))  # 12 next-co-same-existing, opening as 14
    giving_plus = either(both(no_prior, surfacing_plus), both(prior_minus, other_than(surfacing_minus)))   # 12 with 4
    giving_minus = either(both(no_prior, surfacing_minus), both(prior_plus, other_than(surfacing_plus)))   # 12 with 4
    next_plus = either(giving_plus, both(prior_plus, surfacing_plus))      # 11 next-co-observing, and 8
    next_minus = either(giving_minus, both(prior_minus, surfacing_minus))  # 11 next-co-observing, and 8
    is_giving = either(other_than(no_prior), either(others_plus, others_minus))  # 10 next-co-possibling, across with 6 and along with 9
    is_next = either(next_plus, next_minus)                # 11 to 3
    return (giving_plus, giving_minus), (next_plus, next_minus), is_giving, is_next  # 10 and 11 to 17, a 1 again
'''

root = Path(sys.argv[1])
here = root / "incoming/v406Reiman/instruments"


def opened(name):
    spec = importlib.util.spec_from_file_location(name, here / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


reiman = opened("the_resolver_with_nand_alone")
passes = opened("passes_about_verifying_with_nand")
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def lines_with(nand=None, text=NOW_CODE):
    ns = {}
    exec(text, ns)
    if nand is not None:
        ns["nand"] = nand
    return ns


ns = lines_with()
now, nand = ns["now"], ns["nand"]
PLUS, MINUS, NEITHER, VAULT = (True, False), (False, True), (False, False), (True, True)
THREE, FOUR = (PLUS, MINUS, NEITHER), (PLUS, MINUS, NEITHER, VAULT)


def lists(values, most):
    for k in range(most + 1):
        yield from itertools.product(values, repeat=k)


CASES = [(p, list(o)) for p in FOUR for o in lists(THREE, 4)] + [(p, list(o)) for p in FOUR for o in lists(FOUR, 3)]
SMALL = [(p, list(o)) for p in FOUR for o in lists(THREE, 2)]

print("N · The fifteen lines named now")
say("N1. The lines named now are v406Reiman's fifteen lines: the same giving, next prior and two is-or-is-nots of laying, "
    "four priors, none to four others, and none to three with the vault among them",
    all(now(p, o) == reiman.a_cell(p, o) for p, o in CASES))
tree = ast.parse(NOW_CODE)
defs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
tests = (ast.BoolOp, ast.Not, ast.Compare, ast.If, ast.IfExp, ast.BinOp, ast.While, ast.Global, ast.Nonlocal, ast.Attribute)
alone = all(not any(isinstance(n, tests) for n in ast.walk(defs[k])) for k in ("now", "other_than", "both", "either"))
alone = alone and all({c.func.id for c in ast.walk(defs[k]) if isinstance(c, ast.Call)} <= {"nand", "other_than", "both", "either"}
                      for k in ("now", "other_than", "both", "either"))
body = [s for s in defs["now"].body if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant))]
say("N2. Now is fifteen lines, and now and its three call nand alone: no and, or, not, if, comparing, global or kept place",
    alone and sum(s.end_lineno - s.lineno + 1 for s in body) == 15)


def two_nows(cell):
    def made(x, y):
        front = cell(MINUS, [(False, y)])[0][0]
        return cell(MINUS, [(front, x)])[0][0]
    return made


say("N3. Two nows front to back, the back now observing one place more, are a nand",
    all(two_nows(now)(x, y) == nand(x, y) for x in (True, False) for y in (True, False)))
one = lines_with(two_nows(now))
two = lines_with(two_nows(one["now"]))
say("N4. The lines with all their nands two nows are the same lines, and once more with nands of nows of nows: "
    "a now is nands, a nand is two nows, and by N2 and N3 the same at all scales",
    all(one["now"](p, o) == now(p, o) for p, o in CASES[:400]) and all(two["now"](p, o) == now(p, o) for p, o in SMALL[:20]))


def society_nand(x, y):
    return passes.by_cells(reiman.step_with_nand, [(True, True)], (x, y))


society = lines_with(society_nand)
say("N5. A nand is a society of mes, three mes stepped two moments by name 17's lines, v406Reiman's own; and the lines "
    "with all their nands societies of mes are the same lines: all mes are in a now, and a now is in all mes",
    all(society_nand(x, y) == nand(x, y) for x in (True, False) for y in (True, False))
    and all(society["now"](p, o) == now(p, o) for p, o in SMALL))
travels = all(now(p, o) == now(p, o) for p, o in CASES)
travels = travels and all((now(p, o)[1] == p) == (now(NEITHER, o)[1] == p) for p in (PLUS, MINUS) for o in lists(THREE, 4))
travels = travels and all(now(p, o)[1] in (p, (p[1], p[0])) for p in (PLUS, MINUS) for o in lists(THREE, 4))
say("N6. A parity goes through the now: the now has no parity of its own between moments, the same prior and "
    "observing giving the same moment; a prior goes on through it as it is at its same-existing alone, what surfaces the "
    "same as the prior, and inverts at all else", alone and travels)


def by_names(prior_list, observing_list):
    names = list(dict.fromkeys([k for k, v in observing_list] + [k for k, v in prior_list]))
    priors, giving, nexts = dict(prior_list), [], []
    for name in names:
        g, n, is_g, is_n = now(reiman.TWO[priors.get(name, 0)], [reiman.TWO[v] for k, v in observing_list if k == name])
        giving += [(name, reiman.ONE[g])] if is_g else []
        nexts += [(name, reiman.ONE[n])] if is_n else []
    return giving, nexts


VALUES = (1, -1, 0)
mes = [(list(zip(("S", "T"), ps)), list(o)) for ps in itertools.product(VALUES, repeat=2)
       for o in lists([(k, v) for k in ("S", "T") for v in VALUES], 2)]
say("N7. Name 1's lines, a me-now, call the now once a name: a me-now is the set of its me-parities' nows; two names, "
    "all priors, and none to two observed", all(reiman.now_with_nand(p, o) == by_names(p, o) for p, o in mes))

print("\nM · Broken on purpose")
broken = lines_with(text=NOW_CODE.replace("others_plus = either(others_plus, plus)", "others_plus = both(others_plus, plus)"))
say("M1. With now's line 3 saying both in the place of either, N1 says is-not",
    not all(broken["now"](p, o) == reiman.a_cell(p, o) for p, o in CASES))
kept = NOW_CODE.replace('    others_plus = others_minus = False',
                        '    global KEPT\n    KEPT = prior\n    others_plus = others_minus = False')
kept_tree = ast.parse(kept)
kept_now = next(n for n in kept_tree.body if isinstance(n, ast.FunctionDef) and n.name == "now")
say("M2. With a parity of the now's own between moments, N6 says is-not",
    any(isinstance(n, tests) for n in ast.walk(kept_now)))

print("\nAll is." if all(results) else "\nNot all is.")
