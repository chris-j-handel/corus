"""A co-chaining of six selves along, each observing the self before it: each case of their priors, all or none.

A check of a reading: a resolving's sequence through its moments as the sequence along a co-chaining, and a
co-chaining co-orienting, each self same-as the self before it.
A: a first self observing no other. B: a first self one of two with co-parity, bi-coupling both ways.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/co_chaining_along_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"; N = 6
names = list(range(N)); net = {(k, 9): k + 1 for k in range(N - 1)}

def run(pri, T, net, names):
    soc = {k: ([(S, pri[k])], []) for k in names}; h = []
    for t in range(T):
        h.append({k: dict(soc[k][0]).get(S) for k in names}); soc = step(soc, net)
    return h

print("one self observing one parity: its next prior is that parity, with a prior + or - and with the code's state:",
      all(dict(one([(S, p)] if p is not None else [], [(S, a)])[1]).get(S) == a for p in (1, -1, None) for a in (1, -1)))

T = 40; t0 = 2 * N
A1 = A2 = A3 = True
for pri in itertools.product((1, -1), repeat=N):
    h = run(dict(zip(names, pri)), T, net, names)
    A1 = A1 and all(h[t][k] == h[t - 1][k - 1] for t in range(t0, T) for k in range(1, N))
    A2 = A2 and all(h[t][k] == -h[t][k - 1] for t in range(t0, T) for k in range(1, N))
    A3 = A3 and all([h[t][k] for k in range(N - 1, -1, -1)] == [h[u][0] for u in range(t - N + 1, t + 1)] for t in range(t0 + N, T))
print("A  a first self observing no other, and five along after it, each case of the six priors, from a thirteenth 1 to 17:")
print("   each self's prior is the prior of the self before it, one 1 to 17 before:", A1)
print("   each self's prior is not same-as the prior of the self before it, with each 1 to 17:", A2)
print("   the priors along the six, from the last to the first, are the first self's priors through six 1 to 17s:", A3)

names2 = ["o"] + names; net2 = dict(net); net2[("o", 10)] = 0; net2[(0, 10)] = "o"
B1 = B2 = True
for p0 in (1, -1):
    for rest in itertools.product((1, -1), repeat=N - 1):
        pri = {"o": p0, 0: p0}; pri.update(dict(zip(range(1, N), rest)))
        h = run(pri, 60, net2, names2)
        B1 = B1 and all(h[t][k] == h[t][k - 1] for t in range(30, 60) for k in range(1, N))
        B2 = B2 and all(h[t][0] == h[t - 4][0] and h[t][0] != h[t - 2][0] for t in range(34, 60))
print("B  a first self one of two with co-parity, and five along after it, each case of their priors, from a thirty-first 1 to 17:")
print("   each self's prior is same-as the prior of the self before it, with each 1 to 17:", B1)
print("   each self's priors are the right spiral's, + - - +:", B2)
