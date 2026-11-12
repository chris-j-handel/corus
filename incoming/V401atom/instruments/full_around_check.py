"""A 0 going one full around a spiral of selves, executed with Exhibit ONE's code, no line changed.

A check of a reading: with each full around of its 0, each self is one momentary on from a plain one-and-then-the-other.
Run: python3 incoming/V401atom/instruments/full_around_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
step = ns["_17_next_existing"]
one = ns["_1_now_existing"]
S = "s"

def rows(n, T):
    """each self's 10 with each momentary, a spiral of n along with 9, + once with self 1, recorded as the kit's own executing."""
    net = {(k, 9): (k + 1) % n for k in range(n)}
    soc = {k: ([], [(S, 1)] if k == 0 else []) for k in range(n)}
    out = {k: [] for k in range(n)}
    for t in range(T):
        nxt = step(soc, net)
        for k in range(n):
            ten, _ = one(soc[k][0], soc[k][1])
            v = dict(ten).get(S)
            out[k].append("." if v is None else "+" if v > 0 else "-" if v < 0 else "0")
        soc = {k: (nxt[k][0], [(S, v) for (_key, v) in nxt[k][1]]) for k in nxt}
    return out

for n in (3, 5, 7, 9, 11):
    T = 12 * n
    r = rows(n, T)
    z = [t + 1 for t, c in enumerate(r[0]) if c == "0"]
    zk = [[t + 1 for t, c in enumerate(r[k]) if c == "0"][0] for k in range(n)]
    around = z[1] - z[0]
    a, b = z[1], z[2]                      # one full around, from a 0 with self 1 to its next 0 with self 1
    seg = r[0][a:b - 1]                     # momentaries between two 0s
    plain = all(seg[i] != seg[i + 1] for i in range(len(seg) - 1))
    inv = all({r[k][t], r[k][t + around]} in ({"+", "-"}, {"0"}) for k in range(n) for t in range(4 * n, 6 * n))
    same = all(r[k][t] == r[k][t + 2 * around] for k in range(n) for t in range(4 * n, 6 * n))
    print(f"spiral of {n}: a 0 one self on with each {zk[1]-zk[0]} momentaries; one full around {around} momentaries;"
          f" between two 0s a self has {len(seg)} parities, one and then the other: {plain};"
          f" each self inverted with one full around: {inv}; the same with two: {same}")
print("self 1 of a spiral of 5:", "".join(rows(5, 24)[0]))
