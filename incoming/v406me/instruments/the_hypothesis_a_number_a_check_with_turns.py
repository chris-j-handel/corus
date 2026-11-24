"""The hypothesis as a saying of whole numbers and fractions alone, a number a check, all or none: a field's, by
Davis, Matiyasevich and Robinson, 1976, said here with turns. It goes through no file and writes nothing.

    python3 -I incoming/v406me/instruments/the_hypothesis_a_number_a_check_with_turns.py [8]

A turn of the spirals of 1 to m selves is the least number all of 1 to m are parts of: 1, 2, 6, 12, 60, 60, 420.
Its building: a number that is a prime multiplied by itself brings that prime once, and no other number brings a thing.
The turns of 1, of 1 to 2, and on to 1 to n less 1, multiplied, are d. The unit fractions 1/1, 1/2 and on to 1/d are summed.
A field's saying: the hypothesis is, with all numbers n, that sum less n by n halved, multiplied by its own, short of
36 by n by n by n. A number is a check. No smooth curve, no logarithm, no decimal, and no surface it is from.
With 8 it steps n of 8 too, 217,728,000 unit fractions, by whole numbers bounding the sum from both sides.
"""
import sys
from fractions import Fraction
from math import gcd

def brings(j):
    """the prime a number brings: its prime, with j a prime multiplied by itself; 1 with all other numbers"""
    for p in range(2, j + 1):
        if j % p == 0:
            while j % p == 0:
                j //= p
            return p if j == 1 else 1
    return 1

def turn(m):
    t = 1
    for j in range(1, m + 1):
        t *= brings(j)
    return t

top = 8 if len(sys.argv) > 1 and sys.argv[1] == "8" else 7
ok = True
print("the turns of 1 to m selves, m of 1 to 9:", [turn(m) for m in range(1, 10)])
least = 1
for m in range(1, 10):
    least = least * m // gcd(least, m)
    ok &= turn(m) == least
print("   a turn is the least number all of 1 to m are parts of:", "is" if ok else "is-not")
d = 1
for n in range(1, top + 1):
    if n > 1:
        d *= turn(n - 1)
    if d <= 10000:
        s = sum(Fraction(1, k) for k in range(1, d + 1))
        gap = (s - Fraction(n * n, 2)) ** 2
        fits = gap < 36 * n ** 3
        whole = lambda q: f"{q.numerator}" if q.denominator == 1 else f"{q.numerator // q.denominator} and a fraction"
        said = f"the sum is {whole(s)}; its parting from {n * n}/2, multiplied by its own, is {whole(gap)}"
    else:
        S = 10 ** 15                                   # whole numbers alone: S/k cut to a whole number is short of S/k by under 1
        lo = sum(S // k for k in range(1, d + 1)); hi = lo + d
        a, b = 2 * lo - n * n * S, 2 * hi - n * n * S   # twice the parting, by S, from both sides
        worst = max(a * a, b * b)
        fits = worst < 144 * n ** 3 * S * S
        said = f"the sum is from {lo // S} and a fraction, bounded from both sides by whole numbers; its parting multiplied by its own is at most {worst // (4 * S * S) + 1}"
    ok &= fits
    print(f"n {n}: d {d:,}; {said}; short of {36 * n ** 3:,}: {'is' if fits else 'is-not'}")
print("All is, of the numbers stepped." if ok else "A breaking.")
