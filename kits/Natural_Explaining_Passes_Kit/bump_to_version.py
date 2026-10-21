"""bump_to_version.py VERSION "LIVING CELL" FILE [FILE...]
A living file brought to VERSION after its motion: git mv to its _vVERSION name, its first line's version set,
each link to its earlier name at carry/, kits/ and the root .md files re-pointed (archive/ is a record and stays),
and its entry at the Living File Registry's titles, a table row or a narrow list entry, set: "At the repository" to vVERSION, "Living" to LIVING CELL,
"Next" to "pass 4 at its possible projects"."""
import sys, re, os, glob, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry_entry import set_entry
ver, cell, files = sys.argv[1], sys.argv[2], sys.argv[3:]
reg = sorted(glob.glob('Exhibit_TWENTY-SIX_Living_File_Registry_v*.md'))[-1]
for old in files:
    new = re.sub(r'_v[0-9][0-9A-Za-z]*\.md$', f'_v{ver}.md', old); assert new != old, old
    subprocess.run(['git', 'mv', old, new], check=True)
    L = open(new).read().split('\n'); L[0] = re.sub(r'v[0-9][0-9A-Za-z]*$', f'v{ver}', L[0]); open(new, 'w').write('\n'.join(L))
    n = 0
    for p in glob.glob('carry/**/*.md', recursive=True) + glob.glob('kits/**/*.md', recursive=True) + glob.glob('*.md'):
        s = open(p).read()
        if old in s: open(p, 'w').write(s.replace(old, new)); n += s.count(old)
    # registry row: its title cell from the version line
    title = re.sub(r'\s+v[0-9][0-9A-Za-z]*$', '', L[0])
    m = re.match(r'Exhibit (\S+) (.*)', title)
    label = f'**{m.group(1)} · {m.group(2)}**' if m else f'**{title}**'
    s = open(reg).read()
    s = set_entry(s, label, f'v{ver}', f'v{ver}: {cell}', prepend=False, next_='pass 4 at its possible projects'); open(reg, 'w').write(s)
    print(old, '->', new, '· links re-pointed', n)
