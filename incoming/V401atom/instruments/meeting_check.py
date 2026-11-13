"""A stable form's sequence along and a living self meeting it alone: each case, all or none. No opening by chance.

A stable form's parities along are given, one with each 1 to 17, and no line of the code is changing them.
A  a living self with a prior, + or -, observing the sequence alone: each of four cases of one 1 to 17,
   and from the four each sequence; each sequence of one to eight parities read too, each case.
B  the code's state of an empty prior, with the stable form's parity and the living self's sharing arriving: each of four.
C  with the code's own lines, what is along with 9 is 10-next-co-possibling's, the one same sharing as across.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/meeting_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one = ns["_1_now_existing"]
S = "s"

def resolve(prior, arriving):
    out, nxt = one([(S, prior)] if prior is not None else [], [(S, v) for v in arriving])
    return dict(out).get(S), dict(nxt).get(S)

four = [(p, f) for p in (1, -1) for f in (1, -1)]
print("A  a living self observing a stable form's sequence alone")
print("   1 with each of four cases, its next prior is the stable form's parity:", all(resolve(p, [f])[1] == f for p, f in four))
print("   2 with each of four, its sharing is a 0 or the stable form's parity, and not-the-same with none:",
      all(resolve(p, [f])[0] in (0, f) for p, f in four))
print("   3 its sharing is a 0 with its prior the same as the parity, and the parity with its prior not the same:",
      all(resolve(p, [f])[0] == (0 if p == f else f) for p, f in four))
n = 0; ok_prior = ok_share = ok_first = True
for k in range(1, 9):
    for seq in itertools.product((1, -1), repeat=k):
        ends = []
        for p in (1, -1):
            n += 1; prior = p; before = p
            for f in seq:
                s, prior = resolve(prior, [f])
                ok_prior = ok_prior and prior == f
                ok_share = ok_share and s == (0 if f == before else f)
                before = f
            ends.append(prior)
        ok_first = ok_first and ends[0] == ends[1]
print("   each sequence of one to eight parities, with each of two priors, cases:", n)
print("   4 its prior, with each 1 to 17, is the sequence's parity one 1 to 17 before:", ok_prior)
print("   5 its sharing is the sequence's parity with each changing along it, and a 0 with each not-changing:", ok_share)
print("   6 its own first prior is with its first sharing only, as is-or-is-not the same; from it each of two priors is one:", ok_first)

print("B  the code's state of an empty prior, with the stable form's parity and the living self's sharing arriving")
okB = True
for p, f in four:
    s = resolve(p, [f])[0]
    okB = okB and resolve(None, [f, s])[1] == f
print("   7 with each of four, a first prior is inherited, and it is the stable form's parity as it is:", okB)
print("   8 with the living self's own prior arriving in its place, each of four: inherited with co-parity only:",
      all((resolve(None, [f, p])[1] == f) == (p == f) and (resolve(None, [f, p])[1] is None) == (p != f) for p, f in four))

print("C  the code's own lines")
print("   9 6, 10 and 9 are each with 10-next-co-possibling, the one same sharing:",
      "_6_now_co_possibling = _10_next_co_possibling" in code
      and "((_13_next_discovering, 6), _6_now_co_possibling)" in code
      and "((_13_next_discovering, 10), _10_next_co_possibling)" in code
      and "((_13_next_discovering, 9), _10_next_co_possibling)" in code)
