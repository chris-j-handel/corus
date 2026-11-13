"""Along a co-chaining, each self with each 1 to 17: the same as the one before it, or its own prior inverted. Each case.

Four selves along, each with the one before it with 9, each with a prior + or -. With the first, a sequence of six
1 to 17s, each with nothing, + or - arriving. Each case of the priors and of the sequence, all or none.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/span_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"; N = 4
names = list(range(N)); net = {(k, 9): k + 1 for k in range(N - 1)}

ok1 = all(dict(one([(S, q)], [(S, m)])[1])[S] == m for q in (1, -1) for m in (1, -1))
ok2 = all(dict(one([(S, q)], arr)[1])[S] == -q for q in (1, -1) for arr in ([], [(S, 0)]))
print("1  a self with a parity arriving alone, each of four cases: its next prior is that parity, as it is:", ok1)
print("2  a self with nothing arriving, or a 0, each of four cases: its next prior is its prior inverted:", ok2)

n = 0; ok3 = ok4 = True; both = set()
for pri in itertools.product((1, -1), repeat=N):
    for seq in itertools.product((None, 1, -1), repeat=6):
        n += 1
        soc = {k: ([(S, pri[k])], []) for k in names}
        made_before = {}
        for t in range(len(seq) + N):
            x = seq[t] if t < len(seq) else None
            soc[0] = (soc[0][0], [] if x is None else [(S, x)])
            before = {k: dict(soc[k][0])[S] for k in names}
            arriving = {k: [v for _key, v in soc[k][1] if v != 0] for k in names}
            soc = step(soc, net)
            made = {k: dict(soc[k][0])[S] for k in names}
            for k in range(1, N):
                if arriving[k]:
                    ok3 = ok3 and made[k] == arriving[k][0] and made[k] == made_before.get(k - 1, made[k])
                    both.add("the same")
                else:
                    ok4 = ok4 and made[k] == -before[k]
                    both.add("inverted")
            made_before = made
print("cases, four selves along, each of sixteen cases of their priors, with each sequence of six, nothing, + or - arriving with the first:", n)
print("3  a self with a parity arriving from the one before it: its next prior is the next prior of the one before it,")
print("   made one 1 to 17 before, the same, with each case:", ok3)
print("4  a self with nothing arriving from the one before it, that one with nothing distinguished: its next prior is its prior inverted, with each case:", ok4)
print("5  with each self and each 1 to 17 it is one of the two, and no third:", sorted(both))

# 6: with one same 1 to 17, the spans along a co-chaining: consecutive selves with one same prior.
# A first self with each 1 to 17 one of two: nothing arriving, its prior inverting ("along"); or a parity the same
# as its prior arriving, co-parity, nothing distinguished ("across"). Eight selves along, each of 256 cases of their priors.
N2 = 8; names2 = list(range(N2)); net2 = {(k, 9): k + 1 for k in range(N2 - 1)}
def spans_inside(row):
    runs = [len(list(g)) for _v, g in itertools.groupby(row)]
    return runs[1:-1] if len(runs) > 2 else None        # the spans with both ends inside the eight
def along_rows(pattern, pri, T):
    soc = {k: ([(S, pri[k])], []) for k in names2}; rows = []
    for t in range(T):
        p0 = dict(soc[0][0])[S]
        soc[0] = (soc[0][0], [(S, p0)] if pattern[t % len(pattern)] == "across" else [])
        soc = step(soc, net2)
        rows.append([dict(soc[k][0])[S] for k in names2])
    return rows
readings = (
    (("along",), lambda r: all(n == 1 for n in spans_inside(r))),
    (("along", "across"), lambda r: len(set(r)) == 1),
    (("along", "along", "across"), lambda r: all(n == 3 for n in spans_inside(r) or [3])),
    (("along", "along", "along", "across"), lambda r: all(n == 2 for n in spans_inside(r))),
)
print("6  with one same 1 to 17, the spans along eight selves, each of 256 cases of their priors, from a thirty-third 1 to 17:")
said = ("each span is one self, alternating", "one span, each self the same", "each span is three selves", "each span is two selves")
for (pattern, ok), words in zip(readings, said):
    good = all(ok(r) for pri in itertools.product((1, -1), repeat=N2) for r in along_rows(pattern, pri, 56)[32:])
    print("   a first self's 1 to 17s", ", ".join(pattern), "and again:", words, ":", good)
