# v408primes · cascading universes from the origin, transmissioned to the numbers. Universe 0 is 1 to 120, the return of
# the seventeen primes; a next universe's bound is its prior's bound by itself, and its loops are the prior universe's
# me-parities. A path of cascades from the origin reaches any number. A row goes on along the path by one step at all
# cascades. For twins the step is of the seam's other-thans alone: in the universe from B to B by B, the longest stretch of
# the seam of the loops to B with no twin place is shorter than the universe. Whole numbers.
# Execute: python3 -I cascading_universes_from_the_origin.py
from math import log, isqrt
import numpy as np

results = []
def say(s, ok):
    results.append(bool(ok)); print(("is     " if ok else "is-not ") + s)

# the path from the origin to a number: universe k's bound is 120 by itself 2 to the k times
def cascades(digits):                                   # a number of d digits, by its digits alone
    k, b = 0, log(120, 10)                              # universe 0's bound, its digits
    while b < digits: b *= 2; k += 1
    return k
say("the path from the origin: universe 0 to 120, then 14,400, then 207,360,000; 120 by itself eight times at universe 3", 120 ** 2 == 14400 and 14400 ** 2 == 207360000 and (120 ** 2) ** 2 ** 2 == 120 ** 8)
say("a number of 41,024,320 digits, the largest me-parity known now, is reached from the origin in %d cascades" % cascades(41024320), cascades(41024320) == 25)
say("a number of a thousand digits in %d cascades, of a million digits in %d" % (cascades(1000), cascades(10 ** 6)), cascades(1000) == 9 and cascades(10 ** 6) == 19)

# a universe from B to B by B: a number in it uncrossed by the loops to B is a me-parity, both sides of a seam uncrossed are twins
def twin_runs(ps):
    M = 1
    for r in ps: M *= r
    CH, last, start, longest, places = 20000000, None, None, 0, 0
    for lo in range(0, M, CH):
        n = np.arange(lo, min(lo + CH, M), dtype=np.int64); live = np.ones(len(n), bool)
        for r in ps:
            m = n % r; live &= (m != 0) & (m != r - 2)
        tp = n[live]
        if len(tp) == 0: continue
        if start is None: start = int(tp[0])
        g = np.diff(tp) if last is None else np.diff(np.r_[last, tp])
        if len(g): longest = max(longest, int(g.max()))
        places += len(tp); last = int(tp[-1])
    return M, places, max(longest, start + M - last)
def sieve(N):
    s = np.ones(N + 1, bool); s[:2] = False
    for p in range(2, isqrt(N) + 1):
        if s[p]: s[p * p::p] = False
    return s
PS = [2, 3, 5, 7, 11, 13, 17, 19, 23]
for B in (17, 19, 23):
    ps = [p for p in PS if p <= B]
    M, places, longest = twin_runs(ps)
    room = B * B - B - 3                                 # the twin places n of B + 1 to B by B less 3
    s = sieve(B * B); born = [n for n in range(B + 1, B * B - 2) if s[n] and s[n + 2]]
    say("the universe from %d to %d: round the seam %s of its loops, the twin places are %s and the longest stretch between them %d, shorter than the universe's %d: twins are born in it by other-thans alone, %d of them"
        % (B, B * B, f"{M:,}", f"{places:,}", longest, room, len(born)), longest <= room and len(born) > 0)

# passing the place: a twin is a between a, a seam of 6, its bi-folding a by a less 1 uncrossed by the loops
for ps in ([2, 3, 5, 7, 11, 13, 17], [2, 3, 5, 7, 11, 13, 17, 19]):
    M = 1
    for r in ps: M *= r
    n = np.arange(M, dtype=np.int64); live = np.ones(M, bool)
    for r in ps:
        m = n % r; live &= (m != 0) & (m != r - 2)
    a = np.arange(0, M, 6, dtype=np.int64)
    uncrossed = a[np.gcd(a * a - 1, M) == 1]
    gaps = np.diff(np.r_[uncrossed, uncrossed[0] + M])
    say("round the seam %s: the twin places are the betweens, seams of 6, whose bi-folding a by a less 1 is uncrossed; the longest stretch of betweens all crossed, two places a loop, is %d betweens"
        % (f"{M:,}", int(gaps.max()) // 6 - 1), np.array_equal(np.sort((uncrossed - 1) % M), np.nonzero(live)[0]))
print("All is." if all(results) else "A line is-not.")
