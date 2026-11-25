#!/usr/bin/env python3
"""The explorers' spirals locking with a surface's crossings about the world's record prime.

Usage:  python3 -I incoming/v406other2/instruments/the_two_skeletons_locking_about_the_record_prime.py

The record is 2 doubled 136,279,841 times less 1, never written out. The explorers carry spirals of 2 selves
and on; a spiral carried has its crossings of the 10,000,000 numbers past the record all or none. A line
ending sized gives numbers alone; a line ends is or is-not. It opens no file and writes no file.
"""
P, PAST, SPIRALS = 136_279_841, 10_000_000, 2_000_000
sieve = bytearray([1]) * (SPIRALS + 1)
sieve[0] = sieve[1] = 0
for p in range(2, int(SPIRALS ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))


def crossings():
    free = bytearray([1]) * (PAST + 1)
    free[0] = 0
    marks, at_mark = (2, 3, 5, 7, 17, 100, 10_000, 2_000_000), {}
    for q in range(2, SPIRALS + 1):
        if sieve[q]:
            at = (-(pow(2, P, q) - 1)) % q or q
            free[at::q] = bytearray(len(free[at::q]))
        if q in marks:
            at_mark[q] = PAST - sum(free)
    return at_mark, bytes(free)


first, map_1 = crossings()
again, map_2 = crossings()
for q, n in first.items():
    print(f"sized   with the spirals to {q:,} carried, {n:,} of the {PAST:,} numbers past the record are crossed, "
          f"and {PAST - n:,} are with no crossing of them")
same = map_1 == map_2
print(f"{'is' if same else 'is-not':8}stepped again, the crossings are the same at all {PAST:,} numbers")
