"""
membrane.py - a coupling holding its own differings.

The kit wrote a self's own sequencing positions and a coupling's differings as
one space, so an offer of nine positions arriving at a self of seven had to be
mapped, and every mapping supplies a membrane the form does not supply. Three
were built and none made both the pair claim and the trio claim stand.

Here the two spaces are two. A coupling carries its own differings, of its own
count, made at the coupling and owned by neither self. Each self offers into
them at the coupling's own next turn, and takes back at its own next position.
**No position of one self is ever identified with a position of another**, and
nothing is mapped anywhere.

Which is the resolver's own form: it keys on `bi_offering`, the differing, two
signs at one differing sum together, and membrane lives at that two-offering
alone. The differing is not prior to the meeting; it is where two signs meet.
A differing arriving twice is a thing no running makes.

Three cursors run and each is its own: the coupling's, at which differings the
next offerings land; and each self's, at which of its own positions what
surfaced comes back. None of the three is read by anything but its own.
"""
import sys
sys.path.insert(0, '.')
from living import sign, YES, NO


class Coupling:
    """The between two selves make, carrying its own differings.

    It is real and owned by neither, and it holds nothing across a beat: a
    coupling makes a momentary, and a differing is made where two signs meet
    and is gone at the next. Standing alone it holds nothing at all.
    """

    def __init__(self, m, alpha=None):
        self.m = m
        self.cursor = 0
        self.alpha = alpha
        self.acc = 0.0
        self.tally = {}
        self.touched = {}
        self.offered = {}
        self.closed = []          # the differings this coupling has made

    def opens(self):
        if self.alpha is None:
            return True
        self.acc += self.alpha
        if self.acc >= 1.0:
            self.acc -= 1.0
            return True
        return False

    def commence(self):
        """Nothing. A differing is not made by an apparatus tick.

        A coupling is two-way and one-at-a-time: one self offers at its turn
        and the other at its own, and the two signs sum at the one differing
        however many ticks apart the turns fall. **The momentary is made by
        the second offering and not by a beat**, so clearing the differing
        every tick would demand a simultaneity the coupling never carries and
        the two signs would never meet.
        """
        return

    def offer_in(self, who, signs):
        """One sign entering at the differing standing open.

        Two selves stay and one thing crosses, carrying only the sign. A self
        of nine offering nine signs to a self of seven delivers more signs
        than the receiver has positions, so the count of what crosses is
        itself a magnitude and the doubling returns however the landing is
        arranged. The crossing carries whether and never how much.

        The differing stands open until both sides have offered into it. At
        the second the momentary closes: the two sum, what surfaces is one
        sign or the middle where they cancel, and the coupling turns to its
        next differing.
        """
        tot = sum(s for _, s in signs)
        if who in self.offered:
            return []                    # its turn at this differing is taken
        # A sign is offered or it is not, and **the not-offering is a turn
        # taken**, not a turn skipped: it is the middle kept. An even self's
        # whole surface sums to nought at every beat, so its every turn is the
        # not-offering — and a coupling where the not-offering could not take
        # a turn would be one no even self could ever stand at.
        self.offered[who] = 0 if tot == 0 else (1 if tot > 0 else -1)
        if len(self.offered) < 2:
            return []                    # the momentary is not made yet
        d = self.cursor % self.m
        self.cursor += 1
        self.tally[d] = sum(self.offered.values())
        for w in self.offered:
            self.touched.setdefault(w, []).append(d)
        self.offered = {}
        return [d]

    def surfaced(self, d):
        """The one sign at a differing, or the middle where they cancel."""
        t = self.tally.get(d, 0)
        return 0 if t == 0 else (1 if t > 0 else -1)

    def back_to(self, who):
        """What surfaced at the differings this self's own signs went into."""
        return [self.surfaced(d) for d in self.touched.get(who, ())]


def couple(selves, couplings, beats=2500, order=None):
    """Selves coupling through betweens that carry their own differings.

    `couplings` is {(i, j): Coupling} for each pair that couples. Each self
    opens at its own pace, offers into every coupling it stands at, and takes
    back at its own next positions. Nothing is stepped by anything and no
    position is identified with any other.
    """
    N = len(selves)
    turn = order if order is not None else list(range(N))
    for _ in range(beats):
        for c in couplings.values():
            c.commence()
        # who runs its own along at this turn, and who opens its across
        running, opened = [], set()
        for i in turn:
            s = selves[i]
            if not s.beats_now():
                continue                  # its own along has not come round
            running.append(i)
            if s.opens():
                opened.add(i)
                for (u, v), c in couplings.items():
                    if i in (u, v) and c.opens():
                        c.offer_in(i, s.offer())
        # every self that runs beats exactly once, its own along carrying and
        # whatever crossed to it arriving over it. A self that opened and
        # received nothing still runs its own; a beat missed is a self stilled
        # by the apparatus and not by anything of its own.
        for i in running:
            s = selves[i]
            back = []
            for (u, v), c in couplings.items():
                if i in (u, v):
                    other = v if i == u else u
                    for m in c.back_to(other):
                        if m != 0:
                            back.append((s.cursor % s.n, m))
                            s.cursor += 1
            s.take(back)
    return selves


def took(c, who):
    """What surfaced at the differings this self offered into, and clear."""
    ds = c.touched.pop(who, [])
    return [c.surfaced(d) for d in ds]


def made_a_middle(c, since):
    """Did a differing this coupling made since `since` surface as a middle."""
    return any(v == 0 for d, v in c.tally.items() if d >= since)


def all_pairs(n, m, alpha=None):
    return {(i, j): Coupling(m, alpha)
            for i in range(n) for j in range(i + 1, n)}
