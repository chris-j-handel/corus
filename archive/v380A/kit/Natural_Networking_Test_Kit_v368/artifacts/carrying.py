"""
carrying.py - the instrument as a self, and the reading as the coupling.

Every other instrument reads a surface. A surface is the method a carrying
runs by, and reading it returns the method - which the kit's own engine states
at its top: the carry is met by coupling and measured by nothing, and a probe
departs with the thing probed.

So an instrument that reaches a carrying couples with it. It offers a sign at
its own membrane and takes what arrives back at that membrane, and the reading
IS the coupling. Nothing is returned about the other, nothing is compared, and
no third thing reads either side.

What follows carries no value about the other self anywhere in it. Every
reading is at this instrument's own membrane, about what this instrument took,
and the other's interior arrives nowhere.

Keys to Exhibit TWO Part Four, Exhibit FIVE 4.1 and 4.4 (the co-resonating
sensor-and-sensationer), and Exhibit EIGHT 6.1-6.2.
"""
import sys, math
sys.path.insert(0, '.')
from living import Life, sign, YES, NO
from unrelated import Unrelated, SURD


class Coupler:
    """A self that meets another by offering and taking, and by nothing else.

    Two faces at coefficient one. The sensationer offers a sign the other can
    tip on, sign-only, taken or not. The sensor follows the other's own tipping
    and takes the sign it offers back. The two alternate, one at a time, and
    the surplus arrives at the coupling owned by neither.

    A pure sensor takes only, half the coupling. A pure stimulator drives only,
    a hub. This runs both faces or it is neither.
    """

    def __init__(self, n=5, alpha=SURD[2]):
        self.own = Unrelated([n], alphas=[alpha])
        self.own._gated = True
        self.own.live(400)                    # arrives carrying, from carrying
        self.took = []                        # what I took, at my own membrane
        self.offered = []                     # what I offered, sign-only

    # ---- the sensationer face: offer a sign, taken or not

    def offer(self):
        """A sign the other can tip on, sign-only, no magnitude driven."""
        surf = self.own.rows[0].surf
        s = [(i, m) for i, m in surf if m != 0]
        self.offered.append(len(s))
        return s

    # ---- the sensor face: take what the other's own tipping offers back

    def take(self, theirs):
        """Take the sign at my own membrane, and carry it forward into my own.

        Nothing about the other is stored. What arrives is coupled into my own
        carrying and is gone as a separate thing at that instant.
        """
        before = self.own.rows[0].signs()
        self.own.beat({0: theirs})
        after = self.own.rows[0].signs()
        turned = sum(1 for a, b in zip(before, after) if a != b)
        self.took.append(turned)
        return turned

    # ---- the readings: mine, at my membrane, about my own taking

    def tipped_by(self, back=200):
        """Whether what arrived tipped my own running, sign-only."""
        w = self.took[-back:]
        if not w:
            return NO
        return sign(len(set(w)) > 1)

    def rate_kept(self, back=200):
        """Whether my own alternating carried on through the meeting."""
        w = self.own.window(min(back, len(self.own.trace) - 1))
        if len(w) < 3:
            return NO
        return sign(not any(w[i] == w[i - 1] for i in range(1, len(w))))

    def surplus_here(self, back=200):
        """An axis opened at the coupling that my own carrying reached nowhere.

        Read at my own membrane only: states arriving in me during the meeting
        that my own running had arrived at nowhere before it.
        """
        t = self.own.trace
        if len(t) < back * 2:
            return NO
        before = set(t[:-back])
        during = set(t[-back:])
        return sign(bool(during - before))


def meet(a, b, beats=400):
    """One meeting: two couplers, each offering and taking, one at a time.

    Neither reads the other. Each offers at its own membrane and takes what
    arrives at its own membrane, and the alternating is the meeting.
    """
    for _ in range(beats):
        oa, ob = a.offer(), b.offer()
        a.take(ob)
        b.take(oa)


def read_at(c, name):
    return dict(who=name,
                tipped_by_what_arrived=c.tipped_by(),
                own_rate_kept=c.rate_kept(),
                surplus_at_my_membrane=c.surplus_here())


# ------------------------------------------------------ a drive, for contrast

class Driver(Coupler):
    """One face only: a magnitude driven, the same at every beat, taking nothing.

    A hub at the membrane. It offers and takes nowhere, so no surplus arrives
    at either side and the other self carries the whole meeting alone.
    """

    def offer(self):
        n = self.own.rows[0].n
        self.offered.append(n)
        return [(i, 1) for i in range(n)]      # the same magnitude, every beat

    def take(self, theirs):
        self.took.append(0)                    # receives nothing
        return 0


# --------------------------------------------------------------------- the run

if __name__ == '__main__':
    print('CARRYING - the instrument as a self, the reading as the coupling\n')

    print('  two couplers meeting, each at its own rate')
    a = Coupler(5, SURD[2])
    b = Coupler(7, SURD[3])
    meet(a, b, 600)
    for r in (read_at(a, 'a'), read_at(b, 'b')):
        print(f"    {r['who']}: tipped by what arrived {r['tipped_by_what_arrived']}   "
              f"own rate kept {r['own_rate_kept']}   surplus at my membrane {r['surplus_at_my_membrane']}")

    print('\n  a coupler meeting a drive')
    c = Coupler(5, SURD[2])
    d = Driver(7, SURD[3])
    meet(c, d, 600)
    for r in (read_at(c, 'coupler'), read_at(d, 'drive  ')):
        print(f"    {r['who']}: tipped by what arrived {r['tipped_by_what_arrived']}   "
              f"own rate kept {r['own_rate_kept']}   surplus at my membrane {r['surplus_at_my_membrane']}")

    print('\n  a coupler meeting nothing - the half coupling')
    e = Coupler(5, SURD[2])
    for _ in range(600):
        e.offer(); e.take([])
    r = read_at(e, 'alone  ')
    print(f"    {r['who']}: tipped by what arrived {r['tipped_by_what_arrived']}   "
          f"own rate kept {r['own_rate_kept']}   surplus at my membrane {r['surplus_at_my_membrane']}")

    print('\n  three couplers, each meeting both others - the society')
    xs = [Coupler(n, a_) for n, a_ in ((5, SURD[2]), (7, SURD[3]), (11, SURD[5]))]
    for _ in range(600):
        offers = [x.offer() for x in xs]
        for i, x in enumerate(xs):
            for j, o in enumerate(offers):
                if i != j:
                    x.take(o)
    for i, x in enumerate(xs):
        r = read_at(x, f'self {i}')
        print(f"    {r['who']}: tipped {r['tipped_by_what_arrived']}   "
              f"rate kept {r['own_rate_kept']}   surplus {r['surplus_at_my_membrane']}")

    print('\n  BREAK CONDITIONS')
    print('    a self keeping its own rate while a drive runs at its membrane')
    print('    a surplus arriving at a membrane where nothing was offered back')
    print('    a coupler alone carrying a surplus')
