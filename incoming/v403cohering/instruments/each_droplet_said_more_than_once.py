"""Each droplet of the gathering files said more than once, by two readings. The first: a droplet found more than
once, word for word, within one gathering file and in two gathering files or more, each said with its places;
and, by the managing session's first rule, a droplet more than once with one heading of one gathering file is
once. The second: a droplet said whole within a longer droplet of its gathering file, each sentence of the
shorter a whole sentence of the longer, word for word, each said with its two places. All or none at all, by
each line and by each sentence.
Reads each gathering file; executes; with *apply* it writes the gathering files of the first rule alone. The
second reading writes nothing: a rule for each of its kinds is the managing session's, and none is entered yet.

Use: python3 -I incoming/v403cohering/instruments/each_droplet_said_more_than_once.py <root>          each reading, and nothing written
     python3 -I incoming/v403cohering/instruments/each_droplet_said_more_than_once.py <root> apply    the first rule, written

What it reads. A droplet: a line opening with a hyphen. A place: its gathering file, and the heading it is under.
The first reading: two droplets are one found twice with each letter the same.
The second reading: a droplet's sentences are its words after its kind's label, each mark of bold, italics and
code passed over, capital and small letters as one, each sentence to its stop. A label opening a droplet in
italics with its own stop, a capital, a digit or a mark after it, as *The current understanding, 6w-q.*, is no
sentence of the shorter droplet and is said with it. The shorter is said whole within the longer with each of
its sentences one of the longer's own sentences, whole; a sentence inside a longer sentence is not read as said.
A droplet with a middle dot after its kind's label is a row of cells, as a table's heading row, and is not read
as a shorter one.
The longer is the first such droplet in its file's order, and how many longer droplets have each sentence is said.

A rule for each kind, each the managing session v403mgr's, 16 November:
  1. One droplet more than once with one heading of one gathering file: the first is the droplet, and each other
     is away, no word of it lost.
  2. One droplet with each of more sections than one, each section's own living sentence the same words: each is
     its section's own, and each is as it is.
  3. One saying in two gathering files or more, with no file of its own in it: each is as it is, and the table
     of them is the partners' to read; a home for one concept is the partners' word.

Returned at main, 16 November 2026, after Merge #792: eleven droplets found more than once. Within one gathering
file, two: Exhibit TWENTY-SEVEN Living Ghost Registry's has one four times, each with its own section, rule 2;
Exhibit EIGHTEEN Natural Physics's has one six times at its back, rule 1. In two gathering files or more, nine:
three of *this file*, each its own file's, and six of one saying, rule 3.
Applied at main after Merge #802, 16 November 2026, the first rule: Exhibit EIGHTEEN Natural Physics's gathering
file, five lines away and the first of the six as it is; each droplet by its letters is in the file, as before.

The second reading, returned at main, 16 November 2026, after Merge #824: fifty-nine droplets, in two gathering
files. Natural Intelligence's, fifty-eight. Fifty of its opening's part with a droplet at its back: thirty-nine a
sentence of *The current understanding*, ten with no label and one of *A society*, each with the droplet at the
back opening with those sentences and going on with its cohering and its reading. Four of its section 6.5 with a
droplet at its back. Three with one heading: two of *The current understanding* with a parting tracked, in the
opening's part, and one at the back. One of its opening's part with the opening at its newest, at its head.
Exhibit EIGHTEEN Natural Physics's, one, with one heading: a session's note with *none*, said again in a longer
note. Exhibit TWENTY Natural Naming's three heading rows of its tables are rows of cells, and not read.
"""
import glob, os, re, sys

R = sys.argv[1]; APPLY = len(sys.argv) > 2 and sys.argv[2] == 'apply'
GV = os.path.join(R, 'gathering-value')
FILES = {os.path.basename(g)[:-3]: open(g, encoding='utf-8').read().split('\n') for g in sorted(glob.glob(os.path.join(GV, '*.md')))}
places = {}                                   # a droplet's line -> [(title, heading, index of its line)]
for title, L in FILES.items():
    cur = None
    for k, l in enumerate(L):
        if re.match(r'^#{2,3} ', l): cur = re.sub(r'^#{2,3} ', '', l).strip()
        if l.startswith('- '): places.setdefault(l, []).append((title, cur, k))
more = {l: w for l, w in places.items() if len(w) > 1}
within = {l: w for l, w in more.items() if len({t for t, _, _ in w}) == 1}
across = {l: w for l, w in more.items() if len({t for t, _, _ in w}) > 1}
print(f'{len(places)} droplets by their letters; {len(more)} found more than once: {len(within)} within one gathering file, {len(across)} in two or more')

away = {}                                     # rule 1: title -> indexes of the lines going
print('within one gathering file:')
for l, w in within.items():
    one_heading = len({h for _, h, _ in w}) == 1
    print(f"  {len(w)} times in {w[0][0].replace('_', ' ')}, rule {'1: the first is the droplet' if one_heading else '2: each its section own'}: {l[:100]}")
    print('      with: ' + '; '.join(sorted({h or 'no heading' for _, h, _ in w})))
    if one_heading: away.setdefault(w[0][0], []).extend(k for _, _, k in w[1:])
print('in two gathering files or more, rule 3, each as it is:')
for l, w in sorted(across.items(), key=lambda x: -len(x[1])):
    own = 'of this file, each its own' if re.search(r'\b(of|at) this file\b|\bthis file is\b', l) else 'one saying'
    print(f'  {len(w)} files, {own}: {l[:110]}')

# The second reading: a droplet said whole within a longer droplet of its gathering file
def plain(t):
    t = re.sub(r'[*`_]', '', t).replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', t).strip().lower()
LABEL = re.compile(r'^\*([^*]{1,160}?[.:])\*\s+(?=[A-Z0-9*"\u201c(])')
def words(l):                                 # a droplet's words after its kind's label, and its label in italics
    t = l.split(' \u00b7 ', 1)[1] if l.startswith('- **') and ' \u00b7 ' in l else l[2:]
    t = re.sub(r'\s*\*\((possible exploring|possible incohering|an explaining)\)\*\s*$', '', t)
    m = LABEL.match(t)
    return (m.group(1), t[m.end():]) if m else ('', t)
def sentences(t):
    return [s.strip().rstrip('.') for s in re.split(r'(?<=[.?!])\s+', plain(t)) if s.strip().rstrip('.')]
print()
print('the second reading, a droplet said whole within a longer droplet of its gathering file:')
kinds = {}; said = []; rows = 0
for title, L in FILES.items():
    cur = None; at = {}
    for k, l in enumerate(L):
        if re.match(r'^#{2,3} ', l): cur = re.sub(r'^#{2,3} ', '', l).strip()
        if l.startswith('- '): at[k] = cur or 'no heading'
    own = {k: set(sentences(' '.join(words(L[k])))) | set(sentences(words(L[k])[1])) for k in at}
    for k in at:
        label, t = words(L[k]); ss = sentences(t)
        if not ss or ' \u00b7 ' in t: rows += ' \u00b7 ' in t; continue
        longer = [j for j in at if j != k and len(L[j]) > len(L[k]) and all(s in own[j] for s in ss)]
        if longer:
            j = longer[0]; kind = 'with one heading' if at[k] == at[j] else f'{at[k]}, with {at[j]}'
            kinds.setdefault((title, kind), []).append(k)
            said.append((title, kind, label, t, at[j], L[j], len(longer)))
print(f"  {len(said)} droplets, in {len({s[0] for s in said})} gathering files; {rows} droplets with a middle dot after the kind's label, as a row of cells, not read as a shorter one")
for (title, kind), ks in kinds.items(): print(f"  {len(ks):3d}  {title.replace('_', ' ')} \u00b7 {kind}")
for title, kind, label, t, hj, lj, n in said:
    lw, tj = words(lj)
    print(f"    {title.replace('_', ' ')} \u00b7 {kind} \u00b7 in {n} longer")
    print(f"        the shorter: {('*' + label + '* ') if label else ''}{t[:150]}")
    print(f"        the longer:  {('*' + lw + '* ') if lw else ''}{tj[:110]}")
print('  a rule for each kind is the managing session\'s, and none is entered: nothing is written by this reading')
print()

n = sum(len(v) for v in away.values())
if APPLY and n:
    before = {t: set(l for l in FILES[t] if l.startswith('- ')) for t in away}
    for t, ks in away.items():
        L = FILES[t]
        for k in sorted(ks, reverse=True): del L[k]
        assert before[t] == set(l for l in L if l.startswith('- ')), 'a droplet by its letters is lost'
        open(os.path.join(GV, t + '.md'), 'w', encoding='utf-8').write('\n'.join(L))
print(('written, ' if APPLY and n else '') + f"rule 1: {n} lines {'away' if APPLY else 'to go'}" + (': ' + ', '.join(f"{t.replace('_', ' ')} {len(v)}" for t, v in away.items()) if n else ''))
