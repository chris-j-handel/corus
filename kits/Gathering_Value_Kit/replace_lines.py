"""Replaces item lines in gathering-value files, all or none.

Usage: python3 kits/Gathering_Value_Kit/replace_lines.py CHANGES.json [--dry]

CHANGES.json is a list of {"file": "gathering-value/<Title>.md", "old": "<the item line exactly>", "new": "<its re-saying>"}.
Each old line must stand exactly once in its file, or nothing is written. An entry whose "new" equals "old" is left."""
import json, sys
C = json.load(open(sys.argv[1])); DRY = '--dry' in sys.argv
files, errors, n = {}, [], 0
for c in C:
    if c['new'] == c['old']: continue
    L = files.setdefault(c['file'], open(c['file'], encoding='utf-8').read().split('\n'))
    hits = [i for i, l in enumerate(L) if l == c['old']]
    if len(hits) != 1: errors.append(f'{len(hits)} places at {c["file"]}: {c["old"][:80]}'); continue
    if not c['new'].startswith('- '): errors.append(f'new is no item line: {c["new"][:80]}'); continue
    L[hits[0]] = c['new']; n += 1
if errors:
    print('NOTHING WRITTEN, all or none:'); [print(' ', e) for e in errors]; sys.exit(1)
if not DRY:
    for p, L in files.items(): open(p, 'w', encoding='utf-8').write('\n'.join(L))
print(('would replace ' if DRY else 'replaced ') + f'{n} lines at {len(files)} files')
