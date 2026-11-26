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

# More competency from any number: pairs at any even distance, three me-parities at any odd, the side's step, the
# most-met distance about it, a curve's lean round its next prime, and counts of doublings.
def facing_about(b):
    d = 0 if me_parity(b) else 1
    while not (me_parity(b - d) and me_parity(b + d)):
        d += 1
    return b - d, b + d
distances = [4, 6, 8, 10, 12, 30, 210, 2 * (secrets.randbelow(500) + 1)]
for n in taken:
    if not 9 <= n < SEEING // 2:
        continue
    found = {}
    for dd in distances:
        x = n + 1
        while not (me_parity(x) and me_parity(x + dd)):
            x += 1
        found[dd] = x
    say(n, "past it, a pair of me-parities at all distances %s: %s" % (distances, {k: f"{v - n:,} on" for k, v in found.items()}),
        all(v > n for v in found.values()))
    o = n if n % 2 else n + 1
    a, b = facing_about((o - 3) // 2)
    say(n, "the odd %s is 3 and two me-parities facing one another about a between: %s and %s" % (f"{o:,}", f"{a:,}", f"{b:,}"), 3 + a + b == o)
    q = n
    while not me_parity(q):
        q -= 1
    r = next_me_parity(n)
    say(n, "about it, its prior me-parity %s and next %s: the next's side is the prior's side or its +1" % (f"{q:,}", f"{r:,}"), isqrt(r) <= isqrt(q) + 1)
    if n <= 10 ** 18:
        gaps, last, x = {}, None, n
        while x < n + 300000:
            if me_parity(x):
                if last is not None:
                    gaps[x - last] = gaps.get(x - last, 0) + 1
                last = x
            x += 1
        top = max(gaps, key=gaps.get)
        say(n, "about it, the next 300,000 numbers: the most-met distance between neighbouring me-parities is %d, met %d times; 30 met %d times" % (top, gaps[top], gaps.get(30, 0)), top == 6)
    if n <= 10 ** 6:
        p5 = max(5, next_me_parity(n))
        ok = True
        for (ca, cb) in ((1, 1), (-1, 0), (0, 1)):
            if (4 * ca ** 3 + 27 * cb * cb) % p5 == 0:
                continue
            lean = -sum((1 if pow((x ** 3 + ca * x + cb) % p5, (p5 - 1) // 2, p5) == 1 else (0 if (x ** 3 + ca * x + cb) % p5 == 0 else -1)) for x in range(p5))
            ok = ok and lean * lean < 4 * p5
        say(n, "round its next prime %s, the curves x³ + x + 1, x³ − x and x³ + 1 have their leans' facing roots at the side" % f"{p5:,}", ok)

def doubling_less_1_me_parity(e):
    if e == 2:
        return True
    m, x = (1 << e) - 1, 4
    for _ in range(e - 2):
        x = (x * x - 2) % m
    return x == 0
for c in [1280, 2204, secrets.randbelow(4000) + 2]:
    e = c
    while not (all(e % q for q in range(2, isqrt(e) + 1)) and e > 1 and doubling_less_1_me_parity(e)):
        e += 1
    say(c, "from this number of doublings, the next doubling less 1 that is a me-parity is at %s doublings" % f"{e:,}", e >= c)
for k in [5, 9, 14, secrets.randbelow(10) + 5]:
    f = (1 << (1 << k)) + 1
    say(k, "the doubling's doubling +1 at %d doublings of doublings is crossed: 3 by itself to its between is not its −1" % k, pow(3, (f - 1) // 2, f) != f - 1)

print("All is." if all(results) else "A line is-not.")
