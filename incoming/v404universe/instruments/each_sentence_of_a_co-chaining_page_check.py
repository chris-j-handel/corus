"""Each sentence of a page written as a co-chaining: its words natural naming's own, the sentence living already
or not, its living sentence word for word, and each word the chain has not.

Reads the page given, each living file at the root, each gathering file, the set's list of released words and
the table of Exhibit TWENTY Natural Naming's dissolved words; executes; writes no file; decides nothing.

Said in the session: in all the sentences in the report of the value of this session there is only natural
naming and explaining and cohering and co-chaining.

Use: python3 -I incoming/v404universe/instruments/each_sentence_of_a_co-chaining_page_check.py <root> <a page>

What it reads. A sentence of the page is a line opening with its number and a full stop. Under it, a line with
*From* has the living sentence it is from between two single asterisks, or *its* and the numbers of sentences of
the page before it. A line with *Adding:* has what it is adding.
The chain is Exhibit THIRTY Co-Chaining Logic Registry's numbered sentences and the opening of Natural
Intelligence. A word is letters with the hyphens joining them, a name as do-no-harming one word: a name of
more parts than one is the chain's only whole.

Its checks, all or none at all, by each sentence:
  1  no released word, no word Natural Naming has dissolved alone, and no word both partners answered is-not
     as natural naming on 18 November: sharing, empty, improving, first, within, inside, away, toward, reading
  2  the sentence is word for word in no living file: a sentence living already is no adding
  3  it has a From, and a From of the page is of a sentence before it
  4  each living sentence of a From is word for word in a living file or a gathering file
It closes with its fails. After them, deciding nothing: each word the chain has not, with the sentences having
it, a place for a naming sentence; and each sentence longer than twenty-two words.

Returned at main, Merge #986, 18 November 2026, for
incoming/v404universe/The_value_of_this_session_a_co-chaining_of_sentences.md:
  50 sentences, 42 from a living sentence and 8 from a sentence of the page alone; fails: 0.
  38 words the chain has not, among them zone, swath, cone, horizon, hole, fuzzying, atom, me-parity,
  all-parity, same-me, co-me-parity, co-now, bi-now, co-geodesic, triangulating and do-only-harming.
  No sentence longer than twenty-two words.
"""
import csv, glob, os, re, sys

R, PAGE = sys.argv[1], sys.argv[2]
plain = lambda t: re.sub(r'\*\*|\*', '', t)
squeeze = lambda t: re.sub(r'\s+', ' ', t).strip()
words = lambda t: re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", t)

living = {os.path.basename(f): squeeze(plain(open(f, encoding='utf-8').read()))
          for f in sorted(glob.glob(os.path.join(R, '*_v*.md')))}
gathering = {os.path.basename(f): squeeze(plain(open(f, encoding='utf-8').read()))
             for f in sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md')))}

released = set()
for l in open(os.path.join(R, 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt'), encoding='utf-8'):
    l = l.strip()
    if l and not l.startswith('#'):
        released.add(l.lower())
dissolved = set()
with open(os.path.join(R, 'incoming/v403cohering/Each_dissolved_word_with_its_saying.csv'), encoding='utf-8') as fh:
    rows = list(csv.reader(fh))
for r in rows[1:]:
    if r[1].strip().lower().startswith('alone') and ' ' not in r[0].strip():
        dissolved.add(r[0].strip().lower())
is_not = {'sharing', 'empty', 'improving', 'first', 'within', 'inside', 'away', 'toward', 'reading'}

# the chain: Exhibit THIRTY's numbered sentences and the opening of Natural Intelligence
chain_words = set()
thirty = [f for f in glob.glob(os.path.join(R, 'Exhibit_THIRTY_Co-Chaining*_v*.md'))][0]
for l in open(thirty, encoding='utf-8'):
    m = re.match(r'^\d+\. (.*)', l.strip())
    if m:
        chain_words.update(w.lower() for w in words(plain(m.group(1))))
ni = [f for f in glob.glob(os.path.join(R, 'Natural_Intelligence_v*.md'))][0]
for l in open(ni, encoding='utf-8'):
    if l.startswith('**ONE'):
        break
    chain_words.update(w.lower() for w in words(plain(l)))
chain_parts = {p for w in chain_words for p in w.split('-')}
in_chain = lambda w: w in chain_words if '-' in w else (w in chain_words or w in chain_parts)

# the page
sents, cur = [], None
for l in open(PAGE, encoding='utf-8'):
    s = l.rstrip('\n')
    m = re.match(r'^(\d+)\. (.+)$', s)
    if m:
        cur = {'n': int(m.group(1)), 's': squeeze(plain(m.group(2))), 'from': [], 'its': [], 'adding': ''}
        sents.append(cur)
    elif cur and re.match(r'^\s+- From ', s):
        cur['from'] += [squeeze(q) for q in re.findall(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', s)]
        cur['its'] += [int(x) for x in re.findall(r'its (\d+)', s)]
        cur['has_from'] = True
    elif cur and re.match(r'^\s+- Adding:', s):
        cur['adding'] = squeeze(s.split('Adding:', 1)[1])

fails, lines = 0, []
def say(t):
    global fails
    fails += 1
    lines.append('  ' + t)

not_chain = {}
for c in sents:
    ws = [w.lower() for w in words(c['s'])]
    for w in ws:
        for name, group in (('a released word', released), ('a word dissolved alone', dissolved),
                            ('an is-not of 18 November', is_not)):
            if w in group:
                say(f"{c['n']}: {name}, {w}")
        if not in_chain(w):
            not_chain.setdefault(w, []).append(c['n'])
    if any(c['s'] in t for t in living.values()):
        say(f"{c['n']}: living already, word for word")
    if not c.get('has_from'):
        say(f"{c['n']}: no From")
    for k in c['its']:
        if k >= c['n']:
            say(f"{c['n']}: its From is of {k}, no sentence before it")
    for q in c['from']:
        if not any(q in t for t in living.values()) and not any(q in t for t in gathering.values()):
            say(f"{c['n']}: a From found word for word in no file: {q[:80]}")
    if not c['adding']:
        say(f"{c['n']}: no Adding")

print(f"{os.path.basename(PAGE)}: {len(sents)} sentences")
print(f"from a living sentence: {sum(1 for c in sents if c['from'])}; from a sentence of the page alone: "
      f"{sum(1 for c in sents if c['its'] and not c['from'])}")
for t in lines:
    print(t)
print(f"fails: {fails}")
print(f"\neach word the chain has not, {len(not_chain)}, with its sentences:")
for w in sorted(not_chain, key=lambda w: (not_chain[w][0], w)):
    print(f"  {w}: {', '.join(str(n) for n in sorted(set(not_chain[w])))}")
long = [(c['n'], len(words(c['s']))) for c in sents if len(words(c['s'])) > 22]
print(f"\nlonger than twenty-two words: {', '.join(f'{n} ({k})' for n, k in long) or 'none'}")
