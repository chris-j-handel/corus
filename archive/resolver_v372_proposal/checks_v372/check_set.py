"""Checks at the v372 living set: contents against headings, tables' cell counts, ONE inside NI, version lines,
the family words outside quotation, and the code block running.
Usage: python3 check_set.py <folder holding the living files>"""
import re, os, sys
D = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()      # the folder holding the living files of v372
FILES = ["Natural_Intelligence_v372.md", "Exhibit_ONE_Natural_Resolver_v372.md", "Exhibit_TWO_Natural_Networking_v372.md",
         "Exhibit_THREE_Natural_Numbers_v372.md", "Exhibit_FOUR_Natural_Mathematics_v372.md", "Exhibit_TWELVE_Natural_Explaining_v372.md",
         "Exhibit_TWENTY_Natural_Naming_v372.md", "Exhibit_TWENTY-FOUR_Geodesic_Improving_Method_v372.md",
         "Exhibit_TWENTY-EIGHT_Equilibria_Registry_v372.md", "Exhibit_THIRTY_Co-Chaining_Logic_Registry_v372.md"]
ok = True
def say(cond, msg):
    global ok
    if not cond: ok = False; print('  FAIL', msg)

for fn in FILES:
    t = open(os.path.join(D, fn), encoding='utf-8').read(); L = t.split('\n')
    print(fn)
    say(L[0].endswith('v372'), 'version line ' + L[0])
    stale = [i + 1 for i, l in enumerate(L) if re.search(r'v37[01]\b', l) and not re.search(r'(exact|closes|Closed|stands) at v37[01]', l)]
    say(not stale, 'an old version string remains at lines %s' % stale[:5])
    # contents vs headings (numbered sections and named subsections)
    sep = next(i for i, l in enumerate(L) if l.strip() == '---')
    fence = False; heads = []
    for l in L[sep + 1:]:
        if l.startswith('```'): fence = not fence; continue
        if fence: continue
        m = re.match(r'^(#{2,3}) (.*)$', l)
        if m: heads.append(m.group(2).strip())
    entries, notes = [], []
    title = next(i for i, l in enumerate(L) if l.startswith('# '))
    for l in L[title + 1:sep]:
        s = l.strip()
        if not s or s == '&nbsp;' or s.startswith('#') or (s.startswith('**') and s.endswith('**')): continue
        if s.startswith('*') and s.endswith('*'): continue
        if s.startswith('- '): continue
        if len(s) > 160: continue                      # a front paragraph, not a contents line
        entries += [x.strip() for x in s.split(' · ')] if not re.match(r'^\d', s) else [s]
    hk = [re.sub(r' — binary$', '', h) for h in heads]
    ek = [re.sub(r'^\d+ · ', '', e) for e in entries]
    miss = [e for e in ek if e not in hk]
    say(not [e for e in miss if re.match(r'^\d', e)], 'numbered contents entries with no heading: %s' % miss[:5])
    if [e for e in miss if not re.match(r'^\d', e)]: print('  note: contents lines with no heading:', [e for e in miss if not re.match(r'^\d', e)][:3])
    # tables
    fence = False
    i = 0
    while i < len(L):
        if L[i].startswith('```'): fence = not fence
        if not fence and L[i].startswith('|'):
            j = i
            while j < len(L) and L[j].startswith('|'): j += 1
            cells = lambda l: re.sub(r'`[^`]*`', '', l).replace('\\|', '').count('|')
            n0 = cells(L[i])
            bad = [k + 1 for k in range(i, j) if cells(L[k]) != n0]
            say(not bad, 'table rows with a differing cell count at lines %s' % bad[:5])
            i = j; continue
        i += 1
    # family words outside italics, code and backticks, at the changed prose only (a report, not a fail)
    fam = re.compile(r'\b(what|whatever|how|however|somehow|where|wherever|nowhere|somewhere|elsewhere|anywhere|everywhere)\b', re.I)
    fence = False; hits = []
    for n, l in enumerate(L, 1):
        if l.startswith('```'): fence = not fence; continue
        if fence or l.startswith('    '): continue
        s = re.sub(r'\*[^*]+\*', '', l); s = re.sub(r'`[^`]+`', '', s); s = re.sub(r'"[^"]*"', '', s)
        if fam.search(s): hits.append(n)
    if hits: print('  family words at lines', hits[:12])

# ONE inside NI
ni = open(os.path.join(D, FILES[0]), encoding='utf-8').read(); one = open(os.path.join(D, FILES[1]), encoding='utf-8').read()
HEAD = '# EXHIBIT ONE · NATURAL RESOLVER\n\n**Geodesic Discovering Logical Method and Form**\n\n'
body = one.split('---\n\n&nbsp;\n\n', 1)[1].strip()
inside = re.sub(r'(\s*(---|&nbsp;)\s*)+$', '', ni.split(HEAD, 1)[1].split('\n# PART FIVE')[0].strip())
say(inside == body, 'Exhibit ONE inside Natural Intelligence differs from the standalone')
code = body.split('```python', 1)[1].split('```', 1)[0]; ns = {}; exec(code, ns)
say(ns['_1_self_coupling']([], [('k', 1)]) == ([('k', 1)], [('k', 1, -1, 0)]), 'the code does not run')
say('_17_social_abundancing' in ns, 'the third function is missing')
# NI's contents carries ONE's headings
one_heads = [re.sub(r'^#{2,3} ', '', l) for l in one.split('\n') if re.match(r'^#{2,3} ', l)]
say(all(h in ni.split('\n---\n')[0] for h in one_heads), "NI's contents lacks a heading of ONE: %s" % [h for h in one_heads if h not in ni.split('\n---\n')[0]][:3])
print('ALL PASS' if ok else 'SOME FAIL')
