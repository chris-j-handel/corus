"""Runs at the third function of Exhibit ONE v372, _17_social_abundancing: the rings, the order within a momentary,
the corners of a surface around a hole at the joins as declared and at 9 arriving at both along neighbours.
Usage: python3 society_runs.py <folder holding Exhibit_ONE_Natural_Resolver_v372.md>"""
import re, random, itertools, sys, os
FOLDER = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()      # the folder holding Exhibit_ONE_Natural_Resolver_v372.md
code = re.search(r'```python\n(.*?)```', open(os.path.join(FOLDER, 'Exhibit_ONE_Natural_Resolver_v372.md'), encoding='utf-8').read(), re.S).group(1)
ns = {}
exec(code, ns)
C, R, A = ns['_1_self_coupling'], ns['_9_other_releasing'], ns['_17_social_abundancing']
CON, JOI = ns['CONNECTORS'], ns['JOINS']
K = 'k'

def gather(arr):
    return [x for c in (2, 14, 17) for x in arr.get(c, [])]

def surfacings(car, arr, S):
    return {s: dict(C(car.get(s, []), gather(arr.get(s, {})))[0]).get(K) for s in S}

# ---- R58: one momentary at the third function equals the two functions called by hand at each self
def R58():
    S = {'A': {'right': ['B'], 'backward': ['C']}, 'B': {'left': ['A'], 'right': ['C']}, 'C': {'left': ['B'], 'forward': ['A'], 'backward': ['A']}}
    car = {'A': [(K, 1, -1, 1)], 'B': [(K, -1, 1, 0), ('j', 1, 1, 2)], 'C': []}
    arr = {'A': {2: [(K, -1)]}, 'C': {17: [(K, 1), ('j', -1)]}}
    nxt_car, nxt_arr = A(car, arr, {}, S)
    exp_car, exp_arr = {}, {s: {2: [], 14: [], 17: []} for s in S}
    for s in S:
        ten, eleven = C(car.get(s, []), gather(arr.get(s, {})))
        exp_car[s] = eleven
        six = [(k, t) for k, c, t, a in car.get(s, [])]
        nine = R(ten, {k: k for k, v in ten})
        for rel, signs in ((6, six), (10, ten), (9, nine)):
            for nb in S[s].get(CON[rel][1], []):
                exp_arr[nb][JOI[rel]] += signs
    fns = [n.name for n in __import__('ast').parse(code).body if isinstance(n, __import__('ast').FunctionDef)]
    return nxt_car == exp_car and nxt_arr == exp_arr and fns == ['_1_self_coupling', '_9_other_releasing', '_17_social_abundancing']

# ---- R59: the rings at the third function
def ring_at(n, steps, facing):
    S = {i: {facing: [(i + 1) % n]} for i in range(n)}
    car, arr = {}, {0: {2: [(K, 1)]}}
    states, surf = [], []
    for _ in range(steps):
        surf.append(tuple(surfacings(car, arr, S)[i] for i in range(n)))
        car, arr = A(car, arr, {}, S)
        states.append((tuple(tuple(map(tuple, car[i])) for i in range(n)), tuple(tuple((c, tuple(arr[i][c])) for c in (2, 14, 17)) for i in range(n))))
    return surf, states

def recur_at(n, facing):
    surf, st = ring_at(n, 12 * n + 20, facing); first = {}
    for t, s in enumerate(st):
        if s in first: return first[s] + 1, t - first[s]
        first[s] = t

def R59():
    ok = True
    surf, _ = ring_at(1, 8, 'backward'); ok &= [x[0] for x in surf] == [1, 0, -1, 0, 1, 0, -1, 0]
    for n in list(range(1, 12)) + [17, 59]:
        ok &= recur_at(n, 'backward') == (n, 2 if n % 2 == 0 else 4 * n)
        ok &= recur_at(n, 'right') == (n, 2 if n % 2 == 0 else 4 * n)
    for n in range(1, 12):
        ok &= recur_at(n, 'left') == (2 * n, 4 * n)
    # even and odd surfacings, as R45, at the along ring
    for n in list(range(1, 12)) + [17, 59]:
        surf, _ = ring_at(n, 10 * n + 8, 'backward'); per = surf[n:]
        if n % 2 == 0:
            ok &= all(per[t][i] == -per[t + 1][i] for t in range(len(per) - 1) for i in range(n))
            ok &= all(per[t][i] == -per[t][(i + 1) % n] for t in range(len(per)) for i in range(n))
        else:
            ok &= all(per[t + 2 * n][i] == -per[t][i] for t in range(len(per) - 2 * n) for i in range(n))
            ok &= all(per[t + 4 * n][i] == per[t][i] for t in range(len(per) - 4 * n) for i in range(n))
    # the rest returns at no coupling, rings 1..11 over 5000 momentaries
    for n in range(1, 12):
        _, st = ring_at(n, 5000, 'backward')
        rest = (tuple(() for _ in range(n)), tuple(tuple((c, ()) for c in (2, 14, 17)) for _ in range(n)))
        ok &= not any(s == rest for s in st)
    return ok

# ---- R60: the order within a momentary carries nothing
def R60():
    random.seed(1)
    S = {i: {'backward': [(i + 1) % 7], 'right': [(i + 2) % 7], 'left': [(i - 2) % 7]} for i in range(7)}
    car, arr = {}, {0: {2: [(K, 1)]}, 3: {2: [(K, -1)]}}
    ok = True; checked = 0
    for step in range(30):
        base = A(car, arr, {}, S)
        for _ in range(5):
            order = list(S); random.shuffle(order)
            S2 = {s: S[s] for s in order}
            arr2 = {s: {c: random.sample(v, len(v)) for c, v in a.items()} for s, a in arr.items()}
            alt = A(car, arr2, {}, S2)
            ok &= alt[0] == base[0] and all(sorted(alt[1][s][c]) == sorted(base[1][s][c]) for s in S for c in (2, 14, 17))
            checked += 1
        car, arr = base
    return ok and checked == 150

# ---- the hole: three by three with the centre missing
def grid(both_ways=False):
    S = {}
    for r in range(3):
        for c in range(3):
            if (r, c) == (1, 1): continue
            nb = {}
            if c + 1 < 3 and (r, c + 1) != (1, 1): nb['right'] = [(r, c + 1)]
            if c - 1 >= 0 and (r, c - 1) != (1, 1): nb['left'] = [(r, c - 1)]
            along = []
            if r - 1 >= 0 and (r - 1, c) != (1, 1): along.append((r - 1, c))
            if both_ways and r + 1 < 3 and (r + 1, c) != (1, 1): along.append((r + 1, c))
            if along: nb['backward'] = along
            if r + 1 < 3 and (r + 1, c) != (1, 1): nb['forward'] = [(r + 1, c)]
            S[(r, c)] = nb
    return S

def trace(S, seed, steps):
    car, arr = {}, {seed: {2: [(K, 1)]}}
    rows = []
    for t in range(steps):
        rows.append((surfacings(car, arr, S), {s: {c: list(v) for c, v in a.items()} for s, a in arr.items()}))
        car, arr = A(car, arr, {}, S)
    return rows

def R61():
    S = grid(False); rows = trace(S, (1, 0), 40)
    ok = rows[1][1][(0, 0)][17] == [(K, 1)]                      # along arriving at the corner's 17 at momentary 1
    ok &= rows[1][0][(0, 0)] == 1 and rows[2][1][(0, 1)][14] == [(K, 1)]   # continuing into the release at 10, arriving at 14
    ok &= rows[2][0][(0, 1)] == 1 and rows[3][1][(0, 2)][14] == [(K, 1)]   # the top-right corner receives across at 14 at momentary 3
    ok &= rows[3][0][(0, 2)] == 1
    ok &= all(rows[t][0][(1, 2)] is None and not any(rows[t][1].get((1, 2), {}).get(c) for c in (2, 14, 17)) for t in range(40))
    ok &= all(rows[t][0][(2, c)] is None for t in range(40) for c in range(3))   # the bottom row receives nothing
    return ok

def R62():
    S = grid(True); rows = trace(S, (1, 0), 40)
    ok = rows[1][1][(0, 0)][17] == [(K, 1)] and rows[1][1][(2, 0)][17] == [(K, 1)]
    ok &= rows[1][0][(0, 0)] == 1 and rows[1][0][(2, 0)] == 1
    ok &= rows[3][0][(0, 2)] == 1 and rows[3][0][(2, 2)] == 1
    ok &= rows[4][1][(1, 2)][17] == [(K, 1), (K, 1)] and all(not rows[t][1].get((1, 2), {}).get(c) for t in range(4) for c in (2, 14, 17))
    ok &= rows[4][0][(1, 2)] == 1
    car, arr = {}, {(1, 0): {2: [(K, 1)]}}
    for t in range(4): car, arr = A(car, arr, {}, S)
    ok &= car[(1, 2)] == []
    car, arr = A(car, arr, {}, S)
    ok &= car[(1, 2)] == [(K, 1, -1, 0)]
    return ok

if __name__ == '__main__':
    for f in (R58, R59, R60, R61, R62):
        print(f.__name__, f())
    for both in (False, True):
        print('both ways along' if both else 'as declared')
        for t, (surf, arr) in enumerate(trace(grid(both), (1, 0), 8)):
            print('  t=%d' % t, ' | '.join(''.join({1: '+', -1: '-', 0: '0', None: '.'}[surf.get((r, c))] if (r, c) != (1, 1) else '#' for c in range(3)) for r in range(3)),
                  '  (1,2) arriving:', arr.get((1, 2)))
