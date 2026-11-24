"""A me by nand alone, by other-thans and alls, and mes snapped into co-chainings.

A partner's sayings of 23 November, explored by executing. A draft, and no living file.

    python3 -I incoming/v406all2-2/instruments/a_me_by_nand_other_thans_and_alls.py .

1  A me: v406Reiman's fifteen lines of nand, their name said as a me and all else as it is.
2  The fifteen lines by other-thans and alls. An all is two nands in a row, nand is the
   other-than of an all, and either is the other-than of the all of two other-thans.
3  A right spiral step by one other-than: (x, y) to (y, other-than x).
4  Connectors and snaps. A me's giving, by 6, 10 or 9, is an other me's observing. Mes
   snapped along are a co-chaining, and co-chainings snapped across are a surface: Exhibit
   ONE Natural Resolver's own rows of a spiral and of a torus, found in its living file.

v406Reiman's nand, other-than, both and either, and its step, are used as they are, and no
line of them is written again here. It prints a line an is or an is-not, and writes nothing.
"""
import ast
import glob
import itertools
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
sys.dont_write_bytecode = True
sys.path.insert(0, str(root / "incoming" / "v406Reiman" / "instruments"))
import the_resolver_with_nand_alone as with_nand  # noqa: E402
from resolver_as_it_is import (S, exhibit_spiral_priors, exhibit_torus_priors, moments_again,  # noqa: E402
                               opening, self_1_sharings, spiral_couplings, torus_couplings)

nand, other_than, both, either = with_nand.nand, with_nand.other_than, with_nand.both, with_nand.either
TWO, ONE = with_nand.TWO, with_nand.ONE
ITS_NAME = "a_cell" if hasattr(with_nand, "a_cell") else "a_me"
as_it_is = getattr(with_nand, ITS_NAME)


def a_me(prior, observing):
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


def an_all(a, b):
    """Two nands in a row: the other-than of not both."""
    return other_than(nand(a, b))


def an_either(a, b):
    """The other-than of the all of two other-thans."""
    return other_than(an_all(other_than(a), other_than(b)))


def a_me_by_other_thans_and_alls(prior, observing):
    """A me's fifteen lines, their is-or-is-nots said as other-thans and alls."""
    a_plus = a_minus = False
    for plus, minus in observing:
        a_plus = an_either(a_plus, plus)
        a_minus = an_either(a_minus, minus)
    surfacing_plus = an_all(a_plus, other_than(a_minus))
    surfacing_minus = an_all(a_minus, other_than(a_plus))
    prior_plus, prior_minus = prior
    no_prior = an_all(other_than(prior_plus), other_than(prior_minus))
    gives_plus = an_either(an_all(no_prior, surfacing_plus), an_all(prior_minus, other_than(surfacing_minus)))
    gives_minus = an_either(an_all(no_prior, surfacing_minus), an_all(prior_plus, other_than(surfacing_plus)))
    next_plus = an_either(gives_plus, an_all(prior_plus, surfacing_plus))
    next_minus = an_either(gives_minus, an_all(prior_minus, surfacing_minus))
    a_giving = an_either(other_than(no_prior), an_either(a_plus, a_minus))
    a_next = an_either(next_plus, next_minus)
    return (gives_plus, gives_minus), (next_plus, next_minus), a_giving, a_next


def a_right_spiral_step(parity):
    """(x, y) to (y, other-than x): an exchanging and one other-than."""
    x, y = parity
    return y, other_than(x)


def a_snap(connectors, a_giving_me, by, an_observing_me):
    """A connector laid, a coupling. It is no is-or-is-not: a me's giving named an other me's observing."""
    connectors[(a_giving_me, by)] = an_observing_me
    return connectors


def a_co_chaining(n):
    """n mes snapped along by 9, the last to the one opening it: Exhibit ONE's spiral."""
    connectors = {}
    for me in range(n):
        a_snap(connectors, me, 9, (me + 1) % n)
    return connectors


def a_surface(p, q):
    """p by q mes: co-chainings along by 9, snapped across by 10. Exhibit ONE's torus."""
    connectors = {}
    for a in range(p):
        for b in range(q):
            a_snap(connectors, (a, b), 9, ((a + 1) % p, b))
            a_snap(connectors, (a, b), 10, (a, (b + 1) % q))
    return connectors


def all_mes_one_moment(its_lines):
    """v406Reiman's step as it is, as 17-next-existing, its mes by the lines given."""
    def step(society, connectors):
        was = getattr(with_nand, ITS_NAME)
        setattr(with_nand, ITS_NAME, its_lines)
        try:
            return with_nand.step_with_nand(society, connectors)
        finally:
            setattr(with_nand, ITS_NAME, was)
    return step


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def the_lines_of(a_function, of_a_page):
    tree = ast.parse(Path(of_a_page).read_text(encoding="utf-8"))
    return next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == a_function)


def called(fn):
    names = {}
    for n in ast.walk(fn):
        if isinstance(n, ast.Call):
            names[n.func.id] = names.get(n.func.id, 0) + 1
    return names


if __name__ == "__main__":
    living = re.sub(r"[*`]", "", Path(sorted(glob.glob(str(root / "Exhibit_ONE_Natural_Resolver_v*.md")))[0]).read_text(encoding="utf-8"))
    cases = [(p, list(o)) for p in (1, -1, 0) for k in range(5) for o in itertools.product((1, -1, 0), repeat=k)]
    in_two = lambda prior, observed: (TWO[prior], [TWO[v] for v in observed])

    print("1. A me: the fifteen lines, their name said again and all else as it is")
    mine = the_lines_of("a_me", __file__)
    theirs = the_lines_of(ITS_NAME, with_nand.__file__)
    theirs.name = "a_me"
    line(ast.dump(mine) == ast.dump(theirs), "its lines and its words are v406Reiman's, the name apart")
    line(len([n for n in ast.walk(mine) if isinstance(n, (ast.Assign, ast.For, ast.Return))]) == 15, "fifteen lines after its words")
    line(all(a_me(*in_two(p, o)) == as_it_is(*in_two(p, o)) for p, o in cases),
         "a prior +, a prior - and no prior, with none to four observed of +, - and 0, %d cases: the same giving and the same next prior" % len(cases))

    print()
    print("2. The fifteen lines by other-thans and alls")
    two = [(a, b) for a in (False, True) for b in (False, True)]
    line(all(nand(a, b) == other_than(an_all(a, b)) for a, b in two), "nand is the other-than of an all")
    line(all(an_all(a, b) == both(a, b) == other_than(other_than(an_all(a, b))) for a, b in two), "an all is two nands in a row, and two other-thans of it are the all again")
    line(all(an_either(a, b) == either(a, b) for a, b in two), "either is the other-than of the all of two other-thans")
    by_two = the_lines_of("a_me_by_other_thans_and_alls", __file__)
    line(set(called(by_two)) == {"other_than", "an_all", "an_either"} and set(called(the_lines_of("an_either", __file__))) == {"other_than", "an_all"},
         "its lines say other-than, an all and either alone, and either says other-than and an all alone")
    line(all(a_me_by_other_thans_and_alls(*in_two(p, o)) == a_me(*in_two(p, o)) for p, o in cases), "the same giving and the same next prior, %d cases" % len(cases))
    said = called(by_two)
    print("        with one observed, its lines are %d other-thans and %d alls: %d other-thans, %d alls and %d eithers, an either three other-thans and an all"
          % (said["other_than"] + 3 * said["an_either"], said["an_all"] + said["an_either"], said["other_than"], said["an_all"], said["an_either"]))

    print()
    print("3. A right spiral step by one other-than: (x, y) to (y, other-than x)")
    plus, minus = TWO[1], TWO[-1]
    round_of_four = [plus]
    for _ in range(4):
        round_of_four.append(a_right_spiral_step(round_of_four[-1]))
    line(round_of_four[4] == plus and len(set(round_of_four)) == 4, "four steps a round, and a parity's two is-or-is-nots at all four of their places")
    line([ONE[p] for p in round_of_four[:4]] == [1, 0, -1, 0], "from +: +, 0, -, 0")
    line("Number of selves: 1 · a: +, 0, −, 0, +, 0, −, 0, +, 0, −, 0 · b: 4" in living, "Exhibit ONE's row of one self alone: +, 0, -, 0, again with 4")
    line(round_of_four[1] == (False, False) and round_of_four[3] == (True, True), "its two 0s are two: neither, and both together")
    line(a_right_spiral_step(a_right_spiral_step(plus)) == minus and a_right_spiral_step(a_right_spiral_step(minus)) == plus, "two steps are both is-or-is-nots other-than, + to - and - to +: a podaling")
    line(all((4 * 4 * n) % 17 == 17 - n and len({(4 ** k * n) % 17 for k in range(4)}) == 4 for n in range(1, 17)),
         "on the sixteen names, round 17, multiplying by 4 is four steps a round, and two steps are 17 less")
    met = {}
    for p, o in cases:
        a_plus = a_minus = False
        for x, y in in_two(p, o)[1]:
            a_plus, a_minus = either(a_plus, x), either(a_minus, y)
        met[(a_plus, a_minus)] = True
    columns = set(re.findall(r"- Surfacing, 14-next-possibling: ([^:\n]+): ", living))
    line(len(met) == 4 and len(columns) == 4 and {"+", "−", "+ and − together"} <= columns, "a me's lines 3 and 4 are at the same four places: Exhibit ONE's four columns of one self, one moment")

    print()
    print("4. Connectors and snaps: mes snapped into co-chainings, and co-chainings into a surface")
    step, step_by_two = all_mes_one_moment(a_me), all_mes_one_moment(a_me_by_other_thans_and_alls)
    line(all(a_co_chaining(n) == spiral_couplings(n) for n in range(1, 60)) and a_surface(3, 5) == torus_couplings(3, 5), "a co-chaining is a spiral's couplings, and a surface a torus's, a snap a coupling")
    numbered = {"either": 0}

    def an_either_numbered(a, b):
        numbered["either"] += 1
        return with_nand.either(a, b)

    a_me.__globals__["either"] = an_either_numbered
    eithers = []
    for k in range(5):
        numbered["either"] = 0
        a_me(TWO[1], [TWO[1]] * k)
        eithers.append(numbered["either"])
    a_me.__globals__["either"] = with_nand.either
    line(all(eithers[k + 1] - eithers[k] == 2 for k in range(4)), "a snap more at a me is two eithers more, its lines 3 and 4 once more")
    rows = re.findall(r"^- Number of selves: (\d+) · a: ([^·]+) · b: (\d+)$", living, re.M)
    spirals = True
    for n, a, b in rows:
        n = int(n)
        again = moments_again(step, opening(range(n), exhibit_spiral_priors(n)), a_co_chaining(n))[1]
        spirals = spirals and self_1_sharings(step, n) == a.strip().split(", ") and again == int(b)
    line(spirals and len(rows) == 13, "Exhibit ONE's thirteen rows of a spiral of selves, 1 to 59: self 1's givings of twelve moments and its moments to again, by a me and its snaps along")
    line(all(self_1_sharings(step_by_two, int(n)) == a.strip().split(", ") for n, a, b in rows), "the same thirteen rows by other-thans and alls")
    tori = re.findall(r"^- Torus of selves, p along · q across: (\d+) · (\d+)\n\s+- a: (\d+)\n\s+- b: (\d+)", living, re.M)
    surfaces = True
    for p, q, a, b in tori:
        p, q = int(p), int(q)
        selves = [(x, y) for x in range(p) for y in range(q)]
        from_moment, again = moments_again(step, opening(selves, exhibit_torus_priors(p, q)), a_surface(p, q))
        surfaces = surfaces and again == int(a) and from_moment == int(b)
    line(surfaces and len(tori) == 11, "Exhibit ONE's eleven rows of a torus of selves: its moments to again, and the moment it is again from, by a me and its snaps along and across")
    inward = {n: 8 * n - 7 for n in (2, 6, 10, 14)}
    nines = {n: (v - 9) // 16 + 1 for n, v in inward.items() if (v - 9) % 16 == 0}
    said_inward = all(re.search(r"- n: %d\n(?:\s+- .*\n){2}\s+- a: 9 of %s:" % (n, ("1st", "3rd", "5th", "7th")[i]), living) for i, n in enumerate((2, 6, 10, 14)))
    line(nines == {2: 1, 6: 3, 10: 5, 14: 7} and said_inward, "by 8n - 7, the across names 2, 6, 10 and 14 are, a scale inward, the 9 of a 1 to 17: an along name")
    said_outward = all(re.search(r"- n: %d\n(?:\s+- .*\n){3}\s+- b: %d:" % (n, m), living) for n, m in ((1, 1), (9, 2), (17, 3)))
    line(all(8 * m - 7 == n for n, m in ((1, 1), (9, 2), (17, 3))) and said_outward, "and the along names 1, 9 and 17 are, a scale outward, 1, 2 and 3: 9 an across name")
