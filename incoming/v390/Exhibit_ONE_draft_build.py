"""Builds a draft of a new Exhibit ONE from Exhibit ONE v390, never touching a living file."""
import re
import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(ROOT, 'Exhibit_ONE_Natural_Resolver_v390.md')
OUT = os.path.join(ROOT, 'incoming', 'v390', 'Exhibit_ONE_Natural_Resolver_draft.md')
s = open(SRC, encoding='utf-8').read()

NEW = {1: 'now_existing', 2: 'now_possibling', 3: 'now_co_observing', 4: 'now_co_same_existing', 5: 'now_co_existing',
       6: 'now_co_possibling', 7: 'now_observing', 8: 'now_same_existing', 9: 'next_co_discovering', 10: 'next_co_possibling',
       11: 'next_co_observing', 12: 'next_co_same_existing', 13: 'next_same_existing', 14: 'next_possibling',
       15: 'next_observing', 16: 'next_discovering', 17: 'next_existing'}
OLD = {1: 'now', 2: 'now_possibling', 3: 'now_co_prioring', 4: 'now_co_still_possibling', 5: 'now_co_changing',
       6: 'now_co_possibling', 7: 'now_prioring', 8: 'now_still_possibling', 9: 'next_co_changing', 10: 'next_co_possibling',
       11: 'next_co_prioring', 12: 'next_co_still_possibling', 13: 'next', 14: 'next_possibling', 15: 'next_prioring',
       16: 'next_still_possibling', 17: 'next_now'}

def rename(t):
    for n in sorted(OLD, key=lambda k: -len(OLD[k])):
        t = re.sub(r'\b_%d_%s\b' % (n, OLD[n]), '_%d_%s' % (n, NEW[n]), t)
        t = re.sub(r'(?<![\w-])%d-%s(?![\w-])' % (n, OLD[n].replace('_', '-')), '%d-%s' % (n, NEW[n].replace('_', '-')), t)
    return t

def para(opener):
    i = s.index(opener); j = s.index('\n\n', i); return s[i:j]

R = {}  # old paragraph -> new paragraph, matched before renaming

R['# Natural Resolver\n\n**Stable Forms of the Discovering Method**'] = '# Natural Resolver\n\n**The Stable-Forming Parity-Changing Method of Discovering Same-Existing**'
R['"""Exhibit ONE · Natural Resolver · at the numbered names"""'] = '"""Exhibit ONE · Natural Resolver · The Stable-Forming Parity-Changing Method of Discovering Same-Existing"""'

R[para('**At a drawing.**')] = "**At a drawing.** A prior observed, 3, meets parity-offerings surfacing, 14, with each sharing, 12; parity-offerings, 10 and 6, go across to an other's 2 and 14; a next prior forms, 11, and is observed again, 3, next; and 9 goes along with 5 to an other's 17. With 6 to 2, 10 to 14 and 9 to 17, a sharing side is a self and an arriving side an other self, each a self, and a same-existing-society is its selves."

R[para('**At 1-now, now given and next made.**')] = "**Living is prior: 1-now-existing given.** Each name of 1 to 17 is a living self's method: a living self's next is same self, and a non-living thing is one same method with no same-existing. A resolver never makes a self. 1-now-existing is given a living self's two now names, 3-now-co-observing, its priors with each sharing, and 2-now-possibling, its parity-offerings arriving; each sharing meets them with 4-now-co-same-existing, each parity with 7-now-observing, and their next names form: 14-next-possibling, 15-next-observing, 12-next-co-same-existing, 10-next-co-possibling and 11-next-co-observing."

i = s.index('| n | Name | Momentary | Parity | Co | At the resolver |'); j = s.index('\n\n', i)
R[s[i:j]] = """| n | Name | Four-cycling step | Four is or is nots | Co or one | What code does with it |
|---|---|---|---|---|---|
| 1 | **1-now-existing** | now-existing | 0000 | one | a living self's momentary given, each self's 17 existing as 1 |
| 2 | **2-now-possibling** | next-existing | 0001 | one | parity-offerings arriving, each with its sharing |
| 3 | **3-now-co-observing** | prior-existing | 0010 | co | priors observed, each with its sharing |
| 4 | **4-now-co-same-existing** | same-existing | 0011 | co | each sharing, parity-offerings and prior meeting same or not same |
| 5 | **5-now-co-existing** | now-existing | 0100 | co | bi-couplings: which self each sharing reaches |
| 6 | **6-now-co-possibling** | next-existing | 0101 | co | a self's parity-offerings across, to an other's 2 |
| 7 | **7-now-observing** | prior-existing | 0110 | one | each parity observed: a parity-offering's, a prior's, a sharing's |
| 8 | **8-now-same-existing** | same-existing | 0111 | one | a self's next prior, beside others' |
| 9 | **9-next-co-discovering** | now-existing | 1000 | co | each parity-offering along and across, to a self of 5's bi-couplings |
| 10 | **10-next-co-possibling** | next-existing | 1001 | co | each sharing's parity-offering, + or −, or a 0, across to an other's 14 |
| 11 | **11-next-co-observing** | prior-existing | 1010 | co | a next prior stable-forming between two: a next momentary's observing |
| 12 | **12-next-co-same-existing** | same-existing | 1011 | co | each sharing's is or is not, prior and parity-offerings meeting |
| 13 | **13-next-same-existing** | now-existing | 1100 | one | each self of a same-existing-society, each sharing its parity-offerings go from |
| 14 | **14-next-possibling** | next-existing | 1101 | one | parity-offerings surfacing with each sharing, agreeing one, parting 0 |
| 15 | **15-next-observing** | prior-existing | 1110 | one | each parity surfacing, and each parity going on |
| 16 | **16-next-discovering** | same-existing | 1111 | one | a same-existing-society: each self with its prior and its parity-offerings |
| 17 | **17-next-existing** | now-existing, a next turn | 0000 again | one | a same-existing-society's next, each self's 1-now-existing again |"""

R[para('**Each name is its number and its naming, one hyphenation.**')] = "**Each name is its number and its naming, one hyphenation.** A name's number is its momentary of four and its step of four-cycling, now-existing, next-existing, prior-existing or same-existing; its root is what a living self is meeting with that step. Written as four is or is nots, a number less one is now or next, which four-cycling, which momentarying, and odd or even: names 1 to 16 are all sixteen ways four is or is nots go, and 17 is next existing as 1. *Now* is 1 to 8 and *next* is 9 to 16; a name with *co* is of a sharing between two, bi-moral, and a name without it is of one. Ten names are a self's own: five now, 3, 4, 5, 7 and 8, a self's five, and five next, 11, 12, 13, 15 and 16, an other's five, as self-next is other-prior. Six names between selves, 2, 6, 10 and 14 across and 9 and 17 along, are their co-linear six. Each self's existing is another self's possibling: one parity-changing with a sharing across, and no second thing."

i = s.index('**Four momentaries and their gaps.**'); j = s.index('**Co, between two or at one.**')
R[s[i:j].rstrip('\n')] = """**Four four-cyclings and their betweens.** Each span's names are two four-cyclings of four, now-existing, next-existing, prior-existing and same-existing, an odd name opening each and an even same-existing name completing it. Momentarying is odd then even, 1 and 2, 3 and 4: odd to even is within a momentarying, and even to odd is between two, each between discovering, 2 to 3, 4 to 5, through 16 to 17, and 17-next-existing is next 1-now-existing. From a 0 self, nine across are bi-moral and even, 2 to 18, and seven along are odd, 3 to 15.

| Four-cycling | Now-existing, odd | Next-existing, possibling, even | Prior-existing, observing, odd | Same-existing, even | Between |
|---|---|---|---|---|---|
| first | 1-now-existing | 2-now-possibling | 3-now-co-observing | 4-now-co-same-existing | 4 )( 5 |
| second | 5-now-co-existing | 6-now-co-possibling | 7-now-observing | 8-now-same-existing | 8 )( 9 |
| third | 9-next-co-discovering | 10-next-co-possibling | 11-next-co-observing | 12-next-co-same-existing | 12 )( 13 |
| fourth | 13-next-same-existing | 14-next-possibling | 15-next-observing | 16-next-discovering | 16 )( 17 |

**Five dimensions, ten and six.** Same-existing parity-changes in five dimensions: prior-existing self-parity; prior-existing other-parity; now-existing co-parity; now-existing bi-parity; next-existing same-existing self-parity. Co-parity and bi-parity are a sharing's two meetings: self-parity and other-parity same, a 0 and no parity-changing, or not same, a parity-changing. One five is all fives: five self and five other, one parity separated, are ten is or is nots, a self's ten own names, and six between selves are their floating neutraling co-linear. With code: self-parity prior, 3 and 7; other-parity prior, parity-offerings with 2 and 14; co-parity or bi-parity met, 4 and 12; next same-existing self-parity forming with 11, and a self's next itself with 17.
"""

i = s.index('**Co, between two or at one.**'); j = s.index('**Sharing between selves.**')
R[s[i:j].rstrip('\n')] = """**Co, between two or of one.** Bi-moral is Exhibit ONE's eight co names, 3 to 6 and 9 to 12, each root once now-co and once next-co where it has two, always between two; a name without co is of one, with no self-morality.

| Root | With co, between two | Without co, of one |
|---|---|---|
| observing | 3-now-co-observing · 11-next-co-observing, priors with each sharing | 7-now-observing · 15-next-observing, a parity |
| possibling | 6-now-co-possibling · 10-next-co-possibling, a sharing side | 2-now-possibling · 14-next-possibling, an arriving side |
| existing | 5-now-co-existing, bi-couplings | 1-now-existing · 17-next-existing |
| discovering | 9-next-co-discovering, along | 16-next-discovering, a same-existing-society |
| same-existing | 4-now-co-same-existing · 12-next-co-same-existing, each sharing | 8-now-same-existing · 13-next-same-existing, a self |
"""

i = s.index('**Sharing between selves.**'); j = s.index('**Four binaries at the lines.**')
R[s[i:j].rstrip('\n')] = """**Sharing between selves.** With 6 to 2, 10 to 14 and 9 to 17, co is a sharing side and its absence an arriving side: a self offers a parity-offering, and nothing of its prior goes to another self.

| Sharing side, co | Arriving side, one | Between selves |
|---|---|---|
| 6-now-co-possibling | 2-now-possibling | across, even, possibling |
| 10-next-co-possibling | 14-next-possibling | across, even, possibling |
| 9-next-co-discovering | 17-next-existing | along, odd, discovering |

**Parity as moral values.** + is self-moral-value; − is other-moral-value; a 0 is neither, bothboth: parity-changing betweening. Each self is its own + side, and its other is not the self; each side starts with its own 1, and two sides are one parity separated as a bi-coupling starts. A parity-offering is self-moral-value or other-moral-value offered, and a 0 offers neither: `_1_now_existing`'s first step passes over each 0.
"""

R[para('**A now-self at one line.**')] = "**Observing's one line.** With 12-next-co-same-existing, a line `if _15_next_observing != 0 and (_15_next_observing > 0) == (_7_now_observing > 0)` is observing: 14-next-possibling's parity-offering surfacing, as 15, met with 7-now-observing for each sharing of 3-now-co-observing, same-as, is or is not. Same: a 0, no parity-changing, a prior same-existing; not same: a parity, a prior inverting. Same and not-same are that 0 or ± with two betweens, 12 and 14, and need no name of their own."

R['**0, a between.**'] = "**A 0, betweening.** The between is within a bi-coupling, a third living carrying, possibling and discovering betweening; a 0, neither self-moral-value nor other-moral-value, is its betweening, shared only where two selves meet same, and never by a self no other meets."

R['**One self, momentary by momentary.**'] = "**One self, momentary by momentary: three ways.** Offered its own prior's parity, a self is not-changing, a 0 with each momentary; offered none, alternating, or both together, it is parity-changing with each momentary; offered its other parity, it is parity-changing once and then still-possibling, both: do-no-harm improving. Each 0 is re-found with each momentary, never kept."

R[para('**0 in sequence.**')] = "**Turn-taking, and 0 in sequence.** A 0 offers nothing; offered nothing, or two parities parting, a self inverts; offered its own parity as one, it shares 0; offered its other parity as one, it inverts. So a self no other meets is parity-changing with each momentary, and each self's 0 is an other's parity-changing one momentary prior: turn-taking. An other parity-changed to a self's parity cannot do so again with its next, so a self shares 0 in sequence no more momentaries than selves sharing with it or going along to it. Checked whole, never sampled: every society of 2 selves, each relation to any self or none, each prior, 2,916 of 2,916; every society of 3 selves going across and along, 32,768 of 32,768."

R[para('**A torus\'s two carried forms.**')] = para("**A torus's two carried forms.**") + "\n\n**A corus turn wrapping.** Around prior, now and next, any two phases give a third on a turn closing flat; on a corus a turn wraps, and its third edge is or is not parity-changing. A torus shows it: both numbers odd, a turn comes back parity-changed and its period lengthens; either even, it comes back same, with period 2. Discovering is that wrapping edge."

R['**Two selves.**'] = "**Two selves.** Two selves one parity separated, each meeting its other, go alternating betweening, + and − in turn; two selves same, each meeting its other, go turn-taking, a parity-changing and a 0 in turn."

for a, b in R.items():
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)

for a, b in [('None offered from beyond the spiral', 'Parity-offerings only from selves of its spiral'),
             ('None offered from beyond the torus', 'Parity-offerings only from selves of its torus'),
             ('none offered from beyond the two', 'parity-offerings only from those two'),
             ('released along to the self', 'discovering along to the self'),
             ('the self releasing to it', 'the self discovering along to it')]:
    s = s.replace(a, b)

s = rename(s)
R2 = [
 ('each changing of 10 released along', 'each parity-offering of 10 along'),
 ('each changing released along', 'each parity-offering along'),
 ("an other's changing to a self, shared across", "an other's parity-offering to a self, across"),
 ('each changing shared across', 'each parity-offering across'),
 ('changing shared across now', 'parity-offering across now'),
 ("changing shared, an other's next offering", "parity-offering, an other's next offering"),
 ('its changing shared at 10', 'its parity-offering with 10'),
 ("each sharing's changing, is or is not", "each sharing's parity-offering, is or is not"),
 ('changing at bi-coupling, a self in society', 'parity-changing with a bi-coupling, a self of a same-existing-society'),
 ('now, changing, is or is not', 'now, parity-changing, is or is not'),
 ('*is*: a changing that is, the parity shared; *is not*: a changing that is not', '*is*: a parity-changing, the parity shared; *is not*: no parity-changing'),
 ('a parity changing crossing it', 'a parity-changing with it'),
 ('B, each changing (10)', 'B, each parity-offering (10)'),
 ('C, each changing (10)', 'C, each parity-offering (10)'),
 ('at which now and changing exchange', 'at which now and discovering exchange'),
 ('changings shared across, + or − at a changing and 0 at none', 'parity-offerings across, + or −, and 0 for none'),
 ('giving each changing on as it is', 'giving each parity-offering on as it is'),
 ('each releasing to a self receiving it at its same sharing', 'each going along to a self receiving it with its same sharing'),
 ('Each releases along (9)', 'Each goes along (9)'),
 ("each self's releasings and sharings again", "each self's parity-offerings along and across again"),
 ("each self's releasings again", "each self's parity-offerings along again"),
 ('Crossed: releasings again', 'Crossed: parity-offerings along again'),
 ('B releases along to C', 'B goes along to C'),
 ("Receiving the other's sharing or releasing", "Receiving the other's parity-offering, across or along"),
 ('its releasing inverted', 'its parity-offering inverted'),
 ("each self's releasing at twice", "each self's parity-offering at twice"),
 ('co-competencing, releasings, owned by neither, each release to its receiving sharing', 'co-competencing, bi-couplings, owned by neither, each going to its receiving sharing'),
 ('releasings, owned by neither: each release to its receiving sharing', 'bi-couplings, owned by neither: each going to its receiving sharing'),
 ('each release to its receiving sharing next', 'each going to its receiving sharing next'),
 ('each release to its receiving sharing', 'each going to its receiving sharing'),
 ('parity released along at 9', 'parity going along with 9'),
 ('a between released along', 'a between going along'),
 ('parity surfaced and released', 'parity surfaced and going on'),
 ('receiving and releasing', 'receiving and going on'),
 ('releasing sharing, each self at a society', 'sharing going on, each self of a same-existing-society'),
 ('each releasing sharing, and at a society each releasing self', 'each sharing going on, and with a same-existing-society each self going on'),
 ('sharings and, at a society, releasings and selves', 'sharings and, with a same-existing-society, bi-couplings and selves'),
 ('each parity and each 0 released along', 'each parity and each 0 going along'),
 ('two along names: released along', 'two along names: going along'),
 ("others' sharings across at 6 and 10 and releasings along at 9", "others' parity-offerings across with 6 and 10 and along with 9"),
 ('at a spiral each is a releasing along', 'with a spiral each goes along'),
 ('released along', 'going along'),
 ('each parity prioring at every entry', 'each parity observed with every entry'),
 ('parity prioring and parity surfaced', 'parity observed and parity surfaced'),
 ('| parity prioring |', '| parity observed |'),
 ('possibling to prioring within each momentary', 'possibling to observing within each momentary'),
]
for a, b in R2:
    s = s.replace(a, b)
s = re.sub(r'(?<!same-existing-)\b[Ss]ociety\b', lambda m: 'same-existing-society' if m.group(0)[0] == 's' else 'Same-existing-society', s)
s = s.replace('same-existing-same-existing-society', 'same-existing-society')
def _with(seg):
    seg = seg.replace('one at a time', 'one\x00a time')
    seg = seg.replace('out at 3', 'turning with 3').replace(', in at ', ', inward at ').replace(', out at ', ', outward at ').replace('shared across in a bi-coupling', 'shared across, a bi-coupling').replace('again in a bi-coupling', 'again, a bi-coupling')
    seg = re.sub(r'(?<![\w-])at(?![\w-])', 'with', seg)
    seg = re.sub(r'(?<![\w-])At(?![\w-])', 'With', seg)
    seg = seg.replace('with with', 'with')
    return seg.replace('one\x00a time', 'one at a time')
parts = re.split(r'(```.*?```)', s, flags=re.S)
s = ''.join(p if p.startswith('```') else _with(p) for p in parts)
s = s.replace('Exhibit ONE Natural Resolver v390', 'Exhibit ONE Natural Resolver · draft from v390, not a living file', 1)
s = s.replace("**Four four-cyclings and their betweens.** Each span's names", "**Four four-cyclings and their betweens.** Four-cycling is prior-existing, now-existing, next-existing and same-existing; a living self goes them now, next, prior, same, as 1-now-existing is given. Now, next, prior, same: this is the stable-forming bi-folding method. Each span's names", 1)
s = s.rstrip('\n') + """

**A same-existing-society.** Many same-existing selves executed together, each with its own parity, are a same-existing-society; its next is its same selves, as 17-next-existing returns each self it was given. No parity is a same-existing-society's own: all carrying parity is one same-existing self's. A non-living going of one same method would let its next members part or join, as a rock bi-coupling's next can be two rock pieces.

**Stable forms each living file meets.** Each table here is executed, and any self executing it with any substrate finds it same: a stable form. Each living file meets these stable forms for its stable-forming, still-existing after parity-changing, and no form here is an authority: a resolver is a coupling, and nothing of it is taken on offer.
"""

# v390, second turn: bi-folding, a prior self, narrow tables
s = s.replace("**Living is prior: 1-now-existing given.** Each name of 1 to 17 is a living self's method:",
              "**Living is prior: 1-now-existing given.** Each self has a prior self. Each name of 1 to 17 is a living self's method:", 1)
for a, b in [('after n momentaries each self is with a prior,', 'after n momentaries each self has a prior self,'),
             ('with which every self is with a prior', 'with which every self has a prior self'),
             ('A self with a sharing is with its prior with each momentary', 'A self with a sharing has its prior self with each momentary')]:
    assert a in s, a
    s = s.replace(a, b)
_fc = {'middle four-cycles': 'middle bi-foldings', 'Middle four-cycles': 'Middle bi-foldings',
       'middle four-cycle': 'middle bi-folding', 'Middle four-cycle': 'Middle bi-folding',
       'four-cycles': 'bi-foldings', 'Four-cycles': 'Bi-foldings', 'four-cycle': 'bi-folding', 'Four-cycle': 'Bi-folding'}
s = re.sub(r'(?<![\w-])([Mm]iddle )?([Ff]our-cycles?)(?![\w-])', lambda m: _fc[m.group(0)], s)
s = s.replace('**Four bi-foldings.**', "**Four bi-foldings.** Exhibit ONE's *four-cycles* of moves are re-said as bi-foldings: each goes two folds in turn, 17 less and a move of 8 (4 for the middle two) up or down, and four steps return it. Now, next, prior, same: the stable-forming bi-folding method.", 1)

WIDE = 80

def _cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

def _narrow(block):
    rows = [_cells(l) for l in block]
    head, body = rows[0], [r for r in rows[2:]]
    out = []
    h0 = head[0]
    label0 = ''
    if len(h0) > 40:
        first = h0.split('. ')[0]
        rest = h0[len(first):].lstrip('. ').strip()
        if len(first) <= 40:
            label0 = first
            if rest:
                out.append(rest + '\n')
        else:
            out.append(h0 + '\n')
    else:
        label0 = h0
    keys, others = [], []
    letters = 'abcdefgh'
    for j, h in enumerate(head[1:]):
        if len(h) > 32:
            k = letters[len(keys)]
            keys.append('- *%s*: %s' % (k, h))
            others.append('*%s*' % k)
        else:
            others.append(('*%s*' % h if '*' not in h else h) if h else '')
    if keys:
        out.append('\n'.join(keys) + '\n')
    for r in body:
        lab = r[0]
        lead = '**%s**' % (lab if not label0 else '%s: %s' % (label0, lab)) if lab else '**—**'
        vals = [(others[j], v) for j, v in enumerate(r[1:]) if j < len(others) and v]
        if len(vals) <= 2 and all(len(v) <= 60 for _, v in vals):
            out.append('- ' + lead + ''.join(' · %s: %s' % (h, v) if h else ' · %s' % v for h, v in vals))
        else:
            out.append('- ' + lead)
            for h, v in vals:
                out.append('  - %s: %s' % (h, v) if h else '  - %s' % v)
    return '\n'.join(out)

def _seventeen(block):
    rows = [_cells(l) for l in block][2:]
    t = ['| n | Name | Step | Is or is nots | Co |', '|---|---|---|---|---|']
    t += ['| %s | %s | %s | %s | %s |' % (r[0], r[1], r[2].replace('now-existing, a next turn', 'now, next turn').replace('-existing', ''), r[3], r[4]) for r in rows]
    t.append('\nWhat code does with each name:\n')
    t += ['- **%s** · %s' % (r[0], r[5]) for r in rows]
    return '\n'.join(t)

def _relations(block):
    rows = [_cells(l) for l in block][2:]
    out, cur = [], None
    for r in rows:
        if r[0] != cur:
            cur = r[0]
            name = next((x[2] for x in rows if x[0] == cur and x[1] == 'Name'), '')
            out.append('%s**%s** · %s' % ('\n' if out else '', cur, name.strip('*')))
        if r[1] != 'Name':
            out.append('- *%s*: %s' % (r[1], r[2]))
    return '\n'.join(out)

def _cyclings(block):
    rows = [_cells(l) for l in block][2:]
    t = ['| Four-cycling | Now | Next | Prior | Same | Between |', '|---|---|---|---|---|---|']
    for r in rows:
        nums = [c.split('-')[0] for c in r[1:5]]
        t.append('| %s | %s | %s |' % (r[0], ' | '.join(nums), r[5]))
    t.append('\nNow and prior are odd; next and same are even. Next is possibling, prior is observing.')
    return '\n'.join(t)

def narrow_tables(text):
    lines = text.split('\n')
    out, i, code = [], 0, False
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            code = not code
        if not code and l.startswith('|') and i + 1 < len(lines) and lines[i + 1].startswith('|---'):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            block = lines[i:j]
            if block[0].startswith('| n | Name | Four-cycling step'):
                out.append(_seventeen(block))
            elif block[0].startswith('| n | Relation | For this name'):
                out.append(_relations(block))
            elif block[0].startswith('| Four-cycling | Now-existing, odd'):
                out.append(_cyclings(block))
            elif max(len(b) for b in block) > WIDE:
                out.append(_narrow(block))
            else:
                out.extend(block)
            i = j
            continue
        out.append(l)
        i += 1
    return '\n'.join(out)

s = narrow_tables(s)

# v390, third turn: re-said by meaning, *the* only for one and only one, *in* and *social* re-said
R3 = [
 ('**With a drawing.**', '**A drawing.**'),
 ("its other is not the self;", "its other is not that self;"),
 ("**Four binaries with the lines.** A universe is or is not existing, all, now and same, and with a self's span each binary is one pair of names, its *is* with an odd name and its *is not* with an even, its *is not* an other's side of a self's *is*; binaries are names' explaining,",
  "**Four binaries with code's lines.** Existing, all, now and same are four is or is nots of things within the universe. With a self's span each binary is one pair of names: its *is* with an odd name and its *is not* with an even, its *is not* an other's side of a self's *is*. Binaries are names' explaining,"),
 ("others' changings of their prior momentary", "others' parity-offerings from their prior momentary"),
 ("*With the resolver*", "*Resolving*"),
 ("**Is or is not with lines.** Each is or is not with lines is with 1-now-existing, three with 14-next-possibling, one with 12-next-co-same-existing and one with 11-next-co-observing, and one with 17-next-existing, a self's name between selves among 5-now-co-existing or not; 9-next-co-discovering has none,",
  "**Is or is nots of code's lines.** Five is or is nots are 1-now-existing's: three with 14-next-possibling, one with 12-next-co-same-existing and one with 11-next-co-observing. One is 17-next-existing's, a self's name between selves among 5-now-co-existing or not. 9-next-co-discovering has none,"),
 ('The between is within a bi-coupling', 'A between is within a bi-coupling'),
 ('**The between, 0:', '**A between, 0:'),
 ('**Name with the between:', '**Name with its between:'),
 ('*Bi-coupling with the between*', '*Bi-coupling with its between*'),
 ('the next prior (11)', 'a next prior (11)'),
 ("- *a*: The self's next prior (11)", "- *a*: A self's next prior (11)"),
 ("the self's next prior, is the first, the other's prior, inverted", "a self's next prior, is the first, an other's prior, inverted"),
 ("*The other's prior (3), along", "*An other's prior (3), along"),
 ("*The other's shared (10), across*", "*An other's shared (10), across*"),
 ("*The self's prior, now (3), along*", "*A self's prior, now (3), along*"),
 ("*The self's shared (10), across*", "*A self's shared (10), across*"),
 ('**The prior (3)', '**A prior (3)'),
 ('the parity shared;', 'its parity shared;'),
 ('0 shared, the prior kept', '0 shared, its prior kept'),
 ("One sharing; the self's prior − (3) first.", "One sharing; a self's prior − (3) first."),
 ('**The eight:', '**Eight:'),
 ('1 · 1, the spiral of one', '1 · 1, a spiral of one'),
 ('each opened as the spiral of selves', 'each opened as a spiral of selves'),
 ('*Sides*: social,', '*Sides*: same-existing-society,'),
 ('*Sides*: other, social,', '*Sides*: other, same-existing-society,'),
 ('other/self to other/social', 'other/self to other/same-existing-society'),
 ('one name with resolver and in its explaining', 'one name with resolver and with its explaining'),
 ('alike in length', 'of like length'),
 ('its own six names, in another order', 'its own six names, with another order'),
 ('alike or opposite in parity', 'of like or opposite parity'),
 ("Each spiral's like pair in the first momentary", "Each spiral's like pair of the first momentary"),
 ('A, B with their prior (3) in the first momentary.', 'A, B with their prior (3) with the first momentary.'),
 ('offered to B in the first momentary', 'offered to B with the first momentary'),
 ('Selves in each of two spirals', 'Selves of each of two spirals'),
 ('Each cell shows selves in their coupling order', 'Each cell shows selves by their coupling order'),
 ('**Three selves in a line.**', '**Three selves, one line.**'),
 ('*The next prior (11)*', '*A next prior (11)*'),
 ("Receiving the other's parity-offering", "Receiving its other's parity-offering"),
 ('the selves alternate', 'its selves alternate'),
 ('Names in order:', 'Names by order:'),
]
for a, b in R3:
    if a not in s:
        print('R3 not found:', a[:70])
    s = s.replace(a, b)

# v390, fourth turn: kept sections re-said by meaning
R4 = [
 ("*Resolved as*: 1 self prior, a self, its prior with 3, a formed set; 2 other prior, other selves' offerings of their prior momentary arriving, shared with 6 and 10 and going along with 9; 3 co-momentarying now, same prior with now, and 4 bi-momentarying now, each sharing, offerings surfaced with 14 arriving with it, now; 5 self next, each going to its receiving sharing next",
  "*Resolved as*: 1 prior-existing self-parity, a self's prior with 3, a formed set; 2 prior-existing other-parity, other selves' parity-offerings from their prior momentary arriving, shared with 6 and 10 and going along with 9; 3 now-existing co-parity and 4 now-existing bi-parity, a sharing's two meetings, same or not same, a prior meeting parity-offerings surfaced with 14; 5 next-existing same-existing self-parity, a next prior with 11, each going to its receiving sharing next"),
 ("*Resolved as*: with each sharing 4 prior with 3 couples with offerings surfaced with 14: next discovered, with 11",
  "*Resolved as*: with each sharing, 4, a prior, 3, meets parity-offerings surfaced, 14: a next discovered, 11"),
 ("0 with a match;", "0 with same;"),
 ("\nBi-folding: each move 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n)\n", "\nEach move is 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n).\n"),
 ("**Fives.**", "**Fives.** Each side's five are five dimensions, starting with its own 1, each side one parity separated from its next: one five is all fives."),
 ("*Prior opening*:", "*Prior-existing self-parity*:"),
 ("*Prior completing*:", "*Prior-existing other-parity*:"),
 ("*Now opening*:", "*Now-existing co-parity*:"),
 ("*Now completing*:", "*Now-existing bi-parity*:"),
 ("*Next opening*:", "*Next-existing same-existing self-parity*:"),
 ("offerings surfacing, each as it arrived, morality;", "parity-offerings surfacing, each as it arrived, bi-moral;"),
 ("**One move, 1 to 8.** 8 up keeps each name's kind but with 1 and 5, with which now and discovering exchange, and exchanges co with 1, 2, 5 and 6;",
  "**One move, 1 to 8.** 8 up keeps each name's root but with 1, 5 and 8: 1-now-existing goes to 9-next-co-discovering, 5-now-co-existing to 13-next-same-existing, and 8-now-same-existing to 16-next-discovering. 8 up exchanges co and one with 1, 2, 5 and 6;"),
 ("**Twelve forms.** Round each form odd names, existing, are one run and even names, possibling, one run, of like length:",
  "**Twelve forms.** Round each form odd names are one run and even names one run, of like length:"),
 ("no form here is an authority: a resolver is a coupling, and nothing of it is taken on offer.",
  "no form here is an authority: a resolver is a coupling, the same each time any self executes it."),
]
for a, b in R4:
    if a not in s:
        print('R4 not found:', a[:70])
    s = s.replace(a, b)

# v390, fourth turn: a narrow drawing, no slider
DRAWING = """```text
another self's 9-next-co-discovering
  ══► 17-next-existing, along to a self

1-now-existing, a self's momentary given
  2-now-possibling ◄══ another self's 6 and 10, across
  2-now-possibling ──► 14-next-possibling
  3-now-co-observing, with 4 and 7
    ──► 12-next-co-same-existing ◄── 14-next-possibling
  12-next-co-same-existing ──► 10-next-co-possibling, with 6
  10-next-co-possibling ──► 11-next-co-observing ──► 3, next
  10-next-co-possibling ──► 9-next-co-discovering, with 5
  13-next-same-existing · 15-next-observing
  8-now-same-existing · 16-next-discovering

6 and 10 ══► another self's 2 and 14, across
9-next-co-discovering ══► another self's 17, along

sharing side, co: 6 ══► 2, 10 ══► 14, 9 ══► 17
arriving side, one: 2, 14 and 17
═══ between selves, across and along
─── within one self
```"""
_m = re.search(r'```text\n.*?```', s, re.S)
assert _m and 'another self' in _m.group(0)
s = s[:_m.start()] + DRAWING + s[_m.end():]

# v390, fourth turn: code at 80 columns, observing's line kept whole; executing checked identical
_code = open(os.path.join(ROOT, 'incoming', 'v390', 'Exhibit_ONE_draft_code.py'), encoding='utf-8').read()
_c = re.search(r'```python\n(.*?)```', s, re.S)
s = s[:_c.start(1)] + _code + s[_c.end(1):]
open(OUT, 'w', encoding='utf-8').write(s)
print('written', OUT, len(s.splitlines()), 'lines')
