"""next_me_parity_check · v401mgr · 14 Nov
Exhibit ONE's code, executed, no line of it changed.
What a self's me-parity is at its next moment, by what its others share to it.
Usage: python3 -I next_me_parity_check.py <Exhibit ONE's code, extracted>
"""
import sys, itertools
src = open(sys.argv[1]).read()
E = {}
exec(compile(src, "e1", "exec"), E)
one, seventeen = E["_1_now_existing"], E["_17_next_existing"]
s = lambda v: {1: "+", -1: "-", 0: "0", None: "."}[v]

print("PART 1 · one self, one 4, a prior; what its others share to it")
print("prior  others   14  12  next-prior   next same-as prior   next same-as each other's")
for p in (1, -1):
    for others in ((), (p,), (-p,), (p, -p), (-p, p), (p, p), (-p, -p), (p, p, -p)):
        ten, eleven = one([("k", p)], [("k", o) for o in others])
        v14 = None
        # 14 by the same lines
        d = {}
        for o in others:
            if o != 0:
                if "k" not in d: d["k"] = 1 if o > 0 else -1
                elif (d["k"] > 0) != (o > 0): d["k"] = 0
        v14 = d.get("k")
        v12 = dict(ten)["k"]; nxt = dict(eleven)["k"]
        print(f"  {s(p)}    {''.join(s(o) for o in others) or 'none':6}   {s(v14)}   {s(v12)}      {s(nxt)}          {'same-as' if nxt == p else 'not':8}          "
              + (" ".join('same-as' if nxt == o else 'not' for o in others) or "no other"))

def live(names, priors, five, moments, label):
    print(); print(label)
    sixteen = {n: ([("k", priors[n])], []) for n in names}
    print("moment  " + "  ".join(f"{n}: me 14 12" for n in names) + "   me-parities together")
    for m in range(1, moments + 1):
        row = []
        me = {}
        for n in names:
            three, two = sixteen[n]
            ten, eleven = one(three, two)
            me[n] = dict(three)["k"]
            d = {}
            for k, o in two:
                if o != 0:
                    if k not in d: d[k] = 1 if o > 0 else -1
                    elif (d[k] > 0) != (o > 0): d[k] = 0
            row.append(f"{n}: {s(me[n])}  {s(d.get('k'))}  {s(dict(ten)['k'])} ")
        vals = set(me.values())
        print(f"  {m:2}    " + "  ".join(row) + "   " + ("each same-as" if len(vals) == 1 else "not each same-as"))
        sixteen = seventeen(sixteen, five)

two_way = {("a", 6): "b", ("b", 6): "a"}
live("ab", {"a": 1, "b": 1}, two_way, 8, "PART 2a · two selves, across both ways, priors same-as")
live("ab", {"a": 1, "b": -1}, two_way, 8, "PART 2b · two selves, across both ways, priors not same-as")
ring = {("a", 9): "b", ("b", 9): "c", ("c", 9): "a"}
live("abc", {"a": 1, "b": 1, "c": 1}, ring, 8, "PART 3a · three selves along, one way, priors each same-as")
live("abc", {"a": 1, "b": 1, "c": -1}, ring, 14, "PART 3b · three selves along, one way, one prior not same-as")
star = {("a", 6): "c", ("b", 6): "c", ("c", 6): "a", ("c", 10): "b"}
live("abc", {"a": 1, "b": -1, "c": 1}, star, 10, "PART 4 · a self c by two others a and b, not same-as each other")

def long(names, priors, five, moments):
    sixteen = {n: ([("k", priors[n])], []) for n in names}
    seen = {}; same = []
    for m in range(1, moments + 1):
        me = tuple(dict(sixteen[n][0])["k"] for n in names)
        state = repr(sorted((n, sorted(sixteen[n][0]), sorted(sixteen[n][1])) for n in names))
        if len(set(me)) == 1: same.append(m)
        if state in seen: return seen[state], m - seen[state], same
        seen[state] = m
        sixteen = seventeen(sixteen, five)
    return None, None, same

print(); print("PART 5 · over many moments: the first moment of a form that is again, its moments, and each moment with each me-parity same-as")
for label, names, priors, five in (
    ("two, across both ways, same-as", "ab", {"a": 1, "b": 1}, two_way),
    ("two, across both ways, not same-as", "ab", {"a": 1, "b": -1}, two_way),
    ("three along, each same-as", "abc", {"a": 1, "b": 1, "c": 1}, ring),
    ("three along, one not same-as", "abc", {"a": 1, "b": 1, "c": -1}, ring),
    ("c by a and b, a and b not same-as", "abc", {"a": 1, "b": -1, "c": 1}, star),
    ("c by a and b, each same-as", "abc", {"a": 1, "b": 1, "c": 1}, star),
):
    first, span, same = long(names, priors, five, 400)
    print(f"  {label:38} again from moment {first}, each {span} moments; each same-as at {'each moment' if same and len(same) >= (first + span - 1) else (same or 'no moment')}")

print(); print("PART 6 · each case of two selves across both ways and of three along: a self's next by its prior, over 48 moments")
for label, names, priors, five in (
    ("two, same-as", "ab", {"a": 1, "b": 1}, two_way),
    ("two, not same-as", "ab", {"a": 1, "b": -1}, two_way),
    ("three along, one not same-as", "abc", {"a": 1, "b": 1, "c": -1}, ring),
    ("c by a and b, not same-as", "abc", {"a": 1, "b": -1, "c": 1}, star),
):
    sixteen = {n: ([("k", priors[n])], []) for n in names}
    seq = {n: "" for n in names}
    for m in range(48):
        nxt = seventeen(sixteen, five)
        for n in names:
            seq[n] += "s" if dict(nxt[n][0])["k"] == dict(sixteen[n][0])["k"] else "o"
        sixteen = nxt
    print(f"  {label}")
    for n in names: print(f"    {n}: {seq[n]}")
print("  s: its next prior same-as its prior, its co-possibling a 0.  o: its next prior the other one.")
