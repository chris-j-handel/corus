#!/usr/bin/env python3
"""Build the exhibit's next text: new opening paragraphs, section 1 with the window's names,
section 2's band tables from the log, sections 3 to 6 as they are, new sections 7 and 8."""
import csv, re, sys

ex_path, log_csv, spine_md, bands_md, window_json = sys.argv[1:6]
import json
WJ = json.load(open(window_json, encoding='utf-8'))
W = WJ['names']

def fill(text):
    def one(m):
        k = m.group(1)
        if k == 'revision':
            return WJ['revision']
        v = W[k]
        if 'see' in v:
            v = W[v['see']]
        return v['line'].split(' ')[0]
    return re.sub(r'\{([^{}]+)\}', one, text)
old = open(ex_path, encoding='utf-8').read().split('\n')

def idx(prefix):
    return next(i for i, l in enumerate(old) if l.startswith(prefix))

head = old[:idx('**A destiny is next living possibling')]          # title, subtitle, rule
contents = old[idx('1 Our observings, possiblings and discoverings'):idx('## 1 ')]  # contents, nbsp, rule
s3to6 = old[idx('## 3 '):idx('## 7 ')]

OPENING = """**A destiny is next living possibling, ahead.** The living expedition's destinies are its aims, all the concepts natural intelligence reaches from now to all of nature, and this exhibit is their log: a row for a destiny, the areas of surface on its path, its homes, and three columns, our observings, possiblings and discoverings, its chain back to the window's line 1, *Now is the existing moment.*

**The expedition is a self.** A named self is a same-named now-existing thing with its own prior-sequence, the window's line {self}, and the expedition is one, its versions its prior-sequence. Its observing is of its prior, the living files and registries; its possibling is of its next, the gathering files, the working documents and their suggestions; its discovering is of what is in neither yet, the new of its next version. The log's three columns are the expedition observing, possibling and discovering its own destinies, named by the resolver's names: observing, 7 and 15; possibling, 2 and 14; discovering, 13 and 9.

**All open, now.** A row is open to all at any moment, a partner and a session alike, for a suggesting, a pattern-matching, a breaking, an exploring or a possibling. A problem found in the logic is a cohering and co-chaining opportunity, laid as one in its row, and whoever relies on a discovery sees its rigor, line by line, back to now.

**Among the betweens.** A table between two exhibits is a thing of both and of neither alone, and this log is the between of the opening and all the destinies. Natural Emanating surfaces a row whose observing is whole; Natural Exploring walks a row's areas; Natural Intelligence and the field exhibits are the homes; the window of the opening and Exhibit THIRTY lay a row's chain; the gathering files are its possibling's place; Natural Intelligence Corus and corus.me say and surface it.
"""

S1_HEAD = """## 1 Our observings, possiblings and discoverings

A destiny's row is its name and its sentence, the areas of surface on its path, its homes, and three columns named by the resolver's names. Its areas are the sub-concepts its path crosses, local and interim, the places an explorer can walk, and the three columns sort them by the window of the opening as it is now, by the window's own lines {observing} to {discovering}.

- **Observing, 7 and 15**, now and prior-existing. What the window says of a destiny, chained to now: an area a numbered line names, said with its line's number, and a given word the lines use, said with the line it enters at.
- **Possibling, 2 and 14**, next and other-than same-existing. The opportunities open on its path now: an area a suggestion in the window names, or a numbered line with a rewording or its going on offer; then the open notes at the gathering sections of its homes, the candidates, possible explorings, possible incoherings and concerns found at them; then a note a pass found, laid as an opportunity.
- **Discovering, 13 and 9**, other-than next-and-same-existing. The co-chaining opportunities ahead: an area no line and no suggestion names, in italics, a word of the one list marked as one.

A line's reason is by the lines before it, back to line 1. The table gives the window's names, a line apiece, with the names its sentence is said with, as the window is at its revision {revision} of 21 November 2026. A line's number moves with the window's, and a session renewing the log renews it from the window as it is then.
"""

S1_TAIL = """Two findings, laid as opportunities. Line {other-than}, other-than, is said now with things, line {thing}, and things are said as other-than nothings, a word no line names: its chain to line 1 is still a co-chaining opportunity, a hole the window lists. Line {self} says a named self with no living and no observing in it, the observing-self, possibling-self and discovering-self following at {observing-self} to {discovering-self}: by its words a living file, its versions its prior-sequence, is a named self, and the river's two sayings, in 2.6, are the same opportunity.

The marks are a beginning. A pass through a row's homes chose its areas; the instrument making the columns, with the window's names and the areas as its inputs, is in incoming/v405now, renewed in incoming/v406aiming, and anyone corrects a mark.
"""

S7 = """## 7 This exhibit among the betweens

- **A table between two exhibits is a thing of both.** Its rows are things both exhibits name, a row two sayings of one thing, one apiece, as a me-parity is a bi-coupling's me, the window's line {me-parity}, a bi-coupling being both of two selves, line {bi-coupling}. The hard problems at their now name and next name are the between of Hard Problem Registry, the fields' own words, and Resolving the Hard Problem Registry, their resolving, a pair as the second says of itself. The seventeen names' table is the between of Exhibit ONE's code and Exhibit THIRTY's chain. Living File Registry is the set's own between; Living Ghost Registry and Equilibria Registry, one subtitle of not possibly existing, are the between of fields' installations and the resolver.
- **The tables by their two names.** Codons, elements, primes, physics observings, philosophy's dilemmas, engineering cases, the scale ladder and the living societies, a field's things as rows and the resolver's names as columns, all betweens.
- **The log, one more between.** Destinies as rows and the names' three roots as columns, the between of the opening and all the destinies, a row's chain back to line 1.
- **The method is the window's logic, applied to the file set.** A living file and its gathering file are same-named things, line {same-named}, and with its versions a named universal set, line {universal set}; its versions in order are its prior-sequence, line {prior-sequence}. Incoming is other-than, named by no file's name, line {other-than}, and all that are other-than nothings are things, line {thing}: a universal incoming. Versions are prior, now and next, a file same-existing across them, lines {prior} to {same-existing}. Value goes from other-than to same-named by a session's distinguishing, lines {observing} to {discovering}.
- **Geodesic, and a torus.** The file set is a surface dividing itself into sections, value going the shortest way to its one home. Two circles wind through one opening: along, a file's own versions; across, the betweens, incoming to gathering to section, tables and registries. The opening is now, line 1. A torus is the one closing surface with a flow and no rest point, and nothing in the method waits.
- **A reflexive triple.** Natural Explaining, Natural Emanating and this exhibit, one same core apiece, the expedition's own voice connected to the substrates it observes.
- **With the window's co-chaining.** The window lays the opening lines; Exhibit THIRTY carries the along; the betweens carry the across; the log is with both for all destinies.
"""

S8 = """## 8 How the log grows

- All rows are open now, to all, a partner and a session alike, at any moment.
- A session walks a row or an area and marks its columns; a reader matches a mark against its home; an explorer opens an area no row names yet; a breaker looks for its is-not.
- A problem found is laid as its opportunity in the possibling column of its row.
- A new row enters at the foot of its band, and a destiny found to be two becomes two rows.
- As the window's lines move, a session renews the columns from the window as it is then, and an area the window names moves from discovering to possibling to observing.
- The log begins imperfect, and its resolving goes on, doing no harm, as helpers, readers and explorers join.
"""

# Band introductions from the aims page.
intros, band = {}, None
for l in open(bands_md, encoding='utf-8').read().split('\n'):
    m = re.match(r'^## (.+)', l)
    if m:
        band = m.group(1).strip(); continue
    if band and l.strip() and not l.startswith('- ') and band not in intros:
        intros[band] = l.strip()

rows = list(csv.DictReader(open(log_csv, encoding='utf-8')))
bands = list(dict.fromkeys(r['band'] for r in rows))

def esc(t):
    return t.replace('|', '\\|')

S2 = ['## 2 The log', '', 'All the destinies the living file set reaches, in ten bands from one origin to the living expedition itself.', '']
for i, b in enumerate(bands, 1):
    S2 += [f'### 2.{i} {b}', '', intros[b], '',
           '| Destiny | Areas on its path | Home | Observing, 7 and 15 | Possibling, 2 and 14 | Discovering, 13 and 9 |',
           '| --- | --- | --- | --- | --- | --- |']
    for r in rows:
        if r['band'] != b:
            continue
        d = f"**{r['destiny']}.**" + (f" {r['its sentence']}" if r['its sentence'] else '')
        S2.append('| ' + ' | '.join(esc(x) for x in [d, r['areas on its path'], r['home'] or '—',
                                                     r['observing, 7 and 15'], r['possibling, 2 and 14'],
                                                     r['discovering, 13 and 9']]) + ' |')
    S2.append('')

spine = open(spine_md, encoding='utf-8').read().rstrip('\n')
out = head + [fill(OPENING)] + contents + [fill(S1_HEAD), spine, '', fill(S1_TAIL)] + S2 + s3to6 + [fill(S7), S8]
text = '\n'.join(out)
text = re.sub(r'\n{3,}', '\n\n', text).rstrip('\n') + '\n'
text = re.sub(r'(?<!\*)Geodesic Improving Method(?!\*)', '*Geodesic Improving Method*', text)
sys.stdout.write(text)
