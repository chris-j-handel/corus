#!/usr/bin/env python3
"""Travelling by bi-folding, 1, 5, 17, 65, 257, to a far number and to a between there, tested exactly.

Usage:  python3 -I incoming/v406other2/instruments/travelling_by_bi_folding_to_a_far_number_and_a_between_there.py

A bi-folding is a surface four times out, and its next 1. A line ends is or is-not; a line ending sized
gives numbers alone. It opens no file and writes no file.
"""
from math import log10

out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


def plain_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


nexts = [4 ** k + 1 for k in range(1, 9)]
say("a surface's next 1, a bi-folding after a bi-folding, is 5, 17, 65, 257, 1,025, 4,097, 16,385 and 65,537; "
    "5, 17, 257 and 65,537 are primes, with 1, 2, 4 and 8 bi-foldings, and 261 is 9 by 29",
    nexts == [5, 17, 65, 257, 1025, 4097, 16385, 65537]
    and [n for n in nexts if plain_prime(n)] == [5, 17, 257, 65537] and 261 == 9 * 29)
P = 136_279_841
say("the world's record prime, 2 doubled 136,279,841 times less 1, is on the surface of 68,139,921 bi-foldings, "
    "past the one before it", 2 * 68_139_920 < P < 2 * 68_139_921)
say("a number multiplied by its own, from 2, is past the record with 28 multiplyings, and short of it with 27",
    2 ** 27 < P <= 2 ** 28)


def above(p):
    n, s = 2 ** p - 1, 4
    for _ in range(p - 2):
        s = (s * s - 2) % n
    return s == 0


old = (127, 521, 1279, 2203, 4423, 11213)
say("the old records, 2 doubled 127, 521, 1,279, 2,203, 4,423 and 11,213 times less 1, are primes by the "
    "explorer above, a multiplying a doubling: the highest has 3,376 places of ten and 11,211 multiplyings",
    all(above(p) for p in old) and int(11213 * log10(2)) + 1 == 3376)


def below_a_doubling(k, n):
    """the explorer below, the number below it k by 2 doubled n times, k short of the doubling"""
    big = k * 2 ** n + 1
    return any(pow(a, (big - 1) // 2, big) == big - 1 for a in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31))


found = []
for m in (8, 32, 128, 512):
    k = 1
    while not below_a_doubling(k, 2 * m):
        k += 2
    found.append((m, k, len(str(k)) + int(2 * m * log10(2))))
say("past a surface of 8, 32, 128 and 512 bi-foldings, a between is tested exactly by the explorer below, the "
    "number below it k by the surface: the lowest odd k are " + ", ".join(f"{k:,}" for m, k, d in found)
    + ", primes of " + ", ".join(str(d) for m, k, d in found) + " places of ten",
    plain_prime(found[0][1] * 4 ** 8 + 1) and all(k < 4 ** m for m, k, d in found))

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
