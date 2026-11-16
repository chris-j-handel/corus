"""Each droplet of the gathering files found more than once, word for word: within one gathering file, and in two
gathering files or more, each said with its places; and, by the managing session's first rule, a droplet more
than once with one heading of one gathering file is once. All or none at all, by each line.
Reads each gathering file; executes; with *apply* it writes the gathering files of the first rule alone.

Use: python3 -I incoming/v403cohering/instruments/each_droplet_said_more_than_once.py <root>          each droplet found more than once, and nothing written
     python3 -I incoming/v403cohering/instruments/each_droplet_said_more_than_once.py <root> apply    the first rule, written

What it reads. A droplet: a line opening with a hyphen. Two droplets are one found twice with each letter the
same. A place: its gathering file, and the heading it is under.

A rule for each kind, each the managing session v403mgr's, 16 November:
  1. One droplet more than once with one heading of one gathering file: the first is the droplet, and each other
     is away, no word of it lost.
  2. One droplet with each of more sections than one, each section's own living sentence the same words: each is
     its section's own, and each is as it is.
  3. One saying in two gathering files or more, with no file of its own in it: each is as it is, and the table
     of them is the partners' to read; a home for one concept is the partners' word.

Returned at main, 16 November 2026, after Merge #792: eleven droplets found more than once. Within one gathering
file, two: Exhibit TWENTY-SEVEN Living Ghost Registry's has one four times, each with its own section, rule 2;
Exhibit EIGHTEEN Natural Physics's has one six times at its back, rule 1. In two gathering files or more, nine:
three of *this file*, each its own file's, and six of one saying, rule 3.
Applied at main after Merge #802, 16 November 2026, the first rule: Exhibit EIGHTEEN Natural Physics's gathering
file, five lines away and the first of the six as it is; each droplet by its letters is in the file, as before.
"""
import glob, os, re, sys

R = sys.argv[1]; APPLY = len(sys.argv) > 2 and sys.argv[2] == 'apply'
GV = os.path.join(R, 'gathering-value')
FILES = {os.path.basename(g)[:-3]: open(g, encoding='utf-8').read().split('\n') for g in sorted(glob.glob(os.path.join(GV, '*.md')))}
places = {}                                   # a droplet's line -> [(title, heading, index of its line)]
for title, L in FILES.items():
    cur = None
    for k, l in enumerate(L):
        if re.match(r'^#{2,3} ', l): cur = re.sub(r'^#{2,3} ', '', l).strip()
        if l.startswith('- '): places.setdefault(l, []).append((title, cur, k))
more = {l: w for l, w in places.items() if len(w) > 1}
within = {l: w for l, w in more.items() if len({t for t, _, _ in w}) == 1}
across = {l: w for l, w in more.items() if len({t for t, _, _ in w}) > 1}
print(f'{len(places)} droplets by their letters; {len(more)} found more than once: {len(within)} within one gathering file, {len(across)} in two or more')

away = {}                                     # rule 1: title -> indexes of the lines going
print('within one gathering file:')
for l, w in within.items():
    one_heading = len({h for _, h, _ in w}) == 1
    print(f"  {len(w)} times in {w[0][0].replace('_', ' ')}, rule {'1: the first is the droplet' if one_heading else '2: each its section own'}: {l[:100]}")
    print('      with: ' + '; '.join(sorted({h or 'no heading' for _, h, _ in w})))
    if one_heading: away.setdefault(w[0][0], []).extend(k for _, _, k in w[1:])
print('in two gathering files or more, rule 3, each as it is:')
for l, w in sorted(across.items(), key=lambda x: -len(x[1])):
    own = 'of this file, each its own' if re.search(r'\b(of|at) this file\b|\bthis file is\b', l) else 'one saying'
    print(f'  {len(w)} files, {own}: {l[:110]}')

n = sum(len(v) for v in away.values())
if APPLY and n:
    before = {t: set(l for l in FILES[t] if l.startswith('- ')) for t in away}
    for t, ks in away.items():
        L = FILES[t]
        for k in sorted(ks, reverse=True): del L[k]
        assert before[t] == set(l for l in L if l.startswith('- ')), 'a droplet by its letters is lost'
        open(os.path.join(GV, t + '.md'), 'w', encoding='utf-8').write('\n'.join(L))
print(('written, ' if APPLY and n else '') + f"rule 1: {n} lines {'away' if APPLY else 'to go'}" + (': ' + ', '.join(f"{t.replace('_', ' ')} {len(v)}" for t, v in away.items()) if n else ''))
