"""The lean line rigorized, its is and its is-not: executed beside the living code's own lines (session v406geodesic2).

By a partner's word of 24 November, re-said: the nand code is being explored as one line, and this session helps rigorize.
The lean line is v407nanding's, of its page The leanest resolving, laid here as that page has it:

    def now_and_same_existing_me_parity(me_now, other_prior):
        return me_now, NOT_BOTH[(other_prior, other_prior)]

Executed here, all or none, its is and its is-not, beside Exhibit ONE Natural Resolver's own code:
  1  a path of mes closing, all with priors;                 2  its opening;
  3  one me observing itself, and two mes facing;             4  a path with an end me, none back of it;
  5  a parity of two wires, its other-than a crossing;        6  a newborn, a me opening with no prior;
  7  a surface, a me observing two;                          8  what a me's other observes, by the living code.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_lean_line_rigorized_its_is_and_its_is-not.py incoming/v406Reiman/instruments/resolver_as_it_is.py . incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import importlib.util, sys
from itertools import product
sys.dont_write_bytecode = True

LEAN = '''
NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def now_and_same_existing_me_parity(me_now, other_prior):
    return me_now, NOT_BOTH[(other_prior, other_prior)]
'''
_lean = {}; exec(LEAN, _lean)
lean_line, NOT_BOTH = _lean["now_and_same_existing_me_parity"], _lean["NOT_BOTH"]
IS = {1: True, -1: False}                                                         # a parity one is-or-is-not: a + an is, a − an is-not
PARITY = {True: 1, False: -1}


def opened(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def by_the_living_code(it, step, couplings, priors, moments):
    """A society's priors, moment by moment, by Exhibit ONE's own lines; a me with no prior is a 0."""
    society, rows = {k: ([(it.S, p)] if p else [], []) for k, p in priors.items()}, []
    for _ in range(moments):
        rows.append({k: dict(v[0]).get(it.S, 0) for k, v in society.items()}); society = step(society, couplings)
    return rows


def by_the_lean_line(opening, moments, opening_now=None):
    """A path of mes closing: a me's prior and its now, by the lean line alone; its opening now the other-than of its own prior."""
    priors = [IS[p] for p in opening]
    nows = [lean_line(None, p)[1] for p in priors] if opening_now is None else [opening_now(p) for p in priors]
    rows = []
    for _ in range(moments):
        rows.append([PARITY[p] for p in priors])
        pairs = [lean_line(nows[a], priors[a - 1]) for a in range(len(priors))]
        priors, nows = [p for p, _ in pairs], [n for _, n in pairs]
    return rows


def a_surface(it, step, p, q):
    """A torus of p by q mes, all its openings: is the lean line its law from the opening, and which single line is its law settled."""
    mes, T, couplings = [(a, b) for a in range(p) for b in range(q)], 6 * max(p, q) + 14, it.torus_couplings(p, q)
    whole, settled = 0, {"lean": 0, "the me back, a moment, the same": 0, "its own, a moment, its other-than": 0, "none of these": 0}
    for op in product((1, -1), repeat=p * q):
        ms = by_the_living_code(it, step, couplings, dict(zip(mes, op)), T)
        law = lambda da, db, on, as_it, t0: all(ms[t + on][(a, b)] == as_it * ms[t][((a - da) % p, (b - db) % q)] for t in range(t0, T - on) for a, b in mes)
        whole += law(1, 0, 2, -1, 0) or law(0, 1, 2, -1, 0)
        if law(1, 0, 2, -1, T - 10) or law(0, 1, 2, -1, T - 10): settled["lean"] += 1
        elif law(0, 0, 1, -1, T - 10): settled["its own, a moment, its other-than"] += 1
        elif law(1, 0, 1, 1, T - 10) or law(0, 1, 1, 1, T - 10): settled["the me back, a moment, the same"] += 1
        else: settled["none of these"] += 1
    return whole, settled


def newborns(it, step, n):
    """A path of n mes closing, its openings with a me of no prior and a me with one: how many part from the lean line, and from which moment it is their law."""
    parting, from_moment, openings = 0, 0, 0
    for op in product((1, -1, 0), repeat=n):
        if 0 in op and any(op):
            openings += 1; T = 8 * n + 12
            ms = by_the_living_code(it, step, it.spiral_couplings(n), dict(enumerate(op)), T)
            apart = [t for t in range(T - 2) for a in range(n) if ms[t + 2][a] != -ms[t][(a - 1) % n]]
            parting += bool(apart); from_moment = max(from_moment, max(apart) + 1 if apart else 0)
    return openings, parting, from_moment


if __name__ == "__main__":
    it = opened(sys.argv[1], "the_code_as_it_is")
    names, _ = it.resolver(sys.argv[2]); step = names["_17_next_existing"]
    its = opened(sys.argv[3], "the_resolver_with_nand_alone")
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    closing = [(n, op, [[m[a] for a in range(n)] for m in by_the_living_code(it, step, it.spiral_couplings(n), dict(enumerate(op)), 4 * n + 8)])
               for n in range(1, 11) for op in product((1, -1), repeat=n)]
    line("On a path of mes closing, all with priors, a me's prior by the lean line is its prior by the living code's own lines at all moments: one to ten mes, all 2,046 openings, one nand a me a moment",
         len(closing) == 2046 and all(living == by_the_lean_line(op, 4 * n + 8) for n, op, living in closing))
    line("Its opening is one nand more a me, once: a me's opening now is the other-than of its own prior. With the opening now the prior itself, the lean line is the living code's with none of the 2,046 openings",
         all(living[1] == [-p for p in op] for n, op, living in closing) and not any(living == by_the_lean_line(op, 4 * n + 8, opening_now=lambda p: p) for n, op, living in closing))

    one = [m[0] for m in by_the_living_code(it, step, it.spiral_couplings(1), {0: 1}, 13)]
    facing = lambda op: [[m[0], m[1]] for m in by_the_living_code(it, step, it.spiral_couplings(2), dict(enumerate(op)), 14)]
    line("One me observing itself: the lean line is the right spiral step, a me's prior and its now (x, y) to (y, −x), its own again with four moments. Two mes facing, opening alike: the other's next prior is the me's own now at all moments, v407nanding's pair; opening unlike, it is at no moment",
         all((one[t + 1], one[t + 2]) == (one[t + 1], -one[t]) for t in range(11)) and one[:5] == [1, -1, -1, 1, 1] and one[4:8] == one[:4]
         and all(a == b for a, b in facing((1, 1))) and all(a != b for a, b in facing((1, -1))))

    with_a_back = at_the_end = two_moments = True
    for n in range(2, 8):
        couplings = {(i, 9): i + 1 for i in range(n - 1)}                           # a path with an end me: none back of the me 0
        for op in product((1, -1), repeat=n):
            ms = by_the_living_code(it, step, couplings, dict(enumerate(op)), 4 * n + 8)
            with_a_back = with_a_back and all(ms[t + 2][a] == -ms[t][a - 1] for t in range(len(ms) - 2) for a in range(1, n))
            at_the_end = at_the_end and all(ms[t + 1][0] == -ms[t][0] for t in range(len(ms) - 1))
            two_moments = two_moments and all(ms[t + 2][0] == ms[t][0] for t in range(len(ms) - 2))
    line("A path with an end me, 2 to 7 mes, all openings: a me with a me back of it has the lean line from its opening. The end me, none back of it, has a line of one moment, its prior a moment on its other-than; the lean line's two moments with itself as its other is-not its line, its prior two moments on its own again",
         with_a_back and at_the_end and two_moments)

    TWO = its.TWO
    crossed = lambda wires: (wires[1], wires[0])
    wire_by_wire = lambda wires: (its.other_than(wires[0]), its.other_than(wires[1]))
    line("A parity of two wires: its other-than is a crossing of its two wires, no nand, a + a −, a − a + and a none a none. Wire by wire, two nands, a + is a − and a − a +, and a none is both wires, no parity of the three",
         all(crossed(TWO[p]) == TWO[-p] for p in (1, -1, 0)) and all(wire_by_wire(TWO[p]) == TWO[-p] for p in (1, -1))
         and wire_by_wire(TWO[0]) == (True, True) and (True, True) not in TWO.values())

    born = {n: newborns(it, step, n) for n in range(2, 6)}
    line("A newborn, a me opening with no prior, on a path closing of 2 to 5 mes: all 296 openings with a newborn part from the lean line at a moment with a none in the path; and from the moment of its number of mes on, the lean line is the path's at all moments",
         [born[n][0] for n in born] == [4, 18, 64, 210] and all(born[n][1] == born[n][0] and born[n][2] == n for n in born))

    surfaces = {(p, q): a_surface(it, step, p, q) for p, q in ((2, 2), (2, 3), (3, 3))}
    line("A surface, a me observing two: from the opening the lean line, along or across, is the surface's with 8 of 16 openings of a torus of 2 by 2, 10 of 64 of 2 by 3 and 8 of 512 of 3 by 3. Settled, it is with 16, 58 and 386; the me back, a moment, the same, with 6 of 2 by 3 and 12 of 3 by 3; a me's own, a moment, its other-than, with 114 of 3 by 3; and all are with a single line",
         [surfaces[k][0] for k in surfaces] == [8, 10, 8] and [surfaces[k][1]["lean"] for k in surfaces] == [16, 58, 386]
         and [surfaces[k][1]["the me back, a moment, the same"] for k in surfaces] == [0, 6, 12]
         and [surfaces[k][1]["its own, a moment, its other-than"] for k in surfaces] == [0, 0, 114] and all(surfaces[k][1]["none of these"] == 0 for k in surfaces))

    observed = True
    for n in range(1, 9):
        couplings = it.spiral_couplings(n)
        for op in product((1, -1), repeat=n):
            society, rows = {k: ([(it.S, p)], []) for k, p in enumerate(op)}, []
            for _ in range(4 * n + 8): rows.append(society); society = step(society, couplings)
            for t in range(1, len(rows)):
                for a in range(n):
                    was, now = dict(rows[t - 1][(a - 1) % n][0])[it.S], dict(rows[t][(a - 1) % n][0])[it.S]
                    observed = observed and [v for _, v in rows[t][a][1]] == [now if now != was else 0]
    line("What a me's other observes, by the living code, on a path closing of 1 to 8 mes, all 510 openings: the me's now, with its now other-than its prior; and a 0, with its now its prior. The lean line has the me's now at all moments, and no 0",
         observed)

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
