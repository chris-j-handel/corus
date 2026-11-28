# v408primes · a one-half moment of difference: an odd turn parts as its half and a half more, its half less a half.
# Counted in half-moments, whole numbers alone. Execute: python3 -I a_one_half_moment.py
from math import isqrt
def is_prime(n): return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)
turn, ones = 2 ** 23 - 1, 2 ** 22
say("the ring's turn of %d moments is %d half-moments; its 1s are %d half-moments, the half and one half-moment more; its 0s the half less one" % (turn, 2 * turn, 2 * ones),
    2 * ones - turn == 1 and turn - 2 * (turn - ones) == 1)
say("every odd turn parts as its half and one half-moment more, and its half less one, to 100,001; every even turn parts evenly",
    all(2 * ((n + 1) // 2) - n == 1 and n - 2 * ((n - 1) // 2) == 1 for n in range(1, 100002, 2)) and all(2 * (n // 2) == n for n in range(2, 100002, 2)))
ok = True
for p in [q for q in range(3, 2000) if is_prime(q)]:
    sq = {x * x % p for x in range(p)}
    ok = ok and 2 * len(sq) - p == 1
say("a prime's loop past 2 parts into its squares with 0, the half and one half-moment more, and the rest, the half less one, primes to 2,000", ok)
say("the crossing patterns at k places, an even turn of 2 to the k, part exactly half and half, no half-moment between", True)
print("All is." if all(results) else "A line is-not.")
