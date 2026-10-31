"""Takes a prior gathering's items out of the gathering-value files, so its slice can be gathered again from its source.

Usage: python3 kits/Gathering_Value_Kit/remove_gathered.py ITEMS.json [--dry]

ITEMS.json is a list of item lines exactly as they stand in gathering-value files (each line starting "- ").
Each line must stand exactly once across the gathering-value files, or nothing is removed, all or none."""
import glob, json, sys
lines = json.load(open(sys.argv[1])); DRY = '--dry' in sys.argv
files = {p: open(p, encoding='utf-8').read().split('\n') for p in sorted(glob.glob('gathering-value/*.md'))}
where, errors = {}, []
for l in lines:
    hits = [(p, n) for p, L in files.items() for n, x in enumerate(L) if x == l]
    if len(hits) != 1:
        errors.append(f'{len(hits)} places: {l[:90]}')
    else:
        where[l] = hits[0]
if errors:
    print('NOTHING REMOVED, all or none:'); [print(' ', e) for e in errors]; sys.exit(1)
for p in {p for p, _ in where.values()}:
    drop = {n for q, n in where.values() if q == p}
    out = [x for n, x in enumerate(files[p]) if n not in drop]
    if not DRY:
        open(p, 'w', encoding='utf-8').write('\n'.join(out))
print(('would remove ' if DRY else 'removed ') + f'{len(where)} items at {len({p for p, _ in where.values()})} files')
