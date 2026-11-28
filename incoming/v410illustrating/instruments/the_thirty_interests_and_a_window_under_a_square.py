"""v410illustrating · a partner's asking of 27 November, saying 25: the interests in the prime numberings not resolving.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_thirty_interests_and_a_window_under_a_square.py .

It opens v408primes' table of the interests in the primes, and writes in no file. It says what the table's own words
say of the thirty, and executes one thing this session's drawings show: at a seam, a cell between the crossings is
said a me-parity by the torus alone under the square of the seam's next me-parity, a window; and the seam's round
outgrows the window. Its numbers are made by the execution. It resolves no interest.
"""
import csv, sys
from collections import Counter
from math import gcd, prod
from pathlib import Path

def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
def join(xs): xs = [str(x) for x in xs]; return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
KINDS = {"cells of a seam, lifted": [25, 26, 27, 28, 29, 31, 32, 33, 36, 37, 38, 39, 40, 53],
         "a rate, a value or a spread, said smooth": [41, 42, 45, 46, 47, 48, 49, 50, 61],
         "a doubling round a me-parity": [13, 14, 15, 16, 17],
         "curves round a me-parity": [51, 54]}                              # this session's judging of the thirty, said as judged

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    rows = list(csv.DictReader(open(root / "incoming/v408primes/The_interests_in_the_primes.csv", encoding="utf-8"))); k = list(rows[0].keys())
    more = [r for r in rows if r["Standing"].startswith("more")]; resolved = [r for r in rows if r["Standing"] == "resolved"]
    all_on = [r["Row"] for r in more if "going on" in r[k[7]]]
    known = [r["Row"] for r in more if "known, to be laid" in r[k[7]]]; none = [r["Row"] for r in more if "not laid in this session" in r[k[7]]]
    rest = [r["Row"] for r in more if r["Row"] not in known + none]
    line("is", len(rows) == len(more) + len(resolved) and len(all_on) == len(more),
         f"v408primes' table is {len(rows)} interests: {len(resolved)} resolved, and {len(more)} with more competency possible. Of all {len(more)} its own words say one thing: its going on to all universes is not yet laid, and it is proved in its named universe")
    line("is", len(known) + len(none) + len(rest) == len(more),
         f"of the {len(more)}, {len(known)} are with a whole reason known, to be laid; {len(none)} with a whole reason not laid; and {len(rest)}, row {join(rest)}, with its journey gathering it")
    seats = Counter(r[k[3]].split(",")[0] for r in more)
    line("is", sum(seats.values()) == len(more), "by their seat among the ten: " + "; ".join(f"{v} {s_.lower()}" for s_, v in seats.most_common()))
    judged = sorted(n for v in KINDS.values() for n in v)
    line("judged", judged == sorted(int(r["Row"]) for r in more), "this session's judging of the thirty, four kinds: " + "; ".join(f"{len(v)} {s_}, rows {join(v)}" for s_, v in KINDS.items()))

    # a window under a square
    ps = [p for p in range(2, 60) if is_prime(p)]; table = []
    for i in range(2, 7):
        seam = prod(ps[:i]); q = ps[i]; window = q * q
        cells = [n for n in range(2, seam) if gcd(n, seam) == 1]
        inside = [n for n in cells if n < window]; past = [n for n in cells if n >= window]
        table.append((seam, q, window, len(cells), all(map(is_prime, inside)), len(past), sum(1 for n in past if not is_prime(n)) if seam <= 30030 else None))
    line("is", all(t[4] for t in table),
         "at a seam, a cell between the crossings and under the square of the seam's next me-parity is a me-parity: the window. " + "; ".join(f"at {t[0]}, under {t[2]}" for t in table))
    line("is", table[0][2] > table[0][0] and table[1][2] > table[1][0] and all(t[2] < t[0] for t in table[2:]),
         f"at {table[0][0]} and {table[1][0]} the window is past the seam's round. From {table[2][0]} on the round outgrows it: in 100 of the round the window is " + join(max(1, round(100 * t[2] / t[0])) if 100 * t[2] / t[0] >= 0.5 else "under 1" for t in table[2:]))
    line("is", all(t[6] is None or t[6] > 0 for t in table[2:]),
         "past the window a cell between the crossings is a me-parity, or crossed by a me-parity past the seam's own, and the seam's torus says none of which: crossed are " + join(f"{t[6]} of {t[5]} at {t[0]}" for t in table[2:] if t[6] is not None))
    two = []
    for seam in (30, 210, 2310, 30030):
        c2 = [n for n in range(6, seam + 1, 6) if gcd(n - 1, seam) == 1 == gcd(n + 1, seam)]
        two.append((seam, len(c2), sum(1 for n in c2 if is_prime(n - 1) and is_prime(n + 1))))
    line("is", two[0][1] == two[0][2] and all(t[2] < t[1] for t in two[1:]),
         "a seam's cells with a me at both sides are whole at all seams, and not none; the me-parities among them are by the later crossings: " + join(f"{t[2]} of {t[1]} at {t[0]}" for t in two))
    one = next(r for r in resolved if r["Row"] == "1")
    line("found", "from all seams" in one[k[6]], "the table's row 1, resolved, is said seam to its next: from all seams, the uncrossed cell past 1 closest to it is a next prime. It is under the window at all seams")
    line("found", True, "row 61, the field's parity problem of sieves, is the window said by the field: crossings do not say a me-parity past it")
    line("found", True, "it resolves no interest. A simulation is a breaking test alone, a partner's saying of 26 November: a traveling on says no is of all universes")
    return lines, {}

if __name__ == "__main__":
    lines, _ = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['judged']} is judged, and said as judged" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
