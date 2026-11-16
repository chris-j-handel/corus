"""Exhibit NINETEEN Natural Philosophy in the table: each of its seams and each of its dilemmas with the
unchangeable it names and that unchangeable's seat among the seventeen names.
Reads Exhibit NINETEEN Natural Philosophy, Exhibit TWENTY-TWO Resolving the Hard Problem Registry and Exhibit ONE
Natural Resolver; executes; writes no file; decides nothing. Each answer is all or none at all, by each seam
and each dilemma.

Use: python3 -I incoming/v403mgr/instruments/philosophy_by_its_seats.py <root>          each check
     python3 -I incoming/v403mgr/instruments/philosophy_by_its_seats.py <root> csv      one line with each dilemma
     python3 -I incoming/v403mgr/instruments/philosophy_by_its_seats.py <root> json     each seam, for a sheet

Returned at main, 16 November 2026, each check is:
  Thirty-seven seams: each of the twenty-nine from 3.9 names one of the ten unchangeables in its own Torusing in
  it, 3.25 two; the first eight name none in their own lines. Eight of the ten are with a seam; a parity fixing
  as a magnitude and a rate fixing as a value, the two seated with 7 and 15, are with no seam and no dilemma.
  Sixty-six dilemmas in seven branches: forty-one with one of the ten as the fixing each is at, twenty-five
  written none, no observing. Each dilemma reaching with a seam that names one of the ten has that seam's
  unchangeable.
"""
import csv, glob, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
phil = living('Exhibit_NINETEEN_Natural_Philosophy'); hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry'); one = living('Exhibit_ONE_Natural_Resolver')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10
TEN = '(' + '|'.join(re.escape(u) for u in SEAT) + ')'
tens = lambda text: [u for u in re.findall(TEN, text[0].lower() + text[1:] if text else '', re.I) for u in [u[0].lower() + u[1:]]]

# --- part THREE: each seam, and the unchangeable its own Torusing in it names
three = phil.split('\n# PART THREE', 1)[1].split('\n# PART FOUR', 1)[0]
parts = re.split(r'(?m)^## (3\.\d+) (.+)$', three); SEAMS = []
for i in range(1, len(parts), 3):
    tor = re.search(r'\*\*4\. Torusing in it\.\*\* (.*)', parts[i + 2])
    SEAMS.append(dict(number=parts[i], seam=parts[i + 1].strip(), ten=list(dict.fromkeys(tens(tor.group(1)))) if tor else [], said=list(dict.fromkeys(tens(parts[i + 2])))))
# --- part FIVE: each dilemma, by its branch, with the one coupling it splits, its register and the fixing it is at
five = phil.split('\n# PART FIVE', 1)[1]; D = []
for branch, body in re.findall(r'(?ms)^## (5\.\d+ [^\n]+)\n(.*?)(?=^## 5\.\d+ |\Z)', five):
    for dilemma, a, b, c in re.findall(r'(?m)^- \*\*(.+?)\*\*\n  - \*a\* (.*)\n  - \*b\* (.*)\n  - \*c\* (.*)$', body):
        D.append(dict(branch=branch.strip(), dilemma=dilemma, splits=a, register=b, fixing=c, ten=list(dict.fromkeys(tens(c))), seam=(re.search(r'reaches with (3\.\d+)', b) or [None, None])[1]))
of_seam = {s['number']: s for s in SEAMS}

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['its branch of philosophy', 'dilemma', 'the one coupling it splits', 'its register', 'the seam it reaches with', 'the fixing it is at, as written', 'its unchangeable, of ten', 'its now name', 'its next name, 8 up'])
    for d in D:
        t = d['ten'][0] if d['ten'] else ''
        w.writerow([d['branch'], d['dilemma'], d['splits'], d['register'], (d['seam'] + ' ' + of_seam[d['seam']]['seam']) if d['seam'] else '', d['fixing'], ' · '.join(d['ten']),
                    NAME[SEAT[t][0]] if t else '', NAME[SEAT[t][1]] if t else ''])
    sys.exit()
if WHAT == 'json':
    json.dump([[s['number'], s['seam'], ' · '.join(s['ten']), ' and '.join(f'{SEAT[t][0]} with {SEAT[t][1]}' for t in s['ten'])] for s in SEAMS], sys.stdout); sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print(f'Exhibit NINETEEN Natural Philosophy: {len(SEAMS)} seams; {len(D)} dilemmas in {len({d["branch"] for d in D})} branches')
late = [s for s in SEAMS if int(s['number'].split('.')[1]) >= 9]; early = [s for s in SEAMS if int(s['number'].split('.')[1]) < 9]
say(len(SEAMS) == 37 and all(s['ten'] for s in late) and all(not s['said'] for s in early) and [s['number'] for s in late if len(s['ten']) > 1] == ['3.25'],
    'thirty-seven seams: each of the twenty-nine from 3.9 names one of the ten in its own Torusing in it, 3.25 two; the first eight, 3.1 to 3.8, name none in their own lines')
by = {}
for s in SEAMS:
    for t in s['ten']: by.setdefault(t, []).append(s['number'] + ' ' + s['seam'])
say(len(by) == 8 and {t for t in SEAT if t not in by} == {'a parity fixing as a magnitude', 'a rate fixing as a value'} and SEAT['a parity fixing as a magnitude'] == SEAT['a rate fixing as a value'] == (7, 15)
    and not any(t in d['ten'] for d in D for t in ('a parity fixing as a magnitude', 'a rate fixing as a value')),
    'eight of the ten are with a seam; a parity fixing as a magnitude and a rate fixing as a value, the two seated with 7 and 15, are with no seam and with no dilemma')
for t in SEAT: print(f"      {t}, {SEAT[t][0]} and {SEAT[t][1]}: {'; '.join(by.get(t, [])) or 'none'}")
with_ten = [d for d in D if d['ten']]; others = sorted({d['fixing'] for d in D if not d['ten']})
say(len(D) == 66 and len(with_ten) == 41 and others == ['none, no observing'] and len({d['branch'] for d in D}) == 7,
    'sixty-six dilemmas in seven branches: forty-one with one of the ten as the fixing each is at, and twenty-five written none, no observing')
both = [d for d in D if d['seam'] and d['ten'] and of_seam[d['seam']]['ten']]
part = [d for d in both if not set(d['ten']) & set(of_seam[d['seam']]['ten'])]
say(not part, f'each dilemma reaching with a seam that names one of the ten has that seam\'s unchangeable, with {len(both)} such dilemmas')
for d in part: print(f"      parting: {d['dilemma']}, with {d['seam']}: here {'; '.join(d['ten'])}; the seam {'; '.join(of_seam[d['seam']]['ten'])}")
dby = {}
for d in with_ten: dby.setdefault(d['ten'][0], []).append(d['dilemma'])
for t in SEAT: print(f"      {t}: {len(dby.get(t, []))} dilemmas")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
