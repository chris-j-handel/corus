"""Each droplet of one gathering file with a session's name in its plain words, by its kind, and with a droplet
opening with the story of a returning, the droplet re-said with its value, a candidate. For Exhibit TWENTY-SIX
Living File Registry's *No self's name, session or time goes beside a value, a value being its concept said
plainly*. Reads one gathering file, and each instrument of the set's folders; executes; decides nothing; writes
no living file and no gathering file.

Use: python3 -I incoming/v404helping/instruments/each_droplet_with_a_sessions_name.py <root> <a gathering file's title>          each droplet said by its kind, and nothing written
     python3 -I incoming/v404helping/instruments/each_droplet_with_a_sessions_name.py <root> <a gathering file's title> write    its candidates written, incoming/v404helping/Each_droplet_re-said_with_no_story_<title>.json

What it reads. A droplet is a line opening with a hyphen. A session's name is the letter v, small or capital,
with three numerals and its letters after them, as v403bubble, v401atom and v391: in a droplet's plain words,
outside code marks. A name within code marks is of a path, an address, and is passed over.
A kind, the first of these a droplet has, each all or none at all by its own words:
  a returning's story:    opening, after its kind's label, with *The session*, a name, *'s*, an order or none, and
                          *returning*, its page in code marks, *part* with its name or none, a number or none, *with its instrument* and a path
                          in code marks or none, and *executed by a second hand, each check is* or none, to a stop
  a version and a line:   closing with *from Exhibit ONE*, a name, *line* and a number, in its closing label
  a working's sequence:   *the working*, a name, *'s sequence*
  executed by a working:  *executed by the working*, a name
  gathered by a session:  *gathered by the session*, a name
  a session's layings:    a name, *'s laying* or *'s layings*, *since the reading before*
  carried or laid by a session:  *carried whole*, *laid* or *placed here*, *by the managing session*, a name
  an other form:          a name with none of these
A candidate is with a returning's story alone: the story away to its stop, each other word as it is, and the
instrument's path, with one, in code marks before the droplet's closing quotation or closing the droplet, with
the path not in the droplet's other words already. A candidate with a session's name in its plain words still
is said, and is no candidate written. The candidates written are the gathering kit's own form, for its
`replace_lines.py`: the gathering file, the droplet as it is, and the droplet re-said.
An instrument reading or writing a droplet by a session's name is said by its lines: a line of a file of
`incoming/` or `kits/`, outside its opening lines, with the word *session* and a session's name after it.
Returned at main, 16 November 2026, after Merge #850, with Natural Intelligence's gathering file: 2,066
droplets, 198 with a session's name in its plain words. By kind: a returning's story forty-two; a version and a
line eighty-two; a working's sequence nine; executed by a working four; carried or laid by a session one; an
other form sixty. Thirty-nine candidates, each with no session's name in its plain words, and three re-said
with a name still. With each gathering file, its candidates: Natural Intelligence thirty-nine, Exhibit FOUR
Natural Mathematics eight, Exhibit ONE Natural Resolver and Exhibit TWENTY Natural Naming seven each, Exhibit
SIXTEEN Natural Chemistry six, Exhibit EIGHTEEN Natural Physics five, and Exhibit THREE Natural Numbers,
Exhibit SEVEN Natural Societies and Exhibit EIGHT Natural Exploring two each.
The thirty-nine entered by the gathering kit in a scratch folder, the scratch folder away after it: thirty-nine
lines re-said and each other line the same, each heading the same; each word of a line re-said as it was but
its story's; `check_set.py` ALL PASS; the gathering check and `each_droplet_said_more_than_once.py` each the
same answer after as before. Two instruments have an other answer after: `each_is_or_is_not_open.py`, its
naming of thirty-nine askings *none* and thirty-nine lines of its table not now; and
`each_laid_is_or_is_not_to_its_section.py`, reading a story's mark, its page and its number.
"""
import glob, json, os, re, sys

R, TITLE = sys.argv[1], sys.argv[2]; WRITE = len(sys.argv) > 3 and sys.argv[3] == 'write'
G = os.path.join('gathering-value', TITLE + '.md')
L = open(os.path.join(R, G), encoding='utf-8').read().split('\n')
NAME = re.compile(r'(?<![\w/`.-])[vV]\d{3}[A-Za-z]*\b')
plain = lambda l: re.sub(r'`[^`]*`', lambda m: ' ' * len(m.group(0)), l)
ORD = r'(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|twenty-first|twenty-second|twenty-third)'
STORY = re.compile(r"^(- \*\*[^*]+\*\* · )The session [vV]\d{3}[A-Za-z]*'s (?:" + ORD + r" )?returning, `[^`]+`(?:, part [A-Z]+)?(?:, \d+)?(?:, with its instrument `([^`]+)`)?(?:, executed by a second hand, each check is)?\. ")
KINDS = [("a returning's story", STORY),
         ('a version and a line', re.compile(r'from Exhibit ONE [vV]\d{3}[A-Za-z]*, line \d+\)\*\s*$')),
         ("a working's sequence", re.compile(r"the working [vV]\d{3}[A-Za-z]*'s sequence")),
         ('executed by a working', re.compile(r'executed by the working [vV]\d{3}[A-Za-z]*')),
         ('gathered by a session', re.compile(r'gathered by the session [vV]\d{3}[A-Za-z]*')),
         ("a session's layings", re.compile(r"[vV]\d{3}[A-Za-z]*'s layings? (?:and notes )?since the reading before")),
         ('carried or laid by a session', re.compile(r'(?:carried whole|laid|placed here) by the managing session [vV]\d{3}'))]

droplets = with_name = 0; by_kind = {}; names = {}; candidates = []; still = []; head = ''
for k, l in enumerate(L):
    if re.match(r'^#{2,3} ', l): head = re.sub(r'^#{2,3} ', '', l).strip()
    if not l.startswith('- '): continue
    droplets += 1
    found = NAME.findall(plain(l))
    if not found: continue
    with_name += 1
    for n in found: names[n] = names.get(n, 0) + 1
    kind = next((name for name, rx in KINDS if rx.search(l)), 'an other form')
    by_kind.setdefault(kind, []).append((k, head, l))
    if kind == "a returning's story":
        m = STORY.match(l); rest = l[m.end():]; instrument = m.group(2)
        if instrument and instrument not in rest:
            q = re.search(r' — at "[^"]*"\s*$', rest)
            rest = (rest[:q.start()].rstrip() + f' `{instrument}`.' + rest[q.start():]) if q else rest.rstrip() + f' `{instrument}`.'
        new = m.group(1) + rest
        (still if NAME.search(plain(new)) else candidates).append((k, head, l, new))

print(f"{TITLE.replace('_', ' ')}'s gathering file: {droplets} droplets; {with_name} with a session's name in its plain words")
print('   by name: ' + ', '.join(f'{n} {c}' for n, c in sorted(names.items(), key=lambda x: (-x[1], x[0]))))
for kind, _ in KINDS + [('an other form', None)]:
    v = by_kind.get(kind, [])
    if v: print(f'   {len(v):4d}  {kind}: as line {v[0][0] + 1}, under *{v[0][1][:40]}*: {v[0][2][:120]}')
print(f"a returning's story: {len(candidates)} candidates, each with no session's name in its plain words; {len(still)} re-said with a name still in its plain words, and no candidate")
for k, head, l, new in candidates[:2]:
    print(f'   as it is, line {k + 1}: {l[:230]}\n   re-said:          {new[:230]}')
for k, head, l, new in still[:3]:
    print(f"   a name still, line {k + 1}: …{plain(new)[max(0, NAME.search(plain(new)).start() - 70):NAME.search(plain(new)).end() + 40]}…")

print("each line of an instrument of the set's folders with the word session and a session's name, reading or writing a droplet by it:")
for p in sorted(glob.glob(os.path.join(R, 'incoming', '*', '**', '*.py'), recursive=True) + glob.glob(os.path.join(R, 'incoming', '*', '**', '*.sh'), recursive=True) + glob.glob(os.path.join(R, 'kits', '**', '*.py'), recursive=True)):
    if os.path.abspath(p) == os.path.abspath(__file__): continue
    doc = False; found = []
    for i, line in enumerate(open(p, encoding='utf-8').read().split('\n')):
        if line.count('"""') == 1: doc = not doc; continue
        if doc or line.lstrip().startswith('#'): continue
        if re.search(r'[Ss]ession [vV]\d{3}', line): found.append(i + 1)
    if found: print(f'   {os.path.relpath(p, R)}, lines {found}')
if WRITE:
    out = os.path.join(R, 'incoming', 'v404helping', f'Each_droplet_re-said_with_no_story_{TITLE}.json')
    json.dump([{'file': G, 'old': l, 'new': new} for _, _, l, new in candidates], open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'written: {os.path.relpath(out, R)}, {len(candidates)} candidates')
else:
    print('nothing written')
