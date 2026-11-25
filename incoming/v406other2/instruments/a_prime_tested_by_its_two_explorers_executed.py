#!/usr/bin/env python3
"""A prime tested from the number below it and from the number above it: executed with whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/a_prime_tested_by_its_two_explorers_executed.py

The explorer below: a number a, multiplied by its own round n, comes to 1 again with n less 1 multiplyings
and with no fewer, the fewer ones named by the prime parts of n less 1. The explorer above, with n a
doubling less 1: a number multiplied by its own, less 2, and again, round n. A line is a saying, ending
is or is-not; a line ending sized gives numbers alone. It opens no file and writes no file.
"""
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


def parts(n):
    found, d = [], 2
    while d * d <= n:
        if n % d == 0:
            found.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        found.append(n)
    return found


def prime(n):
    return n > 1 and parts(n) == [n]


def below(n, bases=None):
    """the explorer below: a number coming to 1 again round n with n less 1 multiplyings and no fewer"""
    qs = parts(n - 1)
    for a in (bases or range(2, n)):
        if pow(a, n - 1, n) == 1 and all(pow(a, (n - 1) // q, n) != 1 for q in qs):
            return a
    return None


LIMIT = 2000
say(f"a number is a prime with a number coming to 1 again round it with one less multiplyings and no fewer, "
    f"and is no prime with none: 3 to {LIMIT:,}, all numbers below it gone through",
    all((below(n) is not None) == prime(n) for n in range(3, LIMIT + 1)))
say("31, 211 and 2,311 are one more than the turns of 30, 210 and 2,310, and are tested by their turn's primes "
    "alone; 61 by 2, 3 and 5",
    parts(30) == [2, 3, 5] and parts(210) == [2, 3, 5, 7] and parts(2310) == [2, 3, 5, 7, 11] and parts(60) == [2, 3, 5]
    and all(below(n) is not None for n in (31, 61, 211, 2311)))


def above_a_doubling(p):
    """the explorer above, n a doubling p times less 1: 4, then by its own less 2, p less 2 times, to 0"""
    n, s = 2 ** p - 1, 4
    for _ in range(p - 2):
        s = (s * s - 2) % n
    return s == 0


odd = [p for p in range(3, 42) if prime(p)]
say("with 2 doubled p times less 1, the number above is all doublings, and the explorer above alone tests it: "
    "primes with p of 3, 5, 7, 13, 17, 19 and 31, and no primes with 11, 23, 29, 37 and 41",
    all(above_a_doubling(p) == prime(2 ** p - 1) for p in odd)
    and [p for p in odd if above_a_doubling(p)] == [3, 5, 7, 13, 17, 19, 31])
fermat = [2 ** (2 ** k) + 1 for k in range(1, 6)]
say("with 2 doubled 2, 4, 8, 16 and 32 times and 1 more, the number below is all doublings, and the explorer "
    "below alone tests it with 3: 5, 17, 257 and 65,537 are primes, and 4,294,967,297 is 641 by 6,700,417",
    [pow(3, (f - 1) // 2, f) == f - 1 for f in fermat] == [True, True, True, True, False]
    and 641 * 6700417 == fermat[4])


def tree(n, seen=None):
    seen = set() if seen is None else seen
    for q in parts(n - 1):
        if q not in seen:
            seen.add(q)
            if q > 2:
                tree(q, seen)
    return seen


say("a prime's test is of the primes of the number below it, and theirs of the primes below them, to 2: "
    f"2,311 has {sorted(tree(2311))}, 1,999 has {sorted(tree(1999))}, 65,537 has {sorted(tree(65537))}", "sized")
say("all primes of a prime's tree are primes below it, tested the same: the primes to 2,000",
    all(all(prime(q) and q < n and (q == 2 or below(q) is not None) for q in tree(n))
        for n in range(3, LIMIT + 1) if prime(n)))

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
