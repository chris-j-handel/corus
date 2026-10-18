"""offerings_resolve_all.py OFFERINGS JSONL "LIVING TITLE" LIVINGFILE VERSION
Each item at an offerings file (one JSON line per item: line, head, verdict CARRIED|RELEASED|DUPLICATE|RISE|CONCERN, where/why/of)
is archived whole with its verdict at archive/session_vVERSION/offerings_dissolved/<offerings>_resolved_vVERSION.md;
the offerings file keeps its title and a section of the concerns standing, each with its reason."""
import sys, json, os, collections
off, jl, name, liv, ver = sys.argv[1:6]
L = open(off).read().split('\n')
h = [i for i, l in enumerate(L) if l.startswith('# ')][0]
front, body = L[:h + 1], L[h + 1:]
items = [json.loads(x) for x in open(jl) if x.strip()]
cnt = collections.Counter(d['verdict'] for d in items)
def para(line):
    i = line - 1; j = i
    while j < len(L) and L[j].strip() != '':
        j += 1
    return '\n'.join(L[i:j])
base = os.path.basename(off)[:-3]
os.makedirs(f'archive/session_v{ver}/offerings_dissolved', exist_ok=True)
arch = f'archive/session_v{ver}/offerings_dissolved/{base}_resolved_v{ver}.md'
idx = ['| Line | Verdict | Item | At v' + ver + ' |', '|---|---|---|---|']
for d in sorted(items, key=lambda d: d['line']):
    at = str(d.get('where') or d.get('why') or (('of line %s' % d['of']) if d.get('of') else '')).replace('|', '/').replace('\n', ' ')[:300]
    idx.append(f"| {d['line']} | {d['verdict']} | {d['head'].replace('|', '/')[:100]} | {at} |")
open(arch, 'w').write(f"{base}, resolved at v{ver}\n\n# {base}: resolved at v{ver}\n\n**Receiving.** Each item at this offerings file stands below whole, as it stood, each met at v{ver} against {name}: "
    f"{cnt['CARRIED']} carried, {cnt['RELEASED']} resting on a released form, {cnt['DUPLICATE']} duplicating another item, {cnt['RISE']} risen into {name}, and {cnt['CONCERN']} concerns, which stand at the offerings file. Relied on by nothing.\n\n## Index\n\n"
    + '\n'.join(idx) + "\n\n## Items, whole\n\n" + '\n'.join(body).strip() + '\n')
rel = os.path.relpath(arch, 'carry')
sec = [f"## Standing · v{ver}", "", f"**Met at v{ver}.** {len(items)} items stood here; met against [{name}](../{liv}), {cnt['CARRIED']} are carried, {cnt['RELEASED']} rest on released forms, {cnt['DUPLICATE']} duplicate another item and {cnt['RISE']} rose into it, each whole with its verdict at [`{arch}`]({rel}). The {cnt['CONCERN']} concerns below stand, each with its reason; {cnt['CONCERN']} stand now.", ""]
for d in sorted([d for d in items if d['verdict'] == 'CONCERN'], key=lambda d: d['line']):
    sec += [para(d['line']), '', f"*Standing at v{ver}:* {str(d.get('why', '')).strip()}", '']
open(off, 'w').write('\n'.join(front + [''] + sec))
print(off, dict(cnt))
