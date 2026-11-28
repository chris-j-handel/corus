# v408primes · rows of the table resolved farther: the plane and the seeings, the roots of 1 on a crossing's torus,
# doubling's primes, and the stepped rows. Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I rows_from_the_seeing_the_roots_and_doubling.py
from math import isqrt, gcd

N = 4000000
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
def is_prime(n):
    if n <= N:
        return bool(sieve[n])
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
PR = [p for p in range(2, 20000) if sieve[p]]

results = []
def say(row, sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + "row %s · %s" % (row, sentence))

def seen(a, p):
    return 1 if pow(a % p, (p - 1) // 2, p) == 1 else -1

# Row 23. A prime's −1, its loop's last place, is seen as a me again's place when the prime is one past a seam of 4,
# and then the prime is two me agains added, one way alone.
def two_mes(p):
    return [(a, isqrt(p - a * a)) for a in range(1, isqrt(p // 2) + 1) if isqrt(p - a * a) ** 2 == p - a * a]
ok = all((seen(-1, p) == 1) == (p % 4 == 1) and (len(two_mes(p)) == 1) == (p % 4 == 1) and (len(two_mes(p)) == 0) == (p % 4 == 3)
         for p in PR if p > 2)
say(23, "a prime one past a seam of 4 sees its −1 as a me again's place and is two me agains added, one way alone: 13 = 4 + 9, 29 = 4 + 25; one short of a seam of 4, neither; primes to 20,000", ok)

# Row 22. In the plane, a prime one past a seam of 4 is a crossing of two podal plane primes, a + bi and a − bi; a prime
# one short stays whole; 2 is the me again of 1 + i, turned.
def plane_cross(a, b, c, d):
    return (a * c - b * d, a * d + b * c)
ok = all(plane_cross(a, b, a, -b) == (p, 0) for p in PR if p % 4 == 1 for a, b in two_mes(p))
say(22, "in the plane, a prime one past a seam of 4 is a + bi crossed with its podal a − bi: 13 = (2 + 3i)(2 − 3i); one short stays whole; 2 = (1 + i)(1 − i), %s" % (plane_cross(1, 1, 1, -1),),
    ok and plane_cross(1, 1, 1, -1) == (2, 0))

# Row 28. Only primes seeing −1 as a me again's place, and 2, cross a me again's +1: n x n + 1. Stepped, such primes come
# with no last, more at every span.
ok = all(all(p % 4 == 1 or p == 2 for p in PR if p <= n and (n * n + 1) % p == 0) for n in range(1, 3000))
counts = [sum(1 for n in range(2 ** (k - 1), 2 ** k) if is_prime(n * n + 1)) for k in range(4, 12)]
say(28, "a me again's +1 is crossed only by 2 and primes one past a seam of 4; primes one past a me again, between doublings 8 to 2,048, never fewer: %s" % counts,
    ok and all(b >= a for a, b in zip(counts, counts[1:])))

# Row 21. Euler's 41: n x n + n + 41 is a prime for n of 0 to 39, because −163 is seen as other-than from every prime's
# side below 41, and n x n + n + 41 is odd.
ok = all(is_prime(n * n + n + 41) for n in range(40)) and not is_prime(40 * 40 + 40 + 41)
ok = ok and all(seen(-163, p) == -1 for p in PR if 2 < p < 41)
say(21, "n x n + n + 41 is a prime for n of 0 to 39 and 41 x 41 at 40: −163 is seen as other-than from every odd prime's side below 41", ok)

# Row 10. Round a prime, 1 and −1 alone are places whose me again is 1; round a crossing of two odd primes, four are, two
# from its torus's two directions. Halving the across loop finds the other two: a prime told in few moments.
def roots_of_one(n):
    return [x for x in range(1, n) if x * x % n == 1]
ok = all(len(roots_of_one(p)) == 2 for p in PR if 2 < p < 400) and all(len(roots_of_one(p * q)) == 4 for p in PR[1:20] for q in PR[1:20] if p < q)
say(10, "round a prime, 1 and −1 alone have the me again 1; round a crossing of two odd primes, four: round 15, %s" % roots_of_one(15), ok)
def strong(n, a):
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    x = pow(a, d, n)
    if x in (1, n - 1):
        return True
    for _ in range(s - 1):
        x = x * x % n
        if x == n - 1:
            return True
    return False
ok = all((all(strong(n, a) for a in (2, 3, 5, 7) if a % n) == bool(sieve[n])) for n in range(3, 3000000, 2))
say(10, "halving the across loop with 2, 3, 5 and 7 tells every odd number to 3,000,000 prime or crossed, in a few moments each", ok)

# Row 11. A crossing whose parts' across loops all fit its own less one passes as a prime by doubling, and is told by its own
# loop multiplied: 561 = 3 x 11 x 17.
def passes_doubling_all(n):
    return all(pow(a, n - 1, n) == 1 for a in range(2, n) if gcd(a, n) == 1)
def parts(n):
    out, d, m = [], 2, n
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out
korselt = [n for n in range(3, 100000, 2) if not sieve[n] and all((n - 1) % (p - 1) == 0 and n % (p * p) for p in parts(n))]
ok = korselt[:3] == [561, 1105, 1729] and all(passes_doubling_all(n) for n in korselt[:3])
wilson = 1
for k in range(1, 561):
    wilson = wilson * k % 561
say(11, "crossings whose parts' across loops fit their own less one pass as primes by doubling: %s ... %d to 100,000; 561's own loop multiplied is %d, told crossed" % (korselt[:6], len(korselt), wilson),
    ok and wilson == 0)

# Row 52. A place round a prime is a step count along its across loop, living in it: round 11, doubling's steps.
x, steps = 1, {}
for k in range(10):
    steps[x] = k
    x = x * 2 % 11
say(52, "round 11 every place is a step count along doubling's across loop: %s" % dict(sorted(steps.items())), sorted(steps) == list(range(1, 11)))

# Row 16. A prime whose across loop is a doubling halves down to the one me: 3, 5, 17, 257, 65,537, its figure of p sides
# laid by halvings alone; one more than a doubling whose count is no doubling is crossed; 2 to the 32 + 1 = 641 x 6,700,417.
halving = [p for p in range(3, 70000) if sieve[p] and (p - 1) & (p - 2) == 0]
ok = halving == [3, 5, 17, 257, 65537] and (2 ** 32 + 1) == 641 * 6700417
ok = ok and all(not is_prime(2 ** m + 1) for m in range(3, 22) if m & (m - 1))
say(16, "primes whose across loop is a doubling, halving to the one me: %s; one more than a doubling of no doubling's count is crossed; 2 to the 32 + 1 = 641 x 6,700,417" % halving, ok)

# Row 14. One less than a doubling of a crossed count is crossed by the doublings of its parts less one; with a prime count it
# is a prime only at some: 3, 7, 31, 127 ... told by the halving loop of 4.
def lucas_lehmer(p):
    if p == 2:
        return True
    m, s = (1 << p) - 1, 4
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0
ok = all(((1 << (a * b)) - 1) % ((1 << a) - 1) == 0 for a in range(2, 12) for b in range(2, 12))
mers = [p for p in range(2, 1300) if sieve[p] and lucas_lehmer(p)]
say(14, "one less than a doubling of a crossed count is crossed; of a prime count, a prime at %s, to 1,300 stepped" % mers,
    ok and mers == [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279])

# Row 15. A number whose parts add to its double: a doubling's me's times its one-less prime, every one to 100,000 so;
# no odd one, stepped.
perf = [n for n in range(2, 100001) if sum(d for d in range(1, isqrt(n) + 1) if n % d == 0) + sum(n // d for d in range(1, isqrt(n) + 1) if n % d == 0 and d * d != n) == 2 * n]
say(15, "numbers whose parts add to their double to 100,000: %s, every one 2 to the p − 1 times its prime 2 to the p less 1; no odd one" % perf,
    perf == [6, 28, 496, 8128] and all(n == (1 << (p - 1)) * ((1 << p) - 1) for n, p in zip(perf, (2, 3, 5, 7))))

# Row 17. Doubling closes round a prime's own me again as round the prime itself only at 1,093 and 3,511, stepped to 4,000,000.
wief = [p for p in range(3, N) if sieve[p] and pow(2, p - 1, p * p) == 1]
say(17, "doubling closes round a prime's me again as round the prime at %s, stepped to 4,000,000" % wief, wief == [1093, 3511])

# Row 59. Two prime loops meet at their turn alone: broods of 13 and 17 years meet every 221 years; a loop of 12 meets
# loops of 2, 3, 4 and 6 at every turn of its own.
say(59, "loops of 13 and 17 meet every %d moments, their torus's turn; a loop of 12 meets 2, 3, 4 and 6 within its own 12" % (13 * 17),
    min(t for t in range(1, 300) if t % 13 == 0 and t % 17 == 0) == 221 and all(12 % k == 0 for k in (2, 3, 4, 6)))

# Row 40. The distance met most often between neighbouring me-parities, by surface: 2, then 6, the turn of 2 and 3.
gaps = {}
champ_rows, last = [], 2
for n in range(3, N + 1):
    if sieve[n]:
        g = n - last
        gaps[g] = gaps.get(g, 0) + 1
        last = n
    if n in (100, 1000, 10000, 100000, 1000000, 4000000):
        champ_rows.append((n, max(gaps, key=lambda k: (gaps[k], -k))))
say(40, "the distance met most often between neighbouring me-parities, by surface: %s: 6, the turn of 2 and 3, stepped" % champ_rows, champ_rows[-1][1] == 6)

# Row 26. The race round 4: the places one short of a seam of 4 lead, and the places one past lead first at 26,861, the me
# agains of primes all landing on 1, the seen place.
lead, changes = 0, []
for n in range(3, 1000000):
    if sieve[n]:
        lead += 1 if n % 4 == 3 else -1
        if lead < 0 and (not changes or changes[-1][1] >= 0):
            changes.append((n, lead))
        elif lead >= 0 and changes and changes[-1][1] < 0:
            changes.append((n, lead))
say(26, "round 4, the primes one short of a seam of 4 lead; one past takes the lead at %d, and every prime's me again lands on 1, the seen place" % changes[0][0],
    changes[0][0] == 26861 and all(p * p % 4 == 1 for p in PR if p > 2))

# Row 29. Between every me again and its next, a me-parity, stepped to 4,000,000.
say(29, "between every me again and its next, a me-parity, me agains to 4,000,000",
    all(any(sieve[m] for m in range(s * s + 1, (s + 1) * (s + 1))) for s in range(1, isqrt(N))))

print("All is." if all(results) else "A line is-not.")
