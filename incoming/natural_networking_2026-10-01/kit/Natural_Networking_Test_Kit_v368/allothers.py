"""
allothers.py - the seven is the all-others, from wherever the observing falls.

Seven is no subset of eight and no list of seven items. It is whichever seven
the observed one is not, and it re-forms at every observing: any of the eight
can be the one observed, and the all-others is seven at every one of them.

So the reading is one question asked eight times, answered yes or no at each -
never nineteen items sorted into buckets, which is a list-sorting result and
reads nothing about a form whose seven re-forms at each arrival.

And the all-others is no background to the one observed. It carries and
attentions both, at two scales at once - the local coupling and the global
surface, each riding the other's carry, the surplus of one stroke the drive of
the next. The one observed runs in it rather than over it.

  carrying      does the all-others carry - the living running on, arriving
                at positions and re-arriving, landing nowhere
  attentioning  does the all-others attention - a middle standing, the carry
                aging to its own bound

The baseline is verified byte-identical to Exhibit ONE before any
door is opened, as doors.py does.

Keys to Exhibit TWO Part Five, Natural Intelligence 1.13, and Exhibit EIGHT
4.3-4.4.
"""
import sys
sys.path.insert(0, '.')
from doors import run, bi_coupling_v
from resolver import _1_self_coupling as resolver_one

YN = {True: 'yes', False: 'no '}

DOORS = {
    1: 'self-bounding    the carry ages to its bound and releases',
    2: 'self-negation    the sign inverts at the membrane',
    3: 'sign-only        the selection a sign, sizeless',
    4: 'own-time         each row on its own pace',
    5: 'all-edge         every row couples its neighbours directly',
    6: 'no-seat-outside  no standing order imposed',
    7: 'riding, unpinned every row its own surface',
    8: 'own-offering     every row offers its own along',
}


def baseline_verified():
    """Exhibit ONE, byte-identical, before any door is opened."""
    import random
    random.seed(7)
    for _ in range(40):
        W = random.choice((3, 4, 5, 7))
        acc = [(random.randrange(W), random.choice((-1, 1)))
               for _ in range(random.randrange(1, 6))]
        car = [(random.randrange(W), random.choice((-1, 1)), random.choice((-1, 0, 1)),
                random.randrange(4)) for _ in range(random.randrange(0, 4))]
        if bi_coupling_v(car, acc) != resolver_one(car, acc):
            return False
    return True


# --------------------------------------------------------- the two faces read

def carrying(trace, observed, back=400):
    """Does the all-others carry - running on, landing nowhere.

    Read at every row except the one observed. Landing is a state repeating
    at the next beat, and a carrying lands nowhere.
    """
    w = trace[-back:]
    others = [k for k in range(len(w[0])) if k != observed]
    if not others:
        return False
    cols = [tuple(tuple(st[k] for k in others)) for st in w]
    return not any(cols[i] == cols[i - 1] for i in range(1, len(cols)))


def attentioning(trace, observed, back=400):
    """Does the all-others attention - a middle standing at it.

    A middle is a position carrying neither sign: the carry aged to its own
    bound and released there. Read across the all-others together, since the
    all-others is one alternating at its faces and not seven separate rows.
    """
    w = trace[-back:]
    others = [k for k in range(len(w[0])) if k != observed]
    return any(any(x == 0 for k in others for x in st[k]) for st in w)


# --------------------------------------------------------------------- the run

if __name__ == '__main__':
    print('THE ALL-OTHERS - one question, asked at each of the eight\n')

    print(f'  baseline byte-identical to Exhibit ONE: {YN[baseline_verified()]}\n')

    sizes = [3, 5, 7, 11]
    gov = [1, -1, 1, -1, 1]

    print('  WITH THE EIGHT WHOLE - the observing moved around the ring of rows')
    whole = run(sizes, 3000)
    for observed in range(len(sizes)):
        c = carrying(whole, observed)
        a = attentioning(whole, observed)
        print(f'    observing row {observed} (n={sizes[observed]:2d}): '
              f'all-others carrying {YN[c]}   attentioning {YN[a]}   both {YN[c and a]}')

    print('\n  EACH DOOR OPENED SINGLY - all-others read at every row in turn')
    for d in sorted(DOORS):
        tr = run(sizes, 3000, door=d, governor=gov)
        both = [carrying(tr, k) and attentioning(tr, k) for k in range(len(sizes))]
        allboth = all(both)
        print(f'    door {d} {DOORS[d][:17]}: both at every observing {YN[allboth]}   '
              f'per row {[YN[b].strip() for b in both]}')

    print('\n  BREAK CONDITIONS')
    print('    the eight whole, and the all-others failing either face at any observing')
    print('    a door opened, and the all-others carrying both at every observing')
    print('    a reading differing with which row is observed while the eight stand whole')
