"""Stale by a match: a POINTING at a sentence that stands no longer; the item's concern rides with its reason (3.5, 1.5).
Stale concerns by a match (Geodesic Improving Method 1.5): an offerings item that quotes a living sentence
beside which it stands is stale when no part of its quote (first six words) stands at the living file now.
Sizes; decides nothing. Usage: python3 -I incoming/v392F/stale_check.py <root>"""
import re, os, sys, json, glob
root = sys.argv[1]
files = json.load(open(os.path.join(root, 'files.json')))
def living_for(off):
    b = os.path.basename(off)
    m = re.match(r'(Exhibit_[A-Z-]+)_Offerings_to_(.*)\.md', b)
    stem = (m.group(1) + '_' + m.group(2)) if m else b.replace('Offerings_to_', '').replace('.md', '')
    for f in files:
        if f.startswith(stem + '_v'): return f
    return None
def norm(s): return re.sub(r'[^a-z0-9 ]+', ' ', s.lower()); 
tot_items = tot_quoted = tot_stale = 0
rows = []
for off in sorted(glob.glob(os.path.join(root, 'carry', '*Offerings*'))):
    lf = living_for(off)
    if not lf:
        print(f'{"-":>5s} {"-":>6s} {"-":>5s}  {os.path.basename(off)}  (no living file at root; not measured)'); continue
    live = norm(open(os.path.join(root, lf), encoding='utf-8').read())
    live = re.sub(r'\s+', ' ', live)
    t = open(off, encoding='utf-8').read()
    paras = [p for p in t.split('\n\n') if p.startswith('**')]
    quoted = stale = 0
    for p in paras:
        tot_items += 1
        # quotes: Beside "...", quotes in *Standing* paragraphs, or ** ... — beside '...' **
        # double quotes only: an apostrophe is no quote mark (a reader for harm found 's opening a "quote")
        qs = re.findall(r'[Bb]eside ["“]([^"”]{12,})["”]', p) + re.findall(r'["“]([^"”]{20,})["”]', p)
        if not qs: continue
        quoted += 1
        found = False
        for q in qs:
            words = norm(q).split()
            for i in range(0, max(1, len(words) - 5)):
                probe = ' '.join(words[i:i + 6])
                if len(probe) > 15 and probe in live: found = True; break
            if found: break
        if not found: stale += 1
    tot_quoted += quoted; tot_stale += stale
    rows.append((stale, quoted, len(paras), os.path.basename(off)))
rows.sort(reverse=True)
print(f"{'stale':>5s} {'quoted':>6s} {'items':>5s}  offerings file")
for s, q, n, b in rows: print(f"{s:5d} {q:6d} {n:5d}  {b}")
print(f"\nitems {tot_items}, quoting a living sentence {tot_quoted}, quote at no six words of the living file now {tot_stale}")
