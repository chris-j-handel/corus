"""v403cohering: each is-or-is-not? of the session v403bubble's, laid at the head of a gathering file, brought to
the section of the living sentence it names, each droplet word for word as it was laid. No word of a droplet
is changed, and no droplet enters or leaves the gathering files: a line goes from a head to its place.
All or none: with one line not found once as it was read, or one section's heading not found once, nothing is written.

Use: python3 -I incoming/v403cohering/instruments/each_laid_is_or_is_not_to_its_section.py <root> --dry    each droplet with its place, and nothing written
     python3 -I incoming/v403cohering/instruments/each_laid_is_or_is_not_to_its_section.py <root>          the same, written

What it reads. A droplet of this work: an item of a gathering file's head with *The session v403bubble's* in it.
The living sentence it names: the first words in italics after *With*, the whole name of a living file and a colon.
Its section: the heading of the living file that sentence is under, as the gathering kit's re-forming has a living
file's parts and sections, and that heading in the gathering file. A droplet goes to the end of its section, as
the gathering kit's applying places an item, each in the order the head had them.
A sentence of Exhibit ONE Natural Resolver written inside Natural Intelligence is read once, at Exhibit ONE: its
droplet goes to Exhibit ONE Natural Resolver's gathering file, at its section there.

A rule for each droplet with no one section, each the managing session v403mgr's, 16 November:
  1. A droplet with a sentence of a living file's opening, or naming a gathered droplet of the opening's part: at the
     head. The opening's part is in the opening's own order, and a droplet enters it with the opening's next version.
  2. A droplet with a sentence in two lines of its living file, or more: to the section of the first of the lines,
     in the file's own order.
  3. A droplet naming a gathered droplet and no living sentence: to the line under the first such droplet in its
     gathering file, at a head or in a section; two naming one droplet, in the order they had.
A droplet stays as it is, and is said with why, with its sentence or its gathered droplet not found, or its
section's heading not in the gathering file.

It is executed again with each droplet laid after it: a droplet at its section is not read again, and a droplet
at a head by rule 1 or rule 3 is read and is at its place already.

Applied at main after Merge #776, 16 November 2026, before the three rules: sixty droplets of this work at nine
heads, forty-eight brought, each to its section, and twelve at a head. Read before and after by an other reading:
each line of the thirty-three gathering files the same lines, each heading the same and in order, and each line
not of this work in its place and order.
Applied at main after Merge #785, 16 November 2026, with the three rules: twelve droplets of this work at three
heads. Four brought under the droplet each names, rule 3, each at a head: Natural Intelligence's gathering file 2,
Exhibit TWENTY Natural Naming's 1, Exhibit THREE Natural Numbers's 1. Eight at Natural Intelligence's head by
rule 1: six with a sentence of the opening, two of them with that sentence in a second line too, and two naming
a gathered droplet of the opening's part. Executed again: four at their place already, and nothing written.
"""
import glob, os, re, sys

R = sys.argv[1]; DRY = '--dry' in sys.argv
HEAD, OPENING, MARK = 'Head, the whole file', 'Opening', "The session v403bubble's"
GV = os.path.join(R, 'gathering-value')

def norm(s):
    s = s.replace('*', '').replace('’', "'").replace('‘', "'")
    return re.sub(r'\s+', ' ', s).strip()
def ver(p):
    m = re.search(r'_v(\d+)', p); return int(m.group(1)) if m else 0
def heading_of(l):
    return re.sub(r'^#{2,3} ', '', l).strip() if re.match(r'^#{2,3} ', l) else None

# each living file by its whole name and by its gathering file's title
LIVING = {}
for p in glob.glob(os.path.join(R, '*_v*.md')):
    stem = re.sub(r'_v\d+[A-Za-z]*\.md$', '', os.path.basename(p))
    if stem not in LIVING or ver(p) > ver(LIVING[stem]): LIVING[stem] = p
TITLE = {stem.replace('_', ' '): re.sub(r'^Exhibit_[A-Z-]+_', '', stem) for stem in LIVING}      # whole name -> gathering title
PATH = {re.sub(r'^Exhibit_[A-Z-]+_', '', stem): p for stem, p in LIVING.items()}                   # gathering title -> living path
for whole, t in list(TITLE.items()): TITLE[re.sub(r'^Exhibit [A-Z-]+ ', '', whole)] = t             # as Natural Intelligence's gathering file

def lines_with_headings(path):
    """each line of a living file, normalized, with the heading it is under as the gathering kit's re-forming has it:
    (line, heading or OPENING, inside Exhibit ONE's writing in Natural Intelligence)"""
    L = open(path, encoding='utf-8').read().split('\n')
    title_i = next(i for i, l in enumerate(L) if l.startswith('# '))
    body = next((i for i in range(title_i, len(L)) if L[i].strip() == '---'), title_i)
    one = os.path.basename(path).startswith('Exhibit_ONE_')
    has_sections = any(re.match(r'^## ', l) for l in L)
    out, fence, cur, inside = [], False, OPENING, False
    for i, l in enumerate(L):
        if i > body:
            if l.startswith('```'): fence = not fence
            elif not fence:
                if l.startswith('# '):
                    inside = l[2:].strip().startswith('EXHIBIT ONE'); cur = l[2:].strip()
                elif not inside and re.match(r'^## (.+)$', l): cur = l[3:].strip()
                elif not has_sections and i > body + 3:
                    m = re.match(r'^\*\*(\d+(?:\.\d+)+ [^*]+?)\*\*\s*$', l) or (one and re.match(r'^\*\*([^*]{3,90}?)\.?\*\*\s*$', l))
                    if m: cur = m.group(1).strip().rstrip('.')
        out.append((norm(l), cur, inside))
    return out
LINES = {t: lines_with_headings(p) for t, p in PATH.items()}

def named(l):
    """the first naming after With: (whole name, of a gathering file or not, its words in italics)"""
    m = re.search(r"With ((?:Exhibit [A-Z-]+ )?[A-Z][A-Za-z-]+(?: [A-Z][A-Za-z-]+)*)(['’]s? gathering file)?(?:, [^:*]+)?: \*", l)
    if not m: return None
    i = k = m.end()
    while k < len(l):                      # to the closing mark of the italics, bold marks inside passed over
        if l.startswith('**', k): k += 2
        elif l[k] == '*': break
        else: k += 1
    return m.group(1), bool(m.group(2)), l[i:k]

def section_in(gather_lines, heading):
    return [k for k, l in enumerate(gather_lines) if heading_of(l) == heading]

FILES = {os.path.basename(g)[:-3]: open(g, encoding='utf-8').read().split('\n') for g in sorted(glob.glob(os.path.join(GV, '*.md')))}
BEFORE = {T: list(L) for T, L in FILES.items()}
to_section, under, staying, errors = [], [], [], []
for T, L in FILES.items():
    h = section_in(L, HEAD)
    if len(h) != 1: continue
    end = next((k for k in range(h[0] + 1, len(L)) if heading_of(L[k]) is not None), len(L))
    for k in range(h[0] + 1, end):
        l = L[k]
        if not (l.startswith('- ') and MARK in l): continue
        page = re.search(r'`incoming/v403bubble/([^`]+)\.md`,(?: part [A-Z]+,)? (\d+)', l)
        what = (f'{page.group(2)} of {page.group(1)}' if page else l[:70])
        if sum(1 for x in L if x == l) != 1: errors.append(f'{T}: a line not once: {l[:80]}'); continue
        nm = named(l)
        if not nm: staying.append((T, what, 'no living sentence read after With')); continue
        whole, gathered, words = nm; q = norm(words).rstrip('.')
        t = TITLE.get(whole)
        if t is None: staying.append((T, what, f'no living file by the name {whole}')); continue
        if gathered:                                                     # rule 3, and rule 1 with the opening's part
            hits, cur = [], None
            for x in FILES[t]:
                if heading_of(x) is not None: cur = heading_of(x)
                if x.startswith('- ') and MARK not in x and q in norm(x): hits.append((x, cur))
            if not hits: staying.append((T, what, f"the gathered droplet it names is not found in {t.replace('_', ' ')}'s gathering file")); continue
            first, cur = hits[0]
            if cur == OPENING: staying.append((T, what, "at the head, rule 1: the gathered droplet it names is of the opening's part")); continue
            if sum(1 for x in FILES[t] if x == first) != 1: errors.append(f'{t}: a named droplet not once: {first[:80]}'); continue
            under.append((T, l, t, first, cur, what))
        else:
            proper = [cur for x, cur, ins in LINES[t] if q in x and not ins]
            if not proper and any(q in x and ins for x, cur, ins in LINES[t]):   # Exhibit ONE's own sentence, read once, at Exhibit ONE
                t = 'Natural_Resolver'; proper = [cur for x, cur, ins in LINES[t] if q in x]
            if not proper: staying.append((T, what, 'its sentence is not found word for word in its living file')); continue
            dest_h = proper[0]                                           # rule 2: the first of the lines, in the file's own order
            if dest_h == OPENING: staying.append((T, what, "at the head, rule 1: its sentence is of the living file's opening")); continue
            if len(section_in(FILES[t], dest_h)) != 1:
                staying.append((T, what, f"no one heading {dest_h!r} in {t.replace('_', ' ')}'s gathering file")); continue
            to_section.append((T, l, t, dest_h, what, len(proper)))

if errors:
    print('NOTHING WRITTEN, all or none:'); [print(' ', e) for e in errors]; sys.exit(1)

# each line out of its head; then to the end of its section, or under the droplet it names, in the head's order
for T, l, *_ in to_section + under: FILES[T].remove(l)
for T, l, t, dest_h, what, n in to_section:
    L = FILES[t]
    k = section_in(L, dest_h)[0]
    e = next((j for j in range(k + 1, len(L)) if heading_of(L[j]) is not None), len(L))
    while e > k + 1 and not L[e - 1].strip(): e -= 1
    L[e:e] = ([''] if e == k + 1 else []) + [l]
last = {}
for T, l, t, first, cur, what in under:
    L = FILES[t]
    k = L.index(last.get((t, first), first))
    L[k + 1:k + 1] = [l]; last[(t, first)] = l
changed = sorted(T for T in FILES if FILES[T] != BEFORE[T])
if not DRY:
    for T in changed: open(os.path.join(GV, T + '.md'), 'w', encoding='utf-8').write('\n'.join(FILES[T]))

at_place = sum(1 for T, l, t, first, cur, what in under if T == t and BEFORE[T].index(l) == FILES[T].index(l))
print(('would bring ' if DRY else 'brought ') + f'{len(to_section)} droplets to their sections and {len(under) - at_place} under the droplet each names, '
      f'in {len(changed)} gathering files; {at_place} at their place already; {len(staying)} at a head')
by = {}
for T, l, t, dest_h, what, n in to_section: by.setdefault((t, dest_h), []).append(what + ('' if T == t else f", from {T.replace('_', ' ')}'s head") + ('' if n == 1 else f', rule 2: the first of {n} lines'))
for T, l, t, first, cur, what in under: by.setdefault((t, cur), []).append(what + ('' if T == t else f", from {T.replace('_', ' ')}'s head") + ', rule 3: under ' + first[:60] + '…')
for (t, h), ws in sorted(by.items()):
    print(f"  {t.replace('_', ' ')} · {h}: {len(ws)}")
    for w in ws: print(f'      {w}')
if staying: print('  at a head:')
for T, what, why in staying: print(f"      {T.replace('_', ' ')}: {what} · {why}")
