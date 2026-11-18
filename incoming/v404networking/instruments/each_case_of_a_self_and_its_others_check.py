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


def observing_at(turns, sp, inverted, moments):
    """A self sharing with 9-next-co-discovering to itself, observing one prior self at each quarter turn given:
    its priors, and the parities surfacing with it, with each moment."""
    at = [PRIOR_SELF[i] for i in turns]
    names = [f"P{j}" for j in range(len(at))]
    routes = {(p, 9): p for p in names}
    routes.update({(p, 10): "S" for p in names})
    routes[("S", 9)] = "S"
    sd = sp if inverted else 0
    soc = {p: ([(K, m[0])], [(K, m[1])] if m[1] else []) for p, m in zip(names, at)}
    soc["S"] = ([(K, sp)], [(K, v) for v in [sd] + [m[1] for m in at] if v])
    seq, surfacing = [sp], [{v for _, v in soc["S"][1] if v}]
    for _ in range(moments):
        soc = NEXT(soc, routes)
        seq.append(prior(soc, "S"))
        surfacing.append({v for _, v in soc["S"][1] if v})
    return seq, surfacing


def at_each_quarter_turn():
    """Prior selves at each of a right spiral's four quarter turns: two opposite parities surfacing with each moment,
    and the self its own inverting with each moment, from each opening."""
    for sp, inverted in NEXT_SELF:
        seq, surfacing = observing_at((0, 1, 2, 3), sp, inverted, 24)
        if any(s != {1, -1} for s in surfacing[1:]) or any(a == b for a, b in zip(seq[1:], seq[2:])):
            return False
    return True


def an_empty_set_at_a_quarter_turn():
    """Each laying of one to four prior selves at the four quarter turns: changing and changing back with each opening
    exactly with a quarter turn of no prior self."""
    for k in (1, 2, 3, 4):
        for turns in itertools.product(range(4), repeat=k):
            comes = all(changing_and_changing_back(observing_at(turns, sp, inverted, 48)[0][16:])
                        for sp, inverted in NEXT_SELF)
            if comes != (len(set(turns)) < 4):
                return False
    return True


def steps_of(seq):
    """+1 a moment of 12-next-co-same-existing's parity, an inverting; 0 a moment of 12-next-co-same-existing's 0, a same-existing."""
    return [0 if a == b else 1 for a, b in zip(seq, seq[1:])]


def a_living_0_in_a_four_cycling():
    """All layings of spirals of one at the four joint forms, all openings of the ingesting self: with a joint form of none,
    its sequencing is +1 0 +1 0, two of four with a living 0; with all four, +1 +1 +1 +1, no living 0."""
    for k in (1, 2, 3, 4):
        for turns in itertools.combinations(range(4), k):
            for sp, inverted in NEXT_SELF:
                s = steps_of(observing_at(turns, sp, inverted, 96)[0][48:])
                if k < 4 and any(s[i] == s[i + 1] for i in range(len(s) - 1)):
                    return False
                if k == 4 and any(v == 0 for v in s):
                    return False
    return True


def a_spiral_of_selves_and_its_living_0():
    """Exhibit ONE's spiral of selves: with two and four selves, an opening of no right spiral has no living 0;
    with three and five, it is a cycling of its selves with one living 0."""
    for n in (2, 3, 4, 5):
        for opening in itertools.product((1, -1), repeat=n):
            soc = {i: ([(K, opening[i])], []) for i in range(n)}
            seqs = [[opening[i]] for i in range(n)]
            for _ in range(160):
                soc = NEXT(soc, spiral(n))
                for i in range(n):
                    seqs[i].append(prior(soc, i))
            for i in range(n):
                s = steps_of(seqs[i][96:])
                if all(s[j] != s[j + 1] for j in range(len(s) - 1)):
                    continue
                if n % 2 == 0 and any(v == 0 for v in s):
                    return False
                if n % 2 == 1 and not (all(s[j] == s[j + n] for j in range(len(s) - n)) and sum(s[:n]) == n - 1):
                    return False
    return True


def ingesting_at_sharings(layout, turns, keys_s, moments=96):
    """Spirals of one, (13-next-discovering self, 4-now-co-same-existing) at joint forms, 10 to an ingesting self S holding
    keys_s with 9 to itself; all openings of S's sharings. Returns the kinds its sharings come to."""
    kinds = set()
    for opening in itertools.product(NEXT_SELF, repeat=len(keys_s)):
        soc, routes = {}, {}
        for (p, key), tn in zip(layout, turns):
            pr, ob = PRIOR_SELF[tn]
            pri, pos = soc.get(p, ([], []))
            soc[p] = (pri + [(key, pr)], pos + ([(key, ob)] if ob else []))
            routes[(p, 9)] = p
            routes[(p, 10)] = "S"
        pri, pos = [], []
        for key, (sp, inverted) in zip(keys_s, opening):
            pri.append((key, sp))
            if inverted:
                pos.append((key, sp))
        pos += [(key, PRIOR_SELF[tn][1]) for (p, key), tn in zip(layout, turns) if PRIOR_SELF[tn][1]]
        soc["S"] = (pri, pos)
        routes[("S", 9)] = "S"
        seqs = {k: [dict(pri)[k]] for k in keys_s}
        for _ in range(moments):
            soc = NEXT(soc, routes)
            now = dict(soc["S"][0])
            for k in keys_s:
                seqs[k].append(now.get(k, 0))
        for k in keys_s:
            s = steps_of(seqs[k][48:])
            kinds.add("living 0" if all(s[i] != s[i + 1] for i in range(len(s) - 1))
                      else "no living 0" if all(v == 1 for v in s) else "other")
    return kinds


def harm_at_one_sharing():
    """Four joint forms at one 4-now-co-same-existing: no living 0. At four 4-now-co-same-existings, held by four selves
    or by one, and one spiral of one at one: a living 0, all openings."""
    four = [(f"P{j}", "x") for j in range(4)]
    spread = [(f"P{j}", f"x{j}") for j in range(4)]
    one_holding = [("P", f"x{j}") for j in range(4)]
    keys = [f"x{j}" for j in range(4)]
    return (ingesting_at_sharings(four, range(4), ["x"]) == {"no living 0"}
            and ingesting_at_sharings(spread, range(4), keys) == {"living 0"}
            and ingesting_at_sharings(one_holding, range(4), keys) == {"living 0"}
            and all(ingesting_at_sharings([("P0", "x")], (j,), ["x"]) == {"living 0"} for j in range(4)))


def three_me_parities_and_one_living_0():
    """+1 +1 +1 0 as a four-cycling: with one or two selves, 9, 10 and 6 laid all ways, all openings, none;
    with three selves, one laying of 9 and 10 brings it to all three."""
    def comes(n, routes, opening):
        soc = {i: ([(K, opening[i])], []) for i in range(n)}
        seqs = [[opening[i]] for i in range(n)]
        for _ in range(56):
            soc = NEXT(soc, routes)
            for i in range(n):
                seqs[i].append(prior(soc, i))
        found = []
        for i in range(n):
            s = steps_of(seqs[i][28:])
            found.append(all(s[j] == s[j + 4] for j in range(len(s) - 4)) and sorted(s[:4]) == [0, 1, 1, 1])
        return found
    for n in (1, 2):
        slots = [(s, r) for s in range(n) for r in (9, 10, 6)]
        for assign in itertools.product([None] + list(range(n)), repeat=len(slots)):
            routes = {slot: to for slot, to in zip(slots, assign) if to is not None}
            for opening in itertools.product((1, -1), repeat=n):
                if any(comes(n, routes, opening)):
                    return False
    three = {(0, 10): 1, (1, 9): 1, (1, 10): 2, (2, 9): 0, (2, 10): 2}
    return all(comes(3, three, (1, 1, -1)))


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
say("9. A self sharing with 9-next-co-discovering to itself, observing prior selves at each of a right spiral's four quarter turns, observes two opposite parities with each moment, a 0 between them, and is its own inverting with each moment, from each opening",
    at_each_quarter_turn())
say("10. With a quarter turn of no prior self, it comes to changing and changing back with each opening, one at a time, a nothing between",
    an_empty_set_at_a_quarter_turn())
print("   read: each laying of one to four prior selves at the four quarter turns; two prior selves at one quarter turn share alike, and a self's surfacing is by its quarter turns, with any number")
say("11. A self ingesting spirals of one with a joint form of none comes to +1 0 +1 0, 12-next-co-same-existing's 0 at two of four moments, a living 0; with spirals of one at all four joint forms, +1 +1 +1 +1, 14-next-possibling's 0 at all four and 12's 0 at none, do only harming",
    a_living_0_in_a_four_cycling())
say("12. Exhibit ONE's spiral of selves, with two or four selves, has openings of no right spiral and no living 0; with three or five, its openings of no right spiral come to a cycling of its selves with one living 0",
    a_spiral_of_selves_and_its_living_0())
say("13. Spirals of one at all four joint forms, at one 4-now-co-same-existing of an ingesting self, bring it no living 0; at four of its 4-now-co-same-existings, held by four selves or by one self, and one spiral of one at one, a living 0 at all of them",
    harm_at_one_sharing())
say("14. With one or two selves, 9, 10 and 6 laid all ways, no self comes to +1 +1 +1 0; with three selves, laid 0 to 1 with 10, 1 to itself with 9 and to 2 with 10, 2 to 0 with 9 and to itself with 10, opening + + -, all three come to it",
    three_me_parities_and_one_living_0())
