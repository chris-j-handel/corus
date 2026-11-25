"""v408illustrating · the check of the 41st drawing: 37, one self, its rounds and its other-thans, two partings of one shell.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/check_37_one_self_its_rounds_and_its_other-thans.py .

The drawing is for 3.2 of the draft of Exhibit THIRTY-TWO Natural Prime Numbering, v407primes', and its next draft's THREE,
v406geodesic2's: 37 as one self and three rounds of six, and as a cube of 4 other-than its inner cube of 3, once, twice, thrice.
With it, executed apart: v407nanding's sentence of the shell as a nand of three, and v407primes' sentence 74 of the wrapping.
The candidate's is and its is-not are both executed here. Whole numbers alone. It opens the draft and two sessions' pages,
and writes none. All or none: with one line not is, the check is not.
"""
import importlib.util, itertools, os, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("the_opening", os.path.join(HERE, "check_the_opening_twelve_primes_three_rounds_of_four.py"))
o = importlib.util.module_from_spec(spec); spec.loader.exec_module(o)   # the 40th drawing's own lines: a shell, its cells, a cell observed along the corner's line

nand = lambda a, b: 1 - (a & b)                                   # the one logic
def nand_of_three(a, b, c):
    """Three by nand alone, two at a time: a and b, by a nand of a nand with itself; then a nand with c."""
    ab = nand(a, b)
    return nand(nand(ab, ab), c)
others = lambda c, k=3: sum(v == k for v in c)                     # a cell's sides on the shell: its other-thans of the inner cube
def by_others(k):
    cells = o.the_cells(k)
    return [sum(others(c, k) == n for c in cells) for n in (3, 2, 1)]
def the_orders(c):
    """A cell turned by up, forward and right: the six orders of its three ways."""
    return frozenset(itertools.permutations(c))
ABOUT = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))       # the six about a place
def home(q, r, places, k):
    """A place brought to its own place of shell k, by the shell's two steps (2k + 1, -k) and (k, k + 1): whole steps alone."""
    n = o.shell(k)
    return [p for p in places if ((k + 1) * (q - p[0]) - k * (r - p[1])) % n == 0 and (k * (q - p[0]) + (2 * k + 1) * (r - p[1])) % n == 0]
def wraps(k):
    """All places about a shell are of its cells one for one, and all its cells are with six others about them."""
    places = sorted(o.hexed(c)[:2] for c in o.the_cells(k)); w = 4 * k
    return (all(len(home(q, r, places, k)) == 1 for q in range(-w, w + 1) for r in range(-w, w + 1))
            and all(len({home(q + a, r + b, places, k)[0] for a, b in ABOUT} - {(q, r)}) == 6 for q, r in places))
if __name__ == "__main__":
    root = Path(sys.argv[1])
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    cells = o.the_cells(3)
    place = {c: o.hexed(c)[:2] for c in cells}
    rounds = {c: o.ring(o.hexed(c)) for c in cells}

    # ---------- one 37, by its rounds ----------
    line("37 is one self and three rounds of six, 1, 6, 12 and 18, and 4 cubed less 3 cubed: 37 cells at 37 places, observed along the corner's line",
         len(cells) == 37 == 4 ** 3 - 3 ** 3 and len(set(place.values())) == 37 and [sum(r == n for r in rounds.values()) for n in range(4)] == [1, 6, 12, 18])

    # ---------- a cell of the shell, by a nand of three ----------
    all_64 = list(itertools.product(range(4), repeat=3))
    inward = lambda v: int(v < 3)                                  # a way's place is of the inner cube of 3
    line("v407nanding's, executed apart: a cell of the cube of 4 is of the shell by a nand of three, its three ways' inward; of 64 cells 27 are inner and 37 of the shell",
         [c for c in all_64 if nand_of_three(*map(inward, c))] == sorted(cells) and sum(1 - nand_of_three(*map(inward, c)) for c in all_64) == 27
         and all(nand_of_three(a, b, c) == (0 if a and b and c else 1) for a in (0, 1) for b in (0, 1) for c in (0, 1)))

    # ---------- the same 37, by its other-thans ----------
    line("its cells are other-than the inner cube thrice, twice or once: 1 at the corner, 9 on three edges of 3, 27 on three sides of 9",
         by_others(3) == [1, 9, 27] and [c for c in cells if others(c) == 3] == [(3, 3, 3)])
    line("its sides shown are 48 squares, 16 a side: once 27, twice 9 two apiece, thrice 1 three",
         sum(others(c) for c in cells) == 48 == 3 * 16 == 27 + 2 * 9 + 3 * 1)
    line("is: 37's other-thans are its inner cube's own again: once 27 is 3 cubed, twice 9 is 3 by 3, thrice 1 is the one self",
         by_others(3) == [1, 3 * 3, 3 ** 3])
    line("is-not: 7, 19, 61 and 91: once 3, 12, 48 and 75 by inner cubes 1, 8, 64 and 125; twice 3, 6, 12 and 15 by 1, 4, 16 and 25; none is its inner again",
         [by_others(k) for k in (1, 2, 4, 5)] == [[1, 3, 3], [1, 6, 12], [1, 12, 48], [1, 15, 75]] and all(by_others(k) != [1, k * k, k ** 3] for k in (1, 2, 4, 5)))
    line("of the shells stepped to 10,000 it is at 37 alone: three squares of n are n cubed, and three of n are n by n, at 3 alone",
         [n for n in range(1, 10_001) if 3 * n * n == n ** 3] == [3] == [n for n in range(1, 10_001) if 3 * n == n * n])

    # ---------- the two partings, one 37 ----------
    line("a round by its other-thans: round one 3 twice and 3 once, round two 3 and 9, round three 3 and 15; twice 9 and once 27 in all",
         [[sum(rounds[c] == r and others(c) == n for c in cells) for n in (2, 1)] for r in (1, 2, 3)] == [[3, 3], [3, 9], [3, 15]])
    line("the cells other-than twice are on three lines from the corner's cell, a line a way, one cell a round: turns of 120 degrees",
         sorted(place[c] for c in cells if others(c) == 2) == sorted((a * n, b * n) for n in (1, 2, 3) for a, b in ((0, 1), (1, -1), (-1, 0))))

    # ---------- turned by up, forward and right ----------
    orders = {the_orders(c) for c in cells}
    line("turned by up, forward and right, the six orders of its three ways: one still self at its corner, six threes and three sixes, 1, 18 and 18",
         sorted(len(g) for g in orders) == [1] + [3] * 6 + [6] * 3 and all(set(g) <= set(cells) for g in orders))

    # ---------- the wrapping, v407primes' sentence 74, executed apart ----------
    line("the hexagon of 37 wraps with no seam: by its two steps, (7, -3) and (3, 4), all places are of the 37 one for one, and all 37 are with six others about them",
         wraps(3))
    line("is-not, explored: the wrapping is of the shells 7, 19, 61 and 91 too, by their own two steps; it parts 37 from no shell stepped, and 37's parting is its other-thans",
         all(wraps(k) for k in (1, 2, 4, 5)))

    # ---------- the sentences beside the drawing, word for word in their files ----------
    D = "incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md"
    beside = [(D, "37 is a self and three rounds of six, 1, 6, 12 and 18, and 4 cubed less 3 cubed."),
              (D, "37 is the one shell whose other-thans are its inner cube's own again: once the inner cube, 3 cubed; twice its square, 3 by 3; thrice the one self."),
              (D, "Turned by up, forward and right, the shell of 37 is one still self at its corner, six threes and three sixes: 1, 18 and 18."),
              ("incoming/v407nanding/Other-than_all-others_and_other-than_other-thans_as_nand_podalings_of_the_fifteen_lines.md", "The shell of 37 is a nand of three."),
              ("incoming/v407primes/The_prime_numbers_named_and_explained_sentence_by_sentence.md", "The hexagon of 37 wraps into a torus with no seam: all 37 selves have six others about them, and no self is its centre more than another.")]
    line("five sentences beside the drawing are word for word in their files: three of the draft's 3.2, v407nanding's and v407primes'",
         all(s in (root / f).read_text(encoding="utf-8") for f, s in beside))

    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
