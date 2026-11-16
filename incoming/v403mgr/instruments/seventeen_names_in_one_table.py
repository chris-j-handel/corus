"""The seventeen names in one table: each name a line, each thing the set has of a name a column.
Reads Exhibit ONE Natural Resolver's living version, one sentence of Exhibit TWENTY Natural Naming, and two droplets
of the gathering files; executes; writes no file; decides nothing.

Use: python3 -I incoming/v403mgr/instruments/seventeen_names_in_one_table.py <root>        each column, and each check
     python3 -I incoming/v403mgr/instruments/seventeen_names_in_one_table.py <root> csv    the table

Each column has its standing after its name:
  [living ONE]     a table, a line or a field of Exhibit ONE Natural Resolver, as it is
  [living TWENTY]  a sentence of Exhibit TWENTY Natural Naming, as it is
  [executed]       read out of the code's lines or out of the table, all or none at all
  [an is]          an is of the partners, gathered in Exhibit ONE Natural Resolver's gathering file
  [floating]       a suggesting or a candidate, in no living sentence

The planes, a candidate of this session, floating. Exhibit TWENTY Natural Naming has three golden rectangles at
right angles centred on a corus, their twelve corners four triangles of three on four heights about one line, a
right-hand turn of a third about that line bringing each rectangle onto its next. The candidate: a rectangle by
each root of three, existing with discovering, possibling, observing; a height by each four-cycling; and each
four-cycling's same-existing name on the line of the turn. Each check of it is all or none at all, below.

Returned at main, 15 November 2026:
  66 columns, 17 names. Each field of a name in Exhibit ONE Natural Resolver is in a column: is.
  The planes, each check: is. Each four-cycling's three names are one triangle at one height. Each rectangle's
  along sides are through its next rectangle, each passing forward. A right-hand turn of a third brings each name
  of the three onto the name it is after, and a turn the other way onto its next name. Parity's unit square is the
  possibling rectangle as it is: across 6 to 2 and 10 to 14, along 2 with 10 and 6 with 14, its diagonals through
  the corus. Through the corus from each other: 1 and 13, 5 and 9, 2 and 14, 6 and 10, 3 and 15, 7 and 11, 4 and
  16, 8 and 12; of these 7 and 11, 4 and 16, and 8 and 12 are each one dual.
"""
import ast, csv, glob, io, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); twenty = living('Exhibit_TWENTY_Natural_Naming')
L = one.split('\n'); code = one.split('```python', 1)[1].split('```', 1)[0]
N = range(1, 18)

# --- Exhibit ONE Natural Resolver: its table of the seventeen
rows = re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|', one, re.M); assert len(rows) == 17
NAME = {int(r[0]): r[1] for r in rows}; ROOT = {int(r[0]): r[2].strip() for r in rows}; BITS = {int(r[0]): r[3].strip() for r in rows}
CO = {int(r[0]): r[4].strip() for r in rows}; THREE = {int(r[0]): r[5].strip() for r in rows}
NUM = {v: k for k, v in NAME.items()}
names_in = lambda s: [NUM[m] for m in re.findall('|'.join(re.escape(x) for x in sorted(NUM, key=len, reverse=True)), s)]

def part(opening):   # the lines of one part, from its opening words to the next part opening with bold words
    i = next(k for k, l in enumerate(L) if l.startswith(opening)); j = i + 1
    while j < len(L) and not re.match(r'\*\*[A-Z1-9+]', L[j]): j += 1
    return L[i:j]
def table(opening, cols):
    out = {}
    for l in part(opening):
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) == cols and c[0].isdigit(): out[int(c[0])] = c[1:]
    return out

# --- code with each name, and each name two-sided
i = next(k for k, l in enumerate(L) if 'Code with each name:' in l)
CODE_WITH = {int(m.group(1)): m.group(2) for l in L[i:i + 22] for m in [re.match(r'- \*\*(\d+)\*\* · (.+)', l)] if m}; assert len(CODE_WITH) == 17
TWO = table('**Two-sided, each name.**', 4); assert len(TWO) == 17

# --- four four-cyclings and their betweens
CYC, BETWEEN = {}, {}
for l in part('**Four four-cyclings and their betweens.**'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 6 and c[0] in ('first', 'second', 'third', 'fourth'):
        for x in c[1:5]: CYC[int(x)] = c[0]
        a, b = [int(x) for x in re.findall(r'\d+', c[5])]; BETWEEN[a] = BETWEEN[b] = c[5]
assert len(CYC) == 16

# --- co, between two or of one, with its root
OF = {}
for l in part('**Co, between two or of one.**'):
    for kind, seg in re.findall(r'\*(With co, between two|Without co, of one)\*: (.+?)(?= · \*|$)', l):
        ns = names_in(seg); tail = seg.split(NAME[ns[-1]], 1)[1].lstrip(', ').strip()
        for n in ns: OF[n] = ('between two' if kind.startswith('With co') else 'of one') + (': ' + tail if tail else '')
assert len(OF) == 17

# --- sharing between selves; same-existing through one moment; each is-or-is-not of the code
SHARE, BESIDE, ISNOT = {}, {}, {n: [] for n in N}
for l in part('**Sharing between selves.**'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 3 and names_in(c[0]):
        a, b = names_in(c[0])[0], names_in(c[1])[0]
        SHARE[a] = f'sharing side, to {NAME[b]}: {c[2]}'; SHARE[b] = f'observing side, from {NAME[a]}: {c[2]}'
for l in part('**Same-existing through one moment.**'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 3 and names_in(c[0]):
        a, b = names_in(c[0])[0], names_in(c[1])[0]
        BESIDE[a] = f'its is-or-is-not: {c[1]}'; BESIDE[b] = f'the is-or-is-not of {c[0]}'
for l in part('**Where each is-or-is-not stands.**'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 4 and c[0] != 'Code' and not set(c[0]) <= set('-'):
        for n in sorted(set(names_in(c[2])) | {int(x) for x in re.findall(r'\b(\d+)\b', c[2])}): ISNOT[n].append(c[1])
assert sum(len(v) for v in ISNOT.values()) == 12   # ten lines, two of them on two names each

# --- each name and its relations: its fields
F = {}; cur = None
for l in part('**Each name and its relations.**') + [x for o in [f'**{n}** · ' for n in N] for x in part(o)]:
    m = re.match(r'\*\*(\d+)\*\* · ', l)
    if m: cur = int(m.group(1)); F.setdefault(cur, {}); continue
    m = re.match(r'- \*(.+?)\*: (.*)', l)
    if m and cur: F[cur][m.group(1)] = m.group(2)
assert len(F) == 17 and all('Prior and next' in F[n] for n in N)
f = lambda n, k: F[n].get(k, '')
BF = {}
for n in range(1, 17):
    m = re.match(r'([\d-]+), going (8 up|17 less) first from \S+, from (\S+) to it and on to (\S+), each name one apart from (.+)$', f(n, 'Bi-folding')); assert m, n
    BF[n] = m.groups()

# --- each name, three scales
SC = {}; cur = None
for l in part('**Each name, three scales.**'):
    m = re.match(r'- \*\*n: (\d+)\*\*', l)
    if m: cur = int(m.group(1)); SC[cur] = {}; continue
    m = re.match(r'\s+- \*(.+?)\*: (.*)', l)
    if m and cur: SC[cur][m.group(1)] = m.group(2)
assert len(SC) == 17

# --- fives: each side's five; and each odd name of a self's span, receiving and giving on
FIVE = {n: [] for n in N}; side = None
for l in part('**Fives.**'):
    m = re.match(r'- \*\*Side: (.+?)\*\*', l)
    if m: side = m.group(1); continue
    m = re.match(r'\s+- \*(.+?)\*: (\d+)$', l)
    if m and side: FIVE[int(m.group(2))].append(f'{m.group(1).lower()}, by the side {side}')
ODD = {}; cur = None
for l in part('**Odd names, now and 8 up with next.**'):
    m = re.match(r'- \*\*Now: (.+?)\*\*', l)
    if m: cur = NUM[m.group(1)]; ODD[cur] = {}; continue
    m = re.match(r'\s+- \*(.+?)\*: (.*)', l)
    if m and cur: ODD[cur][m.group(1)] = m.group(2)
assert len(ODD) == 4 and sum(len(v) for v in FIVE.values()) == 20

# --- a between, 0
ZERO = {n: [] for n in N}; head = None
for l in part('**Namings among names.**'):
    m = re.match(r'- \*\*A between, 0: (.+?)\*\*', l)
    if m: head = m.group(1); continue
    if l.startswith('- **'): head = None
    if head and '*Names*' in l:
        for n in sorted(set(names_in(l))): ZERO[n].append(head)

# --- Exhibit TWENTY Natural Naming: the four loopings of the bi-foldings, and the two loops of four names
m = re.search(r'moralizing ([\d–]+), competencing ([\d–]+), corusing ([\d–]+) and torusing ([\d–]+)', twenty); assert m
LOOPING = {g.replace('–', '-'): w for g, w in zip(m.groups(), ('moralizing', 'competencing', 'corusing', 'torusing'))}
m = re.search(r'two loops of four names\*\*, ([\d-]+) and ([\d-]+), each by 4 up and 9 less', twenty); assert m
LOOP4 = {int(x): g for g in m.groups() for x in g.split('-')}

# --- the gathering files: the newest seventeen duals, and four names of 2 to 7, each floating
G = open(os.path.join(R, 'gathering-value', 'Natural_Resolver.md'), encoding='utf-8').read()
d = next(l for l in G.split('\n') if l.startswith('- **Possible exploring** · The seventeen names, each a dual'))
DUAL = {int(a): b for a, b in re.findall(r'\b(\d+)-((?:not-|no-)?[a-z]+-and-(?:not-|no-)?[a-z]+)', d.split('The newest seventeen', 1)[1].split('Executed', 1)[0])}; assert len(DUAL) == 17
P = open(os.path.join(R, 'gathering-value', 'Natural_Physics.md'), encoding='utf-8').read()
d = next(l for l in P.split('\n') if '2 is inhaling' in l)
BREATH = {int(a): b for a, b in re.findall(r'\b(\d+) is (inhaling|exhaling|ingesting|exhausting)', d)}; assert len(BREATH) == 4

# --- executed: the code's lines
tree = ast.parse(code); IN = {n: [] for n in N}
num = lambda s: int(s.split('_')[1])
for fn in tree.body:
    if not isinstance(fn, ast.FunctionDef): continue
    IN[num(fn.name)].append('a function of the code'); here = NAME[num(fn.name)]
    for a in fn.args.args: IN[num(a.arg)].append(f'given to {here}')
    made, each, into = set(), set(), set()
    for x in ast.walk(fn):
        if isinstance(x, ast.Assign):
            todo = list(x.targets)
            while todo:
                y = todo.pop()
                if isinstance(y, ast.Name): made.add(num(y.id))
                elif isinstance(y, ast.Tuple): todo.extend(y.elts)
                elif isinstance(y, ast.Subscript) and isinstance(y.value, ast.Name): into.add(num(y.value.id))
        if isinstance(x, (ast.For, ast.comprehension)):
            for y in ast.walk(x.target):
                if isinstance(y, ast.Name): each.add(num(y.id))
    for n in sorted(made): IN[n].append(f'made in {here}')
    for n in sorted(into - made): IN[n].append(f'made in {here}')
    for n in sorted(each): IN[n].append(f'one after one in {here}')
assert all(IN[n] for n in N)
ORD = ['first', 'second', 'third', 'fourth']
FORM = {n: format(((n - 1) % 16) ^ (((n - 1) % 16) >> 1), '04b') for n in N}   # four parities, one changing with each name; 17's are 1's again
STEP = {}
for n in range(1, 17):
    ch = [4 - k for k in range(4) if FORM[n][k] != FORM[n + 1][k]]; assert len(ch) == 1; STEP[n] = ORD[ch[0] - 1]
assert [ORD.index(STEP[n]) + 1 for n in range(1, 17)] == [1, 2, 1, 3, 1, 2, 1, 4] * 2   # as the working v401atom's form, gathered
PARITY = {'co': 'me-parity', 'bi': 'both-parity', 'tri': 'all-parity'}
alike = {}
for a in DUAL:
    for b in DUAL:
        if a != b and DUAL[a] == DUAL[b]: alike[a] = b

# --- the planes, a candidate: a rectangle by each root of three, a height by each four-cycling
phi = (1 + 5 ** 0.5) / 2
RECT = {1: lambda s, t: (0, s, t * phi), 2: lambda s, t: (s, t * phi, 0), 3: lambda s, t: (t * phi, 0, s)}   # R1, R2, R3 of Exhibit TWENTY
PLANE = {1: 'existing with discovering: 1, 5, 9, 13', 2: 'possibling: 2, 6, 10, 14, parity\'s unit square', 3: 'observing: 3, 7, 11, 15'}
HEIGHT = {0: 'outer, first four-cycling', 1: 'inner, second four-cycling', 2: 'inner, third four-cycling', 3: 'outer, fourth four-cycling'}
SIGNS = {0: (1, 1), 1: (-1, 1), 2: (1, -1), 3: (-1, -1)}   # heights 1 + phi, phi - 1, 1 - phi, -1 - phi
XYZ = {n: RECT[n % 4](*SIGNS[(n - 1) // 4]) for n in range(1, 17) if n % 4}
dist = lambda a, b: sum((x - y) ** 2 for x, y in zip(XYZ[a], XYZ[b])) ** 0.5
same = lambda x, y: abs(x - y) < 1e-9
def inside(m, k):   # a point within the rectangle of one root of the three
    ext = [max(abs(XYZ[k + 4 * j][i]) for j in range(4)) for i in range(3)]
    return all(abs(m[i]) < 1e-9 if ext[i] < 1e-9 else abs(m[i]) < ext[i] - 1e-9 for i in range(3))
turn = lambda p: (p[2], p[0], p[1])   # a right-hand turn of a third about the line along (1, 1, 1): x onto y, y onto z, z onto x
CHECKS = [
    ('each four-cycling\'s three names, existing or discovering, possibling, observing, are one triangle at one height',
     all(same(sum(XYZ[4 * j + 1]), sum(XYZ[4 * j + k])) for j in range(4) for k in (2, 3))),
    ('each rectangle\'s along sides are through its next rectangle, each passing forward: existing with discovering through possibling, possibling through observing, observing through existing',
     all(inside(tuple((x + y) / 2 for x, y in zip(XYZ[a], XYZ[b])), k % 3 + 1) for k in (1, 2, 3) for a, b in ((k, k + 8), (k + 4, k + 12)))),
    ('a right-hand turn of a third about the line brings each rectangle onto the one through it: each name of the three onto the name it is after, and the first onto the third',
     all(all(same(x, y) for x, y in zip(turn(XYZ[4 * j + k % 3 + 1]), XYZ[4 * j + k])) for j in range(4) for k in (1, 2, 3))),
    ('a turn the other way brings each name of the three onto its next name, and the third onto the first',
     all(all(same(x, y) for x, y in zip(turn(turn(XYZ[4 * j + k])), XYZ[4 * j + k % 3 + 1])) for j in range(4) for k in (1, 2, 3))),
    ('the outer two triangles are of side 2 and the inner two of side 2 phi, as Exhibit TWENTY Natural Naming has them',
     all(same(dist(4 * j + 1, 4 * j + 2), 2 if j in (0, 3) else 2 * phi) for j in range(4))),
    ('parity\'s unit square, Exhibit ONE Natural Resolver: its two across edges, 6 to 2 and 10 to 14, are each 2, a rectangle\'s across',
     same(dist(6, 2), 2) and same(dist(10, 14), 2)),
    ('its two edges 8 apart, 2 with 10 and 6 with 14, are each 2 phi, a rectangle\'s along',
     same(dist(2, 10), 2 * phi) and same(dist(6, 14), 2 * phi)),
    ('its diagonals, 2 with 14 and 6 with 10, are each through its centre, the corus',
     all(same(x, -y) for a, b in ((2, 14), (6, 10)) for x, y in zip(XYZ[a], XYZ[b]))),
    ('with each root of the three, 4 apart on one side of the corus is across, 8 apart is along, and its two diagonals are through the corus',
     all(same(dist(k, k + 4), 2) and same(dist(k + 8, k + 12), 2) and same(dist(k, k + 8), 2 * phi) and same(dist(k + 4, k + 12), 2 * phi)
         and all(same(x, -y) for a, b in ((k, k + 12), (k + 4, k + 8)) for x, y in zip(XYZ[a], XYZ[b])) for k in (1, 2, 3))),
]
def plane(n):
    if n == 17: return ('a next 1', '', '', '', '')
    if n % 4 == 0: return ('same-existing: 4, 8, 12, 16, on the line of the turn', HEIGHT[(n - 1) // 4], '', '', '')
    k = n % 4; j = (n - 1) // 4
    return (PLANE[k], HEIGHT[j], NAME[n + 4 if j in (0, 2) else n - 4], NAME[n + 8 if j < 2 else n - 8], NAME[k + 4 * (3 - j)])

# --- the table
COLS = [
    ('n, a moment', 'living ONE', lambda n: n),
    ('name', 'living ONE', lambda n: NAME[n]),
    ('root', 'living ONE', lambda n: ROOT[n]),
    ('n − 1 in four binary digits', 'living ONE', lambda n: BITS[n]),
    ('four parities, one changing with each name', 'executed', lambda n: FORM[n]),
    ('the one parity of four changing, to its next name', 'executed', lambda n: STEP.get(n, 'a next 1')),
    ('odd or even', 'living ONE', lambda n: f(n, 'Parity, span').split(', ')[0]),
    ('span', 'living ONE', lambda n: f(n, 'Parity, span').split(', ', 1)[1]),
    ('this scale, 1 to 17', 'living ONE', lambda n: SC[n].get('This scale, 1 to 17', '')),
    ('co or one', 'living ONE', lambda n: CO[n]),
    ('between two or of one, with its root', 'living ONE', lambda n: OF[n]),
    ('its three: next, now, prior', 'living ONE', lambda n: THREE[n]),
    ('its next, a parity', 'an is', lambda n: PARITY[THREE[n].split('-')[0]]),
    ('its now, a parity', 'an is', lambda n: PARITY[THREE[n].split('-')[1]]),
    ('its prior, a parity', 'an is', lambda n: PARITY[THREE[n].split('-')[2]]),
    ('dual, the newest', 'floating', lambda n: DUAL[n]),
    ('dual: its first concept', 'floating', lambda n: DUAL[n].split('-and-')[0]),
    ('dual: its second concept, its next name\'s first', 'floating', lambda n: DUAL[n].split('-and-')[1]),
    ('one dual with', 'floating', lambda n: NAME[alike[n]] if n in alike else ''),
    ('four-cycling', 'living ONE', lambda n: CYC.get(n, 'a next first')),
    ('its between', 'living ONE', lambda n: BETWEEN.get(n, '')),
    ('moments of exchanging', 'living ONE', lambda n: f(n, 'Moments of exchanging')),
    ('code with its name', 'living ONE', lambda n: CODE_WITH[n]),
    ('in the code\'s lines', 'executed', lambda n: '; '.join(IN[n])),
    ('is-or-is-nots of the code on it', 'living ONE', lambda n: ' · '.join(ISNOT[n])),
    ('sides', 'living ONE', lambda n: f(n, 'Sides')),
    ('coming down', 'living ONE', lambda n: TWO[n][0]),
    ('coming up', 'living ONE', lambda n: TWO[n][1]),
    ('8 up, with next', 'living ONE', lambda n: f(n, '8 up').replace(', with next', '')),
    ('8 down', 'living ONE', lambda n: f(n, '8 down')),
    ('receiving, an odd name of a self\'s span', 'living ONE', lambda n: ODD.get(n, {}).get('Receiving', '')),
    ('giving on, 8 up', 'living ONE', lambda n: ODD.get(n, {}).get('Giving on', '')),
    ('9 less, podal within 1 to 8', 'living ONE', lambda n: f(n, '9 less').replace('podal within 1 to 8, ', '')),
    ('17 less, podal within 1 to 16', 'living ONE', lambda n: f(n, '17 less').replace('podal within 1 to 16, ', '')),
    ('its loop of four names, by 4 up and 9 less', 'living TWENTY', lambda n: LOOP4.get(n, '')),
    ('bi-folding', 'living ONE', lambda n: BF[n][0] if n in BF else ''),
    ('its bi-folding\'s looping', 'living TWENTY', lambda n: LOOPING[BF[n][0]] if n in BF else ''),
    ('its bi-folding\'s first move', 'living ONE', lambda n: BF[n][1] if n in BF else ''),
    ('on its bi-folding, to it from', 'living ONE', lambda n: BF[n][2] if n in BF else ''),
    ('on its bi-folding, from it on to', 'living ONE', lambda n: BF[n][3] if n in BF else ''),
    ('bi-foldings one apart', 'living ONE', lambda n: BF[n][4] if n in BF else ''),
    ('middle bi-folding', 'living ONE', lambda n: f(n, 'Middle bi-folding')),
    ('six-cycle', 'living ONE', lambda n: f(n, 'Six-cycle') or f(n, 'Six-cycle, two paths')),
    ('eight-cycle', 'living ONE', lambda n: f(n, 'Eight-cycle')),
    ('one move', 'living ONE', lambda n: f(n, 'One move')),
    ('co-sequencing', 'living ONE', lambda n: f(n, 'Co-sequencing')),
    ('namings among names', 'living ONE', lambda n: f(n, 'Namings')),
    ('five dimensions', 'living ONE', lambda n: f(n, 'Five dimensions')),
    ('fives: its dimension by each side', 'living ONE', lambda n: ' · '.join(FIVE[n])),
    ('a self as three', 'living ONE', lambda n: f(n, 'A self as three')),
    ('bi-coupling', 'living ONE', lambda n: f(n, 'Bi-coupling')),
    ('parity\'s unit square and triangles', 'living ONE', lambda n: f(n, "Parity's unit square") or f(n, "Parity's square and triangles")),
    ('a between, 0', 'living ONE', lambda n: ' · '.join(ZERO[n])),
    ('sharing between selves', 'living ONE', lambda n: SHARE.get(n, '')),
    ('same-existing through one moment', 'living ONE', lambda n: BESIDE.get(n, '')),
    ('inhaling, exhaling, ingesting, exhausting', 'floating', lambda n: BREATH.get(n, '')),
    ('prior and next: its resolving with code', 'living ONE', lambda n: f(n, 'Prior and next')),
    ('1 to 17s inward and outward', 'living ONE', lambda n: f(n, '1 to 17s inward and outward')),
    ('the next scale inward, eight 1 to 17s', 'living ONE', lambda n: SC[n].get('a', '')),
    ('the next scale outward', 'living ONE', lambda n: SC[n].get('b', '')),
    ('even names of its span', 'living ONE', lambda n: f(n, 'Even names of a self\'s span') or f(n, 'Even names of a same-existing-society\'s span')),
    ('plane through the corus, by its root', 'floating', lambda n: plane(n)[0]),
    ('height on the line of the turn, by its four-cycling', 'floating', lambda n: plane(n)[1]),
    ('on its plane, across from it, 4 apart', 'floating', lambda n: plane(n)[2]),
    ('on its plane, along from it, 8 apart', 'floating', lambda n: plane(n)[3]),
    ('on its plane, through the corus from it', 'floating', lambda n: plane(n)[4]),
]
used = {k for n in N for k in F[n]} | {'Bi-folding'}
read = {'Parity, span', 'Sides', 'Co-sequencing', '8 up', '8 down', '9 less', '17 less', 'Bi-folding', 'Middle bi-folding', 'Six-cycle',
        'Six-cycle, two paths', 'Eight-cycle', 'One move', 'Moments of exchanging', 'Five dimensions', 'Namings', 'A self as three',
        'Bi-coupling', "Parity's unit square", "Parity's square and triangles", 'Prior and next', '1 to 17s inward and outward',
        "Even names of a self's span", "Even names of a same-existing-society's span"}
TABLE = [[c[2](n) for c in COLS] for n in N]
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n'); w.writerow([f'{c[0]} [{c[1]}]' for c in COLS]); w.writerows(TABLE)
elif WHAT == 'json':
    json.dump({'columns': [{'name': c[0], 'standing': c[1]} for c in COLS], 'rows': TABLE}, sys.stdout, ensure_ascii=False)
else:
    print(f'{len(COLS)} columns, 17 names. Each field of a name in Exhibit ONE Natural Resolver is in a column: {used <= read}' + ('' if used <= read else f' {sorted(used - read)}'))
    for k, c in enumerate(COLS, 1):
        print(f'  {k:2d}. {c[0]} [{c[1]}]: {sum(1 for r in TABLE if str(r[k - 1]).strip())} names')
    print('The planes, a candidate, each check all or none at all:')
    for label, ok in CHECKS: print(f'  {"is" if ok else "is-not"} · {label}')
    print('Through the corus from each other, each two names with their duals; a same-existing name by its height on the line:')
    for a, b in ((1, 13), (5, 9), (2, 14), (6, 10), (3, 15), (7, 11), (4, 16), (8, 12)):
        print(f'  {a} and {b}, {ROOT[a]} and {ROOT[b]}: {DUAL[a]} · {DUAL[b]}' + (': one dual' if DUAL[a] == DUAL[b] else ''))
