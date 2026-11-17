"""Natural Networking study: selves coupled by design, going on with Exhibit ONE's resolver unchanged.

This instrument reads Exhibit ONE Natural Resolver's code from its file and runs it as written.
It lays couplings of selves (own going along with 9, across with 10 or 6), lets them go on moment
by moment, and observes each self's prior: same-existing with a same parity received, or inverting.

It prints four studies, each with fixed seeds, so a second executing prints the same numbers:

  living     each self's same-existing share; how soon a network comes to its parities again
  growing    same-existing share and coming back, as selves join (16, 64, 144)
  carrying   one prior a hand inverts: does the network come back to its own parities?
             one parity a hand supplies once: how far along do its two goings-on stay apart?
  third      two selves each receive one parity once; a third self observes both across:
             does its sequencing go with the two together, in neither alone?
  all        each of the above (about two minutes)

It reads one file, Exhibit ONE's, and writes none.

Use, with the repository's top folder as its first word (here "."), and a study's name or none for all:
  python3 -I incoming/v404networking/instruments/natural_networking_study.py .
  python3 -I incoming/v404networking/instruments/natural_networking_study.py . third
"""
import collections
import glob
import os
import random
import re
import sys

_words = sys.argv[1:]
ROOT = _words.pop(0) if _words and os.path.isdir(_words[0]) else \
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ONE = sorted(glob.glob(os.path.join(ROOT, "Exhibit_ONE_Natural_Resolver_*.md")))
if not ONE:
    sys.exit("Give the repository's top folder as the first word: Exhibit ONE's file is read from it.")
_code = re.search(r"```python\n(.*?)```", open(ONE[-1], encoding="utf-8").read(), re.S).group(1)
_ns = {}
exec(_code, _ns)
NEXT = _ns["_17_next_existing"]  # Exhibit ONE's 17-next-existing, unchanged
NAME = "x"  # one shared name; names never meet in the resolver, so one name is each name's going on


# ---- layings of couplings -------------------------------------------------------------

def lone(n):
    return {}


def spiral_of_one_each(n):  # each self observing its own going along, with 9
    return {(s, 9): s for s in range(n)}


def pairs(n):  # reciprocal 6 to 2, two by two
    return {(s, 6): s ^ 1 for s in range(n)}


def chain(n):  # own going along with 9, across to the next with 10
    r = spiral_of_one_each(n)
    r.update({(s, 10): s + 1 for s in range(n - 1)})
    return r


def spiral(n):  # a chain, its last self across to its first
    r = spiral_of_one_each(n)
    r.update({(s, 10): (s + 1) % n for s in range(n)})
    return r


def across_both_ways(n):  # a spiral, also across to the prior self with 6
    r = spiral(n)
    r.update({(s, 6): (s - 1) % n for s in range(n)})
    return r


def torus(n):  # side by side, own going along with 9, 10 to the right, 6 below, wrapping
    side = int(round(n ** 0.5))
    r = {}
    for s in range(side * side):
        x, y = s % side, s // side
        r[(s, 9)] = s
        r[(s, 10)] = y * side + (x + 1) % side
        r[(s, 6)] = ((y + 1) % side) * side + x
    return r


def by_chance(n, rng, q=0.7):  # each of 6, 10 and 9 laid with chance q, to a self by chance
    return {(s, c): rng.randrange(n) for s in range(n) for c in (6, 10, 9) if rng.random() < q}


def third_self_of_two_chains(gap, own):
    """two chains of `gap` selves, a and b, each chain's last self across with 10 into one third self m"""
    a, b = list(range(gap)), list(range(gap, 2 * gap))
    m = 2 * gap
    r = {}
    for ch in (a, b):
        for i, s in enumerate(ch):
            r[(s, 9)] = s
            r[(s, 10)] = ch[i + 1] if i + 1 < len(ch) else m
    if own:
        r[(m, 9)] = m
    return r, a[0], b[0], m, m + 1


def third_self_of_two_spirals(size, own):
    """two spirals of `size` selves, each one's last self also across with 6 into one third self m"""
    a, b = list(range(size)), list(range(size, 2 * size))
    m = 2 * size
    r = {}
    for sp in (a, b):
        for i, s in enumerate(sp):
            r[(s, 9)] = s
            r[(s, 10)] = sp[(i + 1) % size]
        r[(sp[-1], 6)] = m
    if own:
        r[(m, 9)] = m
    return r, a[0], b[0], m, m + 1


# ---- going on and observing ------------------------------------------------------------

def first_priors(n, rng):
    return {s: ([(NAME, rng.choice((1, -1)))], []) for s in range(n)}


def received(possibling):  # as the resolver reads it: one parity, or 0 for none or not same
    r = None
    for _, v in possibling:
        if v:
            r = (1 if v > 0 else -1) if r is None else (r if (r > 0) == (v > 0) else 0)
    return r or 0


def state(soc):
    return tuple((dict(p).get(NAME, 0), received(q)) for _, (p, q) in sorted(soc.items()))


def priors(soc):
    return tuple(dict(p).get(NAME, 0) for _, (p, q) in sorted(soc.items()))


def supply(soc, s, parity):  # a hand supplies one parity to self s, once
    soc = {k: (p, list(q)) for k, (p, q) in soc.items()}
    soc[s] = (soc[s][0], soc[s][1] + [(NAME, parity)])
    return soc


def go_on(soc, routes, moments):
    for _ in range(moments):
        soc = NEXT(soc, routes)
    return soc


def comes_to_its_parities_again(soc, routes, cap=20000):
    """moments before its parities come again, the number of moments between, and the states between"""
    seen, t = {}, 0
    while t < cap:
        k = state(soc)
        if k in seen:
            first = seen[k]
            between = [k2 for k2, t2 in seen.items() if t2 >= first]
            return first, t - first, frozenset(between), soc
        seen[k] = t
        soc = NEXT(soc, routes)
        t += 1
    raise RuntimeError("no coming again within cap")


def same_existing_share(routes, n, rng, starts):
    shares, gaps = [], []
    for _ in range(starts):
        soc = first_priors(n, rng)
        before_t, period, _, soc = comes_to_its_parities_again(soc, routes)
        same = 0
        for _ in range(period):
            p0 = priors(soc)
            soc = NEXT(soc, routes)
            same += sum(a == b for a, b in zip(p0, priors(soc)))
        shares.append(same / (period * n))
        gaps.append((before_t, period))
    return sum(shares) / len(shares), gaps


def on_its_spiral(routes, n, rng):
    _, _, between, soc = comes_to_its_parities_again(first_priors(n, rng), routes)
    return between, soc


def comes_back(routes, n, rng, starts):
    back = 0
    for _ in range(starts):
        between, soc = on_its_spiral(routes, n, rng)
        s = rng.randrange(n)
        p, q = soc[s]
        soc = dict(soc)
        soc[s] = ([(NAME, -dict(p)[NAME])], q)  # a hand inverts one prior
        for _ in range(400):
            if state(soc) in between:
                back += 1
                break
            soc = NEXT(soc, routes)
    return back


def window(soc, routes, moments, s=None):
    out = []
    for _ in range(moments):
        soc = NEXT(soc, routes)
        out.append(priors(soc) if s is None else priors(soc)[s])
    return tuple(out)


# ---- studies ---------------------------------------------------------------------------

def say(*lines):
    for ln in lines:
        print(ln)
    print()


def study_living():
    rng = random.Random(404)
    say("LIVING: same-existing share of each self, and how soon a network comes to its parities again",
        "  sixteen selves, 200 first priors by chance each")
    for build in (lone, spiral_of_one_each, pairs, chain, spiral, across_both_ways, torus):
        share, gaps = same_existing_share(build(16), 16, rng, 200)
        print(f"  {build.__name__:20s} same-existing share {share:.3f}   "
              f"comes to its parities again within {max(g[0] for g in gaps)} moments, "
              f"then with each {sorted(set(g[1] for g in gaps))} moments")
    print()
    say("  couplings laid by chance, 40 layings each")
    for n in (2, 8, 32, 128):
        shares, worst = [], 0
        for _ in range(40):
            share, gaps = same_existing_share(by_chance(n, rng), n, rng, 1)
            shares.append(share)
            worst = max(worst, gaps[0][0])
        print(f"  {n:4d} selves   same-existing share {sum(shares) / len(shares):.3f}   "
              f"comes to its parities again within {worst} moments")
    print()


def study_growing():
    rng = random.Random(40404)
    say("GROWING: same-existing share, and coming back after a hand inverts one prior (of 30), as selves join")
    for build in (chain, spiral, torus, "by chance"):
        for n in (16, 64, 144):
            routes = by_chance(n, rng) if build == "by chance" else build(n)
            share, _ = same_existing_share(routes, n, rng, 30)
            name = build if isinstance(build, str) else build.__name__
            print(f"  {name:10s} {n:4d} selves   same-existing share {share:.3f}   "
                  f"comes back {comes_back(routes, n, rng, 30)}/30")
    print()


def study_carrying():
    rng = random.Random(4040)
    say("CARRYING: sixteen selves",
        "  comes back = a hand inverts one prior; its own parities come again (of 200)",
        "  told apart = two selves each receive one parity once (4 pairs); 300 moments later,"
        " how many of 4 are still told apart (mean of 40)")
    for build in (lone, spiral_of_one_each, pairs, chain, spiral, across_both_ways, torus):
        routes = build(16)
        back = comes_back(routes, 16, rng, 200)
        told = []
        for _ in range(40):
            _, soc = on_its_spiral(routes, 16, rng)
            outs = set()
            for x in (1, -1):
                for y in (1, -1):
                    s = go_on(supply(supply(soc, 0, x), 1, y), routes, 300)
                    outs.add(window(s, routes, 32))
            told.append(len(outs))
        print(f"  {build.__name__:20s} comes back {back:3d}/200   received pairs still told apart "
              f"{sum(told) / len(told):.2f} of 4")
    print()
    say("  how far one parity goes: a hand supplies + or - to self 0, once; 300 moments later,"
        " per self along, in how many of 80 is that self's sequencing told apart")
    for build in (chain, spiral, pairs):
        routes, reach = build(16), [0] * 16
        for _ in range(80):
            _, soc = on_its_spiral(routes, 16, rng)
            w = {x: window(go_on(supply(soc, 0, x), routes, 300), routes, 16) for x in (1, -1)}
            for i in range(16):
                reach[i] += [r[i] for r in w[1]] != [r[i] for r in w[-1]]
        print(f"  {build.__name__:8s}", " ".join(f"{v:2d}" for v in reach))
    print()


GROUP = {(1, 1): "++", (1, -1): "+-", (-1, 1): "-+", (-1, -1): "--"}


def reading(seq):
    """how a third self's sequencing groups the four received pairs"""
    groups = collections.defaultdict(list)
    for pair, s in seq.items():
        groups[s].append(GROUP[pair])
    parts = sorted(tuple(sorted(g)) for g in groups.values())
    if len(parts) == 1:
        return "nothing of either"
    if parts == [("++", "+-"), ("-+", "--")]:
        return "a's alone"
    if parts == [("++", "-+"), ("+-", "--")]:
        return "b's alone"
    if parts == [("++", "--"), ("+-", "-+")]:
        return "same or not same"
    if parts == sorted([("++",), ("--",), ("+-", "-+")]):
        return "both +, both -, or not same"
    if len(parts) == 4:
        return "all four apart"
    if sorted(len(g) for g in parts) == [1, 3]:
        alone = [g for g in parts if len(g) == 1][0][0]
        return f"{alone} apart from the other three"
    return "both together, grouped otherwise"


def study_third():
    rng = random.Random(4041)
    say("THIRD SELF: two selves each receive one parity once; a third self observes both across, with a gap.",
        "  300 moments later, how the third self's sequencing groups the four pairs (of 60)")
    for label, build in (
            ("gap 1, third self alone", third_self_of_two_chains(1, False)),
            ("gap 1, third self own going along", third_self_of_two_chains(1, True)),
            ("gap 2, third self alone", third_self_of_two_chains(2, False)),
            ("gap 4, third self alone", third_self_of_two_chains(4, False)),
            ("gap 8, third self alone", third_self_of_two_chains(8, False)),
            ("two spirals of 8, third self alone", third_self_of_two_spirals(8, False))):
        routes, a0, b0, m, n = build
        tally = collections.Counter()
        for _ in range(60):
            _, soc = on_its_spiral(routes, n, rng)
            seq = {}
            for x in (1, -1):
                for y in (1, -1):
                    s = go_on(supply(supply(soc, a0, x), b0, y), routes, 300)
                    seq[(x, y)] = window(s, routes, 32, m)
            tally[reading(seq)] += 1
        both = sum(v for k, v in tally.items() if k not in ("nothing of either", "a's alone", "b's alone"))
        print(f"  {label:38s} both together {both:2d}/60   " +
              ", ".join(f"{k} {v}" for k, v in tally.most_common()))
    print()


STUDIES = {"living": study_living, "growing": study_growing, "carrying": study_carrying,
           "third": study_third}

if __name__ == "__main__":
    asked = _words[0] if _words else "all"
    if asked not in STUDIES and asked != "all":
        sys.exit("A study's name: " + ", ".join(STUDIES) + ", or all.")
    for name, fn in STUDIES.items():
        if asked in (name, "all"):
            fn()
