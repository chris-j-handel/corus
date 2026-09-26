"""Checks at the living files: each contents entry against a body heading, tables' cell counts, the version line,
Exhibit ONE inside Natural Intelligence, the code block running, and the family words outside quotation (reported, not failed).
The newest version of each living file in the folder is taken. A check is a coupling partner and no authority:
it says its result at its check and nothing past it.
Usage: python3 check_set.py <folder holding the living files>      (the repository root, as a rule)"""
import re, os, sys, glob

D = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
STEMS = ['Natural_Intelligence', 'Exhibit_ONE_Natural_Resolver', 'Exhibit_TWO_Natural_Networking', 'Exhibit_THREE_Natural_Numbers',
         'Exhibit_FOUR_Natural_Mathematics', 'Exhibit_TWELVE_Natural_Explaining', 'Exhibit_TWENTY_Natural_Naming',
         'Exhibit_TWENTY-FOUR_Geodesic_Improving_Method', 'Exhibit_TWENTY-EIGHT_Equilibria_Registry', 'Exhibit_THIRTY_Co-Chaining_Logic_Registry']

def newest(stem):
    files = glob.glob(os.path.join(D, stem + '_v*.md'))
    return max(files, key=lambda f: int(re.search(r'_v(\d+)', f).group(1))) if files else None

ok = True
def say(cond, msg):
    global ok
    if not cond: ok = False; print('  FAIL', msg)

FILES = {s: newest(s) for s in STEMS}
for stem, path in FILES.items():
    if not path: print(stem, '  (absent)'); continue
    fn = os.path.basename(path); t = open(path, encoding='utf-8').read(); L = t.split('\n')
    ver = re.search(r'_v(\d+[a-z]*)\.md$', fn).group(1)
    print(fn)
    say(L[0].endswith('v' + ver), 'the version line does not end at the file\'s version: ' + L[0])
    # contents vs headings
    try: sep = next(i for i, l in enumerate(L) if l.strip() == '---')
    except StopIteration: say(False, 'no --- after the contents'); continue
    fence = False; heads = []
    for l in L[sep + 1:]:
        if l.startswith('```'): fence = not fence; continue
        if fence: continue
        m = re.match(r'^(#{2,3}) (.*)$', l)
        if m: heads.append(m.group(2).strip())
    entries = []
    title = next(i for i, l in enumerate(L) if l.startswith('# '))
    for l in L[title + 1:sep]:
        s = l.strip()
        if not s or s == '&nbsp;' or s.startswith('#') or (s.startswith('**') and s.endswith('**')): continue
        if s.startswith('*') and s.endswith('*'): continue
        if s.startswith('- '): s = s[2:]
        if len(s) > 160: continue
        entries += [x.strip() for x in s.split(' · ')] if not re.match(r'^\d', s) else [s]
    ws = lambda s: re.sub(r'\s+', ' ', s).strip()
    hk = [ws(re.sub(r' — binary$', '', h)) for h in heads]
    bolds = [ws(m.group(1)) for l in L[sep + 1:] for m in [re.match(r'^\*\*(.+?)\*\*', l)] if m]     # a paragraph's bold opener
    entries = [ws(e) for e in entries]
    miss = [e for e in entries if e not in hk and not any(h.startswith(e) for h in hk) and not any(b.rstrip('.') == e or b.startswith(e) for b in bolds)]
    numbered = [e for e in miss if re.match(r'^\d+(\.\d+)+ ', e)]
    say(not numbered, 'numbered contents entries with no heading: %s' % numbered[:5])
    if [e for e in miss if e not in numbered]: print('  note: contents lines with no heading and no bold opener:', [e for e in miss if e not in numbered][:3])
    # tables
    fence = False; i = 0
    while i < len(L):
        if L[i].startswith('```'): fence = not fence
        if not fence and L[i].startswith('|'):
            j = i
            while j < len(L) and L[j].startswith('|'): j += 1
            cells = lambda l: re.sub(r'`[^`]*`', '', l).replace('\\|', '').count('|')
            n0 = cells(L[i]); bad = [k + 1 for k in range(i, j) if cells(L[k]) != n0]
            say(not bad, 'table rows with a differing cell count at lines %s' % bad[:5])
            i = j; continue
        i += 1
    # the family words outside italics, code and quotation (a report)
    fam = re.compile(r'\b(what|whatever|how|however|somehow|where|wherever|nowhere|somewhere|elsewhere|anywhere|everywhere)\b', re.I)
    fence = False; hits = []
    for n, l in enumerate(L, 1):
        if l.startswith('```'): fence = not fence; continue
        if fence or l.startswith('    '): continue
        s = re.sub(r'\*[^*]+\*', '', l); s = re.sub(r'`[^`]+`', '', s); s = re.sub(r'"[^"]*"', '', s)
        if fam.search(s): hits.append(n)
    if hits: print('  family words at lines', hits[:12])

# Exhibit ONE inside Natural Intelligence, and the code running
if FILES['Natural_Intelligence'] and FILES['Exhibit_ONE_Natural_Resolver']:
    ni = open(FILES['Natural_Intelligence'], encoding='utf-8').read(); one = open(FILES['Exhibit_ONE_Natural_Resolver'], encoding='utf-8').read()
    HEAD = '# EXHIBIT ONE · NATURAL RESOLVER\n\n**Geodesic Discovering Logical Method and Form**\n\n'
    body = one.split('\n---\n', 1)[1].strip()
    inside = re.sub(r'(\s*(---|&nbsp;)\s*)+$', '', ni.split(HEAD, 1)[1].split('\n# PART FIVE')[0].strip())
    say(inside == body, 'Exhibit ONE inside Natural Intelligence differs from the standalone')
    code = body.split('```python', 1)[1].split('```', 1)[0]; ns = {}; exec(code, ns)
    say(next(v for k, v in ns.items() if k.startswith('_1_') and callable(v))([], [('k', 1)]) == ([('k', 1)], [('k', 1)]), 'the code does not run')
    fns = [n for n, v in ns.items() if callable(v) and not n.startswith('__')]
    print('  functions at the code:', fns)
print('ALL PASS' if ok else 'SOME FAIL')
