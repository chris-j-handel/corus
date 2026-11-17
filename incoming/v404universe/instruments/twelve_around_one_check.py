"""Twelve same spheres around one, by whole numbers and thirds.

Two close packings have twelve around one. This instrument builds each
twelve, and says of each: its three fours; its layers, a prior, an inside and
a next; how the next three come from the prior three; and how many close
layers cross at the one.

It reads no file and writes none.

Run:  python3 -I incoming/v404universe/instruments/twelve_around_one_check.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cubic_twelve():
    found = set()
    for signs in product((1, -1), repeat=2):
        for perm in set(permutations((signs[0], signs[1], 0))):
            found.add(tuple(F(v) for v in perm))
    return sorted(found)


def layers(twelve, axis):
    by = {}
    for v in twelve:
        by.setdefault(dot(v, axis), []).append(v)
    return [by[k] for k in sorted(by)]


def fold_through(v, axis):
    """v folded through the plane at a right angle to the axis."""
    k = 2 * dot(v, axis) / dot(axis, axis)
    return tuple(x - k * a for x, a in zip(v, axis))


def touching(twelve):
    """pairs of the twelve touching each other: as far apart as each is from the one."""
    return [(a, b) for a, b in combinations(twelve, 2) if dot(minus(a, b), minus(a, b)) == 2]


def faces(twelve):
    pairs = set(touching(twelve)) | {(b, a) for a, b in touching(twelve)}
    threes = [t for t in combinations(twelve, 3) if all((a, b) in pairs for a, b in combinations(t, 2))]
    fours = 0
    for q in combinations(twelve, 4):
        links = sum(1 for a, b in combinations(q, 2) if (a, b) in pairs)
        flat = dot(minus(q[1], q[0]), cross(minus(q[2], q[0]), minus(q[3], q[0]))) == 0
        if links == 4 and flat and all(sum(1 for b in q if (a, b) in pairs) == 2 for a in q):
            fours += 1
    return len(pairs) // 2, len(threes), fours


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def close_layers_through_the_one(twelve):
    """planes through the one having six of the twelve in them."""
    found = set()
    for a, b in combinations(twelve, 2):
        n = cross(a, b)
        if n == (0, 0, 0):
            continue
        inside = frozenset(v for v in twelve if dot(v, n) == 0)
        if len(inside) == 6:
            found.add(inside)
    return len(found)


def say(name, twelve, axis):
    prior, inside, nxt = layers(twelve, axis)
    edges, threes, fours = faces(twelve)
    opposite = {tuple(-x for x in v) for v in twelve} == set(twelve)
    inverted = {tuple(-x for x in v) for v in prior} == set(nxt)
    folded = {fold_through(v, axis) for v in prior} == set(nxt)
    print(f"\n{name}")
    print(f"  around one: {len(twelve)}, each as far from the one as each other: "
          f"{len({dot(v, v) for v in twelve}) == 1}")
    print(f"  touchings among the twelve: {edges}; threes each touching each: {threes}; flat fours in a ring: {fours}")
    print(f"  layers by the axis, a prior, an inside and a next: {len(prior)}, {len(inside)}, {len(nxt)}")
    print(f"  the next three are the prior three, each of three inverted together: {inverted}")
    print(f"  the next three are the prior three folded through the inside layer: {folded}")
    print(f"  each of the twelve has its opposite among the twelve: {opposite}")
    print(f"  close layers of six crossing at the one: {close_layers_through_the_one(twelve)}")


def main():
    axis = (F(1), F(1), F(1))
    cubic = cubic_twelve()
    print("cubic close packing: each two of the three coordinates one or its opposite, the third nought")
    for i, name in enumerate(("first", "second", "third")):
        four = [v for v in cubic if v[i] == 0]
        print(f"  the {name} coordinate nought: {len(four)} of the twelve, one plane")
    say("cubic close packing", cubic, axis)

    prior, inside, nxt = layers(cubic, axis)
    hexagonal = sorted(prior + inside + [fold_through(v, axis) for v in prior])
    say("hexagonal close packing: the same prior and inside layers, the next the prior folded through", hexagonal, axis)


if __name__ == "__main__":
    main()
