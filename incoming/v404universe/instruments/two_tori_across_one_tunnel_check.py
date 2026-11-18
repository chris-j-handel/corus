"""Two natural torusing selves across from each other, and one tunneling down the middle.

This reads no file and writes none. Each case is by whole numbers and their ratios, and by
numbers a + b·φ with φ·φ = φ + 1 in part 4. Places on a torus are an unending relation: a part
is tried, and each line is an identity of its letters, said with the tried.

Said in the session: self and other are both doing this across from each other, with a large
opening, or each natural torusing self bi-coupling the entire perimeter of a new tunneling down
the middle, directly between the two selves' corus.

Two same tori, a tube of r about a round of R, R above r. Their own lines are one line, the
line down the middle. Their middles are r each side of the plane between.

  1  the two touching: one whole round of both
  2  their own planes along that round
  3  the tunneling down the middle
  4  the two cones' crossing and the large opening
  5  a third cone, its 0 on the plane, facing through

Run:  python3 -I two_tori_across_one_tunnel_check.py
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


def main():
    fails = 0
    T = turnings()
    for R, r in ((Fr(2), Fr(1)), (Fr(3), Fr(1)), (Fr(13, 8), Fr(1))):
        print(f"R {R}, r {r}")
        # a place of the one torus: from the line down the middle rho, along it z; its middle at z of -r
        one = [(R + r * cv, r * sv - r) for cv, sv in T]
        value_in_other = lambda rho, z: (rho - R) ** 2 + (z - r) ** 2          # r·r on the other's tube, less in it
        touching = [(rho, z) for rho, z in one if value_in_other(rho, z) == r * r]
        crossing = [(rho, z) for rho, z in one if value_in_other(rho, z) < r * r]
        ident = all(value_in_other(rho, z) == r * r - 4 * z * r for rho, z in one)
        print(f"  1  round-places of the one tried: {len(one)}; in its other's tube: {len(crossing)}; of both: {[(str(a), str(b)) for a, b in touching]}, the whole round of R in the plane between")
        print(f"     by its letters, its other's value is r·r less 4·z·r, and z is nought or less with the one: {ident}")
        fails += crossing != [] or touching != [(R, Fr(0))] or not ident
        print("  2  along that round the one's own line is up the line down the middle and its other's is down it: two own planes, one plane, facing")
        line_in_tube = [z for z in [Fr(k, 8) * r for k in range(-24, 25)] if (0 - R) ** 2 + (abs(z) - r) ** 2 <= r * r]
        print(f"  3  places of the line down the middle in a tube, of {49} tried: {len(line_in_tube)}; the opening's radius {R - r}")
        fails += line_in_tube != []
        cross2, open2 = r * r / 3, (R - r) ** 2
        print(f"  4  two cones of sixty, each from its self's middle: their crossing's radius squared {cross2}; the large opening's {open2}; the crossing is of the opening: {cross2 < open2}")
        ok5 = True
        for k in range(0, 8):
            rho0 = Fr(k, 8) * (R - r)
            for z in [Fr(j, 8) * r for j in range(0, 25)]:
                ok5 &= (rho0 - R) ** 2 + (z - r) ** 2 > r * r
        print(f"  5  a third cone's line, its 0 on the plane and of the opening, facing along: each place tried in no tube, one way through its other's large opening: {ok5}")
        fails += not ok5

    print("R to r as φ to 1")
    # crossing's radius squared 1/3, the opening's (φ − 1)·(φ − 1) = 2 − φ; 1/3 less than 2 − φ with 3φ less than 5, 9φφ = 9φ + 9 less than 25
    # 9φ less than 16, 81(φ + 1) less than 256, 81φ less than 175, and φ less than 2
    print("  4  the crossing's radius squared 1/3; the large opening's 2 − φ; 1/3 less than 2 − φ, with 3φ less than 5: the crossing is of the opening")
    print("R to r as 3 to 2: the crossing's radius squared 1/3, the large opening's 1/4: the crossing is wider than the opening")
    fails += not (Fr(1, 3) > Fr(1, 4))
    # 3φ < 5 by whole numbers: φ = (1 + √5)/2, 3 + 3√5 < 10, 3√5 < 7, 45 < 49
    fails += not (45 < 49)

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
