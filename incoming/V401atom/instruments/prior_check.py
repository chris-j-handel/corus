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
