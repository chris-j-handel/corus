"""One dual with two names: the newest seventeen duals, floating, read with Exhibit ONE Natural Resolver's code
and with Exhibit THIRTY Co-Chaining Logic Registry's moves of 4. The partner's asking: 7 and 11 are each
no-other-and-not-prior; is this an error.
Reads the newest seventeen as the partner wrote them, `incoming/v402mgr/For_v403mgr.md`, Exhibit ONE Natural
Resolver and Exhibit THIRTY Co-Chaining Logic Registry; executes; writes no file; decides nothing. Each answer is
all or none at all: by each handing, by each name, by each move, by each line of the code.

Use: python3 -I incoming/v403mgr/instruments/one_dual_with_two_names.py <root>

Returned at main, 16 November 2026, each check is:
  Seventeen duals, each name's second concept its next name's first, sixteen handings each whole. Fourteen duals
  with seventeen names: 4 and 16, 7 and 11, and 8 and 12 are each one dual, each two of one root. A dual has no
  now or next of its name and no co: 7 is now and of one, 11 next and co; with its number each is one name.
  Exhibit ONE's code has three functions; 7 and 11 are each in the lines of 1-now-existing and of no other, and
  one line has 11 with a sharing as that sharing's 7. Across each of Exhibit THIRTY's four moves of 4, two duals
  part by prior and not-now exchanged and by no other concept: 5 with 9 and 6 with 10 part, and 7 with 11 and 8
  with 12 have neither concept and are one dual. 8 up is not of each concept but same with six of eight pairs;
  with 6 and 14, and 7 and 15, no-other is no-other. Not, twice, is the same again: 4 to 8 to 16.
"""
import glob, os, re, sys

R = sys.argv[1]
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); reg = living('Exhibit_THIRTY_Co-Chaining_Logic_Registry')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
page = open(os.path.join(R, 'incoming', 'v402mgr', 'For_v403mgr.md'), encoding='utf-8').read()
block = page.split('**The newest seventeen, as the partner wrote them**', 1)[1].split('```', 2)[1]
DUAL = {int(n): d for n, d in re.findall(r'(?m)^(\d+)-(.+)$', block)}; assert sorted(DUAL) == list(range(1, 18))
first = lambda n: DUAL[n].split('-and-')[0]; second = lambda n: DUAL[n].split('-and-')[1]
ROOT = lambda n: re.sub(r'^\d+-(?:now|next)-(?:co-)?', '', NAME[n])
NOT = {'now': 'not-now', 'not-now': 'now', 'prior': 'not-prior', 'not-prior': 'prior', 'other': 'no-other', 'no-other': 'other', 'same': 'same'}
def no(d): return '-and-'.join(NOT[c] for c in d.split('-and-'))
def swap(d, a, b): return '-and-'.join(b if c == a else a if c == b else c for c in d.split('-and-'))

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')

print('The newest seventeen duals, as the partner wrote them, floating')
say(all(second(n) == first(n + 1) for n in range(1, 17)), "each name's second concept is its next name's first: sixteen handings, each whole")
by = {}
for n in range(1, 18): by.setdefault(DUAL[n], []).append(n)
pairs = sorted(v for v in by.values() if len(v) > 1)
say(len(by) == 14 and pairs == [[4, 16], [7, 11], [8, 12]] and all(ROOT(a) == ROOT(b) for a, b in pairs),
    f"fourteen duals with seventeen names: three are each with two names, each two of one root: {'; '.join(f'{DUAL[a]}, {NAME[a]} and {NAME[b]}' for a, b in pairs)}")
say(not any(re.search(r'(^|-)(co|next)(-|$)', DUAL[n]) for n in range(1, 17)) and 'now' in NAME[7] and 'next' in NAME[11] and '-co-' in NAME[11] and '-co-' not in NAME[7],
    'a dual has no co and no next of its name, 1 to 16: 7 is a now name and of one, 11 a next name and co; with its number each is one name')

print("\nExhibit ONE Natural Resolver's code")
code = '\n'.join(re.findall(r'```(?:python)?\n(.*?)```', one, re.S)); funcs = {m.group(1): f for f in re.split(r'(?m)^(?=def )', code) for m in [re.match(r'def (\w+)', f)] if m}
has = lambda f, n: bool(re.search(r'(?<!\d)_?' + str(n) + r'_(?:now|next)_', funcs[f]))
say(sorted(funcs) == ['_17_next_existing', '_1_now_existing', '_9_next_co_discovering'] and all(has('_1_now_existing', n) for n in (7, 11)) and not any(has(f, n) for f in ('_9_next_co_discovering', '_17_next_existing') for n in (7, 11)),
    'the code has three functions, and 7 and 11 are each in the lines of 1-now-existing and of no other function')
say(funcs['_1_now_existing'].count('_11_next_co_observing[_4_now_co_same_existing] = _7_now_observing') == 1,
    "one line has 11 with a sharing as that sharing's 7: 11-next-co-observing, with each 4-now-co-same-existing, is its 7-now-observing")

print("\nExhibit THIRTY Co-Chaining Logic Registry's moves of 4, across the middle between 8 and 9")
s708 = next(l for l in reg.split('\n') if "Further forms' moves of 4, step 694, are four" in l)
FOUR = sorted(tuple(sorted(map(int, x))) for x in re.findall(r'(\d+) with (\d+) about \d+', s708))
say(FOUR == [(5, 9), (6, 10), (7, 11), (8, 12)] and all(swap(DUAL[a], 'prior', 'not-now') == DUAL[b] for a, b in FOUR)
    and all(DUAL[a] != DUAL[b] for a, b in FOUR[:2]) and all(DUAL[a] == DUAL[b] and 'prior' not in DUAL[a].split('-and-') and 'not-now' not in DUAL[a].split('-and-') for a, b in FOUR[2:]),
    'across each of the four moves of 4, two duals part by prior and not-now exchanged and by no other concept: 5 with 9 and 6 with 10 part by it; 7 with 11 and 8 with 12 have neither concept, and each two are one dual')
up = [(n, n + 8) for n in range(1, 9)]; whole = [(a, b) for a, b in up if no(DUAL[a]) == DUAL[b]]; rest = [(a, b) for a, b in up if (a, b) not in whole]
say(len(whole) == 6 and rest == [(6, 14), (7, 15)] and all(swap(no(DUAL[a]), 'other', 'no-other') == DUAL[b] for a, b in rest),
    '8 up is not, of each concept but same, with six of eight pairs; with 6 and 14, and with 7 and 15, no-other is no-other as written, and by not it is other')
say(no(DUAL[4]) == DUAL[8] == DUAL[12] and no(DUAL[8]) == DUAL[16] == DUAL[4], 'not, twice, is the same again: 4, prior-and-same, to 8 and 12, not-prior-and-same, to 16, prior-and-same')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
