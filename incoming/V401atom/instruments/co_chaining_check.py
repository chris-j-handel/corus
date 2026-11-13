"""A self and an other's parities arriving with a third, and a third's going out arriving with a next: each case, all or none.

A check of a reading: the co-parity or the bi-parity of a self and an other, with a third, as co-chaining and as a
fractal; with their bi-parity nothing inherited, and with their co-parity an inheriting.
One sharing. A third is a self with a prior, + or -, or the code's own state of an empty prior, no self.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/co_chaining_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one = ns["_1_now_existing"]
S = "s"
def resolve(prior, arriving):        # what goes out of a third, and its next prior
    out, nxt = one([(S, prior)] if prior is not None else [], [(S, v) for v in arriving if v is not None])
    return dict(out).get(S), dict(nxt).get(S)
PRIORS = (1, -1, None)               # a third with +, with -, and the code's own state
PM = (1, -1)

print("1  a self and an other's parities arriving with a third, each case:", len(PM) * len(PM) * len(PRIORS))
co = [(a, b, p) for a in PM for b in PM for p in PRIORS if a == b]
bi = [(a, b, p) for a in PM for b in PM for p in PRIORS if a != b]
print("   with their co-parity, a third's next prior is that co-parity, with each prior and with the code's own state:", all(resolve(p, (a, b))[1] == a for a, b, p in co))
print("   with their bi-parity, a third with a prior: its next prior is its own prior inverting:", all(resolve(p, (a, b))[1] == -p for a, b, p in bi if p is not None))
print("   with their bi-parity, a third with a prior: its next prior and its going out the same as with nothing arriving:", all(resolve(p, (a, b)) == resolve(p, ()) for a, b, p in bi if p is not None))
print("   with their bi-parity, the code's own state: nothing inherited, and a 0 goes out:", all(resolve(None, (a, b)) == (0, None) for a, b, p in bi if p is None))
print("   with their bi-parity, a third's next prior the same with + and - as with - and +:", all(resolve(p, (1, -1)) == resolve(p, (-1, 1)) for p in PRIORS))
print("   what goes out of a third: a 0 with their co-parity same-as its prior; a parity with each other case of a third with a prior:",
      all((resolve(p, (a, b))[0] == 0) == (a == b == p) for a in PM for b in PM for p in PM))

print("2  a fractal: two pairs, each with its third, and the two thirds' going out arriving with a next, each case")
n = same = 0; inherit_ok = True; kinds = {"a co-parity of the two thirds' going out": 0, "a bi-parity of them": 0, "one parity alone, the other a 0 or none": 0, "none": 0}
for a, b, d, e in itertools.product(PM, repeat=4):
    for pc, pf in itertools.product(PRIORS, repeat=2):
        for pg in PRIORS:
            n += 1
            c_out, f_out = resolve(pc, (a, b))[0], resolve(pf, (d, e))[0]
            g = resolve(pg, (c_out, f_out))
            # a pair with bi-parity, to a next: the same as that pair not sharing
            c_alt = resolve(pc, ())[0] if a != b else c_out
            f_alt = resolve(pf, ())[0] if d != e else f_out
            same += g == resolve(pg, (c_alt, f_alt))
            par = [v for v in (c_out, f_out) if v not in (0, None)]
            k = "none" if not par else "one parity alone, the other a 0 or none" if len(par) == 1 else "a co-parity of the two thirds' going out" if par[0] == par[1] else "a bi-parity of them"
            kinds[k] += 1
            if pg is None:
                inherit_ok = inherit_ok and g[1] == (par[0] if par and len(set(par)) == 1 else None)
print("   cases:", n)
print("   a pair's bi-parity is, with a next, the same as that pair not sharing, with each case:", same == n)
print("   with a next the code's own state, what is inherited is the one parity of the thirds' going out, as it is, and nothing with a bi-parity of them:", inherit_ok)
print("   what arrives with a next is one of four, each with a case:", "; ".join(kinds), ":", all(v > 0 for v in kinds.values()))
