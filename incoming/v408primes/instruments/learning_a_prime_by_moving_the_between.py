# v408primes · two focal lengths and a between moved up from the side: the method of learning a prime number.
# A number laid as two edges, a and b, about their between c, half their difference d: a x b + d x d = c x c.
# Whole numbers, and half-moments counted whole. Execute: python3 -I learning_a_prime_by_moving_the_between.py
from math import isqrt

def is_prime(n):
    return n > 1 and all(n % k for k in range(2, isqrt(n) + 1))
def is_me_again(m):
    return m >= 0 and isqrt(m) ** 2 == m

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

N = 20000

# 1. Two edges a and b about their between c: their crossing and the me again of half their difference is the between's me again.
say("two edges crossed and the me again of half their difference is their between's me again, 3 x 7 + 2 x 2 = 5 x 5, all edges of one parity to 300",
    all(a * b + ((b - a) // 2) ** 2 == ((a + b) // 2) ** 2 for a in range(1, 301) for b in range(a, 301, 2)))

# 2. Every odd number has its far between, (n + 1) / 2, its edges 1 and n: with all numbers.
say("every odd number is the me again of (n + 1) / 2 less the me again of (n - 1) / 2: its far between, edges 1 and n, to 20,000",
    all(((n + 1) // 2) ** 2 - ((n - 1) // 2) ** 2 == n for n in range(1, N, 2)))

# 3. Learning: from the side up, move the between until its me again less the number is a me again.
def learn(n):
    c, steps = isqrt(n), 0
    if c * c < n:
        c += 1
    while True:
        steps += 1
        if is_me_again(c * c - n):
            d = isqrt(c * c - n)
            return c, d, steps
        c += 1
ok = True
for n in range(3, N, 2):
    c, d, steps = learn(n)
    ok = ok and (is_prime(n) == (c == (n + 1) // 2 and d > 0))
say("an odd number is a prime when the between moved up from its side meets a me again only at its far end, (n + 1) / 2, 3 to 19,999", ok)
c, d, s = learn(899)
say("the twins' crossing 29 x 31 = 899 is learned at the first step up from its side: between %d, half-difference %d, edges %d and %d" % (c, d, c - d, c + d),
    (c, d, s) == (30, 1, 1))
c, d, s = learn(997)
say("a prime, 997, is learned only at its far between %d, after %d steps up from its side" % (c, s), c == 499 and d == 498)

# 4. A me again's between sits at its side, its two edges one: half-difference 0.
say("a me again's between is at its side, its two edges one, 49 = 7 x 7, every me again to 20,000",
    all(learn(s * s)[:2] == (s, 0) for s in range(1, isqrt(N) + 1)))

# 5. 2 and the numbers 2 round 4 have no whole between; counted in half-moments, every number's every pair of edges
#    a x b is a between: 4n is (a + b) x (a + b) less (b - a) x (b - a). 2's one between is 3 half-moments, edges 1 and 2.
say("no number 2 round 4 has a whole between, 2, 6, 10 ..., to 2,000",
    all(not any(is_me_again(c * c - n) for c in range(isqrt(n), n + 1)) for n in range(2, 2000, 4)))
def betweens_in_half_moments(n):
    return [(a + n // a, n // a - a) for a in range(1, isqrt(n) + 1) if n % a == 0]
say("counted in half-moments, 2's one between is %s, edges 1 and 2; every number's betweens are its pairs of edges, to 20,000" % betweens_in_half_moments(2),
    betweens_in_half_moments(2) == [(3, 1)] and all(all(C * C - D * D == 4 * n for C, D in betweens_in_half_moments(n)) for n in range(1, N)))

# 6. A prime is the number with one between and its two edges apart; 1's one between has its edges one.
say("a number is a prime when it has one between in half-moments and its two edges apart; 1's one between has its edges one, to 20,000",
    all(is_prime(n) == (len(betweens_in_half_moments(n)) == 1 and betweens_in_half_moments(n)[0][1] > 0) for n in range(1, N)))

print("All is." if all(results) else "A line is-not.")
