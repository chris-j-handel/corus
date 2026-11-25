#!/usr/bin/env python3
"""The leanest sentences of prime numbering, executed with whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/the_leanest_sentences_of_prime_numbering_executed.py

A line ends is or is-not, and says is of what it stepped. It opens no file and writes no file.
"""
from math import lcm

N = 5000
made = [False] * (N + 1)                 # made by two smaller numbers of 2 and on, multiplied
for a in range(2, N + 1):
    for b in range(a, N // a + 1):
        made[a * b] = True
primes = [n for n in range(2, N + 1) if not made[n]]


def partings(n, least=0):
    """the ways n is primes multiplied, the primes in a row from the lowest"""
    if n == 1:
        return 1
    return sum(partings(n // p, i) for i, p in enumerate(primes) if i >= least and p <= n and n % p == 0)


lines = [
    ("a number from 2 on is made by two smaller numbers multiplied, or by none, and never both: 2 to 5,000",
     all(made[n] != (n in set(primes)) for n in range(2, N + 1))),
    ("a number from 2 on is primes multiplied one way alone: 2 to 5,000",
     all(partings(n) == 1 for n in range(2, N + 1))),
    ("at their turn the spirals of 2 to m all line up, and one past it none of them does: m of 2 to 23",
     all(all((lcm(*range(2, m + 1)) + 1) % k == 1 for k in range(2, m + 1)) for m in range(2, 24))),
    ("2, 3 and 5 line up at 30, and 31, one past, is made by no two smaller numbers", not made[31] and 30 % 2 == 30 % 3 == 30 % 5 == 0),
]
for text, ok in lines:
    print(f"{'is' if ok else 'is-not':8}{text}")
print(f"\n{sum(ok for t, ok in lines)} is; {sum(not ok for t, ok in lines)} is-not.")
