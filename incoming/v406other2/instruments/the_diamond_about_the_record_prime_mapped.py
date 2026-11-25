#!/usr/bin/env python3
"""The diamond about the world's record prime, mapped: the 1 to 5, the 1 to 9 and the 1 to 17 with the record
their middle, a number with the lowest spiral crossing it.

Usage:  python3 -I incoming/v406other2/instruments/the_diamond_about_the_record_prime_mapped.py

The record is 2 doubled 136,279,841 times less 1, and is never written out: a spiral of q selves crosses the
record and g more with 2 doubled round q, less 1, and g more, at q's seam. Spirals of 2 to 2,000,000 selves
are stepped. The record's own test is a field's, of 2024, and is not stepped here. A line ends is or
is-not; a line ending sized gives numbers alone. It opens no file and writes no file.
"""
P = 136_279_841
SPIRALS = 2_000_000
sieve = bytearray([1]) * (SPIRALS + 1)
sieve[0] = sieve[1] = 0
for p in range(2, int(SPIRALS ** 0.5) + 1):
    if sieve[p]:
        sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
record = [(q, (pow(2, P, q) - 1) % q) for q in range(2, SPIRALS + 1) if sieve[q]]
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


def lowest(g):
    """the lowest spiral of 2 to 2,000,000 selves at its seam with the record and g more, or none"""
    for q, r in record:
        if (r + g) % q == 0:
            return q
    return None


say("no spiral of 2 to 2,000,000 selves crosses the record", lowest(0) is None)
crossing = {g: lowest(g) for g in range(-40, 41) if g}
for name, half in (("1 to 5", 2), ("1 to 9", 4), ("1 to 17", 8)):
    row = ", ".join(f"{g:+d} by {crossing[g]:,}" for g in range(-half, half + 1) if g)
    say(f"in the {name} about the record, the record its middle, all other numbers are crossed: {row}",
        all(crossing[g] for g in range(-half, half + 1) if g))
below = next(g for g in range(1, 100_000) if lowest(-g) is None)
above = next(g for g in range(1, 100_000) if lowest(g) is None)
say(f"all numbers from {below - 1} below the record to {above - 1} above it are crossed but the record: "
    f"it is the one prime of {below + above - 1} numbers in a row; {below} below and {above} above are the "
    f"nearest not crossed by these spirals, and are not tested", "sized")
say("round 4, 8 and 16 the record is 3, 7 and 15, one less than the surface, and round 5, 9 and 17 it is 1, 4 and 1",
    [(pow(2, P, n) - 1) % n for n in (4, 8, 16, 5, 9, 17)] == [3, 7, 15, 1, 4, 1])

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
