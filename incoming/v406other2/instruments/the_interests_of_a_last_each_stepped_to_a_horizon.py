#!/usr/bin/env python3
"""The public interests in the primes of a last, each stepped to a horizon with whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/the_interests_of_a_last_each_stepped_to_a_horizon.py

An interest of a last asks a thing with all numbers, with no turn showing it. A line here steps it to a
horizon: is says is to that horizon alone, and nothing past it. It opens no file and writes no file.
"""
N = 2_000_000
sieve = bytearray([1]) * (N + 1)
sieve[0] = sieve[1] = 0
for p in range(2, int(N ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


twins = [p for p in range(3, N - 1) if sieve[p] and sieve[p + 2]]
say(f"pairs of primes two apart go on to the horizon: {len(twins):,} pairs to {N:,}, the highest {twins[-1]:,} with "
    f"{twins[-1] + 2:,}, and a pair in all stretches of 10,000 past 100",
    all(any(sieve[p] and sieve[p + 2] for p in range(lo, lo + 10_000)) for lo in range(100, N - 10_002, 10_000)))
say("a prime is between a number multiplied by its own and the next number multiplied by its own: 1 to 1,413",
    all(any(sieve[m] for m in range(n * n + 1, (n + 1) * (n + 1))) for n in range(1, 1414)))
squares = [n * n + 1 for n in range(1, 1414) if sieve[n * n + 1]]
say(f"primes one more than a number multiplied by its own go on: {len(squares):,} to {N:,}, the highest {squares[-1]:,}",
    len(squares) > 100)
germain = [p for p in range(2, N // 2) if sieve[p] and sieve[2 * p + 1]]
say(f"primes with twice them and 1 more a prime go on: {len(germain):,} to {N // 2:,}, the highest {germain[-1]:,}",
    len(germain) > 1000)


def above(p):
    n, s = 2 ** p - 1, 4
    for _ in range(p - 2):
        s = (s * s - 2) % n
    return s == 0


doublings = [2] + [p for p in range(3, 1300) if sieve[p] and above(p)]
say("2 doubled p times less 1 is a prime with p of 2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607 and 1,279, "
    "and with no other p to 1,300, by the explorer above",
    doublings == [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279])
more = [k for k in range(0, 12) if pow(3, (2 ** (2 ** k)) // 2, 2 ** (2 ** k) + 1) == 2 ** (2 ** k)]
say("2 doubled 2, 4, 8 and 16 times and 1 more are primes, 5, 17, 257 and 65,537, and none of the next seven is, "
    "by the explorer below with 3", more == [1, 2, 3, 4])
gap, lastp, wide = 0, 2, (0, 0)
for m in range(3, N + 1):
    if sieve[m]:
        if m - lastp > gap:
            gap, wide = m - lastp, (lastp, m)
        lastp = m
say(f"the widest stretch with no prime to {N:,} is {gap}, {wide[0]:,} to {wide[1]:,}", "sized")

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
