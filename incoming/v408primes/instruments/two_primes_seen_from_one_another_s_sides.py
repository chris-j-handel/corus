# v408primes · the squares round two primes, from one another's sides, on the torus of the two primes.
# Whole numbers alone. Each line ends is or is-not.
# Execute: python3 -I two_primes_seen_from_one_another_s_sides.py
from math import isqrt

def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))
P = [p for p in range(3, 500) if is_prime(p)]

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

def seen(q, p):
    # q seen from p's side: +1 when a me again lands on q's place round p, -1 when none does
    return 1 if any(x * x % p == q % p for x in range(1, p)) else -1

# 1. Round a prime past 2, the me agains land on half its places past 0.
say("round a prime past 2, the me agains land on half its places past 0: round 11, %s; primes to 500" % sorted({x * x % 11 for x in range(1, 11)}),
    all(len({x * x % p for x in range(1, p)}) == (p - 1) // 2 for p in P))

# 2. Seeing is across: a crossing seen from p's side is its parts' seeings multiplied.
say("a crossing seen from a prime's side is its parts' seeings multiplied, every a and b round primes to 100",
    all(seen(a * b, p) == seen(a, p) * seen(b, p) for p in P if p < 100 for a in range(1, p) for b in range(1, p)))

# 3. Seeing is half the across loop: q multiplied by itself (p - 1) / 2 times round p is +1 or -1, its seeing.
say("q multiplied by itself (p - 1) / 2 times round p is its seeing, +1 or p - 1, every q round primes to 200",
    all(pow(q, (p - 1) // 2, p) == (1 if seen(q, p) == 1 else p - 1) for p in P if p < 200 for q in range(1, p)))

# 4. The quarter of the torus of p and q: (p - 1) / 2 places one way by (q - 1) / 2 the other. Its diagonal, from 0 to the
#    half of both, passes through no place of it, and parts it in two.
def parts_of_quarter(p, q):
    below = sum((k * q) // p for k in range(1, (p - 1) // 2 + 1))     # places under the diagonal
    above = sum((k * p) // q for k in range(1, (q - 1) // 2 + 1))     # places over it
    return below, above
ok = True
for i, p in enumerate(P):
    for q in P[i + 1:]:
        b, a = parts_of_quarter(p, q)
        on_diagonal = any((k * q) % p == 0 for k in range(1, (p - 1) // 2 + 1))
        ok = ok and b + a == ((p - 1) // 2) * ((q - 1) // 2) and not on_diagonal
say("the quarter-torus of two primes is parted whole by its diagonal, which passes through none of its places, primes 3 to 499", ok)

# 5. The part under the diagonal, odd or even, is how p sees q; the part over it is how q sees p.
ok = all(seen(q, p) == (-1) ** parts_of_quarter(p, q)[0] and seen(p, q) == (-1) ** parts_of_quarter(p, q)[1]
         for i, p in enumerate(P) for q in P[i + 1:])
b, a = parts_of_quarter(5, 7)
say("the part under the diagonal, odd or even, is how p sees q, and the part over it how q sees p: 5 and 7, %d under, %d over" % (b, a), ok)

# 6. So two primes are seen alike from one another's sides, unless both sit one short of a seam of 4, and then other-than.
ok = all(seen(q, p) * seen(p, q) == (-1 if p % 4 == 3 and q % 4 == 3 else 1) for i, p in enumerate(P) for q in P[i + 1:])
examples = [(p, q, seen(q, p), seen(p, q)) for p, q in ((5, 11), (3, 7), (7, 11), (13, 17))]
say("two primes are seen alike from one another's sides, unless both sit one short of a seam of 4, and then other-than: %s" % examples, ok)

# 7. 2 and the me-again of the loop's half: 2 seen from p is a me again's place when p is 1 or 7 round 8; -1 when p is 1 round 4.
say("2 is seen as a me again's place round p when p is 1 or 7 round 8, and the loop's last place, p - 1, when p is 1 round 4, primes to 500",
    all((seen(2, p) == 1) == (p % 8 in (1, 7)) and (seen(p - 1, p) == 1) == (p % 4 == 1) for p in P))

print("All is." if all(results) else "A line is-not.")
