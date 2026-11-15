"""v402code · each code table of Exhibit ONE Natural Resolver, executed against the
code taken word for word from the living file. Deciding nothing; reporting same / not same.
Run, from outside the set's folder, R the set's folder: python3 -I tables_check.py R
"""
import importlib.util, sys, os
from math import gcd

import re, glob
R = sys.argv[1] if len(sys.argv) > 1 else "."
_living = sorted(glob.glob(os.path.join(R, "Exhibit_ONE_Natural_Resolver_v*.md")))[-1]
_code = re.search(r"```python\n(.*?)\n```", open(_living, encoding="utf-8").read(), re.S).group(1)
_ns = {}; exec(_code, _ns)
# the code's three functions by their order in the living file, and by no name
ONE, NINE, SEVENTEEN = [v for k, v in _ns.items() if callable(v) and not k.startswith("__")]

S = "s"                      # the one sharing
SYM = {1: "+", -1: "−", 0: "0", None: "·"}
def sym(v): return SYM[v]
def P(ch): return {"+": 1, "−": -1, "-": -1, "0": 0}[ch]

results = []
def report(name, same, detail=""):
    results.append((name, same))
    print(("SAME      " if same else "NOT SAME  ") + name + ((" :: " + detail) if detail else ""))

# ---------------------------------------------------------------- one self
def one(prior, incoming):
    """prior: None or ±1 ; incoming: list of parities for the one sharing.
    returns (sharing value or None if no sharing listed, next prior or None)"""
    pr = [] if prior is None else [(S, prior)]
    out, nxt = ONE(pr, [(S, v) for v in incoming])
    out = dict(out); nxt = dict(nxt)
    return out.get(S, None), nxt.get(S, None)

def surfacing(incoming):
    """14-next-possibling for one sharing with an empty prior: the 10 list equals 12 = 14."""
    out, _ = ONE([], [(S, v) for v in incoming])
    d = dict(out)
    return d.get(S, "empty")

# Parities to one sharing, surfacing
rows = [("", "empty"), ("0", "empty"), ("+", 1), ("−", -1), ("++", 1), ("−−", -1), ("+−", 0), ("−+", 0),
        ("++−", 0), ("−−+", 0), ("+−+", 0), ("0+", 1)]
bad = [(r, surfacing([P(c) for c in r])) for r, want in rows if surfacing([P(c) for c in r]) != want]
report("Parities to one sharing, surfacing (12 rows)", not bad, str(bad) if bad else "")

# One self, one momentary
cells = {(1, ""): (-1, -1), (1, "+"): (0, 1), (1, "−"): (-1, -1), (1, "+−"): (-1, -1),
         (-1, ""): (1, 1), (-1, "+"): (1, 1), (-1, "−"): (0, -1), (-1, "+−"): (1, 1)}
bad = [(k, one(k[0], [P(c) for c in k[1]])) for k, w in cells.items() if one(k[0], [P(c) for c in k[1]]) != w]
report("One self, one momentary (8 cells)", not bad, str(bad) if bad else "")

# + and − alike : every receiving of length <= 4 over {+,−,0}, with prior +, − and empty
from itertools import product
def neg(v): return None if v is None else -v
ok = True
for L in range(0, 5):
    for inc in product([1, -1, 0], repeat=L):
        for pr in (1, -1, None):
            a = one(pr, list(inc)); b = one(neg(pr), [-v for v in inc])
            if (neg(a[0]), neg(a[1])) != b: ok = False
report("+ and − alike (each receiving to four parities, each prior)", ok)

# One cell, four receivings
ok = all(one(p, inc) == (-p, -p) for p in (1, -1) for inc in ([-p], [1, -1], [-1, 1], [], [0]))
report("One cell, four receivings", ok)

# With an empty prior, one momentary
want = {"": (None, None), "+": (1, 1), "−": (-1, -1), "+−": (0, None)}
bad = [(k, one(None, [P(c) for c in k])) for k, w in want.items() if one(None, [P(c) for c in k]) != w]
report("With an empty prior, one momentary (4 cells)", not bad, str(bad) if bad else "")

# One self, momentary by momentary: three ways
def run_one(prior, feeds):
    sh, pr = [], []
    for inc in feeds:
        s, prior = one(prior, inc); sh.append(s); pr.append(prior)
    return "".join(sym(v) for v in sh), "".join(sym(v) for v in pr)
alt = "+−+−+−+−"
want = {"empty": ([[]] * 8, alt, alt), "−": ([[-1]] * 8, "0" * 8, "−" * 8), "+": ([[1]] * 8, "+0000000", "+" * 8),
        "+,− inverting": ([[1], [-1]] * 4, alt, alt), "+ and − together": ([[1, -1]] * 8, alt, alt)}
bad = [(k, run_one(-1, f)) for k, (f, a, b) in want.items() if run_one(-1, f) != (a, b)]
report("One self, momentary by momentary: three ways (5 rows)", not bad, str(bad) if bad else "")

# ---------------------------------------------------------------- societies
def step(soc, routes):
    """one momentary of a same-existing-society; also returns each self's 10 list
    (found by executing 1-now-existing on the same given, as 17-next-existing does)."""
    shared = {k: dict(ONE(pr, inc)[0]).get(S, None) for k, (pr, inc) in soc.items()}
    return SEVENTEEN(soc, routes), shared

def run(priors, routes, T, first_incoming=None):
    soc = {k: (([] if p is None else [(S, p)]), list((first_incoming or {}).get(k, []))) for k, p in priors.items()}
    shares, pri = [], []
    for _ in range(T):
        soc, sh = step(soc, routes)
        shares.append(sh)
        pri.append({k: dict(v[0]).get(S, None) for k, v in soc.items()})
    return shares, pri

def spiral(n, tag=""):
    selves = [(tag, i) for i in range(n)]
    priors = {k: (-1 if k[1] % 2 == 0 else 1) for k in selves}
    routes = {((tag, i), 9): (tag, (i + 1) % n) for i in range(n)}
    return priors, routes

def least_period(seq, start=0):
    """least p with seq[t+p]==seq[t] for all t>=start (within the run)"""
    n = len(seq)
    for p in range(1, (n - start) // 2 + 1):
        if all(seq[t] == seq[t + p] for t in range(start, n - p)): return p
    return None

def eventual(seq, maxp=None):
    """(first index from which seq is periodic, that least period); index 0-based"""
    n = len(seq)
    best = None
    for p in range(1, (maxp or n // 3) + 1):
        t = n - p - 1
        while t >= 0 and seq[t] == seq[t + p]: t -= 1
        start = t + 1
        if start < n - 2 * p:
            if best is None or start < best[0] or (start == best[0] and p < best[1]):
                best = (start, p)
            if best and best[0] == start and p == best[1]:
                pass
    # choose least period among those reaching the earliest start
    return best

# A spiral of selves, column a
a_rows = {1: "+0−0+0−0+0−0", 2: "+−+−+−+−+−+−", 3: "+0−+−+−0+−+−", 4: "+−+−+−+−+−+−", 5: "+0−+−+−+−+−0",
          6: "+−+−+−+−+−+−", 7: "+0−+−+−+−+−+", 8: "+−+−+−+−+−+−", 9: "+0−+−+−+−+−+", 10: "+−+−+−+−+−+−",
          11: "+0−+−+−+−+−+", 17: "+0−+−+−+−+−+", 59: "+0−+−+−+−+−+"}
bad = []
for n, want in a_rows.items():
    pr, ro = spiral(n); sh, _ = run(pr, ro, 12)
    got = "".join(sym(s[("", 0)]) for s in sh)
    if got != want: bad.append((n, got))
report("A spiral of selves, self 1's parities along, momentaries 1 to 12 (13 rows)", not bad, str(bad) if bad else "")

# column b, each number of selves 1 to 59
bad = []; anti_bad = []
spiral_period = {}
for n in range(1, 60):
    want = 4 * n if n % 2 else 2
    pr, ro = spiral(n); T = 3 * want + 8
    sh, pri = run(pr, ro, T)
    seq = [tuple(s[k] for k in sorted(s)) for s in sh]
    p = least_period(seq)
    spiral_period[n] = p
    if p != want: bad.append((n, p))
    if n % 2:
        if not all(tuple((None if v is None else -v) for v in seq[t]) == seq[t + 2 * n] for t in range(len(seq) - 2 * n)):
            anti_bad.append(n)
report("A spiral of selves, momentaries to parities along again, 1 to 59 selves", not bad, str(bad) if bad else "")
report("A spiral of selves, odd: with twice its number each parity inverting, each 0 a 0 again", not anti_bad, str(anti_bad))
for n in (60, 61, 62, 63):
    pr, ro = spiral(n); want = 4 * n if n % 2 else 2
    sh, _ = run(pr, ro, 3 * want + 8); spiral_period[n] = least_period([tuple(s[k] for k in sorted(s)) for s in sh])

# Two momentaries before, inverting : a spiral opening with a prior for each self
def check_two_before(n, priors):
    ro = {(("", i), 9): ("", (i + 1) % n) for i in range(n)}
    T = 40
    sh, pri = run(priors, ro, T)
    # prior held by self k entering momentary m (1-based): P[m][k]; P[1]=opening
    Pm = [dict(priors)] + pri
    ok1 = True
    for m in range(3, T + 1):                       # entering momentary m, index m-1
        for i in range(n):
            src = ("", (i - 1) % n)
            if Pm[m - 1][("", i)] != -Pm[m - 3][src]: ok1 = False
    ok2 = all(sh[0][k] in (1, -1) for k in priors)
    ok3 = True
    for k in priors:
        col = [s[k] for s in sh]
        for t in range(1, T - 1):
            if col[t] == 0 and not (col[t - 1] in (1, -1) and col[t + 1] in (1, -1)): ok3 = False
    return ok1, ok2, ok3
bad = []
import random
random.seed(402)
for n in range(1, 13):
    trials = [dict(spiral(n)[0])] + [{("", i): random.choice([1, -1]) for i in range(n)} for _ in range(40)]
    for pr in trials:
        r = check_two_before(n, pr)
        if not all(r): bad.append((n, r, "alternating" if pr == spiral(n)[0] else "".join(sym(pr[("", i)]) for i in range(n))))
report("Two momentaries before, inverting (spirals of 1 to 12, alternating opening and 40 openings by chance each)",
       not bad, str(bad[:6]) + (" ... %d in all" % len(bad) if len(bad) > 6 else ""))

# ---------------------------------------------------------------- two spirals
def lcm(a, b): return a * b // gcd(a, b)
def two_spirals(m, n, coupled):
    pa, ra = spiral(m, "A"); pb, rb = spiral(n, "B")
    pr = {**pa, **pb}; ro = {**ra, **rb}
    if coupled:
        ro[(("A", 0), 10)] = ("B", 0); ro[(("B", 0), 10)] = ("A", 0)
    return pr, ro

table2 = {(2, 3): (12, 2, 7), (3, 5): (60, 2, 12), (5, 7): (140, 2, 20), (7, 11): (308, 2, 28), (11, 13): (572, 2, 44),
          (13, 17): (884, 2, 52), (17, 59): (4012, 2, 119), (9, 15): (180, 2, 36)}
# a: beside each other, executed as one society, each two numbers 1 to 31
bad = []
for m in range(1, 32):
    for n in range(m, 32):
        want = lcm(spiral_period[m], spiral_period[n])
        if (m, n) in table2 and table2[(m, n)][0] != want: bad.append(("table", m, n, want))
        if want > 1300: continue      # executed below for the table's rows only
        pr, ro = two_spirals(m, n, False)
        sh, _ = run(pr, ro, 2 * want + 4)
        p = least_period([tuple(s[k] for k in sorted(s)) for s in sh])
        if p != want: bad.append((m, n, p, want))
pr, ro = two_spirals(17, 59, False); sh, _ = run(pr, ro, 2 * 4012 + 4)
p1759 = least_period([tuple(s[k] for k in sorted(s)) for s in sh])
if p1759 != 4012: bad.append((17, 59, p1759))
pr, ro = two_spirals(9, 25, False); sh, _ = run(pr, ro, 2 * 900 + 4)
p925 = least_period([tuple(s[k] for k in sorted(s)) for s in sh])
if p925 != 900: bad.append((9, 25, p925))
odd_coprime_bad = [(m, n) for m in range(1, 32, 2) for n in range(m + 2, 32, 2) if gcd(m, n) == 1 and lcm(spiral_period[m], spiral_period[n]) != 4 * m * n]
report("Two spirals beside each other, momentaries to parities along again together (1 to 31; 17·59; 9·25 with 900)",
       not bad and not odd_coprime_bad, str(bad[:8]) + str(odd_coprime_bad[:5]))

# b, c, d, e : bi-coupling across
def c_rule(m, n):
    lo, hi = min(m, n), max(m, n)
    if lo % 2 and hi % 2:
        if lo == hi: return None
        return 4 * lo if hi < 2 * lo else 2 * hi + 1
    if lo % 2 == 0 and hi % 2 == 0: return 1
    return 2 * (lo if lo % 2 else hi) + 1
bad_b, bad_c, bad_d, notes = [], [], [], []
d_kind = {}
equal_odd = {}
for m in range(2, 16):
    for n in range(m, 32):
        pr, ro = two_spirals(m, n, True)
        T = 2 * max(m, n) + 4 * min(m, n) + 60
        sh, pri = run(pr, ro, T)
        seq = [tuple(s[k] for k in sorted(s)) for s in sh]
        st, p = eventual(seq, maxp=40)
        want = c_rule(m, n)
        if want is None:
            equal_odd[m] = (st + 1, p)
            continue
        if p != 2: bad_b.append((m, n, p))
        if st + 1 != want: bad_c.append((m, n, st + 1, want))
        # d: self 1 of each, in the going form: opposite or like, by the kind of the two numbers
        opp = all(pri[t][("A", 0)] == -pri[t][("B", 0)] for t in range(st, T))
        like = all(pri[t][("A", 0)] == pri[t][("B", 0)] for t in range(st, T))
        d_kind.setdefault(("both even" if (m % 2 == 0 and n % 2 == 0) else "one or both odd, unequal"), set()).add("opposite" if opp else "like" if like else "neither")
        if (m, n) in table2 and not opp: bad_d.append((m, n))
report("Bi-coupling across: momentaries to parities along again, 2 (each two numbers 2 to 15, the larger to 31)", not bad_b, str(bad_b[:8]))
report("Bi-coupling across: again from this momentary on, by its three sayings (same range, both odd and equal aside)", not bad_c,
       str(bad_c[:10]) + (" ... %d in all" % len(bad_c) if len(bad_c) > 10 else ""))
report("Bi-coupling across: self 1 of each of opposite parity, each row of the table in this range", not bad_d, str(bad_d[:8]))
print("          across the whole range, self 1 of each in the going form:", {k: sorted(v) for k, v in d_kind.items()})
print("          both odd and equal, the living sentence saying nothing of it; found (from momentary, period):", equal_odd)
# 17 · 59 row
pr, ro = two_spirals(17, 59, True); sh, pri = run(pr, ro, 400)
st, p = eventual([tuple(s[k] for k in sorted(s)) for s in sh], maxp=40)
report("Bi-coupling across: row 17 · 59 (2, from 119, opposite)", (p, st + 1) == (2, 119) and all(pri[t][("A", 0)] == -pri[t][("B", 0)] for t in range(st, 400)), str((p, st + 1)))
# e: like pair of the first momentary
def like_pairs(n):
    pr, _ = spiral(n)
    return [(i + 1, (i + 1) % n + 1) for i in range(n) if n > 1 and pr[("", i)] == pr[("", (i + 1) % n)]]
ok = all(like_pairs(n) == ([] if n % 2 == 0 else [(n, 1)]) for n in range(2, 60))
report("Each spiral's like pair of the first momentary: even, an empty set; odd, the last and the first", ok)

# ---------------------------------------------------------------- torus
def torus(p, q):
    selves = [(i, j) for i in range(p) for j in range(q)]
    priors = {k: (-1 if (k[0] + k[1]) % 2 == 0 else 1) for k in selves}
    routes = {}
    for (i, j) in selves:
        routes[((i, j), 9)] = ((i + 1) % p, j)
        routes[((i, j), 10)] = (i, (j + 1) % q)
    return priors, routes
def torus_rule(p, q):
    if p % 2 and q % 2:
        if (p, q) == (1, 1): return 4, 1
        return (q, 3 * p - 1) if q > 2 * p else (4 * p, 3 * p - 3)
    return 2, 1
table3 = {(1, 3): (3, 2, 12), (2, 3): (2, 1, 12), (1, 5): (5, 2, 20), (3, 3): (12, 6, 12), (3, 5): (12, 6, 60), (3, 7): (7, 8, 84),
          (3, 13): (13, 8, 156), (5, 7): (20, 12, 140), (5, 11): (11, 14, 220), (7, 17): (17, 20, 476), (17, 59): (59, 50, 4012)}
bad_a, bad_b, bad_t, bad_form = [], [], [], []
def torus_check(p, q, T=None):
    pr, ro = torus(p, q)
    wa, wb = torus_rule(p, q)
    T = T or (wb + 4 * wa + 30)
    sh, pri = run(pr, ro, T)
    seq = [tuple(s[k] for k in sorted(s)) for s in sh]
    st, per = eventual(seq, maxp=max(4 * p, q) + 2)
    return (per, st + 1), (wa, wb), sh, pri, st
for p in range(1, 16):
    for q in range(p, 22):
        got, want, sh, pri, st = torus_check(p, q)
        if got[0] != want[0]: bad_a.append((p, q, got[0], want[0]))
        if got[1] != want[1]: bad_b.append((p, q, got[1], want[1]))
        if (p, q) in table3 and table3[(p, q)][:2] != got: bad_t.append((p, q, got))
        # two going forms, both odd, read on each self's next prior
        if p % 2 and q % 2 and (p, q) != (1, 1):
            T = len(pri)
            if q > 2 * p:
                ok = all(pri[t + 1][(i, (j + 1) % q)] == pri[t][(i, j)] for t in range(st, T - 1) for i in range(p) for j in range(q))
                okb = all(pri[t + 1][(i, (j - 1) % q)] == pri[t][(i, j)] for t in range(st, T - 1) for i in range(p) for j in range(q))
                if not (ok or okb): bad_form.append((p, q, "across"))
            else:
                ok = all(pri[t + 2][((i + 1) % p, j)] == -pri[t][(i, j)] for t in range(st, T - 2) for i in range(p) for j in range(q))
                okb = all(pri[t + 2][((i - 1) % p, j)] == -pri[t][(i, j)] for t in range(st, T - 2) for i in range(p) for j in range(q))
                if not (ok or okb): bad_form.append((p, q, "along"))
got, want, *_ = torus_check(17, 59, T=420)
if got != (59, 50): bad_t.append((17, 59, got))
c_bad = [(k, lcm(spiral_period[k[0]], spiral_period[k[1]])) for k, v in table3.items() if lcm(spiral_period[k[0]], spiral_period[k[1]]) != v[2]]
report("A torus of selves: momentaries to parities along and across again (p 1 to 15, q p to 21)", not bad_a, str(bad_a[:10]) + (" ... %d in all" % len(bad_a) if len(bad_a) > 10 else ""))
report("A torus of selves: again from this momentary on (same range)", not bad_b, str(bad_b[:10]) + (" ... %d in all" % len(bad_b) if len(bad_b) > 10 else ""))
report("A torus of selves: its eleven rows, a and b (17 · 59 executed)", not bad_t, str(bad_t))
report("A torus of selves: its eleven rows, c, spirals beside each other", not c_bad, str(c_bad))
report("A torus's two going forms (both odd, same range)", not bad_form, str(bad_form[:10]) + (" ... %d in all" % len(bad_form) if len(bad_form) > 10 else ""))

# ---------------------------------------------------------------- alike selves, a right spiral
def prior_col(priors, routes, who, T=8):
    _, pri = run(priors, routes, T)
    return sym(priors[who]) + "".join(sym(x[who]) for x in pri)
RS = "+−−++−−++"
rows = {
 "A spiral of one, along": ({0: 1}, {(0, 9): 0}),
 "Two selves, both ways along": ({0: 1, 1: 1}, {(0, 9): 1, (1, 9): 0}),
 "Two selves, both ways across": ({0: 1, 1: 1}, {(0, 10): 1, (1, 10): 0}),
 "A spiral of three": ({i: 1 for i in range(3)}, {(i, 9): (i + 1) % 3 for i in range(3)}),
 "A spiral of four": ({i: 1 for i in range(4)}, {(i, 9): (i + 1) % 4 for i in range(4)}),
 "A spiral of five": ({i: 1 for i in range(5)}, {(i, 9): (i + 1) % 5 for i in range(5)}),
}
bad = []
for name, (pr, ro) in rows.items():
    for who in pr:
        g = prior_col(pr, ro, who)
        if g != RS: bad.append((name, who, g))
for ro in ({(0, 9): 1, (1, 9): 0}, {(0, 10): 1, (1, 10): 0}):
    g = prior_col({0: 1, 1: -1}, ro, 0)
    if g != "+−+−+−+−+": bad.append(("one parity apart", g))
report("Alike selves, a right spiral (7 rows, each self)", not bad, str(bad))
# the step (x, y) -> (y, −x) for alike selves
ok = True
for name, (pr, ro) in rows.items():
    _, pri = run(pr, ro, 24)
    col = [pr[0]] + [x[0] for x in pri]
    for t in range(len(col) - 2):
        if (col[t + 1], col[t + 2]) != (col[t + 1], -col[t]): ok = False
report("Alike selves: each prior and its next, a pair (x, y), step to (y, −x)", ok)

# ---------------------------------------------------------------- two selves
def two(pa, pb, mode, key):
    ro = {}
    if mode in ("both", "A from B"): ro[("B", key)] = "A"
    if mode in ("both", "B from A"): ro[("A", key)] = "B"
    sh, _ = run({"A": pa, "B": pb}, ro, 6)
    return "".join(sym(s["A"]) for s in sh), "".join(sym(s["B"]) for s in sh)
want = {(1, 1, "both"): ("−0+0−0", "−0+0−0"), (1, 1, "A from B"): ("−0+−+−", "−+−+−+"), (1, 1, "B from A"): ("−+−+−+", "−0+−+−"),
        (1, 1, "apart"): ("−+−+−+", "−+−+−+"), (1, -1, "both"): ("−+−+−+", "+−+−+−"), (1, -1, "A from B"): ("−+−+−+", "+−+−+−"),
        (1, -1, "B from A"): ("−+−+−+", "+−+−+−"), (1, -1, "apart"): ("−+−+−+", "+−+−+−")}
bad = [(k, key, two(k[0], k[1], k[2], key)) for k, w in want.items() for key in (9, 10) if two(k[0], k[1], k[2], key) != w]
report("Two selves (8 rows, across and along)", not bad, str(bad))

# ---------------------------------------------------------------- two selves, three momentaries, five parities
forms = {(1, -1, -1, 0, -1), (1, -1, 1, -1, -1), (1, 0, 1, -1, -1), (-1, 1, 1, 0, 1), (-1, 1, -1, 1, 1), (-1, 0, -1, 1, 1)}
found = {}
for key in (9, 10):
    for pa in (1, -1):
        for pb in (1, -1):
            pr = {"A": pa, "B": pb}; ro = {("A", key): "B", ("B", key): "A"}
            T = 40
            sh, pri = run(pr, ro, T)
            Pm = [dict(pr)] + pri          # Pm[m-1]: prior entering momentary m
            for me, ot in (("A", "B"), ("B", "A")):
                for m in range(1, T - 1):  # other's momentary m, self's momentary m+1
                    tup = (Pm[m - 1][ot], sh[m - 1][ot], Pm[m][me], sh[m][me], Pm[m + 1][me])
                    found.setdefault(("alike" if pa == pb else "opposite", m >= 2), set()).add(tup)
from_second = found.get(("alike", True), set()) | found.get(("opposite", True), set())
report("Two selves, three momentaries, five parities: the six forms, each momentary from the second",
       from_second == forms, "found %d forms; beyond the six: %s; of the six not found: %s" % (len(from_second), sorted(from_second - forms), sorted(forms - from_second)))
print("          alike openings from the second:", len(found.get(("alike", True), set())), "forms; opposite openings:", len(found.get(("opposite", True), set())), "forms")
first = (found.get(("alike", False), set()) | found.get(("opposite", False), set())) - forms
print("          with the first momentary, forms beyond the six:", sorted(first))
report("Two selves, five parities: the fifth is the first inverting (each form found, the first momentary too)",
       all(t[4] == -t[0] for s in found.values() for t in s))

# ---------------------------------------------------------------- three selves, one line
bad = []
for a, want in ((1, (0, 1, (-1, 1), 1)), (-1, (-1, -1, (-1, 0), -1))):
    soc_pr = {"B": 1, "C": 1}
    sh, pri = run(soc_pr, {("B", 9): "C"}, 2, first_incoming={"B": [(S, a)]})
    got = (sh[0]["B"], pri[0]["B"], (sh[0]["C"], sh[1]["C"]), pri[1]["C"])
    if got != want: bad.append((a, got))
report("Three selves, one line (2 rows)", not bad, str(bad))

# ---------------------------------------------------------------- a spiral opening with an empty prior
want3 = ["+··", "−+·", "+−+", "++−", "−−+", "+−−", "−++", "+−+"]
want5 = ["+····", "−+···", "+−+··", "−+−+·", "+−+−+", "++−+−", "−−+−+", "+−−+−"]
bad = []
for n, want in ((3, want3), (5, want5)):
    pr = {("", i): None for i in range(n)}; ro = {(("", i), 9): ("", (i + 1) % n) for i in range(n)}
    _, pri = run(pr, ro, 8, first_incoming={("", 0): [(S, 1)]})
    got = ["".join(sym(x[("", i)]) for i in range(n)) for x in pri]
    if got != want: bad.append((n, got))
report("A spiral opening with an empty prior, one parity sharing once (spirals of 3 and 5, 8 momentaries)", not bad, str(bad))

print()
print("%d of %d same" % (sum(1 for _, s in results if s), len(results)))
