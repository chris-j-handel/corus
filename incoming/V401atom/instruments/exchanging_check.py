"""One binary with each 1 to 17 and each thing: an exchanging, is or is not. Each case, all or none. No opening by chance.

A self with a prior, + or -, and none to three parities arriving, each +, - or 0. Its 14-next-possibling, its
12-next-co-same-existing, its next prior with 11 and its co-possibling with 10. And two selves with one between,
each co-possibling arriving with its other, each of four cases of their priors.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/exchanging_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"
cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]
def fourteen(c):
    seen = {v for v in c if v != 0}
    return None if not seen else (seen.pop() if len(seen) == 1 else 0)
n = 0; ok1 = ok2 = ok3 = ok4 = True; kinds = set()
for p in (1, -1):
    for c in cases:
        n += 1
        out, nxt = one([(S, p)], [(S, v) for v in c]); ten, eleven = dict(out)[S], dict(nxt)[S]
        m = fourteen(c)
        kinds.add((ten != 0, eleven != p))
        if m == p:                      # nothing distinguished
            ok1 = ok1 and ten == 0 and eleven == p
        elif m in (1, -1):              # distinguished with a parity arriving
            ok2 = ok2 and ten == m and eleven == m
        else:                           # nothing arriving, each a 0, or two not the same
            ok3 = ok3 and ten == -p and eleven == -p
        ok4 = ok4 and ((ten == 0 and eleven == p) or (ten == eleven == -p))
print("cases, a prior + or -, with none to three arriving, each +, - or 0:", n)
print("1  14 the same as a self's prior, nothing distinguished: 10 is a 0 and its prior is the same:", ok1)
print("2  14 a parity and its prior the other one, a distinguishing: its next prior with 11 is the parity arriving, as it is,")
print("   and its co-possibling with 10 is that same parity:", ok2)
print("3  14 nothing or a 0, a distinguishing: its next prior with 11 and its co-possibling with 10 are its prior inverted:", ok3)
print("4  with each case one binary and no third: 10 a 0 with its prior the same, or 10 and 11 one same parity, its prior inverted:", ok4 and len(kinds) == 2)
ok5 = True
for pa, pb in itertools.product((1, -1), repeat=2):
    soc = {"a": ([(S, pa)], []), "b": ([(S, pb)], [])}; net = {("a", 10): "b", ("b", 10): "a"}
    for t in range(16):
        ten = {k: [v for _key, v in one(list(soc[k][0]), list(soc[k][1]))[0]] for k in soc}
        soc = step(soc, net)
        ok5 = ok5 and [v for _k, v in soc["b"][1]] == ten["a"] and [v for _k, v in soc["a"][1]] == ten["b"]
print("5  two selves with one between, each of four cases of their priors: with each 1 to 17 a self's co-possibling with 10")
print("   is its other's possibling with 2, as it is, each of the two with its other:", ok5)
