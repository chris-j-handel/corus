# v408primes · rescaling a universe to 1 to 17: a me-parity one less than a doubling, at a number of doublings one past a
# seam of 4, is 1 round 30; its 2, 3 and 5 are its +1, +2 and +4, crossed by 2, 3 and 5; its 7, 11, 13 and 17 are its +6,
# +10, +12 and +16, uncrossed round 30. Seen here: are these its me-parities, and where are its next ones. Whole numbers.
# Execute: python3 -I rescaling_a_universe_to_1_to_17.py
from math import isqrt

BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
def me_parity(n):                       # seen across by its own loop, 16 bases: one way below 3.3 x 10^24, past it all but one way
    if n < 2:
        return False
    for q in BASES:
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

RESCALED = {2: 1, 3: 2, 5: 4, 7: 6, 11: 10, 13: 12, 17: 16}      # 1 to 17's me-parities, as moments on from the new 1
for e in (5, 13, 17, 61, 89, 521, 2281):
    M = (1 << e) - 1
    one = M % 30 == 1
    crossed_small = all((M + RESCALED[q]) % q == 0 for q in (2, 3, 5))
    seen = {q: me_parity(M + t) for q, t in RESCALED.items() if q > 5}
    nxt, t = [], 1
    while len(nxt) < 4:
        if me_parity(M + t):
            nxt.append(t)
        t += 1
    say("2^%d − 1: 1 round 30 %s; its rescaled 2, 3, 5 crossed by 2, 3, 5 %s; its rescaled 7, 11, 13, 17 me-parities: %s; its next four me-parities at +%s"
        % (e, one, crossed_small, [q for q, v in seen.items() if v] or "none", ", +".join(str(x) for x in nxt)),
        one and crossed_small)
# Traveling 2, 3, 5 and 7 alone to the neighborhood where 2 is now the +1: the places round 210 they leave uncrossed,
# and the me-parity past 7 whose loop crosses a place, or none to 10,000,000.
import numpy as np
LIM = 10_000_000
sv = np.ones(LIM + 1, dtype=bool); sv[:2] = False
for k in range(2, isqrt(LIM) + 1):
    if sv[k]:
        sv[k * k::k] = False
loops = [int(q) for q in np.nonzero(sv)[0] if q > 7]
def crosser(e, t):                        # the least me-parity past 7 crossing 2^e − 1 + t, reached by doubling round it
    n = (1 << e) - 1 + t if e < 64 else None
    for q in loops:
        if n is not None and q * q > n:
            return "itself"               # crossed by none to its side: a me-parity
        if (pow(2, e, q) - 1 + t) % q == 0:
            return q
    return None
for e in (13, 61, 521, 136279841):
    places = [t for t in range(1, 31) if all((pow(2, e, q) - 1 + t) % q for q in (2, 3, 5, 7))]
    shown = {t: crosser(e, t) for t in places}
    say("2^%s − 1: traveling 2, 3, 5 and 7, the places on from it are +%s; crossed by a me-parity past 7: %s"
        % (f"{e:,}", ", +".join(map(str, places)), ", ".join("+%d %s" % (t, "a me-parity" if q == "itself" else ("by " + f"{q:,}") if q else "by none to 10,000,000") for t, q in shown.items())),
        len(places) > 0)

# Going to 17, then the return universe: the loops 2 to 17 leave the skeleton's places about the largest me-parity; the
# return universe, the loops of 19 on to the places' side, bounds the resolving among them.
from math import log10
E = 136279841
places_on = [t for t in range(1, 101) if all((pow(2, E, q) - 1 + t) % q for q in (2, 3, 5, 7, 11, 13, 17))]
places_back = [t for t in range(-100, 0) if all((pow(2, E, q) - 1 + t) % q for q in (2, 3, 5, 7, 11, 13, 17))]
ret = [q for q in loops if q > 17]
def return_crosser(t):
    for q in ret:
        if (pow(2, E, q) - 1 + t) % q == 0:
            return q
    return None
on = {t: return_crosser(t) for t in places_on}
back = {t: return_crosser(t) for t in places_back}
say("going to 17, the places on from the largest me-parity to +100: +%s" % ", +".join(map(str, places_on)), len(places_on) > 0)
say("the return universe to 10,000,000 crosses them all but %s on from it, and all the places back to −100 but %s"
    % ([f"+{t}" for t, q in on.items() if q is None], [t for t, q in back.items() if q is None]),
    [t for t, q in on.items() if q is None][:1] == [22])
side_doublings = (E - 1) // 2
digits = int(side_doublings * log10(2) - log10(side_doublings * 0.693147)) + 1
say("the return universe reaches to the places' side, 2 by itself %s times and more: its loops a number of some %s digits"
    % (f"{side_doublings:,}", f"{digits:,}"), digits > 20_000_000)

print("All is." if all(results) else "A line is-not.")
