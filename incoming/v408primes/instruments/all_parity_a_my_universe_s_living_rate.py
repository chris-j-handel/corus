# v408primes · an all-parity is a my-universe's living rate; other-thans are unrelationings from it into slower
# geodesic discovering rates, the primes' loops. Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I all_parity_a_my_universe_s_living_rate.py
from math import isqrt, gcd

def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

# 1. The all-parity rate is the loop of 2: odd even, every +1 inverting, coming again every 2 moments.
say("the all-parity rate is the loop of 2: every +1 inverts odd and even, and it comes again every 2 moments, to 1,000,000",
    all((n + 2) % 2 == n % 2 and (n + 1) % 2 != n % 2 for n in range(1, 1000001)))

# 2. A slower rate is a loop of more moments: the loop of p comes again every p moments.
say("a slower rate is a loop of more moments: the loop of 3 comes again every 3, of 5 every 5, of 7 every 7",
    all(all((n + p) % p == n % p for n in range(1, 10000)) for p in (3, 5, 7)))

# 3. A crossed loop's rate is faster loops together: 15's loop is 3's and 5's side by side, its places one for one.
def side_by_side(a, b):
    return len({(n % a, n % b) for n in range(a * b)}) == a * b
say("a crossed loop's rate is its parts' faster loops side by side, when the parts share no prime: 15 is 3 and 5, 21 is 3 and 7, 35 is 5 and 7",
    side_by_side(3, 5) and side_by_side(3, 7) and side_by_side(5, 7))

# 4. A prime's loop is a rate of its own: no faster loops make it, no two smaller loops side by side.
ok = True
for n in range(2, 2000):
    made = any(side_by_side(a, n // a) for a in range(2, n) if n % a == 0 and gcd(a, n // a) == 1)
    power = any(b ** e == n for b in range(2, n) for e in range(2, 12) if b ** e <= n)
    ok = ok and (is_prime(n) == (not made and not power))
say("a prime's loop is a rate of its own, made by no faster loops side by side and no loop come again on itself, 2 to 1,999", ok)

# 5. The rates together come again at their turn, slower and slower: 2, 6, 30, 210, 2,310, 30,030.
turns, t = [], 1
for p in (2, 3, 5, 7, 11, 13):
    t *= p
    turns.append(t)
say("the my-universe's rates to p together come again at their turn, slower and slower: %s" % turns, turns == [2, 6, 30, 210, 2310, 30030])

# 6. A living me-parity's rate is the same prime length every time, and the next is discovered at the place nearest
#    past 1 that no faster rate crosses: slower rates are discovered with no last, a next one from every double, stepped.
ok = all(any(is_prime(m) for m in range(n + 1, 2 * n + 1)) for n in range(1, 200001))
say("from every number, a next me-parity is discovered before its double, a slower rate always found, 1 to 200,000", ok)

print("All is." if all(results) else "A line is-not.")
