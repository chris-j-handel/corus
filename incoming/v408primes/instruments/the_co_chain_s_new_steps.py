# v408primes · the co-chain's new steps. Whole numbers alone. Execute: python3 -I the_co_chain_s_new_steps.py
from math import gcd, isqrt
def is_prime(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)
# The +1 from two neighbours' crossing shares no part with either neighbour: a +1 in neither self alone.
say("n x n, the +1 from the crossing of n - 1 and n + 1, shares no part with either, n of 2 to 100,000",
    all(gcd(n * n, n - 1) == 1 and gcd(n * n, n + 1) == 1 and (n - 1) * (n + 1) + 1 == n * n for n in range(2, 100001)))
# Every me again has its next me again by the +1 of its side: a turn closing with all numbers.
say("every me again s x s has its next me again (s + 1) x (s + 1), s x s and its side twice and 1 more, s of 1 to 100,000",
    all((s + 1) * (s + 1) == s * s + 2 * s + 1 for s in range(1, 100001)))
# A prime is not crossed by any other prime's spiral, and comes by +1 alone.
say("a prime is crossed by no other prime's spiral, and every number crossed by no smaller prime's spiral past 1 is a prime, to 50,000",
    all(is_prime(n) == all(n % q for q in range(2, n) if is_prime(q) and q * q <= n) for n in range(2, 50001)))
print("All is." if all(results) else "A line is-not.")
