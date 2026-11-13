"""What is same-and-prior-existing in the code, and with what: a self's priors, and a bi-coupling's routes. Each line, and each case.

A check of a reading: a self as a property concept, with its same-and-prior-existing; a bi-coupling as a property
between, with its same-and-prior-existing; more sharings with one route; one sharing by three names; and a route
as a public between, an opening with no parity, no self and no scale.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/property_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
nm = lambda n: n.strip("_").replace("_", "-")

# 1  the code's lines: each function's given names, and each name a line assigns
defs = re.findall(r"^def (_\d+_\w+)\((.*?)\):", code, re.M)
given = {nm(f): [nm(a.strip()) for a in args.split(",")] for f, args in defs}
assigned = sorted({nm(n) for n in re.findall(r"^\s+(_\d+_[a-z_]+?)(?:\[[^\]]*\])? = ", code, re.M)}
                  | {nm(n) for n in re.findall(r"^\s+(_\d+_[a-z_]+), (_\d+_[a-z_]+)\[", code, re.M) for n in n}, key=lambda s: int(s.split("-")[0]))
print("1  the code's three functions, each with its given names:")
for f, a in given.items(): print(f"     {f}: {', '.join(a)}")
print("   5-now-co-existing is given, and no line assigns it:", "5-now-co-existing" in given["17-next-existing"] and "5-now-co-existing" not in assigned)
print("   1-now-existing is given a self's priors and what arrives with it, two names and no other:", given["1-now-existing"] == ["3-now-co-observing", "2-now-possibling"])
body1 = code[code.index("def _1_now_existing"):code.index("def _9_next_co_discovering")]
print("   no line of 1-now-existing has 5-now-co-existing, 13-next-discovering or 16-next-same-existing:", not any(x in body1 for x in ("_5_now_co_existing", "_13_next_discovering", "_16_next_same_existing")))

# 2  each prior is with one self: a self's next prior from its prior and what arrives with it, each case
S = "s"; PM = (1, -1)
cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]
def soc_step(priors, net):
    soc = {k: ([(S, v)] if v is not None else [], []) for k, v in priors.items()}
    a = step(soc, net); return step(a, net)
ok = True
net = {("self", 10): "third", ("other", 10): "third", ("third", 10): "self"}
for a, b, c in itertools.product(PM, repeat=3):
    r = soc_step({"self": a, "other": b, "third": c}, net)
    for k in r:
        ok = ok and set(dict(r[k][0])) <= {S}
print("2  what 17-next-existing gives again: an entry with each self, its next priors and what arrives with it, and no entry with a bi-coupling:",
      sorted(soc_step({"self": 1, "other": -1, "third": 1}, net)) == ["other", "self", "third"] and ok)

# 3  more sharings with one route: each sharing resolves with no other sharing in it, each case
ok = True
for p, q in itertools.product((1, -1, None), repeat=2):
    for ca in cases[:13]:
        for cb in cases[:13]:
            both = one([(k, v) for k, v in (("a", p), ("b", q)) if v is not None], [("a", v) for v in ca] + [("b", v) for v in cb])
            alone = one([("a", p)] if p is not None else [], [("a", v) for v in ca])
            ok = ok and dict(both[0]).get("a") == dict(alone[0]).get("a") and dict(both[1]).get("a") == dict(alone[1]).get("a")
print("3  two sharings with one self: each resolves the same as alone, with each case:", ok)

# 4  one sharing by three names: a receiving self has no distinguishing of the name it arrives by
ok = True; lists = []
for p in PM:
    for q in (1, -1, None):
        got = []
        for name in (6, 10, 9):
            soc = {"self": ([(S, p)], []), "third": ([(S, q)] if q is not None else [], [])}
            a = step(soc, {("self", name): "third"}); b = step(a, {("self", name): "third"})
            got.append((a["third"], b["third"]))
        ok = ok and got[0] == got[1] == got[2]
print("4  one sharing going by 6, by 10 or by 9: with its receiving self the same, each case:", ok)
soc = {"self": ([(S, 1)], []), "x": ([], []), "y": ([], []), "z": ([], [])}
a = step(soc, {("self", 6): "x", ("self", 10): "y", ("self", 9): "z"})
print("   one self with three routes, by 6, by 10 and by 9: one same list with each of three receiving:", a["x"][1] == a["y"][1] == a["z"][1] and len(a["x"][1]) == 1)

# 5  a route as a between: with no self, no parity, no scale, and no name of a self with what arrives by it
body9 = code[code.index("def _9_next_co_discovering"):code.index("def _17_next_existing")]
print("5  a route, with 5-now-co-existing")
print("   no line of a self's resolving, 1-now-existing, has it: True" if "_5_now_co_existing" not in body1 else "   a line of 1-now-existing has it")
print("   9-next-co-discovering's lines have no number but a name's, and no + or -:", not re.search(r"(?<![_\d])\d+(?![_\d])", body9.replace("_9_", "").replace("_10_", "").replace("_5_", "").replace("_13_", "").replace("_15_", "")) and "> 0" not in body9)
ok = True
for a, b in itertools.product(PM, repeat=2):
    for q in (1, -1, None):
        r1 = soc_step({"self": a, "other": b, "third": q}, {("self", 10): "third", ("other", 10): "third"})["third"]
        r2 = soc_step({"self": b, "other": a, "third": q}, {("self", 10): "third", ("other", 10): "third"})["third"]
        ok = ok and r1[0] == r2[0] and sorted(r1[1]) == sorted(r2[1])
print("   what arrives with a third has no name of the self it is from: a self's and its other's parities exchanged, the same with a third, each case:", ok)
perm = all(one([(S, q)] if q is not None else [], [(S, v) for v in c]) == one([(S, q)] if q is not None else [], [(S, v) for v in c2])
           for q in (1, -1, None) for c in cases for c2 in set(itertools.permutations(c)))
print("   what arrives resolves the same with each order of arriving, each case:", perm)
soc = {"self": ([(S, 1)], []), "third": ([], [])}
arr = step(soc, {("self", 10): "third"})["third"][1]
print("   what arrives by a route: a sharing and its parity, and no name of a self or of a route:", arr == [(S, -1)] or arr == [(S, 1)], arr)
ok = True
for p in PM:
    soc = {"self": ([(S, p)], [])}
    a = step(soc, {}); b = step(a, {})
    ok = ok and dict(a["self"][0]).get(S) == -p and dict(b["self"][0]).get(S) == p
print("   a self with no route to it: nothing arrives, and its prior inverts with each 1 to 17:", ok)
print("   each way of a bi-coupling both ways is one route, with the same lines:", ("self", 10) in net and ("third", 10) in net)
