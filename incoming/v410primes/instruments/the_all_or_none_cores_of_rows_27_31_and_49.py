# Breaking tests of the all-or-none cores of rows 27, 31 and 49, in named universes.
import numpy as np, math
N = 200000
s = np.ones(N + 1, dtype=np.uint8); s[:2] = 0
for i in range(2, int(N**.5) + 1):
    if s[i]: s[i*i::i] = 0
mp = [int(x) for x in np.flatnonzero(s)]
bad = 0
# row 31: a between with me-parities at its -1 and its +1
bet = [p + 1 for p in mp if p + 2 <= N and s[p + 2]]
if any(b % 6 for b in bet if b > 4): bad += 1
places30 = sorted(set(b % 30 for b in bet if b > 6))
print("row 31: betweens to", N, ":", len(bet), "; past 4 all crossings of 6:", all(b % 6 == 0 for b in bet if b > 4), "; past 6, the places round 30:", places30)
# the two all-or-none conditions: the numbers 1 to the number's -1 multiplied at the -1 round the number; the double of the same at the -1 round the number 2 on
both = []
f = 1                                      # the numbers 1 to n - 1 multiplied
for n in range(2, 1500):
    f *= (n - 1) if n > 2 else 1
    c1 = (f + 1) % n == 0
    c2 = (2 * f + 1) % (n + 2) == 0
    truth = bool(s[n]) and bool(s[n + 2])
    if (c1 and c2) != truth and n % 2 == 1: bad += 1
    if bool(s[n]) != c1: bad += 1
    if n % 2 == 1 and bool(s[n + 2]) != c2: bad += 1
    if c1 and c2 and n % 2 == 1: both.append(n)
print("   odd numbers 3 to 1,499 with both: the lower me-parities of the pairs:", both[:12], "...", len(both))
# row 27: me-parities in a row, the same step
S = set(mp); rows = 0
for n in (3, 4, 5, 6, 7):
    small = [r for r in mp if r <= n]
    for a in mp:
        if a > 3000: break
        for d in range(2, 1200, 2):
            if a + (n - 1) * d > N: break
            if all((a + k * d) in S for k in range(n)):
                rows += 1
                for r in small:
                    if d % r and r not in [a + k * d for k in range(n)]: bad += 1
print("row 27: rows of 3 to 7 me-parities with the same step gone through:", rows, "; 5, 11, 17, 23, 29: step 6; 7, 37, 67, 97, 127, 157: step 30;", all(x in S for x in (7, 37, 67, 97, 127, 157)))
print("   199 and 210 on, 10 me-parities:", all((199 + 210 * k) in S for k in range(10)))
# row 49: the all-parity of a number, and of its parts added
M = 100000
lam = np.ones(M + 1, dtype=np.int64)
for p in mp:
    if p > M: break
    q = p
    while q <= M:
        lam[q::q] *= -1; q *= p
tot = np.zeros(M + 1, dtype=np.int64)
for d in range(1, M + 1):
    tot[d::d] += lam[d]
sq = np.zeros(M + 1, dtype=np.int64); sq[[i * i for i in range(1, int(M**.5) + 1)]] = 1
if not np.array_equal(tot[1:], sq[1:]): bad += 1
for n in (10, 17, 100, 99999, 100000):
    if sum(int(lam[d]) * (n // d) for d in range(1, n + 1)) != math.isqrt(n): bad += 1
print("row 49: the all-parity of a number's parts added, 1 to", M, ": 1 at the me agains and 0 at all other numbers:", np.array_equal(tot[1:], sq[1:]), "; the parts of 12:", [(d, int(lam[d])) for d in (1, 2, 3, 4, 6, 12)], "; of 36:", sum(int(lam[d]) for d in (1, 2, 3, 4, 6, 9, 12, 18, 36)))
print("is-nots:", bad)
