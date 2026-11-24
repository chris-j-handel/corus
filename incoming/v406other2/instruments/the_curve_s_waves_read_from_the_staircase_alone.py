#!/usr/bin/env python3
"""The curve's waves read from the staircase alone: the pitches of the primes' own straying.

Usage:  python3 -I incoming/v406other2/instruments/the_curve_s_waves_read_from_the_staircase_alone.py

It steps the primes to 100,000 with whole numbers, and no curve and no function of a curve is in it. On
the primes alone it lays a field's measuring, a logarithm and a cosine: a prime power q of a prime p is a
wave of pitch t, cos(t log q), weighed log p over the square side of q, and fading to none at the horizon:
with no fading the horizon's own edge rings over the pitches. All the waves added are high at some pitches. A field has its curve's first zeros at 14.1347, 21.0220, 25.0109, 30.4249, 32.9351 and
37.5862. A line ends is with a high pitch of the primes by a zero, to 0.2. It writes no file.

A measuring, and no whole-number stepping: its numbers have decimals, and it decides nothing.
"""
from math import cos, log, sqrt

LIMIT = 100_000
sieve = bytearray([1]) * (LIMIT + 1)
sieve[0] = sieve[1] = 0
for p in range(2, int(LIMIT ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
waves = []                                # (weight, the logarithm of a prime power)
for p in range(2, LIMIT + 1):
    if sieve[p]:
        q = p
        while q <= LIMIT:
            waves.append((log(p) / sqrt(q) * (1 - log(q) / log(LIMIT)), log(q)))
            q *= p


def height(t):
    return -sum(w * cos(t * lq) for w, lq in waves)


STEP = 0.02
ts = [10 + STEP * i for i in range(int(30 / STEP) + 1)]
hs = [height(t) for t in ts]
mean = sum(hs) / len(hs)
peaks = []
for i in range(1, len(ts) - 1):
    if hs[i] > hs[i - 1] and hs[i] >= hs[i + 1]:
        peaks.append((hs[i], ts[i]))
peaks.sort(reverse=True)
top = sorted(t for h, t in peaks[:6])
zeros = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862]
print(f"primes stepped to {LIMIT:,}: {sum(sieve):,} primes, {len(waves):,} prime powers; no curve in it")
print("the six highest pitches of the primes' waves, 10 to 40: " + ", ".join(f"{t:.2f}" for t in top))
print("a field's first six zeros of its curve:                 " + ", ".join(f"{z:.2f}" for z in zeros))
ok = len(top) == 6 and all(abs(a - b) <= 0.2 for a, b in zip(top, zeros))
print(f"\n{'is' if ok else 'is-not'}      the six highest pitches of the primes alone are a field's first six zeros, to 0.2")
sixth = sorted(h for h, t in peaks)[-6]
rest = max((h for h, t in peaks if h < sixth), default=0)
print(f"sized   the six are {sixth:.1f} high and more; the highest pitch apart from them is {rest:.1f} high")
