import re, os, sys, json, collections
root = sys.argv[1]
files = json.load(open(os.path.join(root, 'files.json')))
print("== living files: bytes, lines, open words (Improving Passes measure), floating negations ==")
openw = re.compile(r'\b(read|reading|named|said|says|never|alone|unchanged|inside|outside)\b', re.I)
neg = re.compile(r'\b(not|no|never|nothing|none|nor|cannot)\b', re.I)
diss = {w: re.compile(r'\b'+w+r'\b', re.I) for w in ['itself','couple','couples','coupling','membrane','beholding','third']}
tot = collections.Counter()
rows = []
for f in files:
    t = open(os.path.join(root, f), encoding='utf-8').read()
    d = {w: len(r.findall(t)) for w, r in diss.items()}
    rows.append((f, len(t.encode()), t.count('\n'), len(openw.findall(t)), len(neg.findall(t)), d))
    tot['bytes'] += len(t.encode()); tot['neg'] += len(neg.findall(t)); tot['open'] += len(openw.findall(t))
    for w in d: tot[w] += d[w]
for f, b, l, o, n, d in rows:
    print(f"{f[:58]:58s} {b:8d} {l:5d} open={o:4d} neg={n:5d} " + " ".join(f"{k}={v}" for k, v in d.items() if v))
print("TOTAL bytes", tot['bytes'], "open", tot['open'], "neg", tot['neg'], {k: tot[k] for k in diss})
print()
print("== offerings: open items per file ==")
kinds = ['Droplet', 'Insertlet', 'Concern', 'Possible project', 'Aimed at']
grand = collections.Counter()
for f in sorted(os.listdir(os.path.join(root, 'carry'))):
    if 'Offerings' not in f: continue
    t = open(os.path.join(root, 'carry', f), encoding='utf-8').read()
    c = {k: len(re.findall(r'\*\*' + re.escape(k) + r'\b', t)) for k in kinds}
    for k in kinds: grand[k] += c[k]
    tags = collections.Counter(re.findall(r'\bv3(?:8\d|9\d)[A-Z]*\b', t))
    newest = sorted(tags, key=lambda s: (int(re.match(r'v(\d+)', s).group(1)), s))[-3:] if tags else []
    print(f"{f[:60]:60s} {len(t.encode()):7d}B " + " ".join(f"{k}={v}" for k, v in c.items() if v) + f"  tags:{sum(tags.values())} newest:{newest}")
print("GRAND", dict(grand))
