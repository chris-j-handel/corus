"""Natural Intelligence with Exhibit ONE, its next version sized. Reads the files and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/next_version_sized.py <root>

A. The opening at its newest as one sequence is read by `incoming/v404chaining/instruments/the_opening_as_one_sequence.py`,
   the newer one and the one whole with each case: each line after the line of each name in it, each circle, a
   candidate order whole, and each bonded name with no line of its own. This instrument's first part is away
   with it, newer alone. By v404chaining's second hand its lines found a name with *parity* by its many alone,
   and had *other* of line 1, a plain word, as a name.
B. The six parts of the living version after its opening, Exhibit ONE read at Exhibit ONE: each prose sentence by the
   kinds found by word forms. A sentence is of each kind found in it. A number of a kind is a number of sentences
   to read, and no reading of them.

Returned at main, Merge #695, 15 November 2026, its part B, and the same at main after Merge #838:
  B. 1,405 sentences: ONE 148, TWO 138, THREE 179, FOUR 536, FIVE 152, SIX 252.
     by a name whose own sentence in the opening is an is-or-is-not?: 966; ONE 66, TWO 80, THREE 116, FOUR 389, FIVE 109, SIX 206
     by a name of the code, a number 1 to 17 alone or in a name, or the resolver or the code: 312; ONE 4, TWO 19, THREE 52, FOUR 172, FIVE 28, SIX 37
     by self-parity or social-parity: 15; by other-parity: 7
     word for word a sentence of the opening: 11
     by none of these: 346; ONE 81, TWO 52, THREE 45, FOUR 91, FIVE 38, SIX 39
"""
import collections, contextlib, glob, io, os, re, runpy, sys

R = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
sys.argv = [os.path.join(here, 'opening_base.py'), R]
with contextlib.redirect_stdout(io.StringIO()):
    base = runpy.run_path(os.path.join(here, 'opening_base.py'))
pats, name_at, three, sent, plain = base['pats'], base['name_at'], base['three'], base['sent'], base['plain']

# B. the six parts
ni = open(max(glob.glob(os.path.join(R, 'Natural_Intelligence_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
body = ni[ni.find('\n---\n'):]
x = body.find('# EXHIBIT ONE · NATURAL RESOLVER'); y = body.find('\n# FOUR · RESOLVING')
if 0 < x < y: body = body[:x] + body[y:]
opening = {plain(s).strip() for s in sent.values()}
open_names = {k: v for k, v in name_at.items() if three[v] != 'is' and k != 'momentary'}
part = None; S = []; fence = False
for l in body.split('\n'):
    if l.startswith('```'): fence = not fence; continue
    h = re.match(r'^# (ONE|TWO|THREE|FOUR|FIVE|SIX) · ', l)
    if h: part = h.group(1); continue
    if fence or l.startswith('#') or l.startswith('|') or not l.strip() or l.strip() == '---': continue
    s = plain(re.sub(r'^[-*]\s+|^\d+\.\s+', '', l.strip()))
    S += [(part, p) for p in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9"“(])', s) if len(p.split()) >= 4]
kinds = collections.OrderedDict([
    ('by a name whose own sentence in the opening is an is-or-is-not?', lambda s: any(pats[k].search(s) for k in open_names)),
    ('by a name of the code, a number 1 to 17 alone or in a name, or the resolver or the code', lambda s: bool(re.search(r'\b\d{1,2}-(now|next)-|\bresolver\b|\bthe code\b|(?<![\w.-])(1[0-7]|[1-9])(?![\w.,-]| (to|of|and)\b)', s))),
    ('by self-parity or social-parity', lambda s: bool(re.search(r'(?<![\w-])(self-parity|social-parity)(?![\w-])', s, re.I))),
    ('by other-parity', lambda s: bool(re.search(r'(?<![\w-])(other-parity|other-than-parity|universal-parity)(?![\w-])', s, re.I))),
    ('word for word a sentence of the opening', lambda s: s.strip() in opening),
])
parts = collections.Counter(p for p, _ in S)
print('B. the six parts:', len(S), 'sentences;', ', '.join(f'{p} {parts[p]}' for p in ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']))
found = collections.Counter(); by_part = collections.defaultdict(collections.Counter); none = collections.Counter()
for p, s in S:
    ks = [k for k, f in kinds.items() if f(s)]
    for k in ks: found[k] += 1; by_part[k][p] += 1
    if not ks: none[p] += 1
for k in kinds: print(f'   {found[k]:5d}  {k}   ' + ' '.join(f'{p} {by_part[k][p]}' for p in ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']))
print(f'   {sum(none.values()):5d}  by none of these   ' + ' '.join(f'{p} {none[p]}' for p in ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']))
