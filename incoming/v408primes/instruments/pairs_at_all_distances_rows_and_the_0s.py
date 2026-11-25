# v408primes · the hardest rows: the 0s spaced like energy levels, co-possiblings at all distances, the widest and the
# bounded distances, long rows equally apart, and crossing and unrelationing, by societies resolver to resolver. Whole numbers.
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

def uncrossed(form, primes):
    c = 1
    for r in primes:
        c *= r - len({(-x) % r for x in form})
    return c

# A pair of me-parities d apart, a society at 0 and d, is uncrossed round r at r − 1 of r with r crossing d, and r − 2 with r not.
odd_primes = [3, 5, 7, 11, 13]
dists = [2, 4, 6, 8, 10, 12, 14, 30]
seam_counts = {d: uncrossed([0, d], odd_primes) for d in dists}
shares = {d: Fraction(seam_counts[d], seam_counts[2]) for d in dists}
say("47, 32", "a pair d apart, uncrossed round 30,030, the seam of 2 to 13: %s; beside the twins, %s" % (seam_counts, {d: str(v) for d, v in shares.items()}),
    seam_counts[2] == 1485 and shares[6] == 2 and shares[30] == Fraction(8, 3) and shares[4] == 1)

# Pairs of me-parities to 4,000,000 are to the twins' as the seam's uncrossed places are.
living = {d: sum(1 for p in range(3, N) if sieve[p] and sieve[p + d]) for d in dists}
ratio_thousandths = {d: (1000 * living[d]) // living[2] for d in dists}
say(47, "living pairs d apart to 4,000,000: %s; beside the twins, in thousandths: %s" % (living, ratio_thousandths),
    all(abs(Fraction(living[d], living[2]) - shares[d]) < Fraction(1, 10) * shares[d] for d in dists))

# Row 32. All even distances are uncrossed round all seams: r − 1 or r − 2 of r, never none past 3.
say(32, "no prime crosses all of a pair's places: r − 1 or r − 2 of r uncrossed, all even distances to 2,000, primes to 59",
    all(uncrossed([0, d], [p for p in PR if p > 2]) > 0 for d in range(2, 2001, 2)))
gaps_seen = set()
last = 2
for n in range(3, N):
    if sieve[n]:
        gaps_seen.add(n - last)
        last = n
say(32, "as distances from a me-parity to its next, all even distances 2 to 100 are distances from a me-parity to its next below 4,000,000",
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

# Row 27. A row of k me-parities equally d apart is uncrossed round all seams only with d a seam of all primes to k, unless the
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
        c = uncrossed([j * d for j in range(k)], [p for p in PR if p > 2])
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
say(27, "rows equally apart uncrossed round all seams only with their distance a seam of the primes to their length, k of 3 to 8, distances to 400", ok)
say(27, "rows of k me-parities equally apart, a start and a distance: %s; 199 + 210 n is ten" % rows,
    rows[3][:2] == (3, 2) and rows[10] == (199, 210, 2089))


# Row 47. Round a seam, the pairs at all distances together are the places by the places; the distance 0 is the places.
T, places = 210, uncrossed([0], [2, 3, 5, 7])
by_distance = [uncrossed([0, d], [2, 3, 5, 7]) for d in range(T)]
say(47, "round 210, pairs at all distances together are %d, the %d places by themselves; the distance 0 holds %d, every me again its own pair"
    % (sum(by_distance), places, by_distance[0]), sum(by_distance) == places * places and by_distance[0] == places)
T13 = 30030
odd_avg = Fraction(sum(uncrossed([0, d], [3, 5, 7, 11, 13]) for d in range(0, 2 * T13, 2)), T13 * seam_counts[2])
want = Fraction(1)
for r in [3, 5, 7, 11, 13]:
    want *= Fraction((r - 1) * (r - 1), r * (r - 2))
say(47, "round 30,030, the pair shares at all even distances, beside the twins, come to %s on the whole, the product of (r − 1)(r − 1) over r(r − 2)" % odd_avg,
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

# Row 46. A seam's numbers by its places grow at all next primes and pass all whole numbers.
num, den, passes, k = 1, 1, {}, 2
for p in range(2, 100000):
    if sieve[p]:
        num *= p; den *= p - 1
        while num > k * den:
            passes[k] = p; k += 1
say(46, "a seam's numbers by its places pass all whole numbers 2 to %d with primes below 100,000; they pass k at the prime: %s" % (k - 1, passes),
    k - 1 >= 20 and all(passes[j] <= passes[j + 1] for j in range(2, k - 1)))

# Row 41. Twin places round all next seams are more, never fewer: r − 2 of r.
tw = [uncrossed([0, 2], [q for q in [3, 5, 7, 11, 13, 17, 19] if q <= r]) for r in [3, 5, 7, 11, 13, 17, 19]]
say(41, "twin places round the seams of the primes to 3, 5, 7, 11, 13, 17, 19: %s, the next more" % tw, all(b > a for a, b in zip(tw, tw[1:])))
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

# Crossing and unrelationing. A crossing relates a number to a prime other-than it; a me-parity is related to none.
spf = list(range(N + 1))
for i in range(2, isqrt(N) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
odd = bytearray(N + 1)   # 1 for odd across, an odd count of prime parts; 0 for even
for n in range(2, N + 1):
    odd[n] = odd[n // spf[n]] ^ 1
widest = Fraction(0)
for m in range(3, 31):
    for a in range(m):
        o = sum(odd[a or m::m]) if a else sum(odd[m::m])
        c = len(range(a or m, N + 1, m))
        widest = max(widest, Fraction(abs(2 * o - c), c))
say("all-parity", "round all loops of 3 to 30, at all their places, odd and even across come alike, numbers to 4,000,000: apart by %s of a place's numbers at the widest, short of 1 in 100" % widest,
    widest < Fraction(1, 100))
say("all-parity", "a me-parity is related to no prime other-than it: all me-parities to 4,000,000",
    all(spf[p] == p for p in range(2, N + 1) if sieve[p]))

# A me-parity is three parts: its prior, itself and its next. With all three, the parity aims.
say("three", "2 is odd, even, odd: 1, 2, 3, the one me-parity shaped as all-parity", 1 % 2 == 1 and 2 % 2 == 0 and 3 % 2 == 1)
say("three", "past 2, all me-parities to 4,000,000 are even, odd, even: their prior and their next even",
    all((p - 1) % 2 == 0 and (p + 1) % 2 == 0 for p in range(3, N) if sieve[p]))
say("three", "a me-parity's two evens, by 2, are a +1 apart, one odd and one even: the even that is a seam of 4 is at one side",
    all(((p - 1) // 2 + 1 == (p + 1) // 2) and (((p - 1) % 4 == 0) != ((p + 1) % 4 == 0)) for p in range(3, N) if sieve[p]))
two_sq = bytearray(N + 1)
a = 0
while a * a <= N:
    b = a
    while a * a + b * b <= N:
        two_sq[a * a + b * b] = 1
        b += 1
    a += 1
prior = [p for p in range(3, N) if sieve[p] and (p - 1) % 4 == 0]
nxt = [p for p in range(3, N) if sieve[p] and (p + 1) % 4 == 0]
say("three", "aiming prior, a me-parity is two me agains added, all %d to 4,000,000: 5 is 1 and 4, 13 is 4 and 9" % len(prior),
    all(two_sq[p] for p in prior) and two_sq[5] and two_sq[13])
say("three", "aiming next, a me-parity is two me agains added at none, all %d to 4,000,000" % len(nxt), not any(two_sq[p] for p in nxt))
tw_all = [p for p in range(5, N) if sieve[p] and sieve[p + 2]]
say("three", "twins past 3 are about one middle even, a seam of 6: even, odd, even, odd, even, all %d to 4,000,000" % len(tw_all),
    all((p + 1) % 6 == 0 for p in tw_all))
toward = sum(1 for p in tw_all if (p + 1) % 4 == 0)
say("three", "twins aim together at a middle even that is a seam of 12, %d times, and apart %d times, to 4,000,000" % (toward, len(tw_all) - toward),
    all(((p + 1) % 4 == 0) == ((p + 1) % 12 == 0) for p in tw_all))
one, two, other = 0, 0, 0
for n in range(2000000, 4000001):
    if spf[n] >= 159:
        q = n // spf[n]
        if q == 1:
            one += 1
        elif spf[q] == q:
            two += 1
        else:
            other += 1
say("all-parity", "uncrossed by the primes below 159, numbers from 2,000,000 to 4,000,000 are a me-parity, %d, or two me-parities multiplied, %d; none else" % (one, two),
    other == 0 and one > 0 and two > 0)
side_ok = all(sieve[n] for n in range(2000000, 4000001) if spf[n] > 2000)
say("all-parity", "uncrossed by the primes to its side, 2,000, a number from 2,000,000 to 4,000,000 is a me-parity", side_ok and isqrt(4000000) == 2000)

print("All is." if all(results) else "A line is-not.")
