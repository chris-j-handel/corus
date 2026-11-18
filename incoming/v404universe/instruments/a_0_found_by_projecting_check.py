"""A 0 found by projecting: two on a round, their lines drawn back and forward.

This reads no file and writes none. Each case is by whole numbers and their ratios. The turnings
tried are six, a tried part of an unending relation; each line below is an identity of (c, s)
with c·c + s·s = 1, said with the tried.

Beside a gathered note of another session: a self's 0, its location, found by drawing a self's
lines of pointing back until they meet; and three 0s on the plane between two facing cones.

  1  each one's line of up, drawn back; each one's forward arrow, drawn on
  2  the between, the surface's place and the spot: three on one line, an inversion
  3  sixty and thirty: sharing and opening
  4  a cone from a sphere's 0 around a same sphere
  5  a cubic packing, about the line to one touching

Run:  python3 -I a_0_found_by_projecting_check.py
"""
from fractions import Fraction as Fr


def main():
    fails = 0
    rho = Fr(3)
    tried = [(Fr(4, 5), Fr(3, 5)), (Fr(12, 13), Fr(5, 13)), (Fr(40, 41), Fr(9, 41)),
             (Fr(3, 5), Fr(4, 5)), (Fr(15, 17), Fr(8, 17)), (Fr(21, 29), Fr(20, 29))]
    print("1 and 2  two on a round of 3, a turning of (c, s) each side of the place midway")
    for c, s in tried:
        A, B = (rho * c, rho * s), (rho * c, -rho * s)
        up_A, up_B = (c, s), (c, -s)
        # each one's line of up, drawn back: A − t·up_A; the two meet with t of rho, the round's centre
        back_A = tuple(a - rho * u for a, u in zip(A, up_A))
        back_B = tuple(b - rho * u for b, u in zip(B, up_B))
        centre = back_A == back_B == (0, 0)
        # each one's forward arrow, drawn on: the two meet at the spot
        fwd_A, fwd_B = (s, -c), (s, c)
        t = rho * s / c
        on_A = tuple(a + t * f for a, f in zip(A, fwd_A))
        on_B = tuple(b + t * f for b, f in zip(B, fwd_B))
        spot = on_A == on_B == (rho / c, 0)
        between, place = rho * c, rho
        inversion = between * (rho / c) == place * place
        order = between < place < rho / c
        print(f"  ({c}, {s}): the two lines of up, drawn back, at one 0, the round's centre: {centre}; the two forward arrows, drawn on, at one spot: {spot}")
        print(f"    from that 0: the between {between}, the surface's place {place}, the spot {rho / c}, on one line in this order: {order}; the between by the spot is the place by the place: {inversion}")
        fails += not (centre and spot and inversion and order)
    print("  the between and the spot are one inversion apart in the round, the surface's place the same by it")

    print("\n3  sixty and thirty, by squares")
    c60, s60 = Fr(1, 4), Fr(3, 4)      # cosine squared, sine squared of sixty
    c30, s30 = Fr(3, 4), Fr(1, 4)
    print(f"  two directions sixty apart, a cone's two edges: sharing squared {c60}, opening squared {s60}")
    print(f"  an edge and its centerline, thirty apart: sharing squared {c30}, opening squared {s30}")
    print(f"  the two exchanged: {c60 == s30 and s60 == c30}; three of four and one of four")
    fails += not (c60 == s30 and s60 == c30)

    print("\n4  a cone from a sphere's 0 around a same sphere")
    for d, name in ((Fr(2), "touching"), (Fr(5, 2), "apart by a quarter of one"), (Fr(4), "apart by one")):
        sine2 = (Fr(1) / d) ** 2                     # radius 1, centres d apart: sine squared of its half opening
        print(f"  two same spheres {name}: sine squared of a cone's opening from its line {sine2}; thirty each side, sixty across: {sine2 == Fr(1, 4)}")
        fails += (sine2 == Fr(1, 4)) != (d == 2)
    from itertools import permutations, product
    twelve = sorted({p for s in product((1, -1), repeat=2) for p in permutations((s[0], s[1], 0))})
    cos2 = {Fr((a[0]*b[0] + a[1]*b[1] + a[2]*b[2]) ** 2, 4) for a in twelve for b in twelve if a != b and a[0]*b[0] + a[1]*b[1] + a[2]*b[2] > 0}
    touching = sorted({sum(1 for b in twelve if a != b and a[0]*b[0] + a[1]*b[1] + a[2]*b[2] == 1) for a in twelve})
    print(f"  twelve same spheres around one: each one's line sixty from {touching} others' lines, cosine squared {min(cos2)}; twelve cones of sixty across, each with four others edge to edge, none crossing")
    fails += touching != [4] or min(cos2) != Fr(1, 4)
    # with φ: lines (0, 1, φ) and (1, φ, 0): cosine φ / (2 + φ); sixty or wider with 4φφ <= (2 + φ)(2 + φ), which is 0 <= 1 + φ
    print("  twelve with φ: cosine of two lines φ by 2 + φ; four of φφ less than 2 + φ by 2 + φ, by 1 + φ: wider than sixty, twelve cones of sixty with none edge to edge")
    six = 6 * 60
    print(f"  six cones of sixty across round one 0 on a plane: {six} of 360, a whole turn: {six == 360}")

    print("\n5  a cubic packing, about the line to one touching: each other out to distance squared 18")
    packed = [p for p in product(range(-6, 7), repeat=3) if sum(p) % 2 == 0 and p != (0, 0, 0)]
    line = (1, 1, 0)
    found = {}
    for p in packed:
        n2 = sum(x * x for x in p)
        along = sum(x * y for x, y in zip(p, line))
        if n2 > 18 or along <= 0:
            continue
        c2 = Fr(along * along, n2 * 2)
        kind = "on its line" if c2 == 1 else "between its edges" if c2 > Fr(3, 4) else "on an edge" if c2 == Fr(3, 4) else None
        if kind:
            found.setdefault(n2, {}).setdefault(kind, 0)
            found[n2][kind] += 1
    for n2 in sorted(found):
        says = ", ".join(f"{v} {k}" for k, v in found[n2].items())
        print(f"  distance squared {n2}: {says}; each one's own cone, sine squared from its line {Fr(1, 2) / n2}")
    fails += found != {2: {"on its line": 1}, 6: {"on an edge": 4}, 8: {"on its line": 1}, 10: {"between its edges": 2},
                       14: {"between its edges": 4}, 18: {"on its line": 1}}
    print("  the one touching fills the cone; each other apart is beyond it, a narrower cone")

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
