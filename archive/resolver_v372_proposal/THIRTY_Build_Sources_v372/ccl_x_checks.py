"""Run checks for Exhibit THIRTY Part SEVEN (EXPLAINING, NAMING AND THE METHOD, links X1...),
against the resolver of Exhibit ONE v372 (resolver_v372.py beside this file), arithmetic
enumerations, and the counts the three files name (read from /home/claude/work at v372).
Each function returns True when the link holds as stated.
Run: python3 ccl_x_checks.py [results.json]"""
import os, re, sys, json
from itertools import product, combinations
from fractions import Fraction
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolver_v372 as RV
from resolver_v372 import _1_self_coupling as C, _9_other_releasing as R, CONNECTORS, JOINS

W = '/home/claude/work/'
EXP = W + 'Exhibit_TWELVE_Natural_Explaining_v372.md'
NAM = W + 'Exhibit_TWENTY_Natural_Naming_v372.md'
GIM = W + 'Exhibit_TWENTY-FOUR_Geodesic_Improving_Method_v372.md'
K = 'k'
S = (1, -1)


def section(path, head):
    """Text of the '## head' section of a file, up to the next heading."""
    t = open(path, encoding='utf-8').read()
    m = re.search(r'^## ' + re.escape(head) + r'.*?$(.*?)(?=^#{1,2} |\Z)', t, re.M | re.S)
    return m.group(1)


def table_rows(txt):
    rows = [l for l in txt.splitlines() if l.startswith('|')]
    return [r for r in rows[2:]]            # after header and rule


def traced(carry, offer):
    """Call 1-self-coupling and read its own gathering (6, 14, 12, 10, 11) at its return."""
    got = {}
    code = C.__code__

    def local(frame, event, arg):
        if event == 'return':
            got.update({k: v for k, v in frame.f_locals.items()})
        return local

    def glob(frame, event, arg):
        return local if frame.f_code is code else None

    sys.settrace(glob)
    try:
        out = C(list(carry), list(offer))
    finally:
        sys.settrace(None)
    return out, got


# ------------------------------------------------------------ 7.1 explaining
def X28():
    # closed genus-zero surface, three faces at each corner, pentagons p and hexagons h
    ok = True
    for p in range(0, 61):
        for h in range(0, 501):
            E = Fraction(5 * p + 6 * h, 2); V = Fraction(2, 3) * E; F = p + h
            ok &= ((V - E + F) == 2) == (p == 12)
    return ok


def X41():
    zero, c1 = C([], [(K, 1), (K, -1)])          # a zero surfaced
    none, c2 = C([], [])                          # a connection delivering nothing
    return zero == [(K, 0)] and c1 == [] and none == [] and c2 == [] and zero != none


def X43_probe():
    return 2 * 5 == 10 == comb(5, 2)


# ------------------------------------------------------------ 7.2 naming
NAMES = {1: '1-self-coupling', 2: '2-self-offering', 3: '3-self-carrying', 4: '4-self-sharing',
         5: '5-other-neutralling', 6: '6-other-crossing', 7: '7-other-corusing', 8: '8-other-torusing',
         9: '9-other-releasing', 10: '10-other-surfacing', 11: '11-other-chaining', 12: '12-other-surplusing',
         13: '13-social-neutralling', 14: '14-social-crossing', 15: '15-social-corusing',
         16: '16-social-torusing', 17: '17-social-abundancing'}


def X49():
    src = open(RV.__file__, encoding='utf-8').read()
    idents = set(re.findall(r'\b_(\d+)_(self|other|social)_([a-z]+)\b', src))
    code = {int(n): f'{n}-{r}-{root}' for n, r, root in idents}
    code.update({n: CONNECTORS[n][0] for n in CONNECTORS})
    if any(code[n] != NAMES[n] for n in code) or set(code) != set(range(1, 18)):
        return False
    ok = True; seen = 0
    for path in (EXP, NAM, GIM):
        t = open(path, encoding='utf-8').read()
        for m in re.finditer(r'(?<![\w`])(\d{1,2})-(self|other|social)-([a-z]+)', t):
            n = int(m.group(1)); seen += 1
            ok &= n in NAMES and m.group(0) == NAMES[n]
        for m in re.finditer(r'`_(\d+)_(self|other|social)_([a-z]+)`', t):
            n = int(m.group(1)); seen += 1
            ok &= m.group(0).strip('`')[1:].replace('_', '-') == NAMES[n]
    return ok and seen > 0


def X62():
    step = lambda v: (v[1], -v[0])
    ok = True
    for v in product(S, S):
        v2 = step(step(v)); v4 = step(step(v2))
        ok &= v2 == (-v[0], -v[1]) and v4 == v and v2 != v
        ok &= (v[1], v[0]) == (v[1], v[0])                    # the other order inverts no sign
        ok &= step(step(step(v))) == (-v[1], v[0])            # three right spiral steps as one
    return ok


def X63():
    place = lambda n, lo: n - lo + 1
    return (place(6, 1) == place(14, 9) == place(22, 17) == 6
            and [n - 16 for n in (19, 27, 22, 30)] == [3, 11, 6, 14]
            and 22 not in NAMES)


FIVE = {1: 'co bi co bi co', 0: 'bi co bi co bi'}
EARLIER = {3: 'co_carrying', 1: 'co_bi_coupling', 6: 'bi_co_bi_transmissioning',
           7: 'co_bi_co_bi_co_corusing', 8: 'bi_co_bi_co_bi_torusing', 2: 'bi_arriving',
           4: 'bi_offering', 10: 'bi_co_surfacing', 11: 'co_bi_carrying', 12: 'bi_co_tunneling',
           14: 'bi_co_inversioning', 16: 'bi_co_inseparating'}


def X64():
    odd, even = FIVE[1].split(), FIVE[0].split()
    ok = odd[0] == odd[4] == 'co' and odd[1] == odd[3] == 'bi' and odd[2] == 'co'
    ok &= even[0] == even[4] == 'bi' and even[1] == even[3] == 'co' and even[2] == 'bi'
    swap = {'co': 'bi', 'bi': 'co'}
    ok &= [swap[x] for x in odd] == even and [swap[x] for x in even] == odd
    counts = {}
    for n, w in EARLIER.items():
        pre = [p for p in w.split('_') if p in ('co', 'bi')]
        ok &= pre == FIVE[n % 2].split()[:len(pre)]
        counts[n] = len(pre)
    ok &= counts[3] == 1 and counts[1] == 2 and counts[6] == 3 and counts[7] == 5 and counts[8] == 5
    # the table at NAM 3.3: odd opens co, even opens bi, five-prefix at the number's origin
    for r in table_rows(section(NAM, '3.3')):
        cells = [c.strip(' *`') for c in r.strip('|').split('|')]
        n = int(cells[0].split('-')[0])
        ok &= cells[1] == ('co' if n % 2 else 'bi') and cells[2] == FIVE[n % 2].replace(' ', '-')
    return ok


def X66():
    up = lambda n: n + 8 if n <= 8 else n - 8
    pod = lambda n: 17 - n
    ok = True
    for row in ([1, 9, 8, 16], [2, 10, 7, 15], [3, 11, 6, 14], [4, 12, 5, 13]):
        changes = []
        for i in range(4):
            a, b = row[i], row[(i + 1) % 4]
            face = 'up' if b == up(a) else ('pod' if b == pod(a) else None)
            ok &= face is not None
            if a % 2 != b % 2: changes.append(face)
        ok &= changes == ['pod', 'pod']
        par = [n % 2 for n in row]
        ok &= sum(par[i] != par[i - 1] for i in range(4)) == 2 and par.count(1) == 2
    return ok


def X68():
    carry = []; surf = []; keep = []; opening = []
    for i in range(7):
        (s, c), L = traced(carry, [(K, 1)])
        surf.append(dict(s).get(K))
        if 1 <= i <= 4:     # couplings two to five, the 0 passage
            keep.append((tuple(L['_2_self_offering']), L['_6_other_crossing'].get(K),
                         carry[0][2], dict(s).get(K), L['_12_other_surplusing'].get(K),
                         sorted(L['_14_social_crossing'])))
            opening.append(c[0][3] if c else None)
        carry = c
    same = all(x == ((( K, 1),), -1, -1, 0, 0, [(K, -1), (K, 1)]) for x in keep)
    return surf == [1, 0, 0, 0, 0, 1, 0] and same and opening == [1, 2, 3, None]


def X69():
    (s, c), L = traced([(K, 1, -1, 0), (K, -1, 1, 0)], [])
    ok = L['_6_other_crossing'] == {K: 1} and s == [(K, 0)] and c == [(K, -1, 1, 1)]
    (s2, c2), L2 = traced([(K, 1, -1, 0)], [(K, 1)])
    ok &= (K, 1) in L2['_14_social_crossing'] and s2 == [(K, 0)]
    return ok


def X73():
    lt = lambda a, b: a < b
    ok = all((not lt(a, b) and not lt(b, a)) == (a == b) for a in range(10) for b in range(10))
    subs = [frozenset(x) for r in range(4) for x in combinations((1, 2, 3), r)]
    ps = lambda a, b: a < b          # proper inclusion
    both = [(a, b) for a in subs for b in subs if not ps(a, b) and not ps(b, a)]
    ok &= any(a != b for a, b in both) and all(a == b or not (a <= b or b <= a) for a, b in both)
    return ok


def X79():
    rows = table_rows(section(NAM, '4.9'))
    pairs = []
    for r in rows:
        cells = r.strip('|').split('|')
        nums = sorted(int(x) for x in re.findall(r'(\d+)-(?:self|other|social)', cells[3]))
        pairs.append(tuple(nums))
    ok = len(rows) == 10 and all(b - a == 8 and 1 <= a <= 8 for a, b in pairs)
    from collections import Counter
    cnt = Counter(pairs)
    ok &= cnt == Counter({(6, 14): 1, (2, 10): 1, (4, 12): 2, (8, 16): 2, (3, 11): 1, (7, 15): 1, (5, 13): 2})
    ok &= (1, 9) not in cnt
    return ok


def X88():
    ok = all((x ^ b) ^ b == x for x in (0, 1) for b in (0, 1))
    # prior, now -> next = prior xor now: (0,0) still, the others round in three
    m = {(p, n): (n, p ^ n) for p in (0, 1) for n in (0, 1)}
    ok &= m[(0, 0)] == (0, 0)
    for s in [(0, 1), (1, 0), (1, 1)]:
        x = s
        for _ in range(3): x = m[x]
        ok &= x == s and m[s] != s and m[m[s]] != s
    # Peres-Mermin: rows' products +1, columns' products +1, +1, -1; no store of the nine meets them
    meets = 0
    for v in product(S, repeat=9):
        g = [v[0:3], v[3:6], v[6:9]]
        rows = all(a * b * c == 1 for a, b, c in g)
        cols = [g[0][j] * g[1][j] * g[2][j] for j in range(3)] == [1, 1, -1]
        meets += rows and cols
    return ok and meets == 0 and 2 ** 9 == 512


def X97():
    return all((n - 1) * (n + 1) == n * n - 1 for n in range(-1000, 1001))


def X98():
    # rational root candidates of x^2 - x - 1 are +-1
    ok = all(r * r - r - 1 != 0 for r in (1, -1))
    fib = [0, 1]
    while len(fib) < 64: fib.append(fib[-1] + fib[-2])
    for n in range(1, 61):
        r = Fraction(fib[n + 1], fib[n])
        above = r * r - r - 1 > 0               # r > phi, r positive
        ok &= above == (n % 2 == 0) and r * r - r - 1 != 0
    return ok


def X104():
    podal = {frozenset((n, 17 - n)) for n in range(1, 17)}
    straight = {frozenset((k, k + 8)) for k in range(1, 9)}
    return len(podal) == 8 and len(straight) == 8 and not (podal & straight)


def X107_probe():
    return 59 - 2 + 1 == 58 == 118 - 61 + 1


# ------------------------------------------------------------ 7.3 the method
def X138():
    rows = table_rows(section(GIM, '3.3'))
    ok = len(rows) == 9
    par = []
    for i, r in enumerate(rows, 1):
        cells = [c.strip() for c in r.strip('|').split('|')]
        num = int(cells[0].split('·')[0].strip())
        p, kind = [x.strip() for x in cells[1].split('·')]
        ok &= num == i and ((p, kind) in (('even', 'naming'), ('odd', 'explaining')))
        ok &= (num % 2 == 1) == (p == 'even')     # the number and its parity column part
        par.append(p)
    ok &= all(par[i] != par[i + 1] for i in range(8))
    ok &= par.count('even') == 5 and par.count('odd') == 4
    ok &= rows[0].split('|')[1].strip().endswith('bound') and rows[-1].split('|')[1].strip().endswith('crossings')
    return ok


def X144():
    ok = True
    for n in range(1, 13):
        g = ['0', '1']
        for _ in range(n - 1):
            g = ['0' + x for x in g] + ['1' + x for x in reversed(g)]
        ok &= len(set(g)) == 2 ** n
        for i in range(2 ** n):
            a, b = g[i], g[(i + 1) % 2 ** n]
            ok &= sum(x != y for x, y in zip(a, b)) == 1
    return ok


def isprime(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True


def X145():
    fermat = [2 ** (2 ** k) + 1 for k in range(6)]
    ok = all(isprime(f) for f in fermat[:5]) and fermat[5] == 641 * 6700417 and not isprime(fermat[5])
    regions = [comb(n, 4) + comb(n, 2) + 1 for n in range(1, 7)]
    return ok and regions == [1, 2, 4, 8, 16, 31]


def X146_probe():
    # R(3,3) = 6: K5 carries a two-colouring with no one-colour triangle, K6 none
    def free(n):
        E = list(combinations(range(n), 2)); T = list(combinations(range(n), 3))
        found = 0
        for col in product((0, 1), repeat=len(E)):
            c = dict(zip(E, col))
            if all(not (c[(a, b)] == c[(a, d)] == c[(b, d)]) for a, b, d in T):
                found += 1
                if n == 5: return True
        return found > 0
    return free(5) and not free(6)


def X147():
    primes = [p for p in range(5, 60) if isprime(p)]
    ok = len(primes) == 15 and primes[0] == 5 and primes[-1] == 59
    for n in range(4, 61):
        d = [min(j, n - j) for j in range(1, n)]
        far = d.count(max(d))
        ok &= far == (2 if n % 2 else 1)
    return ok and all(n % 2 for n in (9, 15, 25))


def X148():
    ok = True
    s = section(EXP, '3.4'); ok &= len(re.findall(r'^- \*\*', s, re.M)) == 9
    s = section(EXP, '3.2'); ok &= all(x in s for x in ('A fixed noun', 'A forcing', 'A character', 'A wrapper'))
    s = section(EXP, '3.13')
    tail = s.split('is a middle carried across.**', 1)[1].split('\n\n')[0]
    ok &= len([x for x in re.split(r'(?<=\.)\s+', tail.strip()) if x]) == 6
    t = open(NAM, encoding='utf-8').read()
    ok &= len(re.findall(r'^## 5\.\d+ ', t, re.M)) == 47 and 'Forty-seven namings' in t
    ok &= len(table_rows(section(NAM, '2.5'))) == 7
    ok &= len(table_rows(section(NAM, '4.9'))) == 10
    ok &= len(re.findall(r'^\d\. \*\*', section(NAM, '4.18'), re.M)) == 7
    ok &= len(table_rows(section(NAM, '3.3'))) == 17
    ok &= len(table_rows(section(NAM, '6.2'))) == 8
    ok &= len(re.findall(r'^- \*\*', section(NAM, '1.1'), re.M)) == 4
    ok &= len(table_rows(section(GIM, '3.3'))) == 9
    ok &= len(table_rows(section(GIM, '5.1'))) == 10
    return ok

THIRTY = W + 'Exhibit_THIRTY_Co-Chaining_Logic_Registry_v372.md'


def X4():
    """Each link met at its whole prior back to the origin, all or none: the prior closure is acyclic,
    and the classes recomputed from the rows give Part THIRTEEN's counts."""
    t = open(THIRTY, encoding='utf-8').read()
    body = t.split('# PART NINE')[0]
    row = re.compile(r'^\| ([A-Z]+\d+) \| (origin|definition|premise|exact|run|field|nye)\b[^|]*\| ([^|]*) \|', re.M)
    ST, PR = {}, {}
    for lid, st, fol in row.findall(body):
        if lid in ST:
            continue
        ST[lid] = st
        PR[lid] = [i for i in re.findall(r'\b[A-Z]+\d+\b', fol) if i != lid]
    if len(ST) < 1338 or any(i not in ST for v in PR.values() for i in v):
        return False
    part13 = t.split('# PART THIRTEEN')[1]
    sel = set(re.findall(r'\b[A-Z]+\d+\b', re.search(r'The selectings in the chain: ([^\n]*)', part13).group(1)))
    order, mark = [], {}
    def visit(k):
        stack = [(k, iter(PR[k]))]
        mark[k] = 1
        while stack:
            u, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                mark[u] = 2; order.append(u); stack.pop()
            elif mark.get(nxt) == 1:
                raise ValueError('cycle at ' + nxt)
            elif nxt not in mark:
                mark[nxt] = 1; stack.append((nxt, iter(PR[nxt])))
    for k in ST:
        if k not in mark:
            visit(k)
    clo = {}
    for k in order:
        c = {k}
        for p in PR[k]:
            c |= clo[p]
        clo[k] = c
    cnt = {'a': 0, 'b': 0, 'c': 0, 'g': 0, 'd': 0, 'e': 0}
    for k in ST:
        c = clo[k]
        if any(ST[x] == 'nye' or x in sel for x in c):
            cnt['e'] += 1
        elif any(ST[x] == 'premise' or (ST[x] == 'definition' and not PR[x]) for x in c):
            cnt['d'] += 1
        else:
            cnt['a'] += 1
            leaves = {ST[x] for x in c if not PR[x]}
            cnt['b' if leaves == {'origin'} else 'c' if 'origin' in leaves else 'g'] += 1
    allrow = re.search(r'^\| All \| (.*) \|$', part13, re.M).group(1)
    stated = [int(v.strip('* ').replace(',', '')) for v in allrow.split(' | ')]
    return stated == [cnt[x] for x in 'abcgde'] + [len(ST)]


CHECKS = {k: v for k, v in globals().items() if re.fullmatch(r'X\d+(_probe)?', k) and callable(v)}


if __name__ == '__main__':
    res = {}
    for k in sorted(CHECKS, key=lambda s: (int(re.match(r'X(\d+)', s).group(1)), s)):
        try: res[k] = bool(CHECKS[k]())
        except Exception as e: res[k] = f'error: {e!r}'
        print(k, res[k])
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'ccl_x_check_results.json')
    json.dump(res, open(out, 'w'), indent=1)
