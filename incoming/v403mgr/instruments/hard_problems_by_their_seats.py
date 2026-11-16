"""Each hard problem by its seat among the seventeen names. Reads Exhibit TWENTY-TWO Resolving the Hard Problem
Registry's ten parts, each an unchangeable with its two names and each hard problem under it with its number, and
Exhibit TWENTY-ONE Hard Problem Registry's entries; executes; writes no file; decides nothing.

Use: python3 -I incoming/v403mgr/instruments/hard_problems_by_their_seats.py <root>        each part, and each check
     python3 -I incoming/v403mgr/instruments/hard_problems_by_their_seats.py <root> csv    each hard problem, a line

Returned at main, 16 November 2026, each check is:
  255 hard problems under ten unchangeables, each under one and no more: from behind 33, as a place 24, as a last
  33, as a store 9, as an end 25, as a magnitude 19, to one beat 20, as a value 16, to one side 43, as a cut 33.
  By seat: 1 and 9, 24; 2 and 10, 33; 3 and 11, 43; 4 and 12, 20; 5 and 13, 58; 6 and 14, 33; 7 and 15, 35;
  8 and 16, 9. Each is an entry of Exhibit TWENTY-ONE Hard Problem Registry but 172, of no entry; each entry is
  under one of the ten but 166, under part twelve. Each entry has its line of a conserving relation, a conserving
  reach, a reach, an unreachability and a persistence, each in the table with its seat; an unreachability has its
  words with 174 entries and none with 81. 160 of 255 conserving reaches open with a whole.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
resolving = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry'); registry = living('Exhibit_TWENTY-ONE_Hard_Problem_Registry')
FOLD4 = {'A reference fixing unchangeable': ('from behind', 'as a last', 'as an end'), 'A rate fixing unchangeable': ('to one beat', 'as a value'),
         'A magnitude, a build driving it': ('as a magnitude', 'to one side'), 'A parity going along, entering as cost': ('as a place', 'as a store', 'as a cut')}
parts, rows, part = [], [], None
for l in resolving.split('\n'):
    m = re.match(r'# (\d+) (.+?) — (\d+-[a-z-]+) and (\d+-[a-z-]+)$', l)
    if m: part = (int(m.group(1)), m.group(2), m.group(3), m.group(4)); parts.append(part); continue
    m = re.match(r'## (\d+)\.(\d+) (.+?) · (\d+)$', l)
    if m and part and int(m.group(1)) == part[0]:
        rows.append([int(m.group(4)), m.group(3), part[0], part[1][0].lower() + part[1][1:], part[2], part[3], next(k for k, v in FOLD4.items() if part[1].endswith(v))])
assert len(parts) == 10
entries = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r'(?m)^## (\d+) (.+)$', registry)}
FIVE = ('Conserving relation', 'Conserving reach', 'Reach', 'Unreachability', 'Persistence')   # five lines of each entry, as they are
OWN = {}; body = re.split(r'(?m)^## (\d+) .+$', registry)
for i in range(1, len(body), 2):
    OWN[int(body[i])] = {m.group(1): m.group(2) for l in body[i + 1].split('\n') for m in [re.match(r'\*\*(' + '|'.join(FIVE) + r')\.\*\* ?(.*)', l)] if m}
if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['its number in the Hard Problem Registry', 'hard problem', 'part', 'its unchangeable', 'seated with, now', 'and 8 up, next', 'ten fold to four: its fixing by a coarser grain', 'its conserving relation', 'its conserving reach', 'its reach', 'its unreachability', 'its persistence'])
    w.writerows(r + [OWN.get(r[0], {}).get(k, '') for k in FIVE] for r in sorted(rows)); sys.exit()
say = lambda ok, label: print(f'  {"is" if ok else "is-not"} · {label}')
print(f'{len(rows)} hard problems under ten unchangeables; {len(entries)} entries in Exhibit TWENTY-ONE Hard Problem Registry.')
for p in parts: print(f'  {p[0]:2d}. {p[1]}, with {p[2]} and {p[3]}: {sum(1 for r in rows if r[2] == p[0])}')
print('Each check, all or none at all:')
nums = [r[0] for r in rows]
assert 'Numbers 155 and 172 stand at no entry' in registry
later = {int(m.group(3)): (int(m.group(1)), m.group(2)) for m in re.finditer(r'(?m)^## (1[12])\.\d+ (.+?) · (\d+)$', resolving)}
say(len(nums) == len(set(nums)), 'each hard problem is under one unchangeable and no more')
say(set(nums) - set(entries) == {172} and 155 in later, 'each is an entry of Exhibit TWENTY-ONE Hard Problem Registry by its number, but 172, the limits of intelligence, under a parity fixing as a magnitude: of no entry, as that registry has it, with 155 under part eleven')
say(sorted(set(entries) - set(nums)) == [166] and later[166][0] == 12, 'each entry of Exhibit TWENTY-ONE Hard Problem Registry is under one of the ten, but 166, Molyneux\'s problem, under part twelve, the reach and the instruments the same')
say(all(all(k in OWN[n] for k in FIVE) and all(OWN[n][k] for k in FIVE if k != 'Unreachability') for n in entries), 'each entry of Exhibit TWENTY-ONE Hard Problem Registry has its line of a conserving relation, a conserving reach, a reach, an unreachability and a persistence, and each of the four others has its words')
print(f'  an unreachability with its words: {sum(1 for n in entries if OWN[n]["Unreachability"])} entries; with none: {sum(1 for n in entries if not OWN[n]["Unreachability"])}')
whole = sum(1 for n in entries if OWN[n]['Conserving reach'].split()[0].strip(',.') in ('All', 'Every', 'Each', 'Any'))
print(f'  a conserving reach opening with all, every, each or any: {whole} of {len(entries)} entries')
by_seat = {}
for r in rows: by_seat.setdefault((r[4], r[5]), []).append(r[0])
print('  each seat with its hard problems:', {f'{a.split("-")[0]} and {b.split("-")[0]}': len(v) for (a, b), v in sorted(by_seat.items(), key=lambda x: int(x[0][0].split('-')[0]))})
