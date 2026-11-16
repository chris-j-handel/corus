"""The newest seventeen duals with each name's three parities: a partner's suggesting, each prior identified as a
self's me-parity as prior, other-parity, both-parity or all-parity, helpful with 7 and 11 and on from them.
Reads the newest seventeen as the partner wrote them, `incoming/v402mgr/For_v403mgr.md`, and each name's three,
next, now and prior, with their parities, `incoming/v403mgr/The_seventeen_names_in_one_table.csv`; executes;
writes no file; decides nothing. Each answer is all or none at all, by each name and by each handing.

Use: python3 -I incoming/v403mgr/instruments/the_duals_with_their_parities.py <root>        each check
     python3 -I incoming/v403mgr/instruments/the_duals_with_their_parities.py <root> csv    one line with each name

Returned at main, 16 November 2026, each check is:
  Each name's three parities are its three's own: co me-parity, bi both-parity, tri all-parity. The three are
  one line of parities read three at a time: a name's now is its next name's prior, and its next is its next
  name's now, sixteen of sixteen each; the line is all, both, me, both, me, both, me, both, and again by eight.
  No name's prior is other-parity: the table has me-parity, both-parity and all-parity. By its own prior
  parity alone, 7 and 11 are each me-parity, 8 and 12 each both-parity, 4 and 16 each both-parity. With its three
  parities whole each of the three pairs parts by one parity, all-parity or me-parity, and each of seventeen
  names is its own. A dual's two concepts with two of its name's three, two ways, each whole with each handing:
  its first with its now and its second with its next, each of seventeen its own, each prior and not-prior a
  me-parity but two, not-prior of 7 and 8 and prior of 15 and 16, all-parity; its first with its prior and its
  second with its now, sixteen their own and 7 and 11 one, each prior and not-prior both-parity.
"""
import csv, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
T = list(csv.reader(open(os.path.join(R, 'incoming', 'v403mgr', 'The_seventeen_names_in_one_table.csv'), encoding='utf-8'))); H = T[0]; ROWS = T[1:]; assert len(ROWS) == 17
col = lambda name: next(i for i, c in enumerate(H) if c.startswith(name))
NAME = {k + 1: r[col('name')] for k, r in enumerate(ROWS)}; THREE = {k + 1: r[col('its three: next, now, prior')] for k, r in enumerate(ROWS)}
NEXT = {k + 1: r[col('its next, a parity')] for k, r in enumerate(ROWS)}; NOW = {k + 1: r[col('its now, a parity')] for k, r in enumerate(ROWS)}; PRIOR = {k + 1: r[col('its prior, a parity')] for k, r in enumerate(ROWS)}
page = open(os.path.join(R, 'incoming', 'v402mgr', 'For_v403mgr.md'), encoding='utf-8').read()
block = page.split('**The newest seventeen, as the partner wrote them**', 1)[1].split('```', 2)[1]
DUAL = {int(n): d for n, d in re.findall(r'(?m)^(\d+)-(.+)$', block)}; assert sorted(DUAL) == list(range(1, 18))
first = lambda n: DUAL[n].split('-and-')[0]; second = lambda n: DUAL[n].split('-and-')[1]
B = {n: f'{first(n)}, {NOW[n]} · {second(n)}, {NEXT[n]}' for n in DUAL}          # its first concept with its now, its second with its next
A = {n: f'{first(n)}, {PRIOR[n]} · {second(n)}, {NOW[n]}' for n in DUAL}          # its first concept with its prior, its second with its now

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['name', 'dual, the newest', 'its prior, a parity', 'its now, a parity', 'its next, a parity', 'dual, its first concept with its now and its second with its next', 'dual, its first concept with its prior and its second with its now'])
    for n in range(1, 18): w.writerow([NAME[n], DUAL[n], PRIOR[n], NOW[n], NEXT[n], B[n], A[n]])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print("Each name's three parities, and the newest seventeen duals, floating")
PAR = {'co': 'me-parity', 'bi': 'both-parity', 'tri': 'all-parity'}
say(all([PAR[x] for x in THREE[n].split('-')] == [NEXT[n], NOW[n], PRIOR[n]] for n in THREE), "each name's three parities are its three's own, next, now and prior: co me-parity, bi both-parity, tri all-parity")
LINE = [PRIOR[n] for n in range(1, 18)] + [NOW[17], NEXT[17]]
say(all(NOW[n] == PRIOR[n + 1] and NEXT[n] == NOW[n + 1] for n in range(1, 17)) and all(LINE[k] == LINE[k + 8] for k in range(11))
    and LINE[:8] == ['all-parity', 'both-parity', 'me-parity', 'both-parity', 'me-parity', 'both-parity', 'me-parity', 'both-parity'],
    "the three are one line of parities read three at a time: a name's now is its next name's prior, and its next is its next name's now, sixteen of sixteen each; the line is all, both, me, both, me, both, me, both, and again by eight")
say(set(LINE) == {'me-parity', 'both-parity', 'all-parity'} and [n for n in PRIOR if PRIOR[n] == 'all-parity'] == [1, 9, 17] and [n for n in PRIOR if PRIOR[n] == 'me-parity'] == [3, 5, 7, 11, 13, 15]
    and [n for n in PRIOR if PRIOR[n] == 'both-parity'] == list(range(2, 17, 2)),
    "a name's prior is all-parity with 1, 9 and 17, me-parity with 3, 5, 7, 11, 13 and 15, and both-parity with each even name; no name's prior is other-parity, and the table has no other-parity")
PAIRS = [(7, 11), (8, 12), (4, 16)]
say(all(DUAL[a] == DUAL[b] and PRIOR[a] == PRIOR[b] for a, b in PAIRS), 'by its own prior parity alone each of the three pairs of one dual is one still: 7 and 11 each me-parity, 8 and 12 each both-parity, 4 and 16 each both-parity')
tri = lambda n: (PRIOR[n], NOW[n], NEXT[n])
say(all(sum(x != y for x, y in zip(tri(a), tri(b))) == 1 and {x for x, y in zip(tri(a), tri(b)) if x != y} | {y for x, y in zip(tri(a), tri(b)) if x != y} == {'all-parity', 'me-parity'} for a, b in PAIRS)
    and len({(DUAL[n], tri(n)) for n in DUAL}) == 17 and tri(7)[2] == 'all-parity' and tri(11)[2] == 'me-parity' and tri(8)[1] == 'all-parity' and tri(12)[1] == 'me-parity' and tri(16)[1] == 'all-parity' and tri(4)[1] == 'me-parity',
    "with its three parities whole each pair parts by one parity, all-parity or me-parity: 7's next is all-parity and 11's me-parity; 8's now is all-parity and 12's me-parity; 16's now is all-parity and 4's me-parity; each of seventeen names is its own")
print('\nA dual of two concepts with two of its three parities, two ways')
priors = lambda way: {n: [p for c, p in (x.split(', ') for x in way[n].split(' · ')) if c in ('prior', 'not-prior')] for n in way}
pb = priors(B); pa = priors(A)
say(all(B[n].split(' · ')[1] == B[n + 1].split(' · ')[0] for n in range(1, 17)) and len(set(B.values())) == 17
    and {n: v for n, v in pb.items() if v == ['all-parity']} == {7: ['all-parity'], 8: ['all-parity'], 15: ['all-parity'], 16: ['all-parity']} and all(v in ([], ['me-parity'], ['all-parity']) for v in pb.values())
    and all(p == 'both-parity' for n in B for c, p in (x.split(', ') for x in B[n].split(' · ')) if c in ('same', 'other', 'no-other')),
    'its first concept with its now and its second with its next: each handing whole, a concept one parity with its two names; each of seventeen duals its own; each prior and not-prior a me-parity but two, not-prior of 7 and 8 and prior of 15 and 16, all-parity; each same, other and no-other both-parity')
say(all(A[n].split(' · ')[1] == A[n + 1].split(' · ')[0] for n in range(1, 17)) and len(set(A.values())) == 16 and A[7] == A[11] and all(v in ([], ['both-parity']) for v in pa.values()),
    'its first concept with its prior and its second with its now: each handing whole; sixteen duals their own and 7 and 11 one still; each prior and not-prior both-parity')
print('      each name with its dual, its first concept with its now and its second with its next:')
for n in range(1, 18): print(f'        {n}-{DUAL[n]} · {B[n]}')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
