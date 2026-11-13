"""A me-parity living with nothing arriving, a co-chaining of six along from it, and its last sharing: each case, all or none.

A  a self with a prior, + or -, and nothing arriving: two cases, and from the two each 1 to 17.
B  six selves along, each observing the self before it with 9, the first observing no other: each of 64 cases of their priors.
C  the last self's sharing along, with no between given with it: each of 64 cases.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/exhausting_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"; N = 6
names = list(range(N)); net = {(k, 9): k + 1 for k in range(N - 1)}

okA = True
for p in (1, -1):
    out, nxt = one([(S, p)], [])
    okA = okA and dict(nxt)[S] == -p and dict(out)[S] == -p
print("A  a self with a prior and nothing arriving, each of two cases: its next prior is its prior inverted, and its sharing is its next prior;")
print("   from the two, with each 1 to 17 it is alternating and sharing, and no line is ending it:", okA)

T = 40; t0 = 2 * N
B1 = B2 = C1 = C2 = C3 = True
for pri in itertools.product((1, -1), repeat=N):
    soc = {k: ([(S, pri[k])], []) for k in names}; h = []
    for t in range(T):
        h.append({k: dict(soc[k][0])[S] for k in names})
        shared = {k: [v for _key, v in one(list(soc[k][0]), list(soc[k][1]))[0]] for k in names}
        soc = step(soc, net)
        arriving = {k: [v for _key, v in soc[k][1]] for k in names}
        C1 = C1 and arriving[0] == [] and all(arriving[k] == shared[k - 1] for k in range(1, N))
        C2 = C2 and sum(len(arriving[k]) for k in names) == sum(len(shared[k]) for k in range(N - 1))
        if t >= t0:
            C3 = C3 and shared[N - 1] == [-h[t][N - 1]]
    B1 = B1 and all(h[t][k] == h[t - 1][k - 1] for t in range(t0, T) for k in range(1, N))
    B2 = B2 and all([h[t][k] for k in range(N - 1, -1, -1)] == [h[u][0] for u in range(t - N + 1, t + 1)] for t in range(t0 + N, T))
print("B  six selves along, the first with nothing arriving, each of 64 cases of their priors, from a thirteenth 1 to 17:")
print("   each self's prior is the prior of the self before it, one 1 to 17 before:", B1)
print("   the priors along the six, from the last to the first, are the first self's priors through six 1 to 17s:", B2)
print("C  the last self's sharing along, each of 64 cases:")
print("   each self's sharing is arriving with the self after it, as it is, and nothing is arriving with the first:", C1)
print("   the last self's sharing is arriving with no self: each thing arriving is a sharing of the five before it:", C2)
print("   from a thirteenth 1 to 17 the last self's sharing is a parity with each 1 to 17, its next prior, and a 0 with none:", C3)

# D, E: a distinguishing and none, each case; and no distinguishing going on, with a stable form and with a living other
cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]
rule = lambda p, c: any(v != 0 for v in c) and all(v == p for v in c if v != 0)
okD = True
for p in (1, -1):
    for c in cases:
        out, nxt = one([(S, p)], [(S, v) for v in c])
        s, n = dict(out)[S], dict(nxt)[S]
        okD = okD and ((s == 0 and n == p) if rule(p, c) else (s == -p and n == -p))
print("D  a self with a prior, + or -, and none to three arriving, each +, - or 0,", 2 * len(cases), "cases:")
print("   nothing is distinguished with one case only, a parity or more arriving and each the same as its prior: its sharing a 0, its next prior its prior;")
print("   with each other case, and with nothing arriving, its prior is inverting and its sharing is its next prior:", okD)
okE1 = True
for p, f in itertools.product((1, -1), repeat=2):
    prior = p; shares = []
    for t in range(16):
        out, nxt = one([(S, prior)], [(S, f)]); shares.append(dict(out)[S]); prior = dict(nxt)[S]
    okE1 = okE1 and all(v == 0 for v in shares[1:]) and prior == f
print("E  a self observing a stable form alone, each of four cases: from its next 1 to 17, its sharing is a 0 with each, nothing distinguished:", okE1)
okE2 = True
for pa, pb in itertools.product((1, -1), repeat=2):
    soc = {"a": ([(S, pa)], []), "b": ([(S, pb)], [])}; net2 = {("a", 10): "b", ("b", 10): "a"}; sh = {"a": [], "b": []}
    for t in range(32):
        for k in soc:
            sh[k].append(dict(one(list(soc[k][0]), list(soc[k][1]))[0])[S])
        soc = step(soc, net2)
    okE2 = okE2 and all(not (sh[k][t] == 0 and sh[k][t + 1] == 0) for k in sh for t in range(31))
print("   two living selves with one between, each of four cases of their priors: with each a sharing a 0 is with a sharing a parity after it;")
print("   with no two 1 to 17s together is nothing distinguished:", okE2)
