# The numbers of v410illustrating's pages of the 63rd and 64th drawings, the numbers between the prime crossings, and the eight between,
# made again apart, beside v410primes' co-chainings; and the learnings of the multiplying of the uncrossed places. A test proves nothing past its numbers.
from math import gcd
def isp(n): return n > 1 and all(n % d for d in range(2, int(n**0.5)+1))
def lpf(n): return next(d for d in range(2, n+1) if n % d == 0)
no = {}
def t(k, bad): no[k] = no.get(k, 0) + (1 if bad else 0)
P = [n for n in range(2, 400) if isp(n)]
# the co-linear to 359
ps = [p for p in P if p <= 359]; gaps = [(a, b) for a, b in zip(ps, ps[1:])]
t("to 359: 286 numbers in 71 betweens, widest 13 at 114 to 126, 21 of one number",
  (sum(b-a-1 for a, b in gaps), len(gaps), max(b-a-1 for a, b in gaps), sum(1 for a, b in gaps if b-a == 2)) != (286, 71, 13, 21) or (113, 127) not in gaps)
# a cell between the crossings is a me-parity under the next opener's me again, and not past
for seam, q in ((30, 7), (210, 11), (2310, 13)):
    t(f"round {seam}: uncrossed past 1 and under {q*q} are me-parities, all", any(not isp(n) for n in range(2, q*q) if gcd(n, seam) == 1))
    t(f"round {seam}: {q*q} is uncrossed and a crossing", not (gcd(q*q, seam) == 1 and not isp(q*q)))
print("round 30, uncrossed crossings to 120:", [n for n in range(2, 121) if gcd(n, 30) == 1 and not isp(n)])
# the mes of 30 to 359
mes = [n for n in range(1, 360) if gcd(n, 30) == 1]; cr = [n for n in mes if n > 1 and not isp(n)]
from collections import Counter
t("96 mes: 69 me-parities, 26 crossed, 1; least 7 at 13, 11 at 7, 13 at 4, 17 at 2", (len(mes), sum(isp(n) for n in mes), len(cr), dict(Counter(lpf(n) for n in cr))) != (96, 69, 26, {7: 13, 11: 7, 13: 4, 17: 2}))
for a, b, m, k in ((49, 121, 19, 15), (121, 169, 13, 9), (169, 289, 32, 22), (289, 361, 19, 11)):
    t("a universe's mes and me-parities", (sum(1 for n in range(a, b) if gcd(n, 30) == 1), sum(1 for n in range(a, b) if isp(n))) != (m, k))
# two me-parities 2 apart: all pairs to 100,000
tw = [(p, p+2) for p in range(3, 100000) if isp(p) and isp(p+2)]
for p, q in tw:
    bet = (p-1)*(q-1)
    t("pairs 2 apart: betweens the lesser's me again less 1; cells the between's me again less 1; past 3 and 5 the between a crossing of 6", bet != p*p-1 or p*q != (p+1)**2-1 or (p > 3 and (p+1) % 6))
print("pairs 2 apart to 100,000:", len(tw), "; betweens of 3, 5, 11, 17, 29, 41, 59:", [p*p-1 for p in (3, 5, 11, 17, 29, 41, 59)])
# a me-parity's me again: the +1 of a crossing of 24, past 3; at 1 or 19 round 30, past 5
t("a me-parity's me again past 3 at the +1 of a crossing of 24", any((p*p-1) % 24 for p in P if p > 3))
t("at 1 or 19 round 30", any((p*p) % 30 not in (1, 19) for p in P if p > 5))
# the me agains among the uncrossed places: the middles of the odd me-parities, multiplied
for mod, odd in ((6, [3]), (15, [3, 5]), (30, [3, 5]), (210, [3, 5, 7]), (2310, [3, 5, 7, 11])):
    U = [n for n in range(mod) if gcd(n, mod) == 1]; sq = sorted({(a*a) % mod for a in U}); w = 1
    for p in odd: w *= (p-1)//2
    t("me agains among the uncrossed: the middles multiplied", len(sq) != w)
    if mod <= 30: print("round", mod, "the uncrossed me agains:", sq, "; by itself at place 1:", [a for a in U if (a*a) % mod == 1])
# the eight round 15
U = [n for n in range(15) if gcd(n, 15) == 1]; print("the eight:", U)
t("15 less: a between, odd for even", any((15-n) not in U or (15-n) % 2 == n % 2 for n in U))
t("lifted by 2: the eight round 30", sorted(n if n % 2 else n+15 for n in U) != [n for n in range(30) if gcd(n, 30) == 1])
halves = []
from itertools import combinations
for c in combinations(U, 4):
    if 1 in c and all((a*b) % 15 in c for a in c for b in c): halves.append(c)
print("fours of the eight with 1, a four by a four in the four:", halves)
odd = (1, 7, 11, 13); print("odd by odd:", sorted({(a*b) % 15 for a in odd for b in odd}), "; 7 by 7:", 49 % 15)
bits = lambda n, k: bin(n).count("1")
print("round 15 by digits on:", {n: bits(n, 4) for n in range(16)})
t("round 15: uncrossed with an odd number of digits on, alone", any((gcd(n, 15) == 1) != (bits(n, 4) % 2 == 1) for n in range(1, 15)))
for k in (2, 3, 4, 5, 6):
    m = 2**k - 1; U = [n for n in range(1, m) if gcd(n, m) == 1]; one = [n for n in U if bits(n, k) in (1, k-1)]
    print(f"the -1 at {k} doublings, {m}: uncrossed {len(U)}; one digit on or one not on {len(one)}", "" if len(U) == len(one) else "; other-than: " + str([n for n in U if n not in one][:4]))
    t("doubling steps the digits round", any((2*n) % m != ((n << 1) & m | (n >> (k-1))) % m for n in range(1, m)))
    t("the -1 less a number: all digits on for not on", any((m - n) != (n ^ m) for n in range(m+1)))
print("is-nots:", {k: v for k, v in no.items() if v}, "; lines:", len(no), "; all:", sum(no.values()))
