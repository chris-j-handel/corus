#!/usr/bin/env python3
"""The walk of the primes from 2, with nand alone: a prime after a prime, tested by the primes walked.

Usage:  python3 -I incoming/v406other2/instruments/the_walk_of_the_primes_with_nand_alone_executed.py

One cell is in it, nand of two bits. Adding, multiplying, a number round a number, and comparing are that
cell wired, and no other cell. A number is 12 bits. The walk: a number n is a prime with a number coming to
1 again round n with n less 1 multiplyings and no fewer, the fewer named by the primes walked that are
parts of n less 1. The number of multiplyings is numbered by the walk. A line ends is or is-not; a line
ending sized gives numbers alone. It opens no file and writes no file.
"""
W = 12
calls = [0]
HORIZON = 61


def nand(a, b):
    calls[0] += 1
    return 1 - (a & b)


def inv(a):
    return nand(a, a)


def both(a, b):
    return inv(nand(a, b))


def either(a, b):
    return nand(inv(a), inv(b))


def other(a, b):
    t = nand(a, b)
    return nand(nand(a, t), nand(b, t))


def choose(s, x, y):
    n = inv(s)
    return [nand(nand(s, a), nand(n, b)) for a, b in zip(x, y)]


def bits(n):
    return [(n >> i) & 1 for i in range(W)]


def add(x, y, carry=0):
    out = []
    for a, b in zip(x, y):
        t = other(a, b)
        out.append(other(t, carry))
        carry = either(both(a, b), both(t, carry))
    return out, carry


def less(x, y):
    """x less y, and 1 with x at or past y"""
    return add(x, [inv(b) for b in y], 1)


def shift(x, k):
    return ([0] * k + x)[:W]


def times(x, y):
    acc = bits(0)
    for i in range(W // 2):
        total, _ = add(acc, shift(x, i))
        acc = choose(y[i], total, acc)
    return acc


def round_(x, n):
    """x round n: what is left of x past n's seams"""
    for k in range(W // 2 - 1, -1, -1):
        d, at_or_past = less(x, shift(n, k))
        x = choose(at_or_past, d, x)
    return x


def same(x, y):
    r = 1
    for a, b in zip(x, y):
        r = both(r, inv(other(a, b)))
    return r


def power(a, e, n):
    result, base = bits(1), round_(a, n)
    while e:
        if e & 1:
            result = round_(times(result, base), n)
        base = round_(times(base, base), n)
        e >>= 1
    return result


ONE, NONE = bits(1), bits(0)
walked = [2]
trees = {2: []}
for n in range(3, HORIZON + 1):
    nb = bits(n)
    qs = [q for q in walked if same(round_(bits(n - 1), bits(q)), NONE)]
    for a in range(2, n):
        ab = bits(a)
        if same(power(ab, n - 1, nb), ONE) and not any(same(power(ab, (n - 1) // q, nb), ONE) for q in qs):
            walked.append(n)
            trees[n] = qs
            break

plain = [n for n in range(2, HORIZON + 1) if all(n % d for d in range(2, n))]
out = [("is" if walked == plain else "is-not",
        f"the walk from 2 with nand alone finds the primes to {HORIZON}, a prime tested by the primes walked: "
        + ", ".join(str(p) for p in walked))]
reached = all(n in walked or any(same(round_(bits(n), bits(q)), NONE) for q in walked if q < n)
              for n in range(2, HORIZON + 1))
out.append(("is" if reached else "is-not",
            f"a number of 2 to {HORIZON} is a prime walked or has a prime walked as a part: no number is passed over"))
out.append(("is" if all(all(q in walked and q < n for q in qs) for n, qs in trees.items()) else "is-not",
            "a prime's test is of primes walked ahead of it alone"))
out.append(("sized", f"nand is at its two bits {calls[0]:,} times in the walk, and no other cell is in it"))
for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
