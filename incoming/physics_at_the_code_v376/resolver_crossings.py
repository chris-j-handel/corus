"""Exhibit ONE's own society, executed as a chain of selves and as one crossing, two in and two out.

Explored at v376 for the physics observings report's open question, in its words: "does the proposed
NI relation determine the differing observed distributions under their stated conditions, or has the
working only recognized compatible forms?" Each self carries one
sharing 'c' at +1 or -1; each self's offerings reach the two selves either side of it along the chain (connectors
6 and 10); connector 9 is unjoined, a society at one scale. The code is read from Exhibit ONE whole and nothing in it is changed.

Usage: python3 incoming/physics_at_the_code_v376/resolver_crossings.py   (from the repository root)
"""
import re, glob
one = max(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))
code = re.search(r"```python\n(.*?)```", open(one, encoding='utf-8').read(), re.S).group(1)
ns = {}; exec(code, ns)
society = ns['_17_tri_co_offering']
SYM = {1: '+', -1: '-', 0: '0', None: '.'}

def links(pairs):
    r = {}
    for a, b in pairs:
        r[(a, 10)] = b; r[(b, 6)] = a
    return r

def chain(nodes):
    return list(zip(nodes, nodes[1:]))

def run(carry, reach_at, rows, momentaries=10):
    """carry: {self: {'c': sign}}; reach_at(t): the joins at momentary t; rows: [(label, [selves])]"""
    offers = {i: [] for i in carry}
    for t in range(momentaries):
        out = society({i: (list(carry[i].items()), offers[i]) for i in carry}, reach_at(t))
        carry = {i: dict(out[i][0]) for i in carry}; offers = {i: out[i][1] for i in carry}
        print(f'  {t:2d}  ' + '   '.join(f'{lab} ' + ''.join(SYM[carry[i].get("c")] for i in sel)
                                        for lab, sel in rows(t)))

print('1. A chain of 9 selves, + at one end and - at the other, the middle empty')
N = 9; c = {i: {} for i in range(N)}; c[0] = {'c': 1}; c[N - 1] = {'c': -1}
run(c, lambda t: links(chain(range(N))), lambda t: [('', range(N))])

print('\n2. A chain of 8 selves, + at one end and - at the other')
N = 8; c = {i: {} for i in range(N)}; c[0] = {'c': 1}; c[N - 1] = {'c': -1}
run(c, lambda t: links(chain(range(N))), lambda t: [('', range(N))])

print('\n3. A chain of 8 selves, + at both ends')
c = {i: {} for i in range(N)}; c[0] = {'c': 1}; c[N - 1] = {'c': 1}
run(c, lambda t: links(chain(range(N))), lambda t: [('', range(N))])

A, B = list(range(8)), list(range(8, 16))
before = links(chain(A) + chain(B))
after = links(chain(A[:4] + B[4:]) + chain(B[:4] + A[4:]))
def crossing(phase):
    c = {i: {'c': 1 if k % 2 == 0 else -1} for k, i in enumerate(A)}
    c.update({i: {'c': (1 if k % 2 == 0 else -1) * phase} for k, i in enumerate(B)})
    run(c, lambda t: before if t < 5 else after,
        lambda t: [('A', A), ('B', B)] if t < 5 else [('A0-3 B4-7', A[:4] + B[4:]), ('B0-3 A4-7', B[:4] + A[4:])])
print('\n4. One crossing: two whole chains A and B; at momentary 5 the joins 3-4 and 11-12 end and 3-12 and 11-4 arrive; A and B in phase')
crossing(1)
print('\n5. The same crossing, A and B out of phase')
crossing(-1)

print('\n6. The out-of-phase crossing carried on to sixty momentaries: the last three')
c = {i: {'c': 1 if k % 2 == 0 else -1} for k, i in enumerate(A)}
c.update({i: {'c': -1 if k % 2 == 0 else 1} for k, i in enumerate(B)})
offers = {i: [] for i in c}
for t in range(60):
    out = society({i: (list(c[i].items()), offers[i]) for i in c}, before if t < 5 else after)
    c = {i: dict(out[i][0]) for i in c}; offers = {i: out[i][1] for i in c}
    if t >= 57:
        print(f'  {t:2d}  A0-3 B4-7 ' + ''.join(SYM[c[i]['c']] for i in A[:4] + B[4:]) +
              '   B0-3 A4-7 ' + ''.join(SYM[c[i]['c']] for i in B[:4] + A[4:]))

print('\n7. A chain of 9 selves, + at both ends, the other end formed one momentary after the first')
N = 9; c = {i: {} for i in range(N)}; c[0] = {'c': 1}
offers = {i: [] for i in c}; J = links(chain(range(N)))
for t in range(10):
    if t == 1: c[N - 1] = {'c': 1}
    out = society({i: (list(c[i].items()), offers[i]) for i in c}, J)
    c = {i: dict(out[i][0]) for i in c}; offers = {i: out[i][1] for i in c}
    print(f'  {t:2d}  ' + ''.join(SYM[c[i].get('c')] for i in range(N)))
