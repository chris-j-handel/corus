"""The instruments of the working v380L, each said before its result.
From the repository's root: python3 incoming/v380L/instruments.py
Each instrument reads Exhibit ONE's resolver as written at its newest version at the root, or the living files' own
words, and says a result at that instrument alone. A result here is a coupling partner and decides nothing."""
import re, ast, glob, itertools, os

ROOT = '.'
def newest(stem):
    fs = sorted(glob.glob(os.path.join(ROOT, stem + '_v*.md')))
    return fs[-1]
ONE = newest('Exhibit_ONE_Natural_Resolver')
src = open(ONE, encoding='utf-8').read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}; exec(code, ns)
entry = ns['_1_co_bi_tri_offering']; society = ns['_17_co_bi_tri_offering']
print('READ AT', os.path.basename(ONE))

def head(n, t): print('\nINSTRUMENT %d. %s' % (n, t))

# ---------------------------------------------------------------------------------------------------------------
head(1, "Each name's three prefixes by the numbers, its now and the two numbers before it, 17 the next 1; beside the"
        "\n   table of the seventeen names' column From, to. co is said the self, bi the other, tri the social.")
def word(n):
    n = ((n - 1) % 16) + 1
    if n % 2 == 0: return 'bi'
    return 'co' if n <= 7 else 'tri'
said = {'co': 'self', 'bi': 'other', 'tri': 'social'}
rows = re.findall(r"^\| (\d+) \| (\d+-[a-z-]+) \| ([^|]+) \| ([^|]+) \|", src, re.M)[:17]
two = whole = 0
for n, name, par, col in rows:
    n = int(n); three = [word(n), word(n - 1), word(n - 2)]
    t = [s.strip() for s in col.split(',')]; r = [said[w] for w in three]
    a = t[:2] == r[:2]; b = (t == r) if len(set(r)) == 3 else (t == r[:2])
    two += a; whole += b
    print('   %-28s by the numbers %-10s in the name %-5s | table: %-20s | first two agree %-5s | whole agrees %s'
          % (name, '-'.join(three), '-'.join(three) == '-'.join(name.split('-')[1:4]), ', '.join(t), a, b))
print('   the first two agree at %d of 17; the whole agrees, a word said twice in a name said one time at the column, at %d of 17' % (two, whole))
colm = {int(n): [x.strip() for x in c.split(',')] for n, _, _, c in rows}
opens = {n: ('other' if n % 2 == 0 else ('self' if n <= 7 else 'social')) for n in range(1, 18)}
print('   the column alone: its first entry is the self at the odd 1 to 7, the social at the odd 9 to 17 and the other at the even: %d of 17'
      % sum(colm[n][0] == opens[n] for n in colm))
print('   the column alone: its second entry is the next name\'s first entry: %d of 16, parting at %s'
      % (sum(colm[n][1] == colm[n + 1][0] for n in range(1, 17)), [n for n in range(1, 17) if colm[n][1] != colm[n + 1][0]]))

# ---------------------------------------------------------------------------------------------------------------
head(2, "One self at one sharing, one momentary: each carried parity against each offering. The parity released at 10"
        "\n   beside the parity chained at 11.")
same = cases = 0
for p in (1, -1):
    for off in ([], [p], [-p], [0], [1, -1]):
        rel, ch = entry([('s', p)], [('s', o) for o in off])
        r = dict(rel)['s']; c = dict(ch)['s']
        if r != 0: cases += 1; same += (r == c)
        print('   carried %+d | offered %-8s | released %+d | chained next %+d | %s'
              % (p, off, r, c, 'the zero released, the carrying carried on' if r == 0 else 'the release is the next carrying: %s' % (r == c)))
print('   at each changing the release is the next carrying: %d of %d' % (same, cases))
print('   the zero, at each cell: the offerings surfaced at 14 beside the parity chained')
for c, off in (([('s', 1)], [1, 1]), ([('s', 1)], [0, 1]), ([('s', 1)], [1, 1, -1]), ([], [1, -1]), ([], [1]), ([], [0])):
    rel, ch = entry(c, [('s', o) for o in off])
    print('   chained %-6s | offered %-11s | released %-6s | chained next %s'
          % (dict(c).get('s', 'none'), off, dict(rel).get('s', 'none'), dict(ch).get('s', 'none')))

# ---------------------------------------------------------------------------------------------------------------
head(3, "One self at one sharing, carrying +, joined to none, twelve momentaries: its releases.")
c = [('s', 1)]; out = []
for m in range(12):
    rel, c = entry(c, []); out.append(dict(rel)['s'])
print('  ', out)

# ---------------------------------------------------------------------------------------------------------------
head(4, "Societies of selves, each self at one sharing, joined as said at each line, forty-eight momentaries. At each"
        "\n   zero a self releases: the parity it released before the zero and the parity it releases after it.")
def go(n, joins, carried, offered_once=False, m=48):
    st = {i: ([('s', carried[i])] if carried.get(i) else [], []) for i in range(n)}
    if offered_once: st[0] = (st[0][0], [('s', 1)])
    rel = {i: [] for i in range(n)}
    for t in range(m):
        before = {i: dict(st[i][0]).get('s') for i in range(n)}
        st = society(st, joins)
        for i in range(n):
            now = dict(st[i][0]).get('s')
            rel[i].append(0 if (now == before[i] and before[i] is not None) else now)
    return rel
def about(seq):
    o = []
    for k, v in enumerate(seq):
        if v == 0:
            b = next((x for x in reversed(seq[:k]) if x), None); a = next((x for x in seq[k + 1:] if x), None)
            if b and a: o.append((b, a))
    return o
for name, (n, j, f, once) in {
    'two selves carrying + and +, each joined at 10 to the other': (2, {(0, 10): 1, (1, 10): 0}, {0: 1, 1: 1}, False),
    'one self carrying +, joined at 9 to itself': (1, {(0, 9): 0}, {0: 1}, False),
    'three selves carrying none, each joined at 9 to the next and the last to the first, + offered once at self 1': (3, {(i, 9): (i + 1) % 3 for i in range(3)}, {}, True),
    'five selves, the same joining and offering': (5, {(i, 9): (i + 1) % 5 for i in range(5)}, {}, True),
    'seven selves, the same joining and offering': (7, {(i, 9): (i + 1) % 7 for i in range(7)}, {}, True)}.items():
    rel = go(n, j, f, once); pairs = [p for i in rel for p in about(rel[i])]
    print('   %s\n      self 1 releases %s\n      zeros between a parity and its opposite: %d of %d'
          % (name, rel[0][:12], sum(b == -a for b, a in pairs), len(pairs)))

# ---------------------------------------------------------------------------------------------------------------
head(5, "The resolver's own lines. A line is one simple statement, or the opening of a for, an if or a def. For each"
        "\n   pair of names among 1 to 16: is there one line both are at. The sixteen joinings of the four four-cycles"
        "\n   beside the one hundred four other pairs.")
tree = ast.parse(code)
def nums(node):
    s = set()
    for x in ast.walk(node):
        nm = getattr(x, 'id', None) or getattr(x, 'arg', None) or (x.name if isinstance(x, ast.FunctionDef) else None)
        if isinstance(nm, str):
            m = re.match(r'_(\d+)_', nm)
            if m: s.add(int(m.group(1)))
    return s
lines = []
def visit(st):
    if isinstance(st, ast.For):
        lines.append(nums(st.target) | nums(st.iter)); [visit(b) for b in st.body]
    elif isinstance(st, ast.If):
        lines.append(nums(st.test)); [visit(b) for b in st.body + st.orelse]
    elif isinstance(st, ast.FunctionDef):
        lines.append({int(re.match(r'_(\d+)_', a.arg).group(1)) for a in st.args.args} | {int(re.match(r'_(\d+)_', st.name).group(1))})
        [visit(b) for b in st.body]
    elif isinstance(st, (ast.Assign, ast.Return, ast.Expr)):
        lines.append(nums(st))
for st in tree.body: visit(st)
co = set()
for s in lines:
    for a, b in itertools.combinations(sorted(s), 2): co.add((a, b))
cyc = [[1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12]]
L = {(min(c[i], c[(i + 1) % 4]), max(c[i], c[(i + 1) % 4])) for c in cyc for i in range(4)}
rest = [p for p in itertools.combinations(range(1, 17), 2) if p not in L]
print('   joinings of the four four-cycles at one line: %d of %d' % (sum(p in co for p in L), len(L)))
print('   other pairs of names among 1 to 16 at one line: %d of %d' % (sum(p in co for p in rest), len(rest)))

# ---------------------------------------------------------------------------------------------------------------
head(6, "Exhibit ONE's own labels: at the table of the seventeen names a face outward or inward and a connector's"
        "\n   facing; at the resolver's table of connectors each connector's own word.")
full = re.findall(r"^\| (\d+) \| (\S+) \| ([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", src, re.M)[:17]
faces = {int(n): oi.strip() for n, _, _, _, kind, _, oi, _ in full if oi.strip() in ('outward', 'inward')}
print('   faces outward:', sorted(n for n in faces if faces[n] == 'outward'), '| faces inward:', sorted(n for n in faces if faces[n] == 'inward'))
print('   outward is a name of 1 to 8 and inward a name of 9 to 16: %d of %d; each inward 8 up from an outward: %s'
      % (sum((faces[n] == 'outward') == (n < 9) for n in faces), len(faces),
         sorted(n + 8 for n in faces if faces[n] == 'outward') == sorted(n for n in faces if faces[n] == 'inward')))
conn = {int(n): f.strip() for n, _, _, _, kind, _, _, f in full if kind.strip() == 'connector'}
for n in sorted(conn): print('   connector %2d  the table: %-22s the resolver: %-22s %s' % (n, conn[n], ns['CONNECTORS'][n][1], ns['CONNECTORS'][n][2]))
print('   the resolver\'s joins:', ns['JOINS'])

# ---------------------------------------------------------------------------------------------------------------
head(7, "The numbers alone. Each joining of each form of Exhibit ONE's table of forms, two ways: at the table's own"
        "\n   numbers, the joinings going to a lower number; and with 17 the next 1, each taken going up, from a to b"
        "\n   b less a on the round of sixteen.")
forms = {'four-cycle': cyc, 'middle four-cycle': [[9, 5, 12, 8], [7, 11, 6, 10]],
         'six-cycle': [[1, 9, 5, 12, 8, 16], [2, 15, 7, 11, 6, 10], [3, 11, 7, 10, 6, 14], [4, 13, 5, 9, 8, 12]],
         'eight-cycle': [[1, 9, 5, 13, 4, 12, 8, 16], [2, 15, 7, 11, 3, 14, 6, 10]]}
for k, v in forms.items():
    for c in v:
        ups = [(c[(i + 1) % len(c)] - c[i]) % 16 for i in range(len(c))]
        low = sum(c[(i + 1) % len(c)] < c[i] for i in range(len(c)))
        print('   %-18s %-22s to a lower number %d of %d | up by %-30s whole %d' % (k, '-'.join(map(str, c)), low, len(c), ups, sum(ups)))
print('   the joins: 10 to 14 up %d, 9 to 17 up %d, 6 to 2 up %d; 11 to the next 3 up %d' % ((14 - 10) % 16, 8, (2 - 6) % 16, (3 - 11) % 16))

# ---------------------------------------------------------------------------------------------------------------
head(8, "Two selves each carrying + at one sharing; one join from self 1 to self 2, at 6, at 10 or at 9, one at a"
        "\n   time; six momentaries: the receiving self's carrying.")
for k in (6, 10, 9):
    st = {0: ([('s', 1)], []), 1: ([('s', 1)], [])}; o = []
    for t in range(6):
        st = society(st, {(0, k): 1}); o.append(dict(st[1][0])['s'])
    print('   join at %2d: %s' % (k, o))

# ---------------------------------------------------------------------------------------------------------------
head(9, "The resolver's three functions: the names at the entry's lines alone, at the society's lines alone, at both.")
at = {}
for fn in [x for x in tree.body if isinstance(x, ast.FunctionDef)]:
    s = set()
    for x in ast.walk(fn):
        nm = getattr(x, 'id', None) or getattr(x, 'arg', None)
        if isinstance(nm, str) and re.match(r'_(\d+)_', nm): s.add(int(re.match(r'_(\d+)_', nm).group(1)))
    at[int(re.match(r'_(\d+)_', fn.name).group(1))] = s
one_, soc_ = at[1], at[9] | at[17] | {9, 17}
print('   at the entry alone:', sorted(one_ - soc_ - {1}), '| at the society alone:', sorted(soc_ - one_ - {1}), '| at both:', sorted((one_ & soc_) - {1}))
for l in code.split('\n'):
    if ('for _13' in l and '_10_' in l) or '_5_co_bi_co_competencing[' in l or ('for _4' in l and '_9_tri' in l): print('   ' + l.strip()[:118])

# ---------------------------------------------------------------------------------------------------------------
head(10, "Two selves each carrying + at one sharing, one momentary: the offerings arriving next at each self, at no join"
         "\n   and at one join from self 1 to self 2 at 10.")
st = society({0: ([('s', 1)], []), 1: ([('s', 1)], [])}, {})
print('   no join: ', {k + 1: v[1] for k, v in st.items()})
st = society({0: ([('s', 1)], []), 1: ([('s', 1)], [])}, {(0, 10): 1})
print('   one join:', {k + 1: v[1] for k, v in st.items()})

# ---------------------------------------------------------------------------------------------------------------
head(11, "The living files at the root, each at its newest version: the places of each word, each a whole word.")
living = {}
for f in glob.glob(os.path.join(ROOT, '*_v*.md')):
    m = re.match(r'(.+?)_v(\d+)([a-z]?)\.md$', os.path.basename(f))
    if m and (m.group(1) not in living or f > living[m.group(1)]): living[m.group(1)] = f
texts = {k: open(v, encoding='utf-8').read() for k, v in living.items()}
for label, pat in (('side, sides', r'\bsides?\b'), ('step, steps, stepping, stepped', r'\bstep(s|ping|ped)?\b'), ('beat, beats, beating', r'\bbeat(s|ing)?\b'),
                   ('nought', r'\bnought\b'), ("the self's span, the society's span", r"\b(self|society)'s span\b"),
                   ('wound, winding, windings', r'\b(wound|windings?)\b'), ('far side', r'\bfar side\b')):
    n = {k: len(re.findall(pat, t, re.I)) for k, t in texts.items()}
    print('   %-38s %5d places at %2d of %d files' % (label, sum(n.values()), sum(1 for v in n.values() if v), len(n)))

# ---------------------------------------------------------------------------------------------------------------
head(12, "The resolver's functions: each name as received, a parameter of the function or a part of one read at a for,"
         "\n   or as made, assigned within the function. Beside each even name its three prefixes.")
def names_in(node):
    return sorted({int(re.match(r'_(\d+)_', n.id).group(1)) for n in ast.walk(node) if isinstance(n, ast.Name) and re.match(r'_(\d+)_', n.id)})
for fn in [x for x in tree.body if isinstance(x, ast.FunctionDef)]:
    me = int(re.match(r'_(\d+)_', fn.name).group(1))
    params = [int(re.match(r'_(\d+)_', a.arg).group(1)) for a in fn.args.args]
    made, read_from = set(), {}
    for n in ast.walk(fn):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                for base in (t.elts if isinstance(t, ast.Tuple) else [t]):
                    while isinstance(base, ast.Subscript): base = base.value
                    if isinstance(base, ast.Name) and re.match(r'_(\d+)_', base.id): made.add(int(re.match(r'_(\d+)_', base.id).group(1)))
        if isinstance(n, (ast.For, ast.comprehension)):
            src_names = [x for x in names_in(n.iter)]
            for t in names_in(n.target): read_from.setdefault(t, set()).update(src_names)
    print('   at %d: received as parameters %s | made %s' % (me, params, sorted(made)))
    for t in sorted(read_from): print('      %2d is read at a for from %s' % (t, sorted(read_from[t] - {t})))
print('   the even names: ' + '; '.join('%d %s' % (n, '-'.join([word(n), word(n - 1), word(n - 2)])) for n in range(2, 17, 2)))

# ---------------------------------------------------------------------------------------------------------------
head(13, "The resolver's own conditions, each if with the names at it; and societies followed two ways, the zero"
         "\n   delivered at a join as written, and the zero held at the join, a parity alone passing. Random societies:"
         "\n   two to six selves, one to three sharings, joins at 6, 10 and 9 at random, carryings and first offerings"
         "\n   at random, twenty-four momentaries each.")
for fn in [x for x in tree.body if isinstance(x, ast.FunctionDef)]:
    me = int(re.match(r'_(\d+)_', fn.name).group(1))
    for n in ast.walk(fn):
        tests = [n.test] if isinstance(n, ast.If) else (n.ifs if isinstance(n, ast.comprehension) else [])
        for t in tests: print('   at %2d, a condition at the names %s' % (me, names_in(t)))
import random
random.seed(380)
def strip(st): return {k: (v[0], [o for o in v[1] if o[1] != 0]) for k, v in st.items()}
same = both = lone = total = changings = 0
for trial in range(2000):
    n = random.randint(2, 6); sh = ['s%d' % i for i in range(random.randint(1, 3))]
    joins = {}
    for i in range(n):
        for k in (6, 10, 9):
            if random.random() < 0.4: joins[(i, k)] = random.randrange(n)
    st = {i: ([(s, random.choice((1, -1))) for s in sh if random.random() < 0.7],
              [(s, random.choice((1, -1))) for s in sh if random.random() < 0.3]) for i in range(n)}
    a, b, ok = st, st, True
    for m in range(24):
        for i in range(n):
            rel, ch = entry(a[i][0], a[i][1]); before = dict(a[i][0])
            for s, r in rel:
                chained_changed = dict(ch).get(s) != before.get(s)
                total += 1; changings += (r != 0)
                both += (r != 0 and chained_changed); lone += ((r != 0) != chained_changed)
        a = society(a, joins); b = strip(society(b, joins))
        ok = ok and all(dict(a[i][0]) == dict(b[i][0]) for i in range(n))
    same += ok
print('   the zero held at the join: each self\'s carrying the same at each momentary at %d of 2000 societies' % same)
print('   of %d releases, %d a parity; released a parity and the chained parity changed, together: %d; one without the other: %d'
      % (total, changings, both, lone))
