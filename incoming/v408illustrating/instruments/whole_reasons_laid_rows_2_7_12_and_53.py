"""v408illustrating · whole reasons laid, for rows 2, 7, 12 and 53 of v408primes' table: a going on of no number, its sentences gone through.

Usage, from the repository's root (some seconds):
  python3 -I incoming/v408illustrating/instruments/whole_reasons_laid_rows_2_7_12_and_53.py .

A row's going on is a co-chain of sentences of no number. The page beside this instrument lays four, a sentence a +1 from
its prior. Here a sentence is gone through whole at small paths, the me-parities 3 to 97: that is a going through of the
sentence's own saying at those paths, and the reason at all me-parities is the co-chain's.
  is       a sentence gone through whole at the paths named.
  tested   a breaking test, to its stated limit: none found, among no is.
Round p is a path of p mes closing; a living me is a me past 0; across is multiplying. Whole numbers alone. It writes none.
"""
import sys
from math import gcd

MES = [p for p in range(3, 100) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
def parts(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out + ([n] if n > 1 else [])
def a_loop(a, p):
    """A living me's stepping, a, a by a, and on, to the me 1 again: its selves."""
    out, x = [a % p], a % p
    while x != 1: x = x * a % p; out.append(x)
    return out
def the_row_of(s, p): return sum(s ** k for k in range(p))          # 1, s, s by s, and on, p of them, added

if __name__ == "__main__":
    results, tests = [], []
    def line(name, ok): results.append((name, bool(ok)))
    def test(name, ok): tests.append((name, bool(ok)))
    # row 2's own sentence, under the others: a me-parity crossing two numbers multiplied crosses one of them
    line("row 2, its sentence under the others, by descent: with p crossing a by b and not a, and b the least such, p less b by a number is a lesser one or 0, and 0 says b is a part of p, 1; so no least is, and none is. Gone through whole: round the me-parities 3 to 97, two living mes multiplied are a living me, at all pairs",
         all((a * b) % p != 0 for p in MES for a in range(1, p) for b in range(1, p)))
    line("row 12, multiplying by a living me is one for one over the living mes: round the me-parities 3 to 97, a living me by all the living mes is all the living mes, at all living mes",
         all(sorted(a * x % p for x in range(1, p)) == list(range(1, p)) for p in MES for a in range(1, p)))
    def rows(a, p):
        loop = a_loop(a, p); seen, out = set(), []
        for x in range(1, p):
            if x not in seen:
                row = sorted(x * y % p for y in loop); out.append(row); seen.update(row)
        return loop, out
    line("row 12, a loop's rows: a living me by a loop's selves is a row of as many living mes, two rows are one row or with no me of both, and the living mes are whole rows: a loop's selves are a part of p less 1. Gone through whole round the me-parities 3 to 97, all loops",
         all(all(len(r) == len(loop) for r in rs) and sum(len(r) for r in rs) == p - 1 and (p - 1) % len(loop) == 0 for p in MES for a in range(1, p) for loop, rs in [rows(a, p)]))
    def across_other(x, p): return next(y for y in range(1, p) if x * y % p == 1)
    line("row 7, the pairing: a living me is with one across-other, the two multiplied at the me 1; it is its own at the me 1 and at the me one back alone; the others are all in pairs, and all the living mes multiplied are at the me one back. Gone through whole round the me-parities 3 to 97",
         all([x for x in range(1, p) if across_other(x, p) == x] == [1, p - 1] and all(across_other(across_other(x, p), p) == x for x in range(1, p)) for p in MES)
         and all(eval("*".join(str(x) for x in range(1, p))) % p == p - 1 for p in MES))
    line("row 7, its is-not side: round a crossed number past 4, all the numbers short of it multiplied are at the me 0, its two parts among them, or a part and its double. Gone through at all crossed numbers of 6 to 400",
         all(eval("*".join(str(x) for x in range(1, n))) % n == 0 for n in range(6, 401) if len(parts(n)) > 1) and (1 * 2 * 3) % 4 == 2)
    line("row 53, the row of p, its own sentences: with s a seam of p, the row 1, s, s by s and on, p of them, added, is at the me 1 round p and round all parts of s; and s less 1 by the row is s stepped p times, less 1. Gone through at p of 3, 5 and 7 and s of p, twice p and 6 by p",
         all(the_row_of(s, p) % p == 1 and all(the_row_of(s, p) % q == 1 for q in set(parts(s))) and (s - 1) * the_row_of(s, p) == s ** p - 1 for p in (3, 5, 7) for s in (p, 2 * p, 6 * p)))
    def whole(p, s):
        n = the_row_of(s, p)
        return all(len(a_loop(s % q, q)) == p and (q - 1) % p == 0 and gcd(q, s) == 1 for q in set(parts(n)))
    seams = [(p, s) for p in (3, 5, 7) for s in (p, 2 * p, 3 * p, 6 * p) if the_row_of(s, p) < 10 ** 11]
    line(f"row 53, drawn at its numbers: round a me-parity part q of the row, s's loop is p selves, p is a part of q less 1, and q crosses no part of s: at p of 3 and s of 3, the row is 13, at the me 1 round 3; gone through at {len(seams)} rows",
         the_row_of(3, 3) == 13 and len(a_loop(3, 13)) == 3 and all(whole(p, s) for p, s in seams))
    test("row 12 beside it, a living me stepped p less 1 times is at the me 1: round the me-parities 3 to 97, all living mes. No breaking found", all(pow(a, p - 1, p) == 1 for p in MES for a in range(1, p)))
    print("said apart: a sentence gone through at the me-parities 3 to 97 is gone through at them; its reason at all me-parities is the co-chain in the page beside this instrument\n")
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    for name, ok in tests: print(("tested   " if ok else "broken   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is; {sum(ok for _, ok in tests)} of {len(tests)} breaking tests found none")
    sys.exit(0 if all(ok for _, ok in results + tests) else 1)
