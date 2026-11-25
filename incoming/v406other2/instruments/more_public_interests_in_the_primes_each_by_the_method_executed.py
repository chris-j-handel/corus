#!/usr/bin/env python3
"""More public interests in the primes, each by the method of adding 1 and multiplying: executed with whole
numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/more_public_interests_in_the_primes_each_by_the_method_executed.py

A line is a saying, ending is or is-not; a line ending sized gives numbers alone. A line says is of what it
stepped. It opens no file and writes no file.
"""
from collections import Counter

N = 2_000_000
sieve = bytearray([1]) * (N + 1)
sieve[0] = sieve[1] = 0
for p in range(2, int(N ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
primes = [m for m in range(2, N + 1) if sieve[m]]
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


# A test with no prime beside the number: all numbers below it multiplied, and 1 more.
ok = True
for n in range(2, 2001):
    f = 1
    for k in range(2, n):
        f = f * k % n
    ok = ok and ((f + 1) % n == 0) == bool(sieve[n])
say("all numbers below a number multiplied, and 1 more, are at its seam with a prime alone: 2 to 2,000", ok)
# The triangle made with adding alone.
row, ok = [1, 1], True
for n in range(2, 401):
    row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    ok = ok and all(v % n == 0 for v in row[1:-1]) == bool(sieve[n])
say("in the triangle made with adding alone, a row's numbers but its two 1s are all at its seam with a prime "
    "alone: rows 2 to 400", ok)
# Shapes of primes, by a turn's places.
say(f"a pair of primes two apart past 7 begins at 11, 17 or 29 round 30: to {N:,}",
    all(p % 30 in (11, 17, 29) for p in primes if p > 7 and p + 2 <= N and sieve[p + 2]))
fours = [p for p in primes if p + 8 <= N and sieve[p + 2] and sieve[p + 6] and sieve[p + 8]]
say(f"four primes at p, 2, 6 and 8 more begin at 11 round 30 past 5, the places 11, 13, 17 and 19: {len(fours):,} to {N:,}, "
    f"5, 11, 101, 191 and on", fours[:4] == [5, 11, 101, 191] and all(p % 30 == 11 for p in fours[1:]))
say(f"three primes two apart are 3, 5 and 7 alone: to {N:,}",
    [p for p in primes if p + 4 <= N and sieve[p + 2] and sieve[p + 4]] == [3])
two = sum(1 for p in primes if p + 2 <= N and sieve[p + 2])
six = sum(1 for p in primes if p + 6 <= N and sieve[p + 6])
say("of 6's two places, both have a place 6 on and one alone has a place 2 on; pairs of primes 6 apart are "
    f"twice the pairs 2 apart, to a part in 50: {six:,} and {two:,} to {N:,}",
    all((r + 6) % 6 in (1, 5) for r in (1, 5)) and [(r + 2) % 6 in (1, 5) for r in (1, 5)] == [False, True]
    and abs(six - 2 * two) * 50 < six)
gaps = Counter(b - a for a, b in zip(primes, primes[1:]))
say(f"the stretch from a prime to its next is 6 more than any other number, to {N:,}: {gaps[6]:,} of 6, "
    f"{gaps[2]:,} of 2 and {gaps[4]:,} of 4", gaps.most_common(1)[0][0] == 6)
ends = Counter((a % 10, b % 10) for a, b in zip(primes[3:], primes[4:]))
say("a prime's ending has its own ending next less than all other endings, with all four endings: after 1, "
    f"{ends[(1, 1)]:,} of 1, {ends[(1, 3)]:,} of 3, {ends[(1, 7)]:,} of 7 and {ends[(1, 9)]:,} of 9",
    all(ends[(d, d)] < min(ends[(d, e)] for e in (1, 3, 7, 9) if e != d) for d in (1, 3, 7, 9)))
# Rows of primes with one step.
small = [p for p in primes if p < 3000]
rows3 = all((b - a) % 6 == 0 for i, a in enumerate(small) if a > 3 for b in small[i + 1:]
            if 2 * b - a < 3000 and sieve[2 * b - a])
rows5 = [(a, d) for a in small if a > 5 for d in range(2, 700, 2)
         if a + 4 * d < 3000 and all(sieve[a + k * d] for k in range(1, 5))]
say("a row of three primes with one step, past 3, has its step at 6's seam, and a row of five, past 5, at 30's: "
    f"to 3,000; 5, 11, 17, 23 and 29 has 6, and 7, 37, 67, 97, 127 and 157 has 30",
    rows3 and all(d % 30 == 0 for a, d in rows5) and all(sieve[5 + 6 * k] for k in range(5))
    and all(sieve[7 + 30 * k] for k in range(6)))
# A doubling less 1 and a number its own parts added.
M = 10_000
added = [0] * (M + 1)
for d in range(1, M + 1):
    for m in range(2 * d, M + 1, d):
        added[m] += d
say("a number its own smaller parts added is 6, 28, 496 and 8,128 alone to 10,000, each a doubling less 1 a "
    "prime, 3, 7, 31 and 127, by half the doubling",
    [m for m in range(2, M + 1) if added[m] == m] == [6, 28, 496, 8128]
    and [2 ** (q - 1) * (2 ** q - 1) for q in (2, 3, 5, 7)] == [6, 28, 496, 8128])
# The race of the two places of 4.
lead, first = 0, None
for p in primes[1:]:
    lead += 1 if p % 4 == 3 else -1
    if lead < 0:
        first = p
        break
say("of 4's two places, primes at 3 are more than primes at 1, or the same, to 26,860, and at 26,861 primes at 1 "
    "are more", first == 26861)
# Rows of stretches of stretches.
row, ok = primes[:3000], True
for _ in range(400):
    row = [abs(b - a) for a, b in zip(row, row[1:])]
    ok = ok and row[0] == 1
say("the stretches between primes, and the stretches between those, and on, begin with 1 in all rows: "
    "400 rows of the primes to 27,449", ok)

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
