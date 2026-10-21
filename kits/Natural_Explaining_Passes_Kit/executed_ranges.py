"""executed_ranges.py NATURAL_INTELLIGENCE_FILE
Executes Exhibit ONE's code, as Natural Intelligence carries it, at ranges wider than its tables' rows,
and prints each rule beside its executing: True where every case in the range agrees with the rule.
1. A torus of selves, p along and q across, p from 1 to P and q from p to Q: both odd, p the smaller,
   again at q from momentary 3p - 1 when q is more than twice p, and at 4p from 3p - 3 at each other q;
   either number even, at 2, from the first; a torus 1 by 1, the spiral of one, left out.
2. Two spirals crossed at self 1 of each, two different numbers of selves:
   again at 2, from momentary 4m when both odd and n less than twice m, from 2n + 1 when n more,
   from twice the odd number and 1 when one number is even, and from the first when both are even.
3. 0 in sequence: at random societies, none offered from beyond selves, a self shares 0 at no more
   momentaries in sequence than selves sharing or releasing to it."""
import re, sys, random

src = open(sys.argv[1], encoding='utf-8').read()
ns = {}
exec(re.search(r'```python\n(.*?)```', src, re.S).group(1), ns)
one = next(v for k, v in ns.items() if k.startswith('_1_') and callable(v))     # 1, by its number, any naming
step = next(v for k, v in ns.items() if k.startswith('_17_') and callable(v))


def period(outs):
    M = len(outs)
    for T in range(1, M // 3):
        for start in range(0, M - 2 * T):
            if all(outs[i] == outs[i + T] for i in range(start, M - T)):
                return T, start + 1
    return None, None


def torus(p, q, M):
    soc = {(a, b): ([('k', -1 if (a + b) % 2 == 0 else 1)], []) for a in range(p) for b in range(q)}
    rel = {}
    for a in range(p):
        for b in range(q):
            rel[((a, b), 9)] = ((a + 1) % p, b)
            rel[((a, b), 10)] = (a, (b + 1) % q)
    outs = []
    for _ in range(M):
        outs.append(tuple(tuple(one(*soc[s])[0]) for s in sorted(soc)))
        soc = step(soc, rel)
    return outs


def torus_rule(p, q):
    if p % 2 == 0 or q % 2 == 0:
        return 2, 1
    return (q, 3 * p - 1) if q > 2 * p else (4 * p, 3 * p - 3)


def crossed(a, b, M):
    soc, rel = {}, {}
    for sp, n in ((0, a), (1, b)):
        for i in range(n):
            soc[(sp, i)] = ([('k', -1 if i % 2 == 0 else 1)], [])
            rel[((sp, i), 9)] = (sp, (i + 1) % n)
    rel[((0, 0), 10)] = (1, 0)
    rel[((1, 0), 10)] = (0, 0)
    outs = []
    for _ in range(M):
        outs.append(tuple(tuple(one(*soc[s])[0]) for s in sorted(soc)))
        soc = step(soc, rel)
    return outs


def crossed_rule(a, b):
    m, n = min(a, b), max(a, b)
    if m % 2 == 0 and n % 2 == 0:
        return 2, 1
    if m % 2 == 0 or n % 2 == 0:
        return 2, 2 * (n if n % 2 else m) + 1
    return (2, 4 * m) if n < 2 * m else (2, 2 * n + 1)


P, Q = 15, 21
bad = [(p, q) for p in range(1, P + 1) for q in range(p, Q + 1) if (p, q) != (1, 1)
       and period(torus(p, q, max(12 * q, 8 * p) + 40)) != torus_rule(p, q)]
print(f'torus of selves, p 1 to {P}, q p to {Q}:', not bad, bad[:5])

bad = [(a, b) for a in range(2, 16) for b in range(a + 1, 32)
       if crossed_rule(a, b) and period(crossed(a, b, 6 * b + 60)) != crossed_rule(a, b)]
print('two spirals crossed, 2 to 15 and the larger to 31:', not bad, bad[:5])

R = random.Random(390)
ok = True
for trial in range(2000):
    n = R.randint(2, 8)
    soc = {s: ([('k', R.choice([1, -1]))], []) for s in range(n)}
    rel = {(s, name): R.randrange(n) for s in range(n) for name in (6, 10, 9) if R.random() < .5}
    into = {s: len({src for (src, _), t in rel.items() if t == s}) for s in range(n)}
    run = {s: 0 for s in range(n)}
    for _ in range(40):
        for s in range(n):
            ten = dict(one(*soc[s])[0])
            run[s] = run[s] + 1 if ten.get('k') == 0 else 0
            if run[s] > into[s]:
                ok = False
        soc = step(soc, rel)
print('0 in sequence, 2,000 random societies of 2 to 8 selves, 40 momentaries:', ok)
