"""Run checks for Exhibit THIRTY Parts ONE and TWO, against Exhibit ONE v371's resolver
(the first python block of /home/claude/work/Exhibit_ONE_Natural_Resolver_v371.md)."""
import ast, re, json, sys
from itertools import product, permutations, combinations

SRC_MD = '/home/claude/work/Exhibit_ONE_Natural_Resolver_v371.md'
code = re.search(r'```python\n(.*?)```', open(SRC_MD).read(), re.S).group(1)
ns = {}
exec(code, ns)
C = ns['_1_self_coupling']; R = ns['_9_other_releasing']
K = 'k'
S = (1, -1)

def call(carry, offer):
    s, c = C(list(carry), list(offer))
    return dict(s).get(K), (c[0][1:] if c else None), c

# ---------------------------------------------------------------- PART ONE (arithmetic)
def F20():
    self5 = list(range(1, 6)); other5 = list(range(2, 7))
    pairs = list(zip(self5, other5))
    return (len(self5) + len(other5) == 10 and len(set(self5) | set(other5)) == 6
            and pairs == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
            and all((a + b) % 2 == 1 for a, b in pairs)
            and ['co' if n % 2 else 'bi' for n in self5] == ['co', 'bi', 'co', 'bi', 'co']
            and ['co' if n % 2 else 'bi' for n in other5] == ['bi', 'co', 'bi', 'co', 'bi'])

def F21():
    # one side's momentaries alone: odd momentaries 1-2, 3-4, ... complete at 2, 4, ... where no momentary opens
    opens = {1, 3, 5, 7}; completes = {2, 4, 6, 8}
    return all(c not in opens for c in completes)

def next_rules():
    J = list(product(S, S))
    out = []
    for vals in product(S, repeat=4):
        f = dict(zip(J, vals))
        m = {(p, n): (n, f[(p, n)]) for p, n in J}
        out.append((f, m))
    return J, out

def cycles_of(m, states):
    seen = set(); cyc = []
    for s in states:
        if s in seen: continue
        path = []; x = s
        while x not in path and x not in seen:
            path.append(x); x = m[x]
        if x in path: cyc.append(len(path) - path.index(x))
        seen |= set(path)
    return sorted(cyc)

def F27():
    J, rules = next_rules()
    bij = [(f, m) for f, m in rules if len(set(m.values())) == 4]
    nonbij = [(f, m) for f, m in rules if len(set(m.values())) < 4]
    if len(bij) != 4 or len(nonbij) != 12: return False
    if not all(len(set(m.values())) < 4 for f, m in nonbij): return False  # at least two joint states going to one
    cls = {'now': 0, 'one': 0, 'both': 0}
    for f, m in rules:
        dep = [f[(1, n)] != f[(-1, n)] for n in S]
        cls['now' if not any(dep) else 'both' if all(dep) else 'one'] += 1
    if cls != {'now': 4, 'one': 8, 'both': 4}: return False
    named = {'prior': lambda p, n: p, 'minus_prior': lambda p, n: -p,
             'parity': lambda p, n: p * n, 'minus_parity': lambda p, n: -p * n}
    want = {'prior': [1, 1, 2], 'minus_prior': [4], 'parity': [1, 3], 'minus_parity': [1, 3]}
    for name, g in named.items():
        m = {(p, n): (n, g(p, n)) for p, n in J}
        if cycles_of(m, J) != want[name]: return False
    return True

def F31():
    up = lambda p: 8 * (p - 1) + 1
    return [up(p) for p in (1, 2, 3)] == [1, 9, 17] and up(9) == 65

def F32():
    ok = True
    for c, t in product(S, S):
        seq = [c, t, -c, -t, c, t, -c, -t, c]           # positions 1..9
        pairs = [(seq[i], seq[i + 1]) for i in range(8)]
        cnt = {j: pairs.count(j) for j in product(S, S)}
        step = all(pairs[i + 1] == (pairs[i][1], -pairs[i][0]) for i in range(7))
        ok &= all(v == 2 for v in cnt.values()) and step
    return ok

def F35():
    return all((-1) ** k * s == (s if k % 2 == 0 else -s) for k in range(64) for s in S)

def F37():
    J = list(product((0, 1), (0, 1)))
    good = []
    for vals in product((0, 1), repeat=4):
        f = dict(zip(J, vals))
        if all(f[(a, b)] != f[(1 - a, b)] and f[(a, b)] != f[(a, 1 - b)] for a, b in J):
            good.append(vals)
    xor = tuple(a ^ b for a, b in J); xnor = tuple(1 - (a ^ b) for a, b in J)
    return sorted(good) == sorted([xor, xnor])

def F43():
    conds = []
    for possible in (False, True):
        if not possible: conds.append(('not possible',)); continue
        for existing in (False, True):
            if not existing: conds.append(('possible', 'not existing')); continue
            for carrying in (False, True):
                conds.append(('existing', 'carrying' if carrying else 'not carrying'))
    return len(conds) == 4

def one_change_maps(n):
    St = list(product(S, repeat=n))
    flip = lambda s, j: tuple(-v if k == j else v for k, v in enumerate(s))
    for pick in product(range(n), repeat=len(St)):
        yield {St[i]: flip(St[i], pick[i]) for i in range(len(St))}, St

def single_round(m, St):
    s = St[0]; seen = [s]
    for _ in range(len(St)): s = m[s]; seen.append(s)
    return len(set(seen[:len(St)])) == len(St) and seen[-1] == St[0]

def _levels_walk(L, n=16, rule=None):
    def level(k):
        d = 0
        while d < L - 1 and k % n == n - 1:
            k //= n; d += 1
        return d
    rule = rule or level
    v = (0,) * L; seen = {v}; N = n ** L
    for k in range(N):
        d = rule(k); v = tuple((x + (1 if i == d else 0)) % n for i, x in enumerate(v))
        if k < N - 1:
            if v in seen: return False
            seen.add(v)
    return v == (0,) * L

def F97():
    from itertools import permutations
    steps = []
    for perm in permutations(range(2)):
        for sg in product(S, S):
            steps.append(lambda v, perm=perm, sg=sg: (sg[0] * v[perm[0]], sg[1] * v[perm[1]]))
    St = list(product(S, S))
    tab = lambda f: tuple(f(v) for v in St)
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0]); I = lambda v: v
    det = lambda f: (lambda a, b: a[0] * b[1] - a[1] * b[0])(f((1, 0)), f((0, 1)))
    inv = [f for f in steps if det(f) == -1]
    ok = len(steps) == 8 and len(inv) == 4
    ok &= all(tab(lambda v, f=f: f(f(v))) == tab(I) for f in inv)
    ok &= all(tab(lambda v, f=f: f(G(f(v)))) == tab(Fo) for f in inv)
    two = {tab(lambda v, a=a, b=b: a(b(v))) for a in inv for b in inv if tab(a) != tab(b)}
    ok &= two == {tab(G), tab(Fo), tab(lambda v: (-v[0], -v[1]))}
    three = {tab(lambda v, a=a, b=b, c=c: a(b(c(v)))) for a in inv for b in inv for c in inv}
    ok &= three <= {tab(f) for f in inv}
    return ok

def F96():
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0])
    ok = all(G(G(G(v))) == Fo(v) for v in product(S, S))
    from collections import Counter
    k = Counter()
    for st in sorted(REACH):
        if not st: continue
        for off in OFFERS:
            _, _, cc = call([(K,) + st], off)
            if not cc: k['complete'] += 1; continue
            a, b = st[:2], tuple(cc[0][1:3])
            k['same' if a == b else 'right' if b == G(a) else 'other' if b == Fo(a) else 'half' if b == (-a[0], -a[1]) else 'x'] += 1
    return ok and dict(k) == {'half': 72, 'same': 14, 'right': 9, 'other': 9, 'complete': 4}

def F105():
    from itertools import permutations
    def pst(c):
        r = [(1, 1)]
        while len(r) < 4: r.append((r[-1][1], -r[-1][0]))
        return r[c % 4]
    def lev(k, L):
        d = 0
        while d < L - 1 and k % 4 == 3: k //= 4; d += 1
        return d
    ok = True
    for L in (2, 3, 4):
        pos = [0] * L; forms = []
        for k in range(4 ** L):
            forms.append(tuple(pos)); pos[lev(k, L)] = (pos[lev(k, L)] + 1) % 4
        for d in range(1, L):
            for blk in range(4 ** (L - d)):
                inner = {f[:d] for f in forms[blk * 4 ** d:(blk + 1) * 4 ** d]}
                ok &= len(inner) == 4 ** d
    return ok

def F99():
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0])
    St = list(product(S, S)); nG = nF = 0; rule = None
    for r in product(S, repeat=4):
        f = dict(zip(St, r)); m = {v: (v[1], f[v]) for v in St}
        if all(m[v] == G(v) for v in St): nG += 1; rule = f
        if all(m[v] == Fo(v) for v in St): nF += 1
    return nG == 1 and nF == 0 and all(rule[v] == -v[0] for v in St) and all(G(Fo(v)) == v for v in St)

def F103():
    St = list(product(S, S))
    edges = [('x', y, s) for y in S for s in S] + [('y', x, s) for x in S for s in S]
    faces = [(p, q) for p in S for q in S]
    G = lambda v: (v[1], -v[0]); r = [(1, 1)]
    while len(r) < 5: r.append(G(r[-1]))
    ch = sorted(('x', u[0]) if u[0] != w[0] else ('y', u[1]) for u, w in zip(r, r[1:]))
    deg = all(sum(1 for e in edges if (e[0] == 'x' and e[1] == v[1] and e[2] in (v[0], -v[0])) or (e[0] == 'y' and e[1] == v[0] and e[2] in (v[1], -v[1]))) == 4 for v in St)
    return len(St) - len(edges) + len(faces) == 0 and ch == sorted([('x', 1), ('x', -1), ('y', 1), ('y', -1)]) and deg

def F95():
    def lev(k, L):
        d = 0
        while d < L - 1 and k % 4 == 3: k //= 4; d += 1
        return d
    ok = True
    for L, half in ((2, 9), (3, 33), (4, 129)):
        cnt = [0] * L
        for k in range(half - 1): cnt[lev(k, L)] += 1
        ok &= cnt[-1] == 2 and cnt[-2] == 6
        if L == 3: ok &= cnt[0] == 24 and cnt[0] % 4 == 0
        if L == 4: ok &= cnt[:2] == [96, 24]
    # four signs: the inside pair's six steps meet all four joint forms and arrive inverted
    st = [(1, 1)]
    for _ in range(6): st.append((st[-1][1], -st[-1][0]))
    ok &= len(set(st)) == 4 and st[6] == (-1, -1)
    return ok

def F90():
    from collections import deque
    states = sorted(REACH)
    def nx(st, off):
        _, _, cc = call([(K,) + st] if st else [], off)
        return tuple(cc[0][1:]) if cc else ()
    res = []
    for OFF in (OFFERS, [[], [(K, 1)], [(K, -1)]]):
        G = {s: sorted(set(nx(s, o) for o in OFF)) for s in states}
        def bfs(s):
            d = {s: 0}; q = deque([s])
            while q:
                x = q.popleft()
                for y in G[x]:
                    if y not in d: d[y] = d[x] + 1; q.append(y)
            return d
        rounds = []
        def dfs(path, vis):
            v = path[-1]
            if len(path) == 19:
                if () in G[v]: rounds.append(tuple(path))
                return
            for w in G[v]:
                if w not in vis: vis.add(w); path.append(w); dfs(path, vis); path.pop(); vis.discard(w)
        dfs([()], {()})
        res.append((sorted(len(G[s]) for s in states), all(len(bfs(s)) == 19 for s in states),
                    max(max(bfs(s).values()) for s in states), rounds))
    six, single = res
    ok = six[0] == [3] * 19 and six[1] and six[2] == 6 and len(six[3]) == 4
    ok &= single[0] == [2] * 18 + [3] and single[1] and single[2] == 11 and single[3] == []
    singles = [[], [(K, 1)], [(K, -1)]]
    needs = []
    for r in six[3]:   # the calls of each round taking two signs arriving together
        need = [i for i in range(19) if not any(nx(r[i], o) == r[(i + 1) % 19] for o in singles)]
        needs.append(len(need))
        ok &= all(all(len(o) == 2 and o[0][1] == o[1][1] for o in OFFERS if nx(r[i], o) == r[(i + 1) % 19]) for i in need)
    for r in six[3]:   # each family of one sign pair runs upward through its openings
        fam = [s[:2] for s in r[1:]]
        ok &= all(r[i + 1][2] == r[i][2] + 1 for i in range(1, 18) if fam[i - 1] == fam[i])
    return ok and sorted(needs) == [1, 1, 2, 2]

def F91():
    m = 4; N = m * m; words = []
    def go(v, path, vis, word):
        if len(path) == N:
            if ((v[0] + 1) % m, v[1]) == (0, 0) or (v[0], (v[1] + 1) % m) == (0, 0): words.append(word)
            return
        for d, w in ((1, ((v[0] + 1) % m, v[1])), (0, (v[0], (v[1] + 1) % m))):
            if w not in vis: vis.add(w); path.append(w); go(w, path, vis, word + (d,)); path.pop(); vis.discard(w)
    go((0, 0), [(0, 0)], {(0, 0)}, ())
    ok = len(words) == 8
    for w0 in words:
        prof = [len({w[k] for w in words if w[:k] == w0[:k]}) for k in range(15)]
        ok &= prof == [2, 2, 2] + [1] * 12
    # eight signs: a round is a choice at each of sixteen diagonals, odd outward: fifteen free, the sixteenth set, the rest laid
    return ok and 2 ** 15 == 32768

def F88():
    def pst(c):
        r = [(1, 1)]
        while len(r) < 4: r.append((r[-1][1], -r[-1][0]))
        return r[c % 4]
    def lev(k, L):
        d = 0
        while d < L - 1 and k % 4 == 3: k //= 4; d += 1
        return d
    def forms(L):
        pos = [0] * L; out = []
        for k in range(4 ** L + 1):
            f = ()
            for d in range(L): f += pst(pos[d])
            out.append(f)
            if k < 4 ** L: pos[lev(k, L)] += 1
        return out
    ok = True
    for L in (1, 2, 3, 4):
        F = forms(L); N = 4 ** L
        ok &= len(set(F[:N])) == N and F[N] == F[0]
    arr = lambda L, d: [k + 2 for k in range(4 ** L) if lev(k, L) >= d]
    ok &= arr(2, 1) == [5, 9, 13, 17] and arr(3, 2) == [17, 33, 49, 65]
    rel = {N: sum(1 for k in range(N - 5) if lev(k, 2 if N <= 17 else 3) == 0) for N in (9, 13, 17, 25, 65)}
    ok &= rel == {9: 3, 13: 6, 17: 9, 25: 15, 65: 45}
    F4, F6 = forms(2), forms(3)
    inv = lambda F, idx: [p for p, f in enumerate(F, 1) if all(f[i] == -F[0][i] for i in idx)]
    ok &= inv(F4, (0, 1))[0] == 3 and inv(F4, range(4)) == [9] and inv(F6, range(6))[0] == 35
    return ok

def F84():
    ok = all(_levels_walk(L) for L in (2, 3, 4))
    # a whole 1-257 inside one 1-17, the outside once in each 256
    def B(k):
        if k % 256 == 255: return 2
        i = k - k // 256
        return 1 if i % 16 == 15 else 0
    ok &= not _levels_walk(3, rule=B)
    # an outward step at each 9: one per eight, meeting 128 of 256
    v = (0, 0); seen = {v}
    for k in range(256):
        v = ((v[0] + 1) % 16, v[1]) if k % 8 == 7 else (v[0], (v[1] + 1) % 16)
        if v in seen: break
        seen.add(v)
    return ok and len(seen) == 128

def F57():
    # four signs as two pairs; one right spiral step at the first pair, then at the second, alternating
    St = list(product(S, repeat=4))
    A = lambda s: (s[1], -s[0], s[2], s[3]); B = lambda s: (s[0], s[1], s[3], -s[2])
    rounds = set()
    for s0 in St:
        s = s0; seen = [s0]
        for i in range(8):
            s = A(s) if i % 2 == 0 else B(s); seen.append(s)
        firstback = next(i for i in range(1, 9) if seen[i] == s0)
        if firstback != 8 or len(set(seen[:8])) != 8: return False
        rounds.add(frozenset(seen[:8]))
    # the orbits of the alternating pair of steps (as a two-step map) part the sixteen
    return sum(len(r) for r in rounds) >= 16 and len(set().union(*rounds)) == 16

def F58():
    rounds = [m for m, St in one_change_maps(2) if single_round(m, St)]
    St = list(product(S, S))
    right = {(x, y): (y, -x) for x, y in St}; other = {(x, y): (-y, x) for x, y in St}
    return len(list(one_change_maps(2))) == 16 and len(rounds) == 2 and right in rounds and other in rounds

def F59():
    St = list(product(S, S))
    rounds = []; onechange = []
    for img in product(St, repeat=4):
        m = dict(zip(St, img))
        if single_round(m, St):
            rounds.append(m)
            if all(sum(a != b for a, b in zip(s, m[s])) == 1 for s in St): onechange.append(m)
    # NI 8.1: only these two change one sign each step, reach each joint form, and meet no prior the step after
    no_back = [m for m in (dict(zip(St, img)) for img in product(St, repeat=4))
               if all(sum(a != b for a, b in zip(s, m[s])) == 1 for s in St)
               and all(m[m[s]] != s for s in St) and single_round(m, St)]
    return len(rounds) == 6 and len(onechange) == 2 and len(no_back) == 2

def F60():
    St = list(product(S, S))
    ok = True; halfsteps = []
    for m, _ in one_change_maps(2):
        if all(m[m[s]] == (-s[0], -s[1]) for s in St): halfsteps.append(m)
    right = {(x, y): (y, -x) for x, y in St}; other = {(x, y): (-y, x) for x, y in St}
    ok &= len(halfsteps) == 2 and right in halfsteps and other in halfsteps
    for m in (right, other):
        inv = [set(sub) for r in range(0, 5) for sub in combinations(St, r) if {m[s] for s in sub} == set(sub)]
        ok &= [len(x) for x in inv] == [0, 4]
    return ok

def F63():
    maps = [m for m, St in one_change_maps(3) if single_round(m, St)]
    total = 3 ** 8
    if len(maps) != 12 or total != 6561: return False
    St = list(product(S, repeat=3))
    group = []
    for p in permutations(range(3)):
        for fl in product(S, repeat=3):
            group.append(lambda s, p=p, fl=fl: tuple(fl[i] * s[p[i]] for i in range(3)))
    key = lambda m: frozenset(m.items())
    seen = set(); orbits = 0
    for m in maps:
        if key(m) in seen: continue
        orbits += 1
        for g in group:
            seen.add(key({g(s): g(m[s]) for s in St}))
    return orbits == 1

def F64():
    n = 4; N = 1 << n; cycles = set()
    def dfs(path, vis):
        v = path[-1]
        if len(path) == N:
            if bin(v ^ path[0]).count('1') == 1:
                c = tuple(path)
                if c[1] < c[-1]: cycles.add(c)
            return
        for b in range(n):
            w = v ^ (1 << b)
            if not vis[w]:
                vis[w] = True; path.append(w); dfs(path, vis); path.pop(); vis[w] = False
    vis = [False] * N; vis[0] = True; dfs([0], vis)
    es = [frozenset(frozenset((c[i], c[(i + 1) % N])) for i in range(N)) for c in cycles]
    G = [(p, msk) for p in permutations(range(n)) for msk in range(N)]
    def act(g, v):
        p, msk = g; w = 0
        for i in range(n):
            if v >> i & 1: w |= 1 << p[i]
        return w ^ msk
    seen = set(); orbits = 0
    for e in es:
        if e in seen: continue
        orbits += 1
        for g in G: seen.add(frozenset(frozenset(act(g, x) for x in ed) for ed in e))
    return len(cycles) == 1344 and len(G) == 384 and orbits == 9

def F76():
    # x the right sign, y the along sign: (x, y) -> (y, -x) turns along into right; MATH's F at P along, Q right is the same turn
    G = lambda v: (v[1], -v[0]); Fo = lambda v: (-v[1], v[0])
    along, right = (0, 1), (1, 0)
    ok = G(along) == right and G(right) == (0, -1) and Fo(along) == (-1, 0)
    # MATH labels (P, Q) = (along, right): F(P, Q) = (-Q, P)
    to_pq = lambda v: (v[1], v[0]); from_pq = lambda w: (w[1], w[0])
    FPQ = lambda w: (-w[1], w[0])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return ok and all(from_pq(FPQ(to_pq(v))) == G(v) for v in dirs)

def _pair_round():
    r = [(1, 1)]
    while len(r) < 4: r.append((r[-1][1], -r[-1][0]))
    return {s: i for i, s in enumerate(r)}

def _q4_rounds():
    n, N = 4, 16; cycles = []
    def dfs(path, vis):
        v = path[-1]
        if len(path) == N:
            if bin(v ^ path[0]).count('1') == 1 and path[1] < path[-1]: cycles.append(tuple(path))
            return
        for b in range(n):
            w = v ^ (1 << b)
            if not vis[w]:
                vis[w] = True; path.append(w); dfs(path, vis); path.pop(); vis[w] = False
    vis = [False] * N; vis[0] = True; dfs([0], vis)
    return cycles

def _ps(v, i, j): return (1 - 2 * ((v >> i) & 1), 1 - 2 * ((v >> j) & 1))

def F77():
    pos = _pair_round()
    co = lambda v: (pos[_ps(v, 0, 1)], pos[_ps(v, 2, 3)])
    steps = {frozenset((v, v ^ (1 << b))) for v in range(16) for b in range(4)}
    grid = set()
    for a in range(4):
        for b in range(4):
            grid.add(frozenset(((a, b), ((a + 1) % 4, b)))); grid.add(frozenset(((a, b), (a, (b + 1) % 4))))
    return len({co(v) for v in range(16)}) == 16 and {frozenset(co(v) for v in e) for e in steps} == grid \
        and len(steps) == 32 and 16 - len(grid) + 16 == 0

def F78():
    pos = _pair_round(); N = 16
    cycles = _q4_rounds()
    syms = [(p, m) for p in permutations(range(4)) for m in range(16)]
    def act(g, v):
        p, m = g; w = 0
        for i in range(4):
            if v >> i & 1: w |= 1 << p[i]
        return w ^ m
    es = lambda c: frozenset(frozenset((c[i], c[(i + 1) % N])) for i in range(N))
    form = {}; k = 0
    for c in cycles:
        e = es(c)
        if e in form: continue
        for g in syms: form[frozenset(frozenset(act(g, x) for x in ed) for ed in e)] = k
        k += 1
    pairings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    def mono(c, P):
        (i, j), (kk, l) = P
        for o1 in ((i, j), (j, i)):
            for o2 in ((kk, l), (l, kk)):
                st = []
                for t in range(N):
                    u, w = c[t], c[(t + 1) % N]
                    st.append(((pos[_ps(w, *o1)] - pos[_ps(u, *o1)]) % 4, (pos[_ps(w, *o2)] - pos[_ps(u, *o2)]) % 4))
                if all(x in ((1, 0), (0, 1)) for x in st): return st
        return None
    found = []
    for c in cycles:
        for P in pairings:
            st = mono(c, P) or mono(c[::-1], P)
            if st: found.append((c, st)); break
    pats = set()
    for c, st in found:
        w = ''.join('A' if x == (1, 0) else 'B' for x in st)
        w = min(w[r:] + w[:r] for r in range(N))
        pats.add(tuple(sorted((w.count('A'), w.count('B')))) + (w in ('AAABAAABAAABAAAB', 'ABBBABBBABBBABBB'),))
    return len(cycles) == 1344 and k == 9 and len(found) == 48 and len({form[es(c)] for c, _ in found}) == 1 \
        and pats == {(4, 12, True)}

def F80():
    def walk(word):
        a = b = 0; seen = [(0, 0)]
        for ch in word:
            if ch == 'i': b = (b + 1) % 4
            else: a = (a + 1) % 4
            seen.append((a, b))
        return seen
    half = lambda x: ((x[1] - x[0]) % 4) // 2
    s9 = walk('io' * 4); s17 = walk('iiio' * 4)
    return (len(set(s9[:8])) == 8 and s9[8] == s9[0] and len({half(x) for x in s9}) == 1
            and len(set(s17[:16])) == 16 and s17[16] == s17[0]
            and [k + 2 for k, ch in enumerate('iiio' * 4) if ch == 'o'] == [5, 9, 13, 17]
            and [k + 2 for k in range(16) if half(s17[k]) != half(s17[k + 1])] == [3, 7, 11, 15])

def _torus_rounds_dfs(m):
    N = m * m; out = []
    def go(v, path, vis):
        if len(path) == N:
            if ((v[0] + 1) % m, v[1]) == (0, 0) or (v[0], (v[1] + 1) % m) == (0, 0): out.append(tuple(path))
            return
        for w in (((v[0] + 1) % m, v[1]), (v[0], (v[1] + 1) % m)):
            if w not in vis:
                vis.add(w); path.append(w); go(w, path, vis); path.pop(); vis.discard(w)
    go((0, 0), [(0, 0)], {(0, 0)})
    return out

def _diag_constant(c, m):
    N = len(c); ch = {}
    for k in range(N):
        v = c[k]; t = c[(k + 1) % N][0] != v[0]
        if ch.setdefault((v[0] + v[1]) % m, t) != t: return False
    return True

def _closes(bits, m):
    v = (0, 0); seen = {v}
    for _ in range(m * m - 1):
        v = ((v[0] + 1) % m, v[1]) if bits[(v[0] + v[1]) % m] else (v[0], (v[1] + 1) % m)
        if v in seen: return False
        seen.add(v)
    return (((v[0] + 1) % m, v[1]) if bits[(v[0] + v[1]) % m] else (v[0], (v[1] + 1) % m)) == (0, 0)

def F81():
    for m in (4, 6):
        R = _torus_rounds_dfs(m)
        if not all(_diag_constant(c, m) for c in R): return False
    m = 16; count = 0; neck = {}
    for b in product((0, 1), repeat=m):
        # one pass of sixteen steps moves each form of a diagonal alike: a shift by the outward count along it
        a = sum(b)
        if a % 2 == 1:
            count += 1
            k = min(b[r:] + b[:r] for r in range(m)); neck[k] = sum(k)
    reps_ok = all(_closes(k, m) for k in neck) and not _closes((0, 0, 0, 1) * 4, m) and not _closes((0,) * 7 + (1,) + (0,) * 7 + (1,), m) \
        and not any(_closes(b, m) for b in [(0, 1) * 8, (0, 0, 1, 1) * 4, (1,) * 16, (0,) * 16])
    from collections import Counter
    return count == 32768 and len(neck) == 2048 and reps_ok and \
        sorted(Counter(neck.values()).items()) == [(1, 1), (3, 35), (5, 273), (7, 715), (9, 715), (11, 273), (13, 35), (15, 1)]

def F82():
    ok = all(_closes(tuple([0] * (m - 1) + [1]), m) for m in (2, 3, 4, 5, 8, 16))
    ok &= sum(1 for b in product((0, 1), repeat=16) if sum(b) == 1 and b == min(b[r:] + b[:r] for r in range(16))) == 1
    return ok and [2 ** (2 ** k) + 1 for k in range(4)] == [3, 5, 17, 257]

# ---------------------------------------------------------------- PART TWO (the code)
tree = ast.parse(code)

def R2():
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    asg = [t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets]
    sig = {f.name: [a.arg for a in f.args.args] for f in fns}
    return (sig == {'_1_self_coupling': ['_3_self_carrying', '_2_self_offering'],
                    '_9_other_releasing': ['_10_other_surfacing', '_5_other_neutralling']}
            and asg == ['CONNECTORS', 'JOINS'])

NAMES = {1: 'self_coupling', 2: 'self_offering', 3: 'self_carrying', 4: 'self_sharing', 5: 'other_neutralling',
         6: 'other_crossing', 7: 'other_corusing', 8: 'other_torusing', 9: 'other_releasing', 10: 'other_surfacing',
         11: 'other_chaining', 12: 'other_surplusing', 13: 'social_neutralling', 14: 'social_crossing',
         15: 'social_corusing', 16: 'social_torusing', 17: 'social_abundancing'}

def R4():
    ids = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)} | \
          {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)} | \
          {a.arg for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) for a in n.args.args}
    ok = all(f'_{k}_{v}' in ids for k, v in NAMES.items() if k <= 16)
    ok &= not any(i.startswith('_17') for i in ids)
    strs = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str) and '-' in n.value]
    ok &= all(s.split('-', 1)[1].replace('-', '_') == NAMES[int(s.split('-')[0])] for s in strs)
    return ok

def R5():
    odd = [n for n in range(1, 18) if n % 2]; even = [n for n in range(1, 18) if n % 2 == 0]
    co = sum(3 for _ in odd) + sum(2 for _ in even); bi = sum(2 for _ in odd) + sum(3 for _ in even)
    return len(odd) == 9 and len(even) == 8 and co + bi == 85 and co == 43 and bi == 42

def R6():
    roots = {v.split('_')[1] for v in NAMES.values()}
    two = {r: [k for k, v in NAMES.items() if v.split('_')[1] == r] for r in roots}
    return (len(roots) == 13 and {r for r, ks in two.items() if len(ks) == 2} == {'neutralling', 'crossing', 'corusing', 'torusing'}
            and all(ks[1] - ks[0] == 8 for ks in two.values() if len(ks) == 2))

OFFERS = [[], [(K, -1)], [(K, 1)], [(K, -1), (K, -1)], [(K, 1), (K, 1)], [(K, 1), (K, -1)]]

def reach():
    start = (); seen = {start}; frontier = [start]; trans = 0
    while frontier:
        nxt = []
        for st in frontier:
            for off in OFFERS:
                _, _, c = call([(K,) + st] if st else [], off)
                s2 = tuple(c[0][1:]) if c else ()
                trans += 1
                if s2 not in seen: seen.add(s2); nxt.append(s2)
        frontier = nxt
    return seen, trans

REACH, TRANS = reach()

def R7():
    ok = True
    for st in REACH:
        for off in OFFERS:
            s, c = C([(K,) + st] if st else [], off)
            ok &= isinstance(s, list) and all(len(x) == 2 and x[1] in (-1, 0, 1) for x in s)
            ok &= isinstance(c, list) and all(len(x) == 4 and x[1] in S and x[2] in S and 0 <= x[3] <= 4 for x in c)
            C(c, [])  # the returned 11 is taken as the next 3
    return ok

def R9():
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_1_self_coupling')
    reads = [n for n in ast.walk(fn) if isinstance(n, ast.Name) and n.id == '_3_self_carrying' and isinstance(n.ctx, ast.Load)]
    return len(reads) == 3

def R10():
    ok = True
    for c, t, a in product(S, S, range(3)):
        s, st, _ = call([(K, c, t, a)], [])        # surfaces -c, fresh write
        ok &= st == (-c, -t, 0)
        s, st, _ = call([(K, c, t, a)], [(K, c)])  # surfaces 0, continues: 8 kept
        ok &= s == 0 and st == (c, t, a + 1)
    return ok

def R11():
    ok = all(call([(K, c, t, 0)], [])[0] == -c for c, t in product(S, S))
    ok &= C([], [(K, 0)]) == ([], [])
    ok &= C([(K, 1, -1, 0)], [(K, 0)]) == C([(K, 1, -1, 0)], [])
    return ok

def R13():
    s1 = C([], [(K, 1), (K, 1)]); s2 = C([], [(K, 1), (K, -1)])
    s3 = C([], [(K, -1), (K, -1)])
    return (s1 == ([(K, 1)], [(K, 1, -1, 0)]) and s2 == ([(K, 0)], []) and s3 == ([(K, -1)], [(K, -1, -1, 0)]))

def R14():
    ok = True; maxa = {1: 0, -1: 0}
    for c, t, a in product(S, S, range(5)):
        cont = (a + 1 <= 3) or (a + 1 == 4 and t > 0)
        s, st, _ = call([(K, c, t, a)], [(K, c)])
        ok &= s == 0 and (st == (c, t, a + 1) if cont else st is None)
    for st in REACH:
        if st: maxa[st[1]] = max(maxa[st[1]], st[2])
    return ok and maxa == {-1: 3, 1: 4}

def R15():
    ok = True
    for c, t, a in product(S, S, range(3)):
        for off in OFFERS:
            s, st, _ = call([(K, c, t, a)], off)
            if s: ok &= st == (s, -t, 0)
    for sgn in S:
        s, st, _ = call([], [(K, sgn)])
        ok &= s == sgn and st == (sgn, -1, 0)
    return ok

def R16():
    ok = True
    for c, t in product(S, S):
        for off in OFFERS:
            sgn, st, _ = call([(K, c, t, 0)], off)
            if sgn:
                ok &= (st[0], st[1]) == (sgn, -t)                     # (6, 10) = (t, s) opens (7, 8) = (s, -t)
                ok &= (t == sgn) == (st[0] != st[1])                  # agreeing opens opposing, opposing agreeing
                ok &= (st[0], st[1]) == (lambda x, y: (y, -x))(t, sgn)  # the right spiral step of F58
    return ok

def R17():
    s, c = C([(K, 1, -1, 0)], [(K, 1)])
    six = {k: t for k, _, t, _ in [(K, 1, -1, 0)]}
    return s == [(K, 0)] and c == [(K, 1, -1, 1)] and six[K] == -1

def trace(offers, carry=()):
    carry = list(carry); out = []; cs = []
    for off in offers:
        s, carry = C(carry, off); out.append(dict(s).get(K)); cs.append(tuple(carry[0][1:]) if carry else None)
    return out, cs

def R18():
    out, cs = trace([[(K, 1)]] * 7)
    ok = out == [1, 0, 0, 0, 0, 1, 0]
    ok &= cs[:5] == [(1, -1, 0), (1, -1, 1), (1, -1, 2), (1, -1, 3), None] and cs[5] == (1, -1, 0)
    out2, cs2 = trace([[(K, -1)]] + [[(K, 1)]] * 7)
    ok &= cs2[1] == (1, 1, 0) and [x[2] for x in cs2[2:6]] == [1, 2, 3, 4] and cs2[6] is None
    ok &= out2[2:7] == [0, 0, 0, 0, 0]
    return ok

def R19():
    cases = 0; ok = True
    offers = [[]] + [[(K, a)] for a in S] + [[(K, a), (K, b)] for a, b in product(S, S)]
    for c, t in product(S, S):
        for off in offers:
            vals = [v for _, v in off]
            want = c if vals == [c, c] else (0 if vals == [c] else -c)
            s, st, _ = call([(K, c, t, 0)], off)
            ok &= s == want
            if s: ok &= st[0] == s
            if t == -1: cases += 1
    return ok and cases == 14

def R20():
    s1, c1 = C([(K, 1, -1, 0)], [(K, 1)])
    s2, c2 = C([(K, 1, -1, 0)], [(K, 1), (K, 1)])
    return s1 == [(K, 0)] and c1 == [(K, 1, -1, 1)] and s2 == [(K, 1)] and c2 == [(K, 1, 1, 0)]

def R21():
    o0, _ = trace([[(K, 1)]] * 5, [(K, 1, -1, 0)]); o1, _ = trace([[(K, 1)]] * 4, [(K, 1, -1, 1)])
    return o0 == [0, 0, 0, 0, 1] and o1 == [0, 0, 0, 1]

def R22():
    ok = True
    for c, t in product(S, S):
        # fresh write at s = -c (nothing arriving): pair relation kept, next 6 inverts
        s, st, _ = call([(K, c, t, 0)], [])
        ok &= st[1] == -t and ((st[0] == st[1]) == (c == t))
        # fresh write at s = c (two c arriving): both change
        s, st, _ = call([(K, c, t, 0)], [(K, c), (K, c)])
        ok &= s == c and st[1] == -t and ((st[0] == st[1]) != (c == t))
        # kept through a 0: next 6 releases t again
        s, st, _ = call([(K, c, t, 0)], [(K, c)])
        ok &= s == 0 and st[1] == t
    # completing unrenewed: key releases nothing at 6 next
    s, c2 = C([(K, 1, -1, 3)], [(K, 1)])
    ok &= s == [(K, 0)] and c2 == []
    return ok

def R23():
    neg = {st for st in REACH if st and st[1] == -1}; pos = {st for st in REACH if st and st[1] == 1}
    return (len(REACH) == 19 and () in REACH and len(neg) == 8 and len(pos) == 10
            and {st[2] for st in neg} == {0, 1, 2, 3} and {st[2] for st in pos} == {0, 1, 2, 3, 4}
            and TRANS == 114)

def representative(seq):
    nz = [v for v in seq if v != 0]
    if not nz: return []
    tot = max(-2, min(2, sum(nz)))
    if tot == 0: return [(K, 1), (K, -1)]
    return [(K, 1 if tot > 0 else -1)] * abs(tot)

def R24():
    comps = 0; ok = True
    for st in REACH:
        base = [(K,) + st] if st else []
        for L in range(7):
            for seq in product((-1, 0, 1), repeat=L):
                comps += 1
                ok &= C(base, [(K, v) for v in seq]) == C(base, representative(seq))
    return ok and comps == 20767

def R25():
    states = sorted(REACH)
    ops = [[], [(K, 1)], [(K, -1)]]
    trans = len(states) * len(ops)
    def run(st, off, n=6):
        carry = [(K,) + st] if st else []; out = []
        for _ in range(n):
            s, carry = C(carry, off); v = dict(s).get(K); out.append(v if v else 0)
        return out
    pairs = list(combinations(states, 2))
    plus = {p for p in pairs if run(p[0], [(K, 1)]) != run(p[1], [(K, 1)])}
    minus = {p for p in pairs if run(p[0], [(K, -1)]) != run(p[1], [(K, -1)])}
    return trans == 57 and len(pairs) == 171 and len(plus) == 146 and len(minus) == 146 and len(plus | minus) == 171

def R27():
    ok = True
    surf = [('a', 1), ('b', -1), ('c', 0)]; neut = {'a': 'x', 'b': 'y', 'c': 'z'}
    out = R(surf, neut)
    ok &= out == [('x', 1), ('y', -1), ('z', 0)]
    ok &= all(len(x) == 2 for x in out)
    return ok

def R28():
    ok = True
    for c in S:
        carry = []; offs = [[(K, c)]] + [[]] * 8; surf = []; pairs = []
        for off in offs:
            s, carry = C(carry, off); surf.append(dict(s)[K]); pairs.append(carry[0][1:3])
        t = -1
        ok &= surf == [c, -c] * 4 + [c]
        ok &= pairs[:4] == [(c, t), (-c, -t), (c, t), (-c, -t)]
        seq = [pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1], pairs[2][0]]
        ok &= seq == [c, t, -c, -t, c]
    return ok

def R29():
    ok = True
    for c, t in product(S, S):
        seq = [c, t, -c, -t, c]
        prs = [(seq[i], seq[i + 1]) for i in range(4)]
        ok &= sorted(prs) == sorted(product(S, S))
        ok &= all(prs[i + 1] == (prs[i][1], -prs[i][0]) for i in range(3))
        agree = [a == b for a, b in prs]
        ok &= agree[0] == agree[2] and agree[1] == agree[3] and agree[0] != agree[1]
    return ok

def R30():
    ok = True
    for a, b, z in product(S, S, S):
        ok &= (((a == b) != (b == z)) == (z == -a))
    return ok and (1 == 1) and (1 == 1)  # +,+,+: (a,b) and (b,z) both agree

def R31():
    ok = True
    for c, t in product(S, S):
        s, st, _ = call([(K, c, t, 0)], [])
        ok &= s == -c  # 10 surfaces -c while 6 releases t
    _, c1 = C([], [(K, 1)])
    _, c2 = C([], [(K, -1)]); _, c2 = C(c2, [])
    ok &= c1 == [(K, 1, -1, 0)] and c2 == [(K, 1, 1, 0)]
    s1, _ = C(c1, []); s2, _ = C(c2, [])
    ok &= s1 == [(K, -1)] and s2 == [(K, -1)] and c1[0][2] == -1 and c2[0][2] == 1
    a, ca = C([(K, 1, -1, 0)], [(K, 1)]); b, cb = C([(K, 1, -1, 0)], [(K, -1)])
    ok &= a == [(K, 0)] and ca == [(K, 1, -1, 1)] and b == [(K, -1)] and cb[0][1] == -1
    return ok

CON = ns['CONNECTORS']; JOI = ns['JOINS']

def R32():
    want = {2: ('2-self-offering', 'right', 'arriving'), 6: ('6-other-crossing', 'left', 'releasing'),
            9: ('9-other-releasing', 'backward', 'along'), 10: ('10-other-surfacing', 'right', 'releasing'),
            14: ('14-social-crossing', 'left', 'arriving'), 17: ('17-social-abundancing', 'forward', 'along')}
    across = [k for k, v in CON.items() if v[2] != 'along']; along = [k for k, v in CON.items() if v[2] == 'along']
    return CON == want and across == [2, 6, 10, 14] and all(k % 2 == 0 for k in across) and along == [9, 17] and all(k % 2 for k in along)

def R33():
    ok = JOI == {10: 14, 6: 2, 17: 9, 9: 17}
    ok &= all(a % 2 == b % 2 for a, b in JOI.items())
    ok &= 10 - 2 == 8 and 14 - 6 == 8 and (6 + 8, 2 + 8) == (14, 10)
    return ok

def R34():
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    used = {n.id for f in fns for n in ast.walk(f) if isinstance(n, ast.Name)}
    if 'CONNECTORS' in used or 'JOINS' in used: return False
    ns2 = {}; exec(code, ns2); ns2['CONNECTORS'] = {}; ns2['JOINS'] = {}
    C2 = ns2['_1_self_coupling']
    return all(C2([(K,) + st] if st else [], off) == C([(K,) + st] if st else [], off) for st in REACH for off in OFFERS)

def R35():
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    in_fn = any((isinstance(n, ast.Constant) and n.value == 17) or (isinstance(n, ast.Name) and '17' in n.id)
                for f in fns for n in ast.walk(f))
    return (not in_fn) and 17 in CON and 17 in JOI and JOI[17] == 9 and JOI[9] == 17

# two resolvers joined 6 -> 2
def six(carry): return [(k, t) for k, c, t, a in carry]

def two_run(sa, sb, first, ab, ba, calls=12):
    car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}; inbox = {'A': [], 'B': []}
    order = ['A', 'B'] if first == 'A' else ['B', 'A']; log = []
    for i in range(calls):
        me = order[i % 2]; other = 'B' if me == 'A' else 'A'
        rel = six(car[me]); s, c = C(car[me], inbox[me]); inbox[me] = []
        if (ab if me == 'A' else ba): inbox[other] = rel
        log.append((me, dict(s).get(K), rel, car[me], c)); car[me] = c
    return log

def R40():
    tot = zeros = cont = 0
    for sa, sb, f in product(S, S, 'AB'):
        for me, s, rel, cin, cout in two_run(sa, sb, f, True, True):
            tot += 1
            if s == 0:
                zeros += 1
                cont += len(rel) == 1 and cout == [cin[0][:3] + (cin[0][3] + 1,)]
    a_both = [x[1] for x in two_run(-1, -1, 'A', True, True) if x[0] == 'A']
    others = [[x[1] for x in two_run(-1, -1, 'A', ab, ba) if x[0] == 'A'] for ab, ba in [(True, False), (False, True), (False, False)]]
    return (tot == 96 and zeros == 32 and cont == 32 and a_both == [1, -1, 0, 1, -1, 0]
            and all(o == [1, -1, 1, -1, 1, -1] for o in others))

def R41():
    parted = comps = 0
    for sa, sb, f in product(S, S, 'AB'):
        both = two_run(sa, sb, f, True, True)
        for me in 'AB':
            only = two_run(sa, sb, f, me == 'B', me == 'A')
            comps += 1
            parted += [x[1] for x in both if x[0] == me] != [x[1] for x in only if x[0] == me]
    return comps == 16 and parted == 12

def R42():
    ok = True
    # the named instance
    a = C([], [(K, 1)])[1]; relA = six(a); a = C(a, [])[1]
    b = C([], [(K, -1)])[1]; relB = six(b)
    ok &= relA == [(K, -1)] and relB == [(K, -1)]
    sj, cj = C(a, relB); su, cu = C(a, [])
    ok &= sj == [(K, 0)] and cj == [a[0][:3] + (1,)] and su == [(K, 1)] and cu == [(K, 1, -1, 0)]
    # 256 runnings: four seed pairs x each joining of the two legs at each of three rounds
    runs = 0
    for sa, sb in product(S, S):
        for legs in product(product((True, False), repeat=2), repeat=3):
            runs += 1
            car = {'A': C([], [(K, sa)])[1], 'B': C([], [(K, sb)])[1]}; inbox = {'A': [], 'B': []}
            for ab, ba in legs:
                for me, other, joined in (('A', 'B', ab), ('B', 'A', ba)):
                    rel = six(car[me]); cin = car[me]
                    s, c = C(cin, inbox[me]); inbox[me] = []
                    inbox[other] = rel if joined else []
                    if dict(s).get(K) == 0 and cin:
                        ok &= c == [cin[0][:3] + (cin[0][3] + 1,)]
                    car[me] = c
    return ok and runs == 256

def R43():
    ok = True; Cn = {}
    for arriving in S:
        B = C([], [(K, 1)])[1]; Cc = C([], [(K, 1)])[1]
        relB = six(B); sB, B = C(B, [(K, arriving)])
        sC, Cc = C(Cc, relB)
        ok &= relB == [(K, -1)] and sC == [(K, -1)]
        ok &= sB == ([(K, 0)] if arriving == 1 else [(K, -1)])
        relB2 = six(B); sC2, _ = C(Cc, relB2)
        Cn[arriving] = (relB2, sC2)
    ok &= Cn[1] == ([(K, -1)], [(K, 0)]) and Cn[-1] == ([(K, 1)], [(K, 1)])
    return ok

def ring(n, steps):
    carry = [[] for _ in range(n)]; inbox = [[] for _ in range(n)]; inbox[0] = [(K, 1)]
    states = []; surf = []
    for _ in range(steps):
        nb = [[] for _ in range(n)]; row = []
        for i in range(n):
            s, c = C(carry[i], inbox[i]); carry[i] = c
            nb[(i + 1) % n] += R(s, {K: K}); row.append(dict(s).get(K))
        inbox = nb; surf.append(tuple(row))
        states.append((tuple(tuple(c) for c in carry), tuple(tuple(b) for b in inbox)))
    return surf, states

def recur(n):
    surf, st = ring(n, 12 * n + 20); first = {}
    for t, s in enumerate(st):
        if s in first: return first[s] + 1, t - first[s]
        first[s] = t

def R44():
    ok = trace([[(K, 1)], [], [], [], [], []], [])[0] is not None
    surf, _ = ring(1, 8); ok &= [x[0] for x in surf] == [1, 0, -1, 0, 1, 0, -1, 0]
    for n in list(range(1, 12)) + [17, 59]:
        ok &= recur(n) == (n, 2 if n % 2 == 0 else 4 * n)
    return ok

def R45():
    ok = True
    for n in list(range(1, 12)) + [17, 59]:
        surf, _ = ring(n, 10 * n + 8)
        per = surf[n:]
        if n % 2 == 0:
            ok &= all(per[t][i] == -per[t + 1][i] for t in range(len(per) - 1) for i in range(n))
            ok &= all(per[t][i] == -per[t][(i + 1) % n] for t in range(len(per)) for i in range(n))
        else:
            ok &= all(per[t + 2 * n][i] == -per[t][i] for t in range(len(per) - 2 * n) for i in range(n))
            ok &= all(per[t + 4 * n][i] == per[t][i] for t in range(len(per) - 4 * n) for i in range(n))
            if n > 1:
                zs = [(t, [i for i in range(n) if per[t][i] == 0]) for t in range(len(per))]
                ok &= all(len(z) <= 1 for _, z in zs)
                at = [(t, z[0]) for t, z in zs if z]
                ok &= all(b[1] == (a[1] + 1) % n and b[0] - a[0] == 2 for a, b in zip(at, at[1:]))
    return ok and 2 * 59 == 118 and 4 * 59 == 236

def R46():
    rest = None
    for n in range(1, 12):
        _, st = ring(n, 5000)
        rest = ((tuple(() for _ in range(n))), tuple(() for _ in range(n)))
        if any(s == rest for s in st): return False
    return True

def R56():
    SYM = {1: '+', -1: '-', 0: '0'}
    def step(carry, sym):
        inbox = [] if sym == '.' else [(K, {'+': 1, '-': -1, '0': 0}[sym])]
        s, cc = C(list(carry), inbox)
        out = R(s, {K: K}); return tuple(tuple(x) for x in cc), ('.' if not out else SYM[out[0][1]])
    flip = lambda s: '-' if s == '+' else '+'
    E = (); a = step(E, '+')[0]; b = step(a, '.')[0]; D = {a, b}   # the two carryings, reached at the code from empty
    two_carryings = a == ((K, 1, -1, 0),) and b == ((K, -1, 1, 0),)
    def run(st, ins):
        outs = []
        for x in ins: st, o = step(st, x); outs.append(o)
        return st, ''.join(outs)
    checks = {'two carryings': two_carryings}
    # P0: a self given one sign and nothing after surfaces the sign alternating at each call, its carrying a, b, a, b
    st, out = run(E, '+' + '.' * 11); checks['P0 one sign alone alternates'] = out == '+-' * 6 and step(a, '.') == (b, '-') and step(b, '.') == (a, '+')
    # L1: given an alternating arriving, a self surfaces it at the same call, its carrying a or b
    ok = True
    for s0, first in ((E, '+'), (a, '-'), (b, '+')):
        ins = ''.join(first if i % 2 == 0 else flip(first) for i in range(12)); st, out = run(s0, ins)
        ok &= out == ins and st in D
    checks['L1 an alternating arriving surfaces as it arrives'] = ok
    # W: the wave meeting itself at the seed: in phase (even ring) nothing changes; out of phase (odd ring) one 0, then the arriving
    st, out = run(b, '+-' * 6); checks['W even: in phase, no change'] = out == '+-' * 6 and st in D
    st, out = run(a, '+-' * 6); checks['W odd: out of phase, one 0, then the arriving'] = out == '0' + '-+' * 5 + '-' and st in D
    # L2: an alternating arriving with one 0: the self surfaces its own next sign at the 0, the 0 one call later, then the arriving
    ok = True
    for s0, s in ((a, '-'), (b, '+'), (E, '+')):
        ins = s + '0' + flip(s) + s + flip(s) + s + flip(s); st, out = run(s0, ins)
        ok &= out == s + flip(s) + '0' + s + flip(s) + s + flip(s) and st in D
        st2 = s0
        for x in ins[:4]: st2, _ = step(st2, x)
        ok &= st2 in D   # back at the two by the second call after the 0
    checks['L2 a 0 passes one call later'] = ok
    # the rings themselves, n = 1 to 60: the pause formula and no rest
    def ring(n, T):
        carry = [E] * n; inbox = ['.'] * n; inbox[0] = '+'; outs = [[] for _ in range(n)]; rest = False
        for t in range(T):
            nb = ['.'] * n
            for i in range(n):
                carry[i], o = step(carry[i], inbox[i]); outs[i].append(o); nb[(i + 1) % n] = o
            inbox = nb
            rest |= all(x == E for x in carry) and all(x == '.' for x in inbox)
        return [''.join(o) for o in outs], rest
    ok = True
    for n in range(2, 61):
        outs, rest = ring(n, 8 * n + 8)
        ok &= not rest
        for i in range(n):
            zeros = [t for t, x in enumerate(outs[i]) if x == '0']
            want = [n + 2 * i + 2 * n * k for k in range(8)] if n % 2 else []
            ok &= zeros == [z for z in want if z < 8 * n + 8]
    return all(checks.values()) and ok


def R55_probe():
    return C([], []) == ([], [])

def R48():
    ok = all(((n + 8) % 2 == n % 2) for n in range(1, 10))
    ok &= all(((17 - n) % 2 != n % 2) and 17 - (17 - n) == n for n in range(1, 17))
    ok &= all(((9 - n) % 2 != n % 2) and 9 - (9 - n) == n for n in range(1, 9))
    return ok

def R49():
    p9 = sorted({tuple(sorted((n, 9 - n))) for n in range(1, 9)})
    p17 = sorted({tuple(sorted((n, 17 - n))) for n in range(1, 17)})
    p8 = [(n, n + 8) for n in range(1, 10)]
    return (p9 == [(1, 8), (2, 7), (3, 6), (4, 5)] and all((a + b) % 2 for a, b in p9)
            and len(p17) == 8 and all((a + b) % 2 for a, b in p17) and 17 - 17 not in range(1, 18)
            and all(a % 2 == b % 2 for a, b in p8) and (3, 11) in p8 and (7, 15) in p8)

def R50():
    rows = [[n, n + 8, 9 - n, 17 - n] for n in range(1, 5)]
    return rows == [[1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]] and all(17 - (n + 8) == 9 - n for n in range(1, 9))

FORMS = {'1-9-8-16': ([1, 9, 8, 16], 'co co bi bi'), '2-15-7-10': ([2, 15, 7, 10], 'bi co co bi'),
         '3-11-6-14': ([3, 11, 6, 14], 'co co bi bi'), '4-13-5-12': ([4, 13, 5, 12], 'bi co co bi'),
         '9-5-12-8': ([9, 5, 12, 8], 'co co bi bi'), '7-11-6-10': ([7, 11, 6, 10], 'co co bi bi'),
         '1-9-5-12-8-16': ([1, 9, 5, 12, 8, 16], 'co co co bi bi bi'), '2-15-7-11-6-10': ([2, 15, 7, 11, 6, 10], 'bi co co co bi bi'),
         '3-11-7-10-6-14': ([3, 11, 7, 10, 6, 14], 'co co co bi bi bi'), '4-13-5-9-8-12': ([4, 13, 5, 9, 8, 12], 'bi co co co bi bi'),
         '1-9-5-13-4-12-8-16': ([1, 9, 5, 13, 4, 12, 8, 16], 'co co co co bi bi bi bi'),
         '2-15-7-11-3-14-6-10': ([2, 15, 7, 11, 3, 14, 6, 10], 'bi co co co co bi bi bi')}
HIGHER = {'18-31-23-26': ([18, 31, 23, 26], 'bi co co bi'), '19-27-22-30': ([19, 27, 22, 30], 'co co bi bi'),
          '18-31-23-27-22-26': ([18, 31, 23, 27, 22, 26], 'bi co co co bi bi'),
          '19-27-23-26-22-30': ([19, 27, 23, 26, 22, 30], 'co co co bi bi bi')}

def one_run_each(c):
    p = [x % 2 for x in c]; ch = sum(p[i] != p[i - 1] for i in range(len(p)))
    return ch == 2 and p.count(1) == p.count(0)

def R51():
    ok = True
    for c, rnd in list(FORMS.values()) + list(HIGHER.values()):
        ok &= one_run_each(c) and ' '.join('co' if x % 2 else 'bi' for x in c) == rnd
    return ok and not any(17 in c for c, _ in FORMS.values())

def R52():
    odd_p = {'1-9-8-16': '2-15-7-10', '2-15-7-10': '1-9-8-16', '3-11-6-14': '4-13-5-12', '4-13-5-12': '3-11-6-14',
             '9-5-12-8': '7-11-6-10', '7-11-6-10': '9-5-12-8', '1-9-5-12-8-16': '2-15-7-11-6-10',
             '2-15-7-11-6-10': '1-9-5-12-8-16', '3-11-7-10-6-14': '4-13-5-9-8-12', '4-13-5-9-8-12': '3-11-7-10-6-14',
             '1-9-5-13-4-12-8-16': '2-15-7-11-3-14-6-10', '2-15-7-11-3-14-6-10': '1-9-5-13-4-12-8-16'}
    even_p = {'2-15-7-10': '3-11-6-14', '3-11-6-14': '2-15-7-10', '4-13-5-12': '4-13-5-12', '7-11-6-10': '7-11-6-10',
              '2-15-7-11-6-10': '3-11-7-10-6-14', '3-11-7-10-6-14': '2-15-7-11-6-10',
              '2-15-7-11-3-14-6-10': '2-15-7-11-3-14-6-10'}
    oddsw = lambda n: n + 1 if n % 2 else n - 1
    evensw = lambda n: n + 1 if n % 2 == 0 else n - 1
    rots = lambda c: [tuple(c[i:] + c[:i]) for i in range(len(c))]
    rev = lambda c: [c[0]] + c[1:][::-1]
    listed = [sorted(c) for c, _ in FORMS.values()]
    ok = True
    for sw, P in ((oddsw, odd_p), (evensw, even_p)):
        for f, (c, _) in FORMS.items():
            img = [sw(x) for x in c]
            if f in P:
                tgt = FORMS[P[f]][0]
                ok &= (tuple(img) in rots(tgt)) if P[f] == f else (tuple(img) in rots(rev(tgt)))
            else:
                as_form = any(tuple(img) in rots(c2) or tuple(img) in rots(rev(c2)) for c2, _ in FORMS.values())
                ok &= (not all(1 <= x <= 16 for x in img)) or not as_form
    return ok

def R53():
    row = lambda s: [2 + 2 * s * j for j in range(4)]
    ev = [n for n in range(1, 17) if n % 2 == 0]
    return (row(1) == [2, 4, 6, 8] and row(2) == [2, 6, 10, 14] and [n + 8 for n in row(1)] == [10, 12, 14, 16]
            and sorted(row(2) + [4, 8, 12, 16]) == ev and 8 * 1 + 1 == 9 and 8 * 2 + 1 == 17)

def R54():
    return 11 - 3 == 8 and 11 % 2 == 3 % 2 == 1 and R7()

CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'[FR]\d+(_probe)?', k) and callable(v)}

if __name__ == '__main__':
    res = {}
    for k in sorted(CHECKS, key=lambda s: (s[0], int(re.match(r'[FR](\d+)', s).group(1)))):
        try: res[k] = bool(CHECKS[k]())
        except Exception as e: res[k] = f'error: {e!r}'
        print(k, res[k])
    json.dump(res, open(sys.argv[1] if len(sys.argv) > 1 else 'ccl_core_check_results.json', 'w'), indent=1)
