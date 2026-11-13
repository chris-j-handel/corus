"""A bi-coupling's inception, executed with Exhibit ONE's code, no line changed.

A check of a reading: a self with no prior has an arriving parity as it arrives, once; and a prior, once with a self, is with it after.
Run: python3 incoming/V401atom/instruments/inception_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools, random
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"
say = lambda v: "." if v is None else "+" if v > 0 else "-" if v < 0 else "0"

print("one self, by 1-now-existing alone, a prior and an arriving each + or - or none:")
for prior, arriving in itertools.product((None, 1, -1), repeat=2):
    out, kept = one([(S, prior)] if prior else [], [(S, arriving)] if arriving else [])
    print(f"  prior {say(prior)}  arriving {say(arriving)}  ->  going out {say(dict(out).get(S))}  its next prior {say(dict(kept).get(S))}")

def run(n_selves, net, opening, T):
    soc = {k: (list(opening.get(k, [])), []) for k in range(n_selves)}
    pri = {k: [] for k in soc}; out = {k: [] for k in soc}
    for t in range(T):
        for k in soc:
            ten, _ = one(soc[k][0], soc[k][1])
            pri[k].append(say(dict(soc[k][0]).get(S))); out[k].append(say(dict(ten).get(S)))
        nxt = step(soc, net)
        soc = {k: (nxt[k][0], [(S, v) for (_key, v) in nxt[k][1]]) for k in nxt}
    return pri, out

print("a bi-coupling of two selves, each sharing across with 10 to its other; a prior + with self 1 only:")
pri, out = run(2, {(0, 10): 1, (1, 10): 0}, {0: [(S, 1)]}, 14)
for k in (0, 1): print(f"  self {k+1}: its prior {''.join(pri[k])}   its going out {''.join(out[k])}")
print("a bi-coupling of two selves, a prior + with each:")
pri, out = run(2, {(0, 10): 1, (1, 10): 0}, {0: [(S, 1)], 1: [(S, 1)]}, 14)
for k in (0, 1): print(f"  self {k+1}: its prior {''.join(pri[k])}   its going out {''.join(out[k])}")
print("a bi-coupling of two selves, a prior + with one and - with its other:")
pri, out = run(2, {(0, 10): 1, (1, 10): 0}, {0: [(S, 1)], 1: [(S, -1)]}, 14)
for k in (0, 1): print(f"  self {k+1}: its prior {''.join(pri[k])}   its going out {''.join(out[k])}")

random.seed(17)
never = True
for trial in range(400):
    n = random.randint(2, 7)
    net = {}
    for k in range(n):
        for name in (6, 9, 10):
            if random.random() < 0.6: net[(k, name)] = random.randrange(n)
    soc = {k: ([(S, random.choice((1, -1)))] if random.random() < 0.5 else [], []) for k in range(n)}
    had = {k: bool(soc[k][0]) for k in soc}
    for t in range(60):
        nxt = step(soc, net)
        soc = {k: (nxt[k][0], [(S, v) for (_key, v) in nxt[k][1]]) for k in nxt}
        for k in soc:
            if had[k] and not soc[k][0]: never = False
            had[k] = had[k] or bool(soc[k][0])
print("400 societies of 2 to 7 selves, couplings by lot, 60 momentaries each: a self with a prior is with a prior after, each:", never)
