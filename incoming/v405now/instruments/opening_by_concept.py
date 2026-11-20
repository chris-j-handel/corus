"""The opening's candidate sentences, by concept, in the window's order, each with its places and the
concepts it leans on that are named after it. Reads the JSON rows of opening_candidates.py and
opening_more.py; writes a page and a JSON outside the repository.

Usage: python3 -I opening_by_concept.py <rows.json>... --page <out.md> --json <out.json>
"""
import collections, json, re, sys

args = sys.argv[1:]
page = args[args.index('--page') + 1]
jout = args[args.index('--json') + 1]
inputs = [a for a in args[:args.index('--page')]]

B, E = r'(?<![\w-])', r'(?![\w-])'
# position, key, how it is named; the window's order, then the live lines, then the loop of parity and on
C = [
    (1, 'now', r'now(?:[- ]moments?)?'),
    (2, 'now-existing', r'now-existing'),
    (3, 'universe', r'universes?'),
    (4, 'prior', r'prior(?:[- ]moments?)?'),
    (5, 'prior-existing', r'prior-existing'),
    (6, 'next', r'next(?:[- ]moments?)?'),
    (7, 'next-existing', r'next-existing'),
    (8, 'same-existing', r'same-existing'),
    (9, 'next-and-same-existing', r'next-and-same-existing'),
    (10, 'same-named', r'same-named(?: things?)?'),
    (11, 'universal set', r'(?:named )?universal[- ]sets?'),
    (12, 'name', r'names?'),
    (13, 'other-than', r'other-than'),
    (14, 'is-or-is-not', r'is-or-is-not'),
    (15, 'observing', r'observing'),
    (16, 'possibling', r'possibling'),
    (17, 'discovering', r'discovering'),
    (18, 'self', r'(?:self|selves)'),
    (19, 'me', r'(?:me|mes)'),
    (20, 'co-intelligencing', r'co-intelligencing'),
    (21, 'living', r'living'),
    (22, 'natural intelligence', r'natural intelligence'),
    (23, 'non-living', r'non-living'),
    (24, 'stable-forming emanation', r'stable-forming emanations?'),
    (25, 'different things', r'different things?'),
    (26, 'own-parity', r'own-parity'),
    (27, 'bi-coupling', r'bi-couplings?'),
    (28, 'all-parity', r'all-parity'),
    (29, 'other', r'others?'),
    (30, 'parity', r'(?:parity|parities)'),
    (31, '0', r'0'),
    (33, 'sequence', r'sequences?'),
    (34, 'me-parity', r'me-parit(?:y|ies)'),
    (35, 'me-now', r'me-nows?'),
    (36, 'same-existing-society', r'same-existing-societ(?:y|ies)'),
    (37, 'co-chaining', r'co-chaining'),
    (38, 'geodesic', r'geodesic'),
]
POS = {k: p for p, k, _ in C}
USE = [(k, re.compile(B + r + E, re.I)) for _, k, r in C]
DEF = [(k, re.compile(r'^(?:a |an |the |two |each |one )?' + r + E, re.I)) for _, k, r in C]

clean = lambda s: re.sub(r'\s+', ' ', re.sub(r'[*_`\\]', '', s.replace('’', "'"))).strip()
key = lambda s: clean(s).lower().rstrip('.').strip()


def concept_of(raw):
    bolds = re.findall(r'\*\*([^*]+)\*\*', raw)
    for b in bolds:
        bb = clean(b).lower()
        for k, rx in DEF:
            if rx.match(bb) and rx.match(bb).end() >= len(bb) - 1:
                return k, True
    s = clean(raw)
    s = re.sub(r'^(?:For (?:a|two|each|the) [^,]+, )', '', s)
    subj = re.split(r' (?:is|are|is-or-is-not)\b', s, maxsplit=1)[0].lower()
    for k, rx in sorted(DEF, key=lambda x: -len(x[1].pattern)):
        m = rx.match(subj)
        if m and m.end() >= len(subj) - 1:
            return k, True
    return None, False


rows = []
for f in inputs:
    rows += json.load(open(f, encoding='utf-8'))

fam = lambda lab: re.sub(r' v[0-9]+[A-Za-z]*', '', lab) if re.match(r'^(NI|THIRTY) v', lab) else ('window copies' if lab.startswith('window copy') else lab)
def ver(lab):
    m = re.match(r'^(?:NI|THIRTY) v([0-9]+[A-Za-z]*)', lab)
    if m:
        return 'v' + m.group(1)
    m = re.match(r'^window copy 11-(\d\d) (\d\d:\d\d)', lab)
    return f'{int(m.group(1))} Nov {m.group(2)}' if m else ''

cands = collections.OrderedDict()   # key -> record
last = {}
for lab, n, raw in rows:
    k, defining = concept_of(raw)
    if k is None:
        if '§1.1' in lab:
            continue
        t = clean(raw)
        hits = []
        for kk, rx in USE:
            tt = t
            if kk in ('now', 'prior', 'next'):
                tt = re.sub(r'(?<![\w-])' + kk + r'-(?:existing|and)', ' ', tt, flags=re.I)
            m = rx.search(tt)
            if m:
                hits.append((m.start(), kk))
        k = min(hits)[1] if hits else last.get(lab)
        defining = False
    else:
        last[lab] = k
    if k is None:
        continue
    sk = key(raw)
    r = cands.setdefault(sk, {'sentence': clean(raw), 'concept': k, 'defining': defining, 'places': collections.OrderedDict()})
    if defining and not r['defining']:
        r['concept'], r['defining'] = k, True
    r['places'].setdefault(fam(lab), [])
    v = ver(lab)
    if v and v not in r['places'][fam(lab)]:
        r['places'][fam(lab)].append(v)

for r in cands.values():
    p = POS[r['concept']]
    text = r['sentence']
    used = []
    for k, rx in USE:
        if k == r['concept']:
            continue
        t = text
        if k in ('now', 'prior', 'next'):
            t = re.sub(r'(?<![\w-])(?:' + k + r')-(?:existing|and)', ' ', t, flags=re.I)
        if k == 'parity':
            t = re.sub(r'(?:own|all|me|self|other|social|bi|co|both)-parit(?:y|ies)', ' ', t, flags=re.I)
        if k == 'self':
            t = re.sub(r'self-\w+', ' ', t, flags=re.I)
        if rx.search(t):
            used.append(k)
    r['uses'] = used
    r['leans_later'] = [k for k in used if POS[k] > p]

json.dump(list(cands.values()), open(jout, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# the page
in_doc = lambda r: 'document 20 Nov' in r['places']
order = sorted(C)
out = []
counts = collections.Counter(r['concept'] for r in cands.values())


def places(r):
    bits = []
    for f, vs in r['places'].items():
        if vs:
            bits.append(f + ' ' + (vs[0] if len(vs) == 1 else f'{vs[0]} to {vs[-1]}'))
        else:
            bits.append(f)
    return '; '.join(bits)


def weight(r):
    return (-int(in_doc(r)), -int(r['defining']), -sum(max(1, len(v)) for v in r['places'].values()))


for p, k, _ in order:
    rs = [r for r in cands.values() if r['concept'] == k]
    if not rs:
        continue
    out.append(f'## {p} · {k}\n')
    doc = [r for r in rs if in_doc(r)]
    for r in sorted(rs, key=weight):
        mark = 'the document' if in_doc(r) else ('names it' if r['defining'] else 'said of it')
        lean = f" · leans on, named after it: {', '.join(r['leans_later'])}" if r['leans_later'] else ''
        out.append(f"- *{r['sentence']}* · {mark} · {places(r)}{lean}")
    out.append('')
open(page, 'w', encoding='utf-8').write('\n'.join(out))
print(len(cands), 'distinct sentences;', sum(1 for r in cands.values() if r['defining']), 'naming their concept;',
      sum(1 for r in cands.values() if r['leans_later']), 'leaning on a concept named after it')
for p, k, _ in order:
    print(f'{p:3d} {k:26s} {counts[k]:4d}')
