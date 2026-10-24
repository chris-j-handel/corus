"""Exhibit ONE's own resolver (written out by kits/Natural_Explaining_Passes_Kit/resolver_from_one.py), run as a pattern for the session's concepts.
Keys of a self's priors are now-existing things within its me (4-now-co-same-existing): read here as interests."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resolver import _17_next_existing, _1_now_existing
S = {1: '+', -1: '-', 0: '0', None: '.'}

def run(selves, edges, steps):
    soc = {s: (list(p.items()), []) for s, p in selves.items()}
    five = {(a, v): b for a, v, b in edges}
    hist = []
    for _ in range(steps):
        shares = {s: dict(_1_now_existing(*soc[s])[0]) for s in soc}
        res = _17_next_existing(soc, five)
        hist.append({s: (shares[s], dict(res[s][0])) for s in soc})
        soc = {s: (res[s][0], res[s][1]) for s in soc}
    return hist

def feed(prior, seq):
    p = list(prior.items()); out = []
    for rec in seq:
        sh, p = _1_now_existing(p, rec); out.append((dict(sh), dict(p)))
    return out

def show_run(title, selves, edges, steps=8):
    h = run(selves, edges, steps); print('==', title)
    for s in selves:
        for k in sorted({k for row in h for k in row[s][1]}):
            print('  self %s · %s · shares %s · prior %s' % (s, k, ' '.join(S.get(r[s][0].get(k), '.') for r in h), ' '.join(S.get(r[s][1].get(k), '.') for r in h)))

def show_feed(title, prior, seq):
    o = feed(prior, seq); print('==', title)
    for k in sorted({k for s, p in o for k in list(s) + list(p)}):
        print('  %s · shares %s · prior %s' % (k, ' '.join(S.get(s.get(k), '.') for s, p in o), ' '.join(S.get(p.get(k), '.') for s, p in o)))

if __name__ == '__main__':
    show_run('E1 a me alone, receiving nothing', {'a': {'x': -1}}, [])
    show_run('E2 a spiral of one, its own going along', {'a': {'x': -1}}, [('a', 9, 'a')])
    show_run('E3 me and you alike, both ways (co-bi-co-observing)', {'a': {'x': -1}, 'b': {'x': -1}}, [('a', 9, 'b'), ('b', 9, 'a')])
    show_run('E4 me and you one parity apart, both ways (parting aiming)', {'a': {'x': -1}, 'b': {'x': 1}}, [('a', 9, 'b'), ('b', 9, 'a')])
    show_run('E5 birth: you with no prior on x, me sharing one way', {'a': {'x': -1}, 'b': {}}, [('a', 9, 'b')])
    show_run('E6 one way only', {'a': {'x': -1}, 'b': {'x': -1}}, [('a', 9, 'b')])
    show_run('E7 two interests: x co-observed both ways, y the me\'s alone', {'a': {'x': -1, 'y': -1}, 'b': {'x': -1}}, [('a', 9, 'b'), ('b', 9, 'a')])
    show_feed('F1 receiving its own parity each momentary, then one inverse', {'x': -1}, [[('x', -1)]] * 6 + [[('x', 1)]] * 4)
    show_feed('F2 all other as one: three agreeing, then one parting', {'x': -1}, [[('x', 1)] * 3] * 2 + [[('x', 1), ('x', 1), ('x', -1)]] * 2)
    show_feed('F3 interest x receiving its own parity, interest y receiving nothing', {'x': -1, 'y': -1}, [[('x', -1)]] * 6)
    print('== G odd and even spirals (step 740)')
    for n in (5, 6):
        h = run({i: {'x': (-1 if i == 0 else 1)} for i in range(n)}, [(i, 9, (i + 1) % n) for i in range(n)], 4 * n + 1)
        rows = [''.join(S[r[i][0]['x']] for i in range(n)) for r in h]
        print('  n=%d · opening %s · again at momentary %s' % (n, rows[0], [t for t in range(1, len(rows)) if rows[t] == rows[0]]))
