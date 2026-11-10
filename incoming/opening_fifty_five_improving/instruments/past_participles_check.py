"""Past-participles check: a file's own sentences against the set's practice.

Usage:  python3 past_participles_check.py <repository> <file.md> [<file.md> ...]
        python3 past_participles_check.py <repository> --fifty-five

What it does: the Living File Registry records of Natural Intelligence "its
past participles said living at 265 sayings, each by its meaning, four fresh
readers proposing and each pair checked, a self the doer of each observing and
sharing", and of Exhibit ONE that *inverted*, *surfaced*, *kept* and *moved* are
"said living, -ing". This returns each past participle standing as such in a
file's own sentences, for that practice to be met at each.

With --fifty-five it reads the opening of 55 sentences waiting at Natural
Intelligence's gathering-value, in place of a file.

Its refusings, each with its consequence:
 · It holds one list of participles, the ones the set's own records name and
   their near kin; a participle outside the list is passed over.
 · A participle within a quotation is returned too: a working meets whether
   the quotation is of a file said before that practice.
 · *said* and *named* stand in the set's own sentences as participles at many
   places; they are returned and met, not re-said by this instrument.
"""
import re, sys

WORDS = (r'observed|shared|received|gathered|given|taken|named|agreed|inverted|surfaced|'
         r'kept|moved|divided|defined|derived|placed|fixed|held|dissolved|released|'
         r'carried|executed|resolved|coupled|opened|closed')

repo = sys.argv[1].rstrip('/')
if sys.argv[2] == '--fifty-five':
    gv = open(repo + '/gathering-value/Natural_Intelligence.md', encoding='utf-8').read()
    line = [l for l in gv.split('\n')
            if l.startswith('- **Waiting to enter** · The opening, 55 sentences, no word staying')][0]
    sents = {int(n): re.sub(r'\*', '', t).strip() for n, t in
             re.findall(r'(\d+)\.\s(.*?)(?=\s\d+\.\s|\Z)', line.split('motion. ', 1)[1])}
    items = [('the fifty-five', sents)]
else:
    items = []
    for p in sys.argv[2:]:
        t = open(p, encoding='utf-8').read()
        items.append((p.split('/')[-1], {int(n): s for n, s in re.findall(r'^(\d+)\.\s(.+)$', t, re.M)}))

for label, sents in items:
    print(f'== {label}: {len(sents)} sentences')
    found = 0
    for n in sorted(sents):
        for w in sorted(set(re.findall(r'\b(' + WORDS + r')\b', sents[n].lower()))):
            found += 1
            print(f'   · {n}: "{w}"  ·  {sents[n][:95]}')
    print(f'   past participles standing as such: {found}')
