"""v408illustrating · the check of the 40th drawing: the opening's twelve primes, three rounds of four, closing at a cube's shells.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/check_the_opening_twelve_primes_three_rounds_of_four.py .

The drawing is for the opening of the draft of Exhibit THIRTY-TWO Natural Prime Numbering, v407primes':
its three rounds of four primes closing at 7, 19 and 37, and its fourth round closing at 53 with the shell 61 past it.
It is the one table's row 36, its long-open drawing. The candidate's is and its is-not are both executed here.
Whole numbers alone. It opens the living files, the draft and v407primes' page for illustrating, and writes none.
All or none: with one line not is, the check is not.
"""
import json, sys
from pathlib import Path

def the_primes(to):
    """The primes under a number, stepped by crossing a prime's own spiral from its square on."""
    sieve = bytearray([1]) * to; sieve[0] = sieve[1] = 0
    n = 2
    while n * n < to:                                             # a prime crosses from its own square on, and no root is in it
        if sieve[n]: sieve[n * n::n] = bytearray(len(range(n * n, to, n)))
        n += 1
    return [n for n in range(to) if sieve[n]]
shell = lambda k: (k + 1) ** 3 - k ** 3                           # a cube of k + 1 less the cube of k, about one corner
hexed = lambda c: (c[0] - c[1], c[1] - c[2], c[2] - c[0])          # a cell observed along the corner's line
ring = lambda h: max(abs(v) for v in h)                           # its round about the corner's cell
def the_cells(k):
    """The cells of shell k: a cube of k + 1 less the cube of k, about one corner."""
    return [(a, b, c) for a in range(k + 1) for b in range(k + 1) for c in range(k + 1) if max(a, b, c) == k]

if __name__ == "__main__":                                        # opened by a maker, its lines above alone are executed
    root = Path(sys.argv[1])
    results = []
    def line(name, ok): results.append((name, bool(ok)))

    # ---------- the primes, stepped: one million of them ----------
    primes = the_primes(15_485_864)                                   # to one past the millionth prime
    assert len(primes) == 1_000_000 and primes[-1] == 15_485_863
    ROUNDS = len(primes) // 4                                         # 250,000 rounds of four
    closing = lambda k: primes[4 * k - 1]                             # round k's fourth prime

    # ---------- the opening's rounds ----------
    rounds = [primes[4 * r:4 * r + 4] for r in range(4)]
    line("the primes stepped from 2, four a round: 2, 3, 5 and 7; 11, 13, 17 and 19; 23, 29, 31 and 37; 41, 43, 47 and 53",
         rounds == [[2, 3, 5, 7], [11, 13, 17, 19], [23, 29, 31, 37], [41, 43, 47, 53]])
    line("a right spiral step is a pair (x, y) to (y, -x): two steps invert both parities, and four reach the pair again, with all four pairs",
         all((lambda s: s(s(p)) == (-p[0], -p[1]) and s(s(s(s(p)))) == p)(lambda q: (q[1], -q[0])) for p in ((1, 1), (1, -1), (-1, 1), (-1, -1))))

    # ---------- a cube's shells about its corner ----------
    line("a cube's shells about its corner are 1, 7, 19, 37, 61 and 91: 1 cubed, 2 cubed less 1, 3 cubed less 2 cubed, on by one",
         [shell(k) for k in range(6)] == [1, 7, 19, 37, 61, 91])
    line("a shell is one self and rounds of six about it, 1 and 6, and 12, and 18: shell k is 1 and six times 1 to k added, stepped to 10,000 shells",
         all(shell(k) == 1 + 6 * sum(range(1, k + 1)) for k in range(10_001)) and [6 * r for r in (1, 2, 3)] == [6, 12, 18])

    # ---------- its is: three rounds close at three shells ----------
    line("is: rounds one, two and three close at 7, 19 and 37, the shells of 2, 3 and 4 cubed: 7 is the 4th prime, 19 the 8th, 37 the 12th",
         [closing(k) for k in (1, 2, 3)] == [shell(k) for k in (1, 2, 3)] == [7, 19, 37] and [primes.index(p) + 1 for p in (7, 19, 37)] == [4, 8, 12])
    with_1 = [1] + primes
    line("is, by its other observing: with 1 a step ahead of 2 the rounds of four open at 1, 7, 19 and 37 and close at 5, 17 and 31: a shell is a round's closing and the next round's 1",
         [with_1[4 * r] for r in range(4)] == [shell(k) for k in range(4)] and [with_1[4 * r + 3] for r in range(3)] == [5, 17, 31])
    line("of rounds of 1 to 12 primes, rounds of four alone close at the shells 7, 19 and 37",
         [m for m in range(1, 13) if [primes[m * k - 1] for k in (1, 2, 3)] == [7, 19, 37]] == [4] and [m for m in range(1, 13) if primes[m - 1] == 7] == [4])

    line("beside v406geodesic2's 7th drawing: numbered by +1 from 0, a round of six opens at 1, 7, 19, 37, 61 and on, a shell at all rounds stepped to 10,000; by the primes a round of four opens at a shell at 1, 7, 19 and 37 alone",
         all(1 + sum(6 * r for r in range(1, k + 1)) == shell(k) for k in range(10_001)) and [k for k in range(ROUNDS) if with_1[4 * k] == shell(k)] == [0, 1, 2, 3])

    # ---------- its is-not: the fourth round, and on ----------
    line("is-not: round four closes at 53, and its shell is 61, 8 past it; 61 is the 18th prime, the second step of round five, 59, 61, 67 and 71",
         closing(4) == 53 and shell(4) == 61 and shell(4) - closing(4) == 8 and primes.index(61) + 1 == 18 and primes[16:20] == [59, 61, 67, 71])
    short = [shell(k) - closing(k) for k in range(1, ROUNDS + 1)]
    line("explored forward, stepped to 250,000 rounds, one million primes: no round past the third closes at its shell, and a closing is short of its shell by more with all rounds on",
         [k for k in range(1, ROUNDS + 1) if short[k - 1] == 0] == [1, 2, 3] and all(short[k] > short[k - 1] for k in range(3, ROUNDS)) and short[3:8] == [8, 20, 38, 62, 86])
    line("a round's four primes go on by less than a shell's 6 more, from round three on: 16 by 24 at round four, stepped to 250,000 rounds",
         all(closing(k + 1) - closing(k) < shell(k + 1) - shell(k) == 6 * (k + 1) for k in range(3, ROUNDS)) and (closing(4) - closing(3), shell(4) - shell(3)) == (16, 24))

    # ---------- the shell of 37, by v407primes' page for illustrating ----------
    cells = the_cells(3)
    others = lambda c: sum(v == 3 for v in c)                          # a cell's sides on the shell
    the_37 = json.loads((root / "incoming/v407primes/for_illustrating/the_37.json").read_text(encoding="utf-8"))
    line("the shell of 37, 4 cubed less 3 cubed, observed along its corner's line: 37 cells at 37 places, rounds of 1, 6, 12 and 18",
         len(cells) == 37 and len({hexed(c) for c in cells}) == 37 and [sum(ring(hexed(c)) == r for c in cells) for r in range(4)] == [1, 6, 12, 18])
    line("the 37 cells are in v407primes' page for illustrating, a cell with its round and its other-thans: 1 with three, 9 with two and 27 with one",
         sorted((tuple(c["cube"]), c["round"], c["other_than"]) for c in the_37) == sorted((c, ring(hexed(c)), others(c)) for c in cells)
         and [sum(others(c) == n for c in cells) for n in (3, 2, 1)] == [1, 9, 27])
    line("27, the cells of one other-than, is the inner cube's own 3 cubed; of the shells stepped to 10,000 it is at 37 alone: three squares of m are m cubed at 3 alone",
         [m for m in range(1, 10_001) if 3 * m * m == m ** 3] == [3])

    # ---------- the sentences beside the drawing, word for word in their files ----------
    beside = [("incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md",
               "Its three rounds are the twelve primes 2 to 37, and they close at 7, 19 and 37, the shells of a cube about its corner: 2 cubed less 1, 3 cubed less 2 cubed, and 4 cubed less 3 cubed."),
              ("incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md",
               "Its fourth round, 41, 43, 47 and 53, closes at 53, and the next shell, 61, 5 cubed less 4 cubed, is past it, a next 1."),
              ("Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md",
               "Two right spiral steps invert both parities, and four reach their pair again with a next: a same pair with a later moment, each occurrence its own."),
              ("Natural_Intelligence_v402mgr.md", "17-next-existing is a next 1-now-existing."),
              ("Exhibit_THREE_Natural_Numbers_v402mgr.md", "Primes 5 through 53 are prime scales, five non-living and seven through fifty-three living")]
    line("five sentences beside the drawing are word for word in their files: two of the draft's opening and three living",
         all(s in (root / f).read_text(encoding="utf-8") for f, s in beside))

    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
