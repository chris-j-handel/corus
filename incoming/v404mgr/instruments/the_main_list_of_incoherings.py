#!/usr/bin/env python3
"""The main list of incoherings, in the open: one line for one note of a gathering file.

Usage:  python3 -I the_main_list_of_incoherings.py ROOT          a sizing, by gathering file and by state
        python3 -I the_main_list_of_incoherings.py ROOT csv      the list, written to standard output

ROOT is a folder with gathering-value/*.md, the next version's copy for the list as it is worked.
A line of the list is a note opening `- **Possible incohering**`, or a note with an asking, `is-or-is-not? `.
An asking is `is-or-is-not? ` and the sentence after it; the three named as a word, an article or a list
before it, as *An is-or-is-not? is*, or a word of relation after it, as *is-or-is-not? as a doubt*, is
no asking. With two askings in a note its open sentence is the newer, the later one.

A line's name is its gathering file's title and six letters of its note's opening: it goes on the same
while the note's opening goes on the same, a suggesting laid after it, and a session names a line by it
at the thread.

A line's state, by the note's own words:
  answered            an is or an is-not of both partners, or an answering or a resolving, is said in it
  an open sentence    an asking is in it, `is-or-is-not? `, and no answer
  a suggesting in it  a suggesting, a candidate or a re-saying is in it, and no asking
  open                a possible incohering with none of these

It writes no file and decides nothing: a line is settled by both partners' is alone.
"""
import csv
import glob
import hashlib
import os
import re
import sys

ANSWERED = re.compile(r"An is, both partners'|An is, of both partners|An is-not, both partners'|An is-not, of both partners|"
                      r"Two is-nots, both partners'|Answered by|Answered, |Resolved by|Resolved, by|is resolved by|An is-not, by a saying")
SUGGESTING = re.compile(r"A suggesting|a suggesting|A candidate|a candidate|A re-saying|a re-saying|Its re-saying")
ASKING = re.compile(r"is-or-is-not\? (?=\S)")
NAMING_THE_THREE = re.compile(r"is-or-is-not\? (?:or |and |with |of |an |is-not|as |in |is the |has |resolves |goes |for |by )")
THE_THREE_AS_A_WORD = re.compile(r"\b(?:[Aa]n|[Tt]he|[Ee]ach|[Oo]ne|[Aa]|gathered|or|and|its|an other)\s$")


def askings(line):
    """The askings of a note: the three named as a word, before it or after it, passed over."""
    return [a for a in ASKING.finditer(line)
            if not NAMING_THE_THREE.match(line, a.start())
            and not THE_THREE_AS_A_WORD.search(line[max(0, a.start() - 14):a.start()])]


def lines_of(root):
    for path in sorted(glob.glob(os.path.join(root, "gathering-value", "*.md"))):
        title = os.path.basename(path)[:-3].replace("_", " ")
        part = ""
        for line in open(path, encoding="utf-8").read().split("\n"):
            m = re.match(r"#{2,3} (.+)", line)
            if m:
                part = m.group(1)
                continue
            if not line.startswith("- "):
                continue
            possible = line.startswith("- **Possible incohering**")
            asks = askings(line)
            if not possible and not asks:
                continue
            body = re.sub(r"^- \*\*[^*]+\*\* · ", "", line)
            q = re.match(r'"(.+?)" → (.*)$', body) if possible else None
            beside = q.group(1) if q else ""
            rest = q.group(2) if q else body
            ask = ""
            if asks:
                tail = line[asks[-1].end():]
                ask = re.split(r"(?<=[.])\s+(?=Its is |Why it is open|Its is-not |[A-Z])", tail, maxsplit=1)[0].strip()
            if ANSWERED.search(line):
                state = "answered"
            elif asks:
                state = "an open sentence"
            elif SUGGESTING.search(line):
                state = "a suggesting in it"
            else:
                state = "open"
            opening = (beside + " → " + rest[:120]) if q else body[:200]
            name = title + " " + hashlib.sha1(opening.encode("utf-8")).hexdigest()[:6]
            kind = "possible incohering" if possible else "an asking"
            yield [name, title, part, kind, beside[:300], ask[:260], rest[:220], state]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    rows = list(lines_of(argv[1]))
    seen = {}
    for r in rows:                      # two notes with one same opening: the second and on named with a number
        seen[r[0]] = seen.get(r[0], 0) + 1
        if seen[r[0]] > 1:
            r[0] = f"{r[0]}-{seen[r[0]]}"
    if len(argv) > 2 and argv[2] == "csv":
        w = csv.writer(sys.stdout, lineterminator="\n")
        w.writerow(["a line's name", "its gathering file", "the part it is with", "its kind",
                    "the living sentence it is beside", "its open sentence, is-or-is-not?",
                    "what is with it, its opening", "its state"])
        w.writerows(rows)
        return 0
    by_file, by_state = {}, {}
    for r in rows:
        by_file.setdefault(r[1], {}).setdefault(r[7], 0)
        by_file[r[1]][r[7]] += 1
        by_state[r[7]] = by_state.get(r[7], 0) + 1
    print(f"{len(rows)} lines of {len(by_file)} gathering files: " + ", ".join(f"{k} {v}" for k, v in sorted(by_state.items())))
    for title, c in sorted(by_file.items(), key=lambda x: -sum(x[1].values())):
        print(f"  {title[:40]:40s} {sum(c.values()):5d}   " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
