"""welcoming_audit_v368.py · after the contents and the opening sentence, each term's first use in the body
is at or after the sentence that welcomes it. Headings, the subtitle's own words and the names at their
numbers are set aside, since they name what comes and are not sentences of the sequence.
Run: python3 welcoming_audit_v368.py Natural_Intelligence_v368.md
"""
import re, sys
text = open((sys.argv[1:] or ['Natural_Intelligence_v368.md'])[0], encoding='utf-8').read()
body = text.split('\n---\n', 1)[1]
body = body.replace('**Our universe is all existing things.**', '', 1).replace('**Alternating is a stable-forming method.**', '', 1)   # the two origin statements are the opening, as the carry agreed
body = '\n'.join(l for l in body.splitlines() if not l.startswith('#'))          # headings set aside
body = re.sub(r'\d+-(self|other|social)-[a-z]+', 'NAME', body)                    # names at their numbers set aside
body = body.replace('coupling, offering, carrying, sharing, neutralling, crossing, corusing, torusing, releasing, surfacing, chaining, surplusing and abundancing', 'ROOTS')
WELCOME = [('changing', 'Existing things are changing'), ('binary', 'Existing is binary'), ('alternating', 'that changing is alternating'),
    ('stable-forming', 'is stable-forming'), ('parity', 'that binary is parity'), ('momentary', 'A momentary is an opening and its completing'), ('recursioning', 'recursioning existing and discovering both'),
    ('co-', 'Two together with their difference is co-'), ('co-sequential', 'overlapping each other co-sequentially'),
    ('self', 'is a self'), ('coupling', 'is a coupling'), ('society', 'are a society'), ('social', 'what runs among them is social'),
    ('origin', 'the number it opens at'), ('bi-', 'difference alone is bi-'), ('along', 'runs along'), ('across', 'runs across'),
    ('competency', 'Competency is co-unrelationing'), ('morality', 'Morality is bi-unrelationing'), ('resolving', 'run the resolving'),
    ('code', 'run the resolving as code'), ('sign', 'A sign is the binary'), ('key', 'its key NAME where signs meet'),
    ('membrane', 'is a membrane'), ('torus', 'is a torus'), 
    ('surface', 'A surface closing'), ('prime', 'A prime opens a clean axis across'), ('scale', 'A society is a self at the next scale'), ('emanat', 'is an emanation'), ('φ', 'about one number, φ'),
    ('floating neutralling', 'that is floating neutralling'), ('geodesic', 'that is geodesic changing'),
('discovering', 'arriving into it is discovering'), ('exclusivity', 'the universe as an existing thing, exclusivity'), ('reachability', 'reach each number on: reachability'), ('prior', 'prior, now and next'),
    ('unrelat', 'Competency is co-unrelationing'),
    ('half momentar', 'two and one half momentaries: a prior, a now'), ('co-bi-coupling', 'The between of two existing things co-bi-coupling'),
    ('social-co-bi-coupling', 'its social-co-bi-coupling opens'), ('network surface', 'to a natural network surface'),
    ('joint form', 'the same four joint forms'), ('eight half momentaries', 'two consecutive momentaries at each side, eight half momentaries')]
PATTERN = {'torus': r'\btorus\b', 'surface': r'\bsurface\b'}   # the noun, not the -ing of a name at work
early = 0
for term, welcome in WELCOME:
    w = body.find(welcome); m = re.search(PATTERN.get(term, re.escape(term)), body); f = m.start() if m else -1
    if w < 0: print('NO WELCOME', term); early += 1; continue
    if f < w - len(welcome):
        early += 1; print('EARLY', term, '…' + body[max(0, f - 50):f + 30].replace('\n', ' ') + '…')
print(f'{len(WELCOME) - early} of {len(WELCOME)} terms welcomed before their first use')
