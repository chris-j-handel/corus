"""A living file beside its tab of a working document, a line and its words.

Usage: python3 -I a_living_file_beside_its_tab.py <living file> <the tab, exported as markdown>

Marks of form are apart from the comparing: a blank line, a line's break,
a table's rule and a list's indent. All other words and marks are compared,
a line with its line. It prints a place apart with both its sayings, and
the number of places apart at its end.
"""
import difflib
import re
import sys


def words_by_line(path):
    out = []
    for line in open(path, encoding='utf-8'):
        line = line.rstrip()
        if line.endswith('\\'):
            line = line[:-1].rstrip()
        if not line.strip():
            continue
        if re.fullmatch(r'\|(\s*-+\s*\|)+', line.strip()):
            line = re.sub(r'\s+', '', line)
        item = re.match(r'^(\s*)- (.*)$', line)
        if item:
            line = ('  ' if item.group(1) else '') + '- ' + item.group(2)
        out.append(line)
    return out


living, tab = words_by_line(sys.argv[1]), words_by_line(sys.argv[2])
print(len(living), 'lines of words in the living file,', len(tab), 'in its tab')
apart = 0
matcher = difflib.SequenceMatcher(None, living, tab, autojunk=False)
for tag, i1, i2, j1, j2 in matcher.get_opcodes():
    if tag == 'equal':
        continue
    apart += 1
    print('a place apart: line', i1 + 1, 'of the living file')
    for line in living[i1:i2]:
        print('  the living file:', line)
    for line in tab[j1:j2]:
        print('  its tab        :', line)
print('places apart:', apart)
