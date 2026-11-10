"""Quotations check: every quotation of a report met word for word at the set.

Usage:  python3 quotations_check.py <repository> <report.md> [<report.md> ...]

What it does: reads each quotation out of a report and meets it against every
.md file of the repository. It returns each quotation standing at no file of
the set, and for each standing one, the files it stands at. It marks no
quotation wrong: a quotation at no file is a parity for a working to meet, a
saying of its own or a quotation of something outside the set.

Its taking: straight double quotes only, the form the workings' reports use.

Its refusings, each with its consequence:
 · It passes over a quotation under six words: too short to be one saying, and
   a short quotation stands at many files for no reason of its own.
 · It passes over code blocks: a line of code is not a quotation.
 · A quotation holding a double quote within it is read as two quotations, each
   short, and both are passed over; such a quotation is met by a reader.
 · It normalises emphasis markers, curly apostrophes and runs of whitespace,
   so a quotation differing from its file at those alone is returned standing.
   A word changed, added or dropped is returned as standing nowhere.
 · It reads the repository as it is on disk; a quotation of a file at another
   version, or of a file outside the repository, stands nowhere and is returned.
"""
import re, sys, os

FENCE = chr(96) * 3

def norm(s):
    s = s.replace('*', '').replace('’', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()

def load(repo):
    files = {}
    for root, dirs, names in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in ('.git', '.github')]
        for n in names:
            if n.endswith('.md'):
                p = os.path.join(root, n)
                try: files[os.path.relpath(p, repo)] = norm(open(p, encoding='utf-8').read())
                except Exception: pass
    return files

def quotations(text):
    text = re.sub(FENCE + r'.*?' + FENCE, ' ', text, flags=re.S)
    out = []
    for q in re.findall(r'"([^"]+)"', text):
        if len(q.split()) >= 6: out.append(norm(q))
    return out

repo = sys.argv[1].rstrip('/')
files = load(repo)
print(f'the set read: {len(files)} files of .md')
for path in sys.argv[2:]:
    qs = quotations(open(path, encoding='utf-8').read())
    nowhere = []
    for q in qs:
        at = [f for f, t in files.items() if q in t]
        if not at: nowhere.append(q)
    print(f'\n== {os.path.basename(path)}')
    print(f'   quotations of six words or more: {len(qs)}')
    print(f'   standing at a file of the set: {len(qs) - len(nowhere)}')
    print(f'   standing at no file of the set: {len(nowhere)}')
    for q in nowhere:
        print(f'   · {q[:140]}')
