"""Session v385M, run for v385R's open place at the Co-Chaining Logic Registry's steps 170 and 171.
Run from the repository root:  python3 incoming/v385M/round_check.py
It reads no file and changes nothing.

Step 170: a round reaching each joint form of k parities once is 1 to 2^k + 1.
Step 171: such a round, one parity at a time, is the round at k - 1 parities, the new parity inverted, and the
same forms in the other order.
Counted here: each round that reaches each form of k parities once, changing one parity at a step and coming
back to its first form; whether step 171's round is among them; and how many rounds there are that are not
one another with the parities renamed or a parity's two values exchanged."""
from itertools import permutations, product

def rounds(k):
    n = 1 << k; found = []
    def go(path, seen):
        if len(path) == n:
            if bin(path[-1] ^ path[0]).count("1") == 1 and path[1] < path[-1]:   # each round once, not once per direction
                found.append(tuple(path))
            return
        for b in range(k):
            v = path[-1] ^ (1 << b)
            if not seen & (1 << v):
                go(path + [v], seen | (1 << v))
    go([0], 1)
    return found

def step_171(k):
    r = [0, 1]
    for j in range(1, k):
        r = r + [v | (1 << j) for v in reversed(r)]
    return r

def canon(cyc):
    n = len(cyc); i = cyc.index(0)
    a = cyc[i:] + cyc[:i]; b = (a[0],) + tuple(reversed(a[1:]))
    return min(a, b)

def kinds(k, all_rounds):
    left = set(canon(c) for c in all_rounds); count = 0
    while left:
        c = next(iter(left)); count += 1
        for perm in permutations(range(k)):
            for flip in range(1 << k):
                def m(v):
                    w = 0
                    for b in range(k):
                        if v >> b & 1: w |= 1 << perm[b]
                    return w ^ flip
                left.discard(canon(tuple(m(v) for v in c)))
    return count

for k in (2, 3, 4):
    rs = rounds(k); s = canon(tuple(step_171(k)))
    print("k = %d parities: forms %2d, a round is 1 to %2d (step 170: 2^k + 1 = %2d);  rounds one parity at a time: %4d;"
          "  step 171's round among them: %s;  rounds not one another renamed or exchanged: %d"
          % (k, 1 << k, (1 << k) + 1, (1 << k) + 1, len(rs), s in set(canon(c) for c in rs), kinds(k, rs)))
r = step_171(4)
print("step 171's round at four parities:", " ".join(format(v, "04b") for v in r))
