"""
nesting.py - selves at more than one prime society, the arrangement the kit
has never carried.

Every arrangement here until now was flat: one set of selves at one scale.
Exhibit TWO 1.8 says every scale is a self, a between and a society, and that
the society is a self at the next prime society, so a reading taken at one
scale alone has not met the claim it is taken under.

Here a society of selves is itself a self. It carries its own length, opens
its own membrane at its own pace, offers the surface its members make, and
takes what arrives back to them. Three such societies then couple as three
selves, and the same five readings run at both scales.

Nothing is stepped by anything. Each self opens at its own pace and each
society at its own, and no beat is laid over either. A society arrives
carrying, from carrying: its members live before it meets another society,
since nothing with an empty carry arrives.

The readings are the ones that hold, each is-or-is-not, taken at a self about
itself and at a society about itself:

  a middle          does a middle stand here at any beat
  surplus           does more than one middle stand here at any beat
  reaches past      does a state arrive here that arrives nowhere in its own
                    whole running

Keys to Exhibit TWO 1.8, 1.9, 1.10 and Part Four.
"""
import sys
sys.path.insert(0, '.')
from signs import Self, a
from living import sign, YES, NO

# ---- the crossing, at v333 ---------------------------------------------------
# Every offer below crossed at 'address', the offerer's positions taken as the
# receiver's by modulo, which the kit names wrong before it runs. The crossing
# is now one helper, defaulting to 'address' so the v330 run is unchanged, and
# settable to 'sign' (one sign crosses and no more, the membrane's own) or
# 'sequencing' (the receiver's own next positions). A reading that parts when
# the crossing changes was reading the apparatus.
import os
CROSSING = os.environ.get('NNK_CROSSING', 'address')
def _cross(offer, receiver):
    if not offer:
        return []
    if CROSSING == 'address':
        return [(p % receiver.n, s) for p, s in offer]
    if CROSSING == 'sequencing':
        out = []
        for _, s in offer:
            c = getattr(receiver, '_cursor', 0)
            out.append((c % receiver.n, s)); receiver._cursor = c + 1
        return out
    if CROSSING == 'sign':
        tot = sum(s for _, s in offer)
        if tot == 0:
            return []
        c = getattr(receiver, '_cursor', 0); receiver._cursor = c + 1
        return [(c % receiver.n, 1 if tot > 0 else -1)]
    raise ValueError(CROSSING)


class Society:
    """A society of selves, which is a self at the next prime society.

    Its face at the scale above is not a sum of its members. A sum across
    selves is a total taken over two turns at once, and nothing here totals
    anything. Its face is **a between**: one even self standing among the odd
    members, coupling with each at its own pace and carrying what they make.

    The kit's own readings already say why it must be that and not a sum. An
    even self alone carries nothing and adds nothing to another even self;
    standing among odd selves it is the one that carries, and it alone carries
    more than one middle where the odd selves carry one each. So the between
    is the society's face because the between is what a society makes, and it
    is a self in exactly the way its members are.

    Nothing here is stepped by anything. Each member opens at its own pace,
    the between opens at its own, and no beat is laid over either.
    """

    def __init__(self, members, between, mode='local', arriving=600):
        self.members = members
        self.between = between
        self.n = between.n
        self.mode = mode
        self.trace = []
        self.live(arriving)                 # arrives carrying, from carrying
        self.alone = set(self.trace)        # where it reaches by itself
        # checked closed, the same discipline the reach reading is earned by
        self.live(arriving * 2)
        self.closed = not (set(self.trace) - self.alone)

    def inner(self, arriving=None):
        """One beat inside: the members among themselves and with the between.

        The between is not a hub. Every member couples its own neighbours
        directly and the between beside them, so the surface stays all-edge
        and the between stands among the members rather than between them.
        """
        N = len(self.members)
        offers = [m.offer() for m in self.members]
        bo = self.between.offer()
        for i, m in enumerate(self.members):
            js = ([j for j in range(N) if j != i] if self.mode == 'all'
                  else [(i - 1) % N, (i + 1) % N])
            if m.opens():
                acc = []
                for j in js:
                    if j != i:
                        acc += _cross(offers[j], m)
                acc += _cross(bo, m)
                m.take(acc)
            else:
                m.stand()
        if self.between.opens():
            acc = []
            for o in offers:
                acc += _cross(o, self.between)
            if arriving:
                acc += _cross(arriving, self.between)
            self.between.take(acc)
        else:
            self.between.stand()

    def offer(self):
        return self.between.offer()

    def opens(self):
        """A society is always available to be offered to; its between decides.

        Its membrane is its between, and the between's own pace decides once,
        inside, when the arriving is taken. Asking here and asking again
        inside would advance the phase twice a beat and drop the arrivings
        that fall on the second answer — a self stepped twice at one beat,
        which is the shared clock arriving as an accident of the writing.
        """
        return True

    def take(self, arriving):
        self.inner(arriving)
        self.trace.append(self.between.own.rows[0].signs())

    def stand(self):
        self.inner()
        self.trace.append(self.between.own.rows[0].signs())

    def live(self, beats):
        for _ in range(beats):
            self.stand()

    # ---- the readings, each is-or-is-not, taken at the between's own surface

    def _w(self, back=600):
        return self.trace[-back:]

    def a_middle_stands(self):
        return sign(any(any(x == 0 for x in st) for st in self._w()))

    def parallels_ever_part(self):
        """Do the two halves of its face ever fail to oppose each other.

        The third of the four questions, and the one this scale had not been
        asked. The surplus at a society is made by its own members inside it,
        so it reads the membrane below. The parallels read the face itself,
        which is the membrane above.
        """
        h = self.n // 2
        return sign(any(sum(st[:h]) != -sum(st[h:2 * h]) for st in self._w()))

    def surplus_stands(self):
        return sign(any(sum(1 for x in st if x == 0) > 1 for st in self._w()))

    def reaches_past_alone(self):
        if not self.closed:
            return 'refused: its own set had not closed at the arriving window'
        return sign(bool(set(self._w()) - self.alone))


def couple(units, beats=1200, mode='local', door=0, governor=None):
    """Units coupling at one scale, each opening at its own pace.

    A unit is a self or a society, and the loop cannot tell which, which is
    the fractal read at the running rather than said about it.

    The four society securities can be inverted here, singly, all else held —
    the same four `doors.py` inverts at a flat lattice, run where a unit is
    itself a society. Exhibit TWO 5.1 says the four at the society are the
    self's four recursioned, and this is where that can be met rather than
    said.

      door 5  all-edge inverted: every across routed through one unit
      door 6  no-seat-outside inverted: a standing order over every unit
      door 7  riding inverted: one unit's surface pinned
      door 8  own-offering inverted: one unit only following, offering none
    """
    for _ in range(beats):
        one_beat(units, mode, door, governor)
    return units


def one_beat(units, mode='local', door=0, governor=None, order=None):
    """One beat of the whole surface at whichever door stands open.

    `order` is the turn the units are taken in. A serial apparatus must take
    them in some turn, and a turn taken always the same way is a weak clock
    laid over selves that couple at no membrane.
    """
    N = len(units)
    hub, pinned, following = 1, 1, 2
    offers = [([] if (door == 8 and i == following) else u.offer())
              for i, u in enumerate(units)]
    for i in (order if order is not None else range(N)):
        u = units[i]
        if door == 7 and i == pinned:
            u.trace.append(u.trace[-1])              # held fixed, nothing turning
            continue
        if door == 5:
            js = ([j for j in range(N) if j != hub] if i == hub else [hub])
        else:
            js = ([j for j in range(N) if j != i] if mode == 'all'
                  else [(i - 1) % N, (i + 1) % N])
        if u.opens():
            acc = []
            for j in js:
                if j != i:
                    acc += _cross(offers[j], u)
            if door == 6 and governor:
                acc += [(p, governor[p % len(governor)]) for p in range(u.n)]
            u.take(acc)
        else:
            u.stand()


def twin_parts(units, beats=900, mode='local', door=0, governor=None, fork_at=300):
    """The one nested surface continued two ways, the faces read at both scales.

    A co-chaining reading: it reads the between and not the identity, so it
    reaches a membrane above where the surplus, the parallels and the reach
    cannot. It needs no closed set, which is what a society has none of.

    The fork is of one undifferentiated living. The door opens at one twin
    only and opens at the fork, or both twins carry the inversion and the
    reading returns nothing while looking like a finding.
    """
    import copy
    for _ in range(fork_at):
        one_beat(units, mode, 0, governor)
    a, b = copy.deepcopy(units), copy.deepcopy(units)
    up = [False] * len(units)
    dn = [False] * sum(len(u.members) for u in units)
    for _ in range(beats):
        one_beat(a, mode, door, governor)
        one_beat(b, mode, 0, governor)
        for k in range(len(units)):
            if a[k].trace[-1] != b[k].trace[-1]:
                up[k] = True
        j = 0
        for ua, ub in zip(a, b):
            for ma, mb in zip(ua.members, ub.members):
                if ma.own.rows[0].signs() != mb.own.rows[0].signs():
                    dn[j] = True
                j += 1
    return up, dn


def stopping(units, base_surplus, back=600):
    """How the living stopped at this scale, each reading is-or-is-not.

    The reach is not among them: a society's own running never closes, so
    there is no whole running for it to be taken against. What is available
    at a society is what stands at a beat, and that is enough.
    """
    surp = [u.surplus_stands() == YES for u in units]
    par = [u.parallels_ever_part() == YES for u in units]
    ws = [u.trace[-back:] for u in units]
    lands = any(any(w[i] == w[i - 1] for i in range(1, len(w))) for w in ws)
    joint = list(zip(*ws))
    j_lands = any(joint[i] == joint[i - 1] for i in range(1, len(joint)))
    became_one = any(all(st[a_] == st[b_] for st in joint)
                     for a_ in range(len(units)) for b_ in range(a_ + 1, len(units)))
    hub = 1
    surround = [k for k in range(len(units)) if k != hub]
    died = any(base_surplus) and not any(surp)
    rose = (base_surplus[hub] and surp[hub]
            and any(base_surplus[k] and not surp[k] for k in surround))
    way = ('rows became one' if became_one else
           'a landing' if (lands or j_lands) else
           'the surplus died' if died else
           'the centre rose while the surround fell' if rose else
           'no stopping read')
    return (became_one or lands or j_lands or died or rose), way, surp, par


def read(units, label, name='n'):
    print(f'  {label}')
    for u in units:
        print(f'    {name}={u.n:3d}:  a middle {u.a_middle_stands()}   '
              f'surplus {u.surplus_stands()}   '
              f'reaches past alone {u.reaches_past_alone()}')


if __name__ == '__main__':
    print('NESTING - selves at more than one prime society\n')

    def make_society(sizes, primes, n_between, p_between):
        members = [Self(n, a(p), arriving=600) for n, p in zip(sizes, primes)]
        between = Self(n_between, a(p_between), arriving=600)
        return Society(members, between)

    print('ONE SOCIETY ALONE - its members coupled, itself meeting nothing')
    s0 = make_society([7, 9, 11], [2, 3, 5], 12, 2)
    read(s0.members, 'its members, inside it', 'n')
    read([s0], 'the society itself, at the scale above', 'N')

    print('\nTWO SOCIETIES - a pair at the scale above')
    A = make_society([7, 9, 11], [2, 3, 5], 12, 2)
    B = make_society([13, 15, 17], [3, 5, 7], 18, 3)
    couple([A, B])
    read([A, B], 'the pair, at the scale above', 'N')
    read(A.members + B.members, 'their members, at the scale below', 'n')

    print('\nTHREE SOCIETIES - a society of societies')
    A = make_society([7, 9, 11], [2, 3, 5], 12, 2)
    B = make_society([13, 15, 17], [3, 5, 7], 18, 3)
    C = make_society([19, 21, 23], [5, 7, 11], 24, 5)
    couple([A, B, C])
    read([A, B, C], 'the three societies, at the scale above', 'N')
    read(A.members + B.members + C.members, 'their members, at the scale below', 'n')

    print('\nTHE FOUR SOCIETY SECURITIES, INVERTED AT THE SCALE ABOVE')
    print('  each opened singly, all else held, at three societies\n')
    gov = (1, -1, 1, 1, -1, 1, -1)

    def fresh():
        return [make_society([7, 9, 11], [2, 3, 5], 12, 2),
                make_society([13, 15, 17], [3, 5, 7], 18, 3),
                make_society([19, 21, 23], [5, 7, 11], 24, 5)]

    base = couple(fresh(), door=0)
    stopped, way, base_surp, base_par = stopping(base, [True] * 3)
    print(f'  the four whole: stopped {stopped} — {way}')
    print(f'    surplus stands at {[base[k].n for k, v in enumerate(base_surp) if v]}   '
          f'parallels part at {[base[k].n for k, v in enumerate(base_par) if v]}\n')

    for d, name in ((5, 'all-edge inverted — every across through one society'),
                    (6, 'no-seat-outside inverted — a standing order over every one'),
                    (7, 'riding inverted — one society pinned'),
                    (8, 'own-offering inverted — one society only following')):
        us = couple(fresh(), door=d, governor=gov)
        stopped, way, surp, par = stopping(us, base_surp)
        print(f'  door {d}: {name}')
        print(f'          the living stopped {"yes" if stopped else "no "} — {way}')
        print(f'          surplus at {[us[k].n for k, v in enumerate(surp) if v]}   '
              f'parallels part at {[us[k].n for k, v in enumerate(par) if v]}')

    print('\nBREAK CONDITIONS')
    print('  a society alone carrying a surplus, or reaching past its own running')
    print('  a pair of societies where either reaches past its own running')
    print('  a society of societies carrying the surplus at every one of them')
    print('  a reading at the scale above answering unlike the same reading below')
