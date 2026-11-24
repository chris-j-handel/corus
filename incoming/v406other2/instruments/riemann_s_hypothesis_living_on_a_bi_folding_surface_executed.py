#!/usr/bin/env python3
"""Riemann's hypothesis living on a bi-folding surface: its natural naming and explaining, executed with
whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/riemann_s_hypothesis_living_on_a_bi_folding_surface_executed.py

A line is a saying, ending is or is-not; a line ending sized gives numbers alone. Nothing is proved and
nothing is decided: a line says is of what it stepped. It opens no file and writes no file.

Its names: a number's parity is + with an even number of prime parts multiplied and - with an odd number;
the parity lead of n is the -s less the +s of 1 to n; a surface is 4 to the k numbers, its side 2 to the k;
the staircase is the primes to a number.
"""
from array import array
from fractions import Fraction
from math import isqrt

N = 4 ** 11          # 4,194,304, the surface stepped to
out = []


def say(text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))


def num(n):
    return f"{n:,}"


# The spirals crossing a number: its lowest prime part, to N.
low = array("i", range(N + 1))
for p in range(2, isqrt(N) + 1):
    if low[p] == p:
        for m in range(p * p, N + 1, p):
            if low[m] == m:
                low[m] = p

# A number's parity, and the parity of a number with no square part, 0 with a square part.
par = array("b", [0]) * (N + 1)      # + is 1, - is -1
nsq = array("b", [0]) * (N + 1)      # +, - or 0
par[1] = nsq[1] = 1
for n in range(2, N + 1):
    p = low[n]
    q = n // p
    par[n] = -par[q]
    nsq[n] = 0 if q % p == 0 else -nsq[q]

# The two leads, as sums of + and - from 1: plus[n] is the +s less the -s of 1 to n.
plus = array("i", [0]) * (N + 1)
plusq = array("i", [0]) * (N + 1)
stair = array("i", [0]) * (N + 1)
a = b = c = 0
for n in range(1, N + 1):
    a += par[n]
    b += nsq[n]
    if n > 1 and low[n] == n:
        c += 1
    plus[n] = a
    plusq[n] = b
    stair[n] = c

surfaces = [4 ** k for k in range(1, 12)]

# ONE. A number's parts' parities.
M = 100_000
parts = [0] * (M + 1)
partsq = [0] * (M + 1)
for d in range(1, M + 1):
    s, t = par[d], nsq[d]
    for m in range(d, M + 1, d):
        parts[m] += s
        if t:
            partsq[m] += t
say(f"a number's parts' parities come to 1 with a number multiplied by its own and to 0 with all other numbers, "
    f"1 to {num(M)}", all(parts[n] == (1 if isqrt(n) ** 2 == n else 0) for n in range(1, M + 1)))
say(f"a number's parts with no square part have parities coming to 0, all but 1's own, 1 to {num(M)}",
    all(partsq[n] == (1 if n == 1 else 0) for n in range(1, M + 1)))
ok = True
for p in (2, 3, 5, 7, 11, 13):
    q, k = 1, 0
    while q * p <= M:
        q *= p
        k += 1
        ok = ok and parts[q] == (1 if k % 2 == 0 else 0)
say("a prime multiplied by its own k times has parts of parities +, -, +, - and on: 1 with k even and 0 with k odd, "
    "the primes 2 to 13", ok)

# TWO. A surface's side is its squares, and all its spirals' crossings with their parities come to its side.
say("the numbers multiplied by their own on a surface of 4 to the k are its side, 2 to the k, k of 1 to 11",
    all(isqrt(s) ** 2 == s and sum(1 for r in range(1, isqrt(s) + 1) if r * r <= s) == isqrt(s) for s in surfaces))
ok = True
for s in surfaces:
    tot = 0
    for d in range(1, s + 1):
        tot += par[d] * (s // d)
    ok = ok and tot == isqrt(s)
say("on a surface, all spirals' crossings with their spirals' parities come to its side, with none over: "
    "the surfaces 4 to 4,194,304", ok)
ok = True
tot = 0
for n in range(1, 20_001):
    tot += parts[n]
    ok = ok and tot == isqrt(n)
say("and with all n of 1 to 20,000, to the square side of n", ok)
ok = True
for s in surfaces:
    tot = 0
    for d in range(1, s + 1):
        if nsq[d]:
            tot += nsq[d] * (s // d)
    ok = ok and tot == 1
say("with the spirals of no square part alone, the crossings with their parities come to 1, a me: the same surfaces", ok)

# THREE. The fractal: a surface's lead is its side less the leads of its folds.
def folds(n, lead):
    """the leads of n's folds, n over 2, over 3 and on to n over n, added"""
    tot, m = 0, 2
    while m <= n:
        v = n // m
        last = n // v
        tot += lead[v] * (last - m + 1)
        m = last + 1
    return tot


say("a surface's +s less its -s are its side less the same of its folds, the surface over 2, over 3, over 4 and on: "
    "the surfaces 4 to 4,194,304", all(plus[s] == isqrt(s) - folds(s, plus) for s in surfaces))
say("and with all n of 1 to 20,000", all(plus[n] == isqrt(n) - folds(n, plus) for n in range(1, 20_001)))
say("with the numbers of no square part it is 1 less the same of its folds: the surfaces, and all n of 1 to 20,000",
    all(plusq[s] == 1 - folds(s, plusq) for s in surfaces)
    and all(plusq[n] == 1 - folds(n, plusq) for n in range(1, 20_001)))
ok = all(plus[n] == sum(plusq[n // (d * d)] for d in range(1, isqrt(n) + 1)) for n in surfaces)
ok = ok and all(plus[n] == sum(plusq[n // (d * d)] for d in range(1, isqrt(n) + 1)) for n in range(1, 20_001))
say("a surface's lead is the leads of the numbers of no square part on its folds by the squares to its side, "
    "its own bi-foldings inward among them: the surfaces, and all n of 1 to 20,000", ok)

# The 1 to 17: sixteen numbers in four fours and a next 1, a surface of 16, and its bi-foldings.
say("1 to 16 are eight +s and eight -s, the lead at 0 at 16, and 17, a next 1, is a prime: "
    "+ at 1, 4, 6, 9, 10, 14, 15 and 16, and - at 2, 3, 5, 7, 8, 11, 12 and 13",
    [n for n in range(1, 17) if par[n] == 1] == [1, 4, 6, 9, 10, 14, 15, 16] and plus[16] == 0 and low[17] == 17)
say("the numbers multiplied by their own in 1 to 16 are 1, 4, 9 and 16, four, its side, a last of a four apiece: "
    "1 to 4, 5 to 8, 9 to 12 and 13 to 16 end at 4, 8, 12 and 16",
    [r * r for r in range(1, 5)] == [1, 4, 9, 16])
say("16 bi-folds to 64, 64 to 256 and on, four times a scale, a side doubled: 1 to 17, 1 to 65, 1 to 257",
    [4 ** k + 1 for k in (2, 3, 4)] == [17, 65, 257] and [isqrt(4 ** k) for k in (2, 3, 4)] == [4, 8, 16])
ends = [-plus[s] for s in surfaces]
say("the parity lead at a surface's end, the surfaces 4 to 4,194,304, is " + ", ".join(num(v) for v in ends), "sized")
six = [n for n in range(2, 17) if low[n] == n]
say("the primes of 1 to 16 are six, 2, 3, 5, 7, 11 and 13, and they are the spirals crossing 1 to 256, its side 16: "
    "the primes on a surface are the spirals crossing the surface one square out",
    six == [2, 3, 5, 7, 11, 13] and all(low[n] in six for n in range(2, 257) if low[n] != n)
    and all(any(low[n] == q for n in range(2, 257) if low[n] != n) for q in six))
going = [n for n in range(2, 60) if low[n] == n]
say("0 to 60 has seventeen primes, 2 to 59, and sixteen betweens, and 60 is between 59 and 61, both primes: "
    "Natural Numbers 7.5", len(going) == 17 and low[59] == 59 and low[61] == 61 and low[60] != 60)

# FOUR. The lead of a surface beside its side.
most = []
run = 0
k = 1
for n in range(1, N + 1):
    v = -plus[n]
    if v > run:
        run = v
    elif -v > run:
        run = -v
    if n == 4 ** k:
        most.append(run)
        k += 1
say("the parity lead's most on the surfaces 4 to 4,194,304 is 1, 3, 7, 16, 28, 66, 150, 309, 567, 1,253 and 2,254, "
    "the draft's 5.2", most == [1, 3, 7, 16, 28, 66, 150, 309, 567, 1253, 2254])
say("beside sides of 2 to 2,048 it is past the side alone from the surface of 4,096 on",
    [m > 2 ** (i + 1) for i, m in enumerate(most)] == [False] * 5 + [True] * 6)
say(f"the lead multiplied by its own is short of twice its number, with all n of 2 to {num(N)}",
    all(plus[n] * plus[n] < 2 * n for n in range(2, N + 1)))
zeros = [n for n in range(1, N + 1) if plus[n] == 0]
say("the parity lead is at 0 at 2, 4, 6, 10, 16, 26, 40, 96 and 586, and at no number after to 4,194,304",
    zeros == [2, 4, 6, 10, 16, 26, 40, 96, 586])
ok = True
for i in range(2, 11):
    lo, hi = 4 ** i, 4 ** (i + 1)
    ok = ok and any(plusq[n] == 0 for n in range(lo + 1, hi + 1))
say("the lead of the numbers of no square part is at 0 again between a surface and its next, the surfaces 16 to 4,194,304",
    ok)
minus = (N - plus[N]) // 2
say(f"on the surface of {num(N)} the -s are {num(minus)} and the +s {num(N - minus)}, apart by {num(-plus[N])}, "
    f"beside a side of {num(isqrt(N))}", "sized")

# FIVE. A prime born on a surface: a next universe, its horizon its own square.
ok = True
for n in range(2, 4 ** 10 + 1):
    m, far = n, 0
    while m > 1:
        p = low[m]
        if p * p > n:
            far += 1
        m //= p
    if far > 1:
        ok = False
        break
say("a number has at most one prime part past its square side, 2 to 1,048,576", ok)
ok = True
k = 1
for n in range(2, N + 1):
    while 4 ** k < n:
        k += 1
    if low[n] != n and low[n] > 2 ** k:
        ok = False
        break
say(f"a surface's crossed numbers are known by the primes to its side alone, and a prime born past its side crosses "
    f"no number of it: the surfaces 4 to {num(N)}", ok)
high = array("i", [0]) * (N + 1)       # a number's highest prime part
for n in range(2, N + 1):
    q = n // low[n]
    high[n] = low[n] if q == 1 else high[q]
ok = True
for s in surfaces:
    side = isqrt(s)
    known = 1 + sum(par[m] for m in range(2, s + 1) if high[m] <= side)
    born = sum(plus[s // p] for p in range(side + 1, s + 1) if low[p] == p)
    ok = ok and plus[s] == known - born
say("a surface's +s less its -s are those of its numbers known by its side's spirals alone, less those of its folds "
    f"by the primes born on it, a prime born inverting once: the surfaces 4 to {num(N)}", ok)
births = [stair[2 * 2 ** k] - stair[2 ** k] for k in range(1, 21)]
say("between a side and its double a prime is born, the sides 2 to 1,048,576: "
    f"1, 2, 2, 5, 7, 13 and on to {num(births[-1])}", all(v >= 1 for v in births) and births[:6] == [1, 2, 2, 5, 7, 13])

# SIX. The 1 to 17 of 60, and its fracturing.
places = [n for n in range(1, 61) if n % 2 and n % 3 and n % 5]
say("a 60 has sixteen places no spiral of 2, 3 or 5 crosses: 1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, "
    "49, 53 and 59; and 61, 60 and 1, is a next 1",
    places == [1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59] and 61 % 60 == 1)
pset = set(places)
say(f"all primes past 5 are on the sixteen places, 60 after 60, to {num(N)}",
    all(n % 60 in pset for n in range(7, N + 1) if low[n] == n))
say("a 120 is two of them, 32 places, and its primes are known by 2, 3, 5 and 7 alone: 30 primes, "
    "and 121, 11 by 11, the lowest number past it crossed by none of the four",
    sum(1 for n in range(2, 121) if low[n] == n) == 30
    and all((low[n] == n) == (n in (2, 3, 5, 7) or all(n % q for q in (2, 3, 5, 7))) for n in range(2, 121))
    and min(n for n in range(121, 400) if low[n] != n and all(n % q for q in (2, 3, 5, 7))) == 121)
ok = True
for p in [n for n in range(7, 60) if low[n] == n]:
    crossed = sum(1 for n in range(1, 60 * p + 1) if n % 60 in pset and n % p == 0)
    ok = ok and crossed == 16
say("a prime of 7 to 59 is at its seam with sixteen places in its own number of 60s, one place in its own number", ok)
lowest = min(n for n in range(7, 200) if n % 60 in pset and low[n] != n)
say("the lowest place crossed is 49, 7 by 7: a prime crosses no place below its own square",
    lowest == 49 and all(low[n] == n for n in range(7, 49) if n % 60 in pset))

# SEVEN. A turn's ratio, and the staircase's geodesics, one up for m along.
ratio, turn, ratios = Fraction(1), 1, []
for p in (2, 3, 5, 7, 11, 13, 17):
    ratio *= Fraction(p - 1, p)
    turn *= p
    ratios.append(ratio)
say("uncrossed in a turn of 2 is 1/2; with 3, 1/3; with 5, 4/15; with 7, 8/35; with 11, 16/77; with 13, 192/1001; "
    "with 17, 3072/17017: a turn more, a ratio lower",
    ratios == [Fraction(1, 2), Fraction(1, 3), Fraction(4, 15), Fraction(8, 35), Fraction(16, 77),
               Fraction(192, 1001), Fraction(3072, 17017)])
on = {}
for m in range(2, 15):
    on[m] = [n for n in range(m, N + 1, m) if stair[n] * m == n]
lasts = [on[m][-1] for m in range(2, 15)]
say("the staircase is on the geodesic of one up for 2 along at 2, 4, 6 and 8; for 3 along at 27, 30 and 33; "
    "for 4 along at 96, 100 and 120; for 5 along at 330, 335, 340, 350, 355 and 360",
    on[2] == [2, 4, 6, 8] and on[3] == [27, 30, 33] and on[4] == [96, 100, 120]
    and on[5] == [330, 335, 340, 350, 355, 360])
say("it is on all of them, m of 2 to 14, and its last number on them is "
    + ", ".join(num(v) for v in lasts), all(on[m] for m in range(2, 15)) and lasts[:4] == [8, 33, 120, 360])
ok = True
j = 0                                    # how many of the geodesics have their last number below n
for n in range(lasts[0] + 1, N + 1):
    while j < len(lasts) and lasts[j] < n:
        j += 1
    if stair[n] * (j + 1) >= n:          # under the geodesic of j + 1 along, and under all of fewer along with it
        ok = False
        break
say(f"past its last number on a geodesic the staircase is under it, to {num(N)}: m of 2 to 14", ok)
ok = all(lasts[i] < lasts[i + 1] for i in range(len(lasts) - 1))
ok = ok and all(stair[n] * (m + 1) >= n for m in range(2, 14) for n in on[m])
say("a geodesic's last number is below the next geodesic's, and at it the staircase is on or above the next", ok)
# with all numbers, by one turn: the staircase is at most the turn's own primes and its uncrossed places
shown = []
for m in (2, 3, 4, 5):
    t, r, own = 1, Fraction(1), 0
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        t *= p
        r *= Fraction(p - 1, p)
        own += 1
        if r < Fraction(1, m):
            break
    open_places = r * t
    # staircase(n) <= own + open_places * (n / t + 1) < n / m from n0 on
    n0 = int((own + open_places) / (Fraction(1, m) - r)) + 1
    last = on[m][-1]
    good = n0 <= N and all(stair[n] * m < n for n in range(last + 1, n0 + 1))
    shown.append((m, t, good))
say("with all numbers, by one turn and a stepping to it, the staircase is under its geodesic past its last number: "
    "for 2 along by the turn of 6, for 3 by 30, for 4 by 210 and for 5 by 30,030",
    [(m, t) for m, t, g in shown] == [(2, 6), (3, 30), (4, 210), (5, 30030)] and all(g for m, t, g in shown))
say("for 6 along the turn is of 2 to 23, 223,092,870 numbers, past this stepping: 6 along and on are stepped alone",
    "sized")

for kind, text in out:
    print(f"{kind:8}{text}")
kinds = [k for k, t in out]
print(f"\n{kinds.count('is')} is; {kinds.count('is-not')} is-not; {kinds.count('sized')} sized.")
