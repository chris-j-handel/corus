"""A third self with no prior, with both selves of one bi-coupling sharing along to it. Executed with Exhibit ONE's code, no line changed.

A check of a reading: a new self inheriting the prior me-parities of a self and an other.
Two selves share across with 10, each to its other, and each along with 9 to a third self with no prior.
Run: python3 incoming/V401atom/instruments/inheriting_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"
say = lambda v: "." if v is None else "+" if v > 0 else "-" if v < 0 else "0"

def run(net, opening, T, names):
    soc = {k: (list(opening.get(k, [])), []) for k in names}
    pri = {k: [] for k in soc}; out = {k: [] for k in soc}; arr = {k: [] for k in soc}
    for t in range(T):
        for k in soc:
            ten, _ = one(soc[k][0], soc[k][1])
            pri[k].append(say(dict(soc[k][0]).get(S))); out[k].append(say(dict(ten).get(S)))
            arr[k].append("".join(say(v) for _k, v in soc[k][1]) or ".")
        nxt = step(soc, net)
        soc = {k: (nxt[k][0], [(S, v) for (_key, v) in nxt[k][1]]) for k in nxt}
    return pri, out, arr

net = {("self", 10): "other", ("other", 10): "self", ("self", 9): "new", ("other", 9): "new"}
for title, op in [("two alike, + and +", {"self": [(S, 1)], "other": [(S, 1)]}),
                  ("two opposite, + and -", {"self": [(S, 1)], "other": [(S, -1)]}),
                  ("a prior with one only, +", {"self": [(S, 1)]})]:
    pri, out, arr = run(net, op, 16, ["self", "other", "new"])
    print(title)
    for k in ("self", "other", "new"):
        print(f"  {k:5}: its prior {''.join(pri[k])}   its going out {''.join(out[k])}")
    print("  arriving with new:", " ".join(arr["new"]))
print("what one call returns has an entry with each self and none with a coupling:",
      sorted(step({"self": ([(S, 1)], []), "other": ([(S, 1)], [])}, {("self", 10): "other", ("other", 10): "self"}).keys()))
