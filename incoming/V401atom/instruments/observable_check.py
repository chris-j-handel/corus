"""Possibling and co-possibling, and which self is observing each: each line, each name and each case, all or none.

The four possibling names with the table's own column of one or co. What 1-now-existing is returning, read from
its own text. Each sharing an other is receiving, and each 14-next-possibling it is with, each case. And three selves,
two with one between and a third with none, each of eight cases of their priors.
Exhibit ONE's table and code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/observable_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([\w-]+) \| [^|]+\| (\w+) \|", src, re.M)
poss = [(int(n), name, col) for n, name, root, col in rows if root == "possibling"]
print("1  the possibling names, each with the table's column of one or co:", [(n, col) for n, _name, col in poss])
print("   2 and 14, possibling, are with one; 6 and 10, co-possibling, are with co:",
      [(n, col) for n, _name, col in poss] == [(2, "one"), (6, "co"), (10, "co"), (14, "one")]
      and all(("co-possibling" in name) == (col == "co") for _n, name, col in poss))

body1 = code[code.index("def _1_now_existing"):code.index("def _9_next_co_discovering")]
ret = re.search(r"return (.*)", body1).group(1)
print("2  1-now-existing is returning:", ret)
print("   10-next-co-possibling and a next prior are returned, and 14-next-possibling is returned with no line:",
      "_10_next_co_possibling" in ret and "_11_next_co_observing" in ret and "_14_" not in ret)

cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]
def fourteen(c):
    seen = {v for v in c if v != 0}
    return None if not seen else (seen.pop() if len(seen) == 1 else 0)
with_sharing = {}
for p in (1, -1):
    for c in cases:
        s = dict(one([(S, p)], [(S, v) for v in c])[0]).get(S)
        with_sharing.setdefault(s, set()).add(fourteen(c))
sign = lambda v: {1: "+", -1: "-", 0: "0", None: "nothing"}[v]
print("3  each sharing an other is receiving from a self with a prior, and each 14 it is with:")
for s in (1, -1, 0):
    print("     a sharing", sign(s), ": 14", sorted(sign(m) for m in with_sharing[s]))
print("   each sharing is with two 14s or more: with no sharing is a self's 14 one for its other:", all(len(v) >= 2 for v in with_sharing.values()))

ok_c = ok_b = True
for pa, pb, pc in itertools.product((1, -1), repeat=3):
    state = {"a": ([("a", pa)], []), "b": ([("b", pb)], []), "c": ([("c", pc)], [])}
    between = {("a", 10): "b", ("b", 10): "a"}
    for _ in range(8):
        shared = {k: [v for _key, v in one(list(pr), list(arr))[0]] for k, (pr, arr) in state.items()}
        state = step(state, between)
        ok_c = ok_c and state["c"][1] == []
        ok_b = ok_b and [v for _k, v in state["b"][1]] == shared["a"] and [v for _k, v in state["a"][1]] == shared["b"]
print("4  three selves, a and b with one between and c with none, each of eight cases of their priors, eight 1 to 17s:")
print("   a self's 10-next-co-possibling is arriving with its other, as it is, and with each 1 to 17:", ok_b)
print("   and nothing of it is arriving with the third, with each 1 to 17:", ok_c)
