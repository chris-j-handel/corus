"""Each quotation of a page, word for word in a living file or a gathering file; and each word's living sentences.
All or none at all, by each quotation. Reads the page given, each living file at the root and each gathering file;
executes; writes no file; decides nothing.

Use: python3 -I incoming/v404chaining/instruments/each_quotation_word_for_word.py <root> page <a page>
         each quotation of six words or more in italics, outside a table's rows, with each file having it word
         for word, bold and italic marks passed over; it halts with a quotation found in no file
     python3 -I incoming/v404chaining/instruments/each_quotation_word_for_word.py <root> words <a form> ...
         each form, a regular expression with no case: its living sentences and living files, each living file
         with its own number of them, and its droplets in the gathering files

What it reads. A living file is a file at the root with a version in its name, *_v*.md. A sentence is a line
divided after a full stop, a question mark or an exclaiming mark, a line of a table, of code or a heading passed
over. A quotation is the words between two single asterisks, a bold pair inside it passed over.

Returned at main, Merge #858, 17 November 2026:
  words '\\bdestin(?:y|ies)\\b': 324 living sentences in eight living files: Natural Intelligence Corus 272,
  Exhibit FOURTEEN Natural Destinies 24, Exhibit TWENTY-SIX Living File Registry 17, Exhibit NINE Natural Human
  Society three, Exhibit THIRTY Co-Chaining Logic Registry three, Exhibit TWELVE Natural Explaining three, Exhibit
  TWENTY-NINE Natural Illustrating one and Exhibit TWENTY Natural Naming one, its dissolved word; none in Natural
  Intelligence or Exhibit ONE Natural Resolver. 'over the horizon': six living sentences in two living files, five
  of Exhibit EIGHT Natural Exploring.
  page incoming/v404chaining/A_me-parity_and_a_destiny_read_by_the_living_sentences.md: thirty quotations, each
  found.
"""
import collections, glob, os, re, sys

R, WORD = sys.argv[1], sys.argv[2]
plain = lambda t: re.sub(r'\*\*|\*', '', t)
def sents(t):
    out = []
    for l in t.split('\n'):
        l = plain(l).strip().rstrip(' \\')
        if not l or l.startswith(('|', '```', '#')): continue
        out += [s.strip() for s in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9"“(`+−])', l) if s.strip()]
    return out
living = {os.path.basename(f): open(f, encoding='utf-8').read() for f in sorted(glob.glob(os.path.join(R, '*_v*.md')))}
gathering = {os.path.basename(f): open(f, encoding='utf-8').read() for f in sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md')))}

if WORD == 'page':
    page = open(sys.argv[3], encoding='utf-8').read()
    found, missing = 0, []
    for line in page.split('\n'):
        if re.match(r'\|', line): continue
        x = line.replace('***', '\x01\x02\x02').replace('**', '\x02').replace('*', '\x01').split('\x01')
        for i in range(1, len(x), 2):
            q = x[i].replace('\x02', '').strip()
            if len(q.split()) < 6: continue
            where = [f for f, t in list(living.items()) + [('gathering-value/' + f, t) for f, t in gathering.items()] if q in plain(t)]
            if where: found += 1; print(f'   found in {len(where)}, first {where[0][:52]}: {q[:96]}')
            else: missing.append(q)
    print('quotations of six words or more:', found + len(missing), ' found:', found, ' found in no file:', len(missing))
    for q in missing: print('   NOT FOUND:', q)
    sys.exit(1 if missing else 0)

if WORD == 'words':
    for form in sys.argv[3:]:
        pat = re.compile(form, re.I)
        per = collections.Counter({f: sum(1 for s in sents(t) if pat.search(s)) for f, t in living.items()})
        per = {f: n for f, n in per.items() if n}
        drops = {f: sum(1 for l in t.split('\n') if l.startswith('- ') and pat.search(plain(l))) for f, t in gathering.items()}
        drops = {f: n for f, n in drops.items() if n}
        print(f'{form}: {sum(per.values())} living sentences in {len(per)} living files; {sum(drops.values())} droplets in {len(drops)} gathering files')
        for f, n in sorted(per.items(), key=lambda x: -x[1]): print(f'   {n:4d}  {f}')
