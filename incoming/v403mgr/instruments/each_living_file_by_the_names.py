"""Each living file by the names of the seventeen it has whole: one line with each of thirty-three living files,
a column with each name, the namings whole it has of that name, and each naming not Exhibit ONE's.
Reads each living file at the root; executes; writes no file; decides nothing. Each answer is all or none at
all, by each naming whole of each living file.

Use: python3 -I incoming/v403mgr/instruments/each_living_file_by_the_names.py <root>        each check
     python3 -I incoming/v403mgr/instruments/each_living_file_by_the_names.py <root> csv    one line with each living file

What it reads. A naming whole is a number, now or next, and its words, one hyphenation, as 2-now-possibling.
It is Exhibit ONE Natural Resolver's with its number 1 to 17 and that number's own words, a name sixteen on with a
number past 17 and the words of its number sixteen less, again and again, and else an other naming.

Returned at main, 16 November 2026, each check is:
  Thirty-three living files. Each naming whole is Exhibit ONE's or a name sixteen on, but one: 27-next-co-prioring,
  in Exhibit TWENTY-SIX Living File Registry's line of a version; Exhibit THREE Natural Numbers has 27 as
  27-next-co-observing. Ten living files have each of seventeen names whole, and ten have none: Exhibit FOUR
  Natural Mathematics, Exhibit NINE Natural Human Society, Exhibit TEN Natural Health, Exhibit ELEVEN Natural
  Medicine, Exhibit TWELVE Natural Explaining, Exhibit FOURTEEN Natural Destinies, Exhibit FIFTEEN Natural
  Emanating, Exhibit TWENTY-ONE Hard Problem Registry, Exhibit TWENTY-FIVE Living Society Registry and Exhibit
  THIRTY-ONE Me. Exhibit EIGHT Natural Exploring has the six names between selves and 12-next-co-same-existing,
  and no other. Exhibit SIX Natural Transmissioning and Exhibit TWENTY-THREE Natural Values each have 1 to 5, a
  self's five, and no other. Exhibit TWENTY-FOUR Geodesic Improving Method has the four possibling names with 11
  and 17. Each name is whole in eleven living files or more: 2-now-possibling in the most, eighteen, and
  15-next-observing in the fewest, eleven.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
ver = lambda f: int(re.search(r'_v(\d+)', f).group(1))
LIVING = {}
for p in glob.glob(os.path.join(R, '*_v*.md')):
    stem = re.sub(r'_v\d+[A-Za-z]*\.md$', '', os.path.basename(p))
    if stem not in LIVING or ver(p) > ver(LIVING[stem]): LIVING[stem] = p
one = open(LIVING['Exhibit_ONE_Natural_Resolver'], encoding='utf-8').read(); ill = open(LIVING['Exhibit_TWENTY-NINE_Natural_Illustrating'], encoding='utf-8').read()
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
WORD = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY',
        'TWENTY-ONE', 'TWENTY-TWO', 'TWENTY-THREE', 'TWENTY-FOUR', 'TWENTY-FIVE', 'TWENTY-SIX', 'TWENTY-SEVEN', 'TWENTY-EIGHT', 'TWENTY-NINE', 'THIRTY', 'THIRTY-ONE']
def order(stem):
    m = re.match(r'Exhibit_([A-Z-]+)_', stem); return (WORD.index(m.group(1)) if m else 0, stem)
def title(stem): return stem.replace('_', ' ')
ROWS = []
for stem in sorted(LIVING, key=order):
    t = open(LIVING[stem], encoding='utf-8').read(); c = {k: 0 for k in range(1, 18)}; on = []; other = []
    for nm in re.findall(r'(?<![\w-])(\d+-(?:now|next)-[a-z]+(?:-[a-z]+)*)(?![\w-])', t):
        k = int(nm.split('-')[0])
        if NAME.get(k) == nm: c[k] += 1
        elif k > 17 and NAME[(k - 1) % 16 + 1].split('-', 1)[1] == nm.split('-', 1)[1]: on.append(nm)
        else: other.append(nm)
    ROWS.append(dict(stem=stem, c=c, on=on, other=other, has={k for k in c if c[k]}))
BY = {r['stem']: r for r in ROWS}

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['living file', 'names of the seventeen it has whole'] + [NAME[k] for k in range(1, 18)] + ['its namings of a name sixteen on', 'its namings not Exhibit ONE Natural Resolver\'s'])
    for r in ROWS: w.writerow([title(r['stem']), len(r['has'])] + [r['c'][k] or '' for k in range(1, 18)] + [' · '.join(sorted(set(r['on']))), ' · '.join(sorted(set(r['other'])))])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print(f'{len(ROWS)} living files, each read for each naming whole')
others = [(r['stem'], nm) for r in ROWS for nm in r['other']]
say(len(ROWS) == 33 and others == [('Exhibit_TWENTY-SIX_Living_File_Registry', '27-next-co-prioring')] and '27-next-co-observing' in BY['Exhibit_THREE_Natural_Numbers']['on'],
    "each naming whole of each living file is Exhibit ONE Natural Resolver's name of its number or a name sixteen on, but one: 27-next-co-prioring, in Exhibit TWENTY-SIX Living File Registry; Exhibit THREE Natural Numbers has 27 as 27-next-co-observing")
allof = [r['stem'] for r in ROWS if len(r['has']) == 17]; none = [r['stem'] for r in ROWS if not r['has']]
say(len(allof) == 10 and len(none) == 10, f"ten living files have each of seventeen names whole: {'; '.join(title(s) for s in allof)}")
print(f"      with none, ten: {'; '.join(title(s) for s in none)}")
between = {int(x.split('-')[0]) for x in re.findall(r'\d+-(?:now|next)-[a-z-]+', ill.split("Exhibit ONE's six names between selves are:", 1)[1].split('.', 1)[0])}
say(between == {2, 6, 9, 10, 14, 17} and BY['Exhibit_EIGHT_Natural_Exploring']['has'] == between | {12},
    "Exhibit EIGHT Natural Exploring has the six names between selves, 2, 6, 9, 10, 14 and 17, with 12-next-co-same-existing, and no other name")
say(BY['Exhibit_SIX_Natural_Transmissioning']['has'] == BY['Exhibit_TWENTY-THREE_Natural_Values']['has'] == {1, 2, 3, 4, 5},
    "Exhibit SIX Natural Transmissioning and Exhibit TWENTY-THREE Natural Values each have 1 to 5, a self's five, and no other name")
poss = {k for k in range(1, 17) if 'possibling' in NAME[k]}
say(BY['Exhibit_TWENTY-FOUR_Geodesic_Improving_Method']['has'] == poss | {11, 17} and poss == {2, 6, 10, 14}, 'Exhibit TWENTY-FOUR Geodesic Improving Method has the four possibling names, 2, 6, 10 and 14, with 11-next-co-observing and 17-next-existing, and no other name')
files = {k: [r['stem'] for r in ROWS if r['c'][k]] for k in range(1, 18)}
most = max(files, key=lambda k: len(files[k])); fewest = min(files, key=lambda k: len(files[k]))
say(most == 2 and len(files[2]) == 18 and fewest == 15 and len(files[15]) == 11 and [k for k in files if len(files[k]) == 18] == [2] and [k for k in files if len(files[k]) == 11] == [15],
    f"each name is whole in eleven living files or more: {NAME[most]} in the most, {len(files[most])}, and {NAME[fewest]} in the fewest, {len(files[fewest])}")
print('      each name with how many living files have it whole: ' + ', '.join(f'{k} {len(files[k])}' for k in range(1, 18)))
part = [r for r in ROWS if 0 < len(r['has']) < 17]
print('      a living file with some names and not each:')
for r in part: print(f"        {title(r['stem'])}: {', '.join(map(str, sorted(r['has'])))}")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
