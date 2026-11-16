"""Each saying of one of the ten unchangeables, in each living file and each gathering file, by its word form:
fixing, as Exhibit TWENTY-TWO Resolving the Hard Problem Registry's sentence of the ten has each, or fixed, as
Exhibit TWENTY Natural Naming's own section of the ten has each. All or none at all, by each saying.
Reads each living file and each gathering file; executes; writes no file; decides nothing.

Use: python3 -I incoming/v403cohering/instruments/the_ten_names_by_their_word_form.py <root>         each file with a saying of the second form, and each check
     python3 -I incoming/v403cohering/instruments/the_ten_names_by_their_word_form.py <root> long    each such saying with its line too

What it reads. A saying: a or an, one word, then fixing or fixed, then one of the ten endings, as from behind
and as a place. The ten endings are read out of the registry's own sentence of the ten, the one opening with
*Ten in sequence, each a part*, and it halts with that sentence not found or not of ten. A saying in italics or in a quotation is read all the same.

Returned at main, 16 November 2026, after Merge #819:
  living files: 310 sayings with fixing and 34 with fixed, the 34 in Exhibit TWENTY Natural Naming, 18, and in
  Exhibit ELEVEN Natural Medicine, 16.
  gathering files: 9 with fixed, in four files; two of the 9 are the Living Ghost Registry's gathering file's
  mentions of Natural Naming's own words. Each saying with fixing is in the answer alone: a gathering file has
  more with each droplet.
  Exhibit TWENTY Natural Naming's section of the ten has each of the ten with fixed, and the registry's sentence
  has each of the ten with fixing. Each entry's two names, eight apart, are the two the registry's sentence has
  it with, and each entry's binary of four is its now name's by that sentence.
  One entry's first words are not the registry's: a coming, with the registry's an observing.
"""
import glob, os, re, sys

R = sys.argv[1]; LONG = len(sys.argv) > 2
def ver(p):
    m = re.search(r'_v(\d+)', p); return int(m.group(1)) if m else 0
def newest(stem):
    return max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver)
hard = open(newest('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry'), encoding='utf-8').read()
ten_line = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
TEN = re.findall(r'(an? [a-z-]+) fixing ([a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', ten_line)
assert len(TEN) == 10 and len({t for _, t, _, _ in TEN}) == 10, "the registry's sentence is not of ten, each with its own ending"
ENDS = sorted({t for _, t, _, _ in TEN}, key=len, reverse=True)
SAYING = re.compile(r'\b(an? [a-z-]+) (fixing|fixed) (' + '|'.join(map(re.escape, ENDS)) + r')\b')
# the sentence's four binaries, each with two names of a self's span: now with 1 and 2, and on
BINARY = {int(n): b for b, x, y in re.findall(r'(now|existing|same|all) with (\d) and (\d)', ten_line) for n in (x, y)}
assert sorted(BINARY) == list(range(1, 9)), 'the four binaries are not with 1 to 8, two names each'

def read(paths):
    """each file's sayings by form, and each saying with fixed with its line"""
    by, second = {}, []
    for p in paths:
        name = os.path.basename(p)[:-3]
        for k, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
            for m in SAYING.finditer(l):
                by.setdefault(name, {'fixing': 0, 'fixed': 0})[m.group(2)] += 1
                if m.group(2) == 'fixed': second.append((name, k, m.group(0)))
    return by, second

living = {}
for p in glob.glob(os.path.join(R, '*_v*.md')):
    stem = re.sub(r'_v\d+[A-Za-z]*\.md$', '', os.path.basename(p))
    if stem not in living or ver(p) > ver(living[stem]): living[stem] = p
for label, paths in (('living files', sorted(living.values())), ('gathering files', sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md'))))):
    by, second = read(paths)
    print(f"{label}, {len(paths)}: {sum(c['fixing'] for c in by.values())} sayings with fixing, {sum(c['fixed'] for c in by.values())} with fixed")
    for name, c in sorted(by.items()):
        if c['fixed']: print(f"    {name}: fixing {c['fixing']}, fixed {c['fixed']}")
    if LONG:
        for name, k, s in second: print(f'      {name}, line {k}: {s}')

# The names' own section and the registry's sentence, each of the ten
naming = open(newest('Exhibit_TWENTY_Natural_Naming'), encoding='utf-8').read().split('\n')
s = next(i for i, l in enumerate(naming) if l.startswith('## 4.9 '))
e = next(i for i in range(s + 1, len(naming)) if naming[i].startswith('## '))
entries = []
for i in range(s, e):
    m = re.match(r'^- \*\*(an? [a-z-]+) (fixing|fixed) ([a-z ]+?)\*\*', naming[i])
    if m:
        b = re.search(r'\*b\* (\d+)-[a-z-]+ · (\d+)-[a-z-]+, (now|existing|same|all)\b', ' '.join(naming[i:i + 3]))
        entries.append((m.group(1), m.group(2), m.group(3)) + ((b.group(1), b.group(2), b.group(3)) if b else (None, None, None)))
print()
print(f"Exhibit TWENTY Natural Naming's section of the ten: {len(entries)} entries, with fixed {sum(1 for x in entries if x[1] == 'fixed')}, with fixing {sum(1 for x in entries if x[1] == 'fixing')}")
by_end = {t: (h, a, b) for h, t, a, b in TEN}
checks = [
    ("the section has ten entries, each ending one of the registry's ten, each once",
     len(entries) == 10 and sorted(x[2] for x in entries) == sorted(by_end)),
    ("each entry's two names, eight apart, are the two the registry's sentence has it with",
     all(x[2] in by_end and (x[3], x[4]) == by_end[x[2]][1:] for x in entries)),
    ("each entry's binary of four is its now name's, by the registry's own sentence",
     all(x[3] is not None and BINARY.get(int(x[3])) == x[5] for x in entries)),
]
for what, ok in checks: print(('  is · ' if ok else '  is-not · ') + what)
other = [(f'{x[0]} {x[1]} {x[2]}', f'{by_end[x[2]][0]} fixing {x[2]}') for x in entries if x[2] in by_end and x[0] != by_end[x[2]][0]]
print(f"  entries with first words not the registry's: {len(other)}")
for a, b in other: print(f'      the section: {a} · the registry: {b}')
print('each check is' if all(ok for _, ok in checks) else 'a check is-not')
