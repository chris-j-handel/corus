"""A now universe with a sequence of prior nows, a partner's three sentences executed, their is and their is-not (session v406geodesic2).

A partner's sentences of 24 November, re-said one relation a sentence:
    Next is other-than now.    Now is other-than prior.    Next is other-than other-than prior.

Executed here beside Exhibit ONE Natural Resolver's own code, all or none:
  1  a me with none observed, alone;                          2  an end me of a path, none back of it;
  3  the opening moment of all societies gone through;        4  a path of mes closing, all its openings;
  5  a me observing itself, the right spiral;                 6  v407nanding's lean line with a me its own other;
  7  a path with an end me by the lean line alone;            8  other-than other-than, two nands, the thing again.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_a_now_universe_next_is_other-than_now_executed.py incoming/v406Reiman/instruments/resolver_as_it_is.py .
"""
import importlib.util, os, sys
from itertools import product
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("the_rigor", os.path.join(HERE, "check_the_lean_line_rigorized_its_is_and_its_is-not.py"))
rigor = importlib.util.module_from_spec(spec); spec.loader.exec_module(rigor)
lean_line, NOT_BOTH, IS, PARITY = rigor.lean_line, rigor.NOT_BOTH, rigor.IS, rigor.PARITY


def the_three(sequence):
    """A me's priors, moment by moment: is its next the other-than of its now, and its next but one its own again, at all moments."""
    return (all(sequence[t + 1] == -sequence[t] for t in range(len(sequence) - 1)),
            all(sequence[t + 2] == sequence[t] for t in range(len(sequence) - 2)))


def a_path_with_an_end_me_by_the_lean_line(opening, moments):
    """The end me its own other by its now; a me with a me back of it by that me's prior; an opening now by a me's own prior."""
    priors = [IS[p] for p in opening]
    nows, rows = [lean_line(None, p)[1] for p in priors], []
    for _ in range(moments):
        rows.append([PARITY[p] for p in priors])
        pairs = [lean_line(nows[a], nows[a] if a == 0 else priors[a - 1]) for a in range(len(priors))]
        priors, nows = [p for p, _ in pairs], [n for _, n in pairs]
    return rows


if __name__ == "__main__":
    it = rigor.opened(sys.argv[1], "the_code_as_it_is")
    names, _ = it.resolver(sys.argv[2]); step = names["_17_next_existing"]
    living = lambda couplings, priors, moments: rigor.by_the_living_code(it, step, couplings, priors, moments)
    found = [0, 0]

    def line(sentence, it_is):
        found[0] += 1; found[1] += 0 if it_is else 1
        print(("is       " if it_is else "is not   ") + sentence)

    alone = {p: [m[0] for m in living({}, {0: p}, 13)] for p in (1, -1)}
    three_alone = [[m[k] for m in living({}, {0: 1, 1: -1, 2: 1}, 13)] for k in range(3)]
    line("A me with none observed, a now universe with its sequence of prior nows alone: by the living code its next is the other-than of its now, its now the other-than of its prior, and its next its prior again, at all moments, a + and a −; and three mes with no coupling are three such",
         all(the_three(s) == (True, True) for s in alone.values()) and all(the_three(s) == (True, True) for s in three_alone))

    ends, paths = True, {}
    for n in range(2, 8):
        couplings = {(i, 9): i + 1 for i in range(n - 1)}
        for op in product((1, -1), repeat=n):
            paths[op] = [[m[a] for a in range(n)] for m in living(couplings, dict(enumerate(op)), 4 * n + 8)]
            ends = ends and the_three([row[0] for row in paths[op]]) == (True, True)
    line("An end me of a path, none back of it, 2 to 7 mes, all 252 openings: the three sentences are its own at all moments", ends and len(paths) == 252)

    closing = {(n, op): [[m[a] for a in range(n)] for m in living(it.spiral_couplings(n), dict(enumerate(op)), 4 * n + 8)] for n in range(1, 11) for op in product((1, -1), repeat=n)}
    surfaces = True
    for p, q in ((2, 2), (2, 3), (3, 3)):
        mes = [(a, b) for a in range(p) for b in range(q)]
        for op in product((1, -1), repeat=p * q):
            ms = living(it.torus_couplings(p, q), dict(zip(mes, op)), 2)
            surfaces = surfaces and all(ms[1][k] == -ms[0][k] for k in mes)
    line("At its opening, with none yet observed, a me's now is the other-than of its prior: all mes of all societies gone through, paths closing, paths with an end me and tori, all their openings",
         all(rows[1] == [-p for p in rows[0]] for rows in closing.values()) and all(rows[1] == [-p for p in rows[0]] for rows in paths.values()) and surfaces)

    odd = all(rows[t + 1][a] == -rows[t][a] for (n, op), rows in closing.items() for t in range(0, len(rows) - 1, 2) for a in range(n))
    whole = [(n, op) for (n, op), rows in closing.items() if all(the_three([row[a] for row in rows]) == (True, True) for a in range(n))]
    in_turn = [(n, op) for (n, op) in closing if all(op[a] == -op[a - 1] for a in range(n))]
    line("A path of mes closing, one to ten mes, all 2,046 openings: from an even moment to the odd moment after it a me's now is the other-than of its prior, with all; the three sentences are a me's at all moments with ten openings alone, the parities in turn of 2, 4, 6, 8 and 10 mes",
         odd and len(closing) == 2046 and sorted(whole) == sorted(in_turn) and [n for n, _ in sorted(whole)] == [2, 2, 4, 4, 6, 6, 8, 8, 10, 10])

    itself = [m[0] for m in living(it.spiral_couplings(1), {0: 1}, 13)]
    line("A me observing itself: its next is the other-than of its prior, the right spiral, its own again with four moments; its next is the other-than of its now at one moment in two, and the three sentences are its own at some moments alone",
         all(itself[t + 2] == -itself[t] for t in range(11)) and the_three(itself) == (False, False)
         and [itself[t + 1] == -itself[t] for t in range(12)] == [True, False] * 6)

    calls = True
    for prior in (True, False):
        now = lean_line(None, prior)[1]                                          # its opening: a me its own other by its prior
        its_prior, its_next = lean_line(now, now)                                  # a moment on: a me its own other by its now
        calls = calls and now == (not prior) and its_prior == now and its_next == (not now) and its_next == prior
    line("The three sentences are v407nanding's lean line with a me its own other: by its prior at its opening, now is other-than prior; by its now a moment on, next is other-than now; and the two in a row, next is its prior again",
         calls)

    line("A path with an end me by the lean line alone, the end me its own other by its now and an opening now by a me's own prior, is the living code's at all moments: 2 to 7 mes, all 252 openings. The opening and the end me are the lean line's own",
         all(a_path_with_an_end_me_by_the_lean_line(op, len(rows)) == rows for op, rows in paths.items()))

    line("Other-than other-than prior is two nands, and it is the prior again, an is and an is-not",
         all(NOT_BOTH[(NOT_BOTH[(p, p)],) * 2] == p for p in (True, False)))

    print(f"\n{found[0] - found[1]} of {found[0]} are is")
    sys.exit(1 if found[1] else 0)
