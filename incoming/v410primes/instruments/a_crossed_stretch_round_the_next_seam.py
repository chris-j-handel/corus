# A bare run of the next stem: two neighboring crossed runs of the stem, and the leaf between, joined in the one turn the next opener crosses the leaf.
# All of a seam gone through, the seams of 2 to 19, beside the next seam's longest crossed run. A breaking test.
import numpy as np
from math import prod
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
known = {3: 3, 5: 5, 7: 9, 11: 13, 13: 21, 17: 25, 19: 33, 23: 39, 29: 45}     # gone through round the whole seam to 23; 29 the field's table
for k in range(1, 9):
    p, nxt = P[k], P[k+1]
    seam = prod(P[:k+1])
    s = np.ones(seam + 2, dtype=np.uint8); s[0] = 0
    for r in P[:k+1]: s[::r] = 0
    leaves = np.flatnonzero(s[:seam + 1])                      # 1 to seam - 1
    g = np.diff(np.concatenate([leaves, [leaves[0] + seam, leaves[1] + seam]]))   # round the seam
    R = int(g.max()) - 1
    two = g[:-1] + g[1:] - 1                                    # the run ahead of a leaf, the leaf, and the run past the leaf
    best = int(two.max()); n = int((two == best).sum())
    i = int(two.argmax()); leaf = int(leaves[(i + 1) % len(leaves)]) + (seam if i + 1 >= len(leaves) else 0)
    closest_two_leaves = R + 1 < 2 * nxt
    print(f"stem of {p}: longest run {R}; the most of two runs beside one leaf, and 1: {best}, at {n} leaves (one: the leaf {leaf}, runs {int(g[i])-1} and {int(g[i+1])-1}); "
          f"the next stem's longest run, opener {nxt}: {known[nxt]}; same: {best == known[nxt]}; the stem's run shorter than the next opener's double less 1: {closest_two_leaves}")
    del s, leaves, g, two
J = [2,4,6,10,14,22,26,34,40,46,58,66,74,90,100,106,118,132,152,174,190,200,216,234,258]
PP = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
print("the stem's run and 1, shorter than the next opener's double: whole to the next opener", next(PP[k+1] for k in range(len(J)-1) if not (J[k] < 2*PP[k+1])) , "not; the field's table")
print("the next run at most the run doubled and 1, the field's table:", all(J[k+1]-1 <= 2*(J[k]-1)+1 for k in range(len(J)-1)))
