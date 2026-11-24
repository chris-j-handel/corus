"""A prior and its sequence, by other-thans: a partner's three askings, by executing.

    python3 -I incoming/v406all2-2/instruments/a_prior_its_sequence_by_other_thans.py .

1  Is prior a sequence in a me's fifteen lines.
2  Is a prior of a prior in them: a me's next prior, its prior a moment on.
3  Is the nand of prior with prior, its other-than, said as a sequence of priors:
   along moments, and along a co-chaining, a snap an other-than.

A me's lines and the snaps are this folder's, of a_me_by_nand_other_thans_and_alls.py, and
the step is v406Reiman's as it is. Exhibit ONE Natural Resolver's own sentences and rows
are found in its living file. It prints a line an is or an is-not, and writes nothing.
"""
import ast
import glob
import itertools
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.argv = [sys.argv[0], str(root)]
import a_me_by_nand_other_thans_and_alls as draft  # noqa: E402

a_me, other_than, nand, TWO, ONE = draft.a_me, draft.other_than, draft.nand, draft.TWO, draft.ONE
S, opening, a_co_chaining = draft.S, draft.opening, draft.a_co_chaining
step = draft.all_mes_one_moment(a_me)


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def its_other_than(parity):
    """Nand of a parity with itself, at both its is-or-is-nots."""
    plus, minus = parity
    return nand(plus, plus), nand(minus, minus)


def priors_along(mes, priors, moments):
    """A prior of all mes of a co-chaining, a moment a row, as two is-or-is-nots."""
    society, connectors, rows = opening(mes, priors), a_co_chaining(len(mes)), []
    for _ in range(moments):
        rows.append([TWO[dict(society[me][0]).get(S, 0)] for me in mes])
        society = step(society, connectors)
    return rows


if __name__ == "__main__":
    living = re.sub(r"[*`]", "", Path(sorted(glob.glob(str(root / "Exhibit_ONE_Natural_Resolver_v*.md")))[0]).read_text(encoding="utf-8"))
    plus, minus, none, together = TWO[1], TWO[-1], (False, False), (True, True)
    cases = [(p, list(o)) for p in (1, -1, 0) for k in range(5) for o in itertools.product((1, -1, 0), repeat=k)]
    in_two = lambda prior, observed: (TWO[prior], [TWO[v] for v in observed])

    print("1. Prior in a me's fifteen lines")
    lines = draft.the_lines_of("a_me", draft.__file__)
    in_order = sorted((n for n in ast.walk(lines) if isinstance(n, (ast.Assign, ast.For, ast.Return))), key=lambda n: n.lineno)
    with_prior_said = [k + 1 for k, n in enumerate(in_order) if not isinstance(n, ast.For) and any(isinstance(m, ast.Name) and m.id == "prior" for m in ast.walk(n))]
    line(with_prior_said == [7], "prior is said once in the lines, at line 7: one parity, opened as two is-or-is-nots")
    nexts = {a_me(*in_two(p, o))[1] for p, o in cases}
    gives = {a_me(*in_two(p, o))[0] for p, o in cases}
    line(nexts == {plus, minus, none} and gives == {plus, minus, none}, "a next prior and a giving are a +, a - or neither, and at no case both together")

    def surfacing(observed):
        seen = set(v for v in observed if v)
        return {frozenset([1]): plus, frozenset([-1]): minus}.get(frozenset(seen), none)

    with_prior = [(p, o) for p, o in cases if p]
    line(all(a_me(*in_two(p, o))[1] == (TWO[p] if surfacing(o) == TWO[p] else its_other_than(TWO[p])) for p, o in with_prior),
         "with a prior, its next prior is its prior with its own parity surfacing, and with all else the other-than of its prior, nand of prior with prior")
    line(all(ONE[a_me(*in_two(p, o))[0]] == 0 for p, o in with_prior if surfacing(o) == TWO[p]), "with its own parity surfacing it gives a 0: same-existing")
    line(all(a_me(*in_two(0, o))[1] == surfacing(o) for p, o in cases if not p), "with no prior, its next prior is what surfaces")

    print()
    print("2. A prior of a prior: a me's next prior is its prior a moment on")
    alone = [row[0] for row in priors_along([0], {0: 1}, 9)]
    said = "| A spiral of one, along | +, −, −, +, +, −, −, +, + |"
    line([ONE[p] for p in alone] == [1, -1, -1, 1, 1, -1, -1, 1, 1] and said in living, "a me alone, snapped along to itself, its prior of nine moments: +, -, -, +, +, -, -, +, +, Exhibit ONE's row")
    line(all((alone[t + 1], alone[t + 2]) == (alone[t + 1], its_other_than(alone[t])) for t in range(7)), "its prior and its next prior, a pair (x, y), step to (y, other-than x): Exhibit ONE's right spiral, a scale outward of a parity's two is-or-is-nots")
    line(all(alone[t + 2] == its_other_than(alone[t]) for t in range(7)), "its prior two moments on is the other-than of its prior")
    line(all(alone[t + 4] == its_other_than(its_other_than(alone[t])) == alone[t] for t in range(5)), "its prior four moments on is the other-than of the other-than: its prior again")
    giving_0, prior_1, _, _ = a_me(plus, [])
    giving_1, prior_2, _, _ = a_me(a_me(plus, [])[1], [giving_0])
    line(prior_2 == its_other_than(plus) == alone[2], "a me of a me: a_me(a_me(prior, none)'s next prior, its own giving)'s next prior is the other-than of prior")

    print()
    print("3. A sequence of priors by other-thans, along a co-chaining")
    sentence = "prior from its third moment on is a prior of a self it receives from two moments before, inverting."
    line(sentence in living, "Exhibit ONE's sentence of a prior two moments before, inverting")
    two_before = by_snaps = round_it = again = True
    openings = 0
    for n in range(1, 9):
        mes = list(range(n))
        for values in itertools.product((1, -1), repeat=n):
            openings += 1
            rows = priors_along(mes, dict(zip(mes, values)), 4 * n + 1)
            two_before = two_before and all(rows[t][i] == its_other_than(rows[t - 2][(i - 1) % n]) for t in range(2, 4 * n + 1) for i in mes)
            for k in range(1, 2 * n + 1):
                back = rows[0]
                expected = [back[(i - k) % n] for i in mes]
                for _ in range(k):
                    expected = [its_other_than(p) for p in expected]
                by_snaps = by_snaps and rows[2 * k] == expected
            round_it = round_it and rows[2 * n] == ([its_other_than(p) for p in rows[0]] if n % 2 else rows[0])
            again = again and rows[4 * n] == rows[0]
    line(two_before, "a me's prior is the other-than of the prior, two moments before, of the me it observes: all %d openings of 1 to 8 mes, a prior with a me" % openings)
    line(by_snaps, "k snaps back and 2k moments before: the k-th other-than of that me's prior, an even number the prior itself and an odd number its other-than")
    line(round_it, "round a co-chaining of n mes, 2n moments: n other-thans. With n even, its priors again; with n odd, all its priors their other-thans")
    line(again, "with 4n moments, an even number of other-thans with all n: its priors again")
    line("self's parity with twice its number of moments is its parity inverting" in living and "with an odd number of selves, four times its number" in living,
         "Exhibit ONE's own of an odd number: inverting with twice its number of moments, and again with four times")
