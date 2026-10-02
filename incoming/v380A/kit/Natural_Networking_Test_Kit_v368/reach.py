"""
reach.py - the reach reading done right, so the next working does not
rebuild the first sitting's mistakes.

The reach: does a state arrive at a self that arrives nowhere in that
self's own whole running. Is-or-is-not, per self. Three disciplines,
each earned by a void reading:

  phase-matched  the engine phases rows by index; a solo baseline at
                 another phase reads the phase back
  closed         the solo set is checked closed before it baselines
                 (a longer solo run adds no state)
  late           the arriving is discarded; a scan from beat nought
                 reads the forming as the living
"""
import sys
sys.path.insert(0, '.')
from living import Life, Self, sign

BEATS, BURN, CLOSE_CHECK = 2400, 800, 6000


def solo_closed(n, phase):
    """A self's own whole running at its own phase, checked closed."""
    s = Life([n]); s.rows[0] = Self(n, phase=phase); s._gated = True
    s.live(BEATS)
    base = set(st[0] for st in s.trace)
    s.live(CLOSE_CHECK - BEATS)
    grown = set(st[0] for st in s.trace)
    if not grown <= base:
        raise RuntimeError('reading refused: the solo set had not closed '
                           'at the baseline window; lengthen BEATS.')
    return base


def reach_standing(lengths, wiring='ring', beats=BEATS, burn=BURN):
    """Where the reach stands: {index: 'yes'|'no'} at the late window."""
    solos = {k: solo_closed(n, k % 2) for k, n in enumerate(lengths)}
    life = Life(lengths, wiring=wiring, pace='own'); life._gated = True
    life.live(beats)
    return {k: sign(any(life.trace[t][k] not in solos[k]
                        for t in range(burn, beats)))
            for k in range(len(lengths))}


if __name__ == '__main__':
    L = [7, 9, 11, 13, 15, 17, 19]
    for wiring in ('chain', 'ring'):
        st = reach_standing(L, wiring)
        print(f'{wiring}: reach', {k: v for k, v in st.items()})
