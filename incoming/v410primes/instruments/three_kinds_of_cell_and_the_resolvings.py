# Three kinds of cell on a torus of some me-parities; a me-parity on no line of the torus of all the me-parities ahead;
# the digits round the -1 at a number of doublings; the stretches, crossed and uncrossed; and a universe with the universe's own seam.
# Breaking tests of v410primes, 27 November 2026. A test proves nothing past its numbers.
from math import gcd
no = {}
def t(k, bad): no[k] = no.get(k, 0) + (1 if bad else 0)
def isp(n): return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
def kinds(ps):
    m = 1
    for p in ps: m *= p
    k = {"all": [], "other-than-all": [], "other-than-other-than-all": []}
    for n in range(m):
        on = sum(1 for p in ps if n % p == 0)
        k["all" if on == len(ps) else "other-than-all" if on else "other-than-other-than-all"].append(n)
    return m, k
want = {(3, 5): (1, 6, 8), (2, 3, 5): (1, 21, 8), (5, 7): (1, 10, 24), (2, 3, 5, 7): (1, 161, 48)}
for ps, w in want.items():
    m, k = kinds(ps); got = tuple(len(k[a]) for a in ("all", "other-than-all", "other-than-other-than-all"))
    t("three kinds, a cell in one alone", got != w or sum(got) != m); print(ps, m, got)
m15, k15 = kinds((3, 5)); m30, k30 = kinds((2, 3, 5)); eight = k15["other-than-other-than-all"]
even = [n for n in eight if n in k30["other-than-all"]]; odd = [n for n in eight if n in k30["other-than-other-than-all"]]
t("the eight of 3 by 5 with the line of 2: four and four", (even, odd) != ([2, 4, 8, 14], [1, 7, 11, 13])); print("the eight:", eight, "; on the line of 2:", even, "; on no line:", odd)
for ps, q in (((3, 5), 2), ((2, 3, 5), 7), ((2, 3, 5, 7), 11)):
    m, k = kinds(ps)
    t("lifted: a cell on no line is as many finer cells as the me-parity, one on the next line", any(sum(1 for j in range(q) if (c + m*j) % q == 0) != 1 for c in k["other-than-other-than-all"]))
P = [p for p in range(2, 5001) if isp(p)]
t("a me-parity: a number on no line of the torus of all the me-parities ahead, alone, 2 to 5,000", any(all(n % p for p in P if p < n) != isp(n) for n in range(3, 5001)))
# the digits
bits = lambda n: bin(n).count("1")
for k in range(2, 41):
    m = 2**k - 1
    w = 3 if k % 2 else (2**(k & -k) + 1 if k & (k - 1) else 7)
    other = gcd(w, m) == 1 and 2 <= bits(w) <= k - 2
    t("one digit on or one not on, all: at 2, 3 and 4 doublings alone", other != (k >= 5))
for k in (2, 3, 4, 5, 6):
    m = 2**k - 1; U = [n for n in range(1, m) if gcd(n, m) == 1]
    t("at 2, 3 and 4 all, at 5 and 6 not", all(bits(n) in (1, k - 1) for n in U) != (k <= 4))
    t("doubling steps the digits round", any((2*n) % m != ((n << 1) & m | (n >> (k - 1))) % m for n in range(1, m)))
t("round 15: uncrossed with an odd number of digits on, alone", any((gcd(n, 15) == 1) != (bits(n) % 2 == 1) for n in range(1, 15)))
# the stretches, crossed and uncrossed, one after an other
def stretches(m, a, b):
    s = []
    for n in range(a, b + 1):
        u = gcd(n, m) == 1
        if not s or s[-1][0] != u: s.append([u, 0])
        s[-1][1] += 1
    return s
s30 = stretches(30, 1, 30); s35 = stretches(35, 0, 35)
t("with 2 in the seam: an uncrossed between is one number, a crossed between an odd number", any((u and l != 1) or (not u and l % 2 == 0) for u, l in s30))
t("the torus of 5 by 7: 4, 1, 2, 3, 4, 3, 2, 1 and 4 between two crossings", [l for u, l in s35 if u] != [4, 1, 2, 3, 4, 3, 2, 1, 4])
print("round 30:", [("u" if u else "c") + str(l) for u, l in s30]); print("round 35:", [("u" if u else "c") + str(l) for u, l in s35])
# a universe with the universe's own seam
P2 = [p for p in range(2, 110) if isp(p)]; seam = 1
for i, p in enumerate(P2[:-1]):
    seam *= p; q = P2[i + 1]
    t("a universe with its own seam: a cell between the crossings is a me-parity, alone", [n for n in range(p*p, q*q) if gcd(n, seam) == 1] != [n for n in range(p*p, q*q) if isp(n)])
t("49, 77, 91 and 119: between the crossings of 2, 3 and 5, on the crossing of 7", any(gcd(n, 30) != 1 or n % 7 for n in (49, 77, 91, 119)))
print("is-nots:", {k: v for k, v in no.items() if v}, "; lines:", len(no), "; all:", sum(no.values()))
