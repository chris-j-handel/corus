"""Run checks for Exhibit THIRTY Part FIVE · NETWORKING (links W…), from Exhibit TWO v371,
against Exhibit ONE v371's resolver as resolver_v371.py beside this file.
Run:  python3 ccl_two_checks.py [results.json]"""
import ast, os, re, sys, json, copy, symtable, zipfile
from itertools import product, combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v371 as RV

C = RV._1_self_coupling; R = RV._9_other_releasing
CON = RV.CONNECTORS; JOI = RV.JOINS
SRC = open(os.path.join(HERE, 'resolver_v371.py')).read()
TREE = ast.parse(SRC)
KIT_ZIP = '/home/claude/corus/Natural_Networking_Test_Kit_v368.zip'
K = 'k'
S = (1, -1)
OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def reach(Cf=C):
    seen = {()}; fr = [()]
    while fr:
        nx = []
        for st in fr:
            for off in OFFERS:
                _, c = Cf([(K,) + st] if st else [], off)
                s2 = tuple(c[0][1:]) if c else ()
                if s2 not in seen: seen.add(s2); nx.append(s2)
        fr = nx
    return sorted(seen)

REACH = reach()
def carry_of(st): return [(K,) + st] if st else []
def six(carry): return [(k, t) for k, c, t, a in carry]


# ------------------------------------------------ 5.2 the six connectors
def W7():
    ok = True
    for a, b in JOI.items():
        fa, fb = CON[a][1], CON[b][1]
        ok &= {fa, fb} in ({'right', 'left'}, {'forward', 'backward'})
        if {fa, fb} == {'right', 'left'}:
            ok &= {CON[a][2], CON[b][2]} == {'releasing', 'arriving'} and CON[a][2] == 'releasing'
    # the table: 2 meets the right neighbour's 6, 6 the left neighbour's 2, 10 the right's 14, 14 the left's 10, 9 the backward's 17, 17 the forward's 9
    table = {2: 6, 6: 2, 10: 14, 14: 10, 9: 17, 17: 9}
    opposite = {'right': 'left', 'left': 'right', 'forward': 'backward', 'backward': 'forward'}
    ok &= all(CON[b][1] == opposite[CON[a][1]] for a, b in table.items())
    ok &= all(JOI.get(a) == b or JOI.get(b) == a for a, b in table.items())
    return ok and sorted(CON) == [2, 6, 9, 10, 14, 17]


# ------------------------------------------------ 5.3 the local cycle
def W14():
    selfm = [(1, 2), (3, 4), (5, 6), (7, 8)]; otherm = [(2, 3), (4, 5), (6, 7), (8, 9)]
    pos = {x for m in selfm + otherm for x in m}
    return (pos == set(range(1, 10)) and len(selfm) == len(otherm) == 4
            and all(s[1] == o[0] for s, o in zip(selfm, otherm))
            and all(o[1] == s2[0] for o, s2 in zip(otherm, selfm[1:])))


# ------------------------------------------------ 5.4 overlapping momentaries, the four-form
def W18():
    one, other = {1, 2, 3, 4}, {2, 3, 4, 5}
    return (len(one & other) == 3 and len(one | other) == 5
            and sum(1 for x in one if x % 2) == 2 and sum(1 for x in other if x % 2) == 2)

def W20():
    ok = True
    for st in REACH:
        for off in OFFERS:
            s, c = C(carry_of(st), off); v = dict(s).get(K)
            if v:
                ok &= c[0][1] == v and R(s, {K: K}) == [(K, v)]
    return ok

def W21():
    return (JOI == {10: 14, 6: 2, 17: 9, 9: 17} and JOI[9] == 17 and (9, 2) not in JOI.items()
            and 1 not in JOI.values())

def W23():
    now = [(4, 5), (6, 7), (8, 9)]; on = [(a + 8, b + 8) for a, b in now]
    return (on == [(12, 13), (14, 15), (16, 17)]
            and all(a % 2 == 0 and b % 2 == 1 for a, b in now + on) and len(now) * 2 == 6)

def W24():
    ok = True
    for x, y in product(S, S):
        f = lambda p: (p[1], -p[0])
        seq = [(x, y)]
        for _ in range(12): seq.append(f(seq[-1]))
        ok &= seq[4] == (x, y) and seq[6] == (-x, -y) and seq[12] == (x, y)
        ok &= all(set(seq[i + 1:i + 7]) == set(product(S, S)) for i in range(0, 7))
    ok &= (24 // 4, 24 // 6, 36 // 4, 36 // 6) == (6, 4, 9, 6) and 24 == 3 * 8 and 36 == 3 * 12
    return ok


# ------------------------------------------------ 5.5 widening and lengthening
def W25():
    ok = True
    want_odd = [9, 17, 25, 33, 41]
    for s in range(1, 6):
        row = [2 + 2 * s * j for j in range(4)]
        mid = (row[0] + row[-1]) / 2
        ok &= row[1] - row[0] == 2 * s and 2 * (2 * s) == 4 * s
        ok &= 8 * s + 1 == want_odd[s - 1] and row[-1] + 2 * s == 8 * s + 2
        ok &= [r - mid for r in row] == [-3 * s, -s, s, 3 * s] and row[-1] - row[0] == 6 * s == 2 * (3 * s)
        ok &= all(((8 * s + 1) - n) % 2 != n % 2 and 1 <= (8 * s + 1) - n <= 8 * s for n in range(1, 8 * s + 1))
    return ok and [2 + 2 * 2 * j for j in range(4)] == [2, 6, 10, 14]

def W26():
    spans = [2 ** k + 1 for k in range(3, 7)]
    return spans == [9, 17, 33, 65] and 17 - 1 == 16 and len(range(1, 18)) == 17

def primes(a, b): return [p for p in range(a, b + 1) if p > 1 and all(p % d for d in range(2, p))]

def W28():
    P = primes(5, 59)
    wide = sum(1 for i in range(len(P)) if i % 2 == 0)
    gaps = [b - a for a, b in zip(primes(3, 59), primes(3, 59)[1:])]
    return (P == [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59] and len([p for p in P if p <= 53]) == 14
            and (wide, len(P) - wide) == (8, 7) and len(primes(3, 59)) == 16 and len(gaps) == 15
            and all(g % 2 == 0 for g in gaps))

def W29():
    ok = True
    for p in primes(5, 59):
        h = (p - 1) // 2
        dist = lambda k: min(k, p - k)
        far = [k for k in range(p) if dist(k) == max(dist(j) for j in range(p))]
        ok &= far == [h, h + 1] and dist(h) == dist(h + 1) == h
        ok &= (p - 1, (p - 1) // 2) == (p - 1, h)
        oddp = [(i, i + 1) for i in range(1, p, 2)]; evenp = [(i, i + 1) for i in range(2, p, 2)]
        inn = lambda x, L: sum(1 for a, b in L if x in (a, b))
        ok &= all(inn(x, oddp) == 1 and inn(x, evenp) == 1 for x in range(2, p))
        ok &= inn(1, oddp) == 1 and inn(1, evenp) == 0 and inn(p, evenp) == 1 and inn(p, oddp) == 0
    far59 = [k for k in range(59) if min(k, 59 - k) == 29]
    return ok and far59 == [29, 30] and (17 - 1, (17 - 1) // 2) == (16, 8)

def W30():
    ok = 6 / 3 == 2 and 3 / 6 == 0.5
    for L in range(2, 1001, 2):
        pair = 2 * L; waist_pair = pair // 2
        ok &= waist_pair == L and pair / L == 2 and pair - L // 2 == L + L // 2
    return ok and 2 * 440 - 220 == 660


# ------------------------------------------------ 5.7 society, primes below 60
def W33():
    P = primes(2, 59)
    return len(P) == 17 and P[8] == 23 and len(P[:8]) == len(P[9:]) == 8 and sum(P) == 440 and \
        sorted(120 - p for p in P)[0] == 61 and max(120 - p for p in P) == 118


# ------------------------------------------------ 5.10 carrying at its self
def W48():
    st = symtable.symtable(SRC, 'resolver', 'exec')
    fns = {c.get_name(): c for c in st.get_children() if c.get_type() == 'function'}
    ok = set(fns) == {'_1_self_coupling', '_9_other_releasing'}
    for f in fns.values():
        globs = set(f.get_globals())
        for ch in f.get_children():                       # comprehension scopes
            globs |= set(ch.get_globals())
        ok &= globs == set()
    ok &= not any(isinstance(n, (ast.Global, ast.Nonlocal)) for n in ast.walk(TREE))
    for st_ in REACH:
        for off in OFFERS:
            ok &= C(carry_of(st_), off) == C(carry_of(st_), off)
    return ok


# ------------------------------------------------ 5.11 invocation is a caller's
def W56():
    top = TREE.body
    kinds = [type(n).__name__ for n in top]
    calls_at_top = [n for n in top if not isinstance(n, ast.FunctionDef) for m in ast.walk(n) if isinstance(m, ast.Call)]
    return kinds.count('FunctionDef') == 2 and kinds.count('Assign') == 2 and not calls_at_top and \
        all(k in ('Expr', 'FunctionDef', 'Assign') for k in kinds)


# ------------------------------------------------ 5.12 securities: the inversion taken out
def resolver_without_inversion():
    t = SRC.replace("_14_social_crossing.append((_4_self_sharing, -1))", "_14_social_crossing.append((_4_self_sharing, +9))")
    t = t.replace("_14_social_crossing.append((_4_self_sharing, 1))", "_14_social_crossing.append((_4_self_sharing, -1))")
    t = t.replace("+9))", "1))")
    ns = {}; exec(t, ns); return ns['_1_self_coupling']

def W62():
    Cx = resolver_without_inversion()
    ok = Cx([(K, 1, -1, 0)], []) [0] == [(K, 1)] and C([(K, 1, -1, 0)], [])[0] == [(K, -1)]
    for c in S:
        carry = []; surf = []
        for i in range(9):
            s, carry = Cx(carry, [(K, c)] if i == 0 else []); surf.append(dict(s).get(K))
        ok &= surf == [c] * 9
        carry = []; surf = []
        for i in range(9):
            s, carry = C(carry, [(K, c)] if i == 0 else []); surf.append(dict(s).get(K))
        ok &= surf == [c, -c] * 4 + [c]
    return ok

def W65():
    ok = True
    for n in range(3, 9):
        ring = {frozenset((i, (i + 1) % n)) for i in range(n)}
        full = {frozenset(p) for p in combinations(range(n), 2)}
        ok &= (ring == full) == (n == 3)
    return ok

def pairs_parted(drop, n=6):
    def run(st, off):
        carry = carry_of(st); out = []
        for _ in range(n):
            s, carry = C(carry, off); v = dict(s).get(K); out.append(v if v else 0)
        return [v for v in out if v] if drop else out
    P = list(combinations(REACH, 2))
    plus = {p for p in P if run(p[0], [(K, 1)]) != run(p[1], [(K, 1)])}
    minus = {p for p in P if run(p[0], [(K, -1)]) != run(p[1], [(K, -1)])}
    return len(P), len(plus), len(minus), len(plus | minus)

def W70():
    def seq(st, off, n=12):
        carry = carry_of(st); out = []
        for _ in range(n):
            s, carry = C(carry, off); v = dict(s).get(K); out.append(v if v else 0)
        return out
    def first(a, b): return next((i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y), None)
    mins = []
    for a, b in combinations(REACH, 2):
        w = [first(seq(a, o), seq(b, o)) for o in ([(K, 1)], [(K, -1)])]
        mins.append(min(x for x in w if x))
    return (len(REACH) == 19 and pairs_parted(False) == (171, 146, 146, 171) and max(mins) == 6
            and mins.count(6) == 8 and pairs_parted(True) == (171, 78, 78, 123))


# ------------------------------------------------ 5.13 the instrument
def ring(n, steps):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]; inbox[0] = [(K, 1)]
    surf = []
    for _ in range(steps):
        nb = [[] for _ in range(n)]; row = []
        for i in range(n):
            s, c = C(carry[i], inbox[i]); carry[i] = c
            nb[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
        inbox = nb; surf.append(tuple(row))
    return surf

def W77():
    ok = True
    for n in range(1, 41):
        per = ring(n, 8 * n + 8)[n:]
        z = [[i for i in range(n) if per[t][i] == 0] for t in range(len(per))]
        ok &= all(v is not None for r in per for v in r)
        if n % 2 == 0:
            ok &= all(not zi for zi in z)
        else:
            ok &= all(len(zi) <= 1 for zi in z)
            at = [(t, zi[0]) for t, zi in enumerate(z) if zi]
            ok &= all(b[0] - a[0] == 2 for a, b in zip(at, at[1:]))
            ok &= len(at) >= (len(per) - 1) // 2
            if n > 1: ok &= all(b[1] == (a[1] + 1) % n for a, b in zip(at, at[1:]))
    return ok and (3 + 5) % 2 == 0

def two_run(sa, sb, first, ab, ba, calls=12):
    car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}; inbox = {'A': [], 'B': []}
    order = ['A', 'B'] if first == 'A' else ['B', 'A']; log = []
    for i in range(calls):
        me = order[i % 2]; other = 'B' if me == 'A' else 'A'
        rel = six(car[me]); s, c = C(car[me], inbox[me]); inbox[me] = []
        if (ab if me == 'A' else ba): inbox[other] = rel
        log.append((me, dict(s).get(K), rel, car[me], c)); car[me] = c
    return log

def W79():
    parted = tot = 0
    for sa, sb in product(S, S):
        for me in 'AB':
            a = [x[1] for x in two_run(sa, sb, 'A', True, True) if x[0] == me]
            b = [x[1] for x in two_run(sa, sb, 'B', True, True) if x[0] == me]
            tot += 1; parted += a != b
    return (parted, tot) == (8, 8)

def taking_out():
    def load(t):
        ns = {}; exec(compile(ast.fix_missing_locations(t), 'x', 'exec'), ns); return ns
    def fingerprint(ns):
        Cf = ns['_1_self_coupling']; out = []
        seen = {()}; fr = [()]
        while fr:
            nx = []
            for st in fr:
                for off in OFFERS + [[(K, 0)], [(K, 0), (K, 1)]]:
                    try: r = Cf([(K,) + st] if st else [], off)
                    except Exception as e: return ('error', repr(e))
                    out.append((st, tuple(off), repr(r)))
                    c = r[1]; s2 = tuple(c[0][1:]) if c else ()
                    if s2 not in seen and len(seen) < 200: seen.add(s2); nx.append(s2)
            fr = nx
        for a, b in product([(), (1, -1, 0), (-1, 1, 2)], repeat=2):
            car = [x for x in [(('a',) + a) if a else None, (('b',) + b) if b else None] if x]
            for off in ([], [('a', 1), ('b', -1)], [('c', 1)]):
                try: out.append(('2', repr(Cf(car, off))))
                except Exception as e: return ('error', repr(e))
        return out
    F0 = fingerprint(load(copy.deepcopy(TREE)))
    fn = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
    paths = []
    def walk(node, path):
        for field, val in ast.iter_fields(node):
            if isinstance(val, list):
                for i, v in enumerate(val):
                    if isinstance(v, ast.stmt): paths.append((path + [(field, i)], 'stmt'))
                    if isinstance(v, ast.AST): walk(v, path + [(field, i)])
                    if isinstance(v, ast.comprehension):
                        for j, _ in enumerate(v.ifs): paths.append((path + [(field, i), ('ifs', j)], 'if'))
            elif isinstance(val, ast.AST): walk(val, path + [(field, None)])
    walk(fn, [])
    def get(node, path):
        for f, i in path: node = getattr(node, f) if i is None else getattr(node, f)[i]
        return node
    same = []
    for p, kind in paths:
        t = copy.deepcopy(TREE); f = next(n for n in t.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
        parent = get(f, p[:-1]); fld, i = p[-1]; lst = getattr(parent, fld)
        text = ast.unparse(lst[i])
        del lst[i]
        if kind == 'stmt' and not lst: lst.append(ast.Pass())
        try: F = fingerprint(load(t))
        except Exception as e: F = ('error', repr(e))
        if F == F0: same.append((kind, text, p))
    return len(paths), same

def W81():
    n, same = taking_out()
    if n != 23 or len(same) != 1: return False
    kind, text, p = same[0]
    fn = next(x for x in TREE.body if isinstance(x, ast.FunctionDef) and x.name == '_1_self_coupling')
    host = fn
    for f, i in p[:-1]: host = getattr(host, f) if i is None else getattr(host, f)[i]
    gathers_offering = isinstance(host, ast.comprehension) and ast.unparse(host.iter) == '_2_self_offering'
    return kind == 'if' and text == '_7_other_corusing != 0' and gathers_offering


# ------------------------------------------------ 5.14 the numbered form of 440, the chain's centre
def W87():
    ok = all(sum(1 for step in range(1, 441) if (k + step) % 440 == (k + 220) % 440) == 1 for k in range(440))
    own = [k for k in range(440) if k % 440 == (440 - k) % 440]
    return ok and own == [0, 220]

def W92():
    ok = True
    for n in range(1, 201):
        centre = 220 * n
        on_coupling = centre % 440 == 0
        ok &= on_coupling == (n % 2 == 0)
        if not on_coupling: ok &= centre % 440 == 220          # a self's own waist
        ok &= 220 * (n + 1) - centre == 220 and (220 * (n + 1)) % 440 != centre % 440
    return ok and (220 * 3) % 440 == 220 and (220 * 4) % 440 == 0


# ------------------------------------------------ 5.15 the studies at their domains
def W95():
    ok = True
    a_both = [x[1] for x in two_run(-1, -1, 'A', True, True) if x[0] == 'A']
    ok &= a_both == [1, -1, 0, 1, -1, 0]
    for ab, ba in [(True, False), (False, True), (False, False)]:
        ok &= [x[1] for x in two_run(-1, -1, 'A', ab, ba) if x[0] == 'A'] == [1, -1, 1, -1, 1, -1]
    ok &= next(i for i, (x, y) in enumerate(zip(a_both, [1, -1, 1, -1, 1, -1])) if x != y) + 1 == 3
    acct = {}
    for ab, ba in [(True, True), (True, False), (False, True), (False, False)]:
        log = two_run(-1, -1, 'A', ab, ba); n = len(log)
        joined = lambda me: ab if me == 'A' else ba
        rel = [(i, x[0]) for i, x in enumerate(log) if x[2]]
        acct[(ab, ba)] = (len(rel), sum(1 for i, me in rel if joined(me) and i < n - 1),
                          sum(1 for i, me in rel if joined(me) and i == n - 1), sum(1 for i, me in rel if not joined(me)))
    ok &= acct[(True, True)] == (12, 11, 1, 0)
    ok &= all(a[1] + a[2] + a[3] == a[0] for a in acct.values())
    return ok

def interrupted(sa, sb, leg, i0, i1, mode, calls=12):
    car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}
    inbox = {'A': [], 'B': []}; queue = []; log = []
    for i in range(calls):
        me = 'A' if i % 2 == 0 else 'B'; other = 'B' if me == 'A' else 'A'
        rel = six(car[me]); off = inbox[me]; inbox[me] = []
        if me != leg and mode == 'delay' and i >= i1 and queue:
            queue.extend(off); off = [queue.pop(0)] if queue else []
        s, c = C(car[me], off)
        log.append((i, me, off, dict(s).get(K), car[me], c)); car[me] = c
        if me == leg and i0 <= i < i1:
            if mode == 'delay': queue.extend(rel)
        else:
            inbox[other] = rel
    return log

def meets_pattern(sa, sb, leg, i0, i1):
    L = interrupted(sa, sb, leg, i0, i1, 'loss'); D = interrupted(sa, sb, leg, i0, i1, 'delay')
    rcv = [x for x in L if x[1] != leg and x[0] >= i1]
    if not rcv: return False
    j = rcv[0][0]
    same_before = all(L[t][3:] == D[t][3:] for t in range(j))
    l, d = L[j], D[j]
    return (same_before and l[4] == d[4] and l[2] == [(K, 1)] and l[3] == 0 and d[2] == [(K, -1)] and d[3] == -1)

def W96():
    L = interrupted(1, 1, 'A', 0, 4, 'loss'); D = interrupted(1, 1, 'A', 0, 4, 'delay')
    ok = all(L[t][3:] == D[t][3:] for t in range(5))
    ok &= L[5][1] == 'B' and L[5][4] == [(K, 1, -1, 0)] == D[5][4]
    ok &= L[5][2] == [(K, 1)] and L[5][3] == 0 and L[5][5] == [(K, 1, -1, 1)]
    ok &= D[5][2] == [(K, -1)] and D[5][3] == -1
    count = sum(meets_pattern(sa, sb, leg, i0, i1) for sa, sb, leg in product(S, S, 'AB')
                for i0 in range(12) for i1 in range(i0 + 1, 12))
    return ok and count == 30

def W97():
    pos = [(r, c) for r in range(3) for c in range(3)]
    def edges(kinds, removed):
        E = set()
        for r, c in pos:
            if 'across' in kinds and c < 2: E.add(frozenset({(r, c), (r, c + 1)}))
            if 'along' in kinds and r < 2: E.add(frozenset({(r, c), (r + 1, c)}))
        return {e for e in E if not (e & removed)}
    def paths(E, a, b):
        adj = {}
        for e in E:
            x, y = tuple(e); adj.setdefault(x, []).append(y); adj.setdefault(y, []).append(x)
        out = []
        def go(v, seen):
            if v == b: out.append(list(seen)); return
            for w in adj.get(v, []):
                if w not in seen: go(w, seen + [w])
        go(a, [a]); return out
    centre = {(1, 1)}
    E = edges({'across', 'along'}, centre)
    left, right = (1, 0), (1, 2)
    P = paths(E, left, right)
    kind = lambda x, y: 'across' if x[0] == y[0] else 'along'
    ok = len(pos) - 1 == 8 and len(P) == 2
    ok &= all(sorted(kind(p[i], p[i + 1]) for i in range(len(p) - 1)) == ['across', 'across', 'along', 'along'] for p in P)
    deg = {}
    for e in E:
        for v in e: deg[v] = deg.get(v, 0) + 1
    ok &= len(deg) == 8 and all(d == 2 for d in deg.values())          # the eight form one ring
    ok &= paths(edges({'across'}, centre), left, right) == []
    ok &= paths(edges({'across', 'along'}, {(0, 1), (1, 1), (2, 1)}), left, right) == []
    return ok

def W100():
    with zipfile.ZipFile(KIT_ZIP) as z:
        name = next(n for n in z.namelist() if n.endswith('/resolver.py'))
        kit = ast.parse(z.read(name).decode())
    body = lambda t: [ast.dump(n) for n in t.body if not isinstance(n, ast.Expr)]
    return body(kit) == body(TREE) and len(body(TREE)) == 4


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'W\d+', k) and callable(v)}

if __name__ == '__main__':
    res = {}
    for k in sorted(CHECKS, key=lambda s: int(s[1:])):
        try: res[k] = bool(CHECKS[k]())
        except Exception as e: res[k] = f'error: {e!r}'
        print(k, res[k])
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'ccl_two_check_results.json')
    json.dump(res, open(out, 'w'), indent=1)
