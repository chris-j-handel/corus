"""bump_v390.py "LIVING CELL" FILE [FILE...]
A living file at v389 brought to v390 after a motion: git mv to its _v390 name, its version line set, links to its
earlier name at carry/, kits/ and the root .md files re-pointed (archive/ is a record and stays), and its row at the
Living File Registry given LIVING CELL before its earlier entries, which stay as their record. A file already at
v390 keeps its name, and its registry row is given LIVING CELL the same way."""
import glob
import os
import re
import subprocess
import sys

cell, files = sys.argv[1], sys.argv[2:]
reg = sorted(glob.glob('Exhibit_TWENTY-SIX_Living_File_Registry_v*.md'))[-1]
for old in files:
    new = re.sub(r'_v[0-9]+\.md$', '_v390.md', old)
    if new != old:
        subprocess.run(['git', 'mv', old, new], check=True)
        L = open(new, encoding='utf-8').read().split('\n')
        L[0] = re.sub(r'v[0-9]+$', 'v390', L[0])
        open(new, 'w', encoding='utf-8').write('\n'.join(L))
        targets = glob.glob('carry/**/*.md', recursive=True) + glob.glob('kits/**/*.md', recursive=True) + glob.glob('*.md')
        for p in targets:
            s = open(p, encoding='utf-8').read()
            if old in s:
                open(p, 'w', encoding='utf-8').write(s.replace(old, new))
    first = open(new, encoding='utf-8').read().split('\n')[0]
    title = re.sub(r'\s+v[0-9]+$', '', first)
    m = re.match(r'Exhibit (\S+) (.*)', title)
    label = '**%s · %s**' % (m.group(1), m.group(2)) if m else '**%s**' % title
    s = open(reg, encoding='utf-8').read()
    rows = [r for r in s.split('\n') if r.startswith('| ' + label + ' |')]
    assert rows, label
    c = rows[0].split(' | ')
    c[2] = 'v390'
    c[3] = 'v390: ' + cell + '; ' + c[3]
    open(reg, 'w', encoding='utf-8').write(s.replace(rows[0], ' | '.join(c), 1))
    print(old, '->', new)
