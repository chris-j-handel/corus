"""A reading for harm of one returning, by the managing session's own hand. Reads and executes; changes nothing at the repository.
Use: python3 -I incoming/v404mgr/instruments/read_for_harm.py <clone> <a returning's number> [<a page of a partner's sayings> ...]
The returning is merged with main in a scratch worktree, /tmp/scratch/wt_<number>, and each thing is read in it.
A page of sayings has each saying a line opening with a hyphen and the saying in italics, as
incoming/v404mgr/The_sessions_v403cohering_and_v404helping_read_whole.md has each in its part 5.
 1 each file changed, and no living file among them
 2 each gathering file changed: lines away and lines more, each line away shown
 3 the set's checks, and the gathering check of each gathering file changed, at main and with the returning
 4 released words among the words added
 5 six words in sequence of a partner's saying, in a line added
 6 each instrument added or changed: its calls writing, deleting or reaching a network, and its executing
 7 the table of each is-or-is-not? open with the gathering files, after the returning
"""
import os, re, subprocess, sys, json, shutil

clone, n = sys.argv[1], sys.argv[2]
speakings = sys.argv[3:]
K = 'kits/Living_File_Registry_TWENTY-SIX_Improving_Kit'
G = 'kits/Gathering_Value_Kit'


def ex(cmd, cwd, t=240):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=t)
        return r.returncode, (r.stdout + r.stderr)
    except subprocess.TimeoutExpired:
        return 124, 'no answer after %d seconds' % t


wt = f'/tmp/scratch/wt_{n}'
ex(['git', 'worktree', 'remove', '--force', wt], clone)
shutil.rmtree(wt, ignore_errors=True)
ex(['git', 'fetch', '-q', '--depth=120', 'origin', f'refs/pull/{n}/head:refs/remotes/pull/{n}'], clone)
c, o = ex(['git', 'worktree', 'add', '-f', '--detach', wt, 'origin/main'], clone)
c, o = ex(['git', '-c', 'user.name=r', '-c', 'user.email=r@r', 'merge', '--no-ff', '-q', '-m', 'reading', f'refs/remotes/pull/{n}'], wt)
print(f'== returning {n}')
if c != 0:
    _, st = ex(['git', 'diff', '--name-only', '--diff-filter=U'], wt)
    print('  0 merging with main: PARTING in', ' ; '.join(st.split()))
    ex(['git', 'merge', '--abort'], wt)
    sys.exit(0)
print('  0 merging with main: whole')
_, names = ex(['git', 'diff', '--name-status', 'origin/main', 'HEAD'], wt)
rows = [l.split('\t') for l in names.strip().split('\n') if l.strip()]
living = json.load(open(os.path.join(wt, 'files.json')))
lv = [r[-1] for r in rows if r[-1] in living or (('/' not in r[-1]) and r[-1].endswith('.md') and r[-1] != 'README.md')]
print('  1 files changed:', len(rows), '· living files among them:', len(lv), lv[:3])
for r in rows:
    print('      ', r[0], r[-1][:110])
gfs = [r[-1] for r in rows if r[-1].startswith('gathering-value/')]
_, d = ex(['git', 'diff', '-U0', 'origin/main', 'HEAD', '--'] + [r[-1] for r in rows if r[-1].endswith(('.md', '.py', '.csv', '.json'))], wt)
added = [l[1:] for l in d.split('\n') if l.startswith('+') and not l.startswith('+++')]
for g in gfs:
    _, gd = ex(['git', 'diff', '-U0', 'origin/main', 'HEAD', '--', g], wt)
    more = [l for l in gd.split('\n') if l.startswith('+') and not l.startswith('+++')]
    away = [l for l in gd.split('\n') if l.startswith('-') and not l.startswith('---')]
    print(f'  2 {g}: {len(more)} lines more, {len(away)} away')
    for l in away:
        print('      away:', l[1:200])
for name, cmd in (('check_set', [sys.executable, '-I', f'{K}/check_set.py', '.']), ('carry_check', [sys.executable, '-I', f'{K}/carry_check.py', '.'])):
    c, o = ex(cmd, wt)
    print(f'  3 {name}:', (o.strip().split('\n') or [''])[-1].strip()[:110])
for g in gfs:
    t = os.path.basename(g)[:-3]
    a = ex([sys.executable, '-I', f'{G}/gathering_check.py', t], clone)[1].strip().split('\n')[-1]
    b = ex([sys.executable, '-I', f'{G}/gathering_check.py', t], wt)[1].strip().split('\n')[-1]
    print(f'  3 gathering check {t}: at main "{a.strip()}" · with the returning "{b.strip()}"')
c, o = ex([sys.executable, '-I', f'{K}/reader_checks.py', '.', 'origin/main'], wt)
m = re.search(r'3\. Released words.*?(?=\n4\. )', o, re.S)
rel = [l.strip() for l in (m.group(0) if m else '').split('\n')[2:] if l.strip()]
print('  4 released words:', ' | '.join(x[:150] for x in rel) or 'no answer')
says = []
for sp in speakings:
    says += re.findall(r'^- \*(.+?)\*(?: ·|$)', open(sp, encoding='utf-8').read(), re.M)
w = lambda s: re.findall(r"[a-z0-9'+−-]+", s.lower())
grams = set()
for s in says:
    ws = w(s)
    grams |= {' '.join(ws[i:i + 6]) for i in range(len(ws) - 5)}
hits = []
for l in added:
    ws = w(l)
    for i in range(len(ws) - 5):
        g6 = ' '.join(ws[i:i + 6])
        if g6 in grams:
            hits.append(g6)
print('  5 six words in sequence of a partner\'s saying, in a line added:', len(set(hits)), sorted(set(hits))[:4])
for r in rows:
    p = r[-1]
    if p.endswith('.py'):
        src = open(os.path.join(wt, p), encoding='utf-8').read()
        risky = sorted(set(re.findall(r"subprocess|os\.system|urllib|requests|socket|shutil|os\.remove|unlink|rmtree|write_text|open\([^)]*['\"][wa]b?['\"]", src)))
        if risky:
            print(f'  6 {p}: calls {risky}: not executed by this reading')
            continue
        c, o = ex([sys.executable, '-I', os.path.join(wt, p), wt], '/tmp/scratch', 300)
        tail = [x for x in o.strip().split('\n') if x.strip()][-2:]
        print(f'  6 {p}: executing ends {c} ·', ' / '.join(x.strip()[:120] for x in tail))
c, o = ex([sys.executable, '-I', 'incoming/v403mgr/instruments/each_is_or_is_not_open.py', '.'], wt)
t = [x.strip() for x in o.split('\n') if 'the table as it is written' in x]
print('  7', (t or ['no answer'])[0][:150])
