# Interests in the prime numberings not among the 63 rows: breaking tests of their all-or-none cores, in named universes.
import numpy as np, math
from math import gcd, prod
N = 2_000_000
s = np.ones(N + 1, dtype=np.uint8); s[:2] = 0
for i in range(2, int(N**.5) + 1):
    if s[i]: s[i*i::i] = 0
mp = [int(x) for x in np.flatnonzero(s)]
def is_mp(n):
    if n <= N: return bool(s[n])
    if n % 2 == 0: return False
    # a strong test with the me-parities 2 to 37: whole for numbers smaller than 3.3 by 10 to the 24
    d, r = n - 1, 0
    while d % 2 == 0: d //= 2; r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % a == 0: return n == a
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
def parts(n):
    o = []; i = 2
    while i * i <= n:
        while n % i == 0: o.append(i); n //= i
        i += 1
    if n > 1: o.append(n)
    return o
def least_times(a, m):
    x, t = a % m, 1
    while x != 1: x = x * a % m; t += 1
    return t
bad = 0
# 64. the seam and 1
out = []; seam = 1
for p in mp[:12]:
    seam *= p; n = seam + 1
    ps = parts(n) if n < 10**13 else None
    out.append((p, n, "a me-parity" if is_mp(n) else ps))
    if ps and any(q <= p for q in ps): bad += 1
print("64. the seam and 1:", out[:8])
# 65. a me-parity at the -1 of a seam of 4 with its double and 1 a me-parity
sg = [p for p in mp if p % 4 == 3 and p < 3000 and is_mp(2 * p + 1)]
if any((pow(2, p, 2 * p + 1) != 1) for p in sg): bad += 1
other = [p for p in mp if p % 4 == 1 and p < 3000 and is_mp(2 * p + 1)]
if any((pow(2, p, 2 * p + 1) != 2 * p) for p in other): bad += 1
print("65. me-parities to 3,000 at the -1 of a seam of 4 with the double and 1 a me-parity:", sg[:10], "...", len(sg), "; 2 by itself that many times at place 1 round the double and 1 at all; at the +1 of a seam of 4:", other[:6], ": at the -1 at all")
# 66. the +1 of 2 by itself (1 doubled some times) times, and 3
for n in range(1, 9):
    F = 2**(2**n) + 1
    t = pow(3, (F - 1) // 2, F) == F - 1
    truth = n <= 4
    if n <= 6 and t != (is_mp(F) if F < 3 * 10**24 else truth): bad += 1
    if n <= 8 and t != truth: bad += 1
print("66. the times 2, 4, 8, 16, 32, 64, 128, 256: 3 by itself the middle's number of times at the -1:", [pow(3, (2**(2**n)) // 2, 2**(2**n) + 1) == 2**(2**n) for n in range(1, 9)])
# 67. a new me-parity at all numbers of doublings but 6
none_new = []
for n in range(2, 1201):
    M = 2**n - 1
    for m in range(1, n):
        if n % m == 0:
            g = gcd(M, 2**m - 1)
            while g > 1: M //= g; g = gcd(M, 2**m - 1)
    if M == 1: none_new.append(n)
print("67. the numbers of doublings 2 to 1,200 with no new me-parity crossing the -1:", none_new)
# 68. the parts of one in doublings
def spiral2(p):
    out = []; r = 1
    for _ in range(least_times(2, p)):
        r *= 2; out.append(r // p); r %= p
    return out
for p in mp[1:200]:
    L = least_times(2, p); sp = spiral2(p)
    if L % 2 == 0:
        h = L // 2
        if any(sp[i] + sp[i + h] != 1 for i in range(h)): bad += 1
        if pow(2, h, p) != p - 1: bad += 1
print("68. 1 over 7, 11, 13 and 19 in doublings:", ["".join(map(str, spiral2(p))) for p in (7, 11, 13, 19)])
# 69. the Fibonacci numbers and the me-parities
F = [0, 1]
while len(F) < 3000: F.append(F[-1] + F[-2])
for p in mp[3:300]:
    k = p - 1 if p % 5 in (1, 4) else p + 1
    if F[k] % p: bad += 1
for a in range(3, 40):
    for b in range(2, 12):
        if F[a * b] % F[a]: bad += 1
fibmp = [n for n in range(3, 140) if is_mp(F[n])]
if any((not is_mp(n)) and n != 4 for n in fibmp): bad += 1
print("69. the numbers 3 to 139 with the Fibonacci number a me-parity:", fibmp, "; 5 crosses the 5th:", F[5], "; 7 crosses the 8th:", F[8], "; 11 crosses the 10th:", F[10], "; 13 crosses the 14th:", F[14])
# 70. the numbers 1 to the -1 multiplied, at the -1 round the me again
wil = []; f = 1; prev = 1
for p in mp:
    if p > 20000: break
    for k in range(prev + 1, p): f = f * k % (p * p * 1) if False else f
    prev = prev
wil = []
for p in mp:
    if p > 3000: break
    f = 1
    for k in range(2, p): f = f * k % (p * p)
    if (f + 1) % (p * p) == 0: wil.append(p)
print("70. me-parities to 3,000 with the numbers 1 to the -1 multiplied at the -1 round the me again:", wil)
# 72. the parts of one of the numbers with all me-parity parts to an opener, added
from fractions import Fraction
for ops in ((2,), (2, 3), (2, 3, 5)):
    whole = prod(Fraction(p, p - 1) for p in ops)
    part = Fraction(0); lim = 10**6
    nums = [1]
    for p in ops:
        nums = [n * p**k for n in nums for k in range(0, 40) if n * p**k <= lim]
    part = sum(Fraction(1, n) for n in nums)
    print(f"72. openers {ops}: the product {whole}; the parts of one of the {len(nums)} such numbers to 1,000,000, added: {float(part):.6f}")
    if part > whole: bad += 1
print("is-nots:", bad)
