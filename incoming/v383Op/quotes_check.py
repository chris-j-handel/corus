"""Session v383Op: each sentence this report quotes from the repository, found at its file.

Runs from the repository root: python3 incoming/v383Op/quotes_check.py
In the report's parts a span in italics of three words or more is a quotation from a file of the
repository, and italics are used for nothing else. This script takes each such span from each
.md file beside it and looks for it, letter for letter, in the living files at the root, the
README, the carryings, the other folders of incoming/, the kits and the archive. Bold and italic marks are set aside on
both sides, runs of spaces are one space, and curled quotation marks are read as straight ones.
For each span it says the file it is at and the heading it stands under, or says it is not found.

The entries this session laid at the carryings, each paragraph of carry/*.md saying "at v383Op",
are checked the same way, and are set aside from the files searched, so that no entry is found
at itself.
"""
import glob, os, re, sys

here = os.path.dirname(os.path.abspath(__file__))


def plain(text):
    text = text.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    text = text.replace('*', '')
    return re.sub(r'\s+', ' ', text)


corpus = []
laid = []
OURS = 'at v383Op'
for path in (sorted(glob.glob('Natural_Intelligence_v*.md')) + sorted(glob.glob('Exhibit_*.md'))
             + sorted(glob.glob('Natural_Intelligence_Corus_v*.md')) + ['README.md']
             + sorted(glob.glob('carry/*.md')) + sorted(glob.glob('incoming/**/*.md', recursive=True))
             + sorted(glob.glob('kits/**/*.md', recursive=True)) + sorted(glob.glob('archive/**/*.md', recursive=True))):
    if os.path.abspath(path).startswith(here):
        continue
    lines = open(path, encoding='utf-8').read().split('\n')
    if path.startswith('carry/'):
        laid.extend((path, line) for line in lines if OURS in line)
        lines = [line for line in lines if OURS not in line]
    corpus.append((path, lines, plain('\n'.join(lines))))


def heading_of(lines, needle):
    """The nearest heading above the line the span is at (spans stand within one line)."""
    head = ''
    for line in lines:
        if line.startswith('#'):
            head = line.lstrip('# ').strip()
        if needle in plain(line):
            return head
    return head


span = re.compile(r'(?<![*\w])\*(?![*\s])([^*\n]+?)(?<![\s*])\*(?!\*)')
found = missing = 0
parts = [(os.path.basename(part), open(part, encoding='utf-8').read())
         for part in sorted(glob.glob(os.path.join(here, '*.md')))]
for path in sorted(set(path for path, line in laid)):
    parts.append((path + ', the entries at v383Op', '\n'.join(line for p, line in laid if p == path)))
for name, text in parts:
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', '', text)
    text = text.replace('**', '')
    print('\n' + name)
    seen = set()
    for m in span.finditer(text):
        quote = plain(m.group(1)).strip()
        if len(quote.split()) < 3 or quote in seen:
            continue
        seen.add(quote)
        for path, lines, body in corpus:
            if quote in body:
                found += 1
                print('  found   %-52s | %s | %s' % (path[:52], heading_of(lines, quote)[:60], quote[:70]))
                break
        else:
            missing += 1
            print('  MISSING %s' % quote)
print('\nquoted spans found: %d; not found: %d' % (found, missing))
sys.exit(1 if missing else 0)
