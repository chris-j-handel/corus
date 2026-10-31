"""The standing of the repository, said at one run: the living files at the root and their versions, superseded versions
still at the root, each kit's README and its sums, each living file's gathering-value at gathering-value/<Title>.md with
its possible explorings, possible incoherings, explainings and droplets counted, the workings open at the Living File
Registry, the incoming, and the archive. A coupling partner, no authority: each line says a standing and decides nothing.
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

# 3. each living file's gathering-value, gathering-value/<Title>.md, its items counted by kind
print('GATHERING-VALUE')
gvd = os.path.join(ROOT, 'gathering-value')
KINDS = (('explorings', r'^- \*\*Possible exploring\*\*'), ('incoherings', r'^- \*\*Possible incohering\*\*'),
         ('explainings', r'^- \*\*An explaining\*\*'))
print('  %-48s %10s %11s %8s %8s' % ('each living file', 'explorings', 'incoherings', 'explainings', 'droplets'))
totals = [0, 0, 0, 0]
for stem in sorted(living):
    if not living[stem].endswith('.md'): continue
    gv = os.path.join(gvd, re.sub(r'^Exhibit_[A-Z-]+?_(?=[A-Z][a-z])', '', stem) + '.md')
    if not os.path.exists(gv):
        notes.append('no gathering-value file for %s' % stem); continue
    gt = open(gv, encoding='utf-8').read()
    dm = re.search(r'^## Droplets\s*$', gt, re.M)
    body, drops = (gt[:dm.start()], gt[dm.end():]) if dm else (gt, '')
    n = [len(re.findall(k, body, re.M)) for _, k in KINDS] + [len(re.findall(r'^- ', drops, re.M))]
    totals = [t + x for t, x in zip(totals, n)]
    print('  %-48s %10d %11d %8d %8d' % (stem, *n))
    if not dm: notes.append('gathering-value of %s has no Droplets' % stem)
    parked = re.findall(r'^#{2,3} .*\(a section the living file no longer has\)', gt, re.M)
    if parked: notes.append('gathering-value of %s: %d sections its living file no longer has' % (stem, len(parked)))
print('  %-48s %10d %11d %8d %8d' % ('all', *totals))
if os.path.isdir(os.path.join(ROOT, 'carry')):
    notes.append('carry/ is present: its values go to gathering-value/')
reg = living.get('Exhibit_TWENTY-SIX_Living_File_Registry')
rt = open(os.path.join(ROOT, reg), encoding='utf-8').read() if reg else ''
m = re.search(r'\*\*The workings open\.\*\*.*?\n\n(\|.*?)\n\n', rt, re.S)
if m:
    rows = [r for r in m.group(1).split('\n')[2:] if r.startswith('|')]
    print('  workings open at the Living File Registry: %d' % len(rows))
    for r in rows: print('    ' + ' · '.join(c.strip() for c in r.strip('|').split('|')[:4])[:150])
else:
    notes.append('the Living File Registry has no table of the workings open')

# 4. incoming
print('INCOMING')
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
    print('  nothing to say: the root carries one version of each file, each kit has its README and its sums hold, each living file has its gathering-value')
