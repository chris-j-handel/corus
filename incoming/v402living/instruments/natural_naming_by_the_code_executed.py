"""Executes Exhibit ONE Natural Resolver's code, read from its living file, for three things Exhibit TWENTY Natural Naming's
sentences and droplets are of, deciding nothing.

Usage: python3 -I natural_naming_by_the_code_executed.py <repository root>

1. A self's one resolving of one sharing, by its prior and the parities surfacing: Natural Naming's table of a prior and of none.
2. Same and not same, by 14-next-possibling and by 12-next-co-same-existing: a 0 is by not same with the first and by same with the second.
3. Selves along, the last to the first, an odd number n of them: the first pattern of priors is its other one by moment 2n,
   and the first pattern again by moment 4n; and by moment 2n+1 it is the first pattern again too, a thing no living sentence has.
A recorded result, 15 November 2026, at the living files v402mgr: each line as this docstring has it.
"""
import glob, os, re, sys
ROOT = sys.argv[1]
one = sorted(glob.glob(os.path.join(ROOT, 'Exhibit_ONE_Natural_Resolver_v*.md')))[-1]
code = re.search(r"```python\n(.*?)```", open(one, encoding='utf-8').read(), re.S).group(1)
ns = {}
exec(compile(code, one, 'exec'), ns)
resolve, society = ns['_1_now_existing'], ns['_17_next_existing']
s = lambda v: {1: '+', -1: '-', 0: '0'}[v]
K = 'k'
print('living file:', os.path.basename(one))
print('1. a prior | surfacing -> 10-next-co-possibling, 11-next-co-existing')
for prior, obs in [(1, [1]), (1, [-1]), (1, [1, -1]), (1, []), (None, [1]), (None, [1, -1])]:
    ten, eleven = resolve([(K, prior)] if prior else [], [(K, x) for x in obs])
    ten, eleven = dict(ten), dict(eleven)
    print('  ', s(prior) if prior else 'none', '|', ' and '.join(s(x) for x in obs) or 'none', '->',
          s(ten[K]) if K in ten else 'none', ',', s(eleven[K]) if K in eleven else 'none')
print('2. same and not same')
for obs in ([1, 1], [1, -1]):
    ten, _ = resolve([], [(K, x) for x in obs])
    print('   14-next-possibling:', ' and '.join(s(x) for x in obs), 'surfacing', s(dict(ten)[K]))
for obs in ([1], [-1]):
    ten, _ = resolve([(K, 1)], [(K, x) for x in obs])
    print('   12-next-co-same-existing: a prior + and', s(obs[0]), 'surfacing, 10-next-co-possibling', s(dict(ten)[K]))
print('3. selves along, the last to the first')
for n in (3, 5, 7, 9):
    five = {(i, 9): (i + 1) % n for i in range(n)}
    first = tuple(-1 if i % 2 == 0 else 1 for i in range(n))
    soc = {i: ([(K, first[i])], []) for i in range(n)}
    again, other = [], []
    for m in range(1, 4 * n + 1):
        soc = society(soc, five)
        now = tuple(dict(soc[i][0])[K] for i in range(n))
        if now == first: again.append(m)
        if now == tuple(-x for x in first): other.append(m)
    print(f'   n={n}: the first pattern again by moments {again}; its other one by moments {other}')
