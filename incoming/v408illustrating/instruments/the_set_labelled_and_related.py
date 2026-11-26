"""v408illustrating · the set of its drawings, labelled and related: a drawing a row, with its prior, its other-prior, its now and its next.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/the_set_labelled_and_related.py .

A partner's saying of 25 November, in this session's words: a set, by a cohering method of labelling and relating it.
The method: a drawing's label is its number, its name, its view and what it is for; and its relations are four, the four
of the day's rigorizing: its prior, a drawing of this set it goes on from; its other-prior, an other session's drawing or
page it rests on; beside it now, a drawing of the set with one concept by an other observing; and its next.
The table is The_set_of_v408illustrating_s_drawings_a_drawing_a_row.csv. This instrument says a bump: a drawing with no
row, a row with no drawing, a relation naming nothing, a relation said one way alone. It is the 44th drawing's check too.
It opens the set and writes none. All or none.
"""
import csv, re, sys
from pathlib import Path

HOME = "incoming/v408illustrating/"
def the_set(root):
    rows = list(csv.DictReader(open(Path(root) / HOME / "The_set_of_v408illustrating_s_drawings_a_drawing_a_row.csv", encoding="utf-8")))
    parts = lambda s: [p.strip() for p in s.split(";") if p.strip()]
    return rows, parts

if __name__ == "__main__":
    root = Path(sys.argv[1]); rows, parts = the_set(root)
    results = []
    def line(name, ok): results.append((name, bool(ok)))
    drawn = [r for r in rows if r["Drawing"]]; ahead = [r for r in rows if not r["Drawing"]]
    numbers = [r["Drawing"] for r in drawn]; names = [r["Its name"] for r in ahead]
    boards = sorted(int(re.search(r"Draft(\d+)", p.name).group(1)) for p in (root / HOME / "illustrations/artboards").glob("Draft*.dc.html"))
    line("a drawing of the folder is a row of the table and a row a drawing, one for one, the 44th the table's own map",
         sorted(int(n) for n in numbers) in (boards, boards + [44]) and all(r["Its standing"] == "a candidate" for r in drawn) and all(r["Its standing"] == "ahead" for r in ahead))
    line("a drawing of a row is with its maker and its check in the folder, and a view by its number",
         all((root / HOME / "instruments" / r["Its check"]).exists() and (r["Drawing"] == "44" or ((root / HOME / "instruments" / f"make_draft{r['Drawing']}.py").exists()
             and list((root / HOME / "illustrations").glob(f"draft_{r['Drawing']}_*.png")))) for r in drawn))
    line("a label is whole: a name, a view and what it is for, at all rows", all(r["Its name"] and r["Its view"] and r["It is for"] for r in rows))
    known = set(numbers) | set(names)
    line("a prior, a now and a next name a row of the table, at all rows", all(x in known for r in rows for k in ("Its prior", "Beside it now", "Its next") for x in parts(r[k])))
    key = lambda r: r["Drawing"] or r["Its name"]
    nexts = {(key(r), x) for r in rows for x in parts(r["Its next"])}; priors = {(x, key(r)) for r in rows if key(r) != "44" for x in parts(r["Its prior"])}
    line("a next and a prior are one relation said both ways: a drawing's next is with that drawing its prior, at all rows but the map's own", nexts == priors)
    beside = {(key(r), x) for r in rows for x in parts(r["Beside it now"])}
    line("beside is said both ways, a pair a pair: 40 with 41, 42 with 43, 43 with 45, 46 with 49, and 49 with 54", beside == {(b, a) for a, b in beside} and {tuple(sorted(x)) for x in beside} == {("40", "41"), ("42", "43"), ("43", "45"), ("46", "49"), ("49", "54")})
    others = [(r["Drawing"], *[s.strip() for s in o.split(" = ")]) for r in rows for o in parts(r["Its other-prior"])]
    apart = [o for o in others if not (root / o[2]).exists()]
    line("an other-prior is a drawing or a page of an other session, in the set at its place; v408primes' pages alone are ahead of the set, on that session's branch",
         len(others) == 29 and all(o[2].startswith("incoming/v408primes/") for o in apart) and all(len(o) == 3 for o in others))
    line("the map's own prior is the set's drawings, all of them", parts(next(r for r in rows if r["Drawing"] == "44")["Its prior"]) == [n for n in numbers if n != "44"])
    for name, ok in results: print(("is       " if ok else "is-not   ") + name + "\n")
    print(f"{sum(ok for _, ok in results)} of {len(results)} are is")
    sys.exit(0 if all(ok for _, ok in results) else 1)
