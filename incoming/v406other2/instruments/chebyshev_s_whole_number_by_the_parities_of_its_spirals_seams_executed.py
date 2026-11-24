#!/usr/bin/env python3
"""Chebyshev's argument in natural naming, executed with whole numbers alone: a whole number, its prime
parts by the seams of spirals on a surface, set beside its size.

Usage:  python3 -I incoming/v406other2/instruments/chebyshev_s_whole_number_by_the_parities_of_its_spirals_seams_executed.py

A line is a saying, ending is or is-not. Nothing is proved and nothing is decided: a line says is of what
it stepped. It opens no file and writes no file.

Its names: a spiral of q selves has n by q seams on 1 to n, whole; the middle number of 1 to 2n is 2n
multiplied down, over n multiplied down twice; Chebyshev's number of 30 is 30n multiplied down by n
multiplied down, over 15n, 10n and 6n multiplied down.
"""
from math import comb, factorial

out = []


def say(text, ok):
    out.append(("is" if ok else "is-not", text))


LIMIT = 2000
low = list(range(30 * 150 + 1))
for p in range(2, int(len(low) ** 0.5) + 1):
    if low[p] == p:
        for m in range(p * p, len(low), p):
            if low[m] == m:
                low[m] = p
primes = [n for n in range(2, len(low)) if low[n] == n]


def part(number, p):
    e = 0
    while number % p == 0:
        number //= p
        e += 1
    return e


# The middle number of 1 to 2n.
ok1 = ok2 = ok3 = ok4 = ok5 = True
for n in range(1, LIMIT + 1):
    mid = comb(2 * n, n)
    ok2 = ok2 and mid < 4 ** n
    born = 1
    for p in primes:
        if p > 2 * n:
            break
        odd, q = 0, p
        while q <= 2 * n:
            odd += (2 * n // q) % 2          # is the spiral of q at an odd number of seams on 1 to 2n
            q *= p
        e = part(mid, p)
        ok1 = ok1 and e == odd
        ok5 = ok5 and p ** e <= 2 * n
        if p > n:
            ok3 = ok3 and e == 1
            born *= p
        elif n >= 3 and 3 * p > 2 * n:
            ok4 = ok4 and e == 0
    ok3 = ok3 and born < 4 ** n
say(f"a prime's part in the middle number of 1 to 2n is the powers of it with an odd number of seams on 1 to 2n: "
    f"n of 1 to {LIMIT:,}", ok1)
say(f"the middle number is short of 4 to the n: n of 1 to {LIMIT:,}", ok2)
say(f"a prime past n and to 2n has one seam and is in it once, and all of them multiplied are short of 4 to the n: "
    f"n of 1 to {LIMIT:,}", ok3)
say(f"a prime past two thirds of n and to n has two seams and is not in it: n of 3 to {LIMIT:,}", ok4)
say(f"a prime's part in it, multiplied out, is at most 2n: n of 1 to {LIMIT:,}", ok5)


# Chebyshev's number of 30.
def f(x_num, x_den=1):
    """x less x over 2, over 3 and over 5, and x over 30 more, all whole: x is x_num over x_den"""
    return (x_num // x_den - x_num // (2 * x_den) - x_num // (3 * x_den) - x_num // (5 * x_den)
            + x_num // (30 * x_den))


vals = [f(n) for n in range(1, 31)]
say("a number less its seams of 2, of 3 and of 5, and its seams of 30 more, is 1 or 0 alone, 1 to 30: "
    "1 at 1 to 5, 7 to 9, 11, 13, 14, 17, 19, 23 and 29",
    set(vals) == {0, 1} and [n for n in range(1, 31) if f(n)] == [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 17, 19, 23, 29])
say("it comes again with 30, to 3,000", all(f(n) == f(n + 30) for n in range(1, 3001)))
say("it is 1 at all eight places of 30 no spiral of 2, 3 or 5 crosses: 1, 7, 11, 13, 17, 19, 23 and 29",
    all(f(n) == 1 for n in range(1, 31) if n % 2 and n % 3 and n % 5))
ok6 = ok7 = ok8 = True
for n in range(1, 151):
    top = factorial(30 * n) * factorial(n)
    bottom = factorial(15 * n) * factorial(10 * n) * factorial(6 * n)
    ok6 = ok6 and top % bottom == 0
    number = top // bottom
    for p in primes:
        if p > 30 * n:
            break
        at, q = 0, p
        while q <= 30 * n:
            at += f(30 * n, q)
            q *= p
        e = part(number, p)
        ok7 = ok7 and e == at
        if p > 5 * n:
            ok8 = ok8 and e == 1
say("Chebyshev's number of 30 is whole: n of 1 to 150", ok6)
say("a prime's part in it is the powers of it at a place of 1: n of 1 to 150", ok7)
say("a prime past 5n and to 30n is in it once: n of 1 to 150", ok8)

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not.")
