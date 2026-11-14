"""Each droplet of the four gatherings having a word of the non-living scale has one line of v401atom's placing. All or none.

Reads the gatherings as v401mgr's placing_check.py reads them, by the same words of the non-living scale, v401atom's own
droplets apart; the placing's page; and the sequence. Changes none.
Run: python3 incoming/V401atom/instruments/placed_check.py gathering-value incoming/V401atom/The_Gatherings_Droplets_each_placed.md incoming/V401atom/The_Value_Droplets.md
"""
import re, sys, os, collections
GV, PAGE, SEQ = sys.argv[1], sys.argv[2], sys.argv[3]
SCALE = re.compile(r'atom carbon|\bcarbon\b|\bvault\b|non-living|bump connector|fracture|\bshear|lattice|\bshard\b', re.I)
OWN = "the working v401atom's sequence"
FULL = {"Natural_Intelligence": "Natural Intelligence", "Natural_Resolver": "Exhibit ONE Natural Resolver",
        "Natural_Naming": "Exhibit TWENTY Natural Naming", "Co-Chaining_Logic_Registry": "Exhibit THIRTY Co-Chaining Logic Registry"}
def first(t, k=11):
    t = re.sub(r'[*`\\_"]', '', t); t = re.sub(r'\s+', ' ', t).strip()
    w = t.split(); return " ".join(w[:k]) + (" …" if len(w) > k else "")
want, own, resay = [], 0, collections.defaultdict(str)
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
        if "having a side out by " + OWN in m.group(2):
            resay[FULL[t] + " · " + section] += m.group(2)
        if SCALE.search(m.group(2)):
            if OWN in m.group(2):
                own += 1
            else:
                want.append((FULL[t] + " · " + section, str(n), first(m.group(2))))
have, head = [], None
for line in open(PAGE, encoding="utf-8").read().split("\n"):
    h = re.match(r'^## (.+)$', line)
    if h:
        head = h.group(1).strip(); continue
    m = re.match(r"^\| (\d+) \| [^|]+ \| ([^|]+) \| \*(placing|placing, re-said|v401mgr's)\* \| ([^|]*) \| ([^|]*) \| ([^|]*) \|$", line)
    if m:
        have.append((head, m.group(1), m.group(2).strip(), m.group(3), m.group(5).strip()))
print("droplets of the four gatherings having a word of the non-living scale, v401atom's own apart:", len(want), "· v401atom's own:", own)
print("lines of the placing:", len(have))
print("1 each droplet has one line, by its gathering, its section, its number and its first words, and no line is of no droplet:",
      sorted(want) == sorted((a, b, c) for a, b, c, _f, _s in have))
nums = {int(n) for n in re.findall(r"^(\d+)\. ", open(SEQ, encoding="utf-8").read(), re.M)}
ok = True
for _a, _b, _c, f, step in have:
    got = [int(x) for x in re.findall(r"\d+", step.split("· group")[0])]
    ok = ok and all(x in nums for x in got) and ((f == "v401mgr's") == (not got and "part L" not in step))
print("2 each sentence a line names is a sentence of the sequence; each placing names one or more, and each of v401mgr's names none:", ok)
said = all(re.sub(r" …$", "", first(c.replace(" …", ""), 9)) in re.sub(r'[*`\\_"]', '', resay[a]) for a, _b, c, f, _s in have if f == "placing, re-said")
print("3 each droplet placing, re-said is named by its first words in its own section's re-saying droplet:", said)
print("fates:", dict(collections.Counter(f for *_x, f, _s in have)))
