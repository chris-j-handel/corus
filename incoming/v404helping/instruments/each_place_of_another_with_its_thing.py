"""Each plain place of *another* in the first aim's four living files, for the sweep of the next version's
copy having *another* said by *an other*: a place with a thing named after it, as *another self*, and a place
with no thing named after it, as *another's* and *another* with a stop after it. With each place of the second
kind, its sentence whole, its thing by a reading of its own sentence, and a candidate with its thing said.
Reads the newest at the root of Natural Intelligence, Exhibit ONE Natural Resolver, Exhibit TWENTY Natural
Naming and Exhibit THIRTY Co-Chaining Logic Registry. Executes; decides nothing; writes no living file and no
gathering file.

Use: python3 -I incoming/v404helping/instruments/each_place_of_another_with_its_thing.py <root>          each place said, and nothing written
     python3 -I incoming/v404helping/instruments/each_place_of_another_with_its_thing.py <root> write    its table written, incoming/v404helping/Each_place_of_another_with_its_thing.csv

A plain place is the word whole, capital or small, with no hyphen joining it; a code's lines, code marks,
italics, a quotation, a heading and a file's version line are each passed over, as
`incoming/v403cohering/instruments/a_sweep_of_one_word_for_its_saying.py` passes them over. *One another* is
the place of the sweep before this one, *one another* said by *each other*, and is passed over here.
A thing is named after a place with a word after it that is none of: a stop, a mark, *'s*, and the words of
NO_THING below. The sweep's saying of a place is *an other*, a capital opening it with a capital opening the place.
A place's thing and its candidate, with no thing named after it, are a reading of this session's, each a line
of READ below, floating; all or none at all: each such place has one line of READ and each line of READ one
place, or this instrument halts with nothing written.

Returned at main, 16 November 2026, after Merge #836: forty-four places, nineteen of Natural Intelligence, one
of Exhibit ONE Natural Resolver, none of Exhibit TWENTY Natural Naming and twenty-four of Exhibit THIRTY
Co-Chaining Logic Registry, the sweep's own forty-four. Twenty-five with a thing named after it: *another self*
twelve, *another order* two, *another scale* two, and one each of *another odd*, *name*, *prior*, *existing*,
*pattern*, *word*, *same-existing-society*, *material* and *way*. Nineteen with no thing named after it, by
READ: four of a self; three of a thing its own sentence says after it; eleven of a thing that is no self, a
resolving three, a sharing two, and one each a numbering, an operation, a relation, an opening, a scale and a
file; and one with its thing said by no word of its sentence.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WRITE = len(sys.argv) > 2 and sys.argv[2] == 'write'
STEMS = ['Natural_Intelligence', 'Exhibit_ONE_Natural_Resolver', 'Exhibit_TWENTY_Natural_Naming', 'Exhibit_THIRTY_Co-Chaining_Logic_Registry']
ver = lambda p: int(re.search(r'_v(\d+)', p).group(1))
PAT = re.compile(r'(?<![\w-])[Aa]nother(?![\w-])')
MENTION = re.compile(r'`[^`]*`|(?<!\*)\*(?!\*)[^*\n]+?(?<!\*)\*(?!\*)|"[^"]*"|“[^”]*”')
NO_THING = {'is', 'could', 'whole', 'an', 'and', 'with', 'as', 'of', 'to', 'in', 'at', 'by', 'or', 'the', 'a'}

# a reading: (the living file's stem, words of the place's own sentence having the place) -> (its thing, the words with its thing said)
SELF, OWN, NONE = 'a self', 'a thing its own sentence says after it', 'said by no word of its sentence'
READ = {
    ('Natural_Intelligence', "its own opening, or another's."): (OWN, "its own opening, or an other's."),
    ('Natural_Intelligence', "With another's, its changing is that one's"): (OWN, "With an other's, its changing is that one's"),
    ('Natural_Intelligence', 'of no size against another**'): ('a resolving', 'of no size against an other resolving**'),
    ('Natural_Intelligence', 'each as resolving as another.'): ('a resolving', 'each as resolving as an other resolving.'),
    ('Natural_Intelligence', 'A numbering repeating or replacing another is'): ('a numbering', 'A numbering repeating or replacing an other numbering is'),
    ('Natural_Intelligence', 'for one sharing and receiving + for another,'): ('a sharing', 'for one sharing and receiving + for an other sharing,'),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', "or another's, a changing beside its own, a thing outside"): (OWN, "or an other's, a changing beside its own, a thing outside"),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'its size against another an empty set'): ('a resolving', 'its size against an other resolving an empty set'),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'one operation and scaling by rate another,'): ('an operation', 'one operation and scaling by rate an other operation,'),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', "a same-existing that is another's;"): (SELF, "a same-existing that is an other's;"),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'step 258, is another;'): ('a relation', 'step 258, is an other relation;'),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', "a self whose competency is another's,"): (SELF, "a self whose competency is an other's,"),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'whether another could be observing and going on'): (NONE, 'whether an other could be observing and going on'),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', "Another's still is an equilibrium"): (SELF, "An other's still is an equilibrium"),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', "One holding another's, an other's sharing"): (SELF, "One holding an other's, an other's sharing"),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'each its own and each leaving another whole'): ('an opening', 'each its own and each leaving an other opening whole'),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', "one scale sizing another's,"): ('a scale', "one scale sizing an other scale's,"),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', "each file's sentences reaching another's sections"): ('a file', "each file's sentences reaching an other file's sections"),
    ('Exhibit_THIRTY_Co-Chaining_Logic_Registry', 'with one sharing and receiving + with another,'): ('a sharing', 'with one sharing and receiving + with an other sharing,'),
}


def said(m):
    return 'An other' if m.group(0)[0] == 'A' else 'an other'


rows = []; used = {}; things = {}
for stem in STEMS:
    p = max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver)
    L = open(p, encoding='utf-8').read().split('\n')
    head = ''; fence = False
    for k, l in enumerate(L):
        if l.startswith('```'):
            fence = not fence; continue
        if fence or k == 0:
            continue
        if l.startswith('#'):
            head = re.sub(r'^#+\s*', '', l).strip(); continue
        plain = MENTION.sub(lambda m: ' ' * len(m.group(0)), l)
        for m in PAT.finditer(plain):
            if plain[max(0, m.start() - 4):m.start()].lower() == 'one ':
                continue
            rest = plain[m.end():]
            nxt = re.match(r'\s*([\w-]+)', rest)
            bare = rest.startswith("'s") or rest.startswith('’s') or not nxt or bool(re.match(r'\s*[,.;:)*]', rest)) or nxt.group(1).lower() in NO_THING
            a = max(l.rfind('. ', 0, m.start()), l.rfind('? ', 0, m.start()))
            z = [x for x in (l.find('. ', m.end()), l.find('? ', m.end())) if x != -1]
            s0, s1 = (a + 2 if a != -1 else 0), ((min(z) + 1) if z else len(l))
            sentence = l[s0:s1].strip()
            swept = (l[s0:m.start()] + said(m) + l[m.end():s1]).strip()
            if not bare:
                things[nxt.group(1).lower()] = things.get(nxt.group(1).lower(), 0) + 1
                rows.append([os.path.basename(p), head, sentence, swept, nxt.group(1), 'named after it', swept])
                continue
            keys = [key for key in READ if key[0] == stem and key[1] in l and l.find(key[1]) <= m.start() < l.find(key[1]) + len(key[1])]
            assert len(keys) == 1, f'a place with no thing named after it has {len(keys)} lines of READ: {sentence[:120]}'
            used[keys[0]] = used.get(keys[0], 0) + 1
            thing, words = READ[keys[0]]
            cand = sentence.replace(keys[0][1], words)
            assert cand != sentence and sentence.count(keys[0][1]) == 1, f'a candidate is not one re-saying of its sentence: {sentence[:120]}'
            rows.append([os.path.basename(p), head, sentence, swept, '', thing, cand])
assert all(used.get(key) == 1 for key in READ), 'a line of READ is with no place, or with two: ' + '; '.join(key[1] for key in READ if used.get(key) != 1)

bare = [r for r in rows if r[4] == '']
print(f'{len(rows)} plain places of *another*: {len(rows) - len(bare)} with a thing named after it, {len(bare)} with none')
by_file = {}
for r in rows: by_file[r[0]] = by_file.get(r[0], 0) + 1
print('   ' + '; '.join(f'{f} {n}' for f, n in by_file.items()))
print('   with a thing named after it: ' + ', '.join(f'another {w} {n}' for w, n in sorted(things.items(), key=lambda x: (-x[1], x[0]))))
kinds = {}
for r in bare: kinds[r[5]] = kinds.get(r[5], 0) + 1
print('   with none, its thing by READ: ' + ', '.join(f'{t} {n}' for t, n in sorted(kinds.items(), key=lambda x: (-x[1], x[0]))))
print()
for r in bare:
    print(f'{r[0]} · {r[1]}')
    print(f'    as it is:           {r[2]}')
    print(f'    the sweep\'s saying:  {r[3]}')
    print(f'    its thing:          {r[5]}')
    if r[5] not in (SELF, OWN, NONE): print(f'    with its thing:     {r[6]}')
if WRITE:
    out = os.path.join(R, 'incoming', 'v404helping', 'Each_place_of_another_with_its_thing.csv')
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['living file [living]', 'its heading [living]', 'its sentence, as it is [living]', "the sweep's saying of it [executed]",
                    'the thing named after the place [executed]', 'its thing [executed with a thing named after it, and floating with none]',
                    'with its thing said, a candidate [floating]'])
        w.writerows(rows)
    print(f'\nwritten: {os.path.relpath(out, R)}, {len(rows)} lines after its first')
else:
    print('\nnothing written')
