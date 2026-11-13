"""A thing with a prior and with its next prior: each case, all or none. No opening by chance, and no case left out.

A self with two things, each with a prior + or -, and what is arriving with each of the two and with a third thing,
each nothing, +, - or 0. Each thing is with its 4-now-co-same-existing, the one name with a prior and with what is
arriving. And 8-now-same-existing, what its lines are making it with, read from the code's own text.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/same_existing_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one = ns["_1_now_existing"]

n = 0; ok1 = ok2 = ok3 = True
for p1, p2 in itertools.product((1, -1), repeat=2):
    for a1, a2, a3 in itertools.product((None, 1, -1, 0), repeat=3):
        n += 1
        prior = [("k1", p1), ("k2", p2)]
        arriving = [(k, v) for k, v in (("k1", a1), ("k2", a2), ("k3", a3)) if v is not None]
        nxt = dict(one(prior, arriving)[1])
        ok1 = ok1 and "k1" in nxt and "k2" in nxt
        ok2 = ok2 and nxt["k1"] in (p1, -p1) and nxt["k2"] in (p2, -p2)
        ok3 = ok3 and (("k3" in nxt) == (a3 in (1, -1))) and (a3 not in (1, -1) or nxt["k3"] == a3)
print("cases, two things each with a prior + or -, and nothing, +, - or 0 arriving with each and with a third thing:", n)
print("1  each thing with a prior is with a next prior, each case: no line is ending a thing with a prior:", ok1)
print("2  its next prior is its prior the same or its prior inverted: the thing the same, with prior and with now:", ok2)
print("3  a third thing is with a next prior with a parity arriving with it, that parity as it is, and with no other case:", ok3)
body17 = code[code.index("def _17_next_existing"):]
print("4  8-now-same-existing is what 1-now-existing is returning as each self's next prior, a now name with each prior:",
      "_10_next_co_possibling, _8_now_same_existing[_13_next_discovering] = (" in body17
      and "_8_now_same_existing[_13_next_discovering]," in body17)
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([\w-]+) \|", src, re.M)
print("5  the names with same-existing:", [name for _n, name, root in rows if root == "same-existing"])
print("   the names with discovering:", [name for _n, name, root in rows if root == "discovering"], "; each with next:",
      all(name.split("-")[1] == "next" for _n, name, root in rows if root == "discovering"))
