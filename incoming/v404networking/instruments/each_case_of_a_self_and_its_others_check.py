"""Reads Exhibit ONE's code with each case of a self and its others, all or none, and says is or is not for each sentence.

Use, with the repository's top folder as its first word:
  python3 -I incoming/v404networking/instruments/each_case_of_a_self_and_its_others_check.py .

It reads one file, Exhibit ONE Natural Resolver's newest, and executes its code as it is. No case is drawn
by chance and no number of trials is read: each opening and each way of a finite laying is read in sequence.
Changing and changing back is a self's prior same-existing with one moment and inverting with the next:
do-no-harming and improving, the one and then the other.
"""
import glob
import itertools
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."


def version(p):
    m = re.search(r"_v(\d+)[A-Za-z]*\.md$", p)
    return int(m.group(1)) if m else 0


ONE = max(glob.glob(os.path.join(ROOT, "Exhibit_ONE_Natural_Resolver_v*.md")), key=version)
ns = {}
exec(re.search(r"```python\n(.*?)```", open(ONE, encoding="utf-8").read(), re.S).group(1), ns)
NEXT = ns["_17_next_existing"]
K = "x"


def prior(soc, s):
    return dict(soc[s][0]).get(K, 0)


def changing_and_changing_back(seq):
    same = [a == b for a, b in zip(seq, seq[1:])]
    return all(same[i] != same[i + 1] for i in range(len(same) - 1))


def each_opening(n, routes, moments):
    """is: each self of each opening comes to changing and changing back; else the first opening that does not"""
    for opening in itertools.product((1, -1), repeat=n):
        soc = {i: ([(K, opening[i])], []) for i in range(n)}
        seqs = [[opening[i]] for i in range(n)]
        for _ in range(moments):
            soc = NEXT(soc, routes)
            for i in range(n):
                seqs[i].append(prior(soc, i))
        for i in range(n):
            if not changing_and_changing_back(seqs[i][moments - 24:]):
                return "".join("+" if o > 0 else "-" for o in opening)
    return None


def say(sentence, found):
    print(f"{sentence} ({'is' if found is True else 'is not' if found is False else found})")


def chain(n):
    r = {(i, 9): i for i in range(n)}
    r.update({(i, 10): i + 1 for i in range(n - 1)})
    return r


def spiral(n, own=True):
    r = {(i, 9): i for i in range(n)} if own else {}
    r.update({(i, 10): (i + 1) % n for i in range(n)})
    return r


def torus(side):
    r = {}
    for s in range(side * side):
        x, y = s % side, s // side
        r[(s, 9)] = s
        r[(s, 10)] = y * side + (x + 1) % side
        r[(s, 6)] = ((y + 1) % side) * side + x
    return r


PRIOR_SELF = [(1, 0), (-1, -1), (-1, 0), (1, 1)]  # same-existing at +, inverted to -, same-existing at -, inverted to +
NEXT_SELF = [(1, False), (1, True), (-1, False), (-1, True)]  # its prior, and inverted with its last moment or not


def sixteen_ways():
    routes = {("P", 9): "P", ("P", 10): "S", ("S", 9): "S"}
    in_step = after = 0
    for (pp, pd), (sp, inverted) in itertools.product(PRIOR_SELF, NEXT_SELF):
        sd = sp if inverted else 0
        soc = {"P": ([(K, pp)], [(K, pd)] if pd else []), "S": ([(K, sp)], [(K, v) for v in (sd, pd) if v])}
        P, S = [pp], [sp]
        for _ in range(30):
            soc = NEXT(soc, routes)
            P.append(prior(soc, "P"))
            S.append(prior(soc, "S"))
        if not changing_and_changing_back(S[2:]):
            return False, 0, 0
        if S[8:24] == P[8:24]:
            in_step += 1
        elif S[8:24] == P[7:23]:
            after += 1
        else:
            return False, 0, 0
    return True, in_step, after


def prior_selves(k):
    names = [f"P{j}" for j in range(k)]
    routes = {(p, 9): p for p in names}
    routes.update({(p, 10): "S" for p in names})
    routes[("S", 9)] = "S"
    for moments in itertools.product(PRIOR_SELF, repeat=k):
        for sp, inverted in NEXT_SELF:
            sd = sp if inverted else 0
            soc = {p: ([(K, m[0])], [(K, m[1])] if m[1] else []) for p, m in zip(names, moments)}
            soc["S"] = ([(K, sp)], [(K, v) for v in [sd] + [m[1] for m in moments] if v])
            seq = [sp]
            for _ in range(48):
                soc = NEXT(soc, routes)
                seq.append(prior(soc, "S"))
            if not changing_and_changing_back(seq[16:]):
                return False
    return True


def two_both_ways(same_as):
    routes = {(0, 6): 1, (1, 6): 0}
    soc = {0: ([(K, 1)], []), 1: ([(K, 1 if same_as else -1)], [])}
    seqs = [[1], [1 if same_as else -1]]
    for _ in range(24):
        soc = NEXT(soc, routes)
        seqs[0].append(prior(soc, 0))
        seqs[1].append(prior(soc, 1))
    return seqs


print("code:", os.path.basename(ONE))
say("1. A self sharing with 9-next-co-discovering to itself, with none of its others, changes and changes back with each opening of its prior",
    each_opening(1, {(0, 9): 0}, 40) is None)
say("2. A chain of one to twelve selves comes from each opening to each self changing and changing back",
    all(each_opening(n, chain(n), 2 * n + 30) is None for n in range(1, 13)))
found, in_step, after = sixteen_ways()
say("3. In each of sixteen ways a self and its next self can be at a moment, the next self comes to changing and changing back, in step with its prior self or one moment after it",
    found)
print(f"   in step with its prior self: {in_step} ways; one moment after it, one right spiral step, a quarter turn: {after} ways")
say("4. A spiral of two to twelve selves, each sharing with 9-next-co-discovering to itself and with 10-next-co-possibling to its next, its last to its first, comes from each opening to each self changing and changing back",
    all(each_opening(n, spiral(n), 4 * n + 40) is None for n in range(2, 13)))
say("5. A torus of two by two and three by three selves comes from each opening to each self changing and changing back",
    all(each_opening(s * s, torus(s), 4 * s * s + 40) is None for s in (2, 3)))
for k in (1, 2, 3, 4):
    say(f"6.{k} A self sharing with 9-next-co-discovering to itself, observing {k} {'prior self' if k == 1 else 'prior selves'} changing and changing back with each moment apart, comes to changing and changing back",
        prior_selves(k))
same = two_both_ways(True)
other = two_both_ways(False)
say("7. Two selves with priors same-as, bi-coupling both ways, change and change back together",
    changing_and_changing_back(same[0][1:]) and same[0] == same[1])
say("8. Two selves with priors other-than, bi-coupling both ways, each improve with each moment, never do-no-harming",
    all(a != b for a, b in zip(other[0], other[0][1:])) and all(a != b for a, b in zip(other[1], other[1][1:])))
