"""The seventeen names as they are, each by its three, and the places of the seventeen in the living files.
Reads Exhibit ONE Natural Resolver's living version and each living file, and writes none; it decides nothing.

Use: python3 -I incoming/v403mgr/instruments/seventeen_as_they_are.py <root>

1. Each name: across with an even number, along with an odd; its three in the order next, now, prior, each slot
   by its prefix and by its root: its own root, the root of the name it is after, and the root of the name that
   name is after, 1 after 16 as 17 is.
2. Each name's root by the slot same-existing is in.
3. The places of the seventeen names in the living files, as a name in a sentence and as a name of the code.

Returned at main, Merge #706, 15 November 2026:
  2. same-existing is its own root with 4, 8, 12 and 16; the now of 1, 5, 9, 13 and 17, each existing or discovering;
     the prior of 2, 6, 10 and 14, each possibling; and in no slot of 3, 7, 11 and 15, each observing, its three
     the three roots, observing, possibling, and existing or discovering.
  3. a name of the seventeen in a sentence: 3,285 places in 23 living files; a name of the code: 254 places in
     5 living files.
"""
import collections, glob, json, os, re, sys

R = sys.argv[1]
one = open(max(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')),
               key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
rows = re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \| ([a-z-]+)[^|]*\| [^|]*\| (co|one) \| ([a-z-]+) \|', one, re.M)
name = {int(n): nm for n, nm, _, _, _ in rows}; root = {int(n): r for n, _, r, _, _ in rows}
three = {int(n): t.split('-') for n, _, _, _, t in rows}
assert sorted(name) == list(range(1, 18))
r3 = lambda r: 'existing or discovering' if r in ('existing', 'discovering') else r
back = lambda n, k: ((n - k - 1) % 16) + 1          # 1 after 16, as 17 is
print('1. each name by its three, in the order next, now, prior')
slot_of_same = collections.defaultdict(list)
for n in range(1, 18):
    roots = [root[n], root[back(n, 1)], root[back(n, 2)]]
    print(f'   {name[n]:26s} {"across" if n % 2 == 0 else "along ":6s}  ' + ' · '.join(f'{p} {r3(r)}' for p, r in zip(three[n], roots)))
    s = [i for i, r in enumerate(roots) if r == 'same-existing']
    slot_of_same[('its own root', 'its now', 'its prior')[s[0]] if s else 'in no slot'].append((n, r3(root[n])))
print('2. each name by the slot same-existing is in')
for k in ('its own root', 'its now', 'its prior', 'in no slot'):
    print(f'   {k}: {[n for n, _ in slot_of_same[k]]}, each {sorted({r for _, r in slot_of_same[k]})}')
print('3. the places of the seventeen in the living files')
files = json.load(open(os.path.join(R, 'files.json')))
said = re.compile('|'.join(re.escape(name[n]) for n in sorted(name, key=lambda n: -len(name[n]))))
coded = re.compile(r'_(?:1[0-7]|[1-9])_(?:now|next)_[a-z_]+')
ps = pf = cs = cf = 0
for f in files:
    t = open(os.path.join(R, f), encoding='utf-8').read()
    a = len(said.findall(t)); b = len(coded.findall(t))
    ps += a; pf += 1 if a else 0; cs += b; cf += 1 if b else 0
print(f'   a name of the seventeen in a sentence: {ps} places in {pf} living files')
print(f'   a name of the code: {cs} places in {cf} living files')
