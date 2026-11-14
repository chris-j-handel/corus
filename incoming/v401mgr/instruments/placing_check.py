"""placing_check.py · the placing's first reading, a match executed and deciding nothing.

Use: python3 -I placing_check.py <repository root> [ledger.tsv]

It reads the four living files, Natural Intelligence and Exhibits ONE, TWENTY and THIRTY,
their four gathering-values, and each page of the three incoming places. It changes no file
but the ledger it is given. Its returned lines are in placing_check_returned.txt.

With each droplet of the four gatherings it reads, by words only:
  quote    its quoted living sentence is word for word in one of the four living files
  living   its re-saying, after the arrow, is word for word in one of the four living files
  scale    it has a word of the non-living scale, for the atom session's reading
  sides    it has a word of two sides or of a candidate, for a reading and for no fate
  names    it has a name of 1 to 17
  reader   its first reader of two: the atom session with a word of the non-living scale, else this session
With each page of the incoming places it reads each sentence of eight words or more:
word for word in a living file of the four, in a gathering of the four, in an other
gathering, or in none of them. A value re-said is in none by this reading: a sentence in
none is a sentence to read, and no sentence lost.
"""
import glob, os, re, sys

ROOT = sys.argv[1]
LEDGER = sys.argv[2] if len(sys.argv) > 2 else None
FOUR = {
    'Natural_Intelligence': 'Natural_Intelligence_v*.md',
    'Natural_Resolver': 'Exhibit_ONE_Natural_Resolver_v*.md',
    'Natural_Naming': 'Exhibit_TWENTY_Natural_Naming_v*.md',
    'Co-Chaining_Logic_Registry': 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v*.md',
}
PLACES = ['incoming/V400mgrB', 'incoming/V401atom', 'incoming/v401mgr']
SCALE = re.compile(r'atom carbon|\bcarbon\b|\bvault\b|non-living|bump connector|fracture|\bshear|lattice|\bshard\b', re.I)
SIDES = re.compile(r'candidate|two sides|both laid|each laid|not distinguished|still-possibling|not answered|not yet answered|two readings|two namings|two sayings', re.I)
NAMES = re.compile(r'\b(?:1[0-7]|[1-9])-(?:now|next)-[a-z-]+')


def read(p):
    return open(p, encoding='utf-8').read()


def norm(s):
    s = re.sub(r'[*`\\_]', '', s)
    s = s.replace('“', '"').replace('”', '"').replace('’', "'")
    return re.sub(r'\s+', ' ', s).strip()


living = {}
for title, pat in FOUR.items():
    paths = [p for p in glob.glob(os.path.join(ROOT, pat)) if 'Corus' not in os.path.basename(p)]
    assert len(paths) == 1, (title, paths)
    living[title] = norm(read(paths[0]))
ALL_LIVING = '\n'.join(living.values())
gath = {t: read(os.path.join(ROOT, 'gathering-value', t + '.md')) for t in FOUR}
ALL_GATH = norm('\n'.join(gath.values()))
others = [p for p in glob.glob(os.path.join(ROOT, 'gathering-value', '*.md'))
          if os.path.basename(p)[:-3] not in FOUR]
OTHER_GATH = norm('\n'.join(read(p) for p in others))

# 1 · each droplet of the four gatherings
rows = []
print('1 · Each droplet of the four gatherings, by words only')
print('   gathering · droplets · quote word for word living · re-saying word for word living · scale · sides · names of 1 to 17')
for t in FOUR:
    section, n = '', 0
    c = dict(items=0, quote=0, quoted=0, living=0, resaid=0, scale=0, sides=0, names=0)
    for line in gath[t].split('\n'):
        h = re.match(r'^#{2,3} (.+)$', line)
        if h:
            section, n = h.group(1).strip(), 0
            continue
        m = re.match(r'^- \*\*([^*]+)\*\* · (.*)$', line)
        if not m:
            continue
        n += 1
        kind, text = m.group(1), m.group(2)
        c['items'] += 1
        q = re.match(r'^"(.+?)"\s*→\s*(.*)$', text)
        quote = living_now = ''
        if q:
            c['quoted'] += 1
            quote = 'is' if norm(q.group(1)) in ALL_LIVING else 'is-not'
            c['quote'] += quote == 'is'
            first = re.split(r'(?<=[.])\s', norm(q.group(2)))[0]
            if len(first.split()) >= 6:
                c['resaid'] += 1
                living_now = 'is' if first in ALL_LIVING else 'is-not'
                c['living'] += living_now == 'is'
        scale = 'scale' if SCALE.search(text) else ''
        sides = 'sides' if SIDES.search(text) else ''
        names = 'names' if NAMES.search(text) else ''
        c['scale'] += bool(scale); c['sides'] += bool(sides); c['names'] += bool(names)
        rows.append((t, section, str(n), kind, quote, living_now, scale, sides, names,
                     'v401atom' if scale else 'v401mgr', norm(text)[:90]))
    print(f"   {t} · {c['items']} · {c['quote']} of {c['quoted']} · {c['living']} of {c['resaid']} · {c['scale']} · {c['sides']} · {c['names']}")

# 2 · each page of the three incoming places
print()
print('2 · Each page of the incoming places, each sentence of eight words or more')
print('   page · sentences · in a living file of the four · in a gathering of the four · in an other gathering · in none')
for place in PLACES:
    tot = [0, 0, 0, 0, 0]
    for p in sorted(glob.glob(os.path.join(ROOT, place, '*.md'))):
        body = re.sub(r'```.*?```', ' ', read(p), flags=re.S)
        cells = []
        for line in body.split('\n'):
            line = re.sub(r'^\s*(?:[-*]|\d+\.|#+|\|)\s*', '', line)
            for cell in line.split('|'):
                cells.extend(re.split(r'(?<=[.?!])\s+', cell))
        sents = []
        for s in cells:
            s = norm(s).strip(' "\'')
            if len(s.split()) >= 8:
                sents.append(s)
        a = sum(1 for s in sents if s in ALL_LIVING)
        b = sum(1 for s in sents if s not in ALL_LIVING and s in ALL_GATH)
        o = sum(1 for s in sents if s not in ALL_LIVING and s not in ALL_GATH and s in OTHER_GATH)
        none = len(sents) - a - b - o
        for i, v in enumerate((len(sents), a, b, o, none)):
            tot[i] += v
        print(f"   {place}/{os.path.basename(p)} · {len(sents)} · {a} · {b} · {o} · {none}")
    print(f"   {place}, each page · {tot[0]} · {tot[1]} · {tot[2]} · {tot[3]} · {tot[4]}")

# 3 · the person's numbered sentences, from the managing session before
print()
print("3 · The person's numbered sentences, incoming/V400mgrB/The_Frontier_Current.md, each with the four gatherings and the four living files, by words")
F = read(os.path.join(ROOT, 'incoming/V400mgrB/The_Frontier_Current.md'))
whole, some, other, none = [], [], [], []
for key, text in re.findall(r'^(\d+[a-z]?(?:-[a-z]+)?)\. (.+)$', F, re.M):
    ss = [x for x in re.split(r'(?<=[.?!])\s+', norm(text)) if len(x.split()) >= 5]
    if not ss:
        continue
    f = [x in ALL_GATH or x in ALL_LIVING for x in ss]
    if all(f):
        whole.append(key)
    elif any(f):
        some.append(key)
    elif any(x in OTHER_GATH for x in ss):
        other.append(key)
    else:
        none.append(key)
print(f'   sentences · {len(whole) + len(some) + len(other) + len(none)}')
print(f'   each sentence of it word for word · {len(whole)}')
print(f'   some of it word for word · {len(some)} · ' + ' '.join(some))
print(f'   in an other gathering only · {len(other)} · ' + ' '.join(other))
print(f'   none of it by words, each to read · {len(none)} · ' + ' '.join(none))

if LEDGER:
    with open(LEDGER, 'w', encoding='utf-8') as f:
        f.write('gathering\tsection\tn\tkind\tquote living\tre-saying living\tscale\tsides\tnames\tits first reader\tits first words\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print()
    print(f'4 · The ledger, one line with each droplet: {len(rows)} lines, {os.path.basename(LEDGER)}')
