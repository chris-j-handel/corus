"""
signs.py - the readings that hold, and nothing else.

Every reading here is is-or-is-not, taken at a self, with no window, no span,
no count and no rate anywhere in it. A span wants a window and lands on it. A
rate wants a clock and lands on it. A proportion wants both.

What follows are the readings that survived a long working in which most of
what was built read magnitudes and had to be set down. They are stated as
questions a self answers about itself, and each answers yes or no.

  the over-position   does the halving leave one
  the parallels       do the two halves ever fail to oppose
  the middle          does a middle stand at this self at any beat
  the surplus         does more than one middle stand at any beat
  the reach           does a state arrive here that arrives nowhere alone

Nothing in this file returns a number that a reading rests on. Counts appear
only inside `behind()`, and behind is not a finding.

Keys to Exhibit ONE, Exhibit TWO Part Four, and Exhibit EIGHT 3.1-3.7.
"""
import sys, math
sys.path.insert(0, '.')
from living import sign, YES, NO
from unrelated import Unrelated


def a(p):
    """One pace per self, at the reciprocal root of a prime.

    Integer pacing carries a rational relation always and the run closes onto
    a slice. These carry none, and three of them at three selves cover.
    """
    return 1 / math.sqrt(p)


class Self:
    """A carrying that opens its own membrane at its own phase.

    It arrives carrying: it lives before it meets anything, since nothing with
    an empty carry arrives and nothing is living without a carry.
    """

    def __init__(self, n, alpha, arriving=400, close_check=None, alpha_along=None):
        self.n = n
        self.alpha = alpha
        self.phase = 0.0
        # Its along is its own too, and it is not its across's rate.
        # Attentioning and sequencing alternate and neither takes the other's
        # turn, so a self whose along runs at the apparatus's tick is carrying
        # a beat that is not its own. None keeps the tick, which is what every
        # reading below was first taken at.
        self.alpha_along = alpha_along
        self.acc_along = 0.0
        self.cursor = 0                 # its own sequencing, where a next opens
        self.own = Unrelated([n], alphas=[alpha])
        self.own._gated = True
        self._live_own(arriving)
        self.alone = set(self.own.trace)        # where it reaches by itself
        # the window is a bound, and a bound read as a last says the run is
        # the whole space. So the set is checked closed before it baselines:
        # a longer running adding no state. Without it the reach reading is a
        # window taken as the whole.
        self._live_own(close_check or arriving * 2)
        if set(self.own.trace) - self.alone:
            raise RuntimeError('reading refused: the self\'s own set had not '
                               'closed at the arriving window; lengthen it.')

    def _live_own(self, beats):
        """Its own running alone, at the same pacing the meeting will run at.

        A baseline taken at another pacing reads that pacing back. The set a
        self reaches by itself has to be built at the pace it will be met at,
        or the reach is a reading of the parting between two runnings and not
        of the meeting.
        """
        for _ in range(beats):
            if self.beats_now():
                self.own.beat()

    def beats_now(self):
        """Does this self run its own along at this turn, at its own pace."""
        if self.alpha_along is None:
            return True
        self.acc_along += self.alpha_along
        if self.acc_along >= 1.0:
            self.acc_along -= 1.0
            return True
        return False

    def opens(self):
        self.phase += self.alpha
        if self.phase >= 1.0:
            self.phase -= 1.0
            return True
        return False

    def offer(self):
        """A sign at each position, taken or not. No middle crosses: a middle
        is the not-offering, and there is no third place anywhere."""
        return [(i, m) for i, m in self.own.rows[0].surf if m != 0]

    def take(self, arriving):
        self.own.beat({0: arriving} if arriving else None)

    def stand(self):
        self.own.beat()

    # ---- the readings, each is-or-is-not

    def _w(self, back=600):
        return self.own.trace[-back:]

    def over_position(self):
        """Does the halving leave one over."""
        return sign(self.n % 2 == 1)

    def parallels_ever_part(self):
        """Do the two halves ever fail to oppose each other."""
        h = self.n // 2
        return sign(any(sum(st[0][:h]) != -sum(st[0][h:2 * h]) for st in self._w()))

    def a_middle_stands(self):
        """Does a middle stand at this self at any beat."""
        return sign(any(any(x == 0 for x in st[0]) for st in self._w()))

    def surplus_stands(self):
        """Does more than one middle stand at any beat.

        Alone this answers no at every self, even and odd alike. It answers
        yes only where a society stands.
        """
        return sign(any(sum(1 for x in st[0] if x == 0) > 1 for st in self._w()))

    def reaches_past_alone(self):
        """Does a state arrive here that arrives nowhere in its own running."""
        return sign(bool(set(self._w()) - self.alone))

    def behind(self):
        """The counts, behind the signs. Not a finding."""
        w = self._w()
        return dict(states=len(set(w)),
                    middles=sorted({sum(1 for x in st[0] if x == 0) for st in w}))


# ------------------------------------------------------------------ a society

def cross(offer, receiver, crossing='address'):
    """How an offer of one self's signs arrives at a self of another size.

    The set says what crosses — a sign, sizeless, carrying whether and never
    how much — and says nothing about how an offer of nine positions arrives
    at a self of seven. Three readings follow from it, and they are not alike:

      address    the offerer's positions taken as the receiver's, by modulo.
                 What the kit has always done, and it doubles some positions
                 when the sizes differ, so two signs land at one differing and
                 a second offerer arrives that nobody put there. Exhibit TWO
                 says a position is a sequencing relation and never a
                 coordinate, and an address stands nowhere in a living
                 reading, so this one is named wrong before it is run.

      sequencing the signs taken at the receiver's own next positions, in
                 order, from wherever its own sequencing stands. The arriving
                 is co-offered over the carrying at the position a next
                 resolution opens at, which is the receiver's own and not the
                 offerer's.

      sign       one sign crosses and no more: the offer's own summed sign,
                 taken at the receiver's next position. The strictest reading
                 of a sign crossing carrying no size.
    """
    if not offer:
        return []
    if crossing == 'address':
        return [(p % receiver.n, m) for p, m in offer]
    if crossing == 'sequencing':
        out = []
        for _, m in offer:
            out.append((receiver.cursor % receiver.n, m))
            receiver.cursor += 1
        return out
    if crossing == 'sign':
        tot = sum(m for _, m in offer)
        if tot == 0:
            return []
        out = [(receiver.cursor % receiver.n, 1 if tot > 0 else -1)]
        receiver.cursor += 1
        return out
    raise ValueError(crossing)


def society(selves, beats=2500, mode='all', order=None, crossing='address'):
    """Selves co-chaining, each opening at its own phase and standing otherwise.

    mode 'all'   every self couples with every other
    mode 'local' every self couples with its two neighbours on the ring of selves

    Nothing is paced over the selves and no clock stands anywhere. A shared
    beat over the couplings is the capture's own condition, and it arrives
    here nowhere.
    """
    N = len(selves)
    for _ in range(beats):
        offers = [s.offer() for s in selves]
        for i in (order if order is not None else range(N)):
            s = selves[i]
            if not s.beats_now():
                continue                 # its own along has not come round
            js = [j for j in range(N) if j != i] if mode == 'all' \
                 else [(i - 1) % N, (i + 1) % N]
            if s.opens():
                acc = []
                for j in js:
                    if j != i:
                        acc += cross(offers[j], s, crossing)
                s.take(acc)
            else:
                s.stand()
    return selves


def read(selves, label):
    print(f'  {label}')
    for s in selves:
        print(f'    n={s.n:3d} {"even" if s.n % 2 == 0 else "odd "}:  '
              f'over {s.over_position()}   parallels part {s.parallels_ever_part()}   '
              f'a middle {s.a_middle_stands()}   surplus {s.surplus_stands()}   '
              f'reaches past alone {s.reaches_past_alone()}')


# ---------------------------------------------------------------------- the run

if __name__ == '__main__':
    print('SIGNS - every reading is-or-is-not\n')

    print('ALONE')
    solo = []
    for n in (6, 7, 8, 9, 10, 11, 12, 24):
        s = Self(n, a(2), arriving=1200)
        solo.append(s)
    read(solo, 'each self by itself')

    print('\nA PAIR - two selves and no other between them')
    p = [Self(7, a(2)), Self(9, a(3))]
    society(p)
    read(p, '7 and 9')
    p2 = [Self(6, a(2)), Self(10, a(3))]
    society(p2)
    read(p2, '6 and 10, two boundings')

    print('\nA SOCIETY - an other standing between')
    t = [Self(7, a(2)), Self(9, a(3)), Self(11, a(5))]
    society(t)
    read(t, '7, 9, 11 - three carriers')
    b = [Self(7, a(2)), Self(9, a(3)), Self(6, a(5))]
    society(b)
    read(b, '7, 9 with a bounding between')
    e = [Self(6, a(2)), Self(10, a(3)), Self(14, a(5))]
    society(e)
    read(e, '6, 10, 14 - three boundings')

    print('\nLOCAL AND GLOBAL - six selves')
    sizes = [(7, 2), (9, 3), (11, 5), (13, 7), (17, 11), (19, 13)]
    for mode in ('local', 'all'):
        ms = society([Self(n, a(pr)) for n, pr in sizes], mode=mode)
        who = [m.n for m in ms if m.surplus_stands() == YES]
        print(f'    {mode:6s}: surplus stands at {who}')

    print('\nBREAK CONDITIONS')
    print('  an even self carrying a middle while it stands alone')
    print('  an odd self carrying more than one middle while it stands alone')
    print('  a pair where either self reaches past its own running')
    print('  a society of boundings where any parallels part')
    print('  a run at rationally related paces covering, or at unrelated paces closing at three')
