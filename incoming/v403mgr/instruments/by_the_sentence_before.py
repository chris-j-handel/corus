"""Each sentence of Natural Intelligence's living opening by the sentence it is after: the names the two have
together. Reads the living version and the opening rated by three, and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/by_the_sentence_before.py <root>

A name is a name the opening has in bold, with *now-existing*, *prior-existing* and *next-existing*, found by its
word forms. For each sentence after the first:
  1. the new name of the sentence it is after, with that name in it or with none of it
  2. each name the two sentences have together, or none
  3. with none: the nearest sentence it has a name with

Returned at main, Merge #701, 15 November 2026:
  69 sentences after the first. The sentence each is after has a new name in 43; of the 43, 26 have that new name.
  59 have a name together with the sentence each is after. 10 have none: 24, 29, 31, 44, 60, 61, 62, 64, 69 and 70,
  each with its nearest sentence having a name with it; 29, the sentence of a 0, has none.
  The living opening has *by* with one sentence's opening: By observing, after the sentence of observing.
"""
import contextlib, io, os, re, runpy, sys

R = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
sys.argv = [os.path.join(here, 'opening_base.py'), R]
with contextlib.redirect_stdout(io.StringIO()):
    base = runpy.run_path(os.path.join(here, 'opening_base.py'))
pats, sent, plain = dict(base['pats']), base['sent'], base['plain']
for w in ('now-existing', 'prior-existing', 'next-existing'):
    pats[w] = re.compile(r'(?<![\w-])' + w + r'(?![\w-])', re.I)
has = {n: {k for k, p in pats.items() if p.search(plain(sent[n]))} for n in sent}
new = {n: [b.lower() for b in re.findall(r'\*\*(.+?)\*\*', sent[n])] for n in sent}
with_new = 0; have_it = 0; together = 0; none = []
for n in range(2, 71):
    if new[n - 1]:
        with_new += 1
        if any(k in has[n] for k in new[n - 1]): have_it += 1
    if has[n] & has[n - 1]: together += 1
    else:
        near = next((m for m in range(n - 2, 0, -1) if has[n] & has[m]), None)
        none.append((n, near, sorted(has[n] & has[near]) if near else []))
print('sentences after the first:', 69)
print('the sentence each is after has a new name:', with_new, ' and of them, with that new name in it:', have_it)
print('with a name together with the sentence it is after:', together, ' with none:', len(none))
for n, near, ks in none:
    print(f'   {n}  {plain(sent[n])[:86]}')
    print(f'       its nearest sentence with a name of it: {near}, by {", ".join(ks)}')
print('with *by* at its opening:', [(n, plain(sent[n])) for n in sent if re.match(r'By ', plain(sent[n]))])
