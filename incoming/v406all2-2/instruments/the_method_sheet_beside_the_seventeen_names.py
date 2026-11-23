"""The managing table's sheet The method, beside the seventeen names' own.

Usage: python3 -I the_method_sheet_beside_the_seventeen_names.py <the sheet, a csv> <Exhibit ONE, the living file> <the set's table of the seventeen names, a csv>

It goes through the sheet two ways, by executing. Its sayings: a name's
saying beside Exhibit ONE's own, in Code with a name, and beside the set's
table. Its tables: the table the sheet gives a name, beside the names' own
moves, roots, bi-foldings and unit square, and the pairs of the log of the
aims. It prints a line an is or an is-not, and writes nothing.
"""
import csv
import re
import sys

sheet = [r for r in csv.reader(open(sys.argv[1], encoding='utf-8')) if r and r[0].strip().isdigit()]
living = re.sub(r'[*`]', '', ''.join(open(sys.argv[2], encoding='utf-8')))
table = list(csv.reader(open(sys.argv[3], encoding='utf-8')))
code_column = next(i for i, h in enumerate(table[0]) if h.startswith('code with its name'))
of_the_table = {int(r[0]): r for r in table[1:]}


def line(same, saying):
    print(('is' if same else 'is-not').ljust(7), saying)


print('Its sayings, a capital apart')
in_living = in_table = 0
for r in sheet:
    n, saying = int(r[0]), r[2].strip()
    saying = saying[0].lower() + saying[1:]
    in_living += ('- %d · %s' % (n, saying)) in living
    in_table += of_the_table[n][code_column].strip() == saying
line(in_living == 17, "all seventeen are Exhibit ONE's own, word for word, in Code with a name: %d of 17" % in_living)
line(in_table == 17, "all seventeen are the set's table's, its column of the code with its name: %d of 17" % in_table)

its = {int(r[0]): r[4].strip() for r in sheet}
by_table = {}
for n in sorted(its):
    by_table.setdefault(its[n], []).append(n)
print()
print('Its tables')
for name, numbers in by_table.items():
    print('       ', name + ':', ', '.join(str(n) for n in numbers))

print()
print('A name now with its 8 up, its next')
for n in range(1, 10):
    line(its[n] == its[n + 8], '%d and %d: %s, %s' % (n, n + 8, its[n], its[n + 8]))

print()
print('A root, by a name\'s own hyphenation')
roots = {}
for n, r in of_the_table.items():
    name = r[1]
    root = 'same-existing' if name.endswith('same-existing') else name.split('-')[-1]
    roots.setdefault(root, []).append(n)
for root, numbers in roots.items():
    tables = sorted(set(its[n] for n in numbers))
    line(len(tables) == 1, '%s, %s: %s' % (root, ', '.join(str(n) for n in numbers), '; '.join(tables)))

print()
print('The four bi-foldings')
for fold in ((1, 9, 8, 16), (2, 15, 7, 10), (3, 11, 6, 14), (4, 13, 5, 12)):
    tables = sorted(set(its[n] for n in fold))
    line(len(tables) == 1, '%s: %s' % ('-'.join(str(n) for n in fold), '; '.join(tables)))

print()
print("Exhibit ONE's own")
line(len(set(its[n] for n in (2, 10, 14, 6))) == 1, "parity's unit square, 2, 10, 14, 6, in one table: " + ', '.join(its[n] for n in (2, 10, 14, 6)))
prior = '3-now-co-observing, 8-now-same-existing and 11-next-co-observing, prior'
line(prior in living and len(set(its[n] for n in (3, 8, 11))) == 1, 'its prior names, 3, 8 and 11, in one table: ' + ', '.join(its[n] for n in (3, 8, 11)))
line(its[17] == its[1], '17, in its own saying a 1-now-existing again, with 1: %s, %s' % (its[17], its[1]))
along = 'two along names' in living and '9-next-co-discovering and 17-next-existing' in living
line(along and its[9] == its[17], 'its two along names, 9 and 17, in one table: %s, %s' % (its[9], its[17]))

print()
print("The log's own pairs")
for root, pair in (('observing', (7, 15)), ('possibling', (2, 14)), ('discovering', (13, 9))):
    line(its[pair[0]] == its[pair[1]], '%s, %d and %d: %s, %s' % (root, pair[0], pair[1], its[pair[0]], its[pair[1]]))
