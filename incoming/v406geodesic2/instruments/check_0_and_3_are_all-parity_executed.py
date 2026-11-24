"""0 and 3 are all-parity: a partner's sentences executed, their is and their is-not (session v406geodesic2).

A partner's sentences of 24 November, re-said a relation a sentence:
    0 and 3 are all-parity.    Inward of the inward surface and outward of the outward surface are the same.
    Both are all-parity at a birth and at all living nows.    The word for a 0 said before is dissolving from natural naming.

A parity is two wires, a + wire and a − wire: 0 is neither wire, 1 a +, 2 a −, and 3 both wires. Executed here, all or
none, beside v406Reiman's fifteen lines, this session's two lines, and Exhibit ONE Natural Resolver's own code:
  1  as a now, by the fifteen lines;                          2  observed alone;
  3  on a path, by the fifteen lines;                         4  observed with a parity: its is-not;
  5  on a surface, by the fifteen lines: its is-not;          6  this session's two lines of the 34th drawing: their is-not;
  7  a parity's own surfacing: resolved forward;              8  the living code, a prior of 0 a call supplies.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_0_and_3_are_all-parity_executed.py incoming/v406Reiman/instruments/resolver_as_it_is.py . incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import importlib.util, os, sys
from itertools import product
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("a_mes_next", os.path.join(HERE, "check_a_mes_next_what_surfaces_to_it_or_the_other-than_of_its_now.py"))
lines = importlib.util.module_from_spec(spec); spec.loader.exec_module(lines)


def its_own_surfacing(its, wires):
    """A pair of wires surfaces a + with its + wire alone and a − with its − wire alone; with both wires or neither, all-parity."""
    return its.both(wires[0], its.other_than(wires[1])), its.both(wires[1], its.other_than(wires[0]))


def the_two_lines_with_a_paritys_own_surfacing(its, now, observed):
    return lines.the_two_lines_by_nand(its, its_own_surfacing(its, now), [its_own_surfacing(its, o) for o in observed])


def a_society(cell, couplings, nows, moments):
    """A society by a cell of two wires: a me observes what the mes back of it laid a moment before; its nows, moment by moment."""
    backs = {k: [giver for (giver, _), k2 in couplings.items() if k2 == k] for k in nows}
    now, laid, rows = dict(nows), None, []
    for _ in range(moments):
        rows.append(dict(now))
        out = {k: cell(now[k], [] if laid is None else [laid[b] for b in backs[k]]) for k in now}
        laid, now = {k: tuple(out[k][0]) for k in out}, {k: tuple(out[k][1]) for k in out}
    return rows


if __name__ == "__main__":
    it = lines.opened(sys.argv[1], "the_code_as_it_is")
    names, _ = it.resolver(sys.argv[2]); step = names["_17_next_existing"]
    its = lines.opened(sys.argv[3], "the_resolver_with_nand_alone"); its.NAND = lines.Numbered(its.NAND)
    TWO = its.TWO
    PLUS, MINUS, ZERO, THREE = TWO[1], TWO[-1], TWO[0], (True, True)
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    fifteen = lambda now, observed: tuple(its.a_cell(now, list(observed)))[:2]
    two = lambda now, observed: lines.the_two_lines_by_nand(its, now, list(observed))
    own = lambda now, observed: the_two_lines_with_a_paritys_own_surfacing(its, now, list(observed))
    as_one = lambda wires: ZERO if wires == THREE else wires                      # a 3 and a 0, one all-parity
    four = [PLUS, MINUS, ZERO, THREE]
    observings = [observed for k in range(3) for observed in product(four, repeat=k)]

    line("As a now, by the fifteen lines, a 3 and a 0 are the same at a birth and at all moments, all 21 observings: with a parity surfacing a 3 and a 0 are born as it and lay it; with all-parity surfacing a 0 is a 0 again and a 3 a 3 again",
         len(observings) == 21 and all(tuple(map(as_one, fifteen(THREE, o))) == tuple(map(as_one, fifteen(ZERO, o))) for o in observings)
         and all(fifteen(n, [s]) == (s, s) for n in (ZERO, THREE) for s in (PLUS, MINUS)) and fifteen(ZERO, []) == (ZERO, ZERO) and fifteen(THREE, []) == (THREE, THREE))
    line("Observed alone, a 3 and a 0 are the same, by the fifteen lines and by the two lines: no parity surfaces, with all four nows",
         all(f(n, [THREE]) == f(n, [ZERO]) == f(n, []) for f in (fifteen, two) for n in four))

    paths = True
    for n in range(2, 6):
        couplings = it.spiral_couplings(n)
        for opening in product((PLUS, MINUS, ZERO), repeat=n):
            if ZERO in opening:
                with_0 = a_society(fifteen, couplings, dict(enumerate(opening)), 6 * n + 8)
                with_3 = a_society(fifteen, couplings, {k: THREE if w == ZERO else w for k, w in enumerate(opening)}, 6 * n + 8)
                paths = paths and [{k: as_one(w) for k, w in row.items()} for row in with_3] == with_0
    line("On a path of 2 to 5 mes closing, by the fifteen lines, a me opening as a 3 for a 0 has the same moments, with all 296 openings with an all-parity: a me observes one, and a 3 observed alone is a 0",
         paths)

    with_a_three = [(n, o) for n in four for o in observings if THREE in o]
    apart = [(n, o) for n, o in with_a_three if fifteen(n, o) != fifteen(n, [as_one(w) for w in o])]
    line("Observed with a parity, by the fifteen lines, a 3 and a 0 part: a 3 with a + surfaces all-parity, and a 0 with a + surfaces the +. It is with 12 of 32 observings with a 3",
         len(with_a_three) == 32 and len(apart) == 12 and all(len(o) == 2 and (PLUS in o) != (MINUS in o) for _, o in apart))

    torus, mes = it.torus_couplings(2, 2), [(a, b) for a in range(2) for b in range(2)]
    surfaces = {f: 0 for f in ("fifteen", "own")}; openings = 0
    for opening in product((PLUS, MINUS, ZERO), repeat=4):
        if ZERO in opening and (PLUS in opening or MINUS in opening):
            openings += 1
            for name_, f in (("fifteen", fifteen), ("own", own)):
                with_0 = a_society(f, torus, dict(zip(mes, opening)), 24)
                with_3 = a_society(f, torus, {k: THREE if w == ZERO else w for k, w in zip(mes, opening)}, 24)
                surfaces[name_] += [{k: as_one(w) for k, w in row.items()} for row in with_3] != [{k: as_one(w) for k, w in row.items()} for row in with_0]
    line("On a surface, a torus of 2 by 2, by the fifteen lines, a me opening as a 3 for a 0 has other moments with 48 of 64 openings with an all-parity and a parity: a 3 laid beside a parity laid surfaces all-parity",
         openings == 64 and surfaces["fifteen"] == 48)

    as_a_now = [o for o in observings if tuple(map(as_one, two(THREE, o))) != tuple(map(as_one, two(ZERO, o)))]
    line("This session's two lines of the 34th drawing part a 3 from a 0 as a now, with 8 of 21 observings: a 3 born with a parity lays no parity, and a 0 born with it lays it",
         len(as_a_now) == 8 and two(THREE, [PLUS]) == (ZERO, PLUS) and two(ZERO, [PLUS]) == (PLUS, PLUS))

    cases = [(n, o) for n in four for o in observings]
    three_alone = [(n, o) for n, o in cases if THREE not in [n] + list(o)]

    def numbered(what): lines.NANDS[0] = 0; what(); return lines.NANDS[0]
    line("Resolved forward, with a parity's own surfacing at a me's now and at all it observes: a 3 and a 0 are the same with all 84 cases, at a birth and at all nows; with the three, a +, a − and a 0, the two lines are the fifteen lines' still, all 39 cases; on the torus of 2 by 2 a 3 for a 0 has the same moments with all 64 openings; and it is 32 nands with no parity observed and 12 more a thing observed",
         len(cases) == 84 and all(own(n, o) == own(as_one(n), [as_one(w) for w in o]) for n, o in cases)
         and len(three_alone) == 39 and all(own(n, o) == fifteen(n, o) for n, o in three_alone) and surfaces["own"] == 0
         and [numbered(lambda k=k: own(PLUS, [MINUS] * k)) for k in range(3)] == [32, 44, 56])

    def living(society, couplings, moments):
        rows = []
        for _ in range(moments): rows.append({k: dict(v[0]).get(it.S, 0) for k, v in society.items()}); society = step(society, couplings)
        return rows
    couplings = {(0, 9): 1, (1, 9): 0}
    no_prior = [r[1] for r in living({0: ([(it.S, 1)], []), 1: ([], [])}, couplings, 6)]
    a_prior_of_0 = [r[1] for r in living({0: ([(it.S, 1)], []), 1: ([(it.S, 0)], [])}, couplings, 6)]
    line("The living code has a + and a − observed together and no parity observed as one 0. A me with no prior is born with the parity surfacing to it; a me with a prior of 0, a call's own, is a + a moment on with no parity surfacing: the two part, and v406Reiman's lines carry the one alone",
         no_prior == [0, 0, -1, 1, -1, 1] and a_prior_of_0 == [0, 1, -1, 1, -1, 1])

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
