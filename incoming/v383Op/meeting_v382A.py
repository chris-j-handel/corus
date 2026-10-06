"""Session v383Op, meeting the logic working v382A's passes 56 to 59 at Exhibit ONE's resolver.

Runs from the repository root: python3 incoming/v383Op/meeting_v382A.py     (about two minutes)
Reads the newest Exhibit ONE at the root and executes its python block. Parts 1, 2 and 5 call
Exhibit ONE's own 1-co-bi-tri-offering, unchanged. Parts 3 and 4 count every rule of a kind and
say how many each sentence leaves; the cell of part 4 is checked against Exhibit ONE's at each input.

v382A read the published forms as text and executed nothing; it says so. This is the other half:
the same tables and sentences, executed. An executing says what the published form does at the
societies and openings run; it establishes no wider thing by being run.

  1  v382A's tables, incoming/v382A/Meeting_v383Op.md and Health_Biology_Medicine.md, row by row.
  2  Whose prior the next inverts: with one other releasing to a self, and with two.
  3  The offerings at one sharing: every rule from up to four offerings to a parity or 0.
  4  The cell: every cell at two parities with neither parity named over the other, 1,296.
  5  No self still: the most entries in sequence a self carries one parity, beside how many
     release to it; stepped together, and each self entered in an order drawn.

What this instrument carries of its own, to be read with each number:
  - the societies run are small: two selves, spirals of 1 to 7, tori to 3 by 4, two spirals crossed,
    two lone selves releasing to a third, and joins drawn among 5 to 8 selves; each self carries a
    parity, and no non-living other, a carrying of none, is run;
  - windows: part 2 reads entries 3 to 40 of each opening; part 4 reads the living step at entries
    3 to 20 and calls a self still when it is at one parity through the last 31 of 60 entries, at
    512 openings at most; part 5 runs 40 openings of each society;
  - the stepping of parts 2 and 4 is Exhibit ONE's 17, each self at one momentary with each other;
  - part 3's three sentences and part 4's three are this session's choosing among the files' own;
    each count is given alone and together so that the choosing can be seen.
"""
import glob, itertools, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
SIGN = {1: '+', -1: '-', 0: '0', None: 'none'}


def entry(c, offered):
    """One self at one sharing: its carrying c, the parities offered. Returns its carrying chained and its changing shared."""
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]


def ring(n):
    return list(range(n)), {j: [(j + 1) % n] for j in range(n)}


def both_ways():
    return [0, 1], {0: [1], 1: [0]}


def torus(p, q):
    selves = [(i, j) for i in range(p) for j in range(q)]
    return selves, {(i, j): [((i + 1) % p, j), (i, (j + 1) % q)] for i, j in selves}


def crossed(p, q):
    selves = [('P', i) for i in range(p)] + [('Q', i) for i in range(q)]
    joins = {('P', i): [('P', (i + 1) % p)] for i in range(p)}
    joins.update({('Q', i): [('Q', (i + 1) % q)] for i in range(q)})
    joins[('P', 0)].append(('Q', 0))
    joins[('Q', 0)].append(('P', 0))
    return selves, joins


def fed():
    """Two lone selves, each releasing to a third and receiving from none."""
    return ['a', 'b', 's'], {'a': ['s'], 'b': ['s'], 's': []}


def together(step, selves, joins, opening, T):
    """Exhibit ONE's stepping: each self at one momentary with each other. C[s][t] is s's carrying chained at momentary t."""
    c = dict(opening)
    arriving = {s: [] for s in selves}
    C = {s: [c[s]] for s in selves}
    for _ in range(T):
        nxt = {s: [] for s in selves}
        for s in selves:
            c[s], o = step(c[s], arriving[s])
            C[s].append(c[s])
            for to in joins[s]:
                nxt[to].append(o)
        arriving = nxt
    return C


def openings(selves, cap=None, seed=0):
    ops = list(itertools.product((1, -1), repeat=len(selves)))
    if cap and len(ops) > cap:
        ops = random.Random(seed).sample(ops, cap)
    return [dict(zip(selves, op)) for op in ops]


# ---------------------------------------------------------------------------------------------
print('1  v382A\'s tables, executed at Exhibit ONE\'s 1-co-bi-tri-offering')
print()
print('   the local table of pass 57: carrying, offerings surfaced, changing shared, carrying chained')
rows = [(1, [1], 0, 1), (1, [-1], -1, -1), (1, [1, -1], -1, -1), (1, [], -1, -1),
        (-1, [-1], 0, -1), (-1, [1], 1, 1), (-1, [1, -1], 1, 1), (-1, [], 1, 1)]
agree = 0
for c, offered, shared_said, chained_said in rows:
    chained, shared = entry(c, offered)
    ok = (chained, shared) == (chained_said, shared_said)
    agree += ok
    print('     carrying %s  offered %-8s  shared %-2s chained %s   %s' % (
        SIGN[c], ','.join(SIGN[p] for p in offered) or 'none', SIGN[shared], SIGN[chained], 'as said' if ok else 'NOT as said'))
print('   rows as v382A read them: %d of %d' % (agree, len(rows)))
print()
print('   all or none beside the sign of a sum, pass 58, and a 0 offered alone, pass 57')
for offered, surfacing_said in (([1, 1], 1), ([1, -1], 0), ([1, 1, -1], 0), ([-1, -1, 1], 0)):
    # a carrying of none passes one parity on as it is, and shares nothing at parting: the surfacing read directly
    shared, chained = _1([], [('k', p) for p in offered])
    got = dict(shared).get('k', 0)
    s = sum(offered)
    print('     offered %-8s  surfaced %-2s (said %-2s)   the sign of the sum would be %s' % (
        ','.join(SIGN[p] for p in offered), SIGN[got], SIGN[surfacing_said], SIGN[(s > 0) - (s < 0)]))
for c in (1, -1):
    c1, s1 = entry(c, [0])
    c2, s2 = entry(c, [])
    print('     carrying %s, a 0 offered alone: shared %s chained %s; nothing offered: shared %s chained %s; the same: %s' % (
        SIGN[c], SIGN[s1], SIGN[c1], SIGN[s2], SIGN[c2], (c1, s1) == (c2, s2)))
print()
print('   the five-parity rows of pass 56, two selves coupled both ways, none offered from beyond the two:')
print('   at each of the four openings, each entry from the third: is the self\'s next the other\'s prior inverted, also where its own now is kept')
n_all = n_other = n_match = n_match_kept = 0
for op in openings([0, 1]):
    C = together(entry, *both_ways(), op, 40)
    for s, u in ((0, 1), (1, 0)):
        for t in range(2, 40):
            n_all += 1
            n_other += C[s][t + 1] == -C[u][t - 1]
            if C[s][t + 1] == C[s][t]:
                n_match += 1
                n_match_kept += C[s][t + 1] == -C[u][t - 1]
print('     next the other\'s prior inverted: %d of %d entries; entries where its own now is kept: %d, and of those the other\'s prior inverted: %d' % (
    n_other, n_all, n_match, n_match_kept))

# ---------------------------------------------------------------------------------------------
print()
print('2  Whose prior the next inverts')
print()
print('   one other releasing to each self, every opening, each entry from the third, stepped together')
print('   (two selves coupled both ways are the spiral of 2)')
print('   %-22s %9s %9s %28s %24s %22s' % ('', 'openings', 'entries', 'the other\'s prior inverted', 'its own prior inverted', 'its own now inverted'))
for name, (selves, joins) in [('spiral of %d' % n, ring(n)) for n in range(1, 8)]:
    senders = {s: [u for u in selves if s in joins[u]][0] for s in selves}
    tot = oth = own = now = 0
    for op in openings(selves):
        C = together(entry, selves, joins, op, 40)
        for s in selves:
            for t in range(2, 40):
                tot += 1
                oth += C[s][t + 1] == -C[senders[s]][t - 1]
                own += C[s][t + 1] == -C[s][t - 1]
                now += C[s][t + 1] == -C[s][t]
    print('   %-22s %9d %9d %28d %24d %22d' % (name, 2 ** len(selves), tot, oth, own, now))


def drawn_joins(n, seed, most=3):
    r = random.Random(seed)
    selves = list(range(n))
    return selves, {s: r.sample([u for u in selves if u != s], r.randint(1, min(most, n - 1))) for s in selves}


tot = oth = soc = 0
for n in (5, 6, 7, 8):
    for seed in range(30):
        selves, joins = drawn_joins(n, seed)
        senders = {s: [u for u in selves if s in joins[u]] for s in selves}
        ones = [s for s in selves if len(senders[s]) == 1]
        soc += bool(ones)
        for op in openings(selves, 32, seed):
            C = together(entry, selves, joins, op, 40)
            for s in ones:
                for t in range(2, 40):
                    tot += 1
                    oth += C[s][t + 1] == -C[senders[s][0]][t - 1]
print('   joins drawn among 5 to 8 selves, %d societies, the selves one other releases to, 32 openings each:' % soc)
print('   %-22s %9s %9d %28d' % ('', '', tot, oth))
print()
print('   what a self\'s next is a way of: the forms met, and how many of them are met at both nexts')
print('   (the last column is the cell as it is written, and is at both at none by that; the first three are what is run)')
print('   %-22s %-28s %-28s %-34s %s' % ('', 'the others\' priors', 'their priors, its own now', 'their priors, its now and prior', 'their priors and nows, its own now'))
for name, (selves, joins), T, cap in (('spiral of 2', ring(2), 24, None), ('spiral of 5', ring(5), 24, None),
                                       ('torus 2 by 3', torus(2, 3), 24, None), ('torus 3 by 3', torus(3, 3), 24, None),
                                       ('torus 3 by 4', torus(3, 4), 16, None), ('spirals of 3 and 4 crossed', crossed(3, 4), 24, None)):
    senders = {s: [u for u in selves if s in joins[u]] for s in selves}
    seen = [{}, {}, {}, {}]
    for op in openings(selves, cap):
        C = together(entry, selves, joins, op, T)
        for s in selves:
            for t in range(2, T):
                pr = tuple(sorted(C[u][t - 1] for u in senders[s]))
                pn = tuple(sorted((C[u][t - 1], C[u][t]) for u in senders[s]))
                for d, key in zip(seen, (pr, (pr, C[s][t]), (pr, C[s][t], C[s][t - 1]), (pn, C[s][t]))):
                    d.setdefault((len(senders[s]), key), set()).add(C[s][t + 1])
    cells = ['%d forms, %d at both' % (len(d), sum(len(v) > 1 for v in d.values())) for d in seen]
    print('   %-22s %-28s %-28s %-34s %s' % (name[:22], *cells))

# ---------------------------------------------------------------------------------------------
print()
print('3  The offerings at one sharing: every rule from one to four offerings, each + or -, to +, - or 0')
print('   A rule here is of the offerings and names no offerer; a rule of who offers is a selecting, and is not counted.')
shapes = [(a, b) for n in range(1, 5) for a in range(n + 1) for b in [n - a]]
ix = {ab: i for i, ab in enumerate(shapes)}
same_parities = [(ix[x], ix[y]) for x in shapes for y in shapes if x < y and (x[0] > 0) == (y[0] > 0) and (x[1] > 0) == (y[1] > 0)]
mirror = [(ix[(a, b)], ix[(b, a)]) for a, b in shapes if (a, b) <= (b, a)]
i_plus, i_minus = ix[(1, 0)], ix[(0, 1)]
VALUES = (1, -1, 0)
counts = {k: 0 for k in ('all', 'T', 'B', 'N', 'TB', 'TN', 'BN', 'TBN')}
left = []
for f in itertools.product(VALUES, repeat=len(shapes)):
    t = all(f[i] == f[j] for i, j in same_parities)         # no total: one more of a parity already offered changes nothing
    b = f[i_plus] == 1 and f[i_minus] == -1                  # the between a nothing: one offering alone arrives as it is
    n = all(f[i] == -f[j] for i, j in mirror)                # neither parity named over the other
    counts['all'] += 1
    counts['T'] += t; counts['B'] += b; counts['N'] += n
    counts['TB'] += t and b; counts['TN'] += t and n; counts['BN'] += b and n
    if t and b and n:
        counts['TBN'] += 1
        left.append(f)
print('   rules: %d' % counts['all'])
print('   no total, one more of a parity already offered changing nothing:      %d' % counts['T'])
print('   the between a nothing, one offering alone arriving as it is:           %d' % counts['B'])
print('   neither parity named over the other:                                   %d' % counts['N'])
print('   no total and the between a nothing: %d;  no total and neither named: %d;  the between and neither named: %d' % (
    counts['TB'], counts['TN'], counts['BN']))
print('   the three together: %d' % counts['TBN'])
for f in left:
    is_files = all(f[ix[(a, b)]] == (1 if b == 0 else -1 if a == 0 else 0) for a, b in shapes)
    print('     what is left: agreeing, that parity; parting, 0: %s' % ('Exhibit ONE\'s surfacing' if is_files else 'another'))

# ---------------------------------------------------------------------------------------------
print()
print('4  The cell: a carrying of + meeting a match, a mismatch, parting offerings or none; its carrying next, kept or inverted,')
print('   and what it shares, +, - or 0; a carrying of - the same with each parity inverted. Cells: 6 * 6 * 6 * 6.')
KINDS = ('match', 'mismatch', 'parting', 'none')
OUT = [(k, o) for k in (1, -1) for o in (1, -1, 0)]
FILES = {'match': (1, 0), 'mismatch': (-1, -1), 'parting': (-1, -1), 'none': (-1, -1)}


def cell(rule):
    def step(c, offered):
        ps = [p for p in offered if p != 0]
        kind = 'none' if not ps else 'parting' if len(set(ps)) > 1 else 'match' if ps[0] == c else 'mismatch'
        k, o = rule[kind]
        return c * k, c * o
    return step


same = all(cell(FILES)(c, list(off)) == entry(c, list(off))
           for c in (1, -1) for n in range(0, 4) for off in itertools.product((1, -1, 0), repeat=n))
print('   the cell written here as Exhibit ONE\'s, at each carrying and each offering of none to three: the same as Exhibit ONE\'s: %s' % same)


def living_step_at_one_other(rule, T=20):
    step = cell(rule)
    for n in (2, 3, 4, 5):
        selves, joins = ring(n)
        for op in openings(selves):
            C = together(step, selves, joins, op, T)
            for s in selves:
                u = (s - 1) % n
                if any(C[s][t + 1] != -C[u][t - 1] for t in range(2, T)):
                    return False
    return True


def a_sharing_is_a_changing(rule):
    return all((k == 1 and o == 0) or (k == -1 and o == -1) for k, o in rule.values())


STILL_AT = [('torus 3 by 3', torus(3, 3)), ('torus 2 by 3', torus(2, 3)), ('two lone selves releasing to a third', fed()),
            ('spirals of 3 and 4 crossed', crossed(3, 4)), ('spirals of 2 and 3 crossed', crossed(2, 3))]


def a_self_still(rule, selves, joins, T=60):
    step = cell(rule)
    for op in openings(selves, 512):
        C = together(step, selves, joins, op, T)
        if any(len(set(C[s][T // 2:])) == 1 for s in selves):
            return True
    return False


rules = [dict(zip(KINDS, combo)) for combo in itertools.product(OUT, repeat=4)]
L = [r for r in rules if living_step_at_one_other(r)]
S = [r for r in rules if a_sharing_is_a_changing(r)]
print('   cells: %d' % len(rules))
print('   the living step at one other, the next the other\'s prior inverted, spirals of 2 to 5, every opening: %d' % len(L))
print('   a sharing a changing shared, the new parity where the carrying changed and 0 where it did not:       %d' % len(S))
LS = [r for r in L if r in S]
print('   both: %d' % len(LS))
for r in LS:
    print('     %s%s' % (', '.join('%s: %s, shares %s' % (k, 'kept' if r[k][0] == 1 else 'inverted', SIGN[r[k][1]]) for k in KINDS),
                        '   <- Exhibit ONE\'s' if r == FILES else ''))
left = L
print('   the living step at one other, and no self at one parity from some momentary on:')
for name, (selves, joins) in STILL_AT:
    left = [r for r in left if not a_self_still(r, selves, joins)]
    print('     at %-38s %3d left, Exhibit ONE\'s among them: %s' % (name + ':', len(left), FILES in left))
classes = {}
for r in left:
    key = []
    for selves, joins in (ring(1), ring(2), ring(3), torus(2, 3), torus(3, 3), fed()):
        for op in openings(selves, 64):
            C = together(cell(r), selves, joins, op, 16)
            key.append(tuple(tuple(C[s]) for s in selves))
    classes.setdefault(tuple(key), []).append(r)
print('     those %d cells differ in what a self carries, at these societies, as %d' % (len(left), len(classes)))
final = [r for r in left if r in S]
print('   the three together: %d%s' % (len(final), ', Exhibit ONE\'s' if final == [FILES] else ''))
by_size = sorted(STILL_AT, key=lambda x: len(x[1][0]))
N = [r for r in rules if not any(a_self_still(r, selves, joins) for name, (selves, joins) in by_size)]
print('   each alone and each two: the living step %d; a sharing a changing shared %d; no self still at the five %d;' % (len(L), len(S), len(N)))
print('     the living step and the sharing %d; the living step and no self still %d; the sharing and no self still %d' % (
    len(LS), len([r for r in L if r in N]), len([r for r in S if r in N])))
for r in LS:
    if r != FILES:
        at = [name for name, (selves, joins) in STILL_AT if a_self_still(r, selves, joins)]
        print('   the other of the two, a carrying kept at parting offerings, leaves a self still at: %s' % '; '.join(at))
print('   Exhibit ONE\'s cell leaves a self still at: %s' % ('; '.join(
    name for name, (selves, joins) in STILL_AT if a_self_still(FILES, selves, joins)) or 'none of the five'))

# ---------------------------------------------------------------------------------------------
print()
print('5  No self still: the most entries in sequence a self carries one parity, beside how many release to it')
print('   The reason, at the cell: a self shares its new parity where it changed and 0 where it did not, so the parities one')
print('   self shares, in sequence, are +, -, +, -. A self kept at c is offered c, and no -c, at that entry. Each other can')
print('   offer c once; the next parity it shares is -c. So a self with k others releasing to it is kept at most k entries in')
print('   sequence. It leans on: nothing waiting at the opening; nothing offered from beyond the k; each sharing taken once,')
print('   in the order released, at the next entry of the self it is released to. With offerings laid waiting it does not hold.')


def longest_runs(selves, joins, opening, entries, order, seed):
    r = random.Random(seed)
    c = dict(opening)
    waiting = {s: [] for s in selves}
    run = {s: 1 for s in selves}
    most = {s: 1 for s in selves}
    for i in range(entries):
        batch = selves if order == 'together' else [r.choice(selves)]
        released = []
        for s in batch:
            offered, waiting[s] = waiting[s], []
            new, o = entry(c[s], offered)
            run[s] = run[s] + 1 if new == c[s] else 1
            most[s] = max(most[s], run[s])
            c[s] = new
            released.append((s, o))
        for s, o in released:
            for to in joins[s]:
                waiting[to].append(o)
    return most


def drawn(n, seed):
    r = random.Random(seed)
    selves = list(range(n))
    joins = {s: r.sample([u for u in selves if u != s], r.randint(1, min(4, n - 1))) for s in selves}
    return selves, joins


societies = [('spiral of 5', ring(5)), ('torus 3 by 3', torus(3, 3)), ('torus 3 by 4', torus(3, 4)), ('spirals of 3 and 4 crossed', crossed(3, 4))]
societies += [('joins drawn among %d' % n, drawn(n, seed)) for n in (5, 6, 7, 8) for seed in range(6)]
for order in ('together', 'each self entered in an order drawn'):
    by_k = {}
    over = 0
    for name, (selves, joins) in societies:
        k = {s: sum(s in joins[u] for u in selves) for s in selves}
        for i, op in enumerate(openings(selves, 40, seed=1)):
            most = longest_runs(selves, joins, op, 300 if order == 'together' else 300 * len(selves), order, i)
            for s in selves:
                by_k[k[s]] = max(by_k.get(k[s], 0), most[s])
                over += most[s] > k[s] + 1
    print('   %s:' % order)
    print('     others releasing to a self:            ' + '  '.join('%3d' % k for k in sorted(by_k)))
    print('     most entries in sequence at one parity: ' + '  '.join('%3d' % by_k[k] for k in sorted(by_k)))
    print('     selves past k entries kept, k + 1 at one parity: %d' % over)
