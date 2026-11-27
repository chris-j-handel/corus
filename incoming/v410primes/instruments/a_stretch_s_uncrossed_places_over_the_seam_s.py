# The uncrossed places of the stem, a stretch at a time, over the seam's share: at the opener's me again and at other turns of the stem.
# Stretches of W numbers opening at the opener multiplied by itself u times. A showing of a pattern; proving nothing.
import numpy as np
def mps(n):
    s = np.ones(n + 1, dtype=np.uint8); s[:2] = 0
    for i in range(2, int(n**.5) + 1):
        if s[i]: s[i*i::i] = 0
    return [int(x) for x in np.flatnonzero(s)]
ALL = mps(2000)
def over_share(p, x, W):
    ps = [r for r in ALL if r <= p]
    a = np.ones(W, dtype=np.uint8)
    share = 1.0
    for r in ps:
        a[(-x) % r::r] = 0
        share *= (r - 1) / r
    return a.sum() / (W * share)
for p in (97, 199, 499):
    out = []
    for u in (1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 3.0, 3.5, 4.0, 5.0):
        x = int(round(p ** u)); W = max(200000, min(4_000_000, x // 4))
        if u == 2.0: x = p * p
        out.append(f"{u}: {over_share(p, x, W):.3f}")
    print(f"opener {p}: uncrossed places over the seam's share, a stretch opening at the opener by itself that many times ->", "  ".join(out))
