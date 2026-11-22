#!/usr/bin/env python3
"""Each aim of the expedition by its names: the log's table, written from the aims page.

Usage: python3 -I each_aim_by_its_names.py AIMS.md NEXT_ROOT WORDS.py WINDOW.json AREAS.json > Each_aim_by_its_names.csv
       python3 -I each_aim_by_its_names.py --spine WINDOW.json > the window's names under the log, a markdown table,
                                                            the window's own names in italics, its words
  AIMS.md     the aims page, read from its "# The aims, by cluster" heading, its bands as "## " headings and
              its aims as "- **Aim.** sentence *homes*" bullets
  NEXT_ROOT   a checkout of the next version: its gathering-value/ and Exhibit THIRTY
  WORDS.py    incoming/v404mgr/instruments/words_of_no_natural_naming_in_a_page.py
  WINDOW.json window_lines_now.json: the window's names, their lines, their statuses, and the names
              a line's sentence uses
  AREAS.json  aims_areas.json: an aim's areas on its path, and what a pass re-said of its row

A row is an aim, and its areas are the sub-concepts its path crosses. The three columns sort the areas
by the window as it is now. Observing, of 7 and 15: an area a numbered line names, or a word the lines
use as given. Possibling, of 2 and 14: an area a suggestion names, or a numbered line with a rewording
or its going on offer; then the open notes, possible explorings and possible incoherings, at its homes' gathering
sections, named by place; then a note a pass laid. Discovering, of 13 and 9: an area no line and no
suggestion names, in italics, a word of the one list marked. A name the window says now with another
name is read as that name, and a {name} in a pass's words is that name's line now. The window's lines carry their reasons by
the lines before them, back to line 1; --spine prints them. The table sizes a chain and decides nothing.
"""
import csv, glob, json, os, re, sys


def spine(window):
    w = json.load(open(window, encoding='utf-8'))
    names = w['names']

    def num(v):
        m = re.match(r'(\d+)', v['line'])
        return int(m.group(1)) if m else 999

    rows = [(k, v) for k, v in names.items() if 'see' not in v and v['status'] != 'given']
    rows.sort(key=lambda kv: (kv[1]['status'] == 'suggested' and 'below' in kv[1]['line'],
                              'below' in kv[1]['line'], num(kv[1])))
    out = ['| Line | Name | Said with |', '| --- | --- | --- |']
    for k, v in rows:
        under = ', '.join(f"*{u}, given*" if names[u]['status'] == 'given' else
                          f"*{u} {names[u]['line'].split(' ')[0]}*" if re.match(r'\d', names[u]['line']) else
                          f"*{u} below the lines*" for u in v['under'])
        if not under:
            under = 'the origin' if k == 'now' else 'given words only'
        line = v['line']
        if v['status'] == 'suggested':
            line += ', suggested' if 'below' not in line else ''
            if v.get('offer'):
                line += f", {v['offer']} on offer"
        out.append(f'| {line} | *{k}* | {under} |')
    given = [k for k, v in names.items() if v.get('status') == 'given']
    for k, v in names.items():
        if 'see' in v:
            out.append('')
            out.append(f"{k[0].upper() + k[1:]} is said now as {v['see']}, at {names[v['see']]['line']}.")
    out.append('')
    out.append(', '.join(given[:-1]).capitalize() + ' and ' + given[-1] +
               ' are words the lines use and no line names: given words.')
    return '\n'.join(out)


if sys.argv[1] == '--spine':
    print(spine(sys.argv[2]))
    sys.exit(0)

aims_md, root, wordsmod, window, areas_json = sys.argv[1:6]
import importlib.util
_spec = importlib.util.spec_from_file_location('w', wordsmod)
_w = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_w)
LISTED = [re.compile(p, re.I) for _, p in _w.WORDS]


def mark(k):
    return k + ' (of the one list)' if any(rx.search(k) for rx in LISTED) else k


W = json.load(open(window, encoding='utf-8'))['names']
AREAS = json.load(open(areas_json, encoding='utf-8'))


def win(a):
    v = W.get(a)
    if v and 'see' in v:
        return v['see'], W[v['see']]
    return a, v


def fill(text):
    """A {name} in a pass's words is the window's line for that name now."""
    def line(m):
        v = win(m.group(1))[1]
        return v['line'].split(' ')[0] if v else 'no line now'
    return re.sub(r'\{([^{}]+)\}', line, text)

# The gathering files and their sections' open notes.
gdir = os.path.join(root, 'gathering-value')
gath = {}
for p in glob.glob(os.path.join(gdir, '*.md')):
    title = os.path.basename(p)[:-3].replace('_', ' ')
    secs, cur = {}, 'Head'
    for l in open(p, encoding='utf-8'):
        m = re.match(r'^#{2,3} (.+)', l)
        if m:
            cur = m.group(1).strip()
            secs.setdefault(cur, 0)
            continue
        if re.match(r'^- \*\*(Possible exploring|Possible incohering)\*\*', l):
            secs[cur] = secs.get(cur, 0) + 1
    gath[title] = secs

thirty = sorted(glob.glob(os.path.join(root, 'Exhibit_THIRTY_*_v*.md')))[-1]
step_group, g = {}, None
for l in open(thirty, encoding='utf-8'):
    m = re.match(r'^## (\d+) ', l)
    if m:
        g = m.group(1)
    m = re.match(r'^(\d+)\. ', l)
    if m and g:
        step_group[int(m.group(1))] = g

THIS = 'Natural Intelligence Living Expedition Destinies'
TITLES = sorted(gath, key=len, reverse=True)


def section_count(title, sec):
    secs = gath.get(title, {})
    hit = [h for h in secs if h == sec or h.startswith(sec + ' ')]
    return sum(secs[h] for h in hit)


def possessive(t):
    return t + ("'" if t.endswith('s') else "'s")


def nums(s):
    out = []
    for a, b in re.findall(r'(\d+)\s+to\s+(\d+)', s):
        out += list(range(int(a), int(b) + 1))
    out += [int(x) for x in re.findall(r'\d+', re.sub(r'(\d+)\s+to\s+(\d+)', ' ', s))]
    return out


def notes(homes):
    found, at_home, parts = [], 0, 0
    for part in re.split(r';', homes):
        part = part.strip()
        if not part:
            continue
        parts += 1
        if re.search(r",? and its gathering", part):
            at_home = -1
            part = re.split(r",? and its gathering", part)[0]
        elif 'gathering' in part:
            at_home = at_home + 1 if at_home >= 0 else at_home
            continue
        if part.startswith('Exhibit THIRTY, the whole'):
            found.append(("Exhibit THIRTY's gathering", ''))
            continue
        m = re.match(r'Exhibit THIRTY, (steps?|groups?) (.+)', part)
        if m:
            groups = sorted({str(n) for n in nums(m.group(2))} if m.group(1).startswith('group') else
                            {step_group.get(n) for n in nums(m.group(2).split(' and group')[0]) if step_group.get(n)},
                            key=int)
            if 'group' in m.group(2) and m.group(1).startswith('step'):
                groups = sorted(set(groups) | {str(n) for n in nums(m.group(2).split('group')[1])}, key=int)
            for gr in groups:
                if section_count('Co-Chaining Logic Registry', gr):
                    found.append(("Exhibit THIRTY's gathering", f"group {gr}"))
            continue
        m = re.match(r'[Tt]his exhibit, (\d+)', part)
        if m:
            if section_count(THIS, m.group(1)):
                found.append(("this exhibit's gathering", m.group(1)))
            continue
        for t in TITLES:
            if part.startswith(t + "'s opening") or part.startswith(t + ', opening'):
                if section_count(t, 'Opening'):
                    found.append((f"{possessive(t)} gathering", 'its opening'))
                break
            if part.startswith(t + ', ') and not re.search(r'\d', part):
                core = re.sub(r"^(the|a|an) ", '', part[len(t) + 2:].lower()).split(' ')[0]
                core = re.sub(r"'s$", '', core)
                hit = [h for h in gath.get(t, {}) if core and core in h.lower()]
                if hit and gath[t][hit[0]]:
                    found.append((f"{possessive(t)} gathering", hit[0].split(' — ')[0].lower()))
                break
            if part.startswith(t + ' '):
                rest = part[len(t):]
                ks = []
                for a, x, y in re.findall(r'(\d+)\.(\d+) to (?:\d+)\.(\d+)', rest):
                    ks += [f'{a}.{i}' for i in range(int(x), int(y) + 1)]
                ks += re.findall(r'\d+\.\d+', re.sub(r'\d+\.\d+ to \d+\.\d+', ' ', rest))
                for sec in dict.fromkeys(ks):
                    if section_count(t, sec):
                        found.append((f"{possessive(t)} gathering", sec))
                break
    return list(dict.fromkeys(found)), ('all' if at_home == parts else 'some' if at_home else '')


def cell_observing(areas):
    out = []
    for a in areas:
        t, v = win(a)
        if not v or v['status'] == 'suggested':
            continue
        n = int(re.match(r'\d+', v['line']).group(0))
        if t != a:
            out.append((n, f"{a}, as {t} {v['line']}"))
        elif v['status'] == 'line':
            out.append((n, f"{a} {v['line']}"))
        elif v['status'] == 'given':
            out.append((n, f"{a}, given at {v['line']}"))
        else:
            out.append((n, f"{a}, {v['line']}"))
    return '; '.join(t for _, t in sorted(out, key=lambda x: x[0]))


def cell_possibling(areas, homes, note):
    sug = []
    for a in areas:
        t, v = win(a)
        if not v or v['status'] != 'suggested':
            continue
        if t != a:
            a = f"{a}, as {t}"
        if re.fullmatch(r'\d+', v['line']) and v.get('offer'):
            sug.append(f"{a} {v['line']}, {v['offer']} on offer")
        elif re.fullmatch(r'\d+', v['line']):
            sug.append(f"{a}, suggested at {v['line']}")
        elif v['line'] == 'below the lines':
            sug.append(f"{a}, a suggestion below the lines")
        else:
            sug.append(f"{a}, {v['line']}" + (f", {v['offer']} on offer" if v.get('offer') else ''))
    parts = []
    if sug:
        s = '; '.join(sug)
        parts.append(s[0].upper() + s[1:] + '.')
    found, at_home = notes(homes)
    if at_home == 'all':
        parts.append('Its home is a gathering note.')
    elif at_home:
        parts.append('A gathering note is among its homes.')
    if found:
        byfile = {}
        for f, sec in found:
            byfile.setdefault(f, []).append(sec)
        said = []
        for f, secs in byfile.items():
            secs = [x for x in secs if x]
            if len(secs) > 1 and all(x.startswith('group ') for x in secs):
                secs = ['groups ' + secs[0][6:]] + [x[6:] for x in secs[1:]]
            said.append(f + (', ' + (', '.join(secs[:-1]) + ' and ' + secs[-1] if len(secs) > 1 else secs[0]) if secs else ''))
        parts.append('Open notes at ' + '; '.join(said) + '.')
    if note:
        parts.append(note)
    return ' '.join(parts)


def cell_discovering(areas):
    return ', '.join(f'*{mark(a)}*' for a in areas if a not in W)


rows, band, missing = [], None, []
_lines = open(aims_md, encoding='utf-8').read().split('\n')
_start = next((i for i, l in enumerate(_lines) if l.startswith('# The aims, by cluster')), -1)
for l in _lines[_start + 1:]:
    m = re.match(r'^## (.+)', l)
    if m:
        band = m.group(1).strip()
        continue
    m = re.match(r'^- \*\*(.+?)\*\*\s*(.*?)\s*(?:\*([^*]+)\*)?\s*$', l.strip())
    if m and band:
        aim, words, homes = m.group(1).rstrip('.,: '), m.group(2), m.group(3) or ''
        c = AREAS.get(aim)
        if not c:
            missing.append(aim)
            continue
        aim = c.get('aim_said', aim)
        words = fill(c.get('sentence', words))
        homes = fill(c.get('homes', homes))
        areas = c['areas']
        obs = cell_observing(areas)
        rows.append([band, aim, words, ', '.join(areas), homes,
                     (obs[0].upper() + obs[1:] + '.') if obs else '—',
                     cell_possibling(areas, homes, fill(c.get('note', ''))) or '—',
                     cell_discovering(areas) or '—'])
if missing:
    sys.exit('aims with no areas: ' + '; '.join(missing))

w = csv.writer(sys.stdout)
w.writerow(['band', 'destiny', 'its sentence', 'areas on its path', 'home',
            'observing, 7 and 15', 'possibling, 2 and 14', 'discovering, 13 and 9'])
w.writerows(rows)
