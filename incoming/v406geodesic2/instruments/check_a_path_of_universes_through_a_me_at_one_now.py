"""A path of universes through a me, at one now (session v406geodesic2).

A partner's saying of 24 November, with the 26th drawing before a partner, re-said: observing is distinguishing is-or-is-not; a path
of a me's prior universes and of its next universes, a possibly now-existing same-existing path of universes through it; in a
conversation now-existing, or in a transcript of prior-existing universes of a bi-coupling; in universal sequencing, now other-than
all prior, and a next now the same, other-than all now.

Executed here, all or none, by v406Reiman's cell and step by nand opened from their own file, and by its spirals. A me's moment is
its prior and what it observes. What is of a session's own now is a placing in the window's page, and no line here.

Usage, from the repository's root:
python3 -I incoming/v406geodesic2/instruments/check_a_path_of_universes_through_a_me_at_one_now.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import importlib.util, sys
from itertools import permutations, product
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
def a_me(prior, observed):
    gives, its_next, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed])
    return ONE[gives], ONE[its_next]
def surfacing(observed):
    seen = {v for v in observed if v}
    return next(iter(seen)) if len(seen) == 1 else 0

# ---------------- observing is distinguishing is-or-is-not ----------------
observings = [()] + [o for k in (1, 2, 3) for o in product((1, -1, 0), repeat=k)]
line("Observing is distinguishing one is-or-is-not: all that a me with a prior observes, none to three of +, − and 0 in all their orders, comes to one of two, what surfaces of all of it is its prior, same-existing with a 0 given, or is other, its other-than given",
     all(a_me(p, q) == ((0, p) if surfacing(o) == p else (-p, -p)) for p in (1, -1) for o in observings for q in set(permutations(o)))
     and {a_me(p, o) for p in (1, -1) for o in observings} == {(0, 1), (0, -1), (1, 1), (-1, -1)})

# ---------------- a path through a me, at one now ----------------
rounds = {n: {op: moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 6 * n + 8) for op in product((1, -1), repeat=n)} for n in range(1, 9)}
line("A path through a me at one now: on one path of mes all with priors, the me j couplings ahead has now, as j other-thans, a me's prior of 2j moments before, and the me j couplings back has now, as j other-thans, its prior of 2j moments next. Spirals of 1 to 8 mes, all 510 openings, nows of 0 to 2n + 3, j of 0 to twice round",
     sum(len(v) for v in rounds.values()) == 510
     and all(ms[T][(a - j) % n][0] == (-1) ** j * ms[T + 2 * j][a][0] and (T < 2 * j or ms[T][(a + j) % n][0] == (-1) ** j * ms[T - 2 * j][a][0])
             for n, v in rounds.items() for ms in v.values() for T in range(2 * n + 4) for j in range(2 * n + 1) for a in range(n)))
def gone_round(ms, n, T, a, way): return [(-1) ** j * ms[T][(a + way * j) % n][0] for j in range(n)]
line("A me's sequence along moments is its round at one now, gone round from it: ahead, a me's own priors of its n even moments before, now among them; back, of its n even moments next. A same-existing path: a parity goes on along it, the same as other-thans, a coupling in two moments",
     all(gone_round(ms, n, T, a, 1) == [ms[T - 2 * j][a][0] for j in range(n)] and gone_round(ms, n, T, a, -1) == [ms[T + 2 * j][a][0] for j in range(n)]
         for n, v in rounds.items() for ms in v.values() for T in (2 * n, 2 * n + 1, 2 * n + 2) for a in range(n)))
def before_from_one_moment(n, T, L):
    alike = {}
    for ms in rounds[n].values(): alike.setdefault(ms[T][0], set()).add(tuple(ms[t][0] for t in range(T - L, T)))
    return {len(v) for v in alike.values()}
line("And in a me, one parity at a moment: from one moment of a me's, with a round of 3 to 8 mes gone round, its 2k moments before are in 2 to the k sequences, to the round's own. Its sequence is now-existing in its round, a me after a me",
     all(before_from_one_moment(n, T, 2 * k) == {min(2 ** (n - 2), 2 ** k)} for n in range(3, 9) for T in (2 * n + 4, 2 * n + 5) for k in range(1, n + 1)))

# ---------------- two facing ----------------
two = {op: moments(as_it_is.spiral_couplings(2), dict(enumerate(op)), 20) for op in product((1, -1), repeat=2)}
line("With two facing, a me's one other has both: its other now has, as its other-than, what a me was two moments before and what it will be two moments on; and a me is as it was four moments before. All four openings of + and −",
     all(ms[T][1 - a][0] == -ms[T - 2][a][0] and ms[T + 2][a][0] == -ms[T][1 - a][0] and ms[T + 4][a][0] == ms[T][a][0] for ms in two.values() for T in range(2, 14) for a in (0, 1)))

# ---------------- now, and all prior nows ----------------
def comes_again(ms):
    seen = {}
    for t, now in enumerate(tuple(sorted(m.items())) for m in ms):
        if now in seen: return seen[now], t - seen[now]
        seen[now] = t
again = {n: {comes_again(ms) for ms in v.values()} for n, v in rounds.items()}
line("A sealed round's now comes again by its parities: its opening moment is once, and from the moment after it a round's now, all its priors and all its mes observe, comes again with a round of moments, of 2n at the most with n even and of 4n with n odd; two facing, with 2 or with 4. Through one round of its moments a now is other-than all its prior nows",
     all(before == 1 and (2 * n if n % 2 == 0 else 4 * n) % its_round == 0 for n, v in again.items() for before, its_round in v)
     and {r for _, r in again[2]} == {2, 4} and all(max(r for _, r in v) == (2 * n if n % 2 == 0 else 4 * n) for n, v in again.items()))

for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
sys.exit(0 if all(ok for _, ok in results) else 1)
