"""Exhibit THIRTY-TWO Natural Prime Numbering, its draft executed by its own sections.

Whole numbers alone, to 20,000,000; it writes nothing and reaches no network.
A line: the draft's section, is or IS-NOT, the saying, and a note. Grouped by the
draft's sections in their order, for its kit, the one table's concern 69.

Usage: python3 -I exhibit_THIRTY-TWO_executed_by_its_sections.py
"""
from math import gcd, isqrt
from fractions import Fraction
N = 20_000_000
s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
for i in range(2, isqrt(N) + 1):
    if s[i]: s[i*i::i] = bytearray(len(range(i*i, N + 1, i)))
P = [i for i in range(2, 5_000_001) if s[i]]
pi = [0] * 5_000_001
c = 0
for i in range(5_000_001):
    c += s[i]; pi[i] = c
out = []
def say(sec, claim, ok, note=''):
    out.append((sec, 'is' if ok else 'IS-NOT', claim, note))

say('1.3', 'staircase to 60, 100, 120 is 17, 25, 30', (pi[60], pi[100], pi[120]) == (17, 25, 30))
def units(m): return [r for r in range(m) if gcd(r, m) == 1]
tw = []
for m in (6, 30, 210, 2310):
    u = set(units(m)); tw.append(sum(1 for r in u if (r + 2) % m in u))
say('1.3', 'pairs two apart in turns 6, 30, 210, 2310: 1, 3, 15, 135', tw == [1, 3, 15, 135], str(tw))
say('1.3', 'seventh turn places 1*2*4*6*10*12*16 = 92,160', len(units(510510)) == 92160 == 1*2*4*6*10*12*16)
say('1.3', 'turn of 30: all primes fit the flip but 2, 3, 5', all(s[30 - p] for p in (7, 11, 13, 17, 19, 23, 29)),
    '29 pairs with 1, and 1 is no prime' if not s[1] else '')
say('1.4', '8,190 openings of 1 to 12 selves', sum(2 ** n for n in range(1, 13)) == 8190)
le = [x for x in range(1, 121) if pi[x] * 4 < x]
eq = [x for x in range(1, 121) if pi[x] * 4 == x]
gt = [x for x in range(121, 5_000_001) if pi[x] * 4 >= x]
say('1.5', 'staircase above x/4 to 120, on it at 96, 100, 120', not le and eq == [96, 100, 120], f'on it at {eq}; under it at {le[:5]}')
say('1.5', 'past 120 under x/4, stepped to 5,000,000', not gt, f'not under at {gt[:5]}')
u120 = units(120); sq = {}
for r in u120: sq.setdefault(r * r % 120, []).append(r)
say('1.6', 'units of 120: two pieces of 16, squares 1 and 49', sorted((k, len(v)) for k, v in sq.items()) == [(1, 16), (49, 16)])
say('1.6', 'primes ending 1/9 square to 1, ending 3/7 to 49, round 120, from 7 to 1,000,000',
    all((p * p % 120 == 1) == (p % 10 in (1, 9)) for p in P if 7 <= p <= 1_000_000))
say('1.6', 'a prime from 5 on squared is 1 round 24', all(p * p % 24 == 1 for p in P if p >= 5))
bad = [p for p in P if p >= 5 and pow(p, 4, 240) != 1]
say('1.6', 'a prime from 5 on to the fourth is 1 round 240', not bad, f'not so at {bad[:3]}: 5 to the fourth is {pow(5,4,240)} round 240; from 7 on it is')
def lam_max(k):  # largest n with x^k = 1 for all units
    return max(n for n in range(2, 1000) if all(pow(x, k, n) == 1 for x in units(n)))
say('1.6', 'squares close all units with 24 the widest, fourth powers with 240', (lam_max(2), lam_max(4)) == (24, 240))
lead = 0; turn = None
for p in P[1:]:
    lead += 1 if p % 4 == 3 else -1
    if lead < 0: turn = p; break
say('1.6', "Chebyshev's lead turns at 26,861", turn == 26861, str(turn))
say('1.6', 'units of 24 are their own inverse', all(r * r % 24 == 1 for r in units(24)))
# 2.2 Liouville
lp = [0] * 1_000_001
for p in P:
    if p > 1_000_000: break
    q = p
    while q <= 1_000_000:
        for m in range(q, 1_000_001, q): lp[m] += 1
        q *= p
L = 0; worst = True; neg = True
for n in range(1, 1_000_001):
    L += -1 if lp[n] % 2 else 1
    if n > 1 and L > 0: neg = False
    if L * L >= 2 * n: worst = False
say('2.2', 'Liouville lead: the -s lead to 1,000,000', neg)
say('2.2', 'Liouville lead squared short of twice the number to 1,000,000', worst)
def leg(x, ps):
    tot = 0
    from itertools import combinations
    for k in range(len(ps) + 1):
        for c in combinations(ps, k):
            m = 1
            for q in c: m *= q
            tot += (-1) ** k * (x // m)
    return tot
say('2.2', 'Legendre to 120 with 2,3,5,7: 27 uncrossed, staircase 30', leg(120, [2, 3, 5, 7]) == 27 and 27 + 4 - 1 == 30)
rat = []; r = Fraction(1)
for p in (2, 3, 5, 7, 11, 13): r *= Fraction(p - 1, p); rat.append(r)
say('2.2', 'slopes 1/2, 1/3, 4/15, 8/35, 16/77, 192/1001', [str(x) for x in rat] == ['1/2', '1/3', '4/15', '8/35', '16/77', '192/1001'])
say('2.3', 'a prime between n^2 and (n+1)^2, squares to 1,000', all(pi[(n + 1) ** 2] > pi[n * n] for n in range(1, 1000)))
say('2.3', 'Bertrand to 500,000', all(pi[2 * n] > pi[n] for n in range(1, 500_001)))
say('2.3', 'Goldbach to 20,000', all(any(s[p] and s[n - p] for p in range(2, n // 2 + 1)) for n in range(4, 20_001, 2)))
say('2.3', '7 to 907 by 150, seven primes; 199 to 2089 by 210, ten', all(s[7 + 150 * k] for k in range(7)) and all(s[199 + 210 * k] for k in range(10)) and 199 + 210 * 9 == 2089)
say('2.4', '2^11 - 1 = 2047 = 23 * 89; 341 and 2047 pass doubling', 2047 == 23 * 89 and pow(2, 340, 341) == 1 and pow(2, 2046, 2047) == 1)
def fib(n, m):  # F(n) mod m
    a, b = 0, 1
    for bit in bin(n)[2:]:
        c2 = a * ((2 * b - a) % m) % m; d = (a * a + b * b) % m
        a, b = (d, (c2 + d) % m) if bit == '1' else (c2, d)
    return a
def jac5(n): return 1 if n % 5 in (1, 4) else -1
def both(n): return pow(2, n - 1, n) == 1 and fib(n - jac5(n), n) == 0
say('2.4', '2,757,241 = 461 * 5,981 passes doubling and phi', 2757241 == 461 * 5981 and both(2757241))
found = [n for n in range(5, N + 1, 2) if not s[n] and n % 5 in (2, 3) and pow(2, n - 1, n) == 1 and fib(n + 1, n) == 0]
say('2.4', 'no crossed number ending 3 or 7 passes both, to 20,000,000', not found, str(found[:3]))
o = next(k for k in range(1, 3000) if pow(3, k, 2047) == 1)
say('2.4', 'round 2047, 3 has a spiral of 88; gcd(3^44 - 1, 2047) = 23', o == 88 and gcd(pow(3, 44, 2047) - 1, 2047) == 23, str(o))
say('2.5', 'n^2 + n + 41 prime for n 0 to 39', all(s[n * n + n + 41] for n in range(40)) and 40 * 40 + 40 + 41 == 41 * 41)
cic = {c: sum(2520 // (c * k // gcd(c, k)) for k in range(2, 10)) for c in (12, 13, 14, 15, 16, 17, 18)}
say('2.5', 'cicadas in 2,520 years: 350 with 13, 268 with 17, 645 to 1,087 the others', cic[13] == 350 and cic[17] == 268 and min(cic[c] for c in (12, 14, 15, 16, 18)) == 645 and max(cic[c] for c in (12, 14, 15, 16, 18)) == 1087, str(cic))
say('2.6', "Descartes' 198,585,576,189 = 3^2 7^2 11^2 13^2 * 22,021, and 22,021 = 19^2 * 61", 198585576189 == 9 * 49 * 121 * 169 * 22021 and 22021 == 361 * 61)
say('3.2', '37 = 4^3 - 3^3; 1, 7, 19, 37, 61', 37 == 64 - 27 and [3 * n * n + 3 * n + 1 for n in range(5)] == [1, 7, 19, 37, 61])
fours = [(n, 60 - n, 60 + n, 120 - n) for n in (1, 7, 11, 13, 17, 19, 23, 29)]
allp = [f for f in fours if all(s[x] for x in f)]
say('3.3', 'four of the eight fours all primes', allp == [(7, 53, 67, 113), (13, 47, 73, 107), (19, 41, 79, 101), (23, 37, 83, 97)], str(allp))
say('3.5', 'n^3 - n: 24, 60, 120', [n ** 3 - n for n in (3, 4, 5)] == [24, 60, 120])
def pis(m):
    a, b, k = 0, 1, 0
    while True:
        a, b, k = b, (a + b) % m, k + 1
        if (a, b) == (0, 1): return k
P_ = {m: pis(m) for m in (3, 5, 7, 10, 11, 15, 21)}
say('4.1', 'phi torus twice the Pisano period: round 7, 32; round 11, 20', 2 * P_[7] == 32 and 2 * P_[11] == 20, str(P_))
say('4.1', "21's torus 32 with its part 3's torus 8", 2 * P_[3] == 8,
    f"by the same rule as 7's 32, 3's torus is {2 * P_[3]}; 8 is its Pisano period alone; 15's example has 3's as 16")
say('4.1', "15's torus 80, its parts' 16 and 40", 2 * P_[15] == 80 and 2 * P_[3] == 16 and 2 * P_[5] == 40)
say('4.4', 'round ten phi comes again with 60, zeros at 15, 30, 45, 60', P_[10] == 60 and [k for k in range(1, 61) if fib(k, 10) == 0] == [15, 30, 45, 60])
say('5.1', 'surface 1,024: 11 primes to 32, 161 more to 1,021', pi[32] == 11 and pi[1024] - pi[32] == 161)
say('5.1', 'primes to sides: 6, 54, 172, 564', [pi[16], pi[256], pi[1024], pi[4096]] == [6, 54, 172, 564])
gaps = []
for k in range(1, 13):
    lim = 4 ** k; g = 0; prev = 2
    for p in P:
        if p > lim: break
        g = max(g, p - prev); prev = p
    gaps.append(g)
say('5.1', 'widest gaps on surfaces 4^1 to 4^12', gaps == [1, 4, 6, 14, 20, 34, 44, 72, 86, 114, 148, 154], str(gaps))
mu = [1] * 4_194_305; isq = bytearray(4_194_305)
for p in P:
    if p > 4_194_304: break
    for m in range(p, 4_194_305, p): mu[m] = -mu[m]
    for m in range(p * p, 4_194_305, p * p): mu[m] = 0
M = 0; mx = []; k = 1; best = 0; sum_m = [0] * 4_194_305
for n in range(1, 4_194_305):
    M += mu[n]; best = max(best, abs(M)); sum_m[n] = M
    if n == 4 ** k: mx.append(best); k += 1
say('5.2', "the lead's most on surfaces 4 to 4^11, as the lead of the numbers with no square part (Mertens)", mx == [1, 3, 7, 16, 28, 66, 150, 309, 567, 1253, 2254], str(mx) + ': it is the other lead')
spf = list(range(4_194_305))
for i in range(2, isqrt(4_194_304) + 1):
    if spf[i] == i:
        for j in range(i * i, 4_194_305, i):
            if spf[j] == j: spf[j] = i
lam = [1] * 4_194_305
for n in range(2, 4_194_305): lam[n] = -lam[n // spf[n]]
L = 0; best = 0; lx = []; k = 1; sum_l = [0] * 4_194_305
for n in range(1, 4_194_305):
    L += lam[n]; best = max(best, abs(L)); sum_l[n] = L
    if n == 4 ** k: lx.append(best); k += 1
say('5.2', "the lead's most on surfaces 4 to 4^11, as the parity lead of 2.2 (Liouville)", lx == [1, 3, 7, 16, 28, 66, 150, 309, 567, 1253, 2254], str(lx))
say('5.2', 'its square short of twice the surface', all(m * m < 2 * 4 ** (i + 1) for i, m in enumerate(lx)))
say('5.2', 'it passes the side alone from the surface of 4,096 on', [4 ** (i + 1) for i, m in enumerate(lx) if m > 2 ** (i + 1)][0] == 4096)

# 4.3 and 4.4, the parity lead's returns to 0, and the other lead's: the one table's concern 39
z_l = [n for n in range(1, 4_194_305) if sum_l[n] == 0]
say('4.3', 'the parity lead returns to 0 at nine numbers, the last 586', z_l == [2, 4, 6, 10, 16, 26, 40, 96, 586], str(z_l))
say('4.3', 'it returns on no surface from 4,096 to 4,194,304', not [n for n in z_l if n > 586])
ring = [sum(1 for n in range(4 ** (k - 1) + 1, 4 ** k + 1) if sum_m[n] == 0) for k in range(1, 12)]
say('4.3', 'the lead of the numbers with no square part returns to 0 between all surfaces from 16 to 4,194,304', all(ring[2:]), f'returns between the surfaces 1 to 4,194,304: {ring}; none between 4 and 16')
# 5.1, the widest stretch short of its side: concern 42
say('5.1', 'the widest stretch short of its side from 16 on', all(g < 2 ** (k + 1) for k, g in enumerate(gaps) if 4 ** (k + 1) >= 16), 'on the surface of 16 it is 4, its side; from 64 on it is short')
say('5.1', 'the widest stretch short of its side from 64 on', all(g < 2 ** (k + 1) for k, g in enumerate(gaps) if 4 ** (k + 1) >= 64))
# 2.4, the walk on the plane's primes
def gp(a, b):
    if a == 0 or b == 0:
        m = abs(a or b); return m < len(s) and s[m] == 1 and m % 4 == 3
    return s[a * a + b * b] == 1
walks = []
for kk in (2, 4, 8):
    st = [(dx, dy) for dx in range(-3, 4) for dy in range(-3, 4) if 0 < dx * dx + dy * dy <= kk]
    seen = {(1, 1)}; todo = [(1, 1)]; far = 2
    while todo:
        a, b = todo.pop()
        for dx, dy in st:
            q = (a + dx, b + dy)
            if q not in seen and gp(*q):
                seen.add(q); todo.append(q); far = max(far, q[0] ** 2 + q[1] ** 2)
    walks.append(far)
say('2.4', 'walks from 1 + i with steps of length squared 2, 4, 8 bounded at 137, 2,053, 8,737', walks == [137, 2053, 8737], str(walks))
# 5.3, the crossed numbers passing both of a prime's closings, by the draft's own closing of phi
def closes(n):
    e = n - 1 if n % 5 in (1, 4) else 2 * (n + 1)
    return pow(2, n - 1, n) == 1 and fib(e, n) == 0 and fib(e + 1, n) == 1
def pf(n):
    f = set(); d = 3
    while d * d <= n:
        while n % d == 0: f.add(d); n //= d
        d += 2
    if n > 1: f.add(n)
    return f
def order2(p):
    k = 1; x = 2 % p
    while x != 1: x = x * 2 % p; k += 1
    return k
bothall = [n for n in range(3, N + 1, 2) if not s[n] and n % 5 and closes(n)]
say('5.3', 'crossed numbers passing both to 20,000,000: 46, the lowest 219,781', len(bothall) == 46 and bothall[0] == 219781, f'{len(bothall)}, the lowest {bothall[0]}')
one = [n for n in bothall if len({order2(p) for p in pf(n)}) == 1]
say('5.3', "the draft's three are the ones with doubling's spiral of one length round all their parts", one == [2757241, 6368689, 9863461], str(one))
say('5.3', 'none of them ends in 3 or 7', not [n for n in bothall if n % 10 in (3, 7)])

say('5.3', 'the three passing both at 1, 49 or 61 round 120', all(both(n) for n in (2757241, 6368689, 9863461)) and {n % 120 for n in (2757241, 6368689, 9863461)} <= {1, 49, 61}, str([n % 120 for n in (2757241, 6368689, 9863461)]))
order = ['1.3', '1.4', '1.5', '1.6', '2.2', '2.3', '2.4', '2.5', '2.6', '3.2', '3.3', '3.5', '4.1', '4.3', '4.4', '5.1', '5.2', '5.3']
for sec in order:
    for o_ in out:
        if o_[0] == sec: print(' | '.join(o_))
print('IS-NOT:', sum(1 for o_ in out if o_[1] != 'is'), 'of', len(out))
