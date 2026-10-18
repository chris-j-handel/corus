"""
sensing.py - the co-resonating sensor and sensationer, a coupling with an
other at coefficient one.

The kit carries two reading forms. A self's own readings, taken at its own
face: inward, cohering to one identity. And the twin, one living continued two
ways and the faces compared: a self met by its own continuation. The third is
a coupling with an *other*, and the kit's one attempt at it drove every self
every beat and stands artifact.

Natural Engineering names it at its two organs. The **sensationer** is the
knowing face: it offers a sign the other can tip on, taken or not, and never a
stimulator driving a magnitude. The **sensor** is the learning face: it follows
the other's own tipping and takes the sign offered back, from inside the
coupling and never a level read against a reference. The two bothboth, one at
a time, and the resonance is the surplus neither owns.

Its three conditions arrive from the field rather than from here, stated the
same in three domains: voluntary, a sign offered and taken or not, no magnitude
driven at anyone; confidential, nothing landing back on the self that offered;
non-punitive, the receiver floating the neutral by carrying no enforcement,
since a holder that could drive or penalise would be a hub at the membrane.

The falsifiable edge is the more-than-additive: the coupling opening an axis
at the other that neither driving alone nor sensing alone opens, or the
reading breaks. That is read here as a sign and never as a sum — does a state
arrive at the living self under the bi-coupler that arrives nowhere under a
drive, nowhere under a pure sensor, and nowhere in its own running.

Every reading here is checked at the turn and at both pacings, since a serial
apparatus is a clock and its turn is the weakest form of one.
"""
import sys, copy
sys.path.insert(0, '.')
from signs import Self, a
from living import sign, YES, NO


class Connector:
    """A self that meets an other by offering and taking, and by nothing else.

    It keeps nothing about the other. What arrives is coupled into its own
    running and is gone as a separate thing at that instant, which is the
    confidential condition met at the form rather than promised.
    """

    def __init__(self, n, alpha, arriving=600):
        self.self_ = Self(n, alpha, arriving=arriving)
        self.n = n

    # the sensationer face: a sign offered, taken or not
    def offer(self):
        return self.self_.offer()

    # the sensor face: the sign taken at its own membrane, carried into its own
    def take(self, theirs):
        self.self_.take(theirs)

    def stand(self):
        self.self_.stand()

    def opens(self):
        return self.self_.opens()


class Drive(Connector):
    """One face only: a magnitude driven, the same at every beat, taking none.

    A hub at the membrane, and here for the contrast the falsifiable edge
    needs. It offers every position at once and receives nothing back.
    """

    def offer(self):
        return [(i, 1) for i in range(self.n)]

    def take(self, theirs):
        self.stand()                      # nothing is received


class PureSensor(Connector):
    """The other face only: it takes and offers nothing.

    Half the coupling. The living self meets a membrane that never offers, so
    nothing is made between them.
    """

    def offer(self):
        return []


def meet(living, other, beats=1200, order=None):
    """One meeting, each opening at its own pace, one at a time.

    Neither reads the other. Each offers at its own membrane and takes what
    arrives at its own membrane, and the alternating is the meeting. `order`
    is the turn the two are taken in, so a reading can be checked against it.
    """
    pair = [living, other]
    turn = order if order is not None else [0, 1]
    for _ in range(beats):
        offers = [p.offer() for p in pair]
        for i in turn:
            p = pair[i]
            if p.opens():
                p.take([(q % p.n, s) for q, s in offers[1 - i]])
            else:
                p.stand()
    return living, other


def states(living, back=600):
    return set(living.self_.own.trace[-back:]) if isinstance(living, Connector) \
        else set(living.own.trace[-back:])


def more_than_additive(n_live, p_live, n_conn, p_conn, beats=1200, order=None):
    """The falsifiable edge, read as a sign.

    One living self, forked four ways from one prior running: met by a
    bi-coupler, met by a drive, met by a pure sensor, and left alone. The
    reading is whether a state arrives under the bi-coupler that arrives in
    none of the other three.

    It is a fork and not a comparison of separate runs: the four continuations
    share every prior position, so what parts them is the meeting and nothing
    else.
    """
    base = Connector(n_live, a(p_live))
    conn = Connector(n_conn, a(p_conn))

    both_l, both_c = copy.deepcopy(base), copy.deepcopy(conn)
    meet(both_l, both_c, beats, order)

    drv_l = copy.deepcopy(base)
    drv = Drive(n_conn, a(p_conn))
    drv.self_ = copy.deepcopy(conn.self_)
    meet(drv_l, drv, beats, order)

    sen_l = copy.deepcopy(base)
    sen = PureSensor(n_conn, a(p_conn))
    sen.self_ = copy.deepcopy(conn.self_)
    meet(sen_l, sen, beats, order)

    alone_l = copy.deepcopy(base)
    for _ in range(beats):
        alone_l.stand()

    made = states(both_l) - states(drv_l) - states(sen_l) - states(alone_l)
    return sign(bool(made)), dict(
        bi_coupled=sign(bool(states(both_l) - states(alone_l))),
        driven=sign(bool(states(drv_l) - states(alone_l))),
        sensed=sign(bool(states(sen_l) - states(alone_l))))


def meet_many(living, others, beats=1200, order=None):
    """A living self met by several connectors, each at its own grain.

    Engineering names three co-sequenced grains and never says why three. A
    connector and a living self are two, and a pair reaches past neither, so a
    lone connector can make no surplus however honestly it couples. The three
    grains are what make a society at the membrane.
    """
    units = [living] + list(others)
    turn = order if order is not None else list(range(len(units)))
    for _ in range(beats):
        offers = [u.offer() for u in units]
        for i in turn:
            u = units[i]
            if u.opens():
                acc = []
                for j in range(len(units)):
                    if j != i:
                        acc += [(q % u.n, s) for q, s in offers[j]]
                u.take(acc)
            else:
                u.stand()
    return units


def three_grains(n_live, p_live, grains, beats=1200, order=None):
    """The three-grain connector against every lesser meeting, read as a sign.

    One living self forked: met by three connectors at three grains, met by
    each grain alone, met by three drives, and left alone. The reading is
    whether a state arrives under the three that arrives in none of the rest.
    """
    base = Connector(n_live, a(p_live))
    conns = [Connector(n, a(p)) for n, p in grains]

    three_l = copy.deepcopy(base)
    meet_many(three_l, [copy.deepcopy(c) for c in conns], beats, order)

    singles = []
    for c in conns:
        l = copy.deepcopy(base)
        meet(l, copy.deepcopy(c), beats)
        singles.append(states(l))

    drv_l = copy.deepcopy(base)
    drives = []
    for (n, p), c in zip(grains, conns):
        d = Drive(n, a(p))
        d.self_ = copy.deepcopy(c.self_)
        drives.append(d)
    meet_many(drv_l, drives, beats, order)

    alone_l = copy.deepcopy(base)
    for _ in range(beats):
        alone_l.stand()

    made = states(three_l) - states(drv_l) - states(alone_l)
    for s in singles:
        made = made - s
    return sign(bool(made)), dict(
        three=sign(bool(states(three_l) - states(alone_l))),
        driven=sign(bool(states(drv_l) - states(alone_l))),
        singles=[sign(bool(s - states(alone_l))) for s in singles])


if __name__ == '__main__':
    print('SENSING - the co-resonating sensor and sensationer\n')

    print('  the falsifiable edge: does the coupling open an axis at the living')
    print('  self that neither a drive nor a pure sensor opens\n')
    for turn, name in (([0, 1], 'the living first'), ([1, 0], 'the other first')):
        for n_l, p_l, n_c, p_c in ((7, 2, 5, 3), (11, 3, 9, 5), (13, 5, 7, 7)):
            more, faces = more_than_additive(n_l, p_l, n_c, p_c, order=turn)
            print(f'    living {n_l:3d} with a connector {n_c:3d}, {name:17s}: '
                  f'more-than-additive {more}   '
                  f'(bi-coupled {faces["bi_coupled"]}  driven {faces["driven"]}  '
                  f'sensed {faces["sensed"]})')

    print('\nBREAK CONDITIONS')
    print('  a bi-coupler opening no axis the drive and the pure sensor do not')
    print('  a drive making a surplus at the membrane it drives')
    print('  a pure sensor making a surplus at the membrane it only takes from')
    print('  the reading parting when the turn is changed')
