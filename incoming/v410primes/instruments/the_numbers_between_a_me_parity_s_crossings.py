# The numbers between a me-parity's crossings, and the places round a seam laid place by place round the seam's me-parities.
# Breaking tests at the seams of 2 to 13 (2, 6, 30, 210, 2,310, 30,030). A test proves nothing past its numbers.
from math import gcd
from itertools import product
P = [2, 3, 5, 7, 11, 13]
isnots = {}
def no(k, bad=1): isnots[k] = isnots.get(k, 0) + (1 if bad else 0)
seam = 1
for k, p in enumerate(P, 1):
    seam *= p; ps = P[:k]
    # 1: between two neighbouring crossings of a me-parity, the me-parity less 1 numbers
    no("1 the me-parity less 1 between two crossings", any(len([n for n in range(m*p+1, (m+1)*p)]) != p-1 for m in range(4)))
    # 2: a place round the seam is one set of places round the me-parities, and all sets are one place alone
    sets = {}
    for n in range(seam): sets.setdefault(tuple(n % q for q in ps), []).append(n)
    want = 1
    for q in ps: want *= q
    no("2 all sets, one place alone", len(sets) != want or any(len(v) != 1 for v in sets.values()))
    # 3: the numbers one after an other step one place on round all the me-parities at once: one spiral through all places once
    seen = set(); t = tuple(0 for _ in ps)
    for n in range(seam):
        no("3 the spiral is the numbers' own", sets[t][0] != n); seen.add(t); t = tuple((a+1) % q for a, q in zip(t, ps))
    no("3 one spiral, all places once", len(seen) != seam or t != tuple(0 for _ in ps))
    # 4: the uncrossed places are the sets with no place 0: the me-parities less 1, multiplied
    U = [n for n in range(seam) if gcd(n, seam) == 1]
    w = 1
    for q in ps: w *= q-1
    no("4 uncrossed: no place 0, the me-parities less 1 multiplied", len(U) != w or any((0 in s) == (gcd(v[0], seam) == 1) for s, v in sets.items()))
    Us = set(U)
    if seam <= 2310:
        # 5: an uncrossed place by an uncrossed place is an uncrossed place, place by place
        no("5 uncrossed by uncrossed is uncrossed", any((a*b) % seam not in Us for a in U for b in U))
        no("5 place by place", any(tuple((x*y) % q for x, y, q in zip([a % q for q in ps], [b % q for q in ps], ps)) != tuple((a*b) % q for q in ps) for a in U[:40] for b in U[:40]))
        # 6: an uncrossed place has one uncrossed place with the two multiplied at place 1
        no("6 one place with the two multiplied at place 1", any(sum(1 for b in U if (a*b) % seam == 1) != 1 for a in U))
    # 7: the uncrossed places with the place by itself at place 1: 2 by itself the number of the seam's odd me-parities
    own = [a for a in U if (a*a) % seam == 1]
    no("7 by itself at place 1: 2 by itself the odd me-parities' number of times", len(own) != 2 ** (k-1))
    # the fold
    no("the fold", any((seam - a) % seam not in Us for a in U))
    print("seam", seam, "; the me-parities less 1:", [q-1 for q in ps], "; uncrossed:", len(U), "; by itself at place 1:", own if seam <= 210 else len(own))
# the seam 30 laid by place round 5 and place round 6
print("round 30, a line a place round 5, along a line the places round 6:")
for r in range(5): print("  ", r, [next(n for n in range(30) if n % 5 == r and n % 6 == c) for c in range(6)])
print("7 by 11 round 30:", 77 % 30, "; 7 by 13:", 91 % 30, "; 17 by 23:", (17*23) % 30, "; 11, 19, 29 by itself:", 121 % 30, 361 % 30, 841 % 30)
# an opener's universe: the numbers uncrossed by the me-parities to the opener are the universe's me-parities, alone
def isp(n): return n > 1 and all(n % d for d in range(2, int(n**0.5)+1))
primes = [n for n in range(2, 400) if isp(n)]
for i in range(len(primes)-1):
    p, q = primes[i], primes[i+1]
    unc = [n for n in range(p*p, q*q) if all(n % r for r in primes[:i+1])]
    no("the universe: uncrossed are the me-parities alone", unc != [n for n in range(p*p, q*q) if isp(n)])
print("the universe of 5, 25 to 48, uncrossed by 2, 3 and 5:", [n for n in range(25, 49) if n % 2 and n % 3 and n % 5])
print("the universe of 13: numbers", 17*17 - 169, "; me-parities", sum(1 for n in range(169, 289) if isp(n)), "; the seam's uncrossed places", 5760, "of", 30030)
print("is-nots:", isnots, "; all:", sum(isnots.values()))
