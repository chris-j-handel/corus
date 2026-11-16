"""A naming of Exhibit ONE's code, executed with the code as it is: the same, or other. Reads Exhibit ONE Natural
Resolver's living version and each file of the set, executes, and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/a_naming_of_the_code_executes_the_same.py <root>

1. The code as it is, and the same code with each of its names by one map, three maps: a name as its number and its
   dual; as its number, its dual and its root; and as its dual and its root with no number. The duals are the newest
   seventeen, a candidate. Each is executed with the same societies: selves, sharings, priors, parities arriving,
   and couplings with 6, 10 and 9, by one seed, moment by moment, and each next of the two is read together.
2. Each dual read with Exhibit ONE's table: its two concepts by kind, its root, co or one, and its three.
3. The places of a name of the seventeen across the set, a name in a sentence and a name of the code: each place
   of a naming of the code, all or none at all.
4. Sentences of Exhibit ONE Natural Resolver explaining by a name's own word, *now*, *next* or *co*: each for a
   reading, by no map.

Returned at main, Merge #719, 15 November 2026:
  1. 17 names in the code's lines. A name as its number and its dual, and as its number, its dual and its root:
     no two alike; 3,000 societies, 25,675 moments, each next the same as the code's. A name as its dual and its
     root with no number: alike 4 with 16, 7 with 11, and 8 with 12; 7 with 11 together inside the code's
     function of 1-now-existing, and 4 with 16 inside its function of 17-next-existing; a next other than the
     code's with 2,998 of 3,000 societies.
  2. Each odd name's dual is from one of same, other, no-other to one of now, not-now, prior, not-prior, next,
     and each even name's from one of the five to one of the three. A root read out of its dual is the table's
     root with 17 of 17. 4 and 16, 7 and 11, 8 and 12: each two are a co name with a name of one, and the threes
     of each two are other at one of next, now, prior only: co and tri.
  3. living files: 3,285 places of a name in a sentence, in 23, and 254 of a name of the code, in 5.
     gathering files: 1,443 in 33, and 25 in 4. incoming pages and instruments, this one not with them: 46 in 7,
     and 11 in 3. kits: 445 in 1, a version of Exhibit ONE Natural Resolver waiting, and 75 in 2. In the living
     files a name of 9 to 16, each with next as its own word, is in 1,696 places, and 17-next-existing in 136.
  4. 28 sentences of Exhibit ONE Natural Resolver explain by a name's own word, now, next or co.
"""
import glob, json, os, random, re, sys

R = sys.argv[1]
one = open(max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')),
               key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
code = one.split('```python', 1)[1].split('```', 1)[0]
DUAL = {1: 'same-and-now', 2: 'now-and-other', 3: 'other-and-prior', 4: 'prior-and-same', 5: 'same-and-prior',
        6: 'prior-and-no-other', 7: 'no-other-and-not-prior', 8: 'not-prior-and-same', 9: 'same-and-not-now',
        10: 'not-now-and-no-other', 11: 'no-other-and-not-prior', 12: 'not-prior-and-same', 13: 'same-and-not-prior',
        14: 'not-prior-and-no-other', 15: 'no-other-and-prior', 16: 'prior-and-same', 17: 'same-and-next'}
rows = re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|', one, re.M)
assert len(rows) == 17
NAME = {int(n): nm for n, nm, *_ in rows}; ROOT = {int(n): r.split(',')[0].strip() for n, _, r, *_ in rows}
CO = {int(n): c.strip() for n, _, _, _, c, _ in rows}; THREE = {int(n): t.strip() for *_, t in [(r[0], r[5]) for r in rows] for n in [_[0]]}
def with_root(n):   # a dual ending with same, with the root same-existing: same said once
    return DUAL[n] + '-existing' if DUAL[n].endswith('-same') and ROOT[n] == 'same-existing' else DUAL[n] + '-' + ROOT[n]
old = sorted(set(re.findall(r'_(?:1[0-7]|[1-9])_[a-z_]+', code)), key=lambda s: int(s.split('_')[1]))
num = lambda o: int(o.split('_')[1])
maps = {'its number and its dual': {o: f'_{num(o)}_' + DUAL[num(o)].replace('-', '_') for o in old},
        'its number, its dual and its root': {o: f'_{num(o)}_' + with_root(num(o)).replace('-', '_') for o in old},
        'its dual and its root, no number': {o: '_' + with_root(num(o)).replace('-', '_') for o in old}}

def societies(count):
    rng = random.Random(403)
    for s in range(count):
        selves = [f's{i}' for i in range(rng.randint(1, 7))]; keys = ['k', 'm', 'n'][:rng.randint(1, 3)]
        state = {x: ([(k, rng.choice([1, -1])) for k in keys if rng.random() < 0.7],
                     [(rng.choice(keys), rng.choice([1, -1, 0])) for _ in range(rng.randint(0, 4))]) for x in selves}
        five = {(x, n): rng.choice(selves) for x in selves for n in (6, 10, 9) if rng.random() < 0.6}
        yield state, five, rng.randint(1, 16)

a = {}; exec(code, a); fa = a['_17_next_existing']
print(f'1. {len(old)} names in the code\'s lines. The code as it is with the same code by a naming, 3000 societies:')
for label, m in maps.items():
    alike = sorted(sorted(num(o) for o in old if m[o] == v) for v in set(m.values()) if list(m.values()).count(v) > 1)
    moments = other = 0
    try:
        b = {}; exec(re.sub(r'_(?:1[0-7]|[1-9])_[a-z_]+', lambda x: m[x.group(0)], code), b); fb = b[m['_17_next_existing']]
        for state, five, span in societies(3000):
            sa = sb = state
            try:
                for _ in range(span):
                    sa = fa(sa, five); sb = fb(sb, five); moments += 1
                    if repr(sa) != repr(sb): raise ValueError
            except Exception: other += 1
    except Exception: other = 3000
    print(f'   a name as {label}: names alike {alike or "none"}; societies with a next other than the code\'s {other}' + (f'; {moments} moments, each next the same' if not other else ''))
parts = re.split(r'(?m)^(?=def )', code)[1:]
pairs = [[4, 16], [7, 11], [8, 12]]
print('   alike with no number, and together inside one function of the code:',
      [(NAME[int(re.match(r'def _(\d+)', f).group(1))], p) for f in parts for p in pairs if all(re.search(rf'_{n}_[a-z]', f) for n in p)])
print('   the code by its number, its dual and its root:')
for o in old: print(f'     {NAME[num(o)]:26s} {num(o)}-{with_root(num(o))}')

print('2. Each dual with Exhibit ONE\'s table.')
SAME = ('same', 'other', 'no-other'); NOW = ('now', 'not-now', 'prior', 'not-prior', 'next')
two = {n: DUAL[n].split('-and-') for n in DUAL}
print('   each odd name from one of same, other, no-other to one of now, not-now, prior, not-prior, next:', all(two[n][0] in SAME and two[n][1] in NOW for n in range(1, 18, 2)))
print('   each even name from one of now, not-now, prior, not-prior, next to one of same, other, no-other:', all(two[n][0] in NOW and two[n][1] in SAME for n in range(2, 18, 2)))
def root_by_dual(x, y):
    if x == 'same': return 'discovering' if y.startswith('not-') else 'existing'
    if x in SAME: return 'observing'
    return 'same-existing' if y == 'same' else 'possibling'
print('   a root read out of its dual, the same as the table\'s root:', sum(root_by_dual(*two[n]) == ROOT[n] for n in DUAL), 'of 17')
print('     same with now, prior or next: existing. same with not-now or not-prior: discovering. other or no-other first: observing.')
print('     other or no-other second: possibling. same second: same-existing.')
for p, q in pairs:
    d = [(i, x, y) for i, (x, y) in enumerate(zip(THREE[p].split('-'), THREE[q].split('-'))) if x != y]
    print(f'   {p} and {q}, {DUAL[p]}: {CO[p]} and {CO[q]}; {THREE[p]} and {THREE[q]}, other at {["next", "now", "prior"][d[0][0]]} only: {d[0][1]} and {d[0][2]}' if len(d) == 1 else f'   {p} and {q}: {d}')

said = re.compile('|'.join(re.escape(n) for n in sorted(NAME.values(), key=len, reverse=True)))
coded = re.compile(r'_(?:1[0-7]|[1-9])_(?:now|next)_[a-z_]+')
def text(p):   # this instrument is not read with them
    try: return '' if os.path.abspath(p) == os.path.abspath(__file__) else open(p, encoding='utf-8').read()
    except Exception: return ''
def places(paths):
    T = [text(p) for p in paths]; s = [len(said.findall(t)) for t in T]; c = [len(coded.findall(t)) for t in T]
    return sum(s), sum(1 for x in s if x), sum(c), sum(1 for x in c if x)
living = [os.path.join(R, f) for f in json.load(open(os.path.join(R, 'files.json')))]
print('3. the places of a name of the seventeen, in a sentence and of the code, with the files having them')
for label, paths in (('living files', living), ('gathering files', glob.glob(os.path.join(R, 'gathering-value', '*.md'))),
                     ('incoming pages and instruments', glob.glob(os.path.join(R, 'incoming', '**', '*.*'), recursive=True)),
                     ('kits', glob.glob(os.path.join(R, 'kits', '**', '*.*'), recursive=True))):
    s, fs, c, fc = places(paths); print(f'   {label}: {s} in {fs}, and {c} in {fc}')
L = ''.join(text(p) for p in living)
nine_up = sum(len(re.findall(re.escape(NAME[n]), L)) for n in range(9, 17))
print(f'   in the living files, a name of 9 to 16 in a sentence, each with next as its own word: {nine_up} places; 17-next-existing: {len(re.findall(re.escape(NAME[17]), L))}')
body = one.split('```python', 1)[0] + one.split('```', 2)[2]
S = [p for l in body.split('\n') if not l.startswith('|') for p in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9"“(*])', l)]
own = re.compile(r'\bnow-co\b|\bnext-co\b|\b(?:now|next|co) names?\b|\b[Ww]ith(?:out)? co\b|\*[Cc]o\*|\*now\*|\*next\*|with next\b')
hit = [s for s in S if own.search(said.sub('a name', s))]   # each name away first: a name's own word in the sentence's own words
print(f'4. sentences of Exhibit ONE Natural Resolver explaining by a name\'s own word, now, next or co: {len(hit)}')
for s in hit[:6]: print('    ', s.strip()[:170])
