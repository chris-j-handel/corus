"""How each nine-spot diamond sits against the three ring sets.

For every diamond (a ring pair A, B crossing on one side) this returns:
  the angle between its forward diagonal (equal-radius corners) and the
  radial line from the third ring set's centre; the angle between its cross
  diagonal and the tangent of the third set's circles; its distance from the
  third centre; and the angle between its middle row and the tangent of ring
  set A at the diamond centre. Angles are in degrees, instrument returns only.
"""
import os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, '..', 'data')
k = np.load(os.path.join(DATA, 'circles.npy'))
C = {'top': np.array([220.7, 262.4]), 'left': np.array([171.6, 347.0]), 'right': np.array([270.3, 347.0])}
R = {}
for x, y, r in k:
    n = min(C, key=lambda n: np.hypot(*(C[n] - [x, y]))); R.setdefault(n, []).append(r)
for n in R: R[n] = sorted(R[n])
def inter(p0, r0, p1, r1):
    d = np.linalg.norm(p1 - p0); a = (r0*r0 - r1*r1 + d*d) / (2*d); h = np.sqrt(max(r0*r0 - a*a, 0))
    m = p0 + a*(p1 - p0)/d; perp = np.array([-(p1 - p0)[1], (p1 - p0)[0]])/d
    return m + h*perp, m - h*perp
def ang(u, v):
    c = abs(np.dot(u, v))/np.linalg.norm(u)/np.linalg.norm(v); return np.degrees(np.arccos(min(1, c)))
lines = ['| diamond | forward diagonal vs radial to third centre | cross diagonal vs tangent of third circles | distance to third centre | middle row vs tangent of own ring |', '|---|---|---|---|---|']
for A, B in [('left', 'right'), ('top', 'left'), ('top', 'right')]:
    third = [n for n in C if n not in (A, B)][0]
    for s in (0, 1):
        P = {(i, j): inter(C[A], R[A][i], C[B], R[B][j])[s] for i in range(3) for j in range(3)}
        c = P[(1, 1)]; fwd = P[(2, 2)] - P[(0, 0)]; crs = P[(0, 2)] - P[(2, 0)]
        rad3 = c - C[third]; tan3 = np.array([-rad3[1], rad3[0]]); radA = c - C[A]
        lines.append(f'| {A}-{B}, side {s} | {ang(fwd, rad3):.1f} | {ang(crs, tan3):.1f} | {np.linalg.norm(rad3):.1f} | {ang(P[(1, 2)] - P[(1, 0)], np.array([-radA[1], radA[0]])):.1f} |')
out = '\n'.join(lines)
print(out)
open(os.path.join(DATA, 'tangency.md'), 'w').write(out + '\n')
