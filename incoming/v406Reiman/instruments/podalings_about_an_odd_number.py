"""Podalings: a self and an other facing, with one between, a partner's suggesting explored by executing.

Nothing is proved here. By a partner's word a podal pair has no prior side and
no next side: its sides are a self and an other, and a number is their
between. Exhibit ONE Natural Resolver has it, of its names: Sides, self and
other, each sharing between them.

Part 1 is Exhibit ONE Natural Resolver's code as it is in its living file. A
spiral of selves at a number is a between. A self has 9-next-co-discovering to
its next self, as Exhibit ONE opens a spiral. An other faces it: its
9-next-co-discovering is to the self whose next it is. A between self is
across, with 10-next-co-possibling of a self and of an other. Parts 2 and 3
are the surface of a_number_by_its_spirals.py, a self alone and odd prime
spirals side by side, two moments a number. No dividing is in parts 1 to 3.
Part 4 is by numbers' own arithmetic, with no resolver in it, and says so.

A print here is all or none: is, or is not, of all the numbers stepped. None
is an average, a measuring or a statistic.

    python3 -I incoming/v406Reiman/instruments/podalings_about_an_odd_number.py . [--to 3720]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, resolver
from a_number_by_its_spirals import priors_of


def the_surface_with_its_seams(step, to, open_to=59):
    """The surface of a_number_by_its_spirals.py, saying with a number the spirals at their seam with it."""
    society = {(1, 0): ([(S, exhibit_spiral_priors(1)[0])], [])}
    couplings = {((1, 0), 9): (1, 0)}
    opened = {1: (exhibit_spiral_priors(1)[0],)}
    uncrossed, seam = [], {2: set()}
    for k in range(2, to + 1):
        for _ in range(2):
            society = step(society, couplings)
        if priors_of(society, 1) == tuple(-x for x in opened[1]):
            seam[2].add(k)
        crossed = k in seam[2] and k > 2
        for q, was in opened.items():
            if q == 1:
                continue
            now = priors_of(society, q)
            if now == was or now == tuple(-x for x in was):
                seam[q].add(k)
                crossed = True
        if crossed:
            continue
        uncrossed.append(k)
        if k % 2 and k <= open_to:
            start = exhibit_spiral_priors(k)
            for i in range(k):
                society[(k, i)] = ([(S, start[i])], [])
                couplings[((k, i), 9)] = (k, (i + 1) % k)
            opened[k] = tuple(start[i] for i in range(k))
            seam[k] = {k}
    return uncrossed, seam


def a_spiral_alone(step, q, to):
    """A spiral of q selves from its opening, its society number by number, two moments a number."""
    society = {i: ([(S, exhibit_spiral_priors(q)[i])], []) for i in range(q)}
    along = {(i, 9): (i + 1) % q for i in range(q)}
    by_number = {q: society}
    for k in range(q + 1, to + 1):
        for _ in range(2):
            society = step(society, along)
        by_number[k] = society
    return by_number


def its_priors(society, q, ring=None):
    return tuple(dict(society[i if ring is None else (ring, i)][0]).get(S, 0) for i in range(q))


def a_self_and_an_other_facing(step, q):
    """A self with 9 to its next self and an other facing it, with one between, a between self across of both."""
    by_number = a_spiral_alone(step, q, 4 * q)
    opening = its_priors(by_number[q], q)

    def at_seam(p):
        return p == opening or p == tuple(-x for x in opening)

    nexts_priors = together = podal = one_parity = one_pair = True
    for c in range(2 * q, 3 * q + 1):
        between = by_number[c]
        was = its_priors(between, q)
        pairs = [i for i in range(q) if was[i] == was[(i + 1) % q]]
        one_pair = one_pair and len(pairs) == 1
        about = (2 * pairs[0] + 1) % q           # podal about the between's one pair of one parity: self i with self about - i
        its_own_podal = about * (q + 1) // 2 % q  # the self that is its own podal
        society, couplings = {}, {}
        for i in range(q):
            society[("self", i)] = (list(between[i][0]), list(between[i][1]))
            society[("other", i)] = (list(between[i][0]), list(between[i][1]))
            society[("between", i)] = ([], [])
            couplings[(("self", i), 9)] = ("self", (i + 1) % q)
            couplings[(("other", i), 9)] = ("other", (i - 1) % q)
            couplings[(("self", i), 10)] = ("between", i)
            couplings[(("other", i), 10)] = ("between", i)
        for d in range(1, q + 1):
            for _ in range(2):
                society = step(society, couplings)
            a_self, an_other = its_priors(society, q, "self"), its_priors(society, q, "other")
            nexts_priors = nexts_priors and a_self == its_priors(by_number[c + d], q) and an_other == its_priors(by_number[c - d], q)
            if at_seam(was):
                together = together and at_seam(a_self) == at_seam(an_other)
            else:
                together = together and not (at_seam(a_self) and at_seam(an_other))
            podal = podal and all(a_self[i] == an_other[(about - i) % q] for i in range(q))
            received = [v for s, v in society[("between", its_own_podal)][1] if s == S]
            one_parity = one_parity and len(received) == 2 and received[0] == received[1]
    return nexts_priors, together, podal, one_parity, one_pair


def a_new_spiral_in_the_between(step, q):
    """The between selves, with 10 of a self and of an other facing: their priors beside the between spiral's own."""
    by_number = a_spiral_alone(step, q, 5 * q)
    born = on_alone = True
    on_with_both = False
    for c in range(2 * q, 3 * q + 1):
        between = by_number[c]
        society, couplings = {}, {}
        for i in range(q):
            society[("self", i)] = (list(between[i][0]), list(between[i][1]))
            society[("other", i)] = (list(between[i][0]), list(between[i][1]))
            society[("between", i)] = ([], [])
            couplings[(("self", i), 9)] = ("self", (i + 1) % q)
            couplings[(("other", i), 9)] = ("other", (i - 1) % q)
            couplings[(("self", i), 10)] = ("between", i)
            couplings[(("other", i), 10)] = ("between", i)
        for _ in range(2):
            society = step(society, couplings)
        inverting = tuple(-x for x in its_priors(between, q))
        born = born and its_priors(society, q, "between") == inverting
        for with_both in (False, True):
            new = dict(society) if with_both else {("between", i): society[("between", i)] for i in range(q)}
            its = dict(couplings) if with_both else {}
            for i in range(q):
                its[(("between", i), 9)] = ("between", (i + 1) % q)
            all_on = True
            for k in range(1, q + 1):
                for _ in range(2):
                    new = step(new, its)
                all_on = all_on and its_priors(new, q, "between") == tuple(-x for x in its_priors(by_number[c + k], q))
            if with_both:
                on_with_both = on_with_both or all_on
            else:
                on_alone = on_alone and all_on
    return born, on_alone, on_with_both


def two_0s_in_the_between(step, q):
    """The 0s of a self and of an other, as the between selves receive them with a number."""
    by_number = a_spiral_alone(step, q, 5 * q)
    opening = its_priors(by_number[q], q)
    one_and_one = at_the_pair = one_self_on = together_once = parts_the_between = place = seam_by_a_0 = True
    for k in range(q, 5 * q + 1):                       # a number's place on its spiral
        was = its_priors(by_number[k], q)
        pair = [i for i in range(q) if was[i] == was[(i + 1) % q]]
        at_seam = was == opening or was == tuple(-x for x in opening)
        place = place and pair == [(q - 1 + k - q) % q] and at_seam == (pair == [q - 1])
    for c in range(2 * q, 3 * q + 1):
        between = by_number[c]
        was = its_priors(between, q)
        j = [i for i in range(q) if was[i] == was[(i + 1) % q]][0]
        its_own_podal = (2 * j + 1) * (q + 1) // 2 % q
        society, couplings = {}, {}
        for i in range(q):
            society[("self", i)] = (list(between[i][0]), list(between[i][1]))
            society[("other", i)] = (list(between[i][0]), list(between[i][1]))
            society[("between", i)] = ([], [])
            couplings[(("self", i), 9)] = ("self", (i + 1) % q)
            couplings[(("other", i), 9)] = ("other", (i - 1) % q)
            couplings[(("self", i), 10)] = ("between", i)
            couplings[(("other", i), 10)] = ("between", i)
        for d in range(1, q + 2):
            for _ in range(2):
                society = step(society, couplings)
            received = [[v for s, v in society[("between", i)][1] if s == S] for i in range(q)]
            of_a_self = [i for i in range(q) if received[i][0] == 0]
            of_an_other = [i for i in range(q) if received[i][1] == 0]
            one_and_one = one_and_one and len(of_a_self) == 1 and len(of_an_other) == 1
            if not one_and_one:
                continue
            s0, o0 = of_a_self[0], of_an_other[0]
            a_self, an_other = its_priors(society, q, "self"), its_priors(society, q, "other")
            at = lambda p: p == opening or p == tuple(-x for x in opening)
            seam_by_a_0 = seam_by_a_0 and (s0 == q - 1) == at(a_self) and (o0 == 0) == at(an_other)
            if d == 1:
                at_the_pair = at_the_pair and (o0, s0) == (j, (j + 1) % q)
            one_self_on = one_self_on and s0 == (j + d) % q and o0 == (j + 1 - d) % q
            together_once = together_once and ((s0 == o0) == (d % q == (q + 1) // 2)) and (s0 != o0 or s0 == its_own_podal)
            parting = {i for i in range(q) if received[i][0] * received[i][1] < 0}
            same = {i for i in range(q) if received[i][0] * received[i][1] > 0}
            arcs = []
            for a, b in ((o0, s0), (s0, o0)):
                arc, i = set(), (a + 1) % q
                while i != b and len(arc) < q:
                    arc.add(i)
                    i = (i + 1) % q
                arcs.append(arc)
            if {s0, o0} == {j, (j + 1) % q}:
                of_the_pair = set()
            else:
                of_the_pair = arcs[0] if j in arcs[0] else arcs[1]
            parts_the_between = parts_the_between and parting == of_the_pair and same == set(range(q)) - of_the_pair - {s0, o0}
    return one_and_one, at_the_pair, one_self_on, together_once, parts_the_between, place, seam_by_a_0


def one_parity_of_the_between(step, q):
    """The between self that is its own podal: what it receives of both, and its own prior, number with number."""
    by_number = a_spiral_alone(step, q, 4 * q + 2)
    own_prior = True
    moments = []
    for c in range(2 * q, 3 * q + 1):
        between = by_number[c]
        was = its_priors(between, q)
        j = [i for i in range(q) if was[i] == was[(i + 1) % q]][0]
        its_own_podal = (2 * j + 1) * (q + 1) // 2 % q
        society, couplings = {}, {}
        for i in range(q):
            society[("self", i)] = (list(between[i][0]), list(between[i][1]))
            society[("other", i)] = (list(between[i][0]), list(between[i][1]))
            society[("between", i)] = ([], [])
            couplings[(("self", i), 9)] = ("self", (i + 1) % q)
            couplings[(("other", i), 9)] = ("other", (i - 1) % q)
            couplings[(("self", i), 10)] = ("between", i)
            couplings[(("other", i), 10)] = ("between", i)
        priors = {}
        for d in range(1, 3 * q + 2):
            for _ in range(2):
                society = step(society, couplings)
                received = [v for s, v in society[("between", its_own_podal)][1] if s == S]
                moments.append(received[0] if received[0] == received[1] else None)
            priors[d] = its_priors(society, q, "between")[its_own_podal]
        for d in range(1, 3 * q + 1):
            with_the_0s = d % q == (q + 1) // 2 % q
            own_prior = own_prior and priors[d] != 0 and priors[d + 1] == (-priors[d] if with_the_0s else priors[d])
    return own_prior, moments


def all_parity_is_next(now, step):
    """Exhibit ONE Natural Resolver's 1-now-existing: a self's next prior beside the all-parity it is observing."""
    import itertools
    rule = True
    for prior in (1, -1):
        for size in (0, 1, 2, 3):
            for observing in itertools.product((-1, 0, 1), repeat=size):
                parities = [v for v in observing if v]
                all_parity = parities[0] if parities and all(v == parities[0] for v in parities) else 0
                _, next_prior = now([(S, prior)], [(S, v) for v in observing])
                rule = rule and dict(next_prior)[S] == (all_parity if all_parity else -prior)
    of_one = of_two = True
    q = 5
    by_number = a_spiral_alone(step, q, 3 * q)
    of_one = all(len(by_number[k][i][1]) <= 1 for k in by_number for i in range(q))
    between = by_number[2 * q]
    society, couplings = {}, {}
    for i in range(q):
        society[("self", i)] = (list(between[i][0]), list(between[i][1]))
        society[("other", i)] = (list(between[i][0]), list(between[i][1]))
        society[("between", i)] = ([], [])
        couplings[(("self", i), 9)] = ("self", (i + 1) % q)
        couplings[(("other", i), 9)] = ("other", (i - 1) % q)
        couplings[(("self", i), 10)] = ("between", i)
        couplings[(("other", i), 10)] = ("between", i)
    for _ in range(4 * q):
        society = step(society, couplings)
        of_two = of_two and all(len(society[("between", i)][1]) == 2 for i in range(q))
    return rule, of_one and of_two


def a_0_and_its_next(step, q):
    """A spiral facing as Exhibit ONE opens it, and a spiral facing it: its 0 with a number, and the self next of the 0."""
    a_self_it_is = one_self_on = in_turn = True
    for facing in (1, -1):
        society = {i: ([(S, exhibit_spiral_priors(q)[i])], []) for i in range(q)}
        along = {(i, 9): (i + facing) % q for i in range(q)}
        before = None
        for k in range(q + 1, 3 * q + 3):
            for _ in range(2):
                society = step(society, along)
            gives = [None] * q
            for i in range(q):
                received = [v for s, v in society[i][1] if s == S]
                gives[(i - facing) % q] = received[0] if received else None
            priors = its_priors(society, q)
            pair = [i for i in range(q) if priors[i] == priors[(i + 1) % q]]
            zero = [i for i in range(q) if gives[i] == 0]
            if len(pair) != 1 or len(zero) != 1:
                a_self_it_is = False
                continue
            first_of_the_pair = pair[0] if facing == 1 else (pair[0] + 1) % q
            a_self_it_is = a_self_it_is and zero[0] == first_of_the_pair
            if before is not None:
                one_self_on = one_self_on and zero[0] == (before + facing) % q
            before = zero[0]
            in_turn = in_turn and gives[(zero[0] + facing) % q] == (1 if k % 2 == 0 else -1)
    return a_self_it_is, one_self_on, in_turn


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


if __name__ == "__main__":
    root = sys.argv[1]
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 3720
    names, page = resolver(root)
    step = names["_17_next_existing"]
    uncrossed, seam = the_surface_with_its_seams(step, to)
    U = set(uncrossed)
    odd_spirals = sorted(q for q in seam if q > 2)
    all_is = True

    print("1. A self and an other facing, with one between, with Exhibit ONE Natural Resolver's code as it is")
    print(f"   {len(odd_spirals)} odd spirals, 3 to 59 selves, a spiral alone; a turn of betweens, and a turn of distances with a between")
    nexts_priors = together = podal = one_parity = one_pair = True
    for q in odd_spirals:
        n, t_, p, o, l = a_self_and_an_other_facing(step, q)
        nexts_priors, together, podal, one_parity, one_pair = nexts_priors and n, together and t_, podal and p, one_parity and o, one_pair and l
    all_is = all_is and nexts_priors and together and podal and one_parity and one_pair
    print(f"   an other's nexts are a self's priors: an other is as the spiral was with the number as far short of the between, and a self as the number as far past it: {is_or_is_not(nexts_priors)}")
    print(f"   with the between at the spiral's seam, a self and an other are at the seam together or neither; with the between off it, never together: {is_or_is_not(together)}")
    print(f"   a spiral at a number has one pair of one parity: {is_or_is_not(one_pair)} · a self and an other are podal about it, with all moments, a self's parities an other's at the podal selves: {is_or_is_not(podal)}")
    print(f"   the between self that is its own podal has one parity, the same of a self and of an other, with all moments, and never + with -: {is_or_is_not(one_parity)}")
    born = on_alone = True
    on_with_both = False
    for q in odd_spirals:
        b, a, w = a_new_spiral_in_the_between(step, q)
        born, on_alone, on_with_both = born and b, on_alone and a, on_with_both or w
    all_is = all_is and born and on_alone and not on_with_both
    print(f"   a new spiral in the between: with 10-next-co-possibling of a self and of an other alone, the between selves have the between spiral's own priors, all inverting, with the next number: {is_or_is_not(born)}")
    print(f"   the new spiral, with its own 9-next-co-discovering and 10 of no other, is the spiral on, number with number, all inverting: {is_or_is_not(on_alone)}")
    print(f"   with 10 of a self and of an other still, and its own 9, the between is no spiral on: {is_or_is_not(not on_with_both)}")
    z = [True] * 7
    for q in odd_spirals:
        z = [a and b for a, b in zip(z, two_0s_in_the_between(step, q))]
    all_is = all_is and all(z)
    print(f"   two 0s in the between: with a number, the between selves receive one 0 of a self and one 0 of an other, and no other 0: {is_or_is_not(z[0])}")
    print(f"   with the next number the two 0s are with the between's own pair of one parity, a 0 a self of the pair: {is_or_is_not(z[1])}")
    print(f"   with a number more, a self's 0 is with its next self, and an other's 0 with the self whose next it is, the two podal: {is_or_is_not(z[2])}")
    print(f"   the two 0s are with one between self once a turn of the spiral, and it is the one that is its own podal: {is_or_is_not(z[3])}")
    print(f"   the two 0s part the between: on the side of its pair of one parity a self and an other are + with -, and on the side of its own podal self the same: {is_or_is_not(z[4])}")
    print(f"   a number's place on a spiral: its one pair of one parity is one self on with a number, and at the spiral's opening place at its seam and at no other number: {is_or_is_not(z[5])}")
    print(f"   a self is at the spiral's seam with a self's 0 at the spiral's last self, and at no other number; an other, with an other's 0 at the spiral's self 1: {is_or_is_not(z[6])}")
    f = [True] * 3
    for q in odd_spirals:
        f = [a and b for a, b in zip(f, a_0_and_its_next(step, q))]
    all_is = all_is and all(f)
    print(f"   a spiral's 0 is a self: with a number one self of it gives a 0, the self of its pair of one parity it is facing with, a self's facing and an other's: {is_or_is_not(f[0])}")
    print(f"   with the next number the 0 is one self on, in its own facing: {is_or_is_not(f[1])}")
    print(f"   the self next of the 0, in its facing, gives + with an even number and - with an odd number, + and - in turn: {is_or_is_not(f[2])}")
    own_prior = all(one_parity_of_the_between(step, q)[0] for q in odd_spirals)
    of_one = one_parity_of_the_between(step, 1)[1][:8]
    one_self = of_one in ([1, 0, -1, 0, 1, 0, -1, 0], [-1, 0, 1, 0, -1, 0, 1, 0])
    all_is = all_is and own_prior and one_self
    print(f"   the between self that is its own podal has its own prior, one parity, the same number with number, and inverting with the number next after the two 0s are with it: {is_or_is_not(own_prior)}")
    print(f"   with a spiral of one self, the between self receives of both +, 0, -, 0, moment with moment, Exhibit ONE Natural Resolver's own row of one self: {is_or_is_not(one_self)}")
    next_rule, of_two = all_parity_is_next(names["_1_now_existing"], step)
    all_is = all_is and next_rule and of_two
    print(f"   all-parity is next: with 1-now-existing, all cases of a prior and of none to three parities a self is observing, its next prior is their all-parity, the same of all or a 0 of + with -, and with a 0 its prior inverting: {is_or_is_not(next_rule)}")
    print(f"   a self of a spiral is observing of one self, and a between self of two, a self and an other: {is_or_is_not(of_two)}")

    print("2. The surface, all spirals side by side: a number a between, with a self and an other at one distance of it")
    print(f"   2 to {to}, a self alone and {len(odd_spirals)} odd spirals, all its numbers and all their distances gone through")
    rule_at = rule_off = places = True
    for q in odd_spirals:
        for c in range(q, to + 1):
            at = c in seam[q]
            for d in range(1, min(c - q, to - c) + 1):
                an_other, a_self = (c - d) in seam[q], (c + d) in seam[q]
                if at:
                    rule_at = rule_at and an_other == a_self
                else:
                    rule_off = rule_off and not (an_other and a_self)
            if c >= 2 * q and c + q <= to:
                living = sum(1 for d in range(1, q + 1) if (c - d) not in seam[q] and (c + d) not in seam[q])
                places = places and living == (q - 1 if at else q - 2)
    two = all(((c - d) in seam[2]) == ((c + d) in seam[2]) for c in range(4, to) for d in range(1, min(c - 2, to - c) + 1))
    all_is = all_is and rule_at and rule_off and places and two
    print(f"   at its seam with their between, a spiral crosses a self and an other together or neither: {is_or_is_not(rule_at)}")
    print(f"   off its seam with their between, a spiral crosses one of the two and never both: {is_or_is_not(rule_off)}")
    print(f"   of one turn of a spiral's distances, all but one are with neither crossed at its seam, and all but two off it: {is_or_is_not(places)}")
    print(f"   the self alone, two, crosses a self and an other together or neither, with all betweens: {is_or_is_not(two)}")

    print("3. An odd number a between, by the surface's uncrossed numbers and its seams alone")
    fives = range(5, to - 3, 2)
    one_of_three = all(sum(1 for m in (n, n + 2, n + 4) if m in seam[3]) == 1 for n in fives)
    most_two = all(sum(1 for m in (n, n + 2, n + 4) if m in U) <= 2 for n in fives)
    all_is = all_is and one_of_three and most_two
    print(f"   a five opening with an odd number: three odd numbers and two even, and of its three odd numbers one is at three's seam: {is_or_is_not(one_of_three)}")
    print(f"   a five above 3 has two uncrossed at the most, two apart or four apart: {is_or_is_not(most_two)}")

    pairs = (2, 4, 6, 8)
    centres = range(15, to - 7, 2)

    def crossed_of_the_two(c, d, q):
        return ((c - d) in seam[q]) + ((c + d) in seam[q])

    three_at = all([crossed_of_the_two(c, d, 3) for d in pairs] == [0, 0, 2, 0] for c in centres if c in seam[3])
    three_off = all([crossed_of_the_two(c, d, 3) for d in pairs] == [1, 1, 0, 1] for c in centres if c not in seam[3])
    five_at = all(all(crossed_of_the_two(c, d, 5) == 0 for d in pairs) for c in centres if c in seam[5])
    five_off = all(sorted(crossed_of_the_two(c, d, 5) for d in pairs) == [0, 0, 1, 1] for c in centres if c not in seam[5])
    all_is = all_is and three_at and three_off and five_at and five_off
    print("   a 1 to 17 with its 9 on an odd number, the between: its odd names two and two about 9 are four podal pairs, a self and an other at 2, 4, 6 and 8")
    print(f"   three, at its seam with the between, crosses neither of the two at 2, 4 and 8, and both at 6: {is_or_is_not(three_at)}")
    print(f"   three, off its seam, crosses one of the two at 2, at 4 and at 8, and neither at 6: {is_or_is_not(three_off)}")
    print(f"   five, at its seam with the between, crosses neither of the two at all four: {is_or_is_not(five_at)}")
    print(f"   five, off its seam, crosses one of the two at two of the four, and neither at its other two: {is_or_is_not(five_off)}")

    living = {c: [d for d in pairs if c - d in U and c + d in U] for c in centres}
    diamonds = [c for c in centres if 2 in living[c] and 4 in living[c]]
    diamond_is = all(c in seam[3] and c in seam[5] for c in diamonds)
    six_primes = [c for c in centres if living[c] == [2, 4, 8]]
    six_is = all(c in seam[3] and c in seam[5] for c in six_primes)
    a_prime_between = all(set(living[c]) <= {6} for c in centres if c in U)
    primes_with_none = [c for c in centres if c in U and not living[c]]
    primes_with_six = [c for c in centres if c in U and living[c] == [6]]
    none_rule = all(not living[c] for c in centres
                    if c not in seam[3] and ((c - 1) in seam[5] or (c + 1) in seam[5]))
    all_is = all_is and diamond_is and six_is and a_prime_between and none_rule
    print(f"   with 2 and 4 both living, the between is at the seam of three and of five: {is_or_is_not(diamond_is)} · found: {', '.join(map(str, diamonds))}")
    print(f"   with 2, 4 and 8 all living, six primes with one between: found {' and '.join(map(str, six_primes))}, at the seam of three and of five: {is_or_is_not(six_is)}")
    print(f"   with a prime the between, a living podal pair of its 1 to 17 is at 6 and at no other: {is_or_is_not(a_prime_between)}")
    print(f"   primes with it living at 6, from 17 on: {', '.join(map(str, primes_with_six[:6]))} · and with none: {', '.join(map(str, primes_with_none[:6]))}")
    print(f"   a between off three's seam, and one past or one short of five's seam, has no living podal pair in its 1 to 17: {is_or_is_not(none_rule)}")

    gaps = (2, 4, 6, 12, 24, 36)
    wide = range(43, to - 35, 2)
    gaps_at_three = all([d for d in gaps if not crossed_of_the_two(c, d, 3)] == [2, 4] for c in wide if c in seam[3])
    gaps_off_three = all([d for d in gaps if not crossed_of_the_two(c, d, 3)] == [6, 12, 24, 36] for c in wide if c not in seam[3])
    seven_at = all(all(crossed_of_the_two(c, d, 7) == 0 for d in gaps) for c in wide if c in seam[7])
    seven_off = all(sorted(crossed_of_the_two(c, d, 7) for d in gaps) == [0, 0, 0, 0, 1, 1] for c in wide if c not in seam[7])
    by_six = all(not ({c - d, c + d} & (seam[2] | seam[3]))
                 for c in range(43, to - 35) if c not in seam[2] and c not in seam[3] for d in (6, 12, 24, 36))
    all_is = all_is and gaps_at_three and gaps_off_three and seven_at and seven_off and by_six
    print("   a partner's six gaps, 2, 4, 6, 12, 24 and 36, a self and an other at a gap of an odd between, forward and backward")
    print(f"   three, at its seam with the between, crosses neither of the two at 2 and at 4, and at no other of the six: {is_or_is_not(gaps_at_three)}")
    print(f"   three, off its seam, crosses neither of the two at 6, 12, 24 and 36, and at no other of the six: {is_or_is_not(gaps_off_three)}")
    print(f"   seven, at its seam with the between, crosses neither of the two at all six; off its seam, one of the two at two of the six: {is_or_is_not(seven_at and seven_off)}")
    print(f"   a number uncrossed by two and by three has the numbers at 6, 12, 24 and 36 of it, forward and backward, uncrossed by two and by three: {is_or_is_not(by_six)}")

    outward = all(any(c - d in U and c + d in U for d in range(0, c - 1)) for c in range(4, to // 2 + 1))
    all_is = all_is and outward
    print(f"   a number, 4 to {to // 2}, is the between of a self and an other both uncrossed, found outward of it: {is_or_is_not(outward)}")

    print("4. By numbers' own arithmetic, with no resolver in it")
    turn = 3 * 5 * 7
    by_places_is = never_none = True
    for c in range(1, 2 * turn, 2):
        found = sum(1 for e in range(turn) if all((c - 2 * e) % q and (c + 2 * e) % q for q in (3, 5, 7)))
        by_places = 1
        for q in (3, 5, 7):
            by_places *= q - 1 if c % q == 0 else q - 2
        by_places_is = by_places_is and found == by_places
        never_none = never_none and found > 0
    all_is = all_is and by_places_is and never_none
    print(f"   a closed turn of three, five and seven: the pairs uncrossed by all three are a spiral's places less one at its seam and less two off it, multiplied: {is_or_is_not(by_places_is)}")
    print(f"   with an odd between, a closed turn has a pair uncrossed by all three, never none: {is_or_is_not(never_none)}")

    print("All is." if all_is else "NOT ALL IS.")
