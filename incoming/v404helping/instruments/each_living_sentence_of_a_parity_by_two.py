"""Each living sentence saying a parity with a form of two, and each living sentence having a parity
self-orienting, aiming, forward or a direction, across each living file of the set's list but Natural
Intelligence and Exhibit THIRTY Co-Chaining Logic Registry. For a suggesting of a parity, re-said in natural
naming with the head of Natural Intelligence's gathering file, by no authority: a direction, no one of two,
self-orienting, aiming and orienting forward.
Reads the set's list of living files and each living file of it; executes; decides nothing; writes no living
file and no gathering file.

Use: python3 -I incoming/v404helping/instruments/each_living_sentence_of_a_parity_by_two.py <root>          each sentence said by its form, and nothing written
     python3 -I incoming/v404helping/instruments/each_living_sentence_of_a_parity_by_two.py <root> write    its table written, incoming/v404helping/Each_living_sentence_of_a_parity_by_two.csv

What it reads. A sentence is a line's words to a stop, outside a code's lines, a heading and a file's version
line; bold, italic and code marks are passed over for the reading and are in the table as the file has them.
A sentence of a parity has the letters *parit*, as *parity*, *parities* and *me-parity*. A form, each all or
none at all by its own words in that sentence:
  of two:      *two directions*; *one of two*; + with − by *or*, *and* or a mark between, and ±; *odd* with *even*
  of aiming:   *self-orient*; *aim*, *aims*, *aiming*; *forward*; *direction*, *directions*
A form found is a place for a reading and no saying of the sentence's parity: *odd* with *even* is in a
sentence of a name's number too, and + with − in a sentence of two parities.
A saying, each all or none at all by its own words, a sentence's own:
  a parity + or −:           *parity* or *parities* with + with − or ± after it in its own part of the sentence, no
                             stop between them and *together*, *parting* or *part* not after it, as *each sharing's
                             parity, + or −*; + with − or ± with *a sharing's parity* after it; and *a sharing of + or −*
  + and − an implementing:   *an implementing of a parity*
  + and − of two parities:   + and − with *together*, *parting* or *part*
  a number no parity:        *a number and no parity* and *a numbering and no parity*
  a parity a direction:      *parity is a direction*, *parity is its changing direction*, *parity is a changing direction*
The code. Exhibit ONE Natural Resolver's code is executed with each + and − exchanged, by each case of two
whole domains: one self with one sharing, each prior, none, + or −, with each list of + and − reaching it,
none to three; and two selves bi-coupling in their pair with 10, each opening of + and −, eight moments.
All or none at all: each answer is the answer with each + and − exchanged, or this instrument halts.

Returned at main, 16 November 2026, after Merge #845: thirty-one living files, 1,795 sentences of a parity.
Of two, 108 sentences: *two directions* three, *one of two* seven, + with − sixty-one, *odd* with *even*
forty-four. Of aiming, seventy-one: *self-orienting* one, *aiming* fourteen, *forward* twenty-three,
*direction* forty. A saying, forty-one: a parity + or − twenty-eight, in ten living files, thirteen of them
Exhibit TWENTY Natural Naming's; + and − an implementing two; + and − of two parities seven; a number no
parity two; a parity a direction three. The code with each + and − exchanged: forty-five of forty-five cases
and thirty-two of thirty-two moments, each answer exchanged.
"""
import csv, json, os, re, sys

R = sys.argv[1]; WRITE = len(sys.argv) > 2 and sys.argv[2] == 'write'
APART = ('Natural_Intelligence_v', 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v')
FILES = [f for f in json.load(open(os.path.join(R, 'files.json'), encoding='utf-8')) if not f.startswith(APART)]
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'[*`_\\]', '', s)).strip()
PARITY = re.compile(r'parit', re.I)
TWO = [('two directions', r'\btwo directions\b'), ('one of two', r'\bone of two\b'),
       ('+ with −', r'\+\s*(?:or|and|,)\s*[−-](?!\d)|[−-]\s*(?:or|and)\s*\+|±'),
       ('odd with even', r'\bodd\b[^.]*\beven\b|\beven\b[^.]*\bodd\b')]
AIM = [('self-orienting', r'self-orient'), ('aiming', r'\baim(?:ing|s)?\b'), ('forward', r'\bforward\b'), ('direction', r'\bdirections?\b')]
PM = r'(?:\+\s*(?:or|and)\s*[\u2212-]|[\u2212-]\s*or\s*\+|\u00b1)'
SAY = [('a parity + or \u2212', r'parit(?:y|ies)\b[^.;:]{0,45}?' + PM + r'(?!\s*(?:together|parting|part)\b)|' + PM + r',?\s+(?:are\s+)?a sharing.s parit|sharing of ' + PM),
       ('+ and \u2212 an implementing', r'an implementing of a parity'),
       ('+ and \u2212 of two parities', r'\+\s*and\s*[\u2212-]\s*(?:together|parting|part)\b'),
       ('a number no parity', r'a number(?:ing)? and no parity'),
       ('a parity a direction', r'parity is (?:a|its)(?: changing)? direction')]

rows = []; sentences = with_parity = 0
for f in FILES:
    L = open(os.path.join(R, f), encoding='utf-8').read().split('\n'); fence = False; head = ''
    for k, l in enumerate(L):
        if l.startswith('```'): fence = not fence; continue
        if fence or k == 0: continue
        if l.startswith('#'): head = re.sub(r'^#+\s*', '', l).strip(); continue
        for s in re.split(r'(?<=[.?!])\s+', l):
            n = norm(s); sentences += 1
            if not PARITY.search(n): continue
            with_parity += 1
            two = [name for name, rx in TWO if re.search(rx, n, re.I)]
            aim = [name for name, rx in AIM if re.search(rx, n, re.I)]
            say = [name for name, rx in SAY if re.search(rx, n, re.I)]
            if two or aim or say: rows.append([f, head, s.strip(), '; '.join(two), '; '.join(aim), '; '.join(say)])

print(f'{len(FILES)} living files; {sentences} sentences; {with_parity} of a parity; {len(rows)} with a form')
for title, col, forms in (('of two', 3, TWO), ('of aiming', 4, AIM), ('a saying', 5, SAY)):
    print(f'{title}: {sum(1 for r in rows if r[col])} sentences; ' + ', '.join(f"{name} {sum(1 for r in rows if name in r[col].split('; '))}" for name, _ in forms))
by = {}
for r in rows: by.setdefault(r[0], [0, 0]); by[r[0]][0] += bool(r[3]); by[r[0]][1] += bool(r[4])
for f, (a, b) in by.items(): print(f'   {f}: of two {a}, of aiming {b}')
# Exhibit ONE Natural Resolver's code with each + and \u2212 exchanged, by each case, all or none at all
import glob, itertools
ver = lambda p: int(re.search(r'_v(\d+)', p).group(1))
ONE = max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')), key=ver)
code = {}; exec(open(ONE, encoding='utf-8').read().split('```python', 1)[1].split('```', 1)[0], code)
inv = lambda pairs: [(k, -v) for k, v in pairs]
cases = same = 0
for prior in ([], [('s', 1)], [('s', -1)]):                     # one self, one sharing: each prior, and each list of + and \u2212 reaching it to three
    for n in range(4):
        for now in itertools.product((1, -1), repeat=n):
            now = [('s', v) for v in now]
            a_, b_ = code['_1_now_existing'](prior, now); c_, d_ = code['_1_now_existing'](inv(prior), inv(now))
            cases += 1; same += (inv(a_), inv(b_)) == (c_, d_)
pairs = pair_same = 0
for pa, pb in itertools.product((1, -1), repeat=2):               # two selves bi-coupling in their pair with 10: each opening, eight moments
    S = {'a': ([('s', pa)], []), 'b': ([('s', pb)], [])}; T = {'a': ([('s', -pa)], []), 'b': ([('s', -pb)], [])}
    co = {('a', 10): 'b', ('b', 10): 'a'}
    for m in range(8):
        S = code['_17_next_existing'](S, co); T = code['_17_next_existing'](T, co)
        pairs += 1; pair_same += all((inv(S[k][0]), inv(S[k][1])) == (T[k][0], T[k][1]) for k in S)
print(f"{os.path.basename(ONE)}'s code with each + and \u2212 exchanged: one self with one sharing, {same} of {cases} cases each answer exchanged; two selves bi-coupling, {pair_same} of {pairs} moments each answer exchanged")
assert same == cases and pair_same == pairs, 'an answer is not exchanged with each + and \u2212 exchanged'
if '--say' in sys.argv:
    for r in rows:
        if r[5]: print(f"\n{r[0][:44]} | {r[1][:50]} | [{r[5]}]\n    {r[2][:int(sys.argv[sys.argv.index('--say') + 1])]}")
if WRITE:
    out = os.path.join(R, 'incoming', 'v404helping', 'Each_living_sentence_of_a_parity_by_two.csv')
    with open(out, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['living file [living]', 'its heading [living]', 'its sentence [living]', 'a form of two in it [executed]', 'a form of aiming in it [executed]', 'a saying in it [executed]'])
        w.writerows(rows)
    print(f'written: {os.path.relpath(out, R)}, {len(rows)} lines after its first')
else:
    print('nothing written')
