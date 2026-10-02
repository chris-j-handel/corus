"""
living.py - the one engine of the Natural Networking Test Kit v330.

One life: rows on the Exhibit ONE resolver, carry continuous, forkable for
twin-comparisons, wiring stated as explicit structure, readings refused
until the gate passes on this exact wiring.

The carry is not readable from here. It is name-hidden, and the hiding is
the form: a carry is met by coupling and measured by nothing; a probe
departs with the thing probed. Twin-forking replaces every probe: two
continuations of the one life, differing in one offering, their surfaces
compared. Every reading is a sign, a span, or an ordering. Magnitudes are
reachable only through behind(), and behind() is not a finding.
"""
import copy, math
from resolver import _1_self_coupling

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)


def unrelating_pace(k):
    """One pace per row, at the reciprocal root of a prime.

    Whole-number pacing carries a relation between the paces always and the
    run closes onto a small set of positions. These carry none. A root of this
    kind is what the field calls a surd.
    """
    return 1 / math.sqrt(PRIMES[k % len(PRIMES)])

YES, NO = 'yes', 'no'
def sign(b): return YES if b else NO


class Self:
    """A resolver-row. Surface readable; carry its own."""
    def __init__(self, n, phase=0):
        self.n = n
        self.__carry = []                        # met by coupling, read by nothing
        self.__stands = {i: (1 if (i + phase) % 2 == 0 else -1) for i in range(n)}
        self.__sounded = set(range(n))
        self.t = 0

    def couple(self, accepted):
        seq, self.__carry = _1_self_coupling(self.__carry, accepted)
        self.__stands = {i: m for i, m in seq if 0 <= i < self.n}   # only what stands
        self.__sounded = {i for i, m in seq if 0 <= i < self.n}     # what sounded at all
        self.t += 1

    def middles(self):
        """Positions that sounded and took no sign.

        A position that did not sound reads zero at the surface exactly as a
        middle does. Without this record the two are one mark, and a surplus
        read at the surface counts silences.
        """
        return sum(1 for i in self.__sounded if self.__stands.get(i, 0) == 0)

    @property
    def surf(self):
        return [(i, self.__stands.get(i, 0)) for i in range(self.n)]

    @surf.setter
    def surf(self, pairs):                                   # selftell pins a row here
        self.__stands = {i: m for i, m in pairs if m != 0}

    def signs(self):
        return tuple(self.__stands.get(i, 0) for i in range(self.n))

    def at(self, i):                                         # the sign at one sequencing
        return self.__stands.get(i, 0)

    def own_along(self):
        return [((i + 1) % self.n, m) for i, m in self.__stands.items() if m != 0]


class Life:
    """One continuous living of coupled rows.

    wiring: 'ring' | 'chain'   (the across-structure, stated)
    pace:   'own' | 'unrelating' | 'clock'
            own:   each row opens its across every n-th of its own beats.
                   Integer sizes with integer pacing carry a rational
                   relation always, so a run at this pace closes onto a
                   slice and every reading taken on it is a reading of the
                   slice - correctly taken there and nowhere else.
            unrelating: each row opens at the reciprocal root of a
                   prime, which carries no relation to the others, so the
                   run returns to no position twice.
            clock: every beat - the shared beat, the capture's own
                   condition, available so the capture is runnable.
    Readings refuse until gate() has passed on this wiring.
    """
    def __init__(self, lengths, wiring='ring', pace='own'):
        self.lengths = list(lengths)
        self.wiring = wiring
        self.pace = pace
        self.rows = [Self(n, phase=k % 2) for k, n in enumerate(lengths)]
        self.phases = [0.0] * len(lengths)
        self.trace = []
        self._gated = False

    # ---- the living ----
    def _neighbours(self, k):
        n = len(self.rows)
        if n == 1: return []
        if self.wiring == 'chain':
            return [j for j in (k - 1, k + 1) if 0 <= j < n]
        return sorted({(k - 1) % n, (k + 1) % n} - {k})

    def beat(self, offerings=None):
        """One beat of the whole life. offerings: {row_index: [(pos, sign)]}"""
        for k, r in enumerate(self.rows):
            acc = list(r.own_along())
            if self.pace == 'clock':
                opens = True
            elif self.pace == 'unrelating':
                self.phases[k] += unrelating_pace(k)
                opens = self.phases[k] >= 1.0
                if opens:
                    self.phases[k] -= 1.0
            else:
                opens = (r.t % r.n == 0)
            if opens:
                for kk in self._neighbours(k):
                    acc += [(i % r.n, m) for i, m in self.rows[kk].surf if m != 0]
            if offerings and k in offerings:
                acc += [(i, m) for i, m in offerings[k] if m != 0]
            r.couple(acc)
        self.trace.append(tuple(r.signs() for r in self.rows))

    def live(self, beats, offer=None):
        """offer: fn(t) -> offerings dict, or None. The carry rides on."""
        t0 = len(self.trace)
        for t in range(t0, t0 + beats):
            self.beat(offer(t) if offer else None)

    def fork(self):
        """A twin: the one life continued two ways. The honest probe."""
        return copy.deepcopy(self)

    # ---- the gate ----
    def gate(self):
        """The parity gate run on THIS wiring's own bare structure, and the
        resolver gate on lone rows. Readings refuse until this passes."""
        ok = True
        # bare rows, the documented wiring: both neighbours, one-at-a-time
        def bare(n, turns=120):
            row = [1 if i % 2 == 0 else -1 for i in range(n)]
            if n % 2: row[-1] = 1
            fr, sm = set(), set()
            for _ in range(turns):
                for i in range(n):
                    L, R = row[(i - 1) % n], row[(i + 1) % n]
                    t = L + R
                    row[i] = (-1 if t > 0 else 1) if t != 0 else -row[i]
                fr.add(sum(1 for i in range(n) if row[i] == row[(i + 1) % n]))
                sm.add(sum(row))
            return fr, sm
        for n in (2, 4, 6):
            fr, sm = bare(n)
            ok = ok and fr == {0} and sm == {0}
        for n in (3, 5, 7):
            fr, sm = bare(n)
            ok = ok and fr == {1} and sm <= {-1, 1}
        fr, sm = bare(8)
        ok = ok and fr == {0} and sm == {0}
        # lone resolver rows on this engine
        for n, want in ((5, 20), (7, 28), (4, 2), (6, 2)):
            solo = Life([n]); solo._gated = True
            solo.live(500)
            tail = solo.trace[len(solo.trace) // 3:]
            span = len(set(st[0] for st in tail))
            ok = ok and span == want
        self._gated = ok
        return sign(ok)

    def _require_gate(self):
        if not self._gated:
            raise RuntimeError(
                'reading refused: the gate has not passed on this harness. '
                'Run life.gate() first. A harness fallen to the wrong '
                'attractor hands back a clean, confident number, and it is '
                'worth nothing.')

    # ---- the readings: signs, spans, orderings ----
    def window(self, back=600):
        self._require_gate()
        return self.trace[-back:]

    def row_span(self, k, back=600):
        """Which-state-of-span: the count of distinct surfaces, a span."""
        w = self.window(back)
        return len(set(st[k] for st in w))

    def lands(self, back=600):
        w = self.window(back)
        return sign(any(w[i] == w[i - 1] for i in range(1, len(w))))

    def captured(self, back=300):
        w = self.window(back)
        n = len(self.rows)
        return sign(any(all(st[a] == st[b] for st in w)
                        for a in range(n) for b in range(a + 1, n)))

    def joint_span(self, back=600):
        return len(set(self.window(back)))

    def surplus(self, back=600):
        """Captured, present or absent - and the three do not stand alike.

        'captured' is a sign: do any two rows carry the identical surface at
        every beat of the window. It holds.

        'present' against 'absent' compares the joint span to the sum of the
        selves' spans, which is two numbers compared to decide something, and
        the kit's own one rule says that is where the reading went missing
        several steps back. It belongs at behind(). The surplus read
        is-or-is-not stands at signs.py, where it asks whether more than one
        middle stands at a self at any beat, and no number appears in it.

        Kept whole here, named for what it is, until the deciding at the two
        readings runs: whether this parts into the sign it carries and the
        magnitude behind it, or whether society.py's own readings want it
        standing as it is.
        """
        self._require_gate()
        joint = self.joint_span(back)
        selves = [self.row_span(k, back) for k in range(len(self.rows))]
        if self.captured() == YES or joint <= max(selves):
            return 'captured'
        return 'present' if joint > sum(selves) else 'absent'

    def cones(self, window=400, skip=4):
        """Omegaing and apexing per window over this life so far:
        a never-before state arriving, a visited state returning."""
        self._require_gate()
        seen = set(); wins = []
        for w0 in range(0, len(self.trace), window):
            win = self.trace[w0:w0 + window]
            new = any(tuple(st) not in seen for st in win)
            re_ = any(tuple(st) in seen for st in win)
            for st in win: seen.add(tuple(st))
            wins.append((new, re_))
        tail = wins[skip:] or wins
        return dict(omegaing=sign(all(n for n, _ in tail)),
                    apexing=sign(all(r for _, r in tail)))

    def behind(self, back=600):
        """The magnitudes, behind the signs. Not a finding."""
        self._require_gate()
        return dict(joint=self.joint_span(back),
                    selves=[self.row_span(k, back) for k in range(len(self.rows))])
