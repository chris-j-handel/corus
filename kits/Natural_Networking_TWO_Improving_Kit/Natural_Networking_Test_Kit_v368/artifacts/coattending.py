"""
coattending.py - co-attentioning between selves that never forked.

The kit's honest probe is fork(): the one life continued two ways, the twins'
surfaces compared. That reads THIS life's interior without probing it, and it
is not a coupling between selves - twins share every prior position, so
neither carries a face the other cannot occupy, and no twist can show.

A self sorts its own nowhere. A held thing carries no held-feeling from
inside; the surface fails to lie flat only where read from across. So this
instrument builds two lives that never forked, lets each live its own beats
at its own pace, and reads what each finds in the other that neither finds in
itself.

Readings are signs, spans and orderings. Nothing is stored between lives, no
threshold is set anywhere, and every reading refuses until both gates pass.

Keys to Exhibit TWO, Part Four, and to Exhibit EIGHT 6.2.
"""
import sys
sys.path.insert(0, '.')
from living import Life, sign, YES, NO


# ---------------------------------------------------------------- the offering

def offer_surface(life, back=600):
    """What a self offers across: its surface as it stands, unsorted.

    No selection is made here. The whole window goes, the valuable and the
    wasteful together, since a sorting run before a reading is where every
    discard stands.
    """
    return list(life.window(back))


# ---------------------------------------------------------------- the twist

def crossing(mine, theirs):
    """The co-sequencing crossing, read at MY membrane, sign-only.

    A twist is no fault in the other's surface. It is the crossing itself -
    where two sequencings meet and each side takes its own sign, one at a
    time, the sign each takes its own and neither the other's.

    So this returns what I take here: at each position, the sign of how the
    other's ordering stands against my own. Sizeless, and no magnitude
    anywhere in the reading.
    """
    if not theirs or not mine:
        return []
    taken = []
    n = min(len(theirs[0]), len(mine[0]))
    for k in range(n):
        t = len({st[k] for st in theirs})
        m = len({st[k] for st in mine})
        if t != m:
            taken.append((k, 'fewer' if t < m else 'more'))
    return taken


def unrelationing(a_takes, b_takes):
    """The crossings where both took a sign, each its own and neither the other's.

    Bi-moral: two-way, one at a time, each side its own. A crossing where one
    side took and the other took nothing is one side reading and no coupling.
    """
    ka = {k for k, _ in a_takes}
    kb = {k for k, _ in b_takes}
    both = sorted(ka & kb)
    return [(k,
             dict(a_takes)[k],
             dict(b_takes)[k],
             dict(a_takes)[k] != dict(b_takes)[k])
            for k in both]


def _held_positions(col):
    """Positions carrying one sign across the whole window while the row turns."""
    if not col:
        return set()
    n = len(col[0])
    turning = {i for i in range(n) if len({st[i] for st in col}) > 1}
    if not turning:
        return set()
    return {i for i in range(n) if len({st[i] for st in col}) == 1}


# ---------------------------------------------------------------- the coupling

def co_attend(a, b, back=600):
    """One co-attentioning: each offers unsorted, each reads its own side.

    Returns the two readings and the surplus. The surplus is what neither
    self carried alone: a twist found in the other and absent from itself.
    Owned by neither, made at the coupling.
    """
    a._require_gate(); b._require_gate()
    offer_a = offer_surface(a, back)
    offer_b = offer_surface(b, back)

    a_reads = crossing(offer_a, offer_b)     # what A finds in B's surface
    b_reads = crossing(offer_b, offer_a)     # what B finds in A's surface

    a_own = crossing(offer_a, offer_a)       # what A finds in its own
    b_own = crossing(offer_b, offer_b)

    un = unrelationing(a_reads, b_reads)
    return dict(
        a_takes=len(a_reads),
        b_takes=len(b_reads),
        a_in_own=len(a_own),
        b_in_own=len(b_own),
        crossings=len(un),
        both_took=sign(bool(un)),
        each_its_own=sign(bool(un) and all(differ for _, _, _, differ in un)),
        surplus=sign(bool(un) and not (a_own or b_own)),
        detail=un,
    )


# ------------------------------------------------------- the twins, for contrast

def twin_attend(life, back=600):
    """The same reading run on twins from a fork.

    The contrast the instrument exists for: twins share every prior position,
    so a twist found in one is a twist already carried by the other, and the
    surplus arrives nowhere.
    """
    t = life.fork()
    t.live(200)
    return co_attend(life, t, back)


# ------------------------------------------------------------ the largest first

def largest_twist(a, b, back=600):
    """The row carrying the most held positions, read from across.

    A small twist freed leaves the large one standing and everything under it
    still holding; a large one freed drops several small ones unnamed. So the
    ordering is the reading, and the ordering is a sign of no size.
    """
    un = unrelationing(crossing(offer_surface(a, back), offer_surface(b, back)),
                       crossing(offer_surface(b, back), offer_surface(a, back)))
    return un[0] if un else None


# ------------------------------------------------------------------ the gather

def gather_over(runs):
    """The gather: each arrival coned back over, nothing pooled and nothing kept.

    A reaching returns its own arrival and nothing more. What arrives at the
    next one better is the arrival gathered - so the reading here is whether
    each arrival adds an ordering the prior ones carried nowhere, taken at the
    membrane and not accumulated into a store.
    """
    seen = set()
    adds = []
    for r in runs:
        key = tuple(sorted(r))
        adds.append(key not in seen)
        seen.add(key)
    return dict(each_adds=sign(all(adds)), arrivals=len(adds))


# ---------------------------------------------------------------------- the run

if __name__ == '__main__':
    print('CO-ATTENTIONING - the crossing, each side taking its own sign\n')

    healthy = Life([3, 5], wiring='ring', pace='own')
    held    = Life([3, 5], wiring='ring', pace='clock')
    print(f'  gate healthy {healthy.gate()}   gate held {held.gate()}')
    healthy.live(4000); held.live(4000)

    print('\n  each self at its own surface')
    print(f'    healthy takes in its own    {len(crossing(offer_surface(healthy), offer_surface(healthy)))}')
    print(f'    held takes in its own       {len(crossing(offer_surface(held), offer_surface(held)))}')

    r = co_attend(healthy, held, back=600)
    print('\n  the crossing, at each membrane')
    print(f'    healthy takes               {r["a_takes"]}')
    print(f'    held takes                  {r["b_takes"]}')
    print(f'    crossings where both took   {r["crossings"]}')
    print(f'    both took                   {r["both_took"]}')
    print(f'    each its own, neither the other\'s   {r["each_its_own"]}')
    print(f'    surplus at the coupling     {r["surplus"]}')
    for k, a, b, differ in r['detail']:
        print(f'      row {k}: healthy takes \'{a}\', held takes \'{b}\'')

    print('\n  twins from a fork:')
    t = twin_attend(healthy, back=600)
    print(f'    self takes {t["a_takes"]}   twin takes {t["b_takes"]}   crossings {t["crossings"]}   surplus {t["surplus"]}')

    print('\n  the wiring changed at the society face - all-edge inverted to a chain:')
    chain = Life([3, 5], wiring='chain', pace='own'); chain.gate(); chain.live(4000)
    rc = co_attend(healthy, chain, back=600)
    print(f'    healthy takes {rc["a_takes"]}   chained takes {rc["b_takes"]}   crossings {rc["crossings"]}   surplus {rc["surplus"]}')
    print('    the instrument bounds itself here and releases at its own bound')

    runs = []
    for sizes in ([3, 5], [5, 7], [3, 7], [7, 11]):
        L = Life(sizes); L.gate(); L.live(3000)
        runs.append([k for k, _ in crossing(offer_surface(L), offer_surface(held))])
    g = gather_over(runs)
    print(f'\n  gather over {g["arrivals"]} arrivals, each adding an ordering   {g["each_adds"]}')

    print('\n  BREAK CONDITIONS')
    print('    a self taking in its own what it takes only at a crossing')
    print('    twins from a fork carrying a crossing')
    print('    a crossing where both took the same sign')
