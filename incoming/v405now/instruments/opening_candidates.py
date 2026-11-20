"""Every opening sentence the repository has drafted, from each version of Natural Intelligence and of
Exhibit THIRTY, the window's copies, and incoming drafts; each with its sources. Reads git; writes one
JSON file outside the repository.

Usage: python3 -I opening_candidates.py <full clone> <out.json>
"""
import json, re, subprocess, sys

REPO, OUT = sys.argv[1], sys.argv[2]


def git(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True, errors='replace').stdout


def last_text(path, ref='--all'):
    c = git('log', ref, '-1', '--format=%h', '--diff-filter=AM', '--', path).strip()
    return git('show', f'{c}:{path}') if c else ''


def vkey(name):
    m = re.search(r'_v(\d+)([A-Za-z]*)\.md$', name)
    return (int(m.group(1)), m.group(2)) if m else (0, '')


files = sorted({l for l in git('log', '--all', '--name-only', '--format=').split('\n') if l.strip()})
NI = sorted([f for f in files if re.fullmatch(r'Natural_Intelligence_v\d+[a-z]*\.md', f)], key=vkey)
TH = sorted([f for f in files if re.fullmatch(r'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v\d+[A-Za-z]*\.md', f)], key=vkey)
NI = [f for f in NI if vkey(f)[0] >= 380]
TH = [f for f in TH if vkey(f)[0] >= 380]

rows = []  # (source label, order in source, raw sentence)


def sentences(line):
    line = re.sub(r'\s*\\\s*$', '', line.strip())
    line = re.sub(r'^\d+\.\s+', '', line)
    line = re.sub(r'^[-*]\s+', '', line)
    parts = re.split(r'(?<=[.?!])\s+(?=[A-Z*_0-9])', line)
    return [p.strip() for p in parts if len(p.split()) >= 3 and re.search(r'[a-z]', p)]


def add(label, text_lines):
    n = 0
    for l in text_lines:
        for s in sentences(l):
            n += 1
            rows.append((label, n, s))


for f in NI:
    t = last_text(f)
    v = re.search(r'_v(.+)\.md', f).group(1)
    L = t.split('\n')
    # head: sentence lines before the contents
    head = []
    for l in L[1:]:
        if re.match(r'^\*\*(ONE|PART|TWO)\b|^- 1\.1|^# ONE|^---', l.strip()):
            break
        if l.strip().endswith('\\') or (l.strip() and not l.startswith(('#', '**', '&', '-')) and l.count('.') >= 1):
            head.append(l)
    if len(head) >= 3:
        add(f'NI v{v} head', head)
    # sections 1.1 to 1.4 of the body
    body, on = [], False
    for l in L:
        if re.match(r'^## 1\.1 ', l):
            on = True
            continue
        if on and re.match(r'^## 1\.[5-9] |^## 2\.|^# TWO', l):
            break
        if on and l.strip() and not l.startswith('#'):
            body.append(l)
    if body:
        add(f'NI v{v} §1.1–1.4', body)

for f in TH:
    t = last_text(f)
    v = re.search(r'_v(.+)\.md', f).group(1)
    steps = []
    for l in t.split('\n'):
        m = re.match(r'^(\d+)\. (.+)', l)
        if m and int(m.group(1)) <= 70:
            steps.append(m.group(2))
        if m and int(m.group(1)) > 70:
            break
    add(f'THIRTY v{v} steps 1–70', steps)

# the window's copies through history
W = 'incoming/v404mgr/The_window_of_the_opening.md'
for line in git('log', '--all', '--format=%h %ci', '--', W).strip().split('\n')[::-1]:
    h, d = line.split()[0], ' '.join(line.split()[1:3])[5:16]
    t = git('show', f'{h}:{W}')
    tab = [re.match(r'^\|\s*(.+?)\s*\|', l).group(1) for l in t.split('\n')
           if re.match(r'^\|\s*[^|-]', l) and 'Sentence' not in l and not l.startswith('|---')]
    tab = [x for x in tab if not x.startswith('---')]
    add(f'window copy {d}', [x for x in tab if len(x.split()) >= 3])

json.dump(rows, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
srcs = {}
for s, _, _ in rows:
    srcs[s] = srcs.get(s, 0) + 1
for s, n in srcs.items():
    print(f'{n:4d}  {s}')
print(len(rows), 'sentences')
