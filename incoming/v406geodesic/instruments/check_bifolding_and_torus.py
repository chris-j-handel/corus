"""Checks for drafts 2 and 3: each claim executed, all or none at all.

Names 1..16 are n - 1 in four binary digits b3 b2 b1 b0; 17 is 0000 again.
Candidate placement on a torus (axis z, ring radius R, tube radius r):
  high pair b3 b2 -> band around the small opening (tube), in order
      00 outer-top, 01 inner-top, 10 inner-bottom, 11 outer-bottom
      (phi in [0,90], [90,180], [180,270], [270,360])
  low pair b1 b0  -> quarter around the large opening (ring), theta in [90*Q, 90*Q + 90]
"""
import numpy as np

ok = []
def check(label, cond):
    ok.append(bool(cond)); print(("is     " if cond else "IS NOT ") + label)

# ---- the sphere: trirectangular triangle and its bi-folding
def octant_area(n=2000):
    # area of {x,y,z >= 0} on the unit sphere: integral of cos(lat) over lon 0..90, lat 0..90
    lat = (np.arange(n) + 0.5) / n * np.pi / 2
    return np.sum(np.cos(lat)) * (np.pi / 2 / n) * (np.pi / 2)
check("the three-right-angle triangle covers pi/2 of the unit sphere, 1/8 of 4 pi (90 deg of excess)",
      abs(octant_area() - np.pi / 2) < 1e-6)

fold_z = np.diag([1, 1, -1]); fold_y = np.diag([1, -1, 1])   # fold across the equator edge, then across the meridian edge AB
two = fold_y @ fold_z
check("one fold is a mirror (determinant -1)", np.linalg.det(fold_z) < 0)
check("two folds on orthogonal edges are a half-turn about the axis through B (determinant +1, x fixed)",
      np.allclose(two, np.diag([1, -1, -1])))
A, B, C = np.eye(3)[2], np.eye(3)[0], np.eye(3)[1]
check("the bi-folding fixes B and carries A to the south pole and C to -C, the triangle +++ onto +--",
      np.allclose(two @ B, B) and np.allclose(two @ A, -A) and np.allclose(two @ C, -C))

# ---- the torus
R, r = 1.0, 0.42
BANDS = [(0, 90), (90, 180), (180, 270), (270, 360)]
def patch(n):
    k = n - 1
    j, q = k >> 2, k & 3
    return q, j
def patch_curvature(n, m=20000):
    q, j = patch(n)
    a, b = np.radians(BANDS[j])
    phi = a + (np.arange(m) + 0.5) / m * (b - a)
    # K dA = cos(phi) dtheta dphi on a torus of revolution
    return np.sum(np.cos(phi)) * (b - a) / m * (np.pi / 2)
curv = {n: patch_curvature(n) for n in range(1, 17)}
outside = [n for n in curv if patch(n)[1] in (0, 3)]
inside = [n for n in curv if patch(n)[1] in (1, 2)]
check("each of the 16 patches carries total curvature +pi/2 or -pi/2, whatever R and r",
      all(abs(abs(c) - np.pi / 2) < 1e-6 for c in curv.values()))
check("the outside surface is names 1-4 and 13-16, the inside 5-12, the middle eight",
      sorted(outside) == [1, 2, 3, 4, 13, 14, 15, 16] and sorted(inside) == list(range(5, 13)))
check("outside +4 pi (+720 deg, the sphere's eight triangles), inside -4 pi: a torus at nought",
      abs(sum(curv[n] for n in outside) - 4 * np.pi) < 1e-5 and abs(sum(curv[n] for n in inside) + 4 * np.pi) < 1e-5)

def surf(theta, phi):
    return np.array([(R + r * np.cos(phi)) * np.cos(theta), (R + r * np.cos(phi)) * np.sin(theta), r * np.sin(phi)])
def normal(theta, phi):
    return np.array([np.cos(phi) * np.cos(theta), np.cos(phi) * np.sin(theta), np.sin(phi)])
def patch_samples(n, m=7):
    q, j = patch(n)
    th = np.radians(90 * q + (np.arange(m) + 0.5) / m * 90)
    ph = np.radians(BANDS[j][0] + (np.arange(m) + 0.5) / m * 90)
    return [(t, p) for t in th for p in ph]
def which_patch(theta, phi):
    q = int((np.degrees(theta) % 360) // 90); j = int((np.degrees(phi) % 360) // 90)
    return (j << 2 | q) + 1

check("the normals of name 1's patch are the triangle +++ of draft 1, one to one",
      all(np.all(normal(t, p) > 0) for t, p in patch_samples(1)))

half_turn = np.diag([1, -1, -1])
def image_name(n, M):
    names = set()
    for t, p in patch_samples(n):
        x = M @ surf(t, p)
        th = np.arctan2(x[1], x[0]); ph = np.arctan2(x[2], np.hypot(x[0], x[1]) - R)
        names.add(which_patch(th, ph))
    return names
check("17 less is the half-turn about the x axis through the empty 0: each name n onto 17 - n",
      all(image_name(n, half_turn) == {17 - n} for n in range(1, 17)))
check("the half-turn about the x axis carries name 1's patch onto 16's, as the bi-folding carries +++ onto +--",
      image_name(1, half_turn) == {16} and all(np.allclose(np.sign(normal(t, p)), [1, -1, -1]) for t, p in
                                               [(-tt, -pp) for tt, pp in patch_samples(1)]))
check("8 apart is half way round the small opening, through the tube's core: same quarter, bands opposite",
      all(patch(n)[0] == patch(n + 8)[0] and (patch(n)[1] ^ 2) == patch(n + 8)[1] for n in range(1, 9)))
check("4 apart within a half is outer with inner at one height, one side of the core",
      all(patch(n)[0] == patch(n + 4)[0] and (patch(n)[1] ^ 1) == patch(n + 4)[1] for n in (1, 2, 3, 4, 9, 10, 11, 12)))
check("17 is 0000 again: the winding through 1..16 comes back to name 1's patch",
      patch(1) == ((17 - 1) % 16 & 3, ((17 - 1) % 16) >> 2))
check("1 to 8, a self's span, lie on the upper half; 9 to 16, a same-existing-society's, on the lower",
      all(patch(n)[1] in (0, 1) for n in range(1, 9)) and all(patch(n)[1] in (2, 3) for n in range(9, 17)))

print("\nall:", "is" if all(ok) else "IS NOT", f"({sum(ok)} of {len(ok)})")
