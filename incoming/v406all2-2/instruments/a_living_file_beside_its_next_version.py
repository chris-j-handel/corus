"""A living file beside its next version: a line apart, with its words apart.

Usage: python3 -I a_living_file_beside_its_next_version.py <living file> <its next version> [a word]

With a word given, a line apart by that word alone is numbered at the end
and not printed. It prints all other lines apart, a span of words of the
living file beside its span of the next version.
"""
import difflib
import re
import sys

living = [line.rstrip('\n') for line in open(sys.argv[1], encoding='utf-8')]
nxt = [line.rstrip('\n') for line in open(sys.argv[2], encoding='utf-8')]
word = sys.argv[3].lower() if len(sys.argv) > 3 else None


def spans(a, b):
    ta, tb = re.findall(r'\s+|\S+', a), re.findall(r'\s+|\S+', b)
    m = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    return [(''.join(ta[x1:x2]), ''.join(tb[y1:y2]))
            for tag, x1, x2, y1, y2 in m.get_opcodes() if tag != 'equal']


by_the_word = 0
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, living, nxt, autojunk=False).get_opcodes():
    if tag == 'equal':
        continue
    if tag == 'replace' and i2 - i1 == j2 - j1:
        for k in range(i2 - i1):
            found = spans(living[i1 + k], nxt[j1 + k])
            if word and all(re.sub(r'[^a-z]', '', s[0].lower()) == word for s in found):
                by_the_word += 1
                continue
            print('line', i1 + k + 1, 'of the living file, line', j1 + k + 1, 'of its next version')
            for s in found:
                print('   ', repr(s[0]), 'said again as', repr(s[1]))
    else:
        print(tag, ': lines', i1 + 1, 'to', i2, 'of the living file, lines', j1 + 1, 'to', j2, 'of its next version')
        for line in living[i1:i2]:
            print('    the living file :', line)
        for line in nxt[j1:j2]:
            print('    its next version:', line)
if word:
    print('lines apart by the word', word, 'alone:', by_the_word)
