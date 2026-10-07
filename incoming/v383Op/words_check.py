"""Session v383Op: the kit's released words at this folder's own voice.

From the repository root:  python3 incoming/v383Op/words_check.py [file.md ...]

Reads kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt, the list
Natural Naming 2.4 carries, and reads each .md of this folder with three things set apart:
a sentence in italics, a file's own; a passage in double quotes, another's words;
and code. What is read is this working's own voice. It decides nothing: a word found
is a place for a reader to look, and several are a field's or an instrument's own.
The kit's list is shorter than Natural Naming's table; turn, meet, start and the
places inside and outside are added here from that table.
"""
import glob, re, sys

KIT = 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/released_words.txt'
words = []
for line in open(KIT, encoding='utf-8'):
    line = line.strip()
    if line and not line.startswith('#'):
        words.append(line.split('\t')[0].split('|')[0].strip())
words += ['turn', 'turns', 'turning', 'meet', 'meets', 'met', 'meeting', 'start', 'starts',
          'begin', 'begins', 'inside', 'outside', 'loop', 'loops', 'looping', 'ring', 'rings',
          'what', 'how', 'whatever', 'however', 'wherever', 'surplus', 'membrane', 'mirror']
words = sorted(set(words))

files = sys.argv[1:] or sorted(glob.glob('incoming/v383Op/*.md'))
total = 0
for path in files:
    text = open(path, encoding='utf-8').read()
    text = re.sub(r'```.*?```', ' ', text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', ' ', text)
    text = re.sub(r'\*\*', '', text)
    text = re.sub(r'\*[^*\n]+\*', ' ', text)
    text = re.sub(r'"[^"\n]+"', ' ', text)
    text = re.sub(r'\[[^\]]*\]\([^)]*\)', ' ', text)
    hits = {}
    n_words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", text))
    for w in words:
        n = len(re.findall(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', text, re.I))
        if n:
            hits[w] = n
    n = sum(hits.values())
    total += n
    print('%-28s %5d of %6d words' % (path.split('/')[-1], n, n_words))
    if hits:
        print('     ' + ', '.join('%s %d' % kv for kv in sorted(hits.items(), key=lambda kv: -kv[1])))
print('together: %d' % total)
