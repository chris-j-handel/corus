"""One naming motion, v390: each living file and kit file naming 1 to 17 with older names is re-said with the
agreed names, and Exhibit ONE's cycles of moves, once *four-cycles*, are said as bi-foldings.

Usage: python3 incoming/v390/naming_motion.py [--write]
Without --write it reports counts only. With --write each living file changed is moved to _v390 with git mv,
its version line said at v390, and kit files are re-said in place. Prior files stay whole at git and at
archive/session_v390/prior_to_naming_motion/.
Living File Registry is left as its record: its entries say what each version was."""
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
NEW = {1: 'now_existing', 2: 'now_possibling', 3: 'now_co_observing', 4: 'now_co_same_existing', 5: 'now_co_existing',
       6: 'now_co_possibling', 7: 'now_observing', 8: 'now_same_existing', 9: 'next_co_discovering', 10: 'next_co_possibling',
       11: 'next_co_observing', 12: 'next_co_same_existing', 13: 'next_same_existing', 14: 'next_possibling',
       15: 'next_observing', 16: 'next_discovering', 17: 'next_existing'}
OLD = {1: 'now', 2: 'now_possibling', 3: 'now_co_prioring', 4: 'now_co_still_possibling', 5: 'now_co_changing',
       6: 'now_co_possibling', 7: 'now_prioring', 8: 'now_still_possibling', 9: 'next_co_changing', 10: 'next_co_possibling',
       11: 'next_co_prioring', 12: 'next_co_still_possibling', 13: 'next', 14: 'next_possibling', 15: 'next_prioring',
       16: 'next_still_possibling', 17: 'next_now'}
FOLD = {'middle four-cycles': 'middle bi-foldings', 'Middle four-cycles': 'Middle bi-foldings',
        'middle four-cycle': 'middle bi-folding', 'Middle four-cycle': 'Middle bi-folding',
        'four-cycles': 'bi-foldings', 'Four-cycles': 'Bi-foldings', 'four-cycle': 'bi-folding', 'Four-cycle': 'Bi-folding'}
SKIP = {'Exhibit_TWENTY-SIX_Living_File_Registry'}


def rename(t):
    n_ = 0
    for n in sorted(OLD, key=lambda k: -len(OLD[k])):
        if OLD[n] == NEW[n]:
            continue
        t, c = re.subn(r'\b_%d_%s\b' % (n, OLD[n]), '_%d_%s' % (n, NEW[n]), t)
        n_ += c
        t, c = re.subn(r'(?<![\w-])%d-%s(?![\w-])' % (n, OLD[n].replace('_', '-')), '%d-%s' % (n, NEW[n].replace('_', '-')), t)
        n_ += c
    t, c = re.subn(r'(?<![\w-])([Mm]iddle )?([Ff]our-cycles?)(?![\w-])', lambda m: FOLD[m.group(0)], t)
    return t, n_ + c


def main(write):
    os.chdir(ROOT)
    files = sorted(f for f in os.listdir('.') if re.match(r'.+_v389\.md$', f))
    # kit files working now; kit sources and records of earlier versions stay as their record
    kits = ['kits/Natural_Explaining_Passes_Kit/rules_8_lower_file.md', 'kits/Natural_Explaining_Passes_Kit/rules_9_second_family.md']
    arch = os.path.join('archive', 'session_v390', 'prior_to_naming_motion')
    total = 0
    moved = []
    for f in files + sorted(kits):
        stem = re.sub(r'_v389\.md$', '', os.path.basename(f))
        if stem in SKIP:
            continue
        t = open(f, encoding='utf-8').read()
        new, c = rename(t)
        if not c:
            continue
        total += c
        print('%5d  %s' % (c, f))
        if not write:
            continue
        os.makedirs(os.path.dirname(os.path.join(arch, f)) or arch, exist_ok=True)
        shutil.copy(f, os.path.join(arch, f))
        if f in files:
            g = f.replace('_v389.md', '_v390.md')
            subprocess.run(['git', 'mv', f, g], check=True)
            lines = new.split('\n')
            assert lines[0].endswith('v389'), lines[0]
            lines[0] = lines[0][:-4] + 'v390'
            open(g, 'w', encoding='utf-8').write('\n'.join(lines))
            moved.append((f, g, lines[0]))
        else:
            open(f, 'w', encoding='utf-8').write(new)
    print('total', total)
    if write and moved:
        registry(moved)


CELL = 'v390: seventeen resolver names at the agreed names, 1-now-existing to 17-next-existing; Exhibit ONE\'s cycles of moves said as bi-foldings'


def registry(moved):
    reg = 'Exhibit_TWENTY-SIX_Living_File_Registry_v389.md'
    shutil.copy(reg, os.path.join('archive', 'session_v390', 'prior_to_naming_motion', reg))
    new_reg = reg.replace('_v389.md', '_v390.md')
    subprocess.run(['git', 'mv', reg, new_reg], check=True)
    s = open(new_reg, encoding='utf-8').read()
    L = s.split('\n')
    L[0] = L[0][:-4] + 'v390'
    s = '\n'.join(L)
    moved = moved + [(reg, new_reg, L[0])]
    for old, new, first in moved:
        title = re.sub(r'\s+v[0-9][0-9A-Za-z]*$', '', first)
        m = re.match(r'Exhibit (\S+) (.*)', title)
        label = '**%s · %s**' % (m.group(1), m.group(2)) if m else '**%s**' % title
        rows = [r for r in s.split('\n') if r.startswith('| ' + label + ' |')]
        assert rows, label
        c = rows[0].split(' | ')
        c[2] = 'v390'
        cell = CELL if old != reg else 'v390: its own row and each moved file\'s row at v390 after the naming motion; its earlier entries kept as their record'
        c[3] = cell + '; ' + c[3]
        s = s.replace(rows[0], ' | '.join(c), 1)
    open(new_reg, 'w', encoding='utf-8').write(s)
    # links to earlier names, at carry/, kits/ and the root .md files; archive/ is a record and stays
    n = 0
    targets = [os.path.join(dp, f) for top in ('carry', 'kits') for dp, _, fs in os.walk(top) for f in fs if f.endswith('.md')]
    targets += [f for f in os.listdir('.') if f.endswith('.md')]
    for p in targets:
        t = open(p, encoding='utf-8').read()
        u = t
        for old, new, _ in moved:
            u = u.replace(old, new)
        if u != t:
            open(p, 'w', encoding='utf-8').write(u)
            n += 1
    print('registry rows set; files with links re-pointed:', n)


if __name__ == '__main__':
    main('--write' in sys.argv)
