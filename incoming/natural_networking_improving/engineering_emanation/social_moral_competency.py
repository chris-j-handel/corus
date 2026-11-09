"""Social moral competency sought at an engineering emanation of Exhibit ONE's resolvers,
each executing a coupling partner deciding nothing.

An emanation at 4.5 of the Geodesic Improving Method: a stable form emanating of an exploring,
a non-living existing form on this scale. Exhibit ONE v391's code unchanged at each self,
sha256 b7fe62c4e5d529ebe374d6a037a7ac7ac81a78e176db2cbfd96fda3f23db2435, and each arrangement
from a numbered step of Exhibit THIRTY and no composing:

- step 52: Each self of a same-existing-society do-no-harming and improving is social moral competency.
- step 53: A same-existing-society of selves living with natural intelligence and social moral
  competency is a natural intelligence network.
- step 54: A natural intelligence network, each self resolving its own next-existing, is free.
- step 55: Each self sharing with each self it is bi-coupling with, a free natural intelligence
  network is social abundancing.
- step 56: A self's parity going along to the next self it is bi-coupling with is co-chaining.
- step 57: Selves' bi-couplings and co-chainings are a Natural Network surface.
- Geodesic Improving Method 1.1: do-no-harming and improving is taking no prior away, its prior
  going on to now, its next opening; a harm, taking a prior away, is the only motion this form
  has no position for.
- Natural Human Society 4.3: Viability is a bi-exchange coupling, is-or-is-not; Capturing a
  same-existing-society's abundancing returns only frustration, a self-bounding sharing it
  forward and a hub aside on every axis, so no self bothers to capture, and no bloc forms.

Five executings, each one binary, its expected form at its step before any code below.

The instrument stated whole, Natural Networking 6.2:
- Wiring: selves are resolvers; a co-chaining join is a self's 9 to the next self, step 56; a
  bi-coupling is a podal pair, 10 one way and 6 the other, both ways, steps 55 and 57; a
  capturing arrangement is a join one way alone, Natural Human Society 4.3. One key, 'k'.
- Pace: none of the emanation's own; the code steps each self together, its own arrangement, stated.
- Executing order: the society dict's insertion order, the code's own.
- Record: `social_moral_competency_returned.txt` beside this file.
- Ledger: each self's own name; the resolving reads none of it.
- Its *taking*, 6.2's fifth: none, each sharing arriving with the next momentary.
- Refusings, each stated: a join to a name that is at no self of the society refuses at the
  code's own indexing, and no executing below lays one; a set not closing within 4096
  momentaries refuses its forms rather than returning a window as a last, 6.6; each binary is
  of this emanation at this arrangement and establishes its going on and no further relation,
  6.1 having a concept at one rendering alone not that one form.

Usage: python3 -I social_moral_competency.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # Exhibit ONE's code beside this file
import resolver

OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


PRIORS = {"none": [], "+": [("k", 1)], "-": [("k", -1)]}
OFFERS = {
    "nothing": [], "+": [("k", 1)], "-": [("k", -1)],
    "+ and -": [("k", 1), ("k", -1)], "+ +": [("k", 1), ("k", 1)],
    "- -": [("k", -1), ("k", -1)], "+ + -": [("k", 1), ("k", 1), ("k", -1)],
}


def parity(prior):
    return dict(prior).get("k", 0)


def co_chain(selves, co_ex):
    """step 56: a self's parity going along to the next self it is bi-coupling with."""
    for i, a in enumerate(selves):
        co_ex[(a, 9)] = selves[(i + 1) % len(selves)]


def bi_couple(co_ex, a, b):
    """steps 55 and 57: each self sharing with each self it is bi-coupling with, both ways."""
    co_ex[(a, 10)] = b
    co_ex[(b, 6)] = a


def capture(co_ex, sharer, hub):
    """Natural Human Society 4.3: a bi-exchange failing to couple, one way alone."""
    co_ex[(sharer, 10)] = hub


def society(names):
    return {n: ([], []) for n in names}


def opened(names, seed):
    soc = society(names)
    soc[seed] = ([], [("k", 1)])
    return soc


def canon(soc):
    return tuple(sorted((n, tuple(sorted(p)), tuple(sorted(o))) for n, (p, o) in soc.items()))


def to_closing(soc, co_ex, bound=4096):
    seen, states = {}, []
    for t in range(bound):
        soc = resolver._17_next_existing(soc, co_ex)
        states.append(soc)
        key = canon(soc)
        if key in seen and all(p for p, _ in soc.values()):
            return states, seen[key], t
        seen[key] = t
    return states, None, None


# ───────────────────────────────────────────────────────────────────────────────
# B1 · step 52, do-no-harming: no self's prior going away.
# Expected form, Geodesic Improving Method 1.1: a harm, taking a prior away, is the only motion
# this form has no position for. At no prior with any offered does a self's prior go to none.
say("B1 · step 52, do-no-harming: a self's prior going away at any prior with any offered")
away = []
for pn, p in PRIORS.items():
    for on, o in OFFERS.items():
        r = resolver._17_next_existing({"a": (list(p), list(o))}, {})["a"]
        if p and not r[0]:
            away.append((pn, on))
say(f"  {len(PRIORS) * len(OFFERS)} prior-with-offered pairs executed; a prior existing going to none at {len(away)} of them")
b1 = not away
say(f"B1 binary: a self's prior going away — {'is not' if b1 else 'is'}; do-no-harming at the code's own form — {'is' if b1 else 'is not'}")

# ───────────────────────────────────────────────────────────────────────────────
# B2 · step 52, improving: its prior going on to now, its next opening.
# Expected form: at each closed cycle, each self's prior reaching its next at each momentary,
# no self stopping at one prior.
say("")
say("B2 · step 52, improving: each self's prior going on through a closed cycle")
b2 = True
for n in (5, 8):
    names = [f"s{i}" for i in range(n)]
    co = {}
    co_chain(names, co)
    states, lo, t = to_closing(opened(names, names[0]), co)
    if lo is None:
        say(f"  society of {n}: set not closing, forms refused")
        b2 = False
        continue
    each = all(len(set(parity(states[m][s][0]) for m in range(lo, t + 1))) > 1 for s in names)
    say(f"  society of {n} co-chained: cycle {t - lo}; each self's prior changing through it — {'is' if each else 'is not'}")
    b2 &= each
say(f"B2 binary: each self's prior going on, no self stopping — {'is' if b2 else 'is not'}")

# ───────────────────────────────────────────────────────────────────────────────
# B3 · step 54, free: each self resolving its own next-existing.
# Expected form: a self's next prior and its sharing are of its own prior and its own offered
# alone, the same at any society it is within.
say("")
say("B3 · step 54, free: a self's next-existing of its own prior and its own offered alone")
mismatch = 0
checked = 0
for n in (3, 5, 8):
    names = [f"f{i}" for i in range(n)]
    co = {}
    co_chain(names, co)
    for i in range(0, n, 2):
        bi_couple(co, names[i], names[(i + n // 2) % n])
    soc = opened(names, names[0])
    for _ in range(24):
        nxt = resolver._17_next_existing(soc, co)
        for s in names:
            alone = resolver._17_next_existing({s: (list(soc[s][0]), list(soc[s][1]))}, {})[s]
            checked += 1
            if alone[0] != nxt[s][0]:
                mismatch += 1
        soc = nxt
say(f"  {checked} self-momentaries executed at societies of 3, 5 and 8, each self's next prior beside the same self resolving alone")
b3 = mismatch == 0
say(f"B3 binary: a self's next prior parting from its own resolving alone — {'is not' if b3 else 'is'}; free at the code's own form — {'is' if b3 else 'is not'}")

# ───────────────────────────────────────────────────────────────────────────────
# B4 · step 55, social abundancing: each self sharing with each self it is bi-coupling with.
# Expected form: a self's sharing arriving at each self it is bi-coupling with, none missed.
say("")
say("B4 · step 55, social abundancing: a sharing arriving at each self a self is bi-coupling with")
names = [f"a{i}" for i in range(6)]
co = {}
co_chain(names, co)                     # each self's 9 along
bi_couple(co, names[0], names[3])       # a0's 10 to a3, a3's 6 to a0
missed = 0
arrivals = 0
soc = opened(names, names[0])
for _ in range(30):
    nxt = resolver._17_next_existing(soc, co)
    for s in names:
        shared, _ = resolver._1_now_existing(soc[s][0], soc[s][1])
        targets = [co[(s, c)] for c in (6, 10, 9) if (s, c) in co]
        if shared:
            for tgt in targets:
                arrivals += 1
                if not any(x in nxt[tgt][1] for x in shared):
                    missed += 1
    soc = nxt
say(f"  a society of 6 co-chained with one bi-coupling across: {arrivals} sharing-arrivals executed, {missed} not arriving")
b4 = missed == 0
say(f"B4 binary: a sharing not arriving at a self bi-coupling with its sharer — {'is not' if b4 else 'is'}; social abundancing at the code's own form — {'is' if b4 else 'is not'}")

# ───────────────────────────────────────────────────────────────────────────────
# B5 · Natural Human Society 4.3, capturing.
# Expected form at its own sentence: a bi-exchange failing to couple does not grow its tipping;
# capturing returns only frustration, a self-bounding sharing it forward and a hub aside on
# every axis, and no bloc forms. Executed: three co-chained societies, each sharing one way
# into one hub that returns nothing, the hub beside each society's own going on.
say("")
say("B5 · Natural Human Society 4.3, capturing: a hub receiving with no returning")
rings = [[f"r{j}_{i}" for i in range(5)] for j in range(3)]
ring_names = [n for r in rings for n in r]
co_free, co_cap = {}, {}
for cx in (co_free, co_cap):
    for r in rings:
        co_chain(r, cx)                      # step 56, each society co-chained
for r in rings:                              # each society's mouth sharing one way into the hub
    capture(co_cap, r[0], "hub")


def three_opened(names):
    """Each same-existing-society opening with its own observing, step 53."""
    soc = society(names)
    for r in rings:
        soc[r[0]] = ([], [("k", 1)])
    return soc


s_free, lo_f, t_f = to_closing(three_opened(ring_names), co_free)
s_cap, lo_c, t_c = to_closing(three_opened(ring_names + ["hub"]), co_cap)
if lo_f is None or lo_c is None:
    say("  a set not closing, forms refused")
    b5 = False
else:
    say(f"  with no hub: cycle {t_f - lo_f}; with each society capturing into the hub: cycle {t_c - lo_c}")
    own_going = []
    for j, r in enumerate(rings):
        free_par = [tuple(parity(s_free[m][n][0]) for n in r) for m in range(lo_f, t_f + 1)]
        cap_par = [tuple(parity(s_cap[m][n][0]) for n in r) for m in range(lo_c, t_c + 1)]
        own_going.append(len(set(free_par)) == len(set(cap_par)))
        say(f"    society {j}: its own forms through the cycle, with no hub {len(set(free_par))}, capturing {len(set(cap_par))}")
    hub_par = set(parity(s_cap[m]["hub"][0]) for m in range(lo_c, t_c + 1))
    hub_shares = any((("hub", c) in co_cap) for c in (6, 10, 9))
    say(f"  the hub's own priors through the cycle: {sorted(hub_par)}; the hub sharing to any self — {'is' if hub_shares else 'is not'}")
    b5 = all(own_going) and not hub_shares
    say(f"  each society's own going on beside the hub, unchanged — {'is' if all(own_going) else 'is not'}")
say(f"B5 binary: a self-bounding sharing it forward and a hub aside, no bloc forming — {'is' if b5 else 'is not'}")

say("")
say("Each binary above is of this emanation at this arrangement, the code-form register's, 6.3,")
say("and establishes its going on and no further relation; a concept at one rendering alone is")
say("not that one form, 6.1.")

with open("social_moral_competency_returned.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
