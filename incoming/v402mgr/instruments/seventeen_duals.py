"""The seventeen names, each a dual: two concepts and its root, a name's second concept its next name's first.

A candidate, deciding nothing. It reads no file: Exhibit ONE's table of roots and its one move as three are written here.
One sequence of eighteen concepts gives the seventeen: a moment, now or next, in each second place, and between
the moments four going round, prior, other, same, other-than, and prior again.
Use: python3 -I incoming/v402mgr/instruments/seventeen_duals.py
"""
ROOT = {1: "existing", 2: "possibling", 3: "observing", 4: "same-existing", 5: "existing", 6: "possibling", 7: "observing",
        8: "same-existing", 9: "discovering", 10: "possibling", 11: "observing", 12: "same-existing", 13: "discovering",
        14: "possibling", 15: "observing", 16: "same-existing", 17: "existing"}
FOUR = ["prior", "other", "same", "other-than"]
C = [FOUR[(i // 2) % 4] if i % 2 == 0 else ("now" if i < 8 else "next") for i in range(18)]
dual = lambda n: (C[n - 1], C[n])

def name(n):
    a, b = dual(n)
    r = ROOT[n]
    return f"{n}-{a}-and-{b}-existing" if (r == "same-existing" and b == "same") else f"{n}-{a}-and-{b}-{r}"

swap = lambda d: (d[1], d[0])
def change(d, m): return tuple(m.get(x, x) for x in d)
NOW_NEXT = {"now": "next", "next": "now"}
PARITY_O = {"other": "other-than", "other-than": "other"}
PARITY_S = {"same": "prior", "prior": "same"}

if __name__ == "__main__":
    print("the concepts in sequence:", " · ".join(C))
    for n in range(1, 18): print("  ", name(n))
    print("each name's second concept is its next name's first:", all(dual(n)[1] == dual(n + 1)[0] for n in range(1, 17)))
    print("each of 1 to 8 has now, and each of 9 to 17 has next:", all("now" in dual(n) for n in range(1, 9)) and all("next" in dual(n) for n in range(9, 18)))
    print("each odd name has its moment last, each even name first:", all((dual(n)[1] in NOW_NEXT) == (n % 2 == 1) and (dual(n)[0] in NOW_NEXT) == (n % 2 == 0) for n in range(1, 18)))
    print("each dual of 1 to 16 is its own, no two alike:", len({dual(n) for n in range(1, 17)}) == 16)
    print("8 up is now to next, each other concept as it is:", all(dual(n + 8) == change(dual(n), {"now": "next"}) for n in range(1, 9)))
    print("9 less, within 1 to 8, is a dual's two concepts exchanged, with other and other-than exchanged:", all(dual(9 - n) == change(swap(dual(n)), PARITY_O) for n in range(1, 9)))
    print("17 less, within 1 to 16, is a dual's two concepts exchanged, with now and next, and other and other-than, exchanged:", all(dual(17 - n) == change(swap(dual(n)), {**NOW_NEXT, **PARITY_O}) for n in range(1, 17)))
    print("8 up and then 17 less is 9 less:", all(change(swap(change(dual(n), {"now": "next"})), {**NOW_NEXT, **PARITY_O}) == dual(9 - n) for n in range(1, 9)))
    print("4 up, within 1 to 8 and within 9 to 16, is a parity changed, other with other-than and same with prior:", all(dual(n + 4) == change(dual(n), {**PARITY_O, **PARITY_S}) for n in (1, 2, 3, 4, 9, 10, 11, 12)))
    print("the loop 3-7-2-6 is each name of other or other-than:", sorted(n for n in range(1, 9) if set(dual(n)) & set(PARITY_O)) == [2, 3, 6, 7])
    print("the loop 4-8-1-5 is each name of same or prior:", sorted(n for n in range(1, 9) if set(dual(n)) & set(PARITY_S)) == [1, 4, 5, 8])
    print("each observing name has other or other-than:", all(set(dual(n)) & set(PARITY_O) for n in (3, 7, 11, 15)))
    print("7 and 15, each with tri first and each the code's is, are other-than with its moment:", dual(7) == ("other-than", "now") and dual(15) == ("other-than", "next"))
    print("each four-cycling's between, 4 )( 5, 8 )( 9, 12 )( 13, 16 )( 17, is same or prior:", [C[n] for n in (4, 8, 12, 16)])
    print("two names in sequence, an odd and its even, are a three with the moment its middle:", [(C[n - 1], C[n], C[n + 1]) for n in (1, 3, 5, 7)])
    print("17 is 9's dual with the root existing; with a next moment, next is now, and it is 1:", dual(17), "->", change(dual(17), {"next": "now"}), "=", dual(1))
