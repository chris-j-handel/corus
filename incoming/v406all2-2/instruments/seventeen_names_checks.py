"""The seventeen names: the numbers of the opening's proposed lines 38 to 46, executed.

Usage: python3 -I incoming/v406all2-2/instruments/seventeen_names_checks.py [incoming/v403mgr/The_seventeen_names_in_one_table.csv]
Own arithmetic alone: no code of a living file is executed here. A line is "is" or "is-not".
"""
import csv, sys

lines = []
def say(what, ok):
    lines.append(("is    " if ok else "is-not") + " · " + what)
    return ok

up8 = lambda n: n + 8
down8 = lambda n: n - 8
less17 = lambda n: 17 - n
less9 = lambda n: 9 - n if n <= 8 else 25 - n      # 9 less, with an eight

# 1. A name's three, by Exhibit ONE's saying: a prefix of an eight, co bi co bi co bi tri bi,
#    and a name's three its own prefix and the prefixes of the two names before it.
eight = ["co", "bi", "co", "bi", "co", "bi", "tri", "bi"]
p = lambda n: eight[(n - 1) % 8]
three = {n: "-".join([p(n), p(n - 1), p(n - 2)]) for n in range(1, 18)}
table = {1: "co-bi-tri", 2: "bi-co-bi", 3: "co-bi-co", 4: "bi-co-bi", 5: "co-bi-co", 6: "bi-co-bi",
         7: "tri-bi-co", 8: "bi-tri-bi", 9: "co-bi-tri", 10: "bi-co-bi", 11: "co-bi-co", 12: "bi-co-bi",
         13: "co-bi-co", 14: "bi-co-bi", 15: "tri-bi-co", 16: "bi-tri-bi", 17: "co-bi-tri"}
say("a name's three, by its saying, is the table's three, 1 to 17", three == table)
say("1, 9 and 17 are one three, co-bi-tri", three[1] == three[9] == three[17] == "co-bi-tri")

# 2. The four bi-foldings, 8 up or down and 17 less in turn, come to their starting name again.
def round_of(start, moves):
    seq, n = [start], start
    for m in moves:
        n = m(n); seq.append(n)
    return seq
say("1-9-8-16: 8 up, 17 less, 8 up, 17 less", round_of(1, [up8, less17, up8, less17]) == [1, 9, 8, 16, 1])
say("3-11-6-14: 8 up, 17 less, 8 up, 17 less", round_of(3, [up8, less17, up8, less17]) == [3, 11, 6, 14, 3])
say("2-15-7-10: 17 less, 8 down, 17 less, 8 down", round_of(2, [less17, down8, less17, down8]) == [2, 15, 7, 10, 2])
say("4-13-5-12: 17 less, 8 down, 17 less, 8 down", round_of(4, [less17, down8, less17, down8]) == [4, 13, 5, 12, 4])
four = ([1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12])
say("a move of the four bi-foldings is 8 apart or 17 less, and none is 4 apart",
    all(abs(f[i] - f[(i + 1) % 4]) == 8 or f[i] + f[(i + 1) % 4] == 17 for f in four for i in range(4)))

# 3. The two middle bi-foldings, by 4 and 17 less.
up4, down4 = (lambda n: n + 4), (lambda n: n - 4)
say("9-5-12-8: 4 down, 17 less, 4 down, 17 less", round_of(9, [down4, less17, down4, less17]) == [9, 5, 12, 8, 9])
say("7-11-6-10: 4 up, 17 less, 4 up, 17 less", round_of(7, [up4, less17, up4, less17]) == [7, 11, 6, 10, 7])

# 4. With 1 to 9: two loops of four names, by 4 up and 9 less, all eight now names between them.
l9 = lambda n: 9 - n
a = round_of(3, [up4, l9, up4, l9]); b = round_of(4, [up4, l9, up4, l9])
say("3-7-2-6 and 4-8-1-5, by 4 up and 9 less", a == [3, 7, 2, 6, 3] and b == [4, 8, 1, 5, 4])
say("the two loops are all eight now names", sorted(a[:4] + b[:4]) == list(range(1, 9)))

# 5. Outward: a loop's four names open to two bi-foldings.
say("3, 7, 2, 6 open to 3-11-6-14 and 2-15-7-10", {3, 6} | {2, 7} == set(a[:4]) and {3, 11, 6, 14} & set(range(1, 9)) == {3, 6} and {2, 15, 7, 10} & set(range(1, 9)) == {2, 7})
say("4, 8, 1, 5 open to 4-13-5-12 and 1-9-8-16", {4, 13, 5, 12} & set(range(1, 9)) == {4, 5} and {1, 9, 8, 16} & set(range(1, 9)) == {1, 8})

# 6. 8 up is two folds: 9 less, with an eight, and then 17 less. A fold exchanges odd and even; 8 up does not.
say("8 up is 9 less and then 17 less, 1 to 8", all(less17(less9(n)) == n + 8 for n in range(1, 9)))
say("8 down is 9 less and then 17 less, 9 to 16", all(less17(less9(n)) == n - 8 for n in range(9, 17)))
say("9 less is 8 up and then 17 less, 1 to 8 (Exhibit ONE: two moves, 9 less)", all(less17(up8(n)) == 9 - n for n in range(1, 9)))
say("17 less exchanges odd and even, 1 to 16", all((less17(n) - n) % 2 == 1 for n in range(1, 17)))
say("9 less exchanges odd and even, 1 to 16", all((less9(n) - n) % 2 == 1 for n in range(1, 17)))
say("8 apart brings odd onto odd and even onto even", all((up8(n) - n) % 2 == 0 for n in range(1, 9)))
say("9 less and then 17 less, in turn, go round a bi-folding's four names: 1-8-9-16", round_of(1, [less9, less17, less9, less17]) == [1, 8, 9, 16, 1])
for start, names in ((2, {2, 15, 7, 10}), (3, {3, 11, 6, 14}), (4, {4, 13, 5, 12})):
    r = round_of(start, [less9, less17, less9, less17])
    say(f"the two folds in turn from {start} go round {sorted(names)}", set(r) == names and r[-1] == start)

# 7. The four parities of a name, one inverting with a name (the table's own, executed): a fold inverts one, 8 up two.
gray = lambda n: (n - 1) ^ ((n - 1) >> 1)
bits = lambda x: sum(int(d) for d in bin(x)[2:])
say("a name to its next name inverts one parity of four, 1 to 16", all(bits(gray(n) ^ gray(n + 1)) == 1 for n in range(1, 16)))
say("17 less inverts one parity of four, the fourth", all(gray(n) ^ gray(less17(n)) == 8 for n in range(1, 17)))
say("9 less, with an eight, inverts one parity of four, the third", all(gray(n) ^ gray(less9(n)) == 4 for n in range(1, 17)))
say("8 apart inverts two parities of four, the third and the fourth", all(gray(n) ^ gray(n + 8) == 12 for n in range(1, 9)))
say("4 apart inverts two parities of four, the second and the third", all(gray(n) ^ gray(n + 4) == 6 for n in (1, 2, 3, 4, 9, 10, 11, 12)))
steps = [gray(n) >> 2 for n in round_of(1, [less9, less17, less9, less17])]   # the third and the fourth parity, round 1-8-9-16
say("9 less and then 17 less, in turn, invert one parity with a step, the third and then the fourth, and come to the same with four",
    [a ^ b for a, b in zip(steps, steps[1:])] == [1, 2, 1, 2] and steps[0] == steps[-1])

# 8. Inward: a name n is the inward name 8n − 7; a name to its next name is eight inward names, a span;
#    a 1 to 17 inward is two names' going, an odd name to its next odd name; eight of them with 1 to 17.
inward = lambda n: 8 * n - 7
say("8n − 7: 1 for 1, 9 for 2, 17 for 3; 57 for 8, 65 for 9, 73 for 10", [inward(n) for n in (1, 2, 3, 8, 9, 10)] == [1, 9, 17, 57, 65, 73])
say("a name to its next name is eight inward, a span, 1 to 9", all(inward(n + 1) - inward(n) == 8 for n in range(1, 17)))
say("an odd name to its next odd name is sixteen inward, a 1 to 17", all(inward(n + 2) - inward(n) == 16 for n in range(1, 16, 2)))
say("eight 1 to 17s inward are with 1 to 17: 1 to 3, 3 to 5, on to 15 to 17", len(range(1, 16, 2)) == 8)

# 8b. Four moments and a four-cycling, by 8n − 7.
say("four 1 to 17s inward are a span of this scale, 1 to 9: a self's four moments of exchanging", inward(9) - inward(1) == 4 * 16)
say("a four-cycling with its between, 1 to 5, is two 1 to 17s inward", inward(5) - inward(1) == 2 * 16)

# 8c. Parity's unit square, the four possibling names, edge by edge 2, 10, 14, 6.
root = {1: "existing", 2: "possibling", 3: "observing", 4: "same-existing", 5: "existing", 6: "possibling", 7: "observing",
        8: "same-existing", 9: "discovering", 10: "possibling", 11: "observing", 12: "same-existing", 13: "discovering",
        14: "possibling", 15: "observing", 16: "same-existing"}
co_names = {3, 4, 5, 6, 9, 10, 11, 12}
square = [2, 10, 14, 6]
say("the unit square's four dots are the four possibling names", sorted(square) == sorted(n for n in root if root[n] == "possibling"))
say("edge by edge, 2, 10, 14, 6, a name without co and a co name in turn", [n in co_names for n in square] == [False, True, False, True])
edges = [gray(square[i]) ^ gray(square[(i + 1) % 4]) for i in range(4)]
say("an edge of the unit square inverts two parities: 8 apart the third and the fourth, across the second and the third", edges == [12, 6, 12, 6])
say("no bi-folding of the four is of four possibling names", all(sum(root[n] == "possibling" for n in f) < 4 for f in four))
say("2 and 10 are of 2-15-7-10, and 6 and 14 of 3-11-6-14, 8 apart through a bi-folding's centre",
    {2, 10} <= {2, 15, 7, 10} and {6, 14} <= {3, 11, 6, 14} and 10 - 2 == 8 and 14 - 6 == 8)
sides = round_of(2, [less9, less17, less9, less17])[:4]
say("round 2-15-7-10 by its sides, a fold a step: 2, 7, 10, 15, possibling and observing in turn",
    sides == [2, 7, 10, 15] and [root[n] for n in sides] == ["possibling", "observing", "possibling", "observing"])

# 9. The set's table, if given: its columns of the three, the bi-foldings, the loops and the middle bi-foldings.
if len(sys.argv) > 1:
    rows = list(csv.reader(open(sys.argv[1], encoding="utf-8")))
    head = rows[0]
    col = lambda part: next(i for i, h in enumerate(head) if h.startswith(part))
    body = {int(r[0]): r for r in rows[1:]}
    say("the set's table: its three, 1 to 17, is the saying's three", all(body[n][col("its three")] == three[n] for n in range(1, 18)))
    bif = {1: "1-9-8-16", 2: "2-15-7-10", 3: "3-11-6-14", 4: "4-13-5-12"}
    which = lambda n: bif[min(n, 17 - n) if min(n, 17 - n) <= 4 else 9 - min(n, 17 - n)]
    say("the set's table: a name's bi-folding, 1 to 16", all(body[n][col("bi-folding [")] == which(n) for n in range(1, 17)))
    say("the set's table: a name's loop by 4 up and 9 less, 1 to 8", all(body[n][col("its loop of four names")] == ("3-7-2-6" if n in (2, 3, 6, 7) else "4-8-1-5") for n in range(1, 9)))
    say("the set's table: a middle bi-folding with 5 to 12 alone", all((body[n][col("middle bi-folding")] != "") == (5 <= n <= 12) for n in range(1, 18)))

print("\n".join(lines))
print(f"{sum(l.startswith('is    ') for l in lines)} is, {sum(l.startswith('is-not') for l in lines)} is-not")
