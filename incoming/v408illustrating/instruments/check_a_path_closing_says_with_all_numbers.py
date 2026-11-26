"""v408illustrating · the check of the 55th drawing: a path closing, all its mes gone through, says with all numbers.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/check_a_path_closing_says_with_all_numbers.py .

A partner's sayings of 26 November, in this session's words: a simulation ends at a number, and in a universal set it
proves no is; it is for rapid breaking testing, it is not conclusive beyond its stated limits, and it verifies no is. The
all-or-none logic ends at its own bound.

Its lines are of three kinds, said apart.
  is       a path closing, gone through whole: all its mes, all or none. All numbers are at a me of it.
  is       a moving: one rule at all sides, bound by odd and even, all in pairs, or pairs and one over.
  tested   a breaking test, to its stated limit: none found. It is no is beyond its limit, and it is laid among no is.
The sentences are the 52nd, 53rd and 54th drawings', laid in them with stepped numbers under is: a finding against them.
A me again is a number by itself; a part of a number is a number crossing it; across, a number is odd or even by the
number of its prime parts multiplied, v408primes' 73. Whole numbers alone. It writes none.
"""
import sys
from math import isqrt

def parts_of(n):
    """A number's prime parts with their times, the least ahead."""
    out, d = [], 2
    while d * d <= n:
        k = 0
        while n % d == 0: n //= d; k += 1
        if k: out.append((d, k))
        d += 1
    return out + ([(n, 1)] if n > 1 else [])
def across(n): return sum(k for _, k in parts_of(n)) % 2             # 1, odd across; 0, even across
def all_parts(n):
    out = [1]
    for p, k in parts_of(n): out = [d * p ** e for d in out for e in range(k + 1)]
    return sorted(out)
def times(d, p):
    k = 0
    while d % p == 0: d //= p; k += 1
    return k
def the_pairing(n):
    """A number's parts paired by a prime of it: a part with the prime an even number of times, with the part a time more.
    At a prime an odd number of times in the number, all pair. At a prime an even number of times, the parts with it all
    its times are over, and they are paired by the next prime. It gives the pairs, and the parts over."""
    pairs, left = [], all_parts(n)
    for p, k in sorted(parts_of(n), key=lambda pk: pk[1] % 2 == 0):   # a prime an odd number of times goes ahead
        over = []
        for d in left:
            e = times(d, p)
            if e % 2 == 0 and e < k: pairs.append((d, d * p))
            elif e == k and k % 2 == 0: over.append(d)
        left = over
        if not left: break
    return pairs, left
def the_moving(n):
    """A me again of side n, cell by cell: its last row, less a cell, laid as a column more. It gives the cells after the moving, and the cell over."""
    cells = {(r, k) for r in range(n) for k in range(n)}
    one = (n - 1, n - 1); cells.discard(one)
    for k in range(n - 1): cells.discard((n - 1, k)); cells.add((k, n))
    return cells, one
living = lambda m: [a for a in range(m) if all(a % p for p in (2, 3, 5) if m % p == 0)]
aim = lambda a, m: next(e % m for e in (a - 1, a + 1) if e % 4 == 0)
seam = lambda a, m: next(e % m for e in (a - 1, a + 1) if e % 6 == 0)

if __name__ == "__main__":
    results, tests = [], []
    def line(name, ok): results.append((name, bool(ok)))
    def test(name, ok): tests.append((name, bool(ok)))
    # paths closing, gone through whole
    line("a path of 2 mes, whole: an odd me's prior and its next are both the me 0: even, odd, even, the 52nd's", [(a - 1) % 2 for a in (1,)] == [0] and [(a + 1) % 2 for a in (1,)] == [0])
    line("a path of 3 mes, whole: three numbers 2 apart are at all three mes, from all three mes: one of them is at the me 0, crossed by 3; past 3, 5 and 7, twins are two, the 53rd's",
         all(sorted((a + e) % 3 for e in (0, 2, 4)) == [0, 1, 2] for a in range(3)))
    again4 = sorted({(a * a) % 4 for a in range(4)}); two4 = sorted({(x + y) % 4 for x in again4 for y in again4})
    line("a path of 4 mes, whole: a me again is at the me 0 or the me 1, two me agains added are at 0, 1 or 2, and at the me 3 none: aiming next, a me-parity is two me agains added at none, the 52nd's, laid stepped in it",
         again4 == [0, 1] and two4 == [0, 1, 2] and all(((a - 1) % 4 == 0) != ((a + 1) % 4 == 0) for a in (1, 3)) and (3 + 1) % 4 == 0 and (1 - 1) % 4 == 0)
    line("a path of 6 mes, whole: uncrossed by 2 and by 3 are the me one on and the me one back alone, a +1 from the me 0: past 3, a me-parity lives in a seam of 6, the 52nd's", living(6) == [1, 5])
    line("a path of 12 mes, whole: uncrossed by 2 and by 3 are the mes 1, 5, 7 and 11; at 1 and 11 aim and seam are one even, the me 0, and at 5 and 7 its two evens; twins about the me 0 aim together, and about the me 6 apart, the 52nd's",
         living(12) == [1, 5, 7, 11] and [a for a in living(12) if aim(a, 12) == seam(a, 12)] == [1, 11] and aim(11, 12) == aim(1, 12) == 0 and (aim(5, 12), aim(7, 12)) == (4, 8))
    line("a path of 30 mes, whole: of its five seams of 6, the mes 0, 12 and 18 are with both their sides uncrossed by 5, and 6 and 24 are with a side at a seam of 5: twins past 5 are born at three seams of the five, the 53rd's",
         [s for s in range(0, 30, 6) if (s - 1) % 30 in living(30) and (s + 1) % 30 in living(30)] == [0, 12, 18] and living(30) == [1, 7, 11, 13, 17, 19, 23, 29])
    # movings: one rule at all sides, bound by odd and even
    line("a moving, a twin's rooms: the me one on and the me one back are 2 steps apart, and 2 steps come again at a path of 2 mes alone, 2 being short of all paths of more mes: of r mes past 2, a twin's between is uncrossed at r - 2, the 54th's",
         (1 - (-1)) == 2 and 1 % 2 == (-1) % 2)
    line("a moving, a me again: a row of n cells is n - 1 cells and 1 cell; the row, less a cell, laid as a column more, is its side less 1 by its side and 1, and one cell over: the rule is one at all sides, the 53rd's; drawn at 6",
         the_moving(6)[0] == {(r, k) for r in range(5) for k in range(7)} and the_moving(6)[1] == (5, 5))
    p35, o35 = the_pairing(35); p36, o36 = the_pairing(36)
    line("a moving, the pairing: a prime's times in a number's parts are 0 to k, paired two by two from 0, none over with k odd and one over with k even: odd and even bound it; 35's parts are two pairs, none over, and 36's four pairs and 36 over",
         sorted(p35) == [(1, 5), (7, 35)] and o35 == [] and sorted(p36) == [(1, 2), (3, 6), (4, 12), (9, 18)] and o36 == [36] and all(across(a) != across(b) for a, b in p35 + p36))
    line("a moving, one short of a me again: a me again and its next are apart by twice the side and 1, past the side 1 more than 1 apart: one short of a me again is past its prior me again and short of it, no me again",
         all((n + 1) * (n + 1) - n * n == 2 * n + 1 for n in (1, 2, 3)) and 2 * 1 + 1 > 1)
    # breaking tests, to their stated limits: none found; they are no is
    test("a twin's rooms, at the primes r of 3 to 31: r - 2 of r, no breaking found", all(sum(1 for m in range(r) if (m - 1) % r and (m + 1) % r) == r - 2 for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)))
    test("the moving of a me again, cell by cell, sides 2 to 200: no breaking found", all(the_moving(n)[0] == {(r, k) for r in range(n - 1) for k in range(n + 1)} for n in range(2, 201)))
    def whole(n):
        pairs, over = the_pairing(n); side = isqrt(n)
        return (all(across(a) != across(b) for a, b in pairs) and sorted([x for pr in pairs for x in pr] + over) == all_parts(n) and over == ([n] if side * side == n else []))
    test("the pairing, numbers 1 to 20,000: all a number's parts in pairs, an odd with an even across, none over at no me again and the number itself over at a me again, v408primes' 80: no breaking found", all(whole(n) for n in range(1, 20001)))
    test("one short of a me again, sides 2 to 20,000: no me again, and its parts' pairing is with none over at sides 2 to 300: no breaking found",
         all(isqrt(n * n - 1) ** 2 != n * n - 1 for n in range(2, 20001)) and all(the_pairing(n * n - 1)[1] == [] for n in range(2, 301)))
    print("said apart: not said by a path or a moving of this session's, and tested alone in the 52nd's and the 54th's checks: aiming prior, a me-parity is two me agains added; twins are more at a next span by 4; twins are born past all numbers\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    for name, ok in tests: print(("tested   " if ok else "broken   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is; {sum(ok for _, ok in tests)} of {len(tests)} breaking tests found none")
    sys.exit(0 if all(ok for _, ok in results + tests) else 1)
