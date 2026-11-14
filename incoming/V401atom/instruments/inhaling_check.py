"""A self by a snippet, a co-chaining of atoms one after one; and a self by atoms each its own. Each case, all or none.

Exhibit ONE's code, read from its file, no line changed. An atom is one parity, + or -, same-existing; no line changes it.
Run: python3 incoming/V401atom/instruments/inhaling_check.py Exhibit_ONE_Natural_Resolver_v401mgr.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one = ns["_1_now_existing"]
S = "s"
def run(prior, given_each):                      # a self's priors, one by each executing, by what it has each executing
    out = []
    for given in given_each:
        out.append(prior)
        _co, nxt = one([(S, prior)], [(S, v) for v in given])
        prior = dict(nxt)[S]
    return out + [prior]
own = lambda p, n: [p * (-1) ** i for i in range(n)]          # by all-parity alone: its own alternating
T = 8
print("0 a self by all-parity alone, none of its others: its priors are the one and the other of two, in turn, its own alternating:",
      all(run(p, [[]] * T) == own(p, T + 1) for p in (1, -1)))
a = b = 0; follows = True; ownkept = 0
for p in (1, -1):
    for n in range(2, T + 1):
        for s in itertools.product((1, -1), repeat=n):
            a += 1
            got = run(p, [[v] for v in s])
            follows = follows and got[1:] == list(s)                      # each prior after the first is the snippet's parity, one executing on
            ownkept += got == own(p, n + 1)
print("1 a self by a snippet alone, one atom of it each executing, cases:", a)
print("  each of its priors after its first is the snippet's parity of the executing before, as it is:", follows)
print("  its priors are its own alternating in", ownkept, "cases: the snippet itself the one and the other in turn, from its prior's other; and in no other case")
free = True; same_side = True
for p in (1, -1):
    for k in (2, 3):
        for atoms in itertools.product(itertools.product((1, -1), repeat=k), repeat=4):
            b += 1
            mixed = all(len(set(g)) == 2 for g in atoms)
            got = run(p, [list(g) for g in atoms])
            if mixed:
                free = free and got == own(p, 5)
print("2 a self by atoms each its own, two or three each executing, cases:", b)
print("  by atoms of the one orientation and the other together, each executing: a 0, and its priors are its own alternating, as by all-parity alone:", free)

# a snippet taken whole, each atom of it together in one executing: its order, one after one, is in no line
c = 0; order = True; kinds = True
for p in (1, -1):
    for n in range(2, 7):
        for s in itertools.product((1, -1), repeat=n):
            res = set()
            for perm in set(itertools.permutations(s)):
                c += 1
                co, nxt = one([(S, p)], [(S, v) for v in perm])
                res.add((dict(co)[S], dict(nxt)[S]))
            order = order and len(res) == 1
            co, nxt = res.pop()
            both = len(set(s)) == 2
            kinds = kinds and ((both and co == -p and nxt == -p) or (not both and s[0] == p and co == 0 and nxt == p) or (not both and s[0] != p and co == s[0] and nxt == s[0]))
print("3 a self by a snippet whole, each atom of it together in one executing, each order of it, cases:", c)
print("  what the lines return is the same by each order of the snippet: its one after one is in no line:", order)
print("  by a snippet of both orientations: a 0, bi-folding, as by all-parity alone; by a snippet of one orientation: that one parity, as one atom:", kinds)
