"""Writes or re-forms each living file's gathering-value file, gathering-value/<Title>.md, from its living file's own parts and sections.

A gathering-value file mirrors its living file's contents: a head for the whole file, each part, each section, and droplets at the back.
Re-forming keeps every item already written: items stand under their section's heading, matched by the heading's text,
and a section the living file no longer has keeps its items under its old heading until a working places them.

Usage: python3 kits/Gathering_Value_Kit/gathering_value_form.py [repository root]"""
import json, os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
OUT = os.path.join(ROOT, 'gathering-value')
DROPLETS = 'Droplets'
HEAD = 'Head, the whole file'
OPENING = 'Opening'


def structure(path):
    """Parts and sections of a living file, in order: a list of (level, text)."""
    L = open(path, encoding='utf-8').read().split('\n')
    title_i = next(i for i, l in enumerate(L) if l.startswith('# '))
    title = L[title_i][2:].strip()
    body_start = next((i for i in range(title_i, len(L)) if L[i].strip() == '---'), title_i)
    one = os.path.basename(path).startswith('Exhibit_ONE_')
    has_sections = any(re.match(r'^## ', l) for l in L)
    out, fence, skip = [], False, False
    first_part_seen = False
    for i, l in enumerate(L[body_start + 1:], body_start + 1):
        if l.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        if l.startswith('# '):
            text = l[2:].strip()
            skip = text.startswith('EXHIBIT ONE')          # Exhibit ONE's copy inside Natural Intelligence has its own file
            out.append((1, text + (' (its gathering-value is Natural Resolver\'s)' if skip else '')))
            first_part_seen = True
            continue
        if skip:
            continue
        m = re.match(r'^## (.+)$', l)
        if m:
            out.append((2, m.group(1).strip()))
            continue
        if not has_sections:
            m = re.match(r'^\*\*(\d+(?:\.\d+)+ [^*]+?)\*\*\s*$', l) or (one and re.match(r'^\*\*([^*]{3,90}?)\.?\*\*\s*$', l))
            if m and i > body_start + 3:
                out.append((2, m.group(1).strip().rstrip('.')))
    pre = [l for l in L[title_i + 1:body_start] if l.strip() and l.strip() != '&nbsp;'
           and not l.lstrip().startswith(('- ', '**', '#', '*'))]
    lead = [l for l in L[body_start + 1:] if l.strip() and l.strip() != '&nbsp;'][:1]
    if pre or not out or (lead and not lead[0].startswith('#')):
        out.insert(0, (1, OPENING))
    return title, out


def existing_items(path):
    """Items already written in a gathering-value file, by heading text."""
    if not os.path.exists(path):
        return {}
    items, cur = {}, None
    for l in open(path, encoding='utf-8').read().split('\n'):
        m = re.match(r'^#{2,3} (.+)$', l)
        if m:
            cur = m.group(1).strip()
            items.setdefault(cur, [])
            continue
        if cur is not None:
            items[cur].append(l)
    return {k: '\n'.join(v).strip() for k, v in items.items() if '\n'.join(v).strip()}


def write(living, path):
    title, parts = structure(os.path.join(ROOT, living))
    old = existing_items(path)
    used = set()
    L = [f'Gathering-Value · {title}', '', f'# {title} · Gathering-Value', '',
         f'**Each value not yet in {title}, at the section it meets.** A possible exploring is an observing not yet meeting '
         'natural torusing, said as the observing alone, with the sentence it meets. A possible incohering is a sentence not yet '
         'cohering, with its cohering re-saying beside it. A value whose place is not yet clear is a droplet at the back.', '']

    def heading(level, text):
        L.append(('## ' if level == 1 else '### ') + text)
        L.append('')
        if text in old:
            L.append(old[text]); L.append(''); used.add(text)

    heading(1, HEAD)
    for level, text in parts:
        heading(level, text)
    for k in old:                                   # sections the living file no longer has keep their items
        if k not in used and k != DROPLETS:
            heading(2, k + ' (a section the living file no longer has)')
    heading(1, DROPLETS)
    open(path, 'w', encoding='utf-8').write('\n'.join(L).rstrip() + '\n')
    return title, sum(1 for lv, _ in parts if lv == 2)


os.makedirs(OUT, exist_ok=True)
for living in json.load(open(os.path.join(ROOT, 'files.json'))):
    stem = re.sub(r'_v\d+[A-Za-z]*\.md$', '', living)
    name = re.sub(r'^Exhibit_[A-Z-]+?_(?=[A-Z][a-z])', '', stem)
    title, n = write(living, os.path.join(OUT, name + '.md'))
    print(f'{name + ".md":52s} {n:4d} sections')
