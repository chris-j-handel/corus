"""Writes a gathered slice into its gathering-value files, after its reading for harm.

Usage: python3 kits/Gathering_Value_Kit/apply_gathered.py LIVING_TITLE GATHERED.json [READING.json ...] [--dry]

LIVING_TITLE is the title of the living file the slice belongs to (e.g. "Natural Intelligence"); an item with its own "file" goes to that file.
Each reading's corrections replace the item or leaving with the same "from"; a correction whose "fixed" has a "kind" becomes an item.
Each item is checked before anything is written: its file and section exist, and a quoted sentence stands word for word at its living file.
A failed check stops the whole slice, all or none."""
import glob, json, os, re, sys

args = [a for a in sys.argv[1:] if a != '--dry']
DRY = '--dry' in sys.argv
title, gathered, readings = args[0], args[1], args[2:]
G = json.load(open(gathered))
items, leaving = G['items'], G.get('leaving', [])
corrections = [c for r in readings for c in json.load(open(r)).get('corrections', []) if c.get('fixed') is not None]
for f in {c['from'] for c in corrections}:          # an entry with corrections is replaced by all of them together
    items = [i for i in items if i.get('from') != f]
    leaving = [l for l in leaving if l.get('from') != f]
for c in corrections:
    f = dict(c['fixed'])
    f.setdefault('from', c['from'])
    (items if 'kind' in f else leaving).append(f)

norm = lambda s: re.sub(r'\s+', ' ', re.sub(r'[*`_\\]', '', s)).strip()
fname = lambda t: re.sub(r'\s+', '_', t.strip()) + '.md'


def living_text(t):
    for p in sorted(glob.glob('*_v*.md')):
        L = open(p, encoding='utf-8').read()
        m = re.search(r'^# (.+)$', L, re.M)
        if m and m.group(1).strip() == t:
            return norm(L)
    return None


def render(i):
    k = i['kind']
    if k == 'incohering':
        return f'- **Possible incohering** · "{i["sentence"]}" → {i["text"]}'
    if k == 'exploring':
        return f'- **Possible exploring** · {i["text"]} — at "{i["sentence"]}"'
    hint = i.get('kind_hint')
    return f'- {i["text"]}' + (f' *(possible {hint})*' if hint in ('exploring', 'incohering') else '')


errors, by_file = [], {}
for i in items:
    t = i.get('file') or title
    p = os.path.join('gathering-value', fname(t))
    if not os.path.exists(p):
        errors.append(f'no gathering-value file for {t!r}: {i.get("from","")[:60]}'); continue
    if i.get('kind') not in ('incohering', 'exploring', 'droplet'):
        errors.append(f'kind {i.get("kind")!r}: {i.get("from","")[:60]}'); continue
    if i['kind'] != 'droplet':
        lt = living_text(t)
        if lt is None or norm(i.get('sentence', '')) not in lt:
            errors.append(f'sentence not at {t} word for word: {i.get("sentence","")[:90]}'); continue
    by_file.setdefault(p, []).append(i)

for p, its in by_file.items():
    L = open(p, encoding='utf-8').read().split('\n')
    heads = {re.sub(r'^#{2,3} ', '', l).strip(): n for n, l in enumerate(L) if re.match(r'^#{2,3} ', l)}
    for i in its:
        if i['section'] not in heads:
            errors.append(f'no section {i["section"]!r} at {p}')

if errors:
    print('NOTHING WRITTEN, all or none:'); [print(' ', e) for e in errors]; sys.exit(1)

total = 0
for p, its in by_file.items():
    L = open(p, encoding='utf-8').read().split('\n')
    for i in its:
        n = next(k for k, l in enumerate(L) if re.match(r'^#{2,3} ', l) and re.sub(r'^#{2,3} ', '', l).strip() == i['section'])
        e = next((k for k in range(n + 1, len(L)) if re.match(r'^#{2,3} ', L[k])), len(L))
        while e > n + 1 and not L[e - 1].strip():
            e -= 1
        block = [render(i)]
        if e == n + 1:
            block = [''] + block
        L[e:e] = block
        total += 1
    if not DRY:
        open(p, 'w', encoding='utf-8').write('\n'.join(L).rstrip() + '\n')
print(('would write ' if DRY else 'written ') + f'{total} items at {len(by_file)} files; {len(leaving)} leaving')
