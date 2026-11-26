# v408primes · take any number and begin resolving: the universe of this is the proving of this. Whole numbers.
# Execute: python3 -I from_any_number_its_universe_resolving.py [any numbers from 4 to 1,658,522,032,339,943,692,980,990]
# With no numbers given, it takes 10^12, 2^64, 10^18 + 9 and 10^24, and two numbers drawn now, as any.
import sys, secrets
from math import isqrt, gcd

SEEING = 3317044064679887385961981          # below this, the 13 bases see a me-parity one way, by whole numbers
BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
SMALL = [p for p in range(2, 1000) if all(p % q for q in range(2, isqrt(p) + 1))]

def me_parity(n):
    if n < 2:
        return False
    for q in SMALL:
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in BASES:
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

def next_me_parity(n):
    m = n + 1
    while not me_parity(m):
        m += 1
    return m

results = []
def say(n, sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + "from %s · %s" % (f"{n:,}", sentence))

taken = [int(a) for a in sys.argv[1:]] or [10 ** 12, 2 ** 64, 10 ** 18 + 9, 10 ** 24,
                                           secrets.randbelow(10 ** 18) + 10, secrets.randbelow(10 ** 24) + 10]
for n in taken:
    if not 4 <= n < SEEING // 2:
        print("past this instrument's seeing: %s" % n)
        continue
    # Its next me-parity, before its double.
    p = next_me_parity(n)
    say(n, "its next me-parity is %s, %s on, before its double" % (f"{p:,}", p - n), p < 2 * n)
    # Its side: a me-parity between its side's me again and the next me again.
    s = isqrt(n)
    q = next_me_parity(s * s)
    say(n, "its side is %s; between the side's me again and the next, a me-parity, %s" % (f"{s:,}", f"{q:,}"), s * s < q < (s + 1) * (s + 1))
    # Two me-parities facing one another about it as a between.
    d = 0 if me_parity(n) else 1
    while not (me_parity(n - d) and me_parity(n + d)):
        d += 1
    say(n, "about it as a between, two me-parities face one another %s apart from it: %s and %s" % (f"{d:,}", f"{n - d:,}", f"{n + d:,}"),
        n - d + n + d == 2 * n and me_parity(n - d) and me_parity(n + d))
    # The next twins born past it, living in one seam of 6.
    t = n + (5 - n % 6) % 6 or 5
    while not (me_parity(t) and me_parity(t + 2)):
        t += 6
    say(n, "the next twins born past it are %s and %s, %s on, about the seam %s" % (f"{t:,}", f"{t + 2:,}", f"{t - n:,}", f"{t + 1:,}"),
        t > n and (t + 1) % 6 == 0)
    # The next neighbouring me-parities 2 to 246 apart past it.
    a = next_me_parity(n)
    b = next_me_parity(a)
    while b - a > 246:
        a, b = b, next_me_parity(b)
    say(n, "the next neighbouring me-parities 2 to 246 apart past it: %s and %s, %s apart" % (f"{a:,}", f"{b:,}", b - a), 2 <= b - a <= 246)
    # Round all loops of 3 to 30, a me-parity past it at all their living places.
    ok = True
    for m in range(3, 31):
        for r in range(1, m):
            if gcd(r, m) == 1:
                x = n + (r - n) % m
                while not me_parity(x):
                    x += m
                ok = ok and x % m == r and x >= n
    say(n, "round all loops of 3 to 30, a me-parity past it at all their living places", ok)
    # A me again's +1 past its side that is a me-parity.
    k = s
    while not me_parity(k * k + 1):
        k += 1
    say(n, "from its side, the next me again's +1 that is a me-parity: %s by itself, and 1, %s on" % (f"{k:,}", k - s), me_parity(k * k + 1))
    # A society of four past it, 0, 2, 6, 8, up to 10^18.
    if n <= 10 ** 18:
        f = n + (11 - n % 30) % 30
        while not all(me_parity(f + e) for e in (0, 2, 6, 8)):
            f += 30
        say(n, "the next society of four past it: %s, +2, +6, +8, %s on" % (f"{f:,}", f"{f - n:,}"), f >= n)
    # Up to 10^12, the next me-parity round which doubling passes all places.
    if n <= 10 ** 12:
        x = next_me_parity(n)
        while True:
            m, parts, q2 = x - 1, set(), 2
            while q2 * q2 <= m:
                while m % q2 == 0:
                    parts.add(q2); m //= q2
                q2 += 1
            if m > 1:
                parts.add(m)
            if all(pow(2, (x - 1) // r, x) != 1 for r in parts):
                break
            x = next_me_parity(x)
        say(n, "the next me-parity past it round which doubling passes all places: %s" % f"{x:,}", x > n)

print("All is." if all(results) else "A line is-not.")
