"""Each gathering file read with the table of the seventeen names: each naming of a name, each saying of one of
the ten unchangeables, and each seat said with two numbers, all or none at all as the table has it. A resource
for a session improving droplets with do no harm: it finds, and changes nothing.
Reads each gathering file, Exhibit ONE Natural Resolver and Exhibit TWENTY-TWO Resolving the Hard Problem
Registry; executes; writes no file; decides nothing.

Use: python3 -I incoming/v403mgr/instruments/gathering_files_read_with_the_table.py <root>                  each gathering file, and each finding
     python3 -I incoming/v403mgr/instruments/gathering_files_read_with_the_table.py <root> <a file's title>   one gathering file alone, as Natural_Naming
     python3 -I incoming/v403mgr/instruments/gathering_files_read_with_the_table.py <root> csv                one line with each finding

What it reads. A naming: a number, then now or next, then its words, as 9-next-co-discovering. With a number 1 to
17 it is the table's name of that number, or a finding. With a number past 17 it is that number's name sixteen
on, as 27 an 11, or a finding. An unchangeable: one of the ten in the seating's own words, or a finding; said
with two numbers, they are its seat's two, or a finding. A saying in italics is a mention, read all the same.

Returned at main, 16 November 2026: 1,535 namings in the gathering files; each with a number 1 to 17 is the
table's name but one, a dual; twenty-three are with a number past 17, twenty-two of them that number's name
sixteen on. Four sayings of an unchangeable are in other words than the seating's.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
one = living('Exhibit_ONE_Natural_Resolver'); hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
WORDS = {n: NAME[n].split('-', 1)[1] for n in NAME}
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10
TAILS = '|'.join(sorted({re.escape(u.split(' fixing ')[1]) for u in SEAT} | {'to a value'}))
files = sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md')))
if WHAT and WHAT != 'csv': files = [f for f in files if os.path.basename(f) == WHAT + '.md']; assert files, WHAT
FOUND, read = [], {'namings': 0, 'unchangeables': 0, 'seats': 0}
for f in files:
    title = os.path.basename(f)[:-3]
    for k, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
        for m in re.finditer(r'(?<![\w.-])(\d{1,4})-((?:now|next)-[a-z]+(?:-[a-z]+)*)', l):
            n = int(m.group(1)); read['namings'] += 1
            if n <= 17 and NAME[n] != m.group(0): FOUND.append((title, k, 'a naming not the table\'s name of its number', m.group(0), NAME[n]))
            if n > 17 and WORDS[(n - 1) % 16 + 1] != m.group(2): FOUND.append((title, k, "a naming past 17 not its number's name sixteen on", m.group(0), f'{n}-{WORDS[(n - 1) % 16 + 1]}'))
        for m in re.finditer(r'\b(an? [a-z-]+ fixing (?:' + TAILS + r'))(?:, with (\d+)(?:-[a-z-]+)? and (\d+))?', l):
            read['unchangeables'] += 1; u = m.group(1)
            if u not in SEAT:
                FOUND.append((title, k, "an unchangeable in other words than the seating's", u, next((s for s in SEAT if s.split(' fixing ')[1] == u.split(' fixing ')[1]), 'a rate fixing as a value' if u.endswith('to a value') else '')))
            elif m.group(2):
                read['seats'] += 1
                if SEAT[u] != (int(m.group(2)), int(m.group(3))): FOUND.append((title, k, 'an unchangeable with two numbers not its seat', m.group(0), f'{u}, with {SEAT[u][0]} and {SEAT[u][1]}'))
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n'); w.writerow(['gathering file', 'its line', 'the finding', 'as written', 'as the table has it']); w.writerows(FOUND); sys.exit()
print(f"{len(files)} gathering files read with the table: {read['namings']} namings, {read['unchangeables']} sayings of an unchangeable, {read['seats']} of them with two numbers")
kinds = {}
for x in FOUND: kinds.setdefault(x[2], []).append(x)
for kind, xs in kinds.items():
    print(f'  {kind}: {len(xs)}')
    for t, k, _, a, b in xs: print(f'      {t}, line {k}: {a} · the table: {b}')
if not FOUND: print('  each as the table has it')
