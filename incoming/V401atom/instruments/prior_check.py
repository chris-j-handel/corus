"""A prior with the code's lines: each case, all or none. No opening by chance, and no case left out.

A self with a prior, + or -, and the code's state of an empty prior, with none, one, two or three parities arriving,
each +, - or 0. What the lines are doing with a prior, with a sharing and with a next prior, each case.
And each line with 7-now-observing, the name with tri-bi-co, read from the code's own text.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/prior_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools, copy
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one = ns["_1_now_existing"]
S = "s"
cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]
allc = [(p, c) for p in (1, -1, None) for c in cases]
print("cases, a prior + or - or the code's state of an empty prior, with none to three arriving, each +, - or 0:", len(allc))

ok1 = ok2 = ok3 = ok4 = True
for p, c in allc:
    prior = [(S, p)] if p is not None else []
    arriving = [(S, v) for v in c]
    b1, b2 = copy.deepcopy(prior), copy.deepcopy(arriving)
    out, nxt = one(prior, arriving)
    s, n = dict(out).get(S), dict(nxt).get(S)
    ok1 = ok1 and prior == b1 and arriving == b2
    if s not in (0, None):
        ok2 = ok2 and s == n
    if p is not None:
        ok3 = ok3 and n in (p, -p) and ((n == p) == (s == 0))
        if not any(c):
            ok4 = ok4 and n == -p
print("1  with each case a prior is the same with the first line and with the last, and no line is changing it;")
print("   and each parity arriving is the same with the first line and with the last:", ok1)
print("2  with each case, a sharing not a 0 is the sharing one's next prior, as it is:", ok2)
print("3  a self's next prior is its prior the same, its sharing a 0, or its prior inverted, its sharing that next prior:", ok3)
print("4  a self with its prior and nothing arriving, each case: its next prior is its prior inverted:", ok4)

loops = re.findall(r"for _4_now_co_same_existing, _7_now_observing in (\w+):", code)
print("5  each line binding 7-now-observing, tri-bi-co, is over:", loops)
print("   a parity with 7 is an other's arriving with 2, a self's prior with 3, or a sharing going into a next prior with 10, and no other:",
      loops == ["_2_now_possibling", "_3_now_co_observing", "_10_next_co_possibling"])
assigned = set(re.findall(r"^\s*(_\d+_\w+?)(?:\[[^\]]*\])? = ", code, re.M)) | set(re.findall(r"for (_\d+_\w+)", code))
params = re.findall(r"def _17_next_existing\(([^)]*)\)", code)[0].split(", ")
print("6  given with 17-next-existing, and assigned by no line:", [x for x in params if x not in assigned])

# the code's functions, each name with its three from Exhibit ONE's table; and each prior after a first 1 to 17
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| [^|]+\| [^|]+\| [^|]+\| ([a-z-]+) \|", src, re.M)
three = {int(n): t for n, _name, t in rows}
defs = [int(n) for n in re.findall(r"^def _(\d+)_", code, re.M)]
print("7  the code's functions are the names", defs, "each with", sorted({three[n] for n in defs}),
      "; and each name with co-bi-tri is a function, and no other name is:", defs == [n for n in sorted(three) if three[n] == "co-bi-tri"])
print("8  each name with tri-bi-co:", [n for n in sorted(three) if three[n] == "tri-bi-co"], "; none of them a function:",
      not any(three[n] == "tri-bi-co" for n in defs))
a, b = "co-bi-tri".split("-"), "tri-bi-co".split("-")
print("9  co-bi-tri and tri-bi-co: the two ends exchanging, co and tri, and the middle the same, bi:", a[0] == b[2] and a[2] == b[0] and a[1] == b[1] == "bi")
step = ns["_17_next_existing"]
ok10 = True
for pa in (1, -1):
    for pb in (1, -1):
        state = {"a": ([("a", pa)], []), "b": ([("b", pb)], [])}
        between = {("a", 10): "b", ("b", 10): "a"}
        for _ in range(8):
            made = {k: one(*copy.deepcopy(v))[1] for k, v in state.items()}
            state = step(state, between)
            ok10 = ok10 and all(state[k][0] == made[k] for k in state)
print("10 two selves with one between, each of four cases of their priors, eight 1 to 17s: each prior after the first 1 to 17")
print("   is the next prior the lines made with the 1 to 17 before it; with the first, each prior is given, and by no line:", ok10)
