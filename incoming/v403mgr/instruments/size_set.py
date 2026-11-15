"""The set sized for the method by three. Reads the files and writes none; a number here sizes a pass and decides nothing.

Use: python3 -I incoming/v403mgr/instruments/size_set.py <root>

Its rule of a sentence: a line of prose, outside code, tables, headings and rules, with its list mark, its step number
and its bold and italic marks out, divided after . ? or ! before a capital, a digit, a quote mark or a bracket; four words or more.
An entry of a file's contents, a section's number and its title, is no sentence.
Exhibit ONE written inside Natural Intelligence is read once, at Exhibit ONE.

Returned at main, Merge #694, 15 November 2026:
  living files 33, prose sentences about 37,891; the largest Exhibit TWENTY-ONE 9,138, Natural Intelligence Corus 3,715,
    Exhibit FIVE 2,705; Natural Intelligence 1,478
  sentences of 8 words or more, word for word in two living files or more: 65, their places after the first 82;
    47 of the 65 in Natural Intelligence and Exhibit THIRTY only, the opening as steps
  sentences of 8 words or more, twice or more within one living file: 111
  gathering files 33, droplets 6,549; Natural Intelligence 1,945, Natural Physics 779, Natural Naming 494
  bytes: living 5,612,001, gathering 3,348,112
  names of a parity by their living places: other-parity 48 in 7 files, self-parity 51 in 7, social-parity 49 in 3,
    me-parity 7 in 3, all-parity 7 in 3, both-parity 0, universal-parity 0, other-than-parity 0
"""
import collections, glob, json, os, re, sys

R = sys.argv[1]
files = json.load(open(os.path.join(R, 'files.json')))

def prose_sentences(text):
    out = []; fence = False
    for l in text.split('\n'):
        if l.startswith('```'): fence = not fence; continue
        if fence or l.startswith('#') or l.startswith('|') or l.strip() in ('', '---', '&nbsp;'): continue
        s = re.sub(r'^[-*]\s+', '', l.strip())
        if re.match(r'^\d+\.\d+\s', s): continue                 # an entry of a file's contents
        s = re.sub(r'^\d+\.\s+', '', s).rstrip(' \\')
        s = re.sub(r'\*\*|\*|`', '', s)
        for p in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9"“(])', s):
            if len(p.split()) >= 4: out.append(p.strip())
    return out

total = 0; per = {}; at = collections.defaultdict(set); times = collections.Counter()
for f in files:
    t = open(os.path.join(R, f), encoding='utf-8').read()
    if f.startswith('Natural_Intelligence_v'):
        a = t.find('# EXHIBIT ONE · NATURAL RESOLVER'); b = t.find('\n# FOUR · RESOLVING')
        if 0 < a < b: t = t[:a] + t[b:]
    S = prose_sentences(t); per[f] = len(S); total += len(S)
    for s in S: times[s] += 1; at[s].add(f)
print('living files', len(files), ' prose sentences, about', total)
for f, n in sorted(per.items(), key=lambda x: -x[1])[:8]: print(f'  {n:6d}  {f}')
across = {s: fs for s, fs in at.items() if len(fs) >= 2 and len(s.split()) >= 8}
print('sentences of 8 words or more, word for word in two living files or more:', len(across),
      ' their places after the first:', sum(times[s] - 1 for s in across))
print('  of them, in Natural Intelligence and Exhibit THIRTY only:',
      sum(1 for fs in across.values() if all(x.startswith(('Natural_Intelligence_v', 'Exhibit_THIRTY_')) for x in fs)))
print('sentences of 8 words or more, twice or more within one living file:',
      sum(1 for s, n in times.items() if n >= 2 and len(at[s]) == 1 and len(s.split()) >= 8))
G = sorted(glob.glob(os.path.join(R, 'gathering-value', '*.md'))); droplets = {}
for g in G: droplets[os.path.basename(g)] = sum(1 for l in open(g, encoding='utf-8') if l.startswith('- '))
print('gathering files', len(G), ' droplets', sum(droplets.values()))
for g, n in sorted(droplets.items(), key=lambda x: -x[1])[:8]: print(f'  {n:6d}  {g}')
print('bytes: living', sum(os.path.getsize(os.path.join(R, f)) for f in files), ' gathering', sum(os.path.getsize(g) for g in G))
print('names of a parity, by their living places:')
for name in ['other-parity', 'self-parity', 'social-parity', 'universal-parity', 'other-than-parity', 'me-parity', 'both-parity', 'all-parity']:
    each = [len(re.findall(r'(?i)\b' + re.escape(name) + r'\b', open(os.path.join(R, f), encoding='utf-8').read())) for f in files]
    print(f'  {name:18s} places {sum(each):5d}  living files {sum(1 for c in each if c)}')
