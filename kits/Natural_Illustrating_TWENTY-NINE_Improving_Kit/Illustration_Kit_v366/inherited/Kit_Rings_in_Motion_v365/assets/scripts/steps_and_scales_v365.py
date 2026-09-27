"""steps_and_scales_v365.py · the journey's step tested against every other step, and at larger scales (note CCC07)

Standard library only. Run:  python3 steps_and_scales_v365.py

Part 1. The journey (journey.py) steps the sign pair by F(P, Q) = (-Q, P) from the prior (+, -), with the
direction alternating co/bi at the odd origin and bi/co at the even origin. Here every possible step rule on
the four sign pairs is run the same way (4^4 = 256 rules), and for each rule the fixed conditions on
(direction, sign pair) that live through both origins are counted. A fixed condition lives through a running
exactly when it admits every state the running meets, so the count is 2^(8 - states met).

Part 3 (below Part 2 in the run). Moral as do-no-harm improving, decided at each step: a step loses no prior
(no two sign pairs step to one), improves (changes one sign), and never undoes (the next is never the prior).

Part 2. The one-sign-at-a-time cycles through every sign state, at 1 to 4 signs: all of them, those in which
one member changes at every other step, those alternating so at every scale, and the reflected Gray code,
which builds each scale from the prior scale followed by its mirror.
"""
import itertools
from collections import Counter

S = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
sg = lambda s: ''.join('+' if x > 0 else '-' for x in s)


def journeys(step):
    signs = [(1, -1)]
    for _ in range(9):
        signs.append(step[signs[-1]])
    return {o: [(('co' if n % 2 else 'bi') if o == 'odd' else ('bi' if n % 2 else 'co'), signs[n]) for n in range(10)]
            for o in ('odd', 'even')}


def met(j):
    return set(j['odd'][1:]) | set(j['even'][1:])


def part_one():
    print('Part 1 · every step rule on the four sign pairs, run as the journey')
    counts, only_nothing = Counter(), []
    for image in itertools.product(S, repeat=4):
        step = dict(zip(S, image))
        n = 2 ** (8 - len(met(journeys(step))))
        counts[n] += 1
        if n == 1:
            only_nothing.append(step)
    print('   conditions living through both origins, over all 256 rules:', dict(sorted(counts.items())))
    print(f'   rules under which only the condition adding nothing lives: {len(only_nothing)}')
    for step in only_nothing:
        path = [(1, -1)]
        for _ in range(4):
            path.append(step[path[-1]])
        one_at_a_time = all(sum(a != b for a, b in zip(path[i], path[i + 1])) == 1 for i in range(4))
        name = ('(-Q, P)' if all(step[s] == (-s[1], s[0]) for s in S) else
                '(Q, -P)' if all(step[s] == (s[1], -s[0]) for s in S) else '')
        print('     ', ' -> '.join(sg(p) for p in path), '· one sign per step' if one_at_a_time else '· two signs at some step', name)
    named = {'unchanged': lambda s: s, 'both negated': lambda s: (-s[0], -s[1]), 'swapped': lambda s: (s[1], s[0]),
             'P negated': lambda s: (-s[0], s[1]), 'rotation (-Q, P)': lambda s: (-s[1], s[0]),
             'rotation (Q, -P)': lambda s: (s[1], -s[0])}
    for k, g in named.items():
        step = {s: g(s) for s in S}
        m = len(met(journeys(step)))
        print(f'   {k:18s} states met {m} of 8 · conditions living {2 ** (8 - m)}')


def cycles(n):
    N, out = 1 << n, []
    def go(path, seen):
        if len(path) == N:
            if bin(path[-1] ^ path[0]).count('1') == 1:
                out.append(path[:])
            return
        for b in range(n):
            nx = path[-1] ^ (1 << b)
            if nx not in seen:
                seen.add(nx); path.append(nx); go(path, seen); path.pop(); seen.discard(nx)
    go([0], {0})
    return out


def flips(c):
    return [(c[i] ^ c[(i + 1) % len(c)]).bit_length() - 1 for i in range(len(c))]


def alternating_once(f):
    return len(set(f[0::2])) == 1 or len(set(f[1::2])) == 1


def alternating_every_scale(f):
    order = []
    while len(f) > 1:
        for ph in (0, 1):
            if len(set(f[ph::2])) == 1:
                order.append(f[ph]); f = f[1 - ph::2]; break
        else:
            return None
    return tuple(order)


def brgc(n):
    return [i ^ (i >> 1) for i in range(1 << n)]


def part_two():
    print('\nPart 2 · one sign changing per step, every sign state met, back to the start')
    for n in (1, 2, 3, 4):
        cs = cycles(n)
        once = [c for c in cs if alternating_once(flips(c))]
        every = [(c, alternating_every_scale(flips(c))) for c in cs]
        every = [(c, o) for c, o in every if o is not None]
        per_order = sorted(set(Counter(o for _, o in every).values()))
        print(f'   {n} sign(s), {1 << n} states: cycles {len(cs)}; one member at every other step {len(once)}; '
              f'so at every scale {len(every)}; per order of members {per_order}; reflected Gray code among them: {brgc(n) in cs}')
    for n in (2, 3, 4):
        g, ruled = brgc(n), set()
        for perm in itertools.permutations(range(n)):
            relab = [sum(((x >> i) & 1) << perm[i] for i in range(n)) for x in g]
            ruled.add(tuple(relab)); ruled.add(tuple([relab[0]] + relab[:0:-1]))
        print(f'   {n} signs, the rule stated (each scale the prior scale followed by its mirror): '
              f'{len(ruled)} cycles, {len(ruled) // max(1, len(set(itertools.permutations(range(n)))))} per naming')
    g2, g3 = brgc(2), brgc(3)
    print('   the reflected Gray code at 3 signs is the 2-sign code followed by its mirror:',
          g3 == g2 + [4 | x for x in reversed(g2)])
    print('   its changing member at 4 signs, step by step:', flips(brgc(4)))


def part_three():
    print('\nPart 3 · do-no-harm improving, decided at each step, over all 256 rules')
    one = lambda a, b: sum(x != y for x, y in zip(a, b)) == 1
    counts = Counter(); kept = []
    for image in itertools.product(S, repeat=4):
        step = dict(zip(S, image))
        no_harm = len(set(image)) == 4
        improving = all(one(s, step[s]) for s in S)
        never_undo = all(step[step[s]] != s for s in S)
        counts['loses no prior'] += no_harm; counts['changes one sign'] += improving
        counts['both'] += no_harm and improving
        if no_harm and improving and never_undo:
            kept.append(step)
    print('   ', dict(counts), '· all three:', len(kept))
    for step in kept:
        path = [(1, -1)]
        for _ in range(4):
            path.append(step[path[-1]])
        print('     ', ' -> '.join(sg(p) for p in path), '· every sign pair met:', len(set(path)) == 4)


if __name__ == '__main__':
    part_one()
    part_two()
    part_three()
