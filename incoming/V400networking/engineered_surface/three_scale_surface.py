"""Three-scale engineered surface at Exhibit ONE v391's resolver, a coupling partner deciding nothing.

The same code at every node, nothing new in the resolving: `resolver.py` beside this file is
Exhibit ONE v391's code block unchanged, sha256
b7fe62c4e5d529ebe374d6a037a7ac7ac81a78e176db2cbfd96fda3f23db2435, and the scales live in the
join arrangement alone. Natural Networking 1.8: across names one scale are along 9s one scale
inward, bi-tunneling here co-chaining inward; so one wire has two scale readings, and a
society's parity outward is one self's, through its coupling (1.10) -- no gathering function.

The instrument stated whole, Natural Networking 6.2:
- Wiring: nodes are me-parities, each a resolver. A self is a ring of me-parities joined along,
  each node's 9 to the next around the ring. A coupling across between two selves is one podal
  pair of boundary nodes, A's 10 to B and B's 6 to A, both ways. A society is a ring of selves
  so coupled, mouth 0 to waist size//2; two societies couple through one further podal pair,
  size//4 and 3*size//4. One key, 'k', with each sharing, parities gathering at a receiving 14.
- Pace: none of the network's own; the code steps each self's 1-now-existing together with
  17-next-existing, its executing's own arrangement, stated.
- Executing order: insertion order of the society dict, stated; parities deliver with the next
  momentary, none pending, so its *taking* is none.
- Record: each executing's trace at its returned .txt beside this file, momentary by momentary,
  each node's prior and sharing.
- Ledger: node names <society>.<self>.m<n>, the instrument's own; the resolving reads none of it.
- Refusings, each stated: a sharing whose (self, connector) is at no join leaves with its
  momentary, the code's own condition; an executing not closing its set within 4096 momentaries
  refuses its forms rather than handing back a window as a last (6.6); the state canonicalizing
  sorts each list, an instrument's ordering.

An observing is a binary, is or is not (6.4); a number printed is an accounting of an observing
and not that observing. The set closes before a form is read: forms are read only within the
joint form's recurring cycle, after each prior is present.

Usage: python3 three_scale_surface.py  (writes returned traces beside itself)
"""
import resolver


def ring_joins(nodes, co_ex):
    n = len(nodes)
    for i, a in enumerate(nodes):
        co_ex[(a, 9)] = nodes[(i + 1) % n]


def couple_across(co_ex, a, b):
    co_ex[(a, 10)] = b
    co_ex[(b, 6)] = a


def cluster(name, size):
    return [f"{name}.m{i}" for i in range(size)]


def society_ring(name, n_clusters, c_size):
    """A ring of selves: clusters joined along inward, coupled across around the ring."""
    nodes, co_ex, clusters = [], {}, []
    for s in range(n_clusters):
        c = cluster(f"{name}.s{s}", c_size)
        clusters.append(c)
        nodes += c
        ring_joins(c, co_ex)
    for s in range(n_clusters):
        a = clusters[s][0]                      # mouth
        b = clusters[(s + 1) % n_clusters][c_size // 2]  # next self's waist
        couple_across(co_ex, a, b)
    return nodes, co_ex, clusters


def open_surface(nodes, seed):
    soc = {n: ([], []) for n in nodes}
    soc[seed] = ([], [("k", 1)])
    return soc


def canon(soc):
    return tuple(sorted((n, tuple(sorted(p)), tuple(sorted(o))) for n, (p, o) in soc.items()))


def run_to_closing(soc, co_ex, bound=4096):
    """Steps until the joint form recurs with each prior present; refuses past the bound."""
    seen, states = {}, []
    for t in range(bound):
        soc = resolver._17_next_existing(soc, co_ex)
        states.append(soc)
        priors_present = all(p for p, _ in soc.values())
        key = canon(soc)
        if key in seen and priors_present:
            return states, seen[key], t  # cycle from states[seen[key]] to states[t-1], t == recurrence
        seen[key] = t
    return states, None, None  # set not closing within the bound: forms refused


def prior_of(soc, node):
    return dict(soc[node][0]).get("k", 0)


def agreeing_pairs(soc, pairs):
    """The couplings among the given (a, b) pairs whose two priors agree now."""
    out = []
    for a, b in pairs:
        pa, pb = prior_of(soc, a), prior_of(soc, b)
        if pa != 0 and pa == pb:
            out.append((a, b))
    return out


def ring_pairs(nodes):
    n = len(nodes)
    return [(nodes[i], nodes[(i + 1) % n]) for i in range(n)]


def agreeing_trace(states, lo, hi, pairs):
    """Per momentary within the cycle: the agreeing couplings among the pairs, each the place resolving is traveling."""
    return [agreeing_pairs(states[t], pairs) for t in range(lo, hi)]
