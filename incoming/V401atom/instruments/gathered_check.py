"""v401atom's sequence in its homes' gatherings: each sentence once, word for word; each instrument one droplet. All or none.

Reads the sequence's page and the gatherings, and changes none.
Run: python3 incoming/V401atom/instruments/gathered_check.py incoming/V401atom/The_Value_Droplets.md gathering-value
"""
import re, sys, os
PAGE, GV = sys.argv[1], sys.argv[2]
t = open(PAGE, encoding="utf-8").read()
body = t[t.index("## A Parity"):t.index("## L Meeting")]
S = {int(n): x.strip() for n, x in re.findall(r"^(\d+)\. (.*)$", body, re.M)}
norm = lambda s: re.sub(r"\s+", " ", s.replace("*", "")).strip()

def items(title):
    out, sec = [], ""
    for l in open(os.path.join(GV, title + ".md"), encoding="utf-8").read().split("\n"):
        h = re.match(r"^#{2,3} (.+)$", l)
        if h:
            sec = h.group(1).strip()
        elif l.startswith("- ") and "v401atom" in l and "The_Value_Droplets.md" in l and "having a side out" not in l:
            out.append((sec, l))
    return out

reg = items("Co-Chaining_Logic_Registry")
print("the sequence's sentences:", len(S), "· its droplets at the registry's gathering:", len(reg))
once, where = True, {}
for n, x in S.items():
    key = norm(f"{n} · {x}")
    got = [sec for sec, l in reg if key in norm(l)]
    once = once and len(got) == 1
    where.setdefault(got[0] if got else "none", []).append(n)
print("1 each sentence is in one droplet and no second, word for word, by its number:", once)
print("  by its group:")
seen = []
for sec, _l in reg:
    if sec not in seen:
        seen.append(sec)
        ns = sorted(where.get(sec, []))
        runs, a = [], None
        for n in ns:
            if a is None or n != b + 1:
                if a is not None:
                    runs.append((a, b))
                a = n
            b = n
        runs.append((a, b))
        print(f"    {sec[:60]} · " + ", ".join(f"{a} to {b}" for a, b in runs))

named = sorted(set(re.findall(r"`(?:instruments/)?(\w+_check)\.py`", body)))
nr = items("Natural_Resolver")
got = {}
for sec, l in nr:
    m = re.search(r"instruments/(\w+)\.py", l)
    if m:
        got.setdefault(m.group(1), []).append((sec, l))
print("2 instruments the sequence names:", len(named), "· its droplets at Exhibit ONE's gathering:", len(nr))
print("  each instrument named has one droplet and no second:", all(len(got.get(i, [])) == 1 for i in named),
      "· each droplet's instrument is one the sequence names:", all(i in named for i in got))
ok3, ok4 = True, True
for inst, v in got.items():
    for sec, l in v:
        tail = l.split("The_Value_Droplets.md`:")[-1]
        ns = []
        for a, b in re.findall(r"(\d+)(?: to (\d+))?", tail.split(", each at the registry's")[0]):
            ns += list(range(int(a), int(b) + 1)) if b else [int(a)]
        ok3 = ok3 and bool(ns) and all(n in S for n in ns)
        # each sentence a droplet names has that instrument, or is executed
        ok4 = ok4 and any(inst in S[n] for n in ns)
print("3 each sentence a droplet names is a sentence of the sequence:", ok3,
      "· and one or more of them names the droplet's instrument:", ok4)
other = [(g, s) for g in ("Natural_Naming", "Natural_Intelligence", "Geodesic_Improving_Method") for s, _l in items(g)]
print("4 its droplets at the namings' gathering, Natural Intelligence's and the method's:", len(other))
for g, s in other:
    print(f"    {g.replace('_', ' ')} · {s[:70]}")
