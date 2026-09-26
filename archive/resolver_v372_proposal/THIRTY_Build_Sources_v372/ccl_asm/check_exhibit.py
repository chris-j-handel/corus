import re, collections, sys, os
F = os.path.join(os.environ.get('CCL_WORK', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v372.md')
t = open(F, encoding='utf-8').read()
lines = t.split('\n')
ok = True
# 1. ids unique, follows exist
ids = collections.Counter(); fol = []
for l in lines:
    m = re.match(r'^\| ([A-Z]+\d+) \| (origin|definition|premise|exact|run|field|nye)\b.*?\| (.*?) \|', l)
    if m:
        ids[m.group(1)] += 1
        fol.append((m.group(1), m.group(3)))
dups = [k for k, v in ids.items() if v > 1]
missing = []
for lid, f in fol:
    if f.strip() in ('—', ''): continue
    for x in re.split(r',\s*', f):
        mm = re.fullmatch(r'([A-Z]+\d+)', x.strip())
        if not mm or mm.group(1) not in ids: missing.append((lid, x))
print('links', sum(ids.values()), 'distinct', len(ids), 'duplicates', dups, 'follows missing', missing)
ok &= not dups and not missing
# every id cited in Part NINE / TEN exists
nine = t[t.index('# PART NINE'):]
cited = set(re.findall(r'\b([A-Z]{1,2}\d+)\b', nine)) - {'R3', 'K5', 'K6'} | set()
bad = sorted(c for c in set(re.findall(r'\b([A-Z]{1,2}\d+)\b', nine)) if c not in ids)
print('ids cited in NINE and TEN not in the chain:', bad)
ok &= not bad
# 2. family words: outside *italic*, "quoted" spans, and Carried at section names of other files
fam = re.compile(r'\b(what|whatever|whatsoever|how|however|somehow|anyhow|where|wherever|whereas|whereby|wherein|whereof|nowhere|somewhere|elsewhere|anywhere|everywhere|whereabouts)\b', re.I)
hits = []
for i, l in enumerate(lines, 1):
    s = re.sub(r'\*[^*]+\*', '', l)            # italic quoted words
    s = re.sub(r'"[^"]*"', '', s)              # quoted field words
    s = re.sub(r'“[^”]*”', '', s)
    if s.startswith('| '):                     # the Carried at cell names another file's section
        cells = [c for c in re.split(r'(?<!\\)\|', s)[1:-1]]
        if len(cells) == 5: s = '|'.join(cells[:4])
    for m in fam.finditer(s):
        hits.append((i, m.group(0), l[max(0, m.start() - 60):m.end() + 40]))
print('family words outside quotation:', hits)
ok &= not hits
carried = [(i, m.group(0)) for i, l in enumerate(lines, 1) if l.startswith('| ') and len(re.split(r'(?<!\\)\|', l)) == 7
           for m in fam.finditer(re.split(r'(?<!\\)\|', l)[5])]
print('family words inside Carried at (other files\' section names):', carried)
# 3. contents against headings
body_start = t.index('\n---\n')
front, body = t[:body_start], t[body_start:]
heads = []
for l in body.split('\n'):
    if l.startswith('# PART'): heads.append(('P', l[2:]))
    elif l.startswith('## '): heads.append(('S', l[3:]))
cont = []
started = False
for l in front.split('\n'):
    if l.startswith('**PART'): cont.append(('P', l.strip('*'))); started = True
    elif started and l and l != '&nbsp;': cont.append(('S', l))
print('contents entries', len(cont), 'headings', len(heads), 'match', cont == heads)
if cont != heads:
    for a, b in zip(cont, heads):
        if a != b: print('  differ:', a, b); break
ok &= cont == heads
print('parts:', [h for k, h in heads if k == 'P'])

# 4. the Follows relation is acyclic: no link reaches its own prior through its dependents
import sys
sys.setrecursionlimit(10000)
FOLG = {}
for l in lines:
    mm = re.match(r'^\| ([A-Z]+\d+) \| (origin|definition|premise|exact|run|field|nye)\b.*?\| (.*?) \|', l)
    if mm: FOLG[mm.group(1)] = [x.strip() for x in mm.group(3).split(',') if re.fullmatch(r'[A-Z]+\d+', x.strip())]
color = {}; cyc = []
def dfs(v, path):
    color[v] = 1; path.append(v)
    for w in FOLG.get(v, []):
        if w not in FOLG: continue
        if color.get(w) == 1: cyc.append(path[path.index(w):] + [w])
        elif not color.get(w): dfs(w, path)
    path.pop(); color[v] = 2
for v in FOLG:
    if not color.get(v): dfs(v, [])
print('Follows cycles:', cyc[:3])
ok &= not cyc
print('ALL CHECKS', 'PASS' if ok else 'FAIL')
