"""Run checks for Exhibit THIRTY Part FOUR · MATHEMATICS (links M1...), against
Exhibit FOUR Natural Mathematics v372 and the resolver in resolver_v372.py (Exhibit ONE v372's code).
Each function named for a run link returns True when the link holds as the registry states it.
Polynomial identities are checked on a grid wider than each variable's degree, which decides them.
Standard library only."""
import os, sys, re, json, math, cmath
from fractions import Fraction as Fr
from itertools import product, permutations, combinations
from math import gcd, comb, isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as REL  # noqa: E402

S = (1, -1)
K = 'k'


def sgn(x):
    return (x > 0) - (x < 0)


# ---------------------------------------------------------------- exact arithmetic in Q(sqrt 5)
class Q5:
    """a + b*sqrt(5), a and b rational."""
    def __init__(s, a, b=0): s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return Q5(-s.a, -s.b)
    def __sub__(s, o): return s + (-(o if isinstance(o, Q5) else Q5(o)))
    def __rsub__(s, o): return Q5(o) - s
    def __mul__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a * o.a + 5 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def inv(s): d = s.a * s.a - 5 * s.b * s.b; return Q5(s.a / d, -s.b / d)
    def __truediv__(s, o): return s * (o if isinstance(o, Q5) else Q5(o)).inv()
    def __eq__(s, o): o = o if isinstance(o, Q5) else Q5(o); return s.a == o.a and s.b == o.b
    def __float__(s): return float(s.a) + float(s.b) * math.sqrt(5)

R5 = Q5(0, 1)
PHI = Q5(Fr(1, 2), Fr(1, 2))

# ---------------------------------------------------------------- 4.1-4.2
def M22():
    i = 1j
    powers = [i ** k for k in range(9)]
    ok = abs((-1) ** 2 - 1) == 0 and abs(i ** 2 + 1) < 1e-12 and abs(i ** 4 - 1) < 1e-12
    ok &= all(abs(powers[k] - powers[k % 4]) < 1e-12 for k in range(9))
    ok &= abs(i * i - (-1)) < 1e-12                           # two quarter steps are one sign flip
    ok &= all((n + 8) % 2 == n % 2 and (n + 1) % 2 != n % 2 for n in range(1, 65))
    return ok


def M25():
    T = 1.0
    q = lambda t: math.cos(math.pi * t / T)
    ts = [k / 97 for k in range(500)]
    return all(abs(q(t + T) + q(t)) < 1e-9 and abs(q(t + 2 * T) - q(t)) < 1e-9 for t in ts)


def M27():
    self4, other4 = {1, 2, 3, 4}, {2, 3, 4, 5}
    shared, outer = self4 & other4, self4 ^ other4
    occ = [n % 2 for n in sorted(self4)] + [n % 2 for n in sorted(other4)]
    return (len(shared) == 3 and len(outer) == 2 and len(self4 | other4) == 5
            and len(shared) * 2 == 6 and len(occ) == 8 == 4 + 4 == 2 * 3 + 2
            and occ[:4].count(0) == occ[:4].count(1) == 2 and occ[4:].count(0) == occ[4:].count(1) == 2
            and 2 + 2 == 2 * 2 == 4 and (2 + 3, 2 * 3) == (5, 6) and (3 + 3, 3 * 3) == (6, 9))


def M29():
    pairs = set(); pairs_m = set(); ok = True
    for n in range(64):
        z = 1j ** n; w = (-1j) ** n
        key = (round(z.real), round(z.imag), n); keym = (round(w.real), round(w.imag), n)
        ok &= key not in pairs and keym not in pairs_m
        pairs.add(key); pairs_m.add(keym)
        ok &= abs(w - z.conjugate()) < 1e-9                    # -i: the same inversions in the other order
    ok &= abs(1j ** 4 - 1) < 1e-12
    return ok


# ---------------------------------------------------------------- 4.3 the right spiral step at two signs
J = list(product(S, S))
Fm = lambda s: (-s[1], s[0])     # F(P, Q) = (-Q, P), multiplying P + iQ by i
Gm = lambda s: (s[1], -s[0])     # G(P, Q) = (Q, -P)


def all_steps():
    for vals in product(J, repeat=4):
        yield dict(zip(J, vals))


def ham(a, b): return sum(x != y for x, y in zip(a, b))


def M31():
    found = []
    n = 0
    for m in all_steps():
        n += 1
        bij = len(set(m.values())) == 4
        one = all(ham(s, m[s]) == 1 for s in J)
        never_undo = all(m[m[s]] != s for s in J)
        if bij and one and never_undo:
            found.append(m)
    ok = n == 256 and len(found) == 2
    ok &= sorted([tuple(m[s] for s in J) for m in found]) == sorted([tuple(Fm(s) for s in J), tuple(Gm(s) for s in J)])
    for f in (Fm, Gm):                                       # inverted sign alternates P, Q, P, Q from each state
        for s0 in J:
            seq = [s0]
            for _ in range(4): seq.append(f(seq[-1]))
            axes = [[k for k in (0, 1) if seq[j][k] != seq[j + 1][k]][0] for j in range(4)]
            ok &= axes in ([0, 1, 0, 1], [1, 0, 1, 0])
    # the signs of cos t and sin t as t runs forward run F
    qs = [(sgn(math.cos(t)), sgn(math.sin(t))) for t in (math.pi / 4 + k * math.pi / 2 for k in range(8))]
    ok &= all(qs[k + 1] == Fm(qs[k]) for k in range(7))
    return ok


def M33():
    neg = lambda s: (-s[0], -s[1])
    sq = [m for m in all_steps() if all(m[m[s]] == neg(s) for s in J)]
    return (len(sq) == 2 and sorted(tuple(m[s] for s in J) for m in sq)
            == sorted([tuple(Fm(s) for s in J), tuple(Gm(s) for s in J)]))


def power(f, k, s):
    for _ in range(k): s = f(s)
    return s


def M34():
    ok = True
    neg = lambda s: (-s[0], -s[1])
    for f in (Fm, Gm):
        for s in J:
            ok &= power(f, 2, s) == neg(s) and power(f, 6, s) == neg(s) and power(f, 12, s) == s
            ok &= len({power(f, k, s) for k in range(6)}) == 4       # a passage of six meets all four
            ok &= power(f, 8, s) == s and all(power(f, k + 8, s) == power(f, k, s) for k in range(16))
    ok &= (24 // 4, 24 // 6, 36 // 4, 36 // 6, 60 // 4, 60 // 6) == (6, 4, 9, 6, 15, 10)
    ok &= all(n % 4 == 0 and n % 6 == 0 for n in (24, 36, 60)) and 6 * 6 == 36 and 6 * 4 == 24
    return ok


def M36():
    ok = True
    for f in (Fm, Gm):
        for s in J:
            ok &= sgn(f(s)[0] * f(s)[1]) == -sgn(s[0] * s[1])
    for k in range(1, 400):
        t = k * 0.0157 + 0.001
        if abs(math.cos(t)) < 1e-6 or abs(math.sin(t)) < 1e-6: continue
        r = sgn(math.cos(t)) * sgn(math.sin(t))
        ok &= r == sgn(math.tan(t)) == sgn(math.sin(2 * t))
        ok &= abs(math.sin(2 * t) - 2 * math.sin(t) * math.cos(t)) < 1e-12
    return ok


def M38():
    """At one carried key of sign c, the surfaced sign is the sign of (sum of offered signs) - c."""
    ok = True; n14 = 0
    small = [[]] + [[a] for a in S] + [[a, b] for a, b in product(S, S)]
    for c, t in product(S, S):
        for vals in small:
            s, _ = C([(K, c, t, 0)], [(K, v) for v in vals])
            got = dict(s).get(K)
            ok &= got == sgn(sum(vals) - c)
            if t == -1: n14 += 1
        for L in range(3, 5):
            for vals in product((1, 0, -1), repeat=L):
                s, _ = C([(K, c, t, 0)], [(K, v) for v in vals])
                ok &= dict(s).get(K) == sgn(sum(vals) - c)
    named = {(): -1, (1,): 0, (-1,): -1, (1, 1): 1}                # at c = +1
    for vals, want in named.items():
        s, _ = C([(K, 1, -1, 0)], [(K, v) for v in vals])
        ok &= dict(s).get(K) == want
    return ok and n14 == 14


def gray(n):
    if n == 1: return [(1,), (-1,)]
    g = gray(n - 1)
    return [x + (1,) for x in g] + [x + (-1,) for x in reversed(g)]


def M39():
    ok = True
    for n in range(2, 9):
        g = gray(n)
        ok &= len(set(g)) == 2 ** n
        ok &= all(ham(g[k], g[(k + 1) % len(g)]) == 1 for k in range(len(g)))
        prior = gray(n - 1)
        ok &= [x[:-1] for x in g[:len(prior)]] == prior and [x[:-1] for x in g[len(prior):]] == prior[::-1]
    g2 = gray(2)             # read with P the sign changing first, the reflected order runs F;
    ok &= all(g2[(k + 1) % 4] == Fm(g2[k]) for k in range(4))          # with the two labels exchanged it runs G
    g2x = [(q, p) for p, q in g2]
    ok &= all(g2x[(k + 1) % 4] == Gm(g2x[k]) for k in range(4))
    g3 = gray(3)
    ch = [[j for j in range(3) if g3[k][j] != g3[(k + 1) % 8][j]][0] for k in range(8)]
    ok &= ch == [0, 1, 0, 2, 0, 1, 0, 2]
    return ok


# ---------------------------------------------------------------- 4.4 product, doubling, phi
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def M41():
    # (a.b)^2 + |a^b|^2 = |a|^2 |b|^2: degree two in each of six variables, checked at 3^6 points, decided
    g = (-1, 0, 2)
    ok = all(dot(a, b) ** 2 + dot(cross(a, b), cross(a, b)) == dot(a, a) * dot(b, b)
             for a in product(g, repeat=3) for b in product(g, repeat=3))
    for k in range(360):
        th = math.radians(k)
        ok &= abs(math.cos(th) ** 2 + math.sin(th) ** 2 - 1) < 1e-12
    return ok


def M42():
    g = (-1, 0, 2)
    ok = all(cross(a, tuple(r * x for x in a)) == (0, 0, 0) for a in product(g, repeat=3) for r in (-2, 1, 3))
    ok &= dot((1, 0, 0), (0, 1, 0)) == 0
    u = (1.0, 0.0); v = (math.cos(math.pi / 3), math.sin(math.pi / 3))
    sh = u[0] * v[0] + u[1] * v[1]; op = u[0] * v[1] - u[1] * v[0]
    ok &= abs(sh - 0.5) < 1e-12 and abs(op - math.sqrt(3) / 2) < 1e-12 and abs(op / sh - math.tan(math.pi / 3)) < 1e-12
    ok &= cross((1, 0, 0), (0, 1, 0)) == (0, 0, 1)
    # a x b is perpendicular to both: degree <= 2 per variable, 3^6 points
    ok &= all(dot(cross(a, b), a) == 0 == dot(cross(a, b), b) for a in product(g, repeat=3) for b in product(g, repeat=3))
    return ok


# Cayley-Dickson doubling: pairs (a, b), (a, b)(c, d) = (ac - d*b, da + bc*)
def cd_conj(x):
    if isinstance(x, tuple): return (cd_conj(x[0]), cd_neg(x[1]))
    return x
def cd_neg(x):
    if isinstance(x, tuple): return (cd_neg(x[0]), cd_neg(x[1]))
    return -x
def cd_add(x, y):
    if isinstance(x, tuple): return (cd_add(x[0], y[0]), cd_add(x[1], y[1]))
    return x + y
def cd_mul(x, y):
    if isinstance(x, tuple):
        a, b = x; c, d = y
        return (cd_add(cd_mul(a, c), cd_neg(cd_mul(cd_conj(d), b))), cd_add(cd_mul(d, a), cd_mul(b, cd_conj(c))))
    return x * y
def cd_scale(x, c):
    if isinstance(x, tuple): return (cd_scale(x[0], c), cd_scale(x[1], c))
    return x * c
def cd_basis(level, k):
    if level == 0: return 1 if k == 0 else 0
    half = 2 ** (level - 1)
    z = cd_basis(level - 1, -1)
    return (cd_basis(level - 1, k), z) if k < half else (z, cd_basis(level - 1, k - half))
def cd_flat(x): return list(cd_flat(x[0]) + cd_flat(x[1])) if isinstance(x, tuple) else [x]


def M44():
    e = lambda L, k: cd_basis(L, k)
    i, j, k = e(2, 1), e(2, 2), e(2, 3)
    ij, ji = cd_flat(cd_mul(i, j)), cd_flat(cd_mul(j, i))
    kk = cd_flat(k)
    ok = (ij == kk or ij == [-v for v in kk]) and ji == [-v for v in ij]
    ok &= ij == kk                                             # i j = k, j i = -k at this doubling
    # octonions: some triple of units does not associate
    O = [e(3, n) for n in range(8)]
    nonassoc = any(cd_flat(cd_mul(cd_mul(O[a], O[b]), O[c])) != cd_flat(cd_mul(O[a], cd_mul(O[b], O[c])))
                   for a, b, c in product(range(1, 8), repeat=3))
    ok &= nonassoc
    # quaternions associate
    Qb = [e(2, n) for n in range(4)]
    ok &= all(cd_flat(cd_mul(cd_mul(Qb[a], Qb[b]), Qb[c])) == cd_flat(cd_mul(Qb[a], cd_mul(Qb[b], Qb[c])))
              for a, b, c in product(range(4), repeat=3))
    # seven imaginary units on seven lines of three, each two units on one line
    lines = set()
    for a, b in combinations(range(1, 8), 2):
        p = cd_flat(cd_mul(O[a], O[b]))
        c = [n for n, v in enumerate(p) if v != 0]
        ok &= len(c) == 1
        lines.add(frozenset((a, b, c[0])))
    ok &= len(lines) == 7 and all(len(l) == 3 for l in lines)
    ok &= all(sum(1 for l in lines if {a, b} <= l) == 1 for a, b in combinations(range(1, 8), 2))
    # the complex numbers commute, and norms multiply at the four doublings on small whole elements
    ok &= cd_flat(cd_mul(e(1, 0), e(1, 1))) == cd_flat(cd_mul(e(1, 1), e(1, 0)))
    for L in (1, 2, 3):
        dim = 2 ** L
        for xs in [(1, 2, 0, -1, 3, 0, 1, -2)[:dim], (0, 1, 1, 0, -1, 2, 0, 1)[:dim]]:
            for ys in [(2, -1, 1, 0, 0, 1, -1, 1)[:dim]]:
                def build(v, L=L):
                    acc = cd_basis(L, -1)
                    for n, c in enumerate(v):
                        b = cd_basis(L, n)
                        acc = cd_add(acc, cd_scale(b, c))
                    return acc
                x, y = build(xs), build(ys)
                nx = sum(v * v for v in xs); ny = sum(v * v for v in ys)
                nxy = sum(v * v for v in cd_flat(cd_mul(x, y)))
                ok &= nxy == nx * ny
    return ok


def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)
def qconj(q): return (q[0], -q[1], -q[2], -q[3])


def FI_quat():
    ok = True
    for k in range(50):
        th = 0.37 * k; u = (0.0, 0.48, 0.6, 0.64)
        q = (math.cos(th / 2), math.sin(th / 2) * u[1], math.sin(th / 2) * u[2], math.sin(th / 2) * u[3])
        mq = tuple(-x for x in q)
        for v in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0.3, -0.2, 0.9)):
            r1 = qmul(qmul(q, v), qconj(q)); r2 = qmul(qmul(mq, v), qconj(mq))
            ok &= all(abs(a - b) < 1e-12 for a, b in zip(r1, r2))
    # a whole rotation, theta = 2 pi, carries the quaternion from 1 to -1
    th = 2 * math.pi; q = (math.cos(th / 2), math.sin(th / 2), 0, 0)
    ok &= abs(q[0] + 1) < 1e-12 and abs(q[1]) < 1e-12
    # four dimensions: x -> p x q-bar, (p, q) and (-p, -q) the one rotation, and it keeps length
    p = (0.5, 0.5, 0.5, 0.5); q = (math.cos(0.4), 0, math.sin(0.4), 0)
    for x in ((1, 0, 0, 0), (0.2, -0.7, 0.1, 0.4)):
        a = qmul(qmul(p, x), qconj(q)); b = qmul(qmul(tuple(-v for v in p), x), qconj(tuple(-v for v in q)))
        ok &= all(abs(s - t) < 1e-12 for s, t in zip(a, b))
        ok &= abs(sum(v * v for v in a) - sum(v * v for v in x)) < 1e-12
    return ok


def M47():
    ok = 1 < float(PHI) < 2 and (PHI - 1).inv() == PHI      # x = 1 + 1/x at phi: the continued fraction is all ones
    ok &= PHI * PHI == PHI + 1
    p3 = PHI * PHI * PHI
    ok &= p3 == Q5(2, 1) and p3.inv() == Q5(-2, 1) and p3 - p3.inv() == Q5(4)
    # convergents are ratios of Fibonacci numbers
    a, b = 1, 1
    for _ in range(30):
        a, b = b, a + b
        ok &= abs(b / a - float(PHI)) < 1 / (a * a)
    return ok


# ---------------------------------------------------------------- 4.5 accounting
def M50():
    ok = [x for x in range(-50, 51) if -x == x] == [0]
    rats = {Fr(p, q) for p in range(-20, 21) for q in range(1, 21) if p != 0}
    ok &= sorted(r for r in rats if 1 / r == r) == [-1, 1]
    mats = list(product((-1, 0, 1), repeat=9))
    T = lambda m: tuple(m[3 * c + r] for r in range(3) for c in range(3))
    fixed = [m for m in mats if T(m) == m]
    ok &= all(T(T(m)) == m for m in mats) and len(fixed) == 3 ** 6
    ok &= all(m[1] == m[3] and m[2] == m[6] and m[5] == m[7] for m in fixed)
    U = frozenset(range(1, 7))
    subsets = [frozenset(c) for r in range(7) for c in combinations(U, r)]
    ok &= not any(U - s == s for s in subsets)
    ok &= not any(-s == s for s in S)
    gz = [complex(a, b) for a in range(-5, 6) for b in range(-5, 6)]
    ok &= all((z.conjugate() == z) == (z.imag == 0) for z in gz)
    ok &= [v for v in product(range(-3, 4), repeat=3) if tuple(-x for x in v) == v] == [(0, 0, 0)]
    return ok


def M53():
    ok = True
    for N in range(2, 201, 2):
        podal = [k for k in range(N) if (N - k) % N == k]
        shift = [k for k in range(N) if (k + N // 2) % N == k]
        ok &= podal == [0, N // 2] and shift == []
        ok &= all((N - (N - k) % N) % N == k and ((k + N // 2) + N // 2) % N == k for k in range(N))
    return ok


def far_places(N):
    d = [min(j, N - j) for j in range(N)]
    m = max(d)
    return [j for j in range(N) if d[j] == m]


def M54():
    ok = True
    for h in range(1, 60):
        ok &= far_places(2 * h + 1) == [h, h + 1] and far_places(2 * h) == [h]
    ok &= far_places(5) == [2, 3] and far_places(17) == [8, 9] and far_places(59) == [29, 30]
    primes = [p for p in range(5, 60) if all(p % q for q in range(2, isqrt(p) + 1))]
    ok &= len(primes) == 15
    for N in primes + [9, 15, 25]:
        for o in range(N):                                     # at each origin
            d = [min((j - o) % N, (o - j) % N) for j in range(N)]
            m = max(d); far = sorted((j - o) % N for j in range(N) if d[j] == m)
            ok &= far == [(N - 1) // 2, (N + 1) // 2]
    return ok


def involutions(n):
    for perm in permutations(range(n)):
        if all(perm[perm[i]] == i for i in range(n)):
            yield perm


def M55():
    ok = True
    for n in range(1, 10):
        fpf = any(all(p[i] != i for i in range(n)) for p in involutions(n))
        ok &= fpf == (n % 2 == 0)
    for h in range(1, 41):
        top = 2 * h + 1
        odd_pairs = [(k, k + 1) for k in range(1, top, 2)]
        even_pairs = [(k, k + 1) for k in range(2, top, 2)]
        in_odd = {x for p in odd_pairs for x in p}; in_even = {x for p in even_pairs for x in p}
        ok &= len(odd_pairs) == h == len(even_pairs)
        ok &= in_odd & in_even == set(range(2, 2 * h + 1)) and len(in_odd & in_even) == 2 * h - 1
        ok &= (set(range(1, top + 1)) - in_odd) == {top} and (set(range(1, top + 1)) - in_even) == {1}
    ok &= len([(k, k + 1) for k in range(1, 59, 2)]) == 29 == len([(k, k + 1) for k in range(2, 60, 2)])
    return ok


def M58():
    ok = True
    for N in range(2, 121):
        prime = all(N % q for q in range(2, isqrt(N) + 1))
        for k in range(1, N):
            seen = []; x = 0
            while True:
                seen.append(x); x = (x + k) % N
                if x == 0: break
            ok &= len(seen) == N // gcd(N, k)
            if prime: ok &= len(seen) == N
    ok &= 8 // gcd(8, 3) == 8 and 9 // gcd(9, 3) == 3 and gcd(4, 9) == 1
    return ok


def M59():
    ok = True
    for m in range(1, 41):
        for n in range(1, 41):
            met = set(); x = (0, 0)
            while x not in met:
                met.add(x); x = ((x[0] + 1) % m, (x[1] + 1) % n)
            g = gcd(m, n)
            ok &= len(met) == m * n // g
            # windings: the classes (a - b) mod g; each winding one class, g of them
            ok &= len({(a - b) % g for a in range(m) for b in range(n)}) == g
            ok &= all((a - b) % g == 0 for a, b in met)
            if g == 1: ok &= len(met) == m * n
    return ok


def M63():
    half = lambda s: (-s[0], -s[1])
    ok = True
    for s in J:
        ok &= half(s) != s and half(half(s)) == s
        ok &= all(power(Fm, k, s) != s for k in (1, 2, 3)) and power(Fm, 4, s) == s
        ok &= all(power(Gm, k, s) != s for k in (1, 2, 3)) and power(Gm, 4, s) == s
        for f in (half, Fm, Gm):
            seen = set(); x = s
            for n in range(200):
                ok &= (x, n) not in seen; seen.add((x, n)); x = f(x)
    return ok


def matmul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def refl(a): return [[math.cos(2 * a), math.sin(2 * a)], [math.sin(2 * a), -math.cos(2 * a)]]
def rot(a): return [[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]]
def close(A, B, e=1e-12): return all(abs(A[i][j] - B[i][j]) < e for i in range(len(A)) for j in range(len(A[0])))


def M65():
    ok = True
    for x in range(0, 180, 7):
        for y in range(0, 180, 11):
            a, b = math.radians(x), math.radians(y)
            ok &= close(matmul(refl(b), refl(a)), rot(2 * (b - a)))
    RP = lambda s: (-s[0], s[1]); RQ = lambda s: (s[0], -s[1]); SW = lambda s: (s[1], s[0])
    ok &= all(RQ(RP(s)) == (-s[0], -s[1]) for s in J)                  # lines at ninety degrees: the half step
    ok &= all(SW(RP(s)) == Gm(s) and RP(SW(s)) == Fm(s) for s in J)     # lines at forty-five degrees: a quarter step
    return ok


def det(M):
    n = len(M)
    if n == 1: return M[0][0]
    return sum((-1) ** j * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(n))


def M66():
    St = list(product(S, repeat=3))
    inv = [lambda s, j=j: tuple(-v if k == j else v for k, v in enumerate(s)) for j in range(3)]
    ok = True
    for order in permutations(range(3)):
        for s in St:
            x = s
            for j in order: x = inv[j](x)
            ok &= x == tuple(-v for v in s) and x != s
    ok &= len({frozenset((s, tuple(-v for v in s))) for s in St}) == 4
    for n in range(1, 9):
        ok &= det([[-1 if i == j else 0 for j in range(n)] for i in range(n)]) == (-1) ** n
    return ok


def M68():
    pts = list(product(range(-2, 3), repeat=3))
    D = lambda signs: (lambda v: tuple(s * x for s, x in zip(signs, v)))
    one = D((-1, 1, 1)); two = D((-1, -1, 1)); three = D((-1, -1, -1))
    ok = sorted(v for v in pts if one(v) == v) == sorted(v for v in pts if v[0] == 0)          # keeps a plane
    ok &= sorted(v for v in pts if two(v) == v) == sorted(v for v in pts if v[0] == v[1] == 0)  # half step about the third axis
    ok &= [v for v in pts if three(v) == v] == [(0, 0, 0)]
    ok &= det([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]) == 1 and det([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]) == -1
    ok &= all((-s[0], -s[1]) == power(Fm, 2, s) for s in J)
    return ok


# ---------------------------------------------------------------- 4.6 closings, totals, halfway pairing and fold
def M71():
    fifths = Fr(3, 2) ** 12; octaves = 2 ** 7
    return (octaves == 128 and abs(float(fifths) - 129.746337890625) < 1e-12
            and fifths / octaves == Fr(3 ** 12, 2 ** 19) == Fr(531441, 524288))


def M76():
    # two groups, each favouring A; joined they favour B
    A = [(81, 87), (192, 263)]; B = [(234, 270), (55, 80)]
    ok = all(Fr(*a) > Fr(*b) for a, b in zip(A, B))
    ok &= Fr(sum(a for a, _ in A), sum(n for _, n in A)) < Fr(sum(b for b, _ in B), sum(n for _, n in B))
    x, y = 1, -1
    for _ in range(50):
        ok &= x + y == 0
        x, y = -x, -y
    return ok


def trace(offers, carry):
    out = []
    for off in offers:
        s, carry = C(carry, off)
        out.append(dict(s).get(K, 0))
    return out, carry


def M79():
    younger, _ = trace([[(K, 1)]] * 5, [(K, 1, -1, 0)])
    elder, _ = trace([[(K, 1)]] * 4, [(K, 1, -1, 1)])
    ok = younger == [0, 0, 0, 0, 1] and elder == [0, 0, 0, 1]
    # the elder's carrying ends at the third receiving, the younger's at the fourth
    carry = [(K, 1, -1, 1)]; ends_e = None
    for n in range(1, 5):
        s, carry = C(carry, [(K, 1)])
        if ends_e is None and not carry: ends_e = n
    carry = [(K, 1, -1, 0)]; ends_y = None
    for n in range(1, 6):
        s, carry = C(carry, [(K, 1)])
        if ends_y is None and not carry: ends_y = n
    s4, c4 = C([], [(K, 1)])
    ok &= ends_e == 3 and ends_y == 4 and s4 == [(K, 1)] and c4 == [(K, 1, -1, 0)]
    return ok


def M81():
    ok = True
    for s in range(1, 6):
        row = [2 + 2 * s * j for j in range(4)]
        ok &= all(row[j + 1] - row[j] == 2 * s for j in range(3))
        ok &= 2 + 2 * s * 4 == 2 + 8 * s and 8 * s + 1 == 2 + 8 * s - 1 and (8 * s + 1) % 2 == 1
        ok &= 8 * s + 1 not in range(1, 8 * s + 1)
    ok &= [8 * s + 1 for s in range(1, 6)] == [9, 17, 25, 33, 41]
    ok &= [[2 + 2 * s * j for j in range(4)] for s in range(1, 6)] == [[2, 4, 6, 8], [2, 6, 10, 14], [2, 8, 14, 20], [2, 10, 18, 26], [2, 12, 22, 32]]
    return ok


def halfway(s): return lambda n: n + 4 * s if n <= 4 * s else n - 4 * s
def fold(s): return lambda n: 8 * s + 1 - n


def M82():
    ok = True
    for s in range(1, 41):
        H, Fo = halfway(s), fold(s); names = range(1, 8 * s + 1)
        ok &= all(H(H(n)) == n and H(n) != n and H(n) % 2 == n % 2 for n in names)
        ok &= all(Fo(Fo(n)) == n and Fo(n) != n and Fo(n) % 2 != n % 2 for n in names)
        for n in names:
            fh = Fo(H(n))
            ok &= fh == (4 * s + 1 - n if n <= 4 * s else 12 * s + 1 - n) and fh != n
            cyc = [n]; x = n
            for k in range(4):
                x = H(x) if k % 2 == 0 else Fo(x); cyc.append(x)
            ok &= len(set(cyc[:4])) == 4 and cyc[4] == n
        ok &= all(v % 2 == 1 for v in (4 * s + 1, 8 * s + 1, 12 * s + 1))
    cyc = lambda s, n: [n, halfway(s)(n), fold(s)(halfway(s)(n)), halfway(s)(fold(s)(halfway(s)(n)))]
    ok &= cyc(2, 3) == [3, 11, 6, 14] and cyc(1, 3) == [3, 7, 2, 6]
    return ok


def M83():
    ok = True
    for s in range(1, 30):
        for n in range(1, 8 * s + 1):
            ok &= fold(2 * s)(n + 8 * s) == fold(s)(n)
            c = [n, n + 8 * s, 8 * s + 1 - n, 16 * s + 1 - n]
            ok &= len(set(c)) == 4 and fold(2 * s)(c[3]) == n and c[3] - c[2] == 8 * s
            ok &= c[1] % 2 == n % 2 and c[2] % 2 != n % 2
        for t in range(s + 1, 4 * s + 1):
            ok &= all(fold(t)(n + 8 * (t - s)) == fold(s)(n) for n in range(1, 8 * s + 1))
            ok &= (8 * (t - s) == 4 * t) == (t == 2 * s)
        ok &= 8 * ((s + 1) - s) == 8
    rows = [[n, n + 8, 9 - n, 17 - n] for n in range(1, 5)]
    ok &= rows == [[1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]]
    ok &= all(17 - (n + 8) == 9 - n for n in range(1, 9))
    return ok


def M84():
    ok = True
    for s in range(1, 30):
        row = [2 + 2 * s * j for j in range(4)]; mid = Fr(row[0] + row[3], 2)
        ok &= mid == 2 + 3 * s and [r - mid for r in row] == [-3 * s, -s, s, 3 * s]
        ok &= row[2] - row[1] == 2 * s and row[3] - row[0] == 6 * s        # each span twice its reach
        ok &= 6 * s != 8 * s and mid != Fr(8 * s + 1, 2)
    r2 = [2, 6, 10, 14]
    ok &= {(r2[0], r2[3]), (r2[1], r2[2])} == {(2, 14), (6, 10)} and {(r2[0], r2[2]), (r2[1], r2[3])} == {(2, 10), (6, 14)}
    return ok


def M85():
    D = lambda r: (lambda x: 2 + r * (x - 2))
    ok = all(D(r)(D(s)(x)) == D(r * s)(x) for r in range(0, 9) for s in range(0, 9) for x in range(-20, 40))
    ok &= all([D(s)(2 + 2 * j) for j in range(4)] == [2 + 2 * s * j for j in range(4)] for s in range(1, 9))
    ok &= all(D(r)(x) % 2 == 0 for r in range(2, 20, 2) for x in range(-30, 60))
    ok &= [D(d)(4) - 2 for d in (1, 2, 4, 8)] == [2, 4, 8, 16]
    return ok


def M86():
    ok = True
    for s in range(1, 30):
        wider = [2 + 4 * s * j for j in range(4)]
        comp = [2 + 2 * s + 4 * s * j for j in range(4)]
        F2s = fold(2 * s)
        ok &= all(F2s(wider[j]) - comp[3 - j] == 2 * s - 3 for j in range(4))
    ok &= [2 * s - 3 for s in (1, 2, 3)] == [-1, 1, 3]
    ok &= fold(2)(2) == 15 and [4, 8, 12, 16][3] == 16 and 15 == 16 - 1        # holds at s = 1: the odd just before
    ok &= fold(4)(2) == 31 and [6, 14, 22, 30][3] == 30 and 31 == 30 + 1       # fails at s = 2: one after
    return ok


def E(r): return lambda n: r * (n - 2) + 2 if n % 2 == 0 else r * (n + 1) - 1


def M87():
    ok = True
    for B in (8, 16):
        for r in range(1, 7):
            e = E(r); names = range(1, B + 1)
            ok &= all(e(n) % 2 == n % 2 for n in names)
            ok &= all(e(B + 1 - n) == B * r + 1 - e(n) for n in names)
            ok &= all(e(n + B // 2) == e(n) + r * B // 2 for n in range(1, B // 2 + 1))
            ok &= all(e(n + 2) - e(n) == 2 * r for n in range(1, B - 1))
            if r >= 2: ok &= e(B + 1) > B * r + 1
    ok &= [E(2)(n) for n in range(1, 9)] == [3, 2, 7, 6, 11, 10, 15, 14]
    ok &= [E(2)(n) for n in (2, 4, 6, 8)] == [2, 6, 10, 14] and (E(2)(1), E(2)(2)) == (3, 2)
    return ok


# ---------------------------------------------------------------- 4.7 bounding
def M88():
    # degree two in n and in k: a 3 x 3 grid decides it; a wider range besides
    ok = all(n * n - (n - k) * (n + k) == k * k for n in range(-50, 51) for k in range(-50, 51))
    return ok and all(n * n - (n - 1) * (n + 1) == 1 for n in range(-100, 101))


def M89():
    ok = [k for k in range(1, 1000) if k * k == 2 * k] == [2]
    ok &= all(n * n - (n - 2) * (n + 2) == 4 == 2 * 2 for n in range(-100, 101))
    ok &= 4 ** 2 - 2 * 6 == 4 and 10 ** 2 - 8 * 12 == 4
    return ok


def M90():
    ok = [k for k in range(1, 200) if 2 * k - 1 == 1] == [1]     # faces n - k and n + k hold 2k - 1 between
    ok &= (25 - 23) // 2 == 1 and (23 + 25) // 2 == 24
    ok &= (55 - 23) == 32 and (55 - 23) // 2 == 16 and (23 + 55) // 2 == 39 and 39 ** 2 - 23 * 55 == 256 == 16 ** 2
    return ok


def M96():
    ok = abs(math.hypot(1, 1) - math.sqrt(2)) < 1e-15 and abs(math.sqrt(1 + 1 + 1) - math.sqrt(3)) < 1e-15
    pts = [(math.cos(2 * math.pi * k / 5), math.sin(2 * math.pi * k / 5)) for k in range(5)]
    side = math.dist(pts[0], pts[1]); diag = math.dist(pts[0], pts[2])
    ok &= abs(diag / side - float(PHI)) < 1e-12
    c36 = math.cos(math.radians(36)); s18 = math.sin(math.radians(18)); c18 = math.cos(math.radians(18))
    ok &= abs(c36 - float(PHI) / 2) < 1e-15 and abs(s18 - 1 / (2 * float(PHI))) < 1e-15
    ok &= abs(s18 - (math.sqrt(5) - 1) / 4) < 1e-15 and abs(c18 - math.sqrt(10 + 2 * math.sqrt(5)) / 4) < 1e-15
    ok &= (PHI / 2) * (PHI / 2) * 4 - PHI - 1 == Q5(0)           # 4x^2 - 2x - 1 = 0 at x = phi/2, cos 36 exactly
    ok &= Q5(1) / (PHI * 2) == (R5 - 1) / 4
    return ok


def M97():
    ok = True
    for k in range(-890, 891):
        x = math.radians(k / 10)
        if abs(abs(math.tan(x)) - 1) < 1e-6: continue
        t = math.tan(x)
        ok &= abs(math.tan(2 * x) - 2 * t / (1 - t * t)) < 1e-6 * max(1, abs(math.tan(2 * x)))
    # 2t/(1 - t^2) = 2t  <=>  t^3 = 0: nought alone
    ok &= {t for t in (Fr(p, q) for p in range(-40, 41) for q in range(1, 11)) if t * t != 1 and 2 * t / (1 - t * t) == 2 * t} == {0}
    ok &= abs(math.cos(math.radians(90))) < 1e-15                  # the doubled angle at 45 degrees: the pole
    for num in range(1, 64):
        x = Fr(num, 64); bits = format(num, '06b'); y = (2 * x) % 1
        ok &= format(int(y * 64), '06b') == bits[1:] + '0'
    return ok


def M98():
    g = lambda t: 2 * t / (1 - t * t)
    # fixed: 2t/(1-t^2) = t  <=>  t (1 + t^2) = 0  <=>  t = 0 over the reals
    # sign changing, size the same: 2t/(1-t^2) = -t, t != 0  <=>  t^2 = 3
    # t with 2t/(1 - t^2) = -t and t != 0 satisfy t^2 = 3, over the rationals none: checked at p/q below
    ok = not any(2 * t / (1 - t * t) == -t for t in (Fr(p, q) for p in range(1, 60) for q in range(1, 30)) if t * t != 1)
    r3 = math.sqrt(3)
    ok &= abs(g(r3) + r3) < 1e-12 and abs(g(-r3) - r3) < 1e-12
    x = r3; seq = []
    for _ in range(6): x = g(x); seq.append(round(x / r3))
    ok &= seq == [-1, 1, -1, 1, -1, 1]
    ok &= abs(math.tan(math.radians(60)) - r3) < 1e-12 and abs(math.tan(math.radians(120)) + r3) < 1e-12
    # scan: fixed points and sign-changing pairs among t on a fine grid
    fixed = [k for k in range(-3000, 3001) if abs(k / 1000) != 1 and abs(g(k / 1000) - k / 1000) < 1e-12]
    ok &= fixed == [0]
    return ok


def M99():
    ok = True
    for a, b, c in product(range(-4, 5), repeat=3):
        th = 0.5 * math.atan2(2 * b, a - c)
        R = rot(th); M = [[a, b], [b, c]]
        Mp = matmul(matmul([[R[0][0], R[1][0]], [R[0][1], R[1][1]]], M), R)
        ok &= abs(Mp[0][1]) < 1e-9
    th = 0.5 * math.atan2(2 * 2, 5 - 1)
    ok &= abs(math.degrees(th) - 22.5) < 1e-12
    th = 0.5 * math.atan2(2 * 3, 0)                                 # a = c: forty-five degrees
    ok &= abs(math.degrees(th) - 45) < 1e-12
    return ok


def M100():
    ok = True
    for k in range(1, 179):
        x = math.radians(k); t = math.tan(x / 2)
        ok &= abs(math.sin(x) - 2 * t / (1 + t * t)) < 1e-12 and abs(math.cos(x) - (1 - t * t) / (1 + t * t)) < 1e-12
    gen = set()
    for m in range(2, 40):
        for n in range(1, m):
            a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
            ok &= a * a + b * b == c * c
            s, co = Fr(2 * n * m, m * m + n * n), Fr(m * m - n * n, m * m + n * n)   # t = n/m
            ok &= s * s + co * co == 1
            gen.add((min(a, b), max(a, b), c))
    for c in range(1, 500):
        for a in range(1, c):
            b2 = c * c - a * a; b = isqrt(b2)
            if b >= a and b * b == b2:
                g = gcd(gcd(a, b), c)
                ok &= (a // g, b // g, c // g) in gen                  # up to order and a whole multiple
    return ok


# ---------------------------------------------------------------- 4.9 inseparating
def M121():
    vals = [0, 1, 2]                                    # nought < a < one on a chain
    meet = min
    neg = lambda x: max(y for y in vals if meet(x, y) == 0)
    return neg(1) == 0 and neg(0) == 2 and neg(neg(1)) == 2 != 1 and neg(2) == 0


# ---------------------------------------------------------------- 4.10 co-offering
NEUTRALS = ('nought', 'scale', 'bounded infinity')


def M125():
    pairings = list(combinations(NEUTRALS, 2))
    offerings = [(a, b) for a, b in permutations(NEUTRALS, 2)]
    states = list(product(('fixed', 'floating'), repeat=3))
    return len(pairings) == 3 and len(offerings) == 6 and len(states) == 8 == 2 ** 3


def M128():
    offerings = list(permutations(NEUTRALS, 2))
    table = {}
    for r in range(4):
        for fixed in combinations(NEUTRALS, r):
            run = [o for o in offerings if o[0] not in fixed and o[1] not in fixed]
            table.setdefault(r, set()).add((len(run), len(offerings) - len(run)))
    ok = table == {0: {(6, 0)}, 1: {(2, 4)}, 2: {(0, 6)}, 3: {(0, 6)}}
    for n in NEUTRALS:                                    # a neutral fixed partners two of three pairings, both ways
        ok &= sum(1 for o in offerings if n in o) == 4 and sum(1 for p in combinations(NEUTRALS, 2) if n in p) == 2
    return ok


def perm_mul(p, q): return tuple(p[q[i]] for i in range(len(q)))
def perm_inv(p):
    r = [0] * len(p)
    for i, v in enumerate(p): r[v] = i
    return tuple(r)
def parity(p):
    s, seen = 0, set()
    for i in range(len(p)):
        if i in seen: continue
        j, L = i, 0
        while j not in seen: seen.add(j); j = p[j]; L += 1
        s += L - 1
    return s % 2


def gen_group(gens):
    idt = tuple(range(len(gens[0]))); G = {idt}; frontier = [idt]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = perm_mul(g, h)
                if x not in G: G.add(x); nxt.append(x)
        frontier = nxt
    return G


def commutator_subgroup(G):
    return gen_group([perm_mul(perm_mul(a, b), perm_mul(perm_inv(a), perm_inv(b))) for a in G for b in G])


def M133():
    S5 = set(permutations(range(5))); A5 = {p for p in S5 if parity(p) == 0}
    classes = []; left = set(A5)
    while left:
        x = next(iter(left)); cl = {perm_mul(perm_mul(g, x), perm_inv(g)) for g in A5}
        classes.append(len(cl)); left -= cl
    ok = len(A5) == 60 and sorted(classes) == [1, 12, 12, 15, 20]
    # a normal subgroup is a union of classes containing the one, its size dividing 60
    sizes = {1 + sum(c) for r in range(0, 5) for c in combinations(sorted(classes)[1:], r)}
    ok &= sorted(s for s in sizes if 60 % s == 0) == [1, 60]
    ok &= commutator_subgroup(S5) == A5 and commutator_subgroup(A5) == A5      # S5 descends to A5 and stops
    S4 = set(permutations(range(4)))
    d1 = commutator_subgroup(S4); d2 = commutator_subgroup(d1); d3 = commutator_subgroup(d2)
    ok &= (len(d1), len(d2), len(d3)) == (12, 4, 1)                            # S4 > A4 > V4 > 1
    return ok


def ico_vertices():
    p = float(PHI); V = []
    for a, b in product((1, -1), repeat=2):
        V += [(0, a, b * p), (a, b * p, 0), (b * p, 0, a)]
    return V


def M137():
    V = ico_vertices(); d2 = lambda u, v: sum((x - y) ** 2 for x, y in zip(u, v))
    edges = [(i, j) for i, j in combinations(range(12), 2) if abs(d2(V[i], V[j]) - 4) < 1e-9]
    faces = [t for t in combinations(range(12), 3) if all((min(a, b), max(a, b)) in edges for a, b in combinations(t, 2))]
    ok = len(V) == 12 and len(edges) == 30 and len(faces) == 20
    # rotations: frame (u, v, u x v) at an edge sent to each directed edge
    def frame(u, v):
        w = cross(u, v); return [list(u), list(v), list(w)]
    def solve(Fa, Fb):   # R with R Fa^T = Fb^T -> R = Fb^T (Fa^T)^-1
        A = [[Fa[j][i] for j in range(3)] for i in range(3)]; B = [[Fb[j][i] for j in range(3)] for i in range(3)]
        dA = det(A)
        inv = [[(A[(j + 1) % 3][(i + 1) % 3] * A[(j + 2) % 3][(i + 2) % 3] - A[(j + 1) % 3][(i + 2) % 3] * A[(j + 2) % 3][(i + 1) % 3]) / dA for j in range(3)] for i in range(3)]
        return matmul(B, inv)
    u, v = V[edges[0][0]], V[edges[0][1]]
    rots = []
    for i, j in edges + [(b, a) for a, b in edges]:
        R = solve(frame(u, v), frame(V[i], V[j]))
        img = [tuple(sum(R[r][c] * x[c] for c in range(3)) for r in range(3)) for x in V]
        if all(any(d2(y, z) < 1e-9 for z in V) for y in img):
            if not any(close(R, Q, 1e-9) for Q in rots): rots.append(R)
    tr = [round(R[0][0] + R[1][1] + R[2][2], 6) for R in rots]
    ident = tr.count(3.0); halfr = tr.count(-1.0); third = tr.count(0.0)
    fifth = sum(1 for t in tr if abs(t - float(PHI)) < 1e-5 or abs(t - (1 - float(PHI))) < 1e-5)
    ok &= len(rots) == 60 and (ident, halfr, third, fifth) == (1, 15, 20, 24)
    ok &= ident + halfr + third == 36 and Fr(36, 24) == Fr(3, 2)
    return ok


def M139():
    ok = True
    for k in range(360):
        th = math.radians(k); h = 1e-6
        d = ((math.cos(th + h) - math.cos(th - h)) / (2 * h), (math.sin(th + h) - math.sin(th - h)) / (2 * h))
        f = Fm((math.cos(th), math.sin(th)))
        ok &= abs(d[0] - f[0]) < 1e-8 and abs(d[1] - f[1]) < 1e-8
    grp = {1j ** k for k in range(8)}
    ok &= len({(round(z.real), round(z.imag)) for z in grp}) == 4 and {1, -1} <= {complex(round(z.real), round(z.imag)) for z in grp}
    ok &= len({(-1) ** k for k in range(8)}) == 2
    E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    ok &= all(dot(a, b) == (1 if a == b else 0) for a in E3 for b in E3)
    return ok


def colourings(n, edges):
    for c in product((0, 1), repeat=n):
        if all(c[a] != c[b] for a, b in edges): yield c


def connected(n, edges):
    adj = {i: set() for i in range(n)}
    for a, b in edges: adj[a].add(b); adj[b].add(a)
    seen = {0}; st = [0]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y); st.append(y)
    return len(seen) == n


def M140():
    ok = True
    for n in range(3, 15):
        ring = [(i, (i + 1) % n) for i in range(n)]
        cols = list(colourings(n, ring))
        ok &= (len(cols) > 0) == (n % 2 == 0)
        best = min(sum(c[a] == c[b] for a, b in ring) for c in product((0, 1), repeat=n))
        ok &= best == (0 if n % 2 == 0 else 1)
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        for mask in range(2 ** len(pairs)):
            edges = [p for k, p in enumerate(pairs) if mask >> k & 1]
            if not connected(n, edges): continue
            cnt = sum(1 for _ in colourings(n, edges))
            ok &= cnt in (0, 2)
    return ok


def M141():
    V = list(product((1, -1), repeat=3))
    E = [(a, b) for a, b in combinations(V, 2) if ham(a, b) == 1]
    faces = {(j, s) for j in range(3) for s in (1, -1)}
    ok = len(V) == 8 and len(E) == 12 and len(faces) == 6
    signed = []
    for perm in permutations(range(3)):
        for sg in product((1, -1), repeat=3):
            M = [[sg[i] if j == perm[i] else 0 for j in range(3)] for i in range(3)]
            signed.append(M)
    ok &= len(signed) == 48 and sum(1 for M in signed if det(M) == 1) == 24
    return ok


def M142():
    m3 = [[-1 if i == j else 0 for j in range(3)] for i in range(3)]
    m4 = [[-1 if i == j else 0 for j in range(4)] for i in range(4)]
    a = [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    b = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
    ok = det(m3) == -1 and det(m4) == 1 and matmul(a, b) == m4 and det(a) == det(b) == 1
    ok &= [v for v in product(range(-2, 3), repeat=4) if tuple(-x for x in v) == v] == [(0, 0, 0, 0)]
    # the cube's 48 carry x -> -x only among those with determinant -1; the tesseract's rotations carry it
    ok &= det([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]) == -1
    return ok


def M144():
    lip = [v for v in product(range(-1, 2), repeat=4) if sum(x * x for x in v) == 1]
    half = [v for v in product((Fr(1, 2), Fr(-1, 2)), repeat=4) if sum(x * x for x in v) == 1]
    ok = len(lip) == 8 and len(half) == 16 and len(lip) + len(half) == 24
    # (1 + i + j + k) / 2 lies at distance one from its nearest whole points: dividing 1+i+j+k by 2
    # at whole quotients leaves a remainder of norm 4, the divisor's norm, never below it
    a = (1, 1, 1, 1)
    best = min(sum((a[i] - 2 * q[i]) ** 2 for i in range(4)) for q in product(range(-2, 3), repeat=4))
    ok &= best == 4 == 2 * 2
    # (1/2, ..., 1/2) at distance one from its nearest whole points in four dimensions and in no other
    ok &= [d for d in range(1, 30) if Fr(d, 4) == 1] == [4]
    return ok


def M148():
    ok = True
    I = [[1, 0], [0, 1]]
    tref = [[1, 1], [-1, 0]]; fig8 = [[2, 1], [1, 1]]
    P = I
    for k in range(1, 7):
        P = matmul(P, tref)
        ok &= (P == I) == (k == 6)
    ok &= tref[0][0] + tref[1][1] == 1 and fig8[0][0] + fig8[1][1] == 3
    lam = (3 + math.sqrt(5)) / 2
    ok &= abs(lam - float(PHI) ** 2) < 1e-12                      # the figure-eight winds on at phi squared
    P = I
    for k in range(1, 60):
        P = matmul(P, fig8); ok &= P != I and P != [[-1, 0], [0, -1]]
    for a, b, c, d in product(range(-6, 7), repeat=4):
        if a * d - b * c != 1: continue
        M = [[a, b], [c, d]]; t = abs(a + d)
        P = I; order = None
        for k in range(1, 13):
            P = matmul(P, M)
            if P == I: order = k; break
        if t < 2: ok &= order is not None
        if t > 2: ok &= order is None
        if t == 2:
            ok &= M in (I, [[-1, 0], [0, -1]]) or order is None
    return ok


def M150():
    tr = list(combinations(range(5), 2))
    ok = len(tr) == 10 == comb(5, 2)
    for a, b in tr:
        p = list(range(5)); p[a], p[b] = b, a; p = tuple(p)
        ok &= perm_mul(p, p) == tuple(range(5)) and sum(1 for i in range(5) if p[i] == i) == 3
    ok &= [n for n in range(2, 200) if comb(n, 2) == 2 * n] == [5]
    ok &= [k * (k + 1) // 2 for k in range(1, 5)][3] == 10 and [comb(k + 2, 3) for k in range(1, 4)][2] == 10 == 1 + 3 + 6
    ok &= len(list(combinations((1, -1), 2))) == 1
    return ok


def M151():
    pts = [(math.cos(2 * math.pi * k / 5), math.sin(2 * math.pi * k / 5)) for k in range(5)]
    vec = lambda a, b: (pts[b][0] - pts[a][0], pts[b][1] - pts[a][1])
    ok = True
    gens = []
    for i in range(5):
        a, b = i, (i + 1) % 5
        diag = [d for d in combinations(range(5), 2) if a not in d and b not in d and (d[1] - d[0]) % 5 in (2, 3)]
        ok &= len(diag) == 1
        c, d = diag[0]
        u, w = vec(a, b), vec(c, d)
        ok &= abs(u[0] * w[1] - u[1] * w[0]) < 1e-12                              # parallel
        ok &= abs(math.hypot(*w) / math.hypot(*u) - float(PHI)) < 1e-12
        t1 = list(range(5)); t1[a], t1[b] = b, a; t2 = list(range(5)); t2[c], t2[d] = d, c
        t1, t2 = tuple(t1), tuple(t2)
        g = perm_mul(t1, t2)
        ok &= g == perm_mul(t2, t1)                                               # they commute
        left = ({0, 1, 2, 3, 4} - {a, b, c, d}).pop()
        ok &= g[left] == left and all(g[x] != x for x in range(5) if x != left)
        refl_ = tuple((2 * left - x) % 5 for x in range(5))                        # the pentagon's symmetry at that corner
        ok &= g == refl_
        gens.append(g)
    G = gen_group(gens)
    rots = [p for p in G if all(p[x] != x for x in range(5))]
    keep1 = [p for p in G if sum(p[x] == x for x in range(5)) == 1]
    ok &= len(G) == 10 and len(rots) == 4 and len(keep1) == 5
    return ok


def M152():
    def mono_tri(n, col, pairs):
        idx = {p: k for k, p in enumerate(pairs)}
        return any(col[idx[(a, b)]] == col[idx[(a, c)]] == col[idx[(b, c)]] for a, b, c in combinations(range(n), 3))
    p6 = list(combinations(range(6), 2))
    ok = all(mono_tri(6, c, p6) for c in product((0, 1), repeat=15))
    p5 = list(combinations(range(5), 2))
    free = [c for c in product((0, 1), repeat=10) if not mono_tri(5, c, p5)]
    ok &= len(free) == 12
    for c in free:
        for colour in (0, 1):
            es = [p for k, p in enumerate(p5) if c[k] == colour]
            deg = [sum(1 for e in es if v in e) for v in range(5)]
            ok &= len(es) == 5 and deg == [2] * 5 and connected(5, es)            # a five-cycle: pentagon, and pentagram
    return ok


def M156():
    order = (2 ** 46) * (3 ** 20) * (5 ** 9) * (7 ** 6) * (11 ** 2) * (13 ** 3) * 17 * 19 * 23 * 29 * 31 * 41 * 47 * 59 * 71
    ok = order == 808017424794512875886459904961710757005754368000000000
    ps = [p for p in range(2, 72) if all(p % q for q in range(2, isqrt(p) + 1)) and order % p == 0]
    ok &= len(ps) == 15 and ps[0] == 2 and ps[-1] == 71
    upto59 = [p for p in range(2, 60) if all(p % q for q in range(2, isqrt(p) + 1))]
    ok &= len(upto59) == 17 and sorted(set(upto59) - set(ps)) == [37, 43, 53] and 71 in ps
    # j = E4^3 / Delta: its coefficient at the first power of q
    N = 4
    sig3 = lambda n: sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
    E4 = [1] + [240 * sig3(n) for n in range(1, N + 2)]
    def mul(a, b):
        return [sum(a[i] * b[k - i] for i in range(k + 1) if i < len(a) and k - i < len(b)) for k in range(N + 2)]
    E43 = mul(mul(E4, E4), E4)
    D = [1] + [0] * (N + 1)                                             # Delta / q = prod (1 - q^n)^24
    for n in range(1, N + 2):
        for _ in range(24):
            D = [D[k] - (D[k - n] if k >= n else 0) for k in range(N + 2)]
    inv = [Fr(1)] + [Fr(0)] * (N + 1)                                   # 1 / (Delta/q)
    for k in range(1, N + 2):
        inv[k] = -sum(D[i] * inv[k - i] for i in range(1, k + 1))
    jq = mul(E43, inv)                                                  # q * j: coefficients of q^-1, q^0, q^1, ...
    ok &= jq[0] == 1 and jq[1] == 744 and jq[2] == 196884 == 196883 + 1
    return ok


# ---------------------------------------------------------------- field instances (the links stay field)
def FI_four_sq():
    N = 300
    r4 = [0] * (N + 1)
    lim = isqrt(N)
    for a, b, c, d in product(range(-lim, lim + 1), repeat=4):
        n = a * a + b * b + c * c + d * d
        if n <= N: r4[n] += 1
    ok = True
    for n in range(1, N + 1):
        divs = [k for k in range(1, n + 1) if n % k == 0]
        want = 8 * sum(divs) if n % 2 else 24 * sum(k for k in divs if k % 2)
        ok &= r4[n] == want and r4[n] > 0
    return ok and 8 == 3 ** 2 - 1 and 24 == 5 ** 2 - 1


def FI_e8():
    roots = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((1, -1), repeat=2):
            v = [0] * 8; v[i] = a; v[j] = b; roots.add(tuple(Fr(x) for x in v))
    for sg in product((1, -1), repeat=8):
        if sg.count(-1) % 2 == 0: roots.add(tuple(Fr(x, 2) for x in sg))
    return len(roots) == 240 and all(sum(x * x for x in v) == 2 for v in roots)


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'M\d+', k) and callable(v)}
# field instances: the link named stays at standing field; these check the instances its text names
FIELD_INSTANCES = {'M46': FI_quat, 'M143': FI_four_sq, 'M146': FI_e8}

if __name__ == '__main__':
    res = {}
    for k in sorted(CHECKS, key=lambda s: int(s[1:])):
        try: res[k] = bool(CHECKS[k]())
        except Exception as e: res[k] = f'error: {e!r}'
        print(k, res[k])
    for k, f in FIELD_INSTANCES.items():
        try: res[k + ' (field instances)'] = bool(f())
        except Exception as e: res[k + ' (field instances)'] = f'error: {e!r}'
        print(k, '(field instances)', res[k + ' (field instances)'])
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ccl_math_check_results.json')
    json.dump(res, open(out, 'w'), indent=1)
