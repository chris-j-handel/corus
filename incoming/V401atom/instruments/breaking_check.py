"""A co-chaining of eight selves along, and its breaking with one between of two: each case, all or none. No opening by chance.

A first self's 1 to 17s are bi-folding, bi-folding and do-no-harming, and again: with all-parity its other twice, and
with co-parity once. Eight selves along, each with the one before it with 9. With a fortieth 1 to 17 one between of
two is given no more, each of the seven betweens in its case, with each of 256 cases of the selves' priors.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/breaking_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"; N = 8; names = list(range(N)); T = 80; T_BREAK = 40
whole = {(k, 9): k + 1 for k in range(N - 1)}
pattern = ("bi-folding", "bi-folding", "do-no-harming")

def rows(pri, broken):
    soc = {k: ([(S, pri[k])], []) for k in names}; out = []
    for t in range(T):
        net = dict(whole)
        if broken is not None and t >= T_BREAK:
            del net[(broken, 9)]
        p0 = dict(soc[0][0])[S]
        soc[0] = (soc[0][0], [(S, p0)] if pattern[t % 3] == "do-no-harming" else [])
        soc = step(soc, net)
        out.append([dict(soc[k][0])[S] for k in names])
    return out

n = 0; ok1 = ok2 = ok3 = ok4 = True
for pri in itertools.product((1, -1), repeat=N):
    base = rows(pri, None)
    for r in base[2 * N + 8:]:
        runs = [len(list(g)) for _v, g in itertools.groupby(r)][1:-1]
        ok4 = ok4 and all(x == 3 for x in runs)
    for b in range(N - 1):
        n += 1
        got = rows(pri, b)
        ok1 = ok1 and all(len(r) == N and all(v in (1, -1) for v in r) for r in got)
        ok2 = ok2 and all(got[t][:b + 1] == base[t][:b + 1] for t in range(T))
        ok3 = ok3 and all(got[t][k] == -got[t][k - 1] for t in range(T_BREAK + 2 * N, T) for k in range(b + 2, N)) \
                  and all(got[t][b + 1] == -got[t - 1][b + 1] for t in range(T_BREAK + 2, T))
print("cases, each of 256 cases of the priors with each of seven betweens:", n)
print("0  with no breaking, each span along is three selves, from a twenty-fifth 1 to 17:", ok4)
print("1  with a breaking, each of eight selves is with its prior, + or -, with each 1 to 17 after it: no line is ending a self:", ok1)
print("2  each self before the between is as with no breaking, with each 1 to 17:", ok2)
print("3  the self after the between is bi-folding with each 1 to 17, all-parity its other; and each self after it is with it:")
print("   each span along, after the between, is one self, and the spans of three are with it no more:", ok3)

# 4, 5: each self's prior with the fracture's 1 to 17, and the two selves, one each side of the fracture
ok4b = ok5 = True; same_n = notsame_n = 0
for pri in itertools.product((1, -1), repeat=N):
    base = rows(pri, None)
    for b in range(N - 1):
        got = rows(pri, b)
        ok4b = ok4b and all(got[t] == base[t] for t in range(T_BREAK + 1))
        a, c = got[T_BREAK][b], got[T_BREAK][b + 1]
        out, nxt = one([], [(S, a), (S, c)])
        inherited = dict(nxt).get(S)
        if a == c:
            same_n += 1; ok5 = ok5 and inherited == a
        else:
            notsame_n += 1; ok5 = ok5 and inherited is None
print("4  with the fracture's 1 to 17, each self's prior is as with no fracture: each co-chaining after it has its priors from the one before it, as they were:", ok4b)
print("5  the two selves, one each side of the fracture: is-same-as, inside a span, cases:", same_n, "; is-not-same-as, two spans meeting, cases:", notsame_n)
print("   the code's state of an empty prior with the two: a first prior inherited, that same parity, with is-same-as; nothing inherited with is-not-same-as:", ok5)
