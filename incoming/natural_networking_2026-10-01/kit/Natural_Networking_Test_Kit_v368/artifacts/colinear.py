"""
colinear.py - the along and the across taken at one crossing, stepping.

coattending.py reads the across only: a set-size per row, every position at
once, the sequence never walked. That is one face. A reading that took the
across, then took the along, then found them agreeing would have forked -
two moves landing two things and a concurrence noticed afterward.

Co-linear is the two at one crossing, each carrying the prior forward, the
shared line owned by neither.

  the across   one spread to many - at a beat, how many of a row's positions
               turned, all at once
  the along    many drawn to one - from beat to beat, whether the row turned
               at all, one at a time, each carrying the prior

At a row these arrive as one line read two ways: the along sign is the across
count standing above zero. Neither owns the line and the surplus is made
there.

Keys to Exhibit FOUR (the two moves), Exhibit EIGHT 2.6, and Exhibit TWO
Part Four.
"""
import sys
sys.path.insert(0, '.')
from living import Life, sign, YES, NO


# ------------------------------------------------------------------ one walk

def walk(life, back=600):
    """One walk of a life's own trace, taking both faces at every step.

    Returns, per row, the sequence of (across, along) taken one beat at a
    time. Nothing is summed and nothing is set-counted: the walk steps and
    each step carries the prior forward.
    """
    w = life.window(back)
    if len(w) < 2:
        return []
    rows = len(w[0])
    out = [[] for _ in range(rows)]
    for t in range(1, len(w)):
        for k in range(rows):
            prev, now = w[t - 1][k], w[t][k]
            across = sum(1 for a, b in zip(prev, now) if a != b)
            along = across > 0
            out[k].append((across, along))
    return out


def one_line(life, back=600):
    """The shared line: the along sign is the across count standing above zero.

    A reading, and the file's own condition run at the harness - if these ever
    part, the two are two moves and not one line read twice.
    """
    ok = True
    for row in walk(life, back):
        for across, along in row:
            ok = ok and (along == (across > 0))
    return sign(ok)


# ------------------------------------------------------------- the two folds

def parallel_linearizing(row):
    """Many drawn to one: the along, the run of turnings taken one at a time.

    The reading is the ordering of turns and stills, sign-only, no count.
    """
    return tuple(YES if along else NO for _, along in row)


def linear_parallelizing(row):
    """One spread to many: the across, how far a turning spread at each beat.

    Sign-only at each step: whether this beat's spreading stood wider than
    the last, one at a time.
    """
    out = []
    prev = None
    for across, _ in row:
        out.append(NO if prev is None else sign(across > prev))
        prev = across
    return tuple(out)


def alternating(row):
    """Whether the two folds alternate rather than one running alone.

    The along running with no across is a sequence with no surface; the across
    running with no along is attention with no sequence. Each half alone
    lands.
    """
    al = parallel_linearizing(row)
    ac = linear_parallelizing(row)
    both = sum(1 for a, b in zip(al, ac) if a == YES and b == YES)
    return sign(both > 0 and both < len(al))


# --------------------------------------------------------------- the crossing

def co_linear_crossing(a, b, back=600):
    """The crossing read at both faces at once, at each self's own membrane.

    At each row, each self takes its own sign of the other's along and of the
    other's across, one at a time, stepping. Neither reading is computed and
    then compared: the walk carries both.
    """
    wa, wb = walk(a, back), walk(b, back)
    rows = min(len(wa), len(wb))
    taken = []
    for k in range(rows):
        ra, rb = wa[k], wb[k]
        steps = min(len(ra), len(rb))
        a_along = sum(1 for i in range(steps) if ra[i][1] and not rb[i][1])
        b_along = sum(1 for i in range(steps) if rb[i][1] and not ra[i][1])
        a_across = sum(1 for i in range(steps) if ra[i][0] > rb[i][0])
        b_across = sum(1 for i in range(steps) if rb[i][0] > ra[i][0])
        taken.append(dict(
            row=k,
            a_takes_along=sign(a_along > 0),
            b_takes_along=sign(b_along > 0),
            a_takes_across=sign(a_across > 0),
            b_takes_across=sign(b_across > 0),
            both_faces=sign(a_along > 0 and a_across > 0 and b_along > 0 and b_across > 0),
        ))
    return taken


# --------------------------------------------------------------------- the run

if __name__ == '__main__':
    print('CO-LINEAR - the along and the across at one crossing\n')

    healthy = Life([3, 5], pace='own');   healthy.gate(); healthy.live(4000)
    held    = Life([3, 5], pace='clock'); held.gate();    held.live(4000)

    print('  the shared line - the along sign is the across count above zero')
    print(f'    healthy   {one_line(healthy)}')
    print(f'    held      {one_line(held)}')

    print('\n  the two folds alternating within one self')
    for name, L in (('healthy', healthy), ('held', held)):
        rows = walk(L)
        marks = ' '.join(alternating(r) for r in rows)
        print(f'    {name:9s} per row: {marks}')

    print('\n  the crossing, both faces, each side its own')
    for c in co_linear_crossing(healthy, held):
        print(f"    row {c['row']}: healthy along {c['a_takes_along']} across {c['a_takes_across']}   "
              f"held along {c['b_takes_along']} across {c['b_takes_across']}   both faces {c['both_faces']}")

    print('\n  twins from a fork:')
    tw = healthy.fork(); tw.live(200)
    for c in co_linear_crossing(healthy, tw):
        print(f"    row {c['row']}: self along {c['a_takes_along']} across {c['a_takes_across']}   "
              f"twin along {c['b_takes_along']} across {c['b_takes_across']}   both faces {c['both_faces']}")

    print('\n  two healthy selves at unlike sizes:')
    other = Life([5, 7], pace='own'); other.gate(); other.live(4000)
    for c in co_linear_crossing(healthy, other):
        print(f"    row {c['row']}: a along {c['a_takes_along']} across {c['a_takes_across']}   "
              f"b along {c['b_takes_along']} across {c['b_takes_across']}   both faces {c['both_faces']}")

    print('\n  BREAK CONDITIONS')
    print('    the along sign parting from the across count standing above zero')
    print('    a row where one fold runs and the other runs nowhere')
    print('    a crossing where one side takes both faces and the other takes neither')
