"""An arrival read at the receiving's first steps, for its contributor or for the expedition, at one run: its front, the
living files and sections its findings name, its sentences seated at the six things beside all things, and its scripts run
from the repository root. A coupling partner, no authority: each line says a standing and decides nothing.
Usage: python3 kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/arrival_check.py incoming/<arrival folder>"""
import os, re, sys, glob, subprocess

if len(sys.argv) < 2:
    print(__doc__); sys.exit(0)
folder = sys.argv[1].rstrip('/')
ROOT = os.getcwd()
readme = os.path.join(folder, 'README.md')
print('ARRIVAL', folder)
if not os.path.exists(readme):
    print('  no README.md at the folder; the front, from, to, read at, what it brings, standing, is at none'); sys.exit(0)
text = open(readme, encoding='utf-8').read()

# 1. the front
print('THE FRONT')
for key in ('From', 'To', 'Read at', 'What it brings', 'Standing'):
    m = re.search(r'\*?\*?' + key + r'\*?\*?\s*[:.]\s*(.+)', text)
    print('  %-16s %s' % (key + ':', (m.group(1).strip()[:110] if m else 'not said')))

# 2. the living files and sections the findings name
print('THE FILES AND SECTIONS NAMED')
living = {}
for f in glob.glob(os.path.join(ROOT, '*.md')):
    m = re.match(r'(.+?)_v\d+[a-z]?\.md$', os.path.basename(f))
    if m: living[m.group(1).replace('_', ' ')] = os.path.basename(f)
short = {}
for stem in living:
    m = re.match(r'Exhibit ([A-Z-]+) (.+)', stem)
    if m: short[m.group(2)] = stem; short['Exhibit ' + m.group(1)] = stem
    else: short[stem] = stem
found = {}
for name, stem in short.items():
    for m in re.finditer(re.escape(name) + r"(?:'s)?[^.\n]{0,40}?\b(\d+\.\d+)\b", text):
        found.setdefault(stem, set()).add(m.group(1))
    if re.search(r'\b' + re.escape(name) + r'\b', text): found.setdefault(stem, set())
for stem in sorted(found):
    secs = sorted(found[stem], key=lambda s: tuple(int(x) for x in s.split('.')))
    print('  %-52s %s' % (stem, ', '.join(secs) if secs else 'named, no section'))
if not found: print('  no living file named; the expedition finds the file each finding aims at')

# 3. the six things beside all things, by the rigorizer's seats
print('SEATED AT THE SIX THINGS BESIDE ALL THINGS (a seat is a place to meet, deciding nothing)')
rig = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rigorize.py')
r = subprocess.run([sys.executable, rig, 'beside', readme], capture_output=True, text=True)
seats = re.findall(r'seated at: ([^\n]+)\n\s*(.+)', r.stdout)
counts = {}
for s, sent in seats:
    for k in s.split(';')[0].split(','): counts[k.strip()] = counts.get(k.strip(), 0) + 1
print('  ' + (', '.join('%s %d' % kv for kv in sorted(counts.items())) if counts else 'no sentence seated'))
for s, sent in seats[:12]: print('    %-14s %s' % (s.split(';')[0][:14], sent.strip()[:120]))
if len(seats) > 12: print('    ... %d more, at rigorize.py beside %s' % (len(seats) - 12, readme))

# 4. the scripts, run from the repository root
scripts = sorted(glob.glob(os.path.join(folder, '*.py')))
print('THE SCRIPTS, RUN FROM THE ROOT' if scripts else 'THE SCRIPTS: none')
for s in scripts:
    try:
        r = subprocess.run([sys.executable, s], capture_output=True, text=True, timeout=120, cwd=ROOT)
        head = (r.stdout.strip().split('\n') or [''])[0][:100]
        print('  %-36s %s  %s' % (os.path.basename(s), 'ran' if r.returncode == 0 else 'stopped at %d' % r.returncode, head))
        if r.returncode: print('      ' + (r.stderr.strip().split('\n') or [''])[-1][:110])
    except subprocess.TimeoutExpired:
        print('  %-36s ran past two minutes and was stopped' % os.path.basename(s))

print('STANDING')
print('  said above and decided nowhere: the expedition receives each finding at its file\'s carrying, carry/<file>.md, as ready or concern, or releases it whole with its receiving named.')
