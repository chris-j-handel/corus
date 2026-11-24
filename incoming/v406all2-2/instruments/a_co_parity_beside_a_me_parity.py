"""A co-parity, an other thing than a me-parity: a partner's asking of 24 November, by executing.

    python3 -I incoming/v406all2-2/instruments/a_co_parity_beside_a_me_parity.py .

1  The sentences of a co-parity, a me-parity and a like pair, found word for word in their homes,
   and a co-parity's surfacing as the living files say it: its own parity surfacing.
2  In the fifteen lines of nand: a me-parity is two is-or-is-nots, and a co-parity one,
   an all of a prior and what surfaces.
3  An other thing: + and - exchanged; none surfacing; two mes facing.
4  On rounds of 1 to 9 mes, all their openings: a me-parity with all mes at all moments,
   and a co-parity at a like pair, one moment of two.

The fifteen lines and the snaps are this folder's, of a_me_by_nand_other_thans_and_alls.py,
and the step is v406Reiman's as it is. It prints a line an is or an is-not, and writes nothing.
"""
import glob
import inspect
import itertools
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.argv = [sys.argv[0], str(root)]
import a_me_by_nand_other_thans_and_alls as draft  # noqa: E402

with_nand = draft.with_nand
the_fifteen_lines, TWO, ONE, S = draft.a_me, draft.TWO, draft.ONE, draft.S
both, either = with_nand.both, with_nand.either
opening, a_co_chaining = draft.opening, draft.a_co_chaining
step = draft.all_mes_one_moment(the_fifteen_lines)
EXCHANGED = {1: -1, -1: 1, 0: 0}


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def a_page(pattern):
    """A page of the set by its name, its marks of bold, italics and code away."""
    found = sorted(glob.glob(str(root / pattern)))
    return re.sub(r"[*`]", "", Path(found[0]).read_text(encoding="utf-8")) if found else ""


def surfacing(observed):
    seen = frozenset(v for v in observed if v)
    return {frozenset([1]): 1, frozenset([-1]): -1}.get(seen, 0)


def a_co_parity(prior, observed):
    """One is-or-is-not by nand: an all of a prior and what surfaces, with a + or with a -."""
    prior_plus, prior_minus = TWO[prior]
    surfacing_plus, surfacing_minus = TWO[surfacing(observed)]
    return either(both(prior_plus, surfacing_plus), both(prior_minus, surfacing_minus))


def gives(prior, observed):
    return ONE[the_fifteen_lines(TWO[prior], [TWO[v] for v in observed])[0]]


def next_prior(prior, observed):
    return ONE[the_fifteen_lines(TWO[prior], [TWO[v] for v in observed])[1]]


def along(n, values, moments):
    """A round of n mes, a moment a row: a me's prior, and a co-parity is-or-is-not with it."""
    mes = list(range(n))
    society = {me: ([(S, v)] if v else [], []) for me, v in zip(mes, values)}
    connectors, rows = a_co_chaining(n), []
    for _ in range(moments):
        priors = [dict(society[me][0]).get(S, 0) for me in mes]
        observed = [[v for _, v in society[me][1]] for me in mes]
        rows.append((priors, [a_co_parity(priors[me], observed[me]) for me in mes]))
        society = step(society, connectors)
    return rows


if __name__ == "__main__":
    print("1. The sentences, in their homes")
    one = a_page("Exhibit_ONE_Natural_Resolver_v*.md")
    intelligence = a_page("Natural_Intelligence_v*.md")
    numbers = a_page("Exhibit_THREE_Natural_Numbers_v*.md")
    mathematics = a_page("Exhibit_FOUR_Natural_Mathematics_v*.md")
    the_draft = a_page("incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md")
    line("co me-parity, bi other-parity, tri all-parity" in one, "Exhibit ONE Natural Resolver, a name's three: co me-parity, bi other-parity, tri all-parity")
    line(re.search(r"Co-parity and bi-parity are its two \w+\.", one) is not None, "Exhibit ONE Natural Resolver, five dimensions: co-parity and bi-parity, its two")
    line(re.search(r"Its two \w+ are co-parity, the same, \w+ 0, and bi-parity, one inversion\.", intelligence) is not None,
         "Natural Intelligence: co-parity, the same, a 0, and bi-parity, one inversion")
    line("3 now-existing co-parity" in mathematics and "in neither self alone" in mathematics, "Exhibit FOUR Natural Mathematics: 3 now-existing co-parity, in neither self alone")
    line(re.search(r"one pair of coupling selves is \w+ \w+ parity, a like pair", numbers) is not None, "Exhibit THREE Natural Numbers, 7.2: a like pair of coupling selves")
    line("A number is two moments: a spiral's one pair of one parity moves one self on with a second moment." in the_draft, "the draft's 1.2, its bold as it is")
    naming = a_page("Exhibit_TWENTY_Natural_Naming_v*.md")
    thirty = a_page("Exhibit_THIRTY_Co-Chaining_Logic_Registry_v*.md")
    living = "\n".join(re.sub(r"[*`]", "", Path(f).read_text(encoding="utf-8")) for f in sorted(glob.glob(str(root / "*.md"))))
    line("with 14 surfacing its own parity, 0" in naming, "Exhibit TWENTY Natural Naming, 5.44, its line 3: 14 surfacing its own parity, 0")
    line(re.search(r"With its own parity surfacing, two cells, it \w+ 0 and its prior is same-existing\.", thirty) is not None,
         "Exhibit THIRTY Co-Chaining Logic Registry: with its own parity surfacing, a 0 and its prior same-existing")
    its_places = len(re.findall(r"own parity surfacing|surfacing its own parity", living))
    line(its_places == 8 and not re.search(r"same parity surfacing", living, re.I),
         "the living files say its own parity surfacing at %d places, and a same parity surfacing at none" % its_places)

    print()
    print("2. In the fifteen lines of nand")
    observed_lists = [list(o) for k in range(5) for o in itertools.product((1, -1, 0), repeat=k)]
    cases = [(p, o) for p in (1, -1, 0) for o in observed_lists]
    its_lines = inspect.getsource(getattr(with_nand, draft.ITS_NAME))
    line(all(len(TWO[p]) == 2 for p in (1, -1, 0)) and {a_co_parity(p, o) for p, o in cases} == {True, False},
         "a me-parity is two is-or-is-nots, a + and a -; a co-parity is one")
    line("both(prior_plus, surfacing_plus)" in its_lines and "both(prior_minus, surfacing_minus)" in its_lines,
         "a co-parity is an all of a prior and what surfaces, with a + or with a -: the two alls of lines 11 and 12, as they are")
    line(all(a_co_parity(p, o) == (p != 0 and gives(p, o) == 0 and next_prior(p, o) == p) for p, o in cases),
         "with a co-parity, and with it alone: a prior, a 0 given, and its prior same-existing, all %d cases" % len(cases))
    line(all(gives(p, o) == -p for p, o in cases if p and not a_co_parity(p, o)), "with a prior and no co-parity: a + or a - given, the other-than of its prior")

    print()
    print("3. An other thing than a me-parity")
    exchanged = lambda o: [EXCHANGED[v] for v in o]
    line(all(next_prior(EXCHANGED[p], exchanged(o)) == EXCHANGED[next_prior(p, o)] for p, o in cases)
         and all(a_co_parity(EXCHANGED[p], exchanged(o)) == a_co_parity(p, o) for p, o in cases),
         "+ and - exchanged all through: all me-parities invert, and all co-parities are as they were")
    line(all(a_co_parity(-p, o) != a_co_parity(p, o) for p, o in cases if p and surfacing(o)), "a me-parity alone exchanged, with a parity surfacing: its co-parity is other")
    none_surfacing = [(p, o) for p, o in cases if surfacing(o) == 0]
    line(all(next_prior(p, o) != 0 for p, o in none_surfacing if p) and not any(a_co_parity(p, o) for p, o in none_surfacing),
         "with none of an other's surfacing, %d cases: a me-parity goes on, and a co-parity is with none" % len(none_surfacing))
    facing = [along(2, values, 12) for values in itertools.product((1, -1, 0), repeat=2)]
    line(all(with_it[0] == with_it[1] for rows in facing for _, with_it in rows) and any(with_it[0] for rows in facing for _, with_it in rows),
         "two mes facing, all nine openings: a co-parity is one of the two, with both at a moment or with neither")

    print()
    print("4. On rounds of 1 to 9 mes, all their openings with priors")
    with_all = two_moments = a_me_on = odd_moment = even_moment = True
    openings = 0
    for n in range(1, 10):
        for values in itertools.product((1, -1), repeat=n):
            openings += 1
            rows = along(n, values, 4 * n + 2)
            alike = [{i for i in range(n) if priors[i] == priors[(i - 1) % n]} for priors, _ in rows]
            with_one = [{i for i in range(n) if with_it[i]} for _, with_it in rows]
            with_all = with_all and all(v != 0 for priors, _ in rows for v in priors)
            two_moments = two_moments and all(alike[t] == alike[t + 1] for t in range(0, 4 * n + 1, 2))
            a_me_on = a_me_on and all(alike[t + 2] == {(i + 1) % n for i in alike[t]} for t in range(0, 4 * n, 2))
            odd_moment = odd_moment and all(with_one[t] == alike[t] for t in range(1, 4 * n + 2, 2))
            even_moment = even_moment and not any(with_one[t] for t in range(0, 4 * n + 2, 2))
    line(with_all, "a me-parity is with all mes at all moments: all %d openings" % openings)
    line(two_moments and a_me_on, "a like pair, a me alike the me it observes, is at one me two moments, and then a me on")
    line(odd_moment and even_moment, "a co-parity is at a like pair alone, with one moment of its two: a 0 given, and with its other moment none")
    like_one = [along(n, values, 2)[0][0] for n in (3, 5, 7, 9) for values in itertools.product((1, -1), repeat=n)]
    line(all(sum(1 for i in range(len(p)) if p[i] == p[i - 1]) % 2 == 1 for p in like_one), "a round of an odd number is with a like pair at all its openings, an odd number of them")
