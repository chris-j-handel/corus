"""v401atom's sequence, each sentence by its place in Exhibit THIRTY's own order: after the step adding the last name it uses.

Reads the sequence's page and the living file, and changes none. It decides no place: a name used is read by its words only.
Run: python3 incoming/V401atom/instruments/sequence_by_registry_order.py incoming/V401atom/The_Value_Droplets.md Exhibit_THIRTY_Co-Chaining_Logic_Registry_v401mgr.md
"""
import re, sys, collections
t = open(sys.argv[1], encoding="utf-8").read()
body = t[t.index("## A Parity"):t.index("## L Meeting")]
S = [(int(n), re.sub(r"\[[\d, ]+\]|\*[^*]*\*|`[^`]*`", " ", x)) for n, x in re.findall(r"^(\d+)\. (.*)$", body, re.M)]
L = open(sys.argv[2], encoding="utf-8").read().split("\n")
steps, group = [], None
for i, l in enumerate(L):
    h = re.match(r'^## (\d+) ', l)
    if h:
        group = int(h.group(1)); continue
    m = re.match(r'^(\d+)\. (.*)$', l)
    if m and group:
        j = i + 1
        while not L[j].strip():
            j += 1
        a = re.match(r'^\s+\*Adding: (.*?)\.?\*\s*$', L[j])
        steps.append((int(m.group(1)), group, m.group(2), a.group(1) if a else ""))
names = {}
for n, g, s, a in steps:
    for b in re.findall(r'\*\*([^*]+)\*\*', s):
        names.setdefault(b.lower(), (n, g))
for n, g, s, a in steps:
    first = re.sub(r'^(a|an|the|each|one)\s+', '', re.split(r'[,;:]', a)[0].strip(), flags=re.I).strip().lower()
    if first and len(first) > 2 and not first.isdigit():
        names.setdefault(first, (n, g))
pat = {k: re.compile(r'(?<![A-Za-z0-9-])' + re.escape(k) + r's?(?![A-Za-z0-9-])', re.I) for k in names}
by_group, none, rows = collections.Counter(), [], []
for n, x in S:
    used = {k: v for k, v in names.items() if pat[k].search(x)}
    if not used:
        none.append(n); rows.append(f"  {n} · no name of the registry's"); continue
    k = max(used, key=lambda k: used[k][0]); st, g = used[k]
    by_group[g] += 1
    rows.append(f"  {n} · after step {st}, group {g} · its last name: {k}")
print("the sequence's sentences:", len(S), "· the registry's names, by bold and by an Adding line's first words:", len(names))
print("1 sentences having one of the registry's names or more:", len(S) - len(none), "· having none:", none)
print("2 sentences by the group of the step adding their last name: " + ", ".join(f"group {g}: {by_group[g]}" for g in sorted(by_group)))
new = ["atom", "bump", "fold", "cone", "fracture", "dormancy", "snippet", "all-parity", "me-parity", "other-than", "same-as", "corner", "birthing", "resonating"]
print("3 names of the sequence, and the registry's step adding each:", ", ".join(f"{w}: {names[w][0] if w in names else 'none'}" for w in new))
print()
print("Each sentence, its place by its last name:")
print("\n".join(rows))
