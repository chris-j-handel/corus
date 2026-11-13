"""prime_spiral_check.py · Exhibit ONE's code, executed as it is, on a spiral of n selves,
each going along with 9 to a next self and its last to its first.

Use: python3 prime_spiral_check.py <path to Exhibit_ONE_Natural_Resolver_v###.md>
It reads the code from the living file and changes no line of it. An executing is a
check of a reading and decides nothing. Its returned lines are in
prime_spiral_check_returned.txt, executed with Exhibit ONE v391.

Says:
  1. With each self of a prior parity, inverting one to the next along: the number of
     momentaries by which a spiral's parities come again, n from 2 to 59.
  2. With each opening of + and - among n selves, n from 2 to 13: each number of
     momentaries by which parities come again, and how many openings have it.
  3. Two folds among 1 to N names, N/2 up or down and N + 1 less: the sets of four
     they make, and the names they go first from, N of 4, 16 and 64. Arithmetic only,
     with no line of the code.
"""
import re, sys
from itertools import product

src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
step = ns["_17_next_existing"]
S = "s"


def again(parities):
    n = len(parities)
    net = {(k, 9): (k + 1) % n for k in range(n)}
    soc = {k: ([(S, p)], []) for k, p in enumerate(parities)}
    key = lambda s: tuple((tuple(sorted(pr)), tuple(sorted(inc))) for pr, inc in (s[k] for k in range(n)))
    seen, t = {}, 0
    while True:
        k = key(soc)
        if k in seen:
            return seen[k], t - seen[k]   # momentaries before its round, and its round
        seen[k] = t
        soc = step(soc, net)
        t += 1


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


print("1. Each self inverting one to the next along: n, its round, and its round over n")
for n in range(2, 60):
    before, rnd = again([1 if k % 2 == 0 else -1 for k in range(n)])
    print("  %2d %s round %3d  round/n %s  before it %d" % (
        n, "prime" if is_prime(n) else "     ", rnd, ("%d" % (rnd // n)) if rnd % n == 0 else "-", before))

print("2. Each opening of + and - among n selves: each round, and its openings")
for n in range(2, 14):
    rounds = {}
    for op in product((1, -1), repeat=n):
        r = again(list(op))[1]
        rounds[r] = rounds.get(r, 0) + 1
    print("  %2d %s %s" % (n, "prime" if is_prime(n) else "     ",
                           "  ".join("%d: %d" % (r, c) for r, c in sorted(rounds.items()))))

print("3. Two folds among 1 to N: each set of four, by the name it goes first from")
for N in (4, 16, 64):
    h = N // 2
    sets = {}
    for a in range(1, N + 1):
        four = frozenset({a, a + h if a <= h else a - h, N + 1 - a, (N + 1 - a) + h if (N + 1 - a) <= h else (N + 1 - a) - h})
        sets[min(four)] = sorted(four)
    print("  N %2d: %2d sets of four, going first from %s" % (N, len(sets), sorted(sets)))
