"""The standing of the repository as a carry, said at one run: the living files at the root and their versions, superseded
versions still at the root, each kit's README and its sums, the carrying's sections against the living files, the
workings open at the carrying's front, and the incoming not yet received. A coupling partner, no authority: each line
says a standing and decides nothing.
Usage: python3 tools/carry_check.py [repository root]      (run at a session's opening and at its close)"""
import os, re, sys, hashlib, glob

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..'))
VER = re.compile(r'^(.*)_v(\d+)([a-z]*)\.(md|py|zip)$')
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

# 3. the carrying: its sections against the living files, and the workings open
print('THE CARRYING')
liv = os.path.join(ROOT, 'carry', 'Living_Improving_Value.md')
if os.path.exists(liv):
    t = open(liv, encoding='utf-8').read()
    sections = re.findall(r'^## (.+)$', t, re.M)
    print('  Living Improving Value: %d sections, %d words' % (len(sections), len(t.split())))
    exhibits = {}
    for stem in living:
        m = re.match(r'Exhibit_([A-Z-]+)_', stem)
        if m: exhibits[m.group(1)] = stem
    for word, stem in sorted(exhibits.items()):
        if not any(s.startswith('Exhibit ' + word + ' ') or s.startswith('Exhibit ' + word + ' ·') for s in sections):
            notes.append('the carrying has no section for Exhibit %s (%s)' % (word, living[stem]))
    reg = living.get('Exhibit_TWENTY-SIX_Living_File_Registry')
    rt = open(os.path.join(ROOT, reg), encoding='utf-8').read() if reg else ''
    m = re.search(r'\*\*The workings open\.\*\*.*?\n\n(\|.*?)\n\n', rt, re.S)
    if m:
        rows = [r for r in m.group(1).split('\n')[2:] if r.startswith('|')]
        print('  workings open at the Living File Registry: %d' % len(rows))
        for r in rows: print('    ' + ' · '.join(c.strip() for c in r.strip('|').split('|')[:4]))
    else:
        notes.append('the Living File Registry has no table of the workings open')
else:
    notes.append('no carry/Living_Improving_Value.md')
for n in ('Session_Record.md',):
    print('  %-24s %s' % (n, 'present' if os.path.exists(os.path.join(ROOT, 'carry', n)) else 'absent'))

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
    print('  nothing to say: the root carries one version of each file, each kit has its README and its sums hold, the carrying has a section at each exhibit')
