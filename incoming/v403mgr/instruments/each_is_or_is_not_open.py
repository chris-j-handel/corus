"""Each is-or-is-not? open in the gathering files, one line each: its gathering file, the section it is with, the
session whose returning or folder it names, the sentence, and why it is open. A resource for each session and for the partners, who
say is, is-or-is-not? or is-not of each sentence.
Reads each gathering file; executes; writes no file; decides nothing. All or none at all, by each droplet.

Use: python3 -I incoming/v403mgr/instruments/each_is_or_is_not_open.py <root>        each gathering file with its number, and each check
     python3 -I incoming/v403mgr/instruments/each_is_or_is_not_open.py <root> csv    one line with each is-or-is-not?

What it reads. A droplet is a line opening with a hyphen and a bold kind. An is-or-is-not? open is a droplet with
the words is-or-is-not? and, after them, Why it is open: the sentence is between the two, and why is after the
second. A droplet with the first, a sentence opening after it, and no second, is said, by its gathering file,
and is no line of the table; a droplet naming the three, an is, an is-or-is-not? or an is-not, lays none.
The session it names is read out of the droplet's own words: v403bubble's returning, v403cohering's folder or
v403mgr's folder, the first of the three it has, or none. It is no saying of which session laid the droplet.
The table as it is written, `incoming/v403mgr/Each_is_or_is_not_open.csv`, parts from the gathering files with
each droplet received after it: the answer says how many lines apart the two are, and `csv` writes it again.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
ROWS = []; LONE = []
for p in sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md'))):
    title = os.path.basename(p)[:-3].replace('_', ' '); head = ''
    for l in open(p, encoding='utf-8').read().split('\n'):
        m = re.match(r'#{2,3} (.+)', l)
        if m: head = m.group(1); continue
        if not l.startswith('- **') or 'is-or-is-not? ' not in l: continue
        if 'Why it is open:' not in l.split('is-or-is-not? ', 1)[1]:
            if re.search(r'is-or-is-not\? [A-Z]', l): LONE.append(title)
            continue
        before, why = l.rsplit('Why it is open:', 1); sentence = before.rsplit('is-or-is-not? ', 1)[1].strip()
        who = ("v403bubble's returning" if "The session v403bubble's" in l else "v403cohering's folder" if 'incoming/v403cohering' in l else "v403mgr's folder" if 'incoming/v403mgr' in l else 'none')
        ROWS.append((title, head, who, sentence, why.strip()))

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['gathering file', 'the section it is with', 'the session it names', 'is-or-is-not?', 'why it is open'])
    for r in ROWS: w.writerow(r)
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
by = {}
for r in ROWS: by.setdefault(r[0], []).append(r)
print(f'{len(ROWS)} is-or-is-nots open, in {len(by)} gathering files')
for t in sorted(by, key=lambda t: -len(by[t])): print(f'    {t}: {len(by[t])}')
who = {}
for r in ROWS: who[r[2]] = who.get(r[2], 0) + 1
print('  naming: ' + '; '.join(f'{k} {v}' for k, v in sorted(who.items())))
say(all(r[3] and r[4] for r in ROWS), 'each has its sentence and why it is open, each with words')
say(all(r[1] for r in ROWS), 'each is under a heading of its gathering file, a head or a section')
print(f'  a droplet with is-or-is-not?, a sentence opening after it, and no Why it is open, by its gathering file: {len(LONE)}' + (' · ' + '; '.join(f'{t} {LONE.count(t)}' for t in sorted(set(LONE))) if LONE else ''))
tp = os.path.join(R, 'incoming', 'v403mgr', 'Each_is_or_is_not_open.csv')
if os.path.exists(tp):
    was = [tuple(r) for r in csv.reader(open(tp, encoding='utf-8'))][1:]; now = [tuple(r) for r in ROWS]
    print(f'  the table as it is written and the gathering files now: {len([r for r in was if r not in now])} lines of the table not now, {len([r for r in now if r not in was])} now and not of the table')
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
