"""one_ten_v365.py · the one ten: five at two sides, the couplings among five, and the five stitches (Living Improving Value, JJJ02, JJJ03)

Standard library only. Run:  python3 one_ten_v365.py

1. Five is the one count whose couplings are twice itself: C(n, 2) = 2n only at n = 5, so the ten couplings among five
   and the five at two sides are one ten, and no other count joins the two.
2. The pentagon is the one ring whose complement is a ring: among five, the five sides and the five diagonals are both
   rings, the along and the across.
3. R(3, 3) = 6: every two-colouring of the fifteen couplings among six holds a one-colour three, and among five the
   colourings holding none are exactly the twelve whose each colour is a pentagon, the ring and the star.
4. The five stitches. In the regular pentagon each side is parallel to exactly one diagonal, the one sharing no corner
   with it, the diagonal phi times the side; the pair leaves one corner out, each corner once. Each coupling is a
   transposition of the five, an involution holding the other three in place; a stitch's two transpositions commute,
   and together they are the pentagon's mirror through the corner left out.
5. The pentagon's own symmetries are ten, five turns and five mirrors. The five mirrors are the five stitches, and two
   mirrors make the turn by twice the angle between them, so the ten are carried by the stitches.
6. Every ten consecutive numbers is five opposite-parity pairs about the between: at every start a, the pairs
   (a + j, a + 9 - j) sum to 2a + 9, which is odd. The journey's (k, 9 - k) is the start at nought, and the start's
   parity is the origin.
"""
import itertools, math

PHI = (1 + 5 ** 0.5) / 2


def check(name, ok):
    print(f'   {"holds" if ok else "FAILS"} · {name}')
    return ok


def cycle_edges(n):
    return {frozenset((i, (i + 1) % n)) for i in range(n)}


def is_cycle(n, edges):
    deg = {v: sum(v in e for e in edges) for v in range(n)}
    if any(d != 2 for d in deg.values()): return False
    seen, v, prev = [0], 0, None
    while True:
        nxt = [w for e in edges if v in e for w in e if w != v and w != prev][0]
        if nxt == 0: break
        seen.append(nxt); prev, v = v, nxt
    return len(seen) == n


def mono_triangle(n, colour):
    return any(colour[frozenset((a, b))] == colour[frozenset((b, c))] == colour[frozenset((a, c))]
               for a, b, c in itertools.combinations(range(n), 3))


if __name__ == '__main__':
    results = []
    print('1. THE COUPLINGS AMONG FIVE ARE FIVE AT TWO SIDES')
    results.append(check('C(n, 2) = 2n at n = 5 and at no other n from 1 to 100,000',
                         [n for n in range(1, 100001) if n * (n - 1) // 2 == 2 * n] == [5]))
    print('2. THE ONE RING WHOSE COMPLEMENT IS A RING')
    full = lambda n: {frozenset(e) for e in itertools.combinations(range(n), 2)}
    results.append(check('the complement of the n-ring is a ring at n = 5 and at no other n from 3 to 40',
                         [n for n in range(3, 41) if is_cycle(n, full(n) - cycle_edges(n))] == [5]))
    print('3. THE ONE SOCIETY OF FIVE WITH NO FIXED THREE')
    E6 = sorted(full(6), key=sorted)
    results.append(check('every one of the 32,768 two-colourings of the couplings among six holds a one-colour three',
                         all(mono_triangle(6, dict(zip(E6, c))) for c in itertools.product((0, 1), repeat=15))))
    E5 = sorted(full(5), key=sorted); good = []
    for c in itertools.product((0, 1), repeat=10):
        col = dict(zip(E5, c))
        if not mono_triangle(5, col):
            good.append(col)
    results.append(check(f'among five, {len(good)} colourings hold no one-colour three, and in each both colours are pentagons',
                         len(good) == 12 and all(is_cycle(5, {e for e in E5 if col[e] == k}) for col in good for k in (0, 1))))
    print('4. THE FIVE STITCHES')
    P = [(math.cos(math.radians(90 + 72 * i)), math.sin(math.radians(90 + 72 * i))) for i in range(5)]
    vec = lambda e: (P[max(e)][0] - P[min(e)][0], P[max(e)][1] - P[min(e)][1])
    length = lambda e: math.hypot(*vec(e))
    parallel = lambda e, f: abs(vec(e)[0] * vec(f)[1] - vec(e)[1] * vec(f)[0]) < 1e-12
    sides = sorted(cycle_edges(5), key=sorted); diags = sorted(full(5) - cycle_edges(5), key=sorted)
    stitches = []
    for s in sides:
        par = [d for d in diags if parallel(s, d)]
        stitches.append((s, par))
    results.append(check('each side is parallel to exactly one diagonal, the one sharing no corner with it',
                         all(len(p) == 1 and not (s & p[0]) for s, p in stitches)))
    results.append(check('each diagonal is phi times its side', all(abs(length(p[0]) / length(s) - PHI) < 1e-12 for s, p in stitches)))
    out = [(set(range(5)) - s - p[0]).pop() for s, p in stitches]
    results.append(check(f'each stitch leaves one corner out, each corner once: {sorted(out)}', sorted(out) == [0, 1, 2, 3, 4]))
    perm = lambda e: tuple(sorted(e)[1] if v == sorted(e)[0] else sorted(e)[0] if v == sorted(e)[1] else v for v in range(5))
    comp = lambda a, b: tuple(a[b[v]] for v in range(5))
    results.append(check('the ten couplings are the ten transpositions of five, each an involution holding three in place',
                         all(comp(perm(e), perm(e)) == tuple(range(5)) and sum(perm(e)[v] == v for v in range(5)) == 3 for e in E5)))
    mirror = lambda d: tuple((2 * d - v) % 5 for v in range(5))
    results.append(check('a stitch\'s two transpositions commute, and together are the mirror through the corner left out',
                         all(comp(perm(s), perm(p[0])) == comp(perm(p[0]), perm(s)) == mirror(d) for (s, p), d in zip(stitches, out))))
    print('5. THE PENTAGON\'S TEN SYMMETRIES')
    group = {tuple(range(5))}
    while True:
        new = group | {comp(g, mirror(d)) for g in group for d in range(5)}
        if new == group: break
        group = new
    turns = [g for g in group if all((g[v] - v) % 5 == (g[0] - 0) % 5 for v in range(5))]
    results.append(check(f'the five stitch mirrors generate {len(group)} symmetries: {len(turns)} turns and {len(group) - len(turns)} mirrors',
                         len(group) == 10 and len(turns) == 5))
    results.append(check('the mirrors through corners d1 and d2 make the turn by 2(d1 - d2) steps of 72 degrees, twice the angle between them',
                         all(comp(mirror(a), mirror(b)) == tuple((v + 2 * (a - b)) % 5 for v in range(5)) for a in range(5) for b in range(5))))
    print('6. EVERY TEN IS FIVE OPPOSITE-PARITY PAIRS ABOUT THE BETWEEN')
    results.append(check('at every start from -1,000 to 1,000, the pairs (a + j, a + 9 - j) are opposite parity, five of them',
                         all(all((a + j) % 2 != (a + 9 - j) % 2 for j in range(5)) for a in range(-1000, 1001))))
    results.append(check('stepping the start by one exchanges which member of every pair is odd, and by two returns it',
                         all([(a + 1 + j) % 2 for j in range(5)] == [1 - (a + j) % 2 for j in range(5)]
                             and [(a + 2 + j) % 2 for j in range(5)] == [(a + j) % 2 for j in range(5)] for a in range(-1000, 1001))))
    print(f'\n{sum(results)} of {len(results)} lines hold')
