#!/usr/bin/env python3
"""A prime ridden to its own crossing, and 1 more: a larger prime, tested with the prime ridden beside it.

Usage:  python3 -I incoming/v406other2/instruments/a_prime_ridden_to_its_crossing_and_1_more_a_larger_prime.py

The number tested is 2 by k by the prime, and 1 more, with 2 by k short of the prime. The number below it
is the prime's crossing, its primes given. A line ends is or is-not. It opens no file and writes no file.
"""
from math import gcd, log10


def ride(p, ks):
    for k in ks:
        n = 2 * k * p + 1
        if 2 * k < p and any(pow(a, n - 1, n) == 1 and gcd(pow(a, 2 * k, n) - 1, n) == 1 for a in (2, 3, 5, 7)):
            return 2 * k, n
    return None


found = [ride(p, range(1, 20000)) for p in (8191, 2 ** 31 - 1, 2 ** 127 - 1, 2 ** 521 - 1, 2 ** 1279 - 1)]
ok = [c for c, n in found] == [46, 46, 114, 336, 1474] and [int(log10(n)) + 1 for c, n in found] == [6, 11, 41, 160, 389]
print(f"{'is' if ok else 'is-not':8}from 8,191, 2,147,483,647 and 2 doubled 127, 521 and 1,279 times less 1, the lowest "
      "crossing with 1 more a prime is 46, 46, 114, 336 and 1,474 by the prime: primes of 6, 11, 41, 160 and 389 places")
plain = all((46 * 8191 + 1) % d for d in range(2, 615))
print(f"{'is' if plain and ride(31, range(1, 15)) == (10, 311) else 'is-not':8}from 31 it is 10 by 31 and 1 more, 311; "
      "and 46 by 8,191 and 1 more is a prime by plain stepping")
print(f"{'is' if all(ride(p, [m]) is None for p in (8191, 2 ** 31 - 1, 2 ** 127 - 1) for m in (1, 2, 4, 8)) else 'is-not':8}"
      "2, 4, 8 and 16 by these primes, and 1 more, are no primes: a crossing farther is")
