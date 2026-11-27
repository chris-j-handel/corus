"""v410illustrating · the check of the 59th drawing: one triangle, three mirrors; opening a sphere to a torus.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_one_triangle_three_mirrors_opening_a_sphere_to_a_torus.py .

The 59th is one drawing of both the 57th and the 58th, beside the two. Its check opens their two checks and executes
them whole, opens the instrument of the twelve corners as a sphere and as a torus, and executes what the 59th says
more: the two flat layings of triangles, the sixteen patches as a flat laying of four by four, and the three lines an
opening is said along.

Do no harm: it opens this folder's own instruments and, by them, the living files and v403mgr's one table, and writes
in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import importlib.util, itertools, os, sys
from collections import Counter
from pathlib import Path
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
def opened(name):
    spec = importlib.util.spec_from_file_location(name[:28].replace("-", "_"), os.path.join(HERE, name)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
c57 = opened("check_one_triangle_three_right_angles_bi-folding_1_to_17.py")
c58 = opened("check_one_triangle_three_golden_rectangles.py")
tw = opened("twelve_corners_closing_as_a_sphere_and_winding_through_one_opening_as_a_torus.py")
A, B, C = c57.A, c57.B, c57.C
PHI = c58.PHI
FIVE = c58.f.unit((0, 1, PHI))                                   # a rectangle's corner on the side from A to C: a line of a round of five

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))

    # the two drawings it gathers, their checks executed whole
    l57, own57, ent57 = c57.checks(root); l58, own58 = c58.checks(root)
    n57, n58 = Counter(k for k, _ in l57), Counter(k for k, _ in l58)
    line("is", not n57["is-not"] and n57["is"] == 17, f"the 57th's check, executed whole here: {n57['is']} are is, {n57['found']} found, {n57['placing']} a placing")
    line("is", not n58["is-not"] and n58["is"] == 18, f"the 58th's check, executed whole here: {n58['is']} are is, {n58['found']} found, {n58['placing']} a placing")

    # a sphere of twelve corners, and a torus of ten
    two = tw.the_two(); sphere, band, tube, torus, RA, RB, a, b = (two[k] for k in ("sphere", "band", "tube", "torus", "A", "B", "a", "b"))
    sc, ss, sat, snum = tw.surface(sphere); tc, ts, tat, tnum = tw.surface(torus)
    short = lambda k: 360 - 60 * k
    line("is", (len(sc), len(ss), len(sphere), snum) == (12, 30, 20, 2) and set(sat.values()) == {5} and 12 * short(5) == 720 == 8 * 90,
         "a sphere of twelve corners: 30 sides and 20 triangles, five triangles to a corner, 60 short of a whole round: 720, as eight triangles of 90 over are")
    line("is", (len(tc), len(ts), len(torus), tnum) == (10, 30, 20, 0) and set(tat.values()) == {6} and set(ts.values()) == {2} and tw.one_piece(torus) and tw.with_a_hand(torus) and 10 * short(6) == 0,
         "opened at two corners across from one another, their ten triangles through the opening: a torus of ten corners, 30 sides and 20 triangles, six triangles to a corner, a whole round: at nought")
    line("is", 12 * 5 == 10 * 6 == 20 * 3 == 30 * 2 == 60, "sixty is on both: 12 by 5 on the sphere, 10 by 6 on the torus, 20 by 3 and 30 by 2 on both")

    # the two flat layings of triangles
    S = lambda t: tuple(sorted(t))
    caps_a = [S((a, RA[i], RA[(i + 1) % 5])) for i in range(5)]; caps_b = [S((b, RB[i], RB[(i + 1) % 5])) for i in range(5)]
    band_laid = [S((RA[i], RB[i], RB[(i + 1) % 5])) for i in range(5)] + [S((RA[i], RA[(i + 1) % 5], RB[(i + 1) % 5])) for i in range(5)]
    line("is", set(caps_a + caps_b + band_laid) == {S(t) for t in sphere} and set(band_laid) == {S(t) for t in band},
         "the sphere's flat laying is three rows of triangles, 5, 10 and 5: the two fives are the two corners' ten, and the ten between are the band")
    # a torus's flat laying: a corner of the lower row is under the two corners of the middle row it is with through the opening, two on
    line("is", all(S(t) in {S(x) for x in torus} for t in tube) and all(S((RA[i], RB[(i + 2) % 5], RB[(i + 3) % 5])) in {S(x) for x in tube} for i in range(5))
         and not any(tw.beside(RA[i], RB[(i + 2) % 5]) or tw.beside(RA[i], RB[(i + 3) % 5]) for i in range(5))
         and all(sum(1 for t in band if i in t) == 3 and sum(1 for t in tube if i in t) == 3 for i in tc),
         "the torus's flat laying is two rows of ten triangles, the band and the ten through the opening: its lower row of corners is its upper row gone on by two")

    # the 57th's sixteen patches, a flat laying of four by four
    rows = [[n for n in range(1, 17) if c57.patch(n)[1] == j] for j in range(4)]
    line("is", rows == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] and 16 - 32 + 16 == 0 and 4 * 90 == 360,
         "the sixteen patches are four rows of four: outward, inward, inward, outward; 16 corners, 32 sides and 16 patches: nought; four patches of 90 at a corner, a whole round")
    line("is", all(c57.patch(c57.up8(n)) == (c57.patch(n)[0], c57.patch(n)[1] ^ 2) for n in range(1, 9))
         and all(c57.patch(c57.less17(n)) == (3 - c57.patch(n)[0], 3 - c57.patch(n)[1]) for n in range(1, 17)),
         "on the four by four, 8 up is a patch two rows on, and 17 less the patch across the middle of the sixteen")
    line("found", True, "two tori of patches are laid side by side: sixteen patches of four sides, four to a corner, and twenty triangles, six to a corner. Both are at nought. One laid onto the other is not executed")

    # three lines an opening is said along
    ang = lambda p, q: float(np.degrees(np.arccos(np.clip(abs(p @ q), -1, 1))))
    line("is", abs(ang(A, B) - 90) < 1e-9 and abs(ang(B, FIVE) - 90) < 1e-9 and abs(ang(A, FIVE) - 31.717) < 1e-3 and abs(FIVE[0]) < 1e-12 and abs(abs(B[0]) - 1) < 1e-12,
         "three lines: the me's line through A; the co-linear through B, at a right angle to it; and a line of five, 31.72 from the me's line, on the mirror the co-linear is at a right angle to")
    line("found", True, "an opening is said along three lines: the 3rd drawing's along the me's line, the 5th's along the co-linear, and this one's along a line of five. They are not one yet")
    line("placing", True, "the flat layings, their tints and the numbers 1 to 5 on a torus's two rows are the drawing's own placings")
    own = {"own57": own57, "ent57": ent57, "own58": own58, "two": two, "rows": rows}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
