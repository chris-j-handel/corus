"""Each living sentence having a word, or each of two words or more, with its living file and the heading it is
under: a reading for a session considering a sentence by the living sentences. All or none at all, by each sentence
of each living file.
Reads each living file at the root; executes; writes no file; decides nothing.

Use: python3 -I incoming/v403cohering/instruments/each_living_sentence_with_a_word.py <root> <a word's opening letters> [<an other's> …]
     as: … <root> horizon          each living sentence with horizon or horizons
         … <root> fractur          each with fracture, fractured or fracturing
         … <root> gas molecule     each with gas, gases or gaseous and with molecule or molecules, the two in one sentence
         … <root> 'star$' living   each with star whole, and no start, and with living
     with *files* as the last word, the number by living file alone

What it reads. A sentence: a living file's line divided after a full stop, a question mark or the opening's own
line mark, four words or more, code not read. A word: its opening letters at a word's own opening, large or
small; with $ after it, the word whole. A sentence with none is said as none: no living sentence has it.

Returned at main, 16 November 2026, each for a thing the session v403bubble's pages say is not read:
  horizon: 101 living sentences in twelve living files, Exhibit TWENTY-ONE Hard Problem Registry 32, Natural
  Intelligence Corus 26, Exhibit EIGHTEEN Natural Physics 14 and Exhibit EIGHT Natural Exploring 10 among them;
  none in Natural Intelligence, Exhibit ONE Natural Resolver, Exhibit TWENTY Natural Naming or Exhibit THIRTY
  Co-Chaining Logic Registry.
  gas with molecule: 1, of a field's box of gas.   fractur: 2, neither of a stable form.
  film$: 1, of a field's film, and none of a bubble's.   star$ with living: none.
  bubbl: 9 in six living files, each of a field's market, a thought, or a double-double bubble-bubble; none of
  a bubble with its between.
"""
import glob, os, re, sys

R = sys.argv[1]; words = [w for w in sys.argv[2:] if w != 'files']; FILES = sys.argv[-1] == 'files'
assert words, 'a word after the root'
def ver(p):
    m = re.search(r'_v(\d+)', p); return int(m.group(1)) if m else 0
living = {}
for p in glob.glob(os.path.join(R, '*_v*.md')):
    stem = re.sub(r'_v\d+[A-Za-z]*\.md$', '', os.path.basename(p))
    if stem not in living or ver(p) > ver(living[stem]): living[stem] = p
pats = [re.compile(r'(?<![\w-])' + re.escape(w.rstrip('$')) + (r'(?![\w-])' if w.endswith('$') else ''), re.I) for w in words]
total, by = 0, []
for stem in sorted(living):
    head, fence, hits = 'its opening', False, []
    for l in open(living[stem], encoding='utf-8').read().split('\n'):
        if l.startswith('```'): fence = not fence; continue
        if fence: continue
        if l.startswith('#'): head = l.lstrip('# ').strip(); continue
        for s in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9*"“(])|\s*\\\s*$', l):
            if len(s.split()) >= 4 and all(p.search(s) for p in pats): hits.append((head, s.strip()))
    if hits: by.append((stem.replace('_', ' '), hits)); total += len(hits)
words = [w.rstrip('$') for w in words]
print(f"{' with '.join(words)}: {total} living sentences in {len(by)} living files" if total else f"{' with '.join(words)}: none, no living sentence has it")
for name, hits in by:
    print(f'  {name}: {len(hits)}')
    if not FILES:
        for head, s in hits: print(f'      {head[:60]} · {s}')
