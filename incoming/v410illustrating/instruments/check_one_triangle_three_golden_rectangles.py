"""v410illustrating · the check of the 58th drawing: one triangle, three golden rectangles.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_one_triangle_three_golden_rectangles.py .

It executes what the 58th drawing says, ahead of its laying: three golden rectangles at right angles on the one
triangle's three mirrors; their twelve corners closing as a sphere; the one triangle of three right angles as fifteen
of that sphere's 120; nought to sixty with its seventeen primes; a line of five names to a surface, 59; and the
seventeen names across and along. The living files' own sayings are opened beside what is executed, a numbered
sentence of Exhibit THIRTY beside a line.

Do no harm: it opens five living files and v403mgr's one table of the seventeen names, and writes in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, importlib.util, itertools, os, re, sys
from collections import Counter
from pathlib import Path
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
def opened(name):
    spec = importlib.util.spec_from_file_location(name[:24].replace("-", "_"), os.path.join(HERE, name)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
f = opened("a_five_on_the_sphere_opening_to_a_torus_two_ways_executed.py")
c57 = opened("check_one_triangle_three_right_angles_bi-folding_1_to_17.py")

PHI = f.PHI
A, B, C = c57.A, c57.B, c57.C                                  # the one triangle's corners, as the 57th lays them: A the me
def rect(r):
    """three rectangles at right angles, 2 across and 2r along; a rectangle is on a mirror of the three"""
    return [[(0, a, b * r) for a, b in ((1, 1), (1, -1), (-1, -1), (-1, 1))],
            [(a, b * r, 0) for a, b in ((1, 1), (1, -1), (-1, -1), (-1, 1))],
            [(b * r, 0, a) for a, b in ((1, 1), (1, -1), (-1, -1), (-1, 1))]]
RECT = rect(PHI)
G = f.made_by(f.MIRRORS + [f.ROUND3, f.ROUND5])
P0 = f.unit(f.V5 + 1.3 * f.V3 + 0.7 * f.V2)
INSIDE = [g for g in G if np.all(g @ P0 > 1e-9)]              # the fifteen of the one triangle
def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
ACROSS, ALONG, BOTH = [2, 6, 10, 14], [9, 13, 17], [12]         # the names across and along, as Exhibit THIRTY and Natural Naming say them
FIVE_NAMES = [3, 4, 5, 7, 8]                                   # five names before 10, as Exhibit THIRTY's 330 and 509 say them
SENTENCES = {506: "apex of one to fifty-nine's bi-folding", 507: "23, vertex", 509: "adding to 59", 512: "three golden rectangles", 513: "R1, (0, ±1, ±φ)",
             514: "120 degrees", 515: "Twelve corners of three", 516: "twenty-four", 517: "12-next-co-same-existing", 518: "Twelve corners closing as a sphere"}

def cut_of_a_side():
    """a side of the one triangle from a corner: to its corner of five, to its corner of three, to its next corner, in degrees"""
    five, three = f.unit((0, 1, PHI)), f.unit((0, PHI, 1 / PHI))
    a = np.degrees(np.arccos(A @ five)); b = np.degrees(np.arccos(five @ three)); c = np.degrees(np.arccos(three @ C))
    return float(a), float(b), float(c)

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    lf = lambda pat: sorted(root.glob(pat))[0].read_text(encoding="utf-8")
    naming, maths, numbers, thirty, illus = (lf("Exhibit_TWENTY_Natural_Naming_*.md"), lf("Exhibit_FOUR_Natural_Mathematics_*.md"), lf("Exhibit_THREE_Natural_Numbers_*.md"),
                                             lf("Exhibit_THIRTY_Co-Chaining_*.md"), lf("Exhibit_TWENTY-NINE_Natural_Illustrating_*.md"))
    sent = {int(n): t for n, t in re.findall(r"^(\d+)\. (.+)$", thirty, flags=re.M)}

    # three golden rectangles, a rectangle a mirror
    planes = [next(i for i in range(3) if all(abs(c[i]) < 1e-12 for c in r)) for r in RECT]
    sides = [(float(np.linalg.norm(np.subtract(r[0], r[1]))), float(np.linalg.norm(np.subtract(r[1], r[2])))) for r in RECT]
    line("is", sorted(planes) == [0, 1, 2] and all(abs(max(s) - 2 * PHI) < 1e-9 and abs(min(s) - 2) < 1e-9 for s in sides),
         "three rectangles at right angles, 2 across and 2φ along: a rectangle is on a mirror of the one triangle's three, a rectangle a mirror")
    def threads(r):
        R = rect(r); out = []
        for i in range(3):
            j = (i + 1) % 3 if abs(R[i][0][planes[(i + 1) % 3]]) > 1.0 else (i + 2) % 3     # the rectangle its along sides go through
            ax = planes[j]; pts = [p for p in ((np.array(R[i][k]) + np.array(R[i][(k + 1) % 4])) / 2 for k in range(4)) if abs(p[ax]) < 1e-12 and np.linalg.norm(p) < r]
            across = next(k for k in range(3) if abs(abs(R[j][0][k]) - 1) < 1e-12)          # the axis of that one's across
            out.append(len(pts) == 2 and all(abs(p[across]) < 1e-12 and np.linalg.norm(p) < r for p in pts))
        return all(out)
    line("is", threads(PHI), "a rectangle's along sides go through its next, at the middle of that one's across: three threading one way")
    R3 = f.ROUND3; on = lambda v: next(i for i, r in enumerate(RECT) if any(np.allclose(v, c) for c in r))
    line("is", all(len({on(R3 @ np.array(c, float)) for c in RECT[i]}) == 1 for i in range(3)) and sorted(on(R3 @ np.array(RECT[i][0], float)) for i in range(3)) == [0, 1, 2]
         and np.allclose(R3 @ A, C) and np.allclose(R3 @ C, B) and np.allclose(R3 @ B, A),
         "the one triangle's own round of three corners lays a rectangle onto its next, at all three")
    near = lambda r: min(float(np.linalg.norm(np.subtract(p, q))) for p in rect(r)[0] for q in rect(r)[1])
    grid = [1 + k / 1000 for k in range(1, 1500)]
    line("is", all(abs(near(r) - (2 * (1 + r * r - r)) ** 0.5) < 1e-9 for r in (1.2, 1.5, PHI, 2.0)) and abs(near(PHI) - 2) < 1e-9
         and abs(min(grid, key=lambda r: abs(near(r) - 2)) - PHI) < 1e-3 and abs(PHI * PHI - PHI - 1) < 1e-12,
         "with a number r for φ, nearest corners of a rectangle and its next are √(2(1 + r² − r)) from one another: 2, a rectangle's own across, with φ alone")

    # twelve corners closing as a sphere
    corners = [np.array(c, float) for r in RECT for c in r]
    edges = [(i, j) for i, j in itertools.combinations(range(12), 2) if abs(np.linalg.norm(corners[i] - corners[j]) - 2) < 1e-9]
    tris = [t for t in itertools.combinations(range(12), 3) if all(tuple(sorted(p)) in edges for p in itertools.combinations(t, 2))]
    at = Counter(i for t in tris for i in t)
    line("is", len(corners) == 12 and len(edges) == 30 and len(tris) == 20 and set(at.values()) == {5} and 12 * 5 == 20 * 3 == 30 * 2 == 60 and 12 - 30 + 20 == 2,
         "their twelve corners close as a sphere: 30 sides and 20 triangles, five triangles to a corner: 12 by 5, 20 by 3 and 30 by 2 are sixty")
    heights = Counter(round(float(c @ np.ones(3)), 6) for c in corners)
    def side_at(h): t = [c for c in corners if abs(c @ np.ones(3) - h) < 1e-6]; return float(np.linalg.norm(t[0] - t[1]))
    hs = sorted(heights)
    line("is", sorted(heights.values()) == [3, 3, 3, 3] and abs(side_at(hs[0]) - 2) < 1e-9 and abs(side_at(hs[3]) - 2) < 1e-9 and abs(side_at(hs[1]) - 2 * PHI) < 1e-9 and abs(side_at(hs[2]) - 2 * PHI) < 1e-9,
         "about the line of the three alike the twelve corners are four triangles of three: the outer two of side 2, the inner two of side 2φ")
    fives = {f.key((g @ f.V5).reshape(1, 3)) for g in G}
    line("is", len(G) == 120 and {f.key(f.unit(c).reshape(1, 3)) for c in corners} == fives,
         "the twelve corners are the twelve corners of five of the 120 moves: the three mirrors, the round of three, and one round of five")
    rot = Counter(f.period(g) for g in G if np.linalg.det(g) > 0)
    line("is", dict(rot) == {1: 1, 2: 15, 3: 20, 5: 24} and 24 + 36 == 60,
         "the sixty moves of one hand are 24 by fifths and 36 others: 15 of two doings, 20 by thirds, and 1 moving nothing")
    across_from = lambda v, pts: any(np.allclose(-v, p) for p in pts)
    mids = [f.unit(sum(corners[i] for i in t)) for t in tris]
    four = [np.array(v, float) for v in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))]; four_mids = [-v / 3 for v in four]
    line("found", all(across_from(f.unit(c), [f.unit(x) for x in corners]) for c in corners) and all(across_from(m, mids) for m in mids)
         and all(any(np.allclose(f.unit(-v), f.unit(m)) for m in four_mids) for v in four),
         "across the middle from a corner of the twelve is a corner, and from a triangle's middle a triangle's middle; in a form of four corners it is a triangle's middle. Exhibit THIRTY's 508 lays a corner, the middle and a face's middle on one line, with its own unsure of a four-faced form")

    # the one triangle of three right angles, fifteen
    a5, a3, a2 = f.angle_at(f.V5, f.V3, f.V2), f.angle_at(f.V3, f.V2, f.V5), f.angle_at(f.V2, f.V5, f.V3)
    line("is", all(abs(x - y) < 1e-6 for x, y in ((a5, 36), (a3, 60), (a2, 90))) and 120 * 6 == 720 == 8 * 90,
         "a small triangle is of 36, 60 and 90, 6 over 180: 120 of them are 720, as eight of 90 over are")
    seen, rounds = set(), []
    for g in INSIDE:
        k = f.key((g @ P0).reshape(1, 3))
        if k in seen: continue
        orbit = {f.key((np.linalg.matrix_power(R3, n) @ g @ P0).reshape(1, 3)) for n in range(3)}; seen |= orbit; rounds.append(len(orbit))
    line("is", len(INSIDE) == 15 and rounds == [3] * 5, "the one triangle of three right angles is fifteen of the 120: five threes, by its own round of three corners")
    on_side = [[c for c in r if min(c) >= 0] for r in RECT]
    cut = cut_of_a_side()
    line("is", [len(x) for x in on_side] == [1, 1, 1] and abs(sum(cut) - 90) < 1e-9 and abs(np.tan(np.radians(cut[0])) - 1 / PHI) < 1e-9
         and all(abs(x - y) < 0.005 for x, y in zip(cut, (31.72, 37.38, 20.91))),
         f"a side of the one triangle is with one corner of a rectangle, a corner of five: from a corner {cut[0]:.2f}, then {cut[1]:.2f} to a corner of three, then {cut[2]:.2f}: 90")
    mirrors = [g for g in G if np.linalg.det(g) < 0 and abs(np.trace(g) - 1) < 1e-6]
    normals = [f.unit(((np.eye(3) - m) / 2)[:, int(np.argmax(np.abs(np.diag((np.eye(3) - m) / 2))))]) for m in mirrors]
    threes = [c for c in itertools.combinations(range(15), 3) if all(abs(normals[i] @ normals[j]) < 1e-6 for i, j in itertools.combinations(c, 2))]
    line("is", len(mirrors) == 15 and len(threes) == 5 and sorted(i for c in threes for i in c) == list(range(15)),
         "its mirrors are fifteen, five threes of mirrors at right angles: the one triangle's own figure is on this sphere five ways")
    signed = [g for g in G if np.allclose(np.abs(g), np.round(np.abs(g))) and np.allclose(np.abs(g) @ np.ones(3), np.ones(3))]
    line("found", len(signed) == 24 and abs(np.trace(f.ROUND5) - PHI) < 1e-9,
         "24 of the 120 are moves of the 57th's eight triangles; the round of five is none of them, and its number is φ, no whole number: it is given to the form, and no move of the 57th makes it")

    # nought to sixty, and a line of five names to a surface
    behind, ahead = [p for p in range(1, 25) if is_prime(p)], [p for p in range(25, 61) if is_prime(p)]
    line("is", (len(behind), len(ahead)) == (9, 8) and behind[-1] == 23 and 25 == 5 * 5 and ahead[-1] == 59 and "seventeen primes two to fifty-nine" in numbers,
         "nought to sixty is 24 and 36, as the sixty moves are: nine primes to 24 and eight after it, seventeen, 2 to 59; 23 and 25, five fives, are beside 24")
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    col = next(j for j, h in enumerate(table[0]) if h.startswith("its prime, by its position"))
    prime_of = {n: int(table[n][col]) for n in range(1, 18)}
    names = {n: table[n][0] if re.match(r"\d+-", table[n][0]) else next(x for x in table[n] if re.match(rf"{n}-[a-z-]+$", x)) for n in range(1, 18)}
    line("is", [prime_of[n] for n in range(1, 18)] == behind + ahead and prime_of[12] == 37 and prime_of[17] == 59,
         "the one table lays a name's prime by its position: 2 at 1-now-existing to 59 at 17-next-existing, and 37 at 12-next-co-same-existing")
    five = [prime_of[n] for n in FIVE_NAMES]
    line("is", five == [5, 7, 11, 17, 19] and sum(five) == 59 and prime_of[17] == 59 and all(n < 10 for n in FIVE_NAMES),
         "five names before 10, the 3rd, 4th, 5th, 7th and 8th, are with the primes 5, 7, 11, 17 and 19: they add to 59, the seventeenth prime, a surface")
    line("found", sum((25, 35, 45, 55)) == 160,
         "Exhibit THIRTY's 509 is with its own unsure: five names before 10, or fives going up, 25, 35, 45 and 55. The five names add to 59; the fives going up add to 160")

    # the seventeen names across and along, and the numbered sentences
    line("is", "possibling across, 2, 6, 10 and 14, and discovering and existing along, 9 and 17" in sent.get(301, "") and "14-next-possibling is across" in naming
         and "13-next-discovering along" in naming and "12-next-co-same-existing both across and along" in naming,
         "across are 2, 6, 10 and 14, possibling; along are 9, 13 and 17; and 12 is across and along both, the surface: as Exhibit THIRTY and Natural Naming say them")
    line("placing", True, "the names across are laid at a rectangle's across, 2, and the names along at its along, 2φ: the drawing's own placing")
    missing = [n for n, phrase in SENTENCES.items() if phrase not in sent.get(n, "")]
    line("is", not missing, "Exhibit THIRTY's numbered sentences are opened beside the drawing's parts: " + ", ".join(map(str, sorted(SENTENCES))))
    line("is", "Twelve corners closing as a sphere and winding through one opening as a torus" in naming and "stable-forming across 1 to 17" in naming
         and "## 3.3 A pentagon, rectangles and an icosahedron" in illus and "five triples of perpendicular half-rotation axes" in maths,
         "Natural Naming, Natural Mathematics and Natural Illustrating say the twelve corners, the five threes and the part of the drawings asked")
    own = {"cut": cut, "prime_of": prime_of, "names": names, "behind": behind, "ahead": ahead, "normals": normals}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
