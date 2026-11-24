"""A me's next, what surfaces to it or the other-than of its now: two lines executed beside the cell and the living code (session v406geodesic2).

Going on from a partner's sentence of 24 November, next is other-than now, and from the lean line's two is-nots yet open,
a none in the path and a me observing two. The two lines, a relation a line:

    A me's next is the parity surfacing to it; with none surfacing, its next is the other-than of its now.
    A me lays its next, with its next other-than its now.

A none's other-than is a none, a crossing of two wires. Executed here, all or none:
  1  by nand, two wires, case with case with v406Reiman's fifteen lines;      2  their nands numbered;
  3  with both wires, v407nanding's vault: its is-not;                         4  societies, by Exhibit ONE's own code;
  5  with none surfacing and a now as it is: its is-not;                       6  a birth, and a me with a prior.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_a_mes_next_what_surfaces_to_it_or_the_other-than_of_its_now.py incoming/v406Reiman/instruments/resolver_as_it_is.py . incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import importlib.util, sys
from itertools import product
sys.dont_write_bytecode = True
NANDS = [0]


class Numbered(dict):
    def __getitem__(self, k):
        NANDS[0] += 1
        return dict.__getitem__(self, k)


def opened(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def the_two_lines_by_nand(its, now, observed):
    """A me's laying and its next, a parity two wires: the surfacing, or with none surfacing its now crossed; laid with its next other-than its now."""
    a_plus = a_minus = False
    for plus, minus in observed: a_plus, a_minus = its.either(a_plus, plus), its.either(a_minus, minus)
    surfacing_plus, surfacing_minus = its.both(a_plus, its.other_than(a_minus)), its.both(a_minus, its.other_than(a_plus))
    none = its.other_than(its.either(surfacing_plus, surfacing_minus))
    its_next = (its.either(surfacing_plus, its.both(none, now[1])), its.either(surfacing_minus, its.both(none, now[0])))
    laid = (its.both(its_next[0], its.other_than(now[0])), its.both(its_next[1], its.other_than(now[1])))
    return laid, its_next


def by_the_two_lines(couplings, nows, moments, with_none=lambda now: -now):
    """A society by the two lines, a parity a +1, a −1 or a 0: a me's nows, moment by moment."""
    backs = {k: [giver for (giver, _), k2 in couplings.items() if k2 == k] for k in nows}
    now, laid, rows = dict(nows), {k: 0 for k in nows}, []
    for _ in range(moments):
        rows.append(dict(now)); its_next = {}
        for k in now:
            observed = {laid[b] for b in backs[k]} - {0}
            surfacing = observed.pop() if len(observed) == 1 else 0
            its_next[k] = surfacing if surfacing else with_none(now[k])
        laid = {k: its_next[k] if its_next[k] != now[k] else 0 for k in now}; now = its_next
    return rows


def by_the_living_code(it, step, couplings, priors, moments):
    society, rows = {k: ([(it.S, p)] if p else [], []) for k, p in priors.items()}, []
    for _ in range(moments):
        rows.append({k: dict(v[0]).get(it.S, 0) for k, v in society.items()}); society = step(society, couplings)
    return rows


def the_societies(it):
    """The societies gone through: a name, its couplings, its mes, the parities of an opening, its moments."""
    for n in range(1, 11): yield "paths closing, all with priors", it.spiral_couplings(n), list(range(n)), (1, -1), 4 * n + 8
    for n in range(2, 6): yield "paths closing, with newborns", it.spiral_couplings(n), list(range(n)), (1, -1, 0), 8 * n + 12
    for n in range(2, 8): yield "paths with an end me, all with priors", {(i, 9): i + 1 for i in range(n - 1)}, list(range(n)), (1, -1), 4 * n + 8
    for n in range(2, 5): yield "paths with an end me, with newborns", {(i, 9): i + 1 for i in range(n - 1)}, list(range(n)), (1, -1, 0), 8 * n + 12
    for p, q, parities in ((2, 2, (1, -1, 0)), (2, 3, (1, -1, 0)), (3, 3, (1, -1))):
        yield "tori", it.torus_couplings(p, q), [(a, b) for a in range(p) for b in range(q)], parities, 6 * max(p, q) + 14


if __name__ == "__main__":
    it = opened(sys.argv[1], "the_code_as_it_is")
    names, _ = it.resolver(sys.argv[2]); step = names["_17_next_existing"]
    its = opened(sys.argv[3], "the_resolver_with_nand_alone"); its.NAND = Numbered(its.NAND)
    TWO = its.TWO
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    def numbered(what): NANDS[0] = 0; what(); return NANDS[0]

    three, both_wires = [TWO[1], TWO[-1], TWO[0]], (True, True)
    cases = lambda states: [(now, list(observed)) for now in states for k in range(3) for observed in product(states, repeat=k)]
    the_same = lambda now, observed: tuple(its.a_cell(now, observed))[:2] == the_two_lines_by_nand(its, now, observed)
    line("By nand, a parity two wires, the two lines are the laying and the next of v406Reiman's fifteen lines, case with case: a now of the three, a +, a − and a none, with none, one and two observed of the three, all 39 cases",
         len(cases(three)) == 39 and all(the_same(now, observed) for now, observed in cases(three)))
    line("Their nands: 26 with none observed, 32 with one and 38 with two, for the fifteen lines' 46, 52 and 58",
         [numbered(lambda k=k: the_two_lines_by_nand(its, TWO[1], [TWO[-1]] * k)) for k in range(3)] == [26, 32, 38]
         and [numbered(lambda k=k: its.a_cell(TWO[1], [TWO[-1]] * k)) for k in range(3)] == [46, 52, 58])
    with_a_vault = [(now, observed) for now, observed in cases(three + [both_wires]) if both_wires in [now] + observed]
    line("With both wires, v407nanding's vault, as a now or observed, the two lines part from the fifteen lines with 21 of 45 cases: both wires are none of the three parities",
         len(with_a_vault) == 45 and sum(1 for now, observed in with_a_vault if not the_same(now, observed)) == 21)

    numbers, apart, as_it_is = {}, 0, 0
    for name_, couplings, mes, parities, moments in the_societies(it):
        for opening in product(parities, repeat=len(mes)):
            nows = dict(zip(mes, opening)); numbers[name_] = numbers.get(name_, 0) + 1
            living = by_the_living_code(it, step, couplings, nows, moments)
            apart += living != by_the_two_lines(couplings, nows, moments)
            if name_ == "paths closing, all with priors": as_it_is += living == by_the_two_lines(couplings, nows, moments, with_none=lambda now: now)
    line("Societies, by Exhibit ONE's own code: the two lines' moments are the living code's at all moments with all 4,097 openings gone through: paths closing, 2,046 all with priors and 360 with newborns; paths with an end me, 252 and 117; and tori of 2 by 2, 2 by 3 and 3 by 3, 1,322",
         apart == 0 and list(numbers.values()) == [2046, 360, 252, 117, 1322] and sum(numbers.values()) == 4097)
    line("With none surfacing and a me's next its now as it is, with no other-than, the moments are the living code's with none of the 2,046 openings of paths closing: a partner's sentence, next is other-than now, is the line's own",
         as_it_is == 0)

    line("A birth: a me with no prior has the parity surfacing to it as its next, as it is, and lays it; with none surfacing it is a none again and lays none. A me with a prior has its prior again and lays none with its prior surfacing, and its other-than, laid, at all else",
         all(the_two_lines_by_nand(its, TWO[0], [TWO[s]]) == (TWO[s], TWO[s]) for s in (1, -1, 0))
         and all(the_two_lines_by_nand(its, TWO[p], [TWO[s]]) == ((TWO[0], TWO[p]) if s == p else (TWO[-p], TWO[-p])) for p in (1, -1) for s in (1, -1, 0))
         and all(the_two_lines_by_nand(its, TWO[p], [TWO[1], TWO[-1]])[1] == TWO[-p] for p in (1, -1, 0)))

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
