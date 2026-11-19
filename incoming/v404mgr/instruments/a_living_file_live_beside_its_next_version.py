"""A living file as it is live beside the same file as it is in the next version, sentence beside sentence.

Reads one living file at two roots, the live set's and the next version's; executes; writes no file;
sizes nothing and decides nothing. It is for a snapshot a partner asks of a session: a living sentence
re-said, as it is live and as it is in the next version; a sentence away; a sentence new.

Use: python3 -I incoming/v404mgr/instruments/a_living_file_live_beside_its_next_version.py <live root> <next root> "<a living file's title>"

The is a re-said sentence is by is no part of a file: the session lays it beside the pair, from its own
record, a partner's is with its day and the session it was with, or no is yet.
"""
import difflib, os, re, sys


def find(root, title):
    stem = title.replace(" ", "_")
    for f in sorted(os.listdir(root)):
        if f.endswith(".md") and re.sub(r"_v\d+\w*\.md$", "", f).endswith(stem):
            if re.sub(r"_v\d+\w*\.md$", "", f) == stem or re.sub(r"^Exhibit_[A-Z-]+_", "", re.sub(r"_v\d+\w*\.md$", "", f)) == stem:
                return os.path.join(root, f)
    sys.exit("no living file of that title at " + root)


def lines(path):
    return [l.rstrip().rstrip("\\").rstrip() for l in open(path, encoding="utf-8").read().split("\n")]


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    live, nxt = lines(find(sys.argv[1], sys.argv[3])), lines(find(sys.argv[2], sys.argv[3]))
    part = ""
    sm = difflib.SequenceMatcher(None, live, nxt, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        for l in nxt[j1:j2] if tag == "equal" else []:
            if l.startswith("#"):
                part = l.lstrip("# ")
        if tag == "equal":
            continue
        a, b = [l for l in live[i1:i2] if l.strip()], [l for l in nxt[j1:j2] if l.strip()]
        for l in b:
            if l.startswith("#"):
                part = l.lstrip("# ")
        print("== with the part: " + (part or "the opening"))
        if tag == "replace" and len(a) == len(b):
            for x, y in zip(a, b):
                print("   as it is live:            " + x)
                print("   as it is in the next version: " + y)
        else:
            for x in a:
                print("   away, as it is live:      " + x)
            for y in b:
                print("   new in the next version:  " + y)


main()
