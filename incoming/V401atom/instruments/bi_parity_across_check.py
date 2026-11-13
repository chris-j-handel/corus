"""Two selves of one bi-coupling, with bi-parity and with co-parity: what is with each changing of a self's prior.

A check of a reading: bi-parity as same-existing across, and co-parity as a self's own going on along.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/bi_parity_across_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"
say = lambda v: "." if v is None else "+" if v > 0 else "-" if v < 0 else "0"
net = {("self", 10): "other", ("other", 10): "self"}

def run(a, b, T=24):
    soc = {"self": ([(S, a)], []), "other": ([(S, b)], [])}
    rows = []
    for t in range(T):
        prior = {k: dict(soc[k][0]).get(S) for k in soc}
        arriving = {k: [v for _k, v in soc[k][1]] for k in soc}
        out = {k: dict(one(soc[k][0], soc[k][1])[0]).get(S) for k in soc}
        nxt = step(soc, net)
        soc = {k: (nxt[k][0], [(S, v) for (_key, v) in nxt[k][1]]) for k in nxt}
        after = {k: dict(soc[k][0]).get(S) for k in soc}
        rows.append((prior, arriving, out, after))
    return rows

for title, a, b in [("bi-parity, a self + and its other -", 1, -1), ("co-parity, a self + and its other +", 1, 1)]:
    rows = run(a, b)[2:]            # from a third momentary, each self with a parity or a 0 arriving
    print(title)
    for k in ("self", "other"):
        print(f"  {k:5}: its prior {''.join(say(r[0][k]) for r in rows[:12])}   arriving {''.join(say(r[1][k][0]) if r[1][k] else '.' for r in rows[:12])}   its going out {''.join(say(r[2][k]) for r in rows[:12])}")
    o = {"self": "other", "other": "self"}
    changing = [(r, k) for r in rows for k in ("self", "other") if r[3][k] != r[0][k]]
    staying = [(r, k) for r in rows for k in ("self", "other") if r[3][k] == r[0][k]]
    print("  momentaries of a self's prior changing:", len(changing), "; of its prior staying:", len(staying))
    print("    with each changing, a parity arriving across:", all(r[1][k] and r[1][k][0] != 0 for r, k in changing) if changing else None,
          "; with each changing, nothing or a 0 arriving:", all((not r[1][k]) or r[1][k][0] == 0 for r, k in changing) if changing else None)
    print("    with each changing, its next prior same-as what arrives:", all(r[1][k] and r[3][k] == r[1][k][0] for r, k in changing),
          "; same-as its other's prior:", all(r[3][k] == r[0][o[k]] for r, k in changing))
    print("    with each staying, a parity arriving same-as its prior:", all(r[1][k] and r[1][k][0] == r[0][k] for r, k in staying) if staying else None)
    print("    the two priors, with each momentary, same-as each other:", all(r[0]["self"] == r[0]["other"] for r in rows),
          "; one inversion apart:", all(r[0]["self"] == -r[0]["other"] for r in rows))
    print("    a 0 going out:", sum(1 for r in rows for k in o if r[2][k] == 0), "of", 2 * len(rows))
