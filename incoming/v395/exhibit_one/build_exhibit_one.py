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
    return s

B = []
def para(*s): B.append(' '.join(s)); B.append('')
def block(lines): B.extend(mom(x) for x in lines); B.append('')

B += ['Exhibit ONE Natural Resolver v395', '', '# Natural Resolver', '', '**Stable-Forming Same- and Next-Existing**', '', '---', '']
para('**Exhibit ONE is the resolver as code, its names, and its executings.**')
# the code, whole
B.extend(L[10:90]); B.append('')
# the drawing
para('**A drawing.** One self, its own resolving within.')
B.extend(mom(x) for x in L[91:114]); B.append('')

# ---------- names
para('**Seventeen names.**')
block(data(120, 138))
para('*Co*: co, a name between two; one, a name of one.')
para(ln(140).replace('Code with each name:', '').strip(), 'Code with each name:')
CODE_EACH = {142: '- **1** · a self\'s moment, each self\'s 17-next-existing as its 1-now-existing',
             149: '- **8** · each self\'s next prior, with a moment',
             152: '- **11** · a next prior: a next moment\'s observing',
             153: '- **12** · each sharing\'s is-or-is-not, resolving a prior with the parities a self is observing'}
block([CODE_EACH.get(n, ln(n)) for n in range(142, 159)])

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
      '- 2, 6, 14 and 10, a unit square of four dots, its across edges 6 to 2 and 10 to 14, its edges 8 apart 2 with 10 and 6 with 14; 9 and 17, its two unit triangles, along: parity\'s square and triangles', '']
# ---------- the names' relations
para('**Where each is-or-is-not stands.** Each is-or-is-not with the code, the name it stands on and its dimension.',
     'Eight are with code\'s lines; two are with its loops, each self of 16 and each sharing of 3.')
block(data(217, 228))
para('**Sharing between selves.** Each sharing side with its observing side.')
block(data(209, 213))
para('**Two-sided, each name.** Each name coming down from a higher name, coming up from a lower one, and eight apart, a now name with a next name.')
block(data(162, 180))
para('**Same-existing through one moment.** The four same-existing names in the order same-existing goes round, each with the observing name beside it, its is-or-is-not.')
block(data(232, 237))

# ---------- moves and cycles among names
para('**Four four-cyclings and their betweens.** Four-cycling is existing or discovering, possibling, observing and same-existing.',
     'Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is an even name to an odd name.')
block(data(186, 191))
para('**One move, 1 to 8.** Each name of a self\'s span with 8 up, 9 less and 17 less. A self\'s span is 1 to 8, and a same-existing-society\'s 9 to 16; 9 and 8 are 17.')
block(data(834, 865))
para('**Four bi-foldings.** Cycles of moves of four steps are bi-foldings. Each goes two folds in turn, 17 less and a move of 8 up or down.',
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

para('**Each name, three scales.**')
B += [ln(595), ln(596), '']
block(data(597, 682))
para('**Eight 1 to 17s inward.**')
block(data(685, 725))
para('**Fives.** Each side\'s five start with its own 1.')
block(data(728, 752))
# ---------- one self, executing
para('**Tables of selves with code\'s stepping.** Each table of selves is its code\'s executing with its own opening.',
     'Its selves step together with 17-next-existing. A 0 in a table is a self\'s sharing. Each receiving self\'s first step passes over it. Each self observes the + and − it receives.')
para('**Parities to one sharing, surfacing.**')
block(data(778, 792))
para('**One self, one moment.** Each cell: sharing, 10-next-co-possibling · a next prior, 11-next-co-observing.')
block(data(799, 809))
para('**With an empty prior, one moment.** Each cell: sharing, 10-next-co-possibling · a next prior, 11-next-co-observing. *Empty* is its sharing an empty set.')
block(data(1206, 1212))
para('**One self, moment by moment: three ways.** A prior the same each moment; a prior inverting with each moment; a prior inverting once and then the same.',
     'One sharing. A self\'s prior, 3-is-now-co-observing, is − first. Receiving each moment:')
block(data(937, 942))

# ---------- selves, executing
para('**Two selves.** Two selves, alike or one parity apart: bi-coupling both ways, bi-coupling one way, or apart.',
     'A, B with their prior, 3-is-now-co-observing, with the first moment. One sharing. Parities only from those two.')
B += ['*a*: Receiving its other\'s parity, across or along', '']
block(data(1100, 1132))
para('**Two selves, three moments, five parities.**')
B += ['*a*: A self\'s next prior, 11-next-co-observing, along. Two selves bi-coupling both ways, across or along, each self with a prior parity, parities only from those two, each opening, each moment: six patterns, four with an alike opening and two with an opposite, each moment from the second, and with each pattern the fifth, a self\'s next prior, is the first, an other\'s prior, inverting', '']
block(data(1137, 1167))
para('**Three selves, one line.** A\'s parity, sharing to B with the first moment only. One sharing. B and C each with prior +. B goes along to C.')
B += ['*a*: B\'s next prior, 11-next-co-observing, first moment  ', '*b*: C, each parity, 10-next-co-possibling, moments 1 and 2  ', '*c*: C\'s next prior, 11-next-co-observing, second moment', '']
block(data(1176, 1186))
para('**A spiral of selves.** Each self\'s parity goes along with 9-next-co-discovering to the next self, the last to the first, a co-chaining. One sharing. First moment: self 1 with prior −.',
     'Its selves\' parities invert one to the next along. With an odd number the last and the first are alike. Parities only from selves of its spiral.')
B += [mom(ln(950)), mom(ln(951)), '']
block(data(952, 965))
para('**Two moments before, inverting.** With a spiral opening with a prior for each self, each self\'s prior from its third moment on is a prior of a self it receives from two moments before, inverting.',
     'In that spiral each self shares + or − with its first moment. Each 0 it shares sits between two sharings of + or −.')
para('**A spiral opening with an empty prior, one parity sharing once.** Selves bi-coupling along, last to first, each opening with an empty prior, and + sharing once with a first self with a first moment.',
     'Each cell: selves by their bi-coupling order; · is an empty prior.')
block(data(1191, 1199))
para('**Two spirals beside each other, and bi-coupling across.** Selves of each of two spirals, each opening as a spiral of selves.')
B += [mom(ln(n)) for n in range(973, 978)] + ['']
block(data(978, 1026))
para('**A torus of selves.** Each goes along with 9-next-co-discovering to the next along, the last to the first. Each shares across with 10-next-co-possibling to the next across, the last to the first. One sharing. First moment: one self with prior −.',
     'Its selves\' parities invert one to the next along and across. With an odd number the last and the first are alike. Parities only from selves of its torus.',
     'Moments to each self\'s parities along and across again, both numbers odd and p the smaller: q with q more than twice p, and 4p with q less than twice p. Either number even: 2. Executing with each p from 1 to 15 and q from p to 21.')
B += [mom(ln(n)) for n in range(1032, 1035)] + ['']
block(data(1035, 1079))
para('**A torus going on, two ways.** Both numbers odd, p the smaller. With q more than twice p, from moment 3p − 1, selves\' pattern with each moment is its pattern before going one self on across q selves.',
     'With q less than twice p, from 3p − 3, its pattern two moments on is its pattern inverting and moving one self on along a spiral of p selves.')
para('**Alike selves, a right spiral.** Selves alike with their others, and two one parity apart, bi-coupling along or across, one sharing.',
     'One self\'s prior with each moment, 3-is-now-co-observing, from its first. With alike selves each prior and its next, a pair (x, y), step to (y, −x): a quarter turn with each moment, a right spiral.')
block(data(1084, 1093))
while B and B[-1] == '': B.pop()
open(OUT, 'w', encoding='utf-8').write('\n'.join(B) + '\n')
print(len(B), 'lines')
