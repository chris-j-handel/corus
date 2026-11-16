"""Each dissolved word of Exhibit TWENTY Natural Naming's own list, with its saying, in one table: a word a line,
with the entry it is of, the words beside it in its entry, what it is said by, the set's reader check having it or
not, and its places said plainly in the living files and in the gathering files.
Reads Exhibit TWENTY Natural Naming's section of dissolved words, each living file, each gathering file and the
reader check's list of released words; executes; writes no file; decides nothing. All or none at all, by each entry.

Use: python3 -I incoming/v403cohering/instruments/each_dissolved_word_with_its_saying.py <root>        each check, and each reading
     python3 -I incoming/v403cohering/instruments/each_dissolved_word_with_its_saying.py <root> csv    the table, one line with each dissolved word
     python3 -I incoming/v403cohering/instruments/each_dissolved_word_with_its_saying.py <root> file <a living file's title>    each place of a word dissolved alone in one living file, as Natural_Resolver, with the heading it is under and its line's words

What it reads. An entry: an item of the section *Dissolved words, each with its saying*, with its *a*, said by.
A dissolved word: each word or words in italics before the entry's *a*. The words beside it: the entry's own words
not in italics, as *with a set's own voice* and *as nouns*: a word with them is dissolved with them and not alone,
and Exhibit TWENTY Natural Naming has a word list matching a word and not its scale. A place said plainly: the
word whole, with no italics, no code marks and no quotation round it, as the set's checks pass a mention over;
a resolver name's own words, as now-existing, and a file's version line and headings are not read.
A count here sizes a reading and decides nothing: each place is read by its sentence.

The table is `incoming/v403cohering/Each_dissolved_word_with_its_saying.csv`, with the living files' columns:
the gathering files change with each droplet, and their places are in this answer alone.

Returned at main, 16 November 2026:
  119 entries, each with its saying, and 278 dissolved words in them, 268 by their letters.
  The reader check's list has 59 words, 49 of them the section's by their letters; 219 of the section's are not in
  the list. Ten of the list are not the section's by their letters: because, therefore, land, lands and landing,
  each of the file's family of words before this section, and uncounted, holds, travels, neighbours and telling,
  each an other ending of a word of the section.
  Of 129 words dissolved alone and read, the living files say them plainly at 11,105 places: Exhibit TWENTY-ONE Hard
  Problem Registry 2,067, Natural Intelligence Corus 1,720, and Exhibit ONE Natural Resolver 15, the fewest. The
  gathering files say them at about 4,090.
  The section's own sayings: six entries have a word dissolved alone in an other entry, society in three, and
  signs, beat and takes each in one.
  The table's files of incoming/v403mgr: seated in the names and headers of eight tables, and seat in five.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def ver(p):
    m = re.search(r'_v(\d+)', p); return int(m.group(1)) if m else 0
def newest(stem):
    return max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver)

naming = open(newest('Exhibit_TWENTY_Natural_Naming'), encoding='utf-8').read().split('\n')
s = next(i for i, l in enumerate(naming) if l.startswith('## 2.4 Dissolved words, each with its saying'))
e = next(i for i in range(s + 1, len(naming)) if naming[i].startswith('## '))
assert naming[s + 2].startswith('Each entry: **Dissolved** · *a* Said by'), 'the section is not of entries, each Dissolved with its Said by'

ITALIC = re.compile(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)')
ENTRIES = []                                   # (dissolved part, said by)
i = s + 3
while i < e:
    l = naming[i]
    if l.startswith('- '):
        head = l[2:]
        if ' · *a* ' in head: part, said = head.split(' · *a* ', 1)
        elif i + 1 < e and naming[i + 1].startswith('  - *a* '): part, said = head, naming[i + 1][len('  - *a* '):]; i += 1
        else: part, said = head, None
        ENTRIES.append((part.strip(), said.strip() if said else None))
    elif l.startswith('**'): break             # the section's own sentences after its entries
    i += 1

ROWS = []                                      # (word, entry, beside, said by)
for part, said in ENTRIES:
    beside = re.sub(r'\s+', ' ', ITALIC.sub('…', part)).strip()
    beside = re.sub(r'^(?:…[ ,·]*|and |or )+', '', beside).strip(' ,·') if re.sub(r'[… ,·]|and|or', '', beside) else ''
    for w in ITALIC.findall(part):
        ROWS.append((w.strip(), part, beside, said or ''))

check_list = [l.strip().lower() for l in open(os.path.join(R, 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt'), encoding='utf-8') if l.strip() and not l.startswith('#')]
WORDS = {w.lower() for w, *_ in ROWS}

def plain(text):
    """a file's words with each mention passed over: code, italics, quotations, headings and its version line"""
    out = []
    fence = False
    for k, l in enumerate(text.split('\n')):
        if l.startswith('```'): fence = not fence; continue
        if fence or k == 0 or l.startswith('#'): continue
        l = re.sub(r'`[^`]*`', ' ', l)
        l = ITALIC.sub(' ', l)
        l = re.sub(r'"[^"]*"', ' ', l); l = re.sub(r'“[^”]*”', ' ', l)
        out.append(l)
    return '\n'.join(out)

def places(word, texts):
    """in how many files, and at how many places, a word is said plainly, whole and with no hyphen joining it"""
    if not re.search(r'[A-Za-z]{2}', word) or word.startswith('-') or word.endswith('-'): return None
    pat = re.compile(r'(?<![\w-])' + re.escape(word).replace(r'\ ', r'\s+') + r'(?![\w-])', re.I)
    n = [len(pat.findall(t)) for t in texts]
    return sum(1 for x in n if x), sum(n)

living = {}
for p in glob.glob(os.path.join(R, '*_v*.md')):
    stem = re.sub(r'_v\d+[A-Za-z]*\.md$', '', os.path.basename(p))
    if stem not in living or ver(p) > ver(living[stem]): living[stem] = p
LIV = [plain(open(p, encoding='utf-8').read()) for p in sorted(living.values())]
GAT = [plain(open(p, encoding='utf-8').read()) for p in sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md')))]

TABLE = []
for w, part, beside, said in ROWS:
    a, b = places(w, LIV), places(w, GAT)
    TABLE.append([w, 'alone' if not beside else beside, said, 'has it' if w.lower() in check_list else '',
                  '' if a is None else a[0], '' if a is None else a[1], '' if b is None else b[0], '' if b is None else b[1], part])
if WHAT == 'csv':                               # the living files' columns alone: the gathering files change with each droplet
    wr = csv.writer(sys.stdout, lineterminator='\n')
    wr.writerow(['dissolved word [living TWENTY]', 'alone, or with the words beside it in its entry [living TWENTY]', 'said by [living TWENTY]',
                 "the reader check's list [executed]", 'living files saying it plainly [executed]', 'its places in them [executed]',
                 'its entry, whole [living TWENTY]'])
    wr.writerows(r[:6] + r[8:] for r in TABLE); sys.exit()

if WHAT == 'file':                              # one living file, each place of a word dissolved alone
    title = sys.argv[3]
    path = next(p for s, p in living.items() if s == title or s.endswith('_' + title))
    ALONE_SAID = {r[0]: r[2] for r in TABLE if r[1] == 'alone' and r[5] != ''}
    head, fence, n = 'its opening', False, 0
    for k, l in enumerate(open(path, encoding='utf-8').read().split('\n')):
        if l.startswith('```'): fence = not fence; continue
        if fence or k == 0: continue
        if l.startswith('#'): head = l.lstrip('# ').strip(); continue
        m0 = re.match(r'^\*\*([^*]{3,90}?)\.?\*\*', l)
        if m0: head = m0.group(1)
        pl = plain(' \n' + l)
        for w, said in ALONE_SAID.items():
            for m in re.finditer(r'(?<![\w-])' + re.escape(w).replace(r'\ ', r'\s+') + r'(?![\w-])', pl, re.I):
                n += 1
                print(f'{n} · {w} · with {head[:60]} · …{pl[max(0, m.start() - 70):m.end() + 70].strip()}… · said by {said[:80]}')
    print(f'{n} places of a word dissolved alone, said plainly, in {os.path.basename(path)}'); sys.exit()

print(f'{len(ENTRIES)} entries of dissolved words, {len(ROWS)} dissolved words in them, {len(WORDS)} by their letters')
checks = [
    ('each entry has its saying', all(said for _, said in ENTRIES)),
    ('each entry has a dissolved word in italics', all(ITALIC.search(part) for part, _ in ENTRIES)),
]
for what, ok in checks: print(('  is · ' if ok else '  is-not · ') + what)
for part, said in ENTRIES:
    if not said or not ITALIC.search(part): print('      ', part[:100])
missing = [w for w in check_list if w not in WORDS]
print(f"the reader check's list: {len(check_list)} words; dissolved words of the section by their letters: {len(set(check_list) & WORDS)} of them")
print(f"  words of the list not a dissolved word of the section by its letters: {len(missing)}: {', '.join(missing)}")
alone = [r for r in TABLE if r[1] == 'alone' and r[5] != '']
withb = [r for r in TABLE if r[1] != 'alone' and r[5] != '']
print(f'dissolved alone, {len(alone)} words read: said plainly in the living files at {sum(r[5] for r in alone)} places, in the gathering files at {sum(r[7] for r in alone)}')
print(f'dissolved with words beside it, {len(withb)} words read: at {sum(r[5] for r in withb)} places in the living files and {sum(r[7] for r in withb)} in the gathering files, each by its sentence')
print('dissolved alone, the twelve with the most places in the living files:')
for r in sorted(alone, key=lambda r: -r[5])[:12]: print(f"    {r[0]}: {r[5]} places in {r[4]} living files, {r[7]} in {r[6]} gathering files · said by {r[2][:70]}" + ('' if r[3] else ' · not in the check\'s list'))

# each living file by its places of a word dissolved alone
ALONE = [r[0] for r in alone]
def all_places(text):
    return sum(places(w, [text])[1] for w in ALONE)
names = [os.path.basename(p)[:-3] for p in sorted(living.values())]
by_file = sorted(((all_places(t), n) for n, t in zip(names, LIV)), reverse=True)
print('each living file by its places of a word dissolved alone: the five with the most, and the five with the fewest')
for k, n in by_file[:5] + by_file[-5:]: print(f'    {k:5d}  {n}')

# the section's own sayings, each read with each word dissolved alone in an other entry
print("the section's own sayings having a word dissolved alone in an other entry:")
found = 0
for part, said in ENTRIES:
    own = {w.lower() for w in ITALIC.findall(part)}
    text = (said or '').replace('*', '')
    hits = sorted({w for w in ALONE if w.lower() not in own and places(w, [text]) and places(w, [text])[1]})
    if hits: found += 1; print(f"    {part[:60]} · said by … {', '.join(hits)}")
print(f'  {found} entries of {len(ENTRIES)}')

# the table's own files, each header and each file's name, read with each word dissolved alone
print("the table's files of incoming/v403mgr, each name and each header, with a word dissolved alone:")
tfound = {}
for p in sorted(glob.glob(os.path.join(R, 'incoming', 'v403mgr', '*.csv'))):
    header = open(p, encoding='utf-8').readline()
    text = os.path.basename(p)[:-4].replace('_', ' ') + ' , ' + header
    for w in ALONE:
        n = places(w, [text])[1]
        if n: tfound.setdefault(w, []).append(os.path.basename(p)[:-4])
for w, fs in sorted(tfound.items(), key=lambda x: -len(x[1])): print(f'    {w}: {len(fs)} of the tables')
print('each check is' if all(ok for _, ok in checks) else 'a check is-not')
