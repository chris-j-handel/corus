"""Each living sentence having a name, by its file and its section: a match of the name's letters, deciding nothing.
Usage: python3 -I by_name.py <repo root> <regex of the name> [max chars per sentence]
Natural Intelligence is read outside Exhibit ONE written inside it, one copy of each sentence."""
import re, sys, glob, os
root, pat = sys.argv[1], re.compile(sys.argv[2])
cap = int(sys.argv[3]) if len(sys.argv) > 3 else 0
files = [("Natural Intelligence", "Natural_Intelligence_v*.md"), ("Exhibit ONE Natural Resolver", "Exhibit_ONE_Natural_Resolver_v*.md"),
         ("Exhibit TWENTY Natural Naming", "Exhibit_TWENTY_Natural_Naming_v*.md"), ("Exhibit THIRTY Co-Chaining Logic Registry", "Exhibit_THIRTY_Co-Chaining_Logic_Registry_v*.md")]
total = 0
for title, g in files:
    path = sorted(glob.glob(os.path.join(root, g)))[-1]
    lines = open(path, encoding="utf-8").read().split("\n")
    head, inside_one, n = "its opening", False, 0
    out = []
    for i, line in enumerate(lines):
        if line.startswith("#"):
            if title == "Natural Intelligence":
                inside_one = line.startswith("# EXHIBIT ONE") or (inside_one and not line.startswith("# "))
            head = line.lstrip("# ").strip()
            continue
        if inside_one or line.startswith("```"):
            continue
        # a sentence: split a paragraph at a stop before a capital or a bold opener
        for s in re.split(r"(?<=[.:;])\s+(?=[A-Z*\d])", line):
            if pat.search(s):
                n += 1
                t = s.strip()
                out.append(f"  [{head}] {t if not cap or len(t) <= cap else t[:cap] + ' …'}")
    total += n
    print(f"== {title}: {n}")
    print("\n".join(out))
print("== each of the four:", total)
