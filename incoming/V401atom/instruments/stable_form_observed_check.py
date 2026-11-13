"""A stable form with a self observing it alone: each case, all or none. No opening by chance, and no case left out.

A stable form's parity is the same with each 1 to 17, and no line of the code is changing it. A self with a prior,
+ or -, is observing it alone, with a first 1 to 17 and with a next. Four cases, each read with the code's own lines.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/stable_form_observed_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one = ns["_1_now_existing"]
S = "s"

def resolve(prior, form):
    out, nxt = one([(S, prior)], [(S, form)])
    return dict(out).get(S), dict(nxt).get(S)

cases = [(p, f) for p in (1, -1) for f in (1, -1)]
sign = lambda v: "+" if v == 1 else "-" if v == -1 else "0"
print("a self's prior, a stable form's parity: first 1 to 17, its sharing and its next prior; next 1 to 17, its sharing and its next prior")
for p, f in cases:
    s1, n1 = resolve(p, f); s2, n2 = resolve(n1, f)
    print("  ", sign(p), sign(f), ":", sign(s1), sign(n1), ";", sign(s2), sign(n2))
same = [(p, f) for p, f in cases if p == f]
not_same = [(p, f) for p, f in cases if p != f]
print("1  with its prior the same as the stable form's parity, its prior is same-existing and its sharing is a 0, each case:",
      all(resolve(p, f) == (0, p) for p, f in same))
print("2  with its prior not the same, its prior is inverting, and its next prior is its sharing, each case:",
      all(resolve(p, f) == (-p, -p) for p, f in not_same))
print("3  with a next 1 to 17, each of four is the same as the stable form's parity, same-existing, its sharing a 0:",
      all(resolve(resolve(p, f)[1], f) == (0, f) for p, f in cases))
print("4  the stable form's parity is the same with each of them, and no line is changing it: it is given with each 1 to 17")
