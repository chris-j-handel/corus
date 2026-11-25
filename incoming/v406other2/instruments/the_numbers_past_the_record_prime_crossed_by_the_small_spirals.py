#!/usr/bin/env python3
"""The numbers past the world's record prime, crossed by the small spirals; and the next prime past the
old records, tested by the explorer below.

Usage:  python3 -I incoming/v406other2/instruments/the_numbers_past_the_record_prime_crossed_by_the_small_spirals.py

The record is 2 doubled 136,279,841 times less 1. It is never written out here: a spiral of q selves is at
its seam with the record and g more, with g of one place round q, found by 2 doubled round q. A line ends
is or is-not; a line ending sized gives numbers alone. It finds no prime past the record: it crosses, and
what is not crossed is not tested. It opens no file and writes no file.
"""
from math import log, log10

P = 136_279_841
SPIRALS = 2_000_000
PAST = 10_000_000
sieve = bytearray([1]) * (SPIRALS + 1)
sieve[0] = sieve[1] = 0
for p in range(2, int(SPIRALS ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


say("136,279,841 is a prime", all(P % d for d in range(2, int(P ** 0.5) + 1)))
say(f"the record has {int(P * log10(2)) + 1:,} places of ten, and a field's measuring has the stretch to a next "
    f"prime about {int(P * log(2)):,}", "sized")
open_ = bytearray([1]) * (PAST + 1)
open_[0] = 0
open_[1::2] = bytearray(len(open_[1::2]))            # the record is odd: an odd number more is at 2's seam
for q in range(3, SPIRALS + 1):
    if sieve[q]:
        at = (-(pow(2, P, q) - 1)) % q
        if at == 0:
            at = q
        open_[at::q] = bytearray(len(open_[at::q]))
left = [g for g in range(2, PAST + 1, 2) if open_[g]]
say(f"of the {PAST:,} numbers past the record, {PAST - len(left):,} are crossed by a spiral of 2 to {SPIRALS:,} "
    f"selves, and {len(left):,} are not", "sized")
say("the lowest not crossed are the record and " + ", ".join(f"{g:,}" for g in left[:10]) + " more", "sized")
say("none of them is tested here: a test of one is about 136,279,841 multiplyings of a number of 41,024,320 "
    "places by its own, and the primes beside it are not found", "sized")


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


def below(n):
    qs = parts(n - 1)
    for a in range(2, 200):
        if pow(a, n - 1, n) == 1 and all(pow(a, (n - 1) // q, n) != 1 for q in qs):
            return a
    return None


nexts = []
for d in (13, 17, 19, 31):
    n = 2 ** d + 1
    while below(n) is None:
        n += 2
    nexts.append(n)
say("past the old records, 2 doubled 13, 17, 19 and 31 times less 1, the next primes are 8,209, 131,101, 524,309 "
    "and 2,147,483,659, tested by the explorer below with all the primes of the number below found",
    nexts == [8209, 131101, 524309, 2147483659]
    and all(all(m % d for d in range(2, int(m ** 0.5) + 1)) for m in nexts[:3])
    and all(any(m % d == 0 for d in range(2, int(m ** 0.5) + 1)) for n, lo in zip(nexts[:3], (8192, 131072, 524288))
            for m in range(lo, n)))

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
