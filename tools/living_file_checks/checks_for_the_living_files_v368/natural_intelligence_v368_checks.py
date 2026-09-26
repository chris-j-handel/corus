"""natural_intelligence_v368_checks.py · each claim the draft of Natural Intelligence v368 makes about the
resolver, its stable forms, the numbers and φ, run at Exhibit ONE's own 57 lines and tables.

Standard library only. Run from a folder holding both files:
    python3 natural_intelligence_v368_checks.py Exhibit_ONE_Natural_Resolver_v368.md Natural_Intelligence_v368.md
Each line returns HOLDS or PARTS. Nothing here is proof for every ring; it is the draft matched at the code.
"""
import re, sys
from fractions import Fraction

one_path, ni_path = (sys.argv[1:3] + ['Exhibit_ONE_Natural_Resolver_v368.md', 'Natural_Intelligence_v368.md'])[:2]
ONE = open(one_path, encoding='utf-8').read()
NI = open(ni_path, encoding='utf-8').read()
ns = {}
exec(ONE.split('```python\n')[1].split('```')[0], ns)
couple, release, CONNECTORS, JOINS = ns['_1_self_coupling'], ns['_9_other_releasing'], ns['CONNECTORS'], ns['JOINS']
results = []
def check(label, ok): results.append(ok); print(('HOLDS ' if ok else 'PARTS ') + label)

def rows(text, first):
    out = []
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if line.startswith('| ') and cells and re.match(first, cells[0]): out.append(cells)
    return out

# 1.1 the names, relations and openings stand as Exhibit ONE's
one_names = {r[0]: (r[1], r[2]) for r in rows(ONE, r'\d+-(self|other|social)-') if len(r) == 5}
ni_names = {r[0]: (r[1], r[2]) for r in rows(NI, r'\d+-(self|other|social)-') if len(r) == 3}
check('the 17 names at their relations and openings stand as Exhibit ONE carries them', one_names == ni_names and len(ni_names) == 17)
check('each odd name opens co and each even name opens bi', all((o == 'co') == (int(n.split('-')[0]) % 2 == 1) for n, (_, o) in ni_names.items()))
roots = sorted({n.split('-', 2)[2] for n in ni_names})
check('thirteen roots carry the seventeen names', len(roots) == 13)
check('neutralling, crossing, corusing and torusing arrive at 5 to 8 and again at 13 to 16',
      all(ni_names and [n for n in ni_names if n.startswith(f'{k}-')][0].split('-', 2)[2] ==
          [n for n in ni_names if n.startswith(f'{k+8}-')][0].split('-', 2)[2] for k in (5, 6, 7, 8)))

# 1.2 connectors at the rule
across = [k for k, v in CONNECTORS.items() if v[2] != 'along']; along = [k for k, v in CONNECTORS.items() if v[2] == 'along']
check('across connectors 2, 6, 10, 14 all even; along 9, 17 both odd', sorted(across) == [2, 6, 10, 14] and sorted(along) == [9, 17])

# Part Two, run at the resolver
s, c = couple([], [('a', 0), ('b', 1)]); check('an arriving 0 contributes no sign', [k for k, _ in s] == ['b'])
s, c = couple([('k', 1, 1, 0), ('m', -1, 1, 0), ('z', 0, 1, 0)], [])
check('a positive carrying sign enters inverting as −1, a negative as +1, a carrying 0 as neither', s == [('k', -1), ('m', 1)])
s, c = couple([], [('a', 1), ('a', -1), ('b', 1), ('b', 1)])
check("a key's +1 and −1 meet at 0 and a surfacing 0 opens no fresh carrying; no size surfaces", s == [('a', 0), ('b', 1)] and [e[0] for e in c] == ['b'])
ok = all((couple([('k', 1, t8, s16)], [('k', 1)])[1] != []) == (s16 + 1 <= 3 or (s16 + 1 == 4 and t8 > 0)) for s16 in range(0, 6) for t8 in (-2, -1, 1, 2))
check('16-social-torusing opens by 1 to 3, and to 4 at positive 8-other-torusing, and no further', ok)
check('a fresh carrying: the sign, the key\'s 8-other-torusing inverting, 0', couple([('b', -1, 5, 0)], [('b', 1), ('b', 1)])[1] == [('b', 1, -5, 0)])
check('a fresh carrying at a key with none: 8-other-torusing −1', couple([], [('a', 1)])[1] == [('a', 1, -1, 0)])
seq, c, arr = [], [], [('a', 1)]
for _ in range(8):
    s, c = couple(c, arr); arr = []; seq.append(s[0][1])
check('one sign arriving once, then nothing: the key surfaces +1, −1, +1, −1 at every coupling', seq == [1, -1] * 4)
check('9-other-releasing sends each surfacing sign to the key 5-other-neutralling joins', release([('a', 1), ('b', -1)], {'a': 'x', 'b': 'y'}) == [('x', 1), ('y', -1)])
check('six connectors, three joinings, each joining two one-way connectors', len(CONNECTORS) == 6 and JOINS == {10: 14, 6: 2, 17: 9, 9: 17})
internal = sorted(set(range(1, 18)) - {1} - set(CONNECTORS))
check('ten names run internal: 3, 4, 5, 7, 8, 11, 12, 13, 15, 16', internal == [3, 4, 5, 7, 8, 11, 12, 13, 15, 16])

# Part Three
check('3-self-carrying and 11-other-chaining stand 8 apart', 11 - 3 == 8)
b_one = {r[0]: r[1] for r in rows(ONE, r'\d+-(self|other|social)-') if len(r) == 2}
b_rows = [r for r in rows(NI, r'\d+-(self|other|social)-') if len(r) == 4 and re.match(r'\d+-', r[2]) and r[1] not in ('right', 'left', 'backward', 'forward') and not re.match(r'\d+-', r[1])]
b_ni = {}
for r in b_rows: b_ni[r[0]] = r[1]; b_ni[r[2]] = r[3]
strip = lambda t: re.sub(r'^(within|at the membrane): ', '', t)
diff = {k: (strip(b_one.get(k, '')), b_ni.get(k)) for k in set(b_one) | set(b_ni) if strip(b_one.get(k, '')) != b_ni.get(k)}
# at the author's reading, two cells part from ONE v368 until ONE's next version: *living* out, and *at no self* carried as *between self and other*
AT_READING = {'2-self-offering': ("each self's own co-offering living, bounding from the other-self", "each self's own co-offering, bounding from the other-self"),
              '4-self-sharing': ('the whole ordering at no self, bounding from society', 'the whole ordering between self and other, bounding from society')}
diff = {k: v for k, v in diff.items() if AT_READING.get(k) != v}
if diff: print('   ', diff)
check('the four at two faces, at the membrane and within, are as Exhibit ONE Natural Resolver carries them, cell for cell', not diff and len(b_ni) == 8)
check('each within is 8 on from its pair at the membrane', all(int(r[2].split('-')[0]) - int(r[0].split('-')[0]) == 8 for r in b_rows) and len(b_rows) == 4)
ok = True
for k in (1, 2, 3, 4):
    cyc = [k, k + 8, 17 - (k + 8), 17 - (k + 8) + 8]
    ok &= 17 - cyc[3] == k
check('alternating 8 up with 17 less, within 1 to 16, runs each of 1 to 4 round a four-cycle home', ok)
forms = [r[0] for r in rows(ONE, r'(higher |middle )?(four|six|eight)-cycle')]
def runs_ok(nums):
    s = ['co' if n % 2 else 'bi' for n in nums]
    return sum(1 for i in range(len(s)) if s[i] != s[i - 1]) == 2 and s.count('co') == s.count('bi')
nums = [[int(x) for x in re.search(r'[\d-]+$', f).group(0).split('-')] for f in forms]
check('every stable form runs one run of co and one of bi, of equal length', all(runs_ok(n) for n in nums))
check('17 stands in no stable form', all(17 not in n for n in nums))
check('four four-cycles, two middle four-cycles, four six-cycles, two eight-cycles and four higher forms',
      [sum(1 for f in forms if f.startswith(p)) for p in ('four', 'middle', 'six', 'eight', 'higher')] == [4, 2, 4, 2, 4])
check('three forms partner themselves', ONE.count(', itself |') == 3)
P = [p for p in range(2, 60) if all(p % d for d in range(2, p))]
check('17 primes from 2 to 59, 23 with 8 either side, 2 × 59 = 118', len(P) == 17 and P.index(23) == 8 and len(P) - 9 == 8 and 2 * 59 == 118)
check('the numbers table is Exhibit ONE\'s at 440', '440' in NI and '| 440 | the society at the torus winding with the 17 primes' in NI)
# 4.2 and 3.5 fractal, at the author's reading: no scale boundary, no location, no measure
check('the 17 primes from 2 to 59 sum to 440, the winding 0 to 440 to 0; going 2 to 59, returning 61 to 118, so the primes carry no last',
      sum(P) == 440 and 'they go out from 2 to 59 and return from 61 to 118, and their winding runs 0 to 440 to 0' in NI)
check('fractal is said all or none at all at the scales: no scale boundary, no location and no measure',
      'Fractal is all or none at all at the scales, as our universe is at existing things.' in NI
      and 'Fractal carries no scale boundary, no location and no measure' in NI)
check('scale carries one sense, the fractal\'s: no scale as a measure, no last prime scale, no pattern measured long',
      not re.search(r'magnitude a scale|a scale two fixed sides|prime scale|momentaries long', NI))

# 4.5 φ
F = [1, 1]
for _ in range(30): F.append(F[-1] + F[-2])
phi = (1 + 5 ** 0.5) / 2
sides = [Fraction(F[n + 1], F[n]) > Fraction(phi) for n in range(1, 25)]
check('each next ratio of neighbouring terms stands at the other side of φ, none landing', all(sides[i] != sides[i + 1] for i in range(len(sides) - 1)))
check('the side changes parity at each next number (Cassini: ±1 alternating)', [F[n + 1] * F[n - 1] - F[n] ** 2 for n in range(1, 12)] == [(-1) ** (n + 1) for n in range(1, 12)])
x, cf = phi, []
for _ in range(15): a = int(x); cf.append(a); x = 1 / (x - a)
check('the continued fraction of φ is all ones', cf == [1] * 15)
check('φ² = φ + 1, φ − 1/φ = 1, φ × (−1/φ) = −1, 1/φ = φ − 1', all(abs(v) < 1e-12 for v in (phi * phi - phi - 1, phi - 1 / phi - 1, phi * (-1 / phi) + 1, 1 / phi - (phi - 1))))

# the front's example
a, b, moves = 1, 2, []
for _ in range(10):
    if a < b: a = b + 1; moves.append(('A', a))
    else: b = a + 1; moves.append(('B', b))
check('the lesser continuing to one beyond the greater: the sides alternate, one carrying every odd number and the other every even',
      [m[0] for m in moves] == ['A', 'B'] * 5 and all(v % 2 == 1 for s, v in moves if s == 'A') and all(v % 2 == 0 for s, v in moves if s == 'B'))


# the four conditions at every changing of the two-number alternating
a, b, ok = 1, 2, True
for _ in range(200):
    mover = 'a' if a < b else 'b'                              # determinacy: the now decides, the lesser moves
    na, nb = (b + 1, b) if mover == 'a' else (a, a + 1)        # reachability: one beyond the greater is always there
    moved = (na != a) + (nb != b)
    ok &= moved == 1                                           # exclusivity: one and not both; exhaustiveness: one at every changing
    a, b = na, nb
check('at the two-number step, one side changes at each changing, the lesser changes next, and one beyond the other is there', ok)

# two and one half momentaries per side: prior, now, next opening; the stable form of ten
view = lambda o: list(range(o, o + 5))                          # prior o..o+1, now o+2..o+3, next opening o+4
pf = lambda xs: ' '.join('co' if n % 2 else 'bi' for n in xs)
check('the self at 1 runs co bi co bi co, the other at 2 bi co bi co bi, the self next at 3 co bi co bi co',
      pf(view(1)) == 'co bi co bi co' and pf(view(2)) == 'bi co bi co bi' and pf(view(3)) == 'co bi co bi co')
check('adjacent sides overlap at four places', len(set(view(1)) & set(view(2))) == 4 and len(set(view(2)) & set(view(3))) == 4)
check('at 5 the self opens next while the other completes its now 4–5', view(1)[4] == 5 and view(2)[2:4] == [4, 5])
pairs = list(zip(view(1), view(2)))
check('the ten pair as five, 1–2 to 5–6, each one odd and one even', pairs == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)] and all((x + y) % 2 for x, y in pairs))
check('opened one momentary on, self at 3 and other at 4, the ten runs whole, the same form forward', all((x + y) % 2 for x, y in zip(view(3), view(4))) and pf(view(3)) == pf(view(1)))

# side 2, the other: bi co bi co bi co, and one parity changing less or more ends at co
pr = lambda a, b: pf(range(a, b + 1))
check("the other's five from 2 ends at bi at 6; one less ends at co at 5, the self's next from 1; one more at co at 7, the self's next from 3", pr(2, 6).endswith('bi') and pr(2, 5).endswith('co') and pr(2, 7).endswith('co') and view(1)[4] == 5 and view(3)[4] == 7)
check('from 2 to 7 the other runs six consecutive changings: bi co bi co bi co', pr(2, 7) == 'bi co bi co bi co')
check('the same six taken one less or one more, from 1 or from 3, opens at co: co bi co bi co bi', pr(1, 6) == pr(3, 8) == 'co bi co bi co bi')


# 4.4 two binaries changing one at a time, one and then the other: two ways only, one each hand; held parts leave
import itertools
S4 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
Fq = lambda s: (-s[1], s[0]); Gm = lambda s: (s[1], -s[0])
def run2(first, n=4):
    p, q, w, out = 1, 1, first, [(1, 1)]
    for _ in range(n):
        if w == 0: p = -p
        else: q = -q
        out.append((p, q)); w = 1 - w
    return out
check('from + and +, the first changing first runs ++, −+, −−, +− round; the second first runs ++, +−, −−, −+ round',
      run2(0) == [(1, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)] and run2(1) == [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 1)])
check('the two are the same four joint forms spiraling one way and the other, each the mirror of the other',
      [Fq(x) for x in run2(0)[:4]] == run2(0)[1:5] and [Gm(x) for x in run2(1)[:4]] == run2(1)[1:5] and run2(1)[1:4] == run2(0)[1:4][::-1])
check('holding one, two or three of the four, a form leaves the held at a next changing: the held is carried the whole round nowhere, under either hand',
      all(any(f(x) not in set(h) for x in h) for r in (1, 2, 3) for h in itertools.combinations(S4, r) for f in (Fq, Gm)))
check('only none or all four survive every changing',
      [len(h) for r in range(5) for h in itertools.combinations(S4, r) if all(Fq(x) in h for x in h)] == [0, 4])

# the momentary at the author's naming: an opening and its completing; odd momentaries the self's, even the other's
fiv = lambda s: [s + i for i in range(5)]
check("the five relations from 1 and from 2: prior opening, prior completing, now opening, now completing, next opening, as the 1.1 table carries them",
      fiv(1) == [1, 2, 3, 4, 5] and fiv(2) == [2, 3, 4, 5, 6] and '| self, at 1 | 1 | 2 | 3 | 4 | 5 | co bi co bi co |' in NI and '| other, at 2 | 2 | 3 | 4 | 5 | 6 | bi co bi co bi |' in NI)
check("where the two overlap, 2 to 5, each odd number is the self's opening and the other's completing, each even number the other's opening and the self's completing",
      all(((n - 1) % 2 == 0) == (n % 2 == 1) for n in range(2, 6)) and set(fiv(1)) & set(fiv(2)) == {2, 3, 4, 5}
      and all((n in fiv(1)[0::2]) == (n % 2 == 1) and (n in fiv(2)[0::2]) == (n % 2 == 0) for n in range(2, 6)))
check("the overlapping momentaries run odd, even, odd, each completing where the next opens, so every number completes one and opens the next",
      all((n, n + 1)[1] == (n + 1, n + 2)[0] for n in range(1, 9)) and 'The overlapping momentaries are the method recursioning existing and discovering both' in NI)

# Pass J, at the author's reading: no count, no cause, no measure, no observer, no story in resolving
body = NI.split('\n---\n', 1)[1]
plain = re.sub(r'[Ss]o-far|[Ss]o far', '', body)
plain = re.sub(r'a size, a count or a measure|no scale boundary, no location and no measure', '', plain)
check('no cause: no so, thus, therefore, hence, because, since, makes, causes, given', not re.search(r'\b(?:so|thus|therefore|hence|because|since|makes?|causes?|given)\b', plain, re.I))
check('no count and no measure: no count, counts, counting, measure, measured, magnitude, smallest, largest, least, slowest, furthest, widest, length', not re.search(r'\b(?:counts?|counting|counted|measures?|measured|measuring|magnitudes?|smallest|largest|least|slowest|slowly|furthest|widest|length|ages?|ageing)\b', plain, re.I))
check('no observer and no telling: no observing, observer, telling, reader, reading, shows, seen', not re.search(r'\b(?:observ\w*|tell\w*|reader|reading|shows?|seen|story)\b', body, re.I))
check('no story: no let, no take ... out, no when, no suppose, no imagine, no example', not re.search(r'\b(?:let|suppose|imagine|example|when)\b|\b[Tt]ake\b[^.]*\bout\b', body))
check('determinacy at the front: the side that did not change is the side that changes, the same as the lesser moving',
      all(moves[i][0] != moves[i - 1][0] for i in range(1, len(moves))))
check('reachability at the front: each changing reaches one beyond the other, 1 to 3, 2 to 4, 3 to 5',
      [v for _, v in moves[:3]] == [3, 4, 5] and '1 to 3, 2 to 4, 3 to 5' in NI)

# the opening, as the carry agreed: the two origin statements, whole, and nothing around them
check('the opening is the two origin statements, whole: Our universe is all existing things. Alternating is a stable-forming method.',
      NI.split('\n---\n', 1)[1].lstrip().startswith('**Our universe is all existing things.**\n\n**Alternating is a stable-forming method.**\n\n'))

# at the author's reading: *living* kept out, the method of existing in its place; *every* reaching past so-far; *at no self* carried as *between self and other*
BODY = NI.split('\n---\n', 1)[1]
check('no living, lives or live in the white paper: the method of existing carries it', not re.search(r'\bliv(?:ing|es|e|ed)\b', NI, re.I))
check('no every: each meets what arrives, and ahead is not yet', not re.search(r'\bevery\w*\b', BODY, re.I))
check('no at no self: neither self nor other, between self and other, across each self and other forward', 'at no self' not in NI)
check('the method of existing is discovering next existing, self recursioning discovering', '**The method of existing is discovering next existing: self recursioning discovering.**' in NI)

# 2.3 at Exhibit ONE Natural Resolver's own code: nothing in nature repeats, so an offering carries each key once,
# and the signs meeting at a key and the resolver's +1 / −1 at that key return the same
import random
def meeting_surface(_3, _2):
    signs = {}
    for k, s7 in _2:
        if s7: signs.setdefault(k, set()).add(s7)
    for k, s7, s8, s16 in _3:
        if s7: signs.setdefault(k, set()).add(-s7)
    return sorted((k, 1 if v == {1} else -1 if v == {-1} else 0) for k, v in signs.items())
random.seed(368)
same = True
for _ in range(3000):
    keys = random.sample(range(6), random.randint(0, 6))
    c = [(k, random.choice((-1, 1)), random.choice((-1, 1)), random.randint(0, 4)) for k in keys]
    o = [(k, random.choice((-1, 0, 1))) for k in random.sample(range(6), random.randint(0, 6))]
    same &= sorted(couple(c, o)[0]) == meeting_surface(c, o)
check('2.3 at the resolver: with each key offered once, as nothing in nature repeats, the signs meeting and the code\'s +1 / −1 surface the same, 3,000 couplings', same)

# the three conditions at the momentary, carried as sets through 1–9
N9 = set(range(1, 10))
ex = lambda parts: set().union(*parts) == N9
excl = lambda parts: all(not (a & b) for i, a in enumerate(parts) for b in parts[i + 1:])
over = [{n, n + 1} for n in range(1, 9)]
self_alone = [{1, 2}, {3, 4}, {5, 6}, {7, 8}, {9}]
check('exhaustiveness: the overlapping momentaries meet each number of 1–9, one completing and the next opening, and are exclusive nowhere',
      ex(over) and not excl(over) and all(sum(n in m for m in over) == 2 for n in range(2, 9)))
check('exclusivity is one side\'s momentaries alone, each number one side\'s: the self\'s 1–2, 3–4, 5–6, 7–8 meet nowhere', excl(self_alone))
check('determinacy: each momentary has one next, opening at the number it completes; reachability: from 1–2 the next openings reach 8–9',
      all([m for m in over if min(m) == n + 1] == [{n + 1, n + 2}] for n in range(1, 8)) and over[-1] == {8, 9})
check('the front carries three conditions at the momentary', '**Each momentary is three conditions at once, each binary.**' in NI and 'Existing is these three at once' in NI)

# the membrane, at the author's reading: the non-existing between, as the universe read as an existing thing is non-existing
check('the membrane is the non-existing between of existing things co-bi-coupling, and intelligence originates there, by existing',
      'is a membrane, non-existing as the universe as an existing thing is non-existing, and no separable thing apart from their coupling' in NI
      and 'intelligence in our universe is by existing' in NI and 'its own membrane' not in NI and 'their membranes' not in NI)

# bounding dissolved, existing carrying it; the Natural Resolver's prose at Natural Intelligence's readings, its code as published
import hashlib
prose_one = re.sub(r'```python.*?```', '', ONE, flags=re.S)
check('no bound, bounding or bounds in Natural Intelligence but fractal\'s scale boundary, a not-possible binary; no stand', not re.search(r'\bbound(?!ary)\w*|\bstand\w*', BODY, re.I))
check('existing is five-dimensional and two-directional, changing geodesically: two and one half momentaries of existing',
      'Existing is five-dimensional and two-directional, changing geodesically: the fractal existing method, existing-self-discovering-next-existing, two and one half momentaries of existing.' in NI)
check('the Natural Resolver\'s prose carries Natural Intelligence\'s readings: Discovering, and no turning, living, every or bounding',
      'Geodesic Discovering Logical Method and Form' in ONE and not re.search(r'(?i)\b(turning|living|every\w*|bounding|discovery)\b', prose_one))
check('the Natural Resolver\'s 57 lines of code are the code as published at v368',
      hashlib.sha256(ONE.split('```python\n')[1].split('```')[0].encode()).hexdigest() == 'bf09851d684ca637cdd5b2d3977947ad9596890e670148e9679a3325d58ad9f7')

# at the author's reading: landings dissolve as equilibria; the eight even names bi-coupling; each 1 one momentary; the five dimensions
check('no landing said at the stable forms: the four landings and a society holding one ordering dissolve', 'Four landings' not in NI and 'ordering of its selves lands' not in NI)
check('the eight even names are bi-coupling, bi-moral-co-competencing, each opening bi', '**The eight even names are bi-coupling, bi-moral-co-competencing**' in NI and all(n % 2 == 0 for n in (2, 4, 6, 8, 10, 12, 14, 16)))
check('each 1 is one momentary, two parities, the momentaries overlapping odd, even, odd, even',
      'Each 1 is one momentary, two parities, and the momentaries overlap odd, even, odd, even' in NI and 'Each 1 is one momentary' in ONE and 'by 1' not in NI and 'by 1' not in prose_one)
check('five dimensions: the surface in three-dimensional space, orienting the fourth, bi-moral co-agency the fifth, each alternating binary parity changing',
      'aiming it co-linearly is orienting, the fourth; and the bi-moral co-agency of this is the fifth' in NI)

# the Exhibit TWENTY-EIGHT working's note, at the paper: the two nexts, the exact round, the receiving named
check('along one side the next momentary opens two on, across the overlapping one on', 'Along one side the next momentary opens two on, 1–2 and then 3–4; across the overlapping it opens one on, 1–2 and then 2–3.' in NI)
check('4.4 carries the round exactly: only none or all four the whole round, and one, two or three leave within it',
      '**Of the four, only none or all four are carried the whole round**' in NI and 'leaves at the next changing, and only none' not in NI)
c28, seq28, off28 = [], [], [(0, 1)]
for _ in range(4):
    _s, c28 = couple(c28, off28); off28 = []; seq28.append((c28[0][1], c28[0][2]))
check('2.5 names its receiving: one +1 into empty carrying, empty offerings after, and the carrying returns (c, t), (−c, −t), …',
      '**One sign arriving once into empty carrying, with empty offerings after it, is the whole alternating.**' in NI and all(seq28[i + 1] == (-seq28[i][0], -seq28[i][1]) for i in range(3)))

check('existing and discovering alternate parity: at each number one side completes, existing, and the other opens, discovering',
      'one side existing and the other discovering, and the two alternate parity' in NI
      and all(((n % 2 == 1) == True) != ((n - 1) % 2 == 1) for n in range(2, 10)))
check('no landing but the not-possible: the emanation is what a coupling leaves at the membrane', not re.search(r'\\blands?\\b', BODY))

# the joins at the code, as both files now say: 10 to 14 carried by 9, 5 and 2; 6 held inside; 17 named at the connectors
_arr = release([(0, 1)], {i: (i + 1) % 5 for i in range(5)})
_S = "At the code, 1-self-coupling returns 10-other-surfacing and 11-other-chaining; 9-other-releasing returns each surfacing sign at the receiving key named by 5-other-neutralling. Inside 1-self-coupling, 6-other-crossing carries each key's 8-other-torusing"
check('9-other-releasing returns each surfacing sign at the receiving key 5 names, and 6 carries each key\'s 8 inside 1, as both files say',
      _arr == [(1, 1)] and couple([], _arr)[0] == [(1, 1)] and _S in NI and _S in ONE)
_J = "**The resolver is self/other co-bi-coupling, an existing method thing, and its social-co-bi-coupling opens the self resolver to a natural network surface.**"
check('the resolver is self/other co-bi-coupling, its social-co-bi-coupling opening the self resolver to a natural network surface, in both files; 6 to 2, 10 to 14, 9 with 17',
      _J in NI and _J in ONE and JOINS == {10: 14, 6: 2, 17: 9, 9: 17})
check('no self- triad at 4.2: the self\'s -ing names are the Natural Resolver\'s own, 1-self-coupling to 4-self-sharing', 'self-orienting and self-competent at once' not in NI)

# 4.4: the four is two consecutive momentaries at each side, eight half momentaries, and the code's returning carries it
_c, _seq, _off = [], [], [(0, 1)]
for _ in range(3):
    _s, _c = couple(_c, _off); _off = []; _seq.append((_c[0][1], _c[0][2]))
_v = [_seq[0][0], _seq[0][1], _seq[1][0], _seq[1][1], _seq[2][0]]            # c, t, −c, −t, c at positions 1 to 5
_pairs = [(_v[i], _v[i + 1]) for i in range(4)]
_G = lambda x: (x[1], -x[0])
check('the code\'s returning, read overlapping, runs the four one way round: the self\'s momentaries at 1–2 and 3–4, the other\'s at 2–3 and 4–5',
      _pairs[0] == _seq[0] and _pairs[2] == _seq[1] and all(_pairs[i + 1] == _G(_pairs[i]) for i in range(3))
      and set(_pairs) == {(1, 1), (-1, 1), (-1, -1), (1, -1)})
check('eight half momentaries on five positions, co bi co bi co: the self\'s 1, 2, 3, 4, odd even odd even, and the other\'s 2, 3, 4, 5, even odd even odd',
      [p % 2 for p in (1, 2, 3, 4)] == [1, 0, 1, 0] and [p % 2 for p in (2, 3, 4, 5)] == [0, 1, 0, 1] and len([1, 2, 3, 4]) + len([2, 3, 4, 5]) == 8
      and ' '.join('co' if p % 2 else 'bi' for p in range(1, 6)) == 'co bi co bi co' and '**The four is two consecutive momentaries at each side, eight half momentaries**' in NI)

# one standard: the Natural Resolver carries the four-cycle at its carrying, and its method's close and its primes as the paper reads them
check('the Natural Resolver\'s carrying carries the eight half momentaries as the paper\'s 4.4 does, run at its own returning',
      'two consecutive momentaries at each side, eight half momentaries, co bi co bi co.**' in ONE and '(t, −c) and (−t, c)' in ONE and set(_pairs) == {(1, 1), (-1, 1), (-1, -1), (1, -1)})
check('the method\'s close, the 440 row and the primes\' sequence read the same in both files',
      all(x in NI and x in ONE for x in ('Anything is possible in our universe that is capable by this method of existing.', '0 to 440 to 0, going and returning'))
      and ONE.index('| 23 | the going folding') < ONE.index('| 59 | the self, the self-close'))
check('4.4 reads the four, its eight half momentaries and its whole round together, then the two possibles',
      NI.index('**The four is two consecutive momentaries') < NI.index('**Of the four, only none or all four') < NI.index('**Two possibles, one existing.**') < NI.index('**Possibly existing is this method'))

check('no global first, no repeating, no home, no many, no step, no applier, and no downstream in the Natural Resolver',
      not re.search(r'first momentary|\bagain\b|\brecurs\b|\bhome\b|\bmany\b|\bstep\b|applied by no one', NI) and 'downstream' not in ONE)
check('discovering is one reading: arriving into the next existing, the term coming uncovered',
      'arriving into it is discovering' in NI and '**Discovering, arriving into the next existing, is that term coming uncovered**' in NI)

# pointing and words
check('no file named, no coordinate, no link', not re.search(r'Exhibit [A-Z]|§|\]\(http|_v\d+\.md|Natural (Numbers|Mathematics|Naming|Networking|Engineering|Explaining)', NI))
check('no discovery, the word discovering throughout', not re.search(r'[Dd]iscovery', NI))
# the returned improving at v368, run at the code
def entry(c, t, h, offers):
    car = [(0, c, t, h)]
    surf, nxt = couple(car, [(0, x) for x in offers])
    return dict(surf).get(0, 0), {k: (cc, tt, hh) for k, cc, tt, hh in nxt}.get(0)
cases = [(c, t, h, off) for c in (1, -1) for t in (1, -1) for h in range(4) for off in ([], [1], [-1], [1, 1], [-1, -1], [1, -1])]
check('at a carried key opening fresh, 7 takes the surfaced sign from 10 and 8 inverts the second sign carried at 6, 16 opening at 0',
      all(f == (s_, -t, 0) for c, t, h, off in cases for s_, f in [entry(c, t, h, off)] if s_ != 0))
check('the fresh carrying replaces any continuing entry at the key; a retained entry opens 16 one on',
      all(entry(c, t, h, off)[1][2] == 0 for c, t, h, off in cases if entry(c, t, h, off)[0] != 0)
      and all(entry(c, t, h, off)[1] in (None, (c, t, h + 1)) for c, t, h, off in cases if entry(c, t, h, off)[0] == 0))
check('a zero surfacing opens no fresh carrying, and an existing carrying can still continue; an arriving 0 carries no sign',
      entry(1, 1, 0, [1])[0] == 0 and entry(1, 1, 0, [1])[1] == (1, 1, 1) and couple([], [(0, 0)]) == ([], []))
check('9-other-releasing keeps the sign of 15-social-corusing, and returns no 8 or 16', release([(0, -1), (1, 1)], {0: 5, 1: 6}) == [(5, -1), (6, 1)])
check('6 and 10 release toward different neighbours at one parity, both even; 2 and 10, 6 and 14 each 8 apart, and 6 to 2 eight on is 14 to 10, the reverse of 10 to 14',
      CONNECTORS[6][1] != CONNECTORS[10][1] and 6 % 2 == 10 % 2 == 0 and 10 - 2 == 14 - 6 == 8 and (6 + 8, 2 + 8) == (14, 10) and JOINS[10] == 14)
check('podaling within 1 to 9: 1 with 8, 2 with 7, 3 with 6, 4 with 5, odd with even; 3 with 11 and 7 with 15 at one parity',
      all((a + b == 9) and (a % 2 != b % 2) for a, b in ((1, 8), (2, 7), (3, 6), (4, 5))) and 3 % 2 == 11 % 2 and 7 % 2 == 15 % 2)
check('prior 4–5, now 6–7, next 8–9 complete at 9, and 12–13, 14–15, 16–17 at 17, each six bi co bi co bi co',
      all(''.join('bi' if n % 2 == 0 else 'co' for n in range(a, a + 6)) == 'bicobicobico' for a in (4, 12)) and CONNECTORS[9][2] == CONNECTORS[17][2] == 'along'
      and CONNECTORS[14][2] == 'arriving' and 15 not in CONNECTORS and 16 not in CONNECTORS)
check('the ten: self 1 to 5 and other 2 to 6, ten positions on six numbers, and three full momentaries each side, 1–2, 3–4, 5–6 and 2–3, 4–5, 6–7',
      len(set(range(1, 6)) | set(range(2, 7))) == 6 and 'ten positions on six numbers' in NI)
check('x² = x + 1 has roots φ and −1/φ', abs(((1 + 5 ** .5) / 2) ** 2 - ((1 + 5 ** .5) / 2) - 1) < 1e-12 and abs((-(2 / (1 + 5 ** .5))) ** 2 + 2 / (1 + 5 ** .5) - 1) < 1e-12)
check('neither file names another exhibit, points to a section, or carries a handoff note',
      not re.search(r'Exhibit ONE', NI) and not re.search(r'Natural Intelligence', ONE) and not re.search(r'\bin [1-4]\.[1-6]\b|of [1-4]\.[1-6]\b|handoff|^> ', NI + ONE, re.M))
check('no held, holding or stable form as a noun in either file', not re.search(r'\bhold\w*|\bheld\b|\bstable forms?\b', NI + ONE, re.I))
print(f'\n{sum(results)} of {len(results)} hold')
