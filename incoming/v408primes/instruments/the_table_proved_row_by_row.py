# v408primes · the table of the interests in the primes, proved row by row: a row's resolving in its named universe, all
# or none. A named universe is the proving place. The rows proved here are executed here; the rows of a larger universe
# name the instrument beside this one that proves all of it, with the universe to give it. Whole numbers.
# Execute: python3 -I the_table_proved_row_by_row.py
from math import gcd, isqrt, log10
import numpy as np

results, rows = [], {}
def say(row, universe, s, ok):
    results.append(bool(ok)); rows[row] = bool(ok)
    print(("is     " if ok else "is-not ") + "row %d · in %s, all: %s" % (row, universe, s))
def named(row, universe, s, instrument, given=""):
    rows[row] = None
    print("named  row %d · in %s, all: %s · proved by %s%s" % (row, universe, s, instrument, (" " + given) if given else ""))

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

# the sieve of the universe 1 to 16,777,216, and its me-parities
N = 1 << 24
S = np.ones(N + 1, bool); S[:2] = False
for p in range(2, isqrt(N) + 1):
    if S[p]: S[p * p::p] = False
PR = np.nonzero(S)[0]
C = np.cumsum(S)                                               # me-parities along to a number
def spans(top):                                                # spans by 4: (4^(k-1), 4^k]
    k, out = 1, []
    while 4 ** k <= top: out.append((4 ** (k - 1), 4 ** k)); k += 1
    return out
# the home universe 1 to 510,510, its smallest parts
U = 510510
n = np.arange(U + 1, dtype=np.int64)
spf = np.zeros(U + 1, np.int64)
for p in range(2, isqrt(U) + 1):
    if spf[p] == 0:
        idx = np.arange(p * p, U + 1, p); m = spf[idx] == 0; spf[idx[m]] = p
z = spf == 0; z[:2] = False; spf[z] = n[z]; spf[1] = 1
SP = spf.tolist(); me = S[:U + 1]; PU = PR[PR <= U]
def parts(k):
    out = []
    while k > 1: out.append(SP[k]); k //= SP[k]
    return out

# row 1 and row 30 · a next me-parity before a number's double, no last
chain = [2]
while chain[-1] <= 10 ** 24:
    q = 2 * chain[-1] - 1
    while not mp(q): q -= 1
    chain.append(q)
ok = all(b < 2 * a for a, b in zip(chain, chain[1:])) and chain[-1] > 10 ** 24
say(1, "2 to 10^24", "a chain of %d me-parities from 2, all before their prior's double, passes 10^24: past any number a next me-parity, no last" % len(chain), ok)
few = [int((C[2 * np.arange(a + 1, b + 1)] - C[np.arange(a + 1, b + 1)]).min()) for a, b in spans(1 << 20)]
say(30, "2 to 10^24", "a next me-parity before any number's double, by the chain of row 1; between a number and its double, the fewest at spans by 4 to 1,048,576 %s: 1 to 16, then more at a next span" % few,
    ok and few[:2] == [1, 1] and all(y > x for x, y in zip(few[1:], few[2:])))

# row 2 · one way
ok = True
for k in range(2, U + 1):
    a = parts(k); b, x = [], k
    while x > 1:
        q = max(parts(x)); b.append(q); x //= q
    if sorted(a) != sorted(b): ok = False; break
say(2, "1 to 510,510", "a number fractured from its smallest part and from its largest comes to the same prime parts, one way", ok)

# rows 3 and 8 · edges about a between
pairs = np.zeros(U + 1, np.int64)
for x in range(1, isqrt(U) + 1): pairs[x * x::x] += 1          # x by y, x at most y
one = np.nonzero(pairs[1:] == 1)[0] + 1
say(3, "1 to 510,510", "the numbers of one pair of edges are 1 and the me-parities; 1's pair is 1 and 1, its edges one, and 1 is no prime",
    one[0] == 1 and np.array_equal(one[1:], PU))
odd = n[3::2]
say(8, "1 to 510,510", "an odd number is a me-parity with its between finding a me again only at its far end", np.array_equal(pairs[odd] == 1, me[odd]))

# row 4 · 2
say(4, "1 to 510,510", "2 is the one even me-parity", PU[PU % 2 == 0].tolist() == [2])

# row 5 · two primes a torus
SEV = PR[:17].tolist()
say(5, "the 136 tori of two of the seventeen primes", "a number is one me of both paths, the torus's two directions its primes",
    all(len({(k % p, k % q) for k in range(p * q)}) == p * q for i, p in enumerate(SEV) for q in SEV[i + 1:]))

# row 6 · along, the loops of a prime's me's
ok, crossed = True, np.zeros(U + 1, bool)
for i, p in enumerate(PU[PU <= 701].tolist()):
    crossed[2 * p::p] = True; q = int(PU[i + 1])
    ok &= np.array_equal(~crossed[2:q * q], me[2:q * q])
say(6, "2 to the me again of 709", "a number is a me-parity with no loop of its me's crossing it, resolver to resolver", ok and np.array_equal(me[2:], spf[2:] > np.array([isqrt(k) for k in range(2, U + 1)])))

# row 7 · across, its own loop multiplied
ok = True
for k in range(2, 3001):
    f = 1
    for j in range(2, k): f = f * j % k
    ok &= (f == k - 1) == bool(me[k]) and (f == 0 or k == 4 or bool(me[k]))
say(7, "2 to 3,000", "a me-parity's loop multiplied is −1 round it; a crossed loop's, past 4, is 0", ok)

# row 9 · a tree of primes to 2
ok = True
for p in PU[PU > 2].tolist():
    qs = set(parts(p - 1))
    g = next((g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1 for q in qs)), None)
    ok &= g is not None and pow(g, p - 1, p) == 1 and all(me[q] for q in qs)
say(9, "1 to 510,510", "all me-parities' across loops network down, a tree of me-parities below them, to 2 and the one me", ok)

# row 10 · seen in few moments
ok = True
for k in range(3, 3000001, 2):
    d, s = k - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    passes = True
    for a in (2, 3, 5):
        if a % k == 0: continue
        x = pow(a, d, k)
        if x in (1, k - 1): continue
        for _ in range(s - 1):
            x = x * x % k
            if x == k - 1: break
        else: passes = False; break
    if passes != bool(S[k]): ok = False; break
say(10, "1 to 3,000,000", "halving the across loop at 2, 3 and 5 finds a crossing's other roots of 1: a me-parity seen in few moments", ok)

# row 11 · passing as a prime by doubling
psp = [k for k in range(9, U + 1, 2) if not me[k] and pow(2, k - 1, k) == 1]
ok = True
for k in psp:
    f, j = 1, 1
    while f and j < k - 1: j += 1; f = f * j % k
    ok &= f == 0
say(11, "1 to 510,510", "the %d crossings passing as a prime by doubling, 341 to %s, are all seen crossed by their own loop multiplied" % (len(psp), f"{psp[-1]:,}"), ok and psp[0] == 341 and 561 in psp)

# rows 12 and 52 · across loops
ok12 = ok52 = True
for p in PR[PR < 3000].tolist():
    ok12 &= all(pow(a, p - 1, p) == 1 for a in range(1, p))
    if p > 2:
        g = next(g for g in range(2, p) if all(pow(g, (p - 1) // q, p) != 1 for q in set(parts(p - 1))))
        ok52 &= sorted(pow(g, k, p) for k in range(p - 1)) == list(range(1, p))
say(12, "the me-parities to 3,000", "across, a stepping comes again at a part of p − 1", ok12)
say(52, "the me-parities to 3,000", "a place round a me-parity is a step number along its across loop", ok52)

# row 13 · doubling passing all places, past any number
T = 10 ** 12
def full(g, p):
    qs, x, q = set(), p - 1, 2
    while q * q <= x:
        while x % q == 0: qs.add(q); x //= q
        q += 1
    if x > 1: qs.add(x)
    return all(pow(g, (p - 1) // q, p) != 1 for q in qs)
pr = next(k for k in range(T + 1, T + 10 ** 6, 2) if mp(k) and full(2, k))
say(13, "1 to 10^12", "past any number lives a me-parity round which doubling passes all places, %s" % f"{pr:,}", pr == 1000000000091)

# row 14 · a doubling less 1
def ll(p):
    if p == 2: return True
    M, s = (1 << p) - 1, 4
    for _ in range(p - 2): s = (s * s - 2) % M
    return s == 0
mers = [p for p in PR[PR <= 4253].tolist() if ll(p)]
ok = mers == [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253]
ok &= all(mp((1 << k) - 1) is False for k in range(4, 200) if not S[k])
say(14, "1 to 4,000 doublings", "from any number of doublings, the doubling's loop reaches a next doubling less 1 that is a me-parity: %s" % mers, ok)

# row 15 · parts making the double
V = 1000000
sig = np.zeros(V + 1, np.int64)
for d in range(1, V // 2 + 1): sig[2 * d::d] += d
pf = (np.nonzero(sig[1:] == np.arange(1, V + 1))[0] + 1).tolist()
say(15, "1 to 1,000,000", "the numbers whose parts make their double are %s, all a doubling by a doubling less 1, no odd one" % pf,
    pf == [6, 28, 496, 8128] and all(x == 2 ** (q - 1) * (2 ** q - 1) for x, q in zip(pf, [2, 3, 5, 7])))

# row 16 · a doubling's doubling +1
fp = []
for k in range(15):
    F = (1 << (1 << k)) + 1
    fp.append(F == 3 or pow(3, (F - 1) // 2, F) == F - 1)
say(16, "the doublings of doublings 0 to 14", "3 by itself to the between sees the doubling's doubling +1 a me-parity at 0 to 4, 3, 5, 17, 257, 65,537, and crossed at 5 to 14",
    fp == [True] * 5 + [False] * 10)

# row 17 · doubling closing round a me again
close = [p for p in PR[PR <= 10 ** 7].tolist() if p > 2 and pow(2, p - 1, p * p) == 1]
say(17, "1 to 10,000,000", "doubling's loop round a me-parity's me again is its loop by the prime, but at %s" % close, close == [1093, 3511])

# rows 18, 19, 20 · the places of the me-parities
say(18, "1 to 510,510", "all me-parities past 17 are at the skeleton's places round 510,510, past 5 round 30", np.all(np.gcd(PU[PU > 17], U) == 1) and np.all(np.gcd(PU[PU > 5], 30) == 1))
P3 = PU[PU > 3]
say(19, "1 to 510,510", "a me-parity past 3 is a +1 or a −1 from a seam of 6, the between of its prior and its next, both crossed", np.all((P3 % 6 == 1) | (P3 % 6 == 5)))
say(20, "1 to 510,510", "a me-parity's me again past 3 is one past a crossing of 24, and its fourth past 5 one past a crossing of 240",
    np.all((P3 * P3) % 24 == 1) and all(pow(int(p), 4, 240) == 1 for p in PU[PU > 5]))

# row 21 · 41's rule
say(21, "n of 0 to 40", "n by n, n and 41 is a me-parity for n of 0 to 39, and 41 by 41 at 40; −163 seen as other-than from all odd me-parities' sides below 41",
    all(mp(k * k + k + 41) for k in range(40)) and 40 * 40 + 40 + 41 == 41 * 41 and all(pow(-163 % p, (p - 1) // 2, p) == p - 1 for p in PR[1:12].tolist()))

# rows 22 and 23 · two me agains added
Q = 4000000
cnt = np.zeros(Q + 1, np.int32)
for a in range(0, isqrt(Q) + 1):
    b = np.arange(a, isqrt(Q - a * a) + 1); np.add.at(cnt, a * a + b * b, 1)
P1, P3m = PR[(PR <= Q) & (PR % 4 == 1)], PR[(PR <= Q) & (PR % 4 == 3)]
say(22, "1 to 510,510", "in the plane, a me-parity one past a seam of 4 is a + bi by a − bi; one short stays whole, two me agains added at none",
    np.all(cnt[P1[P1 <= U]] == 1) and np.all(cnt[P3m[P3m <= U]] == 0))
say(23, "1 to 4,000,000", "all %s me-parities one past a seam of 4 are two me agains added, one way, and see −1 as a me again's place; one short, none" % f"{len(P1):,}",
    np.all(cnt[P1] == 1) and np.all(cnt[P3m] == 0) and all(pow(int(p) - 1, (int(p) - 1) // 2, int(p)) == 1 for p in P1[:5000]))

# row 24 · seen from one another's sides
ok = True
OD = PR[1:46].tolist()
for p in OD:
    for q in OD:
        if p != q:
            under = sum(q * x // p for x in range(1, (p - 1) // 2 + 1))
            ok &= pow(q, (p - 1) // 2, p) == (p - 1 if under % 2 else 1)
            ok &= ((pow(q, (p - 1) // 2, p) == 1) == (pow(p, (q - 1) // 2, q) == 1)) == (p % 4 == 1 or q % 4 == 1)
say(24, "all two odd me-parities to 199", "two me-parities are seen alike from one another's sides, unless both sit one short of a seam of 4", ok)

# rows 25 and 53 · living places of the loops, more at a next span
BND = np.array([4 ** k for k in range(4, 12)])                 # spans by 4 from 256 to 4,194,304
P22 = PR[(PR > 256) & (PR <= 4 ** 11)]; sid = np.searchsorted(BND, P22)
ok25 = ok53 = True
for m in range(3, 31):
    c = np.bincount(sid * m + P22 % m, minlength=len(BND) * m).reshape(len(BND), m)[1:]
    for r in range(m):
        if gcd(r, m) != 1: continue
        good = bool(np.all(np.diff(c[:, r]) > 0))
        ok25 &= good
        if r == 1: ok53 &= good
say(25, "1 to 4,194,304", "round all loops of 3 to 30, the me-parities at all their living places are more at a next span by 4, 256 on", ok25)
say(53, "1 to 4,194,304", "round all loops of 3 to 30, the me-parities at the place 1 are more at a next span by 4, 256 on", ok53)

# rows 26, 43, 49, 50 · odd and even along
named(26, "1 to 906,150,300", "round 4, those aiming prior go ahead at 26,861; one aim and then the other 256 times; last at 12,382,313", "odd_and_even_along_to_any_number.py", "(906,150,300 its own)")
named(43, "1 to 906,150,300", "odd ahead from 587 to 906,150,255, alike at 906,150,256, even ahead at 906,150,257", "odd_and_even_along_to_any_number.py", "(906,150,300 its own)")
named(49, "1 to 906,150,300", "the podaling spans 2, 2, 4, 6, 10, 14, 56, 490 and 906,149,670 long, the long ones as wide as the side of their length", "odd_and_even_along_to_any_number.py", "(906,150,300 its own)")
named(50, "1 to 906,150,300", "odd and even along, alike only at pairs of selves, the long spans as wide as the side of their selves", "odd_and_even_along_to_any_number.py", "(906,150,300 its own)")

# row 27 · rows at equal selves
SK = np.nonzero(np.gcd(np.arange(U), U) == 1)[0]
say(27, "round the seam 510,510, rows to 17 long", "a row whose selves are the seam is uncrossed by 2 to 17 at all 92,160 places; by the seam's selves a row of 14 at 31,385,539 + 420,420 n",
    all(np.all(np.gcd(SK + j * U, U) == 1) for j in range(17)) and all(mp(31385539 + 420420 * j) for j in range(14)))

# row 28 · me agains' +1
SIDE = 1 << 18
Vv = np.arange(SIDE + 1, dtype=np.int64) ** 2 + 1
R = Vv.copy()
while True:
    e = (R % 2 == 0) & (R > 1)
    if not e.any(): break
    R[e] //= 2
ok = all(pow(int(q) - 1, (int(q) - 1) // 2, int(q)) == int(q) - 1 for q in PR[(PR <= SIDE) & (PR % 4 == 3)])
for q in PR[(PR <= SIDE) & (PR % 4 == 1)].tolist():
    c = next(c for c in range(2, q) if pow(c, (q - 1) // 2, q) == q - 1); r = pow(c, (q - 1) // 4, q)
    for s0 in (r, q - r):
        idx = np.arange(s0, SIDE + 1, q)
        while True:
            e = idx[(R[idx] % q == 0) & (R[idx] > 1)]
            if len(e) == 0: break
            R[e] //= q
ok &= bool(np.all(R % 4 == 1))                                  # what stays: 1, or one me-parity one past a seam of 4
born = R == Vv; small = Vv <= N; born[small] = S[Vv[small]]       # n by n +1 a me-parity
born[0] = False
cs = [int(np.count_nonzero(born[a:b])) for a, b in spans(SIDE)]                # sides from a, short of b
say(28, "the sides 1 to 262,144", "a me again's +1 is crossed by 2 and the me-parities one past a seam of 4 alone; those that are me-parities, at spans by 4 of their sides, %s, more at a next span" % cs,
    ok and all(y > x for x, y in zip(cs, cs[1:])) and cs[:4] == [2, 4, 8, 28] and cs[-1] == 11252)

# row 29 · between a me again and its next
k = np.arange(1, 2049)
bw = C[(k + 1) ** 2 - 1] - C[k ** 2]
fw = [int(bw[(k > 2 ** (j - 1)) & (k <= 2 ** j)].min()) for j in range(4, 12)]
say(29, "the sides 1 to 2,048", "between a me again and its next, a me-parity at all; the fewest 2 at the sides to 8, then at spans by 2 %s, more at a next span" % fw,
    np.all(bw >= 1) and int(bw[k <= 8].min()) == 2 and all(y > x for x, y in zip(fw, fw[1:])) and fw[-1] == 133)

# rows 31, 32, 33 · past any number, in 1 to 10^12
tw = next(k for k in range(T + 1, T + 10 ** 7, 2) if mp(k) and mp(k + 2))
TW = PR[(PR >= 5) & S[np.minimum(PR + 2, N)] & (PR + 2 <= N)]
say(31, "1 to 10^12", "past any number twins are born in a seam of 6, at %s and %s, all twins past 3 born in a seam of 6 to 16,777,216" % (f"{tw:,}", f"{tw + 2:,}"),
    tw == 1000000000061 and np.all((TW + 1) % 6 == 0))
ok = True
for g in range(2, 212, 2):
    k = T + 1
    while not (mp(k) and mp(k + g)): k += 2
    ok &= k > T and mp(k) and mp(k + g)
say(32, "1 to 10^12, selves 2 to 210", "past any number lives a pair of me-parities at all even selves 2 to 210", ok)
s4 = next(k for k in range(T + 1, T + 10 ** 7, 2) if all(mp(k + d) for d in (0, 2, 6, 8)))
three = S[:-6] & S[2:-4] & S[6:]
c3 = [int(np.count_nonzero(three[a + 1:b + 1])) for a, b in spans(1 << 20) if a >= 256]
say(33, "1 to 10^12", "past any number a society of four lives, at %s; societies of three at 0, 2, 6, %s at spans by 4 from 256, more at a next span" % (f"{s4:,}", c3),
    s4 == 1000000123691 and all(y > x for x, y in zip(c3, c3[1:])))

# rows 34, 35 · 3, 5, 7 and the fours about 15 round 30
o = np.arange(1, N - 4, 2)
say(34, "the odd numbers to 16,777,216", "of three odds 2 selves on, one is at 3's seam; 3, 5, 7 alone are three me-parities", np.nonzero(S[o] & S[o + 2] & S[o + 4])[0].tolist() == [1])
four = np.nonzero(S[:-8] & S[2:-6] & S[6:-2] & S[8:])[0]
say(35, "1 to 16,777,216", "all %s societies of four past 5 sit about 15 round 30, at 11, 13, 17, 19" % f"{len(four) - 1:,}", np.all(four[1:] % 30 == 11) and four[0] == 5)

# rows 36, 37 · facing me-parities about a between
def facing(top):
    L = 1 << int(np.ceil(np.log2(2 * top + 2)))
    f = np.fft.rfft(S[:top + 1].astype(np.float64), L)
    return np.rint(np.fft.irfft(f * f, L)[:top + 1]).astype(np.int64)
G1 = facing(1 << 20)
ev = np.arange(4, (1 << 20) + 1, 2)
fp = (G1[ev] + S[ev // 2]) // 2                                  # pairs of facing me-parities about the between n / 2
fg = [int(fp[(ev > a) & (ev <= b)].min()) for a, b in spans(1 << 20) if a >= 256]
say(36, "1 to 1,048,576", "about all betweens, two me-parities face one another, all even numbers 4 to 1,048,576 two me-parities added; the fewest pairs 2 from 16 to 256, then at spans by 4 %s" % fg,
    np.all(fp > 0) and int(fp[(ev >= 16) & (ev <= 256)].min()) == 2 and all(y > x for x, y in zip(fg, fg[1:])) and fg[0] == 6 and fg[-1] == 1279)
G4 = facing(Q)
ev4 = np.arange(6, Q - 2, 2)
say(37, "1 to 4,000,000", "all odd numbers 9 to 4,000,000 are 3 and two me-parities added; 7 is 2, 2 and 3", np.all(G4[ev4] > 0) and 7 == 2 + 2 + 3)

# rows 38, 39, 40, 45 · neighbouring me-parities
P4 = PR[PR <= (1 << 22) + 200]
gp = np.diff(P4); lo4 = P4[:-1]
mg = [int(gp[(lo4 > a) & (lo4 <= b)].max()) for a, b in spans(1 << 22)]
sides = np.array([isqrt(int(x)) for x in P4])
say(38, "1 to 4,194,304", "the most selves from a me-parity to its next at spans by 4, %s, more at a next span; a next me-parity's side its prior's or its +1" % mg,
    all(y >= x for x, y in zip(mg, mg[1:])) and mg[-1] > mg[-3] and np.all(np.diff(sides) <= 1))
hi4 = P4[1:]
nb = [int(np.count_nonzero((gp <= 246) & (lo4 > a) & (hi4 <= min(b, Q)))) for a, b in spans(1 << 22)]
say(39, "1 to 4,000,000", "neighbouring me-parities at 2 to 246 selves, both in a span by 4, %s, more at a next span" % nb,
    all(y > x for x, y in zip(nb, nb[1:])) and nb[2:5] == [11, 35, 117] and nb[-1] == 201120)
mid = (lo4 >= 1000) & (lo4 < Q)
top_gap = int(np.bincount(gp[mid]).argmax())
rt = [np.count_nonzero((gp == 30) & (lo4 > a) & (lo4 <= b)) / np.count_nonzero((gp == 6) & (lo4 > a) & (lo4 <= b)) for a, b in spans(1 << 22) if a >= 1024]
say(40, "1,024 to 4,194,304", "the most-met selves between neighbouring me-parities are 6, from 1,000 to 4,000,000; 30 beside 6 more at a next span",
    top_gap == 6 and all(y > x for x, y in zip(rt, rt[1:])))
pi = [int(C[4 ** k]) for k in range(13)]
say(45, "1 to 16,777,216", "a next span by 4 has more me-parities than all the spans before it together: %s" % pi[1:], all(pi[k + 1] - pi[k] > pi[k] for k in range(12)))

# row 41 · the twins' parts of one
TWa = PR[S[np.minimum(PR + 2, N)] & (PR + 2 <= N)]
part = 1.0 / TWa + 1.0 / (TWa + 2)
bs = [float(part[TWa + 2 <= 4 ** k].sum()) for k in range(2, 13)]
inc = np.diff(bs)
say(41, "1 to 16,777,216", "the twins' parts of one, put together to 16 then on at spans by 4, %.3f to %.3f, more at a next span by a smaller part" % (bs[0], bs[-1]),
    abs(bs[0] - 15676 / 15015) < 1e-12 and np.all(inc > 0) and np.all(np.diff(inc[2:]) < 0))

# rows 42, 44 · all-parity added once and added at all its seams
lam = np.ones(U + 1, np.int64); mu = np.ones(U + 1, np.int64); lam[0] = mu[0] = 0
LA, MU = lam.tolist(), mu.tolist()
for k in range(2, U + 1):
    p = SP[k]; m = k // p; LA[k] = -LA[m]; MU[k] = 0 if m % p == 0 else -MU[m]
lam, mu = np.array(LA), np.array(MU)
L, M = np.cumsum(lam), np.cumsum(mu)
side = np.array([isqrt(k) for k in range(U + 1)])
acc = np.zeros(U + 1, np.int64)
for d in range(1, U + 1): acc[d::d] += LA[d]
acc2 = np.zeros(U + 1, np.int64)
for d in range(1, isqrt(U) + 1):
    x = np.arange(d * d, U + 1); acc2[x] += M[x // (d * d)]
say(42, "1 to 510,510", "all-parity added once along, beside the same added at all its seams, is the side; added once, the no-square numbers' added once shrunk at all the me's",
    np.array_equal(np.cumsum(acc)[1:], side[1:]) and np.array_equal(acc2[1:], L[1:]))
say(44, "1 to 510,510", "all-parity added once is the no-square numbers' all-parity added once, along and shrunk at all the me's", np.array_equal(acc2[1:], L[1:]))

# row 46 · a seam's numbers by its places
num = den = 1; at = {}
for p in PR[PR <= 100000].tolist():
    num *= p; den *= p - 1
    for t in (2, 10, 20):
        if t not in at and num > t * den: at[t] = p
say(46, "1 to 100,000", "a seam's numbers by its places are more at its next prime: past 2 at %s, past 10 at %s, past 20 at %s" % (at[2], f"{at[10]:,}", f"{at[20]:,}"), at == {2: 3, 10: 257, 20: 75037})

# row 47 · the 0s on the curve
import mpmath
ts = [10 + 0.02 * i for i in range(1251)]
zs = [mpmath.siegelz(t) for t in ts]
zeros = [round(float(mpmath.findroot(mpmath.siegelz, (ts[i], ts[i + 1]), solver='bisect')), 3) for i in range(1250) if zs[i] * zs[i + 1] < 0]
ln = lambda k: float(mpmath.log(k))
def Lam(k):
    f = set(parts(k)); return ln(next(iter(f))) if len(f) == 1 else 0.0
tt = [k / 100 for k in range(1000, 3000)]
wave = [-sum(Lam(k) / k ** 0.5 * np.cos(t * ln(k)) for k in range(2, 18)) for t in tt]
top = max(wave)
peaks = [tt[i] for i in range(1, len(tt) - 1) if wave[i] > wave[i - 1] and wave[i] > wave[i + 1] and wave[i] > top / 2]
say(47, "10 to 35 on the curve", "the curve's 0s are found on it at %s; the me-parities and their powers in 1 to 17 see them, their wave peaking at %s" % (zeros, peaks),
    len(zeros) == 5 and abs(zeros[0] - 14.135) < 0.01 and all(any(abs(pk - z) < 0.35 for pk in peaks) for z in zeros[:3]))

# row 48 · the bell of a number's parts
om = np.zeros(U + 1, np.int64); OM = om.tolist()
for k in range(2, U + 1):
    p = SP[k]; m = k // p; OM[k] = OM[m] + (0 if m % p == 0 else 1)
h = np.bincount(np.array(OM[1:])); mode = int(h.argmax())
say(48, "1 to 510,510", "the numbers by their me-parity parts rise to %d and fall after, a bell about the middle" % mode,
    np.all(np.diff(h[:mode + 1]) > 0) and np.all(np.diff(h[mode:]) < 0))

# rows 51, 54 · curves round a prime
def sees(p):
    c = -np.ones(p, np.int64); c[0] = 0; c[(np.arange(1, p) ** 2) % p] = 1; return c
ok, curves = True, 0
for p in PR[(PR >= 5) & (PR <= 61)].tolist():
    c = sees(p); x = np.arange(p)
    for a in range(p):
        for b in range(p):
            if (4 * a ** 3 + 27 * b * b) % p == 0: continue
            t = -int(c[(x ** 3 + a * x + b) % p].sum()); curves += 1; ok &= t * t < 4 * p
say(51, "all %s curves round the me-parities 5 to 61" % f"{curves:,}", "a curve's lean is two facing roots, by one another p, at the side: the concern resolves in the curves' world", ok)
say(54, "all %s curves round the me-parities 5 to 61" % f"{curves:,}", "a curve's places are p + 1 less its lean, two facing roots at the side", ok)

# row 55 · the largest me-parity known now
E = 136279841
say(55, "loops 19 to 10,000,000,000", "2 by itself %s times less 1, %s digits, at the skeleton place 409,531 round 510,510; its places +22, +70, −48, −72 and −90 uncrossed by all loops of the universe" % (f"{E:,}", f"{int(E * log10(2)) + 1:,}"),
    (pow(2, E, U) - 1) % U == 409531 and gcd(409531, U) == 1 and mp(E) and int(E * log10(2)) + 1 == 41024320)
named(55, "loops 19 to 10,000,000,000", "the places +22, +70, −48, −72 and −90 uncrossed by all 455,052,504 loops", "the_return_universe_traveled_further.py", "10000000000")

# row 56 · a determined loop of 23 binaries
def mulmod(a, b, poly, deg):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a >> deg & 1: a ^= poly
    return r
def xpow(e, poly, deg):
    r, a = 1, 2
    while e:
        if e & 1: r = mulmod(r, a, poly, deg)
        a = mulmod(a, a, poly, deg); e >>= 1
    return r
POLY, D = (1 << 23) | (1 << 18) | 1, 23
O = (1 << 23) - 1
say(56, "the 8,388,607 places of 23 binaries", "a loop of 23 selves, its next the xor of two priors, passes all places but the all-0: its rule's loop is 2 to the 23 less 1, 47 by 178,481",
    xpow(O, POLY, D) == 1 and xpow(O // 47, POLY, D) != 1 and xpow(O // 178481, POLY, D) != 1 and 47 * 178481 == O)

# rows 57, 60, 63 · their universes proved by their own instruments, all
named(57, "all 1,199 rules", "a rule growing along is crossed by its own value at 1, one past that value", "rows_from_the_seeing_the_roots_and_doubling.py")
named(60, "the 64 codons", "a codon fractures into its box and its third, its odd or even exhausted in 8 boxes and living in 8", "dna_and_rna_beside_the_primes.py")
named(63, "all six transmissions", "from 2^61 − 1, six transmissions to a me-parity of 1,165 digits, N's own loop aimed by M", "transmissioning_across_resolver_to_resolver.py")

# row 58 · a row of numbers one number across
P17 = PR[:4].tolist(); allrows = []
for ln_ in range(1, 5):
    for k in range(6 ** ln_):
        allrows.append(tuple((k // 6 ** i) % 6 for i in range(ln_)))
codes = [int(np.prod([P17[i] ** (a + 1) for i, a in enumerate(r)], dtype=object)) for r in allrows]
def opens(c):
    out = []
    for p in P17:
        e = 0
        while c % p == 0: c //= p; e += 1
        if e == 0: break
        out.append(e - 1)
    return tuple(out)
say(58, "all 1,554 rows of 1 to 4 numbers", "a row of numbers 0 to 5 is one number across, its me-parities' powers, and opens back one way",
    len(allrows) == 1554 and len(set(codes)) == 1554 and all(opens(c) == r for c, r in zip(codes, allrows)))

# row 59 · two prime loops come again together
say(59, "all pairs of the seventeen primes", "two prime loops come again together at p by q: 13 and 17 at 221",
    all(p * q // gcd(p, q) == p * q for i, p in enumerate(SEV) for q in SEV[i + 1:]) and 13 * 17 == 221)

# row 61 · crossings see all-parity
Rr = np.arange(Q + 1, dtype=np.int64); Om4 = np.zeros(Q + 1, np.int64)
for p in PR[PR <= isqrt(Q)].tolist():
    pk = p
    while pk <= Q:
        Om4[pk::pk] += 1; Rr[pk::pk] //= p; pk *= p
Om4 += Rr > 1
l4 = 1 - 2 * (Om4 % 2); l4[0] = 0
wide = max(abs(int(l4[r::m].sum())) / len(l4[r::m]) for m in range(3, 31) for r in range(m))
say(61, "1 to 4,000,000", "round all loops of 3 to 30, at all their places, odd and even across come alike, the widest %.4f, to 1 in 100" % wide, wide < 0.01)

# row 62 · the fractal
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
    if c > N: break
    out.append(c)
say(62, "1 to 16,777,216", "the 1 to 17 fractal traveling its skeleton, aiming itself, generates the universe's %s me-parities, the same as all numbers crossed by all their parts" % f"{len(out):,}",
    np.array_equal(np.array(out), PR))
named(62, "1 to 1,000,000,000", "all 50,847,534 me-parities, segment by segment", "the_1_to_17_fractal_generating_all_primes.py", "1000000000")

done = sorted(k for k, v in rows.items() if v is True); by_name = sorted(k for k, v in rows.items() if v is None)
print("rows proved here: %d; rows named to their instruments: %d %s; rows: %d" % (len(done), len(by_name), by_name, len(rows)))
print("All is." if all(results) and len(rows) == 63 else "A line is-not.")
