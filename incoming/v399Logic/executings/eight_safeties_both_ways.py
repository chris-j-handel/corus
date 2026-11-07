# v399Logic, 7 November 2026: a reconstruction of Exhibit ONE v391's one-sharing cell table (its lines 798-811),
# not Exhibit ONE's own code. For each case, which is-or-is-nots of each self go both ways and which fix as one,
# over moments 100-199. Binaries per self: a parity reaches it (is-or-is-not); agreeing with its prior (is-or-is-not);
# its sharing is 0 (is-or-is-not); its prior inverting (is-or-is-not).
def step(p, r):
    return (p, 0) if r == p else (-p, -p)            # agreeing: prior same-existing, share 0; else prior inverts
def run(n, src, start, outside=None, steps=200):
    pri = list(start); shared = [None]*n; log = [[] for _ in range(n)]
    for t in range(steps):
        new = shared[:]
        for i in range(n):
            r = outside(t) if (outside and i == 0) else (shared[src[i]] if src[i] is not None else None)
            if r == 0: r_eff = 0
            else: r_eff = r
            p0 = pri[i]; pri[i], new[i] = step(p0, r_eff)
            log[i].append((r is not None and r != 0, r_eff == p0, new[i] == 0, pri[i] != p0))
        shared = new
    out = []
    for i in range(n):
        late = log[i][100:]
        fixed = [name for k, name in enumerate(["reaching", "agreeing", "sharing 0", "inverting"]) if len({x[k] for x in late}) == 1]
        out.append(fixed)
    return out
cases = {
  "alike pair, both ways":            (2, [1, 0], [-1, -1], None),
  "opposite pair, both ways":         (2, [1, 0], [-1, 1], None),
  "one self, nothing reaching":       (1, [None], [1], None),
  "ring of five, re-closed":          (5, [4, 0, 1, 2, 3], [1]*5, None),
  "chain of five, open at one end":   (5, [None, 0, 1, 2, 3], [1]*5, None),
  "alike pair, + offered by no self to one": (2, [1, 0], [1, 1], lambda t: 1),
}
for name, (n, src, start, outside) in cases.items():
    res = run(n, src, start, outside)
    print(f"{name:42s}", " | ".join(f"self {i}: " + (", ".join(f) if f else "all go both ways") for i, f in enumerate(res)))
