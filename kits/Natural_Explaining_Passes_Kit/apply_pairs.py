"""apply_pairs.py LIVINGFILE PAIRS.json ARCHIVE.md [HEADING]
Applies each RESAY item {"old","new","verdict"} of a proposal: each old must occur exactly once.
Each replaced old stands whole, appended to the archive under HEADING."""
import json, sys
P, J, arch = sys.argv[1:4]
head = sys.argv[4] if len(sys.argv) > 4 else 'Re-said at a pass'
t = open(P).read(); rel = []; n = 0
for d in json.load(open(J)):
    if d['verdict'] != 'RESAY' or d['old'] == d['new']:
        continue
    assert t.count(d['old']) == 1, d['old'][:80]
    t = t.replace(d['old'], d['new']); rel.append(d['old']); n += 1
open(P, 'w').write(t)
open(arch, 'a').write(f'\n## {head}\n\n' + '\n\n'.join(rel) + '\n')
print(P, 're-said', n)
