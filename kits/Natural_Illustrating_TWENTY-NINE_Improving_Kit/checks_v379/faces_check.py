"""The faces of Natural Illustrating Part TWO and 4.2 executed again at Exhibit ONE's code, and compared with the
file's sayings: the table at 10 cell for cell, the lone self, the still from beside, two selves at 0, the spiral of five
and the torus of three by five; the sixteen ways are enumerated here, at no execution of the code. A check is a coupling partner and no authority: it says
where a saying and the code agree or part, and decides nothing. Run from the repository root:
    python3 kits/Natural_Illustrating_TWENTY-NINE_Improving_Kit/checks_v379/faces_check.py
"""
import re, glob, sys
from itertools import product

src = open(sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]).read()
code = re.search(r'```python\n(.*?)```', src, re.S).group(1)
ns = {}; exec(code, ns)
one, seventeen = ns['_1_co_bi_offering'], ns['_17_tri_co_offering']
agree = []

def say(name, ok, detail=''):
    agree.append(ok); print(('  agrees  ' if ok else '  PARTS   ') + name + ('' if not detail else ': ' + detail))

# 1. The table at 10, 2.4: three cells at is not, eight at is, one empty, as the file's table writes them
expect = {(None, 'none'): (None, None), (None, '+'): (1, 1), (None, '-'): (-1, -1), (None, '0'): (0, None),
          (1, 'none'): (-1, -1), (1, '+'): (0, 1), (1, '-'): (-1, -1), (1, '0'): (-1, -1),
          (-1, 'none'): (1, 1), (-1, '+'): (1, 1), (-1, '-'): (0, -1), (-1, '0'): (1, 1)}
offer = {'none': [], '+': [('s', 1)], '-': [('s', -1)], '0': [('s', 1), ('s', -1)]}
ok = True
for (prior, now), (e10, e11) in expect.items():
    ten, eleven = one([] if prior is None else [('s', prior)], offer[now])
    if (dict(ten).get('s'), dict(eleven).get('s')) != (e10, e11): ok = False
say('the table at 10, twelve cells', ok)

# 2. One self, 2.5
c, o, t = [], [('s', 1)], []
for _ in range(8): ten, c = one(c, o); t.append(dict(ten)['s']); o = []
say('one self offered + once, + - + - at 10', t == [1, -1] * 4)
c, t = [], []
for _ in range(6): ten, c = one(c, [('s', 1)]); t.append(dict(ten)['s'])
say('one self offered + at each momentary, + then 0', t == [1, 0, 0, 0, 0, 0])

# 3. Two selves joined across both ways, both offered + once, 2.5
def run(society, joins, n):
    out10 = {s: [] for s in society}
    for _ in range(n):
        out = seventeen(society, joins)
        for s in society:
            ten, _e = one(society[s][0], society[s][1]); out10[s].append(dict(ten).get('s'))
        society = {s: (out[s][0], [('s', v) for (_k, v) in out[s][1]]) for s in out}
    return out10
r = run({'A': ([], [('s', 1)]), 'B': ([], [('s', 1)])}, {('A', 10): 'B', ('B', 10): 'A'}, 8)
say('two selves at 0, + 0 - 0 at both', r['A'] == [1, 0, -1, 0] * 2 and r['B'] == [1, 0, -1, 0] * 2)

# 4. The sixteen ways, 2.2, enumerated here and not at Exhibit ONE's code: fifteen with a form still or the prior lost, one cycling all four
forms = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
living = 0; stopped = 0
for bits in product((1, -1), repeat=4):
    way = dict(zip([(1, 1), (1, -1), (-1, 1), (-1, -1)], bits))
    still = any(way[f] == f[1] and f[0] == f[1] for f in forms)
    whole = all(way[(1, n)] != way[(-1, n)] for n in (1, -1))   # the prior carried at both values of now
    cur, path = (1, 1), [(1, 1)]
    for _ in range(6):
        cur = (cur[1], way[cur])
        if cur in path: break
        path.append(cur)
    if not still and whole and len(path) == 4: living += 1
    else: stopped += 1
say('the sixteen ways, one living step and fifteen stopping', (living, stopped) == (1, 15), f'{living} and {stopped}')

# 5. The spiral of five, 4.2: the 0 one self on at each second momentary, parities again at 20
selves = [1, 2, 3, 4, 5]; joins = {(s, 9): selves[i % 5] for i, s in enumerate(selves, start=1)}
r = run({s: ([], [('s', 1)] if s == 1 else []) for s in selves}, joins, 40)
zeros = [(s, m + 1) for s in selves for m, v in enumerate(r[s]) if v == 0]
first = sorted(zeros, key=lambda z: z[1])[:5]
say('the spiral of five, the 0 at selves 1 to 5 at momentaries 6, 8, 10, 12, 14', first == [(1, 6), (2, 8), (3, 10), (4, 12), (5, 14)], str(first))
say('the spiral of five, parities again at 20 from momentary 5', len(selves) == 5 and all(len(r[s]) >= 34 for s in selves) and all(r[s][4:14] == r[s][24:34] for s in selves))

# 6. The torus of three by five, 4.2: parities again at 12
p, q = 3, 5; selves = [(i, j) for i in range(p) for j in range(q)]
joins = {}
for (i, j) in selves: joins[((i, j), 9)] = ((i + 1) % p, j); joins[((i, j), 10)] = (i, (j + 1) % q)
r = run({s: ([], [('s', 1)] if s == (0, 0) else []) for s in selves}, joins, 40)
say('the torus of three by five, parities again at 12', all(r[s][12:24] == r[s][24:36] for s in selves))

print('\n' + ('each saying agrees with the code' if all(agree) else 'a saying parts from the code: met at the carrying'))
sys.exit(0 if all(agree) else 1)
