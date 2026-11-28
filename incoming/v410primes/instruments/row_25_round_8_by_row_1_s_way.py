# Row 25, round 8: me-parities at all four places, past any number, by row 1's way. Breaking tests. A test proves nothing past its numbers.
def factors(n):
    f = []; d = 2
    while d * d <= n:
        while n % d == 0: f.append(d); n //= d
        d += 1 if d == 2 else 2
    if n > 1: f.append(n)
    return f
no = {}
def t(k, bad): no[k] = no.get(k, 0) + (1 if bad else 0)
build = {1: lambda x: (2*x)**4 + 1, 3: lambda x: x*x + 2, 5: lambda x: x*x + 4, 7: lambda x: x*x - 2}
allowed = {1: {1}, 3: {1, 3}, 5: {1, 5}, 7: {1, 7}}
for x in range(3, 4000, 2):
    for a in (3, 5, 7):
        N = build[a](x); f = factors(N)
        t(f"at {a}: the built number at {a} round 8", N % 8 != a)
        t(f"at {a}: the crossing me-parities at 1 or {a} round 8", any(p % 8 not in allowed[a] for p in f))
        t(f"at {a}: one crossing me-parity at {a}", not any(p % 8 == a for p in f))
        t(f"at {a}: no crossing me-parity crosses the multiplied", any(x % p == 0 for p in f))
for x in range(1, 61):
    N = build[1](x); f = factors(N)
    t("at 1: the crossing me-parities at 1 round 8", any(p % 8 != 1 for p in f)); t("at 1: none crosses the multiplied", any((2*x) % p == 0 for p in f))
# row 1's way, three steps at a place
for a, first in ((1, 17), (3, 3), (5, 5), (7, 7)):
    found = [first]
    for _ in range(1 if a == 1 else 2):
        x = 1
        for p in found: x *= p
        N = build[a](x); f = factors(N); nxt = min(p for p in f if p % 8 == a)
        found.append(nxt)
    print("at", a, "round 8:", found)
print("3 by 3 and 2:", 11, 11 % 8, "; 5 by 5 and 4:", 29, 29 % 8, "; 7 by 7 less 2:", 47, 47 % 8, "; 2 by itself 4 times and 1:", 17, 17 % 8)
# the places with the place by itself at place 1
from math import gcd
for m in (4, 5, 6, 8, 12, 24, 30):
    U = [a for a in range(1, m) if gcd(a, m) == 1]; print("round", m, ": uncrossed", U, "; by itself at place 1:", [a for a in U if a*a % m == 1])
print("is-nots:", {k: v for k, v in no.items() if v}, "; lines:", len(no), "; all:", sum(no.values()))
