"""
unrelated.py - rows paced at rates carrying no rational relation.

The kit's engine paces every row at an integer count of its own beats, and
integer rates carry a rational relation always. A run at rationally related
rates closes onto a slice: the joint span reaches a number and repeats it
forever, and every reading the kit returns is taken on that slice.

The readings are correct there. What they cannot be is readings of a run that
covers, and a run that covers is where the living runs.

The three surds of the first three primes carry no integer relation between
them - any combination summing to zero forces all three coefficients to zero,
checkable in four lines. A run paced at them returns to no position twice.

  integer pace [3,5,7]   joint span at 1k/2k/4k/8k beats: 335 335 335 335
  surd pace    [3,5,7]   joint span at 1k/2k/4k/8k beats: 899 1651 2804 4436

Two rows close at either pacing: two rows on a ring couple only to each other,
and two axes carry no difference between the closing case and the covering
one. Three rows carry it.

Keys to Exhibit THREE 5.9 (the caught constructibles), Exhibit EIGHT 5.4-5.6,
and Exhibit TWO Part Four.
"""
import sys, math
sys.path.insert(0, '.')
from living import Life, sign, YES, NO

# the three surds, and the reciprocals that pace with them
SURD = {2: 1 / math.sqrt(2), 3: 1 / math.sqrt(3), 5: 1 / math.sqrt(5)}
PHI = (math.sqrt(5) - 1) / 2      # one over phi; phi squared arrives at phi plus one,
                                  # so one, phi and phi squared close on an integer
                                  # relation and phi alone paces two rows and no more


class Unrelated(Life):
    """One life whose rows open at rates carrying no rational relation.

    Each row carries its own phase, advanced by its own alpha each beat, and
    opens its across when the phase crosses one and returns by one. Nothing
    is scheduled over the rows, no clock stands anywhere, and each row paces
    its own coupling on its own rhythm.
    """

    def __init__(self, lengths, alphas=None, wiring='ring'):
        super().__init__(lengths, wiring=wiring, pace='own')
        if alphas is None:
            alphas = [SURD[p] for p in list(SURD)[:len(lengths)]]
        if len(alphas) != len(lengths):
            raise ValueError('one alpha per row')
        self.alphas = list(alphas)
        self.phase = [0.0] * len(lengths)

    def beat(self, offerings=None):
        for k, r in enumerate(self.rows):
            acc = list(r.own_along())
            self.phase[k] += self.alphas[k]
            opens = self.phase[k] >= 1.0
            if opens:
                self.phase[k] -= 1.0
                for kk in self._neighbours(k):
                    acc += [(i % r.n, m) for i, m in self.rows[kk].surf if m != 0]
            if offerings and k in offerings:
                acc += [(i, m) for i, m in offerings[k] if m != 0]
            r.couple(acc)
        self.trace.append(tuple(r.signs() for r in self.rows))


# ------------------------------------------------------------- the reading

def closes(life, checkpoints=(1000, 2000, 4000, 8000)):
    """Whether the run closes onto a slice, or goes on opening.

    Sign-only. A span reached and repeated at every later checkpoint is a
    closing; a span standing higher at each is a covering. No threshold is
    set anywhere and no rate is read - the ordering is the reading.
    """
    spans = []
    for b in checkpoints:
        while len(life.trace) < b:
            life.beat()
        spans.append(len(set(life.trace[:b])))
    grew = all(spans[i] > spans[i - 1] for i in range(1, len(spans)))
    held = all(spans[i] == spans[-1] for i in range(1, len(spans)))
    return dict(spans=spans, closes=sign(held), covers=sign(grew))


def rational_relation(alphas, depth=6):
    """Whether small integer coefficients arrive at a relation among the rates.

    A reading of the pacing itself, sign-only: is there a small integer
    combination standing near zero. Where one arrives, the run closes.
    """
    from itertools import product
    n = len(alphas)
    best = None
    for coeffs in product(range(-depth, depth + 1), repeat=n):
        if all(c == 0 for c in coeffs):
            continue
        v = abs(sum(c * a for c, a in zip(coeffs, alphas)))
        if best is None or v < best[0]:
            best = (v, coeffs)
    return dict(nearest=best[1], residue_small=sign(best[0] < 1e-9))


# --------------------------------------------------------------------- the run

if __name__ == '__main__':
    print('UNRELATED PACING - the closing lifted\n')

    cases = [
        ('integer pace  [3,5]',   Life([3, 5], pace='own')),
        ('integer pace  [3,5,7]', Life([3, 5, 7], pace='own')),
        ('shared beat   [3,5,7]', Life([3, 5, 7], pace='clock')),
        ('surd pace     [3,5]',   Unrelated([3, 5])),
        ('surd pace     [3,5,7]', Unrelated([3, 5, 7])),
    ]
    for name, L in cases:
        L._gated = True
        r = closes(L)
        print(f'  {name:22s} spans {r["spans"]}   closes {r["closes"]}   covers {r["covers"]}')

    print('\n  the pacing read at itself - does a small integer relation arrive')
    for name, alphas in (('integers  [3,5,7]', [1/3, 1/5, 1/7]),
                         ('surds     [2,3,5]', [SURD[2], SURD[3], SURD[5]]),
                         ('phi alone [1,p,p2]', [1.0, PHI, PHI * PHI])):
        rr = rational_relation(alphas)
        print(f'    {name:20s} nearest coefficients {rr["nearest"]}   relation arrives {rr["residue_small"]}')

    print('\n  BREAK CONDITIONS')
    print('    a run at rationally related rates covering')
    print('    a run at unrelated rates closing at three rows or more')
    print('    two rows carrying the difference between the two cases')
