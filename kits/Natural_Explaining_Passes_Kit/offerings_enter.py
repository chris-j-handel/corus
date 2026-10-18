"""offerings_enter.py LIVINGFILE OFFERINGS "TITLE" ARCHIVE_RELEASED VERSION PREFIX [PREFIX...]
Joins each PREFIX.jsonl and PREFIX_edits.json (parts of one offerings file), refuses overlapping or non-unique
edits, enters risen edits at the living file (each replaced sentence archived), then resolves the offerings file."""
import sys, json, subprocess, os
liv, off, title, arch, ver = sys.argv[1:6]; prefixes = sys.argv[6:]
items, edits = [], []
for p in prefixes:
    items += [json.loads(x) for x in open(p + '.jsonl') if x.strip()]
    if os.path.exists(p + '_edits.json'):
        edits += json.load(open(p + '_edits.json'))
lines = [d['line'] for d in items]; assert len(lines) == len(set(lines)), 'an item met twice'
t = open(liv).read(); spans = []
for d in edits:
    assert t.count(d['old']) == 1, ('not unique', d.get('item'), d['old'][:80])
    i = t.index(d['old']); spans.append((i, i + len(d['old']), d.get('item')))
spans.sort()
bad = [(a[2], b[2]) for a, b in zip(spans, spans[1:]) if a[1] > b[0]]
if bad:
    print('OVERLAPPING edits (items):', bad); sys.exit(1)
rel = []
for d in edits:
    t = t.replace(d['old'], d['new']); rel.append(d['old'])
open(liv, 'w').write(t)
open(arch, 'a').write(f'\n## Re-said at offerings risen, v{ver}\n\n' + '\n\n'.join(rel) + '\n')
j = '/tmp/_joined.jsonl'; open(j, 'w').write('\n'.join(json.dumps(d, ensure_ascii=False) for d in items) + '\n')
here = os.path.dirname(os.path.abspath(__file__))
subprocess.run(['python3', here + '/offerings_resolve_all.py', off, j, title, liv, ver], check=True)
print(liv, 'risen edits', len(edits))
