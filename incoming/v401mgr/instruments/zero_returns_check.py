"""zero_returns_check · v401mgr · 14 Nov
Exhibit ONE's code, executed, no line of it changed.
One self, one 4, a prior, and each list of parities and 0s of its others, none to four:
is a 0 by two parting, or by none of its others, in what 1-now-existing returns; and by what a returned 0 is.
Usage: python3 -I zero_returns_check.py <Exhibit ONE's code, extracted>
"""
import sys, itertools
E = {}
exec(compile(open(sys.argv[1]).read(), "e1", "exec"), E)
one = E["_1_now_existing"]
n = parting = parting_returned = none = none_returned = ret0 = ret0_same = 0
for p in (1, -1):
    for k in range(0, 5):
        for others in itertools.product((1, -1, 0), repeat=k):
            ten, eleven = one([("k", p)], [("k", o) for o in others]); n += 1
            live = [o for o in others if o != 0]
            v10, v11 = dict(ten)["k"], dict(eleven)["k"]
            if live and len(set(live)) == 2:
                parting += 1
                parting_returned += (v10 == 0 or v11 == 0)
            if not live:
                none += 1
                none_returned += (v10 == 0 or v11 == 0)
            if v10 == 0:
                ret0 += 1
                ret0_same += (bool(live) and set(live) == {p})
print("cases:", n)
print("its others parting, its 15 a 0:", parting, "· a 0 in what 1 returns, its 10 or its 11:", parting_returned)
print("none of its others, its 15 a 0 by the line's own:", none, "· a 0 in what 1 returns:", none_returned)
print("a 0 in its 10, returned:", ret0, "· of them, each parity of its others same-as its prior:", ret0_same)
