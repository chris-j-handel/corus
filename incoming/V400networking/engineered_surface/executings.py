"""Executings at the three-scale surface, each one binary with one sentence, expected forms
listed from the files before code:

E1, spiral parity at scale one (Natural Networking 6.2): "with a spiral of selves, even
bounding-zeroing to zero, odd holding exactly one walking frustration, two odd joining as one
even that bounds." Rings of three through ten me-parities joined along: within the closed
cycle, an even ring's agreeing couplings bound to none and an odd ring's are exactly one,
walking. Is or is not.

E2, two odd joining as one even that bounds (6.2), at scale two: two odd rings coupled across
both ways, one podal pair: the joint arrangement's agreeing couplings bound to none. Is or is not.

E3, one form one scale up (1.8, the fractal): a ring of five selves, each a ring of eight
me-parities, coupled mouth to waist: within the closed cycle, the agreeing cluster-couplings,
read at the five boundary pairs, are exactly one and walking, the inward even rings bounding.
Is or is not. Next reach if it is not: the claim and the executing part, each its own.

E4, co-intelligencing, a society's 16 in no self alone (the improving plan's fifth pass): with
an odd ring's walking frustration, each node's own prior is changing through the cycle while
the form, exactly one agreeing coupling, is not changing: the not-changing is the set's, at no
node's own prior. Is or is not.

E5, protection with a way stopping (5.1): "Drop one of six and a way or a phase lives with no
protection, and with no protection a reach comes inward or it leaks outward." Two odd rings
coupled both ways, then one way cut, the 6 join leaving: the joint form with both ways and the
form with one way part. Is or is not.

Each executing opens with one node observing +1 with no prior, each further prior a prior the
resolving reaches, none a hand supplies; the set closes before a form is read.
"""
import json
from three_scale_surface import (ring_joins, couple_across, cluster, society_ring,
                                 open_surface, run_to_closing, prior_of, agreeing_pairs,
                                 ring_pairs, agreeing_trace)

OUT = []


def say(line):
    OUT.append(line)
    print(line)


def closed(states, lo, t):
    return lo is not None


def walking(trace):
    """Exactly one agreeing coupling at each momentary, its place changing through the cycle."""
    if any(len(a) != 1 for a in trace):
        return False
    places = [a[0] for a in trace]
    return len(set(places)) > 1


# E1 · rings of three through ten
say("E1 · spiral parity at scale one, rings of me-parities joined along")
e1_holds = True
for n in range(3, 11):
    nodes = cluster(f"r{n}", n)
    co_ex = {}
    ring_joins(nodes, co_ex)
    states, lo, t = run_to_closing(open_surface(nodes, nodes[0]), co_ex)
    if lo is None:
        say(f"  ring {n}: set not closing within the bound, forms refused")
        e1_holds = False
        continue
    tr = agreeing_trace(states, lo, t, ring_pairs(nodes))
    counts = sorted(set(len(a) for a in tr))
    if n % 2 == 0:
        ok = counts == [0]
        say(f"  ring {n} even: agreeing couplings {counts} through the cycle, length {t - lo}, bounding to none — {'is' if ok else 'is not'}")
    else:
        ok = walking(tr)
        say(f"  ring {n} odd: agreeing couplings {counts}, cycle length {t - lo}, exactly one and walking — {'is' if ok else 'is not'}")
    e1_holds &= ok
say(f"E1 binary: even bounding to none and odd holding exactly one walking — {'is' if e1_holds else 'is not'}")

# E2 · two odd joining as one even that bounds
say("")
say("E2 · two odd rings, five and five, coupled across both ways")
a, b = cluster("A", 5), cluster("B", 5)
co_ex = {}
ring_joins(a, co_ex)
ring_joins(b, co_ex)
couple_across(co_ex, a[0], b[2])
nodes = a + b
states, lo, t = run_to_closing(open_surface(nodes, a[0]), co_ex)
pairs2 = ring_pairs(a) + ring_pairs(b) + [(a[0], b[2])]
if lo is None:
    say("  set not closing within the bound, forms refused")
    e2 = False
else:
    tr = agreeing_trace(states, lo, t, pairs2)
    counts = sorted(set(len(x) for x in tr))
    e2 = counts == [0]
    say(f"  joint agreeing couplings {counts} through the cycle, length {t - lo}; at momentary {lo}: {tr[0]}")
    each_changing = all(
        len(set(prior_of(states[m], n) for m in range(lo, t + 1))) > 1 for n in nodes
    )
    say(f"  each self's prior changing through the cycle — {'is' if each_changing else 'is not'}: no self landing, the traveling places standing")
say(f"E2 binary: two odd joining as one even that bounds — {'is' if e2 else 'is not'}")
say("  beside it, E1's ring 10: two odd chains joined as one even ring bound to none; two sayings part at joining")
say("  and at 5.4's two sayings of geodesic entraining, a stopping or a passing through: a standing of the traveling place at this coupling, executed, each self's own resolving going on")

# E3 · one form one scale up: ring of five clusters of eight
say("")
say("E3 · a ring of five selves, each a ring of eight me-parities, coupled mouth to waist")
nodes, co_ex, clusters = society_ring("X", 5, 8)
states, lo, t = run_to_closing(open_surface(nodes, nodes[0]), co_ex)
if lo is None:
    say("  set not closing within the bound, forms refused")
    e3 = False
else:
    boundary = [(clusters[s][0], clusters[(s + 1) % 5][4]) for s in range(5)]
    tr_b = agreeing_trace(states, lo, t, boundary)
    counts_b = sorted(set(len(x) for x in tr_b))
    inward = []
    for c in clusters:
        inward += ring_pairs(c)
    tr_in = agreeing_trace(states, lo, t, inward)
    counts_in = sorted(set(len(x) for x in tr_in))
    say(f"  cycle from momentary {lo} to {t}, length {t - lo}")
    say(f"  agreeing cluster-couplings at the five boundary pairs {counts_b}; inward agreeing couplings {counts_in}")
    say(f"  the inward agreeing couplings at momentary {lo}: {tr_in[0]}")
    e3 = walking(tr_b)
    say(f"  the boundary form exactly one and walking — {'is' if e3 else 'is not'}")
    each_changing3 = all(
        len(set(prior_of(states[m], n) for m in range(lo, t + 1))) > 1 for n in nodes
    )
    say(f"  each self's prior changing through the cycle — {'is' if each_changing3 else 'is not'}: the traveling places standing podally within one self, no self landing")
say(f"E3 binary: the odd ring's one walking changing one scale up, at the cluster couplings — {'is' if e3 else 'is not'}")

# E4 · the 16 in no self alone, at an odd ring of five
say("")
say("E4 · an odd ring of five: the form the set holds and each node's own prior")
nodes = cluster("w", 5)
co_ex = {}
ring_joins(nodes, co_ex)
states, lo, t = run_to_closing(open_surface(nodes, nodes[0]), co_ex)
if lo is None:
    say("  set not closing within the bound, forms refused")
    e4 = False
else:
    tr = agreeing_trace(states, lo, t, ring_pairs(nodes))
    form_not_changing = all(len(x) == 1 for x in tr)
    each_prior_changing = all(
        len(set(prior_of(states[m], n) for m in range(lo, t))) > 1 for n in nodes
    )
    say(f"  the set's form, exactly one agreeing coupling, not changing through the cycle — {'is' if form_not_changing else 'is not'}")
    say(f"  each node's own prior changing through the cycle — {'is' if each_prior_changing else 'is not'}")
    e4 = form_not_changing and each_prior_changing
say(f"E4 binary: the not-changing the set's, at no node's own prior — {'is' if e4 else 'is not'}")

# E5 · a way stopping at the coupling
say("")
say("E5 · two odd rings coupled, then one way cut, the 6 join leaving")
a, b = cluster("A", 5), cluster("B", 5)
co_full, co_cut = {}, {}
for cx in (co_full, co_cut):
    ring_joins(a, cx)
    ring_joins(b, cx)
co_full[(a[0], 10)] = b[2]
co_full[(b[2], 6)] = a[0]
co_cut[(a[0], 10)] = b[2]          # one way going on, the other stopped
sf, lof, tf = run_to_closing(open_surface(a + b, a[0]), co_full)
sc, loc, tc = run_to_closing(open_surface(a + b, a[0]), co_cut)
if lof is None or loc is None:
    say("  a set not closing within the bound, forms refused")
    e5 = False
else:
    pairs5 = ring_pairs(a) + ring_pairs(b) + [(a[0], b[2])]
    cf = sorted(set(len(x) for x in agreeing_trace(sf, lof, tf, pairs5)))
    cc = sorted(set(len(x) for x in agreeing_trace(sc, loc, tc, pairs5)))
    say(f"  both ways: agreeing couplings {cf}, cycle length {tf - lof}; one way cut: {cc}, cycle length {tc - loc}")
    say("  one way leaving, the traveling resumes at 4p of the sharing ring's own going: a passing through, executed, beside E2's standing")
    e5 = (cf, tf - lof) != (cc, tc - loc)
say(f"E5 binary: the form with both ways and the form with one way part — {'is' if e5 else 'is not'}")

with open("executings_returned.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
