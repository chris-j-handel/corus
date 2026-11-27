"""v410illustrating · twelve corners closing as a sphere, and winding through one opening as a torus: one way of it, executed.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/twelve_corners_closing_as_a_sphere_and_winding_through_one_opening_as_a_torus.py .

Natural Naming says the three golden rectangles' twelve corners closing as a sphere and winding through one opening
as a torus, one and then the other. The 57th drawing says a sphere opening to a torus, 720 and nought; the 58th says
the twelve corners. This instrument executes one way of the two as one: the twelve corners' sphere opened at two
corners across from one another, and its ten triangles of those two corners laid through the opening.

The way is this session's own making, and no living file says it in these numbers. It is a candidate for breaking.
Do no harm: it opens Natural Naming for one sentence, and writes in no file.
A line is an is, executed here; or found, a thing found and laid whole.
"""
import itertools, sys
from collections import Counter
from pathlib import Path
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
CORNERS = [np.array(c, float) for c in
           [(0, a, b * PHI) for a in (1, -1) for b in (1, -1)] + [(a, b * PHI, 0) for a in (1, -1) for b in (1, -1)] + [(b * PHI, 0, a) for a in (1, -1) for b in (1, -1)]]

def surface(tris):
    """a surface of triangles: its corners, its sides, the triangles to a corner, and its number of corners less sides and triangles"""
    sides = Counter(tuple(sorted(p)) for t in tris for p in itertools.combinations(t, 2))
    corners = sorted({i for t in tris for i in t}); at = Counter(i for t in tris for i in t)
    return corners, sides, at, len(corners) - len(sides) + len(tris)
def one_piece(tris):
    seen, edge = {0}, [0]
    while edge:
        k = edge.pop()
        for j, t in enumerate(tris):
            if j not in seen and len(set(t) & set(tris[k])) == 2: seen.add(j); edge.append(j)
    return len(seen) == len(tris)
def with_a_hand(tris):
    """all triangles laid round one way together, a side gone along both ways by its two triangles"""
    order = {0: tuple(tris[0])}; edge = [0]
    while edge:
        k = edge.pop(); a = order[k]; went = {(a[i], a[(i + 1) % 3]) for i in range(3)}
        for j, t in enumerate(tris):
            shared = set(t) & set(tris[k])
            if j == k or len(shared) != 2: continue
            for cand in (tuple(t), (t[0], t[2], t[1])):
                mine = {(cand[i], cand[(i + 1) % 3]) for i in range(3)}
                if not (mine & went): break
            if j in order:
                if {(order[j][i], order[j][(i + 1) % 3]) for i in range(3)} & went: return False
            else: order[j] = cand; edge.append(j)
    return len(order) == len(tris)

if __name__ == "__main__":
    ROOT = Path(sys.argv[1]).resolve()
    said = Counter()
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")
    naming = sorted(ROOT.glob("Exhibit_TWENTY_Natural_Naming_*.md"))[0].read_text(encoding="utf-8")
    line("is", "Twelve corners closing as a sphere and winding through one opening as a torus" in naming,
         "Natural Naming says the twelve corners closing as a sphere and winding through one opening as a torus, one and then the other")

    print("\n1 · Twelve corners closing as a sphere")
    beside = lambda i, j: abs(np.linalg.norm(CORNERS[i] - CORNERS[j]) - 2) < 1e-9
    sphere = [t for t in itertools.combinations(range(12), 3) if all(beside(i, j) for i, j in itertools.combinations(t, 2))]
    corners, sides, at, number = surface(sphere)
    line("is", (len(corners), len(sides), len(sphere)) == (12, 30, 20) and number == 2 and set(sides.values()) == {2} and set(at.values()) == {5} and one_piece(sphere) and with_a_hand(sphere),
         "twelve corners, 30 sides and 20 triangles, a side with two triangles: 12 less 30 and 20 is 2, a sphere; five triangles to a corner")
    short = lambda k: 360 - 60 * k
    line("is", 12 * short(5) == 720 and 12 * 5 == 20 * 3 == 30 * 2 == 60,
         "five triangles of 60 at a corner are 300, 60 short of a whole round: twelve corners are 720 short together, a sphere's 720; and sixty three ways")

    print("\n2 · Opened at two corners across from one another")
    a = 0; b = next(j for j in range(12) if np.allclose(CORNERS[j], -CORNERS[a]))
    axis = CORNERS[a] / np.linalg.norm(CORNERS[a]); t5 = np.radians(72)
    K = np.array([[0, -axis[2], axis[1]], [axis[2], 0, -axis[0]], [-axis[1], axis[0], 0]]); round5 = np.eye(3) + np.sin(t5) * K + (1 - np.cos(t5)) * K @ K
    line("is", all(any(np.allclose(round5 @ c, d) for d in CORNERS) for c in CORNERS) and np.allclose(round5 @ CORNERS[a], CORNERS[a]) and np.allclose(round5 @ CORNERS[b], CORNERS[b]),
         "the line through two corners across from one another is the line of a round of five: the round lays the twelve onto the twelve, and the two as they were")
    caps = [t for t in sphere if a in t or b in t]; band = [t for t in sphere if a not in t and b not in t]
    bc, bs, bat, bnum = surface(band)
    rim = sorted(s for s, n in bs.items() if n == 1)
    rimA = [i for i in range(12) if beside(i, a)]; rimB = [i for i in range(12) if beside(i, b)]
    line("is", (len(caps), len(band)) == (10, 10) and (len(bc), len(bs)) == (10, 20) and bnum == 0 and len(rim) == 10 and len(rimA) == len(rimB) == 5
         and all((s[0] in rimA) == (s[1] in rimA) for s in rim),
         "the two corners and their ten triangles away, ten triangles are as they were: a band of ten corners and 20 sides, with two rims of five sides, a rim round an opening")

    print("\n3 · The ten triangles laid through the opening")
    def ring(r):
        out = [r[0]]
        while len(out) < 5: out.append(next(j for j in r if beside(j, out[-1]) and j not in out[-2:] and (len(out) < 2 or j != out[-2])))
        return out
    A = ring(rimA); B = ring(rimB)
    def laid(Bx):
        k0 = next(k for k in range(5) if beside(A[0], Bx[k]) and beside(A[0], Bx[(k + 1) % 5])); return Bx[k0:] + Bx[:k0]
    B = laid(B)
    if not (beside(A[1], B[1]) and beside(A[1], B[2])): B = laid(B[::-1])   # the other rim gone round the same way: A[i] is beside B[i] and B[i + 1]
    line("is", all(beside(A[i], B[i]) and beside(A[i], B[(i + 1) % 5]) and beside(A[(i + 1) % 5], B[(i + 1) % 5]) for i in range(5)),
         "on the band a corner of one rim is beside two corners of the other rim, at all five")
    tube = [t for i in range(5) for t in ((A[i], A[(i + 1) % 5], B[(i + 3) % 5]), (A[i], B[(i + 2) % 5], B[(i + 3) % 5]))]
    torus = band + [tuple(sorted(t)) for t in tube]
    tc, ts, tat, tnum = surface(torus)
    line("is", (len(tc), len(ts), len(torus)) == (10, 30, 20) and tnum == 0 and set(ts.values()) == {2} and one_piece(torus) and with_a_hand(torus) and len(set(torus)) == 20,
         "through the opening, ten triangles from rim to rim, a corner to two corners it was not beside: ten corners, 30 sides and 20 triangles, a side with two triangles: 10 less 30 and 20 is nought, a torus")
    line("is", set(tat.values()) == {6} and 10 * short(6) == 0 and 10 * 6 == 20 * 3 == 30 * 2 == 60,
         "six triangles to a corner, at all ten: six of 60 are a whole round, nought short: a torus at nought; and sixty three ways again")
    line("is", len(band) == 10 and len(tube) == 10 and all(sum(1 for t in band if i in t) == 3 and sum(1 for t in tube if i in t) == 3 for i in tc),
         "ten triangles are outward, of the sphere, and ten inward, through the opening; a corner is with three of the outward and three of the inward")

    print("\n4 · Beside the 57th and the 58th")
    line("found", True, "the 57th says a sphere 720 and a torus at nought, by eight triangles of three right angles and sixteen patches; here the same two numbers are twelve corners of five and ten corners of six")
    line("found", True, "the 30 sides and the 20 triangles are as many on the sphere and on the torus, and sixty is sixty: two corners are fewer, the two of the line of five")
    line("found", True, "the way through the opening is one of more than one: a corner to the two corners two and three on round the other rim. It is this session's own making, and no living file says it in these numbers")

    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
