"""v408illustrating · a partner's saying of 25 November, of 5 co-linear and 10 bi-planar, rigorized by the cube of 5 on its line.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/a_partner_s_saying_of_five_co-linear_and_ten_bi-planar_rigorized.py .

The saying, in this session's words: 5 is co-linear neutralling; 10 is a bi-planar floating surface; and the co-linear is
along, through the central nothing on the plane. This session has it as the five and the ten of the saying before it.
Its figure is in the set: v406geodesic2's 8th drawing, the cube of 5 with five selves on its line, and v407primes' ten
sixes about it, five's choosings of three. A cell's plane across the line is its three ways added.
Its is and its is-not are both executed. Whole numbers alone. It opens the living files, and writes none. All or none.
"""
import itertools, sys
from pathlib import Path

cells = list(itertools.product(range(5), repeat=3))               # the cube of 5
plane = sum                                                       # a cell's plane across the corner's line
turned = lambda c: frozenset(itertools.permutations(c))           # a cell turned by the six orders of its three ways
on_line = [c for c in cells if len(turned(c)) == 1]

if __name__ == "__main__":
    root = Path(sys.argv[1])
    text = lambda f: (root / f).read_text(encoding="utf-8")
    results = []
    def line(name, ok): results.append((name, bool(ok)))

    line("of the cube of 5's 125 cells, five are still by all six orders of the three ways, and the five are on one line, a step apart: 5 is co-linear",
         on_line == [(a, a, a) for a in range(5)] and len(cells) == 125)
    planes = sorted({plane(c) for c in cells})
    line("across the line are 13 planes, 0 to 12; the line's five are at 0, 3, 6, 9 and 12, a line's cell at a plane's centre",
         planes == list(range(13)) and [plane(c) for c in on_line] == [0, 3, 6, 9, 12])
    between = [p for p in planes if p % 3]
    line("between two of the line's five are two planes, at all four betweens: a between is bi-planar; on a between's plane the line is through at no cell, a central nothing",
         between == [1, 2, 4, 5, 7, 8, 10, 11] and all(not any(plane(c) == p for c in on_line) for p in between))
    sixes = sorted({turned(c) for c in cells if len(turned(c)) == 6}, key=lambda g: sorted(g))
    line("v407primes' ten, executed apart: the sixes about the line are ten, five's choosings of three, one for one with the ten pairs of five, a six with the pair it is with none of",
         len(sixes) == 10 and len({frozenset(range(5)) - set(next(iter(g))) for g in sixes}) == 10 and all(len(frozenset(range(5)) - set(next(iter(g)))) == 2 for g in sixes))
    far = lambda c: 3 * sum(v * v for v in c) - sum(c) ** 2         # a cell's distance from the line, squared, by three
    line("a six is on one plane across the line, a round about it, all six at one distance from the line",
         all(len({plane(c) for c in g}) == 1 and len({far(c) for c in g}) == 1 for g in sixes))
    floating = [g for g in sixes if plane(next(iter(g))) % 3]
    line("is: six of the ten are on a between's planes, about a central nothing, at the planes 4, 5, 5, 7, 7 and 8",
         sorted(plane(next(iter(g))) for g in floating) == [4, 5, 5, 7, 7, 8])
    line("is-not: four of the ten are about a cell of the line, at the planes 3, 6, 6 and 9; the ten are 6 and 4, and the line's two end cells are with no six",
         sorted(plane(next(iter(g))) for g in sixes if g not in floating) == [3, 6, 6, 9])
    ring = lambda c: max(c) - min(c)                              # a cell's round about the line
    turn_of_6 = [[c for c in cells if ring(c) == 1 and min(c) == d] for d in range(4)]
    line("v406geodesic2's turns of 6, the four nearest the line, are bi-planar: three cells on a between's one plane and three on its other, at all four",
         all(len(t) == 6 and sorted(sum(plane(c) == p for c in t) for p in {plane(c) for c in t}) == [3, 3] and {plane(c) % 3 for c in t} == {1, 2} for t in turn_of_6))
    line("is-not: its turns of 12, 18 and 24 are on three, four and five planes",
         [len({plane(c) for c in cells if ring(c) == r and min(c) == 0}) for r in (2, 3, 4)] == [3, 4, 5])
    beside = [("Natural_Intelligence_v402mgr.md", "Within a bi-folding parallel surfaces and co-linear openings through them are one form"),
              ("Exhibit_TWENTY_Natural_Naming_v402mgr.md", "Ten are fixing relations: a relation not floating neutralling can not remain existing through prior, now and next"),
              ("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "A drawing leaves its centre empty."),
              ("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "five sides and five diagonals, along and across"),
              ("Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v402mgr.md", "a middle fixing as an end, with 5-now-co-existing and 13-next-discovering")]
    line("five living sentences beside the saying are word for word in their files",
         all(s in text(f) for f, s in beside))

    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
