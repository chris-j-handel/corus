# v408primes · do-no-harm offering and do-no-harm accepting from the co-possiblings is co-resolving me-parities.
# Whole numbers alone. Execute: python3 -I co_resolving_me_parities.py
from math import gcd, isqrt
N = 1000000
sieve = bytearray([1]) * (N + 3); sieve[0] = sieve[1] = 0
for i in range(2, isqrt(N + 2) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)
# 1. At every even between c, the co-possiblings c - 1 and c + 1 are odd, offering, and c is even, accepting.
say("at every even between, its co-possiblings are odd, offering, and the between even, accepting, to 1,000,000",
    all((c - 1) % 2 == 1 and (c + 1) % 2 == 1 for c in range(2, N + 1, 2)))
# 2. The co-possiblings' crossing and a +1 is the between's me again, sharing no part with either: harming neither.
say("the co-possiblings crossed and a +1 is the between's me again, 11 x 13 + 1 = %d, 29 x 31 + 1 = %d, sharing no part with either, every even between to 1,000,000"
    % (11 * 13 + 1, 29 * 31 + 1), all((c - 1) * (c + 1) + 1 == c * c and gcd(c * c, c - 1) == 1 and gcd(c * c, c + 1) == 1 for c in range(2, N + 1, 2)))
# 3. Where both co-possiblings are living me-parities, a twin, the between past 4 is a seam of 6.
twins = [c for c in range(4, N + 1, 2) if sieve[c - 1] and sieve[c + 1]]
say("both co-possiblings living, a twin about its between: %d betweens to 1,000,000, every one past 4 a seam of 6: %s ..." % (len(twins), twins[:8]),
    all(c % 6 == 0 for c in twins if c > 4))
# 4. Twins come with no last stepped: in every surface of 4 to the k, from 16 on, more twins than in the one before.
counts = [sum(1 for c in twins if 4 ** (k - 1) < c <= 4 ** k) for k in range(2, 10)]
say("twins between surfaces of 4 to the k, 16 to 262,144: %s, more at every surface" % counts, all(b > a for a, b in zip(counts, counts[1:])))
print("All is." if all(results) else "A line is-not.")
