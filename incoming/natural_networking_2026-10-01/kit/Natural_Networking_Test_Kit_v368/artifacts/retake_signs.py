import sys; sys.path.insert(0,'.')
from signs import Self, a, society
def arr(ns): return [Self(n, a(p)) for n,p in zip(ns, (7,11,13,17,19,23)[:len(ns)])]
def readings(selves):
    return [(s.n, s.over_position(), s.parallels_ever_part(), s.a_middle_stands(), s.surplus_stands(), s.reaches_past_alone()) for s in selves]
cases = {"pair 7,9":[7,9], "pair 6,10":[6,10], "trio 7,9,11":[7,9,11], "trio 7,9,6":[7,9,6], "trio 6,10,14":[6,10,14]}
for crossing in ("address","sequencing","sign"):
    print("== crossing:", crossing)
    for label, ns in cases.items():
        selves = society(arr(ns), crossing=crossing)
        for n,o,p,m,su,r in readings(selves):
            print(f"  {label:12s} n={n:2d}: over {o}  part {p}  middle {m}  surplus {su}  reaches {r}")
