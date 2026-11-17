"""A going and a coming back, checked by whole numbers.

A field's Galois connection, in its form from a relation: things, properties,
and which thing has which property.

  going       a set of things      ->  each property each of them has
  coming back a set of properties  ->  each thing having each of them

It reads no file and writes none. It tries each relation there is between
three things and three properties, 512 of them, and each set of things and of
properties with each, and counts where a sentence fails.

Run:  python3 -I incoming/v404universe/instruments/a_going_and_a_coming_back_check.py
"""
from itertools import combinations, product


def subsets(items):
    items = list(items)
    return [frozenset(c) for n in range(len(items) + 1) for c in combinations(items, n)]


def check(things, properties, has):
    going = lambda s: frozenset(p for p in properties if all((t, p) in has for t in s))
    coming_back = lambda q: frozenset(t for t in things if all((t, p) in has for p in q))
    fails = dict.fromkeys(
        ["a going turns an order over", "a coming back turns an order over",
         "a going and a coming back has its start whole",
         "a going and a coming back keeps an order",
         "done twice is done once", "three are one",
         "closed things of the two sides are one to one"], 0)
    S, Q = subsets(things), subsets(properties)
    for a, b in product(S, S):
        if a <= b and not going(b) <= going(a):
            fails["a going turns an order over"] += 1
        if a <= b and not coming_back(going(a)) <= coming_back(going(b)):
            fails["a going and a coming back keeps an order"] += 1
    for a, b in product(Q, Q):
        if a <= b and not coming_back(b) <= coming_back(a):
            fails["a coming back turns an order over"] += 1
    for a in S:
        round_trip = coming_back(going(a))
        if not a <= round_trip:
            fails["a going and a coming back has its start whole"] += 1
        if coming_back(going(round_trip)) != round_trip:
            fails["done twice is done once"] += 1
        if going(round_trip) != going(a):
            fails["three are one"] += 1
    closed_things = {a for a in S if coming_back(going(a)) == a}
    closed_properties = {q for q in Q if going(coming_back(q)) == q}
    if {going(a) for a in closed_things} != closed_properties or \
            {coming_back(q) for q in closed_properties} != closed_things or \
            len(closed_things) != len(closed_properties):
        fails["closed things of the two sides are one to one"] += 1
    return fails, closed_things, closed_properties


def main():
    things, properties = ["t1", "t2", "t3"], ["p1", "p2", "p3"]
    pairs = list(product(things, properties))
    total = dict()
    relations = 0
    for bits in product([0, 1], repeat=len(pairs)):
        has = {pair for pair, bit in zip(pairs, bits) if bit}
        fails, _, _ = check(things, properties, has)
        relations += 1
        for k, v in fails.items():
            total[k] = total.get(k, 0) + v
    print(f"relations tried, three things by three properties: {relations}")
    for k, v in total.items():
        print(f"  {k}: fails {v}")

    print()
    print("one example")
    things = ["robin", "bat", "salmon", "stone"]
    properties = ["living", "flies", "swims"]
    has = {("robin", "living"), ("robin", "flies"), ("bat", "living"), ("bat", "flies"),
           ("salmon", "living"), ("salmon", "swims")}
    fails, closed_things, closed_properties = check(things, properties, has)
    going = lambda s: frozenset(p for p in properties if all((t, p) in has for t in s))
    coming_back = lambda q: frozenset(t for t in things if all((t, p) in has for p in q))
    start = frozenset(["robin"])
    there = going(start)
    back = coming_back(there)
    show = lambda s: "{" + ", ".join(sorted(s)) + "}"
    print(f"  start {show(start)}  going {show(there)}  coming back {show(back)}")
    print(f"  added by a going and a coming back: {show(back - start)}")
    print(f"  again: {show(coming_back(going(back)))}")
    print("  closed sets of things, each with its properties:")
    for a in sorted(closed_things, key=lambda s: (len(s), sorted(s))):
        print(f"    {show(a)}  with  {show(going(a))}")
    print(f"  fails in the example: {sum(fails.values())}")


if __name__ == "__main__":
    main()
