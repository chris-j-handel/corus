"""v410illustrating · the check of the 65th drawing: a me-parity in a seam, even, odd, even.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/check_a_me_parity_in_a_seam_even_odd_even.py .

The 65th is the eleventh figure of the reduced set, one drawing beside the five it gathers, the 49th and the 52nd to
the 55th. It goes by a partner's sayings of 27 November: the +1s living in the seams of natural torusing; the numbers
between the prime crossings; and the eight between, four odd and four even. It goes on from the marker, the commit
that lays the 64th drawing. A number is executed here ahead of its saying: the drawing's numbers are this check's own.

Do no harm: it opens v403mgr's one table, and writes in no file.
A line is an is, executed here; found, a thing found and laid whole; or a placing, the drawing's own.
"""
import csv, sys
from collections import Counter
from math import gcd
from pathlib import Path

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def join(xs): xs = [str(x) for x in xs]; return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
def seam_of(p, k): return next((e for e in (p - 1, p + 1) if e % k == 0), None)      # a me-parity's even that is a seam of k: its prior or its next
def at(p): s6 = seam_of(p, 6); return "" if s6 is None else "its +1" if p == s6 + 1 else "its −1"
def sides(seam): return [x for x in (seam - 1, seam + 1) if is_prime(x)]
def both_sides(seam): return sum(1 for n in range(0, seam, 6) if gcd(n - 1, seam) == 1 == gcd(n + 1, seam))  # a seam's cells with a me at both sides
SEAMS = [6, 30, 210, 2310, 30030]

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    table = list(csv.reader(open(root / "incoming/v403mgr/The_seventeen_names_in_one_table.csv", encoding="utf-8")))
    names = {n: table[n][1] for n in range(1, 18)}
    col = next(i for i, h in enumerate(table[0]) if h.startswith("its prime, by its position")); primes = {n: int(table[n][col]) for n in range(1, 18)}
    ps = [p for p in range(2, 10000) if is_prime(p)]

    # even, odd, even
    line("is", all((p - 1) % 2 == 0 == (p + 1) % 2 for p in ps[1:]) and all(seam_of(p, 6) is not None for p in ps[2:]) and seam_of(3, 6) is None and all(seam_of(p, 4) is not None for p in ps[1:]),
         "a me-parity past 2 is three cells, even, odd, even: its prior, its own, its next. One of its evens is a seam of 4. Past 3 one of its evens is a seam of six, at all me-parities to 10,000")
    to37 = [p for p in ps if 3 < p <= 37]; minus = [p for p in to37 if at(p) == "its −1"]; plus = [p for p in to37 if at(p) == "its +1"]
    line("is", sorted(minus + plus) == to37 and len(minus) == len(plus),
         f"a me-parity past 3 is a seam of six's +1 or its −1. To 37: {join(minus)} are a −1, and {join(plus)} a +1")
    same = [p for p in ps if 3 < p <= 59 and seam_of(p, 6) == seam_of(p, 4)]
    line("is", all(seam_of(p, 6) % 12 == 0 for p in same) and len(same) > 0,
         f"its seam of six and its seam of 4 are one even at {join(same)}, to 59: a seam of twelve")

    # a seam with a me-parity at both its sides
    six = list(range(6, 37, 6)); both = [e for e in six if len(sides(e)) == 2]; one = [e for e in six if len(sides(e)) == 1]
    line("is", len(both) + len(one) == len(six),
         f"of the six seams of six to 36, {join(both)} are with a me-parity at both sides, two about one centre; {join(one)} at one side, {join(sides(e)[0] for e in one)}")
    s360 = list(range(6, 361, 6)); c360 = Counter(len(sides(e)) for e in s360)
    line("is", sum(c360.values()) == 60,
         f"of the sixty seams of six to 360, {c360[2]} are with a me-parity at both sides, {c360[1]} at one, and {c360[0]} at none")
    pairs = [(p, p + 2) for p in ps if p > 3 and is_prime(p + 2)]
    line("is", all((p + 1) % 6 == 0 and p * q == (p + 1) ** 2 - 1 and gcd(p + 1, p * q) == 1 for p, q in pairs),
         f"two me-parities about one centre, past 3 and 5: their centre is a seam of six, crossed by neither, and the two multiplied are the centre's square less 1, at all {len(pairs)} to 10,000")
    counts = [both_sides(sm) for sm in SEAMS]; lifts = [7, 11, 13]
    line("is", counts[0] == 1 and counts[1] == 3 and all(counts[i + 2] == counts[i + 1] * (lifts[i] - 2) for i in range(3)),
         f"a seam's cells with a me at both sides are {join(counts)}, at the seams {join(SEAMS)}: a seam with a me-parity multiplied in is that many by the me-parity less 2")

    # the eight between: four odd and four even, a partner's saying
    eight = [n for n in range(15) if n % 3 and n % 5]; odd = [n for n in eight if n % 2]; even = [n for n in eight if n % 2 == 0]
    mes = [n for n in range(30) if gcd(n, 30) == 1]; on15 = sorted(n + 15 for n in even)
    line("is", sorted(15 - n for n in odd) == even and sorted(odd + on15) == mes,
         f"the eight between of a torus of 3 by 5 are four odd, {join(odd)}, and four even, {join(even)}. 15 less lays odd onto even; with 2 multiplied in they are a row's eight mes, the four even 15 on: {join(on15)}")
    mes_plus = [n for n in mes if n % 6 == 1]; mes_minus = [n for n in mes if n % 6 == 5]
    line("is", len(mes_plus) == 4 == len(mes_minus) and sorted(30 - n for n in mes_plus) == mes_minus,
         f"the row's eight mes are four at a seam of six's +1, {join(mes_plus)}, and four at its −1, {join(mes_minus)}. 30 less lays a +1 onto a −1")
    beside = {n: [e for e in (n - 1, n + 1) if e in even] for n in odd}
    line("is", sum(len(v) for v in beside.values()) == 3 and [n for n in even if all(n not in v for v in beside.values())] == [4] and (3, 5) == (4 - 1, 4 + 1),
         f"of the eight, three odd are with an even between beside them: {'; '.join(f'{n} with {v[0]}' for n, v in beside.items() if v)}. 11 is with a crossing at both sides, and 4 is the centre of the torus's own two, 3 and 5")

    # the names' primes
    rows = {n: (primes[n] - 1, primes[n], primes[n] + 1, seam_of(primes[n], 6), at(primes[n]), seam_of(primes[n], 4)) for n in range(1, 18)}
    centre = {n: primes[n] + 1 for n in range(1, 18) if is_prime(primes[n] + 2)}
    line("is", rows[1][3] is None and rows[2][3] is None and all(rows[n][3] for n in range(3, 18)),
         f"of the seventeen names' primes, a seam of six is beside neither 2 nor 3; the fifteen more are {sum(1 for n in rows if rows[n][4] == 'its −1')} at a −1 and {sum(1 for n in rows if rows[n][4] == 'its +1')} at a +1")
    line("found", True, "two me-parities about one centre with no last is a field's open asking. No line here says it, and the 54th's more at a next span is a measuring")
    line("found", True, "the 55th drawing's saying is with the 55th: a path closing, all its mes gone through, says with all numbers; and a simulation is a breaking test alone")
    line("found", True, "it goes on from the marker, the 64th drawing: a between is one thing from two sides, a partner's is. It is known mathematics, and no method of a far me-parity alone")
    line("placing", True, "the co-linear as a row of cells, a seam of six a tinted cell, a me-parity a dark cell; two rows of cells one over the other, an arc 15 less and an arrow a multiplying in, are the drawing's own placings")
    own = {"names": names, "primes": primes, "rows": rows, "centre": centre, "minus": minus, "plus": plus, "both": both, "one": one, "c360": c360, "pairs": pairs, "counts": counts,
           "odd": odd, "even": even, "mes": mes, "mes_plus": mes_plus, "mes_minus": mes_minus, "same": same, "npairs": len(pairs)}
    return lines, own

if __name__ == "__main__":
    lines, own = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['placing']} is a placing" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
