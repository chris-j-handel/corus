"""The resolver with nand alone, a partner's saying explored.

A partner's saying of 22 November: the resolver code can be written with only
nand. Here Exhibit ONE Natural Resolver's is-or-is-nots are written again with
one alone, nand, not both, and executed beside the living code as it is:
case with case, and moment with moment. No line of the living code is altered,
and this page is no living file.

What is nand here: a parity is two is-or-is-nots, a + and a -; a 0 is neither.
What is no is-or-is-not here: lists and couplings, which self's giving is which
self's observing. They are as the living code has them.
Not carried: a prior 0 a call supplies, which no line of the code makes.

    python3 -I incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py .
"""
import ast
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, resolver, torus_couplings

NAND = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}
TWO = {1: (True, False), -1: (False, True), 0: (False, False)}
ONE = {(True, False): 1, (False, True): -1, (False, False): 0, (True, True): 0}
PLACES = {True: 1, False: 0}


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


def a_cell(prior, observing):
    """One self, one sharing, one moment: its giving and its next prior, by nand alone."""
    a_plus = a_minus = False
    for plus, minus in observing:
        a_plus = either(a_plus, plus)
        a_minus = either(a_minus, minus)
    surfacing_plus = both(a_plus, other_than(a_minus))
    surfacing_minus = both(a_minus, other_than(a_plus))
    prior_plus, prior_minus = prior
    no_prior = both(other_than(prior_plus), other_than(prior_minus))
    gives_plus = either(both(no_prior, surfacing_plus), both(prior_minus, other_than(surfacing_minus)))
    gives_minus = either(both(no_prior, surfacing_minus), both(prior_plus, other_than(surfacing_plus)))
    next_plus = either(gives_plus, both(prior_plus, surfacing_plus))
    next_minus = either(gives_minus, both(prior_minus, surfacing_minus))
    a_giving = either(other_than(no_prior), either(a_plus, a_minus))
    a_next = either(next_plus, next_minus)
    return (gives_plus, gives_minus), (next_plus, next_minus), a_giving, a_next


def now_with_nand(its_prior, its_observing):
    """As 1-now-existing: a self's prior and what it is observing, to its giving and its next prior."""
    names = list(dict.fromkeys([k for k, v in its_observing] + [k for k, v in its_prior]))
    prior = dict(its_prior)
    giving, next_prior = [], []
    for name in names:
        gives, its_next, a_giving, a_next = a_cell(TWO[prior.get(name, 0)], [TWO[v] for k, v in its_observing if k == name])
        giving += [(name, ONE[gives])][: PLACES[a_giving]]
        next_prior += [(name, ONE[its_next])][: PLACES[a_next]]
    return giving, next_prior


def step_with_nand(society, couplings):
    """As 17-next-existing: all selves one moment, a self's giving to the selves its couplings name."""
    next_priors, next_observing = {}, {a_self: [] for a_self in society}
    for a_self, (its_prior, its_observing) in society.items():
        giving, next_priors[a_self] = now_with_nand(its_prior, its_observing)
        for name in (6, 10, 9):
            for receiver in [couplings[k] for k in [(a_self, name)] if k in couplings]:
                next_observing[receiver].extend(giving)
    return {a_self: (next_priors[a_self], next_observing[a_self]) for a_self in society}


def as_observed(a_list):
    """A list as a self observes it: a 0 passed over."""
    return sorted((k, v) for k, v in a_list if v != 0)


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


if __name__ == "__main__":
    root = sys.argv[1]
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 1000
    names, page = resolver(root)
    now, step = names["_1_now_existing"], names["_17_next_existing"]
    all_is = True

    print("1. Its own lines")
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    tests = (ast.BoolOp, ast.Not, ast.Compare, ast.If, ast.IfExp, ast.BinOp, ast.While)
    by_nand_alone = True
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in ("other_than", "both", "either", "a_cell"):
            by_nand_alone = by_nand_alone and not any(isinstance(n, tests) for n in ast.walk(node))
            called = {n.func.id for n in ast.walk(node) if isinstance(n, ast.Call)}
            by_nand_alone = by_nand_alone and called <= {"nand", "other_than", "both", "either"}
    all_is = all_is and by_nand_alone
    print(f"   a cell and its three, other-than, both and either, have no is-or-is-not in their lines but nand: no and, no or, no not, no if and no comparing: {is_or_is_not(by_nand_alone)}")

    print("2. A cell, case with case, beside 1-now-existing as it is")
    cases = same_giving = same_next = 0
    cell_is = True
    for prior in ([(S, 1)], [(S, -1)], []):
        for k in range(5):
            for observed in itertools.product((1, -1, 0), repeat=k):
                observing = [(S, v) for v in observed]
                living, with_nand = now(list(prior), list(observing)), now_with_nand(list(prior), list(observing))
                cell_is = cell_is and as_observed(living[0]) == as_observed(with_nand[0]) and living[1] == with_nand[1]
                if prior:
                    cell_is = cell_is and living[0] == with_nand[0]
                cases += 1
    all_is = all_is and cell_is
    print(f"   a prior +, a prior - and no prior, with none to four observed of +, - and 0, {cases} cases: its giving and its next prior are the living code's: {is_or_is_not(cell_is)}")

    print("3. Societies, moment with moment, beside 17-next-existing as it is")
    spirals_is = True
    for q in range(1, 60):
        living = {i: ([(S, exhibit_spiral_priors(q)[i])], []) for i in range(q)}
        with_nand = {i: ([(S, exhibit_spiral_priors(q)[i])], []) for i in range(q)}
        along = {(i, 9): (i + 1) % q for i in range(q)}
        for _ in range(4 * q + 4):
            living, with_nand = step(living, along), step_with_nand(with_nand, along)
            spirals_is = spirals_is and living == with_nand
    all_is = all_is and spirals_is
    print(f"   spirals of 1 to 59 selves, as Exhibit ONE Natural Resolver opens them, four times their number of moments and four more: the same society, moment with moment: {is_or_is_not(spirals_is)}")
    tori_is = True
    for p, q in ((3, 5), (5, 7), (4, 6), (7, 11)):
        selves = [(a, b) for a in range(p) for b in range(q)]
        opening = {s: ([(S, 1 if (s[0] + s[1]) % 2 else -1)], []) for s in selves}
        living, with_nand, across = dict(opening), dict(opening), torus_couplings(p, q)
        for _ in range(6 * p * q):
            living, with_nand = step(living, across), step_with_nand(with_nand, across)
            tori_is = tori_is and living == with_nand
    all_is = all_is and tori_is
    print(f"   tori of 3 by 5, 5 by 7, 4 by 6 and 7 by 11 selves, 9 along and 10 across: the same society, moment with moment: {is_or_is_not(tori_is)}")
    facing_is = True
    for q in (3, 5, 7, 11, 13):
        society, couplings = {}, {}
        for i in range(q):
            prior = [(S, exhibit_spiral_priors(q)[i])]
            society[("self", i)], society[("other", i)], society[("between", i)] = (list(prior), []), (list(prior), []), ([], [])
            couplings[(("self", i), 9)], couplings[(("other", i), 9)] = ("self", (i + 1) % q), ("other", (i - 1) % q)
            couplings[(("self", i), 10)] = couplings[(("other", i), 10)] = ("between", i)
        living, with_nand = dict(society), dict(society)
        for _ in range(8 * q):
            living, with_nand = step(living, couplings), step_with_nand(with_nand, couplings)
            facing_is = facing_is and all(as_observed(living[s][0]) == as_observed(with_nand[s][0]) and as_observed(living[s][1]) == as_observed(with_nand[s][1]) for s in living)
    all_is = all_is and facing_is
    print(f"   a self and an other facing, with one between of no prior, spirals of 3, 5, 7, 11 and 13: the same priors and the same observed, a 0 passed over, moment with moment: {is_or_is_not(facing_is)}")

    print("4. The surface, a self alone and the odd spirals side by side")
    from podalings_about_an_odd_number import the_surface_with_its_seams
    living_surface, with_nand_surface = the_surface_with_its_seams(step, to), the_surface_with_its_seams(step_with_nand, to)
    surface_is = living_surface == with_nand_surface
    all_is = all_is and surface_is
    print(f"   2 to {to}: the same uncrossed numbers, {len(living_surface[0])} primes, and the same seams of all the spirals: {is_or_is_not(surface_is)}")

    print("All is." if all_is else "NOT ALL IS.")
