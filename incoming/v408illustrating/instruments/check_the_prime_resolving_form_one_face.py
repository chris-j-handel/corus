"""v408illustrating · the check of the 42nd drawing: the prime resolving form, one face, six prime livings across and ten fixings down.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/check_the_prime_resolving_form_one_face.py .

The drawing is made from v407primes' page, incoming/v407primes/The_prime_resolving_form.md, its table as it is: a row one
of ten fixing unchangeable, a column a prime living, a cell an interest. Its cells, its pairs and its interests not yet
resolving are the page's own, opened here from the page, so that a drawing and its page are one saying.
A seat, an interest's row, is a placing: no line here executes it. It opens the page and the living files, and writes
none. All or none: with one line not is, the check is not.
"""
import re, sys
from pathlib import Path

PAGE = "incoming/v407primes/The_prime_resolving_form.md"
COLUMNS = ("Turn", "Surface", "Spiral", "Ghost", "Piece", "Torus")
NOT_YET = (("the hypothesis for pieces", 5, "Piece", "**The hypothesis for pieces**"),   # an interest, its row, its column, its saying in the page's part
           ("Erdős and Kac", 6, "Torus", "**Erdős and Kac**"),
           ("bounded gaps", 7, "Turn", "**Bounded gaps and Cramér**"),
           ("Cramér", 7, "Surface", "**Bounded gaps and Cramér**"),
           ("Brun", 8, "Turn", "**Hardy and Littlewood, and Brun**"))
def the_table(page):
    """The page's table as it is: a row its name, its names now and next, and its six cells."""
    rows = []
    for l in page.split("\n"):
        if l.startswith("| **"):
            c = [x.strip() for x in l.strip("|").split("|")]
            name, now, nxt = re.fullmatch(r"\*\*(.+?)\*\*, (\d+) · (\d+)", c[0]).groups()
            rows.append((name, int(now), int(nxt), c[1:7]))
    return rows

if __name__ == "__main__":
    root = Path(sys.argv[1])
    text = lambda f: (root / f).read_text(encoding="utf-8")
    page = text(PAGE); rows = the_table(page)
    results = []
    def line(name, ok): results.append((name, bool(ok)))

    line("the page's table is ten rows and six columns: Turn, Surface, Spiral, Ghost, Piece and Torus",
         len(rows) == 10 and all(len(r[3]) == 6 for r in rows) and "| The ten, names now · next | " + " | ".join(COLUMNS) + " |" in page)
    named = [[bool(c) for c in r[3]] for r in rows]
    line("of sixty cells 34 are named and 26 are with none named: by column 6, 7, 6, 3, 6 and 6, and by row 2, 3, 4, 3, 3, 3, 3, 4, 4 and 5",
         sum(map(sum, named)) == 34 and [sum(r[j] for r in named) for j in range(6)] == [6, 7, 6, 3, 6, 6] and [sum(r) for r in named] == [2, 3, 4, 3, 3, 3, 3, 4, 4, 5])
    registry = text("Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v402mgr.md")
    seats = ["with 2-now-possibling and 10-next-co-possibling", "with 1-now-existing and 9-next-co-discovering", "with 6-now-co-possibling and 14-next-possibling",
             "with 8-now-same-existing and 16-next-same-existing", "with 5-now-co-existing and 13-next-discovering", "with 7-now-observing and 15-next-observing",
             "with 4-now-co-same-existing and 12-next-co-same-existing", "a rate fixing as a value, with 7 and 15", "with 3-now-co-observing and 11-next-co-observing", "a between fixing as a cut, with 5 and 13"]
    line("a row's names are a name now and that name 8 up next, Resolving the Hard Problem Registry's own seating, a row with its words there: 5 and 13 are with two rows, and 7 and 15 with two",
         all(r[2] == r[1] + 8 for r in rows) and all(s in registry for s in seats)
         and all(str(r[1]) in s and str(r[2]) in s for r, s in zip(rows, seats)))
    line("the rows are five bi-couplings in the page's own order, two rows a pair, and the columns three pairs, two columns a pair",
         "an observing and an opening; a completing and a same-existing; a middle and a parity; a sequencing and a rate; a two-way and a between" in page
         and [r[0].split(" fixing")[0] for r in rows] == ["An observing", "An opening", "A completing", "A same-existing", "A middle", "A parity", "A sequencing", "A rate", "A two-way", "A between"]
         and "The pairs: turn and surface, a row's turn side and its horizon side; spiral and ghost, a prime's closings and a crossed number passing them; piece and torus" in page)
    part = page[page.index("## Not yet resolving, with a suggestion"):page.index("## The not yet resolving, by v406geodesic2's drawings")]
    line("the interests not yet resolving are five, by the page's own part: an interest is in its cell and in the part, word for word",
         all(i in rows[r - 1][3][COLUMNS.index(c)] and s in part for i, r, c, s in NOT_YET))
    beside = [("Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v402mgr.md", "a hard problem is a changing fixing unchangeable"),
              (PAGE, "An interest is one of the ten fixing on one prime living."),
              (PAGE, "A cell with no interest named is a possibly existing interest not yet asked."),
              ("Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "Each of ten unchangeables is a drawing people already make")]
    line("four sentences beside the drawing are word for word in their files: two living, and the page's two", all(s in text(f) for f, s in beside))

    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
