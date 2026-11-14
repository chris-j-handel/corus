"""A self's two 0s, its possibling a 0 and its co-possibling a 0: each case, all or none.

Exhibit ONE's code, read from its file, no line changed. One self having a prior, by none to three parities of its others;
and two selves bi-coupling both ways, each of four cases of their priors, sixteen executings.
Run: python3 incoming/V401atom/instruments/two_zeros_check.py Exhibit_ONE_Natural_Resolver_v401mgr.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"

def places(prior, given):
    """a self's possibling, co-possibling and next prior, each a parity or a 0"""
    vals = [v for v in given if v != 0]
    poss = 0 if not vals or len(set(vals)) > 1 else vals[0]
    out, nxt = one([(S, prior)], [(S, v) for v in given])
    return poss, dict(out)[S], dict(nxt)[S]

both = neither_ok = same_ok = True; n = 0; kinds = set()
for prior in (1, -1):
    for k in range(4):
        for given in itertools.product((1, -1, 0), repeat=k):
            n += 1
            poss, co, nxt = places(prior, given)
            both = both and not (poss == 0 and co == 0)
            same_ok = same_ok and nxt != 0
            kinds.add((poss == 0, co == 0))
            # co-possibling a 0: its possibling same-as its prior, and its prior same-existing
            neither_ok = neither_ok and ((co == 0) == (poss == prior)) and ((co == 0) == (nxt == prior))
print("one self having a prior, cases:", n)
print("1 no case has its possibling a 0 and its co-possibling a 0, the two together:", both)
print("2 its co-possibling is a 0 by its possibling same-as its prior, and by no other case; its prior is then same-existing:", neither_ok)
print("3 its next prior is a parity in each case, and a 0 in none:", same_ok)
print("4 each case is one of three: no 0, improving; its co-possibling a 0, do-no-harming; its possibling a 0, bi-folding:",
      kinds == {(False, False), (False, True), (True, False)})

net = {("a", 10): "b", ("b", 10): "a"}
turn = together = none = True
for pa, pb in itertools.product((1, -1), repeat=2):
    soc = {"a": ([(S, pa)], []), "b": ([(S, pb)], [])}
    seq = {"a": [], "b": []}
    for t in range(16):
        for k in soc:
            prior = dict(soc[k][0])[S]
            given = [v for _key, v in soc[k][1]]
            poss, co, _nxt = places(prior, given)
            seq[k].append("bi" if poss == 0 else "co" if co == 0 else "none")
        soc = step(soc, net)
    a, b = seq["a"][2:], seq["b"][2:]          # from a third executing, each self having its other's co-possibling
    if pa == pb:
        turn = turn and all(x != "none" for x in a) and all(a[i] != a[i + 1] for i in range(len(a) - 1))
        together = together and a == b
        show = " ".join(a[:6])
    else:
        none = none and all(x == "none" for x in a + b)
print("two selves bi-coupling both ways, each of four cases of their priors, from a third executing:")
print("5 of parity: each self has one 0 each executing, its co-possibling a 0 and its possibling a 0 in turn:", turn, "·", show)
print("6 of parity: the two selves have the same one of the two 0s, each executing:", together)
print("7 of imparity: each self has no 0, each executing:", none)
