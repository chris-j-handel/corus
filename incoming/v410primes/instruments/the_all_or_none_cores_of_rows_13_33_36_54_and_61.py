# Breaking tests of the all-or-none cores of rows 13, 33, 36, 54 and 61, in named universes.
import numpy as np
from math import prod
N = 1_000_000
s = np.ones(N + 1, dtype=np.uint8); s[:2] = 0
for i in range(2, int(N**.5) + 1):
    if s[i]: s[i*i::i] = 0
mp = [int(x) for x in np.flatnonzero(s)]
bad = 0
def least_times(a, m):
    x, t = a % m, 1
    while x != 1: x = x * a % m; t += 1
    return t
# rows 13, 14 and 24: 2 round 8
most = []
for p in mp[1:400]:
    m = (p - 1) // 2
    sq = {(c * c) % p for c in range(1, p)}
    two_sq = 2 in sq
    if two_sq != (p % 8 in (1, 7)): bad += 1
    odd_to_m = (m + 1) // 2
    if pow(2, m, p) != (1 if odd_to_m % 2 == 0 else p - 1): bad += 1
    lt = least_times(2, p)
    if lt == p - 1:
        most.append(p)
        if two_sq: bad += 1
    if any(least_times(c, p) == p - 1 for c in list(sq)[:40]): bad += 1
print("rows 13, 14 and 24: odd me-parities to", mp[399], ": 2 at a me again's place at the -1 and the +1 of a seam of 8 alone; 2 of the most least times at:", most[:14], "...", len(most), "of 399")
# row 33: a pattern of places
def whole(pattern):
    k = len(pattern)
    return all(len({x % r for x in pattern}) < r for r in mp if r <= k)
def copies(pattern, seam_mps):
    c = 1
    for r in seam_mps: c *= r - len({x % r for x in pattern})
    return c
def found(pattern, top):
    return [n for n in range(2, top) if all(s[n + x] for x in pattern)]
for pat in ((0, 2, 6), (0, 4, 6), (0, 2, 4), (0, 2, 6, 8), (0, 2, 6, 8, 12), (0, 6, 12, 18, 24)):
    f = found(pat, 100000)
    print(f"row 33: the pattern {pat}: whole: {whole(pat)}; uncrossed copies round 30 and round 210: {copies(pat, (2,3,5))}, {copies(pat, (2,3,5,7))}; to 100,000 found {len(f)}: {f[:5]}")
    if not whole(pat) and len(f) > 1: bad += 1
# round the seam 210, gone through: the copies of (0, 2, 6)
S = 210; unc = {n for n in range(S) if all(n % r for r in (2, 3, 5, 7))}
if sum(1 for n in range(S) if all(((n + x) % S) in unc for x in (0, 2, 6))) != copies((0, 2, 6), (2, 3, 5, 7)): bad += 1
# row 36: podal pairs about a middle
def pairs_about(m): return [(m - b, m + b) for b in range(0, m - 1) if s[m - b] and s[m + b]]
none = [m for m in range(2, 250001) if not any(s[m - b] and s[m + b] for b in range(0, m - 1))] if False else None
ok = True
sm = s[:500001]
for m in range(2, 250001):
    lo = sm[2:m + 1][::-1]; hi = sm[m:2 * m - 1]
    if not (lo & hi).any(): ok = False; bad += 1
print("row 36: the middles 2 to 250,000, a podal pair of me-parities about the middle at all:", ok, "; about 14:", pairs_about(14), "; about 15:", pairs_about(15), "; about 16:", pairs_about(16))
def seam_pairs(m, seam_mps):
    S = prod(seam_mps); unc = {n for n in range(S) if all(n % r for r in seam_mps)}
    direct = sum(1 for b in range(S) if ((m - b) % S) in unc and ((m + b) % S) in unc)
    rule = prod((r - 1) if m % r == 0 else (r - 2) for r in seam_mps if r > 2) * 1
    return direct, rule
for m in (14, 15, 16, 21, 35, 105):
    d, r = seam_pairs(m, (2, 3, 5, 7))
    if d != r: bad += 1
print("   steps round 210 with the middle less the step and the middle and the step both uncrossed, the middles 14, 15, 16, 21, 35, 105:", [seam_pairs(m, (2,3,5,7))[0] for m in (14, 15, 16, 21, 35, 105)])
# row 54: the curve, the across place's me again at the along place by itself by itself, less the along place
out = []
for p in mp[1:120]:
    sqc = np.zeros(p, dtype=np.int64)
    for y in range(p): sqc[(y * y) % p] += 1
    pts = 1 + sum(int(sqc[(x * x * x - x) % p]) for x in range(p))
    lean = p + 1 - pts
    if p % 4 == 3 and lean != 0: bad += 1
    if lean * lean > 4 * p: bad += 1
    if p in (3, 7, 11, 5, 13, 17): out.append((p, pts, lean))
print("row 54: (me-parity, places with the one place apart, lean):", out, "; lean 0 at all me-parities at the -1 of a seam of 4, to", mp[119])
# row 61: the uncrossed places of an earlier seam in a universe: me-parities, and crossings of me-parities past the earlier opener
a, b = 169, 288
unc = [n for n in range(a, b + 1) if all(n % r for r in (2, 3, 5))]
mpu = [n for n in unc if s[n]]; two = [n for n in unc if not s[n]]
def parts(n):
    o = []; i = 2
    while i * i <= n:
        while n % i == 0: o.append(i); n //= i
        i += 1
    if n > 1: o.append(n)
    return o
print("row 61: the universe of 13, uncrossed by 2, 3 and 5:", len(unc), "; me-parities", len(mpu), "; crossings", len(two), [(n, parts(n)) for n in two])
print("is-nots:", bad)
