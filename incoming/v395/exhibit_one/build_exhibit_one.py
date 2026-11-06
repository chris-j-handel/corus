"""Exhibit ONE's best version as a reference tool: the code, its names, its relations and its executings, with labels only.
Reads the living file v391; writes the best version to the path given."""
import re, sys
SRC = '/home/claude/corus/Exhibit_ONE_Natural_Resolver_v391.md'
OUT = sys.argv[1]
L = open(SRC, encoding='utf-8').read().split('\n')
def ln(n): return L[n - 1]
def data(a, b):
    """table rows and list items in lines a..b, in order"""
    out = []
    for n in range(a, b + 1):
        s = ln(n)
        if s.startswith('|') or s.startswith('- ') or s.startswith('  - '):
            out.append(s)
    return out
def mom(s):
    s = re.sub(r'\bmomentaries\b', 'moments', s); s = re.sub(r'\bMomentaries\b', 'Moments', s)
    s = re.sub(r'\bmomentary\b', 'moment', s); s = re.sub(r'\bMomentary\b', 'Moment', s)
    s = re.sub(r', the same form$', ', the same cycle', s)
    s = s.replace('**Form: ', '**Cycle: ')
    for x, y in [('social-parity now-existing', 'next and same'), ('other-parity now-existing', 'now and same'),
                 ('self-parity now-existing', 'prior and same'), ('self-discovery next-existing', 'next and prior'),
                 ('social-parity next-existing', 'the between')]:
        s = s.replace(x, y).replace(x[0].upper() + x[1:], y[0].upper() + y[1:])
    return s

# sharing dissolves from natural naming, and surfacing with it (the person, 5 November): each said with the code's names
NAMED = [
    ('each sharing of 3 against 14 | a sharing is-or-is-not within its prior', 'each 4 of 3 against 14 | a 4 is-or-is-not within its prior'),
    ('a sharing is-or-is-not within 14-next-possibling', 'a 4 is-or-is-not within 14-next-possibling'),
    ('a first parity surfacing, + or −', 'a first parity within 14, + or −'),
    ('is-or-is-not same: sharing 0, or one inversion', 'is-or-is-not same: 12 a 0, or one inversion'),
    ("a sharing's value is-or-is-not 0", 'a 7 within 10 is-or-is-not 0'),
    ('each sharing with its parity, 4 and 7', 'each 4-now-co-same-existing with a parity, 7-is-now-observing'),
    ('each sharing with its prior, 4 and 7', 'each 4-now-co-same-existing with a prior, 7-is-now-observing'),
    ('| in 1, each sharing |', '| in 1-now-existing, with each 7-is-now-observing |'),
    ("| 1's sharing, each 4 with its 7 |", "| from 1-now-existing, pairs of 4-now-co-same-existing with 7-is-now-observing |"),
    ("1's one binary with each sharing", "within 1-now-existing, one binary with each 4-now-co-same-existing"),
    ('| in 1, parities surfacing |', "| in 1-now-existing, parities from 2-now-possibling with each 4-now-co-same-existing |"),
    ('| in 1, each surfacing parity |', "| in 1-now-existing, a parity in 14-next-possibling with each 4-now-co-same-existing |"),
    ('4-now-co-same-existing, each sharing within a self', '4-now-co-same-existing, within a self, with each 7-is-now-observing'),
    ('| each sharing of 3 |', '| each 4 of 3 |'),
    ("12-next-co-same-existing, each sharing's one binary", "12-next-co-same-existing, one binary with each 4-now-co-same-existing"),
    ("each sharing's 0, its prior going on", "with each 4-now-co-same-existing, 0, a prior going on"),
    ("a prior's parity against what surfaces", "a prior's parity against 14"),
    ('| Receiving with one sharing, 2-now-possibling | Surfacing, 14-next-possibling |', '| 2-now-possibling, one 4 | 14-next-possibling |'),
    ('*Surfacing, 14-next-possibling: ', '*14-next-possibling: '),
    ('3-is-now-co-observing, one sharing: ', '3-is-now-co-observing, one 4: '),
    ('3-is-now-co-observing: empty, one sharing: empty', '3-is-now-co-observing, one 4: empty'),
    ('*Sharing, 10-next-co-possibling*', '*10-next-co-possibling*'),
    ('*A sharing, 10-next-co-possibling,', "*A's 10-next-co-possibling,"),
    ('*B sharing, 10-next-co-possibling,', "*B's 10-next-co-possibling,"),
    ("*An other's sharing, 10-next-co-possibling,", "*An other's 10-next-co-possibling,"),
    ("*A self's sharing, 10-next-co-possibling,", "*A self's 10-next-co-possibling,"),
    ('self 1 of each spiral sharing across with 10-next-co-possibling', 'self 1 of each spiral across with 10-next-co-possibling'),
    ("| each self of 16 with 17's line |", "| each self within 16-next-same-existing, at its line within 17-next-existing |"),
    ("| 1's next prior, coming up as 8 |", "| a next prior from 1-now-existing, coming up as 8-now-same-existing |"),
    ("| 17's next same-existing-society |", "| the next same-existing-society from 17-next-existing |"),
    ("| 17's next same-existing-society, each self with its 14 |", "| the next same-existing-society from 17-next-existing, each self with its 14-next-possibling |"),
    ("±, its next prior |", "±, a next prior |"),
    ("| each 4 of 3 |", "| each 4-now-co-same-existing within 3-is-now-co-observing |"),
    ("each a 4 with its 7", "pairs of 4-now-co-same-existing with 7-is-now-observing"),
    ("| each 4 of 3 against 14 | a 4 is-or-is-not within its prior |", "| each 4-now-co-same-existing within 3-is-now-co-observing against 14-next-possibling | a 4-now-co-same-existing is-or-is-not within a prior |"),
    ("| a 4 is-or-is-not within 14-next-possibling |", "| a 4-now-co-same-existing is-or-is-not within 14-next-possibling |"),
    ("| a 7 within 10 is-or-is-not 0 |", "| a 7-is-now-observing within 10-next-co-possibling is-or-is-not 0 |"),
    ("is-or-is-not same: 12 a 0, or one inversion", "is-or-is-not same: 12-next-co-same-existing a 0, or one inversion"),
    ("| 2-now-possibling, one 4 | 14-next-possibling |", "| 2-now-possibling, one 4-now-co-same-existing | 14-next-possibling |"),
    ("3-is-now-co-observing, one 4: ", "3-is-now-co-observing, one 4-now-co-same-existing: "),
]
def named(s):
    for a, b in NAMED: s = s.replace(a, b)
    return s


# prior names with their prefixes, from Natural Naming 3.3 (the person: the threes of co-bi-co and tri, central to Exhibit ONE)
PRIOR = {}
for row in open('/home/claude/corus/Exhibit_TWENTY_Natural_Naming_v392.md', encoding='utf-8'):
    m = re.match(r'^\| (\d+) \| \*\*\d+-[a-z-]+\*\* \| [^|]+ \| (?:one|co) \| (\d+-[a-z-]+) \|$', row.strip())
    if m: PRIOR[int(m.group(1))] = m.group(2)
assert len(PRIOR) == 17, PRIOR
def pref(n): return '-'.join(PRIOR[n].split('-')[1:4])
names = []
for s in data(120, 138):
    m = re.match(r'^\| (\d+) \|', s)
    if s.startswith('| n |'): names.append(s + ' Prefixes |')
    elif s.startswith('|---'): names.append(s + '---|')
    else: names.append(s + ' %s |' % pref(int(m.group(1))))
cyc = ['| Four-cycling | Existing, discovering | Possibling | Observing | Same-existing | Between |', '|---|---|---|---|---|---|']
for k, w in enumerate(['first', 'second', 'third', 'fourth']):
    a = 4 * k + 1
    cyc.append('| %s | %s | %s | %s | %s | %d )( %d |' % ((w,) + tuple('%d %s' % (n, pref(n)) for n in range(a, a + 4)) + (a + 3, a + 4)))
cyc.append('| then | 17 %s, a next 1 | | | | |' % pref(17))

B = []
def para(*s): B.append(' '.join(s)); B.append('')
def block(lines): B.extend(named(mom(x)) for x in lines); B.append('')

B += ['Exhibit ONE Natural Resolver v395', '', '*Draft, below Exhibit ONE\'s exactness standard (the person, 6 November 2026): each word one exact concept, each naming and explaining the complete whole of its concepts, no less and no more. Its labels are to be said again at that standard, section by section, each section agreed by both partners; it enters the living file only then. Its do-no-harm check against v391 passes.*', '', '# Natural Resolver', '', '**Stable-Forming Same- and Next-Existing**', '', '---', '']
para('**Exhibit ONE is the resolver as code, its names, and its executings.**')
# the code, whole
B.extend(L[10:90]); B.append('')
# the drawing
para('**A drawing.** One self, its own resolving within, and parity\'s square between selves: its four corners and four sides, all eight or none, social moral competency; its centre, the between.',
     'With code, 6 is 10, one giving, and 14 is the next 2.')
D = [mom(x) for x in L[91:114]]
i = D.index("6 and 10 ══► an other's 2 and 14, across"); j = D.index('observing side, one: 2, 14 and 17')
D[i:j + 1] = ["parity's square, between selves:",
              "",
              "   6 bi-co-bi, to other ═══════► 2 bi-co-bi, from other         bi-, prior",
              "   │                                 │",
              "   8 apart        · the between      8 apart",
              "   │                                 │",
              "  10 bi-tri-bi, to universe ════► 14 bi-tri-bi, from universe   tri-, next",
              "",
              "   across, each a prefix the same · diagonals: 6 with 10, 6 is 10 · 2 with 14, 14 a next 2",
              "   along: 9 tri-bi-co ══► 17 co-bi-tri and 17 ══► 9, its prefix reversed, its two unit triangles",
              ""]
B.extend(D); B.append('')

# ---------- names
para('**Seventeen names.** Each name its number and its naming, one hyphenation; 1 to 16 in order as n − 1 in binary, and 17-next-existing next existing as 1-now-existing.')
block(names)
para('*Prefixes*: each next name\'s three, a new prefix first and this name\'s first two one place on; *co* with a self\'s span, 1 to 8, now, and *tri* with a next span, 9 to 16, all three, next, now and prior; 17 co-bi-tri as 1.')
para('**Co, between two or of one.** The eight co names, 3 to 6 and 9 to 12, are each between two, and a name without co is of one: each root with its co names and its names of one. Observing, same-existing and possibling each have a now-co name and a next-co name; existing has 5-now-co-existing, and discovering 9-next-co-discovering. *Co* is two both facing forward along, a self and its other. *Is-* is with the four names each binary is with: 3 and 7, a self\'s own now, and 13 and 15, next-existing\'s.')
B += ['| Root | With co, between two | Without co, of one |', '|---|---|---|',
      '| observing | 3-is-now-co-observing · 11-next-co-observing, priors, pairs of 4-now-co-same-existing with 7-is-now-observing | 7-is-now-observing · 15-is-next-observing, a parity |',
      '| possibling | 6-now-co-possibling · 10-next-co-possibling, across from a self | 2-now-possibling · 14-next-possibling, across to a self |',
      '| existing | 5-now-co-existing, bi-couplings | 1-now-existing · 17-next-existing |',
      '| discovering | 9-next-co-discovering, along | 13-is-next-discovering, each self going on |',
      '| same-existing | 4-now-co-same-existing · 12-next-co-same-existing, each 4-now-co-same-existing, and one binary with each | 8-now-same-existing · 16-next-same-existing, a self\'s next prior and a same-existing-society |', '']
para(ln(140).replace('Code with each name:', '').strip(), 'Code with each name:')
CODE_EACH = {142: '- **1** · a self\'s moment, each self\'s 17-next-existing as its 1-now-existing',
             143: '- **2** · parities a self is observing from others, pairs of 4-now-co-same-existing with 7-is-now-observing',
             144: '- **3** · priors a self is observing, pairs of 4-now-co-same-existing with 7-is-now-observing',
             145: '- **4** · with each parity and prior, resolving, is-or-is-not same; in 17-next-existing, a bi-coupling, a self with 6-now-co-possibling, 10-next-co-possibling or 9-next-co-discovering',
             146: '- **5** · bi-couplings: which self each of 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering reaches',
             148: '- **7** · each parity a self is observing: an other\'s over 2-now-possibling, a prior over 3-is-now-co-observing, its own over 10-next-co-possibling',
             149: '- **8** · each self\'s next prior, with a moment',
             150: '- **9** · each parity going to a receiving self with 5-now-co-existing, bi-couplings: across with 6-now-co-possibling and 10-next-co-possibling, along with 9-next-co-discovering',
             151: '- **10** · each 4-now-co-same-existing with a parity, + or −, or a 0, across to an other\'s 14-next-possibling',
             152: '- **11** · a next prior: a next moment\'s observing',
             153: '- **12** · with each 4-now-co-same-existing, an is-or-is-not, resolving a prior with the parities a self is observing',
             154: '- **13** · each self of a same-existing-society, a self 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering go from',
             155: '- **14** · within 1-now-existing, parities from 2-now-possibling with each 4-now-co-same-existing, agreeing one, parting 0; within 17-next-existing, others\' 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering gathering, a next 2-now-possibling',
             156: '- **15** · within 1-now-existing, a parity in 14-next-possibling with each 4-now-co-same-existing; within 9-next-co-discovering and 17-next-existing, each list going on, across or along'}
block([CODE_EACH.get(n, ln(n)) for n in range(142, 159)])
para('**Each name, its sides and its prior and next.** Each name\'s resolving with code is its prior and next.')
B += ['| n | Sides | Prior and next |', '|---|---|---|',
 "| 1 | self: a self's resolving | once for one self with one moment, three steps within it, 14-next-possibling, 12-next-co-same-existing and 10-next-co-possibling with 11-next-co-observing |",
 "| 2 | others to self: parities a self is observing from others | others' parities of their prior moment, across with 6-now-co-possibling and 10-next-co-possibling and along with 9-next-co-discovering, a self observing them now |",
 "| 3 | self: a self's prior, pairs of 4-now-co-same-existing with 7-is-now-observing | prior, a self's own, each 4-now-co-same-existing with a parity, a next moment's same-existing of 11-next-co-observing |",
 "| 4 | self and other: each 4-now-co-same-existing between them | now, each 4-now-co-same-existing with which prior is resolving with now |",
 "| 5 | self and others: a self's bi-couplings | next, each of 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering going to a receiving self |",
 "| 6 | self to other: a self's parities across, to an other's 2-now-possibling | parity, an other's next parity with its 2-now-possibling |",
 "| 7 | other to self: each parity a self is observing | each parity, now and prior, co-linear recursioning forward along observing, up numbers, prior to now, with a self's completing |",
 "| 8 | self: a self's next prior | each self's next prior, with 11-next-co-observing this moment and a next moment's 3-is-now-co-observing |",
 "| 9 | self to other: a self's parities along | each parity of 10-next-co-possibling, a 0 among them, going along to a receiving self with 5-now-co-existing, bi-couplings, a self observing it with its 14-next-possibling as its next moment's 2-now-possibling |",
 "| 10 | self to other: a self's parities across, to an other's 14-next-possibling | parity across now, an other's parity next, possibling |",
 "| 11 | self: a self's next prior, a next moment's 3-is-now-co-observing | next prior, odd, same-existing as 3-is-now-co-observing with a next moment, a self's own |",
 "| 12 | self: an is-or-is-not with each 4-now-co-same-existing | now, is-or-is-not, prior and now resolving |",
 "| 13 | each self of a same-existing-society | each of 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering going on, and with a same-existing-society each self going on |",
 "| 14 | others to self: parities from 2-now-possibling with each 4-now-co-same-existing, for a self | now, parities from 2-now-possibling with each 4-now-co-same-existing, others' prior moment, a self observing it with its now, even, others' possibling with a self until with 11-next-co-observing |",
 "| 15 | others to self: each parity in 14-next-possibling | each parity in 14-next-possibling with a 4-now-co-same-existing, resolving with a self's prior parity with 7-is-now-observing |",
 "| 16 | a same-existing-society: all its selves | a same-existing-society now, each self's 8-now-same-existing and its parities next |",
 "| 17 | a same-existing-society: each self's next | a same-existing-society's next moment, a next now, each self's 1-now-existing then 9-next-co-discovering with 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering |", '']
para('**Each name with a between, 8 up and a self as three.** Each name\'s co-sequencing, its place in a self as three, and its bi-coupling and dots.')
B += ['| n | Co-sequencing | A self as three | Bi-coupling, dots |', '|---|---|---|---|',
 "| 1 | a self's entry to a bi-coupling | a self with 2-now-possibling, bi-momentarying, along, a self prior to its first 6-now-co-possibling across, a bi-coupling with 2-now-possibling | |",
 "| 2 | | a self with 1-now-existing, across, its first 6-now-co-possibling across, a bi-coupling, 6-now-co-possibling self to other and 2-now-possibling other to self | with a between, 6-now-co-possibling across from each of a self's others, to that self; a dot of parity's unit square |",
 "| 3 | with a between | rotation 3, 6, 5, 4, its invisible co-intelligencing method, turning with 3-is-now-co-observing | |",
 "| 4 | with a between | rotation 3, 6, 5, 4, inward with 4-now-co-same-existing, to a self's own corus | with a between, a whole ordering between self and other |",
 "| 5 | with a between | rotation 3, 6, 5, 4, outward with 5-now-co-existing | |",
 "| 6 | | rotation 3, 6, 5, 4, inward with 6-now-co-possibling | with a between, a self's parity across, to an other's 2-now-possibling; a dot of parity's unit square |",
 "| 7 | with a between | co-competent self with 8-now-same-existing, along, prior to 8-now-same-existing across | |",
 "| 8 | with a between | co-competent self with 7-is-now-observing, across, prior with 4-now-co-same-existing again, a bi-coupling | with a between, prior with 4-now-co-same-existing again; 2, 4, 6 and 8, a self's span's even names, completing with 8-now-same-existing |",
 "| 9 | | | a unit triangle, along |",
 "| 10 | | | 8 up, a self among selves of its same-existing-society; a dot of parity's unit square |",
 "| 11 | 8 up from 3-is-now-co-observing | | |",
 "| 12 | 8 up from 4-now-co-same-existing | | 8 up, with a bi-coupling, a self of a same-existing-society |",
 "| 13 | 8 up from 5-now-co-existing | | |",
 "| 14 | | | 8 up, the parities in 14-next-possibling with each 4-now-co-same-existing as one, one parity, a 0 for parting, or an empty set; a self's own inverting with 12-next-co-same-existing; a dot of parity's unit square |",
 "| 15 | 8 up from 7-is-now-observing | | |",
 "| 16 | 8 up from 8-now-same-existing | | 8 up, a same-existing-society, each self with its prior and parities, a same-existing-society with a self again; 10, 12, 14 and 16, a same-existing-society's span's even names, completing with 16-next-same-existing |",
 "| 17 | | | a unit triangle, along |", '']
para('**Odd names, now and 8 up with next.** Each odd name of a self\'s span goes 8 up to its next: 3 and 7 with their root again, observing, as 11 and 15; 1 and 5 on as 9 and 13, discovering. Their pairs are a prior a self observes and that self\'s next prior, and a parity a self observes and a parity in 14.')
B += ['| Now | Receiving | Next, 8 up | Giving on |', '|---|---|---|---|',
 '| 1-now-existing | a moment entering | 9-next-co-discovering | each parity going along |',
 '| 3-is-now-co-observing | prior, pairs of 4-now-co-same-existing with 7-is-now-observing | 11-next-co-observing | next prior |',
 '| 5-now-co-existing | each 6, 10 and 9 reaching a self | 13-is-next-discovering | each list going on, each self of a same-existing-society |',
 '| 7-is-now-observing | parity a self is observing | 15-is-next-observing | parity in 14 and going on |', '']

para('**Namings among names.** Each naming with the names it names.')
B += ['- 1-now-existing · 2-now-possibling: bi-momentarying',
      '- 3-is-now-co-observing · 4-now-co-same-existing: co-intelligencing',
      '- 5-now-co-existing: co-competencing',
      '- 6-now-co-possibling: bi-moralizing',
      '- 7-is-now-observing · 8-now-same-existing: co-competent self',
      '- 12-next-co-same-existing: entraining, shape of an unrelationing surface',
      '- 3, 6, 5, 4: rotation',
      '- 1 to 5, each with its own: five dimensions',
      '- 1 to 9: bi-coupling',
      '- 1 to 17: bi-trupling',
      '- 1 to 17, stable-forming: bi-tri-volutioning',
      '- 2, 6, 14 and 10, a unit square of four dots, its across edges 6 to 2 and 10 to 14, its edges 8 apart 2 with 10 and 6 with 14, its empty centre a between; 9 and 17, its two unit triangles, along: parity\'s square and triangles', '']
# ---------- the names' relations
para('**Where each is-or-is-not stands.** Each is-or-is-not with the code, the name it stands on and its dimension.',
     'Eight are with code\'s lines; two are with its loops, each self within 16-next-same-existing and each 4-now-co-same-existing within 3-is-now-co-observing.')
block(data(217, 228))
para('*Dimension*: the four four-cyclings\' observing and same-existing pairs, prior and same (3 · 4), now and same (7 · 8), next and prior (11 · 12) and next and same (15 · 16), co-sequentially forward; and the between, on the bi-folding 4-13-5-12, a bothbothing and co-linearizing.')
para('**Between selves.** Each co name with its one name, and their prefixes.')
B += ['| Co | One | Between selves |', '|---|---|---|',
      '| 6-now-co-possibling, bi-co-bi | 2-now-possibling, bi-co-bi | across, even, its root possibling, its prefix the same |',
      '| 10-next-co-possibling, bi-tri-bi | 14-next-possibling, bi-tri-bi | across, even, its root possibling, its prefix the same |',
      '| 9-next-co-discovering, tri-bi-co | 17-next-existing, co-bi-tri | along, odd, its root discovering, its prefix reversed |', '']
para('**Two-sided, each name.** Each name coming down from a higher name, coming up from a lower one, and eight apart, a now name with a next name.')
block(data(162, 180))
para('**Same-existing through one moment.** The four same-existing names in the order same-existing goes round, each with the observing name beside it, its is-or-is-not.')
block(data(232, 237))
para('**A between, 0.** Each between of 0 with the names at it.')
B += ['| A between, 0 | Names |', '|---|---|',
 "| one between, three names | 12-next-co-same-existing, prior and now agreeing, a between of moments with each 4-now-co-same-existing. 15-is-next-observing, a between of self and other, each parity in 14-next-possibling, a 0 both with an empty set in 14 and with + and − parting. 16-next-same-existing, a between with a same-existing-society, a self observing it with a next moment's 2-now-possibling. A 0 is indifferencing |",
 "| a self observing it, and that self passing over it with 14-next-possibling | 7-is-now-observing, a 0 a self receives with 2-now-possibling, that self passing over it with 14-next-possibling. It is also a 0 with 10-next-co-possibling, its prior same-existing with 11-next-co-observing |",
 "| four across names, a unit square's four dots | 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling, 14-next-possibling, parity's unit square, its empty centre a between. Each parity and each 0 goes across with 6 and 10. A receiving self passes over a 0 with its 14-next-possibling |",
 "| outward of it, names of entry, prior, 4-now-co-same-existing and selves | 1-now-existing, an entry. 3-is-now-co-observing, 8-now-same-existing and 11-next-co-observing, prior: a 4-now-co-same-existing with a prior, a prior + or − from then on. 4-now-co-same-existing. 5-now-co-existing and 13-is-next-discovering, 6, 10 and 9 and, with a same-existing-society, bi-couplings and selves |",
 "| two along names, going along | 9-next-co-discovering and 17-next-existing, each parity and each 0 going along. A receiving self passes over a 0 with its 14-next-possibling, as across |", '']

# ---------- moves and cycles among names
para('**Four four-cyclings and their betweens.** Each four-cycling is its first name, possibling, observing and same-existing: its first name existing at now, 1 and 5, and discovering at next, 9 and 13.',
     'Existing, discovering and observing are odd; possibling and same-existing even. Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is an even name to an odd name.')
block(cyc)
para('**One move, 1 to 8.** Each name of a self\'s span with 8 up, 9 less and 17 less. 9 less is a podal within 1 to 8, and 17 less a podal within 1 to 16. Two moves along a bi-folding bring each name of 1 to 8 to 9 less, a name across that bi-folding. A self\'s span is 1 to 8, and a same-existing-society\'s 9 to 16; 9 and 8 are 17.')
block(data(834, 865))
para('**Four bi-foldings.** Cycles of moves of four steps are bi-foldings. Each goes two folds in turn, 17 less and a move of 8 (4 for the middle two) up or down, and with four steps reaches its first name again. Existing, possibling, observing, same-existing: the stable-forming bi-folding method.',
     'Each move is 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n).')
block(data(573, 589))
para('**Twelve cycles.** Along each cycle odd names are one run and even names one run, of like length: two and two with bi-foldings, three and three with six-cycles, four and four with eight-cycles; its middle two bi-foldings move 4 in place of 8.',
     'The four six-cycles are one six-cycle, each path with its path backward: 1-9-5-12-8-16 and 3-11-7-10-6-14 move 8 up, 4 down, 17 less, 4 down, 8 up and 17 less, and 4-13-5-9-8-12 and 2-15-7-11-6-10 the same moves backward.',
     'The eight-cycle of the four four-cyclings\' ends is 1-9-5-13-4-12-8-16, and of their inward names 2-15-7-11-3-14-6-10.')
B += ['*a*: Names by order: each move 8 up, 8 down, 4 up, 4 down or 17 less  ',
      '*b*: Partner, odd moments: each name exchanging with the one beside it, 1 with 2 to 15 with 16  ',
      '*c*: Partner, even moments: 2 with 3 to 16 with 17. A dash: its partner an empty set among the twelve', '']
block(data(872, 920))
para('**A self\'s four moments of exchanging.**')
block(data(755, 775))
para('A same-existing-society\'s four: 9 to 11, 11 to 13, 13 to 15 and 15 to 17, each opening with its first name and completing with its last, its even name between, 10, 12, 14 and 16; 17-next-existing a next 1-now-existing.')

para('**Each name, three scales.**')
B += [ln(595), ln(596), '']
block(data(597, 682))
para('**Eight 1 to 17s inward.**')
block(data(685, 725))
para('**Eights.** Each eight among names is four twos of names. With a self\'s span, 1 to 8, each two is two names with now. With each eight-cycle, eight even names and eight odd names, each two is a name with now and its name 8 up with next.')
B += ['| Eight | Each of four, twice, with |', '|---|---|',
 '| a self\'s span, 1 to 8 | two names each, with now |',
 '| eight-cycle 1-9-5-13-4-12-8-16 | its end, with now and with next: eight ends of four moments |',
 '| eight-cycle 2-15-7-11-3-14-6-10 | its inward name, with now and with next: eight inward names |',
 '| eight even names | its even, with now and with next, eight 9s of eight 1 to 17s inward |',
 '| eight odd names | its odd, with now and with next |', '']
para('Across names among eights: 2, 6, 10 and 14 are four moments\' even inward names, each on the eight-cycle of inward names 2-15-7-11-3-14-6-10. 9-next-co-discovering opens a third four-cycling, on the eight-cycle of ends 1-9-5-13-4-12-8-16. 17-next-existing is outward of both.')
para('**Fives.** Each side\'s five start with 1: next and same, now and same, prior and same, next and prior, and the between.')
block(data(728, 752))
# ---------- one self, executing
para('**Tables of selves with code\'s stepping.** Each table of selves is its code\'s executing with its own opening.',
     'Its selves step together with 17-next-existing. A 0 in a table is a 0 in a self\'s 10-next-co-possibling. Each receiving self\'s first step, over 2, passes over it. Each self observes the + and − it receives.')
para('**2-now-possibling to 14-next-possibling, one 4-now-co-same-existing.**')
block(data(778, 792))
para('**+ and − alike.** With one 4-now-co-same-existing, resolving is alike for + and −: each cell with + and − exchanging is that cell exchanging, with a prior and with an empty prior. With each line a prior is + or −. With a 0 in 10-next-co-possibling, a self\'s prior is same-existing with 11-next-co-observing.')
para('**One cell, four receivings.** With a prior of one parity, an inverse parity in 14-next-possibling, + and − together, an empty set in 14-next-possibling, and a 0 a self passes over come to one cell: its prior inverts, its inverting in its 10-next-co-possibling and its next prior with 11-next-co-observing. One cell is alike for four receivings. A resolving follows parities.')
para('**One self, one moment.** Each cell: 10-next-co-possibling · a next prior, 11-next-co-observing.')
block(data(799, 809))
para('**With an empty prior, one moment.** Each cell: 10-next-co-possibling · a next prior, 11-next-co-observing. A + or − in 10 is its next prior; with a 0 in 10, its next prior is an empty set. *Empty* is an empty set.')
block(data(1206, 1212))
para('**One self, moment by moment: three ways.** A prior the same each moment; a prior inverting with each moment; a prior inverting once and then the same.',
     'One 4-now-co-same-existing. A self\'s prior, 3-is-now-co-observing, is − first. Receiving each moment:')
block(data(937, 942))

# ---------- selves, executing
para('**Two selves.** Two selves, alike or one parity apart: bi-coupling both ways, bi-coupling one way, or apart.',
     'A, B with their prior, 3-is-now-co-observing, with the first moment. One 4-now-co-same-existing. Parities only from those two.')
B += ['*a*: Receiving its other\'s parity, across or along', '']
block(data(1100, 1132))
para('**Two selves, three moments, five parities.**')
B += ['*a*: A self\'s next prior, 11-next-co-observing, along. Two selves bi-coupling both ways, across or along, each self with a prior parity, parities only from those two, each opening, each moment: six patterns, four with an alike opening and two with an opposite, each moment from the second, and with each pattern the fifth, a self\'s next prior, is the first, an other\'s prior, inverting', '']
block(data(1137, 1167))
para('**Three selves, one line.** A\'s parity goes to B with the first moment only. One 4-now-co-same-existing. B and C each with prior +. B goes along to C.')
B += ['*a*: B\'s next prior, 11-next-co-observing, first moment  ', '*b*: C, each parity, 10-next-co-possibling, moments 1 and 2  ', '*c*: C\'s next prior, 11-next-co-observing, second moment', '']
block(data(1176, 1186))
para('**A spiral of selves.** Each self\'s parity goes along with 9-next-co-discovering to the next self, the last to the first, a co-chaining. One 4-now-co-same-existing. First moment: self 1 with prior −.',
     'Its selves\' parities invert one to the next along. With an odd number the last and the first are alike. Parities only from selves of its spiral.')
B += [mom(ln(950)), mom(ln(951)), '']
block(data(952, 965))
para('**Two moments before, inverting.** With a spiral opening with a prior for each self, each self\'s prior from its third moment on is a prior of a self it receives from two moments before, inverting.',
     'In that spiral each self\'s 10-next-co-possibling is + or − with its first moment, and each 0 of it is between a + or − before and after.')
para('**A spiral opening with an empty prior, one parity, once.** Selves bi-coupling along, last to first, each opening with an empty prior, and + once to a first self with a first moment.',
     'Each cell: selves by their bi-coupling order; · is an empty prior.')
block(data(1191, 1199))
para('**Two spirals beside each other, and bi-coupling across.** Selves of each of two spirals, each opening as a spiral of selves.')
B += [named(mom(ln(n))) for n in range(973, 978)] + ['']
block(data(978, 1026))
para('**A torus of selves.** Each goes along with 9-next-co-discovering to the next along, the last to the first. Each goes across with 10-next-co-possibling to the next across, the last to the first. One 4-now-co-same-existing. First moment: one self with prior −.',
     'Its selves\' parities invert one to the next along and across. With an odd number the last and the first are alike. Parities only from selves of its torus.',
     'Moments to each self\'s parities along and across again, both numbers odd and p the smaller: q with q more than twice p, and 4p with q less than twice p. Either number even: 2. Executing with each p from 1 to 15 and q from p to 21.')
B += [mom(ln(n)) for n in range(1032, 1035)] + ['']
block(data(1035, 1079))
para('**A torus going on, two ways.** Both numbers odd, p the smaller. With q more than twice p, from moment 3p − 1, selves\' pattern with each moment is its pattern before going one self on across q selves.',
     'With q less than twice p, from 3p − 3, its pattern two moments on is its pattern inverting and moving one self on along a spiral of p selves.')
para('**Alike selves, a right spiral.** Selves alike with their others, and two one parity apart, bi-coupling along or across, one 4-now-co-same-existing.',
     'One self\'s prior with each moment, 3-is-now-co-observing, from its first. With alike selves each prior and its next, a pair (x, y), step to (y, −x): a quarter turn with each moment, a right spiral.')
block(data(1084, 1093))
while B and B[-1] == '': B.pop()
open(OUT, 'w', encoding='utf-8').write('\n'.join(B) + '\n')
print(len(B), 'lines')
