"""v410illustrating · a partner's saying of 27 November, executed: the eight between, four odd and four even.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_eight_between_four_odd_and_four_even.py .

A partner said, of the eight cells between the crossings of a torus of 3 by 5: odd are 1, 7, 11 and 13; even are
2, 4, 8 and 14; four even other-than-alls and four odd other-than-other-than-alls; the eight all or none at alls.
This instrument executes numbers alone, and goes on from the marker, the commit that lays the 64th drawing.
A number is executed here ahead of its saying: a line's numbers are made by the execution, and none is typed.

Do no harm: it opens Natural Naming and Exhibit THIRTY for their sayings, and writes in no file.
A line is an is, executed here; or found, a thing found and laid whole.
"""
import sys
from collections import Counter
from math import gcd
from pathlib import Path

def join(xs): xs = [str(x) for x in xs]; return ", ".join(xs[:-1]) + " and " + xs[-1]
def digits(n): return format(n, "04b")
def is_prime(n): return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))

def checks(root):
    root = Path(root).resolve(); lines = []
    def line(kind, ok, words_): lines.append((kind if ok else "is-not", words_))
    naming = sorted(root.glob("Exhibit_TWENTY_Natural_Naming_*.md"))[0].read_text(encoding="utf-8")
    thirty = sorted(root.glob("Exhibit_THIRTY_*.md"))[0].read_text(encoding="utf-8")
    line("is", "all or none at all" in naming and "morality across" in thirty and "competency along" in thirty,
         "Natural Naming says one fractal method all or none at all with its scales; Exhibit THIRTY says morality across, right and not-right, and competency along")

    eight = [n for n in range(15) if n % 3 and n % 5]; odd = [n for n in eight if n % 2]; even = [n for n in eight if n % 2 == 0]
    line("is", len(eight) == 8 and len(odd) == 4 == len(even),
         f"the eight between the crossings of a torus of 3 by 5 are {join(eight)}: four odd, {join(odd)}, and four even, {join(even)}, as a partner says")

    # a step of 15 lays odd onto even
    pairs = [(n, 15 - n) for n in odd]
    line("is", sorted(15 - n for n in odd) == even and all((15 - n) % 2 != n % 2 for n in eight),
         f"15 less a between is a between, and odd for even: {'; '.join(f'{a} with {b}' for a, b in pairs)}. The four even are the four odd, 15 less")
    twice = [30 - n for n in odd]; on = [n + 15 for n in even]
    line("is", sorted(twice) == sorted(on) and all(n % 2 for n in twice),
         f"15 less and then 15 on is 30 less: the four odd onto {join(sorted(twice))}, odd again. One step of 15 lays odd onto even and even onto odd, and two are as it was")

    # lifted by 2: a row's eight mes
    mes = [n for n in range(30) if gcd(n, 30) == 1]
    lifted = sorted(n if n % 2 else n + 15 for n in eight)
    line("is", lifted == mes and odd == mes[:4] and sorted(on) == mes[4:],
         f"lifted by 2, the eight are a row's eight mes of 30, one for one: the four odd as they are, {join(odd)}, and the four even 15 on, {join(sorted(on))}")
    line("is", [n for n in mes if not is_prime(n)] == [1],
         f"of the row's eight, {join([n for n in mes if is_prime(n)])} are me-parities, and 1 is said alone")

    # four binary digits: all, and none at all
    one_on = [n for n in range(15) if digits(n).count("1") == 1]; one_off = [n for n in range(15) if digits(n).count("1") == 3]; two = [n for n in range(15) if digits(n).count("1") == 2]
    line("is", sorted(one_on + one_off) == eight and two == [n for n in range(1, 15) if n not in eight] and digits(15) == "1111" and digits(0) == "0000" and 15 % 3 == 0 == 15 % 5,
         f"in four binary digits 0 is none on and 15 all four on, one cell of the torus, its opening. The eight are one digit on, {join(one_on)}, or one digit not on, {join(one_off)}. The six more on a crossing, {join(two)}, are two on")
    line("is", all(digits(15 - n) == "".join("1" if d == "0" else "0" for d in digits(n)) for n in range(16)),
         "15 less a number is its four digits, on for not on, all four")

    # two across by four along
    rows = {r: [n for n in eight if n % 3 == r] for r in (1, 2)}
    line("is", all(sorted(n % 5 for n in rows[r]) == [1, 2, 3, 4] for r in rows),
         f"on the torus the eight are two across by four along: its own of 3 at 1, {join(rows[1])}, and at 2, {join(rows[2])}; its own of 5 at 1 to 4 in both")

    # three partings of the eight, not one
    partings = {"odd, a partner's": set(odd), "one digit on": set(one_on), "its own of 3 at 1": set(rows[1])}
    keys = list(partings); cross = {(a, b): len(partings[a] & partings[b]) for i, a in enumerate(keys) for b in keys[i + 1:]}
    line("is", all(len(v) == 4 for v in partings.values()) and set(cross.values()) <= {1, 2, 3},
         "three partings of the eight in four and four: " + "; ".join(f"{k}: {join(sorted(v))}" for k, v in partings.items())
         + ". They are not one parting: " + "; ".join(f"{a} with {b}, {v} of four" for (a, b), v in cross.items()))
    line("found", True, "a partner's namings, an other-than-all of the four even and an other-than-other-than-all of the four odd, are with a step of 15, odd onto even: one step from the four odd is the four even")
    line("found", True, "all or none at all, by its numbers: the opening is 15 and 0 at one cell, all on and none on; and the eight are one digit from the one or from the other. It is this session's executing, and no saying of a partner's meaning")
    line("found", True, "not executed: a social surface, bi-moral and co-competencing, of collective intelligence. Two across and four along is a number alone")
    return lines, {}

if __name__ == "__main__":
    lines, _ = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
