"""Two me-parities on a surface of the neither, executed with the twelve nand lines alone.

The cell is the now-and-same-existing-me-parity as v407nanding's page has it, written here again, its lines not altered.
A surface is cells coupled as the sessions lay it: what a me lays goes to each self its couplings reach.
An opening: two me-parities, A and B, and each other self the neither.

Part T steps all selves together, as Exhibit ONE's 17-next-existing does.
Part N has no stepping together, by a wiring that waits for none: one self at a time, drawn, resolving with
whatever has arrived. v406Reiman's page had this wiring parting from stepping together already; laid here as the
misunderstanding it was.
Part O has no stepping together, a self on its own beat: a self resolves once all couplings into it have an arrival,
with the oldest of each, and a laying of the neither is an arrival as well. No self counts a moment of an other.
Part C is the surface of n is-or-is-nots, a place a self, a coupling one is-or-is-not other.
Part L has all selves living from the opening, no self the neither, by a partner's saying of 26 November:
one me's opening prior is laid again as its other-than, and all selves' own moments are set beside what they were.

Part B has a partner's saying of 26 November of a birth: with a + and a - together a self with no prior is born as one
of the two, which one not observable. Not observable is executed as drawn. The twelve lines are not altered: the one
accepted is what the lines observe.
Part A is a session's own exploring of that saying at all selves, living ones as well: with a + and a - together a self
accepts one offerer, which one not observable. It is no partner's sentence.
In parts B and A a surface is executed twice with the same draws, so that what parts is of the mes and not of the draws.

A line ends is or is-not. A line ending sized gives numbers alone. It opens no file and writes no file.

    python3 -I incoming/v409pvnp/instruments/two_me_parities_on_a_surface_of_the_neither.py .
"""
import collections, random

NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}
def not_both(one, other): return NOT_BOTH[(one, other)]
def other_than(one): return not_both(one, one)
def both(one, other): return other_than(not_both(one, other))
def either(one, other): return not_both(other_than(one), other_than(other))

def now_and_same_existing_me_parity(me_prior, others_now_other_than_their_prior):
    an_other_now_is_plus = an_other_now_is_minus = False
    for this_plus, this_minus in others_now_other_than_their_prior:
        an_other_now_is_plus = either(an_other_now_is_plus, this_plus)
        an_other_now_is_minus = either(an_other_now_is_minus, this_minus)
    surfacing_is_plus = both(an_other_now_is_plus, other_than(an_other_now_is_minus))
    surfacing_is_minus = both(an_other_now_is_minus, other_than(an_other_now_is_plus))
    me_prior_is_plus, me_prior_is_minus = me_prior
    me_prior_is_none = both(other_than(me_prior_is_plus), other_than(me_prior_is_minus))
    lays_plus = either(both(me_prior_is_none, surfacing_is_plus), both(me_prior_is_minus, other_than(surfacing_is_minus)))
    lays_minus = either(both(me_prior_is_none, surfacing_is_minus), both(me_prior_is_plus, other_than(surfacing_is_plus)))
    me_now_is_plus = either(lays_plus, both(me_prior_is_plus, surfacing_is_plus))
    me_now_is_minus = either(lays_minus, both(me_prior_is_minus, surfacing_is_minus))
    return (lays_plus, lays_minus), (me_now_is_plus, me_now_is_minus)

PLUS, MINUS, NEITHER = (True, False), (False, True), (False, False)
out = []
def say(text, ok): out.append((("is" if ok else "is-not") if isinstance(ok, bool) else ok, text))

def a_round(n): return {i: [(i + 1) % n, (i - 1) % n] for i in range(n)}
def a_closing_surface(W, L):
    """Rows bi-coupling both ways across, columns co-chaining along, both closing: v406networking's closing surface."""
    return {(x, y): [((x + 1) % W, y), ((x - 1) % W, y), (x, (y + 1) % L)] for x in range(W) for y in range(L)}
def is_or_is_nots(n): return {p: [p ^ (1 << i) for i in range(n)] for p in range(1 << n)}

def fewest_couplings(outs, src):
    d = {src: 0}; q = collections.deque([src])
    while q:
        s = q.popleft()
        for t in outs[s]:
            if t not in d: d[t] = d[s] + 1; q.append(t)
    return d

def together(outs, opening, moments):
    state = {s: opening.get(s, NEITHER) for s in outs}
    obs = {s: [] for s in outs}
    seq = {s: [state[s]] for s in outs}
    born = {s: (0, []) for s in opening}
    of = {s: {s} for s in opening}
    touch = None
    for t in range(1, moments + 1):
        arriving = {s: [] for s in outs}
        for s in outs:
            was = state[s]
            froms = [frm for frm, g in obs[s] if g != NEITHER]
            lays, state[s] = now_and_same_existing_me_parity(was, [g for _, g in obs[s]])
            if touch is None and len(set().union(of.get(s, set()), *[of[f] for f in froms])) > 1:
                touch = t
            if was == NEITHER and state[s] != NEITHER:
                born[s] = (t, froms); of[s] = set().union(*[of[f] for f in froms])
            for to in outs[s]: arriving[to].append((s, lays))
        obs = arriving
        for s in outs: seq[s].append(state[s])
        if touch == t: touch = (t, sum(1 for x in outs if state[x] != NEITHER))   # the selves born with that moment whole
    return seq, born, touch

def no_clock(outs, opening, resolvings, rng):
    state = {s: opening.get(s, NEITHER) for s in outs}
    inbox = {s: collections.defaultdict(collections.deque) for s in outs}
    back = {}; selves = list(outs)
    for _ in range(resolvings):
        s = rng.choice(selves)
        got = [(frm, q.popleft()) for frm, q in inbox[s].items() if q]
        if state[s] == NEITHER and not got: continue
        was = state[s]
        lays, state[s] = now_and_same_existing_me_parity(was, [g for _, g in got])
        if was == NEITHER and state[s] != NEITHER: back[s] = got[0][0]
        if lays != NEITHER:
            for to in outs[s]: inbox[to][s].append(lays)
    return state, back

LAYINGS = [("a round of 20", a_round(20), 0, 7), ("a round of 21", a_round(21), 0, 8),
           ("a closing surface 9 by 7", a_closing_surface(9, 7), (1, 1), (5, 4)),
           ("a closing surface 12 by 10", a_closing_surface(12, 10), (0, 0), (5, 6)),
           ("8 is-or-is-nots, 8 between", is_or_is_nots(8), 0, 255), ("8 is-or-is-nots, 4 between", is_or_is_nots(8), 0, 15),
           ("9 is-or-is-nots, 5 between", is_or_is_nots(9), 0, 31)]

# ---- Part T
t1 = t2 = t3 = t4 = t5 = t6 = True; kept = 0; same_all = 0
for label, outs, A, B in LAYINGS:
    dA, dB = fewest_couplings(outs, A), fewest_couplings(outs, B)
    others = [s for s in outs if s not in (A, B)]
    same = [s for s in others if dA[s] == dB[s]]
    for pa, pb in ((PLUS, PLUS), (PLUS, MINUS)):
        seq, born, _ = together(outs, {A: pa, B: pb}, 120)
        seqA, _, _ = together(outs, {A: pa}, 120)
        seqB, _, _ = together(outs, {B: pb}, 120)
        t1 &= all(born[s][0] == min(dA[s], dB[s]) + 1 for s in others if dA[s] != dB[s])
        unborn = [s for s in outs if s not in born]
        if pa == pb: t3 &= not unborn
        else:
            t2 &= all(dA[s] == dB[s] for s in unborn); kept += len(unborn); same_all += len(same)
            if dA[B] % 2 == 0 and dA[B] == dB[A]:
                t6 &= any(dA[s] + dB[s] == dA[B] for s in unborn)
        t4 &= seq[A] == seqA[A] and seq[B] == seqB[B]
        t5 &= all(seq[s] == (seqA if dA[s] < dB[s] else seqB)[s] for s in others if dA[s] != dB[s])
say("T1 stepping together, a self is born a moment after its fewest couplings from the nearer me: seven layings, two openings", t1)
say("T2 with two mes unlike, a self never born has the same couplings from both, a + and a - reaching it together", t2)
say(f"   of the selves with the same couplings from both, {kept} of {same_all} are never born", "sized")
say("T3 with two mes alike, all selves are born", t3)
say("T4 a me's own moments, with an other me on the surface, are its moments alone", t4)
say("T5 all selves nearer one me have their moments with that me alone", t5)
say("T6 with an even number of couplings between two mes unlike, a self never born is on a path of fewest couplings between them", t6)

# ---- Part N
rng = random.Random(17)
n1 = True; n2 = True; n3 = True; longer = total = 0; betweens = []
for label, outs, A, B in LAYINGS[1:5:1]:
    dA, dB = fewest_couplings(outs, A), fewest_couplings(outs, B)
    for pa, pb in ((PLUS, PLUS), (PLUS, MINUS)):
        seen = []
        for order in range(7):
            state, back = no_clock(outs, {A: pa, B: pb}, 400 * len(outs), rng)
            unborn = frozenset(s for s in outs if state[s] == NEITHER)
            seen.append(unborn)
            if pa == pb: n1 &= not unborn
            for s in back:
                k, x = 0, s
                while x not in (A, B): x = back[x]; k += 1
                total += 1; longer += k > min(dA[s], dB[s])
        if pa != pb:
            n2 &= len(set(seen)) == 1; betweens.append((label, [len(u) for u in seen]))
n3 = longer == 0
say("N1 waiting for none, two mes alike, all selves are born: seven orders", n1)
say("N2 waiting for none, two mes unlike, the selves never born are the same in all orders", n2)
for label, counts in betweens: say(f"   {label}: never born, an order apiece, {counts}", "sized")
say("N3 waiting for none, all births are by a chain of fewest couplings back to a me", n3)
say(f"   births by a longer chain: {longer} of {total}", "sized")

# ---- Part O
def own_beat(outs, opening, resolvings_each, rng, weights):
    ins = {s: [] for s in outs}
    for frm, tos in outs.items():
        for to in tos: ins[to].append(frm)
    arrived = {(frm, to): collections.deque([NEITHER]) for frm, tos in outs.items() for to in tos}   # opening: none observed
    state = {s: opening.get(s, NEITHER) for s in outs}
    seq = {s: [state[s]] for s in outs}; done = {s: 0 for s in outs}; back = {}
    selves = list(outs); short = len(selves)
    while short:
        s = rng.choices(selves, weights)[0]
        if any(not arrived[(frm, s)] for frm in ins[s]): continue
        got = [(frm, arrived[(frm, s)].popleft()) for frm in ins[s]]
        was = state[s]
        lays, state[s] = now_and_same_existing_me_parity(was, [g for _, g in got])
        if was == NEITHER and state[s] != NEITHER: back[s] = [frm for frm, g in got if g != NEITHER][0]
        for to in outs[s]: arrived[(s, to)].append(lays)
        done[s] += 1; seq[s].append(state[s])
        if done[s] == resolvings_each: short -= 1
    return seq, back

o1 = o2 = o3 = True; orders = 0
for label, outs, A, B in LAYINGS[:6]:
    dA, dB = fewest_couplings(outs, A), fewest_couplings(outs, B)
    K = max(max(dA.values()), max(dB.values())) + 6
    for pa, pb in ((PLUS, PLUS), (PLUS, MINUS)):
        seq_t, born_t, _ = together(outs, {A: pa, B: pb}, K)
        never_t = {s for s in outs if s not in born_t}
        for order in range(5):
            # beats far from even: a self drawn up to forty times as often as an other
            weights = [rng.choice((1, 1, 3, 10, 40)) for _ in outs]
            seq, back = own_beat(outs, {A: pa, B: pb}, K, rng, weights)
            orders += 1
            o1 &= all(seq[s][:K + 1] == seq_t[s][:K + 1] for s in outs)
            o2 &= {s for s in outs if seq[s][K] == NEITHER} == never_t
            for s in back:
                k, x = 0, s
                while x not in (A, B): x = back[x]; k += 1
                o3 &= k == min(dA[s], dB[s])
say(f"O1 a self on its own beat has, resolving by resolving, its moments of stepping together: six layings, two openings, {orders} orders of beats far from even", o1)
say("O2 on its own beat, two mes unlike, the selves never born are the same in all orders, the between of stepping together", o2)
say("O3 on its own beat, all births are by a chain of fewest couplings back to a me", o3)

# ---- Part C
def by_t1_and_t2(n, B, moments):
    """Born a moment after its fewest couplings from the nearer me (T1), and never born with the same from both (T2)."""
    count = 0
    for p in range(1 << n):
        a, b = bin(p).count("1"), bin(p ^ B).count("1")
        count += a != b and min(a, b) <= moments - 1
    return count
rows = []; c1 = True
for n in range(6, 19, 2):
    B = (1 << (n // 2)) - 1; d = n // 2
    if n <= 14:
        _, born, touch = together(is_or_is_nots(n), {0: PLUS, B: MINUS}, d + 3)
        moments, selves = touch
    else:
        moments = (d + 1) // 2 + 1
        selves = by_t1_and_t2(n, B, moments)
    by_t1 = by_t1_and_t2(n, B, moments)
    if n <= 14: c1 &= selves == by_t1
    rows.append((n, d, moments, selves))
say("C1 on a surface of n is-or-is-nots, the selves born with the moment the two mes' births reach one self are T1's and T2's, executed to 14", c1)
for n, d, m, s in rows:
    say(f"   n {n:>2} · the table {1 << n:>7,} · couplings between {d} · moments {m} · selves born {s:>6,}" + ("" if n <= 14 else " (by T1 and T2)"), "sized")
(n0, _, m0, s0), (n1_, _, m1, s1) = rows[0], rows[-1]
say(f"   over these sizes a place more multiplies the table by 2 and the selves born by {(s1 / s0) ** (1 / (n1_ - n0)):.2f}; "
    f"the moments go from {m0} to {m1}", "sized")

# ---- Part L
def a_spiral(n): return {i: [(i + 1) % n] for i in range(n)}                      # Exhibit ONE: 9 to the next self, the last to the first
def a_torus(p, q): return {(a, b): [((a + 1) % p, b), (a, (b + 1) % q)] for a in range(p) for b in range(q)}   # Exhibit ONE: 9 along, 10 across
def exhibit_ones_opening(outs): return {s: (MINUS if (s if isinstance(s, int) else sum(s)) % 2 == 0 else PLUS) for s in outs}
def drawn(outs): return {s: rng.choice((PLUS, MINUS)) for s in outs}
def parting(a, b): return next((t for t, (x, y) in enumerate(zip(a, b)) if x != y), None)
def an_other_than_at(outs, A, opening):
    other = dict(opening); other[A] = MINUS if opening[A] == PLUS else PLUS
    M = 8 * len(outs) + 40
    seq, _, _ = together(outs, opening, M); seq2, _, _ = together(outs, other, M)
    return {s: parting(seq[s], seq2[s]) for s in outs if s != A}

born_as = {name: now_and_same_existing_me_parity(NEITHER, obs)[1] for name, obs in
           (("none", []), ("+", [PLUS]), ("-", [MINUS]), ("+ +", [PLUS, PLUS]), ("- -", [MINUS, MINUS]), ("+ -", [PLUS, MINUS]))}
say("L0 by the twelve lines a self with no prior is none with none reaching it, is born with one parity alone or with two alike, "
    "and is none with a + and a - together",
    born_as == {"none": NEITHER, "+": PLUS, "-": MINUS, "+ +": PLUS, "- -": MINUS, "+ -": NEITHER})
l1 = True
for n in (9, 20, 21):
    outs = a_spiral(n); d = fewest_couplings(outs, 0)
    for opening in [exhibit_ones_opening(outs)] + [drawn(outs) for _ in range(6)]:
        got = an_other_than_at(outs, 0, opening)
        l1 &= all(got[s] == 2 * d[s] for s in got)
say("L1 all living on Exhibit ONE's spiral, a co-chain of 9, 20 and 21 selves: one me's other-than is in all other selves' own moments, "
    "from twice its couplings on, with Exhibit ONE's opening and six drawn", l1)
l2 = True; sized = []
for label, outs, A in (("Exhibit ONE's torus 5 by 7", a_torus(5, 7), (0, 0)), ("Exhibit ONE's torus 9 by 7", a_torus(9, 7), (1, 1)),
                       ("a round of 21 both ways", a_round(21), 0), ("a closing surface 9 by 7", a_closing_surface(9, 7), (1, 1)),
                       ("8 is-or-is-nots", is_or_is_nots(8), 0)):
    row = []
    for opening in [exhibit_ones_opening(outs)] + [drawn(outs) for _ in range(6)]:
        got = an_other_than_at(outs, A, opening)
        never = sum(v is None for v in got.values()); row.append(never); l2 &= never == 0
    sized.append(f"   {label}: of {len(outs) - 1} other selves, never other-than what they were, Exhibit ONE's opening then six drawn, {row}")
say("L2 all living on a surface, a self observing two others or more: one me's other-than is in all other selves' own moments", l2)
for line in sized: say(line, "sized")

# ---- Parts B and A
LINES = now_and_same_existing_me_parity
def unlike_together(obs): return any(g == PLUS for g in obs) and any(g == MINUS for g in obs)
def as_they_are(prior, obs, u): return LINES(prior, obs)
def birth_drawn(prior, obs, u):
    if prior == NEITHER and unlike_together(obs): obs = [PLUS if u < 0.5 else MINUS]
    return LINES(prior, obs)
def accepting_one(prior, obs, u):
    if unlike_together(obs):
        offers = [g for g in obs if g != NEITHER]; obs = [offers[int(u * len(offers))]]
    return LINES(prior, obs)
def together_with(cell, outs, opening, moments, draws):
    state = {s: opening.get(s, NEITHER) for s in outs}
    obs = {s: [] for s in outs}; seq = {s: [state[s]] for s in outs}; born = {s: 0 for s in opening}
    for t in range(1, moments + 1):
        arriving = {s: [] for s in outs}
        for s in outs:
            was = state[s]
            lays, state[s] = cell(was, obs[s], draws[s][t])
            if was == NEITHER and state[s] != NEITHER: born[s] = t
            for to in outs[s]: arriving[to].append(lays)
        obs = arriving
        for s in outs: seq[s].append(state[s])
    return seq, born

rng2 = random.Random(26)
TWO = [("a round of 21", a_round(21), 0, 8), ("a closing surface 9 by 7", a_closing_surface(9, 7), (1, 1), (5, 4)),
       ("8 is-or-is-nots, 8 between", is_or_is_nots(8), 0, 255), ("8 is-or-is-nots, 4 between", is_or_is_nots(8), 0, 15)]
got = {}
for name, cell in (("B", birth_drawn), ("A", accepting_one)):
    all_born = on_time = alone = True; finds = []
    for label, outs, A, B in TWO:
        dA, dB = fewest_couplings(outs, A), fewest_couplings(outs, B)
        M = 6 * max(max(dA.values()), max(dB.values())) + 60
        row = []
        for d in range(3):
            draws = {s: [rng2.random() for _ in range(M + 1)] for s in outs}
            seq, born = together_with(cell, outs, {A: PLUS, B: MINUS}, M, draws)
            seqA, _ = together_with(cell, outs, {A: PLUS}, M, draws)
            seqB, _ = together_with(cell, outs, {B: MINUS}, M, draws)
            all_born &= len(born) == len(outs)
            on_time &= all(born[s] == min(dA[s], dB[s]) + 1 for s in born if s not in (A, B))
            a, b = parting(seq[A], seqA[A]), parting(seq[B], seqB[B])
            alone &= a is None and b is None
            row.append((a is not None) + (b is not None))
        finds.append((label, dA[B], row))
    got[name] = (all_born, on_time, alone, finds)
b_born, b_time, b_alone, _ = got["B"]
say("B1 a + and a - together birthing a self as one of the two, drawn: two mes unlike, all selves are born, the between as well: four layings, three draws", b_born)
say("B2 with that birth, all selves are born a moment after their fewest couplings from the nearer me, in all draws", b_time)
say("B3 with that birth, a me's own moments with an other me on the surface are its moments alone, in all draws", b_alone)
a_born, a_time, a_alone, a_finds = got["A"]
say("A1 a session's own: a self accepting one offerer with a + and a - together: all selves are born, a moment after their fewest couplings", a_born and a_time)
say("A2 a session's own: accepting one offerer, both mes' own moments are other-than their moments alone, in all draws",
    all(k == 2 for _, _, row in a_finds for k in row))
for label, d, row in a_finds:
    say(f"   {label}: of the two mes, with own moments other-than alone, a draw apiece, {row}", "sized")
a3 = True; rows = []
for label, outs, A in (("a closing surface 9 by 7", a_closing_surface(9, 7), (1, 1)), ("8 is-or-is-nots", is_or_is_nots(8), 0)):
    M = 240; r1 = []; r2 = []
    for d in range(3):
        draws = {s: [rng2.random() for _ in range(M + 1)] for s in outs}
        opening = {s: rng2.choice((PLUS, MINUS)) for s in outs}
        other = dict(opening); other[A] = MINUS if opening[A] == PLUS else PLUS
        for cell, r in ((as_they_are, r1), (accepting_one, r2)):
            seq, _ = together_with(cell, outs, opening, M, draws); seq2, _ = together_with(cell, outs, other, M, draws)
            r.append(sum(parting(seq[x], seq2[x]) is None for x in outs if x != A))
    a3 &= all(v == 0 for v in r2)
    rows.append(f"   {label}: of {len(outs) - 1} other selves, never other-than what they were · the lines as they are {r1} · accepting one {r2}")
say("A3 a session's own: all living, accepting one offerer, one me's other-than is in all other selves' own moments, in all draws", a3)
for line in rows: say(line, "sized")

for mark, text in out: print(f"{text}: {mark}" if mark != "sized" else text)
print()
print(sum(m == "is" for m, _ in out), "lines is,", sum(m == "is-not" for m, _ in out), "is-not,", sum(m == "sized" for m, _ in out), "sized")
