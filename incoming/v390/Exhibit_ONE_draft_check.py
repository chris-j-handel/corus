"""Checks the Exhibit ONE draft against Exhibit ONE v390, whole ranges, no sample."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = open(os.path.join(ROOT, 'incoming', 'v390', 'Exhibit_ONE_Natural_Resolver_draft.md'), encoding='utf-8').read()
O = open(os.path.join(ROOT, 'Exhibit_ONE_Natural_Resolver_v390.md'), encoding='utf-8').read()
A, B = {}, {}
exec(re.search(r'```python\n(.*?)```', O, re.S).group(1), A)
exec(re.search(r'```python\n(.*?)```', D, re.S).group(1), B)


def torus(one, step, p, q, m=60):
    soc = {(a, b): ([('k', -1 if (a + b) % 2 == 0 else 1)], []) for a in range(p) for b in range(q)}
    rel = {}
    for a in range(p):
        for b in range(q):
            rel[((a, b), 9)] = ((a + 1) % p, b)
            rel[((a, b), 10)] = (a, (b + 1) % q)
    rows = []
    for _ in range(m):
        rows.append(tuple(tuple(one(*soc[s])[0]) for s in sorted(soc)))
        soc = step(soc, rel)
    return rows


same = all(torus(A['_1_now'], A['_17_next_now'], p, q) == torus(B['_1_now_existing'], B['_17_next_existing'], p, q)
           for p in range(1, 8) for q in range(p, 10))
print('identical resolving, every torus 1x1 to 7x9:', same)
prose = re.sub(r'```.*?```', '', D, flags=re.S)
for word, pat in [('changing alone', r'(?<![\w-])changing\b(?!-)'), ('releas-', r'releas\w*'),
                  ('prioring', r'(?<![\w-])prioring'), ('society alone', r'(?<!same-existing-)\bsociety'),
                  ('at', r'(?<![\w-])at(?![\w-])'), ('beyond', r'beyond'), ('held', r'\bheld\b'),
                  ('in', r'(?<![\w-])in(?![\w-])')]:
    print(word, len(re.findall(pat, prose, re.I)))

import ast
def _body(t):
    m = ast.parse(t)
    m.body = [n for n in m.body if not (isinstance(n, ast.Expr) and isinstance(getattr(n, 'value', None), ast.Constant))]
    return m
names = {'_1_now': '_1_now_existing', '_17_next_now': '_17_next_existing'}
fa = [n.name for n in _body(re.search(r'```python\n(.*?)```', O, re.S).group(1)).body]
fb = [n.name for n in _body(re.search(r'```python\n(.*?)```', D, re.S).group(1)).body]
print('three functions, old and draft:', fa, fb)
widest = max(len(l) for l in re.search(r'```python\n(.*?)```', D, re.S).group(1).split('\n'))
print('widest code line:', widest)
