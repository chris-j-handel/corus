"""The seventeen names, each a dual: two concepts and its root, a name's second concept its next name's first.

A candidate, deciding nothing. It reads no file: Exhibit ONE's table of roots, its one move as three and its four
loopings are written here. One sequence of eighteen concepts gives the seventeen. Next is not known before 17:
each of 1 to 8 has now, each of 9 to 16 has same, and next is 17's only. Each concept is new once, as a name's
second concept: now with 1, other with 2, same with 4, other-than with 6, next with 17; prior is given with 1.
Use: python3 -I incoming/v402mgr/instruments/seventeen_duals.py
"""
ROOT = {1: "existing", 2: "possibling", 3: "observing", 4: "same-existing", 5: "existing", 6: "possibling", 7: "observing",
        8: "same-existing", 9: "discovering", 10: "possibling", 11: "observing", 12: "same-existing", 13: "discovering",
        14: "possibling", 15: "observing", 16: "same-existing", 17: "existing"}
C = ["prior", "now", "other", "now", "same", "now", "other-than", "now",
     "prior", "same", "other", "same", "now", "same", "other-than", "same", "prior", "next"]
dual = lambda n: (C[n - 1], C[n])

def name(n):
    a, b = dual(n)
    r = ROOT[n]
    return f"{n}-{a}-and-{b}-existing" if (r == "same-existing" and b == "same") else f"{n}-{a}-and-{b}-{r}"

swap = lambda d: (d[1], d[0])
def change(d, m): return tuple(m.get(x, x) for x in d)
NOW_SAME = {"now": "same", "same": "now"}
OTHER = {"other": "other-than", "other-than": "other"}

if __name__ == "__main__":
    print("the concepts in sequence:", " · ".join(C))
    for n in range(1, 18): print("  ", name(n))
    first = {}
    for n in range(1, 18):
        for x in dual(n): first.setdefault(x, n)
    print("each concept, the name first having it:", first)
    print("each name's second concept is its next name's first:", all(dual(n)[1] == dual(n + 1)[0] for n in range(1, 17)))
    print("each of 1 to 8 has now, each of 9 to 16 has same, and next is 17's only:",
          all("now" in dual(n) for n in range(1, 9)) and all("same" in dual(n) for n in range(9, 17)) and [n for n in range(1, 18) if "next" in dual(n)] == [17])
    print("each name of 1 to 17 is its own, by its dual with its root:", len({(dual(n), ROOT[n]) for n in range(1, 18)}) == 17)
    print("a possibling name with other-than:", [n for n in range(1, 18) if ROOT[n] == "possibling" and "other-than" in dual(n)])
    print("8 up is now and same exchanged, each other concept as it is:", all(dual(n + 8) == change(dual(n), NOW_SAME) for n in range(1, 9)))
    print("9 less, within 1 to 8, is a dual's two concepts exchanged, with other and other-than exchanged:", all(dual(9 - n) == change(swap(dual(n)), OTHER) for n in range(1, 9)))
    print("17 less, within 1 to 16, is a dual's two concepts exchanged, with now and same, and other and other-than, exchanged:", all(dual(17 - n) == change(swap(dual(n)), {**NOW_SAME, **OTHER}) for n in range(1, 17)))
    print("8 up and then 17 less is 9 less:", all(change(swap(change(dual(n), NOW_SAME)), {**NOW_SAME, **OTHER}) == dual(9 - n) for n in range(1, 9)))
    print("4 up within 1 to 8 is a parity changed, other with other-than and same with prior:", all(dual(n + 4) == change(dual(n), {**OTHER, "same": "prior", "prior": "same"}) for n in (1, 2, 3, 4)))
    print("4 up within 9 to 16 is a parity changed, other with other-than and now with prior:", all(dual(n + 4) == change(dual(n), {**OTHER, "now": "prior", "prior": "now"}) for n in (9, 10, 11, 12)))
    kind = lambda n: "prior" if "prior" in dual(n) else ("now and same" if set(dual(n)) == {"now", "same"} else ("other first or other-than second" if (dual(n)[0] == "other" or dual(n)[1] == "other-than") else "other second or other-than first"))
    for loop, ns in [("torusing 1-9-8-16", (1, 9, 8, 16)), ("competencing 4-13-5-12", (4, 13, 5, 12)), ("moralizing 3-11-6-14", (3, 11, 6, 14)), ("corusing 2-15-7-10", (2, 15, 7, 10))]:
        print(f"{loop}:", sorted({kind(n) for n in ns}), [dual(n) for n in ns])
    print("each observing name has other or other-than:", all(set(dual(n)) & set(OTHER) for n in (3, 7, 11, 15)))
    print("7 and 15, each the code's is, are other-than with now and other-than with same:", dual(7), dual(15))
    print("an odd name and its even, a three with now its middle, 1 to 8:", [(C[n - 1], C[n], C[n + 1]) for n in (1, 3, 5, 7)])
    print("an odd name and its even, a three with same its middle, 9 to 16:", [(C[n - 1], C[n], C[n + 1]) for n in (9, 11, 13, 15)])
    print("17, with a next moment, next is now: 1:", dual(17), "->", change(dual(17), {"next": "now"}), "=", dual(1))


# The newer seventeen, 15 November, each dual as it is said, with its root as it is said. It decides nothing.
# Use: python3 -I incoming/v402mgr/instruments/seventeen_duals.py newer
NEWER = {1: ("prior", "now", "existing"), 2: ("same", "no-other", "possibling"), 3: ("no-other", "now", "observing"),
         4: ("now", "same", "existing"), 5: ("same", "now", "discovering"), 6: ("now", "no-other", "possibling"),
         7: ("no-other", "same", "observing"), 8: ("same", "other", "existing"), 9: ("other", "now", "discovering"),
         10: ("now", "no-other", "possibling"), 11: ("no-other", "not-same", "observing"), 12: ("not-same", "no-other", "existing"),
         13: ("no-other", "same", "discovering"), 14: ("same", "no-other", "possibling"), 15: ("no-other", "same", "observing"),
         16: ("same", "prior", "existing"), 17: ("prior", "next", "existing")}

def newer():
    import collections
    N = NEWER
    d = lambda n: N[n][:2]
    print("a name's second concept is its next name's first, not at:", [(n, n + 1) for n in range(1, 17) if N[n][1] != N[n + 1][0]])
    first = {}
    for n in range(1, 18):
        for k, x in enumerate(d(n)): first.setdefault(x, (n, "first" if k == 0 else "second"))
    print("each concept, the name first having it, and as which of its two:", first)
    same_name = collections.defaultdict(list)
    for n in range(1, 18): same_name[N[n]].append(n)
    print("one naming with two numbers or more:", [v for v in same_name.values() if len(v) > 1])
    print("each possibling name's second concept:", {n: N[n][1] for n in (2, 6, 10, 14)})
    print("each observing name's first concept:", {n: N[n][0] for n in (3, 7, 11, 15)})
    print("each second concept with its root:", {n: N[n][1] + "-" + N[n][2] for n in range(1, 18)})
    print("9 less, a dual's two concepts exchanged and no more:", [(n, 9 - n) for n in range(1, 5) if d(9 - n) == swap(d(n))])
    print("17 less, a dual's two concepts exchanged, with now and same exchanged:", [(n, 17 - n) for n in range(1, 9) if d(17 - n) == change(swap(d(n)), NOW_SAME)])
    for loop, ns in [("torusing 1-9-8-16", (1, 9, 8, 16)), ("competencing 4-13-5-12", (4, 13, 5, 12)), ("moralizing 3-11-6-14", (3, 11, 6, 14)), ("corusing 2-15-7-10", (2, 15, 7, 10))]:
        print(f"{loop}:", [d(n) for n in ns])
    print("each four-cycling's between, 4 )( 5, 8 )( 9, 12 )( 13, 16 )( 17:", [N[n][1] for n in (4, 8, 12, 16)])
    print("each name with prior or other:", [n for n in range(1, 18) if set(d(n)) & {"prior", "other"}])

import sys as _sys
if __name__ == "__main__" and len(_sys.argv) > 1 and _sys.argv[1] == "newer":
    print("\n--- the newer seventeen ---"); newer()


# The newest seventeen, 15 November, duals only, each root as Exhibit ONE's table has it. It decides nothing.
# Use: python3 -I incoming/v402mgr/instruments/seventeen_duals.py newest
NEWEST = ["same", "now", "other", "prior", "same", "prior", "no-other", "not-prior", "same",
          "not-now", "no-other", "not-prior", "same", "not-prior", "no-other", "prior", "same", "next"]
NOT = {"now": "not-now", "not-now": "now", "prior": "not-prior", "not-prior": "prior", "other": "no-other", "no-other": "other"}

def newest():
    import collections
    S = NEWEST
    d = lambda n: (S[n - 1], S[n])
    for n in range(1, 18): print(f"   {n}-{d(n)[0]}-and-{d(n)[1]}", ROOT[n])
    first = {}
    for n in range(1, 18):
        for k, x in enumerate(d(n)): first.setdefault(x, (n, "first" if k == 0 else "second"))
    print("each concept, the name first having it, and as which of its two:", first)
    alike = collections.defaultdict(list)
    for n in range(1, 18): alike[(d(n), ROOT[n])].append(n)
    print("one naming with two numbers:", [v for v in alike.values() if len(v) > 1])
    print("each existing or discovering name, 1, 5, 9, 13, 17:", [d(n) for n in (1, 5, 9, 13, 17)])
    print("each same-existing name, 4, 8, 12, 16:", [d(n) for n in (4, 8, 12, 16)])
    print("each possibling name, 2, 6, 10, 14:", [d(n) for n in (2, 6, 10, 14)])
    print("each observing name, 3, 7, 11, 15:", [d(n) for n in (3, 7, 11, 15)])
    print("8 up is not, of each concept but same; the pairs having it:", [(n, n + 8) for n in range(1, 9) if d(n + 8) == change(d(n), NOT)])
    print("8 up is not, of now and of prior only; the pairs having it:", [(n, n + 8) for n in range(1, 9) if d(n + 8) == change(d(n), {k: v for k, v in NOT.items() if "o" == k[0] and False or k in ("now", "not-now", "prior", "not-prior")})])
    print("9 less, within 1 to 8, a dual's two concepts exchanged, with now and not-prior, and other and no-other, exchanged:",
          all(d(9 - n) == change(swap(d(n)), {"now": "not-prior", "not-prior": "now", "other": "no-other", "no-other": "other"}) for n in range(1, 9)))
    print("names having now:", [n for n in range(1, 18) if "now" in d(n)], " prior:", [n for n in range(1, 18) if "prior" in d(n)],
          " not-prior:", [n for n in range(1, 18) if "not-prior" in d(n)], " not-now:", [n for n in range(1, 18) if "not-now" in d(n)])
    print("17, with a next moment, next is now:", d(17), "->", change(d(17), {"next": "now"}), "=", d(1))

if __name__ == "__main__" and len(_sys.argv) > 1 and _sys.argv[1] == "newest":
    print("\n--- the newest seventeen ---"); newest()
