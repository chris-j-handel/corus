"""dissolve_older.py OFFERINGS JSONL LIVINGNAME LIVINGFILE"""
import sys, json, os, collections
off, jl, name, liv = sys.argv[1:5]
L = open(off).read().split('\n')
mark = [i for i, l in enumerate(L) if l.startswith('## The session v389, entered and dissolved')]
assert len(mark) == 1
k = mark[0]
h = [i for i, l in enumerate(L[:k]) if l.startswith('# ')][0]
front, older, tail = L[:h + 1], L[h + 1:k], L[k:]
items = [json.loads(x) for x in open(jl)]
cnt = collections.Counter(d['verdict'] for d in items)

def para(line):  # 1-based line number in the file
    i = line - 1
    if L[i].lstrip().startswith(('|', '- ', '* ')) or L[i][:1].isdigit(): return L[i]
    j = i
    while j < len(L) and L[j].strip() != '':
        j += 1
    return '\n'.join(L[i:j])

concerns = [d for d in items if d['verdict'] == 'CONCERN']
base = os.path.basename(off)[:-3]
arch = f'archive/session_v389/offerings_dissolved/{base}_before_v389.md'
idx = ['| Line | Verdict | Item | At v389 |', '|---|---|---|---|']
for d in sorted(items, key=lambda d: d['line']):
    at = d.get('where') or d.get('why') or (('of line %s' % d['of']) if d.get('of') else '')
    at = str(at).replace('|', '/').replace('\n', ' ')[:300]
    hd = d['head'].replace('|', '/').replace('\n', ' ')[:100]
    idx.append(f"| {d['line']} | {d['verdict']} | {hd} | {at} |")
open(arch, 'w').write(
    f"{base}, the sessions before v389, read at v389\n\n# {base}: the sessions before v389, read at v389\n\n"
    f"**Receiving.** Each item the sessions before v389 laid at this offerings file stands below whole, as it stood at the file, and each was read at v389 against {name}, one item at a time: "
    f"{cnt['CARRIED']} carried at the living file, {cnt['RELEASED']} resting on a form v389 released, {cnt['DUPLICATE']} a value said by another item, {cnt['RISE']} risen into the living file at v389, and {cnt['CONCERN']} concerns, which stand at the offerings file; the index below gives each item's reading. Relied on by nothing.\n\n"
    "## The index of readings\n\n" + '\n'.join(idx) + "\n\n## The items, whole\n\n" + '\n'.join(older).strip() + '\n')
rel = os.path.relpath(arch, 'carry')
sec = [f"## Standing from the sessions before v389 · v389", "",
       f"**Read at v389.** The sessions before v389 laid {len(items)} items here; read at v389 against [{name}](../{liv}), {cnt['CARRIED']} are carried at it, {cnt['RELEASED']} rest on forms v389 released, {cnt['DUPLICATE']} say a value another item says, and {cnt['RISE']} rose into it at v389, each standing whole with its reading at [`{arch}`]({rel}). The {cnt['CONCERN']} concerns below stand, each as it was laid, with the reason it stands.", ""]
for d in sorted(concerns, key=lambda d: d['line']):
    sec.append(para(d['line']))
    sec.append('')
    sec.append(f"*Standing at v389:* {str(d.get('why', '')).strip()}")
    sec.append('')
open(off, 'w').write('\n'.join(front + [''] + sec + tail))
print(off, dict(cnt))
