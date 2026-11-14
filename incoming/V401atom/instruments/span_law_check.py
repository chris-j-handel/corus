"""A span's number along a co-chaining, by its first self's sequence: each sequence and each case, all or none.

A first self's 1 to 17s are each one of two: bi-folding, all-parity its other; or do-no-harming, a parity is-same-as
its prior in its possibling. Its sequence is said again and again. Each sequence of its least number of 1 to 17s,
one to six, having a bi-folding; each case of the priors of the selves along.
A span is consecutive selves of one same prior in one same 1 to 17. A span-ending is two selves, the one and the next
along, their priors not the same.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/span_law_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"

def least(p):
    L = len(p)
    return not any(L % d == 0 and p == p[:d] * (L // d) for d in range(1, L))

def odd_runs(p):                      # the do-no-harmings one after one, an odd number of them, the sequence said again and again
    L = len(p)
    if "B" not in p:
        return None
    s = p.index("B"); q = p[s:] + p[:s]
    return sum(1 for v, g in itertools.groupby(q) if v == "D" and len(list(g)) % 2 == 1)

def rows(pattern, pri, N, T):
    names = list(range(N)); net = {(k, 9): k + 1 for k in range(N - 1)}
    soc = {k: ([(S, pri[k])], []) for k in names}; out = []
    for t in range(T):
        p0 = dict(soc[0][0])[S]
        soc[0] = (soc[0][0], [(S, p0)] if pattern[t % len(pattern)] == "D" else [])
        soc = step(soc, net)
        out.append([dict(soc[k][0])[S] for k in names])
    return out

allok = True; nseq = ncases = 0
for L in range(1, 7):
    N = L + 4
    okL = True; nL = 0
    for pat in itertools.product("BD", repeat=L):
        if not least(pat) or "B" not in pat:
            continue
        nseq += 1; nL += 1
        want = L - 2 * odd_runs(pat)
        for pri in itertools.product((1, -1), repeat=N):
            ncases += 1
            for r in rows(pat, pri, N, 3 * N + 3 * L + 12)[2 * N + 2 * L:]:
                ends = [1 if r[k] != r[k + 1] else 0 for k in range(N - 1)]
                okL = okL and all(sum(ends[w:w + L]) == want for w in range(1, N - 1 - L + 1))
    allok = allok and okL
    print("a sequence of", L, ": sequences", nL, "; the span-endings in each", L, "selves along are", L,
          "less two for each odd number of do-no-harmings one after one:", okL)
print("sequences:", nseq, "; cases, each sequence with each case of the priors:", ncases, "; each:", allok)
