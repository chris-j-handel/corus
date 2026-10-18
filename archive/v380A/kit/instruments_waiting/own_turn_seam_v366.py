"""own_turn_seam_v366.py · the one beat and the own turn, and the one node where they part.

Standard library only. Runs at the step beside it and changes nothing in the resolver.
Run:  python3 own_turn_seam_v366.py        (about a minute)

The one beat stands every node's turn together. The own turn stands each node's turn one after another round the
ring. Both are an order over the whole ring; neither is free of one. The instrument meets the two and says exactly
where they part, and nothing further.

There are two directions to go round, and they are not the same running.

- **Against the arriving.** Each node takes its turn before its own arriving has turned. One round then stands as the
  one beat at every node but one: the seam, the node where the round closes, whose arriving turned first. At rings 3
  to 12, every standing the ten pairs allow and every place the round can close, the two never part at more than that
  one node.
- **With the arriving.** Each node takes its turn from an arriving that has already turned. The ten pairs are then
  left at every standing but two, the whole ring at rest carrying one sign.

The count is kept at the one beat at every standing. It is not kept at either round: at the seam it parts by one, by
one the other way, or not at all, and never by more. The ten pairs are kept at the one beat at every standing, and at
neither round: the round against the arriving keeps them at part of the standings and leaves them at the rest.

What travels at the seam is open, and it is the question this instrument leaves standing: what an offering, a
receiving and a carrying at one node's own turn carry round to the node where the round closes. Each part below
carries the rings it was run at; nothing here is run at every ring.
"""
import itertools
from ring_window_v366 import ST, step, density, NAME

PAIRS = {((1, 1), (1, 1)), ((-1, -1), (-1, -1)),
         ((1, 1), (-1, -1)), ((-1, -1), (1, 1)),
         ((1, 1), (0, -1)), ((-1, -1), (0, 1)),
         ((0, 1), (1, 1)), ((0, -1), (-1, -1)),
         ((0, 1), (0, 1)), ((0, -1), (0, -1))}

count = lambda x: sum(density(x[i], x[(i + 1) % len(x)]) for i in range(len(x)))
within = lambda x: all((x[i], x[(i + 1) % len(x)]) in PAIRS for i in range(len(x)))
one_beat = lambda x: tuple(step(x[i - 1], x[i]) for i in range(len(x)))
standings = lambda N: [x for x in itertools.product(ST, repeat=N) if within(x)]


def own_turn(x, order):
    x = list(x)
    for i in order:
        x[i] = step(x[i - 1], x[i])
    return tuple(x)


against = lambda N, s: [(s - j) % N for j in range(N)]      # each node turning before its arriving turns
alongwith = lambda N, s: [(s + j) % N for j in range(N)]    # each node turning after its arriving has turned


if __name__ == '__main__':
    print('1. AGAINST THE ARRIVING · ONE ROUND BESIDE THE ONE BEAT · RINGS 3 TO 12')
    for N in range(3, 13):
        X = standings(N); parts = set(); seam_only = True
        for x in X:
            for s in range(N):
                y, b = own_turn(x, against(N, s)), one_beat(x)
                d = [i for i in range(N) if y[i] != b[i]]
                parts |= {len(d)}
                seam_only &= d in ([], [(s + 1) % N])
        print(f'   ring {N:2d}: {len(X):6d} standings the ten pairs allow, {N} places the round can close; '
              f'the round parts from the one beat at {sorted(parts)} node, and only ever at the seam: {seam_only}')

    print('\n2. THE COUNT · RINGS 3 TO 10')
    for N in range(3, 11):
        X = standings(N); whole = 0; parted = {}
        beat = all(count(one_beat(x)) == count(x) for x in X)
        for x in X:
            for s in range(N):
                y = own_turn(x, against(N, s))
                if y == one_beat(x):
                    whole += 1
                else:
                    d = count(y) - count(x); parted[d] = parted.get(d, 0) + 1
        print(f'   ring {N:2d}: the one beat keeps the count at every standing: {beat}; the round is the whole one '
              f'beat at {whole} of {len(X) * N}; where the seam parts them, the count parts by {dict(sorted(parted.items()))}')

    print('\n3. THE TEN PAIRS AT EACH RUNNING · RINGS 3 TO 9')
    for N in range(3, 10):
        X = standings(N); n = len(X) * N
        beat = sum(within(one_beat(x)) for x in X)
        ag = sum(within(own_turn(x, against(N, s))) for x in X for s in range(N))
        wi = sum(within(own_turn(x, alongwith(N, s))) for x in X for s in range(N))
        print(f'   ring {N}: the one beat keeps them at {beat} of {len(X)}; the round against, at {ag} of {n}; '
              f'the round with, at {wi} of {n}')

    print('\n4. WITH THE ARRIVING · THE STANDINGS THAT KEEP THE TEN PAIRS · RINGS 3 TO 8')
    for N in range(3, 9):
        X = standings(N)
        keep = {x for x in X for s in range(N) if within(own_turn(x, alongwith(N, s)))}
        print(f'   ring {N}: {len(keep)} of {len(X)}: {sorted("".join(NAME[a] for a in x) for x in keep)}')

    print('\n5. THE THREE-RING STANDING WHOLE AT PLUS')
    x = ((1, 1),) * 3
    print(f'   the standing            {[NAME[a] for a in x]}  count {count(x)}  within the ten pairs {within(x)}')
    print(f'   the one beat            {[NAME[a] for a in one_beat(x)]}  count {count(one_beat(x))}  '
          f'within the ten pairs {within(one_beat(x))}')
    for s in range(3):
        y = own_turn(x, against(3, s))
        print(f'   the round closing at {(s + 1) % 3}  {[NAME[a] for a in y]}  count {count(y)}  '
              f'within the ten pairs {within(y)}')
