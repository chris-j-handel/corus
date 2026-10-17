"""Session v382F: the Co-Chaining Logic Registry's spiral and torus claims executed at Exhibit ONE's resolver.

Runs from the repository root: python3 incoming/v382F/thirty_at_the_resolver.py
Reads the newest Exhibit ONE at the root, executes its python block, and works the Registry's numeric
claims about spirals, crossed spirals and tori (steps at its lines 1055, 1063, 1075, 1107, 2656, 2668,
2760, 2766, 2910 at v380L), printing each claim and the resolver's own answer. Openings as Exhibit ONE
opens them: each self at a parity, self 1 at −, alternating along (and across at a torus), none offered
from beyond. Counting: 'at momentary t' is the carrying arriving at 3 at the t-th entry, and 'again at d'
is the least d at which each self's carrying and offerings are as they were d momentaries before.
"""
import glob, itertools, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
code = re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1)
ns = {}
exec(code, ns)
_1, _17 = ns['_1_co_bi_tri_offering'], ns['_17_co_bi_tri_offering']
S = {1: '+', -1: '−', 0: '0'}


def period(soc, comp, M, skip):
    forms = []
    for _ in range(M):
        out = _17(soc, comp)
        soc = {s: (out[s][0], out[s][1]) for s in soc}
        forms.append(tuple((tuple(sorted(soc[s][0])), tuple(sorted(soc[s][1]))) for s in soc))
    for d in range(1, M // 2):
        if all(forms[m] == forms[m + d] for m in range(skip, M - d)):
            return d


def spiral(pattern, M=400):
    n = len(pattern)
    return period({i: ([('s', pattern[i])], []) for i in range(n)}, {(i, 9): (i + 1) % n for i in range(n)}, M, 2)


def k_rule(pattern):
    n = len(pattern)
    for k in range(1, 4 * n + 5):
        if tuple(pattern[(i - k) % n] * (-1) ** k for i in range(n)) == tuple(pattern):
            return k


def torus(p, q, M=300):
    sel = [(i, j) for i in range(p) for j in range(q)]
    soc = {s: ([('s', -1 if (s[0] + s[1]) % 2 == 0 else 1)], []) for s in sel}
    comp = {}
    for (i, j) in sel:
        comp[((i, j), 9)] = ((i + 1) % p, j)
        comp[((i, j), 10)] = (i, (j + 1) % q)
    return period(soc, comp, M, 60)


def crossed(m, n, M=200):
    A = [('a', i) for i in range(m)]
    B = [('b', i) for i in range(n)]
    soc = {s: ([('s', -1 if s[1] % 2 == 0 else 1)], []) for s in A + B}
    comp = {}
    for i in range(m):
        comp[(('a', i), 9)] = ('a', (i + 1) % m)
    for i in range(n):
        comp[(('b', i), 9)] = ('b', (i + 1) % n)
    comp[(('a', 0), 10)] = ('b', 0)
    comp[(('b', 0), 10)] = ('a', 0)
    alike_to, zero_at, forms = 0, None, []
    for t in range(1, M + 1):
        ca, cb = soc[('a', 0)][0][0][1], soc[('b', 0)][0][0][1]
        if ca == cb:
            alike_to = t
        ta, _ = _1(soc[('a', 0)][0], soc[('a', 0)][1])
        if zero_at is None and t > 2 and ta[0][1] == 0:
            zero_at = t
        out = _17(soc, comp)
        soc = {s: (out[s][0], out[s][1]) for s in soc}
        forms.append(tuple((tuple(sorted(soc[s][0])), tuple(sorted(soc[s][1]))) for s in soc))
    again_from = next(t0 + 1 for t0 in range(M - 10) if all(forms[t] == forms[t + 2] for t in range(t0, M - 2)))
    return alike_to, zero_at, again_from


print('Exhibit ONE read at', exhibit_one)
print('1055  three selves all alike again at 4:', spiral((-1, -1, -1)))
print('1055  nine selves, each pattern, again at 4, 12 or 36:', sorted({spiral(p) for p in itertools.product((1, -1), repeat=9)}))
bad = [(p, spiral(p), k_rule(p)) for n in range(2, 8) for p in itertools.product((1, -1), repeat=n) if spiral(p) != 2 * k_rule(p)]
print('2668  step 233, again at 2k at each pattern of 2 to 7 selves: partings', bad or 'none')
print('2668  one self at the other parity, odd n, again at 4n:', {n: spiral(tuple([1] + [-1] * (n - 1))) for n in (3, 5, 7)})
print('2668  one self at the other parity, even n, again at 2n:', {n: spiral(tuple([1] + [-1] * (n - 1))) for n in (4, 6)})
print('1063  even spiral alternating again at 2:', {n: spiral(tuple(-1 if i % 2 == 0 else 1 for i in range(n))) for n in (2, 4, 6)})
soc, ch = {0: ([('s', -1)], [])}, []
for _ in range(8):
    out = _17(soc, {(0, 9): 0})
    soc = {0: (out[0][0], out[0][1])}
    ch.append(S[soc[0][0][0][1]])
print('2656  a spiral of one chains two momentaries at a time:', ', '.join(ch))
rows = {(1, 3): 3, (2, 3): 2, (1, 5): 5, (3, 3): 12, (3, 5): 12, (3, 7): 7, (3, 13): 13, (5, 7): 20, (5, 11): 11, (7, 17): 17}
print('1107  the torus at each of Exhibit ONE\'s rows, executed and the table:', {pq: (torus(*pq), rows[pq]) for pq in rows})
print('1107  q at q more than twice p, 4p at a q less, at the odd rows:', all(rows[(p, q)] == (q if q > 2 * p else 4 * p) for (p, q) in rows if p % 2 and q % 2 and p > 1))
print('660   two odd spirals crossed, m the lesser: alike to 2m + 1, the lesser\'s crossing self at 0 at it, again at 2 from 4m at n less than twice m and from 2n + 1 at n more:')
for (m, n), again in {(3, 5): 12, (5, 7): 20, (7, 11): 28, (11, 13): 44, (13, 17): 52, (9, 15): 36, (2, 3): 7}.items():
    alike_to, zero_at, again_from = crossed(m, n)
    said = (4 * m if n < 2 * m else 2 * n + 1) if m % 2 else 2 * n + 1
    print(f'      {m}·{n}: alike to {alike_to} (2m + 1 = {2 * m + 1}), the lesser\'s 0 at {zero_at}, again at 2 from {again_from} (the step says {said}, Exhibit ONE\'s table {again})')
