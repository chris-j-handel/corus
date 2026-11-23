"""The log of the aims beside the managing table: a thing of value with the aims it is a home of,
and an aim with the things of value it names. It goes through the two, and writes nothing.

    python3 -I incoming/v406me/instruments/the_log_of_the_aims_beside_the_managing_table.py LIVE NEXT
    python3 -I incoming/v406me/instruments/the_log_of_the_aims_beside_the_managing_table.py LIVE NEXT aims > The_aims.csv

LIVE is the live set's root, NEXT the next version's root. With aims it gives the working document's sheet
of the aims, a row an aim, and no other line: the sheet is made from the log, and the set has no copy of it.
The log is NEXT's Exhibit FOURTEEN, its part 2, a row an aim, its column Home.
The table is LIVE's incoming/v406me/The_managing_table_of_the_living_expedition.csv, a row a thing of value.
An aim names a thing as a home by its Home having the thing's title, its exhibit number, or, for a folder, its path.
An aim's state: no living home, its Home a gathering note or a folder alone; at rest, a home in a living thing's
own part and its Possibling with none; open, a home in a living thing's own part and its Possibling with some.
"""
import csv, glob, os, re, sys, collections

if len(sys.argv) < 3:
    print(__doc__)
    sys.exit(0)
live, nxt = sys.argv[1], sys.argv[2]
LOG = glob.glob(os.path.join(nxt, "Exhibit_FOURTEEN_*.md"))[0]
TAB = os.path.join(live, "incoming/v406me/The_managing_table_of_the_living_expedition.csv")
rows = list(csv.DictReader(open(TAB, encoding="utf-8")))
standing = {r["The thing"]: r["Its standing"] for r in rows}

band, aims = None, []
for l in open(LOG, encoding="utf-8"):
    m = re.match(r"^### 2\.(\d+) (.*)$", l)
    if m:
        band = (int(m.group(1)), m.group(2).strip())
    elif l.startswith("## ") and not l.startswith("## 2 "):
        band = None
    elif band and l.startswith("| **"):
        c = [x.strip() for x in l.strip().strip("|").split(" | ")]
        name = re.match(r"\*\*(.*?)\*\*", c[0]).group(1).rstrip(".")
        said = re.match(r"\*\*.*?\*\*\s*(.*)$", c[0]).group(1).strip()
        aims.append(dict(n=len(aims) + 1, band=band, name=name, said=said, home=c[2], obs=c[3], pos=c[4], dis=c[5]))

def ways(t):
    short = re.sub(r"^Exhibit [A-Z-]+ ", "", t)
    p = [re.escape(short)]
    m = re.match(r"^(Exhibit [A-Z-]+) ", t)
    if m:
        p.append(re.escape(m.group(1)) + r"(?![A-Z-])")
    return p
own = {
    "The window of the opening": [r"The window"],
    "corus.me": [r"corus\.me", r"home page", r"repository's front page"],
    "Start here": [r"start page"],
    "Exhibit FOURTEEN Natural Destinies": [r"[Tt]his exhibit", r"Natural Destinies"],
    "Exhibit THIRTY-ONE Me": [r"(?<![A-Za-z-])Me (?=\d)", r"Exhibit THIRTY-ONE"],
    "Natural Intelligence": [r"Natural Intelligence(?! Corus)"],
}
things = [r["The thing"] for r in rows]
of, under = {}, collections.defaultdict(list)
for a in aims:
    hs = []
    for t in things:
        ps = own.get(t) or ([re.escape(t) + r"(?![A-Za-z0-9-])"] if t.startswith("incoming/") else ways(t) if next(r["Its kind"] for r in rows if r["The thing"] == t).startswith("a living file") else None)
        if ps and any(re.search(p, a["home"]) for p in ps):
            hs.append(t)
    of[a["n"]] = hs
    for t in hs:
        under[t].append(a["n"])

def in_a_living_file(a):
    """a home at a living thing's own section, step, line or page: a part of its Home that is no gathering note and no folder"""
    for part in a["home"].split(";"):
        part = re.split(r",? and its gathering", part)[0]
        if "start page" in part or ("gathering" not in part and "incoming/" not in part):
            return True
    return False

def state(a):
    if not in_a_living_file(a):
        return "no living home"
    return "at rest" if a["pos"] in ("—", "") else "open"

origin = {"The window of the opening": "v406all2", "A complete co-chaining": "v406other2", "Seventeen names in four four-cyclings": "v406all2-2",
          "Word, number and illustrating, one thing three ways": "v406geodesic2", "Spirals and tori of selves": "v407primes",
          "A prime ladder of societies": "v407primes", "Value brought home": "v406me", "A destiny, next living possibling ahead": "v406aiming"}

if len(sys.argv) > 3 and sys.argv[3] == "aims":
    out = csv.writer(sys.stdout, lineterminator="\n")
    out.writerow(["Aim", "Its band", "The aim", "Its state", "Its things of value", "Sessions at it", "The window says", "Open on its path",
                  "Ahead, no line names it", "Its home, as the log has it", "Its sentence"])
    bare = lambda t: t.replace("*", "").strip()
    for a in aims:
        out.writerow([a["n"], a["band"][1], a["name"], state(a), "; ".join(of[a["n"]]), origin.get(a["name"], ""), bare(a["obs"]), bare(a["pos"]),
                      bare(a["dis"]), bare(a["home"]), a["said"]])
    sys.exit(0)

print(f"The log: {len(aims)} aims in {len(set(a['band'] for a in aims))} bands. The table: {len(rows)} things of value.")
print()
print("1. An aim with the things it names a home")
k = collections.Counter(len(v) for v in of.values())
print("   an aim naming 0, 1, 2, 3 and more things of the table:", k[0], k[1], k[2], sum(v for n, v in k.items() if n > 2))
note = [a for a in aims if not in_a_living_file(a)]
print(f"   aims with a home in a living file's own part: {len(aims) - len(note)}; with a home in a gathering note or a folder alone: {len(note)}")
for a in note:
    print(f"      {a['n']:3d}  2.{a['band'][0]:<2d} {a['name'][:58]:58s} | {a['home'][:84]}")
low = [(a, t) for a in aims for t in of[a["n"]] if standing[t] != "living"]
print("   aims naming a thing not living in the table:", [(a["n"], a["name"][:40], t, standing[t]) for a, t in low])
print()
print("2. A thing with the aims it is a home of")
print(f"   things of the table an aim names a home: {len(under)} of {len(rows)}")
for t in sorted(under, key=lambda t: -len(under[t])):
    print(f"   {len(under[t]):3d} aims in {len(set(aims[n - 1]['band'][0] for n in under[t])):2d} bands · {standing[t]:10s} · {t}")
print("   living files no aim names a home:", [r["The thing"] for r in rows if r["Its kind"].startswith("a living file") and r["The thing"] not in under])
print("   things by their standing, with an aim and with none:", {s: (sum(1 for t in things if standing[t] == s and t in under), sum(1 for t in things if standing[t] == s and t not in under)) for s in ("living", "gathering", "dissolving", "artifact")})
print()
print("3. The ten bands, the table's parts")
total = [0, 0]
for b in sorted(set(a["band"] for a in aims)):
    A = [a for a in aims if a["band"] == b]
    o = sum(1 for a in A if a["obs"] not in ("—", ""))
    g = sum(1 for a in A if not in_a_living_file(a))
    th = collections.Counter(t for a in A for t in of[a["n"]])
    ss = sorted(set(origin[a["name"]] for a in A if a["name"] in origin))
    print(f"   2.{b[0]:<2d} {b[1][:42]:42s} {len(A):3d} aims · the window says {o:2d} · a note or a folder alone {g:2d} · things {len(th):2d} · sessions: {', '.join(ss) or 'none'}")
    total[0] += o; total[1] += 0 if ss else len(A)
    print("        " + "; ".join(f"{re.sub('^Exhibit [A-Z-]+ ', '', t)} {n}" for t, n in th.most_common(5)))
missing = [n for n in origin if n not in [a["name"] for a in aims]]
print("   a session's origin destiny not a row of the log:", missing or "none")
print(f"   aims the window says an area of: {total[0]} of {len(aims)}; aims in a band with no session's origin destiny: {total[1]}")
print()
print("4. An aim's state, and the places an aim names a thing")
k = collections.Counter(state(a) for a in aims)
print(f"   at rest {k['at rest']} · open {k['open']} · no living home {k['no living home']} · places an aim names a thing: {sum(len(v) for v in of.values())}")
print(f"   aims with an area ahead, no line naming it: {sum(1 for a in aims if a['dis'] not in ('—', ''))}")
