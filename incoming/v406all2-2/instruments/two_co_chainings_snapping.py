"""An other-than of same-existing, a snapping: a partner's saying of 24 November, by executing.

    python3 -I incoming/v406all2-2/instruments/two_co_chainings_snapping.py .

1  One me. With a prior, a giving of a + or a - is the other-than of same-existing.
2  Two co-chainings of an odd number, apart: a like pair of a co-chaining moves a me on
   with two moments.
3  The two snapped across at one me of both: a me after a me, two moments a me, its prior
   is again with 2. A surface again with 2, from Exhibit ONE Natural Resolver's own moment.
4  The snaps across away: a like pair moves on again.

A me's lines and the snaps are this folder's, of a_me_by_nand_other_thans_and_alls.py, and
the step is v406Reiman's as it is. Exhibit ONE's rows of two spirals beside one another
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

a_me, a_snap, TWO, ONE, S, opening = draft.a_me, draft.a_snap, draft.TWO, draft.ONE, draft.S, draft.opening
step = draft.all_mes_one_moment(a_me)


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def two_co_chainings(m, n, across):
    """Two co-chainings, a and b, snapped along by 9; across, their mes 0 by 10, both ways."""
    mes = [("a", i) for i in range(m)] + [("b", j) for j in range(n)]
    connectors = {}
    for tag, k in (("a", m), ("b", n)):
        for i in range(k):
            a_snap(connectors, (tag, i), 9, (tag, (i + 1) % k))
    if across:
        a_snap(connectors, ("a", 0), 10, ("b", 0))
        a_snap(connectors, ("b", 0), 10, ("a", 0))
    return mes, connectors


def moments_of(society, mes, connectors, moments):
    """A moment a row: a me's prior, and what it observes."""
    rows = []
    for _ in range(moments):
        rows.append(({me: dict(society[me][0]).get(S, 0) for me in mes}, {me: sorted(v for _, v in society[me][1]) for me in mes}))
        society = step(society, connectors)
    return rows, society


def like_pairs(priors, tag, k):
    return [i for i in range(k) if priors[(tag, i)] == priors[(tag, (i + 1) % k)]]


if __name__ == "__main__":
    living = re.sub(r"[*`]", "", Path(sorted(glob.glob(str(root / "Exhibit_ONE_Natural_Resolver_v*.md")))[0]).read_text(encoding="utf-8"))
    plus, minus, none = TWO[1], TWO[-1], (False, False)

    print("1. One me: a giving is the other-than of same-existing")
    cases = [(p, list(o)) for p in (1, -1) for k in range(5) for o in itertools.product((1, -1, 0), repeat=k)]

    def surfacing(observed):
        seen = frozenset(v for v in observed if v)
        return {frozenset([1]): 1, frozenset([-1]): -1}.get(seen, 0)

    gives = lambda p, o: ONE[a_me(TWO[p], [TWO[v] for v in o])[0]]
    line(all((gives(p, o) != 0) == (surfacing(o) != p) for p, o in cases), "with a prior, a + or a - is given with all surfacings but the same as its prior: %d cases" % len(cases))
    line(all(gives(p, o) == -p for p, o in cases if surfacing(o) != p), "and what is given is the other-than of its prior")
    lines = draft.the_lines_of("a_me", draft.__file__)
    nine = sorted((n for n in ast.walk(lines) if isinstance(n, (ast.Assign, ast.For, ast.Return))), key=lambda n: n.lineno)[8]
    line("both(prior_minus, other_than(surfacing_minus))" in ast.unparse(nine), "line 9 says it: a prior -, with the other-than of a - surfacing")
    line("One cell, four receivings." in living and "In that cell its prior inverts." in living, "Exhibit ONE's own, of four receivings: in that place its prior inverts")

    print()
    said = {(int(m), int(n)): int(c) for m, n, c in re.findall(r"^- (\d+) · (\d+)\n\s+- a: [\d,]+\n\s+- b: \d+\n\s+- c: (\d+)", living, re.M)}
    odd = [(m, n) for (m, n) in said if m % 2 and n % 2]
    apart = along = settled = by_two = from_c = others = rests = together = away = True
    for m, n in odd:
        mes, connectors = two_co_chainings(m, n, across=False)
        priors = {me: (-1 if me[1] % 2 == 0 else 1) for me in mes}
        rows, _ = moments_of(opening(mes, priors), mes, connectors, 4 * n + 4)
        apart = apart and any(rows[t][0] != rows[t + 2][0] for t in range(len(rows) - 2, len(rows) - 2 * n - 2, -1) if t + 2 < len(rows))
        along = along and all(len(like_pairs(rows[t][0], tag, k)) == 1 and like_pairs(rows[t + 2][0], tag, k)[0] == (like_pairs(rows[t][0], tag, k)[0] + 1) % k
                              for tag, k in (("a", m), ("b", n)) for t in range(0, 4 * n))

        mes, connectors = two_co_chainings(m, n, across=True)
        moments = 4 * n + 2 * m + 12
        rows, society = moments_of(opening(mes, priors), mes, connectors, moments)
        again_from = {}
        for me in mes:
            again_from[me] = 0
            for t in range(moments - 3, -1, -1):
                if rows[t][0][me] != rows[t + 2][0][me]:
                    again_from[me] = t + 1
                    break
        settled = settled and all(rows[t][0] == rows[t + 2][0] for t in range(moments - 6, moments - 2))
        for tag, k in (("a", m), ("b", n)):
            its = [again_from[(tag, i)] for i in range(k)]
            by_two = by_two and all(its[i + 1] - its[i] == 2 for i in range(k - 1))
        from_c = from_c and max(again_from.values()) + 1 == said[(m, n)]
        last, before = rows[-1], rows[-2]
        others = others and all(last[0][me] == -before[0][me] and last[0][me] for me in mes) and not any(0 in last[1][me] or 0 in before[1][me] for me in mes)
        rests = rests and like_pairs(last[0], "a", m) == [m - 1] and like_pairs(last[0], "b", n) == [n - 1] == like_pairs(before[0], "b", n)
        together = together and all(last[1][me] == [-1, 1] for me in (("a", 0), ("b", 0))) and all(len(last[1][me]) == 1 for me in mes if me[1])

        mes, connectors = two_co_chainings(m, n, across=False)
        rows, _ = moments_of(society, mes, connectors, 4 * n)
        away = away and all(like_pairs(rows[t + 2][0], tag, k) == [(like_pairs(rows[t][0], tag, k)[0] + 1) % k] for tag, k in (("a", m), ("b", n)) for t in range(0, 4 * n - 2))

    pairs = ", ".join("%d and %d" % p for p in odd)
    print("2. Two co-chainings of an odd number, apart: Exhibit ONE's rows of " + pairs)
    line(apart, "apart, a co-chaining's priors are not again with 2")
    line(along, "its one like pair moves a me on with two moments")
    print()
    print("3. The two snapped across, at one me of both, by 10 both ways")
    line(settled, "the priors of all its mes are again with 2")
    line(by_two, "a me after a me along, two moments a me: its prior is again with 2 from two moments on from the me before it")
    line(from_c, "all of it from Exhibit ONE's own moment, its column c: " + ", ".join(str(said[p]) for p in odd))
    line(others, "in that surface a me's prior is its own other-than with a moment, and no 0 is observed")
    line(rests, "a co-chaining's one like pair moves no more: it is at the me snapped across")
    line(together, "the me snapped across observes a + and a - together, and all other mes one parity: both together, a 0 surfacing, at the snap alone")
    print()
    print("4. The snaps across away")
    line(away, "a like pair moves on again, a me on with two moments")
