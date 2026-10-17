"""
transmissioning.py - three phases, two one-ways each, and the co-chaining extending.

The bi-morality is six: two ways, three each way, one at a time, sequenced,
cycling - both ways forward, neither the reverse of the other. Three phases
carrying two one-ways each is that six at the network surface.

A three-torus carries three windings and drops the two-way at each: its group
is three generators, commuting, each a single direction. So the accounting box
is the six with one way removed at each of the three, and the removing is the
invisibling - six arriving as three, the three ledgers, each one-way, each
carrying its pair of characters.

This instrument runs both and reads the difference:

  two-way   each row offers to both neighbours and receives from both
  one-way   each row offers to one neighbour only, the return removed

and then extends the co-chaining, reading whether each later joiner adds more
than the one before.

Every run is paced at rates carrying no rational relation, so the readings are
taken on a covering run rather than on a closed slice.

Keys to Exhibit TWO Part Four, Exhibit FIVE 1.3, Exhibit EIGHT 5.4-5.6, and
Natural Intelligence 1.13.
"""
import sys, math
sys.path.insert(0, '.')
from living import Life, sign, YES, NO
from unrelated import Unrelated, closes


def surds(n):
    """One alpha per row, carrying no small integer relation between them."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    return [1 / math.sqrt(p) for p in primes[:n]]


class Transmissioning(Unrelated):
    """A ring whose rows offer both ways, or one way with the return removed."""

    def __init__(self, lengths, ways='two'):
        super().__init__(lengths, alphas=surds(len(lengths)), wiring='ring')
        self.ways = ways

    def _neighbours(self, k):
        n = len(self.rows)
        if n == 1:
            return []
        if self.ways == 'one':
            return [(k + 1) % n]                       # the return removed
        return sorted({(k - 1) % n, (k + 1) % n} - {k})


# ------------------------------------------------------------------ readings

def offerings_per_beat(life):
    """How many one-ways run at each beat: the three-and-three, counted."""
    return sum(len(life._neighbours(k)) for k in range(len(life.rows)))


def span_at(life, beats):
    while len(life.trace) < beats:
        life.beat()
    return len(set(life.trace[:beats]))


def extending(sizes, ways='two', beats=6000):
    """The co-chaining extended one joiner at a time, each reading its own arrival.

    Returns the span at each length, and whether each later joiner added more
    than the one before - an ordering, sign-only, with no rate read anywhere.
    """
    spans = []
    for n in range(2, len(sizes) + 1):
        L = Transmissioning(sizes[:n], ways=ways)
        L._gated = True
        spans.append(span_at(L, beats))
    adds = [spans[i] - spans[i - 1] for i in range(1, len(spans))]
    each_more = all(adds[i] > adds[i - 1] for i in range(1, len(adds))) if len(adds) > 1 else None
    return dict(spans=spans, adds=adds,
                each_joiner_adds_more=sign(bool(each_more)) if each_more is not None else '-')


# --------------------------------------------------------------------- the run

if __name__ == '__main__':
    print('TRANSMISSIONING - three phases, two one-ways each\n')

    sizes = [3, 5, 7]

    print('  the one-ways counted at each beat')
    for ways in ('two', 'one'):
        L = Transmissioning(sizes, ways=ways); L._gated = True
        print(f'    {ways:4s}-way ring of {len(sizes)}: {offerings_per_beat(L)} one-ways per beat')

    print('\n  the run, at rates carrying no rational relation')
    for ways in ('two', 'one'):
        L = Transmissioning(sizes, ways=ways); L._gated = True
        r = closes(L)
        print(f'    {ways:4s}-way  spans {r["spans"]}   closes {r["closes"]}   covers {r["covers"]}')

    print('\n  the co-chaining extending, coprime joiners')
    long_sizes = [3, 5, 7, 11, 13]
    for ways in ('two', 'one'):
        e = extending(long_sizes, ways=ways)
        print(f'    {ways:4s}-way  spans {e["spans"]}')
        print(f'             each joiner adds {e["adds"]}   each later adding more {e["each_joiner_adds_more"]}')

    print('\n  a shared-factor joiner beside a coprime one')
    for tail, name in (([3, 5, 7, 11], 'coprime  '), ([3, 5, 7, 9], 'shares 3 ')):
        L = Transmissioning(tail, ways='two'); L._gated = True
        print(f'    {name} {tail}: span {span_at(L, 6000)}')

    print('\n  BREAK CONDITIONS')
    print('    a one-way ring covering as widely as a two-way ring of the same rows')
    print('    a later coprime joiner adding less than the one before')
    print('    a shared-factor joiner adding as much as a coprime one')
