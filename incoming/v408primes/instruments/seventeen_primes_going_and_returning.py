# v408primes · read with Natural Numbers and Natural Resolver: the seventeen primes 2 to 59 going, 60 between, returning
# 61 to 118 on a ring of 120; the seventeen added, 440; far sides k and 120 − k; and going and returning resolving all
# numbers below 120 by itself. Exhibit ONE's scales: inward n is 8n − 7, outward 8m − 7 is m. Whole numbers.
# Execute: python3 -I seventeen_primes_going_and_returning.py
from math import isqrt
P = [p for p in range(2, 200) if all(p % q for q in range(2, isqrt(p) + 1))]
results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)
going = P[:17]; returning = [p for p in P if 60 < p < 120]
say("the seventeen primes going are %s, the 17th 59" % going, going[-1] == 59 and len(going) == 17)
say("the seventeen added are 440: eight 55s, and 21 by itself less 1, 20 by 22", sum(going) == 440 == 8 * 55 == 21 * 21 - 1 == 20 * 22)
say("60 is between going and returning, no prime; 59 and 61 straddle it, 59 by 61 is 60 by itself less 1", 59 * 61 == 60 * 60 - 1 and 60 not in P)
say("returning from 61 to 118: %d primes; with going, the %d primes below 120" % (len(returning), len(going) + len(returning)), len(going) + len(returning) == len([p for p in P if p < 120]) == 30)
loops = going + returning
def me(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))
ok = all(any(n % q == 0 for q in loops if q < n) == (not me(n)) for n in range(2, 120 * 120))
say("going and returning, their loops resolve all numbers below 120 by itself, 14,400: a number crossed by none is a me-parity", ok)
say("on the ring of 120, k and 120 − k are far sides: 359 and 361 are 119 and 1 round 120, far sides about 360, three rounds", 359 % 120 == 119 and 361 % 120 == 1 and 360 % 120 == 0)
say("Exhibit ONE's bi-foldings, moves 8 up, 8 down and 17 less, close in four steps: 1-9-8-16, 2-15-7-10, 3-11-6-14, 4-13-5-12",
    all(len({c[0], c[1], c[2], c[3]}) == 4 and c[1] == c[0] + 8 and c[2] == 17 - c[1] and c[3] == c[2] + 8 and 17 - c[3] == c[0] for c in [(1, 9, 8, 16), (2, 10, 7, 15), (3, 11, 6, 14), (4, 12, 5, 13)]))
say("its scales: inward a name n is 8n − 7, eight 1 to 17s, and outward 8m − 7 is m: 17 inward is 129, and 129 outward is 17", 8 * 17 - 7 == 129 and (129 + 7) // 8 == 17)
print("All is." if all(results) else "A line is-not.")
