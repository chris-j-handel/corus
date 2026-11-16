"""The newest seventeen duals, each concept with its parity: each of seventeen its name's own.
The partner's asking, 7 and 11 each no-other-and-not-prior, and the partner's suggesting, each prior identified
by its parity: a dual's first concept is with its name's now parity and its second with its next.
Reads the newest seventeen as the partner wrote them, `incoming/v402mgr/For_v403mgr.md`; each name's three, next,
now and prior, with their parities, `incoming/v403mgr/The_seventeen_names_in_one_table.csv`; Exhibit ONE Natural
Resolver's code; and Exhibit THIRTY Co-Chaining Logic Registry's moves of 4. Executes; writes no file; decides
nothing. Each answer is all or none at all, by each name, each handing, each move and each line of the code.

Use: python3 -I incoming/v403mgr/instruments/the_duals_with_their_parities.py <root>        each check
     python3 -I incoming/v403mgr/instruments/the_duals_with_their_parities.py <root> csv    one line with each name

Returned at main, 16 November 2026, each check is:
  Each name's three parities are one line of parities read three at a time: all, both, me, both, me, both, me,
  both, and again by eight. No name's prior is other-parity. Each handing of the duals is whole, sixteen of
  sixteen, and with its parity too: a concept is one parity with its two names. Each of seventeen duals, each
  concept with its parity, is its name's own. Each prior and not-prior is a me-parity but two, not-prior of 7 and
  8 and prior of 15 and 16, all-parity; each same, other and no-other is both-parity; each now, not-now and next
  me-parity. A dual's first concept with its name's prior parity has 7 and 11 one, not each: by all or none at
  all the first with the now is the one. Exhibit ONE's code has 7 and 11 each in the lines of 1-now-existing and
  of no other function, and one line has 11 with a sharing as that sharing's 7. Each of Exhibit THIRTY's four
  moves of 4 is the second and fourth parities of the surface inverting together; across it two duals part by
  prior and not-now exchanged, 5 with 9 and 6 with 10, or by all-parity and me-parity exchanged, 7 with 11 and 8
  with 12. 8 up is not, of each concept but same, with its parity as it was, with six of eight pairs; with 6 and
  14, and 7 and 15, no-other is no-other.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
T = list(csv.reader(open(os.path.join(R, 'incoming', 'v403mgr', 'The_seventeen_names_in_one_table.csv'), encoding='utf-8'))); H = T[0]; ROWS = T[1:]; assert len(ROWS) == 17
col = lambda name: next(i for i, c in enumerate(H) if c.startswith(name))
NAME = {k + 1: r[col('name')] for k, r in enumerate(ROWS)}; THREE = {k + 1: r[col('its three: next, now, prior')] for k, r in enumerate(ROWS)}
NEXT = {k + 1: r[col('its next, a parity')] for k, r in enumerate(ROWS)}; NOW = {k + 1: r[col('its now, a parity')] for k, r in enumerate(ROWS)}; PRIOR = {k + 1: r[col('its prior, a parity')] for k, r in enumerate(ROWS)}
page = open(os.path.join(R, 'incoming', 'v402mgr', 'For_v403mgr.md'), encoding='utf-8').read()
block = page.split('**The newest seventeen, as the partner wrote them**', 1)[1].split('```', 2)[1]
DUAL = {int(n): d for n, d in re.findall(r'(?m)^(\d+)-(.+)$', block)}; assert sorted(DUAL) == list(range(1, 18))
first = lambda n: DUAL[n].split('-and-')[0]; second = lambda n: DUAL[n].split('-and-')[1]
WITH = {n: ((first(n), NOW[n]), (second(n), NEXT[n])) for n in DUAL}               # each concept with its parity: its first with its now, its second with its next
said = lambda n: ' · '.join(f'{c}, {p}' for c, p in WITH[n])
OTHER = {n: ((first(n), PRIOR[n]), (second(n), NOW[n])) for n in DUAL}             # its first with its prior, its second with its now

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['name', 'dual, the newest', 'its prior, a parity', 'its now, a parity', 'its next, a parity', "dual, each concept with its parity: its first with its name's now, its second with its next"])
    for n in range(1, 18): w.writerow([NAME[n], DUAL[n], PRIOR[n], NOW[n], NEXT[n], said(n)])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print("Each name's three parities, and the newest seventeen duals, floating")
PAR = {'co': 'me-parity', 'bi': 'both-parity', 'tri': 'all-parity'}
LINE = [PRIOR[n] for n in range(1, 18)] + [NOW[17], NEXT[17]]
say(all([PAR[x] for x in THREE[n].split('-')] == [NEXT[n], NOW[n], PRIOR[n]] for n in THREE) and all(NOW[n] == PRIOR[n + 1] and NEXT[n] == NOW[n + 1] for n in range(1, 17))
    and all(LINE[k] == LINE[k + 8] for k in range(11)) and LINE[:8] == ['all-parity', 'both-parity', 'me-parity', 'both-parity', 'me-parity', 'both-parity', 'me-parity', 'both-parity'],
    "each name's three parities are one line of parities read three at a time: a name's now is its next name's prior, and its next is its next name's now, sixteen of sixteen each; the line is all, both, me, both, me, both, me, both, and again by eight")
say(set(LINE) == {'me-parity', 'both-parity', 'all-parity'} and [n for n in PRIOR if PRIOR[n] == 'all-parity'] == [1, 9, 17], "no name's prior is other-parity: the table has me-parity, both-parity and all-parity, and a name's prior is all-parity with 1, 9 and 17")
say(all(second(n) == first(n + 1) and WITH[n][1] == WITH[n + 1][0] for n in range(1, 17)), "each handing is whole, sixteen of sixteen, and with its parity too: a name's second concept is its next name's first, one parity with the two names")
say(len(set(WITH.values())) == 17 and len(set(DUAL.values())) == 14, 'each of seventeen duals, each concept with its parity, is its name\'s own: seventeen of seventeen; by its two concepts alone, fourteen')
pr = {n: [p for c, p in WITH[n] if c in ('prior', 'not-prior')] for n in WITH}
say(sorted(n for n in pr if pr[n] == ['all-parity']) == [7, 8, 15, 16] and all(('not-prior', 'all-parity') in WITH[n] for n in (7, 8)) and all(('prior', 'all-parity') in WITH[n] for n in (15, 16)) and all(v in ([], ['me-parity'], ['all-parity']) for v in pr.values())
    and all(p == 'both-parity' for n in WITH for c, p in WITH[n] if c in ('same', 'other', 'no-other')) and all(p == 'me-parity' for n in WITH for c, p in WITH[n] if c in ('now', 'not-now', 'next')),
    "each prior and not-prior is a me-parity, a self's me-parity as prior, but two: not-prior of 7 and 8, and prior of 15 and 16, all-parity; each same, other and no-other is both-parity, and each now, not-now and next me-parity")
say(len(set(OTHER.values())) == 16 and OTHER[7] == OTHER[11], "a dual's first concept with its name's prior parity, and its second with its now, has 7 and 11 one, not each: by all or none at all the first with the now is the one")
print(f'      7: {said(7)}\n      11: {said(11)}')

print("\nExhibit ONE Natural Resolver's code, and Exhibit THIRTY Co-Chaining Logic Registry's moves of 4")
one = living('Exhibit_ONE_Natural_Resolver'); reg = living('Exhibit_THIRTY_Co-Chaining_Logic_Registry')
code = '\n'.join(re.findall(r'```(?:python)?\n(.*?)```', one, re.S)); funcs = {m.group(1): f for f in re.split(r'(?m)^(?=def )', code) for m in [re.match(r'def (\w+)', f)] if m}
has = lambda f, n: bool(re.search(r'(?<!\d)_?' + str(n) + r'_(?:now|next)_', funcs[f]))
say(sorted(funcs) == ['_17_next_existing', '_1_now_existing', '_9_next_co_discovering'] and all(has('_1_now_existing', n) for n in (7, 11)) and not any(has(f, n) for f in ('_9_next_co_discovering', '_17_next_existing') for n in (7, 11))
    and funcs['_1_now_existing'].count('_11_next_co_observing[_4_now_co_same_existing] = _7_now_observing') == 1,
    "the code has 7 and 11 each in the lines of 1-now-existing and of no other function, and one line has 11 with a sharing as that sharing's 7")
def bits(n):
    g = (n - 1) ^ ((n - 1) >> 1); return frozenset(k + 1 for k in range(4) if g >> k & 1)
s708 = next(l for l in reg.split('\n') if "Further forms' moves of 4, step 694, are four" in l)
FOUR = sorted(tuple(sorted(map(int, x))) for x in re.findall(r'(\d+) with (\d+) about \d+', s708))
swap = lambda pairs, a, b: tuple((b if c == a else a if c == b else c, p) for c, p in pairs); swap_p = lambda pairs, a, b: tuple((c, b if p == a else a if p == b else p) for c, p in pairs)
say(FOUR == [(5, 9), (6, 10), (7, 11), (8, 12)] and all(sorted(bits(a) ^ bits(b)) == [2, 4] for a, b in FOUR)
    and all(swap(WITH[a], 'prior', 'not-now') == WITH[b] for a, b in FOUR[:2]) and all(swap_p(WITH[a], 'all-parity', 'me-parity') == WITH[b] and DUAL[a] == DUAL[b] for a, b in FOUR[2:]),
    "each of the four moves of 4 is the second and fourth parities of the surface inverting together; across it two duals part by prior and not-now exchanged, 5 with 9 and 6 with 10, or by all-parity and me-parity exchanged, 7 with 11 and 8 with 12")
NOT = {'now': 'not-now', 'not-now': 'now', 'prior': 'not-prior', 'not-prior': 'prior', 'other': 'no-other', 'no-other': 'other', 'same': 'same'}
no = lambda pairs: tuple((NOT[c], p) for c, p in pairs)
up = [(n, n + 8) for n in range(1, 9)]; whole = [(a, b) for a, b in up if no(WITH[a]) == WITH[b]]
say(len(whole) == 6 and [x for x in up if x not in whole] == [(6, 14), (7, 15)] and all(swap(no(WITH[a]), 'other', 'no-other') == WITH[b] for a, b in ((6, 14), (7, 15))),
    '8 up is not, of each concept but same, with its parity as it was, with six of eight pairs; with 6 and 14, and with 7 and 15, no-other is no-other as written, and by not it is other')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
