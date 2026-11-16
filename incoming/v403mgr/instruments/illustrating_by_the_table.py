"""Exhibit TWENTY-NINE Natural Illustrating in the table: its sixteen ways a next follows from a prior and a now,
its ten at five places, and its seventeen names with their sides, bi-foldings and cycles, each read with the
table of the seventeen names as a surface.
Reads Exhibit TWENTY-NINE Natural Illustrating, Natural Intelligence, Exhibit ONE Natural Resolver, Exhibit
TWENTY-TWO Resolving the Hard Problem Registry and Exhibit TWENTY-EIGHT Equilibria Registry; executes; writes no
file; decides nothing. Each answer is all or none at all: by each way with each joint form, by each order of
four joint forms, by each of ten, by each name.

Use: python3 -I incoming/v403mgr/instruments/illustrating_by_the_table.py <root>        each check
     python3 -I incoming/v403mgr/instruments/illustrating_by_the_table.py <root> csv    one line with each way

Returned at main, 16 November 2026, each check is:
  The sixteen ways. Each sentence of Natural Intelligence 2.4 and of Exhibit TWENTY-NINE 2.2 executed: twelve
  lose their prior, four of them with next from now alone and eight with their prior going on with one value of
  now; six of the eight with a joint form still and two, not both and not either, with each joint form moving,
  three going round and a fourth passing on once; four with their prior whole, joint forms still two, one, one
  and none. A way's four answers are four parities: by how many are +, the ways are 1, 4, 6, 4 and 1, the
  surface's own. The eight with their prior going on with one value of now are the eight with one + or three,
  each an even name, a possibling or a same-existing name, with each of twenty-four orders of the four joint
  forms and with + or - as a parity inverting. The six with two + are three pairs, by prior, by now and by
  agreeing. With the going round ++, +-, --, -+ as the first to the fourth parity, in each of its eight round
  orders: prior and now agreeing and an exclusive or are the surface's two slides, 7 and 13; next as prior, next
  inverting its prior, next as now and next inverting now are its four turns, 3, 5, 9 and 15; next always + and
  next always - are 1 and 11.
  Ten at five places. Exhibit TWENTY-NINE 2.7 and 7.1 name each of ten word for word as Exhibit TWENTY-TWO has
  it; Exhibit TWENTY-EIGHT Equilibria Registry 3.3 has each of ten with a name of 1 to 8 and that name 8 up, each
  as Exhibit TWENTY-TWO has it; 2.7's five pairs, 2 and 10 to 6 and 14, are five of the eight pairs of names, six
  of ten with them, and four of ten, with 1 and 9, 7 and 15, and 8 and 16, with none of the five.
  Seventeen names. 2.8 has each of seventeen names as Exhibit ONE has it; each name's side is Exhibit ONE's own
  with sixteen, and with 7-now-observing Exhibit ONE has other to self and 2.8 others to self. Each of four
  bi-foldings is the four names of one first and one second parity, 8 up the third and fourth parities together
  and seventeen less the fourth alone. The eight-cycle is the eight names of existing, discovering and
  same-existing, each once, the fourth parity inverting with each move and the first with none. The unit
  square's going round is 8 up, a sharing, 8 down, a sharing: each sharing the second and third parities together.
"""
import csv, glob, os, re, sys
from itertools import permutations, product

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
ill = living('Exhibit_TWENTY-NINE_Natural_Illustrating'); ni = living('Natural_Intelligence'); one = living('Exhibit_ONE_Natural_Resolver')
hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry'); eq = living('Exhibit_TWENTY-EIGHT_Equilibria_Registry')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
def part(text, head, level='## '):
    return text.split('\n' + level + head, 1)[1].split('\n## ', 1)[0]

# ---- the surface: sixteen names in reflected order, four parities; fourth and second down, third and first across
def bits(n):                                  # the parities inverting from name 1 to name n, of 1 to 4
    g = (n - 1) ^ ((n - 1) >> 1); return frozenset(k + 1 for k in range(4) if g >> k & 1)
BY_BITS = {bits(n): n for n in range(1, 17)}; assert len(BY_BITS) == 16
ACROSS, DOWN = {1, 3}, {2, 4}
def kind(b):
    if not b: return 'nothing'
    if len(b) == 1: return 'one parity, a fold'
    if len(b) == 2: return 'two parities of one direction, a slide' if b in (ACROSS, DOWN) else 'two parities, one of each direction, a turn'
    return 'three parities, a fold with a slide' if len(b) == 3 else 'four parities, a slide both ways'
def moved(a, b): return bits(a) ^ bits(b)     # the parities inverting from name a to name b

# ---- the sixteen ways: a way gives a next with each joint form (prior, now); a step is (prior, now) to (now, next)
ROUND = [(1, 1), (1, -1), (-1, -1), (-1, 1)]                # the going round as Exhibit TWENTY-NINE 2.2 has it: ++, +-, --, -+
s = lambda f: ''.join('+' if v > 0 else '−' for v in f)
WAYS = [dict(zip(ROUND, v)) for v in product((1, -1), repeat=4)]
def step(w, f): return (f[1], w[f])
def whole(w): return len({step(w, f) for f in ROUND}) == 4          # its prior going on whole: no two joint forms going to one
def from_now(w): return all(w[(1, n)] == w[(-1, n)] for n in (1, -1))
def one_value(w): return sum(w[(1, n)] != w[(-1, n)] for n in (1, -1)) == 1
def still(w): return [f for f in ROUND if step(w, f) == f]
def cycles(w):                                # each cycle of joint forms, and each joint form on no cycle
    on = set(); out = []
    for f in ROUND:
        path = [f]
        while step(w, path[-1]) not in path: path.append(step(w, path[-1]))
        c = path[path.index(step(w, path[-1])):]
        if frozenset(c) not in on: on.add(frozenset(c)); out.append(c)
    return out, [f for f in ROUND if not any(f in c for c in out)]
def plus(w): return frozenset(f for f in ROUND if w[f] == 1)
P = lambda v: {(1, 1): v[0], (1, -1): v[1], (-1, -1): v[2], (-1, 1): v[3]}
PRIOR, NOT_PRIOR = P((1, 1, -1, -1)), P((-1, -1, 1, 1)); NOW, NOT_NOW = P((1, -1, -1, 1)), P((-1, 1, 1, -1))
AGREE, XOR = P((1, -1, 1, -1)), P((-1, 1, -1, 1)); ALWAYS_PLUS, ALWAYS_MINUS = P((1, 1, 1, 1)), P((-1, -1, -1, -1))
NOT_BOTH, NOT_EITHER = P((-1, 1, 1, 1)), P((-1, -1, 1, -1))
WORDS = [(PRIOR, 'next as prior'), (NOT_PRIOR, 'next inverting its prior'), (NOW, 'next as now'), (NOT_NOW, 'next inverting now'),
         (AGREE, 'next as prior and now agreeing'), (XOR, 'next as prior and now parting, an exclusive or'), (ALWAYS_PLUS, 'next always +'), (ALWAYS_MINUS, 'next always −')]
def words(w):
    for v, t in WORDS:
        if v == w: return t
    p = plus(w)
    return f'next + with {s(next(iter(p)))} alone' if len(p) == 1 else f'next − with {s(next(f for f in ROUND if f not in p))} alone'
def name_of(w, order=ROUND, sign=1):          # a way as a name: joint forms in an order the first to fourth parity, a parity inverting with sign
    return BY_BITS[frozenset(k + 1 for k, f in enumerate(order) if w[f] == sign)]
def its_prior(w): return 'going on whole' if whole(w) else 'lost, next from now alone' if from_now(w) else 'going on with one value of now'

ROUNDS8 = [(ROUND[k:] + ROUND[:k])[::d] for k in range(4) for d in (1, -1)]
if WHAT == 'csv':
    wr = csv.writer(sys.stdout, lineterminator='\n')
    wr.writerow(['a way a next follows from a prior and a now', 'next with ++', 'next with +−', 'next with −−', 'next with −+', 'its prior', 'joint forms still', 'its going round',
                 'how many of its four answers are +', 'the names of the sixteen it is, with each of eight round orders and with + or − a parity inverting'])
    for w in sorted(WAYS, key=lambda w: (len(plus(w)), name_of(w))):
        cyc, off = cycles(w)
        wr.writerow([words(w)] + ['+' if w[f] == 1 else '−' for f in ROUND] + [its_prior(w), ' · '.join(s(f) for f in still(w)) or 'none',
                    '; '.join(' to '.join(s(f) for f in c) for c in cyc if len(c) > 1) + ('' if not off else ('; ' if any(len(c) > 1 for c in cyc) else '') + 'passing on once: ' + ' · '.join(s(f) for f in off)),
                    len(plus(w)), ', '.join(map(str, sorted({name_of(w, o, sg) for o in ROUNDS8 for sg in (1, -1)})))])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')

print('The sixteen ways a next follows from a prior and a now: Natural Intelligence 2.4, Exhibit TWENTY-NINE Natural Illustrating 2.2')
n24 = part(ni, '2.4 '); i22 = part(ill, '2.2 ')
lose = [w for w in WAYS if not whole(w)]; keep = [w for w in WAYS if whole(w)]; fn = [w for w in lose if from_now(w)]; ov = [w for w in WAYS if one_value(w)]
say('sixteen ways name a next from a prior and a now' in n24 and '**Twelve lose their prior**, two joint forms going to one' in n24 and '**Four have their prior going on whole**' in n24
    and len(WAYS) == 16 and len(lose) == 12 and len(keep) == 4, 'sixteen ways; twelve lose their prior, two joint forms going to one; four have their prior going on whole')
say('Four of them have next from now alone' in n24 and 'Eight have their prior going on with one value of now and lose it with a second value' in n24
    and len(fn) == 4 and len(ov) == 8 and all(w in lose for w in ov) and not any(w in fn for w in ov) and sorted(map(str, fn + ov)) == sorted(map(str, lose)),
    'of the twelve, four have next from now alone and eight have their prior going on with one value of now and lose it with a second')
moving = [w for w in ov if not still(w)]; pinned = [w for w in ov if still(w)]
say('Two of these eight are with each joint form moving' in n24 and 'goes round three joint forms as one cycle, a fourth passing on to it once' in n24 and 'six of them stopping on a corner of prior, now and next agreeing' in i22
    and len(moving) == 2 and all([len(c) for c in cycles(w)[0]] == [3] and len(cycles(w)[1]) == 1 for w in moving) and sorted(map(str, moving)) == sorted(map(str, [NOT_BOTH, NOT_EITHER]))
    and len(pinned) == 6 and all(set(still(w)) <= {(1, 1), (-1, -1)} for w in pinned),
    'two of the eight are with each joint form moving, three going round as one cycle and a fourth passing on to it once: next − with ++ alone, not both, and next + with −− alone, not either; six stop on a corner of prior, now and next agreeing')
ENT = re.findall(r'(?m)^- \*\*(.+?)\*\* · \*a\* (.+?) · \*b\* (.+)$', n24.split('Each entry: **A way**', 1)[1].split('\n\n**', 1)[0])
NUM = lambda t: 0 if t.startswith('an empty set') else {'one': 1, 'two': 2, 'three': 3}.get(t.split(',')[0].split()[0], 4 if t.startswith('all four') else {'two parting forms': 2}.get(t.split(',')[0], -1))
FOUR = {'Next as prior': PRIOR, 'Next as prior and now agreeing, an exclusive or\'s inversion': AGREE, 'Next as prior and now parting, an exclusive or, parity': XOR, 'Next inverting its prior': NOT_PRIOR}
say(len(ENT) == 4 and sorted(map(str, [FOUR[e[0]] for e in ENT])) == sorted(map(str, keep))
    and all(len(still(FOUR[w])) == NUM(a) and max(len(c) for c in cycles(FOUR[w])[0]) == NUM(b) and not cycles(FOUR[w])[1] for w, a, b in ENT)
    and [NUM(a) for _, a, _ in ENT] == [2, 1, 1, 0] and [NUM(b) for _, _, b in ENT] == [2, 3, 3, 4],
    "the four with their prior whole are Natural Intelligence's four entries, each with its joint forms still and its cycle as written: two and two, one and three, one and three, none and all four")
say('next as prior stops on ++ and −−; prior and now agreeing stops on ++, and an exclusive or on −−' in i22 and 'next inverting its prior goes ++ to +− to −− to −+ and round, each form once, one changing with each step' in i22
    and set(still(PRIOR)) == {(1, 1), (-1, -1)} and still(AGREE) == [(1, 1)] and still(XOR) == [(-1, -1)]
    and [step(NOT_PRIOR, f) for f in ROUND] == ROUND[1:] + ROUND[:1] and all(sum(a != b for a, b in zip(f, step(NOT_PRIOR, f))) == 1 for f in ROUND),
    'next as prior stops on ++ and −−, prior and now agreeing on ++, an exclusive or on −−; next inverting its prior goes ++ to +− to −− to −+ and round, each form once, one changing with each step')
both = [w for w in WAYS if all(w[(1, n)] != w[(-1, n)] for n in (1, -1)) and all(w[(p, 1)] != w[(p, -1)] for p in (1, -1))]
say('fifteen squares have a corner with a pin or lose their prior' in i22 and sum(1 for w in WAYS if still(w) or not whole(w)) == 15 and [w for w in WAYS if whole(w) and not still(w)] == [NOT_PRIOR]
    and sorted(map(str, both)) == sorted(map(str, [AGREE, XOR])),
    'fifteen ways have a joint form still or lose their prior, and one, next inverting its prior, has neither; two answer each single changing with a changing, an exclusive or and its inversion')

print('\nA way as four parities, read with the surface of sixteen names')
by = {k: [w for w in WAYS if len(plus(w)) == k] for k in range(5)}
surf = {k: sorted(n for n in range(1, 17) if len(bits(n)) == k) for k in range(5)}
say([len(by[k]) for k in range(5)] == [1, 4, 6, 4, 1] == [len(surf[k]) for k in range(5)] and surf[1] == [2, 4, 8, 16] and surf[3] == [6, 10, 12, 14] and surf[0] == [1] and surf[4] == [11],
    "by how many of a way's four answers are +, the ways are 1, 4, 6, 4 and 1, as the surface's names by parities inverting from 1: nothing 1; one, 2, 4, 8, 16; two, 3, 5, 7, 9, 13, 15; three, 6, 10, 12, 14; four, 11")
ORD = list(permutations(ROUND)); EVEN = set(range(2, 17, 2))
say(sorted(map(str, ov)) == sorted(map(str, by[1] + by[3])) and len(ORD) == 24
    and all({name_of(w, o, sg) for w in ov} == EVEN and {name_of(w, o, sg) for w in WAYS if w not in ov} == set(range(1, 17, 2)) for o in ORD for sg in (1, -1))
    and all(re.search(r'possibling|same-existing', NAME[n]) for n in EVEN) and not any(re.search(r'possibling|same-existing', NAME[n]) for n in range(1, 17, 2)),
    'the eight with their prior going on with one value of now are the eight with one + or three: with each of twenty-four orders of four joint forms as four parities, and + or − a parity inverting, each is an even name, a possibling or a same-existing name; the four from now alone and the four whole are the eight odd names, existing, discovering and observing')
PART = {'by prior': ({(1, 1), (1, -1)}, {(-1, -1), (-1, 1)}), 'by now': ({(1, 1), (-1, 1)}, {(1, -1), (-1, -1)}), 'by agreeing': ({(1, 1), (-1, -1)}, {(1, -1), (-1, 1)})}
pair = {k: [w for w in by[2] if set(plus(w)) in v] for k, v in PART.items()}
say(all(len(v) == 2 for v in pair.values()) and sum(len(v) for v in pair.values()) == 6
    and sorted(map(str, pair['by prior'])) == sorted(map(str, [PRIOR, NOT_PRIOR])) and sorted(map(str, pair['by now'])) == sorted(map(str, [NOW, NOT_NOW])) and sorted(map(str, pair['by agreeing'])) == sorted(map(str, [AGREE, XOR]))
    and sorted(map(str, keep)) == sorted(map(str, pair['by prior'] + pair['by agreeing'])) and sorted(map(str, fn)) == sorted(map(str, pair['by now'] + by[0] + by[4])),
    'the six with two + are three pairs, a pair with each parting of four joint forms as two and two: by prior, next as prior and next inverting its prior; by now, next as now and next inverting now; by agreeing, prior and now agreeing and an exclusive or. The four whole are the pairs by prior and by agreeing; the four from now alone, the pair by now with next always + and next always −')
ROUNDS = [(ROUND[k:] + ROUND[:k])[::d] for k in range(4) for d in (1, -1)]
say(len({tuple(o) for o in ROUNDS}) == 8 and all({name_of(AGREE, o, sg), name_of(XOR, o, sg)} == {7, 13} and {name_of(w, o, sg) for w in (PRIOR, NOT_PRIOR, NOW, NOT_NOW)} == {3, 5, 9, 15}
                                              and {name_of(ALWAYS_PLUS, o, sg), name_of(ALWAYS_MINUS, o, sg)} == {1, 11} for o in ROUNDS for sg in (1, -1))
    and all(kind(bits(n)).endswith('a slide') for n in (7, 13)) and all(kind(bits(n)).endswith('a turn') for n in (3, 5, 9, 15)),
    "with the going round ++, +−, −−, −+ as the first to the fourth parity, in each of its eight round orders and with + or − a parity inverting: prior and now agreeing and an exclusive or are the surface's two slides, 7 and 13; next as prior, next inverting its prior, next as now and next inverting now its four turns, 3, 5, 9 and 15; next always + and next always −, 1 and 11")
print('      each way with the names of the sixteen it is, with each of eight round orders and with + or − a parity inverting:')
for w in sorted(WAYS, key=lambda w: (len(plus(w)), name_of(w))): print(f"        {words(w)} · {', '.join(map(str, sorted({name_of(w, o, sg) for o in ROUNDS for sg in (1, -1)})))}")

print('\nTen at five places: Exhibit TWENTY-NINE 2.7 and 7.1, Exhibit TWENTY-EIGHT Equilibria Registry 3.3, Exhibit TWENTY-TWO')
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10
i27 = part(ill, '2.7 '); i71 = part(ill, '7.1 ')
ten27 = re.findall(r'(an? [a-z-]+ fixing [a-z ]+?)[,.]', i27.split('each has its one name:', 1)[1].split('\n', 1)[0])
ten71 = [t[0].lower() + t[1:] for t in re.findall(r'(?m)^- \*\*(.+?)\.\*\*', i71)]
say(len(ten27) == 10 and set(ten27) == set(SEAT) and ten71 == ten27, "2.7 names each of ten word for word as Exhibit TWENTY-TWO has it, and 7.1's ten drawings are the same ten in the same order")
e33 = part(eq, '3.3 ')
EQ = {what: (int(a), int(b)) for line in re.findall(r'(?m)^  - \*b\* (.+)$', e33) for whats, a, b in re.findall(r'((?:an? [a-z-]+ fixing [a-z ]+?(?: and )?)+), with (\d+) · (\d+)', line) for what in whats.split(' and ')}
say(len(EQ) == 10 and EQ == SEAT and all(b == a + 8 and 1 <= a <= 8 for a, b in EQ.values()) and len(set(EQ.values())) == 8,
    "Exhibit TWENTY-EIGHT Equilibria Registry 3.3 has each of ten with a name of 1 to 8 and that name 8 up, eight pairs of names, each of ten with the two names Exhibit TWENTY-TWO has it with")
m = re.search(r"Equilibria Registry 3\.3: ten pair with five names 2 to 6, .*?with Exhibit ONE's names ((?:\d+ and \d+(?:, )?)+)", i27)
five = [tuple(map(int, x)) for x in re.findall(r'(\d+) and (\d+)', m.group(1))] if m else []
on = [t for t in SEAT if SEAT[t] in five]; off = [t for t in SEAT if SEAT[t] not in five]
say(five == [(2, 10), (3, 11), (4, 12), (5, 13), (6, 14)] and all(p in set(SEAT.values()) for p in five) and len(on) == 6 and len(off) == 4
    and sorted({SEAT[t] for t in off}) == [(1, 9), (7, 15), (8, 16)],
    "2.7 has Equilibria Registry 3.3 as ten with five names 2 to 6, and its five pairs, 2 and 10 to 6 and 14, are five of the Registry's eight pairs of names: six of ten are with them, and four of ten, with 1 and 9, 7 and 15, and 8 and 16, are with none of the five")
print(f"      with a place of the five: {'; '.join(on)}\n      with none: {'; '.join(f'{t}, {SEAT[t][0]} and {SEAT[t][1]}' for t in off)}")

print('\nSeventeen names, their sides, bi-foldings and cycles: Exhibit TWENTY-NINE 2.8 and 2.3, Exhibit ONE Natural Resolver')
i28 = part(ill, '2.8 '); i23 = part(ill, '2.3 ')
listed = re.findall(r'(\d+-(?:now|next)-[a-z-]+)', i28.split('seventeen names of Exhibit ONE', 1)[1].split(', each its number', 1)[0])
say(listed == [NAME[n] for n in range(1, 18)], '2.8 has each of seventeen names as Exhibit ONE has it, in sequence')
SIDE = {int(n): sd for n, sd in re.findall(r'(?m)^\*\*(\d+)\*\* · .+\n- \*Parity, span\*: .+\n- \*Sides\*: (.+)$', one)}; assert sorted(SIDE) == list(range(1, 18))
own = {n: SIDE[n].split(':')[0] for n in SIDE}
sent = i28.split("each name's sides: ", 1)[1].split('. ', 1)[0]
SAID = {int(n): re.sub(r'^a self$', 'self', g.strip()) for nums, g in re.findall(r'((?:\d+(?:, | and )?)+) ([a-z -]+?)(?:;|$)', sent) for n in re.findall(r'\d+', nums)}
part_ = sorted(n for n in SAID if SAID[n] != own[n])
say(sorted(SAID) == list(range(1, 18)) and part_ == [7] and own[7] == 'other to self' and SAID[7] == 'others to self',
    "each name's side in 2.8 is Exhibit ONE's own with sixteen of seventeen; with 7-now-observing Exhibit ONE has other to self and 2.8 has others to self")
BF = [list(map(int, x.split('-'))) for x in re.findall(r'\b(\d+-\d+-\d+-\d+)\b', i28.split('Four bi-foldings, ', 1)[1].split(', each go eight up', 1)[0])]
ring = lambda c: list(zip(c, c[1:] + c[:1]))
say(len(BF) == 4 and sorted(n for c in BF for n in c) == list(range(1, 17)) and all(all((abs(a - b) == 8) != (a + b == 17) for a, b in ring(c)) for c in BF)
    and all(moved(a, b) == ({3, 4} if abs(a - b) == 8 else {4}) for c in BF for a, b in ring(c))
    and all(len({(1 in bits(n), 2 in bits(n)) for n in c}) == 1 for c in BF)
    and len({frozenset((1 in bits(n), 2 in bits(n)) for n in c) for c in BF}) == 4,
    'each of four bi-foldings goes eight up and seventeen less by turns, sixteen names each once: 8 up is the third and fourth parities together, seventeen less the fourth alone, and each bi-folding is the four names of one first and one second parity, the four bi-foldings the four such pairs')
six = list(map(int, re.search(r'a six-cycle ((?:\d+-)+\d+)', i28).group(1).split('-'))); eight = list(map(int, re.search(r'an eight-cycle ((?:\d+-)+\d+)', i28).group(1).split('-')))
ROOT8 = sorted(n for n in range(1, 17) if not re.search(r'possibling|observing', NAME[n]))
say(len(six) == 6 and len(eight) == 8 and sorted(eight) == ROOT8 == sorted(n for n in range(1, 17) if 1 not in bits(n)) and set(six) < set(eight)
    and all(4 in moved(a, b) and 1 not in moved(a, b) for c in (six, eight) for a, b in ring(c))
    and [sorted(moved(a, b)) for a, b in ring(eight)] == [[3, 4], [2, 4], [3, 4], [4]] * 2,
    'the eight-cycle is the eight names of existing, discovering and same-existing, each once, the names with the first parity as name 1 has it; with each move of the six-cycle and of the eight-cycle the fourth parity inverts and the first does not; the eight-cycle is 8 up, 4 less, 8 up and seventeen less, twice')
sq = list(map(int, re.search(r'Going round, ((?:\d+ to )+\d+)', i23).group(1).split(' to ')))[:-1]
say(sq == [2, 10, 14, 6] and sorted(sq) == sorted(n for n in range(1, 17) if 'possibling' in NAME[n]) and not any(sorted(sq) == sorted(c) for c in BF)
    and [sorted(moved(a, b)) for a, b in ring(sq)] == [[3, 4], [2, 3], [3, 4], [2, 3]] and all(1 in bits(n) for n in sq),
    "the unit square's going round, 2 to 10 to 14 to 6 to 2, is the four possibling names and none of four bi-foldings: 8 up, a sharing, 8 down, a sharing, 8 up and 8 down the third and fourth parities together and each sharing the second and third together")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
