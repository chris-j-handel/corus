"""v410illustrating · the check of the 57th drawing, a candidate: One Triangle, Three Right Angles · Bi-Folding 1 to 17,
a Sphere Opening to a Torus. The opening figure of twelve, laid beside the 1st to the 6th drawings it gathers.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_one_triangle_three_right_angles_bi-folding_1_to_17.py .

It writes no file. Its numbers are executed here by its own arithmetic, ahead of the drawing; the drawing's marks are
this module's own values, opened by the maker. It opens Exhibit ONE and Exhibit THIRTY at the root for their own table
and numbered sentences, and writes in neither.

What the six drawings' own checks execute is executed again here, by this session's hand: the triangle and its names
(the 4th), two folds and a torus of sixteen patches (the 2nd and the 3rd), and the co-linear (the 5th).
A line is an is, executed here; or found, a thing found and laid whole; or a placing, laid as an other drawing lays it.
"""
import re, sys
from collections import Counter
from pathlib import Path
import numpy as np

A, B, C = np.array([0, 0, 1.0]), np.array([1.0, 0, 0]), np.array([0, 1.0, 0])      # the me at A; B and C on the me's horizon
CORNER = {"A": A, "B": B, "C": C}

# ---- the seventeen names on the one triangle, as the 4th drawing lays them
SELF_WAY = ["A", ("A", "B"), "B", ("B", "C"), "C", ("C", "A"), "A"]       # names 2 to 8
OTHER_WAY = ["A", ("A", "C"), "C", ("C", "B"), "B", ("B", "A"), "A"]      # names 10 to 16
ON = {1: "A", 9: "A", 17: "A"}
ON.update({2 + i: p for i, p in enumerate(SELF_WAY)})
ON.update({10 + i: p for i, p in enumerate(OTHER_WAY)})
MOMENT = {2: "prior", 4: "now", 6: "next", 8: "same", 10: "prior", 12: "now", 14: "next", 16: "same"}
def said(n):
    """A name's own on the triangle, in words for the drawing's table."""
    p = ON[n]
    if n == 17: return "the me, a next 1"
    if n in (1, 9): return "the me"
    if isinstance(p, tuple): return f"{'the me' if p[0] == 'A' else p[0]} to {'the me' if p[1] == 'A' else p[1]}"
    return f"{'the me' if p == 'A' else p} · {MOMENT[n]}"

# ---- the moves
up8 = lambda n: n + 8
less17 = lambda n: 17 - n
BI_FOLDINGS = [[n, up8(n), less17(up8(n)), up8(less17(up8(n)))] for n in (1, 2, 3, 4)]     # 8 up, 17 less, 8 up; 17 less to its opening name

# ---- a torus of sixteen patches, as the 3rd drawing's check lays them: n - 1 in four binary digits
BAND = ["outward, the me's side", "inward, the me's side", "inward, the far side", "outward, the far side"]
def patch(n):
    k = n - 1
    return k & 3, k >> 2                      # its quarter round the opening, its band round the tube
def curvature(n, m=4000):
    j = patch(n)[1]; a, b = np.radians(90 * j), np.radians(90 * j + 90)
    phi = a + (np.arange(m) + 0.5) / m * (b - a)
    return float(np.sum(np.cos(phi)) * (b - a) / m * (np.pi / 2))
RR, rr = 1.0, 0.42
def surf(theta, phi): return np.array([(RR + rr * np.cos(phi)) * np.cos(theta), (RR + rr * np.cos(phi)) * np.sin(theta), rr * np.sin(phi)])
def name_at(x):
    th = np.degrees(np.arctan2(x[1], x[0])) % 360; ph = np.degrees(np.arctan2(x[2], np.hypot(x[0], x[1]) - RR)) % 360
    return (int(ph // 90) << 2 | int(th // 90)) + 1
def samples(n, m=5):
    q, j = patch(n)
    return [(np.radians(90 * q + (a + 0.5) / m * 90), np.radians(90 * j + (b + 0.5) / m * 90)) for a in range(m) for b in range(m)]
OVER = np.diag([1.0, -1.0, -1.0])            # two right spiral steps about the co-linear, the line through B

def exhibit(root, stem): return sorted(Path(root).glob(stem))[0].read_text(encoding="utf-8")
def names_of(one):
    return re.findall(r"^\| (\d+) \| \*\*(\d+-[a-z-]+)\*\* \| ([^|]+?) \| ([^|]+?) \| (\w+) \| ([a-z-]+) \|", one, flags=re.M)
def entering(thirty, names):
    """The numbered sentence of Exhibit THIRTY a name is said whole at, with none ahead of it."""
    out = {}
    for m in re.finditer(r"^(\d+)\. (.*)$", thirty, flags=re.M):
        k, s = int(m.group(1)), m.group(2)
        for n, name in names:
            if n not in out and re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", s): out[n] = k
    return out
EIGHT = ["co", "bi", "co", "bi", "co", "bi", "tri", "bi"]
def three_of(n): return "-".join(EIGHT[(k - 1) % 8] for k in (n, n - 1, n - 2))

def checks(root):
    lines = []
    def line(kind, ok, words): lines.append((kind if ok else "is-not", words))
    # the triangle
    def angle(P, Q, S):
        q, s = Q - (Q @ P) * P, S - (S @ P) * P
        return np.degrees(np.arccos(q @ s / np.linalg.norm(q) / np.linalg.norm(s)))
    angs = [angle(A, B, C), angle(B, C, A), angle(C, A, B)]
    line("is", all(abs(a - 90) < 1e-9 for a in angs) and abs(sum(angs) - 180 - 90) < 1e-9 and abs(np.radians(90) * 8 - 4 * np.pi) < 1e-9,
         "one triangle is three right angles, 270, and 90 over a flat triangle's 180: one of eight alike on a sphere")
    # the names on it
    one_way = sorted(n for n in ON if isinstance(ON[n], tuple)); moments = sorted(MOMENT)
    line("is", sorted(ON) == list(range(1, 18)) and one_way == [3, 5, 7, 11, 13, 15] and moments == [2, 4, 6, 8, 10, 12, 14, 16]
         and len(one_way) + len(moments) == 14 and [n for n in ON if n not in one_way and n not in moments] == [1, 9, 17],
         "seventeen names are on it: 1, 9 and 17 at the me; six one-way me-parities on its sides; eight moments at its corners: 6 + 4 + 4 = 14 of 17")
    chained = lambda r: all(r[i][1] == r[i + 1] and r[i][0] == r[i - 1] for i in (1, 3, 5)) and r[0] == r[-1] == "A"
    line("is", chained(SELF_WAY) and chained(OTHER_WAY) and [tuple(reversed(p)) for p in OTHER_WAY[5:0:-2]] == [p for p in SELF_WAY[1::2]],
         "a way round goes corner, side, corner, side, corner, side, and is at a next me; an other's is a me's, its other way")
    line("is", ON[2] == ON[8] == ON[10] == ON[16] == "A" and {ON[4], ON[14]} == {"B"} and {ON[6], ON[12]} == {"C"},
         "prior and same are at the me, with both ways; now and next are at B and C, and at C and B")
    # a fold through the me
    mir = np.array([[0, 1.0, 0], [1.0, 0, 0], [0, 0, 1.0]])
    name_of = lambda v: next(k for k, c in CORNER.items() if np.allclose(v, c))
    fold = lambda p: name_of(mir @ CORNER[p]) if isinstance(p, str) else (name_of(mir @ CORNER[p[0]]), name_of(mir @ CORNER[p[1]]))
    line("is", fold("A") == "A" and fold("B") == "C" and all(fold(ON[n]) == ON[n + 8] for n in range(1, 10)) and fold(fold(ON[1])) == ON[17],
         "a fold through the me lays B onto C: a name's own is onto its name 8 up, at 1 to 9; two such folds, its own again, 1 as 17")
    # two folds on two sides at a right angle
    f1, f2 = np.diag([1.0, 1.0, -1.0]), np.diag([1.0, -1.0, 1.0]); two = f2 @ f1
    step = np.array([[1.0, 0, 0], [0, 0, -1.0], [0, 1.0, 0]])            # a right spiral step about the line through B
    line("is", np.linalg.det(f1) < 0 and np.linalg.det(two) > 0 and np.allclose(two, OVER) and np.allclose(step @ step, OVER) and np.allclose(two @ B, B)
         and np.allclose(two @ np.array([1.0, 1.0, 1.0]), [1, -1, -1]),
         "one fold on a side is a mirror; two folds on two sides at a right angle are two right spiral steps about the corner between, both inverting at one step: B as it was, + + + onto + − −")
    # the co-linear
    cross = np.cross([0, 0, 1.0], [0, 1.0, 0])                        # the two folds' circles are in the planes z = 0 and y = 0
    line("is", np.allclose(np.abs(cross / np.linalg.norm(cross)), B), "the two folds' circles are with two points both, B and the point across the sphere from it: the line through the two, through the 0, is the co-linear")
    w, v = np.linalg.eig(OVER); fixed = [v[:, i] for i in range(3) if abs(w[i] - 1) < 1e-9]
    line("is", len(fixed) == 1 and np.allclose(np.abs(fixed[0]), B), "two right spiral steps about the co-linear leave two points of a sphere as they were, its two ends, and no other")
    quarters = [(1, 1), (-1, 1), (-1, -1), (1, -1)]                    # round the co-linear, by the side of the two circles: C's and A's
    line("is", all(sum(a != b for a, b in zip(quarters[i], quarters[(i + 1) % 4])) == 1 for i in range(4)),
         "round the co-linear are four quarters, and a step from a quarter to its next is one fold, one parity of the two inverting")
    line("placing", True, "the four quarters' names are laid as the 5th and the 6th drawings lay them: possibling and a +; co-possibling and a + and a −; possibling and a −; co-possibling and none")
    # the torus
    curv = {n: curvature(n) for n in range(1, 17)}
    outward = [n for n in curv if patch(n)[1] in (0, 3)]; inward = [n for n in curv if patch(n)[1] in (1, 2)]
    line("is", all(abs(abs(c) - np.pi / 2) < 1e-5 for c in curv.values()) and outward == [1, 2, 3, 4, 13, 14, 15, 16] and inward == list(range(5, 13))
         and abs(sum(curv[n] for n in outward) - 4 * np.pi) < 1e-4 and abs(sum(curv.values())) < 1e-4,
         "a torus of sixteen patches, a name a patch: outward 1 to 4 and 13 to 16, the eight triangles of a sphere, 720; inward 5 to 12, 720 the other way: a torus is at nought")
    line("is", all({name_at(OVER @ surf(t, p)) for t, p in samples(n)} == {17 - n} for n in range(1, 17)),
         "two folds about the co-linear lay a name's patch onto the patch of 17 less it, its podal from 1 to 16, at all sixteen")
    line("is", all(patch(n)[0] == patch(n + 8)[0] and patch(n)[1] ^ 2 == patch(n + 8)[1] for n in range(1, 9)),
         "8 up is through the tube: one quarter, and the band across it")
    line("is", all(patch(n)[1] in (0, 1) for n in range(1, 9)) and all(patch(n)[1] in (2, 3) for n in range(9, 17)) and patch(17 - 16) == patch(1),
         "1 to 8 are on the me's side of a torus and 9 to 16 on its far side; 17 is at a next 1")
    rests = [(t, p) for t in (0, np.pi) for p in (0, np.pi) if np.allclose(OVER @ surf(t, p), surf(t, p))]
    spin = lambda a: np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1.0]])
    moved = all(np.linalg.norm(spin(0.3) @ surf(t, p) - surf(t, p)) > 1e-3 for t in np.linspace(0, 6.2, 9) for p in np.linspace(0, 6.2, 9))
    line("found", len(rests) == 4 and moved,
         "the 3rd drawing's torus is opened along the me's line, and the co-linear is across its opening: 17 less leaves four points of it as they were. The 5th opens a sphere along the co-linear. The two openings are at a right angle, and are not one yet")
    # Exhibit ONE and Exhibit THIRTY
    one = exhibit(root, "Exhibit_ONE_Natural_Resolver_*.md"); thirty = exhibit(root, "Exhibit_THIRTY_Co-Chaining_*.md")
    own = names_of(one); names = [(int(n), name) for n, name, *_ in own]
    line("is", len(own) == 17 and all(three_of(int(n)) == t for n, _, _, _, _, t in own),
         "Exhibit ONE's own table: seventeen names, and a name's three is its prefix and the two names' before it, of the eight co bi co bi co bi tri bi")
    three = {int(n): t for n, _, _, _, _, t in own}
    line("is", three[1] == three[9] == three[17] == "co-bi-tri", "1, 9 and 17 are one three in Exhibit ONE's table, co-bi-tri, next, now and prior")
    line("found", True, "the 4th drawing says tri-bi-co at 1 and 17, prior, now and next, by a partner's saying; the asking of it is open, and this drawing lays both")
    folds = "Each goes two folds in turn, 17 less and a move of 8"
    line("found", folds in one, "17 less is said three ways: one fold of a bi-folding's two in Exhibit ONE; two folds on two sides at the 2nd and the 3rd drawings; and at the 4th a one-way me-parity with the corner it comes to")
    flat = sorted(n for b in BI_FOLDINGS for n in b)
    line("is", flat == list(range(1, 17)) and all(less17(b[3]) == b[0] for b in BI_FOLDINGS) and [b[0:2] for b in BI_FOLDINGS] == [[1, 9], [2, 10], [3, 11], [4, 12]],
         "four bi-foldings, sixteen names once: 8 up, 17 less, 8 up and 17 less are at the opening name again, as 1, 9, 8, 16 and 1")
    ent = entering(thirty, names)
    line("is", len(ent) == 17 and ent[1] == ent[2] == 129 and ent[17] == 241 and max(ent.values()) == 572,
         "Exhibit THIRTY says all seventeen names whole, a name at a numbered sentence of its own entering: 1 and 2 at 129, 17 at 241, and 6 at 572, the last")
    return lines, own, ent

if __name__ == "__main__":
    lines, own, ent = checks(sys.argv[1])
    for kind, words in lines: print(f"{kind:8s}{words}")
    c = Counter(k for k, _ in lines)
    print(f"\n{c['is']} are is; {c['found']} are found, whole; {c['placing']} is a placing" + (f"; {c['is-not']} IS-NOT" if c["is-not"] else ""))
    sys.exit(1 if c["is-not"] else 0)
