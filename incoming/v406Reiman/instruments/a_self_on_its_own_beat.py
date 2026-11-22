"""A self on its own beat: Exhibit ONE's forms with no stepping together.

Exhibit ONE's selves step together with 17-next-existing. Here a self's own
moment, 1-now-existing, is the living file's code as it is, and the passing of
its parities to its bi-couplings is this page's own, said below, in place of
17-next-existing's stepping together.

Preparing: no prior is set by hand. A self with no prior receives one opening
parity, and that parity is its prior. All executings go on from that state.
Pace: none from this page. A self resolves once a parity has arrived from
all of its bi-couplings.
The arrival resolved with: the oldest of a bi-coupling's arrivals.
Order: the self resolving next is drawn among the selves with an arrival from
all their bi-couplings, by five seeds.
Record: a self's own trace, by its own resolvings. No trace of all together.

    python3 -I incoming/v406Reiman/instruments/a_self_on_its_own_beat.py .
"""
import random
import sys
from collections import deque
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, resolver, spiral_couplings, torus_couplings


def opening_parities(selves):
    out = {}
    for s in selves:
        k = sum(s) if isinstance(s, tuple) else s
        out[s] = -1 if k % 2 == 0 else 1
    return out


def senders_of(selves, couplings):
    into = {s: [] for s in selves}
    for (sender, way), receiver in couplings.items():
        into[receiver].append((sender, way))
    return into


def stepping_together(names, selves, couplings, resolvings):
    step = names["_17_next_existing"]
    society = {s: ([], [(S, p)]) for s, p in opening_parities(selves).items()}
    trace = {s: [] for s in selves}
    for _ in range(resolvings + 1):
        society = step(society, couplings)
        for s in selves:
            trace[s].append(dict(society[s][0]).get(S, 0))
    return {s: t[1:] for s, t in trace.items()}


def own_beat(names, selves, couplings, resolvings, seed, taking="oldest", ready="every", tick=False):
    one = names["_1_now_existing"]
    rng = random.Random(seed)
    into = senders_of(selves, couplings)
    out = {s: [(way, r) for (sender, way), r in couplings.items() if sender == s] for s in selves}
    arrived = {s: {src: deque() for src in into[s]} for s in selves}
    prior = {}
    for s, p in opening_parities(selves).items():
        sharing, prior[s] = one([], [(S, p)])
        for way, r in out[s]:
            arrived[r][(s, way)].append(sharing)
    trace = {s: [] for s in selves}

    def is_ready(s):
        if len(trace[s]) >= resolvings:
            return False
        if tick:
            return True
        waits = [len(q) for q in arrived[s].values()]
        return all(waits) if ready == "every" else any(waits)

    for _ in range(200000):
        able = [s for s in selves if is_ready(s)]
        if not able:
            break
        s = rng.choice(able)
        received = []
        for q in arrived[s].values():
            if not q:
                continue
            if taking == "oldest":
                received.extend(q.popleft())
            elif taking == "newest":
                received.extend(q.pop())
                q.clear()
            else:
                while q:
                    received.extend(q.popleft())
        sharing, prior[s] = one(prior[s], received)
        trace[s].append(dict(prior[s]).get(S, 0))
        for way, r in out[s]:
            arrived[r][(s, way)].append(sharing)
    return trace


def own_again(t):
    for p in range(1, len(t) // 2 + 1):
        if all(t[i] == t[i + p] for i in range(len(t) // 2, len(t) - p)):
            return p
    return None


if __name__ == "__main__":
    names, page = resolver(sys.argv[1])
    seeds = (1, 2, 3, 4, 5)
    forms = [("a spiral of 5", list(range(5)), spiral_couplings(5)),
             ("a spiral of 7", list(range(7)), spiral_couplings(7)),
             ("a spiral of 9", list(range(9)), spiral_couplings(9))]
    for p, q in ((3, 5), (3, 7), (5, 7), (3, 9)):
        forms.append((f"a torus of {p} along, {q} across", [(a, b) for a in range(p) for b in range(q)], torus_couplings(p, q)))
    all_is = True
    print("A self resolving once a parity has arrived from all of its bi-couplings, with the oldest arrival")
    for name, selves, couplings in forms:
        n = 240
        together = stepping_together(names, selves, couplings, n)
        same = all(own_beat(names, selves, couplings, n, seed) == together for seed in seeds)
        all_is = all_is and same
        again = sorted({own_again(t) for t in together.values()})
        print(f"   {name} · a self's own trace again with {again} of its resolvings · same as stepping together, by five orders: {'is' if same else 'is-not'}")
    print()
    print("Other-than that, a spiral of 5: are the five orders' traces the same as stepping together")
    selves, couplings = list(range(5)), spiral_couplings(5)
    together = stepping_together(names, selves, couplings, 240)
    for label, kw in (("the newest arrival, the older ones dropped", dict(taking="newest")),
                      ("all of a bi-coupling's arrivals together", dict(taking="all")),
                      ("a self drawn to resolve with or with no arrival", dict(tick=True))):
        runs = [own_beat(names, selves, couplings, 240, seed, **kw) for seed in seeds]
        same = all(r == together for r in runs)
        one_another = all(r == runs[0] for r in runs)
        print(f"   {label} · same as stepping together: {'is' if same else 'is-not'} · the five the same as one another: {'is' if one_another else 'is-not'}")
    print()
    print("A torus of 3 along, 5 across: a self resolving on an arrival from any one bi-coupling")
    selves, couplings = [(a, b) for a in range(3) for b in range(5)], torus_couplings(3, 5)
    together = stepping_together(names, selves, couplings, 240)
    runs = [own_beat(names, selves, couplings, 240, seed, ready="any") for seed in seeds]
    print(f"   same as stepping together: {'is' if all(r == together for r in runs) else 'is-not'} · the five the same as one another: {'is' if all(r == runs[0] for r in runs) else 'is-not'}")
    print()
    print("All is, of the seven forms." if all_is else "An is-not is among the seven forms.")
    sys.exit(0 if all_is else 1)
