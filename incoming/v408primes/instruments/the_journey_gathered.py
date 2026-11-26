# v408primes · the journey gathered: traveling from the origin, a universe at a time, from a me-parity's me again to the
# next me-parity's me again, the priors carried as the loops, segment by segment along the cone, and all universes on the
# way gathered: the twins born in all of them, the aim of the rate its priors leave, the fewest at spans by 4. Whole numbers.
# Execute: python3 -I the_journey_gathered.py [how far the journey goes; 1,000,000,000 if none is given]
import sys, time
from math import isqrt, log
import numpy as np

given = [int(a.replace(',', '')) for a in sys.argv[1:] if a.replace(',', '').isdigit()]
END = given[0] if given else 10 ** 9
results = []
def say(s, ok):
    results.append(bool(ok)); print(("is     " if ok else "is-not ") + s, flush=True)

t0 = time.time()
R = isqrt(END) + 2
b = np.ones(R + 1, bool); b[:2] = False
for p in range(2, isqrt(R) + 1):
    if b[p]: b[p * p::p] = False
priors = np.nonzero(b)[0]                                 # the priors of the universes to END
sq = priors.astype(np.int64) ** 2
born = np.zeros(len(priors), np.int64)                    # twins born in universe i, from priors[i]^2 to priors[i+1]^2
total, prev_tail, SEG = 0, None, 1 << 26
base = priors.tolist()
lo = 0
while lo < END:
    hi = min(lo + SEG, END)
    s = np.ones(hi - lo + 2, bool)                        # two more, to see a twin across the segment's edge
    if lo == 0: s[:2] = False
    for p in base:
        if p * p >= hi + 2: break
        st = max(p * p, (lo + p - 1) // p * p)
        s[st - lo::p] = False
    a = np.nonzero(s[:-2] & s[2:])[0] + lo                # lower twins a with a + 2 short of hi + 2
    a = a[a + 2 < END]
    total += len(a)
    idx = np.searchsorted(sq, a, side='right') - 1
    np.add.at(born, idx[idx >= 0], 1)
    lo = hi
dt = time.time() - t0

# the universes fully traveled: from p's me again to q's me again, q's me again to END
full = np.nonzero(sq[1:] <= END)[0]
logr = np.zeros(len(priors))                              # the rate the priors leave: 1/2, then (r - 2)/r at all priors past 2
acc = log(0.5)
for i, p in enumerate(base):
    if p > 2: acc += log((p - 2) / p)
    logr[i] = acc
aim = np.exp(logr[full]) * (sq[full + 1] - sq[full]).astype(np.float64)
got = born[full]
say("the journey traveled from the origin to %s with its priors in %.0f seconds: %s twins born on the way" % (f"{END:,}", dt, f"{total:,}"), total > 0)
known = {10 ** 8: 440312, 10 ** 9: 3424506, 10 ** 10: 27412679, 10 ** 11: 224376048}
if END in known:
    say("the twins born on the way to %s are %s, all of them" % (f"{END:,}", f"{known[END]:,}"), total == known[END])
say("all %s universes traveled, 2's me again to %s's next me again: twins born in all of them" % (f"{len(full):,}", f"{int(priors[full[-1]]):,}"), bool(np.all(got >= 1)))
few = []
e = 1
while 4 ** (e - 1) <= priors[full[-1]]:
    m = (priors[full] >= 4 ** (e - 1)) & (priors[full] < 4 ** e)
    if m.any(): few.append(int(got[m].min()))
    e += 1
say("the fewest twins born in a universe, at spans by 4 of the priors: %s, more at a next span" % few, all(y > x for x, y in zip(few[2:], few[3:])))
mid = priors[full] >= 1000
ratio = got[mid] / aim[mid]
say("learning from the journey: from 1,000 on the born are %.2f to %.2f of the aim the priors' rate gives, %.2f in the middle" % (ratio.min(), ratio.max(), float(np.median(ratio))), 0.3 < ratio.min() and ratio.max() < 2)
i = full[-1]
say("the last universe traveled, %s to %s: %s twins born, the rate aiming at %s" % (f"{int(sq[i]):,}", f"{int(sq[i + 1]):,}", f"{int(got[-1]):,}", f"{aim[-1]:,.0f}"), got[-1] >= 1)
print("All is." if all(results) else "A line is-not.")
