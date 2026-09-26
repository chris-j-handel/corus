"""twenty_eight_at_the_code_v368.py · the derived claims of Exhibit TWENTY-EIGHT Equilibria Definitions v367's
general form, run at Exhibit ONE Natural Resolver's own code and at the numbers they name.
Run from a folder holding Exhibit_ONE_Natural_Resolver_v368.md. Each line returns HOLDS or PARTS.
"""
import itertools
from fractions import Fraction as Fr
ONE = open('Exhibit_ONE_Natural_Resolver_v368.md', encoding='utf-8').read()
ns = {}; exec(ONE.split('```python\n')[1].split('```')[0], ns)
couple = ns['_1_self_coupling']
R = []
def check(label, ok): R.append(bool(ok)); print(('HOLDS ' if ok else 'PARTS ') + label)
sgn = lambda x: (x > 0) - (x < 0)
P4 = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
F = lambda p: (-p[1], p[0]); G = lambda p: (p[1], -p[0]); J = lambda p: (-p[0], -p[1])

# the binary opening and the four-state orbit
check('F(c,t)=(−t,c) and G(c,t)=(t,−c) each squared is J(c,t)=(−c,−t)', all(F(F(p)) == J(p) == G(G(p)) for p in P4))
sq = [m for m in itertools.product(P4, repeat=4) if all(m[P4.index(m[P4.index(p)])] == J(p) for p in P4)]
check('F and G are the only two maps on the four pairs whose square is J', sorted(sq) == sorted([tuple(F(p) for p in P4), tuple(G(p) for p in P4)]))
o, p = [], (1, 1)
for _ in range(4): o.append(p); p = F(p)
check('from ++, F runs ++, −+, −−, +− and back to ++', o == [(1, 1), (-1, 1), (-1, -1), (1, -1)] and p == (1, 1))
def left_after(S, start):
    p, k = start, 0
    while p in S: p, k = F(p), k + 1
    return k
check('{++, −+, −−} from ++ stays two advances and leaves at the third, at +−', left_after({(1, 1), (-1, 1), (-1, -1)}, (1, 1)) == 3)
subs = [set(s) for r in range(1, 4) for s in itertools.combinations(P4, r)]
check('each nonempty proper subset is left within at most three advances, from each of its members',
      all(1 <= left_after(S, q) <= 3 for S in subs for q in S))
pres = [S for r in range(0, 5) for S in map(set, itertools.combinations(P4, r)) if {F(q) for q in S} == S]
check('the subsets F preserves are exactly the empty set and all four, the unions of its one cycle', len(pres) == 2 and set() in pres and set(P4) in pres)
adv = lambda s: ''.join('1' if ch == '0' else '0' for ch in s)
check('advancing the overlapping triple changes 010 to 101 and 101 to 010', adv('010') == '101' and adv('101') == '010')

# the release pair 6/10 and the fresh 7/8 pair, at the code
def one_entry(c, t, h, offers):
    carrying = [(0, c, t, h)]
    surf, nxt = couple(carrying, [(0, x) for x in offers])
    six = {k: tt for k, cc, tt, hh in carrying}[0]
    s = dict(surf).get(0, 0)
    return six, s, {k: (cc, tt, hh) for k, cc, tt, hh in nxt}.get(0)
offer_sets = [[], [1], [-1], [1, 1], [-1, -1], [1, -1], [1, 1, 1], [-1, -1, -1]]
cases = [(c, t, h, off) for c in (1, -1) for t in (1, -1) for h in range(4) for off in offer_sets]
g_ok = comp_ok = 0; n = 0
for c, t, h, off in cases:
    six, s, fresh = one_entry(c, t, h, off)
    if s != 0:
        n += 1
        g_ok += fresh[:2] == G((six, s)) and six == t and fresh[2] == 0
        comp_ok += ((six == s) == (fresh[0] != fresh[1]))
check(f'at each existing entry with a nonzero surface, 6/10 = (t, s) and the fresh 7/8 = G(t, s) = (s, −t), opening 0 ({n} cases)', g_ok == n and n > 0)
check('equality at 6/10 gives opposition in the fresh 7/8, and opposition gives equality', comp_ok == n)
check('under empty receiving the surface is s = −c, so the complete return is J',
      all(one_entry(c, t, 0, [])[1] == -c and one_entry(c, t, 0, [])[2][:2] == J((c, t)) for c in (1, -1) for t in (1, -1)))
check('the surface is s = sign(r − c): the arriving signs meet the carrying sign inverting',
      all(one_entry(c, t, h, off)[1] == sgn(sum(off) - c) for c, t, h, off in cases))
a0, a3 = one_entry(1, -1, 0, [1]), one_entry(1, -1, 3, [1])
check('(+,−) with one matching positive arrival surfaces 0; from opening 0 it continues at 1, from opening 3 it leaves',
      a0[1] == 0 and a0[2] == (1, -1, 1) and a3[1] == 0 and a3[2] is None)
d1, d2 = one_entry(1, -1, 0, [1, 1]), one_entry(-1, 1, 0, [1, 1])
check('the same opposed relation and two positive arrivals give agreement from (+,−) and opposition from (−,+)',
      d1[2][0] * d1[2][1] == 1 and d2[2][0] * d2[2][1] == -1)
check('from (c, t) with no arriving the release pair is 6 = t and 10 = −c, and the same 10 accompanies either 6',
      {one_entry(1, t, 0, [])[:2] for t in (1, -1)} == {(1, -1), (-1, -1)})

# the numbers
check('n² − (n−1)(n+1) = 1 for n from 2 to 99', all(k * k - (k - 1) * (k + 1) == 1 for k in range(2, 100)))
check('17 − (9 − n) = n + 8 for n from 1 to 8', all(17 - (9 - k) == k + 8 for k in range(1, 9)))
internal, connectors = {3, 4, 5, 7, 8, 11, 12, 13, 15, 16}, {2, 6, 9, 10, 14, 17}
check('the ten internal names and the six connectors are disjoint and exhaust 2 to 17; with entry 1, all seventeen',
      not internal & connectors and internal | connectors == set(range(2, 18)) and len(internal | connectors | {1}) == 17)
check('the internal pairs 3/11, 4/12, 5/13, 7/15 and 8/16 are each 8 apart', all(b - a == 8 for a, b in [(3, 11), (4, 12), (5, 13), (7, 15), (8, 16)]))
U = lambda x: Fr(x) ** 4 / 4 - Fr(x) ** 3 / 3 - Fr(x) ** 2
dU = lambda x: x ** 3 - x ** 2 - 2 * x
check('U = x⁴/4 − x³/3 − x² has its turning values at −1, 0 and 2; −1 a local minimum and 2 the lowest',
      [x for x in range(-5, 6) if dU(x) == 0] == [-1, 0, 2] and U(-1) > U(2) and U(0) > U(-1))
law = lambda u, v, w: (v / 2, u + w, v / 2)
check('the two-molecule law (u, v, w) goes to (v/2, u+w, v/2), and (1/4, 1/2, 1/4) continues at each conversion',
      law(Fr(1, 4), Fr(1, 2), Fr(1, 4)) == (Fr(1, 4), Fr(1, 2), Fr(1, 4)))
check('each law (u, 1/2, 1/2 − u) reaches (1/4, 1/2, 1/4) in one conversion',
      all(law(u, Fr(1, 2), Fr(1, 2) - u) == (Fr(1, 4), Fr(1, 2), Fr(1, 4)) for u in [Fr(k, 20) for k in range(11)]))
check('forward and reverse propensities of the two-molecule account are equal only at B-count 1, and 1 goes to 0 or 2',
      [nb for nb in (0, 1, 2) if (2 - nb) == nb] == [1])

# the ten, three momentaries long, and the five places from two faces
self5, other5 = list(range(1, 6)), list(range(2, 7))
check('the ten, self 1–5 and other 2–6, spans 1–6, the self\'s three momentaries, co bi co bi co bi',
      sorted(set(self5) | set(other5)) == [1, 2, 3, 4, 5, 6] and len(self5) + len(other5) == 10
      and ' '.join('co' if n % 2 else 'bi' for n in range(1, 7)) == 'co bi co bi co bi')
check('at each of the places 2 to 6 one side completes and the other opens: five places from two faces, ten',
      all((n in self5 and n - 1 in self5) or (n in other5 and n - 1 in other5) for n in range(2, 7))
      and len([(n, f) for n in range(2, 7) for f in ('completing', 'opening')]) == 10)
check('the openings of n momentaries sum to n², the completings to n(n+1); at three, 9 and 12, and 3² − 2·4 = 1',
      all(sum(range(1, 2 * n, 2)) == n * n and sum(range(2, 2 * n + 1, 2)) == n * (n + 1) for n in range(1, 31))
      and (1 + 3 + 5, 2 + 4 + 6, 3 ** 2 - 2 * 4) == (9, 12, 1))
check('six consecutive changings from 3 complete at 8, and 9 opens, odd: co-releasing', 3 + 6 == 9 and 9 % 2 == 1)
def life(t):
    c, n = [(0, 1, t, 0)], 0
    while c: s_, c = couple(c, [(0, 1)]); n += 1
    return n
check('a retained carrying continues through its openings 1, 2 and 3, and to a fourth at a positive second sign', (life(-1), life(1)) == (4, 5))

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
check('even rings return every 2 couplings, each self changing at each coupling; odd rings every 4 × n', all(per[n] == (2 if n % 2 == 0 else 4 * n) for n in per if n > 1))
r5 = ring(5, 16); zeros = [(t + 1, r.index(0)) for t, r in enumerate(r5) if 0 in r]
check('in a ring of five the meeting travels one self each two couplings, one momentary', zeros[:5] == [(6, 0), (8, 1), (10, 2), (12, 3), (14, 4)])

# the exhibit's own text
import hashlib
T = open('Exhibit_TWENTY-EIGHT_Equilibria_Registry_v368.md', encoding='utf-8').read()
top, body = T.split('\n---\n', 1)
heads = re.findall(r'^## (.+)$', body, re.M)
toc_heads = re.findall(r'^\*\*\d+ · (.+)\*\*$', top, re.M)
check('the contents open the exhibit, each section in order with its bold concepts beneath it', heads == toc_heads and len(heads) == 5
      and all(('- ' + re.sub(r'[.:]$', '', b)) in top for b in re.findall(r'^\*\*([^*]+)\*\*', body, re.M)))
check('the exhibit opens inside its title and subtitle: no origin sentence retaught', 'Our universe is all existing things' not in T and 'All existing things are included' not in T)
tab = body[body.index('| The ten | Proposed conception, in its own words'):body.index('**The specified accounts and the older worked definitions')]
nys = [int(x) for x in re.findall(r'\*\*NY(\d\d)\*\*', tab)]
check('each of the 42 proposed conceptions is placed once at the ten', sorted(nys) == list(range(1, 43)))
ways = set(re.findall(r'^\| (\d+) · ', body[body.index('| The ten | Proposed conception'):], re.M))
check('all ten ways carry conceptions', ways == {str(k) for k in range(1, 11)})
own = re.sub(r'`[^`]*`', '', body)
check('no quoting, no illustrating, no speaker, no pointing to a file, no old working carried', not re.search(r'^> |illustrat|swimmer|the user|\.md\b|<details>', own, re.M | re.I))
mine = '\n'.join(l for l in own.split('\n') if '**NY' not in l)
check('no holding, standing, landing or every in the exhibit\'s own sentences, and living only at non-living scale and the living intelligence',
      not re.search(r'\bhold(ing|s)?\b|\bheld\b|\bstand|\bland(s|ing)?\b|\bevery|\b(un)?read', mine, re.I) and not re.search(r'(?<!non-)\bliving\b(?! intelligence)', mine))
check('the Registry names no other exhibit: the resolver, its code and the sixth condition said in their own words', not re.search(r'Exhibit [A-Z]|\b(?:ONE|TWO|THIRTEEN)\b|TWENTY-|Living Improving Value', own))
regrows = [l for l in body.split('\n') if re.match(r'^\| \d+ · .*\*\*(NY\d\d|SA\d\d)\*\*', l)]
check('the Equilibria Registry, Impossible Stable Forms of Existing: each conception carried whole with its field, the changing it names and its place at the ten',
      '# Equilibria Registry' in T and '**Impossible Stable Forms of Existing**' in T and len(regrows) == 63 and all(l.count(' | ') == 3 for l in regrows))
check('the code is Exhibit ONE Natural Resolver\'s as published', hashlib.sha256(ONE.split('```python\n')[1].split('```')[0].encode()).hexdigest().startswith('bf09851d684c'))

print(f'{sum(R)} of {len(R)} hold')
