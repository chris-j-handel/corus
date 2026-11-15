import sys, re, json
R = sys.argv[1]
L = open(R + '/gathering-value/Natural_Intelligence.md', encoding='utf-8').read().split('\n')
a = next(i for i, l in enumerate(L) if l.startswith('## Opening')); z = next(i for i, l in enumerate(L) if l.startswith('## ONE · NATURAL'))
idx = [i for i in range(a + 1, z) if L[i].startswith('- ')]
concepts = [('the universe', r'\buniverse\b'), ('prior-existing', r'\bprior-existing\b'), ('same-existing', r'\bsame-existing\b(?!-society)'), ('next-existing', r'\bnext-existing\b'),
 ('a sequence', r'\bsequence\b'), ('a moment', r'\bmoments?\b|\bmomentar'), ('a name, a universal set', r'\buniversal set\b|\ba name\b|\bnames?\b|\bnaming\b'), ('is-or-is-not', r'\bis-or-is-not\b'),
 ('observing', r'\bobserving\b'), ('possibling', r'(?<!co-)\bpossibling\b'), ('discovering', r'\bdiscovering\b'), ('living and non-living', r'\bnon-living\b|\bliving\b'),
 ('a self', r'\bsel(f|ves)\b'), ('a me', r'\bmes?\b(?!-)'), ('an other', r'\bothers?\b(?!-)'), ('aiming', r'\baiming\b'), ('a me-parity', r'\bme-parit'), ('other-parity and all-parity', r'\bother-parity\b|\ball-parity\b|\buniversal-parity\b|\buniversal parity\b'),
 ('a parity', r'\bparit(y|ies)\b'), ('a bi-coupling', r'\bbi-coupl'), ('a you, consciousness', r'\byou\b|\bconsciousness\b'), ('resolving', r'\bresolving\b'), ('natural intelligence', r'\bnatural intelligence\b'),
 ('do-no-harming and improving', r'\bdo-no-harming\b|\bimproving\b'), ('co-possibling', r'\bco-possibling\b'), ('a society', r'\bsociet'), ('social moral competency', r'\bsocial moral competenc'),
 ('co-chaining', r'\bco-chaining\b'), ('geodesic', r'\bgeodesic\b'), ('stable-forming', r'\bstable-forming\b|\bstable form'), ('a living file, an expedition', r'\bliving file|\bexpedition\b'),
 ('the atom, a vault, dormancy', r'\batom|\bvault|\bdorman'), ('the seventeen names, the code', r'\b\d{1,2}-(now|next)-|\bthe code\b|\bExhibit ONE\b')]
def core(d):
    t = d.split(' · ', 1)[1] if ' · ' in d else d
    return re.sub(r'^\*[^*]{0,90}\.\*\s*', '', t)
groups = {c: [] for c, _ in concepts}; groups['no name of these'] = []
for k, i in enumerate(idx):
    t = core(L[i]).lower()[:400]; best = None
    for c, p in concepts:
        m = re.search(p, t)
        if m and (best is None or m.start() < best[0]): best = (m.start(), c)
    groups[best[1] if best else 'no name of these'].append(k)
json.dump({'idx': idx, 'groups': groups}, open('/tmp/opening_groups.json', 'w'))
for c, ks in groups.items(): print(f"{len(ks):4d}  {c}")
