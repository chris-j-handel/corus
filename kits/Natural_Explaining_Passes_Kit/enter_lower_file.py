"""enter_lower_file.py LIVING PAIRS.json APPLIED.md THE.md ARCHIVE.md OFFERINGS.md
Pass 3 (rules_8_lower_file.md): enter a reader's pairs and *the* edit at one living file below v389.
1. each RESAY pair entered (old unique), each replaced old appended whole at ARCHIVE;
2. the file must then equal the reader's APPLIED copy;
3. verify_the.py must print OK for THE against it; each line it changes appended whole at ARCHIVE;
4. each ASK item laid at OFFERINGS under '## Standing · v389' as a concern with its Standing line;
nothing is written until each check passes."""
import sys, json, os, re, subprocess
P, J, APP, THE, ARCH, OFF = sys.argv[1:7]
kit = os.path.dirname(os.path.abspath(__file__))
t = open(P).read(); rel = []; asks = []
for d in json.load(open(J)):
    if d['verdict'] == 'ASK': asks.append(d); continue
    if d['verdict'] != 'RESAY' or d['old'] == d['new']: continue
    assert t.count(d['old']) == 1, ('not unique', d['old'][:90])
    t = t.replace(d['old'], d['new']); rel.append(d['old'])
assert t == open(APP).read(), 'applied copy differs from pairs entered'
tmp = APP + '.check'; open(tmp, 'w').write(t)
n = t.count('\n') + 1
r = subprocess.run(['python3', os.path.join(kit, 'verify_the.py'), tmp, '1', str(n), THE], capture_output=True, text=True)
assert r.stdout.strip().endswith('OK'), r.stdout[-400:]
new = open(THE).read()
if not new.endswith('\n') and t.endswith('\n'): new += '\n'
a, b = t.split('\n'), new.split('\n')
the_rel = [x for x, y in zip(a, b) if x != y]
blocks = []
for d in asks:
    w = d['why'].strip()
    head, _, rest = w.partition('. ') if w.startswith('Concern') else ('Concern · at a sentence', '', w)
    blocks.append(f'**{head}.** Beside "{re.sub(r"\s+", " ", d["old"][:120]).strip()}"' + ('…' if len(d['old']) > 120 else '') + f'\n\n*Standing at v389:* {rest}')
open(P, 'w').write(new)
with open(ARCH, 'a') as f:
    if rel: f.write('\n## Re-said at pass 3, released words and numbered names, v389\n\n' + '\n\n'.join(rel) + '\n')
    if the_rel: f.write('\n## *the* at pass 3, v389, each line whole before\n\n' + '\n\n'.join(the_rel) + '\n')
if blocks:
    o = open(OFF).read().rstrip('\n')
    if '\n## Standing · v389\n' not in o: o += '\n\n## Standing · v389\n\n*Concerns met at pass 3, each standing at this file and out of its living file until resolved.*'
    open(OFF, 'w').write(o + '\n\n' + '\n\n'.join(blocks) + '\n')
os.remove(tmp)
print(os.path.basename(P), 're-said', len(rel), '· the lines', len(the_rel), '· concerns', len(blocks))
