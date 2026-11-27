# The crossings of a universe by their least me-parity part: an opener by the numbers of the universe over the opener,
# uncrossed by all smaller me-parities. A breaking test at all universes of the named universe 1 to N.
import sys, numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
lp = np.zeros(N + 1, dtype=np.int32)                 # the least me-parity part of a number
for i in range(2, int(N**.5) + 1):
    if lp[i] == 0:
        seg = lp[i*i::i]; seg[seg == 0] = i
idx = np.flatnonzero(lp == 0); lp[idx] = idx; lp[:2] = 0
mp = idx[idx >= 2]
op = [int(x) for x in mp[mp <= int(N**.5) + 1]]
bad = 0; shown = 0; uni = 0
for k in range(len(op) - 1):
    p, q = op[k], op[k+1]; a, b = p*p, q*q - 1
    if b > N: break
    uni += 1
    L = b - a + 1
    seg = lp[a:b+1]; nums = np.arange(a, b + 1)
    births = int((seg == nums).sum())
    total = 0; parts = []; two = 0
    for r in op[:k+1]:
        lo, hi = -(-a // r), b // r                    # the universe over the opener
        m = lp[lo:hi+1]
        c = int((m >= r).sum())                        # numbers uncrossed by all smaller me-parities
        direct = int(((seg == r) & (nums != r)).sum())
        if c != direct: bad += 1
        # with the opener by itself by itself past the universe's end, the numbers are me-parities
        if r**3 > b:
            if int(((m >= r) & (m != np.arange(lo, hi+1))).sum()) != 0: bad += 1
            two += c
        total += c; parts.append((r, c))
    if births != L - total: bad += 1
    if p in (5, 7, 11):
        print(f"universe of {p}, {a} to {b}: {L} numbers; crossings by least part: {parts}; all {total}; births {L - total}; crossings of two me-parities by the openers with the opener thrice multiplied past the end: {two}")
print("universes gone through:", uni, "; the last opener:", op[uni-1], "; is-nots:", bad)
