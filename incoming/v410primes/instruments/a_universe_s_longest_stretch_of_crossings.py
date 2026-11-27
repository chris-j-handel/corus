# The opening's own longest bare run, a universe at a time: the longest run of crossings from a birth of the universe to the next birth,
# beside the opener, in the named universe 1 to N. Beside the stem's longest crossed run over the opener.
import sys, numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**8
s = np.ones(N + 1, dtype=np.uint8); s[:2] = 0
for i in range(2, int(N**.5) + 1):
    if s[i]: s[i*i::i] = 0
mp = np.flatnonzero(s)
side = int(N**.5)
op = mp[mp <= side + 1]
rows = []
for k in range(len(op) - 1):
    p, q = int(op[k]), int(op[k+1])
    a, b = p*p, q*q - 1
    if b > N: break
    i0 = np.searchsorted(mp, a); i1 = np.searchsorted(mp, b, side='right')   # births of the universe: mp[i0:i1]
    if i1 >= len(mp): break
    births = mp[i0:i1 + 1]                                                   # on to the next birth past the universe
    run = int(np.diff(births).max()) - 1 if len(births) > 1 else 0
    j = int(np.diff(births).argmax()); at = int(births[j])
    rows.append((p, run, run / p, at))
print("universes:", len(rows))
for r in rows[:8]: print(f"  opener {r[0]}: the longest run of crossings from a birth to the next birth: {r[1]}, past the birth {r[3]}; over the opener: {r[2]:.2f}")
for lo, hi in ((2, 7), (11, 97), (101, 997), (1009, 4999), (5003, 9967)):
    rs = [r for r in rows if lo <= r[0] <= hi]
    m = max(rs, key=lambda r: r[2])
    print(f"  openers {lo} to {hi}: the most of run over opener: {m[2]:.3f}, at the opener {m[0]}, run {m[1]} past the birth {m[3]}; the middle of the band: {sorted(r[2] for r in rs)[len(rs)//2]:.3f}")
print("  universes with the run as long as the opener's double or longer:", [r[0] for r in rows if r[1] >= 2 * r[0]])
print("  universes with the run as long as the opener or longer:", [r[0] for r in rows if r[1] >= r[0]])
