"""Run checks for Exhibit THIRTY Part THREE · NUMBERS (links N1...), against Exhibit THREE v372
(/home/claude/work/Exhibit_THREE_Natural_Numbers_v372.md) and the resolver of Exhibit ONE v372
(resolver_v372.py beside this file). Each function is named for its link and returns True when it holds.
Polynomial identities are checked at more points than their degree, so they hold at each value.
Run: python3 ccl_num_checks.py [results.json]"""
import ast, json, os, re, sys, math
from fractions import Fraction as Q
from itertools import product, combinations, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as R, CONNECTORS, JOINS

K = 'k'
S = (1, -1)
CODE = open(os.path.join(HERE, 'resolver_v372.py')).read()
TREE = ast.parse(CODE)


def poly_identity(f, g, deg, pts=None):
    """f == g as polynomials of degree <= deg in one variable: equal at deg + 2 or more points."""
    pts = pts or range(-deg - 3, deg + 40)
    return all(f(Q(x)) == g(Q(x)) for x in pts)


def primes_below(n):
    s = [True] * n; s[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = [False] * len(s[i * i::i])
    return [i for i, v in enumerate(s) if v]


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


P17 = primes_below(60)
T = lambda k: k * (k + 1) // 2


class QR:
    """a + b*sqrt(d), a, b rational: exact arithmetic in Q(sqrt d)."""
    def __init__(s, a, b, d): s.a, s.b, s.d = Q(a), Q(b), d
    def __add__(s, o): o = s._c(o); return QR(s.a + o.a, s.b + o.b, s.d)
    def __sub__(s, o): o = s._c(o); return QR(s.a - o.a, s.b - o.b, s.d)
    def __neg__(s): return QR(-s.a, -s.b, s.d)
    def __mul__(s, o): o = s._c(o); return QR(s.a * o.a + s.d * s.b * o.b, s.a * o.b + s.b * o.a, s.d)
    def inv(s): n = s.a * s.a - s.d * s.b * s.b; return QR(s.a / n, -s.b / n, s.d)
    def __truediv__(s, o): return s * s._c(o).inv()
    def __eq__(s, o): o = s._c(o); return s.a == o.a and s.b == o.b
    def _c(s, o): return o if isinstance(o, QR) else QR(o, 0, s.d)
    def __float__(s): return float(s.a) + float(s.b) * math.sqrt(s.d)


PHI = QR(Q(1, 2), Q(1, 2), 5)


# ------------------------------------------------------------------ ONE · UNI-SCALING
def N3():
    # at n the momentary (n-1, n) completes and (n, n+1) opens; the side is the parity of its opening
    side = lambda opening: 'self' if opening % 2 else 'other'
    return all(side(n - 1) != side(n) and (n - 1) % 2 != n % 2 for n in range(2, 1001))


def N5():
    def ten(o):  # self's five from o, other's five from o + 1
        s5 = list(range(o, o + 5)); t5 = list(range(o + 1, o + 6))
        return s5, t5, list(zip(s5, t5))
    s1, t1, p1 = ten(1); s3, t3, p3 = ten(3)
    full = [(1, 2), (3, 4), (5, 6)]
    cover = sorted({x for m in full for x in m}) == sorted(set(s1) | set(t1))
    same = [(a - 2, b - 2) for a, b in p3] == p1 and all((a + b) % 2 for a, b in p3)
    within = set(s3) | set(t3) <= set(range(1, 10))
    part = [(1, 2), (3, 4)] + [(2, 3), (4, 5)]
    return cover and same and within and all(m in [(k, k + 1) for k in range(1, 9)] for m in part + [(5, 6)])


def N6():
    moms = [(k, k + 1) for k in range(1, 9)]
    exh = {x for m in moms for x in m} == set(range(1, 10))
    det = all(sum(1 for m2 in moms if m2[0] == m[1]) == 1 for m in moms[:-1])
    reach = all({m2[0] for m2 in moms if m2[0] >= m[1]} | {9} >= set(range(m[1], 10)) for m in moms)
    self_only = [m for m in moms if m[0] % 2]
    det_fails = any(not any(m2[0] == m[1] for m2 in self_only) for m in self_only)
    return exh and det and reach and det_fails


def N7():
    ok = sum([1, 3, 5]) == 9 and sum([2, 4, 6]) == 12
    ok &= poly_identity(lambda n: n * n - (n - 1) * (n - 1), lambda n: 2 * n - 1, 2)          # step of the square
    ok &= poly_identity(lambda n: n * (n + 1) - (n - 1) * n, lambda n: 2 * n, 2)               # step of the oblong
    ok &= all(sum(2 * k - 1 for k in range(1, n + 1)) == n * n and sum(2 * k for k in range(1, n + 1)) == n * (n + 1)
              for n in range(1, 1001))
    return ok


def N8():
    return poly_identity(lambda n: (n - 1) * (n + 1), lambda n: n * n - 1, 2)


def N9():
    ok = poly_identity(lambda n: (n - 3) * (n + 3), lambda n: n * n - 9, 2)
    ok &= all((n - k) * (n + k) == n * n - k * k for n in range(0, 200) for k in range(0, 50))
    return ok and 23 * 25 == 24 ** 2 - 1


F8 = lambda n: n + 8
F17 = lambda n: 17 - n
F9 = lambda n: 9 - n


def N11():
    ok = all(F8(n) - 8 == n for n in range(1, 10)) and all(F17(F17(n)) == n for n in range(1, 17)) \
        and all(F9(F9(n)) == n for n in range(1, 9))
    # alternating 8 up/down with 17 less runs round within 1..16
    def up_down(n): return n + 8 if n <= 8 else n - 8
    for n in range(1, 17):
        seen = [n]; x = n
        for i in range(4):
            x = up_down(x) if i % 2 == 0 else F17(x)
            seen.append(x)
        ok &= seen[-1] == n and len(set(seen[:4])) == 4 and all(1 <= y <= 16 for y in seen)
    # 9 less (within 1..8) alternated with 8 up or with 17 less leaves 1..8 at the next step, outside 9 less
    for n in range(1, 9):
        ok &= 9 <= F8(F9(n)) <= 16 and 9 <= F17(F9(n)) <= 16
    ok &= all(F17(F8(n)) == F9(n) for n in range(1, 9))
    return ok


def N12():
    rows = [[n, n + 8, 9 - n, 17 - n] for n in range(1, 5)]
    ok = rows == [[1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]]
    for r in rows:
        steps = [(r[i], r[(i + 1) % 4]) for i in range(4)]
        changes = [(a, b) for a, b in steps if a % 2 != b % 2]
        ok &= len(changes) == 2 and all(a + b == 17 for a, b in changes)
        p = [x % 2 for x in r]
        ok &= sum(p[i] != p[i - 1] for i in range(4)) == 2 and 17 not in r
    ok &= Q(17, 2) == Q(17, 2) and all(n != 17 - n for n in range(1, 17))  # 17 less fixes no name: its centre is 8½
    return ok


def N15():
    ok = True
    for n in range(1, 1000):
        a = sum(x % 2 for x in (n, n + 1, n + 2)); b = sum(x % 2 for x in (n + 1, n + 2, n + 3))
        ok &= {a, b} == {1, 2}
    return ok and [x % 2 for x in (23, 24, 25)] == [1, 0, 1] and [x % 2 for x in (24, 25, 26)] == [0, 1, 0]


def N20():
    ok = True
    for N in range(2, 201):
        for k in range(N):
            met = len({(k * i) % N for i in range(N)})
            ok &= met == N // math.gcd(N, k)
        if is_prime(N):
            ok &= all(len({(k * i) % N for i in range(N)}) == N for k in range(1, N))
    ok &= len({(2 * i) % 9 for i in range(9)}) == 9 and not is_prime(9)
    return ok


def N22():
    ok = 2 * 3 - (2 + 3) == 1 and 2 + 3 == 5 and 2 * 3 == 6
    self4 = set(range(1, 5)); other4 = set(range(2, 6))
    shared = self4 & other4; outer = self4 ^ other4
    ok &= len(shared) == 3 and len(outer) == 2 and len(self4 | other4) == 5
    ok &= 2 * len(shared) == 6 and len(self4) + len(other4) == 2 * 3 + 2
    ok &= 2 + 2 == 2 * 2 == 4 and 3 + 3 == 6 and 3 * 3 == 9
    return ok


# ------------------------------------------------------------------ TWO · CORUSING
def N28():
    p3 = PHI * PHI * PHI
    ok = p3 - p3.inv() == QR(4, 0, 5)
    ok &= math.comb(11, 2) == T(10) == 55
    f = [0, 1]
    while len(f) < 12: f.append(f[-1] + f[-2])
    return ok and f[10] == 55 and N8()


def N30():
    return sum(P17) == 440 and len(P17) == 17 and 8 * 55 == 440 and 21 ** 2 - 1 == 440


# ------------------------------------------------------------------ THREE · UNRELATIONING
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a


def above_phi(x):  # x > 0 rational: x > phi iff x^2 - x - 1 > 0
    return x * x - x - 1 > 0


def N32():
    f = [fib(i) for i in range(1, 302)]  # 1, 1, 2, 3, 5, 8, ...
    ok = f[:7] == [1, 1, 2, 3, 5, 8, 13] and all(f[i] == f[i - 1] + f[i - 2] for i in range(2, len(f)))
    sides = [above_phi(Q(f[i + 1], f[i])) for i in range(1, 300)]  # 2/1, 3/2, 5/3, ...
    ok &= sides[:4] == [True, False, True, False]
    ok &= all(sides[i] != sides[i + 1] for i in range(len(sides) - 1))
    ok &= all(Q(f[i + 1], f[i]) * Q(f[i + 1], f[i]) - Q(f[i + 1], f[i]) - 1 != 0 for i in range(1, 300))
    # the side at each n: M^n = [[F(n+1), F(n)], [F(n), F(n-1)]] and det M = -1, so det M^n = (-1)^n
    M = [[1, 1], [1, 0]]; P = [[1, 0], [0, 1]]
    for n in range(1, 301):
        P = [[P[0][0] * M[0][0] + P[0][1] * M[1][0], P[0][0] * M[0][1] + P[0][1] * M[1][1]],
             [P[1][0] * M[0][0] + P[1][1] * M[1][0], P[1][0] * M[0][1] + P[1][1] * M[1][1]]]
        ok &= P == [[fib(n + 1), fib(n)], [fib(n), fib(n - 1)]] and P[0][0] * P[1][1] - P[0][1] * P[1][0] == (-1) ** n
    return ok


def N33():
    ok = PHI * PHI == PHI + 1
    other = -(PHI.inv())
    ok &= other * other == other + 1 and PHI - PHI.inv() == QR(1, 0, 5) and PHI * other == QR(-1, 0, 5)
    ok &= PHI == QR(1, 0, 5) + PHI.inv()  # phi = 1 + 1/phi: continued fraction all ones
    ok &= math.floor(float(PHI)) == 1
    # pentagon: diagonal over side
    V = [(math.cos(2 * math.pi * k / 5), math.sin(2 * math.pi * k / 5)) for k in range(5)]
    d = math.dist(V[0], V[2]); s = math.dist(V[0], V[1])
    return ok and abs(d / s - float(PHI)) < 1e-12


def N35():
    ok = True
    for n in range(1, 51):
        d = n * n + 4
        x = QR(Q(n, 2), Q(1, 2), d)
        ok &= x * x == x * QR(n, 0, d) + 1 and x == QR(n, 0, d) + x.inv()
        ok &= math.floor(float(x)) == n and 0 < float(x.inv()) < 1
    return ok and QR(Q(1, 2), Q(1, 2), 5) == PHI


def N37():
    # p/q closes at q turns; x^2 - x - 1 has no rational root (candidates +1, -1 give -1 and 1), so k*phi is never whole
    ok = all((q * Q(p, q)).denominator == 1 for p in range(1, 30) for q in range(1, 30))
    ok &= (1 * 1 - 1 - 1) != 0 and ((-1) * (-1) + 1 - 1) != 0
    ok &= all(QR(0, 0, 5) != (PHI * k) - QR(m, 0, 5) for k in range(1, 200) for m in [math.floor(k * float(PHI))])
    return ok


# ------------------------------------------------------------------ FOUR · TORUSING
def N42():
    # at three edges to each vertex (3V = 2E) and sum of sides = 2E: sum(6 - f) = 6F - 2E = 6(V - E + F)
    ok = True
    for E in range(3, 300, 3):
        V = Q(2 * E, 3)
        for F in range(1, 200):
            ok &= 6 * F - 2 * E == 6 * (V - E + F)
    ok &= (12 - 30 + 20) == 2 and (20 - 30 + 12) == 2
    # dodecahedron: 12 five-folds, V 20, E 30; truncated icosahedron: 12 five-folds, 20 six-folds, V 60, E 90
    for fives, sixes, V, E in ((12, 0, 20, 30), (12, 20, 60, 90)):
        F = fives + sixes
        ok &= 3 * V == 2 * E == 5 * fives + 6 * sixes and V - E + F == 2 and sum([1] * fives) == 6 * 2
    # a torus of six-folds: the hexagonal torus, each vertex three edges, sum(6 - f) = 0 = 6 * 0
    for m in range(1, 8):
        F = m * m; E = 3 * F; V = 2 * F
        ok &= V - E + F == 0
    return ok


def N44():
    ok = 19 ** 2 - 1 == 360 == 8 * T(9) == 8 * math.comb(10, 2) and 45 == 5 * 9
    ok &= 21 ** 2 - 1 == 440 == 8 * T(10) and 440 - 360 == 80 == 9 ** 2 - 1 == 8 * T(4) == 8 * math.comb(5, 2)
    ok &= (360 + 80) % 440 == 0 and 21 - 19 == 2
    return ok


# ------------------------------------------------------------------ FIVE · UNIQUENESSING
def N47():
    return [6 + 8 * k for k in range(3)] == [6, 14, 22] and 17 <= 22 <= 25 and 22 > 17 and 9 <= 14 <= 17


def N48():
    con = sorted(CONNECTORS); internal = [n for n in range(2, 18) if n not in CONNECTORS]
    return (len(con) == 6 and len(internal) == 10 and 6 == 8 - 2 and 10 == 8 + 2
            and 6 // 2 == 3 and 10 // 2 == 5 and 8 // 2 == 4 and len(con) + len(internal) + 1 == 17)


OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]


def reach(Cf):
    seen = {()}; frontier = [()]; trans = []
    while frontier:
        nxt = []
        for st in frontier:
            for off in OFFERS:
                s, c = Cf([(K,) + st] if st else [], off)
                s2 = tuple(c[0][1:]) if c else ()
                trans.append((st, tuple(map(tuple, off)), tuple(s), s2))
                if s2 not in seen: seen.add(s2); nxt.append(s2)
        frontier = nxt
    return seen, trans


def N50():
    seen, trans = reach(C)
    ok = len(seen) == 19 and len(trans) == 114
    ok &= all(v in (-1, 0, 1) for _, _, s, _ in trans for _, v in s)
    ok &= all(st == () or (st[0] in S and st[1] in S) for st in seen)
    # take the numeral off each name, and separately permute the numerals: the 114 transitions stand as they were
    names = sorted({n.id for n in ast.walk(TREE) if isinstance(n, ast.Name) and re.match(r'_\d+_', n.id)} |
                   {a.arg for n in ast.walk(TREE) if isinstance(n, ast.FunctionDef) for a in n.args.args if re.match(r'_\d+_', a.arg)})
    stripped = {nm: re.sub(r'^_\d+_', '_', nm) for nm in names}
    nums = [int(re.match(r'_(\d+)_', nm).group(1)) for nm in names]
    perm = dict(zip(sorted(set(nums)), sorted(set(nums))[::-1]))
    permuted = {nm: re.sub(r'^_(\d+)_', lambda m: f'_{perm[int(m.group(1))] + 100}_', nm) for nm in names}
    for ren in (stripped, permuted):
        if len(set(ren.values())) != len(ren): return False
        src = re.sub(r'\b(' + '|'.join(map(re.escape, sorted(ren, key=len, reverse=True))) + r')\b',
                     lambda m: ren[m.group(1)], CODE)
        ns = {}; exec(src, ns)
        C2 = next(v for k, v in ns.items() if callable(v) and k.endswith('self_coupling'))
        seen2, trans2 = reach(C2)
        ok &= trans2 == trans
    return ok


def N52():
    fn = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
    inside = {n.id for n in ast.walk(fn) if isinstance(n, ast.Name)}
    return (set(CONNECTORS) & {2, 4, 6, 8}) == {2, 6} and '_4_self_sharing' in inside and '_8_other_torusing' in inside


def N53():
    ok = poly_identity(lambda k: (2 * k + 1) ** 2 - 1, lambda k: 8 * k * (k + 1) / 2, 2)
    ok &= [(2 * k + 1) ** 2 - 1 for k in range(11)] == [0, 8, 24, 48, 80, 120, 168, 224, 288, 360, 440]
    ok &= all((2 * k + 1) ** 2 - 1 == 8 * math.comb(k + 1, 2) for k in range(0, 200))
    return ok and 440 == 8 * 55 == 8 * math.comb(11, 2)


def N56():
    centres = [c for c in range(5, 10000) if all(is_prime(c + d) for d in (-4, -2, 2, 4))]
    return centres[:2] == [9, 15] and not is_prime(9) and not is_prime(15) and (5, 7, 11, 13) == (9 - 4, 9 - 2, 9 + 2, 9 + 4)


def N57():
    cells = [(r, c) for r in range(3) for c in range(3) if (r, c) != (1, 1)]
    adj = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1
    start, end = (1, 0), (1, 2)
    paths = []
    def dfs(p):
        if p[-1] == end: paths.append(list(p)); return
        for c in cells:
            if c not in p and adj(p[-1], c): dfs(p + [c])
    dfs([start])
    ok = len(paths) == 2 and {tuple(p[1]) for p in paths} == {(0, 0), (2, 0)}
    for p in paths:
        steps = list(zip(p, p[1:]))
        along = sum(1 for a, b in steps if a[0] == b[0]); across = sum(1 for a, b in steps if a[1] == b[1])
        ok &= along == 2 and across == 2
    return ok


def N58():
    ok = [x for x in range(-1000, 1001) if x == -x] == [0]
    ok &= all(F8(n) != 0 for n in range(1, 10)) and all(F17(n) != 0 for n in range(1, 17)) and all(F9(n) != 0 for n in range(1, 9))
    return ok


def N59():
    ok = 17 - 9 == 25 - 17 == 8
    forms = [[1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12], [9, 5, 12, 8], [7, 11, 6, 10],
             [1, 9, 5, 12, 8, 16], [2, 15, 7, 11, 6, 10], [3, 11, 7, 10, 6, 14], [4, 13, 5, 9, 8, 12],
             [1, 9, 5, 13, 4, 12, 8, 16], [2, 15, 7, 11, 3, 14, 6, 10]]
    ok &= not any(17 in f for f in forms) and 25 > 17
    spans = [(1, 9), (9, 17), (17, 25)]
    moms = 0
    for a, b in spans:
        self_m = [(k, k + 1) for k in range(a, b) if (k - a) % 2 == 0]
        other_m = [(k, k + 1) for k in range(a + 1, b) if (k - a) % 2 == 1]
        ok &= len(self_m) == 4 and len(other_m) == 4 and all((x + y) % 2 for x, y in self_m + other_m)
        moms += len(self_m) + len(other_m)
    ok &= moms == 24 and 25 - 1 == 24
    ok &= [n - 1 for n in (6, 14, 22)] == [5, 13, 21]
    return ok


def N60():
    sol = [n for n in range(1, 10001) if 2 * n == n * (n - 1) // 2 and n * (n - 1) % 2 == 0]
    ok = sol == [5] and poly_identity(lambda n: n * (n - 1) / 2 - 2 * n, lambda n: n * (n - 5) / 2, 2)
    return ok and 2 * 5 == math.comb(5, 2) == T(4) == 10


def ring_complement_is_ring(n):
    ring = {frozenset((i, (i + 1) % n)) for i in range(n)}
    comp = {frozenset(e) for e in combinations(range(n), 2)} - ring
    deg = {v: sum(1 for e in comp if v in e) for v in range(n)}
    if not all(d == 2 for d in deg.values()): return False
    # connected single cycle
    seen = {0}; stack = [0]
    while stack:
        v = stack.pop()
        for e in comp:
            if v in e:
                w = next(iter(e - {v}))
                if w not in seen: seen.add(w); stack.append(w)
    return len(seen) == n


def N61():
    return [n for n in range(3, 61) if ring_complement_is_ring(n)] == [5]


def mono_triangle(n, col):
    E = list(combinations(range(n), 2)); c = dict(zip(E, col))
    return any(c[(a, b)] == c[(a, d)] == c[(b, d)] for a, b, d in combinations(range(n), 3))


def N62():
    E6 = list(combinations(range(6), 2))
    ok = all(mono_triangle(6, col) for col in product((0, 1), repeat=len(E6)))
    E5 = list(combinations(range(5), 2))
    good = [col for col in product((0, 1), repeat=len(E5)) if not mono_triangle(5, col)]
    ok &= len(good) == 12
    for col in good:
        for colour in (0, 1):
            edges = [e for e, x in zip(E5, col) if x == colour]
            deg = [sum(1 for e in edges if v in e) for v in range(5)]
            seen = {0}; stack = [0]
            while stack:
                v = stack.pop()
                for e in edges:
                    if v in e:
                        w = e[0] if e[1] == v else e[1]
                        if w not in seen: seen.add(w); stack.append(w)
            ok &= len(edges) == 5 and deg == [2] * 5 and len(seen) == 5
    return ok


def N63():
    ok = True
    for a in range(0, 1001):
        pairs = [(a + j, a + 9 - j) for j in range(5)]
        ok &= all((x + y) % 2 == 1 for x, y in pairs) and all(Q(x + y, 2) == a + Q(9, 2) for x, y in pairs)
        odd_first = [x % 2 for x, _ in pairs]
        odd_next = [(x + 1) % 2 for x, _ in pairs]; odd_two = [(x + 2) % 2 for x, _ in pairs]
        ok &= all(u != v for u, v in zip(odd_first, odd_next)) and odd_two == odd_first
    return ok


def N65():
    pairs9 = sorted({tuple(sorted((k, 9 - k))) for k in range(0, 10)})
    ok = pairs9 == [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5)]
    stations = lambda p: len({x % 9 for x in p})
    ok &= [stations(p) for p in pairs9] == [1, 2, 2, 2, 2]
    ok &= 5 * 2 == 10 and 10 - 1 == 9 and 9 - 1 == 8 and 3 * 2 == 6
    return ok


def N66():
    return len(list(product(S, S))) == 4 and len(range(0, 10)) == 10 and 2 ** 2 * Q(5, 2) - 1 == 9


def N67():
    dbl = [pow(2, i, 17) for i in range(8)]
    sq = sorted({x * x % 17 for x in range(1, 17)})
    three = sorted({3 * x % 17 for x in sq})
    return (dbl == [1, 2, 4, 8, 16, 15, 13, 9] and pow(2, 8, 17) == 1 and 9 * 2 == 17 + 1
            and sorted(dbl) == sq and len(sq) == 8 and sorted(set(sq) | set(three)) == list(range(1, 17)))


def N68():
    sq = {x * x % 17 for x in range(1, 17)}
    j = lambda a, b: (a - b) % 17 in sq
    ok = all(j(a, b) == j(b, a) for a in range(17) for b in range(17) if a != b)
    quads = list(combinations(range(17), 4))
    ok &= len(quads) == 2380
    ok &= not any(all(j(a, b) for a, b in combinations(q, 2)) for q in quads)
    ok &= not any(all(not j(a, b) for a, b in combinations(q, 2)) for q in quads)
    return ok


def N70():
    return 440 + 1 == 21 ** 2 == 9 * 49


def droot(x, b):
    while x >= b:
        s = 0
        while x: s += x % b; x //= b
        x = s
    return x


def N71():
    ok = all(droot(9 * k, 10) == 9 for k in range(1, 2001))
    for b in range(3, 37):
        keep = [m for m in range(1, b) if all(droot(m * k, b) == m for k in range(1, 400))]
        ok &= keep == [b - 1]
    return ok


def N72():
    ok = (6 + 10) // 2 == 8 and (8 + 12) // 2 == 10 and (10 + 14) // 2 == 12 and (12 + 16) // 2 == 14
    ok &= 8 + 16 == 24 and (0 + 24) // 2 == 12 and 6 + 10 == 16
    ok &= 7 * 9 == 8 ** 2 - 1 and 9 * 11 == 10 ** 2 - 1 and 13 * 15 == 14 ** 2 - 1
    ok &= [(10 - k, 10 + k) for k in (2, 3, 4)] == [(8, 12), (7, 13), (6, 14)] and 6 * 14 == 10 ** 2 - 16
    ok &= 14 * 22 == 18 ** 2 - 16 and (14 + 22) // 2 == 18
    ok &= (6 + 22) // 2 == 14 and (10 + 18) // 2 == 14 and 14 - 10 == 4
    reach_span = [(Q(b - a, 2), b - a) for a, b in ((6, 14), (14, 22), (6, 22), (10, 18))]
    return ok and all(r / s == Q(1, 2) for r, s in reach_span)


# ------------------------------------------------------------------ SIX · APEXING
def N75():
    N = 48
    self_far = [k for k in range(N) if (N - k) % N == k]
    ok = self_far == [0, 24]
    ok &= all((24 - d) * (24 + d) == 24 ** 2 - d * d for d in range(1, 24))
    ok &= 23 * 25 == 24 ** 2 - 1 and 22 * 26 == 24 ** 2 - 4 and 7 ** 2 - 1 == 48
    return ok


def N76():
    gaps = [(p, q) for p, q in zip(P17, P17[1:]) if q - p == 6]
    return 5 ** 2 - 1 == 24 == math.factorial(4) and 48 // 2 == 24 and gaps[0] == (23, 29)


def N77():
    behind = [p for p in P17 if p < 24]; ahead = [p for p in P17 if p > 24]
    ok = len(behind) == 9 and len(ahead) == 8 and behind[-1] == 23 and ahead[0] == 29
    ok &= math.comb(9, 2) == 36 == 60 - 24 and math.comb(8, 2) == 28 == T(7)
    ok &= T(6) == 21 and T(8) == 36 and 28 - 21 == 7 and 36 - 28 == 8 and 36 - 21 == 15 == math.comb(6, 2)
    ok &= sum(1 for p, q in zip(P17, P17[1:]) if (q - p) % 2 == 0) == 15
    ok &= Q(36, 24) == Q(3, 2) and Q(9, 8) == Q(len(behind), len(ahead))
    return ok


def icosa_rotations():
    import numpy as np
    phi = (1 + 5 ** 0.5) / 2
    def rot(axis, ang):
        a = np.array(axis, float); a /= np.linalg.norm(a)
        x, y, z = a; c, s = math.cos(ang), math.sin(ang)
        return np.array([[c + x * x * (1 - c), x * y * (1 - c) - z * s, x * z * (1 - c) + y * s],
                         [y * x * (1 - c) + z * s, c + y * y * (1 - c), y * z * (1 - c) - x * s],
                         [z * x * (1 - c) - y * s, z * y * (1 - c) + x * s, c + z * z * (1 - c)]])
    g1 = rot((0, 1, phi), 2 * math.pi / 5)   # about a vertex of the icosahedron
    g2 = rot((1, 1, 1), 2 * math.pi / 3)     # about a face centre
    G = [np.eye(3)]
    key = lambda M: tuple(np.round(M, 6).flatten())
    seen = {key(G[0])}; frontier = [G[0]]
    while frontier:
        nxt = []
        for M in frontier:
            for g in (g1, g2):
                P = g @ M
                if key(P) not in seen: seen.add(key(P)); G.append(P); nxt.append(P)
        frontier = nxt
    return G


def N78():
    G = icosa_rotations()
    angle = lambda M: round(math.degrees(math.acos(max(-1, min(1, (M.trace() - 1) / 2)))))
    cnt = {}
    for M in G: cnt[angle(M)] = cnt.get(angle(M), 0) + 1
    fifths = cnt.get(72, 0) + cnt.get(144, 0)
    return len(G) == 60 and fifths == 24 == 6 * 4 and cnt.get(180) == 15 and cnt.get(120) == 20 and cnt.get(0) == 1 \
        and 15 + 20 + 1 == 36


def N80():
    ok = 28 ** 2 - 24 * 32 == 16 and 28 ** 2 - 27 * 29 == 1
    ok &= (27 - 24, 32 - 27) == (3, 5) and (29 - 24, 32 - 29) == (5, 3)
    ok &= 24 == 5 ** 2 - 1 and 27 == 3 ** 3 and 32 == 2 ** 5 and 24 * 27 * 32 == 144 ** 2
    return ok


# ------------------------------------------------------------------ SEVEN · COUPLING
def N81():
    return (P17 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59] and len(P17) == 17
            and [p for p in P17 if p % 2 == 0] == [2] and P17[8] == 23 and len(P17[:8]) == len(P17[9:]) == 8
            and P17[16] == 59 and sum(P17) == 440)


def N82():
    back = sorted(120 - p for p in P17)
    return back[0] == 61 and back[-1] == 118 and not is_prime(60) and 59 * 61 == 60 ** 2 - 1


def N85():
    far = lambda k: (120 - k) % 120
    ok = far(2) == 118 and far(23) == 97 and far(59) == 61 and [k for k in range(120) if far(k) == k] == [0, 60]
    ok &= [far(x) for x in (24, 27, 32)] == [96, 93, 88] and (93 - 88, 96 - 93) == (5, 3)
    return ok


def ring_run(n, steps, seed=(K, 1), ordering='together'):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]; inbox[0] = [seed]
    surf = []; states = []
    for _ in range(steps):
        row = []
        if ordering == 'together':
            nb = [[] for _ in range(n)]
            for i in range(n):
                s, c = C(carry[i], inbox[i]); carry[i] = c
                nb[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
            inbox = nb
        else:
            for i in range(n):
                s, c = C(carry[i], inbox[i]); carry[i] = c; inbox[i] = []
                inbox[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
        surf.append(tuple(row))
        states.append((tuple(tuple(c) for c in carry), tuple(tuple(b) for b in inbox)))
    return surf, states


def joint_pairs(row):
    n = len(row)
    return [i for i in range(n) if row[i] is not None and row[i] != 0 and row[i] == row[(i + 1) % n]]


def odd_ring_ok(n):
    surf, st = ring_run(n, 6 * n + 6)
    ok = True
    for t, row in enumerate(surf):
        beat = t + 1; tot = sum(x or 0 for x in row)
        ok &= (tot in (1, -1)) if beat % 2 else tot == 0
        if t >= n - 1:  # filled
            z = [i for i in range(n) if row[i] == 0]; jp = joint_pairs(row)
            ok &= (len(jp) == 1 and not z) if beat % 2 else (len(z) == 1 and not jp)
    jt = [(t, joint_pairs(surf[t])[0]) for t in range(n - 1, len(surf)) if (t + 1) % 2]
    ok &= all(b[1] == (a[1] + 1) % n and b[0] - a[0] == 2 for a, b in zip(jt, jt[1:]))
    # opposite at 2n (the state inverts), met again at 4n
    ok &= all(surf[t + 2 * n][i] == -surf[t][i] for t in range(n, len(surf) - 2 * n) for i in range(n))
    first = {}
    for t, s in enumerate(st):
        if s in first:
            ok &= (first[s] + 1, t - first[s]) == (n, 4 * n); break
        first[s] = t
    else:
        return False
    return ok


def N86():
    return all(odd_ring_ok(p) for p in P17 if p > 2)


def N89():
    surf, st = ring_run(2, 12)
    ok = surf[0] == (1, None) and all(sum(r) == 0 and r[0] == -r[1] for r in surf[1:])
    ok &= all(surf[t + 1][0] == -surf[t][0] for t in range(1, 11)) and all(surf[t + 2] == surf[t] for t in range(1, 10))
    return ok


def even_ring_ok(n, extra=6):
    surf, st = ring_run(n, n + extra)
    ok = True
    for t in range(n - 1, len(surf)):
        row = surf[t]
        ok &= not joint_pairs(row) and 0 not in row and sum(row) == 0
    ok &= all(st[t + 2] == st[t] and st[t + 1] != st[t] for t in range(n - 1, len(st) - 2))
    return ok


def N90():
    odd = [p for p in P17 if p > 2]
    sums = sorted({p + q for p in odd for q in odd})
    ok = all(even_ring_ok(n) for n in sums) and 118 in sums
    ok &= even_ring_ok(440, extra=4) and sum(P17) == 440 == 21 ** 2 - 1
    return ok


def N92():
    ok = True
    for n in range(2, 12):
        a, _ = ring_run(n, 4 * n + 4); b, _ = ring_run(n, 4 * n + 4, ordering='sequence')
        ok &= a[0] != b[0] and a != b
    b2, _ = ring_run(2, 13, ordering='sequence')
    ok &= all(b2[t + 3] == b2[t] and b2[t + 1] != b2[t] for t in range(10))          # round at three
    ok &= [sum(1 for r in b2[t:t + 3] if 0 in r) for t in range(0, 12, 3)] == [2, 2, 2, 2]  # 0 at two of each three
    a2, _ = ring_run(2, 13)
    ok &= all(0 not in r and a2[t + 2] == r for t, r in enumerate(a2[1:11], 1))           # round at two, no 0
    # the two functions read no ordering: neither takes a caller, a beat or a neighbour; the third takes the surface and runs all together
    fns = {n.name: [a.arg for a in n.args.args] for n in TREE.body if isinstance(n, ast.FunctionDef)}
    ok &= fns == {'_1_self_coupling': ['_3_self_carrying', '_2_self_offering'],
                  '_9_other_releasing': ['_10_other_surfacing', '_5_other_neutralling'],
                  '_17_social_abundancing': ['_3_self_carrying', '_2_self_offering', '_5_other_neutralling', 'SURFACE']}
    A = RV._17_social_abundancing
    for n in range(2, 12):
        Sf = {i: {'backward': [(i + 1) % n]} for i in range(n)}
        car, arr = {}, {0: {2: [(K, 1)]}}; rows = []
        for _ in range(4 * n + 4):
            rows.append(tuple(dict(C(car.get(i, []), [x for c in (2, 14, 17) for x in arr.get(i, {}).get(c, [])])[0]).get(K) for i in range(n)))
            car, arr = A(car, arr, {}, Sf)
        a, _ = ring_run(n, 4 * n + 4)
        ok &= rows == a
    return ok


def N93():
    odd = [p for p in P17 if p > 2]
    return all(math.lcm(4 * p, 4 * q) == 4 * p * q for p, q in combinations(odd, 2)) and sum(P17) == 440 and N86()


def gaps17():
    return [q - p for p, q in zip(P17, P17[1:])]


def N94():
    g = gaps17()
    return len(g) == 16 and sorted(set(g)) == [1, 2, 4, 6] and [g.count(v) for v in (1, 2, 4, 6)] == [1, 6, 5, 4] \
        and g[0] == 1


def N96():
    g = gaps17()
    matching = [P17[i] for i in range(1, 16) if g[i - 1] == g[i]]
    return matching == [5, 53] and g[1] == g[2] == 2 and g[14] == g[15] == 6


def N98():
    inter = [p for p in primes_below(55) if p > 5]
    pairs = [(p, 60 - p) for p in inter if p < 30 and is_prime(60 - p)]
    ok = pairs == [(7, 53), (13, 47), (17, 43), (19, 41), (23, 37), (29, 31)]
    ok &= len({x for pr in pairs for x in pr}) == 12
    d = [30 - p for p, _ in pairs]
    ok &= d == [23, 17, 13, 11, 7, 1] and 60 * 6 == 360 == 19 ** 2 - 1 and sum(d) == 72 and sum(2 * x for x in d) == 144 == 12 ** 2
    lone = [p for p in inter if not is_prime(60 - p)]
    return ok and lone == [11] and 60 - 11 == 49 == 7 ** 2


def N99():
    return len(P17) + (len(P17) - 1) == 33 and max(P17) < 60


# ------------------------------------------------------------------ EIGHT · INSEPARATING
def farthest(N, s):
    d = lambda a, b: min((a - b) % N, (b - a) % N)
    m = max(d(s, x) for x in range(N))
    return [x for x in range(N) if d(s, x) == m], m


def N100():
    ok = True
    for N in range(2, 1001):
        far, m = farthest(N, 0); h = N // 2
        ok &= (far == [h] and m == h) if N % 2 == 0 else (sorted(far) == [h, h + 1] and m == h)
    odd_primes = [p for p in P17 if p >= 5]
    cnt = 0
    for N in odd_primes + [p - 1 for p in odd_primes] + [9, 15, 25]:
        h = N // 2
        for s in range(N):
            far, m = farthest(N, s); cnt += 1
            ok &= (sorted(far) == sorted([(s + h) % N, (s + h + 1) % N]) and m == h) if N % 2 else (far == [(s + h) % N])
    return ok and sum(odd_primes) == 435 and sum(p - 1 for p in odd_primes) == 420 and 9 + 15 + 25 == 49 \
        and cnt == 435 + 420 + 49


def N104():
    ok = True
    def line(a, b):  # places a..b, 2h + 1 of them
        places = list(range(a, b + 1)); h = (len(places) - 1) // 2
        odd = [(x, x + 1) for x in places[:-1] if (x - a) % 2 == 0]
        even = [(x, x + 1) for x in places[:-1] if (x - a) % 2 == 1]
        both = [x for x in places if any(x in p for p in odd) and any(x in p for p in even)]
        return h, odd, even, both, places
    for n in list(range(3, 60, 2)) + [p for p in P17 if p >= 5] + [9, 15, 25]:
        h, odd, even, both, places = line(1, n)
        ok &= len(odd) == h and len(even) == h and len(both) == 2 * h - 1
        # each end continues past the line: the last place's pairing is with the place after it, the first's with the nought
        ok &= (odd[-1][1] + 1, odd[-1][1] + 2) == (n, n + 1) and (even[0][0] - 2, even[0][0] - 1) == (0, 1)
    h, odd, even, both, places = line(1, 59)
    ok &= h == 29 and len(odd) == 29 and len(even) == 29 and (59, 60) not in odd + even and (0, 1) not in odd + even
    return ok and sum(p for p in P17 if p >= 5) == 435


def N107():
    step = lambda s: (s[1], -s[0])
    ok = True
    for s0 in product(S, S):
        seq = [s0]
        for _ in range(12): seq.append(step(seq[-1]))
        ok &= seq[2] == (-s0[0], -s0[1]) and seq[4] == s0 and seq[6] == (-s0[0], -s0[1]) and seq[12] == s0
        ok &= set(seq[:6]) == set(product(S, S))
    ok &= (24 // 4, 24 // 6) == (6, 4) and ((60 - 24) // 4, (60 - 24) // 6) == (9, 6) and (60 // 4, 60 // 6) == (15, 10)
    ok &= len({x % 4 for x in (6, 14, 22)}) == 1 and 8 // 4 == 2 and 6 * 6 == 36 == 60 - 24
    return ok


def N109():
    ok = [x % 2 for x in (3, 6, 9)] == [1, 0, 1]
    ok &= all(x % 2 == 1 for x in (25, 35, 45, 55)) and all(x % 2 == 0 for x in (30, 40, 50, 60))
    ok &= all((k * m) % 2 != ((k + 1) * m) % 2 for m in range(1, 100, 2) for k in range(1, 101))
    return ok


def N113():
    rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]; cols = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    # the six exclusive-or conditions: each row's parity nought, the columns' parity nought, nought and one
    want = [0, 0, 0] + [0, 0, 1]
    meets = 0; settings = 0
    for v in product((0, 1), repeat=9):
        settings += 1
        par = [sum(v[i] for i in r) % 2 for r in rows + cols]
        if par == want: meets += 1
    along = sum(want[:3]) % 2; across = sum(want[3:]) % 2  # each reads the nine's parity once
    return settings == 512 and meets == 0 and along == 0 and across == 1


# ------------------------------------------------------------------ NINE · TUNNELING
def N114():
    far = lambda k: (440 - k) % 440
    selfp = [k for k in range(440) if far(k) == k]
    pairs = {frozenset((k, far(k))) for k in range(440) if far(k) != k}
    radius = lambda k: abs(220 - k)
    return (selfp == [0, 220] and len(pairs) == 219 and len(pairs) + 2 == 221
            and all(radius(k) == radius(440 - k) for k in range(1, 440)) and radius(220) == 0 and radius(0) == 220)


def N118():
    ok = all(((220 - r) % 2 == (220 + r) % 2 == r % 2) for r in range(0, 221))
    radii = [220 - p for p in P17]
    ok &= all(r % 2 == 1 for p, r in zip(P17, radii) if p > 2) and radii[1] == 217 and radii[-1] == 161
    ok &= [p for p, r in zip(P17, radii) if r % 2 == 0] == [2] and 220 - 2 == 218
    ok &= 440 == 8 * 5 * 11
    fives = [k for k in range(0, 440) if k % 5 == 0]
    ok &= len(fives) == 88 and sum(1 for k in fives if k % 2) == 44 and sum(1 for k in fives if k % 10 == 0) == 44
    ok &= all(fives[i] % 2 != fives[i + 1] % 2 for i in range(87))
    odd_r = sorted({abs(220 - k) for k in fives if k % 2})
    ok &= len(odd_r) == 22 and odd_r[0] == 5 and odd_r[-1] == 215 and all(r % 2 for r in odd_r) and 5 + 435 == 440
    ok &= all(abs(220 - k) % 2 == 0 for k in fives if k % 10 == 0)
    return ok


def N119():
    g = gaps17()
    steps = [abs((220 - q) - (220 - p)) for p, q in zip(P17, P17[1:])]
    return steps == g and sum(steps) == 57 == 59 - 2 and [steps.count(v) for v in (1, 2, 4, 6)] == [1, 6, 5, 4]


def N120():
    pos = [(P17[i], P17[16 - i]) for i in range(8)]
    ok = [a + b for a, b in pos] == [61, 56, 52, 50, 52, 50, 48, 48] and sum(a + b for a, b in pos) + 23 == 440
    ok &= all(k + (440 - k) == 440 for k in range(441))
    ok &= not any(a + b == 46 for a, b in pos)
    by_value = sorted((p, q) for p, q in combinations(P17, 2) if p + q == 46)
    ok &= by_value == [(3, 43), (5, 41), (17, 29)]
    mid = [p for p in P17 if 5 <= p <= 53]
    ok &= len(mid) == 14 and sum(mid) == 376 and 2 + 3 + 59 == 64 == 8 ** 2 and 376 + 64 == 440 and 220 - 64 == 156 == 376 - 220
    return ok


def N122():
    ok = 440 * 2 == 880 and (880 - 220) % 880 == 660
    for m in range(1, 40):
        centre = 220 * m
        ok &= (centre % 440 == 0) if m % 2 == 0 else (centre % 440 == 220)
    return ok


def N124():
    chain = [3, 5, 9, 17]
    ok = all(x - 1 == 2 ** k for x, k in zip(chain, (1, 2, 3, 4)))
    ok &= [(N + 1) // 2 for N in chain] == [2, 3, 5, 9] == [3 - 1, 5 - 2, 9 - 4, 17 - 8]
    ok &= [(N + 1) // 2 for N in chain][1:] == [3, 5, 9] and [(N + 1) // 2 for N in chain][1:] == chain[:-1]
    two_st = [(N - 1) // 2 for N in chain]
    ok &= two_st == [1, 2, 4, 8] and all(N == 2 * t + 1 for N, t in zip(chain, two_st))
    res = [6 // 2, 8 // 2, 10 // 2]
    ok &= res == [3, 4, 5] and set(two_st) & set(res) == {4} and 2 * 4 + 1 == 9
    c = [9]
    for _ in range(3): c.append(2 * c[-1] - 1)
    ok &= c == [9, 17, 33, 65] and all(x - 1 == 2 ** k for x, k in zip(c, (3, 4, 5, 6)))
    ok &= len(range(1, 10)) + len(range(9, 18)) - 1 == 17
    return ok


def N128():
    selfp = lambda N: [k for k in range(N) if (N - k) % N == k]
    ok = all(len(selfp(N)) == (1 if N % 2 else 2) for N in range(1, 500))
    return ok and selfp(9) == [0] and selfp(440) == [0, 220]


def N130():
    pod = [(n, 9 - n) for n in range(1, 5)]
    ok = pod == [(1, 8), (2, 7), (3, 6), (4, 5)] and all((a + b) % 2 for a, b in pod)
    moms = [(k, k + 1) for k in range(1, 9)]
    ok &= [(moms[i], moms[i + 1]) for i in range(0, 8, 2)] == [((1, 2), (2, 3)), ((3, 4), (4, 5)), ((5, 6), (6, 7)), ((7, 8), (8, 9))]
    ok &= {tuple(sorted(p)) for p in pod} & set(moms) == {(4, 5)}
    return ok


def row(s): return [2 + 2 * s * j for j in range(4)]


def N132():
    ok = row(1) == [2, 4, 6, 8] and row(2) == [2, 6, 10, 14] and row(3) == [2, 8, 14, 20] and row(4) == [2, 10, 18, 26] \
        and row(5) == [2, 12, 22, 32]
    ok &= [8 * s + 1 for s in range(1, 6)] == [9, 17, 25, 33, 41]
    ok &= all(2 + 2 * s * 4 == 2 + 8 * s and 8 * s + 1 == 2 + 8 * s - 1 and 8 * s + 1 > 8 * s for s in range(1, 101))
    return ok and len(CONNECTORS) == 6


def N133():
    ok = True
    for s in range(1, 101):
        B = 8 * s
        ud = lambda n: n + 4 * s if n <= 4 * s else n - 4 * s
        fl = lambda n: B + 1 - n
        for n in range(1, B + 1):
            ok &= ud(n) % 2 == n % 2 and fl(n) % 2 != n % 2
            seq = [n]; x = n
            for i in range(4):
                x = ud(x) if i % 2 == 0 else fl(x); seq.append(x)
            ok &= seq[-1] == n and len(set(seq[:4])) == 4
            both = fl(ud(n))
            ok &= both == (4 * s + 1 - n if n <= 4 * s else 12 * s + 1 - n)
        ok &= (B + 1) % 2 == 1 and (4 * s + 1) % 2 == 1 and (12 * s + 1) % 2 == 1
    ok &= [3, 3 + 8, 17 - 11, 6 + 8, 17 - 14] == [3, 11, 6, 14, 3]
    ok &= [3, 3 + 4, 9 - 7, 2 + 4, 9 - 6] == [3, 7, 2, 6, 3]
    return ok


def N134():
    ok = True
    for s in range(1, 60):
        r = row(s); mid = Q(r[1] + r[2], 2)
        ok &= mid == 2 + 3 * s and (r[2] - r[1], mid - r[1]) == (2 * s, s) and (r[3] - r[0], mid - r[0]) == (6 * s, 3 * s)
        ok &= Q(r[2] - r[1], mid - r[1]) == Q(r[3] - r[0], mid - r[0]) == 2
        ok &= sorted(r + [x + 8 * s for x in r]) == sorted(row(2 * s) + [x + 2 * s for x in row(2 * s)])
    E = lambda r: (lambda x: 2 + r * (x - 2))
    ok &= all(E(r)(E(s)(x)) == E(r * s)(x) for r in range(1, 12) for s in range(1, 12) for x in range(-5, 40))
    ok &= all(E(r)(x) % 2 == 0 for r in range(2, 20, 2) for x in range(1, 40))
    return ok


def N135():
    ok = True
    for B in (8, 16):
        for r in range(1, 12):
            e = lambda n: r * (n - 2) + 2 if n % 2 == 0 else r * (n + 1) - 1
            for n in range(1, B + 1):
                ok &= e(n) % 2 == n % 2
                ok &= e(B + 1 - n) == B * r + 1 - e(n)
                if n + B // 2 <= B: ok &= e(n + B // 2) - e(n) == r * B // 2
                if n + 2 <= B: ok &= e(n + 2) - e(n) == 2 * r
    e2 = lambda n: 2 * (n - 2) + 2 if n % 2 == 0 else 2 * (n + 1) - 1
    ok &= [e2(n) for n in range(1, 9)] == [3, 2, 7, 6, 11, 10, 15, 14] and [e2(n) for n in range(2, 9, 2)] == [2, 6, 10, 14]
    ok &= (e2(1), e2(2)) == (3, 2)
    return ok


# ------------------------------------------------------------------ TEN · TRANSMISSIONING
def N141():
    ok = all(17 - (n + 8) == 9 - n for n in range(-5, 30))
    ok &= all(16 * s + 1 - (n + 8 * s) == 8 * s + 1 - n for s in range(-3, 10) for n in range(-5, 30))  # linear in n and s
    return ok and [[n, n + 8, 9 - n, 17 - n] for n in (1,)] == [[1, 9, 8, 16]]


def N49():
    A = RV._17_social_abundancing
    S = {'A': {'backward': ['B'], 'forward': ['B']}, 'B': {'backward': ['A'], 'forward': ['A']}}
    car = {'A': [(K, 1, -1, 0)], 'B': [(K, -1, -1, 1)]}
    nxt_car, nxt_arr = A(car, {}, {}, S)
    ok = nxt_car['A'] == C(car['A'], [])[1] and nxt_car['B'] == C(car['B'], [])[1]
    ok &= nxt_arr['B'][17] == R(C(car['A'], [])[0], {K: K}) and nxt_arr['A'][17] == R(C(car['B'], [])[0], {K: K})
    ok &= nxt_arr['A'][2] == [] and nxt_arr['A'][14] == [] and nxt_arr['B'][2] == [] and nxt_arr['B'][14] == []
    nxt2_car, _ = A(nxt_car, nxt_arr, {}, S)
    ok &= nxt2_car['A'] == C(nxt_car['A'], nxt_arr['A'][17])[1] and nxt2_car['B'] == C(nxt_car['B'], nxt_arr['B'][17])[1]
    return ok and all(n % 2 == 1 for n in (1, 9, 17)) and 9 - 1 == 17 - 9 == 8

CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'N\d+(_probe)?', k) and callable(v)}

if __name__ == '__main__':
    res = {}
    for k in sorted(CHECKS, key=lambda s: int(re.match(r'N(\d+)', s).group(1))):
        try: res[k] = bool(CHECKS[k]())
        except Exception as e: res[k] = f'error: {e!r}'
        print(k, res[k], flush=True)
    if len(sys.argv) > 1: json.dump(res, open(sys.argv[1], 'w'), indent=1)
