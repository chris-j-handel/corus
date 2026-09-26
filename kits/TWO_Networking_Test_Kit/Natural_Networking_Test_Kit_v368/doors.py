"""
THE EIGHT DOORS — the securities of the fractal technology, met as runs.

Four at the self, four at the society. With all eight held the lattice is the
Step-1 living whole. Each door opens one security inverted, singly, all else
held, and the reading is one sign: the living stopped, in that door's own way.

Register: code-form statements about this tested lattice and construction.

The four self securities, and their inversions:
  1 self-bounding      the carry ages to its bound and releases
                       -> inverted: the release removed, entries held forever
  2 self-negation      the sign inverts at the membrane (never-landing)
                       -> inverted: the own-inversion removed
  3 sign-only          the selection a sign, sizeless, no position higher
                       -> inverted: the selection a magnitude, totals kept
  4 own-time           each row accepts the across on its own pace
                       -> inverted: a common clock, every row every beat

The four society securities, and their inversions:
  5 all-edge           every row couples its neighbours directly, no hub
                       -> inverted: every across routed through one row
  6 no-seat-outside    no standing order imposed over the rows
                       -> inverted: a governor, one fixed pattern imposed
                          on every row every beat
  7 riding, unpinned   every row's surface its own, none held
                       -> inverted: one row's surface pinned fixed
  8 own-offering       every row offers its own along (its own co-offering)
                       -> inverted: one row's own offering removed, the row
                          only following others

The baseline (all eight held) is verified byte-identical to the Exhibit ONE
resolver before any door is opened.
"""
import sys, math
sys.path.insert(0, '.')
from resolver import _1_self_coupling as resolver_one

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)


def unrelating_pace(k):
    """One pace per row, at the reciprocal root of a prime.

    A row opening every n-th of its own beats is paced in whole numbers, and
    whole-number sizes with whole-number pacing carry a relation between the
    paces always, so the run closes onto a small set of positions and repeats
    it forever. Every reading taken there is a reading of that set, correctly
    taken there and nowhere else.

    Reciprocal roots of distinct primes carry no such relation, so the running
    returns to no position twice. The field's own word for such a root is a
    surd, and the kit's own pacing instrument returns the parting: whole-number
    paces close at every size run, unrelating paces at three rows or more close
    nowhere.
    """
    return 1 / math.sqrt(PRIMES[k % len(PRIMES)])

YN = {True: 'yes', False: 'no '}

def bi_coupling_v(commencing, accepted, release=True, invert=True, sign_only=True):
    off = {s: c for s, m, c, r in commencing}
    bi = [(s, m) for s, m in accepted if m != 0]
    if invert:
        for s, m, c, r in commencing:
            if m > 0: bi.append((s, -1))
            if m < 0: bi.append((s, 1))
    bma = {}
    for s, m in bi:
        if m > 0: bma[s] = bma.get(s, 0) + 1
        if m < 0: bma[s] = bma.get(s, 0) - 1
    if sign_only:
        bms = [(s, 1 if bma[s] > 0 else (-1 if bma[s] < 0 else 0)) for s in bma]
    else:
        bms = [(s, bma[s]) for s in bma]                    # the magnitude kept
    rc = {}
    for s, m, c, r in commencing:
        if (not release) or r + 1 <= 3 or (r + 1 == 4 and c > 0):
            rc[s] = (m, c, r + 1)
    for s, m in bms:
        if m != 0:
            rc[s] = (m, 0 - off.get(s, 1), 0)
    return bms, [(s, m, c, r) for s, (m, c, r) in rc.items()]


class Row:
    """A resolver-row that keeps its own time.

    Its opening phase rides on the row itself and nowhere else. A pace kept
    in a store beside the rows is a clock standing over the couplings, and a
    forked twin sharing that store is two selves at one beat.
    """

    def __init__(self, n, phase=0, alpha=None, alpha_along=None, **flags):
        self.n = n
        self.flags = flags
        self.alpha = alpha              # its across: when its membrane opens
        self.acc = 0.0
        # Its along is its own too, and it is not the same rate as its across.
        # Attentioning and sequencing alternate, one at each parity and
        # neither at the other's turn, so a self running its along only when
        # its across opens has had its own running between couplings taken
        # away. None here means the along runs at the apparatus's tick, which
        # is the shared beat the whole kit has carried.
        self.alpha_along = alpha_along
        self.acc_along = 0.0
        self.__stands = {i: (1 if (i + phase) % 2 == 0 else -1) for i in range(n)}
        self.__sounded = set(range(n))
        self.own_trace = []          # its own momentaries, at its own beats
        self.own_mid = []            # its own middles, at the same
        self.carry = []
        self.t = 0

    @property
    def surf(self):
        return [(i, m) for i, m in self.__stands.items()]

    def signs(self):
        return tuple(self.__stands.get(i, 0) for i in range(self.n))

    def at(self, i):                                         # the sign at one sequencing
        return self.__stands.get(i, 0)

    def beats_now(self):
        """Does this row run its own along at this turn, at its own pace."""
        if self.alpha_along is None:
            return True
        self.acc_along += self.alpha_along
        if self.acc_along >= 1.0:
            self.acc_along -= 1.0
            return True
        return False

    def opens(self):
        """Does this row open its across at this beat, at its own pace."""
        if self.alpha is None:
            return self.t % self.n == 0
        self.acc += self.alpha
        if self.acc >= 1.0:
            self.acc -= 1.0
            return True
        return False

    def beat(self, acc):
        seq, self.carry = bi_coupling_v(self.carry, acc, **self.flags)
        self.__stands = {i: m for i, m in seq if 0 <= i < self.n}   # only what stands
        self.__sounded = {i for i, m in seq if 0 <= i < self.n}     # what sounded at all
        self.t += 1
        # A self records when it beats and not when an apparatus ticks. A
        # joint trace indexed by a shared tick is a common clock in the
        # recording however clockless the running: a self that did not beat
        # has its unchanged surface written down again, and a reading taken
        # there counts a silence as a landing.
        self.own_trace.append(self.signs())
        self.own_mid.append(self.middles())

    def impose(self, order):
        """A standing order taking the position whatever the self surfaced.

        This is the forcing: one side's not-offer removed, so the sign the
        self took at its own membrane no longer stands. An order that only
        joins the accepted signs is an offering and governs nothing.
        """
        for i, m in order:
            if 0 <= i < self.n:
                self._Row__stands[i] = m
                self._Row__sounded.add(i)
        self.own_trace[-1] = self.signs()
        self.own_mid[-1] = self.middles()

    def middles(self):
        """How many middles stand: positions that sounded and took no sign.

        A position that did not sound reads zero at the surface and is an
        absence, not a middle. Without this record the two are one mark and a
        surplus reading counts silences.
        """
        return sum(1 for i in getattr(self, '_Row__sounded', ())
                   if self.__stands.get(i, 0) == 0)


def _door_flags(door, lengths):
    if door == 1: return [dict(release=False) for _ in lengths]
    if door == 2: return [dict(invert=False) for _ in lengths]
    if door == 3: return [dict(sign_only=False) for _ in lengths]
    return [dict() for _ in lengths]


def _one_beat(rows, door, governor, lengths, order=None, along='clocked'):
    """One beat of the whole lattice, at whichever door stands open.

    `order` is the turn the selves are taken in. A serial apparatus must take
    them in some turn, and taking them always in index order is an ordering
    imposed on selves that couple at no membrane. Couplings synchronize at
    their own membrane and at no other, so two selves that never couple have
    no order between them, and any reading that changes when the turn changes
    was reading the apparatus.
    """
    for k in (order if order is not None else range(len(rows))):
        r = rows[k]
        # `along` decides whether a self beats at all at this turn.
        #
        #   clocked: every self beats its own along at every tick and only its
        #            across is paced, so a beat is shared by every self
        #            whatever its own pace says. Own-time is then already
        #            partly open at the baseline, and door four inverts a
        #            security the apparatus was never holding.
        #   own:     a self beats only at its own turn, so the loop is an
        #            ordering and not a beat, and own-time stands whole.
        if along == 'own' and not r.beats_now():
            continue                     # its own along has not come round
        opens_now = True if door == 4 else r.opens()
        if door == 7 and k == 1:
            r.t += 1
            continue
        acc = []
        if not (door == 8 and k == 2):
            acc = [((i + 1) % r.n, m) for i, m in r.surf if m != 0]
        pace_open = opens_now if along == 'own' else (
            True if door == 4 else r.opens())
        if pace_open:
            if door == 5:
                nbrs = [1] if k != 1 else [j for j in range(len(rows)) if j != 1]
            else:
                nbrs = sorted({(k - 1) % len(rows), (k + 1) % len(rows)} - {k})
            for kk in nbrs:
                acc += [(i % r.n, m) for i, m in rows[kk].surf if m != 0]
        if door == 6 and governor:
            # An order added into the accepted list is another offering: the
            # self cannot tell it from a neighbour's, takes it or not by its
            # own sign, and keeps its own not-offer entire. Nothing stands
            # over the preferring, so nothing is governed. A governing removes
            # the not from one side, so the standing order takes the position
            # whatever the self surfaced.
            acc += [(i, governor[i % len(governor)]) for i in range(r.n)]
            r.beat(acc)
            r.impose([(i, governor[i % len(governor)]) for i in range(r.n)])
            continue
        r.beat(acc)


def run(lengths, beats, door=0, governor=None, with_middles=False, pace='own',
        order=None, along='clocked'):
    flags = [dict() for _ in lengths]
    if door == 1: flags = [dict(release=False) for _ in lengths]
    if door == 2: flags = [dict(invert=False) for _ in lengths]
    if door == 3: flags = [dict(sign_only=False) for _ in lengths]
    rows = [Row(n, phase=k % 2, alpha=(unrelating_pace(k) if pace == 'unrelating' else None),
                **flags[k]) for k, n in enumerate(lengths)]
    trace, mid = [], []
    for t in range(beats):
        _one_beat(rows, door, governor, lengths, order, along)
        trace.append(tuple(r.signs() for r in rows))
        mid.append(tuple(r.middles() for r in rows))
    return (trace, mid) if with_middles else trace


def solo_closed(n, phase, flags, beats=1200, close_check=3000):  # noqa: C901
    """A row's own whole running, alone, at its own phase, checked closed.

    The window is a bound, and a bound read as a last says the enumerated run
    is the whole space. So the set is checked closed before it baselines: a
    longer run adding no state. Without that check the reach reading is a
    window taken as the whole.
    """
    r = Row(n, phase=phase, **flags)   # solo: the across never opens, the pace idle
    seen, t = set(), 0
    for t in range(close_check):
        r.beat([((i + 1) % r.n, m) for i, m in r.surf if m != 0])
        if t < beats:
            base_end = t
            seen.add(r.signs())
        else:
            if r.signs() not in seen:
                raise RuntimeError('reading refused: the solo set had not '
                                   'closed at the baseline window.')
    return seen


def surplus_stands(mid, k, back=600):
    """Does more than one middle stand at this self at any beat.

    Exhibit TWO 5.2's own question, is-or-is-not, no number in it. This is the
    sign the shared clock stops by: the surplus dies, and a reading that only
    asks whether the living landed cannot see it.

    It reads the row's own middle record and never the surface. A position
    that did not sound reads zero at the surface, and a reading taken there
    counts silences as middles.
    """
    return any(m[k] > 1 for m in mid[-back:])


def reach_stands(trace, k, n, phase, flags, back=600):
    """Does a state arrive at this self that arrives nowhere in its own running.

    Exhibit TWO 5.2's own question, is-or-is-not. This is the sign all-edge
    routed through one stops by: the centre rises while every surround falls,
    read as direction and never as ratio.
    """
    alone = solo_closed(n, phase, flags)
    return any(st[k] not in alone for st in trace[-back:])


def twin_parts(lengths, beats, door, governor=None, pace='own', fork_at=None):
    """The one living continued two ways, differing in one door, the faces read.

    A co-chaining reading, and the only kind that reaches a membrane above.
    The surplus, the parallels and the reach all read a self against its own
    identity - inward, cohering to one - and a running that never closes has
    no one identity for them to be taken against. This reads the between
    instead: two continuations of one life and whether a face ever parts.

    It needs no closed set and no window taken as a last. Its answer is a
    sign, per self: did this face ever part from its twin's.
    """
    import copy
    fork_at = fork_at or beats // 3
    # one undifferentiated living to the fork: no door open at either twin yet
    base = [Row(n, phase=k % 2,
                alpha=(unrelating_pace(k) if pace == 'unrelating' else None))
            for k, n in enumerate(lengths)]
    for t in range(fork_at):
        _one_beat(base, 0, governor, lengths)
    a_rows, b_rows = copy.deepcopy(base), copy.deepcopy(base)
    # the door opens at one twin only, and it opens at the fork
    for k, f in enumerate(_door_flags(door, lengths)):
        a_rows[k].flags = f
    parted = [False] * len(lengths)
    for t in range(beats - fork_at):
        _one_beat(a_rows, door, governor, lengths)
        _one_beat(b_rows, 0, governor, lengths)
        for k in range(len(lengths)):
            if a_rows[k].signs() != b_rows[k].signs():
                parted[k] = True
    return parted


def from_one_living(lengths, beats, governor=None, pace='own', order=None,
                    along='clocked', fork_at=None):
    """One living, forked once per door, every reading taken at a continuation.

    Every reading is otherwise a prepared reading: the rows built fresh at
    each call, so two doors compare two lives that never shared a moment and
    the comparability is bought with the emptying. A prepared thing carries
    what a fresh start carries and a living thing carries what its history
    allows, and the two differ - the living's own being the finding.

    So the living runs once to the fork and every door opens at a
    continuation of it. The carry rides through all of the checking and is
    abandoned nowhere, which is the one condition the doors were read without.

    Returns {door: (trace, middles)} with the baseline at nought.
    """
    import copy
    fork_at = fork_at or beats // 3
    base = [Row(n, phase=k % 2,
                alpha=(unrelating_pace(k) if pace == 'unrelating' else None))
            for k, n in enumerate(lengths)]
    for _ in range(fork_at):
        _one_beat(base, 0, governor, lengths, order, along)
    out = {}
    for d in range(0, 9):
        rows = copy.deepcopy(base)
        for k, f in enumerate(_door_flags(d, lengths)):
            rows[k].flags = f                       # the door opens at the fork
        trace, mid = [], []
        for _ in range(beats - fork_at):
            _one_beat(rows, d, governor, lengths, order, along)
            trace.append(tuple(r.signs() for r in rows))
            mid.append(tuple(r.middles() for r in rows))
        out[d] = (trace, mid)
    return out


def read_own(rows, back=600):
    """Every reading a self can take of itself, at its own momentaries.

    What is not here is what cannot be here: the joint span, the capture, and
    rows-becoming-one all need two selves' momentaries laid against each
    other, and there is no shared index to lay them on once each self keeps
    its own. Those readings are the shared tick's own and they leave with it.
    """
    out = []
    for r in rows:
        w = r.own_trace[-back:]
        m = r.own_mid[-back:]
        out.append(dict(
            beats=len(r.own_trace),
            span=len(set(w)),
            lands=any(w[i] == w[i - 1] for i in range(1, len(w))),
            higher=any(abs(x) > 1 for st in w[-200:] for x in st),
            surplus=any(c > 1 for c in m),
            middle=any(c > 0 for c in m)))
    return out


def read(trace, lengths):
    tail = trace[len(trace) // 3:]
    per = []
    for k in range(len(lengths)):
        seq = [st[k] for st in tail]
        per.append(dict(span=len(set(seq)),
                        lands=any(seq[i] == seq[i - 1] for i in range(1, len(seq))),
                        higher=any(abs(m) > 1 for st in seq[-200:] for m in [x for x in st])))
    joint = [tuple(st) for st in tail]
    j_lands = any(joint[i] == joint[i - 1] for i in range(1, len(joint)))
    became_one = any(all(st[a] == st[b] for st in tail[-150:])
                     for a in range(len(lengths)) for b in range(a + 1, len(lengths)))
    return per, j_lands, became_one


if __name__ == '__main__':
    # the identity check first: all securities held, byte-identical to Exhibit ONE
    import random
    rng = random.Random(5)
    ok = True
    carry_a, carry_b = [], []
    for _ in range(300):
        acc = [(i, rng.choice((1, -1))) for i in range(7) if rng.random() < 0.6]
        sa, carry_a = resolver_one(carry_a, acc)
        sb, carry_b = bi_coupling_v(carry_b, acc)
        ok = ok and sa == sb and carry_a == carry_b
    print(f'baseline verified byte-identical to Exhibit ONE, surface and carry: {YN[ok]}\n')

    lengths = [int(x) for x in sys.argv[1].split(',')] if len(sys.argv) > 1 else [5, 6, 7]
    pace = sys.argv[2] if len(sys.argv) > 2 else 'own'
    beats = 2400
    print(f'  harness: lengths {lengths}, ring wiring, {beats} beats, pace {pace}\n')
    base, bj, bo = read(run(lengths, beats, door=0, pace=pace), lengths)
    living = (not bj and not bo and all(not p['lands'] and p['span'] > 2
                                        and not p['higher'] for p in base))
    print(f'ALL EIGHT HELD — the living runs {YN[living]}   '
          f'(spans {[p["span"] for p in base]}, nothing lands, no capture, none higher)\n')

    doors = [
        (1, 'self-bounding inverted — the release removed'),
        (2, 'self-negation inverted — the own-inversion removed'),
        (3, 'sign-only inverted — the selection a magnitude'),
        (4, 'own-time inverted — a common clock over the rows'),
        (5, 'all-edge inverted — every across through one row'),
        (6, 'no-seat-outside inverted — a governor imposed'),
        (7, 'riding inverted — one row pinned fixed'),
        (8, 'own-offering inverted — one row only following'),
    ]
    gov = (1, -1, 1, 1, -1, 1, -1)

    # the two signs Exhibit TWO 5.2 names, read at the eight whole first, so
    # each door's reading is against the living and not against a declared zero
    base_tr, base_mid = run(lengths, beats, door=0, governor=gov, with_middles=True, pace=pace)
    base_surplus = [surplus_stands(base_mid, k) for k in range(len(lengths))]
    base_reach = [reach_stands(base_tr, k, n, k % 2, {})
                  for k, n in enumerate(lengths)]
    print(f'  the eight whole: surplus stands at '
          f'{[lengths[k] for k, v in enumerate(base_surplus) if v]}   '
          f'reach stands at {[lengths[k] for k, v in enumerate(base_reach) if v]}\n')

    for d, name in doors:
        tr, mid = run(lengths, beats, door=d, governor=gov, with_middles=True, pace=pace)
        per, jl, one = read(tr, lengths)
        spans = [p['span'] for p in per]
        lands = any(p['lands'] for p in per) or jl
        higher = any(p['higher'] for p in per)
        flags = ({1: dict(release=False), 2: dict(invert=False),
                  3: dict(sign_only=False)}).get(d, {})
        surp = [surplus_stands(mid, k) for k in range(len(lengths))]
        rch = [reach_stands(tr, k, n, k % 2, flags) for k, n in enumerate(lengths)]
        # the surplus died: it stood at the eight whole and stands nowhere now
        surplus_died = any(base_surplus) and not any(surp)
        # the centre rose while the surround fell — read as direction, never as
        # ratio: did the hub keep what a surround lost. Nothing is compared in
        # size and no threshold stands anywhere in it.
        hub = 1
        surround = [k for k in range(len(lengths)) if k != hub]
        centre_rose = (base_surplus[hub] and surp[hub]
                       and any(base_surplus[k] and not surp[k] for k in surround))
        stopped = lands or one or higher or surplus_died or centre_rose
        way = ('a position stands higher' if higher else
               'rows became one' if one else
               'a landing' if lands else
               'the surplus died' if surplus_died else
               'the centre rose while the surround fell' if centre_rose else
               'no stopping read')
        print(f'  door {d}: {name}')
        print(f'          the living stopped {YN[stopped]} — {way}')
        print(f'          surplus at {[lengths[k] for k, v in enumerate(surp) if v]}   '
              f'reach at {[lengths[k] for k, v in enumerate(rch) if v]}')
