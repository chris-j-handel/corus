"""A bi-coupling of a self and an other, both ways: what goes across each way with each 1 to 17, each case of their two priors.

A check of a reading: one parity with the between of a bi-coupling, with a direction; bi co bi with the centre
of a five, each name with its first prefix from Exhibit ONE's table; and bi-parity as an opening, a 0 between,
with the names of resolving after it.
Exhibit ONE's table and code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/between_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"; say = lambda v: "." if v is None else "+" if v > 0 else "-" if v < 0 else "0"
net = {("self", 10): "other", ("other", 10): "self"}

def across(a, b, T=18):
    soc = {"self": ([(S, a)], []), "other": ([(S, b)], [])}
    rows = []
    for t in range(T):
        out = {k: dict(one(soc[k][0], soc[k][1])[0]).get(S) for k in soc}
        rows.append((dict(soc["self"][0]).get(S), dict(soc["other"][0]).get(S), out["self"], out["other"]))
        soc = step(soc, net)
    return rows[2:]                      # from a third 1 to 17, each self with a parity or a 0 arriving

print("1  a self and an other bi-coupling both ways, each case of their two priors")
res = {}
for a in (1, -1):
    for b in (1, -1):
        r = across(a, b); res[(a, b)] = r
        print(f"   a self {say(a)} and its other {say(b)}: going across from a self {''.join(say(x[2]) for x in r)}   from its other {''.join(say(x[3]) for x in r)}")
co = [res[k] for k in res if k[0] == k[1]]; bi = [res[k] for k in res if k[0] != k[1]]
print("   with co-parity, the two going across are one same with each 1 to 17, a parity or a 0:", all(x[2] == x[3] for r in co for x in r))
print("   with co-parity, that one parity and a 0 are in turn, and the parity inverts with each turn:",
      all([x[2] for x in r][i] == 0 or [x[2] for x in r][i] == -[x[2] for x in r][i - 2] for r in co for i in range(2, len(r))) and all((r[i][2] == 0) != (r[i + 1][2] == 0) for r in co for i in range(len(r) - 1)))
print("   with bi-parity, the two going across are not the same with each 1 to 17, one + and one -, and no 0:", all(x[2] == -x[3] and x[2] != 0 for r in bi for x in r))
print("   with bi-parity, each going across inverts with each 1 to 17:", all(r[i][2] == -r[i + 1][2] for r in bi for i in range(len(r) - 1)))

rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([^|]+) \| ([^|]+) \| (\w+) \| ([\w-]+) \|$", src, re.M)
first = {int(n): t.split("-")[0] for n, _a, _r, _b, _c, t in rows}
print("2  bi co bi about the centre of a five, each name with its first prefix")
for name, five in (("1 to 5, its centre 3", (1, 2, 3, 4, 5)), ("3 to 7, its centre 5", (3, 4, 5, 6, 7))):
    c = five[2]
    print(f"   {name}: {' '.join(first[n] for n in five)} ; about its centre: {first[c - 1]} {first[c]} {first[c + 1]}")
print("   each odd name of 3 to 15 has bi with the name before it and with the name after it:", all(first[n - 1] == "bi" and first[n + 1] == "bi" for n in range(3, 16, 2)))
print("   the diamond, across: 3-5-7:", " ".join(first[n] for n in (3, 5, 7)), "; along: 1-5-9:", " ".join(first[n] for n in (1, 5, 9)))

import itertools
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
body = code[code.index("def _1_now_existing"):code.index("def _9_next_co_discovering")]
order = sorted(set(re.findall(r"^\s+(_\d+_[a-z_]+?)(?:\[[^\]]*\])? = ", body, re.M)), key=lambda n: body.index(n + " =") if n + " =" in body else body.index(n + "["))
names = [n.strip("_").replace("_", "-") for n in order]
print("3  bi-parity as an opening, a 0 between")
cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]
zero = lambda c: dict(one([], [(S, v) for v in c])[0]).get(S) == 0
print("   a 0 with 14-next-possibling with one case only, two parities arriving not the same:", all(zero(c) == ({1, -1} <= set(c)) for c in cases))
print("   the names of 1-now-existing's lines, in the code's order:", ", ".join(names))
i = names.index("14-next-possibling")
print("   after 14-next-possibling its next is 15-next-observing, of one:", names[i + 1] == "15-next-observing", "; and each name after the two is a co name:", all("-co-" in n for n in names[i + 2:]))
evens = [n for n in sorted(first) if n % 2 == 0]
print("   each name with bi first, its next name:", " ".join(f"{n}:{first[n + 1]}" for n in evens), "; co or tri with each:", all(first[n + 1] in ("co", "tri") for n in evens))
print("   a self and an other with bi-parity, bi-coupling both ways: bi-parity again with each 1 to 17, and co-parity with none:", all(x[0] == -x[1] for r in bi for x in r))

print("4  what goes out of a self, and each name's three")
def res(prior, arriving):
    out, nxt = one([(S, prior)] if prior is not None else [], [(S, v) for v in arriving])
    return dict(out).get(S), dict(nxt).get(S)
goes_on = lambda p, c: any(v != 0 for v in c) and all(v == p for v in c if v != 0)
print("   with a self's prior going on, each arriving parity same-as it, a 0 goes out; with each other case a parity goes out:",
      all((res(p, c)[0] == 0) == goes_on(p, c) and (goes_on(p, c) or res(p, c)[0] in (1, -1)) for p in (1, -1) for c in cases))
print("   a 0 arriving is the same as nothing arriving, with each case, a self with a prior and the code's state:",
      all(res(p, c) == res(p, tuple(v for v in c if v != 0)) for p in (1, -1, None) for c in cases))
threes = {int(n): t.split("-") for n, _a, _r, _b, _c, t in rows}
co_now = [n for n in sorted(threes) if threes[n][1] == "co"]; bi_now = [n for n in sorted(threes) if threes[n][1] == "bi"]
print("   each name with co its now has bi its next and bi its prior:", all(threes[n][0] == "bi" and threes[n][2] == "bi" for n in co_now), co_now)
print("   each name with bi its now has co or tri its next and its prior:", all(threes[n][0] in ("co", "tri") and threes[n][2] in ("co", "tri") for n in bi_now), bi_now)
print("   each name of the seventeen is one of the two, or has tri its now:", sorted(set(threes) - set(co_now) - set(bi_now)), [("-".join(threes[n])) for n in sorted(set(threes) - set(co_now) - set(bi_now))])
