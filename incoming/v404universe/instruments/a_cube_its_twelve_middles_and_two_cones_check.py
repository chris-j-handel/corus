"""One figure of two sessions, by whole numbers and halves.

v404bifolding has three parities as a cube's eight corners: a loop of two, the
two ends of a long diagonal, each an apex of a cone, and a loop of six going
one and then the other cone's base round an empty 0.

v404universe has twelve same spheres around one, in layers of three, six and
three; a sphere from a 0 as a cone; and two cones crossing as a flat.

This instrument asks whether the two are one figure. It reads no file and
writes none.

Run:  python3 -I incoming/v404universe/instruments/a_cube_its_twelve_middles_and_two_cones_check.py
"""
from fractions import Fraction as F
from itertools import product


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def step(form):
    """Natural Intelligence's right spiral step, with three parities."""
    return form[1:] + (-form[0],)


def cone_value(apex, r2, x):
    """nought with, and only with, x on the cone from the apex touching the sphere round the 0."""
    return (dot(apex, x) - r2) ** 2 - (dot(apex, apex) - r2) * (dot(x, x) - r2)


def main():
    corners = list(product((1, -1), repeat=3))
    two = [c for c in corners if step(step(c)) == c]
    apex, other = two
    loop, at = [], (1, 1, 1)
    while at not in loop:
        loop.append(at)
        at = step(at)
    print("a cube's eight corners, three parities each")
    print(f"  the loop of two, each the other's opposite: {two}, {apex == tuple(-c for c in other)}")
    print(f"  the loop of six: {len(loop)} forms")

    edges = [(a, b) for i, a in enumerate(corners) for b in corners[i + 1:]
             if sum(1 for x, y in zip(a, b) if x != y) == 1]
    middles = sorted({tuple(F(x + y, 2) for x, y in zip(a, b)) for a, b in edges})
    twelve = sorted({tuple(F(v) for v in p) for s in product((1, -1), repeat=2)
                     for p in {(s[0], s[1], 0), (s[0], 0, s[1]), (0, s[0], s[1])}})
    print("\nthe middles of a cube's twelve edges, and twelve same spheres around one")
    print(f"  edges: {len(edges)}; their middles are cubic close packing's twelve: {middles == twelve}")
    print(f"  each middle at one distance from the 0, squared: {[str(d) for d in sorted({dot(m, m) for m in middles})]}")

    r2 = F(2)
    print("\none sphere round the 0 through the twelve middles, and a cone from each apex")
    for name, p in (("the one apex", apex), ("its opposite", other)):
        on = [n for n in corners if sum(1 for x, y in zip(n, p) if x != y) == 1]
        touching = [m for m in middles if cone_value(p, r2, m) == 0 and dot(p, m) == r2]
        print(f"  {name} {p}: its three edges are lines of its cone: "
              f"{all(cone_value(p, r2, n) == 0 for n in on)}; "
              f"its cone touches the sphere at the middles of those three: {len(touching)}")
    fails = 0
    for x in product(range(-3, 4), repeat=3):
        if cone_value(apex, r2, x) - cone_value(other, r2, x) != -8 * dot(apex, x):
            fails += 1
    print(f"  the one cone less the other is eight of the place along the line of the two apexes: fails {fails}")
    print("  so the two cones cross in the plane between the two apexes, and at no other place: flat")

    print("\nthe twelve by the line of the two apexes: a prior layer, an inside layer, a next layer")
    layers = {}
    for m in middles:
        layers.setdefault(dot(apex, m), []).append(m)
    print(f"  {[len(layers[k]) for k in sorted(layers)]}")
    prior, nxt = layers[min(layers)], layers[max(layers)]
    print(f"  the next three are where the one cone touches the sphere: "
          f"{sorted(nxt) == sorted(m for m in middles if dot(apex, m) == r2)}")
    print(f"  the prior three are the next three, each of three inverted together: "
          f"{sorted(tuple(-v for v in m) for m in nxt) == sorted(prior)}")

    print("\nthe six steps of the loop of six, each at its middle")
    crossings, ways = [], []
    for i, form in enumerate(loop):
        to = loop[(i + 1) % 6]
        crossings.append(tuple(F(x + y, 2) for x, y in zip(form, to)))
        ways.append(dot(apex, to) - dot(apex, form))
    inside = sorted(layers[0])
    print(f"  each middle in the plane between the two apexes: {all(dot(apex, m) == 0 for m in crossings)}")
    print(f"  the six are the inside layer's six: {sorted(crossings) == inside}")
    print(f"  each on the one sphere: {all(dot(m, m) == r2 for m in crossings)}")
    sixth = all(dot(crossings[i], crossings[(i + 1) % 6]) * 2 == r2 for i in range(6))
    print(f"  each a sixth of a circle from the next: {sixth}")
    print(f"  the way of each step through the plane: {['one way' if w > 0 else 'the other' for w in ways]}")
    print(f"  three one way and three the other, in turn: "
          f"{sorted(ways) == [-2, -2, -2, 2, 2, 2] and all(ways[i] == -ways[i - 1] for i in range(6))}")
    print(f"  a form at the 0 itself: {(0, 0, 0) in corners}")


if __name__ == "__main__":
    main()
