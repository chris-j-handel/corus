"""Session v383Op: does a sentence of Natural Medicine or Natural Health tell a reader what to do?

Runs from the repository root: python3 incoming/v383Op/advising_scan.py
The binary examined is the session's own, gathered at Natural Health's offerings: none of the
sentences should read as guidance. A sentence says what a reader is to do, or it does not.

A scan is no reading. It counts the forms a telling takes in English and prints each sentence
found, so that a reader takes each at is or is not:
  - the second person, you and your;
  - a word of recommending or avoiding;
  - must, should, ought, need to;
  - a sentence opening at a bare verb followed by "and", the form "Strip X and Y dissolves".
"Read at the form, ..." opens many sentences of Natural Medicine and is a participle, the
reading said and no one told to read; those are counted apart and not printed.
"""
import glob, re

FILES = sorted(glob.glob('Exhibit_ELEVEN_Natural_Medicine_v*.md'))[-1:] + sorted(glob.glob('Exhibit_TEN_Natural_Health_v*.md'))[-1:]
SECOND = re.compile(r"\b(you|your|yours|yourself)\b", re.I)
URGING = re.compile(r"\b(recommend\w*|avoid\w*|advis\w*|advice|ought|need to|needs to|better to|best to)\b", re.I)
MODAL = re.compile(r"\b(must|should)\b", re.I)
VERBS = 'Strip|Take|Eat|Stop|Use|Avoid|Keep|Give|Treat|Restore|Never|Always|Let|Leave|Hold|Remove|Add|Feed|Rest|Wait|Do not'
BARE = re.compile(r"^\W*(%s)\b[^.]* and [^.]*" % VERBS)
PARTICIPLE = re.compile(r"^\W*Read (at|on|from|across|each|together)\b")

for path in FILES:
    text = open(path, encoding='utf-8').read()
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    found = {'second person': [], 'recommending or avoiding': [], 'must or should': [], 'a bare verb and its outcome': []}
    participles = 0
    for s in sentences:
        bare = s.replace('*', '')
        if SECOND.search(bare):
            found['second person'].append(bare)
        if URGING.search(bare):
            found['recommending or avoiding'].append(bare)
        if MODAL.search(bare):
            found['must or should'].append(bare)
        if PARTICIPLE.search(bare):
            participles += 1
        elif BARE.search(bare):
            found['a bare verb and its outcome'].append(bare)
    print('\n%s: %d sentences' % (path, len(sentences)))
    for kind, hits in found.items():
        print('  %-28s %d' % (kind, len(hits)))
        for h in hits:
            print('      ' + h[:230])
    print('  %-28s %d, not printed' % ('"Read at ...", a participle', participles))
