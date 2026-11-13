"""Along and across as two spirals of one torus of selves, executed with Exhibit ONE's code, no line changed.

A check of a reading: each of along and across with its own number of selves, and what the whole comes to again with.
Run: python3 incoming/V401atom/instruments/along_across_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
step = ns["_17_next_existing"]
S = "s"

def again(p, q, along=9, across=10):
    sel = [(i, j) for i in range(p) for j in range(q)]
    net = {}
    for (i, j) in sel:
        if p > 1: net[((i, j), along)] = ((i + 1) % p, j)
        if q > 1: net[((i, j), across)] = (i, (j + 1) % q)
    soc = {(i, j): ([(S, -1 if (i + j) % 2 == 0 else 1)], []) for (i, j) in sel}
    key = lambda s: tuple((tuple(sorted(s[k][0])), tuple(sorted(s[k][1]))) for k in sel)
    seen, t = {}, 0
    while True:
        k = key(soc)
        if k in seen: return t - seen[k]
        seen[k] = t
        soc = step(soc, net)
        t += 1

print("a spiral alone, n selves along: again with", {n: again(n, 1) for n in (3, 5, 7, 9, 11, 13)})
print("a spiral alone, n selves across: again with", {n: again(1, n) for n in (3, 5, 7, 9, 11, 13)})
print("p along by q across: again with")
for p, q in [(3, 5), (3, 7), (3, 13), (5, 7), (5, 9), (5, 11), (5, 13), (7, 9), (7, 13), (7, 15), (3, 4), (4, 5)]:
    a, b = again(p, q), again(q, p)
    print(f"  {p} by {q}: {a}; {q} by {p}: {b}; alone {4*p if p%2 else 2} and {4*q if q%2 else 2}")
print("along with 10 and across with 9, 3 by 5:", again(3, 5, along=10, across=9), "; along with 6 and across with 10, 3 by 5:", again(3, 5, along=6, across=10))
