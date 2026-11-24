"""Nand-nanding, its is and its is-not explored forward (session v406geodesic2).

A partner's word of 24 November, with the 29th drawing before a partner, re-said: to go on exploring forward into the is and the
is-not of a resolving concern; one of the two is incohering; and then to go on resolving forward.

The concern is the 29th drawing's. Its is: nand-nanding is an other-than of an other-than along the path, a me two couplings on,
with four moments, a me again. Its is-not: nand-nanding is an all of two me-nows, the code's both. Both are executed forward here,
all or none, by v406Reiman's nand, its other-than, its both and its cell, opened from their own file, and by this folder's lines
of a single path. With them, v406all2's both link after link and v406all2-2's co-parity, said at the exchange, are executed apart.

Usage, from the repository's root:
python3 -I incoming/v406geodesic2/instruments/check_nand-nanding_its_is_and_its_is-not_explored_forward.py incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
"""
import importlib.util, sys
from itertools import product
from pathlib import Path

sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", sys.argv[1])
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
sys.path.insert(0, str(Path(sys.argv[1]).resolve().parent))
import resolver_as_it_is as as_it_is
nand, other_than, both, TWO, ONE, S = its.nand, its.other_than, its.both, its.TWO, its.ONE, "one"
results = []
def line(name_, ok): results.append((name_, bool(ok)))
def moments(couplings, priors, how_many):
    """The resolver by nand, all mes, moment after moment: a me's prior."""
    society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: dict(pr).get(S, 0) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
    return out
NEITHER, TOGETHER = (False, False), (True, True)                                 # a 0 two ways: neither a + nor a −, and a + with a − together

# ---------------- two nands in a row, by what they are of ----------------
OF_TWO = {"an all": lambda a, b: nand(nand(a, b), nand(a, b)),
          "an either": lambda a, b: nand(nand(a, a), nand(b, b)),
          "a nand of two, and a nand with the one": lambda a, b: nand(nand(a, b), a),
          "a nand of two, and a nand with the other": lambda a, b: nand(nand(a, b), b),
          "an other-than of the one, and a nand with the other": lambda a, b: nand(nand(a, a), b),
          "an other-than of the other, and a nand with the one": lambda a, b: nand(nand(b, b), a)}
def of_two(form, p, q): return (OF_TWO[form](TWO[p][0], TWO[q][0]), OF_TWO[form](TWO[p][1], TWO[q][1]))
alike, others = [(1, 1), (-1, -1)], [(1, -1), (-1, 1)]
line("Two nands in a row, by what they are of. Of a thing with itself, the thing again. Of two things, six forms: an all and an either are the thing again with the two the same and a 0 with two other-thans, neither or both together; the four with a nand of two and a nand with one of them are a 0 with the two the same and one of the two with other-thans",
     all(other_than(other_than(a)) == a for a in (True, False)) and all(its.both(a, b) == OF_TWO["an all"](a, b) and its.either(a, b) == OF_TWO["an either"](a, b) for a in (True, False) for b in (True, False))
     and all(of_two(f, p, p) == TWO[p] for f in ("an all", "an either") for p in (1, -1)) and all(of_two("an all", p, q) == NEITHER and of_two("an either", p, q) == TOGETHER for p, q in others)
     and all(of_two(f, p, p) == TOGETHER and ONE[of_two(f, p, q)] in (p, q) for f in list(OF_TWO)[2:] for p, q in others))

# ---------------- its is-not, explored forward: of two me-nows ----------------
ABOUT_A_ME = {"a me's now": (0, 0), "a me's prior": (0, -1), "the me back's now": (-1, 0), "the me back's prior": (-1, -1), "the me ahead's now": (1, 0), "the me ahead's prior": (1, -1)}
rounds = {n: [moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 4 * n + 8) for op in product((1, -1), repeat=n)] for n in range(1, 9)}
def a_parity_at_all_moments(form, one, other):
    (da, dt), (db, du) = ABOUT_A_ME[one], ABOUT_A_ME[other]
    return all(of_two(form, ms[t + dt][(a + da) % n], ms[t + du][(a + db) % n]) not in (NEITHER, TOGETHER) for n, v in rounds.items() if n > 2 for ms in v for t in range(2, 4 * n + 4) for a in range(n))
line("Its is-not, explored forward, is incohering. Of two me-nows of a path, a me's now, its prior, the me back's two and the me ahead's two, any two of the six with any form of the six, 180 ways: none is a parity at all moments, and none is a single path me. Rounds of 3 to 8 mes, all their openings",
     sum(1 for f in OF_TWO for u in ABOUT_A_ME for v in ABOUT_A_ME if u != v) == 180 and not any(a_parity_at_all_moments(f, u, v) for f in OF_TWO for u in ABOUT_A_ME for v in ABOUT_A_ME if u != v))
def a_me(prior, observed):
    gives, its_next, _, _ = its.a_cell(TWO[prior], [TWO[o] for o in observed]); return ONE[gives], ONE[its_next]
def surfacing(observed):
    seen = {v for v in observed if v}; return next(iter(seen)) if len(seen) == 1 else 0
observings = [()] + [o for k in (1, 2) for o in product((1, -1, 0), repeat=k)]
line("What an all of two is, of a me's prior and what surfaces: the prior again with the two the same, the cell giving a 0, same-existing; and neither with the two other, the cell giving its other-than. One is-or-is-not of two at a moment, v406all2-2's co-parity, executed apart; and no path",
     all((ONE[of_two("an all", p, surfacing(o))] == p) == (a_me(p, o) == (0, p)) and (of_two("an all", p, surfacing(o)) == NEITHER) == (a_me(p, o) == (-p, -p)) for p in (1, -1) for o in observings))

# ---------------- its is, explored forward: of a me-parity with itself, along the path ----------------
def nands_in_a_row(a, how_many):
    for _ in range(how_many): a = other_than(a)
    return a
line("Its is, explored forward, is cohering. An even number of nands in a row of a thing with itself is the thing again, and an odd number its other-than, 1 to 16. Along the path a me's now is the now, 4k moments before, of the me 2k couplings back, and the other-than of the now, 4k + 2 moments before, of the me 2k + 1 back: k to a round, rounds of 1 to 8 mes, all 510 openings",
     all(nands_in_a_row(a, k) == (a if k % 2 == 0 else other_than(a)) for a in (True, False) for k in range(1, 17)) and sum(len(v) for v in rounds.values()) == 510
     and all(ms[t][a] == (-1) ** j * ms[t - 2 * j][(a - j) % n] for n, v in rounds.items() for ms in v for j in range(1, n + 1) for t in range(2 * j, 4 * n + 8) for a in range(n)))
line("A path closes by nand-nanding: round a path of n mes are n nands; with n even they are nand-nandings, a me its own again with 2n moments; with n odd, once round is its other-than and twice round is n nand-nandings, a me its own again with 4n. A path of one, a me after itself, is its own again with four moments",
     all(ms[t + 2 * n][a] == (-1) ** n * ms[t][a] and ms[t + 4 * n][a] == ms[t][a] for n, v in rounds.items() for ms in v for t in range(1, 8) for a in range(n))
     and all(ms[t + 2][0] == -ms[t][0] and ms[t + 4][0] == ms[t][0] for ms in rounds[1] for t in range(1, 8)))

# ---------------- an all of its links: a path with all ----------------
def a_link(ms, n, a, t): return ms[t + 1][a] == -ms[t - 1][(a - 1) % n]                   # a me's now a moment on, the other-than of the prior of the me back of it
def an_all(things):
    with_all = True
    for thing in things: with_all = both(with_all, thing)
    return with_all
newborn = [(n, moments(as_it_is.spiral_couplings(n), dict(enumerate(op)), 6 * n + 12)) for n in (2, 3, 4) for op in product((1, -1, 0), repeat=n) if 0 in op]
def with_all_by_moments(ms, n): return [an_all(a_link(ms, n, a, t) for a in range(n)) for t in range(1, 6 * n + 10)]
line("An all in a row of a path's links, v406all2's both link after link, executed apart: a path is with all its links at all moments, rounds of 1 to 8 mes, all openings. With a newborn, a me opening with no prior, a path is with not all at its opening, 86 of 89 openings, and with all from its settling on, all 89: an is-or-is-not of a single path, by nand",
     all(an_all(a_link(ms, n, a, t) for a in range(n)) for n, v in rounds.items() for ms in v for t in range(1, 4 * n + 6))
     and len(newborn) == 89 and all(all(with_all_by_moments(ms, n)[-8:]) for n, ms in newborn) and sum(1 for n, ms in newborn if not all(with_all_by_moments(ms, n)[:2])) == 86)

# ---------------- resolving forward, the same way: at a place, a corus ----------------
line("A me's own inverting, one nand of its own me-parity: on a path, a me's prior of an odd moment is the other-than of its prior a moment before, at all odd moments, rounds of 1 to 8 mes, all openings; v406all2-2's moment between, executed apart. A me-parity of a path is a + or a − at all its moments, and at none a 0",
     all(ms[t][a] == -ms[t - 1][a] for n, v in rounds.items() for ms in v for t in range(1, 4 * n + 8, 2) for a in range(n)) and all(ms[t][a] in (1, -1) for n, v in rounds.items() for ms in v for t in range(4 * n + 8) for a in range(n)))

for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
sys.exit(0 if all(ok for _, ok in results) else 1)
