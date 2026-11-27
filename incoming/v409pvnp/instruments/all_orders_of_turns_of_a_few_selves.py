"""All orders of turns of a few selves: one other a moment, a self's couplings in turn.

A laying: each self has the selves it observes, itself among the possible, in an order, one a moment, the order again
with its last. All selves begin their turns together, with the first of their order; an order begun at an other of its
selves is an other laying, and is executed as well. All living, all openings, all selves inverted in turn. The twelve
lines by their table, opened and checked by the instrument beside this one. No opening and no laying is drawn.

Executed until a pair of societies comes again or all selves have parted, so that never is never.

    python3 -I incoming/v409pvnp/instruments/all_orders_of_turns_of_a_few_selves.py .
"""
import itertools, math, re, sys
import numpy as np
from pathlib import Path

src = (Path(__file__).resolve().parent / "an_other_than_carried_or_lost_all_openings.py").read_text()
exec(src[src.index("import itertools"):src.index("def society")])
out = [o for o in out if o[1].startswith("E0")]

def every_order(S, longest, chunk=40000):
    choices = [c for k in range(1, longest + 1) for c in itertools.permutations(range(S), k)]
    P = math.lcm(*range(1, longest + 1))
    full = np.array([[c[j % len(c)] for j in range(P)] for c in choices], np.int64)       # (choices, P): the self observed, a moment of the turn
    observes = np.zeros((len(choices), S), bool)
    for i, c in enumerate(choices): observes[i, list(c)] = True
    n = len(choices) ** S
    openings = np.array(list(itertools.product((1, 2), repeat=S)), np.uint8); O = len(openings)
    kept = []; latest_kept = []; coupled_n = 0
    digits = len(choices) ** np.arange(S - 1, -1, -1)
    for start in range(0, n, chunk):
        ids = np.arange(start, min(n, start + chunk))
        lay_choice = (ids[:, None] // digits) % len(choices)                             # (L, S)
        adj = observes[lay_choice] | np.eye(S, dtype=bool)
        reach = adj.copy()
        for _ in range(S): reach = (reach[:, :, :, None] & reach[:, None, :, :].transpose(0, 1, 3, 2)).any(axis=2) | reach
        ok = reach.all(axis=(1, 2)); coupled_n += int(ok.sum())
        alive = ids[ok]; turn_all = full[lay_choice[ok]]                                 # (L, S, P)
        latest = np.zeros(len(alive), np.int32); pos = np.arange(len(alive))
        for A in range(S):
            idx = pos; turn = turn_all[idx]; L = len(idx)
            if not L: break
            s1 = np.broadcast_to(openings, (L, O, S)).copy(); s2 = s1.copy(); s2[:, :, A] = 3 - s2[:, :, A]
            l1 = np.zeros((L, O, S), np.uint8); l2 = l1.copy()
            parted = np.zeros((L, O, S), np.int32); parted[:, :, A] = -1
            closed = np.zeros((L, O), bool); snap = None; t = 0; mark = P; passing = []
            while len(idx):
                L = len(idx); t += 1
                gather = np.broadcast_to(turn[:, None, :, (t - 1) % P], (L, O, S))
                surf1 = np.take_along_axis(l1, gather, axis=2); surf2 = np.take_along_axis(l2, gather, axis=2)
                s1, l1 = NEXT[s1, surf1], LAYS[s1, surf1]; s2, l2 = NEXT[s2, surf2], LAYS[s2, surf2]
                new = (s1 != s2) & (parted == 0); parted[new] = t
                if snap is not None and (t - snap_t) % P == 0:
                    closed |= ((s1 == snap[0]) & (l1 == snap[1]) & (s2 == snap[2]) & (l2 == snap[3])).all(axis=2)
                whole = (parted != 0).all(axis=2); passes = whole.all(axis=1); fails = (closed & ~whole).any(axis=1)
                if passes.any():
                    latest[idx[passes]] = np.maximum(latest[idx[passes]], parted[passes].max(axis=(1, 2))); passing.append(idx[passes])
                go = ~(passes | fails)
                if not go.all():
                    idx, turn, s1, l1, s2, l2, parted, closed = idx[go], turn[go], s1[go], l1[go], s2[go], l2[go], parted[go], closed[go]
                    if snap is not None: snap = tuple(x[go] for x in snap)
                if t == mark:
                    snap = (s1.copy(), l1.copy(), s2.copy(), l2.copy()); snap_t = t; closed[:] = False; mark *= 2
                if t > 1 << 15: raise SystemExit("a pair of societies did not come again")
            pos = np.sort(np.concatenate(passing)) if passing else np.array([], np.int64)
        for i in pos:
            kept.append([choices[c] for c in lay_choice[ok][i]]); latest_kept.append(int(latest[i]))
    return n, coupled_n, kept, latest_kept

rows = []; h1 = True; soonest_all = {}
asked = [x for x in sys.argv[1:] if re.fullmatch(r"\d,\d", x)] or ["3,3", "4,2", "4,3"]
for S, longest in [(int(a), int(b)) for a, b in (x.split(",") for x in asked)]:
    n, coupled_n, kept, latest = every_order(S, longest)
    soonest = min(latest) if latest else None
    ahead = [(lay, t) for lay, t in zip(kept, latest) if t < 2 * (S - 1)]
    one_alone = sum(all(len(c) == 1 for c in lay) for lay in kept)
    h1 &= not ahead
    rows.append(f"   {S} selves, turns of 1 to {longest}: layings {n:,} · all selves reaching all by couplings {coupled_n:,} · one me's other-than in all other selves, "
                f"with all openings and all selves inverted in turn: {len(kept):,}, {one_alone:,} of them a self observing one alone · "
                f"the soonest farthest parting, moment {soonest} · a co-chain's, {2 * (S - 1)} · ahead of a co-chain's: {len(ahead):,}"
                + (f" · e.g. {min(ahead, key=lambda x: x[1])}" if ahead else ""))
say("H1 of all orders of turns executed, no laying with one me's other-than in all other selves, with all openings, has its farthest parting ahead of a co-chain's", h1)
for r in rows: say(r, "sized")
for mark, text in out: print(f"{text}: {mark}" if mark != "sized" else text)
print()
print(sum(m == "is" for m, _ in out), "lines is,", sum(m == "is-not" for m, _ in out), "is-not,", sum(m == "sized" for m, _ in out), "sized")
