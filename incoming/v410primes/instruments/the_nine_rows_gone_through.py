# The nine rows with no core laid: named universes gone through, and the cores in view. Breaking tests; proving nothing past the numbers named.
import numpy as np, math
N = 10**8
s = np.ones(N + 3, dtype=np.uint8); s[:2] = 0; s[N+1:] = 0
for i in range(2, int(N**.5) + 1):
    if s[i]: s[i*i:N+1:i] = 0
mp = np.flatnonzero(s)
bad = 0
# row 26: round 4, the me-parities at place 3 beside the me-parities at place 1
odd = mp[1:]
c1 = np.cumsum(odd % 4 == 1); c3 = np.cumsum(odd % 4 == 3)
lead1 = odd[np.flatnonzero(c1 > c3)]
ties = odd[np.flatnonzero(c1 == c3)]
print("row 26: the least me-parity with more at place 1 than at place 3:", int(lead1[0]), "; me-parities to 100,000,000 with more at place 1:", len(lead1), "of", len(odd), "; the same number at both, to 26,860:", [int(x) for x in ties[ties < 26861]][:8])
# row 40: two same steps one after an other
g = np.diff(mp)
same = np.flatnonzero(g[:-1] == g[1:])
steps = g[same]
print("row 40: three me-parities with the two steps the same, to 100,000,000:", len(same), "; the step a crossing of 6 at all past 3, 5, 7:", bool((steps[1:] % 6 == 0).all()), "; the opening one:", [int(mp[same[0]]), int(mp[same[0]+1]), int(mp[same[0]+2])], "; the least steps met:", sorted(set(int(x) for x in steps))[:6])
vals, cnt = np.unique(g, return_counts=True)
top = sorted(zip(cnt.tolist(), vals.tolist()), reverse=True)[:4]
print("   the most-met steps to 100,000,000 (met, step):", top)
# row 41: the parts of one of the pairs, added along
lower = mp[:-1][g == 2]
tot = float(np.sum(1.0 / lower + 1.0 / (lower + 2)))
print("row 41: pairs to 100,000,000:", len(lower), "; the parts of one added:", round(tot, 6), "; to 1,000:", round(float(np.sum(1.0/lower[lower<1000] + 1.0/(lower[lower<1000]+2))), 6), "; to 1,000,000:", round(float(np.sum(1.0/lower[lower<10**6] + 1.0/(lower[lower<10**6]+2))), 6))
# rows 42 and 44: the all-parity at the numbers with no me-parity part twice, 0 at all others; added with the named number over the number, whole: 1
M = 10**6
mu = np.ones(M + 1, dtype=np.int64)
for p in mp[mp <= M]:
    p = int(p); mu[p::p] *= -1
    if p * p <= M: mu[p*p::p*p] = 0
for n in (1, 2, 10, 17, 1000, 99991, 10**6):
    d = np.arange(1, n + 1)
    if int(np.sum(mu[1:n+1] * (n // d))) != 1: bad += 1
print("rows 42 and 44: added with the named number over the number, whole: 1, at the named numbers 1, 2, 10, 17, 1,000, 99,991 and 1,000,000:", bad == 0, "; added along to 10, 100, 1,000, 1,000,000:", [int(mu[1:n+1].sum()) for n in (10, 100, 1000, 10**6)])
# row 48: the me-parity parts of a number, at most the doublings
# row 51: the one curve over the plane of a me-parity at the -1 of a seam of 4
def plane_places(p):
    # numbers of the plane: a and b by the root of the -1; the across place's me again at the along place by itself by itself, less the along place
    sq = {}
    for a in range(p):
        for b in range(p):
            r = ((a*a - b*b) % p, (2*a*b) % p)
            sq[r] = sq.get(r, 0) + 1
    tot = 1
    for a in range(p):
        for b in range(p):
            x2 = ((a*a - b*b) % p, (2*a*b) % p)
            x3 = ((x2[0]*a - x2[1]*b) % p, (x2[0]*b + x2[1]*a) % p)
            f = ((x3[0] - a) % p, (x3[1] - b) % p)
            tot += sq.get(f, 0)
    return tot
out = []
for p in (3, 7, 11, 19, 23):
    t = plane_places(p); out.append((p, t, (p + 1)**2))
    if t != (p + 1)**2: bad += 1
print("row 51: (me-parity, the curve's places over the plane of the me-parity, the me-parity's +1 by itself):", out)
print("is-nots:", bad)
