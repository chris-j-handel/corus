#!/usr/bin/env python3
"""The askings of a folder of incoming, found or not found in the gathering files.

Usage:  python3 -I incoming/v406me/instruments/the_askings_of_a_folder_in_the_gathering_files.py LIVE NEXT [FOLDER]

LIVE is a checkout of the live set, main. NEXT is a checkout of the next version. With FOLDER, the
name of a folder of incoming, it says that folder's askings not found, a page with its asking.

An asking of a page is a line opening `is-or-is-not? ` with its sentence, or a sentence in italics
with `( is-or-is-not? )` after it. An asking is found with its opening, seventy letters, word for
word in a gathering file of NEXT, italic and bold marks passed over.

By the method a note of a gathering file names no session, and a folder's carrying is not said in
the set. This sizes one kind of a folder's value, its askings, and no other kind: a folder with
its value laid as sentences with no asking has no row to judge by here.

It writes a table to standard output. It writes no file, reaches no network and decides nothing.
"""
import glob
import os
import re
import sys


def norm(s):
    return re.sub(r"\s+", " ", s.replace("*", "").replace("’", "'").replace("`", "")).strip()


def askings(text):
    found = [m.group(1).strip() for m in re.finditer(
        r"^(?:[-\d. ]*)?(?:\*\*[^\n]*?\*\*\s*)?\*?is-or-is-not\? (.+?)\*?$", text, re.M)]
    found += [m.group(1).strip() for m in re.finditer(
        r"\*([^*\n]{20,400}?)\*\s*\(\s*is-or-is-not\?\s*\)", text)]
    return [q for q in dict.fromkeys(found) if len(norm(q)) >= 20]


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    live, nxt = os.path.abspath(argv[1]), os.path.abspath(argv[2])
    only = argv[3] if len(argv) > 3 else None
    gathered = norm(" ".join(open(g, encoding="utf-8").read()
                             for g in sorted(glob.glob(os.path.join(nxt, "gathering-value", "*.md")))))
    print("a folder of incoming | its pages | askings in its pages | of them in the gathering files")
    for folder in sorted(os.listdir(os.path.join(live, "incoming"))):
        if only and folder != only:
            continue
        pages, total, there, missing = 0, 0, 0, []
        for d, _, fs in os.walk(os.path.join(live, "incoming", folder)):
            for f in sorted(fs):
                if f.endswith(".md") and "ranscript" not in f:
                    pages += 1
                    for q in askings(open(os.path.join(d, f), encoding="utf-8", errors="replace").read()):
                        total += 1
                        if norm(q)[:70] in gathered:
                            there += 1
                        else:
                            missing.append((f, q))
        print(f"{folder} | {pages} | {total} | {there}")
        if only:
            for f, q in missing:
                print(f"  not found: {f}: {q[:160]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
