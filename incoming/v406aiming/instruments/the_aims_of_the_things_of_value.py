"""The aims of the things of value: the log of the aims beside the managing table.

A thing of the managing table, named word for word as the table names it, with the
log's rows naming it a home, by an aim's number: the section of Exhibit FOURTEEN's
log, 2.1 to 2.10, and its row in that section, 2.4.9 the ninth row of Number and form.

A living file, a working document and a folder are found by the log's own homes. A
working session is found by its origin destiny, as its line at the exchange says it.
A thing no home names is laid with this session's reading, marked as such, for a
going through; and with no reading, none.

Usage: python3 -I the_aims_of_the_things_of_value.py LOG_CSV MANAGING_TABLE_CSV OUT_AIMS_CSV OUT_ROOTS_CSV
"""
import csv, re, sys, collections

log_csv, table_csv, out_aims, out_roots = sys.argv[1:5]
log = list(csv.DictReader(open(log_csv)))
table = list(csv.DictReader(open(table_csv)))

bands = []
for r in log:
    if r['band'] not in bands:
        bands.append(r['band'])
seen = collections.Counter()
for r in log:
    seen[r['band']] += 1
    r['n'] = f"2.{bands.index(r['band']) + 1}.{seen[r['band']]}"
by_name = {r['destiny'].strip().rstrip('.'): r for r in log}


def homes(r):
    return [h.strip() for h in re.split(r';\s*', r['home']) if h.strip()]


def short(thing):
    m = re.match(r"Exhibit ([A-Z-]+) (.+)", thing)
    return (f"Exhibit {m.group(1)}", m.group(2)) if m else (None, thing)


def names_thing(home, thing):
    ex, nm = short(thing)
    if thing == 'Exhibit FOURTEEN Natural Destinies' and re.match(r'(?i)this exhibit\b', home):
        return True
    if thing == 'The window of the opening' and re.match(r'(?i)the window\b', home):
        return True
    if thing == 'Exhibit THIRTY-ONE Me' and re.match(r'Me\b', home):
        return True
    if ex and re.match(re.escape(ex) + r"(?![-A-Z])", home):
        return True
    if nm == 'Natural Intelligence':
        return re.match(r"Natural Intelligence(?! Corus)", home) is not None
    if nm in ('Me',):
        return False
    if thing.startswith('incoming/'):
        return thing in home
    return re.match(re.escape(nm) + r"(?![A-Za-z])", home) is not None


# A working session's origin destiny, by its own line at the exchange of 23 November.
origin = {
    'v406me': ['Value brought home'],
    'v406all2': ['The window of the opening'],
    'v407primes': ['Spirals and tori of selves', 'A prime ladder of societies'],
    'v406aiming': ['A destiny, next living possibling ahead'],
    'v406other2': ['A complete co-chaining'],
    'v406all2-2': ['Seventeen names in four four-cyclings'],
    'v406geodesic2': ['Word, number and illustrating, one thing three ways'],
    'incoming/v406Reiman': ['Spirals and tori of selves', 'Primes and composites'],
}
# This session's judging, for a thing no home of the log names: for a going through.
reading = {
    'The next version, offer #717': ['Versions, sessions and a fresh reader', 'A living file'],
    'corus.me': ["The seventeen names' tables, by a partner's suggesting", 'An AI link into the living files'],
    'Start here': ['Versions, sessions and a fresh reader'],
    'The exchange': ['A living expedition', 'Versions, sessions and a fresh reader'],
    'The Gathering Value Kit': ['Value brought home'],
    "The Living File Registry's kit": ['A living file'],
    "The Co-Chaining Logic Registry's kit": ['A complete co-chaining'],
    "Natural Illustrating's kit": ['Word, number and illustrating, one thing three ways'],
    "Natural Networking's kit": ['The Natural Network surface'],
    'The window of the seventeen names': ['Seventeen names in four four-cyclings'],
    "The primes on the resolver's surface, beside the Riemann hypothesis": ['Spirals and tori of selves', 'Primes and composites'],
    'Sphere with a Three-Right-Angle Triangle': ['Sphere and torus, one and then the other'],
    'The valuables of the living expedition, the board': ['Value brought home'],
    'The piles in the gathering files': ['Value brought home'],
    'One sentence in more than one note': ['Value brought home'],
    'The opening\'s lines in eight pages': ['The window of the opening'],
    'Four generations of an opening, waiting to enter': ['The window of the opening'],
}

rows, unfound = [], []
for t in table:
    thing = t['The thing']
    found, how = [], ''
    key = thing if thing in origin else ('incoming/' + thing if 'incoming/' + thing in origin else None)
    if key:
        found = [by_name[a] for a in origin[key]]
        how = 'its origin destiny, by its line at the exchange'
    hs = [r for r in log if any(names_thing(h, thing) for h in homes(r))]
    if hs:
        found += [r for r in hs if r not in found]
        how = (how + '; ' if how else '') + 'the log\'s homes naming it'
    if not found and thing in reading:
        found = [by_name[a] for a in reading[thing]]
        how = "this session's judging, for a going through"
    if not found:
        how = 'no aim found yet'
        unfound.append(thing)
    rows.append({
        'The thing': thing,
        'Its kind': t['Its kind'],
        'Its aims, by the log\'s numbers': ', '.join(r['n'] for r in found),
        'Its aims, by name': '; '.join(r['destiny'].strip().rstrip('.') for r in found),
        'How they are found': how,
    })

with open(out_aims, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

# The four roots and the ten bands: aims of a band naming a living file of a root a home.
roots = ['same-existing', 'observing', 'possibling', 'discovering']
root_of = {}
for t in table:
    m = re.search(r'of the ([a-z-]+) root', t['Its kind'])
    if m:
        root_of[t['The thing']] = m.group(1)
cross = collections.defaultdict(collections.Counter)
for r in log:
    rs = {root_of[t] for t in root_of if any(names_thing(h, t) for h in homes(r))}
    for x in rs or {'no living file'}:
        cross[r['band']][x] += 1
with open(out_roots, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['A band of the log', 'its aims'] + [f'naming a file of the {x} root' for x in roots] + ['naming no living file'])
    n = collections.Counter(r['band'] for r in log)
    for i, b in enumerate(bands, 1):
        w.writerow([f'2.{i} {b}', n[b]] + [cross[b][x] for x in roots] + [cross[b]['no living file']])

print(f'{len(rows)} things; {sum(1 for r in rows if r["How they are found"] != "no aim found yet")} with aims; no aim found yet: {len(unfound)}')
for u in unfound:
    print('  ', u)
