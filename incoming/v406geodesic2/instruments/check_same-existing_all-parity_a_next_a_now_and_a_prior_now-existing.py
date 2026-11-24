"""Same-existing all-parity: a next, a now and a prior, now-existing (session v406geodesic2).

A partner's saying of 24 November, with the 27th drawing before a partner, re-said: the universal same-existing me-now fractal
method is same-existing all-parity, and it is all possible next, prior and now universes as now-existing universes.

Executed here, all or none, at two places. By the seventeen names' own table and Exhibit ONE Natural Resolver's sentence of a
name's three: a next, a now and a prior at one moment. And by v406Reiman's cell and step by nand opened from their own file, its
spirals and its tori: a me's three at one now, a round's openings in its now, and the societies with nows merging.

Usage, from the repository's root:
python3 -I incoming/v406geodesic2/instruments/check_same-existing_all-parity_a_next_a_now_and_a_prior_now-existing.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py incoming/v403mgr/The_seventeen_names_in_one_table.csv Exhibit_ONE_Natural_Resolver_v402mgr.md
"""
import csv, importlib.util, re, sys
from itertools import product
from pathlib import Path

spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", sys.argv[1])
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
sys.path.insert(0, str(Path(sys.argv[1]).resolve().parent))
import resolver_as_it_is as as_it_is
TWO, ONE, S = its.TWO, its.ONE, "one"
results = []
def line(name_, ok): results.append((name_, bool(ok)))

# ---------------- the seventeen names: a moment's three ----------------
table = list(csv.reader(open(sys.argv[2], encoding="utf-8")))
column = {h.split(" [")[0]: i for i, h in enumerate(table[0])}
three = {int(r[0]): tuple(r[column["its three: next, now, prior"]].split("-")) for r in table[1:] if r[0].strip().isdigit()}
EIGHT = "co bi co bi co bi tri bi".split()
exhibit_one = Path(sys.argv[3]).read_text(encoding="utf-8")
its_sentence = re.findall(r"[A-Z][a-z]+ name then has its three[^.]*in the order next, now, prior\.", exhibit_one)
the_rolling = re.findall(r"Tri is in the [a-z]+ slot with 7 and 15[^.]*with 9, 17 and 1: the rolling\.", exhibit_one)
line("By the seventeen names' table, a moment a name, a name's three are its next, its now and its prior at one moment: a new prefix as its next, by the eight co bi co bi co bi tri bi, and the name before's next and now one slot on. All seventeen names, and Exhibit ONE Natural Resolver's own sentence of it found",
     sorted(three) == list(range(1, 18)) and "n, a moment" in column and all(three[k][0] == EIGHT[(k - 1) % 8] for k in three)
     and all(three[k] == (EIGHT[(k - 1) % 8],) + three[k - 1][:2] for k in three if k > 1) and len(its_sentence) == 1)
at = lambda slot: [k for k in sorted(three) if three[k][slot] == "tri"]
line("Same-existing all-parity: tri, all-parity, is a next with 7 and 15, a now with 8 and 16, and a prior with 9, 17 and 1, one prefix through three moments, Exhibit ONE's rolling; and co, bi and tri are a next, a now and a prior among the names, all three",
     (at(0), at(1), at(2)) == ([7, 15], [8, 16], [1, 9, 17]) and len(the_rolling) == 1 and all(any(three[k][slot] == w for k in three) for w in ("co", "bi", "tri") for slot in range(3)))
line("Fractal by the eight: 9 to 16 have the threes of 1 to 8, and 17's three is 1's, a next 1", all(three[k + 8] == three[k] for k in range(1, 9)) and three[17] == three[1])

# ---------------- a me on one path: its three at one now ----------------
def moments(couplings, priors, how_many):
    """All mes, moment after moment: a me's prior, and all it observes as given to it."""
    society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: (dict(pr).get(S, 0), tuple(sorted(v for _, v in ob))) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
    return out
rounds = {n: {op: moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 4 * n + 8) for op in product((1, -1), repeat=n)} for n in range(1, 9)}
its_next = lambda ms, n, a, T: -ms[T][(a - 1) % n][0]                             # with the me back of it, as its other-than
its_prior = lambda ms, n, a, T: -ms[T][(a + 1) % n][0]                            # with the me ahead of it, as its other-than
line("A me's three at one now: the me back of it has its next, as its other-than, what a me will be two moments on; it has its now; the me ahead of it has its prior, what it was two moments before. And a parity rolls through them with moments, a me's next, its now two moments on, its prior four moments on. Spirals of 1 to 8 mes, all 510 openings",
     all(its_next(ms, n, a, T) == ms[T + 2][a][0] and its_prior(ms, n, a, T + 2) == ms[T][a][0] and its_next(ms, n, a, T) == its_prior(ms, n, a, T + 4)
         for n, v in rounds.items() for ms in v.values() for T in range(4 * n + 2) for a in range(n)))

# ---------------- all possible prior universes, and a now ----------------
def a_now(m): return tuple(sorted(m.items()))
def nows_apart(societies, T): return [len({a_now(ms[t]) for ms in societies}) for t in range(T)]
line("On one path of mes all with priors, a round's nows are apart at all moments as its openings are: rounds of 2 to 8 mes, 4 to 256 nows at all their moments. All its possible openings are in a now, none merged",
     all(nows_apart(list(v.values()), 4 * n + 8) == [2 ** n] * (4 * n + 8) for n, v in rounds.items() if n > 1))
def comes_again(ms):
    seen = {}
    for t, now in enumerate(a_now(m) for m in ms):
        if now in seen: return seen[now], t - seen[now]
        seen[now] = t
def two_prior_nows(ms):
    before, its_round = comes_again(ms)
    return before == 1 and a_now(ms[1]) == a_now(ms[1 + its_round]) and a_now(ms[0]) != a_now(ms[its_round])
line("One is-or-is-not of a now's prior is open in all those rounds: the now a moment after an opening is a now of the round as well, its prior now one of two, an opening with none observed, or the round's own",
     all(two_prior_nows(ms) for v in rounds.values() for ms in v.values()))
def a_me(prior, observed):
    gives, its_next_prior, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed])
    return ONE[gives], ONE[its_next_prior]
tori = {}
for p, q, T in ((2, 3, 14), (3, 3, 16), (3, 4, 14)):
    mes = tuple((a, b) for a in range(p) for b in range(q))
    tori[(p, q)] = [moments(as_it_is.torus_couplings(p, q), dict(zip(mes, op)), T) for op in product((1, -1), repeat=p * q)]
newborn = {n: [moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 4 * n + 6) for op in product((1, -1, 0), repeat=n)] for n in (2, 3, 4)}
ends = lambda societies: (len(societies), nows_apart(societies, len(societies[0]))[-1])
def most_prior_nows(societies):
    prior_nows = {}
    for ms in societies:
        for t in range(len(ms) - 1): prior_nows.setdefault(a_now(ms[t + 1]), set()).add(a_now(ms[t]))
    return max(len(v) for v in prior_nows.values())
line("Its is-not, on a surface and with a newborn. On a torus of 2 by 3, of 3 by 3 and of 3 by 4, all openings of + and −, nows merge as it settles: 64 openings come to 16 nows, 512 to 68, and 4096 to 200, and of one now's possible prior nows, as many as 5 with the torus of 3 by 3. On one path with mes opening with no prior among them, 9 come to 5, 27 to 15, and 81 to 37",
     [ends(tori[k]) for k in ((2, 3), (3, 3), (3, 4))] == [(64, 16), (512, 68), (4096, 200)] and [ends(newborn[n]) for n in (2, 3, 4)] == [(9, 5), (27, 15), (81, 37)]
     and most_prior_nows(tori[(3, 3)]) == 5)
settled = [{a_now(ms[t]) for ms in tori[(3, 3)]} for t in (12, 13, 14, 15)]
onto = {}
for ms in tori[(3, 3)]:
    for t in (12, 13, 14): onto.setdefault(a_now(ms[t + 1]), set()).add(a_now(ms[t]))
line("A surface settled: the torus of 3 by 3 has 68 nows at a moment, the same 68 with two moments and 70 in all, and a now of them has one prior now of them and one next",
     settled[0] == settled[2] and settled[1] == settled[3] and all(len(x) == 68 for x in settled) and len(set().union(*settled)) == 70 and all(len(v) == 1 for v in onto.values()))
together = lambda societies: any(1 in m[k][1] and -1 in m[k][1] for ms in societies for m in ms for k in m)
line("By the cell's own lines a + and a − observed together surface as a 0, the same to a me as none observed: all it observes, as one. A me of a surface observes two, and a + with a − is among them at some moment; a me of one path observes one",
     all(a_me(p, (1, -1)) == a_me(p, ()) == a_me(p, (0,)) for p in (1, -1)) and together(tori[(3, 3)]) and together(tori[(2, 3)])
     and all(len(m[k][1]) <= 1 for v in rounds.values() for ms in v.values() for m in ms for k in m))

for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
sys.exit(0 if all(ok for _, ok in results) else 1)
