#!/usr/bin/env python3
"""A user's finding: the set's drawings and its code, a row a thing, with its place and what it helps a user understand.

    python3 -I incoming/v406me/instruments/a_users_finding_of_the_drawings_and_the_code.py ROOT
    python3 -I incoming/v406me/instruments/a_users_finding_of_the_drawings_and_the_code.py ROOT OUT

With ROOT alone it goes through the set's drawings and code beside the catalog in this session's folder, and
says a bump: a thing of the set with no row, or a row whose thing is at no place of the set now.
With OUT it lays the catalog as a table at OUT, and writes no other file.
A drawing's saying is its own name. A code's saying is the opening line of its own words, set as code, word for word.
The living home of a drawing is Exhibit TWENTY-NINE Natural Illustrating, its gathering file and its drawings.
"""
import csv, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
out = sys.argv[2] if len(sys.argv) > 2 else None
CAT = "incoming/v406me/A_users_finding_the_drawings_and_the_code_a_thing_with_its_place.csv"
PIC = (".png", ".svg", ".html", ".jpg", ".gif")
def of(text):
    t = text.lower()
    for words, name in [
        (("riemann", "thirty-two", "thirty_two", "prime", "staircase", "zeros"), "Exhibit THIRTY-TWO Natural Prime Numbering, and Riemann's hypothesis"),
        (("nand", "resolver", "a_me", "cell"), "Exhibit ONE Natural Resolver, its code and its nand lines"),
        (("illustrat", "drawing", "draft", "artboard", "canvas"), "Exhibit TWENTY-NINE Natural Illustrating"),
        (("opening", "window", "working_document", "seventeen"), "Natural Intelligence's opening"),
        (("managing", "table", "aims", "asked", "closing", "harm", "offer"), "The managing of the expedition"),
        (("gathering", "note", "pile", "droplet", "check_set", "carry"), "The gathering files and the set's checks"),
    ]:
        if any(w in t for w in words):
            return name
    return ""
def opening(path):
    try:
        s = open(path, encoding="utf-8", errors="replace").read(4000)
    except OSError:
        return ""
    m = re.search(r'"""(.*?)(?:\n\n|""")', s, re.S)
    line = " ".join(m.group(1).split()) if m else ""
    if not line:
        c = [l[1:].strip() for l in s.split("\n")[:12] if l.startswith("#") and not l.startswith("#!")]
        line = " ".join(c)
    return line[:300]
rows = []
for d, _, files in os.walk(root):
    rel = os.path.relpath(d, root)
    if rel.startswith(".git") or "/.git" in rel:
        continue
    top = rel.split(os.sep)
    home = top[1] if top[0] == "incoming" and len(top) > 1 else top[0]
    stems = {}
    for f in sorted(files):
        p = os.path.join(rel, f)
        if f.endswith(PIC) and (("illustrations" in top) or ("drawings" in top) or ("Illustrat" in rel)):
            stems.setdefault(os.path.splitext(f)[0], []).append(f)
        elif f.endswith(".py"):
            kind = "a drawing's maker" if f.startswith("make_") else "a check" if f.startswith("check") else "a kit's code" if top[0] == "kits" else "an instrument"
            say = opening(os.path.join(root, p))
            rows.append(["`" + os.path.splitext(f)[0] + "`", kind, ("`" + say.replace("`", "") + "`") if say else "", of(f + " " + say), home, p, "", "A code example, with its executing: `python3 -I " + p + "`"])
    for stem, fs in sorted(stems.items()):
        if re.match(r"Draft\d+\.dc$", stem) and os.path.basename(rel) == "artboards":
            continue    # a drawing's board, said with its drawing
        m = re.match(r"draft_(\d+)_(.*)", stem)
        name = (f"Drawing {m.group(1)}: " + m.group(2).replace("_", " ")) if m else stem.replace("_", " ")
        inst = os.path.join(root, os.path.dirname(rel), "instruments")
        withit = [x for x in fs]
        if m and os.path.exists(os.path.join(root, rel, "artboards", f"Draft{m.group(1)}.dc.html")):
            withit.append(f"artboards/Draft{m.group(1)}.dc.html")
        if m and os.path.isdir(inst):
            withit += [x for x in sorted(os.listdir(inst)) if x == f"make_draft{m.group(1)}.py" or (x.startswith("check_") and m.group(2)[:28] in x)]
        its = "In its kit, living" if top[0] == "kits" else "In the gathering files' drawings" if top[0] == "gathering-value" else "A drawing for Natural Illustrating's gathering: a note in its gathering file of the next version, and its file to gathering-value/drawings"
        rows.append([name, "a drawing", name, "Exhibit TWENTY-NINE Natural Illustrating" if not of(stem) else of(stem), home, os.path.join(rel, fs[0]), "; ".join(withit), its])
rows.sort(key=lambda r: (r[1] != "a drawing", r[4], r[5]))
for r in rows:
    r[5] = "`" + r[5] + "`"    # a place is set as code
head = ["The thing", "Its kind", "What it helps a user understand", "Of", "Its session or its home", "Its place", "With it", "For Natural Illustrating"]
if out:
    csv.writer(open(out, "w", newline="")).writerows([head] + rows)
kinds = {}
for r in rows:
    kinds[r[1]] = kinds.get(r[1], 0) + 1
print("The set's drawings and code now: " + ", ".join(f"{k}, {n}" for k, n in sorted(kinds.items(), key=lambda x: -x[1])) + ".")
if not out and os.path.exists(os.path.join(root, CAT)):
    have = set(r[5] for r in list(csv.reader(open(os.path.join(root, CAT), newline="")))[1:])
    now = set(r[5] for r in rows)
    for p in sorted(now - have):
        print("a bump: a thing of the set with no row of the catalog: " + p)
    for p in sorted(have - now):
        print("a bump: a row of the catalog whose thing is at no place of the set now: " + p)
    print("No bump: the catalog and the set are a row a thing." if now == have else f"{len(now ^ have)} bumps.")
