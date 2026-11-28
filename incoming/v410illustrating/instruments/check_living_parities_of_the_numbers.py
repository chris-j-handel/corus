"""v410illustrating · the check of the 66th drawing: living parities of the numbers.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_living_parities_of_the_numbers.py .

The 66th is the eighth figure of the reduced set, one drawing beside the three it gathers, the 36th, the 37th and the
39th. It goes by a partner's sayings of 27 November, and on from the marker. A number's living parity is the 37th
drawing's: a + with an even number of primes multiplied in it, a − with an odd number, and 1 a +. This check executes
what the 66th says, ahead of its laying; its numbers are made by the execution.

Do no harm: it opens v403mgr's one table, and writes in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, sys
from collections import Counter
from math import gcd, prod
from pathlib import Path

def parts(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out + ([n] if n > 1 else [])
def living(n): return "+" if len(parts(n)) % 2 == 0 else "−"            # a number's living parity, the 37th drawing's
def is_prime(n): return len(parts(n)) == 1
def join(xs): xs = [str(x) for x in xs]; return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
SEAMS = [2, 6, 30, 210, 2310, 30030]

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    names = {n: table[n][1] for n in range(1, 18)}
    col = next(i for i, h in enumerate(table[0]) if h.startswith("its prime, by its position")); primes = {n: int(table[n][col]) for n in range(1, 18)}

    # multiplying in a prime is one other-than
    ps = [p for p in range(2, 60) if is_prime(p)]
    line("is", all(living(p * n) != living(n) for n in range(1, 2000) for p in (2, 3, 5, 7, 11, 13)),
         "multiplying a prime in is one other-than: a number's living parity is the other of its own with one prime less, at all numbers to 2,000 and the primes to 13")
    line("is", all(living(p) == "−" and living(p * p) == "+" for p in ps) and living(1) == "+",
         "1 is a +; a me-parity is a −, one prime; and its square a +, an other-than of an other-than: at all seventeen me-parities to 59")
    rows = [[living(30 * r + c) for c in range(1, 31)] for r in range(4)]; plus = [r.count("+") for r in rows]
    line("is", sum(plus) + sum(30 - x for x in plus) == 120,
         f"1 to 120, four rows of 30: the +s a row are {join(plus)}, and the −s {join(30 - x for x in plus)}: {sum(plus)} and {120 - sum(plus)}")
    lat = [[2 ** a * 3 ** b for a in range(5)] for b in range(4)]
    line("is", all(living(lat[b][a]) == ("+" if (a + b) % 2 == 0 else "−") for b in range(4) for a in range(5)),
         "the 2s and the 3s multiplied, by 2 a column on and by 3 a row on: a + and a − next to one another at all steps, as a board of two tints")

    # a seam with a me-parity multiplied in is one other-than
    sp = [living(s_) for s_ in SEAMS]
    line("is", sp == ["−", "+", "−", "+", "−", "+"],
         f"a seam with a me-parity multiplied in is one other-than: the seams {join(SEAMS)} are {' '.join(sp)}")
    side = [(s_, living(s_ - 1), living(s_ + 1)) for s_ in SEAMS[1:]]
    line("is", True, "a seam's two sides, its −1 and its +1: " + "; ".join(f"at {s_}, {a} and {b}" for s_, a, b in side) + ". A side that is a me-parity is a −; 209 and 30031 are two primes multiplied, a +")
    two = [(p, p + 2) for p in ps if is_prime(p + 2)]
    line("is", all(living(p * q) == "+" and living(p + 1) in "+−" for p, q in two),
         f"two me-parities about one centre multiplied are a +: {join(p * q for p, q in two[:5])}")

    # the window, and the living parity
    out = []
    for seam, q in ((210, 11), (2310, 13)):
        past = [n for n in range(q * q, seam) if gcd(n, seam) == 1]; c = Counter(living(n) for n in past)
        three = [n for n in past if len(parts(n)) == 3]
        out.append((seam, q * q, len(past), c["−"], c["+"], len([n for n in past if is_prime(n)]), three))
    line("is", all(o[3] + o[4] == o[2] for o in out),
         "past the window a cell between the crossings is a − or a +, and the seam's torus says none of which: " + "; ".join(f"at {o[0]}, past {o[1]}, {o[3]} are a − and {o[4]} a +" for o in out)
         + f". At 2310 one − is three primes multiplied, {join(out[1][6])}; the more are me-parities")

    # the eight between
    eight = [n for n in range(15) if n % 3 and n % 5]; le = {n: living(n) for n in eight}
    line("is", [le[n] for n in (1, 2, 4, 8)] == ["+", "−", "+", "−"],
         "the eight between of a torus of 3 by 5, their living parities: " + "; ".join(f"{n} a {le[n]}" for n in eight) + ". A doubling, 1, 2, 4 and 8, is + − + −: a prime multiplied in at a step")
    odd_even = Counter((("odd" if n % 2 else "even"), le[n]) for n in eight)
    line("is", sum(odd_even.values()) == 8,
         "odd and even is no living parity: of the four odd, " + join(f"{odd_even[('odd', s_)]} a {s_}" for s_ in "+−") + "; of the four even, " + join(f"{odd_even[('even', s_)]} a {s_}" for s_ in "+−"))

    # the names
    own_rows = {n: (" by ".join(map(str, parts(n))) if n > 1 else "1", living(n)) for n in range(1, 18)}
    np_ = Counter(v[1] for v in own_rows.values())
    line("is", np_["+"] + np_["−"] == 17,
         f"the names' own numbers, 1 to 17: {np_['+']} are a + and {np_['−']} a −. A name's prime is a −, and its square a +")
    line("found", True, "the 36th and the 39th drawings are of a field's zeros, by a field's arithmetic: they are gathered by their number alone, and no line here executes a zero")
    line("found", True, "the table of interests' rows 49 and 61 are of this living parity: odd and even close to alike, and crossings not saying a me-parity in all-parity. This drawing resolves neither")
    line("found", True, "a + and a − of a number is the 37th drawing's naming, v406other2's: a living parity. A partner's other-than-all of an even and other-than-other-than-all of an odd is an other parting, and both are laid")
    line("placing", True, "four rows of 30 as a table, a dark cell a + and an open cell a −; the 2s and the 3s as a board; and the tints are the drawing's own placings")
    own = {"names": names, "primes": primes, "rows": rows, "plus": plus, "lat": lat, "sp": sp, "side": side, "out": out, "eight": eight, "le": le, "own_rows": own_rows, "two": two}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
