# The stem's long bare run, its form and its turn. All of a seam gone through at the openers 5 to 23;
# the podal bare run laid by its between at the openers 5 to 97. A breaking test of sentences; proving nothing past its numbers.
import numpy as np
from math import prod
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
def is_mp(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def least(n, upto):
    for r in P:
        if r > upto: return None
        if n % r == 0: return r

print("== 1. all of a seam gone through: the longest crossed runs, their betweens")
for k in range(2, 9):
    p, prior = P[k], P[k-1]
    seam = prod(P[:k+1]); back = prod(P[:k-1])
    s = np.ones(seam + 2, dtype=np.uint8); s[0] = 0
    for r in P[:k+1]: s[::r] = 0
    pos = np.flatnonzero(s); g = np.diff(pos); R = int(g.max()) - 1
    runs = [(int(pos[i]) + 1, int(pos[i+1]) - 1) for i in np.flatnonzero(g == g.max())]
    line = []
    for a, b in runs:
        mid2 = a + b                       # twice the middle
        if mid2 % 2 == 0:
            N = mid2 // 2
            form = (N % back == 0) and {least(N-1, p), least(N+1, p)} == {prior, p}
            line.append(f"{a} to {b}, between {N}, a crossing of the seam {back}: {N % back == 0}, the -1 and the +1 crossed by {least(N-1,p)} and {least(N+1,p)}, podal form: {form}")
        else:
            line.append(f"{a} to {b}, no between: the middle is two numbers")
    print(f"opener {p}: longest crossed run {R}; the prior opener's double less 1: {2*prior-1}; runs: {len(runs)}")
    for l in line[:4]: print("    ", l)
    if p == 23:
        a, b = runs[0]
        print("     the run of 23, a number with its least crossing me-parity:", " ".join(f"{n - a + 1}:{least(n, p)}" for n in range(a, b + 1)))
    del s, pos, g

print("== 2. the podal bare run by its between, the openers 5 to 97: the between, the run, the numbers at the run's two ends")
def crt(res_mod):
    x, m = 0, 1
    for r, md in res_mod:
        t = ((r - x) * pow(m, -1, md)) % md
        x, m = x + m * t, m * md
    return x % m, m
bad = 0
for k in range(2, 25):
    p, prior = P[k], P[k-1]
    back = prod(P[:k-1]); seam = prod(P[:k+1])
    N1, _ = crt([(0, back), (1, prior), (p - 1, p)])      # the -1 crossed by the prior opener, the +1 by the opener
    N2, _ = crt([(0, back), (prior - 1, prior), (1, p)])   # the other way: the fold
    for N in (N1, N2):
        if N == 0: N = seam
        ok = all(least(N + i, p) is not None for i in range(-(prior - 1), prior))
        if not ok: bad += 1
    fold = (N1 + N2) % seam == 0
    N = min(N1, N2)
    # the run's true ends on the stem: on to the uncrossed places both ways
    a = N - (prior - 1)
    while least(a - 1, p) is not None: a -= 1
    b = N + (prior - 1)
    while least(b + 1, p) is not None: b += 1
    q = P[k+1]
    if k <= 9:
        print(f"opener {p}: between {N} = {N // back} by the seam {back}; the two betweens fold about the seam's middle: {fold}; run {a} to {b}, {b - a + 1} numbers; "
              f"the uncrossed places at its ends {a-1} and {b+1}, me-parities: {is_mp(a-1)} and {is_mp(b+1)}; the opener's universe {p*p} to {q*q-1}; the run past the universe: {a > q*q - 1}")
print("podal runs not all crossed, the openers 5 to 97:", bad)
print("the seam two openers back longer than the universe's end, from the opener:", next(P[k] for k in range(2, 25) if all(prod(P[:j-1]) > P[j+1]**2 for j in range(k, 25))))
