"""Run checks for Exhibit THIRTY Part SIX (EQUILIBRIA, links E1...), against the resolver of
Exhibit ONE v372 (resolver_v372.py beside this file) and the numbers Exhibit TWENTY-EIGHT v372 names.
Each function returns True when the link holds as stated. Run: python3 ccl_eq_checks.py [results.json]"""
import os, re, sys, json
from itertools import product, combinations
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as R, CONNECTORS, JOINS

EQ_MD = '/home/claude/work/Exhibit_TWENTY-EIGHT_Equilibria_Registry_v372.md'
K = 'k'
S = (1, -1)
OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def step(st, off):
    """One call at one key: st is () or (c, t, a); returns (surface or None, next st)."""
    s, c = C([(K,) + st] if st else [], list(off))
    return dict(s).get(K), (tuple(c[0][1:]) if c else ())


def reach():
    seen = {()}; frontier = [()]
    while frontier:
        nxt = []
        for st in frontier:
            for off in OFFERS:
                _, s2 = step(st, off)
                if s2 not in seen: seen.add(s2); nxt.append(s2)
        frontier = nxt
    return seen


REACH = reach()
NONEMPTY = sorted(st for st in REACH if st)
sgn = lambda x: (x > 0) - (x < 0)

# ------------------------------------------------------------ 6.1 momentaries, surface, alternating

def E1():
    prior, now, nxt = (1, 2), (2, 3), (3, 4)
    ok = len(set(prior + now + nxt)) == 4 and prior[1] == now[0] and now[1] == nxt[0]
    ok &= [nxt[0] - now[0], now[0] - prior[0]] == [1, 1]                  # across: next opens one on
    self_m, other_m = [(1, 2), (3, 4)], [(2, 3), (4, 5)]
    ok &= self_m[1][1] + 1 == 5 and other_m[1][1] + 1 == 6                 # along: next opens two on
    ok &= self_m[1][0] - self_m[0][0] == 2 and other_m[1][0] - other_m[0][0] == 2
    views = {o: list(range(o, o + 5)) for o in (1, 2, 3)}                  # the five-views at 1, 2, 3
    for a, b in ((1, 2), (2, 3)):
        shared = sorted(set(views[a]) & set(views[b]))
        ok &= len(shared) == 4
        role = lambda origin, n: 'open' if (n - origin) % 2 == 0 else 'complete'
        ok &= all({role(a, n), role(b, n)} == {'open', 'complete'} for n in shared)
    return ok


def E6():
    ok = True
    for n, m in product(range(3, 13), repeat=2):                           # square grids closed as a torus
        V = [(i, j) for i in range(n) for j in range(m)]
        E = set()
        for i, j in V:
            E.add(frozenset({(i, j), ((i + 1) % n, j)})); E.add(frozenset({(i, j), (i, (j + 1) % m)}))
        F = n * m
        deg = {v: sum(v in e for e in E) for v in V}
        ok &= all(d == 4 for d in deg.values()) and 4 * F == 2 * len(E) and 4 * len(V) == 2 * len(E)
        ok &= len(V) - len(E) + F == 0
    # the cube: four-sided faces but three edges at each point, V - E + F = 2 (the sphere)
    ok &= 8 - 12 + 6 == 2
    return ok


def rounds_two():
    St = list(product(S, S))
    return {'right': {(x, y): (y, -x) for x, y in St}, 'other': {(x, y): (-y, x) for x, y in St}}


def E10():
    ok = True
    for m in rounds_two().values():
        for s0 in m:
            s = s0; changed = []
            for _ in range(8):
                n = m[s]; d = [i for i in range(2) if n[i] != s[i]]
                ok &= len(d) == 1; changed.append(d[0]); s = n
            ok &= all(changed[i] != changed[i + 1] for i in range(7))
    return ok


def E11():
    orders = list(product(('first', 'second'), repeat=2))
    both = [o for o in orders if set(o) == {'first', 'second'}]
    one = [o for o in orders if len(set(o)) == 1]
    return len(orders) == 4 and both == [('first', 'second'), ('second', 'first')] and len(one) == 2


def E12():
    shown = [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]
    r = rounds_two()
    by_other = all(r['other'][shown[i]] == shown[i + 1] for i in range(4))
    by_right = all(r['right'][shown[i]] == shown[i + 1] for i in range(4))
    return by_other and not by_right and len(set(shown[:4])) == 4


def E13():
    ok = True
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            E = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
            A = [[0] * n for _ in range(n)]
            for a, b in E: A[a][b] = A[b][a] = 1
            # odd closed route: trace of A^k > 0 for some odd k <= n
            P = [row[:] for row in A]; odd = False
            for k in range(2, n + 1):
                P = [[sum(P[i][l] * A[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
                if k % 2 == 1 and sum(P[i][i] for i in range(n)) > 0: odd = True
            cols = [c for c in product((0, 1), repeat=n) if all(c[a] != c[b] for a, b in E)]
            # connected wholes
            comp = list(range(n))
            def f(x):
                while comp[x] != x: x = comp[x]
                return x
            for a, b in E: comp[f(a)] = f(b)
            wholes = len({f(x) for x in range(n)})
            ok &= (len(cols) > 0) == (not odd)
            if not odd: ok &= len(cols) == 2 ** wholes
    return ok

# ------------------------------------------------------------ 6.4 the ten

def E37():
    return all(n * n - (n - 1) * (n + 1) == 1 for n in range(-1000, 1001)) and (2, 3)[1] == (3, 4)[0]


def E38():
    self5, other5 = set(range(1, 6)), set(range(2, 7))
    moms = [(1, 2), (3, 4), (5, 6)]
    return (self5 | other5 == set(range(1, 7)) and sorted(x for m in moms for x in m) == list(range(1, 7))
            and ['co' if n % 2 else 'bi' for n in range(1, 7)] == ['co', 'bi', 'co', 'bi', 'co', 'bi'])


def E39():
    table = {2: ('self completing', 'other opening'), 3: ('self opening', 'other completing'),
             4: ('self completing', 'other opening'), 5: ('self opening', 'other completing'),
             6: ('self completing', 'other opening')}
    ok = True
    for n, (sf, of) in table.items():
        self_role = 'opening' if n % 2 == 1 else 'completing'             # self momentaries 1-2, 3-4, 5-6
        other_role = 'opening' if n % 2 == 0 else 'completing'            # other momentaries 2-3, 4-5, 6-7
        ok &= sf == 'self ' + self_role and of == 'other ' + other_role and self_role != other_role
    return ok and len(table) * 2 == 10


def eq_text():
    return open(EQ_MD, encoding='utf-8').read()


def E42():
    t = eq_text()
    ring = [3, 2, 4, 1, 14, 12, 6, 10, 11, 16]
    ok = '3→2→4→1→14→12→6→10→11→16→next 3' in t and '1,10,7,9,8,4,6,5,3,2' in t
    rows = re.findall(r'^\| (\d) \| .*?\| (\d+) · .*?\| (\d+) · .*?\| (\d+)→(\d+) / (\d+)→(\d+) \|$', t, re.M)
    addr = {}
    for place, e, s_, a1, a2, b1, b2 in rows:
        addr[int(e)] = (int(a1), int(a2)); addr[int(s_)] = (int(b1), int(b2))
    edges = [(ring[i], ring[(i + 1) % 10]) for i in range(10)]
    at_ring = [next(w for w, ed in addr.items() if ed == e) for e in edges]
    ok &= len(rows) == 5 and sorted(addr) == list(range(1, 11)) and at_ring == [1, 10, 7, 9, 8, 4, 6, 5, 3, 2]
    ok &= len(set(ring)) == 10 and 6 in ring and 14 in ring
    ok &= edges[3:8] == [(1, 14), (14, 12), (12, 6), (6, 10), (10, 11)]
    return ok


def E46():
    ok = sum((1, 3, 5)) == 9 == 3 ** 2 and sum((2, 4, 6)) == 12 == 3 * 4 and 3 ** 2 - 2 * 4 == 1
    ok &= all(sum(range(1, 2 * n, 2)) == n * n and sum(range(2, 2 * n + 1, 2)) == n * (n + 1) for n in range(1, 101))
    six = list(range(3, 9))
    return ok and len(six) == 6 and six[-1] == 8 and six[-1] + 1 == 9


def ring(n, steps, seed=True):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]
    if seed: inbox[0] = [(K, 1)]
    hist = []
    for _ in range(steps):
        nb = [[] for _ in range(n)]
        for i in range(n):
            s, c = C(carry[i], inbox[i]); carry[i] = c
            nb[(i + 1) % n] += R(s, {K: K})
        inbox = nb
        hist.append((tuple(tuple(c) for c in carry), tuple(tuple(b) for b in inbox)))
    return hist


def E47():
    ok = True
    for n in range(1, 12):
        h = ring(n, 40)
        prev = tuple(() for _ in range(n))
        changed = set()
        for carry, _ in h:
            changed |= {i for i in range(n) if carry[i] != prev[i]}; prev = carry
        ok &= changed == set(range(n))
        rest = ring(n, 100, seed=False)
        ok &= all(st == (tuple(() for _ in range(n)), tuple(() for _ in range(n))) for st in rest)
    return ok


def E50():
    internal = [(3, 11), (4, 12), (5, 13), (7, 15), (8, 16)]
    ten = {x for p in internal for x in p}
    conn = set(CONNECTORS)
    ring_names = {3, 2, 4, 1, 14, 12, 6, 10, 11, 16}
    ok = all(b - a == 8 for a, b in internal) and all(17 - (9 - n) == n + 8 for n in range(1, 9))
    ok &= conn == {2, 6, 9, 10, 14, 17} and not (ten & conn) and ten | conn == set(range(2, 18))
    ok &= ten | conn | {1} == set(range(1, 18)) and len(ten) == 10
    ok &= ring_names & conn == {2, 6, 10, 14} and 1 in ring_names    # the ring's addresses are other names
    return ok

# ------------------------------------------------------------ 6.5 the conceptions

def E53():
    t = eq_text()
    rows = re.findall(r'^\| (\d+) · [^|]*\| \*\*((?:NY|SA)\d\d)\*\*', t, re.M)
    ids = [i for _, i in rows]
    per = {}
    for w, i in rows: per[int(w)] = per.get(int(w), 0) + 1
    want_ids = [f'NY{i:02d}' for i in range(1, 43)] + [f'SA{i:02d}' for i in range(1, 22)]
    return (sorted(ids) == sorted(want_ids) and len(ids) == 63 and len(set(ids)) == 63
            and [per[w] for w in range(1, 11)] == [2, 5, 8, 10, 6, 9, 5, 5, 7, 6]
            and min(per.values()) == 2 and max(per.values()) == 10)


def stationary(P, pi):
    states = list(pi)
    return all(sum(pi[a] * P[a].get(b, 0) for a in states) == pi[b] for b in states)


def E60():
    ok = True
    # NY15: constant +1 at one key from empty returns five complete values, A->B->C->D->E->A
    st = (); seq = []
    for _ in range(11):
        _, st = step(st, [(K, 1)]); seq.append(st)
    cyc = seq[:5]
    ok &= len(set(cyc)) == 5 and seq[5:10] == cyc
    P = {cyc[i]: {cyc[(i + 1) % 5]: Fraction(1)} for i in range(5)}
    ok &= stationary(P, {x: Fraction(1, 5) for x in cyc})
    # NY16: the two exchanged opposed-sign values under empty receiving; stationarity and detailed balance
    for c in S:
        A = (c, -c, 0); _, B = step(A, []); _, A2 = step(B, [])
        ok &= B == (-c, c, 0) and A2 == A
        P = {A: {B: Fraction(1)}, B: {A: Fraction(1)}}; pi = {A: Fraction(1, 2), B: Fraction(1, 2)}
        ok &= stationary(P, pi) and pi[A] * P[A][B] == pi[B] * P[B][A]
    # NY17: A->B, B->A, X->B; at the code an instance X = (+,-,1) under empty receiving goes to B
    A, B, X = (1, -1, 0), (-1, 1, 0), (1, -1, 1)
    ok &= step(A, [])[1] == B and step(B, [])[1] == A and step(X, [])[1] == B
    P = {A: {B: Fraction(1)}, B: {A: Fraction(1)}, X: {B: Fraction(1)}}
    ok &= stationary(P, {A: Fraction(1, 2), B: Fraction(1, 2), X: Fraction(0)})
    return ok

# ------------------------------------------------------------ 6.6 shared exclusions

def E65():
    ok = len(NONEMPTY) == 18; kinds = set()
    for st in NONEMPTY:
        c, t, a = st
        for off in OFFERS:
            _, n = step(st, off)
            ok &= n != st
            if not n: kinds.add('releasing completes')
            elif n == (c, t, a + 1): kinds.add('retaining opens one on')
            elif n[1] == -t and n[2] == 0: kinds.add('fresh writing inverts t')
            else: ok = False
    return ok and len(kinds) == 3


def E66():
    ok = True; longest = {1: 0, -1: 0}
    for st in NONEMPTY:
        for off in OFFERS:
            _, n = step(st, off)
            if n and n[1] == st[1]: ok &= n == (st[0], st[1], st[2] + 1)     # t kept only by retaining
            if n and n[1] != st[1]: ok &= n[2] == 0                           # a fresh write inverts t
    for st in NONEMPTY:
        if st[2] != 0: continue
        cur = st; k = 0
        while True:
            _, n = step(cur, [(K, cur[0])])                                   # the arriving that retains
            if n and n[1] == st[1]: k += 1; cur = n
            else: break
        longest[st[1]] = max(longest[st[1]], k)
    return ok and longest == {-1: 3, 1: 4}


def E67():
    ok = True
    for st in NONEMPTY:
        for off in OFFERS:
            s, n = step(st, off)
            if s == 0: ok &= (not n) or n == (st[0], st[1], st[2] + 1)        # a zero writes nothing fresh
        cur = st; k = 0
        while cur:
            s, cur = step(cur, [(K, cur[0])]); k += 1
            ok &= s == 0
        ok &= k <= 5
    ks = []
    for st in NONEMPTY:
        cur = st; k = 0
        while cur: _, cur = step(cur, [(K, cur[0])]); k += 1
        ks.append(k)
    return ok and max(ks) == 5


def E69():
    ok = True
    for c in S:
        st = (c, -c, 0)
        for _ in range(9):
            s, n = step(st, [])
            ok &= n[1] == -n[0] and n[0] == -st[0] and n[1] == -st[1] and s == -st[0]
            st = n
    # one side's reversal alone: (c, t) -> (-c, t) at t = -c gives (-c, -c), agreeing: opposition fails
    one_side = all((-c) == t for c, t in product(S, S) if t == -c)
    return ok and one_side


def E71():
    return not any(p == p and p == -p for p in S)


def E72():
    alt = [0, 1] * 8
    wins = [tuple(alt[i:i + 3]) for i in range(len(alt) - 2)]
    ok = all({wins[i], wins[i + 1]} == {(0, 1, 0), (1, 0, 1)} for i in range(len(wins) - 1))
    fwd = lambda n: 2 - n; rev = lambda n: n                               # two molecules, equal constants
    ok &= [n for n in range(3) if fwd(n) == rev(n)] == [1] and {1 - 1, 1 + 1} == {0, 2}
    pi = [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]                  # NY31, stationary and balanced
    ok &= pi[0] * fwd(0) == pi[1] * rev(1) and pi[1] * fwd(1) == pi[2] * rev(2)
    return ok


def E73():
    Rn = {(0, 1), (1, 2)}
    trans = all((a, d) in Rn for a, b in Rn for c, d in Rn if b == c)
    ok = not trans and (0, 2) not in Rn
    for a in range(-5, 6):
        b = a + 1
        ok &= (a + 1, b) not in {(x, x + 1) for x in range(-10, 10)} and (a, b + 1) not in {(x, x + 1) for x in range(-10, 10)}
    return ok


def E74():
    St = list(product(S, S)); F = lambda p: (-p[1], p[0])
    ok = True
    for s0 in St:
        seen = {s0}; s = s0
        for _ in range(3): s = F(s); seen.add(s)
        ok &= seen == set(St)
    worst = 0; inv = []
    for r in range(0, 5):
        for sub in combinations(St, r):
            sub = set(sub)
            if {F(x) for x in sub} == sub: inv.append(len(sub))
            if 0 < r < 4:
                for x in sub:
                    k = 0; y = x
                    while y in sub: y = F(y); k += 1
                    worst = max(worst, k)
    s = (1, 1); path = [s]
    for _ in range(3): s = F(s); path.append(s)
    three = {(1, 1), (-1, 1), (-1, -1)}
    ok &= path[:3] == [(1, 1), (-1, 1), (-1, -1)] and path[3] not in three
    return ok and worst == 3 and sorted(inv) == [0, 4]


def E75():
    ok = True
    # unit-ratio fuel-coupled cycle: a f = b w, b = c, c = a, a, b, c > 0
    for f, w in product(range(1, 11), repeat=2):
        a = b = c = Fraction(1)                                            # b = c = a forced by the two unit balances
        ok &= ((a * f == b * w) == (f == w))
    # finite attaining of zero under a nonzero multiplier
    for lam in (Fraction(-1, 2), Fraction(-1), Fraction(-2), Fraction(3)):
        r = Fraction(1)
        for _ in range(200):
            r = lam * r; ok &= r != 0
    # an opposed row through the aggregate route offers zero onward, next and later
    s, cr = C([], [(K, 1), (K, -1)])
    ok &= s == [(K, 0)] and cr == []
    onward = R(s, {K: K})
    ok &= onward == [(K, 0)] and C([], onward) == ([], [])
    for _ in range(5):
        s, cr = C(cr, [(K, 1), (K, -1)]); onward = R(s, {K: K})
        ok &= onward == [(K, 0)] and C([], onward) == ([], [])
    return ok


def E76():
    St = list(product(S, S)); J = {p: (-p[0], -p[1]) for p in St}
    roots = []
    for img in product(St, repeat=4):
        m = dict(zip(St, img))
        if all(m[m[p]] == J[p] for p in St): roots.append(m)
    Fm = {(c, t): (-t, c) for c, t in St}; Gm = {(c, t): (t, -c) for c, t in St}
    ok = len(roots) == 2 and Fm in roots and Gm in roots
    for st in NONEMPTY:
        c, t, a = st
        for off in OFFERS:
            s, n = step(st, off)
            if s: ok &= n[:2] == Gm[(t, s)]                               # 6/10 = (t, s); fresh 7/8 = G(t, s)
        s, n = step(st, [])
        ok &= s == -c and n[:2] == (-c, -t) == J[(c, t)]
    return ok


def E79():
    ok = True
    for st in REACH:
        c = st[0] if st else 0
        for L in range(0, 5):
            for seq in product((-1, 0, 1), repeat=L):
                s, _ = step(st, [(K, v) for v in seq])
                if s is not None: ok &= s == sgn(sum(seq) - c)
    ok &= step((1, -1, 0), [(K, 1), (K, 1)])[1] == (1, 1, 0)                # agreement from (+,-)
    ok &= step((-1, 1, 0), [(K, 1), (K, 1)])[1] == (1, -1, 0)               # opposition from (-,+)
    ok &= step((1, -1, 0), [(K, 1)])[1] == (1, -1, 1)                       # continues from opening 0
    ok &= step((1, -1, 3), [(K, 1)])[1] == ()                               # leaves from opening 3
    return ok


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'E\d+', k) and callable(v)}

if __name__ == '__main__':
    res = {}
    for k in sorted(CHECKS, key=lambda s: int(s[1:])):
        try: res[k] = bool(CHECKS[k]())
        except Exception as e: res[k] = f'error: {e!r}'
        print(k, res[k])
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'ccl_eq_check_results.json')
    json.dump(res, open(out, 'w'), indent=1)
