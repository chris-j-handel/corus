"""Each of the one hundred eighteen elements by its place: its name sixteen on, its span by a field's filling
order, and that span's length, a possibling name of the seventeen.
Reads Exhibit ONE Natural Resolver, Exhibit THREE Natural Numbers and Exhibit SIXTEEN Natural Chemistry;
executes; writes no file; decides nothing. Each answer is all or none at all, by each element and by each span.

Use: python3 -I incoming/v403mgr/instruments/elements_by_their_place.py <root>         each check
     python3 -I incoming/v403mgr/instruments/elements_by_their_place.py <root> csv     one line with each element
     python3 -I incoming/v403mgr/instruments/elements_by_their_place.py <root> json    the table's seven rows, for a sheet

The logic. Exhibit SIXTEEN Natural Chemistry: elements have doubling, each odd twice; their rows are 2, 8, 8, 18,
18, 32, 32, closing with 2, 10, 18, 36, 54, 86 and 118; a field observes an 8s pair with 119 and 120. Exhibit ONE
Natural Resolver: a unit square of four dots, 2-now-possibling, 6-now-co-possibling, 14-next-possibling and
10-next-co-possibling, its two across edges 6 to 2 and 10 to 14, its two edges 8 apart 2 with 10 and 6 with 14.
A field's filling order, written whole here: each span by its n and l added, and then by its n; a span's length
twice an odd number, 2, 6, 10, 14.

Returned at main, 16 November 2026, each check is:
  A field's four lengths of a span, 2, 6, 10 and 14, twice the odd numbers 1, 3, 5 and 7, are the four names of
  root possibling, the four dots of Exhibit ONE Natural Resolver's unit square.
  The square's across edge 6 with 2 adds to eight, a row's eight and the first seam; its across edge 10 with
  14 to twenty-four, the second seam; each diagonal to sixteen; its edges 8 apart to twelve and to twenty; and
  the four to thirty-two, the longest row, two sixteens.
  By the filling order the rows are 2, 8, 8, 18, 18, 32, 32 and close with 2, 10, 18, 36, 54, 86 and 118, as
  Exhibit SIXTEEN Natural Chemistry has them: each row the spans added from the first, 2, 2 and 6, 2 and 6 and
  10, 2 and 6 and 10 and 14.
  By n and l added the groups are eight, 2, 2, 8, 8, 18, 18, 32, 32, each length twice, adding to one hundred
  twenty, the fifth seam, an 8-now-same-existing sixteen on; the elements are these less the last two.
  A shell's 1, 4, 9 and 16, the odd numbers added from one, are the four names of squares, and twice them the
  rows' 2, 8, 18 and 32, adding to sixty.
  The element under each element is 2, 8, 18 or 32 up from it, a row's length: 8 up is one seat, and 32 up
  one name.
  The sixteen from lithium to argon, rows two and three, the first row's two before them: lithium, sodium and
  potassium are 1, 9 and 17. The four same-existing names, 4, 8, 12 and 16, are carbon, neon, silicon and argon,
  4 and 12 co, 8 and 16 one. A field's sharings of each are its place's going round a ring of eight from its
  row's closing: none with neon and argon, four with carbon and silicon. The betweens 8 )( 9 and 16 )( 17 are a
  row closing and its next opening. Each element with a possibling name has two sharings. The slide of two lines
  down brings carbon onto argon. By threes from two: helium 2, carbon 6, argon 18, xenon 54, each three of its
  prior; sixteen on, 2, 6, 2 and 6.
"""
import csv, glob, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); three = living('Exhibit_THREE_Natural_Numbers'); chem = living('Exhibit_SIXTEEN_Natural_Chemistry')
for text, said in ((chem, '**Elements have doubling.** Their rows are 2, 8, 8, 18, 18, 32, 32, each length after 2 twice in sequence, closing with 2, 10, 18, 36, 54, 86 and 118'),
                   (chem, 'doubling, each odd twice'), (chem, '`2 + 8 + 18 + 32 = 60`'), (chem, 'a field observes as the 8s pair its periodicity predicts for 119 and 120'),
                   (one, 'a unit square of four dots, 2-now-possibling, 6-now-co-possibling, 14-next-possibling and 10-next-co-possibling'),
                   (one, 'Its two across edges are sharings, 6 to 2 and 10 to 14. Its two edges 8 apart are 2 with 10 and 6 with 14.'),
                   (three, 'eleven squared less one**, a fifth seam, 8 · T₅')):
    assert said in text, said
NAME, ROOT = {}, {}
for n, name, root in re.findall(r'^\| (\d+) \| \*\*([^*]+)\*\* \| ([^|]+?) \|', one, re.M): NAME[int(n)], ROOT[int(n)] = name, root.split(',')[0]
assert sorted(NAME) == list(range(1, 18))
name_of = lambda n: (n - 1) % 16 + 1

# --- a field's list of elements, by number
SYMBOLS = ('H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe '
           'Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr '
           'Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og').split()
assert len(SYMBOLS) == 118 == len(set(SYMBOLS))
SAID = ('hydrogen helium lithium beryllium boron carbon nitrogen oxygen fluorine neon sodium magnesium aluminium silicon phosphorus sulfur chlorine argon potassium calcium '
        'scandium titanium vanadium chromium manganese iron cobalt nickel copper zinc gallium germanium arsenic selenium bromine krypton rubidium strontium yttrium zirconium '
        'niobium molybdenum technetium ruthenium rhodium palladium silver cadmium indium tin antimony tellurium iodine xenon caesium barium lanthanum cerium praseodymium '
        'neodymium promethium samarium europium gadolinium terbium dysprosium holmium erbium thulium ytterbium lutetium hafnium tantalum tungsten rhenium osmium iridium '
        'platinum gold mercury thallium lead bismuth polonium astatine radon francium radium actinium thorium protactinium uranium neptunium plutonium americium curium '
        'berkelium californium einsteinium fermium mendelevium nobelium lawrencium rutherfordium dubnium seaborgium bohrium hassium meitnerium darmstadtium roentgenium '
        'copernicium nihonium flerovium moscovium livermorium tennessine oganesson').split()
assert len(SAID) == 118 == len(set(SAID)) and SAID[5] == 'carbon' and SAID[17] == 'argon'
# a field's sharings of each of the sixteen from lithium to argon: the hydrogens of its simplest hydride, LiH, BeH2, BH3, CH4, NH3, H2O, HF, and none with neon; and the same with the next eight
SHARINGS = dict(zip(range(3, 19), (1, 2, 3, 4, 3, 2, 1, 0) * 2))
sixteen = lambda z: z - 2 if 3 <= z <= 19 else None           # an element's place among the sixteen from lithium, the first row's two before them; potassium the seventeenth

# --- a field's filling order: each span by its n and l added, and then by its n; a span's length twice an odd number
LETTER = 'spdf'
SPANS = sorted(((n, l) for n in range(1, 9) for l in range(0, 4) if l < n and n + l <= 8), key=lambda s: (s[0] + s[1], s[0]))
E, z = [], 0
for n, l in SPANS:
    for k in range(1, 4 * l + 3):
        z += 1
        E.append(dict(z=z, n=n, l=l, k=k, span=f'{n}{LETTER[l]}', length=4 * l + 2, group=n + l, row=n + max(0, l - 1) if l else n))
assert z == 120
row_of = lambda e: e['n'] + (e['l'] - 1 if e['l'] > 1 else 0) if e['l'] else e['n']       # a row of the table: s opens it, p closes it
for e in E: e['row'] = row_of(e)
ALL = E; E = [e for e in ALL if e['z'] <= 118]
by = {(e['n'], e['l'], e['k']): e for e in ALL}
for e in E:
    u = by.get((e['n'] + 1, e['l'], e['k'])); e['under'] = u if u and u['z'] <= 118 else None

# --- the surface of 1,024
G = lambda n: (n - 1) ^ ((n - 1) >> 1)
def index(bits):
    i = 0
    for b in bits: i = i * 2 + (b ^ (i & 1))
    return i
place = lambda n: (index([(G(n) >> k) & 1 for k in (9, 7, 5, 3, 1)]) + 1, index([(G(n) >> k) & 1 for k in (8, 6, 4, 2, 0)]) + 1)

if WHAT == 'json':
    order = {0: 0, 3: 2, 2: 16, 1: 26}                      # along a row: s, then f, then d, then p, as the row fills
    json.dump({'rows': [[next((f"{e['z']} {SYMBOLS[e['z'] - 1]}|{LETTER[e['l']]}" for e in E if e['row'] == r and order[e['l']] + e['k'] - 1 == c), None) for c in range(32)] for r in range(1, 8)]}, sys.stdout); sys.exit()
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['number', 'element', "a field's name of it", 'its place among the sixteen from lithium, a name', "its sharings, by a field", 'its name, sixteen on', 'its row of the table', "its span, by a field's filling order", "its span's length, a possibling name", 'its place in its span',
                'its going, each odd twice', 'its group of eight, by n and l added', "that group's length", 'the element under it', 'up to the element under it',
                'its line down, of thirty-two', 'its line across, of thirty-two'])
    for e in E:
        u = e['under']
        w.writerow([e['z'], SYMBOLS[e['z'] - 1], SAID[e['z'] - 1], NAME[sixteen(e['z'])] if sixteen(e['z']) else '', SHARINGS.get(e['z'], ''), NAME[name_of(e['z'])], e['row'], e['span'], NAME[e['length']], e['k'], 'first' if e['k'] <= e['length'] // 2 else 'second', e['group'],
                    sum(1 for x in ALL if x['group'] == e['group']), f"{u['z']} {SYMBOLS[u['z'] - 1]}" if u else '', u['z'] - e['z'] if u else '', *place(e['z'])])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print('The one hundred eighteen elements, each by its place:')
lengths = sorted({e['length'] for e in E})
say(lengths == [2, 6, 10, 14] == [2 * o for o in (1, 3, 5, 7)] and all(ROOT[n] == 'possibling' for n in lengths) and [n for n in range(1, 17) if ROOT[n] == 'possibling'] == lengths,
    "a field's four lengths of a span, 2, 6, 10 and 14, twice the odd numbers 1, 3, 5 and 7, are the four names of root possibling, the four dots of Exhibit ONE Natural Resolver's unit square")
seam = lambda k: 8 * k * (k + 1) // 2
say(6 + 2 == 8 == seam(1) and 10 + 14 == 24 == seam(2) and 2 + 14 == 6 + 10 == 16 and (2 + 10, 6 + 14) == (12, 20) and sum(lengths) == 32,
    "the square's across edge 6 with 2 adds to eight, the first seam; its across edge 10 with 14 to twenty-four, the second seam; each diagonal to sixteen; its edges 8 apart to twelve and to twenty; the four to thirty-two")
rows = [sum(1 for e in E if e['row'] == r) for r in range(1, 8)]; closing = [max(e['z'] for e in E if e['row'] == r) for r in range(1, 8)]
spans_of = [[e['length'] for e in E if e['row'] == r and e['k'] == 1] for r in range(1, 8)]
say(rows == [2, 8, 8, 18, 18, 32, 32] and closing == [2, 10, 18, 36, 54, 86, 118] and all(sorted(s) == [2, 6, 10, 14][:len(s)] for s in spans_of),
    'by the filling order the rows are 2, 8, 8, 18, 18, 32, 32, closing with 2, 10, 18, 36, 54, 86 and 118, as Exhibit SIXTEEN Natural Chemistry has them: each row the spans added from the first')
groups = [sum(1 for e in ALL if e['group'] == g) for g in range(1, 9)]
say(groups == [2, 2, 8, 8, 18, 18, 32, 32] and sum(groups) == 120 == seam(5) and name_of(120) == 8 and [e['z'] for e in ALL if e['z'] > 118] == [119, 120] and all(e['span'] == '8s' for e in ALL if e['z'] > 118),
    'by n and l added the groups are eight, 2, 2, 8, 8, 18, 18, 32, 32, each length twice, adding to one hundred twenty, the fifth seam, an 8-now-same-existing sixteen on; the elements are these less the last two, the 8s pair')
shells = [sum(2 * l + 1 for l in range(n)) for n in (1, 2, 3, 4)]
say(shells == [1, 4, 9, 16] == [sum((1, 3, 5, 7)[:n]) for n in (1, 2, 3, 4)] and all(name_of(x * x) in shells for x in range(1, 33)) and [2 * s for s in shells] == [2, 8, 18, 32] and sum(2 * s for s in shells) == 60,
    "a shell's 1, 4, 9 and 16, the odd numbers added from one, are the four names of squares, and twice them the rows' 2, 8, 18 and 32, adding to sixty")
ups = {e['under']['z'] - e['z'] for e in E if e['under']}
say(ups == {2, 8, 18, 32} and all(e['under'] for e in E if e['row'] < 7 and not (e['l'] == 3 and e['n'] == 5) and not (e['l'] == 2 and e['n'] == 6) and not (e['l'] == 1 and e['n'] == 7) and e['span'] != '7s'),
    "the element under each element is 2, 8, 18 or 32 up from it, a row's length")
say(all(name_of(e['under']['z']) == name_of(e['z']) for e in E if e['under'] and e['under']['z'] - e['z'] == 32)
    and all(name_of(e['under']['z']) == (name_of(e['z']) + 7) % 16 + 1 for e in E if e['under'] and e['under']['z'] - e['z'] == 8),
    '32 up, the element under it has its name; 8 up, the element under it has the name 8 apart, one seat')
print('      8 up:', ' '.join(f"{SYMBOLS[e['z'] - 1]}-{SYMBOLS[e['under']['z'] - 1]}" for e in E if e['under'] and e['under']['z'] - e['z'] == 8))
print('      closings by name:', ', '.join(f'{z} a {name_of(z)}' for z in closing))

print('The sixteen from lithium to argon, rows two and three, the first row\'s two before them:')
assert 'four-of-eight an exact middle number' in chem and '**Octet is eight-fold self with one chemical register.**' in chem
CO = {int(n): co for n, co in re.findall(r'^\| (\d+) \| \*\*[^*]+\*\* \| [^|]+ \| [^|]+ \| (co|one) \|', one, re.M)}; assert len(CO) == 17
el = lambda p: SAID[p + 1]                                    # the element with a place among the sixteen
say([e['z'] for e in E if e['row'] in (2, 3)] == list(range(3, 19)) and [sum(1 for e in E if e['row'] == r) for r in (2, 3)] == [8, 8],
    'lithium to argon are sixteen, rows two and three, each an eight')
say([sixteen(min(e['z'] for e in E if e['row'] == r)) for r in (2, 3, 4)] == [1, 9, 17] and [el(p) for p in (1, 9, 17)] == ['lithium', 'sodium', 'potassium'],
    'the elements opening rows two, three and four, lithium, sodium and potassium, are 1-now-existing, 9-next-co-discovering, its 8 up, and 17-next-existing, a next 1')
same = [p for p in range(1, 17) if ROOT[p] == 'same-existing']
say(same == [4, 8, 12, 16] and [el(p) for p in same] == ['carbon', 'neon', 'silicon', 'argon'] and [CO[p] for p in same] == ['co', 'one', 'co', 'one'],
    "the four same-existing names, 4, 8, 12 and 16, are carbon, neon, silicon and argon; by Exhibit ONE Natural Resolver's table 4 and 12 are co and 8 and 16 are one")
ring8 = lambda p: min(p % 8, (8 - p) % 8)                    # a place's going round a ring of eight from the row's closing, the lesser way
say(all(SHARINGS[p + 2] == ring8(p) for p in range(1, 17)) and [SHARINGS[p + 2] for p in same] == [4, 0, 4, 0],
    "a field's sharings of each of the sixteen are its place's going round a ring of eight from its row's closing, the lesser way: none with neon and argon, and four, the far side, with carbon and silicon")
betweens = [(int(a), int(b)) for a, b in re.findall(r'(\d+) \)\( (\d+)', next(l for l in one.split('\n') if l.startswith('Existing, discovering and observing are odd.')))]
say(betweens == [(4, 5), (8, 9), (12, 13), (16, 17)] and [(el(a), el(b)) for a, b in betweens] == [('carbon', 'nitrogen'), ('neon', 'sodium'), ('silicon', 'phosphorus'), ('argon', 'potassium')]
    and all(next(e['row'] for e in E if e['z'] == a + 2) + 1 == next(e['row'] for e in E if e['z'] == b + 2) for a, b in ((8, 9), (16, 17))),
    "of Exhibit ONE Natural Resolver's four betweens, 8 )( 9 and 16 )( 17 are a row closing and its next opening, neon to sodium and argon to potassium; 4 )( 5 and 12 )( 13 are each row's middle, carbon to nitrogen and silicon to phosphorus")
roots = {r: [p for p in range(1, 17) if ROOT[p] in r] for r in (('existing', 'discovering'), ('possibling',), ('observing',), ('same-existing',))}
say(all(SHARINGS[p + 2] == 2 for p in roots[('possibling',)]) and [el(p) for p in roots[('possibling',)]] == ['beryllium', 'oxygen', 'magnesium', 'sulfur']
    and all(SHARINGS[p + 2] + SHARINGS[p + 6] == 4 for p in (1, 2, 3, 4, 9, 10, 11, 12)) and all(ROOT[p].replace('discovering', 'existing') == ROOT[p + 4].replace('discovering', 'existing') for p in (1, 2, 3, 4, 9, 10, 11, 12)),
    "each element with a possibling name has two sharings, beryllium, oxygen, magnesium and sulfur, the unit square's four dots; and each root's two elements of a row, 4 apart, have four sharings together")
G2 = lambda n: (n - 1) ^ ((n - 1) >> 1); bit = lambda n, k: (G2(n) >> (k - 1)) & 1
spot = {p: (index([bit(p, 4), bit(p, 2)]), index([bit(p, 3), bit(p, 1)])) for p in range(1, 17)}
say(all(spot[a][1] == spot[b][1] and (spot[a][0] + 2) % 4 == spot[b][0] for a, b in ((4, 16), (8, 12))) and all(bit(a, 4) != bit(b, 4) and bit(a, 2) != bit(b, 2) and bit(a, 3) == bit(b, 3) and bit(a, 1) == bit(b, 1) for a, b in ((4, 16), (8, 12))),
    'on the second surface carbon and argon are in one line down, two lines apart, and neon and silicon alike: the slide of two lines down, the fourth parity with the second, brings carbon onto argon and neon onto silicon, a co onto a one')
threes = [2, 6, 18, 54]
say(all(b == 3 * a for a, b in zip(threes, threes[1:])) and [SAID[z - 1] for z in threes] == ['helium', 'carbon', 'argon', 'xenon'] and [name_of(z) for z in threes] == [2, 6, 2, 6]
    and [CO[name_of(z)] for z in threes] == ['one', 'co', 'one', 'co'] and [z for z in threes if z in closing] == [closing[0], closing[2], closing[4]] and 3 * 54 > 118,
    "by threes from two: helium 2, carbon 6, argon 18 and xenon 54, each three of its prior, and no element more; sixteen on they are 2, 6, 2 and 6, the unit square's across edge 6 with 2, a one and a co; and 2, 18 and 54 close the first, third and fifth rows")
print('      ' + ' · '.join(f'{p} {el(p)} {SHARINGS[p + 2]}' for p in range(1, 17)))
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
