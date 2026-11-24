#!/usr/bin/env python3
"""The numbers of Exhibit THIRTY-TWO's draft, executed again, with whole numbers alone.

Usage:  python3 -I incoming/v406other2/instruments/the_numbers_of_Exhibit_THIRTY-TWO_s_draft_executed_again.py [ROOT]

A line is a saying of the draft, its section beside it, ending is or is-not; a line ending sized gives
numbers the draft has no saying of. With ROOT, the repository, phi's torus is stepped by the living code
of incoming/v406Reiman/instruments/resolver_as_it_is.py; with no ROOT those lines are not executed.
Nothing is proved: a line says is of the numbers it stepped.

It writes its lines to standard output. It writes no file, reaches no network and decides nothing.
"""
import sys
from math import gcd, isqrt, lcm

N = 20_000_000          # the primes
S = 4_194_304           # the two leads, 4 to the 11
sieve = bytearray([1]) * (N + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N) + 1):
    if sieve[i]:
        sieve[i * i::i] = bytearray(len(sieve[i * i::i]))


def prime(n):
    return bool(sieve[n]) if n <= N else all(n % q for q in range(2, isqrt(n) + 1))


def staircase(n):
    return sum(sieve[: n + 1])


def phi_pair(k, m):
    """Phi's walk 0, 1, 1, 2, 3, 5 and on, round m: its kth and its next."""
    a, b = 0, 1
    for bit in bin(k)[2:]:
        c, d = a * ((2 * b - a) % m) % m, (a * a + b * b) % m
        a, b = (d, (c + d) % m) if bit == "1" else (c, d)
    return a, b


def phi_closing(n):
    x, y, k = 0, 1, 0
    while True:
        x, y, k = y, (x + y) % n, k + 1
        if (x, y) == (0, 1):
            return k


out = []


def say(sec, text, ok):
    out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, sec, text))


# The opening, and part ONE.
shells = [n ** 3 - (n - 1) ** 3 for n in range(1, 6)]
primes60 = [q for q in range(2, 62) if sieve[q]]
say("Opening", "the twelve primes 2 to 37 in rounds of four close at 7, 19 and 37, a cube's shells, and a fourth round at 53, the next shell 61 past it",
    [primes60[i] for i in (3, 7, 11, 15)] == [7, 19, 37, 53] and shells == [1, 7, 19, 37, 61])
say("1.3", "the staircase to 60, 100 and 120 is 17, 25 and 30", [staircase(n) for n in (60, 100, 120)] == [17, 25, 30])
pl = [n for n in range(1, 31) if gcd(n, 30) == 1]
say("1.3", "a turn of 30 has eight places, the stretches across between them 6, 4, 2, 4, 2, 4 and 6",
    pl == [1, 7, 11, 13, 17, 19, 23, 29] and [b - a for a, b in zip(pl, pl[1:])] == [6, 4, 2, 4, 2, 4, 6])
say("1.3", "pairs two apart in the turns of 6, 30, 210 and 2,310 are 1, 3, 15 and 135",
    [sum(1 for n in range(m) if gcd(n, m) == 1 and gcd(n + 2, m) == 1) for m in (6, 30, 210, 2310)] == [1, 3, 15, 135])
say("1.3", "the seventh turn, 510,510, has 92,160 places, 1 by 2 by 4 by 6 by 10 by 12 by 16",
    1 * 2 * 4 * 6 * 10 * 12 * 16 == 92160 and 2 * 3 * 5 * 7 * 11 * 13 * 17 == 510510)
say("1.4", "the openings of 1 to 12 selves are 8,190", sum(2 ** n for n in range(1, 13)) == 8190)
say("1.5", "the primes on the four faces of 30 are 10, 7, 7 and 6",
    [staircase(30 * k) - staircase(30 * k - 30) for k in (1, 2, 3, 4)] == [10, 7, 7, 6])
u = [n for n in range(1, 121) if gcd(n, 30) == 1]
say("1.5", "the four faces' 32 places, less 1, less 49, 77, 91 and 119, with 2, 3 and 5, are the 30 primes",
    len(u) == 32 and [n for n in u if n > 1 and not prime(n)] == [49, 77, 91, 119])
say("1.5", "flipped about 60, the primes of 0 to 120 part at 29 with 91, 43 with 77 and 49 with 71 alone, past the turn's own 2, 3 and 5",
    sorted({min(n, 120 - n) for n in u if prime(n) != prime(120 - n)}) == [29, 43, 49])
on = [n for n in range(1, 121) if 4 * staircase(n) == n]
under = [n for n in range(1, 121) if 4 * staircase(n) < n]
say("1.5", "to 120 the staircase is above the geodesic of one in four, and on it at 96, 100 and 120", on == [96, 100, 120] and under == [1])
run, ok = staircase(120), True
for n in range(121, N + 1):
    run += sieve[n]
    if 4 * run >= n:
        ok = False
        break
say("1.5", f"past 120 the staircase is under the geodesic with all numbers, 121 to {N:,} stepped", ok)
c210 = [n for n in range(1, 211) if gcd(n, 210) == 1]
say("1.5", "by one turn of 210: its 48 uncrossed numbers a turn, with 2, 3, 5 and 7 and less 1, are short of one in four with all numbers from 210 on",
    len(c210) == 48 and max(4 * (3 + 48 + sum(1 for x in c210 if x <= r)) - (210 + r) for r in range(1, 211)) < 0)
say("1.6", "round five doubling steps 2, 4, 3, 1, and round ten multiplying by 3 steps 3, 9, 7, 1",
    [pow(2, k, 5) for k in (1, 2, 3, 4)] == [2, 4, 3, 1] and [pow(3, k, 10) for k in (1, 2, 3, 4)] == [3, 9, 7, 1])
sq = {}
for n in range(1, 120):
    if gcd(n, 120) == 1:
        sq.setdefault(n * n % 120, []).append(n)
say("1.6", "in 120 the uncrossed numbers are two pieces of 16, multiplied by their own 1 and 49 past the 120s",
    sorted(sq) == [1, 49] and len(sq[1]) == len(sq[49]) == 16)
say("1.6", "a prime ending in 1 or 9 is a flip and a prime ending in 3 or 7 a quarter turn, primes 7 to 1,000,000",
    all((q * q % 120 == 1) == (q % 10 in (1, 9)) for q in range(7, 1_000_001) if sieve[q]))
say("1.6", "a prime from 5 on multiplied by its own is one past a whole number of 24s, primes to 1,000,000",
    all(q * q % 24 == 1 for q in range(5, 1_000_001) if sieve[q]))
say("1.6", "a prime from 5 on multiplied by itself four times is one past a whole number of 240s, primes to 1,000,000",
    all(pow(q, 4, 240) == 1 for q in range(5, 1_000_001) if sieve[q]))
say("1.6", f"  5 multiplied by itself four times is 625, {625 % 240} past two 240s; from 7 on it is, primes to 1,000,000: "
           f"{all(pow(q, 4, 240) == 1 for q in range(7, 1_000_001) if sieve[q])}", "sized")
a = b = 0
turning, level = None, []
for q in range(3, 30000):
    if sieve[q]:
        a, b = a + (q % 4 == 3), b + (q % 4 == 1)
        if a == b:
            level.append(q)
        if b > a and turning is None:
            turning = q
say("1.6", "round four the primes one short of a multiple of four lead those one past, to 26,861", turning == 26861)
say("1.6", f"  the two are level at {[q for q in level if q < 26861]}", "sized")
say("1.6", "at the fold, 24: 1, 5, 7, 11, 13, 17, 19 and 23 multiplied by their own are 1 past the 24s",
    all(n * n % 24 == 1 for n in (1, 5, 7, 11, 13, 17, 19, 23)))

# Part TWO.
least = list(range(S + 1))
for i in range(2, isqrt(S) + 1):
    if least[i] == i:
        for j in range(i * i, S + 1, i):
            if least[j] == j:
                least[j] = i
par = [0, 1] + [0] * (S - 1)     # a number's parity: + with an even number of primes multiplied, - with an odd
nsq = [0, 1] + [0] * (S - 1)     # the same, of the numbers with no square part alone
for n in range(2, S + 1):
    q = least[n]
    m = n // q
    par[n] = -par[m]
    nsq[n] = 0 if m % q == 0 else -nsq[m]
L = M = bl = bm = 0
k, most_l, most_m, zeros_l, zeros_m, zl, zm, short2, minus = 1, [], [], [], [], [], 0, True, True
last_zero_l = 0
plus = less = at0 = across = top = low = side_now = 0     # the lead of the numbers with no square part, its two sides
sides_m = {}
for n in range(1, S + 1):
    L += par[n]
    M += nsq[n]
    bl, bm = max(bl, abs(L)), max(bm, abs(M))
    plus, less, at0 = plus + (M > 0), less + (M < 0), at0 + (M == 0)
    top, low = max(top, M), min(low, M)
    if M and side_now and (M > 0) != (side_now > 0):
        across += 1
    side_now = M or side_now
    if n in (4096, 65536, 1048576, 4194304):
        sides_m[n] = (plus, less, at0, across, top, -low)
    if L == 0:
        zl.append(n)
        last_zero_l = n
    zm += M == 0
    if n <= 1_000_000:
        short2 = short2 and L * L < 2 * n
        minus = minus and (L <= 0 or n == 1)
    if n == 4 ** k:
        most_l.append(bl)
        most_m.append(bm)
        zeros_l.append(len(zl))
        zeros_m.append(zm)
        zl, zm, k = [], 0, k + 1
sides = [2 ** i for i in range(1, 12)]
said = [1, 3, 7, 16, 28, 66, 150, 309, 567, 1253, 2254]
say("2.2", "stepped to 1,000,000 the -s lead, and the parity lead multiplied by its own is short of twice the number", short2 and minus)
say("2.2", "the sixteen terms leave 27 of 1 to 120 uncrossed by 2, 3, 5 and 7", sum(1 for n in range(1, 121) if gcd(n, 210) == 1) == 27)
slopes, m = [], 1
for q in (2, 3, 5, 7, 11, 13):
    m *= q
    ph = sum(1 for n in range(m) if gcd(n, m) == 1)
    slopes.append((ph // gcd(ph, m), m // gcd(ph, m)))
say("2.2", "the slopes are 1/2, 1/3, 4/15, 8/35, 16/77 and 192/1001", slopes == [(1, 2), (1, 3), (4, 15), (8, 35), (16, 77), (192, 1001)])
say("2.3", "seven primes, 7 to 907 by 150, and ten, 199 to 2,089 by 210",
    all(prime(7 + 150 * i) for i in range(7)) and all(prime(199 + 210 * i) for i in range(10)))
say("2.4", "341, 11 by 31, and 2,047, 23 by 89, pass doubling's closing",
    11 * 31 == 341 and 23 * 89 == 2047 and pow(2, 340, 341) == 1 and pow(2, 2046, 2047) == 1)
both19, both37 = [], []
for n in range(9, N + 1, 2):
    e = n % 10
    if e != 5 and not sieve[n] and pow(2, n - 1, n) == 1:
        if e in (1, 9) and phi_pair(n - 1, n) == (0, 1):
            both19.append(n)
        if e in (3, 7) and phi_pair(2 * (n + 1), n) == (0, 1):
            both37.append(n)
say("2.4", f"no crossed number ending in 3 or 7 passes doubling's closing and phi's both, to {N:,}", both37 == [])
say("2.4", "2,757,241, 461 by 5,981, a crossed number ending in 1, passes both", 461 * 5981 == 2757241 and 2757241 in both19)
say("5.3", "the crossed numbers passing both of a prime's closings are 2,757,241, 6,368,689 and 9,863,461", both19 == [2757241, 6368689, 9863461])
say("5.3", f"  crossed numbers ending in 1 or 9 passing both, to {N:,}: {len(both19)}; the lowest twelve {both19[:12]}; "
           f"at 1, 49 or 61 round 120: {sum(1 for n in both19 if n % 120 in (1, 49, 61))}", "sized")


def parts(n):
    found, d = [], 2
    while d * d <= n:
        while n % d == 0:
            found.append(d)
            n //= d
        d += 1
    return found + ([n] if n > 1 else [])


def doubling_length(q):
    k, x = 1, 2 % q
    while x != 1:
        x, k = x * 2 % q, k + 1
    return k


one_length = [n for n in both19 if len({doubling_length(q) for q in parts(n)}) == 1]
say("5.3", f"the crossed numbers passing both with doubling's spirals of one length round all their parts, to {N:,}, "
           "are 2,757,241, 6,368,689 and 9,863,461, at 1, 49 and 61 round 120",
    one_length == [2757241, 6368689, 9863461] and [n % 120 for n in one_length] == [1, 49, 61])
say("5.3", f"  of the {len(both19)} passing both, those other than at 1, 49 or 61 round 120 are at "
           f"{sorted({n % 120 for n in both19 if n % 120 not in (1, 49, 61)})}, "
           f"{sum(1 for n in both19 if n % 120 not in (1, 49, 61))} of them; with a part ending in 3 or 7: "
           f"{[n for n in both19 if any(q % 10 in (3, 7) for q in parts(n))]}; the lowest, {both19[0]:,}, is {parts(both19[0])}", "sized")
say("2.4", "round 2,047 multiplying by 3 has a spiral of 88, and 3 multiplied by itself 44 times, less 1, has 23 with 2,047",
    next(k for k in range(1, 2047) if pow(3, k, 2047) == 1) == 88 and gcd(pow(3, 44, 2047) - 1, 2047) == 23)
say("2.5", "n multiplied by its own, n and 41 added, is a prime with n of 0 to 39 and 41 by 41 with 40, and no spiral of 2 to 37 is at its seam with any n",
    all(prime(n * n + n + 41) for n in range(40)) and 40 * 40 + 40 + 41 == 41 * 41
    and all((n * n + n + 41) % q for q in range(2, 38) if sieve[q] for n in range(q)))
say("2.6", "198,585,576,189 is 3, 7, 11 and 13 multiplied by their own, by 22,021, and 22,021 is 19 by 19 by 61",
    9 * 49 * 121 * 169 * 22021 == 198585576189 and 19 * 19 * 61 == 22021)

# Part THREE.
say("3.1", "the primes 7 to 53 are six pairs adding to 60, and 11 with 49",
    [q for q in range(7, 54) if sieve[q] and sieve[60 - q]] == [7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53] and 11 + 49 == 60)
say("3.2", "37 is 1, 6, 12 and 18, and 4 cubed less 3 cubed; n = 3 alone has its shell 3 by n by n, 3 by n and 1 as n cubed, n by n and 1, n to 1,000",
    1 + 6 + 12 + 18 == 37 == 64 - 27 and [n for n in range(1, 1001) if 3 * n * n == n ** 3 and 3 * n == n * n] == [3])
say("3.3", "four of the eight fours of 0 to 120 are all primes: 7, 53, 67, 113; 13, 47, 73, 107; 19, 41, 79, 101; 23, 37, 83, 97",
    [n for n in (1, 7, 11, 13, 17, 19, 23, 29) if all(prime(v) for v in (n, 60 - n, 60 + n, 120 - n))] == [7, 13, 19, 23])
say("3.3", "37, 97 and 157 are primes, with 23, 83 and 143, 143 being 11 by 13", prime(37) and prime(97) and prime(157) and prime(23) and prime(83) and 143 == 11 * 13)
say("3.5", "a cube of n about its line is 24, 60 and 120 with n of 3, 4 and 5, and 120 is twenty threes and ten sixes",
    [n ** 3 - n for n in (3, 4, 5)] == [24, 60, 120] and 5 * 4 * 3 + 10 * 6 == 120)

# Parts FOUR and FIVE.
say("4.1", "round a prime ending in 1 or 9 phi closes by a whole part of one short of it, and round a prime ending in 3 or 7 by a whole part of twice one past it, primes 7 to 10,000",
    all((q - 1) % phi_closing(q) == 0 for q in range(7, 10_000) if sieve[q] and q % 10 in (1, 9))
    and all((2 * (q + 1)) % phi_closing(q) == 0 for q in range(7, 10_000) if sieve[q] and q % 10 in (3, 7)))
say("4.1", "phi's closings round 3, 5, 7, 11, 15 and 21 are 8, 20, 16, 10, 40 and 16", [phi_closing(n) for n in (3, 5, 7, 11, 15, 21)] == [8, 20, 16, 10, 40, 16])
if len(sys.argv) > 1:
    import random
    from pathlib import Path
    root = Path(sys.argv[1]).resolve()
    sys.path.insert(0, str(root / "incoming" / "v406Reiman" / "instruments"))
    from itertools import product
    from resolver_as_it_is import moments_again, opening, resolver, spiral_couplings  # noqa: E402
    names, _ = resolver(str(root))
    step = names["_17_next_existing"]
    again = {n: sorted({moments_again(step, opening(range(n), dict(enumerate(pri))), spiral_couplings(n))[1]
                        for pri in product((1, -1), repeat=n)}) for n in (2, 3, 5, 7, 9, 11)}
    say("1.4", "a spiral of n selves comes again with 4 and with 4n alone, from all its openings, with n a prime, 2 to 11",
        all(again[n] == [4, 4 * n] for n in (2, 3, 5, 7, 11)))
    say("1.4", f"  a spiral of 2 selves comes again with {again[2]}; of 3, 5, 7 and 11 with 4 and 4n alone: "
               f"{all(again[n] == [4, 4 * n] for n in (3, 5, 7, 11))}; of 9 with {again[9]}", "sized")
    random.seed(45)
    tori = {}
    for n in (3, 5, 7, 11, 15, 21):
        sel = [(x, y) for x in range(n) for y in range(n)]
        cn = {((x, y), 9): (y, (x + y) % n) for x, y in sel}
        tori[n] = moments_again(step, opening(sel, {v: random.choice((1, -1)) for v in sel}), cn, most=5000)[1]
    say("4.1", "phi's torus round 7 comes again with 32 and round 11 with 20, twice phi's closing", tori[7] == 32 and tori[11] == 20)
    say("4.1", "21's torus comes again with 32, its part 3's torus with 8 and its part 7's with 32", tori[21] == 32 and tori[3] == 8 and tori[7] == 32)
    say("4.1", "15's torus comes again with 80, its parts' 16 and 40", tori[15] == 80 and tori[3] == 16 and tori[5] == 40)
    say("4.1", f"  phi's torus round 3 comes again with {tori[3]}, twice phi's closing 8; 21's 32 is its parts' {tori[3]} and {tori[7]}, side by side: {tori[21] == lcm(tori[3], tori[7])}", "sized")
say("4.4", "round ten phi's walk comes again with 60, its 0s at 15, 30, 45 and 60, going on turned by 7, 9, 3, 1",
    phi_closing(10) == 60 and [k for k in range(1, 61) if phi_pair(k, 10)[0] == 0] == [15, 30, 45, 60]
    and [phi_pair(k, 10)[1] for k in (15, 30, 45, 60)] == [7, 9, 3, 1])
say("5.1", "the primes to 16, 256, 1,024 and 4,096 are 6, 54, 172 and 564, eleven of them to 31, and 161 from 37 to 1,021",
    [staircase(n) for n in (16, 256, 1024, 4096, 31)] == [6, 54, 172, 564, 11] and prime(37) and prime(1021) and 172 - 11 == 161)
gaps, k, g, last = [], 1, 0, 2
for n in range(3, 4 ** 12 + 1):
    if sieve[n]:
        g, last = max(g, n - last), n
    if n == 4 ** k:
        gaps.append(g)
        k += 1
say("5.1", "the widest stretch across between primes on the surfaces 4 to 16,777,216 is 1, 4, 6, 14, 20, 34, 44, 72, 86, 114, 148 and 154",
    gaps == [1, 4, 6, 14, 20, 34, 44, 72, 86, 114, 148, 154])
say("5.1", "the widest stretch is short of its side from 16 on", all(g < 2 ** (i + 1) for i, g in enumerate(gaps) if i >= 1))
say("5.1", f"  on the surface of 16 the widest stretch is {gaps[1]}, 7 to 11, and its side is 4; it is short of its side from 64 on: "
           f"{all(g < 2 ** (i + 1) for i, g in enumerate(gaps) if i >= 2)}", "sized")
say("5.2", "the parity lead's most on the surfaces 4 to 4,194,304 is 1, 3, 7, 16, 28, 66, 150, 309, 567, 1,253 and 2,254, "
           "multiplied by its own short of twice the surface, and past the side alone from the surface of 4,096 on",
    most_l == said and all(v * v < 2 * 4 ** (i + 1) for i, v in enumerate(most_l))
    and [i for i, v in enumerate(most_l) if v > sides[i]] == list(range(5, 11)))
say("5.2", "Mertens' strict saying of the side alone is of the parity lead", most_m == said)
say("5.2", f"  Mertens' lead, of the numbers with no square part, its most on the same surfaces: {most_m}, past no side: "
           f"{all(v <= s for v, s in zip(most_m, sides))}", "sized")
say("5.2", "the lead of the numbers with no square part returns to 0 on all surfaces from 64 on, more the farther out",
    all(z > 0 for z in zeros_m[2:]) and zeros_m[2:] == sorted(zeros_m[2:]))
say("5.2", "the lead of the numbers with no square part, to the surfaces 4,096, 65,536, 1,048,576 and 4,194,304: on its + side, on its - side, "
           "at 0, across its 0, and its most + and -, as v406me's line of 24 November has them, stepped apart",
    sides_m == {4096: (1402, 2487, 207, 69, 23, 25), 65536: (27263, 37134, 1139, 356, 96, 113),
                1048576: (521539, 521676, 5361, 1652, 311, 368), 4194304: (2236774, 1947776, 9754, 3022, 550, 683)})
say("5.2", f"  stepped here: {sides_m}", "sized")
say("4.3 and 4.4", "the parity lead returns to 0 on all surfaces", all(z > 0 for z in zeros_l))
say("4.3 and 4.4", f"  the parity lead's returns to 0 on the surfaces 4 to 4,194,304: {zeros_l}, its last at {last_zero_l}; "
                   f"the lead of the numbers with no square part's: {zeros_m}", "sized")
say("5.3", "22,021 is at 61 round 120, and 2,757,241, 6,368,689 and 9,863,461 at 1, 49 and 61, all their parts ending in 1 or 9",
    [v % 120 for v in (22021, 2757241, 6368689, 9863461)] == [61, 1, 49, 61]
    and all(x * y == n and prime(x) and prime(y) and x % 10 in (1, 9) and y % 10 in (1, 9)
            for n, x, y in ((2757241, 461, 5981), (6368689, 1129, 5641), (9863461, 2221, 4441))))
say("5.3", "19 by 19 is 1 round 120, and 61 by 61 is 1 round 120", 361 % 120 == 1 and 3721 % 120 == 1)

for r, sec, text in out:
    print(f"{r:>6} | {sec} | {text}")
print(f"{sum(1 for o in out if o[0] == 'is')} is; {sum(1 for o in out if o[0] == 'is-not')} is-not; {sum(1 for o in out if o[0] == 'sized')} sized.")
