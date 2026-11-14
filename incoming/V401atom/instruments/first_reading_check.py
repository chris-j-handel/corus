"""v401atom's first reading: each droplet of the four gatherings having a word of the non-living scale has one line. All or none.

Reads the four gatherings of a gathering-value folder, as v401mgr's placing_check.py reads them, by the same words of
the non-living scale; and the reading's page. The reading is of `main` at c40e680: run it with that folder.
Run: python3 incoming/V401atom/instruments/first_reading_check.py <gathering-value folder> incoming/V401atom/The_First_Reading_of_the_Gatherings_Droplets.md incoming/V401atom/The_Value_Droplets.md
"""
import re, sys, os
GV, PAGE, SEQ = sys.argv[1], sys.argv[2], sys.argv[3]
SCALE = re.compile(r'atom carbon|\bcarbon\b|\bvault\b|non-living|bump connector|fracture|\bshear|lattice|\bshard\b', re.I)
FULL = {"Natural_Intelligence": "Natural Intelligence", "Natural_Resolver": "Exhibit ONE Natural Resolver",
        "Natural_Naming": "Exhibit TWENTY Natural Naming", "Co-Chaining_Logic_Registry": "Exhibit THIRTY Co-Chaining Logic Registry"}
def first(t):
    t = re.sub(r'[*`\\_"]', '', t); t = re.sub(r'\s+', ' ', t).strip()
    w = t.split(); return " ".join(w[:11]) + (" …" if len(w) > 11 else "")
want = []
for t in FULL:
    section, n = '', 0
    for line in open(os.path.join(GV, t + ".md"), encoding="utf-8").read().split("\n"):
        h = re.match(r'^#{2,3} (.+)$', line)
        if h:
            section, n = h.group(1).strip(), 0; continue
        m = re.match(r'^- \*\*([^*]+)\*\* · (.*)$', line)
        if not m:
            continue
        n += 1
        if SCALE.search(m.group(2)):
            want.append((FULL[t] + " · " + section, str(n), first(m.group(2))))
page = open(PAGE, encoding="utf-8").read()
have = []; head = None
for line in page.split("\n"):
    h = re.match(r'^## (.+)$', line)
    if h:
        head = h.group(1).strip(); continue
    m = re.match(r'^\| (\d+) \| [^|]+ \| ([^|]+) \| \*(whole|parts|beyond)\* \| ([^|]*) \| ([^|]*) \|$', line)
    if m:
        have.append((head, m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip()))
print("droplets of the four gatherings having a word of the non-living scale:", len(want))
print("lines of the reading:", len(have))
print("each droplet has one line, by its gathering, its section, its number and its first words, and no line is of no droplet:",
      sorted(want) == sorted((a, b, c) for a, b, c, _r, _s in have))
seq = open(SEQ, encoding="utf-8").read()
nums = {int(n) for n in re.findall(r"^(\d+)\. ", seq, re.M)}
ok = True
for _a, _b, _c, r, sents in have:
    got = [int(x) for x in re.findall(r"\d+", sents)]
    ok = ok and all(x in nums for x in got) and ((r == "beyond") == (not got and "part L" not in sents))
print("each sentence a line names is a sentence of the sequence; each whole and each parting names one or more, and each beyond names none:", ok)
import collections
print("readings:", dict(collections.Counter(r for *_x, r, _s in have)))
