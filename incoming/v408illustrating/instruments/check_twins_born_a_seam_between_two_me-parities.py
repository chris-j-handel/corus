"""v408illustrating · the check of the 53rd drawing: twins born, a seam between two me-parities; v408primes' sentences 188 to 200, executed apart.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/check_twins_born_a_seam_between_two_me-parities.py .

v408primes laid, on 25 November, twins born, and said it to this session at the exchange for drawing. Its sentences are
executed here apart, by this check's own lines, to 4,000,000, that session's own span. v408primes' word of a prime is a
me-parity; twins are two me-parities 2 apart, and their between is the even number a +1 from both; a seam of n is a number
n crosses; a me again is a number by itself. What is with all numbers is said apart from what is stepped.
Its is and its is-not are both executed. Whole numbers alone. It writes none.
"""
import sys
from math import gcd, isqrt

N = 4_000_000
def stepped():
    sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
    for n in range(2, isqrt(N) + 1):
        if sieve[n]: sieve[n * n::n] = bytearray(len(range(n * n, N + 1, n)))
    return sieve
def the_moving(n):
    """A me again of side n, cell by cell: its last row, less a cell, laid as a column more. It gives the cells after the moving, and the cell let go."""
    cells = {(r, k) for r in range(n) for k in range(n)}
    one = (n - 1, n - 1); cells.discard(one)
    for k in range(n - 1): cells.discard((n - 1, k)); cells.add((k, n))
    return cells, one
def the_numbers():
    sieve = stepped()
    mes = [p for p in range(2, N + 1) if sieve[p]]
    twins = [p for p in mes if p + 2 <= N and sieve[p + 2]]          # a twin's lower me-parity; their between is p + 1
    nxt = {}
    for a, b in zip(mes, mes[1:]): nxt[a] = b
    at = {}                                                          # round 30, the seam twins past 5 are born at
    for p in twins:
        if p > 5: at[(p + 1) % 30] = at.get((p + 1) % 30, 0) + 1
    on = {}                                                          # the next me-parity after a twin's upper, and how many on
    for p in twins:
        if p + 2 in nxt: on[nxt[p + 2] - (p + 2)] = on.get(nxt[p + 2] - (p + 2), 0) + 1
    return dict(sieve=sieve, mes=mes, twins=twins, nxt=nxt, at=at, on=on)

if __name__ == "__main__":
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    d = the_numbers(); sieve, twins, nxt = d["sieve"], d["twins"], d["nxt"]
    past3 = [p for p in twins if p > 3]
    line("twins born: 26,860 twins among 283,146 me-parities to 4,000,000, v408primes' 189 executed apart; past 3, all 26,859 are a seam of 6 with a me-parity at both its sides, v408primes' 188",
         len(twins) == 26860 and len(d["mes"]) == 283146 and len(past3) == 26859 and all((p + 1) % 6 == 0 for p in past3) and twins[0] == 3)
    line("their between is even, other-than both, and no prime crosses it with either, v408primes' 191: all 26,860; it is with all numbers a +1 apart",
         all((p + 1) % 2 == 0 and gcd(p + 1, p) == 1 and gcd(p + 1, p + 2) == 1 for p in twins))
    line("round the between the twins are one step back and one step on, and their me agains are both at 1, v408primes' 192 and 193; round the lower twin the between is one step on, and round the upper one step back, v408primes' 194: all 26,860",
         all(p % (p + 1) == p and (p + 2) % (p + 1) == 1 and (p * p) % (p + 1) == 1 and ((p + 2) * (p + 2)) % (p + 1) == 1 and (p + 1) % p == 1 and (p + 1) % (p + 2) == p + 1 for p in twins))
    line("the twins' two paths come again together one short of the between's me again, v408primes' 196: all 26,860; 5 and 7 at 35, 11 and 13 at 143",
         all(p * (p + 2) == (p + 1) * (p + 1) - 1 for p in twins) and 5 * 7 == 35 == 36 - 1 and 11 * 13 == 143 == 144 - 1)
    line("the moving that says it at all sides: a me again's last row, less a cell, laid as a column more, is its side less 1 by its side and 1, with a cell let go; executed cell by cell, sides 2 to 60",
         all(the_moving(n)[0] == {(r, k) for r in range(n - 1) for k in range(n + 1)} and len(the_moving(n)[0]) == n * n - 1 for n in range(2, 61)))
    line("the upper twin's prior is the seam it was born in, and the lower twin's prior is two short of the seam, crossed by no 3, v408primes' 197 and 198, a twin's loop across being its prior: all 26,859 past 3",
         all((p + 2) - 1 == p + 1 and p - 1 == (p + 1) - 2 and (p - 1) % 3 != 0 for p in past3))
    seams30 = [s for s in range(0, 30, 6) if all((s + e) % 5 for e in (-1, 1))]
    line("round 30, twins past 5 are born at three seams, 12, 18 and 0: 8,960, 8,945 and 8,953, v408primes' 199; with all numbers, of the five seams of 6 of a path of 30 mes closing, 6 and 24 are with a side crossed by 5, the me 5 and the me 25",
         d["at"] == {12: 8960, 18: 8945, 0: 8953} and seams30 == [0, 12, 18] and sum(d["at"].values()) == 26858)
    line("born two: past 3, 5 and 7, the next me-parity after a twin is 4 or more on, v408primes' 200; with all numbers, of three numbers 2 apart one is crossed by 3, at all three mes of a path of 3 closing",
         all(nxt[p + 2] - (p + 2) >= 4 for p in twins if p > 3 and p + 2 in nxt) and nxt[5] == 7 and all(sorted((a + e) % 3 for e in (0, 2, 4)) == [0, 1, 2] for a in range(3)))
    line("stepped: the next me-parity after a twin past 3 is 4 on at 4,124 twins, 6 on at 3,719, and more than 6 on at 19,016; the widest is 120 on",
         d["on"].get(2, 0) == 1 and d["on"][4] == 4124 and d["on"][6] == 3719 and sum(v for k, v in d["on"].items() if k > 6) == 19016 and max(d["on"]) == 120 and sum(d["on"].values()) == 26860)
    line("is-not, explored: twins are born at 26,859 of the 666,666 seams of 6 below 4,000,000, 1 seam in 24 and more; and 3 and 5 are twins about 4, no seam of 6",
         len(range(6, N, 6)) == 666666 and 24 * 26859 < 666666 < 25 * 26859 and sieve[3] and sieve[5] and 4 % 6 != 0)
    print("said apart: v408primes' pages are not in the set at this main; its sentences 188 to 200 are opened from its branch at 598b836 · a loop across is that session's naming\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
