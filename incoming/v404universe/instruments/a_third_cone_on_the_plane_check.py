"""A third cone on the plane: a self's next now universe, facing through the hole.

This reads no file and writes none. Each case is by whole numbers and their ratios. Places on
the plane are an unending relation: a grid of them is tried, and each line is an identity of
its letters, said with the tried.

Said in the session: the two facing cones with a between are self and other-than self, in
self universe now. The third cone is self next now universe, on the plane, facing through the
hole in the plane, in the nearly same direction of self now, a prior-existing.

A self's 0 is at (−d, 0, 0), facing up the first line. Its other-than self's 0 is at (d, 0, 0),
facing down it. Each cone is of sixty, thirty each side of its line. The plane is across, with
the between's 0 in it. The hole is the round of the two cones' crossing, its radius squared
d·d by 3.

  1  the hole, and each cone's edges on the plane
  2  a third cone, its 0 on the plane, facing as self now
  3  its turning, to have its other on its line
  4  two same spheres, one beside its other, and the hole

Run:  python3 -I a_third_cone_on_the_plane_check.py
"""
from fractions import Fraction as Fr
from itertools import product


def between_edges(apex, way, p):
    """is p between the edges of a cone of sixty from apex, its line (way, 0, 0)? 1 yes, 0 on an edge, −1 no."""
    along = (p[0] - apex[0]) * way
    across2 = (p[1] - apex[1]) ** 2 + (p[2] - apex[2]) ** 2
    if along <= 0:
        return -1
    v = along * along - 3 * across2
    return (v > 0) - (v < 0)


def main():
    fails = 0
    d = Fr(1)
    self_now, other = (-d, Fr(0), Fr(0)), (d, Fr(0), Fr(0))
    grid = [Fr(k, 12) for k in range(-12, 13)]
    plane = [(Fr(0), y, z) for y, z in product(grid, repeat=2)]

    print("1  the hole, and each cone's edges on the plane")
    in_hole = lambda p: 3 * (p[1] ** 2 + p[2] ** 2) < d * d
    same = all((between_edges(self_now, 1, p) == 1) == in_hole(p) == (between_edges(other, -1, p) == 1) for p in plane)
    hole = [p for p in plane if in_hole(p)]
    print(f"  places tried on the plane: {len(plane)}; of the hole: {len(hole)}")
    print(f"  a place is of the hole, between self now's edges, and between its other-than self's edges, each with the two others: {same}")
    fails += not same

    print("\n2  a third cone, its 0 on the plane, facing as self now")
    ahead = all((between_edges(p, 1, other) == 1) == in_hole(p) for p in plane)
    behind = all((between_edges(p, -1, self_now) == 1) == in_hole(p) for p in plane)
    print(f"  with its 0 of the hole, its other-than self is between its edges ahead; with its 0 past the hole, it is not: {ahead}")
    print(f"  self now, a prior-existing, is between the edges of the same cone drawn back, with its 0 of the hole alone: {behind}")
    print("  by its letters: its other-than self is d ahead and its 0 is r from the between's 0; between its edges with 3·r·r less than d·d, the hole's own bound")
    fails += not (ahead and behind)

    print("\n3  its turning, to have its other-than self on its line")
    for p in ((Fr(0), Fr(0), Fr(0)), (Fr(0), Fr(1, 4), Fr(0)), (Fr(0), Fr(1, 2), Fr(0)), (Fr(0), Fr(7, 12), Fr(0))):
        tan2 = (p[1] ** 2 + p[2] ** 2) / (d * d)
        print(f"  its 0 at {tuple(str(x) for x in p)}: the square of its turning's tangent {tan2}; less than a third, thirty: {tan2 < Fr(1, 3)}")
        fails += (tan2 < Fr(1, 3)) != in_hole(p)
    print("  nought with its 0 the between's 0; less than thirty with each place of the hole: nearly the same direction")

    print("\n4  two same spheres of radius d, one beside its other, and the hole")
    beside2 = (2 * d) ** 2 / 4               # each centre d from the between's 0, squared
    print(f"  each one's 0 from the between's 0, squared: {beside2}; the hole's radius squared: {d * d / 3}; each of the hole: {beside2 < d * d / 3}")
    print("  two same spheres are not one beside its other with both 0s of the hole")
    fails += beside2 < d * d / 3

    print(f"\nfails: {fails}")


if __name__ == "__main__":
    main()
