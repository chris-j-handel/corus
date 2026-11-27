"""v408illustrating · suggestions to v408primes, executed ahead of a word: a path or a moving for a row of its table.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/suggestions_to_v408primes_a_path_or_a_moving_for_a_row.py .

A partner's saying of 26 November, in this session's words: the illustrating pauses but for teaching; this session offers
help with the prime resolving going on toward all, by suggestions to v408primes, and brings to a partner what seems not resolvable.
A suggestion is a path closing gone through whole, or a moving, same-existing at all sides, for a row now by a test. The rows
are v408primes' table's, at its branch's 2c7e375. Its lines are of the 55th's kinds:
  is       a path closing, gone through whole; or a moving, same-existing at all sides, its own reasons gone through.
  tested   a breaking test, to its stated limit: none found. It is laid among no is.
A me again is a number by itself; a part of a number is a number crossing it. Whole numbers alone. It writes none.
"""
import sys
from math import gcd, isqrt

def least_part(n):
    d = 2
    while d * d <= n:
        if n % d == 0: return d
        d += 1
    return n
def parts(n):
    out = []
    while n > 1: p = least_part(n); out.append(p); n //= p
    return out
def me_parities(limit):
    sieve = bytearray([1]) * (limit + 1); sieve[0] = sieve[1] = 0
    for n in range(2, isqrt(limit) + 1):
        if sieve[n]: sieve[n * n::n] = bytearray(len(range(n * n, limit + 1, n)))
    return [n for n in range(limit + 1) if sieve[n]]
# row 23 · the windmill: for a me-parity p one past a seam of 4, the threes (x, y, z), all past 0, with x by x and 4 by y by z added being p
def threes(p):
    out = []
    for x in range(1, isqrt(p) + 1):
        if (p - x * x) > 0 and (p - x * x) % 4 == 0:
            m = (p - x * x) // 4                                      # y by z
            out += [(x, y, m // y) for y in range(1, m + 1) if m % y == 0] if m < 400 else [t for y in range(1, isqrt(m) + 1) if m % y == 0 for t in {(x, y, m // y), (x, m // y, y)}]
    return out
def the_windmill(t):
    """One moving, in three cases by x beside y less z and beside twice y. It is its own way back."""
    x, y, z = t
    if x < y - z: return (x + 2 * z, z, y - x - z)
    if x < 2 * y: return (2 * y - x, y, x - y + z)
    return (x - 2 * y, x - y + z, y)
def the_turn(t): return (t[0], t[2], t[1])                           # y and z, one for the other
def kept(t): return t[0] * t[0] + 4 * t[1] * t[2]
# row 53 · me-parities at the me 1 round a me-parity's loop, with no last
def the_row_of(s, p): return sum(s ** k for k in range(p))          # 1, s, s by s, and on, p of them, added

if __name__ == "__main__":
    results, tests = [], []
    def line(name, ok): results.append((name, bool(ok)))
    def test(name, ok): tests.append((name, bool(ok)))
    grid = [(x, y, z) for x in range(1, 8) for y in range(1, 8) for z in range(1, 8)]
    line("row 23, the windmill, its own reasons: at all three cases x by x and 4 by y by z added is as it was, gone through at 343 threes; x beside y less z and beside twice y are one number at no me-parity, the one a me again, y and z added by itself, and the other 4 by y by y and z added",
         all(kept(the_windmill(t)) == kept(t) for t in grid) and all((y - z) ** 2 + 4 * y * z == (y + z) ** 2 and (2 * y) ** 2 + 4 * y * z == 4 * y * (y + z) for _, y, z in grid))
    line("row 23, its one over: the windmill lets a three be as it was in its middle case alone, x being y, and p is then x by x and 4 by z added, crossed by x: x is 1, the three 1, 1 and a number, and p one past a seam of 4",
         all((x == y) == (the_windmill((x, y, z)) == (x, y, z)) for x, y, z in grid if y - z < x < 2 * y) and all(the_windmill(t) != t for t in grid if not (t[1] - t[2] < t[0] < 2 * t[1])) and all(kept((x, x, z)) == x * (x + 4 * z) for x, _, z in grid))
    line("row 23, drawn at 13 and 17: 13's threes are three, 1 by 1 by 3 over and two paired; turned, 3, 1 and 1 is over: 13 is 9 and 4. 17's are five, and 1, 2 and 2 is over at the turn: 17 is 1 and 16",
         sorted(threes(13)) == [(1, 1, 3), (1, 3, 1), (3, 1, 1)] and [t for t in threes(13) if the_windmill(t) == t] == [(1, 1, 3)] and [t for t in threes(13) if the_turn(t) == t] == [(3, 1, 1)]
         and len(threes(17)) == 5 and [t for t in threes(17) if the_turn(t) == t] == [(1, 2, 2)] and 13 == 9 + 4 and 17 == 1 + 16)
    ps = [p for p in me_parities(20000) if p % 4 == 1]
    def whole(p):
        s = threes(p); st = set(s)
        return (all(the_windmill(t) in st and the_windmill(the_windmill(t)) == t for t in s) and [t for t in s if the_windmill(t) == t] == [(1, 1, (p - 1) // 4)]
                and len(s) % 2 == 1 and len([t for t in s if the_turn(t) == t]) == 1)
    test(f"row 23, the windmill at all {len(ps):,} me-parities one past a seam of 4, to 20,000: its threes are paired with one over, odd in number, and at the turn one is over, y being z: two me agains added. No breaking found", all(whole(p) for p in ps))
    line("row 25, a path of 4 mes, whole: the me 1 by the me 1 is the me 1, and the me 3 by the me 3 is the me 1: a number at the me 3, one short of a seam of 4, is with a me-parity part at the me 3. A seam's 4 times, less 1, is such a number, crossed by no me-parity of the seam: me-parities one short of a seam of 4, with no last",
         (1 * 1) % 4 == 1 and (3 * 3) % 4 == 1 and (1 * 3) % 4 == 3 and all(any(q % 4 == 3 for q in parts(4 * s - 1)) and gcd(4 * s - 1, s) == 1 for s in (3, 21, 231, 4389)))
    line("row 25, a path of 6 mes, whole: of its living mes 1 and 5, 1 by 1 and 5 by 5 are the me 1: a number at the me 5 is with a me-parity part at the me 5. A seam's 6 times, less 1, is such a number: me-parities one short of a seam of 6, with no last",
         (1 * 1) % 6 == 1 and (5 * 5) % 6 == 1 and (1 * 5) % 6 == 5 and all(any(q % 6 == 5 for q in parts(6 * s - 1)) and gcd(6 * s - 1, s) == 1 for s in (5, 55, 935)))
    line("row 30, a path gone through whole: 2, 3, 5, 7, 13, 23, 43, 83, 163, 317 and 631 are me-parities, a next short of its prior's double: at all numbers 1 to 630, a me-parity is past the number and to its double",
         all(least_part(p) == p for p in (2, 3, 5, 7, 13, 23, 43, 83, 163, 317, 631)) and all(b < 2 * a for a, b in zip((2, 3, 5, 7, 13, 23, 43, 83, 163, 317), (3, 5, 7, 13, 23, 43, 83, 163, 317, 631)))
         and all(any(n < p <= 2 * n for p in (2, 3, 5, 7, 13, 23, 43, 83, 163, 317, 631)) for n in range(1, 631)))
    first = me_parities(40)[:6]
    def only(n, k): return all(q in first[:k] for q in parts(n))
    line("rows 1 and 46, a moving of numbering: a number is a me again by a number with no part twice, v408primes' 78; with k me-parities the no-part-twice numbers are 2 doubled k times, and the me agains to N are its side: gone through whole at k of 1 to 6 and N of 4,096, the numbers of k me-parities' parts alone are no more than the side by that doubling",
         all(sum(1 for n in range(1, 4097) if only(n, k)) <= isqrt(4096) * 2 ** k for k in range(1, 7)) and all(len({d for d in range(1, 2 * 3 * 5 * 7 * 11 * 13 + 1) if (2 * 3 * 5 * 7 * 11 * 13) % d == 0 and only(d, k) and all(d % (q * q) for q in first[:k])}) == 2 ** k for k in range(1, 7)))
    def at_one(p, s):
        n = the_row_of(s, p)
        return all(q % p == 1 and gcd(q, s) == 1 for q in parts(n)) and n % p == 1
    line("row 53, a moving, its own reasons at a path of p mes: with s a seam of p, the row 1, s, s by s and on, p of them, added, is at the me 1 round p and round all parts of s; gone through at 3, 5 and 7",
         all(the_row_of(s, p) % p == 1 and all(the_row_of(s, p) % q == 1 for q in set(parts(s))) for p in (3, 5, 7) for s in (p, 2 * p, 6 * p)))
    seams = [(p, s) for p in (3, 5, 7, 11) for s in (p, 2 * p, 3 * p, 6 * p, 10 * p, 30 * p) if the_row_of(s, p) < 10 ** 12]
    test(f"row 53, the row's me-parity parts, at p of 3, 5, 7 and 11 and {len(seams)} seams with the row short of a million millions: all are at the me 1 round p, and cross no part of the seam. No breaking found", all(at_one(p, s) for p, s in seams))
    print("said apart: v408primes' table's rows are opened from its branch at 2c7e375, its pages not in the set at this main\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    for name, ok in tests: print(("tested   " if ok else "broken   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is; {sum(ok for _, ok in tests)} of {len(tests)} breaking tests found none")
    sys.exit(0 if all(ok for _, ok in results + tests) else 1)
