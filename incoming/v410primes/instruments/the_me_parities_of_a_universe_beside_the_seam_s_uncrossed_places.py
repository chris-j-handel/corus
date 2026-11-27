# The births of a universe from the openers ahead: the seam's uncrossed places, the seam's share, and the births.
# A named universe, 1 to N. A breaking test and a showing of patterns: proving nothing past N.
import sys, itertools
from fractions import Fraction
from collections import Counter
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**8

# 1. The copy rule, seam to next seam: the uncrossed places round a seam.
print("== the copy rule, seam to next seam")
seam, unc = 1, [0]            # round the seam 1, the one place 0 is uncrossed
for r in (2, 3, 5, 7, 11, 13):
    nxt = seam * r
    copies = {u: [u + k * seam for k in range(r)] for u in unc}
    crossed_one = all(sum(1 for c in cs if c % r == 0) == 1 for cs in copies.values())
    new = sorted(c for cs in copies.values() for c in cs if c % r)
    pairs_prior = [u for u in unc if ((u + 2) % seam) in set(unc)] if seam > 2 else []
    s_new = set(new)
    pairs_new = [u for u in new if ((u + 2) % nxt) in s_new]
    line = f"  opener {r}: seam {seam} to {nxt}; uncrossed {len(unc)} to {len(new)}; one copy crossed of all places: {crossed_one}"
    if seam > 2:
        ok2 = all(sum(1 for k in range(r) if (u + k*seam) % r == 0 or (u + 2 + k*seam) % r == 0) == 2 for u in pairs_prior)
        line += f"; pairs 2 apart {len(pairs_prior)} to {len(pairs_new)}; two copies crossed of all pairs: {ok2}"
    else:
        line += f"; pairs 2 apart round {nxt}: {len(pairs_new)}"
    print(line)
    seam, unc = nxt, new

# 2. The sieve of the named universe.
s = bytearray([1]) * (N + 3); s[0] = s[1] = 0; s[N+1] = s[N+2] = 0
i = 2
while i * i <= N:
    if s[i]: s[i*i:N+1:i] = bytearray(len(range(i*i, N + 1, i)))
    i += 1
side = int(N ** 0.5)
openers = [p for p in range(2, side + 2) if s[p]]

# 3. Universe by universe: the seam's share and the births.
print("== universe by universe, 1 to", N)
share1 = Fraction(1); share2 = Fraction(1, 2)      # the uncrossed share of places; of pairs 2 apart
rows = []
for k in range(len(openers) - 1):
    p, q = openers[k], openers[k + 1]
    f1 = float(share1 * (1 - Fraction(1, p))) if k < 40 else None
    share1 = share1 * (p - 1) / p if k < 40 else share1
    if k >= 40:
        # floats past the 40th opener
        if k == 40: s1f, s2f = float(share1), float(share2)
        s1f *= (p - 1) / p
    if p > 2:
        if k < 40: share2 = share2 * (p - 2) / p
        else: s2f *= (p - 2) / p
    a, b = p * p, q * q - 1
    if b > N: break
    L = b - a + 1
    births = s.count(1, a, b + 1)
    two = sum(1 for n in range(a, b - 1) if s[n] and s[n + 2])
    S1 = float(share1) if k < 40 else s1f
    S2 = float(share2) if k < 40 else s2f
    rows.append((p, a, b, L, births, two, L * S1, (L - 2) * S2))
print("  universes whole:", len(rows))
print("  opener | universe | length | the seam's share of births | births | the seam's share of pairs 2 apart | births 2 apart")
for r in rows[:9]:
    print(f"  {r[0]} | {r[1]} to {r[2]} | {r[3]} | {r[6]:.2f} | {r[4]} | {r[7]:.2f} | {r[5]}")
def band(lo, hi):
    rs = [r for r in rows if lo <= r[0] <= hi]
    B = sum(r[4] for r in rs); S = sum(r[6] for r in rs); T = sum(r[5] for r in rs); S2 = sum(r[7] for r in rs)
    return len(rs), B, S, B / S, T, S2, T / S2
print("  bands of openers: universes | births | the seam's share | births over share | births 2 apart | share | over share")
for lo, hi in ((2, 7), (11, 97), (101, 997), (1009, 4999), (5003, 9967)):
    n, B, S, r1, T, S2, r2 = band(lo, hi)
    print(f"  {lo} to {hi}: {n} | {B} | {S:.1f} | {r1:.4f} | {T} | {S2:.1f} | {r2:.4f}")
print("  universes with births more than the seam's share:", [r[0] for r in rows if r[4] > r[6]][:12], "...", sum(1 for r in rows if r[4] > r[6]), "of", len(rows))
print("  universes with births 2 apart more than the seam's share:", sum(1 for r in rows if r[5] > r[7]), "of", len(rows))
print("  the universe as a part of the seam, the universes of 7, 11, 13, 17: 72 of 210, 48 of 2310, 120 of 30030, 72 of 510510")

# 4. Spans from a number's me again to the next number's me again: a birth in all spans (rows 29 and 38).
no_birth = 0; least = None
for n in range(2, side):
    c = s.count(1, n * n + 1, (n + 1) * (n + 1))
    if c == 0: no_birth += 1
    if n >= 2 and (least is None or c < least[0]): least = (c, n)
print("== spans from a number's me again to the next number's me again, numbers 2 to", side - 1, ": spans with no birth:", no_birth, "; least births in a span:", least[0], "at the number", least[1])

# 5. The most-met number of selves from a birth to the next birth, a universe at a time (row 40).
champ = Counter(); last_other = None
for r in rows:
    a, b = r[1], r[2]
    g = Counter(); prev = None
    for n in itertools.compress(range(a, b + 1), s[a:b + 1]):
        if prev is not None: g[n - prev] += 1
        prev = n
    if g:
        top = max(g.values()); tops = sorted(d for d, c in g.items() if c == top)
        champ[tuple(tops)] += 1
        if tops != [6]: last_other = (r[0], tops)
print("== the most-met number of selves from a birth to the next birth, a universe at a time:", dict(sorted(champ.items(), key=lambda kv: -kv[1])[:6]))
print("   the last universe with a most-met other than 6 alone:", last_other)
