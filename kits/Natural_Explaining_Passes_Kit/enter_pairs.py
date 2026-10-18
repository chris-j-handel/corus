"""enter_pairs.py LIVING PAIRS.json ARCHIVE.md OFFERINGS.md "heading"
Enter a pass's RESAY pairs at a living file (each old unique, each replaced old archived whole), and lay each ASK
item at the file's offerings under '## Standing · v389' as a concern with its Standing line; checks before writing."""
import sys, json, re
P, J, ARCH, OFF, head = sys.argv[1:6]
t = open(P).read(); rel = []; blocks = []
for d in json.load(open(J)):
    if d['verdict'] == 'ASK':
        w = d['why'].strip()
        h, _, rest = w.partition('. ') if w.startswith('Concern') else ('Concern · at a sentence', '', w)
        q = re.sub(r'\s+', ' ', d['old'][:120]).strip()
        blocks.append(f'**{h}.** Beside "{q}"' + ('…' if len(d['old']) > 120 else '') + f'\n\n*Standing at v389:* {rest}')
        continue
    if d['verdict'] != 'RESAY' or d['old'] == d['new']: continue
    assert t.count(d['old']) == 1, ('not unique', d['old'][:90])
    t = t.replace(d['old'], d['new']); rel.append(d['old'])
open(P, 'w').write(t)
if rel: open(ARCH, 'a').write(f'\n## {head}\n\n' + '\n\n'.join(rel) + '\n')
if blocks:
    o = open(OFF).read().rstrip('\n')
    if '\n## Standing · v389\n' not in o: o += '\n\n## Standing · v389\n\n*Concerns met at v389, each standing at this file and out of its living file until resolved.*'
    open(OFF, 'w').write(o + '\n\n' + '\n\n'.join(blocks) + '\n')
print(P, 're-said', len(rel), '· concerns', len(blocks))
