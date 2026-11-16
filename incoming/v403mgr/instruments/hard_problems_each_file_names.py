"""Each hard problem of the Hard Problem Registry a living file names word for word, with the unchangeable it is
under and that unchangeable's seat: Exhibit ELEVEN Natural Medicine, and each other living file, by one reading.
Reads each living file, Exhibit ONE Natural Resolver, Exhibit FIVE Natural Engineering, and this session's table
of each hard problem, written by its own instrument out of Exhibit TWENTY-TWO Resolving the Hard Problem
Registry; executes; writes no file; decides nothing. Each answer is all or none at all, by each title and file.

Use: python3 -I incoming/v403mgr/instruments/hard_problems_each_file_names.py <root>          each check
     python3 -I incoming/v403mgr/instruments/hard_problems_each_file_names.py <root> csv      one line with each hard problem a file names
     python3 -I incoming/v403mgr/instruments/hard_problems_each_file_names.py <root> json     each file by the ten, for a sheet

A title is named with its words whole, capital letters or small: each title of two words or more, and each title
of one word but three, Aging, Dreaming and Sleep, each a word of other sentences too.

Returned at main, 16 November 2026, each check is:
  Thirteen living files name a hard problem of the registry, and eighteen name none; the two registries
  themselves are not read. Exhibit FIVE Natural Engineering names its own seventeen, and no other.
  Exhibit ELEVEN Natural Medicine names eleven: five with a two-way fixing to one side, two with a rate fixing as
  a value, and one each with a between fixing as a cut, a parity fixing as a magnitude, a completing fixing as a
  last and an opening fixing as a place; four of the ten unchangeables have none of medicine's eleven.
"""
import csv, glob, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
one = open(max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
T = [(int(r['its number in the Hard Problem Registry']), r['hard problem'], r['its unchangeable'], r['its now name'], r['its next name, 8 up'])
     for r in csv.DictReader(open(os.path.join(R, 'incoming/v403mgr/Each_hard_problem_by_its_seat.csv'), encoding='utf-8'))]
assert len(T) == 255
TEN = list(dict.fromkeys(t[2] for t in sorted(T, key=lambda t: t[0]))); assert len(TEN) == 10
NOT = {'Aging', 'Dreaming', 'Sleep'}
named = lambda text, title: re.search(r'(?<![A-Za-z])' + re.escape(title) + r'(?![A-Za-z])', text, re.I) is not None
newest = {}
for f in glob.glob(os.path.join(R, '*_v*.md')):
    stem = re.sub(r'_v\d+\w*\.md$', '', os.path.basename(f)); v = int(re.search(r'_v(\d+)', f).group(1))
    if stem not in newest or v > newest[stem][0]: newest[stem] = (v, f)
REG = ('Exhibit_TWENTY-ONE_Hard_Problem_Registry', 'Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry')
said = lambda stem: stem.replace('_', ' ')
HITS = {}
for stem in sorted(newest):
    if stem in REG: continue
    text = open(newest[stem][1], encoding='utf-8').read()
    HITS[stem] = [t for t in T if t[1] not in NOT and named(text, t[1])]
assert len(newest) == 33 and len(HITS) == 31

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['living file', 'a hard problem it names', 'its number in the Hard Problem Registry', 'its unchangeable', 'its now name', 'its next name, 8 up'])
    for stem, hits in HITS.items():
        for n, title, u, a, b in hits: w.writerow([said(stem), title, n, u, a, b])
    sys.exit()
if WHAT == 'json':
    json.dump({'ten': TEN, 'files': [[said(stem), len(hits)] + [sum(1 for h in hits if h[2] == u) for u in TEN] for stem, hits in HITS.items() if hits]}, sys.stdout); sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
withs = [s for s in HITS if HITS[s]]; nones = [s for s in HITS if not HITS[s]]
print(f'Each hard problem a living file names: {sum(len(v) for v in HITS.values())} namings in {len(withs)} files')
say(len(withs) == 13 and len(nones) == 18, 'thirteen living files name a hard problem of the registry, and eighteen name none; the two registries themselves are not read')
for s in withs: print(f"      {said(s)[:52]:52} {len(HITS[s]):3} · " + '; '.join(f"{u.split(' fixing')[0]} {sum(1 for h in HITS[s] if h[2] == u)}" for u in TEN if any(h[2] == u for h in HITS[s])))
eng = open(newest['Exhibit_FIVE_Natural_Engineering'][1], encoding='utf-8').read()
own = {int(n) for n in re.findall(r'(?m)^  - \*a\* (\d+) → §', eng.split('\n## 5.4 ', 1)[1].split('\n# ', 1)[0])}
say(own == {h[0] for h in HITS['Exhibit_FIVE_Natural_Engineering']} and len(own) == 17, 'Exhibit FIVE Natural Engineering names its own seventeen engineering hard problems, and no other of the registry')
med = HITS['Exhibit_ELEVEN_Natural_Medicine']; by = {u: [h[1] for h in med if h[2] == u] for u in TEN}
say(len(med) == 11 and len(by['a two-way fixing to one side']) == 5 and len(by['a rate fixing as a value']) == 2 and sorted(len(v) for v in by.values()) == [0, 0, 0, 0, 1, 1, 1, 1, 2, 5]
    and {u for u in TEN if not by[u]} == {'an observing fixing from behind', 'a same-existing fixing as a store', 'a middle fixing as an end', 'a sequencing fixing to one beat'},
    'Exhibit ELEVEN Natural Medicine names eleven: five with a two-way fixing to one side, two with a rate fixing as a value, one each with four more of the ten, and none with an observing fixing from behind, a same-existing fixing as a store, a middle fixing as an end or a sequencing fixing to one beat')
for u in TEN: print(f"      {u}: {'; '.join(by[u]) or 'none'}")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
