"""A sphere from a 0 as a cone, and two cones crossing, by whole numbers and fractions.

A sphere, and a 0 outside it: the lines from the 0 touching the sphere are a
cone. This instrument tries three crossings of two such cones, and says of
each whether the crossing is flat, in a plane.

  1  two same spheres touching, each one's cone from its centre around its other
  2  two 0s and one same sphere, a cone from each 0 around it
  3  two 0s and two spheres, a cone from each 0 around its own sphere

With one mix of the two cones being two planes together, the crossing is in
those planes. With no such mix it is in no two planes. The instrument looks
for each such mix, exactly.

It reads no file and writes none.

Run:  python3 -I incoming/v404universe/instruments/two_cones_crossing_check.py
"""
from fractions import Fraction as F
from itertools import product


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cone_value(apex, centre, r2, x):
    """nought with, and only with, x on the cone from the apex touching the sphere."""
    p, v = minus(apex, centre), minus(x, centre)
    return (dot(p, v) - r2) ** 2 - (dot(p, p) - r2) * (dot(v, v) - r2)


def cone_matrix(apex, centre, r2):
    """the cone as a four by four table, by its values at whole-number places."""
    pts = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    f = lambda x: F(cone_value(apex, centre, r2, tuple(F(c) for c in x)))
    m = [[F(0)] * 4 for _ in range(4)]
    m[3][3] = f((0, 0, 0))
    for i in range(3):
        e = tuple(1 if k == i else 0 for k in range(3))
        n = tuple(-c for c in e)
        m[i][i] = (f(e) + f(n)) / 2 - m[3][3]
        m[i][3] = m[3][i] = (f(e) - f(n)) / 4
    for i in range(3):
        for j in range(i + 1, 3):
            e = tuple(1 if k in (i, j) else 0 for k in range(3))
            m[i][j] = m[j][i] = (f(e) - m[i][i] - m[j][j] - 2 * m[i][3] - 2 * m[j][3] - m[3][3]) / 2
    return m


# polynomials in t, a list of fractions, lowest first
def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmod(a, b):
    a = trim(a)
    while len(a) >= len(b) and a != [0]:
        k = a[-1] / b[-1]
        shift = len(a) - len(b)
        a = trim([a[i] - (k * b[i - shift] if i >= shift else 0) for i in range(len(a))])
        if len(a) == 1 and a[0] == 0:
            break
    return a


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, pmod(a, b)
    return [c / a[-1] for c in a] if a != [0] else a


def det3(m):
    def d2(a, b, c, d):
        return padd(pmul(a, d), [-x for x in pmul(b, c)])
    t0 = pmul(m[0][0], d2(m[1][1], m[1][2], m[2][1], m[2][2]))
    t1 = pmul(m[0][1], d2(m[1][0], m[1][2], m[2][0], m[2][2]))
    t2 = pmul(m[0][2], d2(m[1][0], m[1][1], m[2][0], m[2][1]))
    return padd(padd(t0, [-x for x in t1]), t2)


def mixes_being_two_planes(m1, m2):
    """the degree of what each three by three part of (first less t of the second) shares:
    nought says no mix is two planes, and the crossing is in no planes."""
    pencil = [[[m1[i][j], -m2[i][j]] for j in range(4)] for i in range(4)]
    shared = [F(0)]
    for rows in product(range(4), repeat=1):
        for cols in range(4):
            sub = [[pencil[i][j] for j in range(4) if j != cols] for i in range(4) if i != rows[0]]
            shared = pgcd(shared, det3(sub)) if shared != [0] else trim(det3(sub))
    return len(shared) - 1, shared


def say(title, m1, m2):
    degree, shared = mixes_being_two_planes(m1, m2)
    flat = degree > 0
    print(f"\n{title}")
    print(f"  a mix of the two cones is two planes together: {flat}")
    if flat and degree == 1:
        print(f"    the mix: the first less {-shared[0] / shared[1]} of the second")
    print(f"  the crossing is flat, in planes: {flat}")


def main():
    one = F(1)
    # 1 two same spheres touching
    a, b = (F(-1), F(0), F(0)), (F(1), F(0), F(0))
    half_opening_sine_squared = one / dot(minus(a, b), minus(a, b))
    print("two same spheres touching, each one's cone from its centre around its other")
    print(f"  the sine of a cone's half opening, squared: {half_opening_sine_squared}, a half opening of thirty")
    fails = 0
    for x in product(range(-3, 4), repeat=3):
        x = tuple(F(c) for c in x)
        if cone_value(a, b, one, x) - cone_value(b, a, one, x) != 4 * x[0]:
            fails += 1
    print(f"  the one cone less the other is four of the place along the line of centres: fails {fails}")
    print("  so the two cross with that place nought only: the plane between the two")
    fails = 0
    for y, z in product(range(-3, 4), repeat=2):
        if cone_value(a, b, one, (F(0), F(y), F(z))) != 1 - 3 * (y * y + z * z):
            fails += 1
    print(f"  in that plane a cone is nought with a distance squared of {F(1, 3)} from the point touching: fails {fails}")
    print("  the crossing is one circle around the point of the two touching")
    say("1  two same spheres touching", cone_matrix(a, b, one), cone_matrix(b, a, one))

    # 2 two 0s, one same sphere
    centre = (F(0), F(0), F(0))
    p, q = (F(1), F(1), F(0)), (F(0), F(1), F(2))
    ka, kb = dot(p, p) - 1, dot(q, q) - 1
    fails = 0
    for x in product(range(-4, 5), repeat=3):
        x = tuple(F(c) for c in x)
        lp, lq = dot(p, x) - 1, dot(q, x) - 1
        left = kb * cone_value(p, centre, one, x) - ka * cone_value(q, centre, one, x)
        if left != (2 * lp - lq) * (2 * lp + lq):
            fails += 1
    print("\ntwo 0s and one same sphere")
    print(f"  four of the first cone less the second is two planes together, at each of 729 places: fails {fails}")
    say("2  two 0s and one same sphere", cone_matrix(p, centre, one), cone_matrix(q, centre, one))

    # 3 two 0s, two spheres
    p3, c3 = (F(2), F(0), F(0)), (F(0), F(0), F(0))
    q3, d3 = (F(1), F(-2), F(2)), (F(0), F(3), F(1))
    say("3  two 0s and two spheres, each cone around its own", cone_matrix(p3, c3, one), cone_matrix(q3, d3, one))


if __name__ == "__main__":
    main()
