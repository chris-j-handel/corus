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

# two facing cones, by whole numbers: spheres of radius 1, centres on one line, 2 apart; x along the line, r from it
half = Fraction(1, 3)                       # a cone of thirty: (r/x)^2 is one third
x = Fraction(1)                             # where the two cones' sides cross: x^2/3 = (2 - x)^2/3
print("5 two same spheres touching, and their two cones, each from its own centre to its other:")
print("  the two cones are on one line, the line of the two centres, facing: co-linear: True")
print("  the point of the two touching is the middle of the two centres, one point, nothing in it:", x == Fraction(2, 2))
print("  the two cones' sides cross in one circle around that point, in the plane between the two:", half * x * x == half * (2 - x) ** 2)
t1, t2 = Fraction(3, 2), Fraction(1, 2)     # each cone's side touches its other sphere in a circle
print("  each cone's side touches its other sphere in one circle, the two circles the same, one each side of the point:",
      t1 * t1 + Fraction(3, 4) == 3 and (2 - t1) ** 2 + Fraction(3, 4) == 1 and t1 - 1 == 1 - t2)
dot = lambda u, v: sum(a * b for a, b in zip(u, v))
print("6 the twelve around one centre:")
print("  touchings among the twelve, each two at sixty:", sum(1 for u, v in itertools.combinations(V, 2) if dot(u, v) == 1),
      "· and each of the twelve touching the one: 12 · together:", 12 + sum(1 for u, v in itertools.combinations(V, 2) if dot(u, v) == 1))
planes = [[v for v in V if v[i] == 0] for i in range(3)]
print("  the twelve are three fours, by three planes each at a right angle to each other; each four is two lines at a right angle:",
      all(len(p) == 4 for p in planes) and all(sorted(dot(p[0], q) for q in p[1:]) == [-2, 0, 0] for p in planes))
ok = True
for u in V:
    others = sorted(dot(u, v) for v in V if v != u)
    ok = ok and others == [-2] + [-1] * 4 + [0] * 2 + [1] * 4
    ten = [v for v in V if v != u and dot(u, v) != -2]
    ok = ok and len(ten) == 10 and all(tuple(-a for a in v) in ten for v in ten)
print("  from each one: its one straight across, its own line; and ten others, five lines: four at sixty, two at ninety, four at one hundred twenty:", ok)
print("  each of the four at sixty is in a plane other than its own:", all(all(sum(1 for i in range(3) if v[i] == 0 and u[i] == 0) == 0 for v in V if dot(u, v) == 1) for u in V))
