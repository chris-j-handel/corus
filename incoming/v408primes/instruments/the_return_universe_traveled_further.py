# v408primes · the return universe traveled further about the largest me-parity seen to now: the loops of 19 on, segment
# by segment, all at once round their own primes by doubling 28 times, crossing the six places left at 10,000,000.
# Whole numbers. It names its universe of loops, 19 to the number given, and proves all of it, a place crossed or not.
# Execute: python3 -I the_return_universe_traveled_further.py [how far, to 10^12]
import sys, time
from math import isqrt
import numpy as np

given = [int(a.replace(',', '')) for a in sys.argv[1:] if a.replace(',', '').isdigit()]
FAR = min(given[0], 10 ** 12) if given else 10 ** 9
E = 136279841
PLACES = [22, 70, 100, -48, -72, -90]
SEG = 10 ** 8

base = np.ones(isqrt(FAR) + 2, dtype=bool); base[:2] = False
for k in range(2, isqrt(len(base)) + 1):
    if base[k]:
        base[k * k::k] = False
small = np.nonzero(base)[0]

def mulmod(a, b, q):                         # a by b round q, whole, for q below 2^40: b taken in two parts
    bh, bl = b >> np.uint64(16), b & np.uint64(0xFFFF)
    return ((((a * bh) % q) << np.uint64(16)) + a * bl) % q
def doubling_round(q):                       # 2 by itself E times, round all q at once
    r = np.ones(len(q), dtype=np.uint64); b = np.full(len(q), 2, dtype=np.uint64) % q
    e = E
    while e:
        if e & 1:
            r = mulmod(r, b, q)
        b = mulmod(b, b, q)
        e >>= 1
    return r

t0 = time.time()
crossed = {t: None for t in PLACES}
loops = 0
lo = 19
while lo <= FAR:
    hi = min(lo + SEG, FAR + 1)
    seg = np.ones(hi - lo, dtype=bool)
    for p in small:
        p = int(p)
        if p * p >= hi:
            break
        st = max(p * p, lo + (-lo) % p)
        seg[st - lo::p] = False
    q = (np.nonzero(seg)[0] + lo).astype(np.uint64)
    loops += len(q)
    m = (doubling_round(q) + q - 1) % q        # the largest me-parity round q
    for t in PLACES:
        if crossed[t] is None:
            shift = (np.uint64(t) % q) if t > 0 else (q - np.uint64(-t) % q) % q
            hit = np.nonzero((m + shift) % q == 0)[0]
            if len(hit):
                crossed[t] = int(q[hit[0]])
    lo = hi
dt = time.time() - t0

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)
say("the return universe traveled from 19 to %s: %s loops in %.0f seconds" % (f"{FAR:,}", f"{loops:,}", dt), loops > 0)
say("the six places left at 10,000,000: %s" % ", ".join(("%+d crossed by %s" % (t, f"{q:,}")) if q else ("%+d uncrossed" % t) for t, q in crossed.items()), True)
print("All is." if all(results) else "A line is-not.")
