"""Session v381F: the tour's parts, written from Natural Intelligence at the root as emanations of it.

Runs from the repository root: python3 incoming/v381F/tour_parts.py
Reads the newest Natural Intelligence at the root and writes, beside this script at tour/, one file per part
of the tour: the front with its contents; Parts ONE to THREE; Exhibit ONE inside it; Part FOUR; Parts FIVE and
SIX; and a page of five sentences a session meets first. Each part opens with one line saying what it is: an
emanation written from the living file, carrying nothing of its own, the living file at the root its prior.
Each is under 100 KB, so a page fetch receives it whole. build.js could write the same at each build.
A writing from the living file, changing nothing in it.
"""
import glob, os, re

ni = sorted(glob.glob('Natural_Intelligence_v*.md'))[-1]
version = open(ni, encoding='utf-8').readline().strip()
text = open(ni, encoding='utf-8').read()
out_dir = 'incoming/v381F/tour'
os.makedirs(out_dir, exist_ok=True)
line = ('*An emanation of %s, written from the living file at the root by `incoming/v381F/tour_parts.py`; '
        'it carries nothing of its own, and the living file is its prior and its newest. Part %s of the tour.*\n\n')

marks = ['# ONE · NATURAL', '# EXHIBIT ONE · NATURAL RESOLVER', '# FOUR · RESOLVING', '# FIVE · DISCOVERING NEXT']
idx = [text.index(m) for m in marks]
parts = [
    ('0_Front_and_Contents', text[:idx[0]]),
    ('1_ONE_TWO_THREE_the_method', text[idx[0]:idx[1]]),
    ('2_EXHIBIT_ONE_the_method_as_an_object', text[idx[1]:idx[2]]),
    ('3_FOUR_resolving', text[idx[2]:idx[3]]),
    ('4_FIVE_SIX_discovering_and_intelligence', text[idx[3]:]),
]
for i, (name, body) in enumerate(parts):
    with open(os.path.join(out_dir, name + '.md'), 'w', encoding='utf-8') as f:
        f.write(line % (version, i) + body)

# five sentences a session meets first, each quoted whole from the file with its section named
def section(number):
    m = re.search(r"\n## %s [^\n]*\n(.*?)(?=\n## |\n# |\Z)" % re.escape(number), text, re.S)
    return m.group(1).strip() if m else ''

first = [
    ('1.1 Universe, the changing set of all existing things', section('1.1').split('\n\n')[0]),
    ('1.4 No other possible method', section('1.4').split('\n\n')[0]),
    ('2.5 All or none at all, of no size', section('2.5').split('\n\n')[0]),
    ('5.4 Two methods parting at the now', section('5.4')),
    ('6.5 Non-living existing things included, its sentence of AI', [p for p in section('6.5').split('\n\n') if 'AI is existing' in p][0]),
]
with open(os.path.join(out_dir, 'Five_Sentences_First.md'), 'w', encoding='utf-8') as f:
    f.write('# Five passages of Natural Intelligence a session meets first\n\n')
    f.write(line % (version, 'first'))
    for title, body in first:
        f.write('## %s\n\n%s\n\n' % (title, body))

for name in sorted(os.listdir(out_dir)):
    print('%-48s %6.1f KB' % (name, os.path.getsize(os.path.join(out_dir, name)) / 1024))
