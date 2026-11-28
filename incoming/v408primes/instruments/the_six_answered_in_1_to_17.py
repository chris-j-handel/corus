# v408primes · the six rows with more competency possible, answered in 1 to 17, and from any number: odd numbers whose
# parts make their double, doubling closing round a prime's own me again, rows at equal selves past 13, the twins' parts
# of one put together, the 0s found on the curve, and crossings about any number. Whole numbers, and the curve's 0s.
# Execute: python3 -I the_six_answered_in_1_to_17.py [any numbers to 10^12]
import sys, secrets, math
from math import isqrt, gcd
from fractions import Fraction
import numpy as np

given = [int(a.replace(',', '')) for a in sys.argv[1:] if a.replace(',', '').isdigit()]
taken = [n for n in given if 30 <= n <= 10 ** 12] or [10 ** 6 + 1, 10 ** 9 + 7, 10 ** 12 - 11, secrets.randbelow(10 ** 12 - 100) + 50]

results = []
def say(row, sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + "row %s · %s" % (row, sentence))

def sieve_to(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = False
    return s
S = sieve_to(50_000_000)
P17 = [p for p in range(2, 18) if S[p]]

def parts(n):
    out, q = {}, 2
    while q * q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1; n //= q
        q += 1 if q == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out
def sigma(n):
    t = 1
    for p, k in parts(n).items():
        t *= (p ** (k + 1) - 1) // (p - 1)
    return t

# Row 15. Odd numbers whose parts make their double.
odd17 = {n: sigma(n) for n in range(1, 18, 2)}
say(15, "in 1 to 17, the odd numbers' parts make %s: none its double; 6, a doubling by a doubling less 1, 2 by 3, makes 12, its double"
    % odd17, all(v != 2 * n for n, v in odd17.items()) and sigma(6) == 12 and 3 == 2 * 2 - 1)
M = 1_000_000
sig = np.zeros(M + 1, dtype=np.int64)
for d in range(1, M + 1):
    sig[d::d] += d
odd_sq = all((int(sig[n]) % 2 == 1) == (isqrt(n) ** 2 == n) for n in range(1, 100001, 2))
say(15, "an odd number's parts make an odd number at a me again, at no other, all odd numbers to 100,000", odd_sq)
shape_ok = True
for n in range(1, 100001, 2):
    if int(sig[n]) % 4 == 2:
        oddexp = [(p, k) for p, k in parts(n).items() if k % 2 == 1]
        shape_ok = shape_ok and len(oddexp) == 1 and oddexp[0][0] % 4 == 1 and oddexp[0][1] % 4 == 1
say(15, "parts making twice an odd number, as a double would, come at a me again but for one me-parity aiming prior, to a power one past a seam of 4: all odd numbers to 100,000", shape_ok)
none_odd = not any(int(sig[n]) == 2 * n for n in range(1, M + 1, 2))
evens = [n for n in range(2, M + 1, 2) if int(sig[n]) == 2 * n]
say(15, "to 1,000,000, no odd number's parts make its double; the even ones are %s, all a doubling by a doubling less 1" % evens,
    none_odd and all(any(n == (1 << (e - 1)) * ((1 << e) - 1) for e in range(2, 21)) for n in evens))
ok = True
for n in taken:
    o = n if n % 2 else n + 1
    ok = ok and sigma(o) != 2 * o
say(15, "from any odd number given or drawn, its parts are not its double: %s" % [n if n % 2 else n + 1 for n in taken], ok)

# Row 17. Doubling closing round a prime's own me again.
def loop(a, m):
    k, x = 1, a % m
    while x != 1:
        x = x * a % m; k += 1
    return k
in17 = {p: (loop(2, p), loop(2, p * p)) for p in P17 if p > 2}
say(17, "in 1 to 17, round a me-parity's me again doubling's loop is the prime's loop by the prime: %s" % in17,
    all(b == a * p for p, (a, b) in in17.items()))
closing = [int(p) for p in np.nonzero(S[:10_000_001])[0] if p > 2 and pow(2, int(p) - 1, int(p) * int(p)) == 1]
say(17, "to 10,000,000, doubling closes round a prime's own me again at its prior at %s, and at no other" % closing, closing == [1093, 3511])
ok = True
for n in taken:
    p = n + 1
    while not (S[p] if p < len(S) else all(p % q for q in range(2, isqrt(p) + 1))):
        p += 1
    ok = ok and pow(2, p - 1, p * p) != 1
say(17, "from any number given or drawn, its next me-parity's me again has doubling's loop the prime's loop by the prime", ok)

# Row 27. Rows of me-parities at equal selves past 13.
rows17 = [(a, d) for d in range(2, 9, 2) for a in range(2, 18) if a + 2 * d <= 17 and S[a] and S[a + d] and S[a + 2 * d]]
say(27, "in 1 to 17, rows of three at equal selves: %s; the one at 2 selves holds 3, the others at seams of 2 and 3, or holding 3"
    % rows17, (3, 2) in rows17 and (5, 6) in rows17)
best = None
primes = np.nonzero(S)[0]
for d in range(30030, 420421, 30030):
    a = primes[primes + 13 * d < len(S)]
    keep = np.ones(len(a), dtype=bool)
    for j in range(1, 14):
        keep &= S[a + j * d]
    if keep.any():
        a0 = int(a[keep][0])
        if best is None or a0 + 13 * d < best[0] + 13 * best[1]:
            best = (a0, d)
say(27, "by the seam's selves, a row of 14 me-parities: %s + %s n, n of 0 to 13, its last %s" % (f"{best[0]:,}", f"{best[1]:,}", f"{best[0] + 13 * best[1]:,}") if best else "no row of 14 found",
    best is not None and all(S[best[0] + j * best[1]] for j in range(14)) and best[1] % 30030 == 0)

# Row 41. The twins' parts of one, put together along.
tw17 = [(p, p + 2) for p in P17 if p + 2 <= 17 and S[p + 2]]
f17 = sum(Fraction(1, p) + Fraction(1, q) for p, q in tw17)
say(41, "in 1 to 17, the twins %s put their parts of one together to %s" % (tw17, f17), f17 == Fraction(1, 3) + Fraction(2, 5) + Fraction(1, 7) + Fraction(1, 11) + Fraction(1, 13))
U = 10 ** 15
tw = primes[(primes + 2 < len(S))]
tw = tw[S[tw + 2]]
units = (U // tw) + (U // (tw + 2))
sp = [(4 ** k, 4 ** (k + 1)) for k in range(1, 12)]
put = [int(units[tw < hi].sum()) for lo, hi in sp]
more_by = [b - a for a, b in zip(put, put[1:])]
say(41, "put together along, in parts of 10^15, to 4^k for k 2 to 12: %s; more at a next span, by a smaller part from 4^7" % [round(x / U, 6) for x in put],
    all(m > 0 for m in more_by) and all(b < a for a, b in zip(more_by[5:], more_by[6:])))

# Row 47. The 0s found on the curve, and seen from the me-parities in 1 to 17.
def theta(t):
    return t / 2 * math.log(t / (2 * math.pi)) - t / 2 - math.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)
def Z(t):
    a = math.sqrt(t / (2 * math.pi)); N = int(a); p = a - N
    main = 2 * sum(math.cos(theta(t) - t * math.log(n)) / math.sqrt(n) for n in range(1, N + 1))
    c0 = math.cos(2 * math.pi * (p * p - p - 1 / 16)) / math.cos(2 * math.pi * p)
    return main + (-1) ** (N - 1) * a ** -0.5 * c0
zeros, t = [], 10.0
while t < 35:
    if Z(t) * Z(t + 0.01) < 0:
        lo, hi = t, t + 0.01
        for _ in range(40):
            mid = (lo + hi) / 2
            if Z(lo) * Z(mid) <= 0:
                hi = mid
            else:
                lo = mid
        zeros.append(round((lo + hi) / 2, 3))
    t += 0.01
say(47, "the curve's 0s from 10 to 35, found on the curve: %s" % zeros, len(zeros) == 5 and abs(zeros[0] - 14.135) < 0.01)
def lam(n):
    f = parts(n)
    return math.log(next(iter(f))) if len(f) == 1 else 0.0
ts = [k / 100 for k in range(1000, 3000)]
wave = [-sum(lam(n) / math.sqrt(n) * math.cos(tt * math.log(n)) for n in range(2, 18)) for tt in ts]
top = max(wave)
peaks = [ts[i] for i in range(1, len(ts) - 1) if wave[i] > wave[i - 1] and wave[i] > wave[i + 1] and wave[i] > top / 2]
say(47, "the me-parities and their powers in 1 to 17 see the curve's first 0s, their wave's peaks at %s" % peaks,
    len(peaks) >= 3 and all(any(abs(pk - z) < 0.35 for pk in peaks) for z in zeros[:3]))

# Row 61. Crossings about any number: round its loops, odd and even across alike.
odd17 = sum(1 for n in range(2, 18) if sum(parts(n).values()) % 2 == 1)
say(61, "in 1 to 17, odd across %d and even across %d, 1 among them: alike" % (odd17, 17 - odd17), odd17 == 9)
ok, widest = True, Fraction(0)
W = 100000
for n in taken:
    lo = n; hi = n + W
    rem = np.arange(lo, hi, dtype=np.int64); odd = np.zeros(W, dtype=np.uint8)
    for p in primes[primes <= isqrt(hi) + 1].tolist():
        pk = p
        while pk < hi:
            st = (-lo) % pk
            odd[st::pk] ^= 1; rem[st::pk] //= p
            pk *= p
    odd ^= (rem > 1).astype(np.uint8)
    for m in range(3, 31):
        for a in range(m):
            sel = odd[(a - lo) % m::m]
            o = int(sel.sum()); c = len(sel)
            widest = max(widest, Fraction(abs(2 * o - c), c))
say(61, "about any number given or drawn, in 100,000 numbers on, round all loops of 3 to 30 at all their places, odd and even across alike to %s at the widest" % (round(float(widest), 4)),
    widest < Fraction(1, 10))

print("All is." if all(results) else "A line is-not.")
