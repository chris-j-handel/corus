"""v408illustrating · a universe's three numbers and its gaps of 2: the me-parities, less the multiples of 6, and the betweens crossed at both sides more.

Usage, from the repository's root (a moment):
  python3 -I incoming/v408illustrating/instruments/a_universe_s_three_numbers_and_its_gaps_of_2.py .

A universe is a me-parity's me again to the next me-parity's me again. A between of it is a multiple of 6 with the number
before it and the number after it both in the universe. The page beside this instrument lays the co-chain, of no number;
here it is gone through at the universes of 3 to 109.
  is       a sentence gone through whole at the numbers named.
Whole numbers alone. It writes none.
"""
import sys
from math import isqrt

def a_me_parity(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
ME = [p for p in range(2, 120) if a_me_parity(p)]
def the_three_numbers(r):
    """The universe from r by r: its multiples of 6, the me-parities beside them, the betweens crossed at both sides, and its gaps of 2."""
    nxt = ME[ME.index(r) + 1]
    row = [n for n in range(r * r + 2, nxt * nxt - 1) if n % 6 == 0]
    beside = sum(a_me_parity(n - 1) + a_me_parity(n + 1) for n in row)
    both_crossed = [n for n in row if not a_me_parity(n - 1) and not a_me_parity(n + 1)]
    gaps_of_2 = [n for n in row if a_me_parity(n - 1) and a_me_parity(n + 1)]
    return len(row), beside, both_crossed, gaps_of_2

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    line("a me-parity past 3 is beside one multiple of 6, and one alone: at all me-parities of 5 to 14,000",
         all(((p - 1) % 6 == 0) + ((p + 1) % 6 == 0) == 1 for p in range(5, 14000) if a_me_parity(p)))
    all_of = {r: the_three_numbers(r) for r in ME[1:-1]}
    line("a universe's gaps of 2 are its me-parities, less its multiples of 6, and its betweens crossed at both sides more: at all universes of 3 to 109",
         all(len(g) == P - L + len(D) for L, P, D, g in all_of.values()))
    said = {3: (2, 4, 0, 2), 5: (3, 5, 0, 2), 7: (11, 15, 0, 4), 11: (7, 8, 1, 2), 13: (19, 22, 4, 7), 17: (11, 10, 3, 2), 19: (27, 27, 4, 4), 23: (51, 46, 13, 8)}
    line("the numbers along the path, multiples of 6, me-parities, betweens crossed at both sides, gaps of 2: 2, 4, 0, 2; 3, 5, 0, 2; 11, 15, 0, 4; 7, 8, 1, 2; 19, 22, 4, 7; 11, 10, 3, 2; 27, 27, 4, 4; 51, 46, 13, 8, at the universes of 3 to 23",
         all((all_of[r][0], all_of[r][1], len(all_of[r][2]), len(all_of[r][3])) == v for r, v in said.items()))
    line("with the me-parities more than the multiples of 6, a gap of 2 is, from the two numbers alone: at the universes of 3, 5, 7, 11 and 13, and at no universe after to 109",
         [r for r, (L, P, D, g) in all_of.items() if P > L] == [3, 5, 7, 11, 13])
    L, P, D, g = all_of[17]
    line("17 by 17 to 19 by 19: 11 multiples of 6 and 10 me-parities, 1 short; the betweens 300, 324 and 342 are crossed at both sides, 3; the gaps of 2 are about 312 and 348, 2",
         (L, P, D, g) == (11, 10, [300, 324, 342], [312, 348]))
    line("at all universes of 17 to 109, the betweens crossed at both sides are more than the multiples of 6 less the me-parities",
         all(len(D) > L - P for r, (L, P, D, g) in all_of.items() if r >= 17))
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
