"""tangent_double_angle_v365.py · tan(2x) = 2 tan(x) / (1 - tan(x)^2) at the nine-spot diamonds (notes EEE01 to EEE04)

Needs numpy. Reads ../data/circles.npy, the ring circles tangency.py reads. Run:  python3 tangent_double_angle_v365.py

1. At each nine-spot diamond (three circles of one set crossing three of another), the angle psi between the
   radial directions from the two centres at the centre spot, and the diamond's diagonal ratio
   t = |forward diagonal| / |cross diagonal|. For small cells t = tan(psi / 2) exactly, so tan(psi) = 2t / (1 - t^2).
2. Where the parity of a diamond changes: t = 1, psi = 90 degrees, each ring's radius tangent to the other ring,
   which is the circle having the two centres as its diameter. Along a ring of radius r about one centre, with the
   other centre at distance d, this happens at the angles +-arccos(r / d) from the other centre, and nowhere if r > d.
3. The double-angle map t -> 2t / (1 - t^2): its fixed point is 0, and its only pair swapped with the sign changing
   and the size kept is t = +-sqrt(3), the 60 and 120 degree angles.
4. Doubling the angle reads the binary digits of x / pi: the sign of tan at the k-th doubling is + for a 0 and - for a 1.
   A sign that never changes is every digit alike, which is only the fixed point 0, the same as pi.
5. The journey's eight spots (journey.py) lie at multiples of 45 degrees; tan(2 theta) there is 0 at the four axis
   spots and has its pole at the four diagonal spots, and the journey's step of three round eight alternates them.
6. The identity's residence, checked (notes EEE05, GGG05 to GGG07): the journey's step F(P, Q) = (-Q, P) is the quarter
   turn of the signs of (cos, sin); the journey's agree/oppose is the sign of tan, and it tips at every quarter turn;
   the sine of the doubled angle carries that sign; cos and sin pass through zero by turns; the angle with
   tan 2theta = 2b / (a - c) removes the coupling b from a symmetric pair (Jacobi, Mohr, principal axes);
   and t = n/m gives the Pythagorean triple (m^2 - n^2, 2mn, m^2 + n^2).
"""
import math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, '..', 'data')
C = {'top': np.array([220.7, 262.4]), 'left': np.array([171.6, 347.0]), 'right': np.array([270.3, 347.0])}


def rings():
    k = np.load(os.path.join(DATA, 'circles.npy')); R = {}
    for x, y, r in k:
        n = min(C, key=lambda n: np.hypot(*(C[n] - [x, y]))); R.setdefault(n, []).append(r)
    return {n: sorted(R[n]) for n in R}


def inter(p0, r0, p1, r1):
    d = np.linalg.norm(p1 - p0); a = (r0 * r0 - r1 * r1 + d * d) / (2 * d); h = math.sqrt(max(r0 * r0 - a * a, 0))
    m = p0 + a * (p1 - p0) / d; perp = np.array([-(p1 - p0)[1], (p1 - p0)[0]]) / d
    return m + h * perp, m - h * perp


def part_one(R):
    print('1 · the double-angle formula at the six nine-spot diamonds')
    for A, B in [('left', 'right'), ('top', 'left'), ('top', 'right')]:
        for s in (0, 1):
            P = {(i, j): inter(C[A], R[A][i], C[B], R[B][j])[s] for i in range(3) for j in range(3)}
            c = P[(1, 1)]; uA = (c - C[A]) / np.linalg.norm(c - C[A]); uB = (c - C[B]) / np.linalg.norm(c - C[B])
            psi = math.degrees(math.acos(float(np.clip(uA @ uB, -1, 1))))
            t = np.linalg.norm(P[(2, 2)] - P[(0, 0)]) / np.linalg.norm(P[(0, 2)] - P[(2, 0)])
            print(f'   {A}-{B} side {s}: psi {psi:5.1f}°, t {t:.3f}, tan psi {math.tan(math.radians(psi)):.3f}, '
                  f'2t/(1-t²) {2 * t / (1 - t * t):.3f}, the angle t gives {math.degrees(2 * math.atan(t)):5.1f}°')


def part_two(R):
    print('\n2 · where a diamond\'s parity changes along each ring (psi = 90°, t = 1)')
    d = np.mean([np.linalg.norm(C[a] - C[b]) for a, b in [('left', 'right'), ('top', 'left'), ('top', 'right')]])
    for r in R['left']:
        if r < d:
            a = math.degrees(math.acos(r / d))
            print(f'   ring {r:5.1f} (centre spacing {d:.1f}): changes at ±{a:.1f}° from each other centre, '
                  f'so at {[round(v, 1) for v in sorted([-a, a, 60 - a, 60 + a])]}° from one of them, both others counted')
        else:
            print(f'   ring {r:5.1f} (centre spacing {d:.1f}): no change on this ring; at r = d it touches at the other centre')


def part_three():
    print('\n3 · the map t -> 2t/(1 - t²)')
    t = math.sqrt(3); seq = [round(t, 6)]
    for _ in range(5):
        t = 2 * t / (1 - t * t); seq.append(round(t, 6))
    print('   from sqrt(3):', seq)
    print('   fixed points: t(1 - t²) = 2t gives t = 0 only; swapped pair: 2t/(1 - t²) = -t gives t² = 3')


def part_four():
    print('\n4 · doubling reads the binary digits of x/pi')
    for frac in (0.3, 1 / 3, 0.0):
        x = frac * math.pi; y = frac; digits = []
        for _ in range(12):
            digits.append(int(2 * y)); y = (2 * y) % 1
        signs = ''.join('0' if abs(math.tan((2 ** k) * x)) < 1e-9 else ('+' if math.tan((2 ** k) * x) > 0 else '-') for k in range(12))
        print(f'   x/pi = {frac:.4f}: signs {signs}  binary digits {"".join(map(str, digits))}')


def part_five():
    print('\n5 · tan(2 theta) at the journey\'s eight spots, in arrival order 1 to 8')
    ring = [-90, -45, 0, 45, 90, 135, 180, 225]      # B, LR, R, UR, T, UL, L, LL, as journey.py's RING
    out = []
    for n in range(1, 9):
        th = ring[(3 * (n - 1)) % 8]
        out.append('pole' if th % 90 else '0')
    print('   ', ', '.join(out), '· 0 and 9 at the centre, where no direction is')


def part_six():
    print('\n6 · the identity\'s residence, checked')
    sgn = lambda v: 1 if v > 0 else -1
    ok_step = ok_rel = ok_sin2 = True
    for deg in (45, 135, 225, 315):
        th = math.radians(deg); P, Q = sgn(math.cos(th)), sgn(math.sin(th))
        rot = (sgn(math.cos(th + math.pi / 2)), sgn(math.sin(th + math.pi / 2)))
        ok_step &= rot == (-Q, P)
        ok_rel &= (P == Q) == (math.tan(th) > 0)
        ok_sin2 &= sgn(math.sin(2 * th)) == sgn(math.tan(th))
    print(f'   F(P, Q) = (-Q, P) is the quarter turn of the signs of (cos, sin): {ok_step}')
    print(f'   agree/oppose is the sign of tan, tipping at every quarter turn: {ok_rel}')
    print(f'   the sine of the doubled angle carries that sign: {ok_sin2}')
    order, prev = [], (sgn(math.cos(1e-6)), sgn(math.sin(1e-6)))
    for k in range(1, 3601):
        th = math.radians(k / 10 + 1e-6); cur = (sgn(math.cos(th)), sgn(math.sin(th)))
        if cur[0] != prev[0]: order.append('cos')
        if cur[1] != prev[1]: order.append('sin')
        prev = cur
    print('   which of cos and sin passes through zero, once round from just past 0°:', ', '.join(order))
    for a_, b_, c_ in ((5.0, 2.0, 1.0), (3.0, 1.5, 3.0)):
        th = 0.5 * math.atan2(2 * b_, a_ - c_); co, si = math.cos(th), math.sin(th)
        off = (c_ - a_) * si * co + b_ * (co * co - si * si)
        print(f'   pair a={a_}, c={c_}, coupling b={b_}: turn {math.degrees(th):.1f}° with tan 2θ = 2b/(a − c); coupling left {off:.1e}')
    for n_, m_ in ((1, 2), (1, 3), (2, 3)):
        tt = n_ / m_
        print(f'   t = {n_}/{m_}: 2t/(1 − t²) = {2 * tt / (1 - tt * tt):.4f} = {2 * m_ * n_}/{m_ * m_ - n_ * n_}, '
              f'triple ({m_ * m_ - n_ * n_}, {2 * m_ * n_}, {m_ * m_ + n_ * n_})')


if __name__ == '__main__':
    R = rings()
    part_one(R); part_two(R); part_three(); part_four(); part_five(); part_six()
