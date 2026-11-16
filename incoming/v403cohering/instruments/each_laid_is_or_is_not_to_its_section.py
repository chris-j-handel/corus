"""v403cohering: each is-or-is-not? of the session v403bubble's, laid at the head of a gathering file, brought to
the section of the living sentence it names, each droplet word for word as it was laid. No word of a droplet
is changed, and no droplet enters or leaves the gathering files: a line goes from a head to a section.
All or none: with one line not found once as it was read, or one section's heading not found once, nothing is written.

Use: python3 -I incoming/v403cohering/instruments/each_laid_is_or_is_not_to_its_section.py <root> --dry    each droplet with its section, and nothing written
     python3 -I incoming/v403cohering/instruments/each_laid_is_or_is_not_to_its_section.py <root>          the same, written

What it reads. A droplet of this work: an item of a gathering file's head with *The session v403bubble's* in it.
The living sentence it names: the first words in italics after *With*, the whole name of a living file and a colon.
Its section: the heading of the living file that sentence is under, as the gathering kit's re-forming has a living
file's parts and sections, and that heading in the gathering file. A droplet goes to the end of its section, as
the gathering kit's applying places an item, each in the order the head had them.

A droplet stays at its head, and is said with why, with each of these:
  its sentence is in the living file's opening, before its first part: the opening's part is in the opening's
    own order, read by the managing session's instruments
  its sentence is not found word for word, or is found in more than one line of the living file
  it names a gathered droplet and no living sentence, and that droplet is at the head too, is in the opening's
    part, or is not found once
  its section's heading is not in the gathering file
A sentence of Exhibit ONE Natural Resolver written inside Natural Intelligence is read once, at Exhibit ONE: its
droplet goes to Exhibit ONE Natural Resolver's gathering file, at its section there.

It can be executed again with each droplet laid after it: a droplet at its section is not read again.

Applied at main after Merge #776, 16 November 2026: sixty droplets of this work at nine heads. Forty-eight brought,
each to its section: Natural Intelligence's gathering file 23, Exhibit FOUR Natural Mathematics's 6, Exhibit TWENTY
Natural Naming's 4, Exhibit ONE Natural Resolver's 4, one of the four from Natural Intelligence's head, Exhibit
SIXTEEN Natural Chemistry's 3, Exhibit EIGHTEEN Natural Physics's 3, Exhibit THREE Natural Numbers's 2, Exhibit
SEVEN Natural Societies's 2 and Exhibit EIGHT Natural Exploring's 1. Twelve staying: five of the opening, four by
a sentence in it and one by a gathered droplet of its part; two with a sentence in two lines of its living file;
two with a gathered droplet found more than once; three with a gathered droplet at the head too.
Read before and after by an other reading: each line of the thirty-three gathering files the same lines, each
heading the same and in order, and each line not of this work in its place and order.
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
    i, k = m.end(), m.end()
    while k < len(l):                      # to the closing mark of the italics, bold marks inside passed over
        if l.startswith('**', k): k += 2
        elif l[k] == '*': break
        else: k += 1
    return m.group(1), bool(m.group(2)), l[i:k]

def section_in(gather_lines, heading):
    return [k for k, l in enumerate(gather_lines) if re.match(r'^#{2,3} ', l) and re.sub(r'^#{2,3} ', '', l).strip() == heading]

FILES = {os.path.basename(g)[:-3]: open(g, encoding='utf-8').read().split('\n') for g in sorted(glob.glob(os.path.join(GV, '*.md')))}
going, staying, errors = [], [], []
for T, L in FILES.items():
    h = section_in(L, HEAD)
    if len(h) != 1: continue
    end = next((k for k in range(h[0] + 1, len(L)) if re.match(r'^#{2,3} ', L[k])), len(L))
    for k in range(h[0] + 1, end):
        l = L[k]
        if not (l.startswith('- ') and MARK in l): continue
        page = re.search(r'`incoming/v403bubble/([^`]+)\.md`,(?: part [A-Z]+,)? (\d+)', l)
        what = (f'{page.group(2)} of {page.group(1)}' if page else l[:70])
        nm = named(l)
        if not nm: staying.append((T, what, 'no living sentence read after With')); continue
        whole, gathered, words = nm; q = norm(words).rstrip('.')
        t = TITLE.get(whole)
        if t is None: staying.append((T, what, f'no living file by the name {whole}')); continue
        if gathered:
            hits, cur = [], None
            for x in FILES[t]:
                if re.match(r'^#{2,3} ', x): cur = re.sub(r'^#{2,3} ', '', x).strip()
                if x.startswith('- ') and MARK not in x and q in norm(x): hits.append(cur)
            if len(hits) != 1: staying.append((T, what, f"the gathered droplet it names is found {len(hits)} times in {t.replace('_', ' ')}'s gathering file")); continue
            if hits[0] == HEAD and t == T: staying.append((T, what, 'the gathered droplet it names is at the head too')); continue
            if hits[0] == OPENING: staying.append((T, what, "the gathered droplet it names is in the opening's part")); continue
            dest_t, dest_h = t, hits[0]
        else:
            proper = [(cur, ins) for x, cur, ins in LINES[t] if q in x and not ins]
            inside = [1 for x, cur, ins in LINES[t] if q in x and ins]
            if not proper and inside:          # Exhibit ONE's own sentence, read once, at Exhibit ONE
                t = 'Natural_Resolver'; proper = [(cur, ins) for x, cur, ins in LINES[t] if q in x]
            if len(proper) != 1: staying.append((T, what, f'its sentence is found in {len(proper)} lines of its living file')); continue
            dest_t, dest_h = t, proper[0][0]
            if dest_h == OPENING: staying.append((T, what, "its sentence is in the living file's opening")); continue
        if len(section_in(FILES[dest_t], dest_h)) != 1:
            staying.append((T, what, f"no one heading {dest_h!r} in {dest_t.replace('_', ' ')}'s gathering file")); continue
        if sum(1 for x in L if x == l) != 1: errors.append(f'{T}: a line not once: {l[:80]}'); continue
        going.append((T, l, dest_t, dest_h, what))

if errors:
    print('NOTHING WRITTEN, all or none:'); [print(' ', e) for e in errors]; sys.exit(1)

# written: each line out of its head, and to the end of its section, in the head's order
for T, l, dest_t, dest_h, what in going:
    FILES[T].remove(l)
for T, l, dest_t, dest_h, what in going:
    L = FILES[dest_t]
    n = section_in(L, dest_h)[0]
    e = next((k for k in range(n + 1, len(L)) if re.match(r'^#{2,3} ', L[k])), len(L))
    while e > n + 1 and not L[e - 1].strip(): e -= 1
    L[e:e] = ([''] if e == n + 1 else []) + [l]
changed = sorted({T for T, *_ in going} | {d for _, _, d, _, _ in going})
if not DRY:
    for T in changed: open(os.path.join(GV, T + '.md'), 'w', encoding='utf-8').write('\n'.join(FILES[T]))

print(('would bring ' if DRY else 'brought ') + f'{len(going)} droplets to their sections, in {len(changed)} gathering files; {len(staying)} staying at a head')
by = {}
for T, l, dest_t, dest_h, what in going: by.setdefault((dest_t, dest_h), []).append((what, T))
for (dest_t, dest_h), ws in sorted(by.items()):
    print(f"  {dest_t.replace('_', ' ')} · {dest_h}: {len(ws)}")
    for what, T in ws: print(f'      {what}' + ('' if T == dest_t else f", from {T.replace('_', ' ')}'s head"))
if staying: print('  staying:')
for T, what, why in staying: print(f"      {T.replace('_', ' ')}: {what} · {why}")
