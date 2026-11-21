"""The opening's versions, name by name: each name Natural Intelligence's living opening defines in bold, with its
living sentence, and each sentence of that name in each other version of the opening and in the living files.
Reads; writes the one table given; decides nothing.

Use: python3 -I incoming/v404chaining/instruments/the_opening_its_versions_name_by_name.py <root> <the copy's root> <table>
     <root> a checkout of main, its living files as at corus.me; <the copy's root> a checkout of the copy's branch

The versions read:
  living              Natural Intelligence's opening at <root>, the one at corus.me: each name's own sentence
  the copy            the next version's copy at <the copy's root>, its opening's sentence of the same number, where
                      it differs
  the waiting opening the candidate of fifty-five lines at the head of Natural Intelligence's gathering file, also
                      named the opening at its newest: the line with the name in bold
  Exhibit THIRTY-ONE Me, the living file explaining the opening's names: up to three sentences defining the name
  an is of both partners, gathered: a sentence defining the name after *An is* in Natural Intelligence's gathering
                      file, up to three
  another living file each other living file's sentence defining the name in bold, up to three
A sentence defining a name opens with the name, after A, An, The or Each, and has *is* or *are* after it.

Returned at main, Merge #864, and the copy at its newest commit, 17 November 2026: 46 names, 74 sentences beside
46 living ones; the waiting opening has a line for 31 of the 46 names; the copy differs at sentence 50, a moment
for a momentary. Ten names have no sentence beside the living one.
"""
import re, glob, os, sys, csv, collections
R, COPY, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
plain = lambda t: re.sub(r'\*\*|\*', '', t)
def opening(path):
    ni = open(path, encoding='utf-8').read()
    op = re.search(r'^# Natural Intelligence\n\n\*\*[^\n]*\*\*\n\n(.*?)\n\n\*\*ONE · ', ni, re.S | re.M).group(1)
    return [l.rstrip(' \\') for l in op.split('\n') if l.strip()]
L = opening(max(glob.glob(os.path.join(R, 'Natural_Intelligence_v*.md'))))
C = opening(max(glob.glob(os.path.join(COPY, 'Natural_Intelligence_v*.md'))))
own = collections.OrderedDict()
for i, s in enumerate(L, 1):
    for b in re.findall(r'\*\*(.+?)\*\*', s): own.setdefault(b.lower(), i)
def sents(t):
    out = []
    for l in t.split('\n'):
        p = plain(l).strip().rstrip(' \\')
        if not p or p.startswith(('|', '```', '#')): continue
        out += [s.strip() for s in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9"“(`+−])', p) if s.strip()]
    return out
def defines(name, s):
    n = re.escape(name).replace(r'\ ', r'[ -]')
    return re.match(rf"^(?:A|An|The|Each)?\s*{n}s?\b(?:,[^.]*?)?\s+(?:is|are)\b", s, re.I) is not None
g = open(os.path.join(R, 'gathering-value', 'Natural_Intelligence.md'), encoding='utf-8').read()
cand = re.search(r'^- \*\*An explaining\*\* · The opening at its newest, laid.*$', g, re.M).group(0)
clines = [l for l in re.split(r'\s(?=\d{1,2}\. (?:\((?:newer|not yet distinguished)\) )?[A-Z\[*])', cand[cand.find(' 1. '):].strip()) if re.match(r'\d{1,2}\. ', l)]
cown = {}
for l in clines:
    for b in re.findall(r'\*\*(.+?)\*\*', l): cown.setdefault(b.lower(), l)
me = sents(open(max(glob.glob(os.path.join(R, 'Exhibit_THIRTY-ONE_Me_v*.md'))), encoding='utf-8').read())
gis = []
for l in g.split('\n'):
    if l.startswith('- ') and re.search(r'An is[:,]', plain(l)):
        gis += [s for s in sents(plain(l).split('An is', 1)[1].lstrip(':, '))]
others = {}
for f in sorted(glob.glob(os.path.join(R, '*_v*.md'))):
    b = os.path.basename(f)
    if b.startswith(('Natural_Intelligence_v', 'Exhibit_THIRTY_')): continue
    t = open(f, encoding='utf-8').read()
    others[b] = [plain(s) for s in re.findall(r'(?m)(?:^|(?<=\. ))((?:A|An|Each)?\s*\*\*[^*]+\*\*[^.\n]{0,300}\.)', t)]
rows = [['Name', 'Its living sentence, at corus.me', 'Version', 'Place', 'Sentence']]
count = collections.Counter()
for name, i in own.items():
    base = plain(L[i - 1])
    def add(version, place, s):
        rows.append([name, base, version, place, ' '.join(s.split())]); count[version] += 1
    add('living', f'Natural Intelligence, the opening, {i}', base)
    if plain(C[i - 1]) != base: add('the copy', f'the copy, the opening, {i}', plain(C[i - 1]))
    if name in cown: add('the waiting opening', 'Natural Intelligence\'s gathering file, its head', plain(cown[name]))
    for s in [s for s in me if defines(name, s)][:3]: add('Exhibit THIRTY-ONE Me', 'Exhibit THIRTY-ONE Me', s)
    seen = set()
    for s in gis:
        if defines(name, s) and s not in seen and s != base and len(seen) < 3: seen.add(s); add('an is of both partners, gathered', 'Natural Intelligence\'s gathering file', s)
    k = 0
    for f, ss in others.items():
        for s in ss:
            if k < 3 and defines(name, s) and s != base: add('another living file', f.replace('_', ' ').rsplit(' v', 1)[0], s); k += 1
with open(OUT, 'w', encoding='utf-8', newline='') as fh: csv.writer(fh, lineterminator='\n').writerows(rows)
print('names:', len(own), ' rows:', len(rows) - 1, dict(count))
print('names with no sentence beside the living one:', [n for n in own if sum(1 for r in rows[1:] if r[0] == n) == 1])
print('copy differs at:', [i for i in range(1, 71) if plain(C[i-1]) != plain(L[i-1])])
print('waiting opening lines with a name of the living opening:', sum(1 for n in own if n in cown), 'of', len(own))
