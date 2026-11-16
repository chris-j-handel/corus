"""Each number, 1 to 1,025, by its logical 1 to 17: the table of the seventeen names bi-folded forward.
Reads Exhibit ONE Natural Resolver's table of names and Exhibit THREE Natural Numbers; executes; writes no file;
decides nothing. Each answer is all or none at all, by each number or by a rule's own lines.

Use: python3 -I incoming/v403mgr/instruments/each_number_by_its_logical_seventeen.py <root>        each check, and eight numbers
     python3 -I incoming/v403mgr/instruments/each_number_by_its_logical_seventeen.py <root> csv    the table

The logic, each a living sentence:
  sixteen on     Exhibit THREE Natural Numbers: forms among 1 to 16 come again with 17 to 32, sixteen on. A number's
                 name among seventeen is its place within its sixteen; each column of the seventeen names is its own.
  by fours       Exhibit THREE Natural Numbers: pairs step a chain by two parities, 5, 17, 65 and 257; four 1 to 17s
                 are 1 to 65. Four roots are a four-cycling, four four-cyclings a 1 to 17, and on to 1 to 1,025.
  outward        Exhibit THREE Natural Numbers: 1 to 17 inward and outward steps it four, 17, 257 and 4,097. A number's
                 1 to 17 is a name of its 1 to 257, and its 1 to 257 a name of 1 to 4,097.
  a podal        Exhibit THREE Natural Numbers: a fold about a lays n on 2a less n; within one to a seam it is its odd
                 centre squared less n; on a ring of N it is k with N less k. Exhibit FOUR Natural Mathematics: on
                 names 1 to 8s a halfway pairing and a fold, taken one and then the other, reach four names.

Returned at main, 16 November 2026, each check is:
  Each line of Exhibit THREE Natural Numbers's table, nought to four hundred forty, is this table's line.
  Each seam to 1,025 is an 8-now-same-existing or a 16-next-same-existing, two and two, and its odd centre squared
  its next name, a 9-next-co-discovering or a next 1-now-existing. 360 and 440 are each an 8-now-same-existing.
  A podal is a fold, and each fold is one of the folds of the names: a fold sixteen on is the same fold.
  Parity's unit square: its across edges are the fold of a ring of 440, its diagonals the fold of a ring of 880,
  its edges 8 apart the halfway pairing. Two folds, one and then the other, are a going on.
  Each two hundred twenty on is a same-existing name, 4 down: 220 a 12, 440 an 8, 660 a 4, 880 a 16.
  A fold about no number has no name with itself; a ring's fold has two, 8 apart and of one root; each seam's ring
  has same-existing names with themselves and no other. Two and one hundred eighteen on a ring of 120 are a 2 with
  a 6, parity's unit square's across edge; the elements' turn with 60 is a 12-next-co-same-existing.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); three = living('Exhibit_THREE_Natural_Numbers')
rows = re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \| (.*?) \|', one, re.M); assert len(rows) == 17
NAME = {int(n): nm for n, nm, _ in rows}; ROOT = {int(n): r.split(',')[0].strip() for n, _, r in rows}
ROW3 = {int(c[0]): c[1:] for l in three.split('\n') for c in [[x.strip() for x in l.strip().strip('|').split('|')]] if len(c) == 6 and c[0].isdigit()}
HAS3 = {int(m.group(1)): m.group(2) for l in three.split('\n') for m in [re.match(r'- \*\*(\d+)\*\* · (.+)', l)] if m}
for s in ('Forms among 1 to 16 come again with 17 to 32, sixteen on', '19-27-22-30', 'A fold about a lays n on 2a less n',
          'A podal within one to a seam is its odd centre squared less n', 'four 1–17s hold it', '17, 257 and 4,097',
          'eight hundred eighty stations, coupling on four hundred forty'): assert s in three, s

TOP = 1025; ORD = ['first', 'second', 'third', 'fourth']; SUP = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
place = lambda n: (n - 1) % 16 + 1
def form(n):
    if n < 2: return '—'
    f, m, d = [], n, 2
    while d * d <= m:
        k = 0
        while m % d == 0: m //= d; k += 1
        if k: f.append(str(d) + (str(k).translate(SUP) if k > 1 else ''))
        d += 1
    if m > 1: f.append(str(m))
    return 'prime' if f == [str(n)] else ' · '.join(f)
SEAM = {4 * k * (k + 1): 2 * k + 1 for k in range(1, 40)}   # 8 · T_k, with its odd centre
TRI = {k * (k + 1) // 2: k for k in range(1, 60)}; FIB = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987}
def kinds(n):
    out = []
    if n in SEAM: out.append(f'seam, {SEAM[n]}² − 1')
    r = round(n ** 0.5)
    if r * r == n: out.append(f'{r}²' + (', a seam and one' if n - 1 in SEAM else ''))
    if n in TRI: out.append('T' + str(TRI[n]).translate(str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')))
    if n in FIB: out.append('prior two added')
    for k in range(1, 11):
        if n == 2 ** k: out.append('2' + str(k).translate(SUP))
        if n == 2 ** k + 1: out.append('2' + str(k).translate(SUP) + ' + 1')
        if n == 2 ** k - 1 and n > 1: out.append('2' + str(k).translate(SUP) + ' − 1')
    return ', '.join(dict.fromkeys(out))   # a form said once: four is 2² as a square and as two to a power
BF = {}
for b in ('1-9-8-16', '2-15-7-10', '3-11-6-14', '4-13-5-12'):
    for x in b.split('-'): BF[int(x)] = [int(y) for y in b.split('-')]
def doubling(n):   # on names 1 to 8s a halfway pairing and a fold, one and then the other: four names
    m = 8
    while m < n: m *= 2
    half = lambda x: x + m // 2 if x <= m // 2 else x - m // 2
    a = half(n); b = m + 1 - a; c = half(b)
    assert m + 1 - c == n and len({n, a, b, c}) == 4
    return m, [n, a, b, c]
far = lambda n, N: (N - n % N) % N
def row(n):
    p = place(n); B = (n - 1) // 16; q = (n - 1) % 8 + 1; d = [(n - 1) // 4 ** k % 4 for k in range(4)] + [(n - 1) // 256]
    S = min(s for s in SEAM if s >= n); m, four = doubling(n)
    return [n, ('odd' if n % 2 else 'even') + (', now' if (n - 1) // 8 % 2 == 0 else ', next'),
            NAME[p] if p > 1 or n == 1 else '17-next-existing, a next 1-now-existing', p, B + 1,
            d[4] + 1, d[3] + 1, d[2] + 1, ORD[d[1]], ROOT[p],
            NAME[B % 16 + 1], NAME[(n - 1) // 256 + 1],
            form(n), kinds(n), n + 8 if p <= 8 else n - 8, 16 * B + 17 - p, 8 * ((n - 1) // 8) + 9 - q,
            '-'.join(str(16 * B + x) for x in BF[p]), f'1 to {m}: ' + '-'.join(map(str, four)),
            S, S + 1 - n, far(n, 440), NAME[place(far(n, 440))] if far(n, 440) else 'nought', abs(220 - n % 440),
            far(n, 880), NAME[place(far(n, 880))] if far(n, 880) else 'nought', far(n, 120)]
HEAD = ['n', 'odd or even, with its span', 'its name among seventeen, sixteen on', 'its place among seventeen', 'its 1 to 17, sixteen on',
        'by fours: its 1 to 257 of 1 to 1,025', 'by fours: its 1 to 65 of its 1 to 257', 'by fours: its 1 to 17 of its 1 to 65',
        'by fours: its four-cycling of its 1 to 17', 'by fours: its root of its four-cycling',
        'outward: its 1 to 17 as a name of its 1 to 257', 'outward again: its 1 to 257 as a name of 1 to 4,097',
        'its form', 'forms it has', '8 apart within its sixteen', '17 less within its sixteen', '9 less within its eight',
        'its bi-folding, sixteen on', 'its bi-folding with its own doubling span, a halfway pairing and a fold',
        'the seam it is within', 'its podal within 1 to that seam', 'far side on a ring of 440', 'its far side\'s name, ring of 440',
        'radius from the waist, 220', 'far side on a ring of 880, two surfaces', 'its far side\'s name, ring of 880', 'far side on a ring of 120']
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n'); w.writerow(HEAD); w.writerows(row(n) for n in range(1, TOP + 1)); sys.exit()

say = lambda ok, label: print(f'  {"is" if ok else "is-not"} · {label}')
print('Each check, all or none at all:')
ok = all(ROW3[n] == [('even' if n == 0 else row(n)[1]), form(n), str(far(n, 440)) if n else '0', str(abs(220 - n % 440)), str(far(n, 120))] for n in range(1, 441)) and ROW3[0] == ['even', '—', '0', '220', '0']
say(ok, 'each line of Exhibit THREE Natural Numbers\'s table, nought to four hundred forty, is this table\'s line: odd or even with its span, form, far side with 440, radius, far side with 120')
say(all(('seam' in HAS3[n]) == (n in SEAM) for n in HAS3 if n), 'each seam of Exhibit THREE Natural Numbers\'s list is a seam here, and no other number of its list')
seams = sorted(s for s in SEAM if s <= TOP)
say(all(place(s) in (8, 16) for s in seams) and [place(s) for s in seams][:8] == [8, 8, 16, 16, 8, 8, 16, 16],
    f'each seam to 1,025 is an 8-now-same-existing or a 16-next-same-existing, two and two: {seams}')
say(all(place(s + 1) in (9, 1) for s in seams), 'each seam\'s odd centre squared is its next name: a 9-next-co-discovering, or a 17-next-existing as a next 1-now-existing')
pairs = lambda c: sorted({tuple(sorted((p, place(c - p)))) for p in range(1, 17)})
show = lambda P: ' '.join(f'{a}-{b}' for a, b in P)
kindsof = {'17 less, 33 less, 49 less, each fold of sixteens': 17, '9 less, 25 less, 41 less, each fold of eights': 9,
           'a ring of 8, 24, 120, 360, 440': 440, 'a ring of 16, 48, 80, 880': 880}
print('A podal is a fold, and each fold is one of the folds of the names:')
for label, c in kindsof.items(): print(f'  {label}: {show(pairs(c))}')
say(all(pairs(c) == pairs(c + 16 * k) for c in (17, 9, 440, 880) for k in range(1, 30)), 'a fold sixteen on is the same fold of the names')
say(all(pairs(N) == pairs(440) for N in (8, 24, 120, 360)) and all(pairs(N) == pairs(880) for N in (16, 48, 80)), 'each ring of a kind folds the names alike')
say({(2, 6), (10, 14)} <= set(pairs(440)) and {(2, 14), (6, 10)} <= set(pairs(880)),
    'parity\'s unit square: its across edges, 6 with 2 and 10 with 14, are the fold of a ring of 440; its diagonals, 2 with 14 and 6 with 10, the fold of a ring of 880; its edges 8 apart, 2 with 10 and 6 with 14, the halfway pairing')
say(all(ROOT[a] == ROOT[b] for a, b in pairs(440) + pairs(880) if ROOT[a] in ('possibling', 'same-existing')),
    'each ring\'s fold has possibling with possibling and same-existing with same-existing')
say(all(17 - (9 - n) == n + 8 for n in range(1, 9)) and all(far(far(n, 440), 880) == n + 440 for n in range(1, 440)),
    'two folds, one and then the other, are a going on: 9 less and then 17 less is 8 up; a ring of 440\'s fold and then a ring of 880\'s is 440 on')
say([place(k) for k in (220, 440, 660, 880)] == [12, 8, 4, 16] and all(ROOT[place(220 * k)] == 'same-existing' for k in range(1, 400)),
    'each two hundred twenty on is a same-existing name, 4 down: 220 a 12-next-co-same-existing, 440 an 8-now-same-existing, 660 a 4-now-co-same-existing, 880 a 16-next-same-existing')
say(row(22)[17] == '19-27-22-30' and row(22)[2] == NAME[6], 'twenty-two is a 6-now-co-possibling sixteen on, on 19-27-22-30, as Exhibit THREE Natural Numbers has it')
say(sorted(doubling(n)[1] for n in (3, 4)) == [[3, 7, 2, 6], [4, 8, 1, 5]] and all(sorted(doubling(n)[1]) == sorted(BF[n]) for n in range(9, 17)),
    'a halfway pairing and a fold with 1 to 8 are the two loops of four names, and with 1 to 16 the four bi-foldings')
four = living('Exhibit_FOUR_Natural_Mathematics'); physics = living('Exhibit_EIGHTEEN_Natural_Physics')
for text, s in ((four, 'A declaring of zero is a fixed set fixing as a place'), (four, 'An accounting with an empty fixed set has nothing for an accounting to number from'),
                (physics, 'Two and one hundred eighteen stand podal'), (physics, 'Its going has 2 to 59, a turn stands with 60, its back has 61 to 118')): assert s in text, s
print('A fold with a name with itself, and a fold fixing none:')
fixed = lambda c: sorted(p for p in range(1, 17) if place(c - p) == p)
say(all(fixed(c) == [] for c in range(1, 1026, 2)) and all(p % 2 != place(c - p) % 2 for c in (9, 17) for p in range(1, 17)),
    'a fold about no number, 9 less, 17 less and each odd one, has no name with itself, and exchanges odd and even')
say(all(place(p + 8) != p and place(p + 8) % 2 == p % 2 for p in range(1, 17)), '8 apart has no name with itself, and has odd with odd and even with even')
say(all(len(fixed(c)) == 2 and fixed(c)[1] - fixed(c)[0] == 8 and ROOT[fixed(c)[0]].replace('discovering', 'existing') == ROOT[fixed(c)[1]].replace('discovering', 'existing') for c in range(2, 1026, 2)),
    'a ring\'s fold has two names with themselves, 8 apart and of one root, existing with discovering as one')
say(all(fixed(s) in ([4, 12], [8, 16]) for s in SEAM), 'each seam\'s ring has same-existing names with themselves and no other: 4 with 12, or 8 with 16, its origin and its waist')
print('  a ring of 120, of 440, of 880, of 118, of 60:', {N: [NAME[x] for x in fixed(N)] for N in (120, 440, 880, 118, 60)})
print('The elements, Exhibit EIGHTEEN Natural Physics, each number by its name:')
say(place(2) == 2 and place(118) == 6 and (2, 6) in pairs(120), 'two and one hundred eighteen, podal on a ring of 120, are a 2-now-possibling with a 6-now-co-possibling: parity\'s unit square\'s across edge, 6 with 2')
say([place(n) for n in (59, 60, 61)] == [11, 12, 13] and fixed(120) == [4, 12], 'its going to 59, an 11-next-co-observing; its turn with 60, a 12-next-co-same-existing, with itself on its ring; its back from 61, a 13-next-discovering')
print('  two, ten, eighteen, thirty-six, fifty-four, eighty-six, one hundred eighteen:', [place(n) for n in (2, 10, 18, 36, 54, 86, 118)])
print('Eight numbers, each by its logical 1 to 17: its name, then outward, its 1 to 17 as a name, and its 1 to 257 as a name:')
for n in (220, 360, 361, 440, 441, 660, 880, 881):
    r = row(n); print(f'  {n}: {r[2]} · {r[10]} · {r[11]}; by fours {r[5]}, {r[6]}, {r[7]}, {r[8]}, {r[9]}; {r[13] or r[12]}; far side on 440 {r[21]}, {r[22]}; on 880 {r[24]}, {r[25]}')
