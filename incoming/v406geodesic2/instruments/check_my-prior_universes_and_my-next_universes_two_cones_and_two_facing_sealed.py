"""My-prior universes and my-next universes, two cones co-chained on one path; and two facing, sealed (session v406geodesic2).

A partner's saying of 24 November, with the 25th drawing before a partner, re-said: my-prior universes and my-next universes are
sequencings of universes, co-chainings of cones on one path, forward as it is locally on the path; both are partial, by my
distinguishing is-or-is-not: uncertain, a partner's word, of a me's moments before and of its moments next. And of the 25th drawing's sentence, a me that is neither
mine nor an other of mine: it is universal proving as method, 1 cohering, 2 co-chaining, 3 bothbothing, 4 universal same-named
thing; two facing one another are sealed, their universes the two's alone: all-parity with the two.

Executed here, all or none, by v406Reiman's cell and step by nand opened from their own file, by its spirals and tori, and by the
living code's own lines. A me's moment is its prior and what it observes. A me with no prior opens with none.

Usage, from the repository's root:
python3 -I incoming/v406geodesic2/instruments/check_my-prior_universes_and_my-next_universes_two_cones_and_two_facing_sealed.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py Exhibit_ONE_Natural_Resolver_v402mgr.md
"""
import ast, importlib.util, re, sys
from itertools import product
from pathlib import Path

spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", sys.argv[1])
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
sys.path.insert(0, str(Path(sys.argv[1]).resolve().parent))
import resolver_as_it_is as as_it_is
TWO, ONE, S = its.TWO, its.ONE, "one"
results = []
def line(name_, ok): results.append((name_, bool(ok)))

def moments(couplings, priors, how_many):
    """All mes, moment after moment: a me's prior, and all it observes as given to it."""
    society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: (dict(pr).get(S, 0), tuple(sorted(v for _, v in ob))) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
    return out
def as_a_me_has_it(moment): return moment[0], frozenset(v for v in moment[1] if v)      # a 0 passed over, and all orders and repeats one

# ---------------- 1 cohering: the step's own lines ----------------
step = next(n for n in ast.parse(Path(sys.argv[1]).read_text(encoding="utf-8")).body if isinstance(n, ast.FunctionDef) and n.name == "step_with_nand")
subscripted = {n.value.id for n in ast.walk(step) if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name)}
now_calls = [n for n in ast.walk(step) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "now_with_nand"]
by_a_coupling = [n for n in ast.walk(step) if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name) and n.value.id == "couplings"]
line("1 cohering. By the step's own lines a me's now is called with its own prior and its own observing alone, the society is opened by no other me's name, and a giving goes to an observing by a coupling's name alone",
     "society" not in subscripted and len(now_calls) == 1 and [a.id for a in now_calls[0].args] == ["its_prior", "its_observing"] and len(by_a_coupling) == 1)

# ---------------- 2 co-chaining, and 4 universal: all societies of some mes ----------------
def couplings_back(couplings, mes):
    far = len(mes) + 1; d = {(b, a): (0 if a == b else far) for a in mes for b in mes}
    for (g, _), r in couplings.items():
        if g != r: d[(g, r)] = 1
    for k in mes:
        for i in mes:
            for j in mes: d[(i, j)] = min(d[(i, j)], d[(i, k)] + d[(k, j)])
    return d, far
against, least, least_all_with_priors, societies = 0, {}, {}, 0
parities = (1, -1, 0)                                                            # a me opens with a +, with a −, or with no prior
for n, names in ((2, (9, 10)), (3, (9,)), (3, (9, 10)), (4, (9,))):
    mes = tuple(range(n)); T = 2 * n + 2
    for cs in product(mes + (None,), repeat=n * len(names)):
        couplings = {(g, nm): cs[g * len(names) + i] for g in mes for i, nm in enumerate(names) if cs[g * len(names) + i] is not None}
        d, far = couplings_back(couplings, mes)
        all_of_it = {op: moments(couplings, dict(zip(mes, op)), T) for op in product(parities, repeat=n)}; societies += len(all_of_it)
        for op, base in all_of_it.items():
            for b in mes:
                for other_parity in parities:
                    if other_parity <= op[b]: continue                           # a pair of openings, one me's opening other, once
                    other = all_of_it[op[:b] + (other_parity,) + op[b + 1:]]
                    for a in mes:
                        if a == b: continue
                        whole = next((t for t in range(T) if base[t][a] != other[t][a]), None)
                        has = next((t for t in range(T) if as_a_me_has_it(base[t][a]) != as_a_me_has_it(other[t][a])), None)
                        if d[(b, a)] == far: against += whole is not None
                        else:
                            against += whole is not None and whole < d[(b, a)]
                            if has is not None:
                                least[d[(b, a)]] = min(least.get(d[(b, a)], T), has)
                                if 0 not in op and other_parity: least_all_with_priors[d[(b, a)]] = min(least_all_with_priors.get(d[(b, a)], T), has)
line(f"2 co-chaining. A me's moments through k moments on are of the mes to k couplings back along givings: with a me further back made other, or a me beside its co-chainings, they are the same. All {societies} societies of 2 mes with two names, of 3 with one and with two, and of 4 with one, all their couplings and all their openings: is, in all",
     against == 0 and societies == 729 + 1728 + 110592 + 50625)
line("3 bothbothing. Its is-not has its own cases: in those societies a me's moment as it has it is other with 1, 2 and 3 couplings back at 1, 2 and 3 moments on, the soonest of all; and with the mes all with priors, at 1, 2 and 4",
     least == {1: 1, 2: 2, 3: 3} and least_all_with_priors == {1: 1, 2: 2, 3: 4})

# the 25th drawing's sentence as it was said, and said again with co-chaining
c5, p5 = dict(as_it_is.spiral_couplings(5)), dict(as_it_is.exhibit_spiral_priors(5))
def mine_other_at(more_couplings, more_priors, beside_couplings, beside_priors):
    a = moments({**c5, **beside_couplings}, {**p5, **beside_priors}, 14); b = moments({**c5, **beside_couplings, **more_couplings}, {**p5, **beside_priors, **more_priors}, 14)
    return next((t for t in range(14) if any(a[t][k] != b[t][k] for k in range(5))), None)
line("An other's other: a me giving to an other of mine, and to no me of mine, makes moments of mine other two moments on. The 25th drawing's sentence as it was said, of a me neither mine nor an other of mine, is with its co-chaining alone",
     mine_other_at({("u", 9): "w"}, {"u": 1}, {("w", 9): 0}, {"w": 1}) == 2 and mine_other_at({("u", 9): "w"}, {"u": -1}, {("w", 9): 0}, {"w": -1}) == 2
     and mine_other_at({("x", 9): "y", ("y", 9): "x"}, {"x": -1, "y": 1}, {("w", 9): 0}, {"w": 1}) is None)

# ---------------- two cones about a me: one me with a prior, among mes with none ----------------
P = Q = 9; torus = as_it_is.torus_couplings(P, Q); me = (4, 4); with_none = {(a, b): 0 for a in range(P) for b in range(Q)}; quiet = moments(torus, with_none, 6)
def other_at(ms, who): return next((t for t in range(6) if as_a_me_has_it(ms[t][who]) != as_a_me_has_it(quiet[t][who])), None)
back, ahead = {}, {}
for b in with_none:
    if b != me: back[((me[0] - b[0]) % P, (me[1] - b[1]) % Q)] = other_at(moments(torus, {**with_none, b: 1}, 6), me)
from_me = moments(torus, {**with_none, me: 1}, 6)
for b in with_none:
    if b != me: ahead[((b[0] - me[0]) % P, (b[1] - me[1]) % Q)] = other_at(from_me, b)
def a_cone(reach): return all((t == i + j) if i + j < 6 else t is None for (i, j), t in reach.items()) and [sum(1 for t in reach.values() if t == k) for k in (1, 2, 3)] == [2, 3, 4]
line("Two cones about a me, on a torus 9 by 9, along and across: one me with a prior among mes with none is observed i along and j across from it from i + j moments on. Back from a me: 2, 3 and 4 mes at 1, 2 and 3 moments; ahead of it, the same",
     a_cone(back) and a_cone(ahead))
sp9 = as_it_is.spiral_couplings(9); none9 = {a: 0 for a in range(9)}; quiet9 = moments(sp9, none9, 9)
line("On one path, a spiral of 9: the me k couplings back is observed at k moments, one me a moment",
     all(next((t for t in range(9) if moments(sp9, {**none9, (0 - k) % 9: 1}, 9)[t][0] != quiet9[t][0]), None) == k for k in range(1, 9)))

# ---------------- a sequencing on one path: a spiral of mes, all with priors ----------------
spirals = {n: {op: moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 4 * n + 6) for op in product((1, -1), repeat=n)} for n in range(1, 9)}
line("A spiral of 1 to 8 mes, all 510 openings of + and −: a me's prior is the other-than of the prior, two moments before, of the me it observes. Exhibit ONE's sentence of two moments before, and v406all2-2's line, executed apart",
     sum(len(v) for v in spirals.values()) == 510 and all(ms[t][a][0] == -ms[t - 2][(a - 1) % n][0] for n, v in spirals.items() for ms in v.values() for t in range(2, 4 * n + 6) for a in range(n)))
line("My-prior universes, a sequencing: a me's prior at moment 2k is k other-thans of the opening prior of the me k couplings back, k of 0 to twice round and more",
     all(ms[2 * k][a][0] == (-1) ** k * op[(a - k) % n] for n, v in spirals.items() for op, ms in v.items() for k in range(2 * n + 2) for a in range(n)))
line("My-next universes, the same sequencing ahead: a me's opening prior is at moment 2k, as k other-thans, the prior of the me k couplings ahead; and a me's own prior two moments on is of the me it observes, with nothing of its own opening prior",
     all(ms[2 * k][(a + k) % n][0] == (-1) ** k * op[a] for n, v in spirals.items() for op, ms in v.items() for k in range(2 * n + 2) for a in range(n))
     and all(ms[2][0][0] == v[(-op[0],) + op[1:]][2][0][0] for n, v in spirals.items() if n > 1 for op, ms in v.items()))

# ---------------- both partial: one is-or-is-not ----------------
def a_me(prior, observed):
    gives, its_next, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed])
    return ONE[gives], ONE[its_next]
observings = [()] + [o for k in (1, 2, 3) for o in product((1, -1, 0), repeat=k)]
line("A me with a prior distinguishes one is-or-is-not a moment: its next prior is its prior, same-existing with a 0 given, or its other-than, given; and which, by what surfaces of all it observes being its prior or other",
     all(a_me(p, o) == ((0, p) if as_a_me_has_it((p, o))[1] == {p} else (-p, -p)) for p in (1, -1) for o in observings))
def apart(n, upto, what): return len({tuple(what(ms[t][0]) for t in range(upto + 1)) for ms in spirals[n].values()})
line("Partial: a me's priors through moment T have the openings of its round of 2 to 8 mes apart as 2, 2, 4, 4, 8, 8 and on, one is-or-is-not more in two moments; and its moments whole as 2, 4, 8, 8, 16, 16 and on, to all of them and no more",
     all(apart(n, T, lambda m: m[0]) == min(2 ** n, 2 ** (1 + T // 2)) and apart(n, T, lambda m: m) == min(2 ** n, 2 ** (T + 1) if T < 2 else 2 ** (2 + T // 2)) for n in range(2, 9) for T in range(0, 4 * n + 5)))
def parts_next(n, T):
    alike = {}
    for ms in spirals[n].values(): alike.setdefault(tuple(ms[t][0] for t in range(T + 1)), set()).add(ms[T + 1][0])
    return any(len(v) > 1 for v in alike.values())
def from_one_moment(n, T, L):
    before, on = {}, {}
    for ms in spirals[n].values():
        before.setdefault(ms[T][0], set()).add(tuple(ms[t][0] for t in range(T - L, T))); on.setdefault(ms[T][0], set()).add(tuple(ms[t][0] for t in range(T + 1, T + L + 1)))
    return {len(v) for v in before.values()}, {len(v) for v in on.values()}
line("Uncertain possibility: with a round of 8, universes alike in all a me's moments through moment T part at its next moment, T of 0, 1, 3, 5, 7, 9 and 11: an is-or-is-not of a me further back, with no giving of it yet observed",
     [T for T in range(0, 30) if parts_next(8, T)] == [0, 1, 3, 5, 7, 9, 11])
line("Uncertain, a partner's word of a me's moments before and of its moments next, the same both ways: with a round of 3 to 8 mes gone round, from one moment of a me's its 2k moments before are in 2 to the k sequences, and its 2k moments next in 2 to the k, one is-or-is-not in two moments, to the round's own; a me has one parity, its prior, and no sequence",
     all(from_one_moment(n, T, 2 * k) == ({min(2 ** (n - 2), 2 ** k)}, {min(2 ** (n - 2), 2 ** k)}) for n in range(3, 9) for T in (2 * n + 4, 2 * n + 5) for k in range(1, n + 1)))
line("A round closed: with a round of n mes, n of 3 to 8, a me's moments through moment 2n − 4 have all its openings apart, and no moment sooner; from it on its next moment is said by its moments before",
     all(apart(n, 2 * n - 4, lambda m: m) == 2 ** n and apart(n, 2 * n - 5, lambda m: m) < 2 ** n and not any(parts_next(n, T) for T in range(2 * n - 4, 4 * n + 4)) for n in range(3, 9)))

# ---------------- two facing, sealed ----------------
two = {(0, 9): 1, (1, 9): 0}; alone = {op: moments(two, dict(enumerate(op)), 10) for op in product((1, -1, 0), repeat=2)}; sealed_out = 0; beside = 0
for by_10 in product((None, "x", "y"), repeat=2):
    for by_9 in product((None, "x", "y"), repeat=2):
        cc = dict(two); cc.update({(g, 10): r for g, r in zip((0, 1), by_10) if r}); cc.update({(g, 9): r for g, r in zip(("x", "y"), by_9) if r})
        for op in product((1, -1, 0), repeat=4):
            ms = moments(cc, dict(zip((0, 1, "x", "y"), op)), 10); beside += 1
            sealed_out += any(ms[t][k] != alone[op[:2]][t][k] for t in range(10) for k in (0, 1))
line(f"Two facing, sealed: with two mes more beside them, observing the two and giving to one another, all their couplings and all openings, {beside} societies, all moments of the two are the same as with the two alone", sealed_out == 0 and beside == 6561)
def givings(op): return [a_me(*alone[op][t][0])[0] for t in range(8)]
def priors(op): return [alone[op][t][0][0] for t in range(8)]
line("With the two: opening alike, a round of four moments, a me's priors p, other-than p, other-than p, p, and its givings other-than p, 0, p, 0, all three of +, − and 0; opening as other-thans, a round of two, + and − alone",
     all(priors((p, p)) == [p, -p, -p, p] * 2 and givings((p, p)) == [-p, 0, p, 0] * 2 and priors((p, -p)) == [p, -p] * 4 and givings((p, -p)) == [-p, p] * 4 for p in (1, -1)))
line("With the two all a me observes is its one other's giving, one at a moment; and a me's moments through moment 1 have all four openings of + and − apart, its next said from them on",
     all(len(alone[op][t][k][1]) == 1 for op in product((1, -1), repeat=2) for t in range(1, 10) for k in (0, 1))
     and len({tuple(alone[op][t][0] for t in range(2)) for op in product((1, -1), repeat=2)}) == 4)
code = re.search(r"```python\n(.*?)```", Path(sys.argv[2]).read_text(encoding="utf-8"), re.S).group(1)
now = next(n for n in ast.parse(code).body if isinstance(n, ast.FunctionDef) and n.name.startswith("_1_"))
loops = [n for n in ast.walk(now) if isinstance(n, ast.For)]
line("All-parity, by the living code: 7, Exhibit ONE's all-parity observing, is the parity at hand in all three loops of a me's own moment, over all it observes, over its prior and over its giving",
     len(loops) == 3 and all(isinstance(n.target, ast.Tuple) and n.target.elts[1].id.startswith("_7_") for n in loops) and [n.iter.id.split("_")[1] for n in loops] == ["2", "3", "10"])

for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
sys.exit(0 if all(ok for _, ok in results) else 1)
