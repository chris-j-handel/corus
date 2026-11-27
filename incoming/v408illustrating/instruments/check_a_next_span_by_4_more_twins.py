"""v408illustrating · the check of the 54th drawing: a next span by 4 beside its prior, more twins; v408primes' sentences 132, 163 and 209, executed apart.

Usage, from the repository's root (about a minute):
  python3 -I incoming/v408illustrating/instruments/check_a_next_span_by_4_more_twins.py .

v408primes laid that twins are more at a next span by 4, and that, resolver to resolver, a twin's places are uncrossed at
r - 2 of r. They are executed here apart, by this check's own lines, to 4,194,304, nine spans by 4 whole. A span by 4 is
the numbers from a number to short of 4 times it; a twin is of the span of its lower me-parity; a twin's room, round a
seam, is a me of the seam's path with the me a step back and the me a step on both uncrossed by the seam's primes.
A room is with all numbers; a birth is stepped: they are said apart. Its is and its is-not are both executed.
Whole numbers alone. It writes none.
"""
import bisect, sys
from math import gcd, isqrt

N = 4 ** 11
PAST = N + 400                                                       # stepped a little past the last span, for a last me-parity's next
SPANS = [(4 ** k, 4 ** (k + 1)) for k in range(2, 11)]
SEAMS = [(3, 6), (5, 30), (7, 210), (11, 2310), (13, 30030)]
def stepped():
    sieve = bytearray([1]) * (PAST + 1); sieve[0] = sieve[1] = 0
    for n in range(2, isqrt(PAST) + 1):
        if sieve[n]: sieve[n * n::n] = bytearray(len(range(n * n, PAST + 1, n)))
    return sieve
def rooms(seam):
    """Round a seam, the mes of its path that are a twin's room: the me a step back and the me a step on both uncrossed by the seam's primes."""
    return [m for m in range(seam) if gcd(m - 1, seam) == 1 and gcd(m + 1, seam) == 1]
def the_numbers():
    sieve = stepped()
    mes = [p for p in range(2, PAST + 1) if sieve[p]]
    lowers = [p for p in mes if p + 2 <= PAST and sieve[p + 2]]
    twins = [[p for p in lowers[bisect.bisect_left(lowers, a):bisect.bisect_left(lowers, b)]] for a, b in SPANS]
    living = [bisect.bisect_left(mes, b) - bisect.bisect_left(mes, a) for a, b in SPANS]
    widest = [max(mes[k + 1] - mes[k] for k in range(bisect.bisect_left(mes, a), bisect.bisect_left(mes, b))) for a, b in SPANS]
    cut = sum(1 for p in twins[-1] if p + 2 <= 4_000_000)
    return dict(sieve=sieve, mes=mes, lowers=[p for p in lowers if p < N], twins=twins, living=living, widest=widest, cut=cut)

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    d = the_numbers(); born = [len(t) for t in d["twins"]]
    line("births, stepped: a span by 4, 16 to 64 and on to 4,194,304, is with 4, 10, 19, 71, 183, 570, 1,819, 5,856 and 19,460 twins, at all nine spans more than its prior; to 4,000,000 the last is 18,325, v408primes' 163 executed apart",
         born == [4, 10, 19, 71, 183, 570, 1819, 5856, 19460] and all(a < b for a, b in zip(born, born[1:])) and d["cut"] == 18325)
    thousand = [round(1000 * b / (hi - lo), 1) for b, (lo, hi) in zip(born, SPANS)]
    line("is-not, explored: of a span's numbers, twins are fewer in a thousand at all next spans: 83.3, 52.1, 24.7, 23.1, 14.9, 11.6, 9.3, 7.4 and 6.2; a next span's twins are short of 4 times its prior's",
         thousand == [83.3, 52.1, 24.7, 23.1, 14.9, 11.6, 9.3, 7.4, 6.2] and all(4 * a > b for a, b in zip(born, born[1:])))
    line("me-parities are more at all next spans, 12, 36, 118 and on to 213,922, and the widest from a me-parity of a span to its next is more at all: 6, 14, 20, 34, 44, 72, 86, 114 and 148, v408primes' 209 executed apart",
         d["living"][:3] == [12, 36, 118] and d["living"][-1] == 213922 and all(a < b for a, b in zip(d["living"], d["living"][1:])) and d["widest"] == [6, 14, 20, 34, 44, 72, 86, 114, 148])
    found = [len(rooms(s)) for _, s in SEAMS]
    line("rooms: round the seams 6, 30, 210, 2,310 and 30,030 a twin's rooms are 1, 3, 15, 135 and 1,485, a next seam's being its prior's by r - 2, v408primes' 132 executed apart",
         found == [1, 3, 15, 135, 1485] and all(b == a * (r - 2) for (r, _), a, b in zip(SEAMS[1:], found, found[1:])))
    line("rooms, with all numbers: of the r mes of a path of r closing, a twin's between is uncrossed by r at all but the me one on and the me one back, r - 2 of r, at all primes r of 3 to 31; a next seam is with rooms at all",
         all(sum(1 for m in range(r) if (m - 1) % r and (m + 1) % r) == r - 2 > 0 for r in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)))
    r30 = set(rooms(30030)); all_twins = d["lowers"]
    in_rooms = [p for p in all_twins if 13 < p and p + 1 < 30030]
    line("a twin past 13 is born in a room: all twins to 4,194,304 are at a room round 30,030; and a room is no birth: of the 1,485 rooms below 30,030, twins are born at 465",
         all(((p + 1) % 30030) in r30 for p in all_twins if p > 13) and len(in_rooms) == 465 and all(p + 1 in r30 for p in in_rooms))
    line("is-not, explored: a room with no birth, the least past 13 round 30,030: 120 is no room, 119 being 7 by 17; the least room with no birth is 360, 361 being 19 by 19",
         120 not in r30 and 119 == 7 * 17 and min(m for m in sorted(r30) if m > 14 and not (d["sieve"][m - 1] and d["sieve"][m + 1])) == 360 and 361 == 19 * 19 and d["sieve"][359])
    print("said apart: more twins at all next spans is stepped, nine spans; it is no saying with all spans · v408primes' pages are not in the set at this main; its sentences are opened from its branch at 09b70e9\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
