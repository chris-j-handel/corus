#!/usr/bin/env python3
"""A number's cone and its podal pairs of primes: executed with whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/a_number_s_cone_and_its_podal_pairs_of_primes_executed.py

A number n's cone forward is n to 2n, and its podal pair is n less k with n and k more, the same below as
above. A line is a saying, ending is or is-not; a line ending sized gives numbers alone. Nothing is decided:
a line says is of what it stepped. It opens no file and writes no file.
"""
N = 200_000
sieve = bytearray([1]) * (2 * N + 1)
sieve[0] = sieve[1] = 0
for p in range(2, int((2 * N) ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


def pairs(n):
    return [(n - k, n + k) for k in range(0, n - 1) if sieve[n - k] and sieve[n + k]]


stair = [0] * (2 * N + 1)
for m in range(1, 2 * N + 1):
    stair[m] = stair[m - 1] + sieve[m]
say(f"a number has a prime in its cone forward, past it and to its double: 2 to {N:,}",
    all(stair[2 * n] - stair[n] >= 1 for n in range(2, N + 1)))
least, far, at = [], 0, 0
ok = True
for n in range(2, N + 1):
    k = 0
    while k < n - 1 and not (sieve[n - k] and sieve[n + k]):
        k += 1
    if k >= n - 1:
        ok = False
        break
    if k > far:
        far, at = k, n
say(f"a number is the middle of a podal pair of primes, the same below it as above: 2 to {N:,}", ok)
say(f"the farthest a number's nearest pair is from it, 2 to {N:,}, is {far:,}, about {at:,}", "sized")
say("a prime is its own podal pair, the same below as above by none: 2 to 2,000",
    all(pairs(p)[0] == (p, p) for p in range(2, 2001) if sieve[p]))
say("about 15 the podal pairs of primes are 13 with 17, 11 with 19 and 7 with 23: the six places of 30 past 1 "
    "and 29", pairs(15) == [(13, 17), (11, 19), (7, 23)])
say("about 30 they are six, 29 with 31, 23 with 37, 19 with 41, 17 with 43, 13 with 47 and 7 with 53; "
    "11 has 49, 7 by 7", pairs(30) == [(29, 31), (23, 37), (19, 41), (17, 43), (13, 47), (7, 53)])
say(f"about 60 they are {len(pairs(60))}, and about 120, {len(pairs(120))}; about 64, {len(pairs(64))}", "sized")
say("a number's pair has one prime below it and one in its cone forward, a prime born past it: 4 to 2,000, "
    "all numbers no prime", all(all(a < n < b <= 2 * n for a, b in pairs(n)) for n in range(4, 2001) if not sieve[n]))


# Adding 1 and multiplying: a prime born with adding 1, and the plus ones and less ones of the seams of 6.
say(f"a prime past 3 is one less or one more than a seam of 6, a podal pair about the seam: to {2 * N:,}",
    all(m % 6 in (1, 5) for m in range(5, 2 * N + 1) if sieve[m]))
ones = [m for m in range(5, 2 * N + 1) if m % 6 in (1, 5)]
say(f"one less and one more than the seams of 6, to {2 * N:,}, are {len(ones):,} numbers, and {sum(sieve[m] for m in ones):,} "
    f"of them are primes; the lowest no prime are {', '.join(str(m) for m in ones if not sieve[m])[:14]}", "sized")
say("one less or one more than a seam of 6 is no prime at 25, 35, 49 and 55, 5 by 5, 5 by 7, 7 by 7 and 5 by 11",
    [m for m in ones if not sieve[m]][:4] == [25, 35, 49, 55])


def lowest(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return d
        d += 1
    return n


turn, rows = 1, []
for q in (2, 3, 5, 7, 11, 13):
    turn *= q
    rows.append((turn, lowest(turn - 1), lowest(turn + 1), q))
say("a turn's primes multiplied are crossed by them alone, and one less and one more are crossed by none of them, "
    "their lowest parts all past the turn's primes: the turns of 2 to 30,030",
    all(lo > q and hi > q for t, lo, hi, q in rows[1:]))
say("one less and one more than the turns 6, 30 and 2,310 are primes, 5 and 7, 29 and 31, 2,309 and 2,311; "
    "209 is 11 by 19 and 30,031 is 59 by 509, primes born past their turns",
    [(t, lo == t - 1, hi == t + 1) for t, lo, hi, q in rows[1:]]
    == [(6, True, True), (30, True, True), (210, False, True), (2310, True, True), (30030, True, False)]
    and 209 == 11 * 19 and 30031 == 59 * 509)

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
