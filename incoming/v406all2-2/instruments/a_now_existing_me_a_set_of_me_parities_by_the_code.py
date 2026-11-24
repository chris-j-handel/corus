"""A me, no parity and in no co-parity; a now-existing me, a universal set of me-parities.

    python3 -I incoming/v406all2-2/instruments/a_now_existing_me_a_set_of_me_parities_by_the_code.py .

A partner's word of 24 November, beside the two codes as they are, by executing.

1  The sentences of a me, a me-parity and a co-parity, found word for word in their homes.
2  By the living code of name 1, 1-now-existing: a self's prior is a set of named parities,
   and the fifteen lines of nand are one of them, once a named prior, apart.
3  One is-or-is-not of a co-parity: a me-parity with what surfaces of others, of neither alone.
4  v406geodesic2's sentence 42, asked of this window: executed apart by this folder's lines,
   with rounds of 9 and of 10 mes, all their openings.
5  v406geodesic2's asking of a single path with a name: rounds of mes with two named
   parities, a name apart.

The fifteen lines and the snaps are this folder's, of a_me_by_nand_other_thans_and_alls.py;
the two codes are v406Reiman's and Exhibit ONE Natural Resolver's, as they are. It prints a
line an is or an is-not, and writes nothing.
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

with_nand = draft.with_nand
the_fifteen_lines, nand, TWO, ONE, S = draft.a_me, draft.nand, draft.TWO, draft.ONE, draft.S
opening, a_co_chaining = draft.opening, draft.a_co_chaining
step = draft.all_mes_one_moment(the_fifteen_lines)


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def a_page(pattern):
    """A page of the set by its name, its marks of bold, italics and code away."""
    found = sorted(glob.glob(str(root / pattern)))
    return re.sub(r"[*`]", "", Path(found[0]).read_text(encoding="utf-8")) if found else ""


def its_other_than(parity):
    """Nand of a parity with itself, at both its is-or-is-nots."""
    plus, minus = parity
    return nand(plus, plus), nand(minus, minus)


def other_thans(parity, how_many):
    for _ in range(how_many):
        parity = its_other_than(parity)
    return parity


def a_named_prior_apart(name, priors, observing):
    """The fifteen lines with one named prior and what is observed with its name alone."""
    gives, its_next, _, a_next = the_fifteen_lines(TWO[dict(priors).get(name, 0)], [TWO[v] for k, v in observing if k == name])
    return ([(name, ONE[gives])] if ONE[gives] else []), ([(name, ONE[its_next])] if a_next else [])


def priors_along(n, values, moments):
    """A round of n mes, a moment a row: a me's prior as two is-or-is-nots."""
    mes = list(range(n))
    society, connectors, rows = opening(mes, dict(zip(mes, values))), a_co_chaining(n), []
    for _ in range(moments):
        rows.append([TWO[dict(society[me][0]).get(S, 0)] for me in mes])
        society = step(society, connectors)
    return rows


if __name__ == "__main__":
    print("1. The sentences, in their homes")
    me = a_page("Exhibit_THIRTY-ONE_Me_v*.md")
    naming = a_page("Exhibit_TWENTY_Natural_Naming_v*.md")
    one = a_page("Exhibit_ONE_Natural_Resolver_v*.md")
    intelligence = a_page("Natural_Intelligence_v*.md")
    mathematics = a_page("Exhibit_FOUR_Natural_Mathematics_v*.md")
    the_opening = a_page("incoming/v406all2/The_window_of_the_opening_as_v406all2_goes_on_with_it.md")
    the_draft = a_page("incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md")
    line("A me is a self's universal set." in me, "Exhibit THIRTY-ONE Me: A me is a self's universal set.")
    line("a me's universal set of me-parities going on, now-existing, its prior, now and next same-existing four-cycling" in naming,
         "Exhibit TWENTY Natural Naming, 2.4: a me's universal set of me-parities going on, now-existing")
    line("co me-parity, bi other-parity, tri all-parity" in one, "Exhibit ONE Natural Resolver, a name's three: co me-parity, bi other-parity, tri all-parity")
    line(re.search(r"Its two \w+ are co-parity, the same, \w+ 0, and bi-parity, one inversion\.", intelligence) is not None,
         "Natural Intelligence: co-parity, the same, a 0, and bi-parity, one inversion")
    line("a self's parity and an other's same or not same" in naming, "Natural Naming: a self's parity and an other's same or not same, of co-parity and bi-parity")
    line("3 now-existing co-parity" in mathematics and "in neither self alone" in mathematics, "Exhibit FOUR Natural Mathematics: 3 now-existing co-parity, in neither self alone")
    line(re.search(r"A parity is a me \w+ a set of me: a me is a set of mes", me) is not None, "Exhibit THIRTY-ONE Me, 167: a parity said as a me, and a me as a set of mes")
    line("All-parity is the named universal set of all now-existing me-parities." in the_opening, "the opening's line 31, in v406all2's window: all-parity, the named universal set of all now-existing me-parities")
    line("A partner's word of A cell is a same-existing me-parity now-existing.: is" in the_opening, "a partner's is of 23 November, in v406all2's window: the code's unit, a same-existing me-parity now-existing")
    line("A cell is one is-or-is-not of a co-parity: with is, a 0, its prior same-existing; with is-not, one inversion, other-than-prior." in the_draft,
         "the draft's 1.1, its bold as it is")

    print()
    print("2. By the living code of name 1: a self's prior a set of named parities, and the fifteen lines one of them")
    names, _ = with_nand.resolver(str(root))
    name_1 = names["_1_now_existing"]
    as_observed = with_nand.as_observed
    two, three = (S, "b"), (S, "b", "c")
    cases = 0
    whole = apart = True
    for its_names, most in ((two, 3), (three, 2)):
        things = [(k, v) for k in its_names for v in (1, -1, 0)]
        for values in itertools.product((1, -1, None), repeat=len(its_names)):
            priors = [(k, v) for k, v in zip(its_names, values) if v]
            for how_many in range(most + 1):
                for observing in itertools.product(things, repeat=how_many):
                    cases += 1
                    giving, next_prior = name_1(list(priors), list(observing))
                    by_a_name = [a_named_prior_apart(k, priors, observing) for k in its_names]
                    whole = whole and as_observed(giving) == sorted(g for gives, _ in by_a_name for g in gives)
                    whole = whole and sorted(next_prior) == sorted(p for _, nexts in by_a_name for p in nexts)
                    for k in its_names:
                        others_away = [(name, v) for name, v in observing if name == k]
                        alone = name_1([p for p in priors if p[0] == k], others_away)
                        apart = apart and as_observed([g for g in giving if g[0] == k]) == as_observed(alone[0])
                        apart = apart and sorted(p for p in next_prior if p[0] == k) == sorted(alone[1])
    line(whole, "name 1 with two and with three named priors is the fifteen lines once a named prior: its giving and its next prior, all %d cases" % cases)
    line(apart, "a named prior resolves apart: with all other names away, its giving and its next prior are as they were, all cases")
    a_me_with_two = name_1([(S, 1), ("b", -1)], [(S, 1), ("b", 1)])
    line(as_observed(a_me_with_two[0]) == [("b", 1)] and sorted(a_me_with_two[1]) == [("b", 1), (S, 1)],
         "a self with two named priors, a + and a -, at one now: no one parity. One is same-existing with a 0 given, and one inverts")
    a_prior_of_a_spiral = opening([0], {0: 1})[0][0]
    line(a_prior_of_a_spiral == [(S, 1)] and TWO[1] == (True, False), "in a spiral's opening a self's prior is a set of one named parity, and the fifteen lines open with the parity alone")
    lines_of = {n.name: n for n in ast.walk(ast.parse(Path(with_nand.__file__).read_text(encoding="utf-8"))) if isinstance(n, ast.FunctionDef)}
    called = lambda fn: {n.func.id for n in ast.walk(lines_of[fn]) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    line(draft.ITS_NAME in called("now_with_nand") and draft.ITS_NAME not in called("adding_with_nand") | called("multiplying_with_nand"),
         "v406Reiman's code as it is: its lines as name 1 call the fifteen lines once a name, and its adding and multiplying are nands alone, with no call of them")

    print()
    print("3. One is-or-is-not of a co-parity: a me-parity with what surfaces of others")
    observed_lists = [list(o) for k in range(5) for o in itertools.product((1, -1, 0), repeat=k)]
    in_two = lambda prior, observed: (TWO[prior], [TWO[v] for v in observed])

    def surfacing(observed):
        seen = frozenset(v for v in observed if v)
        return {frozenset([1]): 1, frozenset([-1]): -1}.get(seen, 0)

    with_prior = [(p, o) for p in (1, -1) for o in observed_lists]
    gives = lambda p, o: ONE[the_fifteen_lines(*in_two(p, o))[0]]
    next_prior_of = lambda p, o: ONE[the_fifteen_lines(*in_two(p, o))[1]]
    line(all(gives(p, o) == 0 and next_prior_of(p, o) == p for p, o in with_prior if surfacing(o) == p), "is, the same surfacing as a me-parity's prior: a 0 given, its prior same-existing")
    line(all(gives(p, o) == -p == next_prior_of(p, o) for p, o in with_prior if surfacing(o) != p), "is-not, all other surfacings: one inversion, other-than-prior, all %d cases of a prior" % len(with_prior))
    of_neither_alone = all({gives(p, o) == 0 for o in observed_lists} == {True, False} for p in (1, -1))
    of_neither_alone = of_neither_alone and all({gives(p, o) == 0 for p in (1, -1)} == {True, False} for o in observed_lists if surfacing(o))
    line(of_neither_alone, "of neither alone: a prior is with both an is and an is-not, and a parity surfacing is with both")

    print()
    print("4. v406geodesic2's sentence 42, apart: rounds of 9 and of 10 mes, all their openings")
    ahead = back = a_moment_between = True
    openings = 0
    for n in (9, 10):
        for values in itertools.product((1, -1), repeat=n):
            openings += 1
            rows = priors_along(n, values, 4 * n + 1)
            for now in range(4 * n + 1):
                for j in range(n):
                    if now - 2 * j >= 0:
                        ahead = ahead and all(rows[now][(i + j) % n] == other_thans(rows[now - 2 * j][i], j) for i in range(n))
                    if now + 2 * j <= 4 * n:
                        back = back and all(rows[now][(i - j) % n] == other_thans(rows[now + 2 * j][i], j) for i in range(n))
            a_moment_between = a_moment_between and all(rows[t + 1][i] == its_other_than(rows[t][i]) for t in range(0, 4 * n, 2) for i in range(n))
    line(ahead, "the me j couplings ahead is now, as j other-thans, with a me's prior of 2j moments before: all %d openings, all nows, all j to a round" % openings)
    line(back, "the me j couplings back is now, as j other-thans, with a me's prior of 2j moments on")
    line(a_moment_between, "and a moment between: a me's prior of an odd moment is the other-than of its prior a moment before")
    line(ahead and back and a_moment_between, "with it, on a round at one now: all a me's priors of all its moments are, by other-thans, with the n mes of its round, a me a moment of two")

    print()
    print("5. Rounds of 1 to 5 mes, a me with two named parities: a name apart")

    def two_named_along(n, values, moments, its_names):
        society = {me: ([(name, values[me][k]) for k, name in enumerate((S, "b")) if name in its_names], []) for me in range(n)}
        connectors, rows = a_co_chaining(n), []
        for _ in range(moments):
            rows.append({name: [TWO[dict(society[me][0]).get(name, 0)] for me in range(n)] for name in its_names})
            society = step(society, connectors)
        return rows

    a_name_apart = a_single_path = True
    openings = with_both = 0
    for n in range(1, 6):
        for values in itertools.product(list(itertools.product((1, -1), repeat=2)), repeat=n):
            openings += 1
            with_both += any(a != b for a, b in values)
            rows = two_named_along(n, values, 4 * n + 1, (S, "b"))
            for name in (S, "b"):
                alone = two_named_along(n, values, 4 * n + 1, (name,))
                a_name_apart = a_name_apart and all(rows[t][name] == alone[t][name] for t in range(4 * n + 1))
                a_single_path = a_single_path and all(rows[t][name][i] == its_other_than(rows[t - 2][name][(i - 1) % n]) for t in range(2, 4 * n + 1) for i in range(n))
    line(a_name_apart, "a round of mes with two named parities is two rounds, a name apart: with the other name away a name's priors are as they were, all %d openings" % openings)
    line(a_single_path and with_both > 0, "a name apart is a single path: a me's prior with a name is the other-than of the prior, two moments before, of the me it observes, with %d openings of a me with a + and a - at one now" % with_both)
