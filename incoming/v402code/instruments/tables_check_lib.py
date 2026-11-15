"""v402code · the helpers of tables_check.py, for each other instrument · each code table of Exhibit ONE Natural Resolver, executed against the
code taken word for word from the living file. Deciding nothing; reporting same / not same.
Run, from outside the set's folder, R the set's folder: python3 -I tables_check.py R
"""
import importlib.util, sys, os
from math import gcd

import re, glob
R = sys.argv[1] if len(sys.argv) > 1 else "."
_living = sorted(glob.glob(os.path.join(R, "Exhibit_ONE_Natural_Resolver_v*.md")))[-1]
_code = re.search(r"```python\n(.*?)\n```", open(_living, encoding="utf-8").read(), re.S).group(1)
_ns = {}; exec(_code, _ns)
# the code's three functions by their order in the living file, and by no name
ONE, NINE, SEVENTEEN = [v for k, v in _ns.items() if callable(v) and not k.startswith("__")]

S = "s"                      # the one sharing
SYM = {1: "+", -1: "−", 0: "0", None: "·"}
def sym(v): return SYM[v]
def P(ch): return {"+": 1, "−": -1, "-": -1, "0": 0}[ch]

results = []
def report(name, same, detail=""):
    results.append((name, same))
    print(("SAME      " if same else "NOT SAME  ") + name + ((" :: " + detail) if detail else ""))

# ---------------------------------------------------------------- one self
def one(prior, incoming):
    """prior: None or ±1 ; incoming: list of parities for the one sharing.
    returns (sharing value or None if no sharing listed, next prior or None)"""
    pr = [] if prior is None else [(S, prior)]
    out, nxt = ONE(pr, [(S, v) for v in incoming])
    out = dict(out); nxt = dict(nxt)
    return out.get(S, None), nxt.get(S, None)

def surfacing(incoming):
    """14-next-possibling for one sharing with an empty prior: the 10 list equals 12 = 14."""
    out, _ = ONE([], [(S, v) for v in incoming])
    d = dict(out)
    return d.get(S, "empty")

# ---------------------------------------------------------------- societies
def step(soc, routes):
    """one momentary of a same-existing-society; also returns each self's 10 list
    (found by executing 1-now-existing on the same given, as 17-next-existing does)."""
    shared = {k: dict(ONE(pr, inc)[0]).get(S, None) for k, (pr, inc) in soc.items()}
    return SEVENTEEN(soc, routes), shared

def run(priors, routes, T, first_incoming=None):
    soc = {k: (([] if p is None else [(S, p)]), list((first_incoming or {}).get(k, []))) for k, p in priors.items()}
    shares, pri = [], []
    for _ in range(T):
        soc, sh = step(soc, routes)
        shares.append(sh)
        pri.append({k: dict(v[0]).get(S, None) for k, v in soc.items()})
    return shares, pri

def spiral(n, tag=""):
    selves = [(tag, i) for i in range(n)]
    priors = {k: (-1 if k[1] % 2 == 0 else 1) for k in selves}
    routes = {((tag, i), 9): (tag, (i + 1) % n) for i in range(n)}
    return priors, routes

def least_period(seq, start=0):
    """least p with seq[t+p]==seq[t] for all t>=start (within the run)"""
    n = len(seq)
    for p in range(1, (n - start) // 2 + 1):
        if all(seq[t] == seq[t + p] for t in range(start, n - p)): return p
    return None

def eventual(seq, maxp=None):
    """(first index from which seq is periodic, that least period); index 0-based"""
    n = len(seq)
    best = None
    for p in range(1, (maxp or n // 3) + 1):
        t = n - p - 1
        while t >= 0 and seq[t] == seq[t + p]: t -= 1
        start = t + 1
        if start < n - 2 * p:
            if best is None or start < best[0] or (start == best[0] and p < best[1]):
                best = (start, p)
            if best and best[0] == start and p == best[1]:
                pass
    # choose least period among those reaching the earliest start
    return best


def lcm(a, b): return a * b // gcd(a, b)
def two_spirals(m, n, coupled):
    pa, ra = spiral(m, "A"); pb, rb = spiral(n, "B")
    pr = {**pa, **pb}; ro = {**ra, **rb}
    if coupled:
        ro[(("A", 0), 10)] = ("B", 0); ro[(("B", 0), 10)] = ("A", 0)
    return pr, ro
