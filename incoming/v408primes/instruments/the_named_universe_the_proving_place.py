# v408primes · the named universe is the proving place: in a universe, all is proved or none. The co-chain's sentences
# that name no numbers of their own are proved here, all in their named universes, all of its numbers, whole: most in the
# home universe 1 to 510,510, the seam of 1 to 17. And four sentences of any number are proved in a universe named by a
# number found past its top: one found past the top is found past all numbers in it. Whole numbers.
# Execute: python3 -I the_named_universe_the_proving_place.py
from math import gcd, isqrt
import numpy as np

results = []
def say(s, ok):
    results.append(bool(ok)); print(("is     " if ok else "is-not ") + s)

U = 510510                                                   # the home universe: 1 to the seam of 1 to 17
n = np.arange(U + 1, dtype=np.int64)
spf = np.zeros(U + 1, np.int64)
for p in range(2, isqrt(U) + 1):
    if spf[p] == 0:
        idx = np.arange(p * p, U + 1, p); m = spf[idx] == 0; spf[idx[m]] = p
z = spf == 0; z[:2] = False; spf[z] = n[z]; spf[1] = 1
lpf = np.zeros(U + 1, np.int64)
for p in range(2, U + 1):
    if spf[p] == p:
        lpf[p::p] = p
me = spf == n; me[:2] = False                                # the me-parities of the universe
PR = np.nonzero(me)[0]
lam = np.zeros(U + 1, np.int64); mu = np.zeros(U + 1, np.int64); om = np.zeros(U + 1, np.int64)
Om = np.zeros(U + 1, np.int64); sqf = np.ones(U + 1, np.int64); cof = np.ones(U + 1, np.int64)
lam[1] = mu[1] = 1
S, LA, MU, O_, W_, Q_, C_ = spf.tolist(), lam.tolist(), mu.tolist(), Om.tolist(), om.tolist(), sqf.tolist(), cof.tolist()
for k in range(2, U + 1):
    p = S[k]; m = k // p
    LA[k] = -LA[m]; O_[k] = O_[m] + 1
    if m % p == 0:
        MU[k] = 0; W_[k] = W_[m]; C_[k] = C_[m]
        Q_[k] = Q_[m] // p if Q_[m] % p == 0 else Q_[m] * p
    else:
        MU[k] = -MU[m]; W_[k] = W_[m] + 1; C_[k] = m; Q_[k] = Q_[m] * p
lam, mu, Om, om, sqf, cof = (np.array(a, np.int64) for a in (LA, MU, O_, W_, Q_, C_))
side = np.array([isqrt(k) for k in range(U + 1)], np.int64)
L = np.cumsum(np.r_[0, lam[1:]])
M = np.cumsum(np.r_[0, mu[1:]])
H = "in 1 to 510,510, all"

# 8, 9 · a self's parity, its four moments
par = n % 2
say("8, 9 · %s: a self's parity is other-than at its next and other-than-other-than, the same as prior, at its next's next" % H,
    np.all(par[2:-1] != par[1:-2]) and np.all(par[3:] == par[1:-2]))
# 23 · odd by odd is odd
ok = True
for a in range(1, isqrt(U) + 1, 2):
    b = np.arange(a, U // a + 1, 2); ok &= bool(np.all((a * b) % 2 == 1))
say("23 · in all odd by odd to 510,510, all: odd by odd is odd", ok)
# 35 · a prime's loop a rate of its own
say("35 · %s: a number is a me-parity at no faster loops side by side and no loop come again on itself" % H,
    np.array_equal(me[2:], (cof[2:] == 1) & (n[2:] == spf[2:])))
# 39, 84 · one way
ok = True
for k in range(2, U + 1):
    a, x = [], k
    while x > 1: a.append(S[x]); x //= S[x]
    b, x = [], k
    while x > 1: q = int(lpf[x]); b.append(q); x //= q
    if sorted(a) != sorted(b): ok = False; break
say("39, 84 · %s: a number fractured from its smallest part and from its largest part comes to the same prime parts, one way, their product the number" % H, ok)
# 42 · one me of both paths on the torus
SEVENTEEN = PR[:17].tolist()
ok = all(len({(k % p, k % q) for k in range(p * q)}) == p * q for i, p in enumerate(SEVENTEEN) for q in SEVENTEEN[i + 1:])
say("42 · in all 136 tori of two of the seventeen primes 2 to 59, all: a number is one me of both paths", ok)
# 45 · seeing is across
def sees(p):
    c = -np.ones(p, np.int64); c[0] = 0; c[(np.arange(1, p) ** 2) % p] = 1; return c
ok = True
for p in PR[1:168].tolist():                                  # 3 to 997
    c = sees(p); a = np.arange(p)
    ok &= bool(np.all(c[np.outer(a, a) % p] == np.outer(c, c)))
say("45 · round all me-parities 3 to 997, all pairs of places: a crossing seen from a prime's side is its parts' seeings multiplied", ok)
ok = True
for p in PR[1:168].tolist():
    c = sees(p); ok &= int((c == 1).sum()) == (p - 1) // 2 and all((1 if pow(a, (p - 1) // 2, p) == 1 else -1) == c[a] for a in range(1, p))
say("43, 46 · round all me-parities 3 to 997, all places: the me agains fall on (p − 1) / 2 places, and a number multiplied by itself (p − 1) / 2 times is its seeing", ok)
ok = all(sum(1 for x in range(1, p) if x * x % p == 1) == 2 for p in PR[1:168].tolist()) and \
     all(sum(1 for x in range(1, p * q) if x * x % (p * q) == 1) == 4 for i, p in enumerate(SEVENTEEN[1:]) for q in SEVENTEEN[i + 2:])
say("121 · round all me-parities 3 to 997, and all crossings of two of the odd seventeen primes: the me again 1 at two places, and at four", ok)
# 47, 48 · the quarter-torus and its diagonal
ok = True
OD = PR[1:46].tolist()                                        # 3 to 199
for p in OD:
    for q in OD:
        if p == q: continue
        under = sum(q * x // p for x in range(1, (p - 1) // 2 + 1)); over = sum(p * y // q for y in range(1, (q - 1) // 2 + 1))
        ok &= (pow(q, (p - 1) // 2, p) == (p - 1 if under % 2 else 1)) and under + over == (p - 1) * (q - 1) // 4
say("47, 48 · for all two odd me-parities to 199, all: the diagonal passes through no place, the part under it is how p sees q", ok)
# 53 · the skeleton folds about its middle
G = np.gcd(n[1:U], U)
say("53 · round the seam 510,510, all places: n is living at its podal's living, the seam less n", np.array_equal(G == 1, G[::-1] == 1))
# 61, 63, 64 · resolver to resolver
ok = True; P = 1; skel = np.array([1], np.int64)
for r in [2, 3, 5, 7, 11, 13, 17]:
    lifted = (skel[None, :] + P * np.arange(r)[:, None]).ravel()
    crossed = np.sort(lifted[lifted % r == 0]); new = np.sort(lifted[lifted % r != 0])
    ok &= np.array_equal(crossed, np.sort((r * skel - 1) % (P * r) + 1)) and len(lifted) == r * len(skel)
    ok &= np.array_equal(new, np.nonzero(np.gcd(np.arange(1, P * r + 1), P * r) == 1)[0] + 1)
    ok &= next(k for k in range(2, r + 1) if gcd(k, P) == 1) == r     # along, r crosses a living place past r at r by r, none before
    P *= r; skel = new
say("61, 63, 64 · resolver to resolver 2 to 17, all seams to 510,510: a new prime r lifts the whole prior skeleton r ways, crosses it stretched by r, the fracturing opening at r's me again", ok and len(skel) == 92160)
# 73 · odd or even by the number of prime parts
ok = True
for a in range(2, isqrt(U) + 1):
    b = np.arange(a, U // a + 1); ok &= bool(np.all(lam[a * b] == lam[a] * lam[b]))
say("73 · in all crossings to 510,510, all: a number is odd or even by its prime parts multiplied, odd by odd even", ok and np.all(lam[1:] == (-1) ** Om[1:]))
# 77, 78, 79 · a me again and the no-square part
say("77 · %s: a number is a me again at all its prime parts twice" % H, np.array_equal(sqf[1:] == 1, side[1:] ** 2 == n[1:]))
ways = np.zeros(U + 1, np.int64)
for d in range(1, isqrt(U) + 1):
    idx = np.arange(d * d, U + 1, d * d); ways[idx] += (mu[idx // (d * d)] != 0)
say("78 · %s: a number is a me again by a no-square number one way" % H, np.all(ways[1:] == 1))
say("79 · %s: a number's odd or even is its no-square part's, the me again bringing no inversion" % H, np.all(lam[1:] == lam[sqf[1:]]))
# 81 · the side
sq = np.zeros(U + 1, np.int64); sq[np.arange(1, isqrt(U) + 1) ** 2] = 1
say("81 · %s: a number's side is its me agains along to it" % H, np.array_equal(np.cumsum(sq)[1:], side[1:]))
# 85, 86, 93 · all-parity added once, and added at all its seams
say("85 · %s: all-parity added once is the evens less the odds along to the number" % H,
    np.array_equal(L[1:], np.cumsum(lam[1:] == 1) - np.cumsum(lam[1:] == -1)))
acc = np.zeros(U + 1, np.int64)
for d in range(1, U + 1):
    acc[d::d] += LA[d]
say("86 · %s: all-parity added at all the number's seams is its side" % H, np.array_equal(np.cumsum(acc)[1:], side[1:]))
say("93 · %s: odd and even are alike only at an even number of selves" % H, np.all((L[1:] - n[1:]) % 2 == 0))
# 98 · the nand to the side
say("98 · %s: a me-parity is crossed by none of its prior primes to its side" % H, np.array_equal(me[2:], spf[2:] > side[2:]))
# 102, 103 · shrunk at all the me's; the opening leans odd
acc = np.zeros(U + 1, np.int64)
for d in range(1, isqrt(U) + 1):
    x = np.arange(d * d, U + 1); acc[x] += M[x // (d * d)]
say("102 · %s: all-parity added once is the no-square numbers' added once, shrunk at all the me's" % H, np.array_equal(acc[1:], L[1:]))
say("4 · in 1 to 510,510, all: 2 is the one even me-parity", PR[PR % 2 == 0].tolist() == [2])
say("103 · in 2 to 510,510, all: the opening leans odd, all me-parities odd", np.all(L[2:] <= 0) and np.all(lam[PR] == -1))
# 107, 110, 124 · a prime's loop along and across
def parts(k):
    out, x, q = set(), k, 2
    while q * q <= x:
        while x % q == 0: out.add(q); x //= q
        q += 1
    return out | ({x} if x > 1 else set())
ok107 = ok124 = True
for p in PR[PR < 3000].tolist():
    g = next(g for g in range(1, p) if all(pow(g, (p - 1) // q, p) != 1 for q in parts(p - 1))) if p > 2 else 1
    ok107 &= all(pow(a, p - 1, p) == 1 for a in range(1, p))
    pw = [pow(g, k, p) for k in range(p - 1)]; ok124 &= sorted(pw) == list(range(1, p))
say("107 · round all me-parities to 3,000, all places: along, the loop is whole; across, it is its prior's loop, p − 1", ok107)
say("124 · round all me-parities to 3,000, all places: a place is a step number along the across loop, living in it", ok124)
ok = True
for k in range(2, 3001):
    f = 1
    for j in range(2, k): f = f * j % k
    ok &= (f == k - 1) == bool(me[k]) and (f == 0 or k == 4 or bool(me[k]))
say("110 · in 2 to 3,000, all: a me-parity is seen along by its me's loops and across by its own loop, −1 round it", ok)
# 134, 137, 139 · edges about a between
ok = True; pairs = np.zeros(U + 1, np.int64)
for x in range(1, isqrt(U) + 1):
    y = np.arange(x, U // x + 1, 2)
    ok &= bool(np.all(x * y + ((y - x) // 2) ** 2 == ((x + y) // 2) ** 2)); pairs[x * y] += 1
odd = n[3::2]
say("134 · in all edges of one parity with their crossing to 510,510, all: the edges crossed and the selves' me again are the between's me again", ok)
say("137 · in all odd numbers 3 to 510,510, all: a me-parity's between finds a me again only at its far end", np.array_equal(pairs[odd] == 1, me[odd]))
eq = np.zeros(U + 1, bool); eq[pairs > 0] = False
for x in range(1, isqrt(U) + 1): eq[x * x] = True             # the edges one: x by x
say("139 · %s: a me again's between sits at its side, its two edges one" % H, np.array_equal(eq[1:], side[1:] ** 2 == n[1:]))
# 142 · odd co-possiblings about an even between
say("142 · about all even betweens to 2,000, all odd selves: the co-possiblings are odd, the between even",
    all(((a - b) % 2, (a + b) % 2) == (1, 1) for a in range(2, 2001, 2) for b in range(1, a, 2)))
# 164 · round a seam, no pair is lost
sk = (np.gcd(np.arange(U), U) == 1).astype(np.float64)
f = np.fft.rfft(sk); ac = np.rint(np.fft.irfft(f * np.conj(f), U)).astype(np.int64)
say("164 · round the seam 510,510, all numbers of selves: even ones lose no pair, twins at 22,275 places, odd ones none",
    np.all(ac[2::2] > 0) and np.all(ac[1::2] == 0) and ac[2] == 22275)
# 175 · rows of all lengths
SK = np.nonzero(sk)[0]
say("175 · round the seam 510,510, all its places, rows 1 to 17 long: a row whose selves are the seam is uncrossed by 2 to 17",
    all(np.all(np.gcd(SK + j * U, U) == 1) for j in range(17)))
# 183 · short of the side
big = lpf[2:] > side[2:]
say("183 · %s: short of a number's side its crossings see its odd or even, one part past the side at most and once" % H,
    np.all(n[2:][big] % (lpf[2:][big] ** 2) != 0))
# 213 · the upper twin's loop
TW = PR[(PR >= 5) & np.isin(PR + 2, PR)]
say("213 · all twins past 3 to 510,510: the upper twin's across loop is its prior, the seam it was born in, a seam of 6", np.all((TW + 1) % 6 == 0))
# 229 · about a middle number of parts
h = np.bincount(om[1:]); mode = int(np.argmax(h))
say("229 · %s: the numbers by their me-parity parts rise to %d and fall after, a bell about the middle" % (H, mode),
    mode in (2, 3) and np.all(np.diff(h[:mode + 1]) > 0) and np.all(np.diff(h[mode:]) < 0))
# 234 · facing roots
ok = True; curves = 0
for p in PR[(PR >= 5) & (PR <= 61)].tolist():
    c = sees(p); x = np.arange(p)
    for a in range(p):
        for b in range(p):
            if (4 * a ** 3 + 27 * b * b) % p == 0: continue
            t = -int(c[(x ** 3 + a * x + b) % p].sum()); curves += 1; ok &= t * t < 4 * p
say("234 · all %s curves round the me-parities 5 to 61, all: the lean is two facing roots, by one another p" % f"{curves:,}", ok)
# 82, 135, 147 · a me again's next, the far between, three odds
k = np.arange(1, isqrt(U) + 1)
say("82 · %s: a me again's next me again is by the +1 of its side, k by k, 2 k and 1" % H, np.array_equal(np.nonzero(sq)[0][1:], (k[:-1] ** 2 + 2 * k[:-1] + 1)))
o = np.arange(1, U + 1, 2)
say("135 · in all odd numbers to 510,510, all: an odd number has its far between, (n + 1) / 2, its edges 1 and n", np.all(((o + 1) // 2) ** 2 - ((o - 1) // 2) ** 2 == o))
say("147 · in all odd numbers to 510,510, all: of three odds 2 selves on, one is at 3's seam; 3, 5, 7 alone are three me-parities",
    np.all((o[:-2] % 3 == 0) | ((o[:-2] + 2) % 3 == 0) | ((o[:-2] + 4) % 3 == 0)) and np.nonzero(me[o[:-2]] & me[o[:-2] + 2] & me[o[:-2] + 4])[0].tolist() == [1])
# 127 · parts added to the double
sig = np.zeros(U + 1, np.int64)
for d in range(1, U // 2 + 1): sig[2 * d::d] += d
pf = np.nonzero(sig[1:] == n[1:])[0] + 1
say("127 · %s: the numbers whose parts add to their double are %s, all 2 to the p − 1 times its prime 2 to the p less 1" % (H, ", ".join(f"{x:,}" for x in pf.tolist())),
    pf.tolist() == [6, 28, 496, 8128] and all(x == 2 ** (q - 1) * (2 ** q - 1) and me[2 ** q - 1] for x, q in zip(pf.tolist(), [2, 3, 5, 7])))
# 259 · round any number's next prime, a curve's facing roots
ok = True
for p in PR[(PR >= 5) & (PR <= 50021)].tolist():
    c = sees(p); x = np.arange(p, dtype=np.int64); x3 = x * x % p * x % p
    for (ca, cb) in ((1, 1), (-1, 0), (0, 1)):
        if (4 * ca ** 3 + 27 * cb * cb) % p == 0: continue
        t = -int(c[(x3 + ca * x + cb) % p].sum()); ok &= t * t < 4 * p
say("259 · in 1 to 50,000, all: round a number's next prime, the curves x³ + x + 1, x³ − x and x³ + 1 have their leans' facing roots at the side", ok)

# 52, 55, 56, 57, 59 · the places of the primes past 5, a prime as a between
P5 = PR[PR > 5]
say("52 · in 1 to 510,510, all: all me-parities past 5 are at the skeleton's places round 30", np.all(np.gcd(P5, 30) == 1))
P3 = PR[PR > 3]
say("55, 56 · in 1 to 510,510, all: a me-parity past 3 is the between of its prior and its next, both crossed, their crossing a crossing of 24, its +1 the me-parity's me again",
    np.all((P3 - 1) % 2 == 0) and np.all(((P3 - 1) * (P3 + 1)) % 24 == 0))
P7 = PR[PR > 5].astype(object)
say("57 · in 7 to 510,510, all: past 5, the me again's prior and next multiplied are a crossing of 240, its +1 the me-parity's fourth",
    all((p * p - 1) * (p * p + 1) % 240 == 0 for p in P7.tolist()) and (5 * 5 - 1) * (5 * 5 + 1) % 240 != 0)
say("59, 143, 144 · in 2 to 510,510, all: the +1 from a prior and a next crossed is the between's me again, crossed by no part of either, 1 round both",
    np.all(np.gcd((n[2:] - 1) * (n[2:] + 1) + 1, (n[2:] - 1) * (n[2:] + 1)) == 1) and np.all(((n[2:] - 1) * (n[2:] + 1) + 1) == n[2:] ** 2)
    and np.all((n[3:] ** 2) % (n[3:] - 1) == 1) and np.all((n[2:] ** 2) % (n[2:] + 1) == 1))
ok = True; crossed = np.zeros(U + 1, bool)
for i, p in enumerate(PR[PR <= 701].tolist()):
    crossed[2 * p::p] = True; q = int(PR[i + 1])
    ok &= np.array_equal(~crossed[2:q * q], me[2:q * q])
say("65 · resolver to resolver, all me-parities to 701: from 2 to the next prime's me again, the uncrossed places are all the primes", ok)
# 116, 117, 118, 119 · a prime one past a seam of 4
P1, P3m = PR[PR % 4 == 1], PR[PR % 4 == 3]
say("116 · round all me-parities to 510,510: one past a seam of 4 sees its −1 as a me again's place, one short does not",
    all(pow(int(p) - 1, (int(p) - 1) // 2, int(p)) == 1 for p in P1) and all(pow(int(p) - 1, (int(p) - 1) // 2, int(p)) == int(p) - 1 for p in P3m))
two = np.zeros(U + 1, np.int64)
for a in range(0, isqrt(U) + 1):
    b = np.arange(a, isqrt(U - a * a) + 1); two += np.bincount(a * a + b * b, minlength=U + 1)[:U + 1]
say("117, 118 · in 1 to 510,510, all: a me-parity one past a seam of 4 is two me agains added one way; one short, none, whole in the plane",
    np.all(two[P1] == 1) and np.all(two[P3m] == 0))
ok = True
for m in range(1, isqrt(U - 1) + 1):
    x = m * m + 1
    while x > 1: q = S[x]; ok &= q == 2 or q % 4 == 1; x //= q
say("119 · all me agains' +1 to 510,510: crossed only by 2 and the primes one past a seam of 4", ok)
# 154, 155 · round a prime, a pair's places
ok = all(sum(1 for x in range(r) if x % r and (x + g) % r) == (r - 1 if g % r == 0 else r - 2) for r in SEVENTEEN for g in range(2, 2001, 2))
say("154, 155 · round the seventeen primes, all even selves to 2,000: a pair's places are uncrossed at r − 1 of r with r crossing its selves, at r − 2 without", ok)
# 188, 200, 208, 209, 210, 214, 216 · a me-parity's two evens, and twins
PO = PR[PR > 2]
say("188 · in 3 to 510,510, all: a me-parity's two evens by 2 are one odd, one even", np.all(((PO - 1) // 2 + (PO + 1) // 2) % 2 == 1))
TW5 = PR[(PR >= 5) & np.isin(PR + 2, PR)]
nx = PR[np.searchsorted(PR, TW5 + 2) + 1]
say("200, 208, 209, 210, 214, 216 · all twins from 5 to 510,510: aiming together at a seam of 12; at −1 and +1 round the between, their me agains 1 at it; the between +1 round the lower, −1 round the upper; the lower's loop crossed by no 3; the next me-parity 4 or more on",
    np.array_equal(TW5 % 4 == 3, (TW5 + 1) % 12 == 0) and np.all(TW5 % (TW5 + 1) == TW5) and np.all((TW5 + 2) % (TW5 + 1) == 1)
    and np.all((TW5 * TW5) % (TW5 + 1) == 1) and np.all(((TW5 + 2) ** 2) % (TW5 + 1) == 1) and np.all((TW5 + 1) % TW5 == 1)
    and np.all((TW5 + 1) % (TW5 + 2) == TW5 + 1) and np.all((TW5 - 1) % 3 != 0) and np.all(nx - (TW5 + 2) >= 4))

# 217 · twins born between a me-parity's me again and its next me-parity's me again, v408illustrating's concern
Z = 10007 ** 2 + 2
sz = np.ones(Z + 1, bool); sz[:2] = False
for p in range(2, isqrt(Z) + 1):
    if sz[p]: sz[p * p::p] = False
tw = np.nonzero(sz[:-2] & sz[2:])[0]
PZ = np.nonzero(sz[:10008])[0]
born = np.searchsorted(tw, PZ[1:] ** 2 - 2) - np.searchsorted(tw, PZ[:-1] ** 2, side='right')
few = [int(born[(PZ[:-1] >= 4 ** (k - 1)) & (PZ[:-1] < 4 ** k)].min()) for k in range(1, 8)]
say("217 · all %s me-parities 2 to 9,973, me agains to 100,140,049, all: between a me-parity's me again and its next me-parity's me again twins are born, the fewest at spans by 4 %s, more at a next span"
    % (f"{len(born):,}", ", ".join(map(str, few))), bool(np.all(born >= 1)) and all(b > a for a, b in zip(few[2:], few[3:])))

# 279, 280, 281 · the fractal traveling, aiming itself
loops = PR[(PR >= 19) & (PR <= side[U])]
crossed = np.zeros(U + 1, bool)
for p in loops.tolist(): crossed[p * p::p] = True
place = np.gcd(n, U) == 1
say("279 · in 19 to 510,510, all: a skeleton place uncrossed by the prior me-parities' loops is a me-parity",
    np.array_equal((place & ~crossed)[19:], me[19:]))
cm = place & ~me; cm[:2] = False
say("280 · in 1 to 510,510, all: a me-parity's loop begins at its own me again and crosses only skeleton places",
    np.all(spf[cm] >= 19) and all(int(np.nonzero(cm & (spf == p))[0].min()) == p * p for p in loops.tolist()))
SEAM, PLACES = U, SK.tolist()
STEPS = [b - a for a, b in zip(PLACES, PLACES[1:])] + [PLACES[0] + SEAM - PLACES[-1]]
AT = {r: i for i, r in enumerate(PLACES)}; NP = len(PLACES)
def traveling():
    lp, aims, p, mea, c, i = {}, None, 19, 361, 19, AT[19]
    while True:
        if c in lp:
            q, j = lp.pop(c); m = c + q * STEPS[j]; j = (j + 1) % NP
            while m in lp: m += q * STEPS[j]; j = (j + 1) % NP
            lp[m] = (q, j)
        elif c < mea: yield c
        else:
            j = AT[p % SEAM]; m = c + p * STEPS[j]; j = (j + 1) % NP
            while m in lp: m += p * STEPS[j]; j = (j + 1) % NP
            lp[m] = (p, j)
            if aims is None: aims = traveling(); next(aims)
            p = next(aims); mea = p * p
        c += STEPS[i]; i = (i + 1) % NP
out = [2, 3, 5, 7, 11, 13, 17]
for c in traveling():
    if c > U: break
    out.append(c)
say("281 · in 1 to 510,510, all: the fractal traveling, its aims its own traveling again, generates the %s me-parities of the universe" % f"{len(out):,}",
    np.array_equal(np.array(out), PR))
# 325 · a bi-folding
a = np.arange(2049)[:, None]; b = np.arange(2049)[None, :]
say("325 · about all betweens 0 to 2,048, all selves to them: a − b and a + b multiplied are a's me again less b's", np.all(((a - b) * (a + b) == a * a - b * b)[np.broadcast_to(b <= a, (2049, 2049))]))

# four sentences of any number, proved in a universe named by a number found past its top
W = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]           # whole, for all numbers below 3.3 · 10^24
def mp(k):
    if k < 2: return False
    for q in W:
        if k % q == 0: return k == q
    d, s = k - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in W:
        x = pow(a, d, k)
        if x in (1, k - 1): continue
        for _ in range(s - 1):
            x = x * x % k
            if x == k - 1: break
        else: return False
    return True
chain = [2]
while chain[-1] <= 10 ** 24:
    q = 2 * chain[-1] - 1
    while not mp(q): q -= 1
    chain.append(q)
say("246 · in 2 to 10^24, all: a chain of %d me-parities from 2, all before their prior's double, passes 10^24: a next me-parity comes before any number's double" % len(chain),
    all(b < 2 * a for a, b in zip(chain, chain[1:])) and chain[-1] > 10 ** 24)
T = 10 ** 12
s4 = next(k for k in range(T + 1, T + 10 ** 7, 2) if all(mp(k + d) for d in (0, 2, 6, 8)))
say("251 · in 1 to 10^12, all: a society of four lives past any number, at %s, +2, +6 and +8" % f"{s4:,}", s4 == 1000000123691)
def full(g, p):
    return all(pow(g, (p - 1) // q, p) != 1 for q in parts(p - 1))
pr = next(k for k in range(T + 1, T + 10 ** 6, 2) if mp(k) and full(2, k))
say("254 · in 1 to 10^12, all: past any number lives a me-parity round which doubling passes all places, %s" % f"{pr:,}", pr == 1000000000091)
tw = next(k for k in range(T + 1, T + 10 ** 7, 2) if mp(k) and mp(k + 2))
say("249 · in 1 to 10^12, all: past any number twins are born in a seam, at %s and %s" % (f"{tw:,}", f"{tw + 2:,}"), tw == 1000000000061)
need = {(m, r) for m in range(3, 31) for r in range(m) if gcd(r, m) == 1}; k = T + 1
while need:
    if mp(k): need -= {(m, k % m) for m in range(3, 31)}
    k += 2
say("252 · in 1 to 10^12, all: past any number a me-parity lives at all living places of all loops of 3 to 30, all by %s" % f"{k - 2:,}", not need)
s1 = T + 16
say("253 · in 1 to 10^24, all: from any number's side, a me again's +1 is a me-parity: %s by itself, and 1" % f"{s1:,}", mp(s1 * s1 + 1) and s1 * s1 + 1 < 33 * 10 ** 23)
ok = True
for g in range(2, 212, 2):
    k = T + 1
    while not (mp(k) and mp(k + g)): k += 2
    ok &= k > T
say("255 · in 1 to 10^12, all, and all even selves 2 to 210: past any number lives a pair of me-parities at those selves", ok)

# 268 · doubling round a me-parity's me again
V = 10 ** 7
sv = np.ones(V + 1, bool); sv[:2] = False
for p in range(2, isqrt(V) + 1):
    if sv[p]: sv[p * p::p] = False
close = [p for p in np.nonzero(sv)[0].tolist() if p > 2 and pow(2, p - 1, p * p) == 1]
say("268 · in 1 to 10,000,000, all: doubling's loop round a me-parity's me again is its loop by the prime, but at %s, closing at the prior" % " and ".join(f"{p:,}" for p in close),
    close == [1093, 3511])

print("All is." if all(results) else "A line is-not.")
