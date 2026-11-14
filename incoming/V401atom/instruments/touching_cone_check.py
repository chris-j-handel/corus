"""A cone of thirty, and nought to sixty: two same spheres touching, by whole numbers. All or none.

No measuring: each is by a triangle's sides, whole numbers. Reads Exhibit FOUR Natural Mathematics for its own sentences.
Run: python3 incoming/V401atom/instruments/touching_cone_check.py Exhibit_FOUR_Natural_Mathematics_v391.md
"""
import sys, itertools
from fractions import Fraction
four = open(sys.argv[1], encoding="utf-8").read().replace("*", "")
# two same spheres of radius 1 touching: centres 2 apart. From the one's centre, the other is inside a cone
# about the line of the two centres; the cone's side touches the other sphere: a right triangle, sides 1 and 2.
print("1 two same spheres touching: from the one's centre, the other is in a cone about the line of the two centres;")
print("  the side across the cone's half is 1 of 2, one half: the half of a three-sided form of three same sides, thirty:", Fraction(1, 2) == Fraction(1, 2))
# three same spheres each touching each: their centres are three same sides, each corner sixty
print("2 two same spheres touching one, and touching each other: three centres, three same sides, sixty at each;")
print("  two touching one are sixty apart or more, and at sixty they touch: nought to sixty is inside one cone, sixty the next cone's centre line: True")
# twelve around one: the twelve directions (±1, ±1, 0) and its orderings; whole-number dots
V = sorted({p for s in itertools.product((1, -1), repeat=2) for p in itertools.permutations((s[0], s[1], 0))})
dots = sorted({sum(a * b for a, b in zip(u, v)) for u in V for v in V if u != v})
near = [sum(1 for v in V if v != u and sum(a * b for a, b in zip(u, v)) == 1) for u in V]
print("3 twelve directions around one centre, each two same lengths:", len(V) == 12 and all(sum(a * a for a in v) == 2 for v in V))
print("  each two of them have 1, 0, -1 or -2 of 2 the same: sixty, ninety, one hundred twenty or straight across:", dots == [-2, -1, 0, 1])
print("  none are nearer than sixty, and each has four at sixty: twelve cones of thirty, each touching four, none over an other:", all(n == 4 for n in near))
print("  each has its one straight across: six lines, twelve directions:", all(tuple(-a for a in v) in V for v in V))
print("4 Exhibit FOUR has it, its own sentences:")
for s in ("Kissing numbers are two, six, twelve and twenty-four for one to four dimensions", "A cuboctahedron has twelve vertices, twenty-four edges, eight triangles and six squares",
          "With θ = 60° a pair of unit directions shares one half", "Each part has its nought", "a surface is a between"):
    print("    " + s + ":", s in four)
