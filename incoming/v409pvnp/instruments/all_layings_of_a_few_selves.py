"""All layings of a few selves: where is one me's other-than in all other selves' own moments, and how soon?

A laying: each self has the selves it observes, one or more, itself among the possible. All living, all openings,
all selves inverted in turn, the lines as they are (all others together). The table of the lines is opened and checked
by the instrument beside this one. No opening and no laying is drawn.

Executed until a pair of societies comes again or all selves have parted, so that never is never.

    python3 -I incoming/v409pvnp/instruments/all_layings_of_a_few_selves.py .
"""
import itertools
import numpy as np
from pathlib import Path

src = (Path(__file__).resolve().parent / "an_other_than_carried_or_lost_all_openings.py").read_text()
exec(src[src.index("import itertools"):src.index("def society")])
out = [o for o in out if o[1].startswith("E0")]

def stepping(state, lay, gather, shape):
    got = np.take_along_axis(lay, gather, axis=2).reshape(shape)
    plus = (got == 1).any(axis=3); minus = (got == 2).any(axis=3)
    surf = np.where(plus & ~minus, 1, np.where(minus & ~plus, 2, 0))
    return NEXT[state, surf], LAYS[state, surf]

def every_laying(S, most_observed, chunk=20000):
    choices = [c for k in range(1, most_observed + 1) for c in itertools.combinations(range(S), k)]
    layings = np.array(list(itertools.product(range(len(choices)), repeat=S)), np.int32)
    K = most_observed
    member = np.zeros((len(choices), K), np.int64)
    for i, c in enumerate(choices): member[i] = list(c) + [c[-1]] * (K - len(c))
    observes = np.zeros((len(choices), S), bool)
    for i, c in enumerate(choices): observes[i, list(c)] = True
    # all selves reaching all: by couplings alone
    adj = observes[layings] | np.eye(S, dtype=bool)                 # adj[l, s, f]: s observes f, or is f
    reach = adj.copy()
    for _ in range(S): reach = (reach[:, :, :, None] & reach[:, None, :, :].transpose(0, 1, 3, 2)).any(axis=2) | reach
    coupled = np.flatnonzero(reach.all(axis=(1, 2)))
    openings = np.array(list(itertools.product((1, 2), repeat=S)), np.uint8); O = len(openings)
    alive = coupled; latest = np.zeros(len(layings), np.int32)
    for A in range(S):
        passing = []
        for start in range(0, len(alive), chunk):
            idx = alive[start:start + chunk]
            ins = member[layings[idx]]
            L = len(idx)
            s1 = np.broadcast_to(openings, (L, O, S)).copy(); s2 = s1.copy(); s2[:, :, A] = 3 - s2[:, :, A]
            l1 = np.zeros((L, O, S), np.uint8); l2 = l1.copy()
            parted = np.zeros((L, O, S), np.int32); parted[:, :, A] = -1
            closed = np.zeros((L, O), bool); snap = None; t = 0; mark = 2
            while len(idx):
                L = len(idx); t += 1
                gather = np.broadcast_to(ins[:, None, :, :], (L, O, S, K)).reshape(L, O, S * K); shape = (L, O, S, K)
                s1, l1 = stepping(s1, l1, gather, shape); s2, l2 = stepping(s2, l2, gather, shape)
                new = (s1 != s2) & (parted == 0); parted[new] = t
                if snap is not None:
                    closed |= ((s1 == snap[0]) & (l1 == snap[1]) & (s2 == snap[2]) & (l2 == snap[3])).all(axis=2)
                whole = (parted != 0).all(axis=2)                       # all other selves parted, an opening
                passes = whole.all(axis=1)                              # with all openings
                fails = (closed & ~whole).any(axis=1)                   # an opening come again with a self never parted
                if passes.any():
                    latest[idx[passes]] = np.maximum(latest[idx[passes]], parted[passes].max(axis=(1, 2)))
                    passing.append(idx[passes])
                go = ~(passes | fails)
                if not go.all():
                    idx, ins, s1, l1, s2, l2, parted, closed = idx[go], ins[go], s1[go], l1[go], s2[go], l2[go], parted[go], closed[go]
                    if snap is not None: snap = tuple(x[go] for x in snap)
                if t == mark:                                           # a later mark, twice as far: a society comes again past its settling
                    snap = (s1.copy(), l1.copy(), s2.copy(), l2.copy()); closed[:] = False; mark *= 2
                if t > 1 << 14: raise SystemExit("a pair of societies did not come again")
        alive = np.sort(np.concatenate(passing)) if passing else np.array([], np.int64)
    return choices, layings, coupled, alive, latest

def one_co_chain(S, observed):
    """With a self's observing of itself set aside: each self observes one other, and the others are one round through all."""
    others = [[f for f in fs if f != s] for s, fs in enumerate(observed)]
    if any(len(o) != 1 for o in others): return False
    x, seen = 0, set()
    while x not in seen: seen.add(x); x = others[x][0]
    return len(seen) == S and x == 0

def a_round_through_all(S, observed):
    """Among a laying's couplings, a round through all its selves: each self observing the self before it on the round."""
    for perm in itertools.permutations(range(1, S)):
        order = (0,) + perm
        if all(order[i] in observed[order[(i + 1) % S]] for i in range(S)): return True
    return False

rows = []; f1 = f2 = True
for S, K in ((3, 3), (4, 4), (5, 2)):
    choices, layings, coupled, alive, latest = every_laying(S, K)
    kept = [[choices[c] for c in layings[i]] for i in alive]
    rounds = sum(a_round_through_all(S, lay) for lay in kept)
    chains = sum(one_co_chain(S, lay) for lay in kept)
    soonest = int(latest[alive].min()) if len(alive) else None
    f1 &= rounds == len(kept); f2 &= soonest == 2 * (S - 1)
    rows.append(f"   {S} selves, a self observing 1 to {K} selves: layings {len(layings):,} · all selves reaching all by couplings {len(coupled):,} · "
                f"one me's other-than in all other selves, with all openings and all selves inverted in turn: {len(kept):,} · with a round through all "
                f"their selves {rounds:,}, {chains:,} of them that round alone · the soonest farthest parting, moment {soonest} · a co-chain's, {2 * (S - 1)}")
say("F1 of all layings of 3 to 5 selves, the ones with one me's other-than in all other selves, with all openings, each have among their couplings "
    "a round through all their selves", f1)
say("F2 of them none has its farthest parting ahead of a co-chain's, twice its couplings along", f2)
for r in rows: say(r, "sized")

for mark, text in out: print(f"{text}: {mark}" if mark != "sized" else text)
print()
print(sum(m == "is" for m, _ in out), "lines is,", sum(m == "is-not" for m, _ in out), "is-not,", sum(m == "sized" for m, _ in out), "sized")
