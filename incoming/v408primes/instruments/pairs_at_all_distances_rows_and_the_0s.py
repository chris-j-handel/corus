# v408primes · the hardest rows: the 0s spaced like energy levels, co-possiblings at all distances, the widest and the
# bounded distances, and long rows equally apart, by societies carried resolver to resolver. Whole numbers alone.
# Execute: python3 -I pairs_at_all_distances_rows_and_the_0s.py
from math import isqrt
from fractions import Fraction

N = 4000000
sieve = bytearray([1]) * (N + 400); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N + 399) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
PR = [p for p in range(2, 60) if sieve[p]]

results = []
def say(row, sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + "row %s · %s" % (row, sentence))

def carried(form, primes):
    c = 1
    for r in primes:
        c *= r - len({(-x) % r for x in form})
    return c

# A pair of me-parities d apart, a society at 0 and d, is carried at a turn by r − 1 of r where r crosses d, and r − 2 where not.
odd_primes = [3, 5, 7, 11, 13]
dists = [2, 4, 6, 8, 10, 12, 14, 30]
turn_counts = {d: carried([0, d], odd_primes) for d in dists}
shares = {d: Fraction(turn_counts[d], turn_counts[2]) for d in dists}
say("47, 32", "a pair d apart, carried round the turn of 2 to 13: %s; beside the twins, %s" % (turn_counts, {d: str(v) for d, v in shares.items()}),
    turn_counts[2] == 1485 and shares[6] == 2 and shares[30] == Fraction(8, 3) and shares[4] == 1)

# Living pairs to 4,000,000 stand to the twins' as the turn's carried places do.
living = {d: sum(1 for p in range(3, N) if sieve[p] and sieve[p + d]) for d in dists}
ratio_thousandths = {d: (1000 * living[d]) // living[2] for d in dists}
say(47, "living pairs d apart to 4,000,000: %s; beside the twins, in thousandths: %s" % (living, ratio_thousandths),
    all(abs(Fraction(living[d], living[2]) - shares[d]) < Fraction(1, 10) * shares[d] for d in dists))

# Row 32. All even distances are carried at all turns: r − 1 or r − 2 of r, never none past 3. With all turns.
say(32, "all even distances are carried at all turns, r − 1 or r − 2 of r places kept, none past 3 crossing them all; turns of primes to 59",
    all(carried([0, d], [p for p in PR if p > 2]) > 0 for d in range(2, 2001, 2)))
gaps_seen = set()
last = 2
for n in range(3, N):
    if sieve[n]:
        gaps_seen.add(n - last)
        last = n
say(32, "as distances from a me-parity to its next, all even distances 2 to 100 are lived below 4,000,000",
    all(g in gaps_seen for g in range(2, 101, 2)))

# Row 38. The widest distance from a me-parity to its next, to 4,000,000, and it stays short of twice the me-parity's side and 1.
widest, at, last, ok, sides_ok = 0, 0, 2, True, True
for n in range(3, N):
    if sieve[n]:
        g = n - last
        if g > widest:
            widest, at = g, last
        ok = ok and (g - 1) * (g - 1) < 4 * last
        sides_ok = sides_ok and isqrt(n) <= isqrt(last) + 1
        last = n
say(38, "the widest distance from a me-parity to its next below 4,000,000 is %d, after %d; at all me-parities, the distance less 1, by itself, is short of 4 times the me-parity" % (widest, at), ok)
say(38, "at all me-parities below 4,000,000, the next me-parity's side is the prior's side or its +1", sides_ok)

# Row 39. Me-parities and their next no more than 246 apart come at all spans by 4 stepped, never fewer.
spans = []
for k in range(3, 12):
    lo, hi = 4 ** (k - 1), 4 ** k
    c, last = 0, None
    for n in range(lo, min(hi, N)):
        if sieve[n]:
            if last is not None and n - last <= 246:
                c += 1
            last = n
    spans.append(c)
say(39, "me-parities with their next no more than 246 apart, span by 4, 16 to 4,000,000: %s, never fewer" % spans, all(b >= a for a, b in zip(spans, spans[1:])))

# Row 27. A row of k me-parities equally d apart is carried at all turns only with d a seam of all primes to k, unless the
# row holds such a prime itself: 3, 5, 7; 5, 11, 17, 23, 29; and 199 + 210 n, ten.
def primorial_to(k):
    t = 1
    for p in PR:
        if p <= k:
            t *= p
    return t
ok = True
for k in range(3, 9):
    for d in range(2, 400, 2):
        c = carried([j * d for j in range(k)], [p for p in PR if p > 2])
        ok = ok and ((c > 0) == (d % (primorial_to(k) // 2) == 0 or d % primorial_to(k) == 0))
rows = {}
for k in range(3, 11):
    t = primorial_to(k)
    best = None
    for d in ([2, 6, 30, 150, 210] if k <= 7 else [210]):
        for a in range(2, 3000):
            if all(a + j * d < N and sieve[a + j * d] for j in range(k)):
                last_term = a + (k - 1) * d
                if best is None or last_term < best[2]:
                    best = (a, d, last_term)
                break
    rows[k] = best
say(27, "rows equally apart carried at all turns only with their distance a seam of the primes to their length, k of 3 to 8, distances to 400", ok)
say(27, "rows of k me-parities equally apart, a start and a distance: %s; 199 + 210 n is ten" % rows,
    rows[3][:2] == (3, 2) and rows[10] == (199, 210, 2089))


# Row 47. Round a turn, the pairs at all distances together are the places by the places; the distance 0 holds the me agains.
T, places = 210, carried([0], [2, 3, 5, 7])
by_distance = [carried([0, d], [2, 3, 5, 7]) for d in range(T)]
say(47, "round the turn of 210, pairs at all distances together are %d, the %d places by themselves; the distance 0 holds %d, every me again its own pair"
    % (sum(by_distance), places, by_distance[0]), sum(by_distance) == places * places and by_distance[0] == places)
T13 = 30030
odd_avg = Fraction(sum(carried([0, d], [3, 5, 7, 11, 13]) for d in range(0, 2 * T13, 2)), T13 * turn_counts[2])
want = Fraction(1)
for r in [3, 5, 7, 11, 13]:
    want *= Fraction((r - 1) * (r - 1), r * (r - 2))
say(47, "round the turn of 2 to 13, the pair shares at all even distances, beside the twins, come to %s on the whole, the product of (r − 1)(r − 1) over r(r − 2)" % odd_avg,
    odd_avg == want)

# Rows 27 and 13. Rows equally apart to 13, all below 4,000,000, their distance a seam of the primes to their length.
for k in (11, 12, 13):
    s_ = primorial_to(k)
    best = None
    for d in range(s_, 200001, s_):
        if (k - 1) * d >= N:
            break
        for a in range(2, N - (k - 1) * d):
            if sieve[a] and all(sieve[a + j * d] for j in range(1, k)):
                if best is None or a + (k - 1) * d < best[2]:
                    best = (a, d, a + (k - 1) * d)
                break
    rows[k] = best
say(27, "rows of 11, 12 and 13 me-parities equally apart below 4,000,000, with the least last: %s" % {k: rows[k] for k in (11, 12, 13)},
    all(rows[k] is not None and rows[k][1] % primorial_to(k) == 0 for k in (11, 12, 13)))

# Row 46. A turn's numbers by its places, T over the places kept, grow at every next prime and pass every whole number.
num, den, passes, k = 1, 1, {}, 2
for p in range(2, 100000):
    if sieve[p]:
        num *= p; den *= p - 1
        while num > k * den:
            passes[k] = p; k += 1
say(46, "a turn's numbers by its places pass every whole number 2 to %d with primes below 100,000; they pass k at the prime: %s" % (k - 1, passes),
    k - 1 >= 20 and all(passes[j] <= passes[j + 1] for j in range(2, k - 1)))

# Row 41. Twin places at every next turn are more, never fewer: r − 2 of every r.
tw = [carried([0, 2], [q for q in [3, 5, 7, 11, 13, 17, 19] if q <= r]) for r in [3, 5, 7, 11, 13, 17, 19]]
say(41, "twin places at the turns to 3, 5, 7, 11, 13, 17, 19: %s, every next more" % tw, all(b > a for a, b in zip(tw, tw[1:])))
tspans = []
for kk in range(3, 12):
    lo, hi = 4 ** (kk - 1), min(4 ** kk, N)
    tspans.append(sum(1 for n in range(lo, hi) if sieve[n] and sieve[n + 2]))
say(41, "twins, span by 4, 16 to 4,000,000: %s, never fewer" % tspans, all(b >= a for a, b in zip(tspans, tspans[1:])))

# Row 37. All odd numbers from 7 to 4,000,000 are three me-parities: 2, 2, 3 for 7, and 3 with a between of two for all others.
ok = True
for n in range(9, N, 2):
    m = n - 3
    q = 3
    while not (sieve[q] and sieve[m - q]):
        q += 2
        if q > m // 2:
            ok = False; break
say(37, "all odd numbers 9 to 4,000,000 are 3 with two me-parities about their between; 7 is 2, 2 and 3", ok and sieve[2] and sieve[3])

# The lead. Crossers alone see the me agains and the across, never the lead.
spf = list(range(N + 1))
for i in range(2, isqrt(N) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
lam = bytearray(N + 1)   # 1 for a lead of −1, 0 for +1
for n in range(2, N + 1):
    lam[n] = lam[n // spf[n]] ^ 1
lead = [0] * (N + 1)
for n in range(1, N + 1):
    lead[n] = lead[n - 1] + (-1 if lam[n] else 1)
seams = [d for d in range(1, 1001) if T13 % d == 0]
ok, widest = True, Fraction(0)
for d in seams:
    plus = sum(1 for m in range(d, N + 1, d) if not lam[m])
    minus = N // d - plus
    sign = -1 if lam[d] else 1
    ok = ok and plus - minus == sign * lead[N // d]
    widest = max(widest, Fraction(abs(lead[N // d]), N // d))
say("lead", "for all seams of 2 to 13 to 1,000, numbers to 4,000,000 that the seam crosses, with lead +1 and with lead −1, differ by the lead at the seam's span alone; the widest is %s of the span, short of 1 in 50" % widest,
    ok and widest < Fraction(1, 50))
say("lead", "a me-parity's lead is −1 and a number of two me-parities across has a lead of +1: 7 and 35", lam[7] == 1 and lam[35] == 0)

print("All is." if all(results) else "A line is-not.")
