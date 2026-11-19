"""Each numbered sentence of the chain, Exhibit THIRTY Co-Chaining Logic Registry: is it co-chaining from its priors?

Reads Exhibit THIRTY at the root given, the set's list of released words, the table of Exhibit TWENTY Natural
Naming's dissolved words and the four sessions' one list of words of no natural naming; executes; writes no
file; decides nothing. An executing finds candidates, and an executing is not a pass.

Said in the session: start at the beginning of exhibit thirty and do every sentence and all the gathering for
thirty as well. they all need to co-chaining from priors.

Use: python3 -I incoming/v404universe/instruments/each_sentence_of_the_chain_from_its_priors.py <root>
         the chain sized, and a line with a part
     python3 -I incoming/v404universe/instruments/each_sentence_of_the_chain_from_its_priors.py <root> part <a number>
         a line with a sentence of the part: its words opening with it, its cites and its words of a list
     python3 -I incoming/v404universe/instruments/each_sentence_of_the_chain_from_its_priors.py <root> word <a word>
         the sentence a word opens with, the sentence adding it, and its sentences before its adding

What it reads. A sentence of the chain is a line opening with its number and a full stop; its adding is the
line after it with *Adding:*; a part is a heading of two hashes with its number. A word is letters with the
hyphens joining them, with no case; a closing s is passed over, as selves with self and parities with parity.
Words of grammar are passed over: an article, a word of relation, a joining word, a self's small words.

Four findings with a sentence, a sentence with none of the four found co-chaining from its priors:
  1  a word opening with it, in no sentence before it, that its own adding has not
  2  a cite of a step after it, a sentence from its next and not from a prior
  3  a released word, or a word Natural Naming has dissolved alone
  4  a word of the one list, no natural naming by a partner's is-not

Its own check: a sentence with its number one after the number before, and an adding with a sentence.
It closes with its fails.

Returned on 18 November 2026, fails 0 with both:
  the next version's copy, Exhibit THIRTY v403mgr: 755 sentences in 46 parts; 1 with 308, 2 with none, 3 with
  122, 4 with 525; none of the four with 153. The first part, 1 to 11: none of the four with its eleven.
  main, Exhibit THIRTY v402mgr: 1 with 308, 2 with none, 3 with 140, 4 with 548; none of the four with 132.
"""
import csv, glob, os, re, sys, collections

R = sys.argv[1]
MODE = sys.argv[2] if len(sys.argv) > 2 else ''
ARG = sys.argv[3] if len(sys.argv) > 3 else ''
plain = lambda t: re.sub(r'\*\*|\*|__', '', t)
GRAMMAR = set('''a an the is are was be being been of and or to with its it as by in on at for from no not one two
three four five six this that these those which while than then their they them only any all none both either neither
each other own same whole so if but nor into onto over under up down out off through about between among after before
again once twice yet still also too more most less least first next now prior here there when where what who whose how
why i we our us you your he she his her me my mine'''.split())
KEEP = {'other', 'own', 'same', 'whole', 'next', 'now', 'prior', 'between', 'all', 'one', 'me', 'first', 'each'}
GRAMMAR -= KEEP


def norm(w):
    w = w.lower()
    if w == 'selves':
        return 'self'
    if w.endswith('ies') and len(w) > 4:
        return w[:-3] + 'y'
    if w.endswith('s') and not w.endswith('ss') and len(w) > 3:
        return w[:-1]
    return w


def words(t):
    return [norm(w) for w in re.findall(r"[A-Za-zφ]+(?:-[A-Za-z]+)*", plain(t)) if len(w) > 1]


thirty = sorted(glob.glob(os.path.join(R, 'Exhibit_THIRTY_Co-Chaining*_v*.md')))[0]
parts, sents, cur, part = [], [], None, None
for l in open(thirty, encoding='utf-8'):
    s = l.rstrip('\n')
    m = re.match(r'^## (\d+) (.+)$', s)
    if m:
        part = (int(m.group(1)), m.group(2)); parts.append(part); continue
    m = re.match(r'^(\d+)\. (.+)$', s.strip())
    if m and part:
        cur = {'n': int(m.group(1)), 's': m.group(2), 'part': part[0], 'adding': None}
        sents.append(cur); continue
    m = re.match(r'^\s*\*Adding: (.+?)\*?\s*$', s)
    if m and cur and cur['adding'] is None:
        cur['adding'] = m.group(1)

released = set()
for l in open(os.path.join(R, 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt'), encoding='utf-8'):
    l = l.strip()
    if l and not l.startswith('#'):
        released.add(l.lower())
dissolved = set()
p = os.path.join(R, 'incoming/v403cohering/Each_dissolved_word_with_its_saying.csv')
if os.path.exists(p):
    for r in list(csv.reader(open(p, encoding='utf-8')))[1:]:
        if r[1].strip().lower().startswith('alone') and ' ' not in r[0].strip():
            dissolved.add(r[0].strip().lower())
listed = set()
p = os.path.join(R, 'incoming/v404mgr/Words_of_no_natural_naming_with_their_natural_naming.md')
if os.path.exists(p):
    for l in open(p, encoding='utf-8'):
        if l.startswith('| *'):
            cell = l.split('|')[1]
            if re.fullmatch(r'\s*(\*[^*]+\*,?\s*)+', cell):          # a word with no words beside it
                for w in re.findall(r'\*([^*]+)\*', cell):
                    if ' ' not in w.strip():
                        listed.add(w.strip().lower())
listed |= {'zone', 'warning', 'wrapper'}

seen, opens, adds = set(), {}, {}
fails = 0
for i, c in enumerate(sents):
    if c['n'] != i + 1 or c['adding'] is None:
        fails += 1
    ws = words(c['s'])
    aw = set(words(c['adding'] or ''))
    for w in aw:
        adds.setdefault(w, c['n'])
    raw = [w.lower() for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", plain(c['s']))]
    c['new'] = []
    for w in dict.fromkeys(ws):
        if w in GRAMMAR:
            continue
        if w not in seen:
            opens[w] = c['n']
            c['new'].append((w, w in aw))
    seen.update(ws)
    c['cites'] = sorted({int(x) for m in re.finditer(r'steps? ([0-9][0-9, andto]*)', plain(c['s'])) for x in re.findall(r'\d+', m.group(1))})
    c['later'] = [k for k in c['cites'] if k > c['n']]
    c['rel'] = sorted({w for w in raw if w in released or w in dissolved})
    c['list'] = sorted({w for w in raw if w in listed})
    c['f1'] = [w for w, a in c['new'] if not a]
    c['whole'] = not (c['f1'] or c['later'] or c['rel'] or c['list'])

if MODE == 'part':
    k = int(ARG)
    title = dict(parts)[k]
    mine = [c for c in sents if c['part'] == k]
    print(f"part {k}, {title}: {len(mine)} sentences, {mine[0]['n']} to {mine[-1]['n']}")
    for c in mine:
        print(f"\n{c['n']}. {plain(c['s'])}")
        print(f"     adding: {c['adding']}")
        if c['new']:
            print('     words opening with it: ' + ', '.join(w + ('' if a else ' [its adding has it not]') for w, a in c['new']))
        if c['cites']:
            print('     cites: ' + ', '.join(str(x) + (' [a step after it]' if x > c['n'] else '') for x in c['cites']))
        if c['rel']:
            print('     released or dissolved alone: ' + ', '.join(c['rel']))
        if c['list']:
            print('     of the one list: ' + ', '.join(c['list']))
        print('     ' + ('co-chaining from its priors, by the four' if c['whole'] else 'a finding with it'))
    print(f"\nco-chaining from its priors: {', '.join(str(c['n']) for c in mine if c['whole']) or 'none'}")
    print(f"fails: {fails}")
    sys.exit(0)

if MODE == 'word':
    w = norm(ARG)
    print(f"{w}: opening with sentence {opens.get(w, 'none')}; in an adding with sentence {adds.get(w, 'none')}")
    before = [c['n'] for c in sents if w in words(c['s']) and c['n'] < adds.get(w, 10 ** 9)]
    print(f"  its sentences before its adding: {len(before)}" + (': ' + ', '.join(map(str, before[:40])) if before else ''))
    sys.exit(0)

N = len(sents)
print(f"{os.path.basename(thirty)}: {N} sentences in {len(parts)} parts")
print(f"  1  a word opening with it that its own adding has not: {sum(1 for c in sents if c['f1'])}")
print(f"  2  a cite of a step after it: {sum(1 for c in sents if c['later'])}")
print(f"  3  a released word, or a word dissolved alone: {sum(1 for c in sents if c['rel'])}")
print(f"  4  a word of the one list: {sum(1 for c in sents if c['list'])}")
print(f"  none of the four, co-chaining from its priors: {sum(1 for c in sents if c['whole'])}")
print(f"  with none of 1 and 2, its words and its cites of priors: {sum(1 for c in sents if not c['f1'] and not c['later'])}")
lw = collections.Counter(w for c in sents for w in c['list'])
print('  words of the one list, by sentences: ' + ', '.join(f'{w} {n}' for w, n in lw.most_common()))
rw = collections.Counter(w for c in sents for w in c['rel'])
print('  released or dissolved alone, by sentences: ' + ', '.join(f'{w} {n}' for w, n in rw.most_common(14)))
print("\na part: its sentences · none of the four · 1 · 2 · 3 · 4")
for k, title in parts:
    mine = [c for c in sents if c['part'] == k]
    if not mine:
        continue
    print(f"  {k:>2} {title[:60]:60s} {len(mine):>3} · {sum(c['whole'] for c in mine):>3} · {sum(bool(c['f1']) for c in mine):>3} · "
          f"{sum(bool(c['later']) for c in mine):>3} · {sum(bool(c['rel']) for c in mine):>3} · {sum(bool(c['list']) for c in mine):>3}")
print(f"\nits own check, a sentence's number after the number before and an adding with it: fails: {fails}")
