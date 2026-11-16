"""Exhibit THIRTY Co-Chaining Logic Registry in the table: the numbered sentence each name of the seventeen enters
with, a name's side in three files, the twelve forms among names by the surface's four parities, and a next
adding now and prior.
Reads Exhibit THIRTY Co-Chaining Logic Registry, Exhibit ONE Natural Resolver and Exhibit TWENTY-NINE Natural
Illustrating; executes; writes no file; decides nothing. Each answer is all or none at all: by each numbered
sentence, by each name, by each move of each form, by each adding.

Use: python3 -I incoming/v403mgr/instruments/co_chaining_logic_by_the_names.py <root>          each check
     python3 -I incoming/v403mgr/instruments/co_chaining_logic_by_the_names.py <root> csv      one line with each name
     python3 -I incoming/v403mgr/instruments/co_chaining_logic_by_the_names.py <root> forms    one line with each form

Returned at main, 16 November 2026, each check is:
  755 numbered sentences, 1 to 755 with none missing, in 46 groups. Each naming whole is Exhibit ONE's name of its
  number, and one is a name sixteen on. Each of seventeen names is named whole, 1 and 2 entering first and 6 last.
  A name's side: twelve of seventeen are one saying in the three files; with 2, 14 and 15 this file has other to
  self and the two others have others to self; with 7 this file and Exhibit ONE have other to self and Exhibit
  TWENTY-NINE others to self; with 5 this file has self and other and the two others self and others.
  Twelve forms among names, four bi-foldings and eight further forms: each move is 8 up or down, the third and
  fourth parities together, 17 less, the fourth alone, or a move of 4 across the middle, the second and fourth
  together; each move inverts the fourth parity and none the first. The two eight-cycles are the sixteen names
  parted by the first parity, existing, discovering and same-existing, the second surface's two outer lines down,
  and possibling and observing, its two middle lines down; each other
  form is within one of the two. Each form's changings of odd and even are two, each a 17 less. Names two moves
  apart are one parity apart: the third with a bi-folding, the second with a middle bi-folding. Rotation 3, 6,
  5, 4 is one line across the second surface, one parity with each move, the third and the first by turns.
  A next adding now and prior, each as it is, inverting or a 0: eight addings, the same again after one, two,
  two, four, three and six, and two not again; none after five.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
reg = living('Exhibit_THIRTY_Co-Chaining_Logic_Registry'); one = living('Exhibit_ONE_Natural_Resolver'); ill = living('Exhibit_TWENTY-NINE_Natural_Illustrating')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))

# ---- the registry's numbered sentences, each with its group
S = {}; G = {}; ORDER = []; cur = None
for l in reg.split('\n'):
    m = re.match(r'## (\d+) (.+)', l)
    if m: cur = int(m.group(1)); G[cur] = m.group(2); continue
    m = re.match(r'(\d+)\. (.+)', l)
    if m and cur: S[int(m.group(1))] = (cur, m.group(2)); ORDER.append(int(m.group(1)))
def sentence_with(words): return next(s for n, (g, s) in sorted(S.items()) if words in s)

# ---- the surface: sixteen names in reflected order, four parities; fourth and second down, third and first across
def bits(n):
    g = (n - 1) ^ ((n - 1) >> 1); return frozenset(k + 1 for k in range(4) if g >> k & 1)
def moved(a, b): return sorted(bits(a) ^ bits(b))
ring = lambda c: list(zip(c, c[1:] + c[:1]))
def move_words(a, b):
    return '17 less' if a + b == 17 else f'{abs(a - b)} {"up" if b > a else "down"}'
SURFACE = [[next(n for n in range(1, 17) if (4 in bits(n), 2 in bits(n)) == r and (3 in bits(n), 1 in bits(n)) == c) for c in ((False, False), (False, True), (True, True), (True, False))]
           for r in ((False, False), (False, True), (True, True), (True, False))]

# ---- names: entering, and sides in three files
whole = {}; other_naming = []
for n in ORDER:
    for nm in sorted(set(re.findall(r'(?<![\w-])(\d+-(?:now|next)-[a-z-]+)', S[n][1]))):
        k = int(nm.split('-')[0])
        if NAME.get(k) == nm: whole.setdefault(k, []).append(n)
        else: other_naming.append((n, nm))
SIDE1 = {int(n): sd.split(':')[0] for n, sd in re.findall(r'(?m)^\*\*(\d+)\*\* · .+\n- \*Parity, span\*: .+\n- \*Sides\*: (.+)$', one)}; assert sorted(SIDE1) == list(range(1, 18))
s260 = sentence_with('Sides of names are a self, an other and a same-existing-society each name is with')
SIDE30 = {}
for clause in s260.split(': ', 1)[1].split(';'):
    clause = re.sub(r'^\s*and ', '', clause.strip()); side = re.sub(r'^a self$', 'self', clause.split(' with ', 1)[0].strip())
    for part in re.findall(r' with ((?:\d+(?:, | and )?)+)', clause):
        for n in re.findall(r'\d+', part): SIDE30[int(n)] = side
sent29 = ill.split("each name's sides: ", 1)[1].split('. ', 1)[0]
SIDE29 = {int(n): re.sub(r'^a self$', 'self', g.strip()) for nums, g in re.findall(r'((?:\d+(?:, | and )?)+) ([a-z -]+?)(?:;|$)', sent29) for n in re.findall(r'\d+', nums)}

# ---- forms among names
s335 = sentence_with('Stable-forming is that move along each of four bi-foldings of names'); s694 = sentence_with('Further forms, step 337, each go by 4 up or 4 down')
BF = [list(map(int, x.split('-'))) for x in re.findall(r'(?<![\w-])(\d+(?:-\d+){3})(?![\w-])', s335)]
FURTHER = [list(map(int, x.split('-'))) for x in re.findall(r'(?<![\w-])(\d+(?:-\d+){3,7})(?![\w-])', s694)]
KIND = lambda c: 'a bi-folding' if c in BF else {4: 'a middle bi-folding', 6: 'a six-cycle', 8: 'an eight-cycle'}[len(c)]
FORMS = BF + FURTHER
ROOT = lambda n: re.sub(r'^\d+-(?:now|next)-(?:co-)?', '', NAME[n])
FIRST = lambda c: {1 in bits(n) for n in c}

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['name', 'the numbered sentence it enters whole with', "that sentence's group", 'each numbered sentence naming it whole', "its side, Exhibit ONE Natural Resolver's",
                "its side, this file's", "its side, Exhibit TWENTY-NINE Natural Illustrating's", 'its first parity, as 1 has it or inverting', 'its eight-cycle', 'each form of twelve it is in'])
    eights = [c for c in FURTHER if len(c) == 8]
    for k in range(1, 17 + 1):
        w.writerow([NAME[k], whole[k][0], f'{S[whole[k][0]][0]} {G[S[whole[k][0]][0]]}', ' · '.join(map(str, whole[k])), SIDE1[k], SIDE30[k], SIDE29[k],
                    '' if k == 17 else ('inverting' if 1 in bits(k) else 'as 1 has it'), '' if k == 17 else '-'.join(map(str, next(c for c in eights if k in c))),
                    ' · '.join('-'.join(map(str, c)) for c in FORMS if k in c)])
    sys.exit()
if WHAT == 'forms':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['a form among names', 'its kind', 'its moves, by numbers', 'its moves, by parities inverting', 'its changings of odd and even', "its names' first parity", "its names' roots"])
    for c in FORMS:
        w.writerow(['-'.join(map(str, c)), KIND(c), ', '.join(move_words(a, b) for a, b in ring(c)), ', '.join(' and '.join(map(str, moved(a, b))) for a, b in ring(c)),
                    sum((a - b) % 2 for a, b in ring(c)), 'inverting' if FIRST(c) == {True} else 'as 1 has it', ', '.join(sorted({ROOT(n) for n in c}))])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')

print(f'Exhibit THIRTY Co-Chaining Logic Registry: {len(S)} numbered sentences in {len(G)} groups')
say(ORDER == list(range(1, len(ORDER) + 1)) and len(S) == len(ORDER) and sorted(G) == list(range(1, len(G) + 1)), f'its numbered sentences are 1 to {len(ORDER)} in sequence with none missing, and its groups 1 to {len(G)}')
say(all(NAME[(int(nm.split('-')[0]) - 1) % 16 + 1].split('-', 1)[1] == nm.split('-', 1)[1] and int(nm.split('-')[0]) > 17 for n, nm in other_naming),
    f"each naming whole is Exhibit ONE's name of its number, and {len(other_naming)} is a name sixteen on: " + '; '.join(f'{nm}, with sentence {n}' for n, nm in other_naming))
enter = sorted(range(1, 18), key=lambda k: (whole[k][0], k))
say(sorted(whole) == list(range(1, 18)) and all(str(k) in re.findall(r'\d+', sentence_with('Each number 1 to 17 is one name')) or 1 < k < 17 for k in range(1, 18)),
    'each of seventeen names is named whole; the sequence of their entering: ' + ', '.join(f'{k} with {whole[k][0]}' for k in enter))

print("\nA name's side, in three files")
same = [k for k in range(1, 18) if SIDE1[k] == SIDE30[k] == SIDE29[k]]; part = [k for k in range(1, 18) if k not in same]
say(sorted(SIDE30) == sorted(SIDE29) == list(range(1, 18)) and len(same) == 12 and part == [2, 5, 7, 14, 15], 'each of seventeen names has its side in each of the three files; twelve are one saying in the three, and five part: 2, 5, 7, 14 and 15')
say(all(SIDE1[k] == SIDE29[k] == 'others to self' and SIDE30[k] == 'other to self' for k in (2, 14, 15)) and SIDE1[7] == SIDE30[7] == 'other to self' and SIDE29[7] == 'others to self'
    and SIDE1[5] == SIDE29[5] == 'self and others' and SIDE30[5] == 'self and other',
    "with 2, 14 and 15 this file has other to self and the two others have others to self; with 7 this file and Exhibit ONE have other to self and Exhibit TWENTY-NINE others to self; with 5 this file has self and other and the two others self and others")

print('\nTwelve forms among names, by the four parities of the surface')
say(len(BF) == 4 and len(FURTHER) == 8 and [len(c) for c in FURTHER] == [4, 4, 6, 6, 6, 6, 8, 8] and sorted(n for c in BF for n in c) == list(range(1, 17)) and all(len(set(c)) == len(c) for c in FORMS),
    'four bi-foldings, sixteen names each once, and eight further forms: two middle bi-foldings, four six-cycles and two eight-cycles')
MV = {(a, b) for c in FORMS for a, b in ring(c)}
say(all(a + b == 17 or abs(a - b) in (8, 4) for a, b in MV) and all(moved(a, b) == ([4] if a + b == 17 else [3, 4] if abs(a - b) == 8 else [2, 4]) for a, b in MV)
    and all(min(a, b) <= 8 < max(a, b) for a, b in MV if abs(a - b) == 4),
    'each move of each form is 8 up or down, 17 less or 4 up or down: 8 the third and fourth parities together, 17 less the fourth alone, and each move of 4 across the middle between 8 and 9, the second and fourth together; each move inverts the fourth parity, and none the first')
eights = [c for c in FURTHER if len(c) == 8]
say(len(eights) == 2 and sorted(eights[0] + eights[1]) == list(range(1, 17)) and all(len(FIRST(c)) == 1 for c in FORMS) and FIRST(eights[0]) != FIRST(eights[1])
    and {ROOT(n) for n in next(c for c in eights if 1 in c)} == {'existing', 'discovering', 'same-existing'} and {ROOT(n) for n in next(c for c in eights if 2 in c)} == {'possibling', 'observing'}
    and {r[k] for r in SURFACE for k in (0, 3)} == set(next(c for c in eights if 1 in c)) and {r[k] for r in SURFACE for k in (1, 2)} == set(next(c for c in eights if 2 in c)),
    "the two eight-cycles are the sixteen names parted by the first parity, one the names of existing, discovering and same-existing, the second surface's two outer lines down, and one the names of possibling and observing, its two middle lines down; each of twelve forms is within one of the two")
say('changings of odd and even are exactly two, each with a 17 less' in sentence_with('With each of twelve forms, four bi-foldings and eight further forms')
    and all(sum((a - b) % 2 for a, b in ring(c)) == 2 and all((a + b == 17) == bool((a - b) % 2) for a, b in ring(c)) for c in FORMS),
    "with each of twelve forms its changings of odd and even are two, each a 17 less, and each other move is with odd or even as it was")
two = lambda c: [(c[i], c[(i + 2) % len(c)]) for i in range(len(c))]
mids = [c for c in FURTHER if len(c) == 4]
say('add to 13 or to 21' in sentence_with('With each middle bi-folding, step 694, names two moves apart') and all(a + b in (13, 21) and moved(a, b) == [2] for c in mids for a, b in two(c))
    and all(a + b in (9, 25) and moved(a, b) == [3] for c in BF for a, b in two(c)),
    'names two moves apart are one parity apart: with each of four bi-foldings they add to 9 or to 25, the third parity alone; with each middle bi-folding to 13 or to 21, the second alone')
s708 = sentence_with("Further forms' moves of 4, step 694, are four")
FOUR = [tuple(map(int, x)) for x in re.findall(r'(\d+) with (\d+) about (\d+)', s708)]
say(len(FOUR) == 4 and sorted(tuple(sorted((a, b))) for a, b, _ in FOUR) == [(5, 9), (6, 10), (7, 11), (8, 12)] and {frozenset((a, b)) for a, b, _ in FOUR} == {frozenset(p) for p in MV if abs(p[0] - p[1]) == 4} and all(a + b == 2 * m for a, b, m in FOUR)
    and sorted(m for _, _, m in FOUR) == [7, 8, 9, 10], "the forms' moves of 4 are four, 9 with 5, 12 with 8, 7 with 11 and 6 with 10, each about the name between its two, and the four centres 7, 8, 9 and 10 add to 17 as two pairs")
s707 = sentence_with('Rotation 3, 6, 5, 4, step 267, is four names of two bi-foldings'); rot = [3, 6, 5, 4]
say(all(a in c and b in c for (a, b), c in (((3, 6), [3, 11, 6, 14]), ((5, 4), [4, 13, 5, 12]))) and [3, 11, 6, 14] in BF and [4, 13, 5, 12] in BF
    and [moved(a, b) for a, b in ring(rot)] == [[3], [1], [3], [1]] and sorted(rot) == sorted(SURFACE[1]) and [SURFACE[1].index(n) for n in rot] == [1, 2, 3, 0]
    and '6 and 4 are 8 up as 14 and 12' in s707 and '3 and 5 are 17 less as 14 and 12' in s707 and moved(6, 14) == moved(4, 12) == [3, 4] and moved(3, 14) == moved(5, 12) == [4],
    f"rotation 3, 6, 5, 4 is one parity inverting with each move, the third and the first by turns: one line across the second surface, {' '.join(map(str, SURFACE[1]))}, going across and round its edge; 6 and 4 are 8 up as 14 and 12, and 3 and 5 are 17 less as 14 and 12")

print('\nA next adding now and prior, each as it is, inverting or a 0')
s711 = sentence_with('With numbers, a next adding now and prior')
def again(a, b):                              # the fewest moments after which each value is the same again, from each of two first pairs; none within twelve: 0
    for k in range(1, 13):
        ok = True
        for x in ([1, 0], [0, 1]):
            x = list(x)
            while len(x) < 40: x.append(a * x[-1] + b * x[-2])
            ok = ok and all(x[n + k] == x[n] for n in range(1, 24))
        if ok: return k
    return 0
def grows(a, b):                              # by the adding's own line each value is larger than the last: not again
    x = [0, 1]
    while len(x) < 60: x.append(a * x[-1] + b * x[-2])
    return all(abs(x[n + 1]) == abs(x[n]) + abs(x[n - 1]) for n in range(1, 59)) and all(abs(x[n + 1]) > abs(x[n]) for n in range(3, 59))
ADD = {(a, b): again(a, b) for a in (1, -1, 0) for b in (1, -1, 0) if (a, b) != (0, 0)}
say(len(ADD) == 8 and ADD[(1, 0)] == 1 and ADD[(-1, 0)] == 2 and ADD[(0, 1)] == 2 and ADD[(0, -1)] == 4 and ADD[(-1, -1)] == 3 and ADD[(1, -1)] == 6
    and ADD[(1, 1)] == 0 and ADD[(-1, 1)] == 0 and grows(1, 1) and grows(-1, 1) and 5 not in ADD.values()
    and all(w in s711 for w in ('after one', 'after two', 'after four', 'both inverting after three', 'now as it is and prior inverting after six', 'an empty set of eight after five')),
    'eight addings: now on its own the same again after one, and inverting after two; prior on its own after two, and inverting after four; both inverting after three; now as it is and prior inverting after six; both as they are, and now inverting with prior as it is, not again, each value larger than the last by the adding\'s own line, read with sixty moments; none after five')
say(sorted(set(ADD.values()) - {0}) == [1, 2, 3, 4, 6], "the rounds are one, two, three, four and six: a field's turns of a pattern going on with a surface, a turn of a third and a turn of a sixth among them")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
