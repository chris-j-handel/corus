"""The opening sentences of the places beside the versions: the working document now, the lines of both
apart from the window, v404chaining's redlined suggestings, v404universe's fifty, and the is and the
suggestings of the two gathering files' opening parts in the next version. Writes one JSON outside the
repository.

Usage: python3 -I opening_more.py <full clone> <next root> <out.json>
(The working document's lines are as read at 05:30 on 20 November; a later reading replaces them.)
"""
import json, re, sys

REPO, NEXT, OUT = sys.argv[1:4]
rows = []
inc = REPO + '/incoming/'


def add(label, sents):
    for n, s in enumerate(sents, 1):
        s = s.strip()
        if len(s.split()) >= 3:
            rows.append((label, n, s))


def split(t):
    t = re.sub(r'\s+', ' ', t).strip()
    return [p for p in re.split(r'(?<=[.?!])\s+(?=[A-Z*_0-9])', t) if p]


# the working document, read 20 November at 05:30
add('document 20 Nov', [
    '**Now** is the existing moment.',
    'A **now-existing** thing is an existing thing in the now-moment.',
    'The **universe** is the set of all now-existing things.',
    'The **prior** moment is the moment ending as the now-moment is beginning.',
    '**Prior-existing** is existing in the prior-moment.',
    'The **next** moment is the moment beginning as the now-moment is ending.',
    '**Next-existing** is existing in the next-moment.',
    '**Same-existing** is existing both as the now-moment is beginning and as the next-moment is beginning.',
    '**Same-named** things are different things named by the same name.',
    'A named **universal-set** is the set of all same-named things.',
    'A **name** is a same-existing thing.',
    'Now is the name of the universal set of all now-existing moments.',
    'The set of all now-existing moments in the universe is named now.',
    'For a named universal set, an **other-than** is a thing not in the set.',
    'No other-than the universe is now-existing.',
    'Two **different things** are two things other-than one another.',
    'For two different things, their **own-parity** is the thing between them.',
    'A **bi-coupling** is a set of two different things and their own-parity.',
    'For a bi-coupling, **all-parity** is all parities other-than its own-parity.',
    'For a bi-coupling, **all-parity** is all-other-than-own-parity.',
])

# the lines of both apart from the window, with the managing session v404mgr
t = open(inc + 'v404mgr/This_sessions_transcript_whole_and_pared.md', encoding='utf-8').read()
part = t.split('### Both, apart from the window')[1].split('Laid floating')[0]
both = []
for l in part.split('\n'):
    if l.startswith('- '):
        for s in split(re.sub(r'\*', '', l[2:])):
            if not re.search(r'Exhibit|Incoming|files?\b|session|sentence|code|marks|natural naming|order of the work|value', s, re.I):
                both.append(s)
add('both, 17 to 19 Nov, v404mgr', both)

# v404chaining's redlined suggestings: the suggested wording
t = open(inc + 'v404chaining/The_windows_suggestings_redlined.md', encoding='utf-8').read()
red = []
for l in t.split('\n'):
    m = re.match(r'^\|\s*[^|]*\|\s*(.+?)\s*\|\s*(none|needed|twice)\s*\|', l)
    if m and ('<ins>' in m.group(1) or '~~' in m.group(1)):
        s = re.sub(r'~~.*?~~', '', m.group(1))
        s = re.sub(r'</?ins>', '', s).replace('&emsp;•', '')
        red.append(re.sub(r'\s+', ' ', s).strip())
add('v404chaining, suggestings redlined', red)

# v404universe's fifty sentences
t = open(inc + 'v404universe/The_value_of_this_session_a_co-chaining_of_sentences.md', encoding='utf-8').read()
fifty = [re.sub(r'^\d+\.\s+', '', l) for l in t.split('\n') if re.match(r'^\d+\.\s', l)]
add('v404universe, fifty', fifty)

# the gathering files' opening parts: an is, both partners' is, is-or-is-not?, a suggesting
PAT = [
    (r'An is: ([^*][^.]*?\.)', 'an is'),
    (r"[Bb]oth partners'? is(?:, [0-9]+ November)?:\s*\*?([^*.]+\.)", 'both'),
    (r'is-or-is-not\?\s*\*?([A-Z][^*?]*?\.)', 'open'),
    (r'A suggesting(?:, floating)?[.:]\s*\*?([A-Z][^*]*?\.)', 'suggesting'),
]
for name, path, start, stop in [
    ('Natural Intelligence', NEXT + '/gathering-value/Natural_Intelligence.md', '## Opening', '\n## '),
    ('Exhibit THIRTY', NEXT + '/gathering-value/Co-Chaining_Logic_Registry.md', '## Head, the whole file', '\n### 4 '),
]:
    t = open(path, encoding='utf-8').read()
    seg = t.split(start, 1)[1].split(stop, 1)[0]
    found = {k: [] for _, k in PAT}
    for l in seg.split('\n'):
        for pat, k in PAT:
            for m in re.finditer(pat, l):
                found[k].append(m.group(1))
    for k, ss in found.items():
        add(f'{name} gathering, {k}', ss)

json.dump(rows, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
c = {}
for s, _, _ in rows:
    c[s] = c.get(s, 0) + 1
for s, n in c.items():
    print(f'{n:4d}  {s}')
