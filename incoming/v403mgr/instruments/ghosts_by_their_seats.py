"""Each entry of the Living Ghost Registry by its seats among the seventeen names: its ten unchangeables, each seated
with a name and that name 8 up, and its ten ghost positions. Reads Exhibit TWENTY-SEVEN Living Ghost Registry's
entries, each one's two lines of signature as they are, and Exhibit TWENTY-TWO Resolving the Hard Problem Registry's
sentence of the ten in sequence; executes; writes no file; decides nothing. Each answer is all or none at all.

Use: python3 -I incoming/v403mgr/instruments/ghosts_by_their_seats.py <root>         each entry, and each check
     python3 -I incoming/v403mgr/instruments/ghosts_by_their_seats.py <root> json    the entries, for a sheet

An entry's signature names an unchangeable by its gathering, store-seeking or value-pinning; an unchangeable not
named in it is not read as absent from the observing, only as not in the entry's line.

Returned at main, 16 November 2026, each check is:
  Thirteen entries. Each has premature closure among its ghost positions. No entry has criterion-regressing: the
  seat of an opening fixing as a place, 1-now-existing and 9-next-co-discovering, has no entry.
  Of molecular chemistry's seven entries, entropy, equilibrium, the single native state and the single catalytic
  transition-state stroke have value-pinning; each of medicine's three has value-pinning and line-demanding. The
  seat they share is a rate fixing as a value, 7-now-observing and 15-next-observing.
"""
import glob, json, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
ghosts = living('Exhibit_TWENTY-SEVEN_Living_Ghost_Registry'); hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry')
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10
# the registry's own table: each unchangeable with its gathering
GATHER = {}
for l in ghosts.split('\n'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) == 2 and c[1].endswith(('-seeking', '-regressing', '-enumerating', '-reaching', '-demanding', '-pinning', '-forcing')): GATHER[c[1]] = c[0]
assert len(GATHER) == 10
KEY = {'origin-seeking': 'from behind', 'criterion-regressing': 'as a place', 'space-enumerating': 'as a last', 'store-seeking': 'as a store', 'interior-reaching': 'as an end',
       'magnitude-demanding': 'as a magnitude', 'order-demanding': 'to one beat', 'value-pinning': 'as a value', 'choice-forcing': 'to one side', 'line-demanding': 'as a cut'}
for g, tail in KEY.items(): assert GATHER[g].endswith(tail), (g, GATHER[g])
FIX = {g: next(k for k in SEAT if k.endswith(tail)) for g, tail in KEY.items()}
POS = ['false inclusion', 'false exclusion', 'novelty erasing', 'tradition blocking', 'imposing affirmation', 'imposing departure',
       'premature closure', 'permanent indeterminacy', 'false failure', 'false success']
parts = re.split(r'(?m)^## (5\.\d+) (.+)$', ghosts); E = {}
for i in range(1, len(parts), 3):
    body = parts[i + 2].split('\n## ')[0]
    u = next(l for l in body.split('\n') if l.startswith('**Ten-unchangeable signature.**')); p = next(l for l in body.split('\n') if l.startswith('**Ten-position signature.**'))
    E[parts[i + 1].strip()] = ([g for g in KEY if re.search(g, u, re.I)], [x for x in POS if re.search(x, p, re.I)])
CHEMISTRY = ['Entropy', 'Equilibrium', 'Electron', 'The single native state', 'The single catalytic transition-state stroke', 'Proton', 'Element']
MEDICINE = ['Minimal residual disease', 'Diagnostic code as the disease', 'Homeostasis']
assert all(x in E for x in CHEMISTRY + MEDICINE)
if WHAT == 'json':
    json.dump({'unchangeables': [[g, FIX[g], list(SEAT[FIX[g]])] for g in KEY], 'positions': POS, 'entries': [[n, u, p] for n, (u, p) in E.items()]}, sys.stdout, ensure_ascii=False); sys.exit()
say = lambda ok, label: print(f'  {"is" if ok else "is-not"} · {label}')
print(f'{len(E)} entries, each by its ten unchangeables in the order of their seating, and its ghost positions:')
for n, (u, p) in E.items(): print(f'  {n[:44]:44s} ' + ''.join('X' if g in u else '.' for g in KEY) + '  ' + ''.join('X' if x in p else '.' for x in POS))
print('Each check, all or none at all, of the entries\' own lines:')
say(all('premature closure' in p for u, p in E.values()), 'each entry has premature closure among its ghost positions')
say(all('criterion-regressing' not in u for u, p in E.values()), 'no entry has criterion-regressing: the seat of an opening fixing as a place, 1-now-existing and 9-next-co-discovering, has no entry')
with_value = [n for n in CHEMISTRY if 'value-pinning' in E[n][0]]
say(with_value == ['Entropy', 'Equilibrium', 'The single native state', 'The single catalytic transition-state stroke'], 'of molecular chemistry\'s seven entries, four have value-pinning: entropy, equilibrium, the single native state, the single catalytic transition-state stroke')
say(all({'value-pinning', 'line-demanding'} <= set(E[n][0]) for n in MEDICINE), 'each of medicine\'s three entries has value-pinning and line-demanding')
say(SEAT[FIX['value-pinning']] == (7, 15) and SEAT[FIX['line-demanding']] == (5, 13), 'value-pinning is a rate fixing as a value, with 7-now-observing and 15-next-observing; line-demanding is a between fixing as a cut, with 5-now-co-existing and 13-next-discovering')
print('  each unchangeable with the entries having it:')
for g in KEY: print(f'    {FIX[g]}, {SEAT[FIX[g]][0]} and {SEAT[FIX[g]][1]}: {sum(1 for u, p in E.values() if g in u)} of {len(E)}')
