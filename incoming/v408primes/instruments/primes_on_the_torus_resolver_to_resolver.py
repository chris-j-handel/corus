# v408primes · where the primes are on a surface: a torus of primes, resolver to resolver.
# Whole numbers alone: +1, multiplying, a number round a number, comparing. Each line ends is or is-not.
# Execute: python3 -I primes_on_the_torus_resolver_to_resolver.py

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

PRIMES = [n for n in range(2, 400) if is_prime(n)]
results = []

def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

# 1. Two primes are a torus: p places along, q across. The +1 steps one along and one across together,
#    and winds the torus, passing all p x q places once, then comes again at p x q, its turn.
ok = True
for i, p in enumerate(PRIMES[:10]):
    for q in PRIMES[i + 1:12]:
        seen, place, n = set(), (0, 0), 0
        while True:
            seen.add(place)
            n += 1
            place = ((place[0] + 1) % p, (place[1] + 1) % q)
            if place == (0, 0):
                break
        ok = ok and n == p * q and len(seen) == p * q
say("two primes p and q: the +1 winds their torus through all p x q places once and comes again at p x q (primes 2 to 37)", ok)

# 2. A number is located on the torus by its two places alone: the place along and the place across
#    are one number of the turn, no other. Triangulating a number from two primes.
ok = True
for p, q in [(11, 13), (5, 7), (29, 31), (17, 37)]:
    where = {}
    for n in range(p * q):
        where.setdefault((n % p, n % q), []).append(n)
    ok = ok and all(len(v) == 1 for v in where.values())
say("a number of the turn of p and q is one place of their torus, found again from its two places alone: 97 on the torus of 11 and 13 is (9, 6), and (9, 6) is 97 alone", ok and (97 % 11, 97 % 13) == (9, 6))

# 3. The crossings: p crosses the numbers at 0 along, a circle across the torus; q at 0 across, a circle
#    along it. The two circles meet once, at the turn. p + q - 1 places crossed, (p - 1) x (q - 1) uncrossed.
ok = True
for p, q in [(2, 3), (3, 5), (5, 7), (11, 13)]:
    crossed = sum(1 for n in range(p * q) if n % p == 0 or n % q == 0)
    meet = [n for n in range(p * q) if n % p == 0 and n % q == 0]
    ok = ok and crossed == p + q - 1 and meet == [0]
say("the crossings of two primes are two circles of their torus, meeting at its turn alone: p + q - 1 crossed, (p - 1) x (q - 1) uncrossed", ok)

# 4. Resolver to resolver: the torus of the primes to p, its turn the primes multiplied, passes on to the
#    torus with the next prime r: a place is lifted r ways, one of them crossed by r and r - 1 a place.
def places(turn, ps):
    return [n for n in range(turn) if all(n % p for p in ps)]

ok, turn, ps = True, 1, []
for r in PRIMES[:6]:
    before = places(turn, ps) if ps else [0]
    after_turn, after_ps = turn * r, ps + [r]
    after = places(after_turn, after_ps)
    for a in before:
        lifts = [a + k * turn for k in range(r)]
        if sum(1 for x in lifts if x % r == 0) != 1:
            ok = False
    ok = ok and len(after) == len(before) * (r - 1)
    turn, ps = after_turn, after_ps
say("resolver to resolver: a place of the torus to p is r places of the next torus, one crossed by r and r - 1 uncrossed, turns 2 to 30,030", ok)

# 5. The horizon: on the torus of the primes to p, the uncrossed places past 1 and below the next prime's
#    square are the primes there, all of them and no other number.
ok = True
for k in range(1, 8):
    ps = PRIMES[:k]
    horizon = PRIMES[k] * PRIMES[k]
    uncrossed = [n for n in range(2, horizon) if all(n % p for p in ps)]
    primes_there = [n for n in range(PRIMES[k - 1] + 1, horizon) if is_prime(n)]
    ok = ok and uncrossed == primes_there
say("on the torus of the primes to p, the uncrossed places from 2 to the next prime's square are all the primes there and no other number, p of 2 to 17 (horizons 9 to 361)", ok)

# 6. The bi-folding: a turn folded about its half is a pair of cones, vertex 0 and the turn, widest at
#    the half. An uncrossed place n has its podal turn - n uncrossed too, and the two make the turn,
#    0 round the turn: an all-parity of 0, the +1's and the -1's orientation together.
ok = True
for ps in [[2, 3], [2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11]]:
    t = 1
    for p in ps:
        t *= p
    pl = set(places(t, ps))
    ok = ok and all((t - n) in pl and (n + (t - n)) % t == 0 for n in pl)
say("a turn's uncrossed places fold onto themselves about its half: n and turn - n, both uncrossed, making 0 round the turn, turns 6 to 2,310", ok)

# 7. Two primes alone: on the torus of 5 and 7 by itself, an uncrossed place is a prime or is crossed by a
#    prime below 5. Two primes locate a number; the primes to its horizon tell its crossing.
p, q = 5, 7
unc = [n for n in range(2, p * q) if n % p and n % q]
not_prime = [n for n in unc if not is_prime(n)]
say("two primes alone locate a number and do not tell its crossing: uncrossed on the torus of 5 and 7 and crossed by 2 or 3, %s" % not_prime, len(not_prime) > 0)

# 8. The places a number has on the torus of the primes to its horizon tell its crossing all or none.
ok = True
for n in range(2, 5000):
    ps = [p for p in PRIMES if p * p <= n]
    uncrossed = all(n % p for p in ps)
    ok = ok and uncrossed == is_prime(n)
say("a number's places on the torus of the primes to its horizon tell it prime or crossed, all or none, 2 to 4,999", ok)

# 9. Any two primes' torus holds all the other primes among its uncrossed places.
ok = True
for i, p in enumerate(PRIMES[:8]):
    for q in PRIMES[i + 1:9]:
        ok = ok and all(n % p and n % q for n in PRIMES if n not in (p, q))
say("all primes past the two are uncrossed places of any two primes' torus, primes to 397, pairs of 2 to 23", ok)

# 10. The torus carries itself: on the torus of the primes to p, the uncrossed place past 1 nearest 1 is
#     the next prime, and it becomes the next torus's circle. From 2 the resolver goes on with no prime given.
ok, ps = True, [2]
while len(ps) < len(PRIMES):
    n = 2
    while not all(n % p for p in ps):
        n += 1
    ok = ok and n == PRIMES[len(ps)]
    ps.append(n)
say("from 2, the uncrossed place nearest past 1 is the next prime, torus to torus, 2 to 397", ok)

print("All is." if all(results) else "A line is-not.")
