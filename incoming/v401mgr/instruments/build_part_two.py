"""build_part_two · v401mgr · 14 Nov
Part two, a podal and no less: each rule is living words and their next words, word for word.
It reads the living files and changes none. It says each rule's places by file, and that no *17 less* or *9 less* is after the rules, in each file it has rules for.
Usage: python3 -I build_part_two.py <the set's root> [each]
"""
import sys, re
R = sys.argv[1]; EACH = len(sys.argv) > 2
P16, P8 = "podal within 1 to 16", "podal within 1 to 8"
rules = [
 ("- *9 less*: podal within 1 to 8, ", "- *Its "+P8+"*: "),
 ("- *17 less*: podal within 1 to 16, ", "- *Its "+P16+"*: "),
 ("  - *9 less: 9 − n*: ", "  - *Its "+P8+"*: "),
 ("  - *17 less: 17 − n*: ", "  - *Its "+P16+"*: "),
 ("going 17 less first from ", "going by a "+P16+" first from "),
 ("Each goes two folds in turn, 17 less and a move of 8", "Each goes two folds in turn, a "+P16+" and a move of 8"),
 ("8 down (n − 8) or 17 less (17 − n).", "8 down (n − 8) or a "+P16+" (17 − n)."),
 ("**Two moves, 9 less.**", "**Two moves, a "+P8+".**"),
 ("to its 9 less. Its 9 less is a name across", "to its "+P8+". Its "+P8+" is a name across"),
 ("Each name and its 9 less:", "Each name and its "+P8+":"),
 ("with 8 up, 9 less and 17 less.", "with 8 up, its "+P8+" and its "+P16+"."),
 ("move 8 up, 4 down, 17 less, 4 down, 8 up and 17 less,", "move 8 up, 4 down, a "+P16+", 4 down, 8 up and a "+P16+","),
 ("4 up, 4 down or 17 less", "4 up, 4 down or a "+P16),
 ("17 less, podal within 1 to 16; and 9 less, podal within 1 to 8, two together.", "a "+P16+"; and a "+P8+", two together."),
 ("each time with 17 less, podal within 1 to 16.", "each time with a "+P16+"."),
 ("17 less exchanges now and next.", "The "+P16+" exchanges now and next."),
 ("9 less within a self's span, 1 to 8.", "the podal within a self's span, 1 to 8."),
]
files = {"Exhibit ONE Natural Resolver": "Exhibit_ONE_Natural_Resolver_v401mgr.md", "Natural Intelligence": "Natural_Intelligence_v401mgr.md"}
pat = re.compile(r"\b(17|9) less\b")
rows = []; total = {}
for name, f in files.items():
    t = open(R + "/" + f).read(); before = len(pat.findall(t)); n_rules = 0
    for old, new in rules:
        c = t.count(old)
        if c:
            rows.append((name, old, new, c, old.count(" less")))
            n_rules += c * len(pat.findall(old))
            if EACH:
                for i, l in enumerate(open(R + "/" + f).read().split("\n"), 1):
                    if old in l: print(f"{name} · line {i} · {old.strip()} → {new.strip()}", file=sys.stderr)
        t = t.replace(old, new)
    left = pat.findall(t)
    assert not left, (name, len(left))
    assert n_rules == before, (name, n_rules, before)
    total[name] = before
print("| The living file | The living words | The next words | Places |\n|---|---|---|---|")
for name, old, new, c, _ in rows:
    print(f"| {name} | {old.strip().replace('|','\\|')} | {new.strip().replace('|','\\|')} | {c} |")
print()
for name in total: print(f"**{name}:** each place of *17 less* and of *9 less* has its next words; none is after them.")
print("places: " + ", ".join(f"{k} {v}" for k, v in total.items()), file=sys.stderr)
