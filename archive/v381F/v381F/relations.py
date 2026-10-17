"""Session v381F: the living files' relations to each other, across and along, computed from the root.

Runs from the repository root: python3 incoming/v381F/relations.py
Across: which living file names which other, by its title or its exhibit number, counted at each file.
Along: the concept words each file carries, its -ing words, those shared by many files and those one file
alone carries; the resolver's seventeen names at each file; and the released words of the kit's list at each file.
Writes beside this script: Naming_Matrix.tsv, Concept_Ings.tsv, Seventeen_Names_At_Each_File.tsv,
Released_Words_At_Each_File.tsv, and prints a short account. A gathering, deciding nothing.
"""
import json, re, collections

files = json.load(open('files.json'))
texts = {f: open(f, encoding='utf-8').read() for f in files}
NUM = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN',
       'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY', 'TWENTY-ONE', 'TWENTY-TWO',
       'TWENTY-THREE', 'TWENTY-FOUR', 'TWENTY-FIVE', 'TWENTY-SIX', 'TWENTY-SEVEN', 'TWENTY-EIGHT', 'TWENTY-NINE', 'THIRTY']


def title_of(f):
    return next(l[2:].strip() for l in texts[f].split('\n') if l.startswith('# '))


titles = {f: title_of(f) for f in files}
short = {}
for f in files:
    m = re.match(r"Exhibit_([A-Z-]+)_", f)
    short[f] = ('Exhibit ' + m.group(1)) if m else titles[f]

# across: naming
patterns = {}
for f in files:
    t = titles[f]
    pats = [re.escape(t)]
    m = re.match(r"Exhibit_([A-Z-]+)_", f)
    if m:
        n = m.group(1)
        pats.append(r"Exhibit\s+%s\b(?!-)" % re.escape(n))
    if f.startswith('Natural_Intelligence_v'):
        pats = [r"Natural Intelligence\b(?! Corus)"]
    patterns[f] = re.compile('|'.join(pats))

matrix = {}
for f in files:
    body = texts[f]
    row = {}
    for g in files:
        if g == f:
            continue
        n = len(patterns[g].findall(body))
        if n:
            row[g] = n
    matrix[f] = row

with open('incoming/v381F/Naming_Matrix.tsv', 'w', encoding='utf-8') as out:
    out.write('file naming\tfile named\ttimes\n')
    for f in files:
        for g, n in sorted(matrix[f].items(), key=lambda x: -x[1]):
            out.write('%s\t%s\t%d\n' % (short[f], short[g], n))

named_by = collections.Counter()
names_out = collections.Counter()
for f in files:
    for g, n in matrix[f].items():
        named_by[g] += 1
        names_out[f] += 1

# along: concept -ings
stop = set('being thing things something nothing anything everything during according following morning evening king ring string wing'.split())
ings = {}
for f in files:
    words = re.findall(r"\b[a-z][a-z-]*ing\b", texts[f].lower())
    c = collections.Counter(w for w in words if w not in stop and len(w) > 5)
    ings[f] = c
all_ings = collections.Counter()
for f in files:
    for w in ings[f]:
        all_ings[w] += 1
common = [w for w, n in all_ings.items() if n >= 24]
particular = {f: [w for w, n in ings[f].most_common() if all_ings[w] == 1][:12] for f in files}
with open('incoming/v381F/Concept_Ings.tsv', 'w', encoding='utf-8') as out:
    out.write('file\tits twelve most carried -ings\t-ings it alone carries, the twelve most carried\n')
    for f in files:
        out.write('%s\t%s\t%s\n' % (short[f], ', '.join('%s %d' % (w, n) for w, n in ings[f].most_common(12)),
                                    ', '.join(particular[f])))

# the seventeen names: the current seventeen from Exhibit ONE's table, and old-form names beside them
exhibit_one = sorted(f for f in files if f.startswith('Exhibit_ONE_'))[0]
CURRENT = set(re.findall(r"\b\d{1,2}-(?:co|bi|tri)-(?:co|bi|tri)-(?:co|bi|tri)-[a-z]+ing\b",
                         texts[exhibit_one].split('**Each name and its relations.**')[0]))
NAME = re.compile(r"\b\d{1,2}-(?:co|bi|tri)(?:-(?:co|bi|tri)){1,3}-[a-z]+(?:-[a-z]+)?ing\b")
with open('incoming/v381F/Seventeen_Names_At_Each_File.tsv', 'w', encoding='utf-8') as out:
    out.write('file\tsayings of the current seventeen\tdistinct current names\tthe current names\tdistinct old-form names\tthe old-form names\n')
    seventeen = {}
    for f in files:
        found = NAME.findall(texts[f])
        current = sorted(set(m for m in found if m in CURRENT), key=lambda s: int(s.split('-')[0]))
        old = sorted(set(m for m in found if m not in CURRENT), key=lambda s: int(s.split('-')[0]))
        seventeen[f] = (sum(1 for m in found if m in CURRENT), current, old)
        out.write('%s\t%d\t%d\t%s\t%d\t%s\n' % (short[f], seventeen[f][0], len(current), ' '.join(current), len(old), ' '.join(old)))

# released words of the kit's list
released = [w.strip() for w in open('kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt')
            if w.strip() and not w.startswith('#')]
rel_rx = re.compile(r"\b(" + '|'.join(re.escape(w) for w in released) + r")\b", re.I)
with open('incoming/v381F/Released_Words_At_Each_File.tsv', 'w', encoding='utf-8') as out:
    out.write('file\tversion\twords\treleased words of the kit list\tper thousand words\tthe five most\n')
    loads = {}
    for f in files:
        body = re.sub(r"```.*?```", '', texts[f], flags=re.S)
        hits = collections.Counter(m.lower() for m in rel_rx.findall(body))
        n = sum(hits.values()); words = len(body.split())
        loads[f] = (n, words, 1000.0 * n / words, hits.most_common(5))
        out.write('%s\t%s\t%d\t%d\t%.1f\t%s\n' % (short[f], texts[f].split('\n')[0].split()[-1], words, n, 1000.0 * n / words,
                                                 ', '.join('%s %d' % h for h in hits.most_common(5))))

print('ACROSS: files named by the most other files')
for g, n in named_by.most_common(8):
    print('  %-32s named by %2d files' % (short[g], n))
print('ACROSS: files naming the most other files')
for f, n in names_out.most_common(8):
    print('  %-32s names %2d files' % (short[f], n))
print('ACROSS: files named by no other file:', ', '.join(short[g] for g in files if named_by[g] == 0) or 'none')
print('ACROSS: files naming no other file:', ', '.join(short[f] for f in files if names_out[f] == 0) or 'none')
print('ALONG: -ings carried by 24 or more of the 32 files (%d):' % len(common))
print('  ' + ', '.join(sorted(common, key=lambda w: -all_ings[w])))
print('ALONG: the current seventeen names, files carrying all seventeen:',
      ', '.join(short[f] for f in files if len(seventeen[f][1]) == 17))
print('ALONG: files carrying one or more of the current seventeen (%d):' % sum(1 for f in files if seventeen[f][0]),
      ', '.join('%s %d' % (short[f], len(seventeen[f][1])) for f in files if seventeen[f][0]))
print('ALONG: files carrying old-form resolver names and none current:',
      ', '.join('%s %d' % (short[f], len(seventeen[f][2])) for f in files if seventeen[f][2] and not seventeen[f][0]))
print('ALONG: files carrying none of the current seventeen (%d):' % sum(1 for f in files if not seventeen[f][0]),
      ', '.join(short[f] for f in files if not seventeen[f][0]))
print('ALONG: released words of the kit list per thousand words, the five lightest and the five heaviest:')
order = sorted(files, key=lambda f: loads[f][2])
for f in order[:5] + order[-5:]:
    print('  %-32s %-6s %5.1f  %s' % (short[f], texts[f].split('\n')[0].split()[-1], loads[f][2], ', '.join('%s %d' % h for h in loads[f][3][:3])))
