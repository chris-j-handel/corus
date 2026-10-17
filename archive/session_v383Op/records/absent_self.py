"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/absent_self.py
"""
import itertools, random, collections
src = open('incoming/v383Op/two_lines.py').read().split("print('1  Spirals")[0]
exec(src)
def step(p, q, c, arr, hole=None):
    nxt = {s: {} for s in c}; kinds = {}; shared = {}
    for s in c:
        if s == hole: continue
        two = [arr[s].get('along', 0), arr[s].get('across', 0)]
        kinds[s] = kind(c[s], two)
        c[s], o = entry(c[s], two); shared[s] = o
        i, j = s
        nxt[((i + 1) % p, j)]['along'] = o
        nxt[(i, (j + 1) % q)]['across'] = o
    return nxt, kinds, shared
def run(p, q, seed, pre=40, post=60, hole=None):
    r = random.Random(seed)
    selves = [(i, j) for i in range(p) for j in range(q)]
    c = {s: r.choice((1, -1)) for s in selves}; arr = {s: {} for s in selves}
    for t in range(pre): arr, k, sh = step(p, q, c, arr)
    hist = []
    c2 = dict(c); arr2 = {s: dict(v) for s, v in arr.items()}
    for t in range(post):
        arr2, k, sh = step(p, q, c2, arr2, hole)
        hist.append((dict(c2), k, sh))
    return hist
for p, q in ((3, 3), (4, 5), (5, 5)):
    hole = (p // 2, q // 2)
    diff_by_t = collections.Counter(); still_max = 0; allreach = 0; N = 200; twice = collections.Counter(); kinds_h = collections.Counter(); kinds_i = collections.Counter()
    final_diff = []
    for seed in range(N):
        a = run(p, q, seed); b = run(p, q, seed, hole=hole)
        selves = [s for s in a[0][0] if s != hole]
        for t in range(60):
            d = sum(a[t][0][s] != b[t][0][s] for s in selves); diff_by_t[t] += d
        final_diff.append(sum(a[59][0][s] != b[59][0][s] for s in selves))
        # longest stillness at hole run, per self
        for s in selves:
            runl = 0
            for t in range(60):
                kinds_h[b[t][1][s]] += 1; kinds_i[a[t][1][s]] += 1
                if b[t][1][s] == '.': runl += 1; still_max = max(still_max, runl)
                else: runl = 0
        # sides offering nothing twice in sequence, intact vs hole: shared 0 twice in a row by a present self
        for s in selves:
            for t in range(59):
                if b[t][2][s] == 0 and b[t + 1][2][s] == 0: twice['hole run'] += 1
                if a[t][2][s] == 0 and a[t + 1][2][s] == 0: twice['intact'] += 1
    n = len(selves)
    print('torus %d by %d, the self at %s absent after a common prior, %d openings' % (p, q, hole, N))
    print('   selves of %d differing from the intact, on average, at momentaries 1,2,3,5,8,12,20,40,60:' % n, [round(diff_by_t[t - 1] / N, 1) for t in (1, 2, 3, 5, 8, 12, 20, 40, 60)])
    print('   at momentary 60: differing at none: %d openings; at every self: %d; least %d most %d' % (sum(d == 0 for d in final_diff), sum(d == n for d in final_diff), min(final_diff), max(final_diff)))
    print('   longest still possibling of a present self, momentaries in sequence:', still_max, '; a present self sharing 0 twice in sequence:', dict(twice))
    tot_h = sum(kinds_h.values()); tot_i = sum(kinds_i.values())
    print('   of each 1000 entries, with the hole:', {k: round(1000 * v / tot_h) for k, v in sorted(kinds_h.items())}, ' intact:', {k: round(1000 * v / tot_i) for k, v in sorted(kinds_i.items())})
