"""Each droplet of the gathering files found more than once, word for word: within one gathering file, and in two
gathering files or more, each said with its places. All or none at all, by each line.
Reads each gathering file; executes; writes no file; decides nothing: which of two goes is a rule to ask.

Use: python3 -I incoming/v403cohering/instruments/each_droplet_said_more_than_once.py <root>

What it reads. A droplet: a line opening with a hyphen. Two droplets are one found twice with each letter the
same. A place: its gathering file, and the heading it is under.

Returned at main, 16 November 2026, after Merge #792: eleven droplets found more than once.
  Within one gathering file, two: Exhibit TWENTY-SEVEN Living Ghost Registry's gathering file has one four times,
  each with its own section and that section's own living sentence, *Others: no record so far.*; Exhibit EIGHTEEN
  Natural Physics's has one six times at its back, *v401mgr's layings and notes since the reading before: none.*
  In two gathering files or more, nine: one in twenty-five, one in four and one in three, each of *this file* and
  its own file's; and six in two, three or four files, each one saying with no file of its own in it.
"""
import glob, os, re, sys

R = sys.argv[1]
places = {}
for g in sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md'))):
    title, cur = os.path.basename(g)[:-3].replace('_', ' '), None
    for l in open(g, encoding='utf-8').read().split('\n'):
        if re.match(r'^#{2,3} ', l): cur = re.sub(r'^#{2,3} ', '', l).strip()
        if l.startswith('- '): places.setdefault(l, []).append((title, cur))
more = {l: w for l, w in places.items() if len(w) > 1}
within = {l: w for l, w in more.items() if len({t for t, _ in w}) == 1}
across = {l: w for l, w in more.items() if len({t for t, _ in w}) > 1}
print(f'{len(places)} droplets by their letters; {len(more)} found more than once: {len(within)} within one gathering file, {len(across)} in two or more')
print('within one gathering file:')
for l, w in within.items():
    print(f'  {len(w)} times in {w[0][0]}: {l[:110]}')
    print('      under: ' + '; '.join(h or 'no heading' for _, h in w))
print('in two gathering files or more:')
for l, w in sorted(across.items(), key=lambda x: -len(x[1])):
    own = 'of this file, each its own' if re.search(r'\b(of|at) this file\b|\bthis file is\b', l) else 'one saying'
    print(f'  {len(w)} files, {own}: {l[:110]}')
    print('      ' + '; '.join(f'{t}, {h}' for t, h in w[:6]) + (' …' if len(w) > 6 else ''))
