"""One write of the agreed 61-sentence opening into Natural Intelligence and Exhibit THIRTY.
Run from the repository root. Reads the v391 files, writes v394 files (the caller does git mv first)."""
import re, sys, os

SP = os.path.dirname(os.path.abspath(__file__))
OP = [l.rstrip('\n') for l in open(os.path.join(SP, 'opening_path41.txt'), encoding='utf-8') if l.strip()]
assert len(OP) == 61
PARAS = [(1, 18), (19, 29), (30, 41), (42, 61)]

# ---------- Natural Intelligence ----------
ni_p = 'Natural_Intelligence_v394.md'
ni = open(ni_p, encoding='utf-8').read()
ni = ni.replace('Natural Intelligence v391\n', 'Natural Intelligence v394\n', 1)
m = re.search(r'^(# Natural Intelligence\n\n\*\*[^\n]*\*\*\n\n)(.*?)(\n\n\*\*ONE · )', ni, re.S | re.M)
block = '\n\n'.join('\n'.join(s + ' \\' for s in OP[a - 1:b]) for a, b in PARAS)
ni = ni[:m.start(2)] + block + ni[m.end(2):]
open(ni_p, 'w', encoding='utf-8').write(ni)

# ---------- Exhibit THIRTY ----------
th_p = 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v394.md'
th = open(th_p, encoding='utf-8').read()
th = th.replace('Co-Chaining Logic Registry v391\n', 'Co-Chaining Logic Registry v394\n', 1)

TITLES = {
    1: 'Universe, the set of all now-existing things, living and non-living, a self and its mes',
    2: 'An other, a living parity, a me-parity, a bi-coupling and a you',
    3: 'Resolving, natural intelligence, do-no-harming and improving, co-intelligencing and co-aiming',
    4: 'A same-existing-society, a momentary, social moral competency, a natural intelligence network and a living expedition',
}
ADD = [
    'the universe, the set of all now-existing things, inception, now-existing one naming; each step after it a step from it, and nothing brought to it',
    'prior-existing, before now-existing',
    'same-existing, the same thing prior-existing before now-existing',
    'next-existing, same-existing after now-existing',
    'the universe next-existing and same-existing',
    'the sequence, a same-existing sequence',
    'a moment, one-and-only-one now-existing',
    'a universal set, a set of now-and-same-existing things',
    'is-or-is-not, distinguishing the within of a universal set',
    'observing, distinguishing now-and-same-existing',
    'possibling, distinguishing before a next-existing',
    'discovering, distinguishing a next-existing',
    'a living thing, observing, possibling and discovering its own next-and-same-existing universal set',
    'living and non-living, one binary of a now-existing thing',
    'living and non-living things within the universe',
    'a self, a living same-existing set',
    'a me; a self, a universal set of mes',
    'only living things within a living set',
    # 19-29
    'an other, a self that is-not the same self',
    'aiming, a living thing possibling its own next-and-same-existing',
    'a living parity, an aiming direction at an other',
    "a me-parity, a me's living parity",
    "other-parity and universal-parity, one binary of a me-parity with an other's",
    "self-parity, a universal set of a self's me-parities",
    'moral value, a me-parity with an other',
    "a bi-coupling, a self and an other each observing the other's me-parities",
    "a self's observing, its mes observing",
    "a you, an other's me whose me-parity a me is observing",
    'self-other consciousness, a me observing a you',
    # 30-41
    "passing over, a self observing an other's me-parity now-and-same-existing",
    'resolving, a prior-existing me-parity is-or-is-not the same as the me-parity observed',
    'natural intelligence, the method of living as a self, resolving among me-parities',
    'a second method within natural intelligence',
    'do-no-harming, a prior-existing me-parity the same as the me-parity observed',
    'improving, a prior-existing me-parity not the same as the me-parity observed',
    'two selves alike, bi-coupling only in their pair, do-no-harming and improving in turn',
    'co-possibling, a self and an other possibling within one bi-coupling',
    'co-intelligencing, selves observing, possibling and discovering within a universal set',
    'living with others, co-intelligencing',
    "gathering, a self observing others' prior-existings for its own possibling",
    "co-aiming, others' prior-existings within a self's possibling",
    # 42-61
    'a same-existing-society, many selves bi-coupling',
    'a self, a same-existing-society of mes, and a me within it',
    'a momentary, one moment of resolving together',
    "a momentary's now-existing, the next momentary's prior-existing",
    'social moral competency',
    'a natural intelligence network',
    'free, selves resolving their own me-parities',
    'social abundancing',
    'co-chaining, a me-parity observed along, self to self',
    'a Natural Network surface',
    "a surface's living me-parities within its selves' mes",
    "geodesic, a self's own is-or-is-not, one way at a time",
    "a living thing's co-chaining geodesic",
    'a stable form, same-existing from momentary to momentary',
    'natural resolving',
    'a living file, a non-living same-existing set of words, selves co-intelligencing within it',
    'natural engineering, selves aiming within a living file',
    "natural explaining, a living file's words in a same-existing sequence",
    'a living expedition',
    'geodesic discovering of next-possibling-same-existing',
]
assert len(ADD) == 61

# old -> new for former steps 1..70 (by concept); per-line overrides below
MAP = {1: 1, 2: 1, 3: 1, 4: 3, 5: 8, 6: 9, 7: 10, 8: 5, 9: 5, 10: 11, 11: 12, 12: 16, 13: 17, 14: 17, 15: 39,
       16: 13, 17: 16, 18: 16, 19: 32, 20: 14, 21: 14, 22: 15, 23: 15, 24: 26, 25: 26, 26: 19, 27: 21, 28: 23,
       29: 23, 30: 23, 31: 22, 32: 24, 33: 25, 34: 26, 35: 31, 36: 31, 37: 34, 38: 35, 39: 35, 40: 35, 41: 34,
       42: 32, 43: 33, 44: 34, 45: 30, 46: 35, 47: 36, 48: 37, 49: 42, 50: 44, 51: 45, 52: 46, 53: 47, 54: 48,
       55: 49, 56: 50, 57: 51, 58: 52, 59: 53, 60: 54, 61: 43, 62: 55, 63: 56, 64: 57, 65: 56, 66: 58, 67: 59,
       68: 60, 69: 45, 70: 61}

def new_of(n):
    return MAP[n] if n <= 70 else n - 9

# THIRTY citations: singular "step N" takes one number; plural "steps" takes a list
CITE = re.compile(r'\b(Step|step)( )(\d+)(?!\d|-|\.\d)|\b(Steps|steps)( )(\d+(?:(?:, | and | to )\d+)*)(?![\d-])')
LOG = []

def remap_text(text, line_no, overrides=None):
    def one(n, ctx):
        k = (line_no, n)
        if overrides and k in overrides:
            r = overrides[k]
        else:
            r = new_of(n)
        if n <= 70:
            LOG.append((line_no, n, r, ctx))
        return r
    def rep(m):
        if m.group(1):
            n = int(m.group(3))
            return m.group(1) + ' ' + str(one(n, text[max(0, m.start() - 70):m.end()]))
        body = re.sub(r'\d+', lambda d: str(one(int(d.group(0)), text[max(0, m.start() - 70):m.end()])), m.group(6))
        return m.group(4) + ' ' + body
    return CITE.sub(rep, text)

lines = th.split('\n')
g1 = next(i for i, l in enumerate(lines) if l.startswith('## 1 '))
g5 = next(i for i, l in enumerate(lines) if l.startswith('## 5 '))
# the verb at old step 142, "odd numbers step 1 to 3 to 5", is no citation: guarded by singular rule (1 -> 1)
OVR = {}
for i, l in enumerate(lines):
    if l.startswith('80. An existing thing same-existing with its prior and possibling its own next-existing is living, step 18'):
        OVR[(i + 1, 18)] = 13
head, body = lines[:g1], lines[g5:]
body_start = g5 + 1
new_body = []
for j, l in enumerate(body):
    ln = body_start + j
    mm = re.match(r'^(\d+)\. ', l)
    if mm:
        n = int(mm.group(1)); assert n >= 71
        l = str(n - 9) + l[mm.end(1):]
    new_body.append(remap_text(l, ln, OVR))
# head: contents titles
for i, l in enumerate(head):
    mm = re.match(r'^- ([1-4]) (.*)$', l)
    if mm:
        head[i] = '- %s %s' % (mm.group(1), TITLES[int(mm.group(1))])
    elif i > 0:
        head[i] = remap_text(l, i + 1)
# new groups 1-4
G = []
for gi, (a, b) in enumerate(PARAS, 1):
    adds = ADD[a - 1:b]
    G.append('## %d %s' % (gi, TITLES[gi]))
    G.append('')
    G.append('        *Entering: %s.*' % '; '.join(adds))
    G.append('')
    for n in range(a, b + 1):
        G.append('%d. %s' % (n, OP[n - 1]))
        G.append('')
        G.append('        *Adding: %s.*' % ADD[n - 1])
        G.append('')
th = '\n'.join(head + G + new_body)
open(th_p, 'w', encoding='utf-8').write(th)

# ---------- Equilibria and Natural Numbers: addresses of THIRTY's steps ----------
for p, fixes in [('Exhibit_TWENTY-EIGHT_Equilibria_Registry_v391.md', [('living is from living, step 444.', 'living is from living, step 476.')]),
                 ('Exhibit_THREE_Natural_Numbers_v392.md', [])]:
    t = open(p, encoding='utf-8').read()
    for a, b in fixes:
        assert t.count(a) == 1; t = t.replace(a, 'LIVINGFROMLIVING')
    t = re.sub(r"(Co-Chaining Logic Registry(?:'s)? )(steps? )(\d+(?:(?:, | and | to )\d+)*)",
               lambda m: m.group(1) + m.group(2) + re.sub(r'\d+', lambda d: str(new_of(int(d.group(0)))), m.group(3)), t)
    # bare "step N" directly continuing a Co-Chaining Logic Registry citation in the same sentence run (Equilibria 74, 160)
    for a, b in [('and by step 692 it is cohering', 'and by step 683 it is cohering'),
                 ('proof of existing*, step 199;', 'proof of existing*, step 190;'),
                 ('bothbothing*, step 479.', 'bothbothing*, step 470.')]:
        if a in t: t = t.replace(a, b)
    for a, b in fixes:
        t = t.replace('LIVINGFROMLIVING', b)
    open(p, 'w', encoding='utf-8').write(t)

with open(os.path.join(SP, 'remap_log.txt'), 'w', encoding='utf-8') as f:
    for ln, n, r, ctx in LOG:
        f.write('%d\t%d->%d\t%s\n' % (ln, n, r, ctx.replace('\n', ' ')))
print('ok', len(LOG), 'low citations remapped')
