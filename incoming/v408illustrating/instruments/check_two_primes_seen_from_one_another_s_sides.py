"""v408illustrating · the check of the 48th drawing: two primes seen from one another's sides, the quarter parted by its diagonal.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/check_two_primes_seen_from_one_another_s_sides.py .

The drawing is of v408primes' sentences 43 to 49, by its instrument two_primes_seen_from_one_another_s_sides.py, its
answer to this session's asking at the exchange on 25 November. Its numbers are executed here apart, by this check's own
lines. A pair is a me of both primes' paths, by the 47th drawing: v408primes' word of it is a place.
Its is and its is-not are both executed. Whole numbers alone. It writes none. All or none.
"""
import itertools, sys
from pathlib import Path

prime = lambda n: n > 1 and all(n % d for d in range(2, n) if d * d <= n)
by_itself = lambda p: sorted({x * x % p for x in range(1, p)})      # a number by itself, round a prime
seen = lambda q, p: 1 if q % p in by_itself(p) else -1               # q seen from p's side
def quarter(p, q):
    """The pairs of the quarter of two primes, (p - 1) / 2 by (q - 1) / 2: under its diagonal, over it, and on it."""
    pairs = [(k, j) for k in range(1, (p - 1) // 2 + 1) for j in range(1, (q - 1) // 2 + 1)]
    return [x for x in pairs if p * x[1] < q * x[0]], [x for x in pairs if p * x[1] > q * x[0]], [x for x in pairs if p * x[1] == q * x[0]]

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    P = [p for p in range(3, 200) if prime(p)]
    line("round a prime past 2, a number by itself is (p less 1) by 2 of the numbers 1 to p less 1: round 5, 1 and 4; round 7, 1, 2 and 4; round 11, 1, 3, 4, 5 and 9; primes to 199",
         [by_itself(p) for p in (5, 7, 11)] == [[1, 4], [1, 2, 4], [1, 3, 4, 5, 9]] and all(2 * len(by_itself(p)) == p - 1 for p in P))
    line("q seen from p's side is q multiplied by itself (p less 1) by 2 times round p, 1 or p less 1; primes to 199, all q",
         all(pow(q, (p - 1) // 2, p) == (1 if seen(q, p) == 1 else p - 1) for p in P for q in range(1, p)))
    two = list(itertools.combinations(P, 2))
    line("the quarter of two primes is parted whole by its diagonal: no pair is on it, and the pairs under it with the pairs over it are all its pairs; all pairs of primes 3 to 199",
         all(not on and len(u) + len(o) == ((p - 1) // 2) * ((q - 1) // 2) for p, q in two for u, o, on in [quarter(p, q)]))
    line("the pairs under the diagonal, odd or even, are how p sees q, and the pairs over it how q sees p; all pairs of primes 3 to 199",
         all(seen(q, p) == (-1) ** len(u) and seen(p, q) == (-1) ** len(o) for p, q in two for u, o, _ in [quarter(p, q)]))
    drawn = {(p, q): (len(quarter(p, q)[0]), len(quarter(p, q)[1]), seen(q, p), seen(p, q)) for p, q in ((5, 7), (5, 11), (7, 11))}
    line("5 and 7: 3 under and 3 over, seen -1 and -1; 5 and 11: 6 and 4, seen 1 and 1; 7 and 11: 8 and 7, seen 1 and -1",
         drawn == {(5, 7): (3, 3, -1, -1), (5, 11): (6, 4, 1, 1), (7, 11): (8, 7, 1, -1)})
    line("is: two primes are seen alike from one another's sides; is-not: with both one short of a seam of 4 they are seen other-than, 7 and 11, and 3 and 7; all pairs of primes 3 to 199",
         all((seen(q, p) == seen(p, q)) != (p % 4 == 3 and q % 4 == 3) for p, q in two))
    line("a quarter's pairs are an odd number with both primes one short of a seam of 4, and with them alone: under and over are then one odd and one even",
         all((((p - 1) // 2) * ((q - 1) // 2) % 2 == 1) == (p % 4 == 3 and q % 4 == 3) for p, q in two))
    print("said apart: v408primes' instrument and its co-chain are not in the set at this main; opened from its branch at 9897e4a, its 5 and 7 are 3 under and 3 over, as here\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
