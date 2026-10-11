"""Session v381F: each living file's far side in Natural Intelligence, the section it loops out of and back to.

Runs from the repository root: python3 incoming/v381F/loopings.py
Reads Natural Intelligence at the root and splits it at its sections; reads each other living file and finds
the words it carries most and the set carries least (each word weighted by how many files carry it); then
finds the sections of Natural Intelligence those words are at most, the file's far side, said at two sections.
Writes Loopings.tsv beside this script and prints the map. A computing, deciding nothing: the far side it finds
is where the words meet, and whether the file loops there is read at the file.
"""
import json, re, math, collections

files = json.load(open('files.json'))
ni = next(f for f in files if f.startswith('Natural_Intelligence_v'))
text = {f: open(f, encoding='utf-8').read() for f in files}
WORD = re.compile(r"[a-z][a-z-]{4,}")
STOP = set('about above after again along among because before being below between could every first other'
           ' their there these those through under until where which while would shall might within without'
           ' thing things exhibit natural intelligence section table whole'.split())


def words(s):
    return [w for w in WORD.findall(s.lower()) if w not in STOP]


# Natural Intelligence at its sections, Exhibit ONE inside it left aside (the file's own sentences)
body = text[ni].split('# EXHIBIT ONE')[0] + text[ni].split('# FOUR · RESOLVING')[1]
parts = re.split(r"\n## (\d+\.\d+ [^\n]+)\n", body)
sections = {}
for i in range(1, len(parts), 2):
    sections[parts[i]] = collections.Counter(words(parts[i + 1]))

df = collections.Counter()
per_file = {}
for f in files:
    c = collections.Counter(words(text[f]))
    per_file[f] = c
    for w in c:
        df[w] += 1
N = len(files)


def short(f):
    m = re.match(r"Exhibit_([A-Z-]+)_", f)
    return ('Exhibit ' + m.group(1)) if m else next(l[2:].strip() for l in text[f].split('\n') if l.startswith('# '))


def subtitle(f):
    ls = text[f].split('\n')
    t = next(i for i, l in enumerate(ls) if l.startswith('# '))
    return next(l.strip('* ').strip() for l in ls[t + 1:] if l.startswith('**'))


rows = []
for f in files:
    if f == ni:
        continue
    c = per_file[f]
    total = sum(c.values())
    weight = {w: (n / total) * math.log(N / df[w]) for w, n in c.items() if df[w] < N}
    own = sorted(weight, key=weight.get, reverse=True)[:40]
    scores = {}
    for sec, sc in sections.items():
        size = sum(sc.values()) or 1
        scores[sec] = sum(weight[w] * math.sqrt(sc[w]) for w in own if w in sc) / math.sqrt(size)
    best = sorted(scores, key=scores.get, reverse=True)[:2]
    rows.append((short(f), subtitle(f), best, own[:8]))

with open('incoming/v381F/Loopings.tsv', 'w', encoding='utf-8') as out:
    out.write('file\tsubtitle\tfar side in Natural Intelligence, first\tsecond\tthe words it carries most and the set least\n')
    for name, sub, best, own in rows:
        out.write('%s\t%s\t%s\t%s\t%s\n' % (name, sub, best[0], best[1], ', '.join(own)))

print('%-28s %-46s %s' % ('file', 'far side in Natural Intelligence', 'its own words'))
for name, sub, best, own in rows:
    print('%-28s %-46s %s' % (name, best[0][:46], ', '.join(own[:5])))
