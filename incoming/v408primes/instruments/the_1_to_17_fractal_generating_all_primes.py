# v408primes · the 1 to 17 fractal generating all the primes endlessly: traveling the skeleton of the seam of 2 to 17,
# a place a me-parity when no prior me-parity's loop crosses it, and a me-parity aiming itself, its loop begun at its
# own me again and crossing only the skeleton's places. Whole numbers; it has no last, and this run stops it to look.
# Execute: python3 -I the_1_to_17_fractal_generating_all_primes.py [how many me-parities to look at, to 3,000,000]
import sys, time
from math import gcd, isqrt
import numpy as np

given = [int(a.replace(',', '')) for a in sys.argv[1:] if a.replace(',', '').isdigit()]
LOOK = min(given[0], 3_000_000) if given else 1_000_000

FRACTAL = [2, 3, 5, 7, 11, 13, 17]                    # the me-parities of 1 to 17
SEAM = 1
for p in FRACTAL:
    SEAM *= p                                          # 510,510
PLACES = [r for r in range(1, SEAM + 1) if gcd(r, SEAM) == 1]   # the skeleton: 92,160 living places
STEPS = [b - a for a, b in zip(PLACES, PLACES[1:])] + [PLACES[0] + SEAM - PLACES[-1]]
AT = {r: i for i, r in enumerate(PLACES)}
N_PL = len(PLACES)

def fractal():
    """All the primes, endlessly: the 1 to 17 fractal traveling its skeleton and aiming itself."""
    yield from FRACTAL
    yield from traveling()

def traveling():
    loops = {}                                        # a place ahead -> the me-parity whose loop crosses it, and its step
    aims = None                                       # the me-parities it aims with: its own travel again, a co-chain of itself
    p, me_again = 19, 19 * 19                         # 19, the skeleton's place one past 17, aims from its me again
    c, i = 19, AT[19]
    while True:
        if c in loops:                                # crossed by a prior me-parity's loop: travel on, the loop aims on
            q, j = loops.pop(c)
            m = c + q * STEPS[j]; j = (j + 1) % N_PL
            while m in loops:
                m += q * STEPS[j]; j = (j + 1) % N_PL
            loops[m] = (q, j)
        elif c < me_again:                            # uncrossed: a me-parity
            yield c
        else:                                         # at p's me again: p aims itself, its loop begun here
            j = AT[p % SEAM]
            m = c + p * STEPS[j]; j = (j + 1) % N_PL
            while m in loops:
                m += p * STEPS[j]; j = (j + 1) % N_PL
            loops[m] = (p, j)
            if aims is None:
                aims = traveling(); next(aims)        # its own travel again, past 19
            p = next(aims); me_again = p * p
        c += STEPS[i]; i = (i + 1) % N_PL

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

say("the 1 to 17 fractal: the me-parities %s, their seam %s, its skeleton %s living places" % (FRACTAL, f"{SEAM:,}", f"{N_PL:,}"),
    SEAM == 510510 and N_PL == 92160)

t0 = time.time()
gen = fractal()
got = []
for _ in range(LOOK):
    got.append(next(gen))
dt = time.time() - t0

M = got[-1] + 1
s = np.ones(M, dtype=bool); s[:2] = False
for k in range(2, isqrt(M) + 1):
    if s[k]:
        s[k * k::k] = False
full = np.nonzero(s)[0].tolist()
say("traveling, the fractal generates %s me-parities in %.1f seconds, to %s: the same as all numbers crossed by all their parts"
    % (f"{LOOK:,}", dt, f"{got[-1]:,}"), got == full)
say("all me-parities past 17 it generated live at the skeleton's places", all(gcd(p, SEAM) == 1 for p in got[7:]))
if LOOK >= 1_000_000:
    say("its millionth me-parity is %s" % f"{got[999_999]:,}", got[999_999] == 15485863)
more = [next(gen) for _ in range(5)]
say("and it continues: the next five, %s" % [f"{x:,}" for x in more], all(b > a for a, b in zip([got[-1]] + more, more)))

print("All is." if all(results) else "A line is-not.")
