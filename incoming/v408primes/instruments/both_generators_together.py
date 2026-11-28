# v408primes · both generators together, both-both: the 1 to 17 fractal traveling its skeleton round 510,510, now, and
# the seventeen primes going 2 to 59 and returning 61 to 118, the return bounding a universe, 120 by itself; the next
# universe bounded by the prior's bound by itself, a power; its loops the prior universe's me-parities, prior; the
# skeleton the same at all seams, same-existing; the loops more at a next universe, changing. Whole numbers.
# Execute: python3 -I both_generators_together.py
import time
from math import gcd, isqrt
import numpy as np

SEAM = 510510
skeleton = np.array([gcd(r, SEAM) == 1 for r in range(SEAM)], dtype=bool)      # the 1 to 17 fractal's places, same-existing

def travel(lo, hi, loops):
    """Now: the skeleton's places from lo to hi, a place uncrossed by the loops given is a me-parity."""
    out = []
    S = 1 << 24
    for a in range(lo, hi, S):
        b = min(a + S, hi)
        idx = np.arange(a, b)
        alive = skeleton[idx % SEAM].copy()
        for q in loops:
            if q * q >= b:
                break
            st = max(q * q, a + (-a) % q)
            alive[st - a::q] = False
        out.append(idx[alive])
    return np.concatenate(out) if out else np.array([], dtype=np.int64)

results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)

fractal = [2, 3, 5, 7, 11, 13, 17]
t0 = time.time()
u0 = fractal + [int(x) for x in travel(18, 120, fractal)]                 # the 1 to 17 fractal travels to 120
going = u0[:17]; returning = [p for p in u0 if 60 < p < 120]
say("universe 0: the fractal travels to 120; the seventeen going %s to %d, added 440; returning %d, %d to %d; 60 between"
    % ("2", going[-1], len(returning), returning[0], returning[-1]), going[-1] == 59 and sum(going) == 440 and len(returning) == 13)
bound, loops, universes = 120, u0, []
for k in (1, 2):
    nxt = bound * bound                                                     # next: the prior bound by itself, a power
    found = [int(x) for x in travel(bound, nxt, [q for q in loops if q > 17])]
    universes.append((k, bound, nxt, len(found)))
    loops = loops + found                                                   # changing: the loops more
    bound = nxt
dt = time.time() - t0
for k, lo, hi, n in universes:
    say("universe %d: the return at %s bounds it; traveled on the skeleton to %s, crossed by the prior universe's me-parities: %s me-parities more"
        % (k, f"{lo:,}", f"{hi:,}", f"{n:,}"), n > 0)
# Seen again apart, by all numbers crossed by all their parts, without the skeleton or the universes.
N = bound
s = np.ones(N, dtype=bool); s[:2] = False
for i in range(2, isqrt(N) + 1):
    if s[i]:
        s[i * i::i] = False
apart = np.nonzero(s)[0]
say("both together, %s me-parities below %s in %.0f seconds, the same as all numbers crossed by all their parts"
    % (f"{len(loops):,}", f"{N:,}", dt), len(loops) == len(apart) and int(np.sum(np.array(loops, dtype=np.int64))) == int(np.sum(apart.astype(np.int64))))
say("universe 3 is bounded by %s, the bound by itself again: its loops are the %s me-parities of universes 0 to 2"
    % (f"{N * N:,}", f"{len(loops):,}"), N * N == 120 ** 8)
print("All is." if all(results) else "A line is-not.")
