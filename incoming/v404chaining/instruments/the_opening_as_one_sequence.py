"""The opening at its newest as one sequence: each sentence after the sentence of each name in it. All or none at
all, by each sentence of the candidate.
Reads the candidate in the head of Natural Intelligence's gathering file, and each living file at the root;
executes; writes no file; decides nothing.

Use: python3 -I incoming/v404chaining/instruments/the_opening_as_one_sequence.py <root>
     python3 -I incoming/v404chaining/instruments/the_opening_as_one_sequence.py <root> order
         the candidate order whole, each of its rows as the page has them
     python3 -I incoming/v404chaining/instruments/the_opening_as_one_sequence.py <root> page <a page>
         each row of a page's order read with this executing's own, each letter

What it reads.
  A name: a name the candidate has in bold. Its own line is the first line with it in bold, and its own sentence
  the first sentence with it in bold. A name is found by its word forms: with s; a name with y by y and by ies;
  self by self and selves; name by name, names, named and naming.
  A part: a line's own sentence, the line divided after a full stop; or an adding in square marks, whole. An
  adding opening with the words Not yet distinguished is a note of its line: it goes with the sentence it is
  after and is read by no binary.
  The word other, in five places read by hand, is a plain word and no name of a self: each is in PLAIN, word
  for word, and passed over.

It says:
  1. by lines: each line with a name before that name's own line, the line's own sentences and its addings apart
  2. by lines: each circle, lines each having a name of an other of them, with no order having each after each
  3. by sentences: each part with a name before that name's own sentence, and each circle of sentences
  4. the candidate order whole, by one rule with three lines: a part is after the own sentence of each name in
     it and after the sentence before it in its line, an adding after the sentence it is added to; a line's
     parts go on together until a name parts them; and of the parts ready, the one first in the candidate goes
     first. Each part going to an other place is said with the name it is after. Then the one binary again,
     with each part of the order.
  5. each bonded name, two words or more with a hyphen, with no line of its own: the lines having it, and its
     places in the living files and in Natural Intelligence's gathering file
  6. each name the living opening has in bold, in a line of the candidate with no line of its own in it

Returned at main, Merge #835, 16 November 2026:
  1. eleven lines: 7, 9, 10, 13, 14, 15, 17, 18, 19, 27 and 33. Six by their own sentences: 7, parity; 10,
     is-or-is-not and non-living; 13, self and other; 17 and 18, me-parity; 19, parity and all-parity. Six by an
     adding: 9, 14, 15, 17, 27 and 33, line 17 by each. Line 1 has other a plain word.
     `incoming/v403mgr/instruments/next_version_sized.py` says eleven too, and not the same eleven: it has
     line 1, by other, and no line 7. Its lines find a name with parity by its many alone, and line 7's parity
     and line 19's all-parity are each one.
  2. two circles of lines: 10 with 11, a name and is-or-is-not; and 17, 18 and 23, a self, a me and a me-parity.
  3. thirteen parts with a name before that name's own sentence, and no circle of sentences: each circle of
     lines opens by its sentences.
  4. 95 parts: 68 own sentences, 21 addings and 6 notes. Eighteen go to an other place, ten own sentences and
     eight addings, and each other part is in the candidate's own order. The binary again: each part of the
     order is after the own sentence of each name in it.
  5. eighteen bonded names with no line of their own. Seven are in no living file: non-same-existing,
     society-self, now-and-same-existing, other-than-self-parity, prior-and-same-existing, self-interesting and
     self-other. now-existing is in twelve lines of the candidate and in seventeen living files of thirty-three.
  6. two: universal set, in lines 18, 24, 25 and 44; and stable form, in lines 17, 48 and 51.
"""
import collections, glob, os, re, sys

R = sys.argv[1]; WORD = sys.argv[2] if len(sys.argv) > 2 else ''
PLAIN = ('no other things', 'each with each other', 'the other one of two', 'the one and then the other',
         'facing each other')

g = open(os.path.join(R, 'gathering-value', 'Natural_Intelligence.md'), encoding='utf-8').read()
found = re.findall(r'^- \*\*An explaining\*\* · The opening at its newest, laid.*$', g, re.M)
assert len(found) == 1, 'the candidate, once in the head: ' + str(len(found))
cand = found[0]
lines = re.split(r'\s(?=\d{1,2}\. (?:\((?:newer|not yet distinguished)\) )?[A-Z\[*])', cand[cand.find(' 1. '):].strip())
lines = [l for l in lines if re.match(r'\d{1,2}\. ', l)]
num = lambda l: int(re.match(r'(\d+)\.', l).group(1))
assert [num(l) for l in lines] == list(range(1, len(lines) + 1)), [num(l) for l in lines]
plain = lambda s: re.sub(r'\*\*|\*', '', s)

# parts: (line, place in its line) -> kind, text
parts = {}; order0 = []
for l in lines:
    n = num(l); body = re.sub(r'^\d+\. ', '', l); k = 0; mark = ''
    m = re.match(r'(\((?:newer|not yet distinguished)\) )', body)
    if m: mark = m.group(1); body = body[m.end():]
    for piece in re.split(r'(\[[^\]]*\])', body):
        piece = piece.strip()
        if not piece: continue
        if piece.startswith('['):
            kind = 'note' if piece.startswith('[Not yet distinguished') else 'adding'
            parts[(n, k)] = (kind, piece); order0.append((n, k)); k += 1
        else:
            for s in re.split(r'(?<=\.)\s+(?=[A-Z*])', piece):
                parts[(n, k)] = ('own', mark + s); mark = ''; order0.append((n, k)); k += 1
assert all(parts[p][0] == 'own' for p in order0 if p[1] == 0), 'each line opens with its own sentence'

own_line, own_part = {}, {}
for p in order0:
    kind, t = parts[p]
    for b in re.findall(r'\*\*(.+?)\*\*', t):
        assert kind == 'own', ('a name in bold in an adding', p, b)
        own_line.setdefault(b.lower(), p[0]); own_part.setdefault(b.lower(), p)

def forms(k):
    if k == 'self': core = r'sel(?:f|ves)'
    elif k == 'name': core = r'nam(?:es?|ed|ing)'
    elif k.endswith('y'): core = re.escape(k[:-1]) + r'(?:y|ies)'
    else: core = re.escape(k).replace(r'\ ', r'[ -]') + r's?'
    return re.compile(r'(?<![\w-])' + core + r'(?![\w-])', re.I)
P = {k: forms(k) for k in own_part}
def text_read(t):
    t = plain(t)
    for ph in PLAIN: t = t.replace(ph, ph.replace('other', '·'))
    return t
def names_in(p):
    kind, t = parts[p]
    return set() if kind == 'note' else {k for k in P if P[k].search(text_read(t))}
has = {p: names_in(p) for p in order0}
plain_places = [(p[0], ph) for p in order0 for ph in PLAIN if parts[p][0] != 'note' and ph in plain(parts[p][1])]
assert sorted(ph for _, ph in plain_places) == sorted(PLAIN), plain_places

def circles(nodes, need):
    """each set of two or more, each reaching each: no order has each after each"""
    reach = {a: set() for a in nodes}
    for a in nodes:
        todo = list(need[a])
        while todo:
            b = todo.pop()
            if b not in reach[a]: reach[a].add(b); todo.extend(need[b])
    seen, out = set(), []
    for a in nodes:
        if a in seen: continue
        ring = sorted([a] + [b for b in reach[a] if a in reach[b] and b != a])
        if len(ring) > 1: out.append(ring)
        seen.update(ring)
    return out

# 1 and 2, by lines
by_line = collections.defaultdict(lambda: {'own': set(), 'adding': set()})
for p in order0:
    kind = parts[p][0]
    if kind == 'note': continue
    for k in has[p]:
        if own_line[k] > p[0]: by_line[p[0]][kind].add(k)
need_line = {n: set() for n in range(1, len(lines) + 1)}
for p in order0:
    if parts[p][0] == 'own':
        need_line[p[0]] |= {own_line[k] for k in has[p] if own_line[k] != p[0]}
line_circles = circles(sorted(need_line), need_line)

# 3 and 4, by sentences
need = {p: set() for p in order0}
for i, p in enumerate(order0):
    need[p] |= {own_part[k] for k in has[p] if own_part[k] != p}
    before = [q for q in order0[:i] if q[0] == p[0] and parts[q][0] == 'own']
    if before: need[p].add(before[-1])      # after the sentence before it in its line, or the one it is added to
part_circles = circles(order0, need)
early = {p: sorted(k for k in has[p] if own_part[k] > p) for p in order0}

placed, new = set(), []
ring_of = {p: r for r in part_circles for p in r}
def ready(p):
    inside = set(ring_of.get(p, ()))
    return all(q in placed or (q in inside and q > p) for q in need[p])
while len(new) < len(order0):
    cands = [p for p in order0 if p not in placed and ready(p)]
    assert cands, 'no part ready'
    same = [p for p in cands if new and p[0] == new[-1][0]]
    nxt = (same or cands)[0]
    new.append(nxt); placed.add(nxt)
at = {p: i for i, p in enumerate(new)}
# a part goes to an other place with a part of a later place in the candidate before it in the order
high, goes = (0, -1), set()
for p in new:
    if p < high: goes.add(p)
    else: high = p
not_after = [(p, k) for p in new for k in has[p] if own_part[k] != p and at[own_part[k]] > at[p]]

def why(p):
    last = max(need[p], key=lambda q: at[q])
    ks = sorted(k for k in has[p] if own_part[k] == last)
    if ks: return 'after ' + ', '.join('*' + k + '*' for k in ks)
    return 'with the sentence it is added to' if parts[p][0] != 'own' else 'with the sentence before it in its line'
def rows():
    out = []
    for i, p in enumerate(new, 1):
        out.append(f'| {i} | {p[0]} | {parts[p][1]} | {why(p) if p in goes else ""} |')
    return out

if WORD == 'order':
    print('\n'.join(rows())); sys.exit(0)
if WORD == 'page':
    page = open(sys.argv[3], encoding='utf-8').read().split('\n')
    theirs = [l for l in page if re.match(r'\| \d+ \| \d+ \| ', l)]
    mine = rows()
    print('rows of the page:', len(theirs), ' rows of this executing:', len(mine),
          ' each letter the same:', theirs == mine)
    sys.exit(0 if theirs == mine else 1)

kinds = collections.Counter(parts[p][0] for p in order0)
print('the opening at its newest:', len(lines), 'lines,', len(own_part), 'names in bold,', len(order0), 'parts:',
      kinds['own'], 'own sentences,', kinds['adding'], 'addings,', kinds['note'], 'notes')
print('the word other, plain and passed over:', ', '.join(f'line {n}, {ph}' for n, ph in plain_places))
print('1. by lines, each line with a name before that name\'s own line:', len(by_line))
for n in sorted(by_line):
    for kind in ('own', 'adding'):
        if by_line[n][kind]:
            print(f'   line {n:2d}  {"its own sentences" if kind == "own" else "an adding":17s}  '
                  + ', '.join(f'{k} ({own_line[k]})' for k in sorted(by_line[n][kind], key=lambda k: own_line[k])))
print('   by their own sentences:', sorted(n for n in by_line if by_line[n]['own']),
      ' and line 1 with other a plain word')
print('   by an adding:', sorted(n for n in by_line if by_line[n]['adding']))
print('2. by lines, each circle:', len(line_circles))
for r in line_circles:
    print('   lines', r)
    for a in r:
        for b in r:
            ks = sorted({k for p in order0 if p[0] == a and parts[p][0] == 'own' for k in has[p] if own_line[k] == b and a != b})
            if ks: print(f'      line {a} has {", ".join(ks)}, the name of line {b}')
print('3. by sentences, each part with a name before that name\'s own sentence:', sum(1 for p in order0 if early[p]))
for p in order0:
    if early[p]: print(f'   line {p[0]:2d}, {parts[p][0]:6s}  {", ".join(early[p])}  ::  {plain(parts[p][1])[:74]}')
print('   each circle of sentences:', len(part_circles), part_circles)
print('4. the candidate order whole:', len(new), 'parts;', len(goes), 'go to an other place,',
      sum(1 for p in goes if parts[p][0] == 'own'), 'own sentences and', sum(1 for p in goes if parts[p][0] != 'own'), 'addings')
for p in new:
    if p in goes: print(f'   line {p[0]:2d}, {parts[p][0]:6s}  {why(p):46s}  ::  {plain(parts[p][1])[:60]}')
print('   each other part in the candidate\'s own order:', [p for p in new if p not in goes] == [p for p in order0 if p not in goes])
print('   the binary again, each part after the own sentence of each name in it:', not not_after, not_after)

living = sorted(f for f in glob.glob(os.path.join(R, '*_v*.md')))
text = {os.path.basename(f): open(f, encoding='utf-8').read() for f in living}
bonded = collections.defaultdict(list)
have = set(own_part) | {k + 's' for k in own_part} | {re.sub(r'y$', 'ies', k) for k in own_part}
for l in lines:
    for w in set(re.findall(r'(?<![\w-])[a-z]+(?:-[a-z]+)+(?![\w-])', plain(l).lower())):
        if w not in have and w not in ('is-or-is-not', 'is-or-is-other-than'): bonded[w].append(num(l))
print('5. bonded names with no line of their own:', len(bonded), ' living files read:', len(living))
in_none = []
for w, ns in sorted(bonded.items(), key=lambda x: (-len(x[1]), x[0])):
    pat = re.compile(r'(?<![\w-])' + re.escape(w) + r'(?:s|ies)?(?![\w-])', re.I)
    each = {f: len(pat.findall(t)) for f, t in text.items()}
    files = sum(1 for c in each.values() if c)
    if not files: in_none.append(w)
    print(f'   {w:26s} lines {sorted(ns)}   living files having it: {files}, its places: {sum(each.values())};'
          f' its places in Natural Intelligence\'s gathering file: {len(pat.findall(g))}')
print('   in no living file:', in_none)

ni = text[max((f for f in text if re.match(r'Natural_Intelligence_v', f)), key=lambda f: int(re.search(r'_v(\d+)', f).group(1)))]
op = re.search(r'^# Natural Intelligence\n\n\*\*[^\n]*\*\*\n\n(.*?)\n\n\*\*ONE · ', ni, re.S | re.M).group(1)
sent = [l.rstrip(' \\') for l in op.split('\n') if l.strip()]
living_own = {}
for s in sent:
    for b in re.findall(r'\*\*(.+?)\*\*', s): living_own.setdefault(b.lower(), s)
print('6. each name the living opening has in bold, in a line of the candidate with no line of its own there:')
for k, s in living_own.items():
    if k in own_part or len(k) < 2: continue
    pat = re.compile(r'(?<![\w-])' + re.escape(k).replace(r'\ ', r'[ -](?:same-existing )?') + r's?(?![\w-])', re.I)
    ns = sorted({num(l) for l in lines if pat.search(plain(l))})
    if ns: print(f'   {k}: lines {ns}; its living sentence: {s}')
