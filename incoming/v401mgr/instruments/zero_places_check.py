"""zero_places_check · v401mgr · 14 Nov
Exhibit ONE's code, executed, no line of it changed.
One self, one 4, a prior, and each list of parities and 0s of its others, none to four:
which of its places is a 0, and what it has by its possibling a 0.
Usage: python3 -I zero_places_check.py <Exhibit ONE's code, extracted>
"""
import sys, itertools
E = {}
exec(compile(open(sys.argv[1]).read(), "e1", "exec"), E)
one = E["_1_now_existing"]
z8 = z12 = z14 = n = 0
as_none = True
for p in (1, -1):
    base = one([("k", p)], [])
    for k in range(0, 5):
        for others in itertools.product((1, -1, 0), repeat=k):
            ten, eleven = one([("k", p)], [("k", o) for o in others]); n += 1
            d = {}
            for o in others:
                if o != 0:
                    if "k" not in d: d["k"] = 1 if o > 0 else -1
                    elif (d["k"] > 0) != (o > 0): d["k"] = 0
            if d.get("k") == 0:
                z14 += 1
                as_none = as_none and (ten, eleven) == base
            if dict(ten)["k"] == 0: z12 += 1
            if dict(eleven)["k"] == 0: z8 += 1
print("cases:", n)
print("its possibling, 14, a 0:", z14)
print("its co-possibling, 12, a 0:", z12)
print("its next prior, its 8, a 0:", z8)
print("by its 14 a 0, each return same-as its return by none of its others:", as_none)
