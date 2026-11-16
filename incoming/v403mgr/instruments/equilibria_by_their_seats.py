"""Each observing of Exhibit TWENTY-EIGHT Equilibria Registry, a conception of equilibria as it is written, by
the unchangeable it is with and that unchangeable's seat among the seventeen names.
Reads Exhibit TWENTY-EIGHT Equilibria Registry, Exhibit TWENTY-TWO Resolving the Hard Problem Registry, Exhibit
ONE Natural Resolver and Exhibit FOUR Natural Mathematics; executes; writes no file; decides nothing.
Each answer is all or none at all, by each observing and by each name.

Use: python3 -I incoming/v403mgr/instruments/equilibria_by_their_seats.py <root>        each check
     python3 -I incoming/v403mgr/instruments/equilibria_by_their_seats.py <root> csv    one line with each observing

Returned at main, 16 November 2026, each check is:
  Sixty-three observings, forty-two conceptions selves propose and twenty-one specifying accounts and prior
  definitions, no one twice; each of ten has as many as its heading says, and each parting within it as many
  as its own line says.
  Each of the ten has in Exhibit TWENTY-EIGHT Equilibria Registry the two names it has in Exhibit TWENTY-TWO
  Resolving the Hard Problem Registry, a name and that name 8 up.
  The table of fields at ten has each observing once, with the one of ten its own entry is under.
  The four binaries, now, existing, same and all, each with two names of 1 to 8 and those names 8 up, are the
  four forms of two parities of the reflected order, the third and the second, one changing from each binary
  to its next and round to the first: a cycle of four.
  8 up brings each of the ten onto its own seat. 9 less and 17 less each bring each of now onto one of all and
  each of existing onto one of same: an opening with a same-existing, an observing with a parity and a rate,
  a two-way with a completing, a sequencing with a between and a middle.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
eq = living('Exhibit_TWENTY-EIGHT_Equilibria_Registry'); hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry')
one = living('Exhibit_ONE_Natural_Resolver'); four = living('Exhibit_FOUR_Natural_Mathematics')
for text, said in ((eq, 'Sixty-three observings, forty-two conceptions selves propose and twenty-one specifying accounts and prior definitions'),
                   (eq, '17 less (9 less n) being **n + 8**'), (four, 'With two parities a cycle is four'), (four, 'the reflected binary code')):
    assert said in text, said
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))

# --- the ten, each with its two names: Exhibit TWENTY-TWO's seating
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10
FOLD4 = {'A reference fixing unchangeable': ('an observing fixing from behind', 'a completing fixing as a last', 'a middle fixing as an end'),
         'A rate fixing unchangeable': ('a sequencing fixing to one beat', 'a rate fixing as a value'),
         'A magnitude, a build driving it': ('a parity fixing as a magnitude', 'a two-way fixing to one side'),
         'A parity going along, entering as cost': ('an opening fixing as a place', 'a same-existing fixing as a store', 'a between fixing as a cut')}
for k, v in FOLD4.items(): assert f'**{k}** — ' + v[0] in hard, k
four_of = lambda u: next(k for k, v in FOLD4.items() if u in v)

# --- Exhibit TWENTY-EIGHT, 3.3: four binaries, each with two names now and those names 8 up, and the ten with them
b33 = eq.split('\n## 3.3 ', 1)[1].split('\n## 3.4 ', 1)[0]
BINARY, TEN33 = {}, {}
for binary, a, b in re.findall(r'^- \*\*(now|existing|same|all)\*\*\n  - \*a\* (.+)\n  - \*b\* (.+)$', b33, re.M):
    for n in re.findall(r'(\d+)-', a): BINARY[int(n)] = binary
    for chunk in b.split(';'):
        m = re.search(r'with (\d+) · (\d+)', chunk)
        for what in re.findall(r'an? [a-z-]+ fixing [a-z ]+?(?= and |,)', chunk): TEN33[what.strip()] = (int(m.group(1)), int(m.group(2)))
assert sorted(BINARY) == list(range(1, 17)) and len(TEN33) == 10, (BINARY, TEN33)

# --- Exhibit TWENTY-EIGHT, 4.3 to 4.12: each observing, under its one of ten and its parting
body = eq.split('\n## 4.3 ', 1)[1].split('\n## 4.13 ', 1)[0]
E, HEAD, PARTING = [], {}, []
for title, count, text in re.findall(r'(?ms)^(?:## 4\.\d+ )?(An? [a-z-]+ fixing [a-z ]+?), (\d+) observings\n(.*?)(?=^## 4\.\d+ |\Z)', '## 4.3 ' + body):
    ten = title[0].lower() + title[1:]; assert ten in SEAT, ten
    HEAD[ten] = int(count)
    for kind, k, part in re.findall(r'(?ms)^\*\*(A [a-z, ]+?) fixing unchangeable\*\*, (\d+)\.\n(.*?)(?=^\*\*A [a-z, ]+? fixing unchangeable\*\*, \d+\.|\Z)', text):
        got = re.findall(r'(?m)^- \*\*((?:NY|SA)\d+)\*\* · (.+)\n  - \*a\* (.*)\n  - \*b\* (.*)\n  - \*c\* (.*)\n  - \*d\* (.*)$', part)
        PARTING.append((ten, kind, int(k), len(got)))
        for code, words, field, changing, subject, adds in got:
            E.append(dict(code=code, words=words, ten=ten, kind=kind[0].lower() + kind[1:], field=field, changing=changing, subject=subject, adds=adds))

# --- Exhibit TWENTY-EIGHT, 4.13: fields at ten
f413 = eq.split('\n## 4.13 ', 1)[1].split('\n## 4.14 ', 1)[0]
order = re.search(r'\*a\* 1 (\w[\w-]*) · \*b\* 2 (\w[\w-]*) · \*c\* 3 (\w[\w-]*) · \*d\* 4 (\w[\w-]*) · \*e\* 5 (\w[\w-]*) · \*f\* 6 (\w[\w-]*) · \*g\* 7 (\w[\w-]*) · \*h\* 8 (\w[\w-]*) · \*j\* 9 (\w[\w-]*) · \*k\* 10 (\w[\w-]*)', f413).groups()
LETTER = dict(zip('abcdefghjk', (next(u for u in SEAT if re.match(r'an? ' + re.escape(w) + ' fixing', u)) for w in order)))
FIELDS = []                                                   # (subject and its fields, one of ten, observing)
for subject, rows in re.findall(r'(?ms)^- \*\*(.+?)\*\*\n(.*?)(?=^- \*\*|\Z)', f413):
    for letter, codes in re.findall(r'(?m)^  - \*([a-k])\* (.*)$', rows):
        FIELDS += [(subject, LETTER[letter], c) for c in re.findall(r'(?:NY|SA)\d+', codes)]

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['observing', 'its own words', 'the unchangeable it is with, of ten', 'seated with, now', 'and 8 up, next', 'its binary of four', 'ten fold to four: its fixing by a coarser grain',
                'what is fixing unchangeable', 'a conception a self proposes, or a specifying account', 'field', 'the changing it has', 'subject', 'one conception, a further one, or another claim',
                'its subject and fields, in the table of fields at ten'])
    for e in E:
        a, b = SEAT[e['ten']]
        w.writerow([e['code'], e['words'], e['ten'], NAME[a], NAME[b], BINARY[a], four_of(e['ten']), e['kind'], 'a conception a self proposes' if e['code'].startswith('NY') else 'a specifying account or a prior definition',
                    e['field'], e['changing'], e['subject'], '' if e['adds'] == '—' else e['adds'], ' · '.join(s for s, t, c in FIELDS if c == e['code'])])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
codes = [e['code'] for e in E]
print(f'Exhibit TWENTY-EIGHT Equilibria Registry: {len(E)} observings under ten')
say(len(codes) == 63 == len(set(codes)) and sum(c.startswith('NY') for c in codes) == 42 and sum(c.startswith('SA') for c in codes) == 21,
    'sixty-three observings, forty-two conceptions selves propose and twenty-one specifying accounts and prior definitions, no one twice')
say(all(HEAD[u] == sum(e['ten'] == u for e in E) for u in SEAT) and len(HEAD) == 10 and all(k == got for _, _, k, got in PARTING),
    'each of ten has as many observings as its heading says, and each parting within it as many as its own line says')
say(TEN33 == SEAT, 'each of the ten has in this registry the two names it has in Exhibit TWENTY-TWO Resolving the Hard Problem Registry, a name and that name 8 up')
say(sorted(c for _, _, c in FIELDS) == sorted(codes) and all(t == next(e['ten'] for e in E if e['code'] == c) for _, t, c in FIELDS),
    'the table of fields at ten has each observing once, with the one of ten its own entry is under')
for u in SEAT:
    mine = [e for e in E if e['ten'] == u]
    print(f'      {u}, {SEAT[u][0]} and {SEAT[u][1]}, {BINARY[SEAT[u][0]]}: ' + '; '.join(f'{k}: {" ".join(e["code"] for e in mine if e["kind"] == k)}' for k in dict.fromkeys(e['kind'] for e in mine)))

print('The four binaries and the three moves:')
G = lambda n: (n - 1) ^ ((n - 1) >> 1); par = lambda n, k: (G(n) >> (k - 1)) & 1
form = {b: {(par(n, 3), par(n, 2)) for n in range(1, 9) if BINARY[n] == b} for b in ('now', 'existing', 'same', 'all')}
ring = ['now', 'existing', 'same', 'all']
say(all(len(v) == 1 for v in form.values()) and len({next(iter(v)) for v in form.values()}) == 4 and all(BINARY[n] == BINARY[n + 8] for n in range(1, 9))
    and all(sum(x != y for x, y in zip(next(iter(form[ring[i]])), next(iter(form[ring[(i + 1) % 4]])))) == 1 for i in range(4)),
    'the four binaries, now, existing, same and all, each with two names of 1 to 8 and those names 8 up, are the four forms of two parities, the third and the second, one changing from each binary to its next and round to the first: a cycle of four')
moves = {'9 less': lambda n: (9 if n < 9 else 25) - n, '17 less': lambda n: 17 - n, '8 up': lambda n: n + 8 if n < 9 else n - 8}
of = lambda n: frozenset(u for u, s in SEAT.items() if n in s)
say(all(of(moves['8 up'](n)) == of(n) for n in range(1, 17)), '8 up brings each of the ten onto its own seat')
swap = {'now': 'all', 'all': 'now', 'existing': 'same', 'same': 'existing'}
say(all(BINARY[moves[m](n)] == swap[BINARY[n]] for m in ('9 less', '17 less') for n in range(1, 17)),
    '9 less and 17 less each bring each of now onto one of all, and each of existing onto one of same')
for a in (1, 2, 3, 4):
    print(f'      9 less, {a} with {9 - a}: {" and ".join(sorted(of(a)))} with {" and ".join(sorted(of(9 - a)))}')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
