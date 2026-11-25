"""v407nanding · a prime round 24 and round 60: back to 1 in two multiplyings, and in four, executed with whole numbers.

Usage, from the repository's root:
  python3 -I incoming/v407nanding/instruments/a_prime_round_24_and_round_60_check.py .

A partner's saying of 24 November: one prime twisting looping into and out of 24, 4 other-thans, not two; the small
direction 0-24 and the large direction of natural torusing stable form 24-60. A number round n is what is past n's
seams. A prime's round is its places by multiplying by itself, round n, to 1 again. All or none.
"""
import sys

HORIZON = 1_000_000
sieve = bytearray([1]) * (HORIZON + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(HORIZON ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
primes = [n for n in range(HORIZON + 1) if sieve[n]]
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def round_of(p, n):
    out, x = [p % n], p % n
    while True:
        x = x * p % n
        if x == p % n:
            return out
        out.append(x)


say("T1. A cube of 3 has 24 about its line, and a cube of 4 has 60: 24 is 2 by 3 by 4, and 60 is 3 by 4 by 5, three in a row",
    27 - 3 == 24 == 2 * 3 * 4 and 64 - 4 == 60 == 3 * 4 * 5)
past3 = [p for p in primes if p > 3]
say(f"T2. Round 24, a prime past 3 is back at 1 in two multiplyings, all {len(past3):,} of them to {HORIZON:,} (stepped)",
    all(p * p % 24 == 1 for p in past3))
say("T3. Round 24, the primes past 3 are at eight places, 1, 5, 7, 11, 13, 17, 19 and 23, and a place's round is two or one",
    sorted({p % 24 for p in past3}) == [1, 5, 7, 11, 13, 17, 19, 23] and all(len(round_of(r, 24)) <= 2 for r in (1, 5, 7, 11, 13, 17, 19, 23)))
past5 = [p for p in primes if p > 5]
say(f"T4. Round 60, a prime past 5 is back at 1 in four multiplyings, all {len(past5):,} of them to {HORIZON:,} (stepped)",
    all(pow(p, 4, 60) == 1 for p in past5))
four = [p for p in past5 if p * p % 60 != 1]
two = [p for p in past5 if p * p % 60 == 1]
say("T5. Round 60, a prime past 5 is back in two with one more or one less than a number of fives, and in four, a round of "
    f"four places, with two or three more: {len(two):,} and {len(four):,} of them (stepped)",
    all(p % 5 in (1, 4) for p in two) and all(p % 5 in (2, 3) and len(round_of(p, 60)) == 4 for p in four))
say("T6. 7 round 24 is 7 and 1, a round of two; 7 round 60 is 7, 49, 43 and 1, a round of four",
    round_of(7, 24) == [7, 1] and round_of(7, 60) == [7, 49, 43, 1])
say("M1. Round 60 in two multiplyings alone, the primes past 5 are not all back at 1, and T4's four is needed",
    not all(p * p % 60 == 1 for p in past5))
print("\nAll is." if all(results) else "\nNot all is.")
