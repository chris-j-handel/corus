"""v406geodesic2 · the check of the fourth drawing: local, global, local in the one triangle.

Usage: python3 -I check_one_triangle.py PATH_TO_Exhibit_ONE_Natural_Resolver.md

The candidate laid on the drawing:
  the one triangle, a me at its corner A and two tips B and C on the me's horizon;
  two routes round it from the me, one way (a self's, names 2 to 8) and its other way (an other's, 10 to 16);
  in a route, four moments at the corners (prior, now, next, same) and three one-way me-parities on the sides;
  1, 9 and 17 at the me.
All or none: with one line not is, the check is not.
"""
import math, re, sys
import numpy as np

results = []
def check(name, ok): results.append((name, bool(ok)))

A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
CORNER = {"me": A, "B": B, "C": C}

# ---------- the triangle ----------
def angle_at(P, Q, S):
    tq = Q - (Q @ P) * P; ts = S - (S @ P) * P
    return math.degrees(math.acos(tq @ ts / np.linalg.norm(tq) / np.linalg.norm(ts)))
angs = [angle_at(A, B, C), angle_at(B, C, A), angle_at(C, A, B)]
check("the triangle: three right angles", all(abs(a - 90) < 1e-9 for a in angs))
t = np.linspace(0, 1, 91)
far = [(math.cos(math.radians(90 * u)), math.sin(math.radians(90 * u)), 0.0) for u in t]
check("the far side is the me's horizon: 90 degrees from the me, tip to tip",
      all(abs(math.degrees(math.acos(np.clip(A @ np.array(p), -1, 1))) - 90) < 1e-9 for p in far))
check("a corner is 90 degrees from its far side, with all three corners",
      all(abs(P @ Q) < 1e-12 for P, Q in ((A, B), (B, C), (C, A))))
# three right spiral steps at the corners and the triangle's own 90 make a round
area_deg = math.degrees(4 * math.pi / 8)            # an eighth of a unit sphere, as an angle
check("three corner right angles and the triangle's own 90: 360", abs(3 * 90 + area_deg - 360) < 1e-9 and abs(sum(angs) - 180 - area_deg) < 1e-9)

# ---------- the two routes, and the names laid on them ----------
# a place is a corner ("me", "B", "C") or a one-way side (from, to)
self_route  = ["me", ("me", "B"), "B", ("B", "C"), "C", ("C", "me"), "me"]      # names 2..8
other_route = ["me", ("me", "C"), "C", ("C", "B"), "B", ("B", "me"), "me"]      # names 10..16
place = {1: "me", 9: "me", 17: "me"}
place.update({2 + i: p for i, p in enumerate(self_route)})
place.update({10 + i: p for i, p in enumerate(other_route)})
moment = {2: "prior", 4: "now", 6: "next", 8: "same", 10: "prior", 12: "now", 14: "next", 16: "same"}

check("seventeen names laid, 1 to 17", sorted(place) == list(range(1, 18)))
one_way = [n for n in place if isinstance(place[n], tuple)]
moments = [n for n in place if n in moment]
check("six one-way me-parities: 3, 5, 7 and 11, 13, 15, on the three sides one way and its other way",
      sorted(one_way) == [3, 5, 7, 11, 13, 15]
      and {frozenset(place[n]) for n in (3, 5, 7)} == {frozenset(place[n]) for n in (11, 13, 15)} == {frozenset(s) for s in (("me", "B"), ("B", "C"), ("C", "me"))}
      and {place[n] for n in (3, 5, 7)} == {tuple(reversed(place[n])) for n in (11, 13, 15)})
check("four moments with a self, 2 4 6 8, and four with an other, 10 12 14 16, at the corners",
      sorted(moments) == [2, 4, 6, 8, 10, 12, 14, 16] and all(isinstance(place[n], str) for n in moments))
check("6 + 4 + 4 = 14 of 17, with 1, 9 and 17", len(one_way) + len(moments) == 14 and sorted(set(place) - set(one_way) - set(moments)) == [1, 9, 17])
check("a route is local, global, local: from the me, along the far side, to the me",
      all(r[0] == "me" and r[-1] == "me" and frozenset(r[3]) == frozenset(("B", "C")) for r in (self_route, other_route)))
check("the fourth moment, same, is at the corner of prior: the me", place[2] == place[8] == place[10] == place[16] == "me")
# a route's sides in sequence: a side ends at the corner the next name is at
def chained(r): return all(r[i][1] == r[i + 1] and r[i][0] == r[i - 1] for i in (1, 3, 5))
check("a route goes corner, side, corner, side, corner, side, corner", chained(self_route) and chained(other_route))

# ---------- the fold laying one tip onto its other ----------
Mir = np.array([[0, 1.0, 0], [1.0, 0, 0], [0, 0, 1.0]])          # the mirror through the me and the far side's middle
def name_of(v):
    for k, c in CORNER.items():
        if np.allclose(v, c): return k
def fold(p): return name_of(Mir @ CORNER[p]) if isinstance(p, str) else (name_of(Mir @ CORNER[p[0]]), name_of(Mir @ CORNER[p[1]]))
check("the fold is the me's own: the me as it is, tip B onto tip C and C onto B", fold("me") == "me" and fold("B") == "C" and fold("C") == "B")
Mid = (B + C) / np.linalg.norm(B + C)
check("the fold's line is the geodesic from the me to the far side's middle, at a right angle with it",
      np.allclose(Mir @ Mid, Mid) and abs(np.cross(A, Mid) @ np.cross(B, C)) < 1e-12)
check("8 up is the fold: a name's place folded is the place of its name 8 up, 1 to 9", all(fold(place[n]) == place[n + 8] for n in range(1, 10)))
check("two folds, 16 up: a name's own place again, 1 as 17", fold(fold(place[1])) == place[17] and np.allclose(Mir @ Mir, np.eye(3)))
check("one fold is a mirror, the route's way round inverting; two folds are none", np.linalg.det(Mir) < 0 and np.linalg.det(Mir @ Mir) > 0)
# the hand: a self's way round goes from P's tip to Q's, as a right spiral step F(P, Q) = (-Q, P) brings P's axis to Q's
F = np.array([[0, -1.0, 0], [1.0, 0, 0], [0, 0, 1.0]])
check("a self's way round follows a right spiral step about the me: tip B toward tip C", np.allclose(F @ B, C) and self_route[3] == ("B", "C"))
check("four right spiral steps about the me: the same triangle", np.allclose(np.linalg.matrix_power(F, 4), np.eye(3)))

# ---------- 17 less ----------
def reaches(n, m):      # one-way n ends at the corner of moment m
    return isinstance(place[n], tuple) and isinstance(place[m], str) and place[n][1] == place[m]
ok17 = all(reaches(n, 17 - n) or reaches(17 - n, n) or place[n] == place[17 - n] == "me" for n in range(1, 17))
check("17 less: a one-way me-parity with the corner it reaches, its name with that corner's other moment; 1 with 16 and 8 with 9 at the me", ok17)

# ---------- beside Exhibit ONE's own table ----------
text = open(sys.argv[1], encoding="utf-8").read()
rows = {int(m.group(1)): (m.group(2), m.group(3)) for m in re.finditer(r"^\| (\d+) \| \*\*[^*]+\*\* \| ([a-z\-]+)[^|]*\| [^|]*\| [^|]*\| ([a-z\-]+) \|", text, re.M)}
check("Exhibit ONE's table of seventeen names is found", sorted(rows) == list(range(1, 18)))
roots = {n: rows[n][0] for n in rows}
check("Exhibit ONE: an odd name's root is existing, observing or discovering, a me-parity's; an even name's possibling or same-existing",
      all(roots[n] in ("existing", "observing", "discovering") for n in range(1, 18, 2)) and all(roots[n] in ("possibling", "same-existing") for n in range(2, 17, 2)))
mom = re.findall(r"\*Names\*: (\d+)-[a-z\-]+ · (\d+)-[a-z\-]+ · (\d+)-", text)
check("Exhibit ONE: a self's four moments of exchanging are about 2, 4, 6 and 8", [int(m[1]) for m in mom[:4]] == [2, 4, 6, 8])
bif = [[int(x) for x in m.split("-")] for m in re.findall(r"^- \*\*(\d+-\d+-\d+-\d+)\*\*", text, re.M)]
check("Exhibit ONE: four bi-foldings, two pairs 8 apart in each: two mirror pairs of the drawing",
      len(bif) == 4 and all({n + 8 if n <= 8 else n - 8 for n in b} == set(b) for b in bif))
check("Exhibit ONE: 8 and 16, the moments same, are its same-existing names of one", roots[8] == roots[16] == "same-existing")

for name, ok in results: print(("is       " if ok else "is not   ") + name)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
print("\nBeside the check, a parting for a partner's word:")
print("  Exhibit ONE's table, its three in the order next, now, prior:", ", ".join(f"{n} {rows[n][1]}" for n in (1, 9, 17)))
print("  The drawing, by a partner's word of 21 November: 1 tri-bi-co, 9 co-bi-tri, 17 tri-bi-co")
sys.exit(0 if all(ok for _, ok in results) else 1)
