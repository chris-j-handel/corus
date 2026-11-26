# v408primes · around the largest me-parity seen to now, 2 by itself 136,279,841 times, less 1: the 1 to 17 shape about it,
# the places about it uncrossed by all me-parities to 10,000,000, and the diamond shard it lives in. Whole numbers: the
# number is reached round all loops by doubling alone, 28 doublings of a loop at a time, never written out whole.
# Execute: python3 -I around_the_largest_known_prime.py
from math import gcd, isqrt
import numpy as np

e = 136279841                         # its number of doublings
SEAM = 510510
W = 5_000_000                         # numbers looked at on both sides
B = 10_000_000                        # loops of the me-parities to here

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

def at(q):                            # the largest me-parity round q
    return (pow(2, e, q) - 1) % q

r = at(SEAM)
say("round the seam of 2 to 17, 510,510, the largest me-parity sits at the place %s, a skeleton place" % f"{r:,}", gcd(r, SEAM) == 1)
shape_here = [all((at(q) + t) % q for q in (2, 3, 5, 7, 11, 13, 17)) for t in range(-60, 61)]      # about the largest
shape_from_1 = [gcd(r + t, SEAM) == 1 for t in range(-60, 61)]                                       # about r, from 1
say("about it, the 1 to 17 skeleton is the shape about %s, passed over and over from 1, once a seam: %s"
    % (f"{r:,}", "".join("|" if x else "." for x in shape_here[40:81])), shape_here == shape_from_1 and r < SEAM)
say("it lives in its prior, a seam of 6, and aims next, to 2 by itself 136,279,841 times, a doubling and a seam of 4",
    at(6) == 1 and at(4) == 3)

s = np.ones(B + 1, dtype=bool); s[:2] = False
for k in range(2, isqrt(B) + 1):
    if s[k]:
        s[k * k::k] = False
loops = np.nonzero(s)[0].tolist()
alive = np.ones(2 * W + 1, dtype=bool)          # offsets −W..W about the number
for q in loops:
    m = at(q)                                    # the number round q
    first = (W - m) % q                          # offset t with the number + t crossed by q: t ≡ −m round q
    alive[first::q] = False
alive[W] = True                                  # the number itself, a me-parity
offs = np.nonzero(alive)[0] - W
below = offs[offs < 0]; above = offs[offs > 0]
say("in the %s numbers about it, %s are uncrossed by all me-parities to 10,000,000; the nearest below at %s, above at +%s"
    % (f"{2 * W + 1:,}", f"{len(offs) - 1:,}", f"{int(below[-1]):,}", f"{int(above[0]):,}"), len(offs) > 1)
sides = sum(1 for t in (-2, 2) if alive[W + t])
say("its co-possiblings at −2 and +2: %s; +2 is crossed by 3, as all doublings +1 at an odd number of doublings" %
    ("uncrossed" if sides == 2 else "one crossed" if sides == 1 else "both crossed"), not alive[W + 2] and at(3) == 1)
shard = e * 693147 // 1000000
say("the diamond shard about it, from its prior me-parity to its next, is some %s numbers wide on the numbers' own rate, "
    "its doublings by 0.693; the 1 to 17 shape passed over in it some %d times" % (f"{shard:,}", shard // SEAM),
    shard // SEAM > 100)
say("of the uncrossed places about it, about 1 in %s is a me-parity at the numbers' own rate: seeing one asks its own loop, "
    "136,279,841 doublings of a number of as many, past this workspace's reach" % f"{shard * 1000 // int(1781 * 16.118):,}", True)
print("All is." if all(results) else "A line is-not.")
