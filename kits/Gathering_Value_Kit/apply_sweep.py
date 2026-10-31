"""Writes one sweep batch after its separate reading for harm, all or none.

Usage: python3 kits/Gathering_Value_Kit/apply_sweep.py NAME [--dry]      (in the repository root; files at incoming/v393L/passes/SWEEP_<NAME>_*.json)

The re-sayer's replace and remove lists are joined with the reader's fixes (a fix replaces the re-saying of its line, or re-says
an unchanged line), restores (a removed line kept) and removes (a line whose value was only an offering). Each line must stand once."""
import json, os, subprocess, sys

name, DRY = sys.argv[1], '--dry' in sys.argv
P = f'incoming/v393L/passes/SWEEP_{name}_'
R = json.load(open(P + 'replace.json'))
X = json.load(open(P + 'remove.json'))
F = json.load(open(P + 'reading.json')) if os.path.exists(P + 'reading.json') else {}
by_old = {r['old']: r for r in R}
for f in F.get('fix', []):
    if f['old'] in by_old:
        by_old[f['old']]['new'] = f['new']
    elif f['old'] in X:                                  # a removed line re-said instead
        X.remove(f['old']); by_old[f['old']] = {'file': f.get('file'), 'old': f['old'], 'new': f['new']}
    else:
        by_old[f['old']] = {'file': f.get('file'), 'old': f['old'], 'new': f['new']}
for l in F.get('restore', []):
    if l in X: X.remove(l)
X += [l for l in F.get('remove', []) if l not in X]
for l in X:
    by_old.pop(l, None)
files = {r['file'] for r in by_old.values() if r.get('file')}
for r in by_old.values():                               # a fix naming no file: the one file holding its line
    if not r.get('file'):
        hits = [f for f in files or set() if r['old'] in open(f, encoding='utf-8').read().split('\n')]
        if not hits:
            import glob
            hits = [f for f in glob.glob('gathering-value/*.md') if r['old'] in open(f, encoding='utf-8').read().split('\n')]
        if len(hits) != 1:
            sys.exit(f'NOTHING WRITTEN: a fix stands at {len(hits)} files: {r["old"][:80]}')
        r['file'] = hits[0]
final_r, final_x = P + 'replace_final.json', P + 'remove_final.json'
json.dump(list(by_old.values()), open(final_r, 'w'), indent=1, ensure_ascii=False)
json.dump(X, open(final_x, 'w'), indent=1, ensure_ascii=False)
d = ['--dry'] if DRY else []
for cmd in (['python3', 'kits/Gathering_Value_Kit/replace_lines.py', final_r, '--dry'],
            ['python3', 'kits/Gathering_Value_Kit/remove_gathered.py', final_x, '--dry']):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode or 'NOTHING' in r.stdout:
        sys.exit('NOTHING WRITTEN, all or none:\n' + r.stdout + r.stderr)
if not DRY:
    for cmd in (['python3', 'kits/Gathering_Value_Kit/replace_lines.py', final_r],
                ['python3', 'kits/Gathering_Value_Kit/remove_gathered.py', final_x]):
        r = subprocess.run(cmd, capture_output=True, text=True); print(r.stdout.strip().split('\n')[-1])
        if r.returncode: sys.exit(r.stdout + r.stderr)
else:
    print(f'would replace {len(by_old)} and remove {len(X)}')
