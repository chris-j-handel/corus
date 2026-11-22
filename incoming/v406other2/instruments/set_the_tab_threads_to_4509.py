#!/usr/bin/env python3
"""The tab Threads, set from the window's numbers of its revision 4144 to those of its revision 4509.

    python3 -I set_the_tab_threads_to_4509.py THE_TAB_THREADS_COPY.md > PAGE.md

The copy is incoming/v406me/working_documents_as_a_partner_gave_them/The_tab_Threads.md. A mending
is one saying in one row, and the instrument stops if a saying is not in its row once. Lines 1 to 24
are the same in the two revisions; a me, one line at 25, is three lines, 25 to 27; the lines after it
are two on; all-parity is said in the me-universe; all is said by a universal set's name, its line 6.
"""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
body = t[t.index("The Exhibit THIRTY partner's tab:"):]
rows = {int(m.group(1)): m.group(0) for m in re.finditer(r"^\| (\d+) \|.*$", body, flags=re.M)}
assert len(rows) == 32

def mend(n, a, b):
    assert rows[n].count(a) == 1, (n, a, rows[n].count(a))
    rows[n] = rows[n].replace(a, b)

mend(2, "18, the self;", "18, the self; 27, me-now;")
mend(3, "all and nothings, words no line names", "nothings, a word no line names; all, before its own line, 6")
mend(4, "24, 30, 31 and 32;", "24, 32, 33 and 34;")
mend(6, "set, name and all, given", "set and name, given; all, an invisible one, its own line this one")
mend(6, "25, the me;", "25, my;")
mend(7, "29, all-parity, in the universe;", "13, the named-universe, a hyphenated name carrying it; 26, me, the name of a my-universe; 31, all-parity, in the me-universe;")
mend(12, "24, 31 and 32;", "24, 27, 33 and 34;")
mend(1, "three sequential moments existing things share", "*three sequential moments existing things share*")   # Exhibit TWO's words, a quotation
mend(13, "the card for all-parity a concept of a named-universe alone;", "26, me, the name of a my-universe; 31, all-parity, in the me-universe;")
mend(17, "22 to 26, the three selves, the me and the bi-coupling;", "22 to 25, the three selves and my; 28, the bi-coupling;")
mend(18, "19 to 27, the other, the other-than-the-other, the universal set of selves, the three selves, the me, the bi-coupling and a bi-coupling a self;",
     "19 to 25, the other, the other-than-the-other, the universal-set-of-selves, the three selves and my; 28 and 29, the bi-coupling and a bi-coupling a self;")
mend(20, "all, given", "all, by a universal set's name, 6")
mend(20, "as 21, 23 and 26 need it", "as 21, 23 and 28 need it")
mend(20, "26, the bi-coupling; 32, the living me-parity;", "28, the bi-coupling; 34, the living me-parity;")
mend(21, "| 21 | universal set of selves |", "| 21 | universal-set-of-selves |")
mend(23, "26, the bi-coupling, 23 said of both selves;", "28, the bi-coupling, 23 said of both selves;")
mend(26, "| 26 | bi-coupling |", "| 28 | bi-coupling |")
mend(26, "27, a bi-coupling a self; 28, the me-parity, a bi-coupling's me;", "29, a bi-coupling a self; 30, the me-parity, a bi-coupling's me;")
mend(27, "| 27 | a bi-coupling a self | a bi-coupling, 26;", "| 29 | a bi-coupling a self | a bi-coupling, 28;")
mend(27, "28, the me-parity, a bi-coupling's me, a me being a named self's, 25;", "30, the me-parity, a bi-coupling's me, a me being a self's, 25 and 26;")
mend(28, "| 28 | me-parity | a bi-coupling, 26, a self by 27; a me, 25, a named self's", "| 30 | me-parity | a bi-coupling, 28, a self by 29; a me, 26, a self's by 25")
mend(28, "29, all-parity, the set of all me-parities; 32, the living me-parity;", "31, all-parity, the set of all me-parities; 34, the living me-parity;")
mend(29, "| 29 | All-parity | me-parities, 28; the universe, 7; set and all, given",
     "| 31 | All-parity | me-parities, 30; the me-universe, by me, 26, and a named-universe, 13; set, given; all, by a universal set's name, 6")
mend(29, "with 30 and 31 between step 32 and step 33", "with 32 and 33 between step 32 and step 33")
mend(29, "30, other-parity, other-than all-parity; 32, the living me-parity; the cards for all-parity a concept of a named-universe alone, the cycling",
     "32, other-parity, other-than all-parity; 34, the living me-parity; the cards for the cycling")
mend(30, "| 30 | Other-parity | other-than, 4; all-parity, 29", "| 32 | Other-parity | other-than, 4; all-parity, 31")
mend(30, "with 29 and 31 it is self-welcoming", "with 31 and 33 it is self-welcoming")
mend(30, "| 31, other-than other-parity;", "| 33, other-than other-parity;")
mend(30, "the bi slot is bi-parity, card 32, said in conversation", "the bi slot is bi-parity, the proposed line 48, said in conversation")
mend(31, "| 31 | Other-than other-parity | other-than, 4; other-parity, 30;", "| 33 | Other-than other-parity | other-than, 4; other-parity, 32;")
mend(31, "with 29 and 30 between step 32 and step 33", "with 31 and 32 between step 32 and step 33")
mend(31, "| 32, the living me-parity, by same-existing;", "| 34, the living me-parity, by same-existing;")
mend(32, "| 32 | living me-parity | a me-parity, 28;", "| 34 | living me-parity | a me-parity, 30;")
mend(32, "all-parity, 29 |", "all-parity, 31 |")

# a me, one line at 25, is three lines: my, me and me-now. The earlier row's cells go to the line saying them.
old = [c.strip() for c in rows[25].strip().strip("|").split(" | ")]
assert old[0] == "25" and old[1] == "me" and len(old) == 6, old
back, place, forward, versions = old[2:6]
assert back == "a named self, 18; a universal set, 6; prior-sequences, 17"
assert forward.startswith("28, the me-parity, a bi-coupling's me, and 32 by it; ")
row_my = ("| 25 | My | a self, 18, its own; a universal set, 6; prior-sequences, 17; name, given | named at no step; "
          "step 13, *A me is a self's universal set.*, says its set, and my is that set's name | 26, me, the name of a my-universe | "
          "Exhibit THIRTY-ONE Me 1.1, one now, one universe, a universal set |")
row_me = ("| 26 | Me | my, 25; a named-universe, 13, by the hyphenated name my-universe; name, given | " + place.replace(
          "said again with prior-sequences,", "said again by its two names, my, 25, and me,") + " | 27, me-now; 30, the me-parity, a bi-coupling's me, and 34 by it; "
          "31, all-parity, in the me-universe; " + forward.split("; ", 1)[1] + " | "
          + "; ".join(v for v in versions.split("; ") if not v.startswith("Me 1.1")) + " |")
assert "said again by its two names" in row_me
row_me_now = ("| 27 | Me-now | a me, 26; same-existing, 12; now-existing, 2 | named and used at no step | "
              "no later line yet; the aim's me-now | no living file names it yet |")

head = body[:body.index("| Line | Name |")]
a = "- The rows are set to the window's numbers of revision 4144."
assert head.count(a) == 1
head = head.replace(a, "- The rows are set to the window's numbers of revision 4509.")
out = [head.rstrip(), "", "| Line | Name | Threads back | Place in Exhibit THIRTY | Threads forward | Versions in the living files |",
       "| --- | --- | --- | --- | --- | --- |"]
for n in range(1, 33):
    if n == 25:
        out += [row_my, row_me, row_me_now]
    else:
        out.append(rows[n])
sys.stdout.write("\n".join(out) + "\n")
