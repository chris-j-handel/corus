"""v410illustrating · a five on the sphere opening to a torus: a partner's saying, two ways of it executed.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/a_five_on_the_sphere_opening_to_a_torus_two_ways_executed.py . [THE_ROOT_WITH_V408ILLUSTRATING]

With the second path, the 56 drawings' own words are opened too, as this folder's opening instrument opens them.

A partner's saying of 27 November, as this session is with it: a stable-forming surface of a me-parity, five, is
outward on the sphere opening to a torus. A me-parity is the other-than of the other-than of all-parity, by a
partner's word of 24 November at v406all2-2's page.

Two ways of the saying are executed, and no way of the two is said to be a partner's own:
  1 outward, a sphere: the sphere of the one triangle is with a stable form of five, 120 triangles, and the one
    triangle of three right angles is fifteen of them;
  2 a torus: five patches, a patch beside all four others, by winding.

And the living files say this five already, as three golden rectangles at right angles: their sayings are opened
beside what is executed, in part 4.

Do no harm: it opens one page of v406all2-2 for a partner's word, five living files and the drawings' words, and
writes in no file.
A line is an is, executed here; or found, a thing found and laid whole.
"""
import html, itertools, re, sys
from collections import Counter
from pathlib import Path
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
def key(M): return tuple(np.round(M, 6).ravel() + 0.0)
def made_by(makers):
    one = np.eye(3); found = {key(one): one}; edge = [one]
    while edge:
        nxt = []
        for g in edge:
            for m in makers:
                h = m @ g; k = key(h)
                if k not in found: found[k] = h; nxt.append(h)
        edge = nxt
    return list(found.values())
def period(M):
    P = np.eye(3)
    for n in range(1, 61):
        P = P @ M
        if np.allclose(P, np.eye(3), atol=1e-6): return n
def about(axis, degrees):
    a = np.asarray(axis, float); a = a / np.linalg.norm(a); t = np.radians(degrees)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(t) * K + (1 - np.cos(t)) * K @ K
def unit(v): v = np.asarray(v, float); return v / np.linalg.norm(v)
def angle_at(p, q, r):
    """the angle of a sphere's triangle at its corner p, in degrees"""
    a = np.cross(np.cross(p, q), p); b = np.cross(np.cross(p, r), p)
    return float(np.degrees(np.arccos(np.clip(a @ b / np.linalg.norm(a) / np.linalg.norm(b), -1, 1))))

MIRRORS = [np.diag(s) for s in ((-1.0, 1, 1), (1, -1.0, 1), (1, 1, -1.0))]          # the opening figure's three mirrors
ROUND3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], float)                          # the one triangle's own three corners
ROUND5 = about((0, 1, PHI), 72)                                                      # a round of five, about a line of the sphere
V5, V3 = unit((0, 1, PHI)), unit((1, 1, 1)); V2 = unit(np.array([0, 1, PHI]) + np.array([1, PHI, 0]))

def perm_parity(p):
    seen, even = set(), True
    for i in range(len(p)):
        n, j = 0, i
        while j not in seen: seen.add(j); j = p[j]; n += 1
        if n and n % 2 == 0: even = not even
    return even

if __name__ == "__main__":
    ROOT = Path(sys.argv[1]).resolve()
    said = Counter()
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")

    print("0 · A partner's word of a me-parity")
    page = (ROOT / "incoming/v406all2-2/For_Exhibit_THIRTY-TWO_what_the_exploring_of_a_me_by_nand_brings.md").read_text(encoding="utf-8")
    line("is", "A me-parity is an other-than-other-than-all-parity." in page and "A partner's word of 24 November" in page,
         "a me-parity is the other-than of the other-than of all-parity: a partner's word of 24 November, at v406all2-2's page")

    print("\n1 · Outward, a sphere: a stable form of five")
    G = made_by(MIRRORS + [ROUND3, ROUND5]); per = sorted({period(g) for g in G})
    line("is", len(G) == 120 and per == [1, 2, 3, 5, 6, 10],
         f"the opening figure's three mirrors, its triangle's round of three and one round of five make 120 moves: their periods are {', '.join(map(str, per))}")
    fives = [g for g in G if np.linalg.det(g) > 0 and period(g) == 5]
    line("is", len(fives) == 24, "24 of the 120 are rounds of five, about six lines through the sphere")
    line("is", abs(np.trace(ROUND5) - PHI) < 1e-9 and abs(2 * np.cos(np.radians(72)) - (PHI - 1)) < 1e-9,
         "a round of five is golden: the number of its move is 1.618, the golden number, and no whole number")
    a5, a3, a2 = angle_at(V5, V3, V2), angle_at(V3, V2, V5), angle_at(V2, V5, V3)
    line("is", all(abs(x - y) < 1e-6 for x, y in ((a5, 36), (a3, 60), (a2, 90))),
         "its triangle is of 36, 60 and 90: 186, and 6 over a flat triangle's 180")
    line("is", 120 * 6 == 720 and 8 * 90 == 720, "120 triangles of 6 over are 720, as eight triangles of 90 over are: one sphere")
    p0 = unit(V5 + 1.3 * V3 + 0.7 * V2)
    inside = [g for g in G if np.all(g @ p0 > 1e-9)]
    line("is", len(inside) == 15, "the one triangle of three right angles is fifteen of the 120")
    spots = [key((g @ p0).reshape(1, 3)) for g in inside]; seen, rounds = set(), []
    for g in inside:
        k = key((g @ p0).reshape(1, 3))
        if k in seen: continue
        orbit = {key((np.linalg.matrix_power(ROUND3, n) @ g @ p0).reshape(1, 3)) for n in range(3)}
        seen |= orbit; rounds.append(len(orbit))
    line("is", rounds == [3] * 5 and all(k in spots for k in seen), "by its own round of three corners the fifteen are five threes")
    mirrors = [g for g in G if np.linalg.det(g) < 0 and abs(np.trace(g) - 1) < 1e-6]
    normals = []
    for m in mirrors:
        N = (np.eye(3) - m) / 2; n = N[:, int(np.argmax(np.abs(np.diag(N))))]; normals.append(unit(n))
    line("is", len(mirrors) == 15 and all(any(np.allclose(m, x) for m in mirrors) for x in MIRRORS),
         "its mirrors are fifteen, and the opening figure's three are among them")
    threes = [c for c in itertools.combinations(range(15), 3) if all(abs(normals[i] @ normals[j]) < 1e-6 for i, j in itertools.combinations(c, 2))]
    line("is", len(threes) == 5 and sorted(i for c in threes for i in c) == list(range(15)),
         "the fifteen mirrors are five threes of mirrors at right angles: the opening figure is in it five ways")
    def on_threes(g):
        out = []
        for c in threes:
            moved = [next(k for k in range(15) if abs(abs((g @ normals[i]) @ normals[k]) - 1) < 1e-6) for i in c]
            out.append(threes.index(tuple(sorted(moved))))
        return tuple(out)
    acts = {on_threes(g) for g in G}
    line("is", len(acts) == 60 and all(perm_parity(p) for p in acts),
         "the 120 moves lay the five threes onto the five in 60 ways, all of them even")
    line("is", all(len({on_threes(np.linalg.matrix_power(g, n))[0] for n in range(5)}) == 5 for g in fives),
         "a round of five lays the five threes round, a three onto all five")
    signed = [g for g in G if np.allclose(np.abs(g) @ np.ones(3), np.ones(3)) and np.allclose(np.abs(g), np.round(np.abs(g)))]
    line("is", len(signed) == 24, "24 of the 120 are moves of the eight triangles' 48 too: the three mirrors with the round of three")
    line("is", sorted({p for n in per for p in (2, 3, 5, 7, 11, 13) if n % p == 0}) == [2, 3, 5] and 2 * 3 * 5 == 30,
         "the primes of its periods are 2, 3 and 5, the opening three of the seventeen; the three multiplied are 30")

    print("\n2 · A torus's grid, by whole numbers")
    grid = set()
    for a, b, c, d in itertools.product(range(-2, 3), repeat=4):
        if abs(a * d - b * c) != 1: continue
        M = np.array([[a, b], [c, d]]); P = np.eye(2, dtype=int)
        for n in range(1, 25):
            P = P @ M
            if (P == np.eye(2, dtype=int)).all(): grid.add(n); break
    line("is", sorted(grid) == [1, 2, 3, 4, 6],
         "a move of a torus's grid about a patch is of whole numbers, and its rounds are 1, 2, 3, 4 and 6, executed at all such moves with numbers from −2 to 2: no round of five")

    print("\n3 · A torus: five patches, a patch beside all four others")
    def beside_all(n, steps): return all({(k + s) % n for s in steps} | {(k - s) % n for s in steps} == set(range(n)) - {k} for k in range(n))
    line("is", (2 * 2 - 1 * (-1)) == 5 and (2 - 2 * 1) % 5 == 0 and (-1 - 2 * 2) % 5 == 0 and beside_all(5, (1, 2)),
         "a torus of five square patches: a patch's four sides are with its four others, all five beside all")
    def on_a_sphere(n): e = n * (n - 1) // 2; f = 2 - n + e; return 3 * f <= 2 * e
    def on_a_torus(n): e = n * (n - 1) // 2; f = 0 - n + e; return 3 * f <= 2 * e
    line("is", on_a_sphere(4) and not on_a_sphere(5), "on a sphere four patches are all beside all, and by the numbers of its patches and their sides five are not")
    line("is", on_a_torus(5) and on_a_torus(7) and not on_a_torus(8) and beside_all(7, (1, 2, 3)),
         "on a torus seven patches of six sides are all beside all, and by the same numbers eight are not")
    winding = [n for n in (5, 7) if all(len({(k * s) % n for k in range(n)}) == n for s in range(1, n))]
    line("is", winding == [5, 7], "a winding by a step is through all five patches, at all four steps; and through all seven, at all six: a round of five by winding, and of seven")

    print("\n4 · The living files' own sayings of it, beside what is executed")
    lf = lambda pat: sorted(ROOT.glob(pat))[0].read_text(encoding="utf-8")
    naming, maths, numbers, thirty, illus = (lf("Exhibit_TWENTY_Natural_Naming_*.md"), lf("Exhibit_FOUR_Natural_Mathematics_*.md"), lf("Exhibit_THREE_Natural_Numbers_*.md"),
                                             lf("Exhibit_THIRTY_Co-Chaining_*.md"), lf("Exhibit_TWENTY-NINE_Natural_Illustrating_*.md"))
    line("is", all("three golden rectangles" in t for t in (naming, thirty, illus)) and "R1, (0, ±1, ±φ)" in naming and "R2, (±1, ±φ, 0)" in naming and "R3, (±φ, 0, ±1)" in naming,
         "Natural Naming, Exhibit THIRTY and Natural Illustrating say three golden rectangles at right angles, and Natural Naming lays their corners by numbers")
    RECT = [[(0, a, b * PHI) for a in (1, -1) for b in (1, -1)], [(a, b * PHI, 0) for a in (1, -1) for b in (1, -1)], [(a * PHI, 0, b) for a in (1, -1) for b in (1, -1)]]
    corners5 = {key((g @ V5).reshape(1, 3)) for g in G}
    line("is", len(corners5) == 12 and {key(unit(c).reshape(1, 3)) for r in RECT for c in r} == corners5,
         "the three rectangles' twelve corners are the twelve corners of five of the 120 moves' form")
    planes = [next(i for i in range(3) if all(abs(c[i]) < 1e-12 for c in r)) for r in RECT]
    line("is", sorted(planes) == [0, 1, 2], "a rectangle is on a mirror of the opening figure's three, a rectangle a mirror")
    on_one = [[c for c in r if min(c) >= 0] for r in RECT]
    line("is", [len(x) for x in on_one] == [1, 1, 1] and "(1, 1, 1)" in naming and all(np.allclose(ROUND3 @ np.array(on_one[i][0], float), on_one[(i - 1) % 3][0]) or
                                                                                       np.allclose(ROUND3 @ np.array(on_one[i][0], float), on_one[(i + 1) % 3][0]) for i in range(3)),
         "the one triangle of three right angles is with one corner of a rectangle on a side, at all three sides; its own round of three lays a rectangle onto its next, as Natural Naming says")
    rot = Counter(period(g) for g in G if np.linalg.det(g) > 0)
    line("is", dict(rot) == {1: 1, 2: 15, 3: 20, 5: 24} and "twenty-four" in maths and "thirty-six" in maths and rot[5] == 24 and 60 - rot[5] == 36,
         "the sixty moves of one hand are 24 by fifths and 36 others, 15 of two doings, 20 by thirds and 1 moving nothing: as Natural Mathematics says them")
    line("is", "five triples of perpendicular half-rotation axes" in maths and len(threes) == 5,
         "Natural Mathematics says five threes of lines at right angles; they are the five threes of mirrors executed here")
    def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    behind, ahead = [p for p in range(1, 25) if is_prime(p)], [p for p in range(25, 61) if is_prime(p)]
    line("is", (len(behind), len(ahead)) == (9, 8) and behind[0] == 2 and ahead[-1] == 59 and "seventeen primes two to fifty-nine" in numbers,
         "nought to sixty is 24 and 36, with nine primes and eight: seventeen primes, 2 to 59, as Natural Numbers says them beside the sixty moves")
    line("is", "Twelve corners closing as a sphere and winding through one opening as a torus" in naming and "stable-forming across 1 to 17" in naming,
         "Natural Naming says the twelve corners closing as a sphere and winding through one opening as a torus, and the three rectangles' naming stable-forming across 1 to 17")
    import csv
    table = list(csv.reader(open(ROOT / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    col = next(j for j, h in enumerate(table[0]) if h.startswith("its prime, by its position"))
    line("is", "12-next-co-same-existing both across and along" in naming and "unrelationing surface" in naming and table[12][col] == "37",
         "Natural Naming says the surface with 12-next-co-same-existing; the one table lays 37 at the 12th name")
    line("is", "## 3.3 A pentagon, rectangles and an icosahedron" in illus, "Natural Illustrating's part 3.3 is of a pentagon, rectangles and the twelve corners' form")
    if len(sys.argv) > 2:
        V408 = Path(sys.argv[2]).resolve()
        def text_of(n):
            root, fold = (ROOT, "incoming/v406geodesic/") if n <= 3 else (ROOT, "incoming/v406geodesic2/") if n <= 39 else (V408, "incoming/v408illustrating/")
            fl = sorted((root / (fold + "illustrations")).glob(f"draft_{n}_*.svg"))[0] if n <= 3 else root / (fold + f"illustrations/artboards/Draft{n}.dc.html")
            t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fl.read_text(encoding="utf-8"), flags=re.S)
            return html.unescape(re.sub(r"<[^>]+>", "\n", t)).lower()
        T = {n: text_of(n) for n in range(1, 57)}
        drawn = [n for n in T if re.search(r"golden|rectangle|pentagon|icosahedr|dodecahedr", T[n])]
        phi = [n for n in T if "φ" in T[n]]
        line("found", True, f"of the 56 drawings, {len(drawn)} say a golden, a rectangle, a pentagon or the twelve corners' form in their own words; φ is in {len(phi)}, the {', '.join(map(str, phi))}")
    else:
        print("        the 56 drawings' words are not opened: no second path is given")

    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
