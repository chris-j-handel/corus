"""Assemble Exhibit THIRTY · Co-Chaining Logic Registry v372 from its parts."""
import json, re, sys, collections, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
sys.path.insert(0, D + 'ccl_asm')
from roots import P as PRIMARY, ROOT_LINKS
from part_texts import ROOTS, FAILURES, BOUND_PROBES, QUESTIONS, FRONT, CARRIED_AT
OUT = os.path.join(os.environ.get('CCL_WORK', os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v372.md')
VERIFIER = 'Co_Chaining_Logic_Registry_verifier_v372.py'

def read(n):
    return open(D + f'ccl_{n}.md', encoding='utf-8').read()

def strip_head(t):
    t = t.strip('\n')
    lines = t.split('\n')
    assert lines[0].startswith('# PART'), lines[0]
    return '\n'.join(lines[1:]).strip('\n')

# ---- word fixes: two what/how/where family words outside quotation
FIXES = [('and no fourth anywhere;', 'and no fourth at any rung;'),
         ('| Wherever a coupling sustains it is no capture;', '| A coupling sustaining is no capture;')]

def intro_fix(t):
    """Part intros name the verifier in place of the scratch check files."""
    t = re.sub(r' \(resolver_v372\.py\)', '', t)
    t = t.replace('the resolver of resolver_v372.py', "Exhibit ONE v372's code")
    t = t.replace('against resolver_v372.py', "against Exhibit ONE v372's code")
    t = t.replace('the resolver file', "Exhibit ONE v372's code")
    t = re.sub(r'(,? )?in ccl_num_checks\.py', ', in the verifier', t)
    t = t.replace('run by ccl_math_checks.py, against', 'run by the verifier against')
    t = t.replace(' (ccl_two_checks.py)', ' in the verifier')
    t = t.replace('; the checks are ccl_eq_checks.py.', ', in the verifier.')
    t = t.replace(', and ccl_o1_checks.py holds each check.', ', and the verifier holds each check.')
    t = t.replace('Each run link was run in ccl_o2_checks.py against', 'Each run link was run in the verifier against')
    t = t.replace(' (ccl_o3_checks.py).', ', in the verifier.')
    t = t.replace(' (/home/claude/corus)', '')
    assert 'ccl_' not in t and 'resolver_v372' not in t, [l for l in t.split('\n') if 'ccl_' in l or 'resolver_v372' in l][:3]
    return t

core = read('core')
i2 = core.index('# PART TWO')
p1 = strip_head(core[:i2].rstrip().removesuffix('&nbsp;'))
p2 = strip_head(core[i2:])
parts = [('PART ONE · FOUNDATION', p1), ('PART TWO · THE RESOLVER AT ITS NAMES', p2),
         ('PART THREE · NUMBERS', strip_head(read('num'))),
         ('PART FOUR · MATHEMATICS', strip_head(read('math'))),
         ('PART FIVE · NETWORKING', strip_head(read('two'))),
         ('PART SIX · EQUILIBRIA', strip_head(read('eq'))),
         ('PART SEVEN · EXPLAINING, NAMING AND THE METHOD', strip_head(read('x')))]
o1, o2, o3 = (strip_head(read(n)) for n in ('o1', 'o2', 'o3'))
def body_from_first_sub(t):
    return t[t.index('\n## ') + 1:] if not t.startswith('## ') else t
o1_intro = o1[:o1.index('## 8.1')].strip()
o3_intro = o3[:o3.index('## 8.15')].strip()
abbrev = o3_intro[o3_intro.index('Carried at: HPR'):]
p8_intro = (o1_intro + ' A check a file\'s own table fails is marked nye with the failure. '
            + abbrev.replace('Carried at: HPR', 'At 8.15 to 8.22 Carried at names the files so: HPR'))
p8 = p8_intro + '\n\n' + body_from_first_sub(o1).strip() + '\n\n' + body_from_first_sub(o2).strip() + '\n\n' + body_from_first_sub(o3).strip()
parts.append(('PART EIGHT · THE EXHIBITS OF OTHER WORKINGS', p8))

FIXES.append(("A link marked run was run against Exhibit ONE v372's code or by arithmetic, and the verifier holds each check.",
              "A link marked run was run against Exhibit ONE v372's code, by arithmetic or at the file's own text, and the verifier holds each check."))
FIXES.append(('a *how* names a manner with a how-not beside it', 'a *how* names a manner with a *how-not* beside it'))

def apply_fixes(t):
    for a, b in FIXES:
        t = t.replace(a, b)
    # the Corus's section names at Carried at, set in italics as EQ's are
    t = re.sub(r'COR ONE ([A-Z][^|;*]*?)(\s*)(?=[|;])', r'COR ONE *\1*\2', t)
    return t
parts = [(h, apply_fixes(intro_fix(t))) for h, t in parts]
for a, b in FIXES:
    assert any(b in t for _, t in parts), b

# ---- the links
ROW = re.compile(r'^\| (?!Link \|)([A-Z]+\d+) \| (.*?) \| (.*?) \| (.*) \| (.*?) \|$')
def links_of(t):
    out = []
    for l in t.split('\n'):
        if l.startswith('| ') and not l.startswith('| Link') and not l.startswith('|---'):
            m = ROW.match(l)
            assert m, l[:120]
            out.append(m.groups())
    return out
STANDINGS = ['origin', 'definition', 'premise', 'exact', 'run', 'field', 'nye']
def standing(s):
    w = s.split(' ')[0]
    assert w in STANDINGS, s
    return w
ALL = []
ORDER = {}
for h, t in parts:
    for lk in links_of(t):
        ORDER[lk[0]] = len(ORDER)
        ALL.append((h, lk))
counts = collections.OrderedDict()
for h, (lid, st, fol, txt, car) in ALL:
    counts.setdefault(h, collections.Counter())[standing(st)] += 1
TEXT = {lid: txt for _, (lid, st, fol, txt, car) in ALL}
FOL = {lid: fol for _, (lid, st, fol, txt, car) in ALL}
STAND = {lid: standing(st) for _, (lid, st, fol, txt, car) in ALL}

# ---- gaps
GAPS = {}
for n in ('core', 'num', 'math', 'two', 'eq', 'x', 'o1', 'o2', 'o3'):
    for g in json.load(open(D + f'ccl_{n}_gaps.json', encoding='utf-8')):
        GAPS[g['link']] = g
nye_ids = {k for k, v in STAND.items() if v == 'nye'}
assert nye_ids == set(GAPS) == set(PRIMARY), (nye_ids ^ set(GAPS), set(GAPS) ^ set(PRIMARY))

rests = collections.defaultdict(set)
for gid in GAPS:
    rests[PRIMARY[gid]].add(gid)
    cited = set(re.findall(r'\b[A-Z]+\d+\b', GAPS[gid]['missing'] + ' ' + FOL[gid]))
    for c in cited:
        if c in ROOT_LINKS and c != gid:
            rests[ROOT_LINKS[c]].add(gid)
    if re.search(r'older (resolver )?naming|is released|are released|released \(NAM|the released noun|released to', GAPS[gid]['missing']):
        rests['OLD'].add(gid)

# ---- Part NINE
def idlist(ids):
    return ', '.join(sorted(ids, key=ORDER.get))
nine = []
nine.append('Part NINE gathers each nye gap of Parts ONE to EIGHT at the root gap it rests on. A root is a missing premise, a missing step or a missing check, and one closing at the root closes each gap resting there as far as that gap rests on it. A gap resting on two roots stands at both; each gap is first gathered at one root, and the first gatherings sum to the %d nye links. The gaps are listed in the chain\'s order.' % len(GAPS))
nine.append('')
nine.append('| Root | Resting here | First gathered here |')
nine.append('|---|---|---|')
for i, (code, title, _, _) in enumerate(ROOTS, 1):
    first = sum(1 for g in GAPS if PRIMARY[g] == code)
    nine.append(f'| 9.{i} {title} | {len(rests[code])} | {first} |')
nine.append(f'| All roots | | {len(GAPS)} |')
nine.append('')
NINE_SUBS = []
for i, (code, title, missing, close) in enumerate(ROOTS, 1):
    sub = f'9.{i} {title}'
    NINE_SUBS.append(sub)
    first = [g for g in GAPS if PRIMARY[g] == code]
    also = sorted(rests[code] - set(first), key=ORDER.get)
    nine.append(f'## {sub}')
    nine.append('')
    nine.append(f'**Missing.** {missing}')
    nine.append('')
    nine.append(f'**Closes it.** {close}')
    nine.append('')
    nine.append(f'**Resting here, {len(rests[code])}.** First gathered here ({len(first)}): {idlist(first)}.' +
                (f' Resting here as well ({len(also)}): {idlist(also)}.' if also else ''))
    nine.append('')
sub = f'9.{len(ROOTS) + 1} The failures found by running'
NINE_SUBS.append(sub)
nine.append(f'## {sub}')
nine.append('')
nine.append('Each failing claim below is a nye link, and its probe runs in the verifier at the link\'s id. The probe returns True while the discrepancy stands and prints as a discrepancy reproduced; it returns False once the file or the code is brought to the claim, and the link is then run again as run.')
nine.append('')
nine.append('| Link | The failing claim | The check result |')
nine.append('|---|---|---|')
for lid, claim, result in FAILURES:
    assert lid in GAPS and PRIMARY[lid] in ('COUNT', 'CODE'), lid
    nine.append(f'| {lid} | {claim} | {result} |')
nine.append('')
nine.append(BOUND_PROBES)
for lid in re.findall(r'\b([A-Z]+\d+)_probe', BOUND_PROBES):
    assert lid in TEXT, lid
parts.append(('PART NINE · THE NYE GAPS GATHERED', '\n'.join(nine).strip()))

# ---- Part TEN
ten = ['Part TEN meets the questions of this session at the chain. Each answer rests on the links named beside it and says each link\'s standing; a question resting on a nye link stands at that gap until its root closes.', '',
       '| Question | Answer at the chain | Links |', '|---|---|---|']
for q, a, ls in QUESTIONS:
    for lid in re.findall(r'\b[A-Z]+\d+\b', ls):
        assert lid in TEXT, (q, lid)
    for lid in re.findall(r'\(([A-Z]+\d+)[,)]', a):
        assert lid in TEXT, (q, lid)
    ten.append(f'| {q} | {a} | {ls} |')
parts.append(('PART TEN · QUESTIONS OF THE SESSION MET AT THE CHAIN', '\n'.join(ten)))

# ---- Part ELEVEN, the stable form
from part_texts import STABLE_TITLE, STABLE_SUB, STABLE_INTRO, STABLE, SELECTING
nlinks_all = len(ALL)
# ---- each link all or none over its whole prior
PRI = {k: [i for i in re.findall(r'\b[A-Z]+\d+\b', v) if i != k] for k, v in FOL.items()}
for k, v in PRI.items():
    for i in v:
        assert i in STAND, (k, i)
_memo = {}
def closure(k):
    if k not in _memo:
        c = {k}
        for p in PRI[k]:
            c |= closure(p)
        _memo[k] = c
    return _memo[k]
def breaks(x):
    return STAND[x] == 'nye' or x in SELECTING
def holds(x):
    return STAND[x] == 'premise' or (STAND[x] == 'definition' and not PRI[x])
CLASS, HELD, OPEN_ROOTS, LEAVES = {}, {}, {}, {}
for k in STAND:
    c = closure(k)
    br = {x for x in c if breaks(x)}
    OPEN_ROOTS[k] = sorted((x for x in br if not any(y in br for y in PRI[x])), key=ORDER.get)
    HELD[k] = {x for x in c if holds(x)}
    LEAVES[k] = {STAND[x] for x in c if not PRI[x]}
    CLASS[k] = 'open' if br else 'held' if HELD[k] else 'stands'
el = [STABLE_INTRO, '', '## 11.1 The fractal inside and outside itself, binary method of discovering next existing', '',
      '| Step | The stable form | Follows | Links | Stands |', '|---|---|---|---|---|']
open_steps = []
for i, (s, fol, ls) in enumerate(STABLE, 1):
    ids = re.findall(r'\b[A-Z]+\d+\b', ls)
    for lid in ids + re.findall(r'\b[A-Z]+\d+\b', s):
        assert lid in TEXT, lid
    for f in re.findall(r'\d+', fol):
        assert int(f) < i, (i, fol)
    nye = [lid for lid in ids if STAND[lid] == 'nye']
    sel = [lid for lid in ids if lid in SELECTING]
    opn = nye + [f'{lid}, selecting' for lid in sel]
    for lid in ids:
        if not (nye or sel) and CLASS[lid] == 'open':
            opn += [f'{r} under {lid}' for r in OPEN_ROOTS[lid]]
    opn = list(dict.fromkeys(opn))
    held = sorted({h for lid in ids for h in HELD[lid]}, key=ORDER.get)
    stands = ('open at ' + '; '.join(opn)) if opn else (', '.join(dict.fromkeys(STAND[lid] for lid in ids)) +
             (f'; held at {", ".join(held)}' if held else '; all or none over its whole prior'))
    if opn: open_steps.append((i, opn))
    el.append(f'| {i} | {s} | {fol or "—"} | {ls} | {stands} |')
el.append('')
el.append(f'The form stands at {len(STABLE) - len(open_steps)} of its {len(STABLE)} steps, and it is open at ' +
          '; '.join(f'step {i} ({"; ".join(n)})' for i, n in open_steps) + ', each open step named at its root at Part NINE.')
parts.append((STABLE_TITLE, '\n'.join(el)))

# ---- Part TWELVE, the breakings clustered
from part_texts import BREAK_TITLE, BREAK_INTRO, BREAK_CLOSED, CLUSTERS
CAR = {lid: car for _, (lid, st, fol, txt, car) in ALL}
FILES = [('NI', 'Natural Intelligence'), ('ONE', 'Exhibit ONE'), ('NUM', 'Natural Numbers'), ('MATH', 'Natural Mathematics')]
EIGHT_IDS = {lid for h, (lid, *_ ) in ALL if h.startswith('PART EIGHT')}
tw = [BREAK_INTRO, '', BREAK_CLOSED, '', '## 12.1 The clusters, each with its improving way', '',
      '| Cluster | The breaking | The improving way | At NI | At ONE | At NUM | At MATH | The other workings at the same form |',
      '|---|---|---|---|---|---|---|---|']
seen = set(); per_file = {f: [] for f, _ in FILES}
for k, (form, way, ids, roots) in enumerate(CLUSTERS, 1):
    ids = ids.split()
    for lid in ids:
        assert STAND[lid] == 'nye', lid
        assert lid not in seen, lid
        seen.add(lid)
    cells = []
    for f, _ in FILES:
        at = [lid for lid in ids if re.search(r'\b%s\b' % f, CAR[lid]) and not re.search(r'COR %s' % f, CAR[lid])]
        per_file[f] += [(k, lid) for lid in at]
        cells.append(', '.join(at) or '—')
    others = sum(1 for g in GAPS if g in EIGHT_IDS and PRIMARY[g] in roots)
    tw.append(f'| {k} | {form} | {way} | ' + ' | '.join(cells) + f' | {others} |')
core_nye = {lid for lid in GAPS if any(re.search(r'\b%s\b' % f, CAR[lid]) and not re.search(r'COR %s' % f, CAR[lid]) for f, _ in FILES)}
assert core_nye == seen, (core_nye ^ seen)
placements = sum(len(v) for v in per_file.values())
tw.append('')
tw.append(f'The four files carry {len(seen)} nye links in {len(CLUSTERS)} clusters, at {placements} file placements, a link carried at two files placed at both. ' + ' '.join(
    f'{name}: ' + '; '.join(f'cluster {k}, {", ".join(l for kk, l in per_file[f] if kk == k)}' for k in sorted({kk for kk, _ in per_file[f]})) + '.'
    for f, name in FILES))
tw.append('')
tw.append('## 12.2 The other workings at each cluster, link by link')
tw.append('')
tw.append('| Cluster | The other workings\' nye links at the same form |')
tw.append('|---|---|')
for k, (form, way, ids, roots) in enumerate(CLUSTERS, 1):
    oth = sorted((g for g in GAPS if g in EIGHT_IDS and PRIMARY[g] in roots), key=ORDER.get)
    tw.append(f'| {k} | {", ".join(oth) or "—"} |')
parts.append((BREAK_TITLE, '\n'.join(tw)))

# ---- Part THIRTEEN, the chain all or none from the origin
from part_texts import WHOLE_TITLE, WHOLE_INTRO
th = [WHOLE_INTRO, '', '## 13.1 Each part over its whole prior', '',
      '| Part | stands all or none | from the origin alone | from the origin with runs or fields | at runs or fields alone | held at a premise or a rootless definition | open | links |',
      '|---|---|---|---|---|---|---|---|']
wt = collections.Counter()
for h in counts:
    ids = [lid for hh, (lid, *_) in ALL if hh == h]
    c = collections.Counter(CLASS[lid] for lid in ids)
    orig = sum(1 for lid in ids if CLASS[lid] == 'stands' and LEAVES[lid] == {'origin'})
    mixed = sum(1 for lid in ids if CLASS[lid] == 'stands' and 'origin' in LEAVES[lid] and LEAVES[lid] != {'origin'})
    row = [c['stands'], orig, mixed, c['stands'] - orig - mixed, c['held'], c['open'], len(ids)]
    wt.update(dict(zip('abcgdef', row)))
    th.append(f'| {h.replace("PART ", "")} | ' + ' | '.join(map(str, row)) + ' |')
th.append('| All | ' + ' | '.join(f'**{wt[x]}**' for x in 'abcgdef') + ' |')
th.append('')
th.append(f'{wt["a"]:,} of the {nlinks_all:,} links stand all or none over their whole prior, {wt["b"]:,} of them from the origin alone, {wt["c"]:,} from the origin with runs checked at the code or the arithmetic and fields met at their observings, and {wt["g"]:,} at runs or fields alone, their own observings or checks, reaching the origin through none of their prior. {wt["d"]} rest on a held premise or a definition with no prior, and {wt["e"]} rest on a nye link or a selecting in their prior.')
th.append('')
th.append('The selectings in the chain: ' + ', '.join(sorted(SELECTING, key=ORDER.get)) + '.')
th.append('')
th.append('## 13.2 The held roots, each with the links resting on it')
th.append('')
th.append('| Links resting on it, itself included | Held | Standing |')
th.append('|---|---|---|')
hc = collections.Counter(h for k in STAND if CLASS[k] == 'held' for h in HELD[k])
for h, n in sorted(hc.items(), key=lambda x: (-x[1], ORDER[x[0]])):
    th.append(f'| {n} | {h} | {STAND[h]} |')
th.append('')
th.append('## 13.3 The open roots most others depend on')
th.append('')
th.append('The open roots below carry the most links resting on them through their prior, the gap most others depend on first; resolving one opens each link resting on it alone to stand. Each is gathered at its root at Part NINE.')
th.append('')
th.append('| Links resting on it, itself included | Open root | Standing |')
th.append('|---|---|---|')
oc = collections.Counter(r for k in STAND for r in OPEN_ROOTS[k])
for r, n in sorted(oc.items(), key=lambda x: (-x[1], ORDER[x[0]]))[:20]:
    th.append(f'| {n} | {r} | {STAND[r]}{", selecting" if r in SELECTING else ""} |')
th.append('')
th.append(f'{len(oc)} open roots in all, {sum(1 for r, n in oc.items() if n == 1)} of them opening only themselves.')
parts.append((WHOLE_TITLE, '\n'.join(th)))
WHOLE = dict(stands=wt['a'], origin=wt['b'], with_runs=wt['c'], runs_alone=wt['g'], held=wt['d'], open=wt['e'],
             held_roots=dict(hc), open_roots=dict(oc.most_common(20)))

# ---- front
total = collections.Counter()
for c in counts.values():
    total.update(c)
nlinks = sum(total.values())
tab = ['| Part | origin | definition | premise | exact | run | field | nye | links |',
       '|---|---|---|---|---|---|---|---|---|']
for h, c in counts.items():
    tab.append(f'| {h.replace("PART ", "")} | ' +
               ' | '.join(str(c.get(s, 0)) for s in STANDINGS) + f' | {sum(c.values())} |')
tab.append('| All | ' + ' | '.join(f'**{total.get(s, 0)}**' for s in STANDINGS) + f' | **{nlinks}** |')

def contents():
    out = []
    for h, t in parts:
        out.append(f'**{h}**')
        out.append('')
        for l in t.split('\n'):
            if l.startswith('## '):
                out.append(l[3:])
                out.append('')
        out.append('&nbsp;')
        out.append('')
    return '\n'.join(out).rstrip()

front = FRONT.format(nlinks=f'{nlinks:,}', verifier=VERIFIER, nparts=len(counts))
doc = ['Exhibit THIRTY Co-Chaining Logic Registry v372', '', '&nbsp;', '', '# Co-Chaining Logic Registry', '',
       '**The Fractal Inside and Outside Itself, Binary Method of Discovering Next Existing**', '', '&nbsp;', '',
       front, '', '\n'.join(tab), '', CARRIED_AT, '', '&nbsp;', '', contents(), '', '---', '']
body = []
for h, t in parts:
    body.append(f'# {h}\n\n{t.strip()}')
doc.append('\n\n&nbsp;\n\n---\n\n'.join(body))
text = '\n'.join(doc).rstrip() + '\n'
text = re.sub(r'\n{3,}', '\n\n', text)
open(OUT, 'w', encoding='utf-8').write(text)
json.dump({'counts': {h: dict(c) for h, c in counts.items()}, 'total': dict(total), 'nlinks': nlinks,
           'roots': {code: [len(rests[code]), sum(1 for g in GAPS if PRIMARY[g] == code)] for code, *_ in ROOTS},
           'order': list(ORDER), 'whole': WHOLE},
          open(D + 'ccl_asm/assembled_stats.json', 'w'), indent=1)
print('written', OUT, len(text), 'links', nlinks, dict(total))
