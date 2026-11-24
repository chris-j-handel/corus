#!/usr/bin/env python3
"""The world's record prime brought back into the 1 to 17: out by doubling round a spiral, and back.

Usage:  python3 -I incoming/v406other2/instruments/the_record_prime_brought_back_into_the_1_to_17.py

The record is 2 doubled 136,279,841 times less 1, and is never written out: round a spiral of n selves it
is 2 doubled round n, less 1. A line ends is or is-not; a line ending sized gives numbers alone. It opens
no file and writes no file.
"""
P = 136_279_841
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


def round_(n):
    return (pow(2, P, n) - 1) % n


def parts(n):
    found, d = [], 2
    while d * d <= n:
        if n % d == 0:
            found.append(d)
            while n % d == 0:
                n //= d
        d += 1
    return found + ([n] if n > 1 else [])


say("out and back round a spiral is 27 multiplyings of a number by its own and the multiplyings by 2 with them: "
    "136,279,841 is past 2 doubled 27 times and short of 28", 2 ** 27 < P < 2 ** 28)
say("round 17 the record is 1, a next 1; round 16 it is 15, one less than the surface",
    round_(17) == 1 and round_(16) == 15)
say("round the primes of 1 to 16, 2, 3, 5, 7, 11 and 13, it is 1, 1, 1, 3, 1 and 5",
    [round_(q) for q in (2, 3, 5, 7, 11, 13)] == [1, 1, 1, 3, 1, 5])
say("round 30 it is at the place 1, and round 60 and round 120 at the place 31; round 12 at 7, one less than "
    "4's seam and one more than 6's", [round_(n) for n in (30, 60, 120, 12)] == [1, 31, 31, 7])
say("the record and 1 more is half its surface of 68,139,921 bi-foldings: bi-folded back 68,139,919 times it is "
    "8, half the surface of 16, and the record is 7, one less", P - 2 * 68_139_919 == 3 and 2 ** 3 - 1 == 7)
say("7 is of the record's kind, 2 doubled 3 times less 1, a prime; in 1 to 16 the kind is 1, 3, 7 and 15, with "
    "3 and 7 primes", [2 ** k - 1 for k in (1, 2, 3, 4)] == [1, 3, 7, 15])
say("the record's test, by the explorer above, is of 2 alone, the number above it all doublings; its number of "
    f"doublings is a prime, the primes of the number below it {parts(P - 1)}", parts(P) == [P])
ok = all(pow(2, p, 120) - 1 in (7, 31) for p in (3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279))
say("round 120 a doubling less 1, a prime past 3, is at 7 or at 31: the fourteen of them to 1,279 doublings", ok)

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
