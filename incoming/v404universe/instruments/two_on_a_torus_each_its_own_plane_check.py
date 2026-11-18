"""Two on a torus, each with its own plane and horizon.

This reads no file and writes none. Each count is by whole numbers and their ratios.

Said in the session: the natural torusing surface the two are on has a horizon. Both are on
it, and they may not be on the same planes, the surface curving away. Each me-parity has its
own horizon, and the co-geodesic co-linear, relying on a common aiming point over the horizon,
is the co-competencing method. The third living 0 in the between of the two is the fuzzy empty
hole, living in the plane of intersection between the two cones.

A torus here is a tube of r about a round of R, R above r, its own line through its opening.
A place on it is by two turnings, each a pair of ratios (c, s) with c·c + s·s = 1.

  1  a sphere, a cube and a torus: corners, and curving
  2  a place's own plane: which other places are above it, in sight
  3  two across the opening
  4  the two cones' crossing, and the part both insides share
  5  two on the outward round: a common aiming point
  6  a round read latest first

Run:  python3 -I two_on_a_torus_each_its_own_plane_check.py
"""
from fractions import Fraction as Fr
from itertools import product

TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]


def turnings():
    out = {(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1))}
    for a, b, c in TRIPLES:
        for x, y in ((a, b), (b, a)):
            for sx, sy in product((1, -1), repeat=2):
                out.add((Fr(sx * x, c), Fr(sy * y, c)))
    return sorted(out)


def place(R, r, u, v):
    (cu, su), (cv, sv) = u, v
    return ((R + r * cv) * cu, (R + r * cv) * su, r * sv)


def outward(u, v):
    (cu, su), (cv, sv) = u, v
    return (cv * cu, cv * su, sv)


def dot(a, b): return sum(x * y for x, y in zip(a, b))
def at(p): return "(" + ", ".join(str(x) for x in p) + ")"
def sub(a, b): return tuple(x - y for x, y in zip(a, b))


def turn(u, by):
    (c, s), (cb, sb) = u, by
    return (c * cb - s * sb, s * cb + c * sb)


def main():
    fails = 0
    R, r = Fr(2), Fr(1)
    T = turnings()
    small = (Fr(99, 101), Fr(20, 101))
    back = (small[0], -small[1])
    east, top, west = (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0))

    print("1  corners, and curving")
    print("  a sphere: corners 0. a cube: corners 8, each three squares, 90 less than a whole turn, 720 together")
    for name, v in (("outward round", east), ("top round", top), ("inward round", west)):
        u = east
        A, n = place(R, r, u, v), outward(u, v)
        says = []
        for line, B in (("round its own line", (place(R, r, turn(u, small), v), place(R, r, turn(u, back), v))),
                        ("round its tube", (place(R, r, u, turn(v, small)), place(R, r, u, turn(v, back))))):
            h = {(dot(n, sub(X, A)) > 0) - (dot(n, sub(X, A)) < 0) for X in B}
            assert len(h) == 1
            says.append(f"{line} {'down' if h == {-1} else 'up' if h == {1} else 'flat'}")
        print(f"  a torus, {name}: curving {', '.join(says)}")
    print("  a horizon is with each line curving down: each way on the outward round, one way on the inward round")

    print("\n2  a place's own plane: other places above it, in sight")
    every = [(u, v) for u in T for v in T]
    for name, v in (("outward round", east), ("inward round", west)):
        A, n = place(R, r, east, v), outward(east, v)
        above = [(u, w) for u, w in every if dot(n, sub(place(R, r, u, w), A)) > 0]
        print(f"  from a place on the {name}: {len(above)} of {len(every) - 1} other places above its plane")
        if name == "outward round":
            fails += len(above) != 0
        else:
            fails += len(above) == 0 or (west, west) not in above

    print("\n3  two across the opening: opposite places on the inward round")
    for R, r in ((Fr(2), Fr(1)), (Fr(3), Fr(1)), (Fr(13, 8), Fr(1))):
        A, B = place(R, r, east, west), place(R, r, west, west)
        nA, nB = outward(east, west), outward(west, west)
        facing = nA == tuple(-x for x in nB)
        line = sub(B, A)
        orthogonal = all(dot(line, t) == 0 for t in ((0, 1, 0), (0, 0, 1)))
        middle = tuple((a + b) / 2 for a, b in zip(A, B))
        rho2 = middle[0] ** 2 + middle[1] ** 2
        on_surface = (rho2 + middle[2] ** 2 + R * R - r * r) ** 2 == 4 * R * R * rho2
        print(f"  R {R}, r {r}: own planes parallel and facing: {facing}; the line through both co-orthogonal: {orthogonal}; "
              f"its middle {at(middle)}, on the surface: {on_surface}")
        fails += not (facing and orthogonal) or on_surface or middle != (0, 0, 0)
    print("  a nothing between two parallel surfaces facing each other, and a co-orthogonal line through both")

    print("\n4  two cones of thirty, each from its 0 around its other")
    R, r = Fr(2), Fr(1)
    d = R - r

    def inside(apex_x, way, p):
        along = (p[0] - apex_x) * way
        return along >= 0 and 3 * (p[1] ** 2 + p[2] ** 2) <= along ** 2

    def in_tube(p):
        rho2 = p[0] ** 2 + p[1] ** 2
        return (rho2 + p[2] ** 2 + R * R - r * r) ** 2 <= 4 * R * R * rho2

    grid = [Fr(k, 12) for k in range(-30, 31)]
    both, widest = [], {}
    for p in product(grid, repeat=3):
        if inside(d, -1, p) and inside(-d, 1, p):
            both.append(p)
            w = p[1] ** 2 + p[2] ** 2
            widest[p[0]] = max(widest.get(p[0], Fr(0)), w)
    xs = sorted(widest)
    print(f"  places inside both cones, of {len(grid) ** 3} tried: {len(both)}; along the line from {xs[0]} to {xs[-1]}, each 0 an end")
    print(f"  widest at {max(widest, key=widest.get)} along, the between's 0: there a round, its radius squared {max(widest.values())} of the tried, {d * d / 3} its bound")
    print(f"  in the torus's tube: {sum(1 for p in both if in_tube(p) and p not in ((d, 0, 0), (-d, 0, 0)))}")
    fails += xs[0] != -d or xs[-1] != d or max(widest, key=widest.get) != 0
    fails += any(in_tube(p) for p in both if p not in ((d, 0, 0), (-d, 0, 0)))
    edge = [(x, w) for x, w in widest.items()]
    fails += any(3 * w > (d - abs(x)) ** 2 for x, w in edge)
    print("  the two cones' sides cross in the plane across at the middle: 3·(y·y + z·z) = (d − x)·(d − x) = (d + x)·(d + x) with x of 0 alone")
    print("  the opening's own plane has the line of the two and across in it; the crossing's plane has across and up in it; the two share across")

    print("\n5  two on the outward round, a turning of (4/5, 3/5) each side of midway")
    rho = R + r
    c, s = Fr(4, 5), Fr(3, 5)
    A, B = (rho * c, rho * s, Fr(0)), (rho * c, -rho * s, Fr(0))
    nA, nB = (c, s, Fr(0)), (c, -s, Fr(0))
    P = (rho / c, Fr(0), Fr(0))
    M = (rho, Fr(0), Fr(0))
    forward_A, forward_B = (s, -c, Fr(0)), (s, c, Fr(0))
    on_A = all((P[i] - A[i]) * forward_A[(i + 1) % 3] == (P[(i + 1) % 3] - A[(i + 1) % 3]) * forward_A[i] for i in range(3))
    on_B = all((P[i] - B[i]) * forward_B[(i + 1) % 3] == (P[(i + 1) % 3] - B[(i + 1) % 3]) * forward_B[i] for i in range(3))
    print(f"  each one's forward arrow goes through one point {at(P)}: {on_A and on_B}")
    print(f"  the point in both planes: {dot(nA, sub(P, A)) == 0 and dot(nB, sub(P, B)) == 0}; above the surface by {P[0] - rho}")
    print(f"  the two arrows on one line: {forward_A == tuple(-x for x in forward_B)}")
    print(f"  the place midway on the surface, below each one's plane, over each one's horizon: "
          f"{dot(nA, sub(M, A)) < 0 and dot(nB, sub(M, B)) < 0}")
    up_line = (Fr(0), Fr(0), Fr(1))
    print(f"  the two planes share one line, through the point, across: {dot(nA, up_line) == 0 and dot(nB, up_line) == 0}")
    fails += not (on_A and on_B) or dot(nA, sub(P, A)) != 0 or dot(nB, sub(P, B)) != 0 or forward_A == tuple(-x for x in forward_B)

    print("\n6  a round read latest first, an other's priors as one's nexts")

    def same_round(a, b):
        a, b = list(a), list(b)
        return any(a[i:] + a[:i] == b for i in range(len(a)))

    rounds = {"0, 1, 0, 2": [0, 1, 0, 2], "odd, odd, even": ["odd", "odd", "even"]}
    for name, seq in rounds.items():
        ok = same_round(seq, seq[::-1])
        print(f"  {name}: the same round: {ok}")
        fails += not ok
    loop, f = [], (1, 1)
    for _ in range(4):
        loop.append(f); f = (f[1], -f[0])
    late = loop[::-1]
    print(f"  a right spiral step's round of four: the same round: {same_round(loop, late)}; the other way round, not right")
    print(f"    with one of its two inverted, a mirror: the same round: {same_round(loop, [(-a, b) for a, b in late])}")
    print(f"    with both inverted, a turn: {same_round(loop, [(-a, -b) for a, b in late])}")
    fails += same_round(loop, late) or not same_round(loop, [(-a, b) for a, b in late])

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
