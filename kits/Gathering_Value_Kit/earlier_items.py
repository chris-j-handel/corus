"""Finds the item lines an earlier gathering wrote, so a slice gathered under an earlier brief can be read again and mended.

Usage: python3 kits/Gathering_Value_Kit/earlier_items.py LIVING_TITLE OUT_RESOLVED.json OUT_LINES.json GATHERED.json [READING.json ...]

It resolves each gathered file with its readings as apply_gathered.py did (corrections replace every entry of their source),
renders each item as apply_gathered.py renders it (both as placed and as a droplet, for a quote gone stale since), and finds
each rendering in gathering-value/. It writes the resolved draft (items and leavings, for a new reading for harm) and the
lines found (for remove_gathered.py), and names each item found at no place or at several."""
import glob, json, re, sys
title, out_resolved, out_lines, files = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
gathered = [f for f in files if 'reading' not in f]
readings = [f for f in files if 'reading' in f]
items, leaving = [], []
for g in gathered:
    G = json.load(open(g)); items += G['items']; leaving += G.get('leaving', [])
corr = [c for r in readings for c in json.load(open(r)).get('corrections', []) if c.get('fixed') is not None]
for f in {c['from'] for c in corr}:
    items = [i for i in items if i.get('from') != f]; leaving = [l for l in leaving if l.get('from') != f]
for c in corr:
    for f in (c['fixed'] if isinstance(c['fixed'], list) else [c['fixed']]):
        f = dict(f); f.setdefault('from', c['from']); (items if 'kind' in f else leaving).append(f)
json.dump({'slice': ' + '.join(gathered), 'items': items, 'leaving': leaving}, open(out_resolved, 'w'), indent=1, ensure_ascii=False)

def render(i):
    k = i['kind']
    if k == 'incohering': return f'- **Possible incohering** · "{i["sentence"]}" → {i["text"]}'
    if k == 'exploring': return f'- **Possible exploring** · {i["text"]} — at "{i["sentence"]}"'
    if k == 'reading': return f'- **A reading** · {i["text"]}'
    h = i.get('kind_hint')
    return f'- {i["text"]}' + (f' *(possible {h})*' if h in ('exploring', 'incohering') else ' *(a reading)*' if h == 'reading' else '')

def as_droplet(i):
    return render({'kind': 'droplet', 'kind_hint': i['kind'], 'text': f'{i["text"]} — at *{i.get("sentence","").strip()}*'})

lines = {}
for p in glob.glob('gathering-value/*.md'):
    for l in open(p, encoding='utf-8').read().split('\n'):
        if l.startswith('- '): lines.setdefault(l, []).append(p)
found, missing, several = [], [], []
for i in items:
    cands = [render(i)] + ([as_droplet(i)] if i['kind'] in ('incohering', 'exploring') else [])
    hit = [c for c in cands if c in lines]
    if not hit: missing.append(i.get('from', '')[:70])
    elif len(lines[hit[0]]) > 1 or hit[0] in found: several.append(hit[0][:90])
    else: found.append(hit[0])
json.dump(found, open(out_lines, 'w'), indent=1, ensure_ascii=False)
print(f'{len(items)} items resolved, {len(found)} found once, {len(missing)} at no place, {len(several)} at several')
for m in missing: print('  no place:', m)
for s in several: print('  several:', s)
