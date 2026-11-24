"""The next draft of Exhibit THIRTY-TWO Natural Prime Numbering, by its parts: an instrument of v406me's reporting.

    python3 -I incoming/v406me/instruments/the_next_draft_of_exhibit_thirty-two_by_its_parts.py ROOT [OUT]

ROOT is the set's root. The opening draft is v407primes'. A part of a next draft is a session's own file,
incoming/<session>/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_a_next_draft_its_<PART>.md, with <PART> one of
OPENING, ONE, TWO, THREE, FOUR, FIVE, and its lines from its title "# <PART> ..." on.

It says, a part a line: whose the part is now, the opening draft's or a next draft's; its words; and the rows of
the one table at it, open, carried in and let go. With OUT it lays the draft with the next parts in their places,
a trial copy outside the set, for the instruments of an exhibit's form to execute on. It reports, and is no gate.

    python3 -I incoming/v406me/instruments/the_next_draft_of_exhibit_thirty-two_by_its_parts.py ROOT --part ONE

With --part and a part's name, or "the whole", it says the open rows of the one table at that part, a row with its
place, its concern, the words offered for it, the four shown of them, and its source: all a part's writer goes
through, in one place.
"""
import csv, glob, os, re, sys

PARTS = ["OPENING", "ONE", "TWO", "THREE", "FOUR", "FIVE"]
root = sys.argv[1] if len(sys.argv) > 1 else "."
one = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--part" else None
out = sys.argv[2] if len(sys.argv) > 2 and not one else None
draft = os.path.join(root, "incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md")
table = os.path.join(root, "incoming/v406me/Exhibit_THIRTY-TWO_the_concerns_of_all_sessions_in_one_table.csv")

L = open(draft, encoding="utf-8").read().split("\n")
starts = {}
for i, l in enumerate(L):
    m = re.match(r"^# (OPENING|ONE|TWO|THREE|FOUR|FIVE)\b", l)
    if m:
        starts[m.group(1)] = i
order = sorted(starts, key=starts.get)
close = next(i for i in range(starts[order[-1]], len(L)) if L[i].strip() == "---")
ends = {p: (starts[order[k + 1]] if k + 1 < len(order) else close) for k, p in enumerate(order)}

nexts = {}
for f in sorted(glob.glob(os.path.join(root, "incoming/*/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_a_next_draft_its_*.md"))):
    part = re.search(r"_its_([A-Z]+)\.md$", f).group(1)
    N = open(f, encoding="utf-8").read().split("\n")
    t = next((i for i, l in enumerate(N) if re.match(r"^# " + part + r"\b", l)), None)
    if part in PARTS and t is not None:
        nexts[part] = (f, N[t:])

rows = list(csv.reader(open(table, encoding="utf-8", newline="")))
ix = {h: i for i, h in enumerate(rows[0])}
num = {"1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR", "5": "FIVE"}
at = {p: {"open": 0, "carried in": 0, "let go": 0} for p in PARTS + ["the whole"]}
by_part = {p: [] for p in PARTS + ["the whole"]}
for r in rows[1:]:
    pl = r[ix["Its place in the draft"]]
    ps = sorted({num[m] for m in re.findall(r"(?<![\d.])([1-5])\.\d", pl)})
    if not ps:
        ps = ["OPENING"] if "opening" in pl.lower() else ["the whole"]
    for p in ps:
        at[p][r[ix["Its standing"]]] = at[p].get(r[ix["Its standing"]], 0) + 1
        by_part[p].append(r)

words = lambda lines: sum(len(l.split()) for l in lines)
if one:
    if one not in by_part:
        sys.exit("a part is one of: " + ", ".join(by_part))
    op = [r for r in by_part[one] if r[ix["Its standing"]] == "open"]
    print(f"{one}: {len(op)} rows of the one table open at it")
    for r in op:
        print(f"\nRow {r[ix['Concern']]} · at {r[ix['Its place in the draft']]} · {r[ix['Its kind']]} · found by {r[ix['Found by']]}")
        print("  the concern: " + r[ix["The concern, an is-or-is-not, or a thing to mend"]])
        print("  words offered: " + r[ix["A suggested improving"]])
        if "Shown of the four" in ix:
            print("  " + r[ix["Shown of the four"]])
        print("  its source: " + r[ix["Its source"]])
    sys.exit(0)
print("The next draft of Exhibit THIRTY-TWO, by its parts")
laid = 0
body = []
for p in order:
    old = L[starts[p]:ends[p]]
    if p in nexts:
        f, new = nexts[p]
        laid += 1
        who = os.path.relpath(f, root).split(os.sep)[1]
        print(f"  {p:<8} a next draft's, {who}'s · {words(new)} words, the opening draft's {words(old)} · rows at it: {at[p]}")
        body += [l for l in new] + [""]
    else:
        print(f"  {p:<8} the opening draft's · {words(old)} words · rows at it: {at[p]}")
        body += old
print(f"  the whole · rows at it: {at['the whole']}")
print(f"{laid} of {len(order)} parts are a next draft's. Rows of the one table: " +
      ", ".join(f"{k} {sum(1 for r in rows[1:] if r[ix['Its standing']] == k)}" for k in ("open", "carried in", "let go")) + ".")
if out:
    whole = L[:starts[order[0]]] + body + L[close:]
    open(out, "w", encoding="utf-8").write("\n".join(whole))
    print(f"Laid as a trial copy: {out}, {words(whole)} words.")
