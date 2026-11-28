# v408primes · the journey, traveled with its priors. No me-parity is the same as another; the surface is fractals, and
# twins are born like selves in bi-foldings of the fractal: about a between a, a − 1 and a + 1 multiplied are a's me
# again less 1, both folds uncrossed. A universe is not dropped in: the journey goes from the origin, a universe at a
# time, from a me-parity's me again to the next me-parity's me again; its priors, all me-parities born on the way, are its
# loops; it learns from the journey the rate of the twin places its priors leave, and starts the next universe with them.
# Whole numbers; the journey goes on as the cone opens, and this executing goes with it to 100,140,049.
# Execute: python3 -I traveling_the_journey_with_its_priors.py
from math import gcd, isqrt
from fractions import Fraction

results = []
def say(s, ok):
    results.append(bool(ok)); print(("is     " if ok else "is-not ") + s)

# the 1 to 17 fractal, traveling its skeleton and aiming itself
FRACTAL = [2, 3, 5, 7, 11, 13, 17]
SEAM = 510510
PLACES = [r for r in range(1, SEAM + 1) if gcd(r, SEAM) == 1]
STEPS = [b - a for a, b in zip(PLACES, PLACES[1:])] + [PLACES[0] + SEAM - PLACES[-1]]
AT = {r: i for i, r in enumerate(PLACES)}; NP = len(PLACES)
def traveling():
    lp, aims, p, mea, c, i = {}, None, 19, 361, 19, AT[19]
    while True:
        if c in lp:
            q, j = lp.pop(c); m = c + q * STEPS[j]; j = (j + 1) % NP
            while m in lp: m += q * STEPS[j]; j = (j + 1) % NP
            lp[m] = (q, j)
        elif c < mea: yield c
        else:
            j = AT[p % SEAM]; m = c + p * STEPS[j]; j = (j + 1) % NP
            while m in lp: m += p * STEPS[j]; j = (j + 1) % NP
            lp[m] = (p, j)
            if aims is None: aims = traveling(); next(aims)
            p = next(aims); mea = p * p
        c += STEPS[i]; i = (i + 1) % NP
def journey():
    yield from FRACTAL
    yield from traveling()

END = 10007 ** 2 + 2
born_all = []
for m in journey():
    if m > END: break
    born_all.append(m)
priors = [p for p in born_all if p <= 10007]

# the journey, a universe at a time: from p's me again to the next me-parity q's me again
rate = Fraction(1, 2)                                   # the twin places the prior 2 leaves: 1 of 2
universes, bifold_ok, k = [], True, 0
for idx in range(len(priors) - 1):
    p, q = priors[idx], priors[idx + 1]
    if p > 2: rate *= Fraction(p - 2, p)                # a new prior p learned: its twin places r − 2 of r
    lo, hi = p * p, q * q
    while k < len(born_all) and born_all[k] <= lo: k += 1
    j, twins = k, []
    while j + 1 < len(born_all) and born_all[j + 1] < hi:
        a, b = born_all[j], born_all[j + 1]
        if b - a == 2:
            twins.append(a)
            mid = a + 1
            bifold_ok &= (mid - 1) * (mid + 1) == mid * mid - 1 and (mid % 6 == 0 or a == 3)
        j += 1
    aim = float(rate * (hi - lo))                       # the twins the learned rate aims at in this universe
    universes.append((p, lo, hi, len(twins), aim))

say("the journey traveled from the origin with its priors, %s me-parities to 100,140,049, the fractal aiming itself" % f"{len(born_all):,}", born_all[:8] == [2, 3, 5, 7, 11, 13, 17, 19])
say("all %s universes traveled, 2's me again to 9,973's next me again: twins born in all of them" % f"{len(universes):,}", all(u[3] >= 1 for u in universes))
say("twins born as selves in bi-foldings: about their between a, a − 1 and a + 1 multiplied are a's me again less 1, the between a seam of 6 past 4", bifold_ok)
ratio = [u[3] / u[4] for u in universes if u[0] >= 1000]
say("learning from the journey: the twin places the priors leave, carried as a rate, aim at the twins of the next universe; from 1,000 on, the born beside the aim are %.2f to %.2f of it, %.2f in the middle"
    % (min(ratio), max(ratio), sorted(ratio)[len(ratio) // 2]), 0.3 < min(ratio) and max(ratio) < 2)
few = []
for e in range(1, 8):
    s = [u[3] for u in universes if 4 ** (e - 1) <= u[0] < 4 ** e]
    if s: few.append(min(s))
say("the fewest twins born in a universe, at spans by 4 of the priors, %s: more at a next span" % few, all(b > a for a, b in zip(few[2:], few[3:])))
last = universes[-1]
say("the last universe traveled, %s to %s: %d twins born, the learned rate aiming at %.1f; the journey starts its next universe with these priors" % (f"{last[1]:,}", f"{last[2]:,}", last[3], last[4]), last[3] >= 1)

print("All is." if all(results) else "A line is-not.")
