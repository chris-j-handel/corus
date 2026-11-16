"""The sixty-four codons of a field's genetic code on the surface's eight by eight, a 1 to 65: each base two
parities, each two codons next to each other one parity apart.
Reads Exhibit ONE Natural Resolver, Exhibit FOUR Natural Mathematics, Exhibit SIXTEEN Natural Chemistry and
Exhibit SEVENTEEN Natural Biology; executes; writes no file; decides nothing. Each answer is all or none at all,
by each codon of sixty-four and by each square of sixteen.

Use: python3 -I incoming/v403mgr/instruments/codons_on_the_surface.py <root>         each check
     python3 -I incoming/v403mgr/instruments/codons_on_the_surface.py <root> csv     one line with each codon
     python3 -I incoming/v403mgr/instruments/codons_on_the_surface.py <root> json    the eight by eight, for a sheet

The logic. Exhibit SEVENTEEN Natural Biology: a codon has six binary sharings, 2⁶ = 4³ = 64 codons, four bases,
twenty amino acids. Exhibit FOUR Natural Mathematics: the reflected order, one parity changing with each number;
with two parities a cycle is four. Exhibit SIXTEEN Natural Chemistry has the genetic code as another table with
another substrate, a table-to-table pattern two drawings; here the code is read by the names' own logic, each
answer an is or an is-not. A field's table, the standard genetic code, is nature's observing here, written whole
in this instrument, in a field's own order of bases, U, C, A, G.

Returned at main, 16 November 2026, each check is:
  Sixty-four codons, twenty amino acids and a stop. A field's order U, C, A, G is the reflected order of two
  parities, a pyrimidine or a purine, and keto or amino, one changing from each base to its next and round.
  Three moves among four bases, U with C and A with G, U with G and C with A, U with A and C with G: each comes
  to its base again after two, each two are the third, and each changes two of three parities and not the
  third, a pyrimidine or a purine, keto or amino, weak or strong; weak or strong is the two the same or not.
  On the eight by eight each two codons next to each other, along, across and round each edge, are one base
  and one parity apart; each square of four is the four codons of two first bases, gone round U, C, A, G.
  In the third place U with C is the same amino acid with each of sixteen squares. A with G parts with two
  squares alone: methionine and tryptophan, the two amino acids with one codon alone.
  Eight squares are whole, one amino acid, and eight parted. A square is whole with two of three: its first
  base strong, its second base strong, its second base a pyrimidine.
  Of the three moves with the first two bases together, one alone brings each whole square onto a parted and
  each parted onto a whole: U with G and C with A. On the surface it is two folds, one and then the other:
  65 less, and 17 less with each sixteen. With the sixteen squares as the sixteen names it pairs 1 with 13,
  5 with 9, 2 with 14, 6 with 10, 3 with 15, 7 with 11, 4 with 16 and 8 with 12.
"""
import csv, glob, itertools, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); four = living('Exhibit_FOUR_Natural_Mathematics')
chem = living('Exhibit_SIXTEEN_Natural_Chemistry'); bio = living('Exhibit_SEVENTEEN_Natural_Biology')
for text, said in ((bio, 'Codon has six binary sharings, across and both ways — 2⁶ = 4³ = 64 codons'), (bio, 'Four bases are alphabet, twenty amino acids elements'),
                   (chem, 'a table-to-table pattern is two drawings'), (four, 'With two parities a cycle is four'), (four, 'the reflected binary code')):
    assert said in text, said
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))

# --- a field's table, the standard genetic code, in a field's own order of bases U, C, A, G: first, second, third
ORDER = 'UCAG'
TABLE = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
SAID = {'F': 'phenylalanine', 'L': 'leucine', 'S': 'serine', 'Y': 'tyrosine', '*': 'stop', 'C': 'cysteine', 'W': 'tryptophan', 'P': 'proline', 'H': 'histidine',
        'Q': 'glutamine', 'R': 'arginine', 'I': 'isoleucine', 'M': 'methionine', 'T': 'threonine', 'N': 'asparagine', 'K': 'lysine', 'V': 'valine', 'A': 'alanine',
        'D': 'aspartate', 'E': 'glutamate', 'G': 'glycine'}
CODE = {a + b + c: TABLE[16 * i + 4 * j + k] for i, a in enumerate(ORDER) for j, b in enumerate(ORDER) for k, c in enumerate(ORDER)}

# --- each base two parities: a purine, 1, or a pyrimidine, 0; amino, 1, or keto, 0
PQ = {'U': (0, 0), 'C': (0, 1), 'A': (1, 1), 'G': (1, 0)}; BASE = {v: k for k, v in PQ.items()}
strong = lambda b: PQ[b][0] ^ PQ[b][1]                       # weak or strong: the two the same or not
MOVES = {'U with C and A with G': lambda b: BASE[(PQ[b][0], 1 - PQ[b][1])],
         'U with G and C with A': lambda b: BASE[(1 - PQ[b][0], PQ[b][1])],
         'U with A and C with G': lambda b: BASE[(1 - PQ[b][0], 1 - PQ[b][1])]}
PARITIES = {'a pyrimidine or a purine': lambda b: PQ[b][0], 'keto or amino': lambda b: PQ[b][1], 'weak or strong': strong}

# --- the surface's eight by eight, the numbers 1 to 64 by the reflected order, three parities down and three across
G = lambda n: (n - 1) ^ ((n - 1) >> 1)
def index(bits):
    i = 0
    for b in bits: i = i * 2 + (b ^ (i & 1))
    return i
def codon_of(n):                                             # a number's six parities, two with each base
    g = [(G(n) >> k) & 1 for k in (5, 4, 3, 2, 1, 0)]
    return ''.join(BASE[(g[i], g[i + 1])] for i in (0, 2, 4))
PLACE = {n: (index([(G(n) >> k) & 1 for k in (5, 3, 1)]), index([(G(n) >> k) & 1 for k in (4, 2, 0)])) for n in range(1, 65)}
AT = {v: n for n, v in PLACE.items()}; NUMBER = {codon_of(n): n for n in range(1, 65)}
assert len(AT) == 64 and sorted(NUMBER) == sorted(CODE)
whole = {a + b: len({CODE[a + b + c] for c in ORDER}) == 1 for a in ORDER for b in ORDER}
three = lambda sq: strong(sq[0]) + strong(sq[1]) + (1 - PQ[sq[1]][0])      # first strong, second strong, second a pyrimidine
rumer = MOVES['U with G and C with A']

if WHAT == 'json':
    json.dump({'eight by eight': [[{'number': AT[(r, c)], 'codon': codon_of(AT[(r, c)]), 'amino acid': SAID[CODE[codon_of(AT[(r, c)])]], 'whole': whole[codon_of(AT[(r, c)])[:2]]}
                                   for c in range(8)] for r in range(8)]}, sys.stdout, ensure_ascii=False); sys.exit()
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['its number on the surface', 'codon', 'amino acid', 'its square of four, its first two bases', 'its square, whole or parted',
                'of three, first base strong, second base strong, second base a pyrimidine', 'its line down, of eight', 'its line across, of eight', "its square's name, of the sixteen squares", 'its name, sixteen on',
                "its place in a field's table, of sixty-four", 'with U and C exchanged in its third place', 'with A and G exchanged in its third place',
                'the codon two folds bring it onto, 65 less and 17 less with each sixteen', "that codon's square, whole or parted"])
    for n in range(1, 65):
        c = codon_of(n); t = MOVES['U with C and A with G'](c[2]); o = c[:2] + t; f = rumer(c[0]) + rumer(c[1]) + c[2]
        same = 'the same amino acid' if CODE[o] == CODE[c] else f'{SAID[CODE[c]]} from {SAID[CODE[o]]}'
        w.writerow([n, c, SAID[CODE[c]], c[:2], 'whole' if whole[c[:2]] else 'parted', three(c[:2]), PLACE[n][0] + 1, PLACE[n][1] + 1, NAME[(n - 1) // 4 + 1], NAME[(n - 1) % 16 + 1],
                    16 * ORDER.index(c[0]) + 4 * ORDER.index(c[1]) + ORDER.index(c[2]) + 1, same if c[2] in 'UC' else '', same if c[2] in 'AG' else '', f, 'whole' if whole[f[:2]] else 'parted'])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print("A field's genetic code on the surface's eight by eight:")
say(len(CODE) == 64 and len(set(CODE.values()) - {'*'}) == 20 and '*' in CODE.values(), 'sixty-four codons, twenty amino acids and a stop')
say(all(sum(x != y for x, y in zip(PQ[ORDER[i]], PQ[ORDER[(i + 1) % 4]])) == 1 for i in range(4)) and len(set(PQ.values())) == 4,
    "a field's order U, C, A, G is the reflected order of two parities, a pyrimidine or a purine, and keto or amino, one changing from each base to its next and round: a cycle of four")
print('Three moves among four bases:')
say(all(m(m(b)) == b and m(b) != b for m in MOVES.values() for b in ORDER) and all(MOVES[y](MOVES[x](b)) == MOVES[z](b) for x, y, z in itertools.permutations(MOVES) for b in ORDER),
    'each comes to its base again after two, with no base with itself, and each two of them, one and then the other, either first, are the third')
unchanged = {name: [p for p, f in PARITIES.items() if all(f(m(b)) == f(b) for b in ORDER)] for name, m in MOVES.items()}
say(all(len(v) == 1 for v in unchanged.values()) and len({v[0] for v in unchanged.values()}) == 3
    and all(all(f(m(b)) != f(b) for b in ORDER) for name, m in MOVES.items() for p, f in PARITIES.items() if p not in unchanged[name]),
    'three parities, a pyrimidine or a purine, keto or amino, weak or strong, are the three partings of four bases two and two; each move changes two of them and not the third')
for name in MOVES: print(f'      {name}: not changing {unchanged[name][0]}')
print('On the eight by eight:')
def one_apart(a, b):
    d = [i for i in range(3) if a[i] != b[i]]
    return len(d) == 1 and sum(x != y for x, y in zip(PQ[a[d[0]]], PQ[b[d[0]]])) == 1
say(all(one_apart(codon_of(AT[(r, c)]), codon_of(AT[(r, (c + 1) % 8)])) and one_apart(codon_of(AT[(r, c)]), codon_of(AT[((r + 1) % 8, c)])) for r in range(8) for c in range(8)),
    'each two codons next to each other, along, across and round each edge, are one base and one parity apart')
squares = {}
for (r, c), n in AT.items(): squares.setdefault((r // 2, c // 2), []).append(codon_of(n))
say(all(len({x[:2] for x in v}) == 1 and {x[2] for x in v} == set(ORDER) for v in squares.values())
    and all([codon_of(4 * k + i)[2] for i in (1, 2, 3, 4)] in (list('UCAG'), list('GACU')) for k in range(16)),
    'each square of four is the four codons of two first bases, a four-cycling, gone round U, C, A, G, and its next square the other way round')
say(all(CODE[sq + 'U'] == CODE[sq + 'C'] for sq in whole), 'in the third place U with C is the same amino acid, with each of sixteen squares')
parting = sorted(sq for sq in whole if CODE[sq + 'A'] != CODE[sq + 'G'])
alone = sorted(SAID[a] for a in set(CODE.values()) if list(CODE.values()).count(a) == 1)
say(parting == ['AU', 'UG'] and alone == ['methionine', 'tryptophan'] and {CODE['AUG'], CODE['UGG']} == {'M', 'W'},
    'in the third place A with G parts with two squares alone, AUA from AUG and UGA from UGG: methionine and tryptophan, the two amino acids with one codon alone')
say(sum(whole.values()) == 8 and all(whole[sq] == (three(sq) >= 2) for sq in whole),
    'eight squares are whole, one amino acid, and eight parted; a square is whole with two of three, its first base strong, its second base strong, its second base a pyrimidine, and parted with fewer')
print('      whole:', ' '.join(sorted(sq for sq in whole if whole[sq])), '· parted:', ' '.join(sorted(sq for sq in whole if not whole[sq])))
flips = {name: all(whole[m(sq[0]) + m(sq[1])] != whole[sq] for sq in whole) for name, m in MOVES.items()}
say(flips == {'U with C and A with G': False, 'U with G and C with A': True, 'U with A and C with G': False},
    'of the three moves with the first two bases together, one alone brings each whole square onto a parted and each parted onto a whole: U with G and C with A')
fold = lambda n, j: ((n - 1) ^ (2 ** j - 1)) + 1           # 2 to the j and one, less, with each 2 to the j
say(all(codon_of(fold(fold(n, 6), 4)) == rumer(codon_of(n)[0]) + rumer(codon_of(n)[1]) + codon_of(n)[2] for n in range(1, 65))
    and all(fold(n, 6) == 65 - n and fold(n, 4) == 16 * (2 * ((n - 1) // 16)) + 17 - n for n in range(1, 65)),
    'on the surface it is two folds, one and then the other, 65 less, and 17 less with each sixteen: a pyrimidine or a purine changing with the first base and with the second')
sq_name = {codon_of(4 * m)[:2]: m for m in range(1, 17)}                    # a square's name: its four numbers' four-cycling, of sixteen
pairs = {frozenset((sq_name[sq], sq_name[rumer(sq[0]) + rumer(sq[1])])) for sq in whole}
say(sorted(sq_name[sq] for sq in whole if whole[sq]) == [2, 5, 7, 8, 10, 13, 15, 16] and
    pairs == {frozenset(p) for p in ((1, 13), (5, 9), (2, 14), (6, 10), (3, 15), (7, 11), (4, 16), (8, 12))},
    "with the sixteen squares as the sixteen names, by a field's order, the whole squares are 2, 5, 7, 8, 10, 13, 15 and 16, and the move pairs 1 with 13, 5 with 9, 2 with 14, 6 with 10, 3 with 15, 7 with 11, 4 with 16 and 8 with 12: the fourth and the second parities changing together")
say(all(codon_of(fold(n, 1)) == codon_of(n)[:2] + MOVES['U with C and A with G'](codon_of(n)[2]) and fold(n, 1) == 2 * (2 * ((n - 1) // 2)) + 3 - n for n in range(1, 65))
    and {frozenset((codon_of(n), codon_of(fold(n, 1)))) for n in range(1, 65) if CODE[codon_of(n)] != CODE[codon_of(fold(n, 1))]} == {frozenset(('AUA', 'AUG')), frozenset(('UGA', 'UGG'))},
    '3 less, with each two, the first parity changing alone, changes no amino acid but with two twos: AUA with AUG, and UGA with UGG')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
