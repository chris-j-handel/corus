# The triangle of row 45's co-chaining, round a me-parity: copies at all scales, uncrossed numbers of a row by the row's digits,
# crossings by the carryings, and the middle number of a row at a number's double. Breaking tests. A test proves nothing past its numbers.
from math import comb
def digits(n, p):
    d = []
    while n: d.append(n % p); n //= p
    return d or [0]
def carries(a, b, p):
    c = 0; k = 0
    while a or b or c:
        s = a % p + b % p + c; c = 1 if s >= p else 0; k += c; a //= p; b //= p
    return k
def times(p, n):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k
def isp(n): return n > 1 and all(n % d for d in range(2, int(n**0.5)+1))
no = {}
def t(k, bad): no[k] = no.get(k, 0) + (1 if bad else 0)
for p in (2, 3, 5, 7, 11):
    R = 200 if p > 2 else 300
    t("1 the row at the me-parity: 1, crossed, 1", any(comb(p, k) % p for k in range(1, p)))
    for n in range(R):
        dn = digits(n, p); w = 1
        for d in dn: w *= d + 1
        row = [comb(n, k) for k in range(n+1)]
        t("3 uncrossed numbers of a row: the digits, a digit and 1, multiplied", sum(1 for x in row if x % p) != w)
        for k in range(n+1):
            dk = digits(k, p) + [0]*len(dn); v = 1
            for a, b in zip(dn, dk): v *= comb(a, b)
            t("2 a number of the triangle round the me-parity: the opening triangle at the digits, multiplied", (row[k] - v) % p)
            if n < 120: t("4 the times crossed: the carryings", times(p, row[k]) != carries(k, n-k, p))
    # two copies and a crossed triangle between, at the scales p and p by p
    for s in (p, p*p):
        for n in range(s, 2*s):
            for k in range(n+1):
                c = comb(n, k) % p
                if k <= n - s: t("2 a copy", c != comb(n-s, k) % p)
                elif k >= s: t("2 a copy", c != comb(n-s, k-s) % p)
                else: t("2 crossed between", c != 0)
P = [q for q in range(2, 2100) if isp(q)]
for n in range(3, 1000):
    M = comb(2*n, n)
    for q in P:
        if q > 2*n: break
        if n < q <= 2*n: t("5 past the number and to the double: once", times(q, M) != 1)
        elif 3*q > 2*n and q <= n: t("5 past 2 over 3 of the number and to the number: crosses not", M % q == 0)
print("rows 0 to 8 round 2:"); [print("   ", "".join("1" if comb(n, k) % 2 else "." for k in range(n+1)).center(9)) for n in range(9)]
print("row 6:", [comb(6, k) for k in range(7)], "; digits of 6 round 2:", digits(6, 2)[::-1], "; odd:", [comb(6, k) for k in range(7) if comb(6, k) % 2])
print("row 4 round 3:", [comb(4, k) for k in range(5)], "; digits of 4 round 3:", digits(4, 3)[::-1], "; uncrossed:", [comb(4, k) for k in range(5) if comb(4, k) % 3])
print("20, row 6: 3 and 3 added round 2, carryings:", carries(3, 3, 2), "; 20 is 4 by 5")
M = comb(16, 8); print("the middle number of row 16:", M, "; 11:", times(11, M), "; 13:", times(13, M), "; 7:", times(7, M), "; 16 over 3:", 16/3)
print("is-nots:", {k: v for k, v in no.items() if v}, "; lines:", len(no), "; all:", sum(no.values()))
