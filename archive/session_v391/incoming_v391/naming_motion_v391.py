"""One naming motion, v391, bothboth: 13 and 16 exchange roots.

13-next-same-existing is 13-next-discovering, and 16-next-discovering is 16-next-same-existing,
so each root's names share one parity and the four hold all or none: observing 3, 7, 11, 15 odd;
possibling 2, 6, 10, 14 even; same-existing 4, 8, 12, 16 even; existing 1, 5, 17 and discovering 9, 13 odd.

Usage: python3 incoming/v391/naming_motion_v391.py [--write]
Without --write it reports counts only. With --write each file is re-said in place and its prior is
copied whole to archive/session_v391/prior_to_naming_motion/ first. Versions and registry rows are set
after, by kits/Natural_Explaining_Passes_Kit/bump_to_version.py. Sentences saying which names a root has
are re-said by meaning after this motion, each one read."""
import os
import re
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SWAP = [('_13_next_same_existing', '_13_next_discovering'), ('_16_next_discovering', '_16_next_same_existing'),
        ('13-next-same-existing', '13-next-discovering'), ('16-next-discovering', '16-next-same-existing')]
KITS = ['kits/Natural_Explaining_Passes_Kit/rules_10_session_v390_words.md']
ARCH = os.path.join('archive', 'session_v391', 'prior_to_naming_motion')


def swap(t):
    n = 0
    for i, (a, _) in enumerate(SWAP):
        t, c = re.subn(r'(?<![\w-])%s(?![\w-])' % re.escape(a), '\0%d\0' % i, t)
        n += c
    for i, (_, b) in enumerate(SWAP):
        t = t.replace('\0%d\0' % i, b)
    return t, n


def main(write):
    os.chdir(ROOT)
    files = sorted(f for f in os.listdir('.') if re.match(r'.+_v39[01]\.md$', f))
    files = [f for f in files if not f.startswith('Exhibit_TWENTY-SIX_Living_File_Registry')]
    total = 0
    for f in files + KITS:
        t = open(f, encoding='utf-8').read()
        new, c = swap(t)
        if not c:
            continue
        total += c
        print('%5d  %s' % (c, f))
        if write:
            os.makedirs(ARCH, exist_ok=True)
            shutil.copy(f, os.path.join(ARCH, os.path.basename(f)))
            open(f, 'w', encoding='utf-8').write(new)
    print('total', total, '(written)' if write else '(report only)')


if __name__ == '__main__':
    main('--write' in sys.argv)
