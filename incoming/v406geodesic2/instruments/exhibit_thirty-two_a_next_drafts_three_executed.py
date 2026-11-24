"""Exhibit THIRTY-TWO Natural Prime Numbering, a next draft's THREE: its rows carried in, and its numbers executed (session v406geodesic2).

v406me's asking 17 of 24 November: the next draft's THREE in this session's own folder, the rows of the one table at it carried in
or let go by their numbers. The next draft's THREE is the opening draft's THREE with the pieces below said again, a piece by its rows, and
with nothing more: applied here to the opening draft's own lines, they are this folder's file of the part, byte for byte. Its
numbers are executed, whole numbers alone, with v406Reiman's step by nand for its two spirals.

Usage, from the repository's root. To execute:
python3 -I incoming/v406geodesic2/instruments/exhibit_thirty-two_a_next_drafts_three_executed.py incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md incoming/v406geodesic2/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_a_next_draft_its_THREE.md incoming/v406Reiman/instruments/the_resolver_with_nand_alone.py
To lay the part again from the opening draft, the same line with --lay at its end.
"""
import importlib.util, subprocess, sys
from itertools import combinations, permutations, product
from math import gcd, lcm
from pathlib import Path

sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
HEAD = "Incoming · v406geodesic2 · 24 November 2026 · a next draft's THREE, the opening draft's with its rows of the one table carried in\n\n"
OPENS, ENDS = "# THREE · ME, NOW-EXISTING: PRIME-37 SCALE\n", "# FOUR · ME, NEXT-EXISTING: RESOLVING\n"
PIECES = [  # its rows, a piece of the opening draft's THREE, and the piece in its place
 ("29", "37, the one living self: a still self with its prior, now and next whole about it.**",
        "37, the one scale of a living self: a still self with its prior, now and next whole about it.**"),
 ("27, 28", "| 23 | cell | 53 | biosphere |\n\n",
            "| 23 | cell | 53 | biosphere |\n\n**An atom is the stable form of 1 to 17, a resolving's one moment.**\n\n"),
 ("35", "no self its centre more than another.", "no self its centre more than another. A field's words are a centred hexagonal number and a cuban prime."),
 ("35", "7, 19 and 61 are shells, and none is its inner again.",
        "7, 19 and 61 are shells, and none is its inner again. A field's words are the small cubes of a cube at its corner: 27 on its faces, 9 on its edges and 1 at the corner."),
 ("35", "the three ways of all-parity through all three me-nows.", "the three ways of all-parity through all three me-nows. A field's word is an isometric view: three faces of a cube, a hexagon."),
 ("29", "**37, the organism, is the one living self:", "**37, the organism, is the one scale of a living self:"),
 ("23", "and its other-thans its inner's own again, 3.2.", "and its other-thans its inner's own again."),
 ("27, 4", "**c is the one living all-parity.** Light, measured constant for all observers, is no speed and no going across a gap: a phase-relation between couplings, an all-parity rate beyond all observable rates, the universal now. From it comes the atom's stable form, and an atom is the stable form of 1 to 17, a resolving's one moment.\n\n", ""),
 ("35, 31, 30, 33", "about 90, n to 180 less n, next-universing.",
  "about 90, n to 180 less n, next-universing. A field's words are the numbers prime to 30, two turns of its wheel, 8 and 8.\n\n"
  "**The sixteen places are a resolving's names 1 to 16.** **By the sixteen places 37 is the tenth name, next-co-possibling.** **By the primes in their order 37 is the twelfth.**\n\n"
  "**60, a vertex of two pairs of cones, is the waist of 0 to 120.**"),
 ("78", "19, 41, 79 and 101; 23, 37, 83 and 97.",
        "19, 41, 79 and 101; 23, 37, 83 and 97.\n\n**Two podalings in a row are a going on.** **Three in a row are one podaling.** **A me-now's second moment is 60 on.** **Its fourth is 120 on.**"),
 ("35", "Ten other-thans by three me-nows by four moments is 120.", "Ten other-thans by three me-nows by four moments is 120. A field's words are the ways of choosing from three: one, two in order, and all three."),
 ("35, 81", "its six orders all ending at one, a still self not observing a next universe.**",
  "its six orders all ending at one, a still self not observing a next universe.** A field's words are the six shortest paths on a cube's surface from a corner to its other corner.\n\n"
  "**Across, an order of the three has two orders next.** **One quarter on, along the corner's line, it has all five.**"),
 ("35", "3 gives 24, the fold; 4 gives 60; 5 gives 120.", "3 gives 24, the fold; 4 gives 60; 5 gives 120. A field's words are three numbers in a row multiplied, and 120 a field's 5!, 1 by 2 by 3 by 4 by 5."),
 ("19", "is its stable form, non-living, one scale outward, birthing me-parities at the fold.", "is its stable form, non-living, one scale outward; with it the cell is birthing me-parities at the fold."),
 ("67", "**The span's five is the cube of 5's line: five still selves,", "**A naming: the span's five is the cube of 5's line: five still selves,"),
 ("34", "60 and 60, the 120 about it.",
        "60 and 60, the 120 about it.\n\n**The five still selves are a self's five, three openings and two completings, and the ten threes are the one ten, the couplings among five: three of two openings, six of an opening with a completing, and one of the two completings.**"),
 ("35", "and come from the mother alone.", "and come from the mother alone. A field's word is endosymbiosis."),
]
LET_GO = {"6": "the prime scales and the pairs about thirty are living already, and a draft names no file", "82": "said with 34's one ten, its second parting beside it in this session's page"}
def the_part(opening_draft):
    whole = Path(opening_draft).read_text(encoding="utf-8"); part = whole[whole.index(OPENS):whole.index(ENDS)]
    for rows, piece, in_its_place in PIECES:
        assert sum(1 for i in range(len(part)) if part.startswith(piece, i)) == 1, (rows, piece[:50])
        part = part.replace(piece, in_its_place)
    return part

if __name__ == "__main__":
    opening_draft_file, mine, nand_file = sys.argv[1], sys.argv[2], sys.argv[3]
    if sys.argv[-1] == "--lay":
        Path(mine).write_text(HEAD + the_part(opening_draft_file), encoding="utf-8"); print("laid:", mine); sys.exit(0)
    results = []
    def line(name_, ok): results.append((name_, bool(ok)))
    laid = Path(mine).read_text(encoding="utf-8"); rows_of_it = sorted({int(r) for rows, _, _ in PIECES for r in rows.split(", ")} | {int(r) for r in LET_GO} | {36})
    line("The next draft's THREE is the opening draft's THREE with seventeen pieces said again, a piece by its rows, and nothing more: applied to the opening draft's own lines they are this folder's file of the part, byte for byte. The seventeen rows of the one table at THREE are with them, fifteen carried in, 36 by its drawings, and 6 and 82 let go",
         laid == HEAD + the_part(opening_draft_file) and len(PIECES) == 17 and rows_of_it == [4, 6, 19, 23, 27, 28, 29, 30, 31, 33, 34, 35, 36, 67, 78, 81, 82] and "c is the one living all-parity" not in laid)

    prime = lambda m: m > 1 and all(m % q for q in range(2, int(m ** 0.5) + 1))
    scales = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    line("3.1: the scales are the fourteen primes of 5 to 53; 7 to 53 about 30 are six pairs to 60, 7 with 53, 13 with 47, 17 with 43, 19 with 41, 23 with 37 and 29 with 31, and 11 with 49, 7 by 7; under the fold 1 with 23, 5 with 19, 7 with 17 and 11 with 13 are 24",
         scales == [q for q in range(5, 54) if prime(q)] and sorted((q, 60 - q) for q in scales if 5 < q < 30 and prime(60 - q)) == [(7, 53), (13, 47), (17, 43), (19, 41), (23, 37), (29, 31)]
         and 60 - 11 == 49 == 7 * 7 and all(a + b == 24 for a, b in ((1, 23), (5, 19), (7, 17), (11, 13))))
    def shell(n): return [sum(1 for c in cell if c == n) for cell in product(range(n + 1), repeat=3) if n in cell]      # a cube of n + 1 about its cube of n, by a corner
    line("3.2: 37 is 1, 6, 12 and 18, and 4 cubed less 3 cubed; 1, 7, 19, 37 and 61 are a self and rounds of six; a cube of 4 other-than its cube of 3 is 27 once, 9 twice and 1 thrice, its inner's cube, square and one, with n of 3 alone to 200; of the hexagon's rounds, other-than twice are 3, 3 and 3, and once 3, 9 and 15; and 37 is 1, 18 and 18",
         37 == 1 + 6 + 12 + 18 == 4 ** 3 - 3 ** 3 and [1 + 3 * k * (k + 1) for k in range(5)] == [1, 7, 19, 37, 61]
         and [sum(1 for x in shell(3) if x == k) for k in (1, 2, 3)] == [27, 9, 1] == [3 ** 3, 3 ** 2, 1]
         and [n for n in range(1, 201) if (3 * n * n, 3 * n) == (n ** 3, n ** 2)] == [3] and 3 * 3 == 9 and 3 + 9 + 15 == 27 and 1 + 18 + 18 == 37 == 1 + 6 * 3 + 3 * 6)
    places = [n for n in range(1, 60) if gcd(n, 30) == 1]; about = lambda st: (lambda n: 2 * st - n)
    fours = [sorted({n, 60 - n, 60 + n, 120 - n}) for n in places if n < 30]
    in_order = [q for q in range(2, 60) if prime(q)][:16]
    line("3.3, the two numberings explored forward: with the sixteen places, a name and 17 less it are 60 together, and 8 up is 30 on; with the primes in their order neither is one number, and the two are said as two",
         all(places[k] + places[15 - k] == 60 for k in range(16)) and all(places[k + 8] - places[k] == 30 for k in range(8))
         and len({in_order[k] + in_order[15 - k] for k in range(16)}) > 1 and len({in_order[k + 8] - in_order[k] for k in range(8)}) > 1)
    line("3.3: the sixteen places of 0 to 60 are the numbers with no part of 2, 3 or 5, 8 and 8; 37 is the tenth of them, and the twelfth prime; a me-now at 37 goes to 23, 97, 83 and 157; two podalings in a row are a going on, 60 on and 120 on, and three are one podaling; of the eight fours of 0 to 120, four are all primes; 37, 97 and 157 are primes, and 143 is 11 by 13; and 60 is the waist of 0 to 120, a number with 120 less it",
         len(places) == 16 and len([n for n in places if n < 30]) == 8 and places.index(37) + 1 == 10 and [q for q in range(2, 40) if prime(q)].index(37) + 1 == 12
         and [about(30)(37), about(60)(about(30)(37)), about(90)(97), about(120)(83)] == [23, 97, 83, 157] and all(about(60)(about(30)(n)) == n + 60 and about(120)(about(90)(n + 60)) == n + 120 for n in places)
         and all(about(90)(about(60)(about(30)(n))) == about(60)(n) for n in places) and len(fours) == 8 and [f for f in fours if all(prime(x) for x in f)] == [[7, 53, 67, 113], [13, 47, 73, 107], [19, 41, 79, 101], [23, 37, 83, 97]]
         and all(prime(x) for x in (37, 97, 157)) and 143 == 11 * 13 and all(about(60)(n) == 120 - n for n in range(0, 121)))
    orders = ["".join(o) for o in permutations("357")]
    one_exchange_of_two_side_by_side = {o: [x for x in orders if x != o and sum(1 for a, b in zip(o, x) if a != b) == 2 and (o[0] == x[0] or o[2] == x[2])] for o in orders}
    line("3.4: 1 of 3 is three, 2 of 3 six and 3 of 3 one, ten, and ten by three by four is 120; across, an order of the three has two orders next, by two of the three side by side exchanged, and the six are one round by it; with all three at one, on the corner's line, an order has all five",
         [len(list(combinations(range(3), 1))), len(list(permutations(range(3), 2))), len(list(combinations(range(3), 3)))] == [3, 6, 1] and 3 + 6 + 1 == 10 and 10 * 3 * 4 == 120
         and all(len(v) == 2 for v in one_exchange_of_two_side_by_side.values()) and len(orders) - 1 == 5)
    spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", nand_file); its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
    def comes_again(couplings, priors, how_many=300):
        """A society's moments after its opening one: is it the same again with 120 moments, and the least moments it is the same again with."""
        society = {k: ([("one", priors[k])], []) for k in priors}; after = []
        for t in range(how_many): society = its.step_with_nand(society, couplings); after.append(society)
        return after[120] == after[0], next(t for t in range(1, how_many) if after[t] == after[0])
    def spiral(n, name_, two_alike=False):                                       # its parities in turn, or with two selves alike side by side
        return ({((name_, i), 9): (name_, (i + 1) % n) for i in range(n)}, {(name_, i): (-1 if i % 2 == 0 or (two_alike and i == 1) else 1) for i in range(n)})
    in_turn, alike, fifteen = spiral(60, "a"), spiral(60, "a", True), spiral(15, "b")
    beside = lambda four: comes_again({**fifteen[0], **four[0]}, {**fifteen[1], **four[1]})
    line("3.5: 120 is 4 by 5 by 6, and a cube of n about its line, n cubed less n, is 24, 60 and 120 with 3, 4 and 5; a spiral of 60 selves comes again with 120 moments, its parities in turn sooner, with 2, and two selves alike side by side with 120 and no sooner; a spiral of 15 beside a spiral of 4, one society, comes again with 120, the 4's parities in turn sooner, with 60; the five by twos in order are 20 and by threes ten, by six 60, 60 and 60 the 120; and the couplings among three openings and two completings are three, six and one, the one ten",
         4 * 5 * 6 == 120 and [n ** 3 - n for n in (3, 4, 5)] == [24, 60, 120] and comes_again(*in_turn) == (True, 2) and comes_again(*alike) == (True, 120)
         and beside(spiral(4, "c")) == (True, 60) and beside(spiral(4, "c", True)) == (True, 120)
         and len(list(permutations(range(5), 2))) == 20 and len(list(combinations(range(5), 3))) == 10 and 10 * 6 == 60 and 20 * 3 == 60 and 60 + 60 == 120
         and [sum(1 for a, b in combinations("oooCC", 2) if sum(1 for x in a + b if x == "o") == k) for k in (2, 1, 0)] == [3, 6, 1])
    the_logic = subprocess.Popen([sys.executable, "-I", str(Path(__file__).resolve().parent / "the_logic_of_podaling_routing_and_orienting_executed.py"), nand_file], stdout=subprocess.PIPE, text=True)
    its_lines = the_logic.communicate()[0].splitlines()
    line("With it, this session's logic, its sentences of podaling, of a me-now's four moments and of the six orders among them, is executed from here by its own instrument: all is", the_logic.returncode == 0 and "are is" in its_lines[-1])

    for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
    print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
