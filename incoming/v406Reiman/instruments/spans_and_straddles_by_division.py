"""Spans and straddles, by division. No resolver is in this page.

A field's arithmetic, executed for the window's own numbers: a prime in a
doubling span, all or none, and the two numbers beside a product of primes,
one less and one more. By a partner's word of 22 November no average and no
measuring is in it: an average is no thing of nature.

    python3 -I incoming/v406Reiman/instruments/spans_and_straddles_by_division.py
"""
import math
import random
import sys


def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(range(i * i, n + 1, i)))
    return s


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def rho(n, rng):
    if n % 2 == 0:
        return 2
    while True:
        c, y, m, g, r, q = rng.randrange(1, n), rng.randrange(1, n), 128, 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = math.gcd(q, n)
                k += m
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = math.gcd(abs(x - ys), n)
        if g != n:
            return g


def factors(n, rng):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    d = rho(n, rng)
    return sorted(factors(d, rng) + factors(n // d, rng))


if __name__ == "__main__":
    rng = random.Random(17)
    top = 2 ** 27 + 1
    s = sieve(top)
    print("A doubling span, all or none")
    spans_all = all(any(s[2 ** k + 1 : 2 ** (k + 1) + 2]) for k in range(1, 27))
    print("   a prime in all the doubling spans to 2^27 + 1:", "is" if spans_all else "is-not")
    print()
    print("One less and one more than the product of the primes to a prime")
    primes = [p for p in range(2, 40) if s[p]]
    waist = 1
    for p in primes:
        waist *= p
        if p in (3, 5, 7, 11, 13, 17, 19, 37):
            less, more = factors(waist - 1, rng), factors(waist + 1, rng)
            apart = not (set(less) & set(more)) and all(f > p for f in less + more)
            print(f"   {waist:,} (to {p}) · less: {' × '.join(f'{f:,}' for f in less)} · more: {' × '.join(f'{f:,}' for f in more)} · no prime of the product, and none of both: {'is' if apart else 'is-not'}")
    print()
    print("The same from the primes a product itself opened, by no order of size")
    opened, waist = [2], 2
    for stepn in range(1, 6):
        less, more = factors(waist - 1, rng), factors(waist + 1, rng)
        digits = len(str(waist))
        print(f"   {stepn} · a product of {digits} digit{'s' if digits > 1 else ''} · less: {', '.join(f'{f:,}' for f in less) or 'none'} · more: {', '.join(f'{f:,}' for f in more)}")
        new = [f for f in less + more if f not in opened]
        opened += new
        for f in new:
            waist *= f
    missing = [p for p in primes if p not in opened]
    print("   primes to 37 opened by none of the five:", ", ".join(str(p) for p in missing))
