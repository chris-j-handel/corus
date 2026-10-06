"""Session v383Op: the network surface of Exhibit TWO, read at the torus of the resolver.

Runs from the repository root: python3 incoming/v383Op/network_surface.py     (about a minute)

The self's saying examined: "the at tori explaining is the natural network surface we have been
trying to understand in exhibit two ... the or nothing is the still possibling of both sides".

THE WIRING, said first as Exhibit TWO 6.2 asks of each run:
  engine      Exhibit ONE's 1-co-bi-tri-offering at the root, unchanged; the kit of Exhibit TWO runs an
              older code, and nothing here is that kit's.
  membrane    each self carries one parity at one sharing; each self releases to two, the next along and
              the next across, the last to the first: the torus of the Co-Chaining Logic Registry's step
              243. Both neighbours. The surface of Exhibit TWO is not said closed; this one is.
  pace/order  parts 1, 2 and 4: every self at one momentary with every other, the common beat the Registry's
              step 244 calls the executing's. Part 3: one self at a time, the order drawn.
  taking      part 3 states four, each at its column; two keep a waiting place at each coupling, a store
              Natural Networking 6.12 says the resolver does not supply; one keeps one sharing resting at
              a coupling and no more; the fourth lays no 0 there.
  record      a momentary is counted at each self as its own entries; where selves are stepped together
              the count is the beat's.
  refusing    none: no guard, no value excluded. Openings: each self at + or -; no carrying of none.

  1  The nothing at a coupling, each of 4,672 openings of three tori.
  2  The second momentary read off the opening, and the momentary from which the takings are one number.
  3  One self at a time at four takings, beside the beat: what the own turn needs to be the one beat.
  4  A self absent after a common prior: the missing section Exhibit TWO 6.12 calls its next
     executable subject, with signs flowing.
"""
import collections, glob, itertools, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']


def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]


def kind(c, offered):
    ps = [p for p in offered if p]
    if not ps:
        return 'R'                       # a releasing: nothing offered, its own inverted
    if len(set(ps)) > 1:
        return 'P'                       # parting offerings
    return '.' if ps[0] == c else 'T'    # still possibling, or a taking


def senders(p, q, s):
    i, j = s
    return ((i - 1) % p, j), (i, (j - 1) % q)          # the one releasing along to s, the one sharing across to s


def beat(p, q, c, last, absent=None):
    """One momentary of every self together. last[s] is what s shared at the momentary before."""
    kinds, shared = {}, {}
    new = dict(c)
    for s in c:
        if s == absent:
            continue
        two = [0 if u == absent else last.get(u, 0) for u in senders(p, q, s)]
        kinds[s] = kind(c[s], two)
        new[s], shared[s] = entry(c[s], two)
    return new, shared, kinds


TORI = ((2, 3), (3, 3), (3, 4))
print('1  The nothing at a coupling: tori of 2 by 3, 3 by 3 and 3 by 4, every opening, momentaries 2 to 60')
print('   (so by the cell: a self shares its changing, and nothing where its changing is not; counted, and no finding.')
print('   The counts by what the receiving self meets are those of incoming/v383Op/two_lines.py, its fifth part.)')
couplings = nothing = from_still = twice = selves_run = 0
met_at_nothing = collections.Counter()
second = [0, 0]
settle = collections.Counter()
for p, q in TORI:
    selves = [(i, j) for i in range(p) for j in range(q)]
    for op in itertools.product((1, -1), repeat=p * q):
        c = dict(zip(selves, op))
        last, prior_kinds, prior_shared = {}, None, None
        takings = []
        for t in range(1, 61):
            c_before = dict(c)
            c, shared, kinds = beat(p, q, c, last)
            takings.append(sum(1 for s in selves if kinds[s] == 'T'))
            if t == 2:
                both = sum(all(op[selves.index(s)] != op[selves.index(u)] for u in senders(p, q, s)) for s in selves)
                one = sum(len({op[selves.index(s)] != op[selves.index(u)] for u in senders(p, q, s)}) == 2 for s in selves)
                second[0] += 1
                second[1] += takings[-1] == both and sum(1 for s in selves if kinds[s] == 'P') == one
            if t >= 2:
                for s in selves:
                    for u in senders(p, q, s):
                        couplings += 1
                        if last[u] == 0:
                            nothing += 1
                            from_still += prior_kinds[u] == '.'
                            met_at_nothing[kinds[s]] += 1
                    twice += shared[s] == 0 and last[s] == 0
            last, prior_kinds = shared, kinds
        settle[next(i for i in range(60) if len(set(takings[i:])) == 1) + 1] += 1
names = {'T': 'a taking', '.': 'still possibling', 'R': 'a releasing', 'P': 'parting offerings'}
print('   couplings at a momentary: %d; carrying nothing: %d; of those, the releasing self still possibling at the momentary before: %d' % (
    couplings, nothing, from_still))
print('   at a side offering nothing the receiving self meets: %s' % ', '.join('%s %d' % (names[k], v) for k, v in sorted(met_at_nothing.items(), key=lambda x: -x[1])))
print('   a self sharing nothing at two momentaries in sequence: %d' % twice)

print()
print('2  The second momentary read off the opening, each of %d openings' % second[0])
print('   the takings are the selves parting from both sides at the opening, and the parting offerings those parting from one: %d' % second[1])
print('   the momentary from which the takings are one number to the sixtieth: %s' % ', '.join('%d: %d openings' % kv for kv in sorted(settle.items())))
print('   at a spiral that momentary is the second at every opening, incoming/v383Op/two_lines.py; at a torus the two')
print('   sides parting change the number until it settles.')


def receivers(p, q, s):
    i, j = s
    return ((i + 1) % p, j), (i, (j + 1) % q)


def one_at_a_time(p, q, opening, momentaries, taking, seed, absent=None):
    """One self at a time, the order drawn among those that can act.
    'one resting': at most one sharing rests at a coupling. A self takes when each side's is there, a parity or a 0,
                   and releases when each it releases to has taken its last. No queue and no round.
    'one resting, no 0': the same, a 0 not laid at the coupling: the nothing as an absence.
    'waiting, each': sharings wait in the order released; a self opens when one has come from each side.
    'waiting, any': the same waiting; a self opens at whatever has come."""
    r = random.Random(seed)
    selves = [(i, j) for i in range(p) for j in range(q) if (i, j) != absent]
    c = dict(opening)
    seq = {s: [] for s in selves}
    if taking.startswith('one resting'):
        lay_zero = taking == 'one resting'
        rest = {(u, s): None for s in selves for u in senders(p, q, s)}
        half = {s: 'take' for s in selves}
        held = {}
        while True:
            ready = []
            for s in selves:
                if half[s] == 'take':
                    if len(seq[s]) < momentaries and (not seq[s] or all(rest[(u, s)] is not None for u in senders(p, q, s))):
                        ready.append(s)
                elif all(rest.get((s, v)) is None for v in receivers(p, q, s)):
                    ready.append(s)
            if not ready:
                break
            s = r.choice(ready)
            if half[s] == 'take':
                offered = [rest[(u, s)] for u in senders(p, q, s)] if seq[s] else []
                if seq[s]:
                    for u in senders(p, q, s):
                        rest[(u, s)] = None
                c[s], o = entry(c[s], offered)
                seq[s].append((c[s], o))
                held[s], half[s] = o, 'release'
            else:
                for v in receivers(p, q, s):
                    if v != absent and (lay_zero or held[s] != 0):
                        rest[(s, v)] = held[s]
                half[s] = 'take'
        return seq
    waiting = {s: {u: [] for u in senders(p, q, s)} for s in selves}

    def can(s):
        if len(seq[s]) >= momentaries:
            return False
        if not seq[s]:
            return True
        ready = [bool(waiting[s][u]) for u in senders(p, q, s)]
        return all(ready) if taking == 'waiting, each' else any(ready)
    while True:
        ready = [s for s in selves if can(s)]
        if not ready:
            break
        s = r.choice(ready)
        if not seq[s]:
            offered = []
        elif taking == 'waiting, each':
            offered = [waiting[s][u].pop(0) for u in senders(p, q, s)]
        else:
            offered = [waiting[s][u].pop(0) for u in senders(p, q, s) if waiting[s][u]]
        c[s], o = entry(c[s], offered)
        seq[s].append((c[s], o))
        for to in receivers(p, q, s):
            if to != absent:
                waiting[to][s].append(o)
    return seq


TAKINGS = ('one resting', 'waiting, each', 'waiting, any', 'one resting, no 0')
print()
print('3  One self at a time, the order drawn, 40 of each self\'s own momentaries, beside the same opening stepped together.')
print('   Each cell: runs at which each self\'s own sequence is the beat\'s / runs at which each self reaches its fortieth momentary.')
print('   %-14s %6s   %-24s %-24s %-24s %s' % ('', 'runs', 'one sharing resting at a', 'sharings waiting; one', 'sharings waiting;', 'one resting, and a 0'))
print('   %-14s %6s   %-24s %-24s %-24s %s' % ('', '', 'coupling; taken at both', 'from each side taken', 'whatever has come', 'not laid: the nothing'))
print('   %-14s %6s   %-24s %-24s %-24s %s' % ('', '', 'sides, a 0 among them', '', '', 'as an absence'))
total = {t: [0, 0] for t in TAKINGS}
all_runs = 0
for p, q in ((2, 3), (3, 3), (3, 4), (3, 7), (5, 5)):
    selves = [(i, j) for i in range(p) for j in range(q)]
    r = random.Random(383)
    got_n = {t: [0, 0] for t in TAKINGS}
    runs = 0
    for trial in range(60):
        opening = {s: r.choice((1, -1)) for s in selves}
        c, last, ref = dict(opening), {}, {s: [] for s in selves}
        for _ in range(40):
            c, last, kinds = beat(p, q, c, last)
            for s in selves:
                ref[s].append((c[s], last[s]))
        for seed in (trial, 1000 + trial):
            runs += 1
            for t in TAKINGS:
                got = one_at_a_time(p, q, opening, 40, t, seed)
                got_n[t][0] += all(got[s] == ref[s] for s in selves)
                got_n[t][1] += all(len(got[s]) == 40 for s in selves)
    all_runs += runs
    for t in TAKINGS:
        total[t] = [a + b for a, b in zip(total[t], got_n[t])]
    print('   torus %d by %-3d %6d   %-24s %-24s %-24s %s' % (p, q, runs, *('%d / %d' % tuple(got_n[t]) for t in TAKINGS)))
print('   %-14s %6d   %-24s %-24s %-24s %s' % ('together', all_runs, *('%d / %d' % tuple(total[t]) for t in TAKINGS)))
print('   The second column is so by its construction, a result of the field\'s (Kahn, 1974), and it keeps a waiting place at')
print('   each coupling. The first keeps no waiting place past one sharing and no round; it has a self wait on both its sides.')

print()
print('4  A self absent after a common prior of 40 momentaries; 200 openings drawn at each torus; 60 momentaries on,')
print('   the same opening with the self present beside it. An absent self offers nothing and takes nothing.')
for p, q in ((3, 3), (4, 5), (5, 5), (7, 7)):
    selves = [(i, j) for i in range(p) for j in range(q)]
    hole = (p // 2, q // 2)
    present = [s for s in selves if s != hole]
    r = random.Random(383)
    same_all = most = longest = twice = 0
    differing_end = []
    reach = []
    below = [((hole[0] + 1) % p, hole[1]), (hole[0], (hole[1] + 1) % q)]      # the two the absent self released to
    below_kinds = collections.Counter()
    for trial in range(200):
        c = {s: r.choice((1, -1)) for s in selves}
        last = {}
        for _ in range(40):
            c, last, kinds = beat(p, q, c, last)
        a, la = dict(c), dict(last)
        b, lb = dict(c), dict(last)
        run_len = {s: 0 for s in present}
        ever = False
        here = 0
        for t in range(60):
            a, la_new, ka = beat(p, q, a, la)
            b, lb_new, kb = beat(p, q, b, lb, absent=hole)
            for s in present:
                run_len[s] = run_len[s] + 1 if kb[s] == '.' else 0
                longest = max(longest, run_len[s])
                twice += lb_new[s] == 0 and lb.get(s) == 0
            for s in below:
                below_kinds[kb[s]] += 1
            la, lb = la_new, lb_new
            d = sum(a[s] != b[s] for s in present)
            ever = ever or d > 0
            most = max(most, d)
            here = max(here, d)
        reach.append(here)
        same_all += not ever
        differing_end.append(sum(a[s] != b[s] for s in present))
    print('   torus %d by %d, %d selves present:' % (p, q, len(present)))
    print('      openings at which no present self ever carries otherwise than with the self present: %d of 200' % same_all)
    reached = sorted(x for x in reach if x)
    print('      at the other %d, the most present selves carrying otherwise at one momentary: least %d, middle %d, most %d of %d' % (
        len(reached), reached[0], reached[len(reached) // 2], reached[-1], len(present)))
    print('      a present self still possibling, most momentaries in sequence: %d; sharing nothing twice in sequence: %d' % (longest, twice))
    stalled = 0
    r2 = random.Random(383)
    for trial in range(40):
        opening = {s: r2.choice((1, -1)) for s in selves if s != hole}
        got = one_at_a_time(p, q, opening, 40, 'one resting', trial, absent=hole)
        stalled += not all(len(v) == 40 for v in got.values())
    print('      the same absence with one self at a time, one sharing resting, taken at both sides: runs at which a present self')
    print('      never reaches its fortieth momentary, waiting on the absent side: %d of 40' % stalled)
print('   At the beat an absent side is met as a nothing at each momentary, which is this instrument laying a 0 where nothing')
print('   is. A present self shares nothing at no two momentaries in sequence; the Registry\'s step 611 says two at most at a torus.')
