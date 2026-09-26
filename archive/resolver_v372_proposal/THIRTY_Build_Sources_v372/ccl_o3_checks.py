"""Run checks for Exhibit THIRTY Part EIGHT, sections 8.15 to 8.22 (the last third of the
exhibits of other workings): TWENTY-ONE, TWENTY-TWO, TWENTY-THREE, TWENTY-FIVE, TWENTY-SIX,
TWENTY-SEVEN, TWENTY-NINE and the Corus v330, at /home/claude/corus.

Each function named for a link returns True when the link holds as written.
A function named LINK_probe returns True when the failure named at that nye gap is found.
The resolver is imported from resolver_v372.py in this folder."""
import ast, json, math, os, re, sys
from fractions import Fraction
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV                      # the resolver, Exhibit ONE v372's code
C = RV._1_self_coupling
REPO = '/home/claude/corus'

def read(name):
    return open(os.path.join(REPO, name), encoding='utf-8').read()

HPR = 'Exhibit_TWENTY-ONE_Hard_Problem_Registry_v342.md'
RHR = 'Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v344.md'
LSR = 'Exhibit_TWENTY-FIVE_Living_Society_Registry_v347.md'
LFR = 'Exhibit_TWENTY-SIX_Living_File_Registry_v348.md'
LGR = 'Exhibit_TWENTY-SEVEN_Living_Ghost_Registry_v345a.md'

FORM = ['Conditions prior', 'Statement', "The field's account of its hardness", 'Accounts', 'Specifications',
        'Specifications withdrawn', 'Common requirement', 'Conserving relation', 'Conserving reach', 'Reach',
        'Unreachability', 'Persistence', 'Addresses', 'Approaches', 'Narrowing recorded', 'Progress', 'Own record']

def hp_entries():
    body = read(HPR).split('## The collection')[0]
    parts = re.split(r'^## (\d+) (.+)$', body, flags=re.M)
    return [(int(parts[i]), parts[i + 1].strip(), parts[i + 2]) for i in range(1, len(parts), 3)]

def hp_val(entry, prop):
    m = re.search(r'^\*\*' + re.escape(prop) + r'\.\*\*(.*)$', entry, re.M)
    return m.group(1).strip() if m else None

# ---------------------------------------------------------------- 8.15 TWENTY-ONE
def HP11_probe():
    # the form's seventeen properties in order at 254 entries; entry 33 carries two more
    off = [(n, [p for p in re.findall(r'^\*\*([^*]+?)\.\*\*', e, re.M) if p not in FORM])
           for n, _, e in hp_entries() if re.findall(r'^\*\*([^*]+?)\.\*\*', e, re.M) != FORM]
    return off == [(33, ['Which of the three the properties key to', 'What the approaches leave untouched'])]

def HP12():
    nums = [n for n, _, _ in hp_entries()]
    return (len(nums) == 255 and nums == sorted(nums) and nums[0] == 1 and nums[-1] == 257
            and sorted(set(range(1, 258)) - set(nums)) == [155, 172])

def HP16():
    E = hp_entries()
    return (len(E) == 255 and sum(bool(hp_val(e, 'Unreachability')) for *_, e in E) == 174
            and sum(bool(hp_val(e, 'Specifications withdrawn')) for *_, e in E) == 34
            and sum(bool(hp_val(e, 'Narrowing recorded')) for *_, e in E) == 231)

# ---------------------------------------------------------------- 8.16 TWENTY-TWO
def RH3():
    ok = all(n * n - (n - 1) * (n + 1) == 1 for n in range(2, 1001))
    ok &= (3 * 3 - 2 * 4, 4 * 4 - 3 * 5, 5 * 5 - 4 * 6, 24 * 24 - 23 * 25, 16 * 16 - 15 * 17) == (1,) * 5
    return ok and 4 * 4 - 2 * 6 == 4

def RH5():
    pairs = [(a, a + 1) for a in range(2, 6)]
    turns = [t for a, b in pairs for t in ((a, '<', b), (b, '>', a))]
    lesser = [min(t[0], t[2]) for t in turns]
    return (len(turns) == 8 and turns[0] == (2, '<', 3) and turns[-1] == (6, '>', 5)
            and all(turns[2 * i][0] == turns[2 * i + 1][2] for i in range(4))
            and all(pairs[i][1] == pairs[i + 1][0] for i in range(3)) and lesser == [2, 2, 3, 3, 4, 4, 5, 5])

TEN = ['arriving', 'opening', 'bound', 'carry', 'middle', 'sign', 'sequencing', 'rate', 'two-way', 'membrane']

def RH10():
    four = {'a reference held': ['arriving', 'bound', 'middle'], 'a rate held': ['sequencing', 'rate'],
            'a magnitude driven': ['sign', 'two-way'], 'a returned sign entered as cost': ['opening', 'carry', 'membrane']}
    t = read(RHR)
    said = all(k in t.lower() for k in four)
    flat = [x for v in four.values() for x in v]
    return said and sorted(flat) == sorted(TEN) and [len(v) for v in four.values()] == [3, 2, 2, 3]

def rh_deployed():
    t = read(RHR)
    return re.findall(r'^## (\d+)\.(\d+) (.+?) \(Hard Problem Registry ([\d, and]+)\)', t, re.M)

def RH15():
    h = rh_deployed()
    counts = [sum(1 for p, *_ in h if p == str(k)) for k in range(1, 13)]
    e21 = {n: name for n, name, _ in hp_entries()}
    nums = [int(x) for *_, n in h for x in re.findall(r'\d+', n)]
    named_ok = all(e21[int(re.findall(r'\d+', n)[0])] == name.strip() for _, _, name, n in h
                   if int(re.findall(r'\d+', n)[0]) in e21)
    return (len(h) == 257 and counts == [33, 24, 33, 9, 25, 19, 20, 16, 43, 33, 1, 1]
            and set(nums) - set(e21) == {155, 172} and set(e21) <= set(nums) and named_ok)

def RH16_probe():
    t = read(RHR)
    loc = t.split('**Resolving locator**')[1].split('# The given')[0]
    L = re.findall(r'^(\d+) (.+?) · [\d.]+(?: and [\d.]+)?, ', loc, re.M)
    name2num = {name: n for n, name, _ in hp_entries()}
    off = [int(n) - name2num[name] for n, name in L if name in name2num]
    unmatched = [name for n, name in L if name not in name2num]
    nums = [int(n) for n, _ in L]
    return (len(L) == 176 and nums[0] == 2 and nums[-1] == 177 and off.count(1) == 174 and len(unmatched) == 2)

# ---------------------------------------------------------------- 8.18 TWENTY-FIVE
def ls_entries():
    t = read(LSR)
    body = t.split('\n# 2 Collecting')[1].split('\n# 3 Passing')[0]
    parts = re.split(r'^## (2\.\d+) .+$', body, flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]

def LS7():
    E = ls_entries()
    lines = [re.search(r'^\*\*Any member carrying it\.\*\* (.*)$', e, re.M).group(1) for _, e in E]
    return len(E) == 22 and all(re.match(r'(No\b|No pair|No population)', l) for l in lines)

def LS11():
    E = ls_entries()
    st = {k: re.search(r'^\*\*Standing in the ten\.\*\* (.*)$', e, re.M).group(1) for k, e in E}
    filled = sorted(k for k, s in st.items() if 'All ten stand fill' in s)
    rest = sorted(set(st) - set(filled), key=lambda k: int(k.split('.')[1]))
    return (len(filled) == 18 and rest == ['2.2', '2.4', '2.5', '2.15']
            and 'The bound and the rate stand empty' in st['2.2'] and 'Filled at eight; 3 nye and 6 empty' in st['2.15'])

# ---------------------------------------------------------------- 8.19 TWENTY-SIX
def lf_rows():
    t = read(LFR)
    s1 = t.split('## 1.1 Living files')[1].split('## 1.3 Clusters')[0]
    rows = re.findall(r'^\| \*\*(.+?)\*\* \| (.+?) \|$', s1, re.M)
    return rows[:29], rows[29:]

def LF2():
    liv, imp = lf_rows()
    names = [n for n, _ in liv]
    return (len(liv) == 29 and len(imp) == 5 and names[0] == 'Natural Intelligence'
            and names[-1] == 'TWENTY-SEVEN · Living Ghost Registry'
            and not any('TWENTY-EIGHT' in n or 'TWENTY-NINE' in n for n in names))

def LF3():
    t = read(LFR)
    cl = t.split('## 1.3 Clusters')[1].split('# PART TWO')[0]
    rows = re.findall(r'^\| \*\*(.+?)\*\* \| (.+?) \|$', cl, re.M)
    seated = [x.strip() for _, m in rows for x in m.split('·')]
    words = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE',
             'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY',
             'TWENTY-ONE', 'TWENTY-TWO', 'TWENTY-THREE', 'TWENTY-FOUR', 'TWENTY-FIVE', 'TWENTY-SIX', 'TWENTY-SEVEN']
    got = {s.split(' ')[0] for s in seated if s.split(' ')[0] in words}
    return (len(rows) == 7 and len(seated) == 26 and len(set(seated)) == 26
            and sorted(set(words) - got) == ['TWENTY-FOUR', 'TWENTY-SIX', 'TWENTY-THREE'])

def LF4():
    h = rh_deployed()
    c = [sum(1 for p, *_ in h if p == str(k)) for k in range(1, 11)]
    odd, even = c[0::2], c[1::2]
    return all(o > e for o, e in zip(odd, even)) and sum(odd) == 154 and sum(even) == 101

def cross(pattern, cells):
    return [n for n, s in cells if re.search(pattern, s)]

def LF7():
    liv, imp = lf_rows()
    titles = [n for n, _ in liv + imp]
    return (len(cross(r'\bSocial\b(?!-)', liv)) == 9 and len(cross(r'Social-', liv)) == 1
            and sum('Registry' in n for n in titles) + len(cross('Registry', liv)) == 7
            and len(cross(r'(?<!-)\bCompetency\b', liv)) == 3 and len(cross(r'\bSelf-', liv)) == 4)

def LF8_probe():
    liv, imp = lf_rows()
    stable = cross(r'\bStable', liv)
    value = cross(r'\bValue\b', liv + imp)
    surface = cross(r'Surface', liv + imp)
    return (len(stable) == 8 and 'Natural Intelligence Corus' in stable
            and len(surface) == 3 and len(value) == 4)

# ---------------------------------------------------------------- 8.20 TWENTY-SEVEN
def GH13():
    state, flow, either = {1, 7, 8, 9}, {3, 4, 5, 10}, {2, 6}
    return state | flow | either == set(range(1, 11)) and len(state) + len(flow) + len(either) == 10

DOOR_HOLDING = {1: 1, 2: 8, 3: 9, 4: 6, 5: 4, 6: 2, 7: 5, 8: 3, 9: 10, 10: 7}

def GH14():
    t = read(LGR)
    sec = t.split('## 7.10')[2] if t.count('## 7.10') > 1 else t.split('## 7.10')[1]
    rows = re.findall(r'^\| (\d+) · \w[\w-]* \| .+? \| (\d+) · \*\*', sec, re.M)
    got = {int(a): int(b) for a, b in rows}
    return got == DOOR_HOLDING and sorted(got.values()) == list(range(1, 11))

def GH15_probe():
    reached = {1, 7, 8, 3, 4, 5}                # 7.10's second table: (i)(iv)->1, (v)(vii)->7, (vi)->8, (viii)->3,4, (ix)->5
    t = read(LGR)
    said = 'Door lines 6, 9 and 10 carry surplus, bound and reach beside' in t
    return said and sorted(set(range(1, 11)) - reached) == [2, 6, 9, 10]

def GH16():
    t = read(LGR)
    sec = t.split('## 7.11')[2] if t.count('## 7.11') > 1 else t.split('## 7.11')[1]
    rows = re.findall(r'^\| (\d+) · [\w-]+ \| `(\w+)` · (within|at the membrane)', sec, re.M)
    nm = {int(a): (b, c) for a, b, c in rows}
    within = sorted(k for k, (_, f) in nm.items() if f == 'within')
    names = [nm[k][0] for k in range(1, 11)]
    adj = re.findall(r'^\| (\d+) · [\w-]+ \| `(\w+)` → `(\w+)` \| `(\w+)` \| (?:`(\w+)`|No shared)', sec, re.M)
    adj = [(a, x, y, b) for a, x, y, b, _ in adj]
    shared = sorted(int(a) for a, x, y, b in adj if b in (x, y))
    return (len(nm) == 10 and len(set(names)) == 8 and within == [3, 4, 6, 9]
            and len({nm[k][0] for k in within}) == 4 and len({nm[k][0] for k in (1, 2, 5, 7, 8, 10)}) == 4
            and nm[2][0] == nm[7][0] and nm[8][0] == nm[10][0] and len(adj) == 10 and shared == [1, 5])

def GH21():
    rows = [2, 8, 8, 18, 18, 32, 32]
    ends = [sum(rows[:i + 1]) for i in range(7)]
    return sum(rows) == 118 and 2 + 8 + 18 + 32 == 60 and 60 not in ends and ends == [2, 10, 18, 36, 54, 86, 118]

# ---------------------------------------------------------------- 8.21 TWENTY-NINE
def I5():
    a, b = [24, 27, 32], [24, 29, 32]
    g = lambda r: [r[i + 1] - r[i] for i in range(2)]
    return g(a) == [3, 5] and g(b) == [5, 3] and a[-1] - a[0] == b[-1] - b[0] == 8

def I6():
    ok = True
    for k in range(1, 2001):
        x = -1.55 + 3.1 * k / 2001
        d = 1 - math.tan(x) ** 2
        if abs(math.cos(x)) < 1e-6 or abs(math.cos(2 * x)) < 1e-3 or abs(d) < 1e-9: continue
        ok &= math.isclose(math.tan(2 * x), 2 * math.tan(x) / d, rel_tol=1e-9, abs_tol=1e-9)
    return ok

def I8():
    P = [p for p in range(2, 60) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    return len(P) == 17 and P[0] == 2 and P[-1] == 59 and sum(P) == 440

def I9():
    # the resolver's own identifiers give names 1 to 17; the roots of 1 to 16 are twelve, and 17 adds a thirteenth
    src = open(os.path.join(HERE, 'resolver_v372.py')).read()
    ids = {n.id for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Name) and re.fullmatch(r'_\d+_\w+', n.id)}
    ids |= {a.arg for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef) for a in n.args.args if re.fullmatch(r'_\d+_\w+', a.arg)}
    ids |= {n.name for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef)}
    num = {int(re.match(r'_(\d+)_', i).group(1)): i.split('_', 3)[3] for i in ids}
    roots16 = {num[k] for k in range(1, 17)}
    s17 = RV.CONNECTORS[17][0].split('-')[-1]
    return sorted(num) == list(range(1, 18)) and len(roots16) == 12 and s17 == 'abundancing' and num[17] == s17 and s17 not in roots16

# ---------------------------------------------------------------- 8.22 Corus v330
def CO12():
    phi = (1 + 5 ** 0.5) / 2
    x = Fraction(1)
    fib = [1, 1]
    ok = True
    for i in range(40):
        x = 1 + 1 / x
        fib.append(fib[-1] + fib[-2])
        ok &= x == Fraction(fib[-1], fib[-2])
    return ok and abs(float(x) - phi) < 1e-15 and abs(phi * phi - phi - 1) < 1e-12

def CO19():
    gaps = [1, 2, 4, 6]
    kept = [p for p in permutations(range(4)) if all(gaps[p[i]] < gaps[p[i + 1]] for i in range(3))]
    return len(list(permutations(range(4)))) == 24 and kept == [(0, 1, 2, 3)]

def CO21():
    return 7 * 17 - 1 == 118 and 59 * 2 == 118 and 6.94 < 118 / 17 < 6.95

CHECKS = {k: v for k, v in globals().items()
          if re.fullmatch(r'(HP|RH|V|LS|LF|GH|I|CO)\d+(_probe)?', k) and callable(v)}
ORDER = ['HP', 'RH', 'V', 'LS', 'LF', 'GH', 'I', 'CO']

if __name__ == '__main__':
    res = {}
    for k in sorted(CHECKS, key=lambda s: (ORDER.index(re.match(r'[A-Z]+', s).group(0)),
                                           int(re.search(r'\d+', s).group(0)))):
        try: res[k] = bool(CHECKS[k]())
        except Exception as e: res[k] = f'error: {e!r}'
        print(k, res[k])
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'ccl_o3_check_results.json')
    json.dump(res, open(out, 'w'), indent=1)
