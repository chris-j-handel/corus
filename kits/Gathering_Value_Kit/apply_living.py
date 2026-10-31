"""Writes one living-file motion after its readings, all or none.

Usage: python3 kits/Gathering_Value_Kit/apply_living.py KEY LIVING_FILE VERSION [--dry]
       e.g. apply_living.py ME Exhibit_THIRTY-ONE_Me_v392.md v393L

Joins incoming/v393L/passes/LIVING_<KEY>_replace.json with LIVING_<KEY>_reading.json (fix, drop, add, requote_fix) and,
when present, LIVING_<KEY>_reading2.json (fix, naming a replacement by its old or its new). Each old must stand once in the
living file. The file takes VERSION in its name and its version line; its gathering-value items are re-quoted or, met,
removed; then node build.js lists it and gathering_value_form.py re-forms its gathering-value."""
import json, os, re, subprocess, sys

key, living, version = sys.argv[1], sys.argv[2], sys.argv[3]
DRY = '--dry' in sys.argv
P = f'incoming/v393L/passes/LIVING_{key}_'
load = lambda n, d: json.load(open(P + n)) if os.path.exists(P + n) else d
R = load('replace.json', [])
F = load('reading.json', {})
F2 = load('reading2.json', {})
by = {r['old']: dict(r) for r in R}
for f in F.get('fix', []):
    if f['old'] not in by: sys.exit('NOTHING WRITTEN: a fix names no replacement: ' + f['old'][:80])
    by[f['old']]['new'] = f['new']
for o in F.get('drop', []):
    by.pop(o, None)
for a in F.get('add', []):
    by[a['old']] = dict(a)
for f in F2.get('fix', []):
    hit = by.get(f['old']) or next((r for r in by.values() if r['new'] == f['old']), None)
    if hit is None: sys.exit('NOTHING WRITTEN: a second fix names no replacement: ' + f['old'][:80])
    hit['new'] = f['new']
s = open(living, encoding='utf-8').read()
olds = list(by)
for o in olds:
    if s.count(o) != 1: sys.exit(f'NOTHING WRITTEN: stands {s.count(o)} times: {o[:80]}')
for a in olds:                                          # no two replacements overlap
    for b in olds:
        if a != b and a in b: sys.exit('NOTHING WRITTEN: one replacement inside another: ' + a[:60])
heads = lambda t: re.findall(r'^#{1,3} .*$', t, re.M)
before = heads(s)
for r in by.values():                                  # a removal takes one blank line with it
    o = r['old']
    if r['new'] == '' and o + '\n\n' in s:
        o = o + '\n\n'
    s = s.replace(o, r['new'], 1)
first = s.split('\n', 1)[0]
s = s.replace(first, re.sub(r'v\d+[A-Za-z]*$', version, first), 1)
gone = [h for h in before if h not in heads(s)]
new_name = re.sub(r'_v\d+[A-Za-z]*\.md$', f'_{version}.md', living)
Q = load('requote.json', [])
qb = {q['old']: dict(q) for q in Q}
for f in F.get('requote_fix', []) + F2.get('requote_fix', []):
    qb.setdefault(f['old'], {'file': f.get('file')}).update(f)
rq = [{'file': q['file'], 'old': q['old'], 'new': q['new']} for q in qb.values() if q.get('new')]
met = [q['old'] for q in qb.values() if not q.get('new')]
json.dump(rq, open(P + 'requote_apply.json', 'w'), indent=1, ensure_ascii=False)
json.dump(met, open(P + 'met_remove.json', 'w'), indent=1, ensure_ascii=False)
print(f'{len(by)} replacements; {len(rq)} re-quotes; {len(met)} met; headings gone: {gone}')
for cmd in (['python3', 'kits/Gathering_Value_Kit/replace_lines.py', P + 'requote_apply.json', '--dry'],
            ['python3', 'kits/Gathering_Value_Kit/remove_gathered.py', P + 'met_remove.json', '--dry']):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode or 'NOTHING' in r.stdout: sys.exit('NOTHING WRITTEN:\n' + r.stdout + r.stderr)
if DRY:
    print(f'would write {new_name}, {len(s.split())} words'); sys.exit()
open(living, 'w', encoding='utf-8').write(s)
if new_name != living:
    subprocess.run(['git', 'mv', living, new_name], check=True)
for cmd in (['python3', 'kits/Gathering_Value_Kit/replace_lines.py', P + 'requote_apply.json'],
            ['python3', 'kits/Gathering_Value_Kit/remove_gathered.py', P + 'met_remove.json'],
            ['node', 'build.js'], ['python3', 'kits/Gathering_Value_Kit/gathering_value_form.py', '.']):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit(r.stdout + r.stderr)
print(f'written {new_name}, {len(s.split())} words')
