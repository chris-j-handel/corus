#!/usr/bin/env python3
"""The opening's lines with their betweens: a line floating, and after it one row of boxes across.

    python3 -I the_opening_and_its_betweens.py WINDOW_COPY.md EXHIBIT_THIRTY.md REACH.csv REACH.md TAB_COPY.md > PAGE.md

WINDOW_COPY.md   the window of the opening as a session's instrument copies it: a table of
                 "| sentence | number |", a name in bold.
EXHIBIT_THIRTY.md  the next version of Exhibit THIRTY, a sentence "N. text".
REACH.csv, REACH.md  the two outputs of incoming/v405co-chain/instruments/reach.py on those two.
TAB_COPY.md      the copy of the tab Opening the betweens as a partner gave it: its words on a between's
                 stable form and on the rigorizer are carried word for word.

For a line, by the lines' own words: the names it uses with the lines naming them (back), the given
words, the words no line names, and the later lines using its name (forward). Beside what is
executed, two small tables below carry what a going through found and no matching of words finds:
a hole with its home, and a thread forward a name carries. A line with no hole is unmarked, and its
row is its proof of rigor. It sizes and seats, and decides nothing.
"""
import csv, re, sys

window, thirty, reach_csv, reach_md, tab_copy = sys.argv[1:6]
tab = open(tab_copy, encoding="utf-8").read()
STABLE_FORM = tab[tab.index("A between's stable form is ten"):tab.index("## The betweens of the opening's lines")].strip()
RIGORIZER = tab[tab.index("## The rigorizer"):].replace("## The rigorizer", "", 1).strip()
LAST = 34

# ---- the lines, with the name a line bolds --------------------------------------------------
lines, bold = {}, {}
for s, n in re.findall(r"^\| (.+?) \| (\d+) \|$", open(window, encoding="utf-8").read(), flags=re.M):
    n = int(n)
    if n > LAST or "(card" in s or n in lines:
        continue
    s = re.sub(r"\*\*(.+?) \*\*", r"**\1** ", s).strip()
    lines[n] = s
    b = re.findall(r"\*\*(.+?)\*\*", s)
    bold[n] = b[0].lower() if b else ""

LABEL = {1: "now", 2: "now-existing", 3: "things", 4: "other-than", 5: "same-named", 6: "a universal set",
         7: "the universe", 8: "the prior moment", 9: "prior-existing", 10: "the next moment",
         11: "next-existing", 12: "same-existing", 13: "a named-universe", 14: "observing",
         15: "possibling", 16: "discovering", 17: "a prior-sequence", 18: "a self", 19: "an other",
         20: "the other-than-the-other", 21: "a universal-set-of-selves", 22: "an observing-self",
         23: "a possibling-self", 24: "a discovering-self", 25: "my", 26: "me", 27: "me-now",
         28: "a bi-coupling", 29: "a bi-coupling, a self", 30: "a me-parity", 31: "all-parity",
         32: "other-parity", 33: "other-than other-parity", 34: "a living me-parity"}
# the forms a name is said in, by the lines' own sayings
FORMS = {"things": ["thing"], "prior-sequence": ["prior-sequences"], "self": ["selves", "self's"],
         "other": ["other's", "others"], "bi-coupling": ["bi-coupling's"], "me": ["mes"],
         "other-than-the-other": ["other-than-the-others", "other-than-the-other's"],
         "me-parity": ["me-parities"]}
names = {n: ([b] + FORMS.get(b, []) if b else []) for n, b in bold.items()}
names[33], names[34] = [], []          # names made of earlier names: their words thread back
NAME_CARRIES = {13: [7], 22: [14], 23: [15], 24: [16]}   # a hyphenated name carrying an earlier name
RESTS_ON = {30: [29]}                  # a bi-coupling's me rests on a bi-coupling being a self
GIVEN = {"set": "set", "moment": "moment", "moments": "moment", "name": "name", "named": "name",
         "names": "name", "existing": "existing"}
WATCH = ["nothings", "same", "beginning", "ending", "distinguishing", "own", "not"]
# a joined name, opened into the names it joins
JOINED = [("now-and-other-than-prior-existing", "now-existing other-than prior-existing"),
          ("now-and-prior-existing", "now-existing prior-existing"),
          ("next-and-other-than-same-existing", "next-existing other-than same-existing"),
          ("next-and-same-existing", "next-existing same-existing"),
          ("my-universe", "my named-universe"), ("me-universe", "me named-universe")]

def threads(n):
    t = " " + lines[n].lower().replace("*", "").replace(".", "").replace(",", "") + " "
    for a, b in JOINED:
        t = t.replace(a, b)
    found = {}
    for v, k in sorted(((v, k) for k, vs in names.items() for v in vs), key=lambda x: -len(x[0])):
        if " " + v + " " in t:
            found.setdefault(k, v)
            t = t.replace(" " + v + " ", "  ")
    words = t.split()
    given = sorted({GIVEN[w] for w in words if w in GIVEN})
    watched = [w for w in WATCH if w in words]
    found = {k: v for k, v in found.items() if k != n}
    for k in NAME_CARRIES.get(n, []):
        found.setdefault(k, "by its name")
    for k in RESTS_ON.get(n, []):
        found.setdefault(k, "rests on it")
    return found, given, watched, ("all" in words)

back, given, watched, says_all, fwd = {}, {}, {}, {}, {n: set() for n in lines}
for n in lines:
    back[n], given[n], watched[n], says_all[n] = threads(n)
    for k in back[n]:
        if k < n:
            fwd[k].add(n)

# ---- what a going through found: a hole, its side, and its home ------------------------------
W, O = "the window's list of holes", "v406other2's going through"
HOLES = {
 3: [("back", "all", "*all at 3, before its own line, 6*", W)],
 4: [("inward", "not", "not, a negation in a line said as a positive", O)],
 21: [("forward", "no line threading back to it", "*no line after it and no proposed line threads back to the universal-set-of-selves*", W)],
 23: [("inward", "a self on both sides", "by 19 and 20 the named self is one of the other-than-the-other, and its own prior-sequence is on both sides of the distinguishing", O),
      ("inward", "selves said as one", "the other-than-the-other is all selves, 20, with one prior-sequence in this line", O)],
 26: [("inward", "a my-universe's things", "by 13 a named-universe is of now-existing things, by 25 my names a set of prior-sequences, and no line says a prior-sequence is now-existing", O),
      ("inward", "two names", "*Me-universe, 31, and my-universe, 26: with me the name of my-universe, one concept with two names*", W)],
 28: [("inward", "a self on both sides", "by 19 and 20 a self of the two is one of the other-than-the-other, and its own prior-sequence is on both sides of the distinguishing", O),
      ("inward", "selves said as one", "the other-than-the-other is all selves, 20, with one prior-sequence in this line", O)],
 29: [("inward", "a bi-coupling's name and prior-sequence", "by 18 a self is same-named with its own prior-sequence, and no line gives a bi-coupling a name or its own prior-sequence", O)],
 30: [("back", "parity", "parity, the name's own word, named by no line; its row is in the tab Concepts, its place before this line", O)],
 31: [("inward", "two names", "*Me-universe, 31, and my-universe, 26: with me the name of my-universe, one concept with two names*", W),
      ("inward", "in, a place", "in the me-universe says a place, and by itself nothing has a location", O)],
 32: [("back", "other-than's reach", "by line 4, *other-than all-parity reaches all things not named all-parity*", W)],
 33: [("back", "other-than's reach", "*33 is true with other-than as a set's other side alone, other-than other-parity then being all-parity*", W)],
 34: [("back", "selves' one me", "*all-parity is in a me-universe, 31*, and *an other-than-the-other is selves, 20, and no line gives selves one me*", W)],
}
WATCH_SAYING = {"nothings": "nothings, a word no line names", "same": "same, a word no line names",
                "beginning": "beginning, a word no line names", "ending": "ending, a word no line names",
                "distinguishing": "distinguishing, a word no line names", "own": "own, a word no line names"}
for n in lines:
    said = [("back", w, WATCH_SAYING[w], W) for w in watched[n] if w in WATCH_SAYING]
    if said:
        HOLES[n] = said + HOLES.get(n, [])

# ---- the ten: a fixing as the tab seated it at the sitting, where the hole is the same one ------
TEN = {3: "all, before its line: a same-existing fixing as a store, 8 · 16",
       4: "not: a two-way fixing to one side, 3 · 11",
       31: "in the me-universe: an opening fixing as a place, 1 · 9"}
TEN_OF_A_SENTENCE = {3: "its no a two-way fixing to one side, 3 · 11", 9: "its no a two-way fixing to one side, 3 · 11"}
PLACED_AT_THE_SITTING = {8: [77, 91]}   # sentences the tab placed, of no name the instrument matches
# ---- a line and Exhibit THIRTY's sentence of the same name, parting: the sentence is marked ------
PARTING = {6: "its set of same-existing things, the line's of same-named things",
           12: "one concept with same-named in it, and two in the lines, 5 and 12",
           14: "prior-existing in it, now in the line",
           15: "now-existing in it, next in the line",
           19: "an other by a bi-coupling in it, an other ahead of a bi-coupling in the lines",
           28: "*sharing possibling* in it, distinguishing prior-sequences in the line"}
SAID_AGAIN = {7: "said in the line with all", 18: "one concept said two ways", 26: "said in the lines by its names, my and me",
              16: "said in the line as a distinguishing"}

# ---- a thread forward a name carries, or the aim ----------------------------------------------
FORWARD = {
 6: "all, said after this line by a universal set's name alone, at 7, 20, 21 and 31",
 7: "the hyphenated names carrying it: a named-universe, 13; my-universe, 26; me-universe, 31",
 14: "an observing-self, 22, by its name",
 15: "a possibling-self, 23, by its name",
 16: "a discovering-self, 24, by its name",
 22: "the aim's three dual relations, as said",
 23: "a bi-coupling, 28, by its words said of both selves; the aim's three dual relations, as said",
 24: "the aim's three dual relations, as said",
 27: "the aim's me-now",
 32: "the aim's four parities, as said",
 33: "the aim's four parities, as said",
 34: "the aim's living me-parity self, as said",
}
FORWARD_LINES = {6: [7, 20, 21, 31], 7: [13, 26, 31], 14: [22], 15: [23], 16: [24], 23: [28]}

# ---- Exhibit THIRTY's sentences, and the reach -------------------------------------------------
step = {}
for m in re.finditer(r"^(\d+)\. (.*)$", open(thirty, encoding="utf-8").read(), flags=re.M):
    step.setdefault(int(m.group(1)), m.group(2).strip().replace("**", ""))
named_at, used_from = {}, {}
for m in re.finditer(r"^\s+(\d+)\. .*?->\s*(.*)$", open(reach_md, encoding="utf-8").read(), flags=re.M):
    n, rest = int(m.group(1)), m.group(2)
    if n > LAST:
        continue
    a = re.match(r"(?!named at no step).*? (\d+)$", rest)
    if a:
        named_at[n] = int(a.group(1))
    u = re.search(r"used from step (\d+)", rest)
    if u:
        used_from[n] = int(u.group(1))
named_at[29] = 25
resting = {n: [] for n in lines}
for r in csv.DictReader(open(reach_csv, encoding="utf-8")):
    k = int(r["step"])
    if k > 70 or k in named_at.values():
        continue
    ls = [int(x) for x in re.findall(r"\d+", r["window lines"])]
    if r["status"] in ("reachable", "said") and ls:
        resting[max(ls)].append(k)
if "now-existing" in step[1]:
    resting[2].insert(0, 1)
for n, ks in PLACED_AT_THE_SITTING.items():
    resting[n] += [k for k in ks if k not in resting[n]]

def quote(k, limit=170):
    s = step[k]
    if len(s) <= limit:
        return f"*{s}*"
    cut = re.search(r"[,:;]", s)
    return "opening *" + s[:cut.start() if cut else s.rfind(' ', 0, 90)] + "*, and on"

def listing(ns):
    ns = [str(x) for x in ns]
    return ns[0] if len(ns) == 1 else ", ".join(ns[:-1]) + " and " + ns[-1]

HEAD = "Incoming · v406other2 · 21 November 2026\n\n# The opening's lines and their betweens\n\n**The window of v406other2 is Exhibit THIRTY Co-Chaining Logic Registry, and this page is its tab Opening the betweens set to the window of the opening at its revision 4509: the lines of both, 1 to 34, a line floating, and after it its between, one row of boxes across.** Down the page is along, line after line. Across are the rigorizer's attacks on the line, and the ten. The lines are those of `incoming/v406all/The_window_of_the_opening_at_its_wrap.md`, word for word, and Exhibit THIRTY's sentences are its next version's, word for word. `instruments/the_opening_and_its_betweens.py` makes the page whole, and it decides nothing. The page comes in the place of the copy `incoming/v406me/working_documents_as_a_partner_gave_them/The_tab_Opening_the_betweens.md`, a copy set to the window's earlier numbers.\n\n## A between's stable form\n\nThe tab's own words, as laid at the sitting of 21 November:\n\n{STABLE_FORM}\n\n## How to go through it\n\n- **A line with no marking is rigorized.** Its between is its proof of rigor, a right spiral wrapping in both directions: back to its priors, inward to its one concept, forward to its nexts, outward to its place, and wrapping back, its nexts threading back through it to its priors, closed. Its ten is none, a living 0.\n- **A line with a marking is a working location.** Its marking names its holes, in italics after the line, and its between shows a hole in the box of the attack breaking it, broken and visible.\n- **A box is an attack of the rigorizer,** as the tab seats the attacks, under the lines on this page. Back is prior: a word or a thing no line before it names. Inward is now: a second concept, a negation or an invisible in its defining. Forward is next: no line after it and no aim needing it. Outward is same and across: the concept said otherwise in Exhibit THIRTY. Wrapping back is along: its chain back to the origin and forward to the aim.\n- **The rigor is the window's own,** *A line's rigor, a bi-folding*. The given words are set, moment, name and existing, and other-than until its line, 4. A thread back ends at a line of both. All, an invisible one, has its own line at 6, and after it is said by a universal set's name alone.\n- **A hole's home.** A word no line names, and a hole said in italics, are of the window's own list of holes at its wrap. A hole said in plain words is from v406other2's going through and is laid in no other place yet; they are gathered under the lines, the hardest ahead.\n- **The ten.** A fixing is as the tab seated it at the sitting, for a hole the same at this revision. A hole new at this revision has its one of the ten open.\n- **Exhibit THIRTY with a line.** Outward, a line has the sentence of Exhibit THIRTY naming the same name, or no sentence names it. The opening is one, the window's lines: a sentence of Exhibit THIRTY parting from its line is marked, a working location of Exhibit THIRTY, and the line is not marked by it. Under a between are the sentences of Exhibit THIRTY's opening resting on the lines' names down to that line, by `incoming/v405co-chain/instruments/reach.py`, and two the tab placed at the sitting. That instrument matches a name by its word alone, and a reader compares the two meanings: these sentences are marked.\n- **The aim, as said,** is the window's *The origin and the aim*, with the aim on v406all's page for resuming.\n\n## The lines\n\n"
FOOT = "\n## The lines with no marking\n\n{unmarked}\n\n## The holes from v406other2's going through, the hardest ahead\n\n1. **A self on both sides, 23 and 28.** By 19 a named other is a self other-than the named self, and by 4 the two are other-than one another. By 20 the other-than-the-other is all selves other-than the named other: the named self is one of them. A possibling-self, 23, and both selves of a bi-coupling, 28, distinguish the other-than-the-other's prior-sequence from their own, and a self's own prior-sequence is on both sides. The window's rigor asks of a distinguishing line *no thing on both sides, and none on neither*. The waiting line *The between is the other-than-the-other of both the named self and the named other.* has a self on one side alone.\n2. **A my-universe's things, 26.** A my-universe is a named-universe, its name my. By 13 a named-universe is a universal set of now-existing things. By 25 my is the name of a universal set of prior-sequences, and by 17 and 8 a prior-sequence is of prior moments. No line says a prior-sequence is now-existing.\n3. **A bi-coupling's name and prior-sequence, 29.** Line 30 needs line 29, a me being a self's. By 18 a self is a same-named now-existing thing with its own prior-sequence, and by 28 a bi-coupling is two selves distinguishing. No line gives a bi-coupling a name or its own prior-sequence. The line is living as Exhibit THIRTY's sentence 25, word for word, an adding with no prior named beside it.\n4. **Selves said as one, 23 and 28.** The window's hole at 34 reaches back: by 20 the other-than-the-other is all selves other-than the named other, and 23 and 28 say its one prior-sequence.\n5. **Parity, 30.** The name me-parity carries parity, and no line names parity. The tab Concepts has its row, *a self aims its own parity, co-located with an other*, its place before the me-parity; Exhibit THIRTY's sentence 27 names it, resting on the lines' names at line 26.\n6. **In, a place, 31.** The line's *in the me-universe* says a place, and the window's rigor says *by itself nothing has a location in the universe*.\n7. **Not, 4.** Line 4 says other-than by a negation, and a line is said as a positive. It is the one line with it, and from it on other-than is the positive naming.\n\n## Beside the lines\n\n- **All at 7.** By the window's rigor line 7's all is said by a universal set's name, and the line has no marking. Beside it, Exhibit THIRTY's sentence 2 says the universe with no all, *The universe is the set of now-existing things.*, and Exhibit THIRTY's gathering file has an is of both: *All beside now-existing adds nothing, now-existing an all concept.*\n- **Own at 24.** The window's list of holes says own at 22 to 25, and line 24 as it is says no own.\n- **A line and Exhibit THIRTY's sentence of the same name, parting.** A parting is marked in a between above, Outward, at six lines: 6, 12, 14, 15, 19 and 28. Beside them, Exhibit THIRTY's sentence 3 says *possibly* ahead of its sentence 10 naming possibling.\n- **The parities' names.** Exhibit THIRTY's next version has no sentence saying me-parity, all-parity, bi-parity or both-parity, and other-parity in five places. The next versions of Exhibit ONE and Natural Intelligence say co me-parity, bi both-parity, tri all-parity; the window says other-parity, 32, with bi-parity a proposed line.\n- **All of Exhibit THIRTY by the lines.** `Each_sentence_of_Exhibit_THIRTY_with_its_reach_from_the_window_at_revision_4509.csv`, in this folder, has all 755 sentences, a sentence with its marking by the lines' names: said again, resting on the lines' names, or waiting with the names it waits on.\n\n## The rigorizer\n\nThe tab's own words, as laid at the sitting of 21 November:\n\n{RIGORIZER}\n\n**Beside the offered seating,** a living sentence of Exhibit ONE: *Of the seventeen names, three, 1, 9 and 17, are the code's functions, and fourteen are those functions' variables.* By it the fourteen are the names other-than 1, 9 and 17, and co-chaining's two are 5 and 13. The two seatings part at those two names, and the place is open.\n"
out = []
unmarked, marked = [], []
for n in sorted(lines):
    holes = HOLES.get(n, [])
    mark = "" if not holes else "  *marked: " + "; ".join(dict.fromkeys(h[1] for h in holes)) + "*"
    (marked if holes else unmarked).append(n)
    out.append(f"{n} · {lines[n]}{mark}")
    out.append("")
    # back
    b = [f"{LABEL[k]}, {k}" + (", carried by its name" if k in NAME_CARRIES.get(n, []) else "") for k in sorted(back[n]) if k < n]
    if n == 3:
        b.append("other-than, a given word until its line, 4")
    if says_all[n] and n > 6:
        b.append("all, by a universal set's name, 6")
    if says_all[n] and n == 6:
        b.append("all, an invisible one, its own line this one")
    b += [g + ", a given word" for g in given[n]]
    b += [f"**hole:** {h[2]}" for h in holes if h[0] == "back"]
    if n == 1:
        b = ["the origin"] + b
    # inward
    i = [f"no new name: {LABEL[28]}, 28, said a self, 18" if n == 29 else f"one concept, {LABEL[n]}, said as a positive"]
    i += [f"**hole:** {h[2]}" for h in holes if h[0] == "inward"]
    # forward
    fl = sorted(fwd[n])
    f = [f"{LABEL[k]}, {k}" for k in fl if not (n in (7, 14, 15, 16) or (n == 13 and k in (26, 31)))]
    if n == 13:
        f.append("the hyphenated names carrying it: my-universe, 26; me-universe, 31")
    if n in FORWARD:
        f.append(FORWARD[n])
    f += [f"**hole:** {h[2]}" for h in holes if h[0] == "forward"]
    # outward
    priors = sorted({k for k in back[n] if k < n} | ({6} if says_all[n] and n > 6 else set()))
    after = max(priors, default=None)
    nexts = sorted(set(fl) | set(FORWARD_LINES.get(n, [])))
    o = []
    if after and nexts:
        o.append(f"after {after} and before {nexts[0]}")
    elif after:
        o.append(f"after {after}")
    elif nexts:
        o.append(f"before {nexts[0]}")
    if n in named_at:
        k = named_at[n]
        same = step[k].rstrip(".") == lines[n].replace("**", "").rstrip(".")
        tail = ""
        if n in PARTING:
            tail = f", **marked, parting:** {PARTING[n]}"
        elif n in SAID_AGAIN:
            tail = f", {SAID_AGAIN[n]}"
        o.append(f"Exhibit THIRTY's sentence {k}, " + ("word for word" if same else quote(k)) + tail)
    else:
        u = f", used from its sentence {used_from[n]}" if n in used_from else ""
        o.append(f"a name no sentence of Exhibit THIRTY names{u}")
    # wrapping back
    if holes:
        w = "open at " + "; ".join(dict.fromkeys(h[1] for h in holes))
    else:
        if nexts and priors:
            w = f"{listing(nexts)} thread{'s' if len(nexts) == 1 else ''} back through it to {listing(priors)}: closed"
        elif nexts:
            w = f"{listing(nexts)} thread back to it, the origin: closed"
        else:
            w = f"the aim threads back through it to {listing(priors)}: closed"
    ten = "none: a living 0" if not holes else TEN.get(n, "a hole, its one of the ten open")
    out.append("| Back, prior | Inward, now | Forward, next | Outward, same and across | Wrapping back, along | The ten |")
    out.append("| --- | --- | --- | --- | --- | --- |")
    out.append("| " + " | ".join("; ".join(x) for x in (b, i, f, o)) + f" | {w} | {ten} |")
    if resting[n]:
        out.append("")
        out.append("Of Exhibit THIRTY, resting on the lines to this one, marked: "
                   + "; ".join(f"{k}, {quote(k)}" + (f", {TEN_OF_A_SENTENCE[k]}" if k in TEN_OF_A_SENTENCE else "") for k in resting[n]))
    out.append("")
sys.stdout.write(HEAD.replace("{STABLE_FORM}", STABLE_FORM) + "\n".join(out)
                 + FOOT.replace("{unmarked}", " ".join(f"{n}, {LABEL[n]}." for n in unmarked)).replace("{RIGORIZER}", RIGORIZER))
sys.stderr.write(f"unmarked {unmarked}\nmarked {marked}\n")
