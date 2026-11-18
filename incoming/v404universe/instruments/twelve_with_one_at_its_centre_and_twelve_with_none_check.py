"""Twelve corners with one at its centre, and twelve with none.

This reads no file and writes none. Each count is by whole numbers and their ratios, and by
numbers a + b·φ with φ·φ = φ + 1.

Twelve corners are (0, ±1, ±r) and its two turns, (±r, 0, ±1) and (±1, ±r, 0): three
rectangles, 2 by 2r, each through the two others. Exhibit THIRTY has them with a ratio r.

  r of 1    a field's twelve around one, its cuboctahedron
  r of φ    twelve with five nearest each, a field's icosahedron

Run:  python3 -I twelve_with_one_at_its_centre_and_twelve_with_none_check.py
"""
from fractions import Fraction as Fr
from itertools import combinations, product


class N:
    """a + b·φ, a and b ratios of whole numbers."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(s, o): o = n(o); return N(s.a + o.a, s.b + o.b)
    def __sub__(s, o): o = n(o); return N(s.a - o.a, s.b - o.b)
    def __neg__(s): return N(-s.a, -s.b)
    def __mul__(s, o):
        o = n(o)
        return N(s.a * o.a + s.b * o.b, s.a * o.b + s.b * o.a + s.b * o.b)

    def sign(s):
        p, q = 2 * s.a + s.b, s.b            # a + bφ = (p + q√5) / 2
        if p >= 0 and q >= 0: return 0 if (p == 0 and q == 0) else 1
        if p <= 0 and q <= 0: return -1
        d = p * p - 5 * q * q
        d = d if p > 0 else -d
        return (d > 0) - (d < 0)

    def __eq__(s, o): return (s - n(o)).sign() == 0
    def __lt__(s, o): return (s - n(o)).sign() < 0
    def __hash__(s): return hash((s.a, s.b))

    def __repr__(s):
        if s.b == 0: return str(s.a)
        many = "" if abs(s.b) == 1 else str(abs(s.b))
        if s.a == 0: return f"{'−' if s.b < 0 else ''}{many}φ"
        return f"{s.a} {'−' if s.b < 0 else '+'} {many}φ"


def n(x): return x if isinstance(x, N) else N(x)


PHI = N(0, 1)


def twelve(r, other_hand=False):
    r = n(r); out = []
    for s, t in product((1, -1), repeat=2):
        one, rr = N(s), r * t
        base = (N(0), rr, one) if other_hand else (N(0), one, rr)
        for k in range(3):
            out.append(tuple(base[(i - k) % 3] for i in range(3)))
    return out


def d2(p, q): return sum(((a - b) * (a - b) for a, b in zip(p, q)), N(0))
def dot(u, v): return sum((a * b for a, b in zip(u, v)), N(0))
def sub(p, q): return tuple(a - b for a, b in zip(p, q))


def read(r, name):
    P = twelve(r)
    assert len(set(P)) == 12
    O = (N(0), N(0), N(0))
    pairs = list(combinations(range(12), 2))
    near = min((d2(P[i], P[j]) for i, j in pairs), key=lambda x: (x - N(0)).a + (x - N(0)).b * Fr(1618, 1000))
    for i, j in pairs: assert not d2(P[i], P[j]) < near
    E = [(i, j) for i, j in pairs if d2(P[i], P[j]) == near]
    each = sorted({sum(1 for e in E if k in e) for k in range(12)})
    Eset = set(E)
    T = [t for t in combinations(range(12), 3) if all(p in Eset for p in combinations(t, 2))]
    S = []
    for q in combinations(range(12), 4):
        inside = [p for p in combinations(q, 2) if p in Eset]
        if len(inside) == 4 and all(sum(1 for p in inside if k in p) == 2 for k in q):
            S.append(q)
    centre = {d2(p, O) for p in P}
    assert len(centre) == 1
    c = centre.pop()
    print(f"\n{name}")
    print(f"  nearest two corners, distance squared: {near}; touchings: {len(E)}; each corner touching: {each}")
    print(f"  threes: {len(T)}; fours: {len(S)}; corners less touchings and faces: {12 - len(E) + len(T) + len(S)}")
    print(f"  the centre to each corner, distance squared: {c}")
    if c == near:
        print("  the centre is as far from each corner as a corner from its nearest: one same sphere is at the centre, touching twelve")
    elif c < near:
        print("  the centre is nearer each corner than a corner its nearest: no same sphere is at the centre")
    else:
        print("  the centre is further from each corner than a corner its nearest: a same sphere at the centre touches none")
    # each corner's missing angle, a regular three's corner 60 and a square's 90
    for t in T:
        assert len({d2(P[a], P[b]) for a, b in combinations(t, 2)}) == 1
    for q in S:
        a = q[0]; nb = [k for k in q if (min(a, k), max(a, k)) in Eset]
        assert dot(sub(P[nb[0]], P[a]), sub(P[nb[1]], P[a])) == 0
    miss = sorted({360 - 60 * sum(1 for t in T if k in t) - 90 * sum(1 for q in S if k in q) for k in range(12)})
    print(f"  each corner's faces are less than a whole turn by: {miss} of 360; twelve corners: {12 * miss[0]}")
    return len(E), len(T), len(S), 12 * miss[0]


print("Twelve corners, (0, ±1, ±r) and its two turns")
a = read(1, "r of 1")
b = read(PHI, "r of φ")
assert a == (24, 8, 6, 720) and b == (30, 20, 0, 720)

print("\nBetween the two, r of 5/4, 3/2")
for r in (Fr(5, 4), Fr(3, 2)):
    P = twelve(r)
    ds = sorted({(d2(P[i], P[j]).a) for i, j in combinations(range(12), 2)})
    c = d2(P[0], (N(0),) * 3).a
    print(f"  r {r}: twenty-four at distance squared {ds[0]}, six at {ds[1]}; the centre to each corner {c}")
    assert ds[1] == 4 and sum(1 for i, j in combinations(range(12), 2) if d2(P[i], P[j]).a == ds[0]) == 24

print("\nThe centre and a corner's nearest, with r from 1 to φ")
for r in (N(1), N(Fr(9, 8)), N(Fr(5, 4)), N(Fr(3, 2)), N(Fr(8, 5)), PHI):
    P = twelve(r)
    between = d2((N(0), N(1), r), (r, N(0), N(1)))          # a corner of one rectangle and its next
    assert between == (r * r - r + 1) * 2
    centre = d2(P[0], (N(0),) * 3)
    less = between - centre
    assert less == (r - 1) * (r - 1)
    print(f"  r {r}: a corner to its nearest {between}, the centre to a corner {centre}, less by {less}")
print("  less by (r − 1)·(r − 1) with each: nought with r of 1 alone")

print("\nA square of r of 1 closing: its two across lines")
P = twelve(1); sq = ((N(0), N(1), N(1)), (N(1), N(0), N(1)), (N(0), N(-1), N(1)), (N(-1), N(0), N(1)))
assert all(p in P for p in sq)
for r, nm in ((N(1), "1"), (PHI, "φ")):
    A, B = (N(0), N(1), r), (N(0), N(-1), r)
    C, D = (r, N(0), N(1)), (-r, N(0), N(1))
    print(f"  r of {nm}: one across line {d2(A, B)}, the other {d2(C, D)}, a side {d2(A, C)}")
print("  one across line stays 4 and a side comes to it with φ: each square closes as two threes, eight and twelve are twenty")

print("\nThe closing's two hands")
A, B = set(twelve(PHI)), set(twelve(PHI, other_hand=True))
step = {(p[1], -p[0], p[2]) for p in A}
mirror = {(-p[0], p[1], p[2]) for p in A}
print(f"  the two are the same twelve: {A == B}; a right spiral step, (x, y) to (y, −x), brings one onto the other: {step == B}")
print(f"  a mirror, x to −x, brings each onto its own place: {mirror == A}")
assert A != B and step == B and mirror == A

print("\nA torus of squares, m by n, opposite sides joined")
for m, k in ((3, 3), (4, 6)):
    V, E, F = m * k, 2 * m * k, m * k
    print(f"  {m} by {k}: corners {V}, touchings {E}, faces {F}; corners less touchings and faces: {V - E + F}; each corner four squares, less than a whole turn by {360 - 4 * 90}")
    assert V - E + F == 0

print("\nRead")
print("  twelve corners of either form are each a sixth of a turn less than a whole: 720, two whole turns, with 2 by corners, touchings and faces")
print("  a torus's corners are less by none, with 0")
print("  with r of 1 one same sphere is at the centre; with φ no same sphere is")
print("fails: 0")
