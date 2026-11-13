"""A self's exhausted parities, one after one, and a later self with them: each case, all or none. No opening by chance.

A self with a prior, + or -, and a sequence of one to eight 1 to 17s, with each of them nothing, +, - or 0 arriving.
Its 10-next-co-possibling with each 1 to 17: a parity with each distinguishing, and a 0 with nothing distinguished.
Its exhausted sequence is each parity of them, one after one, each 0 out of it. And a later self, with a prior + or -,
with that sequence arriving alone, one with each 1 to 17.
Exhibit ONE's code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/exhausted_sequence_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one = ns["_1_now_existing"]
S = "s"

def live(prior, arriving_seq):
    tens, priors = [], []
    for a in arriving_seq:
        out, nxt = one([(S, prior)], [] if a is None else [(S, a)])
        tens.append(dict(out)[S]); prior = dict(nxt)[S]; priors.append(prior)
    return tens, priors

n = 0; ok1 = ok2 = ok3 = ok4 = ok5 = True; seen = set()
for k in range(1, 9):
    for seq in itertools.product((None, 1, -1, 0), repeat=k):
        for p in (1, -1):
            n += 1
            tens, priors = live(p, seq)
            E = [v for v in tens if v != 0]
            ok1 = ok1 and all(E[i] == -E[i - 1] for i in range(1, len(E)))
            ok2 = ok2 and (not E or E[0] == -p)
            ok3 = ok3 and E == [priors[i] for i, v in enumerate(tens) if v != 0]
            seen.add(tuple(E))
            for q in (1, -1):
                tens2, priors2 = live(q, E)
                ok4 = ok4 and priors2 == E
                E2 = [v for v in tens2 if v != 0]
                ok5 = ok5 and (E2 == E if (not E or q != E[0]) else E2 == E[1:])
print("cases, a prior + or -, with one to eight 1 to 17s, each with nothing, +, - or 0 arriving:", n)
print("1  a self's exhausted parities, one after one, each 0 out of them, are alternating, each the one before it inverted:", ok1)
print("2  the first of them is its first prior inverted:", ok2)
print("3  each of them is its next prior with that distinguishing, as it is:", ok3)
print("   each exhausted sequence of the cases is alternating from + or from -, and no other is:",
      all(all(E[i] == -E[i - 1] for i in range(1, len(E))) for E in seen), "; sequences not the same:", len(seen))
print("4  a later self with that sequence arriving alone, one with each 1 to 17, each of two priors: its priors are the sequence, one with one:", ok4)
print("5  and its own exhausted sequence is that sequence again; with its first prior the same as the first of them, from the second:", ok5)
