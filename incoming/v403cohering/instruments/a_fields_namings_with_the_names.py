"""Each field's naming of Exhibit TWENTY Natural Naming's sixth part, with the resolver's names the file has with
it, in one table: a field's naming a line, whole as the field has it, with its gathering, its relation or its
receiving, each resolver name written with it, and an invisible under it. A field's word goes on whole with its
own result, and its gathering is beside it: the table has both.
Reads Exhibit TWENTY Natural Naming's two sections of a field's namings with resolver's names, and Exhibit ONE
Natural Resolver's table of names; executes; writes no file; decides nothing. All or none at all, by each entry.

Use: python3 -I incoming/v403cohering/instruments/a_fields_namings_with_the_names.py <root>        each check, and each reading
     python3 -I incoming/v403cohering/instruments/a_fields_namings_with_the_names.py <root> csv    the table, one line with each field's naming

What it reads. A section's entries are after its line *Each entry:*, which has the entry's own name in bold and
each letter with what it is. An entry's letter of field namings, *Existing … namings* or *Existing field words*,
or *Terms it gathers*, has its namings one after one with a middle dot or a comma between; an entry with no such
letter is one field naming, its own name. A table with no letter of resolver names has them in the section's own
sentence after it, of each of its entries. A resolver name: a number, now or next, and its words, read with Exhibit ONE's name of that number.

Returned at main, 16 November 2026: 27 entries and 118 of a field's namings, each check is. Each resolver name
written is Exhibit ONE's name of its number, and no field's naming is in two gatherings. A field's namings are
with eleven of the seventeen names, 11-next-co-observing 58 and 1-now-existing 55 the most, and with none of
5-now-co-existing, 7-now-observing, 9-next-co-discovering, 13-next-discovering, 15-next-observing and
17-next-existing. The table is `incoming/v403cohering/A_fields_namings_with_the_names.csv`.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def ver(p):
    m = re.search(r'_v(\d+)', p); return int(m.group(1)) if m else 0
def newest(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=ver), encoding='utf-8').read()
one = newest('Exhibit_ONE_Natural_Resolver')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
L = newest('Exhibit_TWENTY_Natural_Naming').split('\n')
RESOLVER = re.compile(r'(?<![\w.-])(\d{1,2})-((?:now|next)-[a-z]+(?:-[a-z]+)*)')

def section(opening):
    s = next(i for i, l in enumerate(L) if l.startswith(opening))
    e = next(i for i in range(s + 1, len(L)) if L[i].startswith('## ') or L[i].startswith('# '))
    return L[s][3:].strip(), L[s + 1:e]

ROWS, ENTRIES, lacking = [], 0, []
for opening in ('## 6.2 ', '## 6.4 '):
    title, body = section(opening)
    letters, entry = {}, None
    def close(entry):
        global ENTRIES
        if not entry: return
        ENTRIES += 1
        name, f = entry['name'], entry['f']
        for k in letters:
            if k not in f: lacking.append((title, name, k))
        lk = next((k for k, v in letters.items() if v.startswith('Existing') or v.startswith('Terms')), None)
        namings = [x.strip() for x in f.get(lk, '').split(' · ' if ' · ' in f.get(lk, '') else ', ') if x.strip()] if lk else [name]
        rel = ' '.join(f[k] for k, v in sorted(letters.items()) if k in f and ('relation' in v.lower() or 'receiving' in v.lower()) and 'Resolver' not in v)
        rk = next((k for k, v in letters.items() if v.startswith('Resolver')), None)
        res = f.get(rk, '')
        inv = next((f[k] for k, v in letters.items() if 'invisible' in v.lower() and k in f), '')
        for w in namings:
            ROWS.append([w, name if lk else 'a field naming, its own', rel, res, ', '.join(m.group(1) for m in RESOLVER.finditer(res)), inv, title])
    for l in body:
        if l.startswith('Each entry:'):
            close(entry); entry = None
            letters = {k: v.strip() for k, v in re.findall(r'\*([a-d])\* ([^·]+)', l)}
            group = len(ROWS)
        elif l.startswith('- **') and letters:
            close(entry)
            entry = {'name': re.match(r'- \*\*(.+?)\*\*', l).group(1), 'f': {}}
            for k, v in re.findall(r' · \*([a-d])\* ((?:(?! · \*[a-d]\* ).)+)', l): entry['f'][k] = v.strip()
        elif entry and re.match(r'^  - \*([a-d])\* ', l):
            entry['f'][l[5]] = l[8:].strip()
        elif l.startswith('**') and entry:
            close(entry); entry = None
            if not any(v.startswith('Resolver') for v in letters.values()) and RESOLVER.search(l):
                # a table with no letter of resolver names: the section's own sentence after it has them, of each entry
                res = ', '.join(m.group(0) for m in RESOLVER.finditer(l))
                for r in ROWS[group:]: r[3] = res; r[4] = ', '.join(m.group(1) for m in RESOLVER.finditer(res))
    close(entry)

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(["a field's naming, whole [living TWENTY]", 'its gathering [living TWENTY]', 'its relation, or its receiving [living TWENTY]',
                'resolver names with it [living TWENTY]', "each name's number [executed]", 'an invisible under it [living TWENTY]', "its section of Exhibit TWENTY Natural Naming"])
    w.writerows(ROWS); sys.exit()

print(f"{ENTRIES} entries of two sections, {len(ROWS)} of a field's namings in them")
names = [(int(m.group(1)), m.group(0)) for r in {(r[1], r[3]) for r in ROWS} for m in RESOLVER.finditer(r[1])]
written = [(int(m.group(1)), m.group(0)) for res in {(r[1], r[6], r[3]) for r in ROWS} for m in RESOLVER.finditer(res[2])]
checks = [
    ("each entry has each letter of its section's own line", not lacking),
    ("each resolver name written is Exhibit ONE's name of its number", all(n in NAME and NAME[n] == s for n, s in written)),
    ("each field's naming has a resolver name with it", all(r[4] for r in ROWS)),
]
for what, ok in checks: print(('  is · ' if ok else '  is-not · ') + what)
for t, n, k in lacking: print(f'      {t}: {n}, no {k}')
for n, s in sorted(set(written)):
    if n not in NAME or NAME[n] != s: print(f'      written {s} · Exhibit ONE: {NAME.get(n)}')
for r in ROWS:
    if not r[4]: print(f'      with no resolver name: {r[0]} · {r[1]}')
by = {n: 0 for n in NAME}
for r in ROWS:
    for n in {int(x) for x in r[4].split(', ') if x}: by[n] += 1
print("each name of the seventeen by a field's namings with it:")
for n in sorted(NAME): print(f'    {by[n]:3d}  {NAME[n]}')
print('  names with none: ' + (', '.join(NAME[n] for n in sorted(NAME) if not by[n]) or 'none'))
seen = {}
for r in ROWS: seen.setdefault(r[0].lower(), []).append(r[1])
twice = {w: g for w, g in seen.items() if len(g) > 1}
print(f"a field's naming in two gatherings or more: {len(twice)}" + (': ' + '; '.join(f'{w}, {len(g)}' for w, g in twice.items()) if twice else ''))
print('each check is' if all(ok for _, ok in checks) else 'a check is-not')
