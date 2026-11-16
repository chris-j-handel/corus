"""Exhibit TWO Natural Networking in the table: each of its tables and lists of the seventeen names, read line
by line with the names' own moves and with Exhibit ONE Natural Resolver's fields.
Reads Exhibit TWO Natural Networking and Exhibit ONE Natural Resolver; executes; writes no file; decides
nothing. Each answer is all or none at all, by each line of each table.

Use: python3 -I incoming/v403mgr/instruments/networking_by_the_names.py <root>          each check
     python3 -I incoming/v403mgr/instruments/networking_by_the_names.py <root> csv      one line with each line read

Returned at main, 16 November 2026, each check is:
  Forty-three lines of ten tables and lists of the file's first part, each as the names' own moves and Exhibit
  ONE Natural Resolver's table have it. The six connector names are 2, 6, 9, 10, 14 and 17, each sharing end with
  its observing end, 6 to 2, 10 to 14 and 9 to 17. Each line of eight on is 8 up; each podal line 9 less; each
  local fold 9 less as 8 up and then 17 less. Four across openings have a spacing, twice it, and four of it and
  one, 9, 17 and 25, each a fold's own number. Each wider row is four names of one root.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
net = living('Exhibit_TWO_Natural_Networking'); one = living('Exhibit_ONE_Natural_Resolver')
NAME, ROOT = {}, {}
for n, name, root in re.findall(r'^\| (\d+) \| \*\*([^*]+)\*\* \| ([^|]+?) \|', one, re.M): NAME[int(n)], ROOT[int(n)] = name, root.split(',')[0]
assert sorted(NAME) == list(range(1, 18))
L = net.split('\n')
def table(head):                                             # the rows of the table with this header line
    i = next(k for k, l in enumerate(L) if l.startswith(head)); rows = []
    for l in L[i + 2:]:
        if not l.startswith('|'): break
        rows.append([c.strip() for c in l.strip('|').split('|')])
    return rows
def entries(head):                                           # the entries of the list with this header: its name, and each lettered part
    i = next(k for k, l in enumerate(L) if l.replace('**', '').startswith('Each entry: ' + head)); out = []; j = i + 1
    while j < len(L) and (not L[j].strip() or L[j].startswith(('- **', '  - *'))):
        m = re.match(r'- \*\*(.+?)\*\*(.*)$', L[j])
        if m:
            e = {'name': m.group(1)}; e.update(dict(re.findall(r'\*([a-z])\* ([^·]+?)(?= · |$)', m.group(2)))); out.append(e)
        c = re.match(r'  - \*([a-z])\* (.*)$', L[j])
        if c and out: out[-1][c.group(1)] = c.group(2)
        j += 1
    return out
num = lambda s: [int(x) for x in re.findall(r'(?<![\w.])(\d+)(?:-(?:now|next)-[a-z-]+)?', s)]
up8 = lambda n: n + 8; less9 = lambda n: 9 - n; less17 = lambda n: 17 - n

READ = []                                                    # each line read: where, as written, the relation executed, is
def line(where, written, relation, ok): READ.append((where, written, relation, ok))

# 1 · six connector names
con = entries('Connector')
for e in con:
    n = num(e['name'])[0]; other = num(e['b'])[0]; sharing = e['a'].startswith('sharing'); across = 'across' in e['a']
    line('six connector names', f"{e['name']} · {e['a']} · {e['b']}", f"{'even, root possibling, across' if across else 'odd, along'}; its other end {NAME[other]}",
         (n % 2 == 0) == across and (ROOT[n] == 'possibling') == across and {n, other} in ({2, 6}, {10, 14}, {9, 17}) and next(num(x['b'])[0] for x in con if num(x['name'])[0] == other) == n
         and next(x['a'].startswith('sharing') for x in con if num(x['name'])[0] == other) != sharing)
# 2 · eight on
for a, b in table('| One through nine | Eight on |'):
    line('one through nine, eight on', f'{a} | {b}', '8 up', num(b)[0] == up8(num(a)[0]))
# 3 · podal within 1 to 8
for a, b in table('| Name | Podal within 1 to 8, 9 less |'):
    line('podal within 1 to 8, 9 less', f'{a} | {b}', '9 less', num(b)[0] == less9(num(a)[0]))
# 4 · a local fold and its first larger going-and-returning
for a, b in table('| Local fold | Its first larger going-and-returning |'):
    x, y = num(a); p, q, r = num(b)
    line('a local fold, and its first larger going and returning', f'{a} | {b}', '9 less is 8 up and then 17 less', y == less9(x) and p == x and q == up8(x) and r == less17(q) == y)
# 5 · co-bi-exchanging, and prior and now
for k, (label, a, b) in enumerate(table('| Co-bi-exchanging | Self\'s opening–completing | Other\'s opening–completing |'), 1):
    line('co-bi-exchanging', f'{label} | {a} | {b}', "a self's two names, and its other's one on", num(a) == [2 * k - 1, 2 * k] and num(b) == [2 * k, 2 * k + 1])
# 6 · a relation through its unfolding
for e in entries('Relation through its unfolding'):
    a, b = num(e['a']), num(e['b'])
    line('a relation through its unfolding', f"{e['name']} · {e['a']} · {e['b']}", 'an even name and its next odd; the two spans 8 up from each other',
         a[0] % 2 == 0 and a[1] == a[0] + 1 and b == [up8(a[0]), up8(a[1])])
# 7 · four across openings
for e in entries('Four across openings'):
    ns = num(e['name']); s = ns[1] - ns[0]
    line('four across openings', f"{e['name']} · spacing {e['a']} · halfway {e['b']} · odd completing {e['c']}", 'spacing, twice it, and four of it and one: a fold\'s 9, 17, 25',
         all(y - x == s for x, y in zip(ns, ns[1:])) and int(e['a']) == s and int(e['b']) == 2 * s and int(e['c']) == 4 * s + 1)
# 8 · wider rows
for e in entries('Wider row'):
    ns = num(e['name'])
    line('wider rows', f"{e['name']} · {e['a'][:80]}", 'one root with the four: ' + ROOT[ns[0]], len({ROOT[n] for n in ns}) == 1 and all(y - x == 4 for x, y in zip(ns, ns[1:])))
# 9 · with a between, eight on
for e in entries('With a between'):
    line('with a between, and within, eight on', f"{e['name']} · {e['b']}", '8 up', num(e['b'])[0] == up8(num(e['name'])[0]))
# 10 · direction with a sharing coupling
for label, a, b in table('| Direction with a sharing coupling | Sharing | Observing |'):
    line('direction with a sharing coupling', f'{label} | {a} | {b}', 'a sharing end to its observing end, as the connectors have them',
         (num(a)[0], num(b)[0]) in {(num(x['name'])[0], num(x['b'])[0]) for x in con if x['a'].startswith('sharing')})

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(["a table or a list of Exhibit TWO Natural Networking", 'its line, as written', 'the relation among names, executed', 'is, or is-not'])
    w.writerows([a, b, c, 'is' if ok else 'is-not'] for a, b, c, ok in READ); sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print(f"Exhibit TWO Natural Networking, its first part's tables and lists of names: {len(READ)} lines read")
groups = {}
for a, b, c, ok in READ: groups.setdefault(a, []).append(ok)
SAID = {'six connector names': 'the six connector names are 2, 6, 9, 10, 14 and 17: each across one even and of root possibling, each along one odd; each sharing end has its observing end, 6 to 2, 10 to 14 and 9 to 17',
        'one through nine, eight on': 'each of nine lines is 8 up, 1 to 9 on to 9 to 17',
        'podal within 1 to 8, 9 less': 'each of four lines is 9 less',
        'a local fold, and its first larger going and returning': 'each of four lines has 9 less as 8 up and then 17 less',
        'co-bi-exchanging': "each of four lines has a self's two names and its other's one on, nine places together",
        'a relation through its unfolding': 'each of three lines has an even name and its next odd, and its other span 8 up',
        'four across openings': "each line's spacing, halfway and odd completing are its spacing, twice it, and four of it and one: 9, 17 and 25, each a fold's own number",
        'wider rows': 'each wider row is four names of one root, 4 apart: possibling, and same-existing',
        'with a between, and within, eight on': 'each line has its name 8 up',
        'direction with a sharing coupling': 'each of two lines is a sharing end to its observing end, as the connectors have them'}
for g, oks in groups.items(): say(all(oks), f'{SAID[g]} · {len(oks)} lines')
say({num(e['name'])[0] for e in con} == {2, 6, 9, 10, 14, 17} and len(READ) == sum(len(v) for v in groups.values()) and all(ok for *_, ok in READ),
    "each line read of Exhibit TWO Natural Networking's tables and lists of names is as the names' own moves and Exhibit ONE Natural Resolver's table have it: the two files cohere")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
