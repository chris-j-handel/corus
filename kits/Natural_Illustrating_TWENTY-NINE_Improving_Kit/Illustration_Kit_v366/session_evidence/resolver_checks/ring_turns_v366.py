"""ring_turns_v366.py · ONE's preserved kernel as a turn, alone and in rings, run at TWO's harness (notes JJJ04 to JJJ08)

Standard library only. Imports the preserved kernel beside it and changes nothing in it.
Run:  python3 ring_turns_v366.py            (every seed at rings 3 to 13, under a minute)
      python3 ring_turns_v366.py --seeds 16 (every seed at rings 3 to 16, some minutes)

The harness is Natural Networking's test kit (crt_counter_v265.py): each node receives its left neighbour's standing
sign, all nodes at one beat, the ring set alternating + - + - ... A defect is a node at rest (sign 0) or a joint (two
neighbours standing at the same sign); an odd ring cannot alternate all round, so it holds at least one (Konig's
bipartite theorem: an odd cycle is not two-colourable).

1. Alone, and the two mirrors. A key carried with sign s and torusing t, nothing arriving, steps to (-s, -t): each sign
   inverted in its own place, two mirrors at a right angle, the half turn. Two mirrors at an angle a make a turn by 2a,
   so mirrors at 45 degrees make the quarter turn, and the two orders of the same two mirrors are the two hands.
2. TWO's gate at ONE's kernel. Even rings: no defect, the surface summing to zero at every beat, period two. Odd rings,
   every odd ring to 59: exactly one defect at every beat, a joint and a node at rest by turns; the node at rest
   travels one place every two beats; the ring stands at the opposite sign after one circuit (2N beats) and home after
   two (4N), four beats per position.
3. Every seed. From every one of the 2^N sign seeds, the kernel keeps the count of defects exactly at every beat:
   none removed, none added.
4. The joint is where a node turns by a quarter. At every beat of an odd ring exactly one node steps into or out of
   rest, and every other node takes the half turn; a ring agreeing whole runs + 0 - 0, the cosine of the quarter turn.
5. Two odd rings joined. Opened at their joints and joined, they make an even ring with no defect, which bounds;
   joined anywhere else, the even ring carries both joints and never bounds.
6. The register. Every odd prime ring 3 to 59 runs 4p at ONE's kernel, so the sixteen at one common beat count
   lcm(4p) = 4 x (3 x 5 x ... x 59) = 2 x 59#: the scales combine coprime and the one four is shared, and the common
   beat walks one of 4^15 parallel closed lines on the register's torus.
7. An exploration, not a proposal: the node's two in-place inversions exchanged into one bi-inversion (the carried
   torusing, inverted, entering where the carried sign did; the fresh torusing taking the prior sign). Alone it runs the
   quarter turn, period four. In rings every node becomes a joint: whole-ring agreement and whole-ring rest.
"""
import itertools, math, sys
from math import lcm, prod
from Natural_Resolver_v345a_kernel import co_bi_coupling as kernel

S4 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ODD_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]


def quarter_exploration(co_carrying, bi_arriving):
    prior = {k: s for k, s, t, a in co_carrying}
    inv = [(k, s) for k, s in bi_arriving if s != 0]
    for k, s, t, a in co_carrying:
        if t > 0: inv.append((k, -1))
        if t < 0: inv.append((k, 1))
    tun = {}
    for k, s in inv:
        tun[k] = tun.get(k, 0) + (1 if s > 0 else -1)
    surf = [(k, 1 if v > 0 else (-1 if v < 0 else 0)) for k, v in tun.items()]
    carry = {}
    for k, s, t, a in co_carrying:
        if a + 1 <= 3 or (a + 1 == 4 and t > 0):
            carry[k] = (s, t, a + 1)
    for k, s in surf:
        if s != 0:
            carry[k] = (s, prior.get(k, 1), 0)
    return surf, [(k, s, t, a) for k, (s, t, a) in carry.items()]


def alone(f):
    rows = []
    for s in (1, -1):
        for t in (1, -1):
            c, tr = [('k', s, t, 0)], [(s, t)]
            for _ in range(4):
                _, c = f(c, []); c = [x for x in c if x[0] == 'k']
                tr.append((c[0][1], c[0][2]) if c else 'released')
                if not c: break
            rows.append(tr)
    return rows


class Ring:
    def __init__(self, N, f=kernel, seed=None):
        self.N, self.f = N, f
        seed = seed or [1 if i % 2 == 0 else -1 for i in range(N)]
        self.stands = {i: seed[i] for i in range(N) if seed[i]}; self.carry = []

    def step(self):
        acc = [(i, self.stands[(i - 1) % self.N]) for i in range(self.N) if self.stands.get((i - 1) % self.N)]
        seq, self.carry = self.f(self.carry, acc)
        self.stands = {i: m for i, m in seq if 0 <= i < self.N and m != 0}

    def surface(self):
        return tuple(self.stands.get(i, 0) for i in range(self.N))

    def state(self):
        return (tuple(sorted(self.stands.items())), tuple(sorted(self.carry)))


def defects(s):
    N = len(s)
    rest = [i for i in range(N) if s[i] == 0]
    joint = [i for i in range(N) if s[i] != 0 and s[i] == s[(i + 1) % N]]
    return rest, joint


def run(N, f=kernel, seed=None, beats=None):
    r = Ring(N, f, seed); seen, S, period = {}, [], None
    for t in range(beats or 8 * N + 8):
        st = r.state()
        if st in seen and period is None:
            period = t - seen[st]
        seen.setdefault(st, t); S.append(r.surface()); r.step()
    return period, S


def show(s):
    return ''.join({1: '+', -1: '-', 0: '0'}[x] for x in s)


def part1():
    print('1. ALONE, AND THE TWO MIRRORS')
    for tr in alone(kernel):
        print('   the kernel alone:', ' -> '.join(str(x) for x in tr))
    NP = lambda p: (-p[0], p[1])          # mirror in the Q axis, the line at 90 degrees
    NQ = lambda p: (p[0], -p[1])          # mirror in the P axis, the line at 0 degrees
    SW = lambda p: (p[1], p[0])           # mirror in the diagonal, the line at 45 degrees
    half = [NP(NQ(p)) for p in S4]
    kern = [tuple(alone(kernel)[i][1]) for i in range(4)]
    print(f'   two mirrors at 0 and 90 degrees give (-P, -Q), the half turn, the kernel alone at every state: {half == kern}')
    print(f'   mirrors at 45 and 90 degrees, one order: {[NP(SW(p)) == (-p[1], p[0]) for p in S4]} = the quarter turn (-Q, P)')
    print(f'   the same two mirrors, the other order:   {[SW(NP(p)) == (p[1], -p[0]) for p in S4]} = its mirror (Q, -P)')
    ok = True
    for a, b in itertools.product(range(0, 180, 15), repeat=2):
        ra, rb = math.radians(2 * a), math.radians(2 * b)
        Ma = [[math.cos(ra), math.sin(ra)], [math.sin(ra), -math.cos(ra)]]
        Mb = [[math.cos(rb), math.sin(rb)], [math.sin(rb), -math.cos(rb)]]
        M = [[sum(Mb[i][k] * Ma[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        th = math.radians(2 * (b - a))
        R = [[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]]
        ok &= all(abs(M[i][j] - R[i][j]) < 1e-12 for i in range(2) for j in range(2))
    print(f'   two mirrors at lines a then b make the turn by 2(b - a), every a, b in 15-degree steps: {ok}')


def part2():
    print('\n2. TWO\'S GATE AT ONE\'S KERNEL, TWO\'S HARNESS')
    for N in list(range(2, 15)) + [p for p in ODD_PRIMES if p > 13]:
        period, S = run(N)
        S = S[2:]
        kinds = sorted({(len(defects(s)[0]), len(defects(s)[1])) for s in S})
        sums = sorted({sum(s) for s in S})
        flipped = all(S[t + period // 2] == tuple(-x for x in S[t]) for t in range(len(S) - period // 2))
        line = f'   ring {N:2d} ({"odd " if N % 2 else "even"}): period {period:3d}{" = 4N" if period == 4 * N else ""}, ' \
               f'(rest, joints) at a beat {kinds}, surface sums {sums}, opposite sign at half the period {flipped}'
        if N % 2:
            rests = [defects(s)[0][0] for s in S if defects(s)[0]]
            moves = {(rests[i + 1] - rests[i]) % N for i in range(len(rests) - 1)}
            gaps = {b - a for a, b in zip([t for t, s in enumerate(S) if 0 in s], [t for t, s in enumerate(S) if 0 in s][1:])}
            line += f'; the node at rest moves {moves} place every {gaps} beats'
        print(line)


def part3(top):
    print(f'\n3. EVERY SEED, RINGS 3 TO {top}')
    for N in range(3, top + 1):
        kept, closed, total, counts = 0, 0, 0, {}
        for seed in itertools.product((1, -1), repeat=N):
            period, S = run(N, seed=list(seed), beats=4 * N + 8)
            d = {len(defects(s)[0]) + len(defects(s)[1]) for s in S}
            total += 1; kept += len(d) == 1; closed += period is not None
            counts[min(d)] = counts.get(min(d), 0) + 1
        print(f'   ring {N:2d}: {kept} of {total} seeds keep their count of defects at every beat, {closed} of them seen round their '
              f'whole cycle; seeds by count {dict(sorted(counts.items()))}')


def part4():
    print('\n4. THE JOINT IS WHERE A NODE TURNS BY A QUARTER')
    for N in (3, 5, 7, 9, 11, 13):
        _, S = run(N)
        S = S[2:]
        per_beat = {sum(1 for i in range(N) if not (S[t][i] != 0 and S[t + 1][i] == -S[t][i])) for t in range(len(S) - 1)}
        print(f'   ring {N:2d}: nodes per beat not taking the half turn {per_beat}')
    _, S = run(5, beats=6)
    print('   ring 5 from the alternating seed:', ' '.join(show(s) for s in S))
    for N in range(2, 13):
        period, S = run(N, seed=[1] * N, beats=13)
        cos = [round(math.cos(k * math.pi / 2)) for k in range(12)]
        assert all(s == (c,) * N for s, c in zip(S[1:], cos)) and period == 4, N
    print('   a ring agreeing whole, rings 2 to 12, from its first beat runs', ' '.join(show(s) for s in run(5, seed=[1] * 5, beats=9)[1][1:]),
          '= cos(k x 90 degrees) at every node, period four: True')


def part5():
    print('\n5. TWO ODD RINGS JOINED')
    for A, B in ((3, 3), (3, 5), (5, 7), (7, 11), (3, 13)):
        a = [1 if i % 2 == 0 else -1 for i in range(A)]          # its one joint stands at the seam, nodes A-1 and 0
        b = [1 if i % 2 == 0 else -1 for i in range(B)]
        tally = {}
        for i, j, sgn in itertools.product(range(A), range(B), (1, -1)):
            seed = a[i:] + a[:i] + [sgn * x for x in b[j:] + b[:j]]
            d = len(defects(tuple(seed))[1])
            period, S = run(A + B, seed=seed, beats=4 * (A + B) + 4)
            bounds = period == 2 and all(sum(s) == 0 for s in S[2:])
            tally[(d, bounds)] = tally.get((d, bounds), 0) + 1
        at_joints = [1 if i % 2 == 0 else -1 for i in range(A)] + [-1 if i % 2 == 0 else 1 for i in range(B)]
        p0, S0 = run(A + B, seed=at_joints)
        print(f'   {A} and {B} into {A + B}: opened at both joints, defects {len(defects(tuple(at_joints))[1])}, period {p0}, '
              f'bounds {p0 == 2 and all(sum(s) == 0 for s in S0[2:])}; all {2 * A * B} joinings by (defects, bounds): {dict(sorted(tally.items()))}')


def part6():
    print('\n6. THE REGISTER')
    periods = [run(p, beats=4 * p + 8)[0] for p in ODD_PRIMES]
    print(f'   each odd prime ring 3 to 59 at ONE\'s kernel runs 4p: {periods == [4 * p for p in ODD_PRIMES]}')
    L = lcm(*periods); P = prod(periods); primorial = prod([2] + ODD_PRIMES)
    print(f'   sixteen rings, {sum(ODD_PRIMES)} nodes; with the ring of two, {sum(ODD_PRIMES) + 2}')
    print(f'   at one common beat they count lcm(4p) = {L:,} = 4 x the product of the scales: {L == 4 * prod(ODD_PRIMES)}; = 2 x 59#: {L == 2 * primorial}')
    print(f'   the product of the periods is {P:.4e}; it is the count x 4^15: {P == L * 4 ** 15}')
    for primes in ([3, 5], [3, 5, 7]):
        walks = []
        for offs in itertools.product(range(4), repeat=len(primes) - 1):
            rings = [Ring(p) for p in primes]
            for r, o in zip(rings[1:], offs):
                for _ in range(o): r.step()
            pts = set()
            for _ in range(lcm(*[4 * p for p in primes])):
                pts.add(tuple(r.state() for r in rings))
                for r in rings: r.step()
            walks.append(frozenset(pts))
        union = frozenset().union(*walks)
        print(f'   rings {primes}: one common beat visits {len(walks[0])} joint states of {prod(4 * p for p in primes)}; '
              f'the {len(walks)} quarter offsets give {len(set(walks))} parallel lines, disjoint {sum(map(len, walks)) == len(union)}, '
              f'together the whole torus {len(union) == prod(4 * p for p in primes)}')


def part7():
    print('\n7. AN EXPLORATION, NOT A PROPOSAL: ONE BI-INVERSION AT THE NODE')
    for tr in alone(quarter_exploration):
        print('   alone:', ' -> '.join(str(x) for x in tr))
    for N in range(3, 10):
        period, S = run(N, quarter_exploration, beats=16 * N + 16)
        S = S[2:]
        most = max(len(defects(s)[0]) + len(defects(s)[1]) for s in S)
        agree = sum(1 for s in S if 0 not in s and len(set(s)) == 1)
        rest = sum(1 for s in S if set(s) == {0})
        print(f'   ring {N}: period {period}, most defects at a beat {most} of {N}, beats agreeing whole {agree}, beats at rest whole {rest}, of {len(S)}')


if __name__ == '__main__':
    top = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 13
    part1(); part2(); part3(top); part4(); part5(); part6(); part7()
