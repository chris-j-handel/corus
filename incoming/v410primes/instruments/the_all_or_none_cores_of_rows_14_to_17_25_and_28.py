# Breaking tests of the all-or-none cores of rows 14, 15, 16, 17, 25 and 28, in named universes. Proving nothing past the numbers gone through.
import numpy as np
def is_mp(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True
def parts_mp(n):
    out = []; i = 2
    while i * i <= n:
        while n % i == 0: out.append(i); n //= i
        i += 1
    if n > 1: out.append(n)
    return out
def least_times(a, m):
    x, t = a % m, 1
    while x != 1: x = x * a % m; t += 1
    return t
bad = 0
# row 14
for a in range(2, 13):
    for b in range(2, 13):
        if (2**(a*b) - 1) % (2**a - 1): bad += 1
r14 = [n for n in range(2, 62) if is_mp(2**n - 1)]
if any(not is_mp(n) for n in r14): bad += 1
print("row 14: the times with the -1 of 2 by itself that many times a me-parity, 2 to 61:", r14)
for p in (11, 23, 29, 37, 41, 43, 47, 53):
    q = parts_mp(2**p - 1)
    if any((x - 1) % (2 * p) for x in q): bad += 1
    if p in (11, 23, 29): print(f"   the times {p}: {2**p - 1} is", " by ".join(map(str, q)), "; the parts at the +1 of a crossing of", 2*p, ":", [(x - 1) // (2*p) for x in q])
# row 15
N = 10**7
sig = np.zeros(N + 1, dtype=np.int64)
for d in range(1, N + 1):
    sig[d::d] += d
perfect = [int(x) for x in np.flatnonzero(sig[1:] == 2 * np.arange(1, N + 1)) + 1]
print("row 15: numbers to", N, "with parts adding to the double:", perfect)
for p in (2, 3, 5, 7, 13):
    M = 2**p - 1; n = M * 2**(p - 1)
    if not is_mp(M): bad += 1
    if p <= 7 and n not in perfect: bad += 1
# row 16
r16 = [m for m in range(1, 65) if is_mp(2**m + 1)] if True else []
print("row 16: the times 1 to 40 with the +1 of 2 by itself that many times a me-parity:", [m for m in range(1, 41) if is_mp(2**m + 1)])
for a in range(1, 9):
    for b in (3, 5, 7):
        if (2**(a*b) + 1) % (2**a + 1): bad += 1
F5 = 2**32 + 1; print("   the times 32:", F5, "is 641 by", F5 // 641, "; same:", F5 == 641 * 6700417, "; 641 less 1 over 64:", 640 // 64, "; 6700417 less 1 over 64:", (6700417 - 1) / 64)
F6 = 2**64 + 1; print("   the times 64:", F6 % 274177 == 0, "; 274177 less 1 over 128:", (274177 - 1) / 128)
# row 17
same = []
for p in range(3, 4000, 2):
    if not is_mp(p): continue
    d = least_times(2, p); e = least_times(2, p * p)
    if e not in (d, d * p): bad += 1
    if e == d: same.append(p)
print("row 17: odd me-parities to 4,000 with the least times of 2 the same round the me-parity and round its me again:", same, "; round 9:", least_times(2, 9), "; round 49:", least_times(2, 49), "; round 1093:", least_times(2, 1093))
# rows 25 and 28, round 4
for n in range(1, 3000):
    for q in set(parts_mp(n * n + 1)):
        if q != 2 and q % 4 != 1: bad += 1
print("rows 25 and 28: the me-parity parts of the +1 of a me again, the numbers 1 to 2,999: 2, or at the +1 of a seam of 4: is-nots counted below")
print("   4 by 3 less 1:", 11, is_mp(11), "; 4 by 3 by 7 by 11, less 1:", 4*231 - 1, parts_mp(4*231 - 1), "; 10 by 10 and 1:", 101, is_mp(101), "; 130 by 130 and 1:", 130*130 + 1, parts_mp(130*130 + 1))
print("is-nots:", bad)
