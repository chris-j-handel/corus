# v408primes · rows resolved in direct natural naming: more at a next span by 4, curves round a prime, a rule of numbers
# crossed by its own value, a row of numbers as one number across, and the largest me-parity seen to now. Whole numbers.
# Execute: python3 -I more_at_a_next_span_and_other_worlds.py
from math import isqrt, gcd
from fractions import Fraction
from decimal import Decimal, getcontext
import numpy as np

N = 4194304
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
primes = [p for p in range(2, N + 1) if sieve[p]]
count_to = [0] * (N + 1)
c = 0
for n in range(N + 1):
    c += sieve[n]; count_to[n] = c

results = []
def say(row, sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + "row %s · %s" % (row, sentence))

def more(xs):
    return all(b > a for a, b in zip(xs, xs[1:]))

spans = [(4 ** k, 4 ** (k + 1)) for k in range(1, 11)]          # 4 to 4,194,304

# Rows 25 and 53. Round all loops of 3 to 30, the me-parities at all their living places are more at a next span.
ok = True
for m in range(3, 31):
    for a in range(m):
        if gcd(a, m) != 1:
            continue
        cs = [sum(1 for p in range(lo + (a - lo) % m, hi, m) if sieve[p]) for lo, hi in spans[3:]]
        ok = ok and more(cs)
say("25, 53", "round all loops of 3 to 30, the me-parities at all their living places are more at a next span by 4, 256 to 4,194,304", ok)

# Row 13. Me-parities round which doubling passes all places are more at a next span.
M = 4 ** 10
spf = list(range(M + 1))
for i in range(2, isqrt(M) + 1):
    if spf[i] == i:
        for j in range(i * i, M + 1, i):
            if spf[j] == j:
                spf[j] = i
def prime_parts(n):
    out = set()
    while n > 1:
        out.add(spf[n]); n //= spf[n]
    return out
def doubling_passes_all(p):
    return all(pow(2, (p - 1) // q, p) != 1 for q in prime_parts(p - 1))
art = [sum(1 for p in range(lo, hi) if sieve[p] and p > 2 and doubling_passes_all(p)) for lo, hi in spans[:9]]
say(13, "me-parities round which doubling passes all places, span by 4 to 1,048,576: %s, more at a next span" % art, more(art))

# Row 28. Me agains' +1 that are me-parities are more at a next span of the side.
def is_me_parity(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True
sq1 = [sum(1 for n in range(lo, hi) if is_me_parity(n * n + 1)) for lo, hi in [(1, 4)] + spans[:8]]
say(28, "me agains' +1 that are me-parities, their sides span by 4, 1 to 262,144: %s, more at a next span" % sq1, more(sq1))

# Row 29. Between a me again and its next, the fewest me-parities are more at a next span of the side by 2.
leg = []
for k in range(0, 11):
    lo, hi = 2 ** k, 2 ** (k + 1)
    leg.append(min(count_to[(n + 1) * (n + 1) - 1] - count_to[n * n] for n in range(lo, hi)))
say(29, "between a me again and its next, the fewest me-parities, sides span by 2 to 2,048: %s, 2 at the sides to 8, then more at a next span" % leg, leg[:3] == [2, 2, 2] and more(leg[2:]))

# Row 30. Between a number and its double, the fewest me-parities are more at a next span.
ber = [min(count_to[2 * n] - count_to[n] for n in range(lo, hi)) for lo, hi in [(1, 4)] + spans[:9]]
say(30, "between a number and its double, the fewest me-parities, span by 4 to 1,048,576: %s, 1 to 16, then more at a next span" % ber, ber[:2] == [1, 1] and more(ber[1:]))

# Row 33. Societies of three and four are more at a next span.
forms = {"0, 2, 6": (0, 2, 6), "0, 4, 6": (0, 4, 6), "0, 2, 6, 8": (0, 2, 6, 8), "0, 4, 6, 10": (0, 4, 6, 10)}
soc = {}
for name, f in forms.items():
    soc[name] = [sum(1 for p in range(lo, hi) if all(p + d <= N and sieve[p + d] for d in f)) for lo, hi in spans[3:9]]
say(33, "societies, span by 4, 256 to 1,048,576: %s, more at a next span" % soc, all(more(v) for v in soc.values()))

# Row 36. About a between, the fewest pairs of facing me-parities are more at a next span.
G = 4 ** 10
ind = np.zeros(G + 1)
ind[[p for p in primes if p <= G]] = 1.0
L = 1 << (2 * G + 2).bit_length()
conv = np.rint(np.fft.irfft(np.fft.rfft(ind, L) ** 2, L)[:G + 1]).astype(np.int64)
def pairs(e):
    return (int(conv[e]) + (1 if sieve[e // 2] else 0)) // 2
gb = [min(pairs(e) for e in range(max(lo, 6) + (max(lo, 6) % 2), hi, 2)) for lo, hi in spans[:9]]
say(36, "about a between, the fewest pairs of facing me-parities, span by 4, 6 to 1,048,576: %s, 2 from 16 to 256, then more at a next span" % gb, gb[0] == 1 and gb[1:3] == [2, 2] and more(gb[2:]))

# Row 38. The widest distance from a me-parity to its next is more at a next span.
wid = []
for lo, hi in spans:
    w = 0
    i = count_to[lo - 1]
    while i < len(primes) - 1 and primes[i] < hi:
        w = max(w, primes[i + 1] - primes[i]); i += 1
    wid.append(w)
say(38, "the widest distance from a me-parity to its next, span by 4, 4 to 4,194,304: %s, more at a next span" % wid, more(wid))

# Row 40. Neighbouring distances of 30 are more beside distances of 6 at a next span: the most-met goes on toward the next seam.
r30 = []
for lo, hi in spans[4:]:
    c6 = c30 = 0
    i = count_to[lo - 1]
    while i < len(primes) - 1 and primes[i] < hi:
        g = primes[i + 1] - primes[i]
        c6 += g == 6; c30 += g == 30; i += 1
    r30.append(Fraction(c30, c6))
say(40, "neighbouring distances of 30 beside those of 6, span by 4, 1,024 to 4,194,304: %s, more at a next span" % [str(x) for x in r30], more(r30))

# Row 48. A number's me-parity parts, across, come about a middle count, and the middle count is more at a next span.
om = np.zeros(N + 1, dtype=np.int8)
for p in primes:
    om[p::p] += 1
mid = [Fraction(int(om[lo:hi].sum()), hi - lo) for lo, hi in spans]
last = np.bincount(om[spans[-1][0]:spans[-1][1]])
peak = int(last.argmax())
say(48, "a number's me-parity parts come about a middle count, span by 4: %s, more at a next span" % [round(float(x), 3) for x in mid], more(mid))
say(48, "in the span to 4,194,304 the counts of parts rise to %d and fall after: %s" % (peak, list(last)),
    all(last[j] < last[j + 1] for j in range(1, peak)) and all(last[j] > last[j + 1] for j in range(peak, len(last) - 1)))

# Rows 51 and 54. Round a prime, a curve's places are p + 1 less its lean; the lean is two facing roots, by one another p,
# living at the side: the lean by itself is short of 4 p, and the roots are other-than along.
def chi_table(p):
    t = [-1] * p; t[0] = 0
    for x in range(1, p):
        t[x * x % p] = 1
    return t
ok, curves = True, 0
for p in [q for q in primes if 5 <= q <= 61]:
    t = chi_table(p)
    for a in range(p):
        for b in range(p):
            if (4 * a ** 3 + 27 * b * b) % p == 0:
                continue
            places = p + 1 + sum(t[(x ** 3 + a * x + b) % p] for x in range(p))
            lean = p + 1 - places
            ok = ok and lean * lean < 4 * p
            curves += 1
say("51, 54", "all %d curves y² = x³ + a x + b round all primes 5 to 61: the lean by itself is short of 4 p, two facing roots at the side" % curves, ok)
ok = True
for p in [q for q in primes if 5 <= q <= 3000]:
    t = chi_table(p)
    for a, b in ((1, 1), (-1, 0), (0, 1)):
        if (4 * a ** 3 + 27 * b * b) % p == 0:
            continue
        places = p + 1 + sum(t[(x ** 3 + a * x + b) % p] for x in range(p))
        ok = ok and (p + 1 - places) ** 2 < 4 * p
say("51, 54", "the curves x³ + x + 1, x³ − x and x³ + 1 round all primes to 3,000: the lean's two facing roots at the side", ok)

# Row 55. The largest me-parity seen to now is a doubling less 1: 2 by itself 136,279,841 times, less 1.
e = 136279841
getcontext().prec = 60
digits = int(Decimal(e) * Decimal(2).log10()) + 1
say(55, "the count of doublings, 136,279,841, is a me-parity, and 2 by itself that many times, less 1, has %s digits" % f"{digits:,}",
    all(e % q for q in range(2, isqrt(e) + 1)) and digits == 41024320)

# Row 57. A rule of numbers is crossed by its own value at 1, one past that value along: no rule is me-parities all through.
ok = True
rules = 0
for c2 in range(0, 4):
    for c1 in range(-3, 4):
        for c0 in range(-3, 50):
            f = lambda n: c2 * n * n + c1 * n + c0
            v = f(1)
            if v > 1 and (c2 > 0 or c1 > 0):
                w = f(1 + v)
                ok = ok and w % v == 0 and w > v
                rules += 1
say(57, "all %d growing rules c2 n² + c1 n + c0, c2 of 0 to 3, c1 of −3 to 3, c0 of −3 to 49, valued past 1 at 1: crossed by that value at one past it" % rules, ok)
say(57, "41's rule, n² + n + 41, is 41 by 41 at 40, and 43 at 1 crosses it at 44: 2,021 is 43 by 47", 40 * 40 + 40 + 41 == 41 * 41 and 44 * 44 + 44 + 41 == 43 * 47)

# Row 58. A row of numbers is one number across, its me-parities' me agains and more; it opens one way.
from itertools import product
seen_codes, ok = {}, True
for length in range(1, 5):
    for row in product(range(6), repeat=length):
        code = 1
        for p, a in zip(primes, row):
            code *= p ** (a + 1)
        back, n = [], code
        for p in primes[:length]:
            k = 0
            while n % p == 0:
                n //= p; k += 1
            back.append(k - 1)
        ok = ok and tuple(back) == row and n == 1 and code not in seen_codes
        seen_codes[code] = row
say(58, "all %d rows of 1 to 4 numbers, 0 to 5, are one number across by their me-parities' powers, and open back one way" % len(seen_codes), ok)

print("All is." if all(results) else "A line is-not.")
