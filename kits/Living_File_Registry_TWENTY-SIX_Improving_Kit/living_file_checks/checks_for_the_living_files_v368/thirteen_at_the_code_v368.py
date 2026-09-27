"""thirteen_at_the_code_v368.py · the claims of Exhibit THIRTEEN Resolving Hard Problems v368, run at
Exhibit ONE Natural Resolver's own code and at the numbers they name, and the exhibit's own text checked
at each improved part. Run from a folder holding Exhibit_ONE_Natural_Resolver_v368.md and parts/.
Each line returns MET or PARTS."""
import itertools, os, re
from fractions import Fraction as Fr
ONE = open('Exhibit_ONE_Natural_Resolver_v368.md', encoding='utf-8').read()
CODE = ONE.split('```python\n')[1].split('```')[0]
ns = {}; exec(CODE, ns)
couple = ns['_1_self_coupling']
R = []
def check(label, ok): R.append(bool(ok)); print(('MET   ' if ok else 'PARTS ') + label)

# 1.5 · the exclusive or
fns = list(itertools.product((0, 1), repeat=4))           # outputs at 00, 01, 10, 11
idx = {(a, b): 2 * a + b for a in (0, 1) for b in (0, 1)}
def flips_each(f):
    return all(f[idx[(a, b)]] != f[idx[(1 - a, b)]] and f[idx[(a, b)]] != f[idx[(a, 1 - b)]] for a in (0, 1) for b in (0, 1))
ch = [f for f in fns if flips_each(f)]
check('of the sixteen ways two signs can be answered, exactly two change at each single change: exclusive or and its complement',
      sorted(ch) == sorted([(0, 1, 1, 0), (1, 0, 0, 1)]))
def run(a, b, n=9):
    s = [a, b]
    while len(s) < n: s.append(s[-1] ^ s[-2])
    return ''.join(map(str, s))
step = [0]
for _ in range(7): step.append(step[-1] ^ 1)
check('taken as the step, the exclusive or runs 0101 and returns what it met at each second step', ''.join(map(str, step)) == '01010101')
check('taken of the prior and the now, it runs 011, 101 or 110 from each start but nothing, returning after three',
      {run(a, b)[:3] for a, b in [(0, 1), (1, 0), (1, 1)]} == {'011', '101', '110'} and run(0, 0) == '0' * 9
      and all(run(a, b)[i] == run(a, b)[i + 3] for a, b in [(0, 1), (1, 0), (1, 1)] for i in range(6)))
# the Peres–Mermin square: rows parity 0, columns parity 0, 0, 1
sols = [v for v in itertools.product((0, 1), repeat=9)
        if all(sum(v[3 * r:3 * r + 3]) % 2 == 0 for r in range(3)) and [sum(v[c::3]) % 2 for c in range(3)] == [0, 0, 1]]
check('six exclusive-or constraints on nine signs, rows 0 and columns 0, 0, 1: none of the 512 meets them all', len(sols) == 0 and 2 ** 9 == 512)

# 2.2 and part 5 · the four-cycles, 8 up and 17 less
up, less17, less9 = (lambda n: n + 8 if n <= 8 else n - 8), (lambda n: 17 - n), (lambda n: 9 - n)
cyc = {}
for a in (1, 2, 3, 4):
    c, x = [], a
    for k in range(4): c.append(x); x = up(x) if k % 2 == 0 else less17(x)
    cyc[a] = c
check('alternating 8 up with 17 less runs 1-9-8-16, 2-10-7-15, 3-11-6-14 and 4-12-5-13',
      [cyc[a] for a in (1, 2, 3, 4)] == [[1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]])
par = lambda n: n % 2
check('round each four-cycle the parity is kept at 8 up and changes at 17 less, exactly twice',
      all(sum(par(c[i]) != par(c[(i + 1) % 4]) for i in range(4)) == 2
          and all(par(c[i]) == par(c[i + 1]) for i in (0, 2)) for c in cyc.values()))
check('9 less within 1 to 8 pairs 1 with 8, 2 with 7, 3 with 6, 4 with 5, the two faces at once',
      [(a, less9(a)) for a in (1, 2, 3, 4)] == [(1, 8), (2, 7), (3, 6), (4, 5)] and all(less9(a) == less17(up(a)) for a in range(1, 9)))

# 2.3 and part 4 · the carry's bound at the code
check("the code continues each carrying to 3, and to 4 at positive 8-other-torusing",
      '_16_social_torusing + 1 <= 3 or (_16_social_torusing + 1 == 4 and _8_other_torusing > 0)' in CODE)
def one_entry(c, t, h, offers):
    carrying = [(0, c, t, h)]
    surf, nxt = couple(carrying, [(0, x) for x in offers])
    return dict(surf).get(0, 0), {k: (cc, tt, hh) for k, cc, tt, hh in nxt}.get(0)
check('a nonzero surface at each carrying under empty receiving: the return is +1, −1 or 0 and never a fourth',
      all(one_entry(c, t, h, off)[0] in (-1, 0, 1) for c in (1, -1) for t in (1, -1) for h in range(4)
          for off in ([], [1], [-1], [1, -1], [1, 1])))

check('12-other-surplusing takes +1 at each positive sign and −1 at each negative, of any magnitude',
      all(one_entry(c, t, 0, [m])[0] == one_entry(c, t, 0, [(m > 0) - (m < 0)])[0] for c in (1, -1) for t in (1, -1) for m in (5, -7, 2, -1)))

# 2.5 · the ten, three momentaries long, five places from two faces
self5, other5 = list(range(1, 6)), list(range(2, 7))
check('the self 1–5 and the other 2–6 span 1 to 6, three momentaries 1–2, 3–4, 5–6', sorted(set(self5 + other5)) == list(range(1, 7)))
places = [n for n in range(2, 7) if n in self5 and n in other5 or n == 6]
check('five places at 2 to 6, where at each number one side completes and the other opens', places == [2, 3, 4, 5, 6])
check('the openings 1+3+5 = 9 = 3² and the completings 2+4+6 = 12 = 3·4, and 3² − 2·4 = 1',
      1 + 3 + 5 == 9 == 3 ** 2 and 2 + 4 + 6 == 12 == 3 * 4 and 3 ** 2 - 2 * 4 == 1)

# 2.5 and 5.4 · φ, the rate named at no value
fib = [1, 1]
while len(fib) < 16: fib.append(fib[-1] + fib[-2])
phi = (1 + 5 ** 0.5) / 2
sides = [Fr(fib[i + 1], fib[i]) > phi for i in range(1, 14)]
check('the ratios of neighbouring terms alternate above and below φ, side changing at each next', all(sides[i] != sides[i + 1] for i in range(len(sides) - 1)))

# 3.1 and 3.8 · the primes
pr = [p for p in range(2, 60) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
check('the primes 2 to 59 are 17, with 16 openings between them, and 118 is 2 selves of 59', len(pr) == 17 and pr[-1] == 59 and len(pr) - 1 == 16 and 2 * 59 == 118)

# part 5 · the pairs as momentaries, the crossings, and the slightest tipping
# Exhibit ONE Natural Resolver's pairs, each round the other way, and the crossings
import re
part = {}
for line in ONE.split('\n'):
    m = re.match(r'\| four-cycle (\d+)-(\d+)-(\d+)-(\d+) \|.*?\| (?:four-cycle ([\d-]+), round the other way|—) \| (?:four-cycle ([\d-]+), round the other way|four-cycle [\d-]+, itself|—) \|', line)
    if m:
        row = int(m.group(1)); part[row] = (m.group(5), m.group(6) if m.group(6) else ('itself' if 'itself' in line.split('|')[-2] else None))
rowof = {'1-9-8-16': 1, '2-15-7-10': 2, '3-11-6-14': 3, '4-13-5-12': 4}
odd = {r: rowof.get(v[0]) for r, v in part.items()}; even = {r: (rowof.get(v[1]) if v[1] not in ('itself', None) else v[1]) for r, v in part.items()}
check('the four row cycles pair as overlapping momentaries: odd 1–2 and 3–4, even 2–3 and 4 with itself, each round the other way',
      odd == {1: 2, 2: 1, 3: 4, 4: 3} and even == {1: None, 2: 3, 3: 2, 4: 'itself'} and ONE.count('round the other way') >= 8)
check('the crossings 6 and 14 share row 3 with carrying and chaining, and the forms through them partner themselves at the even momentary',
      '| four-cycle 3-11-6-14 | 3-self-carrying · 11-other-chaining · 6-other-crossing · 14-social-crossing' in ONE
      and 'middle four-cycle 7-11-6-10, itself' in ONE and 'eight-cycle 2-15-7-11-3-14-6-10, itself' in ONE)

# the slightest tipping, in a ring of selves
releasing = ns['_9_other_releasing']
def ring(n, steps):
    carry = [[] for _ in range(n)]; offer = [[] for _ in range(n)]; offer[0] = [(0, 1)]; rows = []
    for _ in range(steps):
        surf = []
        for i in range(n):
            out, carry[i] = couple(carry[i], offer[i]); surf.append(dict(out).get(0))
        offer = [[] for _ in range(n)]
        for i in range(n):
            if surf[i] is not None: offer[(i + 1) % n] += releasing([(0, surf[i])], {0: 0})
        rows.append(tuple(surf))
    return rows
def period(rows, start=60):
    for p_ in range(1, 200):
        if all(rows[t] == rows[t + p_] for t in range(start, start + 2 * p_)): return p_
per = {n: period(ring(n, 500)) for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17)}
check('one +1 offered once at one self: the ring of 1 runs +, 0, −, 0 and round', ring(1, 4) == [(1,), (0,), (-1,), (0,)])
check('even rings return at 2 couplings, each self changing at each coupling; odd rings at 4 × n', all(per[n] == (2 if n % 2 == 0 else 4 * n) for n in per if n > 1))
r5 = ring(5, 16); zeros = [(t + 1, r.index(0)) for t, r in enumerate(r5) if 0 in r]
check('in a ring of five the meeting travels one self each two couplings, one momentary', zeros[:5] == [(6, 0), (8, 1), (10, 2), (12, 3), (14, 4)])


# the exhibit's own text, at each improved part
TEN = ['an arriving named from behind', 'an opening named as a place', 'a bound named as a last', 'a carry named as a store',
       'a middle named as an end', 'a sign named as a magnitude', 'a sequencing named to one beat', 'a rate named as a value',
       'a two-way named to one side', 'a membrane named as a cut']
RELEASED = [r'\bhold\w*', r'\bheld\b', r'\bland\w*', r'\bturn\w*', r'\bevery\w*', r'\bstand(?!ard)\w*', r'disequilib\w*',
            r'at no self', r'at no seat', r'odd-even', r'even-odd', r'equal length', r'\bdiscovery\b', r'\btechnolog\w*',
            r'\bbounding\b', r'self-bound\w*', r'swimmer', r'flip', r'Smolin', r'Duhem', r'Quine',
            r'one stable form', r'\bread\w*', r'\bunread\w*', r'\bstable forms?\b(?! (?:is not possible|of existing))', r'\breadings\b']
ALLOWED_LIVING = ['non-living scale', 'living intelligence']
PARTS = {}
if os.path.isdir('parts'):
    PARTS = {n: open(f'parts/v368_{n}.md', encoding='utf-8').read() for n in range(1, 8) if os.path.exists(f'parts/v368_{n}.md')}
elif os.path.exists('Exhibit_THIRTEEN_Resolving_Hard_Problems_v368.md'):   # beside the living files: the parts from the exhibit itself
    _x = open('Exhibit_THIRTEEN_Resolving_Hard_Problems_v368.md', encoding='utf-8').read().split('\n---\n', 2)[2]
    for _p in re.split(r'\n(?=# \d )', '\n' + _x):
        if _p.strip().startswith('# '): PARTS[int(_p.strip()[2])] = _p.strip('\n') + '\n'
improved = sorted(PARTS)
for n in improved:
    t = PARTS[n]
    found = []
    for r in RELEASED:
        for m in re.finditer(r, t, re.I if r[0] != 'S' else 0):
            ctx = t[max(0, m.start() - 20): m.end() + 40]
            if r.startswith(r'\bstable') and ('named as a stable form' in ctx or 'names one face as a stable form' in ctx or 'as a stable form' in ctx):
                continue
            found.append(m.group(0))
    liv = [m for m in re.finditer(r'\bliving\b', t) if not any(t[m.start() - 4: m.end() + 14].find(a) >= 0 or t[m.start(): m.end() + 13] == a for a in ALLOWED_LIVING)]
    liv = [m for m in liv if 'non-living' not in t[m.start() - 4: m.end()] and 'living intelligence' not in t[m.start(): m.end() + 13]]
    check(f'part {n}: no released word' + (f' ({", ".join(sorted(set(found + [m.group(0) for m in liv])))})' if found or liv else ''), not found and not liv)
    other = re.findall(r'Exhibit [A-Z-]+|\b(?:TWO|THREE|TWENTY(?:-[A-Z]+)?|ONE)\b|Natural Intelligence|Registry|Living Improving', t)
    check(f'part {n}: names no other file, as published' + (f' ({sorted(set(other))})' if other else ''), not other)
    old = re.findall(r'an? [a-z-]+ held (?:as|from|to) [a-z ]+?(?=[.,:;*]|$)', t, re.M)
    check(f'part {n}: the ten by the names they carry at TWENTY-EIGHT' + (f' ({old[:3]})' if old else ''), not old)
    tens = [w for w in TEN if w in t.lower()]
    if n in (2, 7):
        u = t[t.index('| the running |'):] if n == 7 else t
        pos = [u.lower().index(w) for w in TEN]
        check(f'part {n}: the ten are listed in TWENTY-EIGHT\'s order, 1 to 10', pos == sorted(pos))
    if n == 5:
        check('part 5: each of the ten is met at its pair, once as a lead', all(t.count(f'**{k} · {w[0].upper() + w[1:]}.**') == 1 for k, w in enumerate(TEN, 1)))
    nums = re.findall(r'\b(\d+) · (an? [a-z-]+ named [a-z ]+?)(?=[.,|*]| and |$)', t, re.M)
    check(f'part {n}: each numbered way carries its own number', all(w.lower().strip().startswith(TEN[int(k) - 1]) for k, w in nums))
if os.path.exists('Exhibit_THIRTEEN_Resolving_Hard_Problems_v368.md'):
    X = open('Exhibit_THIRTEEN_Resolving_Hard_Problems_v368.md', encoding='utf-8').read()
    top = X.split('\n---\n')[1]
    check('the exhibit opens with its title and subtitle and a floating contents of its bold concepts',
          X.startswith('Exhibit THIRTEEN Resolving Hard Problems v368') and '**1 Binarying**' in top and '\n- ' in top)
    first = X.split('## 1.1 Two binaries, and no third\n\n', 1)[1].split('\n')[0]
    check('the exhibit opens from inside its title and subtitle', first.startswith('**Resolving a hard problem is membraning the scientific method and the geodesic method.**'))
print(f'{sum(R)} of {len(R)} met')
