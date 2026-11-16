"""Exhibit FIVE Natural Engineering in the table: each engineering case with its properties, as it is written,
and each engineering hard problem with the unchangeable it is under and that unchangeable's seat.
Reads Exhibit FIVE Natural Engineering, Exhibit TWENTY-TWO Resolving the Hard Problem Registry and Exhibit ONE
Natural Resolver, and this session's table of each hard problem, written by its own instrument out of Exhibit
TWENTY-TWO; executes; writes no file; decides nothing. Each answer is all or none at all, by each entry.

Use: python3 -I incoming/v403mgr/instruments/engineering_by_its_seats.py <root>          each check
     python3 -I incoming/v403mgr/instruments/engineering_by_its_seats.py <root> csv      one line with each engineering case
     python3 -I incoming/v403mgr/instruments/engineering_by_its_seats.py <root> json     each engineering hard problem, for a sheet

Returned at main, 16 November 2026, each check is:
  Twenty-four engineering cases, each with each of four properties: arrangement and goal; its particular coupling
  and fixing form; residue; observing. Each has one alone of a fifth: a proposal's arrangement and remaining work,
  with twelve, or an arrangement sharing, with twelve.
  Seventeen engineering hard problems, 5.4: each has one of the ten unchangeables with the two names Exhibit
  TWENTY-TWO Resolving the Hard Problem Registry seats it with, and each is under the unchangeable its number is
  under in that registry. Eight of the ten have one or more; an observing fixing from behind and a sequencing
  fixing to one beat have none.
"""
import csv, glob, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
eng = living('Exhibit_FIVE_Natural_Engineering'); hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry'); one = living('Exhibit_ONE_Natural_Resolver')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10

# --- each engineering case: a list of properties, one or two cases with each list
lines = eng.split('\n'); CASES = []; section = ''
i = 0
while i < len(lines):
    l = lines[i]
    if l.startswith('## '): section = l[3:].strip()
    m = re.match(r'Each entry: \*\*Property\*\* · (.+)$', l)
    if m:
        cols = dict(re.findall(r'\*([a-z])\* ([^·]+?)(?= · |$)', m.group(1)))
        lead = next((lines[k] for k in range(i - 1, max(i - 8, 0), -1) if lines[k].startswith('**')), '')
        lead = re.sub(r'\*\*', '', lead.split('.**')[0].split('**')[1] if lead.startswith('**') else '')
        props = {c: {} for c in cols}; j = i + 1; prop = None
        while j < len(lines) and not lines[j].startswith(('#', 'Each entry:', '---')) and (lines[j].startswith(('- **', '  - *')) or not lines[j].strip()):
            pm = re.match(r'- \*\*(.+?)\*\*', lines[j]); cm = re.match(r'  - \*([a-z])\* (.*)$', lines[j])
            if pm: prop = pm.group(1)
            elif cm and prop and cm.group(1) in props: props[cm.group(1)][prop] = cm.group(2)
            j += 1
        for c in cols:
            if 'Its particular coupling and fixing form' in props[c]:
                CASES.append(dict(section=section, lead=lead, case=cols[c].strip(), props=props[c]))
        i = j
    else: i += 1
PROPS = ['Arrangement and goal', 'Its particular coupling and fixing form', 'Residue', 'Observing', "Proposal's arrangement and remaining work", 'Arrangement sharing']

# --- 5.4, engineering hard problems: each with its number of Exhibit TWENTY-ONE, its section of Exhibit TWENTY-TWO, and one of the ten
b54 = eng.split('\n## 5.4 ', 1)[1].split('\n# ', 1)[0]
HP = [dict(observing=o, number=int(n), section=s, ten=t, a=int(a), b=int(b), receiving=r) for o, n, s, t, a, b, r in
      re.findall(r'(?m)^- \*\*(.+?)\*\*\n  - \*a\* (\d+) → §([\d.]+); (an? [a-z-]+ fixing [a-z ]+?), with (\d+)-[a-z-]+ and (\d+)-[a-z-]+\n  - \*b\* (.+)$', b54)]
table = {int(r['its number in the Hard Problem Registry']): r for r in csv.DictReader(open(os.path.join(R, 'incoming/v403mgr/Each_hard_problem_by_its_seat.csv'), encoding='utf-8'))}
key = 'its unchangeable'

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(["its section of Exhibit FIVE Natural Engineering", 'its opening sentence', 'engineering case'] + [p[0].lower() + p[1:] for p in PROPS])
    for c in CASES: w.writerow([c['section'], c['lead'], c['case']] + [c['props'].get(p, '') for p in PROPS])
    sys.exit()
if WHAT == 'json':
    json.dump([[h['observing'], h['number'], table[h['number']]['hard problem'] if 'hard problem' in table[h['number']] else '', '§' + h['section'], h['ten'], NAME[h['a']], NAME[h['b']],
                table[h['number']][key], h['receiving']] for h in HP], sys.stdout, ensure_ascii=False); sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print(f'Exhibit FIVE Natural Engineering: {len(CASES)} engineering cases with a list of properties; {len(HP)} engineering hard problems')
four = PROPS[:4]
say(all(all(p in c['props'] for p in four) for c in CASES), f'each of the {len(CASES)} cases has each of four properties: arrangement and goal; its particular coupling and fixing form; residue; observing')
fifth = [c for c in CASES if PROPS[4] in c['props']]; sharing = [c for c in CASES if PROPS[5] in c['props']]
say(all((PROPS[4] in c['props']) != (PROPS[5] in c['props']) for c in CASES), f"each has one alone of a fifth: a proposal's arrangement and remaining work, with {len(fifth)}, or an arrangement sharing, with {len(sharing)}")
for c in CASES: print(f"      {c['section'][:44]:44} · {c['case'][:60]}")
print('Its engineering hard problems, 5.4:')
say(all(h['ten'] in SEAT and SEAT[h['ten']] == (h['a'], h['b']) for h in HP) and len(HP) > 0,
    'each has one of the ten unchangeables, with the two names Exhibit TWENTY-TWO Resolving the Hard Problem Registry seats it with')
part = [h for h in HP if table[h['number']][key] != h['ten']]
say(not part, "each is under the unchangeable its number is under in Exhibit TWENTY-TWO Resolving the Hard Problem Registry, by this session's table of each hard problem")
for h in part: print(f"      parting: {h['observing']}, {h['number']}: here {h['ten']}; in the table {table[h['number']][key]}")
by = {}
for h in HP: by.setdefault(h['ten'], []).append(h['observing'])
for t in SEAT: print(f"      {t}, {SEAT[t][0]} and {SEAT[t][1]}: {'; '.join(by.get(t, [])) or 'none'}")
say(len(HP) == 17 and len(by) == 8 and {t for t in SEAT if t not in by} == {'an observing fixing from behind', 'a sequencing fixing to one beat'},
    'seventeen engineering hard problems; eight of the ten unchangeables have one or more, and two have none: an observing fixing from behind, with 2 and 10, and a sequencing fixing to one beat, with 4 and 12')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
