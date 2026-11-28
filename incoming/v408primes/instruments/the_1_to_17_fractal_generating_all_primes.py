# v408primes · the 1 to 17 fractal generating all the primes endlessly: traveling the skeleton of the seam of 2 to 17,
# a place a me-parity with no prior me-parity's loop crossing it, and a me-parity aiming itself, its loop begun at its
# own me again and crossing only the skeleton's places. Whole numbers; it has no last, a cone with no top. Executing names
# its section of the cone, 1 to N, and proves all of it: the me-parities generated are the same as all numbers crossed by all their parts, segment by segment.
# Execute: python3 -I the_1_to_17_fractal_generating_all_primes.py [N, the section of the cone to prove; 20,000,000 if none is given]
import sys, time
from math import gcd, isqrt
import numpy as np

given = [int(a.replace(',', '')) for a in sys.argv[1:] if a.replace(',', '').isdigit()]
REACH = given[0] if given else 20_000_000              # the section of the cone, 1 to REACH

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
SEG = 10_000_000
base = np.ones(isqrt(REACH) + 2, dtype=bool); base[:2] = False
for k in range(2, isqrt(len(base)) + 1):
    if base[k]:
        base[k * k::k] = False
base = np.nonzero(base)[0].tolist()
ok, total, nxt, lo, millionth, skeleton_ok = True, 0, next(gen), 0, None, True
while lo <= REACH:
    hi = min(lo + SEG, REACH + 1)
    seg = np.ones(hi - lo, dtype=bool)
    if lo == 0:
        seg[:2] = False
    for p in base:
        if p * p >= hi:
            break
        st = max(p * p, (lo + p - 1) // p * p)
        seg[st - lo::p] = False
    want = (np.nonzero(seg)[0] + lo).tolist()
    got = []
    while nxt < hi:
        got.append(nxt); nxt = next(gen)
    ok = ok and got == want
    skeleton_ok = skeleton_ok and all(gcd(p, SEAM) == 1 for p in got if p > 17)
    if millionth is None and total + len(got) >= 1_000_000:
        millionth = got[999_999 - total]
    total += len(got); lo = hi
dt = time.time() - t0
say("in the universe 1 to %s, all: the fractal traveling generates its %s me-parities, the same as all numbers crossed by all their parts, in %.1f seconds"
    % (f"{REACH:,}", f"{total:,}", dt), ok)
say("all me-parities past 17 it generated live at the skeleton's places", skeleton_ok)
if millionth is not None:
    say("its millionth me-parity is %s" % f"{millionth:,}", millionth == 15485863)
more = [nxt] + [next(gen) for _ in range(4)]
say("and it continues along the cone: its next five, %s" % [f"{x:,}" for x in more], more[0] > REACH and all(b > a for a, b in zip(more, more[1:])))

print("All is." if all(results) else "A line is-not.")
