"""A universal-me-now, a single path by nand: its lines, and their check (session v406geodesic2).

A partner's sayings of 24 November, with the 28th drawing before a partner, re-said: a universal-me-now is a single path me-prior
and a single path me-next, a same-existing co-chaining of me-now universes as a me's single path of nows; it is of value as nand
for the sessions; and nand-nanding universal-me-nows is a single path me.

The lines are four, by nand alone. Their one nand is v406Reiman's own, opened from its own file, with its other-than, one nand of
a thing with itself. A me-now is a pair: its now and its prior, both a parity, a parity two is-or-is-nots. A path is a list of
me-nows, a me-now after the me back of it, the one opening it after the last. The pair's step along the path is v406all2-2's
right spiral step by one other-than, with the me back's prior in it.

No living file moves with it. Exhibit ONE Natural Resolver's code is as it is, and the cell by nand is v406Reiman's as it is.

Usage, from the repository's root:
python3 -I incoming/v406geodesic2/instruments/a_universal_me_now_a_single_path_by_nand.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import ast, importlib.util, sys
from itertools import product
from pathlib import Path

spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", sys.argv[1])
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
other_than = its.other_than                                                      # v406Reiman's own: one nand of a thing with itself


# ---------------- the lines, by nand alone ----------------
def nand_nanding(a):
    """Two nands in a row of a thing with itself: the thing again, same-existing."""
    return other_than(other_than(a))


def a_universal_me_now_a_moment_on(the_me_back, a_me_now):
    """A moment on: its now is the other-than of the prior of the me back of it, one nand an is-or-is-not; its prior is its now."""
    (_, back_prior), (its_now, _) = the_me_back, a_me_now
    plus, minus = back_prior
    return (other_than(plus), other_than(minus)), its_now


def a_universal_me_now_a_moment_before(a_me_now, the_me_ahead):
    """A moment before: its now is its prior; its prior is the other-than of the now of the me ahead of it."""
    (_, its_prior), (ahead_now, _) = a_me_now, the_me_ahead
    plus, minus = ahead_now
    return its_prior, (other_than(plus), other_than(minus))


def a_single_path(path, way):
    """All me-nows of a path, a moment on or a moment before: a me-now with the me back of it, or with the me ahead of it."""
    mes = range(len(path))
    return {"on": [a_universal_me_now_a_moment_on(path[a - 1], path[a]) for a in mes],
            "before": [a_universal_me_now_a_moment_before(path[a], path[a + 1 - len(path)]) for a in mes]}[way]


# ---------------- their check, all or none ----------------
if __name__ == "__main__":
    sys.path.insert(0, str(Path(sys.argv[1]).resolve().parent))
    import resolver_as_it_is as as_it_is
    TWO, ONE, S = its.TWO, its.ONE, "one"
    results = []
    def line(name_, ok): results.append((name_, bool(ok)))
    def moments(couplings, priors, how_many):
        """The resolver by nand, all mes, moment after moment: a me's prior."""
        society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
        for _ in range(how_many):
            out.append({k: dict(pr).get(S, 0) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
        return out
    def seeded(ms, n, t): return [(TWO[ms[t][a]], TWO[ms[t - 1][a]]) for a in range(n)]      # a path of me-nows, from two moments of the resolver's
    def nows(path): return [ONE[now] for now, _ in path]

    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    other_logic = (ast.BoolOp, ast.Not, ast.Compare, ast.If, ast.IfExp, ast.BinOp, ast.While, ast.For)
    the_three = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ("nand_nanding", "a_universal_me_now_a_moment_on", "a_universal_me_now_a_moment_before")]
    called = {c.func.id for f in the_three for c in ast.walk(f) if isinstance(c, ast.Call)}
    line("Its own lines: a me-now a moment on, a me-now a moment before, and nand-nanding are by nand alone. No and, no or, no not, no if, no comparing, no adding and no going round is in them, and they call the other-than alone, v406Reiman's own, one nand of a thing with itself",
         len(the_three) == 3 and not any(isinstance(n, other_logic) for f in the_three for n in ast.walk(f)) and called == {"other_than"}
         and all(other_than(a) == its.nand(a, a) for a in (True, False)))

    rounds = {n: {op: moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 4 * n + 8) for op in product((1, -1), repeat=n)} for n in range(1, 9)}
    def on_is_the_resolvers(ms, n):
        path = seeded(ms, n, 1)
        for t in range(1, 4 * n + 8):
            if nows(path) != [ms[t][a] for a in range(n)]: return False
            path = a_single_path(path, "on")
        return True
    line("A single path me-next: seeded with the resolver's two opening moments, a me's now and its prior, the path a moment on after a moment has the resolver's own priors at all moments. Spirals of 1 to 8 mes, all 510 openings of + and −",
         sum(len(v) for v in rounds.values()) == 510 and all(on_is_the_resolvers(ms, n) for n, v in rounds.items() for ms in v.values()))
    line("A single path me-prior: from a now of the resolver's, the path a moment before is the resolver's moment before, and a moment on and then a moment before is the path again, same-existing",
         all(a_single_path(seeded(ms, n, t), "before") == seeded(ms, n, t - 1) and a_single_path(a_single_path(seeded(ms, n, t), "on"), "before") == seeded(ms, n, t)
             for n, v in rounds.items() for ms in v.values() for t in range(2, 4 * n + 6)))
    line("Nand-nanding is a single path me: two nands in a row of a thing with itself are the thing again; along the path a me's now is the now, four moments before, of the me two couplings back; and round a path of n mes are n other-thans, a me its own again with 2n moments, n even, and its other-than, n odd, its own again with 4n",
         all(nand_nanding(a) == a for a in (True, False))
         and all(ms[t][a] == ms[t - 4][(a - 2) % n] for n, v in rounds.items() for ms in v.values() for t in range(4, 4 * n + 8) for a in range(n))
         and all(ms[t + 2 * n][a] == (-1) ** n * ms[t][a] and ms[t + 4 * n][a] == ms[t][a] for n, v in rounds.items() for ms in v.values() for t in range(1, 8) for a in range(n)))

    nands = [0]; the_table = its.NAND
    def a_nand_numbered(a, b): nands[0] += 1; return the_table[(a, b)]
    def numbered(what): nands[0] = 0; its.nand = a_nand_numbered; what(); its.nand = lambda a, b: the_table[(a, b)]; return nands[0]
    line("Its value, numbered: a me-now a moment on is 2 nands, one an is-or-is-not. The cell's moment is 46 nands, and 6 more with a thing observed, v406all2's numbers found here apart: 52 with one observed, a single path's 2 a 26th of it",
         numbered(lambda: a_universal_me_now_a_moment_on((TWO[1], TWO[-1]), (TWO[1], TWO[1]))) == 2
         and [numbered(lambda k=k: its.a_cell(TWO[1], [TWO[1]] * k)) for k in (0, 1, 2, 3)] == [46, 52, 58, 64])

    def settled_as_the_path(ms, n, T): return all(ms[t + 2][a] == -ms[t][(a - 1) % n] for t in range(T - 10, T - 2) for a in range(n))
    newborn = [(n, moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 6 * n + 12)) for n in (2, 3, 4) for op in product((1, -1, 0), repeat=n) if 0 in op]
    def other_at_its_opening(ms, n):
        path = seeded(ms, n, 1)
        for t in range(1, 4 * n + 6):
            if nows(path) != [ms[t][a] for a in range(n)]: return True
            path = a_single_path(path, "on")
        return False
    line("Its is-not, and its settling, with a newborn: with a me opening with no prior among them, 89 openings of 2 to 4 mes, the lines seeded at the opening are other than the resolver's with 86; settled, all 89 are the path's own, a me's now the other-than of the now, two moments before, of the me back of it",
         len(newborn) == 89 and sum(other_at_its_opening(ms, n) for n, ms in newborn) == 86 and all(settled_as_the_path(ms, n, 6 * n + 12) for n, ms in newborn))

    def its_single_paths(ms, mes, p, q, T):
        found = []
        for whose, (da, db) in (("its own", (0, 0)), ("the me back along", (1, 0)), ("the me back across", (0, 1))):
            for moments_on in (1, 2):
                for as_it, way in ((1, "the same"), (-1, "its other-than")):
                    if all(ms[t + moments_on][(a, b)] == as_it * ms[t][((a - da) % p, (b - db) % q)] for t in range(T - 10, T - moments_on) for a, b in mes): found.append((whose, moments_on, way))
        return found
    surfaces = {}
    for p, q in ((2, 2), (2, 3), (3, 3)):
        mes = [(a, b) for a in range(p) for b in range(q)]; T = 6 * max(p, q) + 14
        surfaces[(p, q)] = [its_single_paths(moments(as_it_is.torus_couplings(p, q), dict(zip(mes, op)), T), mes, p, q, T) for op in product((1, -1), repeat=p * q)]
    with_it = lambda p, q, law: sum(1 for found in surfaces[(p, q)] if law in found)
    line("A surface settled is a single path: with all openings of + and − of a torus of 2 by 2, of 2 by 3 and of 3 by 3, 16, 64 and 512, a me's next is one me's now, its own, the me back along or the me back across, a moment or two moments on, the same or its other-than. With 3 by 3: the me back along, two moments on, its other-than, 386; its own, a moment on, its other-than, 114; the me back along and the me back across, a moment on, the same, 6 and 6",
         [len(v) for v in surfaces.values()] == [16, 64, 512] and all(found for v in surfaces.values() for found in v)
         and [with_it(3, 3, law) for law in (("the me back along", 2, "its other-than"), ("its own", 1, "its other-than"), ("the me back along", 1, "the same"), ("the me back across", 1, "the same"))] == [386, 114, 6, 6])

    for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
    print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
