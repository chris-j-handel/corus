"""What remains unexplained, a partner's asking of 22 November: four of its places explored by executing.

Nothing is proved here.

1. A society of cells deeper than a table of cases. All its selves open with no
   prior, quiet until an other gives. A self with no prior gives the parity its
   others give with one parity among them, and nothing with two: Natural
   Intelligence 3.4's own sentence. A place of a question is two selves, the
   one a + with is and a - with is-not, and its other the other way. With a
   giver of + and a giver of - a moment, both, either and other-than are
   written, layer after layer, and two numbers of three places are added along
   their carry. A self gives to three others at the most, by its 6, 10 and 9.
2. A number the between of a living podal pair, by numbers' own arithmetic.
3. A spiral with its couplings the other way, by the living code.
4. Natural Numbers' own seventeen primes of 2 to 59.

    python3 -I incoming/v406Reiman/instruments/what_remains_explored.py .
"""
import itertools
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, resolver
from the_resolver_with_nand_alone import step_with_nand


def is_or_is_not(ok):
    return "is" if ok else "IS NOT"


class Layers:
    """A society of selves with no prior, layer after layer, built of a question's lines."""

    def __init__(self):
        self.made = {}
        self.order = []

    def giver(self, parity_of):
        name = ("giver", len(self.order))
        self.made[name] = ("giver", parity_of)
        self.order.append(name)
        return name

    def cell(self, *observed):
        name = ("cell", len(self.order))
        self.made[name] = ("cell", list(observed))
        self.order.append(name)
        return name

    def lay(self, answers):
        """Levels, then a self's givings to three others at the most, with selves of no prior passing a giving on."""
        slow = {name: 0 for name in self.order}
        while True:
            level = {}
            for name in self.order:
                kind, of = self.made[name]
                level[name] = 0 if kind == "giver" else max(level[o] + 1 + slow[o] for o in of)
            last = max(level[a] + 1 + slow[a] for a in answers)
            wanting = {name: [] for name in self.order}
            for name in self.order:
                kind, of = self.made[name]
                if kind == "cell":
                    for o in of:
                        wanting[o].append((name, level[name]))
            for k, a in enumerate(answers):
                wanting[a].append((("answer", k), last))
            couplings, selves, givers, again = {}, set(), {}, False
            for name in self.order:
                if not wanting[name]:
                    selves.add(name)
                    continue
                at = level[name]
                latest = max(t for _, t in wanting[name])
                wires = {}
                for t in range(latest, at, -1):
                    here = sum(1 for _, when in wanting[name] if when == t)
                    wires[t] = here + (math.ceil(wires[t + 1] / 3) if t < latest else 0)
                if self.made[name][0] == "giver":
                    frontier = [(name, k) for k in range(math.ceil(wires[at + 1] / 3))]
                    givers[name] = list(frontier)
                elif wires[at + 1] > 3:
                    slow[name] += 1
                    again = True
                    break
                else:
                    frontier = [name]
                selves.update(frontier)
                for t in range(at + 1, latest + 1):
                    passing = [(name, "passing", t, k) for k in range(math.ceil(wires[t + 1] / 3))] if t < latest else []
                    to = [who for who, when in wanting[name] if when == t] + passing
                    outlets = [(one, key) for one in frontier for key in (9, 10, 6)]
                    for outlet, who in zip(outlets, to):
                        couplings[outlet] = who
                    selves.update(passing)
                    frontier = passing
            if not again:
                break
        selves.update(("answer", k) for k in range(len(answers)))
        self.couplings, self.selves, self.givers, self.last = couplings, selves, givers, last
        return last

    def answer(self, step, case, answers):
        society = {one: ([], []) for one in self.selves}
        for name, copies in self.givers.items():
            parity = self.made[name][1](case)
            for one in copies:
                society[one] = ([], [(S, parity)] if parity else [])
        for _ in range(self.last):
            society = step(society, self.couplings)
        return [society[("answer", k)][1] for k in range(len(answers))]


def adding_in_layers(places):
    layers = Layers()
    plus, minus = layers.giver(lambda case: 1), layers.giver(lambda case: -1)

    def both_whole(u, v):
        return layers.cell(layers.cell(u, v, plus), layers.cell(layers.cell(u, minus), layers.cell(v, minus)))

    def either_whole(u, v):
        return layers.cell(layers.cell(u, v, minus), layers.cell(layers.cell(u, plus), layers.cell(v, plus)))

    def both(x, y):
        return both_whole(x[0], y[0]), either_whole(x[1], y[1])

    def either(x, y):
        return either_whole(x[0], y[0]), both_whole(x[1], y[1])

    def other_than(x):
        return x[1], x[0]

    def a_place(i):
        return (layers.giver(lambda case, i=i: 1 if case[i] else -1), layers.giver(lambda case, i=i: -1 if case[i] else 1))

    one, other = [a_place(i) for i in range(places)], [a_place(places + i) for i in range(places)]
    carry, added = None, []
    for a, b in zip(one, other):
        the_two = both(a, b)
        apart = both(either(a, b), other_than(the_two))
        if carry is None:
            added.append(apart)
            carry = the_two
        else:
            with_carry = both(apart, carry)
            added.append(both(either(apart, carry), other_than(with_carry)))
            carry = either(the_two, with_carry)
    added.append(carry)
    answers = [x[0] for x in added]
    return layers, answers, layers.lay(answers)


if __name__ == "__main__":
    root = sys.argv[1]
    names, page = resolver(root)
    step = names["_17_next_existing"]
    all_is = True

    print("1. A society of cells deeper than a table of cases")
    quiet = names["_1_now_existing"]([], []) == ([], [])
    one_parity = all(names["_1_now_existing"]([], [(S, v) for v in given])[0] == ([(S, 1)] if 1 in given and -1 not in given else [(S, -1)] if -1 in given and 1 not in given else [(S, 0)] if given else [])
                     for wide in range(4) for given in itertools.product((1, -1), repeat=wide))
    all_is = all_is and quiet and one_parity
    print(f"   a self with no prior, observing nothing, gives nothing and has no prior next; observing, it gives the parity its others give with one parity among them, and a 0 with two, none to three others: {is_or_is_not(quiet and one_parity)}")
    places = 3
    layers, answers, last = adding_in_layers(places)
    three = all(key in (9, 10, 6) for _, key in layers.couplings) and len(set(layers.couplings)) == len(layers.couplings)
    same = same_with_nand = True
    for case in itertools.product((False, True), repeat=2 * places):
        a = sum(1 << i for i in range(places) if case[i])
        b = sum(1 << i for i in range(places) if case[places + i])
        wanted = [[(S, 1)] if (a + b) >> i & 1 else [(S, -1)] for i in range(places + 1)]
        same = same and layers.answer(step, case, answers) == wanted
        same_with_nand = same_with_nand and layers.answer(step_with_nand, case, answers) == wanted
    all_is = all_is and three and same and same_with_nand
    print(f"   two numbers of 0 to 7 added along their carry by a society of {len(layers.selves)} selves of no prior, {last} layers, a self giving to three others at the most: its answer is the numbers' own adding with all 64 pairs, by the living code and by the cell by nand alone: {is_or_is_not(three and same and same_with_nand)}")

    print("2. A number the between of a living podal pair")
    to = 200000
    prime = bytearray([1]) * (2 * to + 2)
    prime[0] = prime[1] = 0
    for i in range(2, math.isqrt(2 * to + 1) + 1):
        if prime[i]:
            prime[i * i::i] = bytearray(len(prime[i * i::i]))
    between = six = True
    for n in range(4, to + 1):
        d = next((d for d in range(1, n - 1) if prime[n - d] and prime[n + d]), None)
        between = between and d is not None
    for p in range(5, 2001):
        if prime[p]:
            six = six and all(d % 6 == 0 for d in range(1, p - 3) if prime[p - d] and prime[p + d])
    all_is = all_is and between and six
    print(f"   a number of 4 to {to} is the between of a living podal pair: {is_or_is_not(between)}")
    print(f"   about a prime of 5 to 2000 a living podal pair with neither of its two three is at a multiple of six, all its pairs: {is_or_is_not(six)}")

    print("3. A spiral with its couplings the other way")
    mirror = True
    for q in (5, 7, 11, 13, 17, 19, 23):
        priors = exhibit_spiral_priors(q)
        one = {i: ([(S, priors[i])], []) for i in range(q)}
        other = {i: ([(S, priors[(-i) % q])], []) for i in range(q)}
        along, back = {(i, 9): (i + 1) % q for i in range(q)}, {(i, 9): (i - 1) % q for i in range(q)}
        for _ in range(4 * q):
            one, other = step(one, along), step(other, back)
            mirror = mirror and all(sorted(one[i][0]) == sorted(other[(-i) % q][0]) and sorted(one[i][1]) == sorted(other[(-i) % q][1]) for i in range(q))
    all_is = all_is and mirror
    print(f"   a spiral of 5 to 23 selves with its couplings the other way is its mirror, moment with moment, the cell having no right of its own: {is_or_is_not(mirror)}")

    print("4. Natural Numbers' own seventeen")
    seventeen = [n for n in range(2, 60) if prime[n]]
    all_is = all_is and len(seventeen) == 17 and seventeen[-1] == 59 and not prime[60]
    print(f"   the primes of 2 to 59 are seventeen, and sixty is no prime: {is_or_is_not(len(seventeen) == 17 and seventeen[-1] == 59 and not prime[60])}")

    print("All is, of the cases and numbers stepped." if all_is else "NOT ALL IS.")
