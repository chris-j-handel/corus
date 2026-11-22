"""v406geodesic2 · the bi-foldings on the torus of the third drawing, executed.

Usage: python3 -I the_bi-foldings_on_the_torus.py PATH_TO_Exhibit_ONE_Natural_Resolver.md

The third drawing's placing, a candidate of v406geodesic: a name n of 1 to 16 as n - 1 in four binary digits,
the two of its four-cycling round the small opening, outer top, inner top, inner bottom, outer bottom,
and the two of its root round the large opening, a right spiral step a name. One self, sixteen names, a name
at a place: a torus of names, and no torus of selves. This instrument executes the moves of Exhibit ONE
Natural Resolver's bi-foldings on it: 8 up or down, 4 up or down, and 17 less.
"""
import math, re, sys
import numpy as np

R, r = 2.0, 1.0
HEIGHT = ["outer top", "inner top", "inner bottom", "outer bottom"]
def q(n): return (n - 1) // 4            # its height round the small opening
def p(n): return (n - 1) % 4             # its place round the large opening
def at(n):
    th, ph = math.radians(45 + 90 * q(n)), math.radians(45 + 90 * p(n))
    return np.array([(R + r * math.cos(th)) * math.cos(ph), (R + r * math.cos(th)) * math.sin(ph), r * math.sin(th)])
def core(n):
    ph = math.radians(45 + 90 * p(n)); return np.array([R * math.cos(ph), R * math.sin(ph), 0.0])

results = []
def line(name, ok): results.append((name, bool(ok)))

line("8 up: the same place round the large opening, and two right spiral steps round the small, through the tube's core",
     all(p(n) == p(n + 8) and (q(n + 8) - q(n)) % 4 == 2 and np.allclose(at(n) + at(n + 8), 2 * core(n)) for n in range(1, 9)))
line("4 up: the same place round the large opening, and one right spiral step round the small",
     all(p(n) == p(n + 4) and (q(n + 4) - q(n)) % 4 == 1 for n in range(1, 13)))
H = np.diag([1.0, -1.0, -1.0])
line("17 less: two right spiral steps of the whole torus about one line through its 0, no mirror, with all sixteen",
     all(np.allclose(H @ at(n), at(17 - n)) for n in range(1, 17)) and np.linalg.det(H) > 0 and np.allclose(H @ H, np.eye(3)))
line("17 less: round neither opening alone: a name's height and its place both go to their podal, q to 3 - q and p to 3 - p",
     all(q(17 - n) == 3 - q(n) and p(17 - n) == 3 - p(n) for n in range(1, 17)))

text = open(sys.argv[1], encoding="utf-8").read()
four = [[int(x) for x in m.split("-")] for m in re.findall(r"^- \*\*(\d+-\d+-\d+-\d+)\*\*", text, re.M)]
line("Exhibit ONE Natural Resolver: its four bi-foldings are found", sorted(map(sorted, four)) == sorted(map(sorted, [[1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12]])))
middle = [[9, 5, 12, 8], [7, 11, 6, 10]]
line("Exhibit ONE Natural Resolver: its two middle bi-foldings are found", all("-".join(map(str, m)) in text for m in middle))

def move(a, b):
    if a + b == 17: return "17 less"
    d = b - a
    return {8: "8 up", -8: "8 down", 4: "4 up", -4: "4 down"}.get(d, "no move of the three")
def moves(b): return [move(b[i], b[(i + 1) % 4]) for i in range(4)]

line("a bi-folding of the four: 17 less and a move of 8, one and then its other, and its fourth move to its opening name",
     all(sorted(set(moves(b))) in (["17 less", "8 up"], ["17 less", "8 down"]) and moves(b)[0] != moves(b)[1] for b in four))
line("a bi-folding of the four is at two places of the large opening and all four heights of the small",
     all(len({p(n) for n in b}) == 2 and len({q(n) for n in b}) == 4 for b in four))
line("two of the four are at one pair of places and two at its other: 1-9-8-16 with 4-13-5-12, and 2-15-7-10 with 3-11-6-14",
     {frozenset(p(n) for n in b) for b in four} == {frozenset({0, 3}), frozenset({1, 2})})
line("a middle bi-folding: 17 less and a move of 4, one and then its other",
     all(sorted(set(moves(b))) in (["17 less", "4 up"], ["17 less", "4 down"]) for b in middle))
line("a middle bi-folding is on the inner surface alone, inner top and inner bottom, at two places of the large opening",
     all({q(n) for n in b} == {1, 2} and len({p(n) for n in b}) == 2 for b in middle))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is\n")
for b in four + middle:
    print("-".join(map(str, b)) + ":  " + ";  ".join(f"{n} {HEIGHT[q(n)]}, place {p(n) + 1}" for n in b) + "  ·  " + ", ".join(moves(b)))
sys.exit(0 if all(ok for _, ok in results) else 1)
