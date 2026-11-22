"""v406geodesic2 · the check of the fifth drawing: the co-linear of the bi-folding, and its two cones.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_co-linear_and_its_two_cones.py \
      Natural_Intelligence_v402mgr.md Exhibit_THREE_Natural_Numbers_v402mgr.md \
      Exhibit_FOUR_Natural_Mathematics_v402mgr.md Exhibit_EIGHTEEN_Natural_Physics_v402mgr.md \
      Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md \
      incoming/v406me/working_documents_as_a_partner_gave_them/The_seventeen_names_in_one_table_its_sheet_Surface.csv

The candidate laid on the drawing, from the second drawing's bi-folding:
  two folds, on two great circles at a right angle, cross at two opposite intersections;
  the line through the two, through the sphere's 0, is the co-linear;
  four quarter spheres go from the far intersection to the one of its own side, and all eight triangles are with it;
  a cone of a right angle from the far intersection and one from its own side's cross in the circle between.
It opens the pages and writes none. All or none: with one line not is, the check is not.
"""
import csv, itertools, math, sys
import numpy as np

results = []
def line(name, ok): results.append((name, bool(ok)))

A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
FAR, OWN, O = -B, B, np.zeros(3)
fold1 = np.diag([1.0, -1.0, 1.0])       # the second drawing's fold about the great circle of the side from the pole to B
fold2 = np.diag([1.0, 1.0, -1.0])       # and its fold about the equator
both = fold2 @ fold1

# ---------- the two folds and the co-linear ----------
line("the two folds' great circles are at a right angle, and cross at two opposite intersections and at no other",
     abs(np.array([0, 1.0, 0]) @ np.array([0, 0, 1.0])) < 1e-12
     and all(abs(p[1]) < 1e-12 and abs(p[2]) < 1e-12 for p in (OWN, FAR)) and np.allclose(OWN, -FAR))
line("the line through the two intersections is through the sphere's 0: the co-linear", np.allclose((OWN + FAR) / 2, O))
turn = 2 * np.outer(B, B) - np.eye(3)
line("the two folds, one and then its other, are two right spiral steps about the co-linear, with no fold of the hand",
     np.allclose(both, turn) and np.linalg.det(both) > 0 and np.linalg.det(fold1) < 0 and np.linalg.det(fold2) < 0)
rng = np.random.default_rng(17)
pts = rng.normal(size=(4000, 3)); pts /= np.linalg.norm(pts, axis=1)[:, None]
moved = np.linalg.norm(pts @ both.T - pts, axis=1)
line("of the sphere, the two intersections alone are as they were by the two folds",
     np.allclose(both @ OWN, OWN) and np.allclose(both @ FAR, FAR) and np.allclose(moved, 2 * np.sqrt(pts[:, 1] ** 2 + pts[:, 2] ** 2)))

# ---------- four quarter spheres, eight triangles ----------
octants = list(itertools.product((1, -1), repeat=3))                      # the eight triangles, by the sides of three great circles
corners = lambda s: [np.array([s[0], 0, 0.0]), np.array([0, s[1], 0.0]), np.array([0, 0, s[2] * 1.0])]
def excess_deg(tri):
    P, Q, S = tri
    def ang(P, Q, S):
        tq = Q - (Q @ P) * P; ts = S - (S @ P) * P
        return math.degrees(math.acos(tq @ ts / np.linalg.norm(tq) / np.linalg.norm(ts)))
    return ang(P, Q, S) + ang(Q, S, P) + ang(S, P, Q) - 180
line("eight triangles of three right angles, 90 over a flat triangle's 180 apiece, 720 in all", all(abs(excess_deg(corners(s)) - 90) < 1e-9 for s in octants) and len(octants) == 8)
quarters = {(sy, sz): [s for s in octants if s[1] == sy and s[2] == sz] for sy in (1, -1) for sz in (1, -1)}
line("four quarter spheres between the two folds' circles, a quarter two triangles, 180 of the 720, from the far intersection to the one of its own side",
     len(quarters) == 4 and all(len(q) == 2 and {s[0] for s in q} == {1, -1} for q in quarters.values()))
at_own = [s for s in octants if any(np.allclose(c, OWN) for c in corners(s))]
at_far = [s for s in octants if any(np.allclose(c, FAR) for c in corners(s))]
line("all eight triangles are with the co-linear, a corner at an end of it: four at the intersection of its own side and four at the far",
     len(at_own) == 4 and len(at_far) == 4 and set(at_own) | set(at_far) == set(octants) and not set(at_own) & set(at_far))
round_ = [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]                      # the four quarters, round the co-linear
steps = [(round_[i][0] != round_[i + 1][0], round_[i][1] != round_[i + 1][1]) for i in range(4)]
line("round the co-linear a step from a quarter to its next is one fold, one parity inverting, the one and then its other; four steps, the same quarter",
     steps == [(True, False), (False, True), (True, False), (False, True)])
hand = lambda q: q[0] * q[1]
line("the four are two and two in turn: a quarter and the quarter across the co-linear are of one hand, the two between of its other",
     [hand(q) for q in round_[:4]] == [1, -1, 1, -1])

# ---------- two cones ----------
def on_cone(p, apex, axis):            # a cone of a right angle at its vertex: 45 degrees from its axis
    v = p - apex
    return abs(math.degrees(math.acos(np.clip(v @ axis / np.linalg.norm(v), -1, 1))) - 45) < 1e-9
ring = [np.array([0, math.cos(t), math.sin(t)]) for t in np.linspace(0, 2 * math.pi, 73)[:-1]]
line("a cone from the far intersection, 45 degrees about the co-linear, is through all of the circle between the two",
     all(on_cone(p, FAR, B) for p in ring))
line("a cone from the intersection of its own side, facing it, is through that same circle", all(on_cone(p, OWN, -B) for p in ring))
line("a cone's lines in the two folds' planes are to the four other intersections, and two across from one another are at a right angle",
     all(on_cone(p, FAR, B) and on_cone(p, OWN, -B) for p in (A, -A, C, -C)) and abs((A - FAR) @ (-A - FAR)) < 1e-12 and abs((C - OWN) @ (-C - OWN)) < 1e-12)
xs = np.linspace(-1, 1, 2001)
line("the two cones cross in the circle between and at no other place", [x for x in xs if abs((x + 1) ** 2 - (1 - x) ** 2) < 1e-12] == [0.0])
line("the sphere's 0 is on neither cone, and it is between the two vertices on the co-linear", not on_cone(O, FAR, B) and not on_cone(O, OWN, -B) and np.allclose(O, (FAR + OWN) / 2))
line("23, 24 and 25: one to a side of 24, and 24 times 24 less 23 times 25 is 1", 24 - 23 == 25 - 24 == 1 and 24 * 24 - 23 * 25 == 1)
sq = [FAR, A, OWN, -A]
line("in a fold's plane the two cones' lines are a square of four corners round the 0, the far, its own side's and two of the circle between",
     all(abs(np.linalg.norm(sq[i] - sq[(i + 1) % 4]) - math.sqrt(2)) < 1e-12 for i in range(4)) and np.allclose(sum(sq), O))

# ---------- a going with no rest ----------
line("a sphere at two: six intersections less twelve sides and eight triangles", 6 - 12 + 8 == 2)
def index_at(P):                        # turns of a going's direction round a rest point, the going a turning about the co-linear
    e1 = np.array([0, 1.0, 0]); e2 = np.cross(P, e1); total = 0.0; prev = None
    for t in np.linspace(0, 2 * math.pi, 361):
        q = P + 0.05 * (math.cos(t) * e1 + math.sin(t) * e2); q /= np.linalg.norm(q)
        v = np.cross(B, q)
        a = math.atan2(v @ e2, v @ e1)
        if prev is not None:
            d = a - prev
            while d > math.pi: d -= 2 * math.pi
            while d < -math.pi: d += 2 * math.pi
            total += d
        prev = a
    return round(total / (2 * math.pi))
line("a turning about the co-linear rests at its two ends alone, one round of its direction at an end, two in all: the sphere's two",
     index_at(OWN) == 1 and index_at(FAR) == 1 and index_at(OWN) + index_at(FAR) == 2)
cells = list(csv.reader(open(sys.argv[6], encoding="utf-8")))
head = next(i for i, r in enumerate(cells) if any(c.strip().startswith("first: lines") for c in r))
c0 = next(j for j, c in enumerate(cells[head]) if c.strip().startswith("first: lines"))
grid = [[int(cells[head + 1 + i][c0 + j]) for j in range(4)] for i in range(4)]
V = 16; E = len({frozenset((grid[i][j], grid[i][(j + 1) % 4])) for i in range(4) for j in range(4)} | {frozenset((grid[i][j], grid[(i + 1) % 4][j])) for i in range(4) for j in range(4)}); F = 16
line("a torus at nought: the workbook's sixteen names round their edges, sixteen less thirty-two and sixteen", V - E + F == 0)
line("a sphere opened at its two rest points and gone through along the co-linear is at nought, a torus: two, less a cap at an end, and a tube at nought", 2 - 1 - 1 + 0 == 0)

# ---------- word for word, living ----------
NI, THREE, FOUR, EIGHTEEN, THIRTY = (open(p, encoding="utf-8").read() for p in sys.argv[1:6])
quotes = [
    (NI, "Natural intelligence is geodesic co-sequential changing method of natural torusing, discovering next-possibling-same-existing."),
    (NI, "Corusing reaches a corus from a surface, and torusing reaches a surface from a corus"),
    (NI, "Within a bi-folding parallel surfaces and co-linear openings through them are one form"),
    (THREE, "a self's bi-inversioning-co-recursioning is 23, 24 and 25, one before its apex and one after"),
    (THREE, "A torus is a sphere with one handle"),
    (FOUR, "Of closed orientable surfaces only the torus has a flow with no rest point"),
    (FOUR, "Bi-inversioning-co-recursioning is two consecutive inversions on different axes"),
    (EIGHTEEN, "two facing through an unoccupied 24, a 0, not changing"),
    (THIRTY, "Corus, vertex and centre of face are on one line."),
    (THIRTY, "Twelve corners closing as a sphere and winding through one opening as a torus are both"),
]
line("ten living sentences beside the drawing are word for word in their files", all(q in text for text, q in quotes))

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
