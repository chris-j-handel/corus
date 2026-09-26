"""Run checks for Exhibit THIRTY Part EIGHT, first third (8.1 FIVE to 8.7 ELEVEN),
against the resolver as a runnable file (resolver_v371.py beside this file).

Usage:  python3 ccl_o1_checks.py            -> prints each check and its result
        python3 ccl_o1_checks.py --runs     -> prints the run checks as JSON [{link, check}]
Each function named by a link id holds for that link's run standing. A function ending in
_probe shows the failure a nye link names (it returns True when the failure shows).
"""
import ast, json, math, os, random, re, sys, cmath
from fractions import Fraction
from itertools import product, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from resolver_v371 import _1_self_coupling as C, _9_other_releasing as R9, CONNECTORS, JOINS

SRC = open(os.path.join(HERE, 'resolver_v371.py')).read()
TREE = ast.parse(SRC)
K = 'k'
S = (1, -1)


def sgn(x):
    return (x > 0) - (x < 0)


def call(carry, offer):
    s, c = C(list(carry), list(offer))
    return s, c


def at(ret, key=K):
    """(surfaced sign or None, returned entry fields or None) at one key."""
    s, c = ret
    return dict(s).get(key), {e[0]: e[1:] for e in c}.get(key)


SIX_OFFERINGS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def reach():
    seen = {()}; todo = [()]
    while todo:
        st = todo.pop()
        base = [(K,) + st] if st else []
        for off in SIX_OFFERINGS:
            _, c = C(base, off)
            nxt = tuple(c[0][1:]) if c else ()
            if nxt not in seen:
                seen.add(nxt); todo.append(nxt)
    return seen


NINETEEN = reach()


def offerings(maxlen, key=K):
    for L in range(maxlen + 1):
        for seq in product((-1, 0, 1), repeat=L):
            yield [(key, v) for v in seq]


# ------------------------------------------------------------------ 8.1 FIVE
def G7():
    w = cmath.exp(2j * math.pi / 3)
    if abs(1 + w + w * w) > 1e-12:
        return False
    V, I, N = 230.0, 5.0, 3600
    def mean_p(phi):
        return sum((math.sqrt(2) * V * math.cos(2 * math.pi * n / N)) *
                   (math.sqrt(2) * I * math.cos(2 * math.pi * n / N - phi)) for n in range(N)) / N
    ok = True
    for phi in (0.0, math.pi / 2, math.pi, 0.3, 2.0, -1.1):
        ok &= abs(mean_p(phi) - V * I * math.cos(phi)) < 1e-6
    return ok and mean_p(0) > 0 and abs(mean_p(math.pi / 2)) < 1e-6 and mean_p(math.pi) < 0


def G9():
    return (440 == 8 * 55 == 3 * 146 + 2 == 4 * 110 and 55 == sum(range(1, 11)) == math.comb(11, 2))


def G12():
    rows = [((437, 438), (440, 440), (-3, -2), (3, 2)), ((443, 444), (440, 440), (3, 4), (3, 4)),
            ((439, 441), (440, 440), (-1, 1), (1, 1)), ((439, 442), (440, 440), (-1, 2), (1, 2)),
            ((437, 438), (440, 441), (-3, -3), (3, 3))]
    ok = abs(437 - 440) == abs(443 - 440) == 3
    for (a0, a1), (b0, b1), es, bs in rows:
        ok &= (a0 - b0, a1 - b1) == es and (abs(a0 - b0), abs(a1 - b1)) == bs
    for e in range(-40, 41):
        for d in range(-40, 41):
            b, b2 = abs(e), abs(e + d)
            ok &= b2 * b2 - b * b == d * (2 * e + d)
            if e and d and abs(d) < abs(e):
                ok &= sgn(b2 - b) == sgn(e * d)
    return ok


def G13():
    r = Fraction(3, 2) ** 12 / 2 ** 7
    cents = 1200 * math.log2(531441 / 524288)
    return (r == Fraction(3 ** 12, 2 ** 19) == Fraction(531441, 524288) and round(cents, 2) == 23.46
            and Fraction(432, 440) == Fraction(54, 55))


def G18():
    first = {m: call([(0, 1, m, 3)], [(0, 1)]) for m in (1, 7, -1)}
    ok = (first[1] == ([(0, 0)], [(0, 1, 1, 4)]) and first[7] == ([(0, 0)], [(0, 1, 7, 4)])
          and first[-1] == ([(0, 0)], []))
    second = {m: call(first[m][1], []) for m in (1, 7, -1)}
    return (ok and second[1] == ([(0, -1)], [(0, -1, -1, 0)]) and second[7] == ([(0, -1)], [(0, -1, -7, 0)])
            and second[-1] == ([], []))


def G20():
    V, I, N = 1.0, 1.0, 3600
    th = [2 * math.pi * n / N for n in range(N)]
    three = [sum(V * I * math.cos(t - 2 * math.pi * j / 3) ** 2 for j in range(3)) for t in th]
    quad = [V * I * (math.cos(t) ** 2 + math.sin(t) ** 2) for t in th]
    opp = [V * I * (math.cos(t) ** 2 + math.cos(t - math.pi) ** 2) for t in th]
    return (max(abs(x - 1.5 * V * I) for x in three) < 1e-12 and max(abs(x - V * I) for x in quad) < 1e-12
            and max(opp) - min(opp) > 1.9)


def G21():
    a = call([(K, 1, -1, 0), (K, 1, 1, 2)], [])
    b = call([(K, 1, -1, 0), (K, -1, 1, 1)], [])
    ok = a == ([(K, -1)], [(K, -1, -1, 0)]) and b == ([(K, 0)], [(K, -1, 1, 2)])
    rnd = random.Random(5)
    for _ in range(3000):
        carry = [(rnd.choice('kj'), rnd.choice(S), rnd.choice(S), rnd.randint(0, 4)) for _ in range(rnd.randint(0, 5))]
        off = [(rnd.choice('kjm'), rnd.choice((-1, 0, 1))) for _ in range(rnd.randint(0, 5))]
        _, c = call(carry, off)
        ok &= len({e[0] for e in c}) == len(c)
    return ok


def G22():
    rnd = random.Random(7)
    ok = True
    states = [st for st in NINETEEN]
    for _ in range(300):
        carry = []
        for key in 'kj':
            st = rnd.choice(states)
            if st:
                carry.append((key,) + st)
        off = [(rnd.choice('kj'), rnd.choice((-1, 0, 1))) for _ in range(rnd.randint(1, 5))]
        s0, c0 = call(carry, off)
        for perm in set(permutations(off)):
            s, c = call(carry, list(perm))
            ok &= dict(s) == dict(s0) and sorted(c) == sorted(c0)
            order = []
            for key, v in list(perm):
                if v != 0 and key not in order:
                    order.append(key)
            for e in carry:
                if e[0] not in order:
                    order.append(e[0])
            ok &= [x[0] for x in s] == order
    return ok


def G29():
    return (72 + 1 == 73 == (59 - 2) + 16 and 146 == 2 * 73 == 144 + 2 and 3 * 146 == 438
            and 438 + 1 + 1 == 440 and 3 * 120 == 360 == 8 * math.comb(10, 2)
            and 440 - 360 == 3 * (146 - 120) + 2 == 3 * 26 + 2 == 80 == 16 * 5
            and math.comb(5, 2) == 10 == 5 + 5 and 12 * 10 == 120)


def G30():
    ok = True
    for N in range(1, 65):
        ring = {(i, (i + 1) % N) for i in range(N)} if N > 2 else ({(0, 1), (1, 0)} if N == 2 else {(0, 0)})
        chain = {(i, i + 1) for i in range(N - 1)}
        ok &= len(chain) == N - 1 and (N < 3 or len(ring) == N)
        for k in range(N + 1):
            ok &= (N - k) + k == N
        if N % 2 == 0:
            for k in range(N):
                o = (k + N // 2) % N
                ok &= min((o - k) % N, (k - o) % N) == N // 2
    return ok


# ------------------------------------------------------------------ 8.2 SIX
def T5_probe():
    empty_alike = all(call([], [(K, s)] * n) == call([], [(K, s)]) for s in S for n in range(1, 8))
    parted = False
    for st in NINETEEN:
        if not st:
            continue
        c = st[0]
        one, seven = call([(K,) + st], [(K, c)]), call([(K,) + st], [(K, c)] * 7)
        parted |= at(one)[0] == 0 and at(seven)[0] == c
    return empty_alike and parted


def T9():
    ok = all(call([(K,) + st] if st else [], [(K, 0)]) == call([(K,) + st] if st else [], []) for st in NINETEEN)
    sA, _ = call([], [(K, 1), (K, -1)])
    relA = R9(sA, {K: K})
    sB, cB = call([], relA)
    relB = R9(sB, {K: K})
    sC, cC = call([], relB)
    return ok and sA == [(K, 0)] and relA == [(K, 0)] and sB == [] and cB == [] and sC == [] and cC == []


def _fn(name):
    return next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == name)


def _loads_within(fn):
    args = {a.arg for a in fn.args.args}
    stored = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
    loads = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    builtins = set(dir(__builtins__)) if not isinstance(__builtins__, dict) else set(__builtins__)
    return loads - args - stored - builtins, args


def T14():
    no_import = not any(isinstance(n, (ast.Import, ast.ImportFrom)) for n in ast.walk(TREE))
    out1, a1 = _loads_within(_fn('_1_self_coupling'))
    out9, a9 = _loads_within(_fn('_9_other_releasing'))
    return (no_import and a1 == {'_3_self_carrying', '_2_self_offering'}
            and a9 == {'_10_other_surfacing', '_5_other_neutralling'} and not out1 and not out9)


# ------------------------------------------------------------------ 8.3 SEVEN
def S10():
    ok = True
    for p in range(1, 61):
        for q in range(1, 61):
            meet = next(n for n in range(1, p * q + 1) if n % p == 0 and n % q == 0)
            ok &= meet == math.lcm(p, q) and ((meet == p * q) == (math.gcd(p, q) == 1))
    return ok


def S15():
    J = list(product(S, S))
    R = lambda s: (s[1], -s[0]); L = lambda s: (-s[1], s[0])
    rep = lambda f, n, s: s if n == 0 else rep(f, n - 1, f(s))
    return all(rep(L, 3, s) == R(s) and rep(R, 3, s) == L(s) and rep(R, 3, rep(L, 3, s)) == s
               and rep(L, 4, s) == s and L(s) != R(s) for s in J)


def S19():
    return 5 ** 2 - 4 * 6 == 1 and 4 * 6 == 24


def _primes(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def S20():
    P = _primes(70)
    span = [p for p in P if 5 <= p <= 53]
    gaps = [b - a for a, b in zip(P, P[1:])]
    first6 = next(i for i, g in enumerate(gaps) if g == 6)
    both = {p: (p - P[P.index(p) - 1], P[P.index(p) + 1] - p) for p in span}
    return (len(span) == 14 and span[:7] == [5, 7, 11, 13, 17, 19, 23] and span[7:] == [29, 31, 37, 41, 43, 47, 53]
            and gaps[:9] == [1, 2, 2, 4, 2, 4, 2, 4, 6] and (P[first6], P[first6 + 1]) == (23, 29)
            and [p for p in span if both[p] == (2, 2)] == [5] and [p for p in span if both[p] == (6, 6)] == [53]
            and max(max(g) for g in both.values()) == 6)


def S23():
    return all((8 - k) * (8 + k) == 64 - k * k for k in range(9)) and 7 * 9 == 63 and 6 * 10 == 60 and 8 * 8 == 64


# ------------------------------------------------------------------ 8.4 EIGHT
def K5():
    return T14()


def K24():
    ok = all(-(-x) == x for x in range(-50, 51))
    ok &= all(1 / (1 / Fraction(x, y)) == Fraction(x, y) for x in range(-9, 10) if x for y in range(1, 9))
    ok &= all(z.conjugate().conjugate() == z for z in (complex(a, b) for a in range(-3, 4) for b in range(-3, 4)))
    rnd = random.Random(3)
    for _ in range(50):
        M = [[rnd.randint(-9, 9) for _ in range(4)] for _ in range(3)]
        T = [list(r) for r in zip(*M)]
        ok &= [list(r) for r in zip(*T)] == M
    U = set(range(20))
    for _ in range(50):
        A = {x for x in U if rnd.random() < 0.5}
        ok &= U - (U - A) == A
    f = lambda x: x ** 4 / 4 + x ** 2 / 2
    def xp(p):  # solve x^3 + x = p
        x = 0.0
        for _ in range(80):
            x -= (x ** 3 + x - p) / (3 * x * x + 1)
        return x
    fstar = lambda p: p * xp(p) - f(xp(p))
    ps = [i / 1000 for i in range(-40000, 40001)]
    fs = [fstar(p) for p in ps]
    for x0 in (-2.0, -0.7, 0.0, 0.4, 1.5):
        fss = max(x0 * p - v for p, v in zip(ps, fs))
        ok &= abs(fss - f(x0)) < 1e-5
    return ok


def K26_probe():
    sample = {Fraction(a, b) for a in range(-12, 13) if a for b in range(1, 13)}
    fixed = {x for x in sample if 1 / x == x}
    return fixed == {Fraction(1), Fraction(-1)}


def K27():
    return all(-s != s for s in S) and [x for x in range(-50, 51) if -x == x] == [0] and 0 not in S


# ------------------------------------------------------------------ 8.5 NINE
def H4():
    N = 10000
    share = [min(Fraction(i, N), 1 - Fraction(i, N)) for i in range(N + 1)]
    best = max(share)
    return best == Fraction(1, 2) and [i for i, v in enumerate(share) if v == best] == [N // 2]


def H22():
    rnd = random.Random(11)
    for _ in range(10000):
        bal = {}
        for _ in range(rnd.randint(1, 8)):
            amt = rnd.randint(1, 10 ** 6)
            dr, cr = rnd.sample('ABCDEFG', 2)
            bal[dr] = bal.get(dr, 0) + amt
            bal[cr] = bal.get(cr, 0) - amt
        if sum(bal.values()) != 0:
            return False
    return True


def H24_probe():
    m1 = Fraction(0 + 1, 2); m2 = Fraction(1 + 1, 2)
    return m1 not in (0, 1) and m2 in (1,)


# ------------------------------------------------------------------ 8.6 TEN
def A10():
    def omega(n, deltas):
        return n - max(deltas)
    ala = (18, [9, 12, 15])
    ok = omega(*ala) == 3
    n, d = ala
    for step in (2, 4):
        ok &= omega(n + step, [x + step for x in d]) == 3
    ok &= omega(18, [9, 12]) == 6 and omega(18, [9]) == 9
    ok &= all(b - a == 3 for a, b in zip(d, d[1:]))
    fam = [3, 6, 9]
    return ok and [f % 2 for f in fam] == [1, 0, 1] and fam[1] - fam[0] == fam[2] - fam[1] == 3


# ------------------------------------------------------------------ 8.7 ELEVEN
def D2():
    ok = True; cases = 0
    for st in NINETEEN:
        if not st:
            continue
        c, t, a = st
        for off in offerings(4):
            cases += 1
            s, e = at(call([(K,) + st], off))
            elig = a + 1 <= 3 or (a + 1 == 4 and t > 0)
            if s:
                ok &= e == (s, -t, 0)
            else:
                ok &= s == 0 and (e == (c, t, a + 1) if elig else e is None)
    return ok and cases == 18 * 121


def D3():
    ok = True
    for c, t in product(S, S):
        st = (c, t, 0)
        for _ in range(12):
            s, e = at(call([(K,) + st], [(K, c), (K, c)]))
            ok &= s == c and e is not None and e[2] == 0
            st = e
        carry = [(K, c, t, 0)]; opens = []
        for _ in range(12):
            ret = call(carry, [(K, c)])
            s, e = at(ret)
            opens.append((s, None if e is None else e[2]))
            carry = ret[1]
        top = 4 if t > 0 else 3
        want = [(0, a) for a in range(1, top + 1)] + [(0, None), (c, 0)]
        ok &= opens[:len(want)] == want
    return ok


def D5():
    fn = _fn('_1_self_coupling')
    parents = {}
    for node in ast.walk(fn):
        for ch in ast.iter_child_nodes(node):
            parents[ch] = node
    zeros = []
    for node in ast.walk(fn):
        if (isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Subscript)
                and getattr(node.targets[0].value, 'id', None) == '_11_other_chaining'
                and isinstance(node.value, ast.Tuple) and isinstance(node.value.elts[2], ast.Constant)
                and node.value.elts[2].value == 0):
            zeros.append(node)
    if len(zeros) != 1:
        return False
    p = parents[zeros[0]]
    cond = isinstance(p, ast.If) and isinstance(p.test, ast.Compare) and isinstance(p.test.ops[0], ast.NotEq)
    loop = parents[p]
    over_surfacing = isinstance(loop, ast.For) and getattr(loop.iter, 'id', None) == '_10_other_surfacing'
    ok = cond and over_surfacing
    for c, t in product(S, S):
        for _ in range(50):
            s, e = at(call([(K, c, t, 0)], [(K, c)]))
            ok &= s == 0 and e == (c, t, 1)
    return ok


def D6():
    ok = True
    for st in NINETEEN:
        base = [(K,) + st] if st else []
        cc = st[0] if st else 0
        seen = {}
        for off in offerings(4):
            tot = sum(sgn(v) for _, v in off)
            met = bool(st) or any(v for _, v in off)
            key = (sgn(tot - cc), met)
            r = call(base, off)
            if key in seen:
                ok &= seen[key] == r
            else:
                seen[key] = r
    return ok


def D14():
    together = call([], [(K, 1), (K, -1)])
    s1, c1 = call([], [(K, 1)])
    s2, c2 = call(c1, [(K, -1)])
    return together == ([(K, 0)], []) and s1 == [(K, 1)] and s2 == [(K, -1)] and c2 == [(K, -1, 1, 0)]


def D19():
    X = range(6)
    pairs = [(a, b) for a in X for b in X]
    diag = [p for p in pairs if p[0] == p[1]]
    ok = len(pairs) == 36 and len(diag) == 6 and len(pairs) - len(diag) == 30
    perms = list(permutations(range(4)))
    ok &= len(perms) == 24 == math.factorial(4)
    for chosen in perms:
        ok &= sum(1 for p in perms if p != chosen) == 23
    return ok


def D24():
    ok = True
    for t1, t2 in product(S, S):
        for a1 in range(5):
            for a2 in range(5):
                s, _ = at(call([(K, 1, t1, a1), (K, -1, t2, a2)], []))
                ok &= s == 0
    return ok


def D25():
    ok = call([], []) == ([], [])
    for st in NINETEEN:
        if not st:
            continue
        for off in SIX_OFFERINGS:
            _, e = at(call([(K,) + st], off))
            ok &= e != st
            if e is not None and e[2] == st[2] + 1:
                ok &= e[:2] == st[:2]
            elif e is not None:
                ok &= e[2] == 0 and e[1] == -st[1]
    return ok


def D29():
    phi = (1 + 5 ** 0.5) / 2
    P = _primes(59)
    return all(abs((1 / phi) ** q / (1 / phi) ** p - (1 / phi) ** (q - p)) < 1e-12 for p, q in zip(P, P[1:]))


def D34():
    rnd = random.Random(13)
    return all((a + d) - (b + d) == a - b for a, b, d in
               ((Fraction(rnd.randint(-999, 999), 10), Fraction(rnd.randint(-999, 999), 10),
                 Fraction(rnd.randint(-999, 999), 10)) for _ in range(10000)))


def C_without_list(carry, offer):
    """1-self-coupling with 12-other-surplusing summed straight, no 14-social-crossing list built."""
    crossing = {k: t for k, c, t, a in carry}
    surplus = {}
    for k, c in offer:
        if c > 0: surplus[k] = surplus.get(k, 0) + 1
        if c < 0: surplus[k] = surplus.get(k, 0) - 1
    for k, c, t, a in carry:
        if c > 0: surplus[k] = surplus.get(k, 0) - 1
        if c < 0: surplus[k] = surplus.get(k, 0) + 1
    surfacing = [(k, sgn(v)) for k, v in surplus.items()]
    chaining = {}
    for k, c, t, a in carry:
        if a + 1 <= 3 or (a + 1 == 4 and t > 0):
            chaining[k] = (c, t, a + 1)
    for k, s in surfacing:
        if s != 0:
            chaining[k] = (s, 0 - crossing.get(k, 1), 0)
    return surfacing, [(k, c, t, a) for k, (c, t, a) in chaining.items()]


def D36():
    ok = True; n = 0
    states = sorted(NINETEEN)
    for st1 in states:
        for st2 in states:
            carry = ([('k',) + st1] if st1 else []) + ([('j',) + st2] if st2 else [])
            for L in range(3):
                for seq in product([('k', 1), ('k', -1), ('k', 0), ('j', 1), ('j', -1)], repeat=L):
                    n += 1
                    ok &= C(list(carry), list(seq)) == C_without_list(list(carry), list(seq))
    return ok and n == 361 * 31


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'[GTSKHAD]\d+(_probe)?', k) and callable(v)}

RUNS = [
    {"link": "G7", "check": "abs(1 + w + w^2) < 1e-12 at w = exp(2*pi*i/3); the mean over 3,600 steps of a cycle of (sqrt2 V cos th)(sqrt2 I cos(th - phi)) equals V I cos phi within 1e-6 at six phases, positive at phi = 0, zero at pi/2, negative at pi."},
    {"link": "G9", "check": "440 == 8*55 == 3*146 + 2 == 4*110 and 55 == 1 + ... + 10 == C(11, 2)."},
    {"link": "G12", "check": "The file's five tone rows give its signed differences and beat rates; for integer e, d in -40..40, b'^2 - b^2 == d(2e + d) with b = |e|, b' = |e + d|, and sign(b' - b) == sign(e d) whenever e, d nonzero and |d| < |e|."},
    {"link": "G13", "check": "(3/2)^12 / 2^7 == 3^12 / 2^19 == 531441/524288; 1200 log2 of it rounds to 23.46; 432/440 == 54/55."},
    {"link": "G18", "check": "_1_self_coupling([(0, 1, m, 3)], [(0, 1)]) returns ([(0, 0)], [(0, 1, m, 4)]) at m = 1 and 7 and ([(0, 0)], []) at m = -1; each returned carrying under an empty offering returns ([(0, -1)], [(0, -1, -m, 0)]) at m = 1 and 7 and ([], []) at m = -1."},
    {"link": "G20", "check": "Over 3,600 steps: the three-phase sum of VI cos^2(th - 2 pi j/3) stays 3VI/2 within 1e-12, two phases in quadrature stay VI, and two opposed by half a cycle range from 0 to 2VI."},
    {"link": "G21", "check": "Carrying [(k, +1, -1, 0), (k, +1, +1, 2)] under an empty offering returns ([(k, -1)], [(k, -1, -1, 0)]); [(k, +1, -1, 0), (k, -1, +1, 1)] returns ([(k, 0)], [(k, -1, +1, 2)]); 3,000 random carryings with repeated keys return each key once."},
    {"link": "G22", "check": "300 random carryings from the nineteen at two keys, each under every ordering of a random offering of up to five signs: the surfacing (as a map) and the carrying (as a set) stay the same, and the surfaced list follows the order keys first meet a nonzero sign in the offering, then the carried keys."},
    {"link": "G29", "check": "72 + 1 == 73 == (59 - 2) + 16; 146 == 2*73 == 144 + 2; 3*146 == 438; 438 + 2 == 440; 3*120 == 360 == 8*C(10, 2); 440 - 360 == 3*26 + 2 == 80 == 16*5; C(5, 2) == 10 == 5 + 5; 12*10 == 120."},
    {"link": "G30", "check": "For N from 1 to 64: a chain has N - 1 connections and a simple ring N (N >= 3); k and N - k sum to N; at even N, stations k and (k + N/2) mod N stand N/2 apart both ways."},
    {"link": "T9", "check": "At each of the nineteen carryings an offering [(k, 0)] returns what [] returns; a self offered (+, -) at empty carrying surfaces (k, 0), 9 releases (k, 0), a second self offered that release at empty carrying returns ([], []), and a third offered the second's release returns ([], [])."},
    {"link": "T14", "check": "The resolver file has no import; _1_self_coupling takes (_3_self_carrying, _2_self_offering) and _9_other_releasing (_10_other_surfacing, _5_other_neutralling); every name either function loads is an argument, a name it binds itself, or a builtin."},
    {"link": "S10", "check": "For p, q from 1 to 60 the first n >= 1 divisible by both equals lcm(p, q), and it equals p*q exactly when gcd(p, q) == 1."},
    {"link": "S15", "check": "On the four joint forms with R(x, y) = (y, -x) and L(x, y) = (-y, x): L^3 == R, R^3 == L, R^3 after L^3 is the identity, L^4 is the identity, and L differs from R at each form."},
    {"link": "S19", "check": "5^2 - 4*6 == 1 and 4*6 == 24."},
    {"link": "S20", "check": "The primes from 5 to 53 are fourteen: 5..23 seven and 29..53 seven; the gaps from 2 run 1, 2, 2, 4, 2, 4, 2, 4, 6, the first six at 23 -> 29; within 5..53 only 5 has gaps (2, 2) on both sides and only 53 has (6, 6), six being the widest gap met."},
    {"link": "S23", "check": "(8 - k)(8 + k) == 64 - k^2 for k from 0 to 8; 7*9 == 63, 6*10 == 60, 8*8 == 64."},
    {"link": "K5", "check": "The same tree check as T14: no import, and each function loads only its own two arguments, names it binds, and builtins."},
    {"link": "K24", "check": "Applied twice each returns its argument: negation on -50..50, the multiplicative inverse on nonzero fractions, complex conjugation on a grid, the transpose on 50 random 3x4 matrices, set complement on 50 random subsets of 20; the Legendre transform of f(x) = x^4/4 + x^2/2 taken twice (numerically, p-grid step 0.001 over [-40, 40]) returns f at five points within 1e-5."},
    {"link": "K27", "check": "-s != s at s = +1 and -1; among the integers -50..50 only 0 has -x == x, and 0 is no sign."},
    {"link": "H4", "check": "Over 10,001 cuts x = i/10000, the cutter's share min(x, 1 - x) (the chooser taking the larger) is greatest, 1/2, at x = 1/2 alone."},
    {"link": "H22", "check": "10,000 random ledgers of one to eight entries, each entry debiting one account and crediting another the same amount: every trial balance sums to zero."},
    {"link": "A10", "check": "omega = chain length - highest delta: 18:3 at delta 9, 12, 15 is omega-3, and elongated by 2 or 4 carbons at the carboxyl end (each delta + 2 or + 4) stays omega-3; 18:2 (9, 12) is omega-6, 18:1 (9) omega-9; the double bonds stand three apart and 3, 6, 9 read odd, even, odd."},
    {"link": "D2", "check": "Each of the eighteen nonempty carryings at one key under each of the 121 offerings of up to four signs from -1, 0, +1: at a nonzero surfacing s the entry returns (s, -t, 0); at a 0 surfacing it returns (c, t, a + 1) within the bound and is gone past it."},
    {"link": "D3", "check": "From (c, t, 0), each (c, t): two c at each of 12 calls surface c each time with the returned opening 0; one c at each call surfaces 0 with openings 1, 2, 3 (and 4 at t > 0), then 0 with the key empty, then c with opening 0."},
    {"link": "D5", "check": "In _1_self_coupling's tree one assignment only writes an 11-other-chaining entry with opening 0, under `if _7_other_corusing != 0` in the loop over _10_other_surfacing; a caller re-seeding (c, t, 0) under one c at each of 50 calls gets (c, t, 1) back each time."},
    {"link": "D6", "check": "At each of the nineteen carryings, the 121 offerings of up to four signs grouped by the sign of (their signed total less the carried sign) and by whether any sign meets the key: within each group the whole return (surfacing and carrying) is identical."},
    {"link": "D14", "check": "_1_self_coupling([], [(k, +1), (k, -1)]) returns ([(k, 0)], []); + then - at two calls surface + and then - and return [(k, -1, +1, 0)]."},
    {"link": "D19", "check": "A six-set has 36 ordered pairs, 6 on the diagonal and 30 off it; four things have 4! = 24 matchings, and for each chosen one 23 others differ."},
    {"link": "D24", "check": "Carrying (k, +1, t1, a1) and (k, -1, t2, a2) at one key, with nothing arriving, surfaces (k, 0) at each t1, t2 in {+1, -1} and a1, a2 in 0..4."},
    {"link": "D25", "check": "_1_self_coupling([], []) returns ([], []); each of the eighteen nonempty carryings under each of the six offerings returns an entry differing from the one given: a continuing keeps sign and second sign and opens by one, a fresh write opens at 0 with the second sign inverted."},
    {"link": "D29", "check": "With phi = (1 + sqrt5)/2, for each pair of neighbouring primes p < q up to 59, (1/phi)^q / (1/phi)^p equals (1/phi)^(q - p) within 1e-12."},
    {"link": "D34", "check": "(a + d) - (b + d) == a - b over 10,000 random rationals a, b, d."},
    {"link": "D36", "check": "A copy of _1_self_coupling summing 12-other-surplusing straight from the offering and the carrying, building no 14-social-crossing list, returns exactly what the resolver returns at 361 carryings over two keys (each key one of the nineteen) under each of the 31 offerings of up to two signs from (k, +1), (k, -1), (k, 0), (j, +1), (j, -1)."},
]


if __name__ == '__main__':
    if '--runs' in sys.argv:
        print(json.dumps(RUNS, indent=1)); sys.exit(0)
    order = lambda s: ('GTSKHAD'.index(s[0]), int(re.match(r'[A-Z](\d+)', s).group(1)))
    res = {}
    for k in sorted(CHECKS, key=order):
        try:
            res[k] = bool(CHECKS[k]())
        except Exception as e:
            res[k] = f'error: {e!r}'
        print(k, res[k])
    missing = [r['link'] for r in RUNS if r['link'] not in CHECKS]
    print('runs listed without a function:', missing or 'none')
