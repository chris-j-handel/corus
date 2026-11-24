"""For Exhibit THIRTY-TWO Natural Prime Numbering: four of its sentences by a me's lines.

    python3 -I incoming/v406all2-2/instruments/for_exhibit_thirty_two_by_a_me_s_lines.py .

The draft's sentences of its 1.1, 1.2, 1.4 and 1.6, executed by a me's fifteen lines of nand
and its snaps along, with what the lines add: a reason. And a partner's saying of nand as a
method of compressing, beside numbers of it.

A me's lines and the snaps are this folder's, of a_me_by_nand_other_thans_and_alls.py, and
the step is v406Reiman's as it is. It prints a line an is or an is-not, and writes nothing.
"""
import itertools
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.argv = [sys.argv[0], str(root)]
import a_me_by_nand_other_thans_and_alls as draft  # noqa: E402

a_me, other_than, nand, TWO, ONE, S = draft.a_me, draft.other_than, draft.nand, draft.TWO, draft.ONE, draft.S
opening, a_co_chaining, moments_again = draft.opening, draft.a_co_chaining, draft.moments_again
step = draft.all_mes_one_moment(a_me)


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def rows_of(n, priors, moments):
    """A moment a row: the priors of a spiral's mes, and what a me observes."""
    mes = list(range(n))
    society, connectors, rows = opening(mes, priors), a_co_chaining(n), []
    for _ in range(moments):
        rows.append(([dict(society[me][0]).get(S, 0) for me in mes], [[v for _, v in society[me][1]] for me in mes]))
        society = step(society, connectors)
    return rows


if __name__ == "__main__":
    in_two = lambda prior, observed: (TWO[prior], [TWO[v] for v in observed])
    observed_lists = [list(o) for k in range(5) for o in itertools.product((1, -1, 0), repeat=k)]

    def surfacing(observed):
        seen = frozenset(v for v in observed if v)
        return {frozenset([1]): 1, frozenset([-1]): -1}.get(seen, 0)

    print("1.1  A self with its prior: the same, a 0 and its prior same-existing; other than its prior, one inversion")
    with_prior = [(p, o) for p in (1, -1) for o in observed_lists]
    gives = lambda p, o: ONE[a_me(*in_two(p, o))[0]]
    next_prior = lambda p, o: ONE[a_me(*in_two(p, o))[1]]
    line(all(gives(p, o) == 0 and next_prior(p, o) == p for p, o in with_prior if surfacing(o) == p), "the same surfacing as its prior: a 0 given, and its prior as it is")
    line(all(gives(p, o) == -p == next_prior(p, o) for p, o in with_prior if surfacing(o) != p), "all other surfacings: its prior's other-than given, and its next prior: %d cases of a prior" % len(with_prior))
    line(all(next_prior(0, o) == surfacing(o) for o in observed_lists), "added by the lines: with no prior, its next prior is what surfaces, %d cases" % len(observed_lists))

    print()
    print("1.2  A number is two moments: a spiral's one pair of one parity moves one self on with a second moment")
    like = lambda priors: [i for i in range(len(priors)) if priors[i] == priors[(i + 1) % len(priors)]]
    moves = one_0 = True
    for n in range(3, 60, 2):
        rows = rows_of(n, {i: (-1 if i % 2 == 0 else 1) for i in range(n)}, 2 * n + 4)
        moves = moves and all(len(like(rows[t][0])) == 1 and like(rows[t + 2][0])[0] == (like(rows[t][0])[0] + 1) % n for t in range(2 * n))
        zeros = [sum(1 for o in rows[t][1] for v in o if v == 0) for t in range(2, 2 * n + 2)]
        one_0 = one_0 and sorted(set(zeros)) == [0, 1] and all(zeros[t] + zeros[t + 1] == 1 for t in range(len(zeros) - 1))
    line(moves, "spirals of an odd number, 3 to 59: one like pair, moving a me on with two moments")
    line(one_0, "and one 0 given with two moments, by the me observing its own parity: same-existing")
    even = all(not like(rows_of(n, {i: (-1 if i % 2 == 0 else 1) for i in range(n)}, 1)[0][0]) for n in range(2, 60, 2))
    line(even, "a like pair is an odd spiral's own: spirals of an even number, 2 to 58, their parities inverting me to me, bring none")

    print()
    print("1.4  Four times an odd span, twice an even span, and twice an odd span its opening inverts after")
    flip = {1: -1, -1: 1, 0: 0}
    law = by_one_line = True
    openings = 0
    for n in range(1, 9):
        for values in itertools.product((1, -1), repeat=n):
            openings += 1
            rows = [r[0] for r in rows_of(n, dict(enumerate(values)), 4 * n + 1)]
            law = law and rows[4 * n] == rows[0] and (rows[2 * n] == [flip[v] for v in rows[0]] if n % 2 else rows[2 * n] == rows[0])
            for t in range(4 * n + 1):
                back, others = t // 2, (t + 1) // 2
                said = [rows[0][(i - back) % n] * (-1) ** others for i in range(n)]
                by_one_line = by_one_line and rows[t] == said
    line(law, "all %d openings of 1 to 8 mes, a prior with a me: again with 4n moments; with 2n, as it was with n even and all inverting with n odd" % openings)
    line(by_one_line, "added by the lines, its reason: a me's prior with moment t is the opening prior of the me t/2 back, with an other-than a snap. A spiral's whole table from its opening row, by one line")
    again = {}
    for n in (2, 3, 5, 7):
        again[n] = sorted({moments_again(step, opening(range(n), dict(enumerate(v))), a_co_chaining(n))[1] for v in itertools.product((1, -1), repeat=n)})
    line(again == {2: [2, 4], 3: [4, 12], 5: [4, 20], 7: [4, 28]}, "a prime's own, from all its openings: 3, 5 and 7 again with 4 and with 4n alone, and 2 with 2 and with 4")

    print()
    print("1.6  A pair (x, y) stepping to (y, -x); a self alone, giving +, 0, -, 0")
    alone = rows_of(1, {0: 1}, 9)
    priors = [r[0][0] for r in alone]
    givings = [r[1][0][0] for r in alone[1:]]
    line(all((priors[t + 1], priors[t + 2]) == (priors[t + 1], -priors[t]) for t in range(7)), "a me alone: its prior and its next prior step (x, y) to (y, -x)")
    line(givings[:8] == [-1, 0, 1, 0, -1, 0, 1, 0], "its givings from a prior +: -, 0, +, 0, a 0 with two moments")
    x_y = TWO[1]
    four = [x_y]
    for _ in range(3):
        four.append((four[-1][1], other_than(four[-1][0])))
    line([ONE[p] for p in four] == [1, 0, -1, 0] and four[1] == (False, False) and four[3] == (True, True), "added by the lines: -x is one other-than. On a parity's two is-or-is-nots the step is +, 0, -, 0, its two 0s neither and both")

    print()
    print("Nand, a method of compressing: a partner's saying of 24 November, beside numbers of it")
    its = draft.with_nand
    numbered = {"nands": 0}
    as_it_is = its.nand

    def a_nand_numbered(a, b):
        numbered["nands"] += 1
        return as_it_is(a, b)

    its.nand = a_nand_numbered
    nands = []
    for k in range(5):
        numbered["nands"] = 0
        getattr(its, draft.ITS_NAME)(TWO[1], [TWO[1]] * k)
        nands.append(numbered["nands"])
    its.nand = as_it_is
    line(nands == [46, 52, 58, 64, 70], "a me's one moment is 46 nands with none observed, and 6 more with an observed more: 52 with one")
    line(4 * 59 * 59 == 13924, "a spiral of 59 mes to its priors again: 236 moments of 59 mes, 13,924 moments of a me, from fifteen lines and 59 snaps")
