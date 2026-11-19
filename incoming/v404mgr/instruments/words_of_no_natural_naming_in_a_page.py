#!/usr/bin/env python3
"""Words both partners named as no natural naming: their places in a page.

Usage:  python3 -I words_of_no_natural_naming_in_a_page.py PAGE [PAGE ...]
        python3 -I words_of_no_natural_naming_in_a_page.py --set ROOT

With pages, each place of a listed word is printed with its line, a place
inside a quotation in italics passed over: a living sentence quoted as it is
keeps its own words. With --set, the places are sized over the living files
of ROOT, with the chain and Exhibit ONE apart.

The list is the page Words_of_no_natural_naming_with_their_natural_naming.md
beside this instrument's folder; a word enters it by an is-not of both
partners alone. It sizes a pass and decides nothing.
"""
import glob
import os
import re
import sys

WORDS = [
    ("sharing", r"\bshar(?:ing|ings|e|es|ed)\b"),
    ("empty", r"\bempty\b"),
    ("improving, as a name of resolving", r"\bimprov(?:ing|e|es|ed)\b"),
    ("first", r"\bfirst\b"),
    ("each", r"\beach\b"),
    ("changing", r"\bchang(?:ing|e|es|ed)\b"),
    ("advancing", r"\badvanc(?:ing|e|es|ed)\b"),
    ("exactly", r"\bexactly\b"),
    ("ring", r"\brings?\b"),
    ("zone", r"\bzones?\b"),
    ("warning, wrapper", r"\b(?:warnings?|wrappers?)\b"),
    ("is with no, a negation", r"\b(?:is|are) (?:then )?with no\b"),
    ("joint", r"\bjoint\b"),
    ("meeting", r"\bmeet(?:ing|ings|s)?\b"),
    ("within", r"\bwithin\b"),
    ("inside", r"\binside\b"),
    ("reading", r"\bread(?:ing|s)?\b"),
]


def without_quotations(line):
    """A line with each quotation in italics taken out."""
    return re.sub(r"(?<!\*)\*(?!\*)[^*\n]{3,}?(?<!\*)\*(?!\*)", " ", line)


def page(path):
    found = 0
    in_code = False
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        bare = without_quotations(line)
        for name, pat in WORDS:
            for m in re.finditer(pat, bare, flags=re.I):
                found += 1
                a = max(0, m.start() - 40)
                print(f"  {path}:{n}: {name}: …{bare[a:m.end() + 30].strip()}…")
    return found


def whole_set(root):
    files = [f for f in sorted(glob.glob(os.path.join(root, "*.md")))
             if re.match(r"(Exhibit_|Natural_)", os.path.basename(f))]
    texts = {f: re.sub(r"```.*?```", "", open(f, encoding="utf-8").read(), flags=re.S) for f in files}
    chain = [t for f, t in texts.items() if "Exhibit_THIRTY_" in f]
    one = [t for f, t in texts.items() if "Exhibit_ONE_" in f]
    print(f"{len(files)} living files")
    for name, pat in WORDS:
        n = sum(len(re.findall(pat, t, flags=re.I)) for t in texts.values())
        k = sum(1 for t in texts.values() if re.search(pat, t, flags=re.I))
        c = sum(len(re.findall(pat, t, flags=re.I)) for t in chain)
        o = sum(len(re.findall(pat, t, flags=re.I)) for t in one)
        print(f"  {name:36s} {n:6d} places in {k:2d} files · the chain {c:5d} · Exhibit ONE {o:4d}")


def main(argv):
    if len(argv) >= 3 and argv[1] == "--set":
        whole_set(argv[2])
        return 0
    if len(argv) < 2:
        print(__doc__)
        return 2
    total = sum(page(p) for p in argv[1:])
    print(f"{total} places of a word of no natural naming, quotations in italics passed over")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
