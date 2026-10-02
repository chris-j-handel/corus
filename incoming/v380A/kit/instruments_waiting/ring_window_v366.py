"""ring_window_v366.py · the resolver's keeping at every ring, from a standing three nodes long.

Standard library only. Imports Exhibit ONE's resolver beside it and changes nothing in it.
Run:  python3 ring_window_v366.py

At the ring harness each node takes its left neighbour's standing sign at one beat. Read at Exhibit ONE's rows, the
resolver's step at a node is then: the 10-other-surfacing is the sign of the arriving less the 7-other-corusing the node
carries at 11-other-chaining, the carrying kept while the node rests. A node takes the half turn unless the arriving
agrees with what it carries; then it rests one beat.

1. The step. The two-line step gives the resolver's surfacings exactly, every seed of every ring 2 to 12, whole cycles.
2. The ten pairs. After the first beat a node stands at one of four: +, -, or at rest carrying + or -. Of the sixteen
   neighbour pairs only ten are ever met, five mirror pairs under each sign inverted, and six never; every seed's first
   beat meets only these ten, and the step keeps them, checked at all 26 standings three nodes long that the ten allow.
   So no node rests two beats, and the carried sign is always kept: the two-line step is the resolver on every ring, not
   only on the rings run.
3. The standing three long. At each of the 26, the changing of defects at the middle node is the joint arriving from the
   left less the joint leaving to the right. Round any ring the joints meet, so the count of defects is kept at every
   ring of every size. The joint is the current; a defect is carried, never made or lost. Without the ten pairs the
   standing does not close: rings outside the ten pairs can change their count.
4. The seventeen prime rings. The primes 2 to 59 are seventeen. At the resolver the ring of two carries no defect and
   meets at nought at every beat, and adds nothing to the register's count; the sixteen odd rings carry one joint each.

This instrument arrived from the Natural Illustrating work and is re-laid at Exhibit ONE's version 366 naming. It
returns identically at the earlier naming and at this one.
"""
import itertools
from math import lcm
from resolver import _1_self_coupling as kernel

sgn = lambda v: (v > 0) - (v < 0)
ST = [(1, 1), (-1, -1), (0, 1), (0, -1)]           # (surfacing, carrying): +, -, at rest carrying +, at rest carrying -
NAME = {(1, 1): '+', (-1, -1): '-', (0, 1): '0+', (0, -1): '0-'}


def step(left, own):
    m = sgn(left[0] - own[1])
    return (m, m if m else own[1])


def kernel_ring(seed, beats):
    N = len(seed); stands = {i: seed[i] for i in range(N)}; carry = []; out = []
    for _ in range(beats):
        out.append(tuple(stands.get(i, 0) for i in range(N)))
        acc = [(i, stands[(i - 1) % N]) for i in range(N) if stands.get((i - 1) % N)]
        seq, carry = kernel(carry, acc)
        stands = {i: m for i, m in seq if m != 0}
    return out


def step_ring(seed, beats):
    N = len(seed); x = [(seed[(i - 1) % N],) * 2 for i in range(N)]       # the first beat: each node takes its arriving
    out, states = [tuple(seed), tuple(s[0] for s in x)], [x]
    for _ in range(beats - 2):
        x = [step(x[(i - 1) % N], x[i]) for i in range(N)]
        out.append(tuple(s[0] for s in x)); states.append(x)
    return out, states


def density(a, b):                                   # a defect at a node: at rest, or the left member of a joint
    return (a[0] == 0) + (a[0] != 0 and a[0] == b[0])


joint = lambda a, b: int(a[0] != 0 and a[0] == b[0])


if __name__ == '__main__':
    print('1. THE STEP')
    same, pairs, longest = True, set(), 0
    for N in range(2, 13):
        for seed in itertools.product((1, -1), repeat=N):
            k = kernel_ring(list(seed), 4 * N + 8)
            s, states = step_ring(list(seed), 4 * N + 8)
            same &= k == s
            for x in states:
                pairs |= {(x[i], x[(i + 1) % N]) for i in range(N)}
            for i in range(N):
                run = 0
                for row in k:
                    run = run + 1 if row[i] == 0 else 0; longest = max(longest, run)
    print(f'   the surfacing at the sign of the arriving less the carrying gives the resolver\'s surfacings at every '
          f'seed of rings 2 to 12: {same}; longest rest {longest} beat')
    print('\n2. THE TEN PAIRS')
    print(f'   pairs met: {len(pairs)} of 16: {" ".join(NAME[a] + NAME[b] for a, b in sorted(pairs))}')
    W = [(a, b, c) for a, b, c in itertools.product(ST, repeat=3) if (a, b) in pairs and (b, c) in pairs]
    first = all(((s, s), (t, t)) in pairs for s in (1, -1) for t in (1, -1))
    kept = all((step(a, b), step(b, c)) in pairs for a, b, c in W)
    no_second_rest = all(step(a, b)[0] != 0 for a, b in pairs if b[0] == 0)
    print(f'   standings three long the ten allow: {len(W)}; every first beat within the ten: {first}; '
          f'the step keeps the ten: {kept}')
    print(f'   a node at rest never rests the next beat, so the carried sign is always kept: {no_second_rest}')
    flip = lambda a: (-a[0], -a[1])
    stitches = {frozenset({(a, b), (flip(a), flip(b))}) for a, b in pairs}
    print(f'   every sign inverted, the ten pair into {len(stitches)} mirror pairs, none its own mirror: '
          f'{all(len(st) == 2 for st in stitches)}; '
          f'{" · ".join(" ".join(NAME[a] + NAME[b] for a, b in sorted(st)) for st in sorted(stitches, key=lambda st: sorted(st)))}')
    never = sorted(set(itertools.product(ST, repeat=2)) - pairs)
    print(f'   never met: {len(never)}, {" ".join(NAME[a] + NAME[b] for a, b in never)}: '
          f'sixteen pairs, ten met and six never met')
    print('\n3. THE STANDING THREE LONG')
    closes = all(density(step(a, b), step(b, c)) - density(b, c) == joint(a, b) - joint(b, c) for a, b, c in W)
    print(f'   at all {len(W)}, the changing of defects = the joint arriving from the left - the joint leaving to '
          f'the right: {closes}')
    loops = [cyc for n in (1, 2, 3) for cyc in itertools.product(ST, repeat=n)]
    broken = [cyc for cyc in loops if sum(density(step(cyc[i - 1], cyc[i]), step(cyc[i], cyc[(i + 1) % len(cyc)]))
                                          - density(cyc[i], cyc[(i + 1) % len(cyc)]) for i in range(len(cyc))) != 0]
    print(f'   without the ten pairs, rings of one to three standings that change their count: {len(broken)}, e.g. '
          f'{" ".join(NAME[s] for s in broken[0])}')
    print('   so the count of defects is kept at every ring of every size, from a standing three nodes long')
    print('\n4. THE SEVENTEEN PRIME RINGS')
    primes = [p for p in range(2, 60) if all(p % d for d in range(2, p))]
    print(f'   the primes 2 to 59: {len(primes)}; 59 is the {len(primes)}th')
    two = kernel_ring([1, -1], 8)
    print(f'   the ring of two runs {" ".join("".join("+" if v > 0 else "-" if v < 0 else "0" for v in r) for r in two)}: '
          f'no defect {all(density(ST[0 if r[0] > 0 else 1], ST[0 if r[1] > 0 else 1]) == 0 and 0 not in r for r in two)}, '
          f'meeting at nought {all(sum(r) == 0 for r in two)}')
    odd = primes[1:]
    print(f'   the register with the ring of two counts {lcm(2, *[4 * p for p in odd]):,}, without it '
          f'{lcm(*[4 * p for p in odd]):,}: the same {lcm(2, *[4 * p for p in odd]) == lcm(*[4 * p for p in odd])}')
    print(f'   sixteen odd rings, one joint each: {len(odd)} joints travelling; the ring of two, none')
