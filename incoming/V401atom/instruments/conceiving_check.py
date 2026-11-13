"""The code's own state of an empty prior with each sharing, no self, with both selves of one bi-coupling sharing along
to it, with more sharings than one. A new self has inherited priors: what is inherited here is each co-parity of its two.

A check of a reading: a new self's birthing is its inheriting, with co-parity, and a me-parity's conceiving is with
bi-parity, its 0 a new corus; two things, each with its own name.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/conceiving_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
say = lambda v: "." if v is None else "+" if v > 0 else "-" if v < 0 else "0"

def run(net_of, opening, T, names, sharings):
    soc = {k: (list(opening.get(k, [])), []) for k in names}
    pri = {k: {s: [] for s in sharings} for k in names}
    out = {k: {s: [] for s in sharings} for k in names}
    for t in range(T):
        for k in names:
            ten, _ = one(soc[k][0], soc[k][1])
            for s in sharings:
                pri[k][s].append(say(dict(soc[k][0]).get(s))); out[k][s].append(say(dict(ten).get(s)))
        soc = step(soc, net_of(t))
    return pri, out

both = {("self", 10): "other", ("other", 10): "self", ("self", 9): "new", ("other", 9): "new"}
names = ["self", "other", "new"]

print("1  four sharings with one bi-coupling: two with co-parity, a and b, and two with bi-parity, c and d")
op = {"self": [("a", 1), ("b", -1), ("c", 1), ("d", -1)], "other": [("a", 1), ("b", -1), ("c", -1), ("d", 1)]}
pri, out = run(lambda t: both, op, 16, names, "abcd")
for s in "abcd":
    print(f"  sharing {s}: self {pri['self'][s][0]} other {pri['other'][s][0]}   new, its prior {''.join(pri['new'][s])}   its going out {''.join(out['new'][s])}")
co = all(set(pri["new"][s][3:]) <= {"+", "-"} for s in "ab"); bi = all(set(pri["new"][s]) == {"."} for s in "cd")
print("  with each co-parity of its two, a prior is inherited, from a third 1 to 17:", co)
print("  with each bi-parity of its two, nothing is inherited with each 1 to 17, and a 0 going out:", bi and all(set(out["new"][s][1:]) == {"0"} for s in "cd"))
print("  the prior inherited with a, with each 1 to 17 from a third, same-as each of the two:",
      all(pri["new"]["a"][t] == pri["self"]["a"][t] == pri["other"]["a"][t] for t in range(3, 16)))

print("2  one sharing with bi-parity, and a new self's 0 going back to each of the two")
back = dict(both); back[("new", 10)] = "self"; back[("new", 9)] = "other"
op = {"self": [("c", 1)], "other": [("c", -1)]}
p1, o1 = run(lambda t: both, op, 16, names, "c"); p2, o2 = run(lambda t: back, op, 16, names, "c")
print("  each of the two, its prior and its going out, the same with a new self's 0 going back and with none:",
      all(p1[k]["c"] == p2[k]["c"] and o1[k]["c"] == o2[k]["c"] for k in ("self", "other")))

print("3  one sharing with bi-parity, and from a ninth 1 to 17 one of the two sharing with a new self no more")
one_only = {k: v for k, v in both.items() if k != ("other", 9)}
pri, out = run(lambda t: both if t < 8 else one_only, op, 16, names, "c")
for k in names:
    print(f"  {k:5}: its prior {''.join(pri[k]['c'])}   its going out {''.join(out[k]['c'])}")
first = next(t for t in range(16) if pri["new"]["c"][t] != ".")
print("  a new self's first prior is with a 1 to 17, of sixteen its number", first + 1, "; same-as the going out of the one still sharing, two 1 to 17s before:",
      pri["new"]["c"][first] == out["self"]["c"][first - 2])
inv = {"+": "-", "-": "+"}
print("  from it, with each 1 to 17, a new self's prior one inversion apart from the prior of the one still sharing:",
      all(pri["new"]["c"][t] == inv[pri["self"]["c"][t]] for t in range(first, 16)),
      "; same-as the prior of the one sharing no more:", all(pri["new"]["c"][t] == pri["other"]["c"][t] for t in range(first, 16)))

print("4  one sharing with bi-parity, and from a ninth 1 to 17 both of the two sharing with a new self no more")
none = {k: v for k, v in both.items() if k[1] != 9}
pri, out = run(lambda t: both if t < 8 else none, op, 16, names, "c")
print(f"  new  : its prior {''.join(pri['new']['c'])}   its going out {''.join(out['new']['c'])}")
