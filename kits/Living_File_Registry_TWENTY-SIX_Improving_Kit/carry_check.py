"""The standing of the repository as a carry, said at one run: the living files at the root and their versions, superseded
versions still at the root, each kit's README and its sums, each living file's own carrying at carry/<file>.md with its
next, its ready offerings and its concerns, the workings open at the Living File Registry, and the incoming not yet
received. A coupling partner, no authority: each line says a standing and decides nothing.
Usage: python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/carry_check.py [repository root]      (run at a session's opening and at its close)"""
import os, re, sys, hashlib, glob

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..'))
VER = re.compile(r'^(.*)_v(\d+)([A-Za-z]*)\.(md|py|zip)$')
notes = []

def stem_version(name):
    m = VER.match(name)
    return (m.group(1), int(m.group(2)), m.group(3)) if m else None

# 1. the root: newest of each, and superseded versions still there
root_files = sorted(f for f in os.listdir(ROOT) if os.path.isfile(os.path.join(ROOT, f)))
by_stem = {}
for f in root_files:
    sv = stem_version(f)
    if sv: by_stem.setdefault(sv[0], []).append((sv[1], sv[2], f))
living = {}
print('LIVING FILES AT THE ROOT')
for stem, vs in sorted(by_stem.items(), key=lambda kv: kv[0]):
    vs.sort()
    newest = vs[-1]; living[stem] = newest[2]
    print('  %-52s v%d%s' % (stem, newest[0], newest[1]))
    for v in vs[:-1]:
        notes.append('superseded at the root: %s (newest is %s); it can leave for archive/' % (v[2], newest[2]))
# the version line of each md
for stem, f in living.items():
    if f.endswith('.md'):
        first = open(os.path.join(ROOT, f), encoding='utf-8').readline().strip()
        v = stem_version(f)
        if not first.endswith('v%d%s' % (v[1], v[2])): notes.append('version line of %s reads "%s"' % (f, first[:60]))

# 2. kits
print('KITS')
kits = os.path.join(ROOT, 'kits')
if os.path.isdir(kits):
    for kit in sorted(os.listdir(kits)):
        kd = os.path.join(kits, kit)
        if not os.path.isdir(kd): continue
        files = [os.path.relpath(os.path.join(dp, f), kd) for dp, dn, fn in os.walk(kd) for f in fn]
        has_readme = os.path.exists(os.path.join(kd, 'README.md'))
        sums = os.path.join(kd, 'SHA256SUMS'); standing = 'no SHA256SUMS'
        if os.path.exists(sums):
            bad, missing = 0, 0
            for line in open(sums, encoding='utf-8'):
                h, p = line.rstrip('\n').split('  ', 1)
                fp = os.path.join(kd, p)
                if not os.path.exists(fp): missing += 1
                elif hashlib.sha256(open(fp, 'rb').read()).hexdigest() != h: bad += 1
            standing = 'sums hold' if not (bad or missing) else 'sums differ at %d, missing %d' % (bad, missing)
        print('  %-42s %4d files  README %s  %s' % (kit, len(files), 'yes' if has_readme else 'NO', standing))
        if not has_readme: notes.append('kit without a README: ' + kit)
        if standing != 'sums hold': notes.append('kit %s: %s' % (kit, standing))
else:
    print('  (no kits/ folder)')

# 3. the carrying: the front, and each living file's own carrying with its next, its ready offerings and its concerns
print('THE CARRYING')
carry = os.path.join(ROOT, 'carry')
liv = os.path.join(carry, 'Living_Improving_Value.md')
if os.path.exists(liv):
    t = open(liv, encoding='utf-8').read()
    print('  Living Improving Value, the front: %d words' % len(t.split()))
    if re.search(r'^## ', t, re.M): notes.append("the front carries a file's section; each file's carrying is its own file at carry/<file>.md")
else:
    notes.append('no carry/Living_Improving_Value.md')
print('  %-56s %-6s %5s %7s   next' % ('each file at its own carrying', 'words', 'ready', 'open'))
ready_total = concern_total = 0
for stem in sorted(living):
    if not living[stem].endswith('.md'): continue
    cf = os.path.join(carry, stem + '.md')
    if not os.path.exists(cf):
        notes.append('no carrying at carry/%s.md' % stem); continue
    ct = open(cf, encoding='utf-8').read()
    def part(name):
        m = re.search(r'^## ' + name + r'\s*\n(.*?)(?=^## |\Z)', ct, re.M | re.S)
        body = m.group(1).strip() if m else ''
        if body == 'None.' or not body: return 0
        return len([b for b in re.split(r'\n\s*\n', body) if b.strip()])
    ready, concern = part('Ready'), part('Concern')
    ready_total += ready; concern_total += concern
    nm = re.search(r'^\*\*Next at this file(.*?)\*\*[ \t]*(.*?)$', ct, re.M)
    nxt = ((nm.group(1).strip(':,. ') + ' ' + nm.group(2).strip()).strip() if nm else '(no next said)')[:70]
    print('  %-56s %6d %5d %7d   %s' % (stem, len(ct.split()), ready, concern, nxt))
    if 'None.' not in ct and ready == 0 and concern == 0: notes.append('carrying of %s says neither Ready nor Concern' % stem)
    if not nm: notes.append('carrying of %s has no "Next at this file" paragraph' % stem)
print('  ready offerings %d, concerns open %d' % (ready_total, concern_total))
reg = living.get('Exhibit_TWENTY-SIX_Living_File_Registry')
rt = open(os.path.join(ROOT, reg), encoding='utf-8').read() if reg else ''
m = re.search(r'\*\*The workings open\.\*\*.*?\n\n(\|.*?)\n\n', rt, re.S)
if m:
    rows = [r for r in m.group(1).split('\n')[2:] if r.startswith('|')]
    print('  workings open at the Living File Registry: %d' % len(rows))
    for r in rows: print('    ' + ' · '.join(c.strip() for c in r.strip('|').split('|')[:4])[:150])
else:
    notes.append('the Living File Registry has no table of the workings open')
for n in ('Session_Record.md',):
    print('  %-24s %s' % (n, 'present' if os.path.exists(os.path.join(carry, n)) else 'absent'))

# 4. incoming
print('INCOMING, NOT YET RECEIVED')
inc = os.path.join(ROOT, 'incoming')
if os.path.isdir(inc):
    for d in sorted(os.listdir(inc)):
        dd = os.path.join(inc, d)
        if os.path.isdir(dd):
            n = sum(len(fn) for _, _, fn in os.walk(dd)); print('  %-28s %3d files' % (d, n))
else:
    print('  (no incoming/ folder)')

# 5. archive
arc = os.path.join(ROOT, 'archive')
print('ARCHIVE: %d files' % (sum(len(fn) for _, _, fn in os.walk(arc)) if os.path.isdir(arc) else 0))

print('STANDING')
if notes:
    for n in notes: print('  - ' + n)
else:
    print('  nothing to say: the root carries one version of each file, each kit has its README and its sums hold, each living file has its own carrying')
