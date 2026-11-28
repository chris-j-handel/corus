# v408primes · whole reasons laid in the session's sentences, a row at a time, the sentences of
# The_whole_reasons_laid.md. A whole reason is sequential logic, a self to its other-than closing, at all numbers;
# the instrument proves its logical steps as steps, and its sentences in the cone's sections beside them.
# Row 30: between a number and its double, a me-parity, at all numbers. Whole numbers.
# Execute: python3 -I whole_reasons_laid.py
from math import comb, isqrt, log
import numpy as np

results = []
def say(s, ok):
    results.append(bool(ok)); print(("is     " if ok else "is-not ") + s)

V = 1000000
S = np.ones(2 * V + 1, bool); S[:2] = False
for p in range(2, isqrt(2 * V) + 1):
    if S[p]: S[p * p::p] = False
PR = np.nonzero(S)[0]

# 1, 2 · the 2n-th row of the triangle and its middle M
say("30.1 · the 2n-th row of the triangle has 2n + 1 numbers, together 4 to the n: a row is its prior doubled, sequential logic (rows to 4,000 shown)",
    all(sum(comb(2 * n, k) for k in range(2 * n + 1)) == 4 ** n for n in range(0, 2001, 37)))
say("30.2 · its middle M is the largest of its 2n + 1 numbers: M is at least 4 to the n over 2n + 1 (n to 3,000 shown)",
    all(comb(2 * n, n) == max(comb(2 * n, k) for k in range(2 * n + 1)) and comb(2 * n, n) * (2 * n + 1) >= 4 ** n for n in range(1, 3001, 41)))
# 3, 4, 5 · a me-parity's power in M
def power_in_M(p, n):                       # the selves to 2n crossed by p, by p by p, and on, less the same twice to n
    e, q = 0, p
    while q <= 2 * n:
        e += (2 * n) // q - 2 * (n // q); q *= p
    return e
def power_of(p, m):
    e = 0
    while m % p == 0: m //= p; e += 1
    return e
ok = all(power_in_M(p, n) == power_of(p, comb(2 * n, n)) for n in range(1, 401) for p in PR[PR <= 2 * n].tolist())
say("30.3, 30.4 · M is the numbers to 2n multiplied over those to n multiplied twice; a me-parity's power in it is its crossings of the selves to 2n by p, by p by p and on, less those to n twice (n to 400, all me-parities)", ok)
ok = all(p ** power_in_M(p, n) <= 2 * n for n in range(1, 3001) for p in PR[PR <= 2 * n].tolist()[:60])
say("30.5 · a me-parity's part of M is at most 2n: all of p's powers to 2n give at most 1, a power at a time (n to 3,000; the step 2n // q less twice n // q is 0 or 1, at all n)",
    ok and all((2 * n) // q - 2 * (n // q) in (0, 1) for n in range(1, 3001) for q in range(2, 2 * n + 1, 7)))
ok6 = ok7 = True
for n in range(3, 3001):
    for p in PR[PR <= 2 * n].tolist():
        e = power_in_M(p, n)
        if p * p > 2 * n: ok6 &= e <= 1
        if 3 * p > 2 * n and p <= n: ok7 &= e == 0
say("30.6 · a me-parity past the side of 2n is in M once at most (n to 3,000, and at all n: its me again is past 2n)", ok6)
say("30.7 · a me-parity past two-thirds of n's double and to n is in M at none: it crosses the selves to 2n twice and those to n once, twice over (n from 3 to 3,000, and at all n)", ok7)
# 8 · the me-parities to x multiplied, less than 4 to the x
prod, ok, j = 1, True, 0
for x in range(1, 20001):
    if S[x]: prod *= x
    ok &= prod < 4 ** x if x % 97 == 0 or x < 200 else True
mid = all(comb(2 * m + 1, m) < 4 ** m and all(comb(2 * m + 1, m) % p == 0 for p in PR[(PR >= m + 2) & (PR <= 2 * m + 1)].tolist()) for m in range(1, 1500, 13))
say("30.8 · the me-parities to any x multiplied are less than 4 to the x, by sequential logic: the middle of the (2m + 1)-th row is crossed by all me-parities from m + 2 to 2m + 1 and is less than 4 to the m (x to 20,000 and m to 1,500 shown)",
    ok and mid)
# 9, 10, 11 · is-not a me-parity between n and 2n: M other-than itself from 468 on
def f(n): return (n / 3) * log(4) - log(2 * n + 1) - (2 * n) ** 0.5 * log(2 * n)
def fp(n): return log(4) / 3 - 2 / (2 * n + 1) - (log(2 * n) + 2) / (2 * n) ** 0.5
grows = all(-log(y) / (2 * y ** 1.5) < 0 for y in (936.0, 1e4, 1e8, 1e16))   # (ln y + 2) / side of y falls past y = 1
say("30.9, 30.10, 30.11 · with no me-parity between n and 2n, M is the me-parities to 2n / 3 only, at most 2n to the side of 2n by 4 to two-thirds of 2n; from 468 on, 4 to the n over 2n + 1 is more: M other-than itself (f(468) = %.3f, f's rate at 468 = %.3f, its rate rising past it)" % (f(468), fp(468)),
    f(468) > 0 and fp(468) > 0 and grows and all(f(n) > 0 for n in range(468, 100001)))
exact = all(4 ** n > (2 * n + 1) * (2 * n) ** isqrt(2 * n) * 4 ** ((2 * n) // 3 + 1) for n in range(1500, 5001, 97))
say("30.11 · the same in whole numbers, with the side and two-thirds whole: 4 to the n past (2n + 1) by 2n to its side by 4 to two-thirds of 2n and 1 (n from 1,500 to 5,000 shown)", exact)
# 12 · below 468, the chain
chain = [2, 3, 5, 7, 13, 23, 43, 83, 163, 317, 631]
say("30.12 · below 468, the chain %s, all me-parities, all before their prior's double, place a me-parity between n and 2n" % chain,
    all(S[c] for c in chain) and all(b < 2 * a for a, b in zip(chain, chain[1:])) and all(any(n < c <= 2 * n for c in chain) for n in range(1, 468)))
# 13 · the whole
C = np.cumsum(S)
say("30.13 · between any number and its double, a me-parity: at all numbers, by the whole reason; and in the cone's section 1 to 1,000,000, all",
    bool(np.all(C[2 * np.arange(1, V + 1)] - C[np.arange(1, V + 1)] >= 1)))

print("All is." if all(results) else "A line is-not.")
