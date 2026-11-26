# v408primes · odd and even along to any number, across: a number is odd with an odd number of prime parts multiplied,
# even with an even number. Counted along to the number given, segment by segment, by whole numbers.
# Execute: python3 -I odd_and_even_along_to_any_number.py [a number to 2,000,000,000]
# With no number given, it counts along to 906,150,300, past where even goes ahead.
import sys
from math import isqrt
import numpy as np

given = [int(a.replace(',', '')) for a in sys.argv[1:] if a.replace(',', '').isdigit()]
N = given[0] if given else 906150300
if not 2 <= N <= 2000000000:
    print("past this instrument's reach: %s" % N); sys.exit(0)

root = isqrt(N) + 1
small = np.ones(root + 1, dtype=bool); small[:2] = False
for i in range(2, isqrt(root) + 1):
    if small[i]:
        small[i * i::i] = False
primes = np.nonzero(small)[0].tolist()

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

S = 1 << 23
carry = 0                       # odd less even along, before the segment: the lead's other-than, -L
even_ahead_at = None            # the first number past 2 where even is ahead
alike_after_587 = []            # numbers from 587 where odd and even are alike
widest, widest_at = 0, 0
race = 0                        # me-parities aiming next less those aiming prior, along: round 4, 3 less 1
prior_ahead_at, changes, last_prior_ahead = None, 0, None
lo = 1
while lo <= N:
    hi = min(lo + S, N + 1)
    rem = np.arange(lo, hi, dtype=np.int64)
    odd = np.zeros(hi - lo, dtype=np.uint8)
    for p in primes:
        if p * p >= hi and p >= hi:
            break
        pk = p
        while pk < hi:
            start = (-lo) % pk
            odd[start::pk] ^= 1
            rem[start::pk] //= p
            pk *= p
    odd ^= (rem > 1).astype(np.uint8)
    step = np.where(odd == 1, 1, -1).astype(np.int64)     # +1 for odd across, −1 for even
    if lo == 1:
        step[0] = -1                                     # 1 has no parts: even
    along = np.cumsum(step) + carry                      # odd less even along to n
    n0 = lo
    # even ahead: odd less even below 0, from 3 on
    idx = np.nonzero(along < 0)[0]
    idx = idx[(idx + n0) >= 3]
    if even_ahead_at is None and len(idx):
        even_ahead_at = int(idx[0] + n0)
    z = np.nonzero(along == 0)[0]
    z = z[(z + n0) >= 587]
    if len(z) and len(alike_after_587) < 5:
        alike_after_587 += [int(x + n0) for x in z[:5 - len(alike_after_587)]]
    m = int(np.argmax(np.abs(along)))
    if abs(int(along[m])) > abs(widest):
        widest, widest_at = int(along[m]), m + n0
    carry = int(along[-1])
    crossed = np.zeros(hi - lo, dtype=bool)
    if lo == 1:
        crossed[0] = True
    for p in primes:
        if p * p >= hi:
            break
        start = max(p * p, lo + (-lo) % p)
        crossed[start - lo::p] = True
    me = np.nonzero(~crossed)[0] + lo
    me = me[me > 2]
    if len(me):
        steps = np.where(me % 4 == 3, 1, -1).astype(np.int64)
        runs = np.cumsum(steps) + race
        ahead = runs < 0
        before = race < 0
        if prior_ahead_at is None and ahead.any():
            prior_ahead_at = int(me[np.argmax(ahead)])
        flips = np.count_nonzero(ahead[1:] != ahead[:-1]) + (1 if ahead[0] != before else 0)
        changes += int(flips)
        if ahead.any():
            last_prior_ahead = int(me[np.nonzero(ahead)[0][-1]])
        race = int(runs[-1])
    lo = hi

say("along to %s, odd less even is %s at the end" % (f"{N:,}", f"{carry:,}"), True)
if N >= 906150257:
    say("even goes ahead past 2 at %s: odd is ahead or alike from 3 to the number before" % (f"{even_ahead_at:,}" if even_ahead_at else "none"),
        even_ahead_at == 906150257)
say("from 587, odd and even alike along at: %s" % (alike_after_587 or "none"), True)
say("along to it, odd and even are apart by %s at the most, at %s, whose side is %s" % (f"{abs(widest):,}", f"{widest_at:,}", f"{isqrt(widest_at):,}"), True)
say("round 4, the me-parities aiming prior go ahead of those aiming next at %s, and one aim and then the other goes ahead %d times along to %s; the last number with those aiming prior ahead, %s; at the end, those aiming next ahead by %s"
    % (f"{prior_ahead_at:,}" if prior_ahead_at else "none", changes, f"{N:,}", f"{last_prior_ahead:,}" if last_prior_ahead else "none", f"{race:,}"),
    N < 26861 or prior_ahead_at == 26861)
print("All is." if all(results) else "A line is-not.")
