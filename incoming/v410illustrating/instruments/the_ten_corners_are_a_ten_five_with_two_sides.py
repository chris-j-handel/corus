"""v410illustrating · the ten corners are a ten: five with two sides, one ten with all tens.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_ten_corners_are_a_ten_five_with_two_sides.py .

A partner's saying of 27 November, as this session is with it: in resolving a ten is the same as all other tens, a
same-named universal set of all tens; it is in Natural Numbers, in Exhibit ONE, and between the hard problems and
natural living as ten misunderstandings of living competency and ten kinds of ghosts. This session had said that no
name is laid on the ten corners of the 59th drawing's torus. This instrument executes the ten corners as a ten, and
opens the living files' tens beside them, a ten a line.

Do no harm: it opens seven living files and this folder's instrument of the twelve corners, and writes in no file.
A line is an is, executed here; or found, a thing found and laid whole.
"""
import importlib.util, itertools, os, re, sys
from collections import Counter
from pathlib import Path
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("tw", os.path.join(HERE, "twelve_corners_closing_as_a_sphere_and_winding_through_one_opening_as_a_torus.py"))
tw = importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
PHI = tw.PHI

def lines_of_five():
    """the ten corners as five lines through the middle: a corner of one rim, and the corner across the sphere from it on the other rim"""
    two = tw.the_two(); A, B, C = two["A"], two["B"], tw.CORNERS
    across = {i: next(j for j in range(12) if np.allclose(C[j], -C[i])) for i in range(12)}
    return two, across, [(A[i], across[A[i]]) for i in range(5)]

if __name__ == "__main__":
    ROOT = Path(sys.argv[1]).resolve()
    said = Counter()
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")
    lf = lambda pat: sorted(ROOT.glob(pat))[0].read_text(encoding="utf-8")
    numbers, naming, thirty, illus = lf("Exhibit_THREE_Natural_Numbers_*.md"), lf("Exhibit_TWENTY_Natural_Naming_*.md"), lf("Exhibit_THIRTY_Co-Chaining_*.md"), lf("Exhibit_TWENTY-NINE_Natural_Illustrating_*.md")
    equil, ghost, hard = lf("Exhibit_TWENTY-EIGHT_Equilibria_Registry_*.md"), lf("Exhibit_TWENTY-SEVEN_Living_Ghost_Registry_*.md"), lf("Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_*.md")
    sent = {int(n): t for n, t in re.findall(r"^(\d+)\. (.+)$", thirty, flags=re.M)}

    print("1 · One ten, as Natural Numbers says it")
    line("is", "each observing of a number is that one number" in numbers and "a ten of five with two directions and a ten of couplings among five are one ten" in numbers,
         "Natural Numbers says a number its own, an observing of a number that one number: a ten of five with two sides and a ten of couplings among five are one ten")
    line("is", 2 * 5 == 5 * 4 // 2 == 10 and [n for n in range(2, 200) if 2 * n == n * (n - 1) // 2] == [5],
         "five with two sides is ten, and the couplings among five are ten: the two are one number at five alone, of the numbers to 200")

    print("\n2 · The ten corners, five with two sides")
    two, across, five = lines_of_five(); A, B, C = two["A"], two["B"], tw.CORNERS
    line("is", len(A) == len(B) == 5 and all(q in B for _, q in five) and len({q for _, q in five}) == 5,
         "the ten corners are two rims of five; a corner of one rim is across the sphere from a corner of the other: five lines through the middle, two ends a line")
    tube = {tuple(sorted(p)) for t in two["tube"] for p in itertools.combinations(t, 2)}
    line("is", not any(tw.beside(p, q) for p, q in five) and all(tuple(sorted(x)) in tube for x in five) and all((B.index(q) - A.index(p)) % 5 == 3 for p, q in five),
         "a line's two ends are not beside one another on the sphere; through the opening they are, at all five: as the 57th says 8 up through the tube")
    line("is", across[two["a"]] == two["b"] and 6 * 2 == 12 and 5 * 2 == 10,
         "the twelve corners are six lines of five: five are the ten corners' lines, and the sixth is the line of the opening")

    print("\n3 · The couplings among the five lines")
    def rectangle(i, j):
        p, q = C[A[i]], C[A[j]]; return float(np.linalg.norm(p - q)), float(np.linalg.norm(p + q)), abs(float(np.linalg.det(np.array([p, q, np.cross(p, q)])))) > 1e-9
    pairs = list(itertools.combinations(range(5), 2)); recs = [rectangle(i, j) for i, j in pairs]
    line("is", len(pairs) == 10 and all(sorted((round(d1, 9), round(d2, 9))) == [2.0, round(2 * PHI, 9)] for d1, d2, _ in recs),
         "two lines of the five are a golden rectangle's four corners, 2 across and 2φ along: the couplings among five are ten rectangles")
    sides = [(i, j) for (i, j), (d1, _, _) in zip(pairs, recs) if abs(d1 - 2) < 1e-9]; diags = [(i, j) for (i, j), (d1, _, _) in zip(pairs, recs) if abs(d1 - 2 * PHI) < 1e-9]
    ring = lambda ps: sorted(Counter(x for p in ps for x in p).values()) == [2] * 5
    line("is", len(sides) == 5 and len(diags) == 5 and ring(sides) and ring(diags) and all((j - i) % 5 in (1, 4) for i, j in sides) and all((j - i) % 5 in (2, 3) for i, j in diags),
         "the ten part as two rounds of five: at five a rectangle's across is a rim's side, and at five its along is across a rim: five sides and five across, as Natural Numbers says a ten's two sides")
    line("is", 10 + 5 == 15, "the 58th's fifteen mirrors are fifteen rectangles: these ten among the five lines, and five with the line of the opening")

    print("\n4 · The living files' tens, a ten a line")
    line("is", "Ten is with a self as five with two directions, 2n, and with a same-existing-society as couplings among five" in numbers and "five sides and five diagonals" in numbers,
         "Natural Numbers: a ten with a me as five with two sides, and with a society as the couplings among five, five sides and five across")
    line("is", "ten names of a self's own resolving are seventeen" in numbers and "five before 10, co-sequencing, 3, 4, 5, 7 and 8" in sent.get(330, "")
         and [n + 8 for n in (3, 4, 5, 7, 8)] == [11, 12, 13, 15, 16] and "11, 12, 13, 15 and 16" in sent.get(330, ""),
         "Exhibit ONE's names, by Natural Numbers and Exhibit THIRTY's 330: ten names of a me's own resolving, five before 10 and five after, a name of the second five 8 up from its own")
    line("is", "THE TEN, FIVE PLACES AT TWO FACES" in equil and "2 and 10, 3 and 11, 4 and 12, 5 and 13, 6 and 14" in illus,
         "the Equilibria Registry: the ten at five places with two faces, the names 2 to 6 and their names 8 up, as Natural Illustrating says them")
    line("is", "Each of ten is with its name, now, and its name 8 up, next" in naming and "## 4.9 Ten unchangeables, one name each" in naming,
         "Natural Naming: ten fixings, a name a fixing; a fixing is with its name now and its name 8 up next")
    line("is", "Five switches, two directions with each, and ten positions" in ghost,
         "the Living Ghost Registry: ten positions of a ghost, five with two sides")
    line("is", "they pair into five co-changing pairs" in hard and "one ten with two sides" in hard,
         "the Resolving the Hard Problem Registry: ten one-way changings in five pairs, one ten with two sides")
    line("found", True, "all six living tens are five with two sides, and at four of them the two sides are a name now and its name 8 up: as the ten corners are five lines with two ends, an end beside its other through the opening")

    print("\n5 · Found beside it")
    eq, th = {2, 3, 4, 5, 6}, {3, 4, 5, 7, 8}
    line("found", "seatings part with files" in illus and sorted(eq & th) == [3, 4, 5],
         "the five names part with the files, as Natural Illustrating says it of the seatings: 2 to 6 at the Equilibria Registry; 3, 4, 5, 7 and 8 at Exhibit THIRTY's 330; 3, 4 and 5 are at both")
    line("found", "They must not merge with ten positions" in ghost and "ten positions, ten unchangeables, and eight sides remain each its own" in ghost,
         "the Living Ghost Registry says its two tens not merged, a ten its own; Natural Numbers says all tens one ten; a partner says a ten the same-named set of all tens. The two sayings are laid side by side")
    line("found", True, "which five names are at the five lines is not executed: a line is with a name now at one end and its name 8 up at its other, by four living files, and the files part on the five")

    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
