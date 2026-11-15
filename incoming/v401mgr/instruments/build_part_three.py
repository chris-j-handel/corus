"""build_part_three · v401mgr · 14 Nov
Part three, a moment and no momentary: the noun *momentary*, *momentaries*, by its natural name, *moment*, *moments*.
A describing word, *momentary* before the thing it is of, and a compound by a hyphen before it, are as they are.
It reads the living files and changes none, but by its second word: `rehearse` writes the next words into a copy of the set given as its third word.
Usage: python3 -I build_part_three.py <the set's root> [rehearse <a copy's root>]
"""
import sys, re, glob, os
R = sys.argv[1]
DESCRIBING = {"stable-forming", "stable", "now-existing", "existing", "not-changing", "changing", "universe", "sequencing"}
pat = re.compile(r"(?<![\w-])(momentar(?:y|ies))\b( (\w[\w'-]*))?", re.I)
pat_any = re.compile(r"\bmomentar(?:y|ies)\b", re.I)
def next_word(w):
    low = w.lower(); new = "moments" if low.endswith("ies") else "moment"
    return new.capitalize() if w[0].isupper() else new
def transform(t):
    n = [0]; asis = [0]; mention = [0]
    def rep(m):
        w = m.group(1); nxt = (m.group(3) or "").lower()
        s, e = m.start(1), m.end(1)
        if s > 0 and t[s-1] == "*" and e < len(t) and t[e] == "*":
            mention[0] += 1; return m.group(0)
        if w.lower() == "momentary" and nxt in DESCRIBING:
            asis[0] += 1; return m.group(0)
        n[0] += 1; return next_word(w) + (m.group(2) or "")
    new = pat.sub(rep, t)
    return new, n[0], asis[0] + mention[0]
rows = []; tot = 0; tot_asis = 0; tot_comp = 0
for f in sorted(glob.glob(R + "/*.md")):
    t = open(f).read(); allm = len(pat_any.findall(t))
    if not allm: continue
    new, n, asis = transform(t)
    comp = allm - n - asis   # a compound by a hyphen before it
    assert len(pat_any.findall(new)) == asis + comp, f
    rows.append((os.path.basename(f), n, asis, comp)); tot += n; tot_asis += asis; tot_comp += comp
    if len(sys.argv) > 3 and sys.argv[2] == "rehearse":
        open(sys.argv[3] + "/" + os.path.basename(f), "w").write(new)
print("| The living file | The noun, re-said | A describing word or the word named, as it is | A compound, as it is |\n|---|---|---|---|")
for f, n, a, c in rows: print(f"| {f[:-3].replace('_', ' ')} | {n} | {a} | {c} |")
print(f"| **Each living file having it, {len(rows)}** | **{tot}** | **{tot_asis}** | **{tot_comp}** |")
if len(sys.argv) > 3 and sys.argv[2] == "rehearse":
    C = sys.argv[3]; gh = gq = 0
    for g in sorted(glob.glob(C + "/gathering-value/*.md")):
        L = open(g).read().split("\n"); out = []
        for l in L:
            if l.startswith("#"):
                new, n, _ = transform(l); gh += n; out.append(new)
            elif l.startswith("- **Possible incohering** · \""):
                e = l.find("\" →")
                if e > 0:
                    new, n, _ = transform(l[:e]); gq += n; out.append(new + l[e:])
                else: out.append(l)
            else: out.append(l)
        open(g, "w").write("\n".join(out))
    print(f"rehearsed in the copy: gatherings' headings {gh}, gatherings' quoted living words {gq}", file=sys.stderr)
