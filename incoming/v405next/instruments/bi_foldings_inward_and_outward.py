"""Bi-foldings inward and outward, executed with the files' own moves.

    python3 -I incoming/v405next/instruments/bi_foldings_inward_and_outward.py EXHIBIT_ONE.md EXHIBIT_THIRTY.md

The moves are Exhibit THIRTY's step 609, a fold whole with a scale s: on the
names 1 to 8s, a move of 4s up or down, and 8s + 1 less. With s one, inward, it
is 4 up or down and 9 less on 1 to 8; with s two, outward, 8 up or down and
17 less on 1 to 16. A bi-folding goes the two in turn and comes to its starting
name again after four moves.

It executes the folds and sets them beside the files' own sayings:

  inward    the two bi-foldings with 1 to 9, beside Exhibit THIRTY's step 610
  outward   the four bi-foldings with 1 to 17, beside Exhibit ONE's four
  opening   which outward bi-foldings an inward one's names go to, beside
            Exhibit THIRTY's step 613, a name with its 9 less
  middle    the inward fold moved up by 4, on 5 to 12 with 17 less, beside
            Exhibit ONE's middle bi-foldings
  odd/even  the run of odd and even names round a bi-folding
  fractal   n inward as 8n - 7, beside Natural Intelligence 4.15's 1, 2 and 3
            of one scale as 1, 9 and 17 of the next

A line ends with same or not same, the executed beside the said. It sizes and
decides nothing: a line of the window rests on the lines before it, and this
only executes the arithmetic its cards draw on. The cards say *inside* and
*outside*; this says inward and outward, the one list's natural naming.
"""
import re
import sys


def fold(start, half, whole, lo, lead):
    """Four moves from start: a move of half (up in the lower half of the span,
    down in the upper) and whole less, in turn, the one named by lead ahead."""
    names, n = [start], start
    kinds = ["move", "less"] if lead == "move" else ["less", "move"]
    for step in range(4):
        if kinds[step % 2] == "move":
            n = n + half if n < lo + half else n - half
        else:
            n = whole - n
        names.append(n)
    return names


def as_cycle(names):
    """A bi-folding as its four names, back at its starting name."""
    return tuple(names[:4]) if names[4] == names[0] else None


def same_round(a, b):
    """The same four names round in the same order, from any of them."""
    return any(tuple(a[i:] + a[:i]) == tuple(b) for i in range(4))


def same_either_way(a, b):
    return same_round(list(a), b) or same_round(list(reversed(a)), b)


def show(c):
    return "-".join(str(n) for n in c)


def odd_even(c):
    return " ".join("odd" if n % 2 else "even" for n in c)


def verdict(ok):
    return "same" if ok else "not same"


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    one = open(sys.argv[1], encoding="utf-8").read()
    thirty = open(sys.argv[2], encoding="utf-8").read()

    # The files' own sayings.
    four = re.search(r"\*\*Four bi-foldings\.\*\*(.*?)\*\*Two moves, 9 less\.\*\*", one, re.S)
    if four is None:
        sys.exit("no Four bi-foldings in " + sys.argv[1])
    one_four = [tuple(int(x) for x in m.split("-"))
                for m in re.findall(r"^- \*\*(\d+-\d+-\d+-\d+)\*\*", four.group(1), re.M)]
    one_middle = sorted({tuple(int(x) for x in m.split("-"))
                         for m in re.findall(r"\*Middle bi-folding\*: (\d+-\d+-\d+-\d+)", one)})
    s610 = re.search(r"^610\. (.*)$", thirty, re.M).group(1)
    thirty_inward = [tuple(int(x) for x in m.split(", "))
                     for m in re.findall(r"round (\d, \d, \d, \d)", s610)]
    s613 = re.search(r"^613\. (.*)$", thirty, re.M).group(1)
    thirty_opening = {}
    for a, b, c in re.findall(r"(\d-\d-\d-\d) opens? to (\d+-\d+-\d+-\d+) and (\d+-\d+-\d+-\d+)", s613) + \
            re.findall(r"and (\d-\d-\d-\d) to (\d+-\d+-\d+-\d+) and (\d+-\d+-\d+-\d+)", s613):
        thirty_opening[tuple(int(x) for x in a.split("-"))] = [
            tuple(int(x) for x in b.split("-")), tuple(int(x) for x in c.split("-"))]

    print("Bi-foldings inward and outward, executed")
    print()

    # Inward: s one, 4 up or down and 9 less on 1 to 8, from 3 and from 4, the move ahead.
    inward = [as_cycle(fold(start, 4, 9, 1, "move")) for start in (3, 4)]
    print("Inward, 4 and 9 less on 1 to 8")
    for c, t in zip(inward, thirty_inward):
        print("  from %d: %s, Exhibit THIRTY 610 %s: %s" % (c[0], show(c), show(t), verdict(c == t)))
    eight = sorted(n for c in inward for n in c)
    print("  all eight now names between them: %s" % verdict(eight == list(range(1, 9))))
    print()

    # Outward: s two, 8 up or down and 17 less on 1 to 16, every bi-folding found.
    found = []
    for start in range(1, 17):
        for lead in ("move", "less"):
            c = as_cycle(fold(start, 8, 17, 1, lead))
            if c and not any(same_either_way(c, f) for f in found):
                found.append(c)
    print("Outward, 8 and 17 less on 1 to 16: %d bi-foldings" % len(found))
    for e in one_four:
        hit = [f for f in found if same_either_way(f, e)]
        print("  Exhibit ONE %s: %s" % (show(e), verdict(bool(hit))))
    print("  sixteen names between them: %s" % verdict(sorted(n for c in found for n in c) == list(range(1, 17))))
    print()

    # Opening: an inward bi-folding's names go to two outward ones, a name with its 9 less.
    print("Opening, inward to outward")
    for c in inward:
        goes = [e for e in one_four if set(e) & set(c)]
        said = thirty_opening.get(c, [])
        ok = len(goes) == 2 and all(any(same_either_way(g, s) for s in said) for g in goes)
        print("  %s goes to %s, Exhibit THIRTY 613: %s" % (show(c), " and ".join(show(g) for g in goes), verdict(ok)))
        for g in goes:
            pair = sorted(set(g) & set(c))
            print("    %s holds %s, a name and its 9 less: %s" % (show(g), " and ".join(map(str, pair)),
                                                                verdict(len(pair) == 2 and sum(pair) == 9)))
    print()

    # Middle: the inward fold moved up by 4, on 5 to 12, with 4 and 17 less.
    middle = []
    for start in range(5, 13):
        c = as_cycle(fold(start, 4, 17, 5, "move"))
        if c and not any(same_either_way(c, m) for m in middle):
            middle.append(c)
    print("Middle, 4 and 17 less on 5 to 12: %d bi-foldings" % len(middle))
    for e in one_middle:
        print("  Exhibit ONE's middle %s: %s" % (show(e), verdict(any(same_either_way(m, e) for m in middle))))
    shifted = all(any(same_either_way(tuple(n + 4 for n in c), m) for m in middle) for c in inward)
    print("  both the inward fold moved up by 4: %s" % verdict(shifted))
    print()

    # Odd and even round the bi-foldings.
    print("Odd and even round the bi-foldings")
    for c in inward:
        print("  inward %s: %s" % (show(c), odd_even(c)))
    for e in one_four:
        print("  outward %s: %s" % (show(e), odd_even(e)))
    print()

    # Fractal: n inward is 8n - 7.
    scale = {n: 8 * n - 7 for n in range(1, 18)}
    print("Fractal, n inward as 8n - 7")
    print("  " + ", ".join("%d to %d" % (n, m) for n, m in scale.items()))
    print("  1, 2 and 3 of one scale as 1, 9 and 17 of the next: %s" % verdict([scale[1], scale[2], scale[3]] == [1, 9, 17]))
    print("  a name's 1 to 17 inward begins 8 names after the one before it: %s"
          % verdict(all(scale[n + 1] - scale[n] == 8 for n in range(1, 17))))


if __name__ == "__main__":
    main()
