"""v402mgr: do no harm, each living file. Its prior version with the noun re-said is its next version, letter for letter:
no other word is changed. The Living File Registry has its own entries of the version beside it."""
import sys, re, subprocess
R = sys.argv[1]
src = open(R + '/incoming/v402mgr/instruments/build_part_three.py', encoding='utf-8').read()
ns = {}; exec(src.split("rows = []")[0].replace("R = sys.argv[1]", "R = None"), ns); transform = ns['transform']
ok = True
for f in open('/tmp/changed.txt').read().split():
    prior = subprocess.run(['git', '-C', R, 'show', 'origin/main:' + f], capture_output=True, text=True).stdout
    nxt = open(R + '/' + re.sub(r'_v\d+[A-Za-z]*\.md$', '_v402mgr.md', f), encoding='utf-8').read()
    want, n, _ = transform(prior)
    wl, nl = want.split('\n'), nxt.split('\n')
    wl[0] = re.sub(r' v\d+[A-Za-z]*$', ' v402mgr', wl[0])
    diff = [i for i in range(max(len(wl), len(nl))) if (wl[i] if i < len(wl) else None) != (nl[i] if i < len(nl) else None)]
    if 'Living_File_Registry' in f:
        rest = [i for i in diff if not (nl[i].startswith('  - *b* v402mgr') or nl[i].startswith('  - *c* v402mgr: *moment*'))]
        print(f"  {f}: {n} places; lines other-than by its own entries of the version: {len(diff) - len(rest)}; by anything else: {len(rest)}"); ok &= not rest
    else:
        if diff: print('  OTHER-THAN', f, diff[:5]); ok = False
print('each of', len(open('/tmp/changed.txt').read().split()), 'living files: its prior with the noun re-said is its next, letter for letter' if ok else 'A LIVING FILE IS OTHER-THAN')
