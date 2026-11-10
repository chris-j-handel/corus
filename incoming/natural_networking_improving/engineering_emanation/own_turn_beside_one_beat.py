"""The periods of a ring met at each self's own turn beside the one beat, a coupling partner deciding nothing.

Natural Networking's gathering-value has this droplet at its back, a possible exploring:
*A relation and its periods found with selves stepping together is-or-is-not found again with
each self at its own turn.* Each period this session returned, at `incoming/V400networking/`
and at `social_moral_competency.py` beside this file, was found with selves stepping together,
the code's own arrangement at `_17_next_existing`. This instrument meets those periods at each
self's own turn and says whether they are found again.

The kit's `own_turn_seam_v366.py`, re-executed this sitting and returning its waiting record
line for line, has the two turn orders apart: *against the arriving*, each self at its turn
before its own arriving has turned, and *with the arriving*, each self at its turn from an
arriving already turned, and the two are not the same running. Both orders are executed below.

Exhibit ONE v391's code unchanged at each self: `_1_now_existing` resolves the one self at its
turn, and the sharing goes to each self its co-existing joins it to, the three connectors 6, 10
and 9 alike, the delivering of `_17_next_existing`'s own loop. One round is each self at its
turn once, one round beside one momentary of the one beat.

The instrument stated whole, Natural Networking 6.2:
- Wiring: a ring of selves co-chained, each self's 9 to the next, Exhibit THIRTY step 56. One
  key, 'k'. At a self's turn its prior and its offered resolve, its prior goes on, its offered
  empties, and its sharing arrives at each self it joins to, to wait at that self's offered
  until that self's own turn.
- Pace: one round is each self at its turn once, the turn order stated at each executing.
- Executing order: against the arriving, the ring's order reversed from the joins; with the
  arriving, the ring's order along the joins.
- Record: `own_turn_returned.txt` beside this file.
- Ledger: each self's own name.
- Its *taking*, 6.2's fifth: a sharing waits at a receiving self's offered until that self's own
  turn, which is this arrangement's whole parting from the one beat, stated.
- Refusings, each stated: a set not closing within 4096 rounds refuses its forms rather than
  returning a window as a last, 6.6; one key alone, each sharing of one parity; the periods
  below are of a ring co-chained one way, a bi-coupling across at no executing here.

Usage: python3 -I own_turn_beside_one_beat.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import resolver

OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


def ring(n):
    selves = [f"m{i}" for i in range(n)]
    co_ex = {}
    for i, a in enumerate(selves):
        co_ex[(a, 9)] = selves[(i + 1) % n]
    return selves, co_ex


def one_beat(selves, co_ex, bound=4096):
    """The code's own arrangement: each self stepping together."""
    soc = {s: ([], []) for s in selves}
    soc[selves[0]] = ([], [("k", 1)])
    seen, states = {}, []
    for t in range(bound):
        soc = resolver._17_next_existing(soc, co_ex)
        states.append(soc)
        key = tuple(sorted((s, tuple(sorted(p)), tuple(sorted(o))) for s, (p, o) in soc.items()))
        if key in seen and all(p for p, _ in soc.values()):
            return states, seen[key], t
        seen[key] = t
    return states, None, None


def own_turn(selves, co_ex, order, bound=4096):
    """Each self at its own turn: `_1_now_existing` at the one self, its sharing waiting."""
    prior = {s: [] for s in selves}
    offered = {s: [] for s in selves}
    offered[selves[0]] = [("k", 1)]
    seen, states = {}, []
    for t in range(bound):
        for s in order:
            sharing, nxt = resolver._1_now_existing(prior[s], offered[s])
            prior[s] = nxt
            offered[s] = []
            for c in (6, 10, 9):
                if (s, c) in co_ex:
                    offered[co_ex[(s, c)]] = offered[co_ex[(s, c)]] + list(sharing)
        states.append(({s: list(prior[s]) for s in selves},
                       {s: list(offered[s]) for s in selves}))
        key = (tuple(sorted((s, tuple(sorted(prior[s]))) for s in selves)),
               tuple(sorted((s, tuple(sorted(offered[s]))) for s in selves)))
        if key in seen and all(prior[s] for s in selves):
            return states, seen[key], t
        seen[key] = t
    return states, None, None


def agreeing(prior_map, selves):
    """The couplings of the ring whose two priors agree now, each the place resolving is traveling."""
    out = []
    n = len(selves)
    for i, a in enumerate(selves):
        b = selves[(i + 1) % n]
        pa = dict(prior_map[a]).get("k", 0)
        pb = dict(prior_map[b]).get("k", 0)
        if pa != 0 and pa == pb:
            out.append((a, b))
    return out


say("The periods of a co-chained ring at each self's own turn beside the one beat, rings 3 to 10.")
say("One round is each self at its turn once; one momentary of the one beat is each self together.")
say("")
say(f"{'ring':>5s}  {'one beat':>9s}  {'against the arriving':>21s}  {'with the arriving':>18s}   the one place")
rows = []
for n in range(3, 15):
    selves, co_ex = ring(n)
    _, lo_b, t_b = one_beat(selves, co_ex)
    beat = (t_b - lo_b) if lo_b is not None else None

    against = list(reversed(selves))
    s_a, lo_a, t_a = own_turn(selves, co_ex, against)
    per_a = (t_a - lo_a) if lo_a is not None else None

    s_w, lo_w, t_w = own_turn(selves, co_ex, selves)
    per_w = (t_w - lo_w) if lo_w is not None else None

    # the one place, at the own turn against the arriving
    place = "—"
    if lo_a is not None:
        tr = [agreeing(s_a[m][0], selves) for m in range(lo_a, t_a)]
        sizes = sorted(set(len(x) for x in tr))
        if sizes == [1]:
            idx = [selves.index(x[0][0]) for x in tr]
            changes = [i for i in range(1, len(idx)) if idx[i] != idx[i - 1]]
            gaps = sorted(set(changes[i] - changes[i - 1] for i in range(1, len(changes)))) or ["—"]
            place = f"one, moving each {gaps} rounds, {len(set(idx))} of {n} places"
        else:
            place = f"agreeing couplings {sizes}"
    say(f"{n:5d}  {str(beat):>9s}  {str(per_a):>21s}  {str(per_w):>18s}   {place}")
    rows.append((n, beat, per_a, per_w))

say("")
say("The three period families met at each ring, 4N and 2 stepping together, 2 and 2N−1 against")
say("the arriving, 2N+2 and N+1 with the arriving, each at an odd ring and at an even ring:")
parts = []
for n, beat, per_a, per_w in rows:
    odd = n % 2
    expect = ((4 * n) if odd else 2, 2 if odd else 2 * n - 1, (2 * n + 2) if odd else n + 1)
    got = (beat, per_a, per_w)
    if expect != got:
        parts.append((n, expect, got))
say(f"  {len(rows)} rings executed, a ring parting from its family at {len(parts)} of them"
    + (f": {parts}" if parts else ""))

same_against = [r for r in rows if r[1] == r[2]]
same_with = [r for r in rows if r[1] == r[3]]
say(f"The one beat's period found again against the arriving at {len(same_against)} of {len(rows)} rings; "
    f"with the arriving at {len(same_with)} of {len(rows)} rings.")
say(f"The droplet's binary, a period found with selves stepping together found again with each self at its own "
    f"turn — {'is' if len(same_against) == len(rows) and len(same_with) == len(rows) else 'is not'}, "
    f"at the rings and the two turn orders above.")
say("")
say("Each row is of this arrangement, a ring co-chained one way with one key, and establishes its")
say("going on and no further relation; a concept at one rendering alone is not that one form, 6.1.")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "own_turn_returned.txt"),
          "w", encoding="utf-8") as f:
    f.write("\n".join(OUT) + "\n")
