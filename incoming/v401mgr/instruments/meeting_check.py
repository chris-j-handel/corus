"""meeting_check · v401mgr · 14 Nov
Exhibit ONE's code, executed, no line of it changed.
Two selves a and b, across both ways, and a self c having both as its others.
Usage: python3 -I meeting_check.py <Exhibit ONE's code, extracted>
"""
import sys
src = open(sys.argv[1]).read()
E = {}
exec(compile(src, "e1", "exec"), E)
one, seventeen = E["_1_now_existing"], E["_17_next_existing"]
s = lambda v: {1: "+", -1: "-", 0: "0", None: "."}[v]

def poss(two):
    d = {}
    for k, o in two:
        if o != 0:
            if k not in d: d[k] = 1 if o > 0 else -1
            elif (d[k] > 0) != (o > 0): d[k] = 0
    return d.get("k")

def live(names, priors, five, moments, label):
    print(); print(label)
    sixteen = {n: ([("k", priors[n])], []) for n in names}
    print("moment  " + "  ".join(f"{n}: prior possibling co-possibling next-prior" for n in names))
    rows = []
    for m in range(1, moments + 1):
        row = []
        for n in names:
            three, two = sixteen[n]
            ten, eleven = one(three, two)
            row.append((dict(three)["k"], poss(two), dict(ten)["k"], dict(eleven)["k"]))
        rows.append(row)
        print(f"  {m:2}    " + "  ".join(f"{n}:   {s(r[0])}       {s(r[1])}           {s(r[2])}           {s(r[3])}     " for n, r in zip(names, row)))
        sixteen = seventeen(sixteen, five)
    return rows

both = {("a", 6): "b", ("b", 6): "a", ("a", 10): "c", ("b", 10): "c"}
r = live("abc", {"a": 1, "b": -1, "c": 1}, both, 8, "PART 1 · a and b not same-as, across both ways; c by both, and neither by c")
print("  a's next prior same-as b's prior at each moment:", all(x[0][3] == x[1][0] for x in r), "· b's same-as a's:", all(x[1][3] == x[0][0] for x in r))
print("  a 0 in a place of a or of b:", any(0 in x[0] or 0 in x[1] for x in r), "· c's possibling a 0 from its second moment:", all(x[2][1] == 0 for x in r[1:]))
r = live("abc", {"a": 1, "b": -1, "c": -1}, both, 8, "PART 2 · the same, c's prior the other one")
r = live("abc", {"a": 1, "b": 1, "c": 1}, both, 8, "PART 3 · a and b same-as, across both ways; c by both")
print("  c's possibling a 0 at a moment:", any(x[2][1] == 0 for x in r))
back = dict(both); back.update({("c", 6): "a", ("c", 10): "b"})
r = live("abc", {"a": 1, "b": -1, "c": 1}, back, 14, "PART 4 · a and b not same-as, across both ways; c by both, and both by c")
print("  a 0 in a place of a or of b:", any(0 in x[0] or 0 in x[1] for x in r), "· c's possibling a 0 at each moment after its first:", all(x[2][1] == 0 for x in r[1:]))

print(); print("PART 5 · the order of a and b in 16-next-same-existing, each order: what 17-next-existing returns")
import itertools
ref = None; same = True
for order in itertools.permutations("abc"):
    sixteen = {n: ([("k", {"a": 1, "b": -1, "c": 1}[n])], []) for n in order}
    for m in range(6): sixteen = seventeen(sixteen, both)
    got = {n: (sorted(sixteen[n][0]), sorted(sixteen[n][1])) for n in "abc"}
    if ref is None: ref = got
    same = same and got == ref
print("  each of six orders, by six moments, one same return:", same)
