"""Exhibit ONE's best version waiting, its explaining to Natural Intelligence's gathering-value, the found droplets to Natural Resolver's. Run at repo root."""
import re, os, shutil
SP = os.path.dirname(os.path.abspath(__file__))
WAIT = ' Both partners agreeing, it enters the living file at its own motion.'

# 1. the best version, waiting, in the kit
d = 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/waiting'
os.makedirs(d, exist_ok=True)
shutil.copy(os.path.join(SP, 'exhibit_one_best.md'), os.path.join(d, 'Exhibit_ONE_Natural_Resolver_best_version.md'))

# 2. explaining leaving Exhibit ONE, to Natural Intelligence's gathering-value
ex = open(os.path.join(SP, 'exhibit_one_explaining_out.md'), encoding='utf-8').read()
partA = ex.split('## Part B')[0]
units = re.findall(r'^- `(\d+)\.\d+` · (E|L\+E) · (.+)$', partA, re.M)
assert len(units) == 62, len(units)
lines = ["- Explaining at Exhibit ONE, leaving it for its reference (the person: Exhibit ONE is a reference tool, and its explaining is Natural Intelligence's value around it), each sentence below as Exhibit ONE v391 says it, at its line, waiting for Natural Intelligence's sections around Exhibit ONE. *(an explaining)*"]
for n, c, t in units:
    lines.append('- %s *(an explaining, from Exhibit ONE v391, line %s)*' % (t.strip(), n))
g = 'gathering-value/Natural_Intelligence.md'
s = open(g, encoding='utf-8').read().rstrip('\n')
open(g, 'w', encoding='utf-8').write(s + '\n' + '\n'.join(lines) + '\n')

# 3. Natural Resolver's gathering-value: the waiting best version, the concerns, the found droplets
r = 'gathering-value/Natural_Resolver.md'
R = open(r, encoding='utf-8').read().split('\n')
i = R.index('## Head, the whole file'); j = i + 1
while not R[j].startswith('## '): j += 1
k = j
while R[k - 1].strip() == '': k -= 1
R[k:k] = [
 "- **Waiting to enter** · Exhibit ONE's best version as a reference tool (v395, 5 November 2026), at `kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/waiting/Exhibit_ONE_Natural_Resolver_best_version.md`: the code and the drawing whole; the seventeen names and code with each name; where each is-or-is-not stands, sharing between selves, two-sided, same-existing through one moment; four four-cyclings, one move, four bi-foldings, twelve cycles, three scales, eight 1 to 17s inward, fives, four moments of exchanging; then one self and selves executing, two selves to a torus; each table whole, each with only the labels its reading needs, and *moment* for *momentary*. Its prose is 1,271 words of the 6,094 of v391's; its explaining waits at Natural Intelligence's gathering-value, and its sections each saying again what a table or a section says leave: Co as a gloss, each name and its relations (17 field lists), odd names, namings among names, two moves, + and − alike, one cell, eight even names, eights, across names. Read against Natural Intelligence's opening, 55 sentences, the highest reference for each all or none (the person)." + WAIT,
 "- **Possible incohering** · *Four-cycling is existing or discovering, possibling, observing and same-existing.* The opening's \"**Stable-forming** is observing, possibling, discovering and same-existing together.\" says discovering where Exhibit ONE's first and second four-cyclings open with existing, 1-now-existing and 5-now-co-existing, and its third and fourth with discovering, 9 and 13: one of the two is to be said as the other, waiting for the person. — at \"Four-cycling is observing prior-existing, possibling now-existing, discovering next-existing and same-existing.\"",
 "- **Possible incohering** · The *Dimension* column of *Where each is-or-is-not stands* and the *Fives* name five dimensions: social-parity now-existing, other-parity now-existing, self-parity now-existing, self-discovery next-existing and social-parity next-existing; the opening's *other-parity* is a me-parity the same as an other's, and *social-parity* and *self-discovery* are at no sentence of it: the column's naming waits for the person. — at \"Each is-or-is-not with the code, the name it stands on and its dimension.\"",
 "- **Possible incohering** · The drawing's *6 ══► 2, 10 ══► 14, 9 ══► 17* parts from the code: in 17-next-existing, 6, 10 and 9 each go into the receiving self's 14-next-possibling list, its next 2-now-possibling, and `_6_now_co_possibling = _10_next_co_possibling` (Natural Naming's gathering-value; the kit's Living Improving Value; v391's plan, *One route*). The drawing drawn as the code is, waiting for the person. — at \"**A drawing.** One self, its own resolving within.\"",
 "- **Possible incohering** · Three of the code's names each name two things: `_4`, `_13` and `_15` are one thing within 1-now-existing and another within 9-next-co-discovering and 17-next-existing (the archive's carryings; v391's verdict table), and `_14_next_possibling` is a self's surfacing within 1 and others' lists gathering within 17: one name, two kinds, waiting for the person. — at \"Of the seventeen names, three, 1, 9 and 17, are the code's functions, and fourteen are those functions' variables.\"",
]
src = open(os.path.join(SP, 'exhibit_one_sources.md'), encoding='utf-8').read()
part = src[src.index('## 2. kits/**'):src.index('## 5. ')]
found = []
cur = ''
for line in part.split('\n'):
    m = re.match(r'^#{2,3} (.*)$', line)
    if m: cur = m.group(1).strip(); continue
    m = re.match(r'^\d+\. (.+?) · (REFERENCE|EXPLAINING|INCOHERING|EXPLORING) · (.+)$', line)
    if m:
        where, kind, text = m.groups()
        kind = {'REFERENCE': 'a reference', 'EXPLAINING': 'an explaining', 'INCOHERING': 'a possible incohering', 'EXPLORING': 'a possible exploring'}[kind]
        found.append('- %s, at %s *(%s; found at %s)*' % (text.strip(), where.strip().replace('**', '*'), kind, re.sub(r'\s*\(\d+\)\s*$', '', cur)))
R = '\n'.join(R).rstrip('\n') + '\n' + "- Gathered for Exhibit ONE's best version (v395, 5 November 2026) from the kit, the archive branch and five earlier pull requests, each with where it meets Exhibit ONE; 92 more meet it at other partner gathering-values, each gathered there. *(an explaining)*\n" + '\n'.join(found) + '\n'
open(r, 'w', encoding='utf-8').write(R)
print('explaining to NI:', len(units), ' found to Natural Resolver:', len(found))
