#!/usr/bin/env python3
"""Exhibit THIRTY, a group a row: its sentences, their marking by the lines, the notes gathered at it,
the aims naming it a home, and the sessions' pages naming its sentences.

    python3 -I the_groups_of_Exhibit_THIRTY_with_what_is_at_them.py EXHIBIT_THIRTY.md REACH.csv GATHERING.md AIMS.csv INCOMING_DIR [SESSION ...] > TABLE.csv

EXHIBIT_THIRTY.md  its next version, a group "## N title", a sentence "N. text".
REACH.csv          its sentences marked by the lines, by incoming/v405co-chain/instruments/reach.py.
GATHERING.md       its gathering file in the next version, a group "### N title", a note "- **kind** · ...".
AIMS.csv           incoming/v406aiming/Each_aim_by_its_names.csv, an aim with its home.
INCOMING_DIR       the set's incoming folder; SESSION, a folder of it whose pages are gone through.

A session's page names a sentence by "step N", "steps N to M", "sentence N" or "group N" in a line
saying Exhibit THIRTY. It matches by the words alone, sizes, and decides nothing.
"""
import csv, os, re, sys, collections
thirty, reach, gathering, aims, incoming, *sessions = sys.argv[1:]
src = open(thirty, encoding="utf-8").read()
heads = [(m.start(), int(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^## (\d+) (.+)$", src, flags=re.M)]
groups, group_of = {}, {}
for i, (pos, n, title) in enumerate(heads):
    end = heads[i + 1][0] if i + 1 < len(heads) else len(src)
    ss = sorted({int(a) for a in re.findall(r"^(\d+)\. ", src[pos:end], flags=re.M)})
    groups[n] = (title, ss)
    for k in ss:
        group_of[k] = n
mark = {n: collections.Counter() for n in groups}
for r in csv.DictReader(open(reach, encoding="utf-8")):
    k = int(r["step"])
    s = r["status"]
    mark[group_of[k]]["said again" if s == "said" else "resting" if s.startswith("reachable") else "waiting"] += 1
# the notes gathered, by the gathering file's own groups; the head's notes are at no group
notes = {n: collections.Counter() for n in groups}
pile = collections.Counter()
cur = None
for line in open(gathering, encoding="utf-8"):
    m = re.match(r"^### (\d+) ", line)
    if m:
        cur = int(m.group(1)); continue
    if re.match(r"^## ", line):
        cur = None; continue
    m = re.match(r"^- \*\*([^*]+)\*\* ·", line)
    if m:
        (notes[cur] if cur in notes else pile)[m.group(1)] += 1

def named(text):
    """the groups a saying names, by its steps and its groups"""
    out = set()
    for a, b in re.findall(r"(?:steps?|sentences?) (\d+)(?: (?:to|and) (\d+))?", text):
        a, b = int(a), int(b) if b else int(a)
        if " to " in text and b > a and b - a < 200:
            ks = range(a, b + 1)
        else:
            ks = (a, b)
        out |= {group_of[k] for k in ks if k in group_of}
    for a, b in re.findall(r"groups? (\d+)(?: (?:to|and) (\d+))?", text):
        a, b = int(a), int(b) if b else int(a)
        out |= {g for g in (range(a, b + 1) if b > a and b - a < 46 else (a, b)) if g in groups}
    return out
aim = collections.Counter()
for r in csv.DictReader(open(aims, encoding="utf-8")):
    for part in re.split(r";", r["home"]):
        if re.search(r"Exhibit THIRTY(?!-)", part):
            for g in named(part):
                aim[g] += 1
cites = {s: collections.Counter() for s in sessions}
for s in sessions:
    for root, _, files in os.walk(os.path.join(incoming, s)):
        for f in files:
            if not f.endswith(".md") or "ranscript" in f:
                continue
            for line in open(os.path.join(root, f), encoding="utf-8", errors="replace"):
                for sent in re.split(r"(?<=[.;:]) ", line):
                    if re.search(r"Exhibit THIRTY(?!-)", sent):
                        for g in named(sent):
                            cites[s][g] += 1
w = csv.writer(sys.stdout)
w.writerow(["group", "its title", "its sentences", "from", "to", "said again by a line", "resting on the lines", "waiting",
            "possible incoherings", "explainings", "possible explorings", "aims naming it a home"] + [f"places in {s}'s pages" for s in sessions])
for n in sorted(groups):
    title, ss = groups[n]
    w.writerow([n, title, len(ss), ss[0], ss[-1], mark[n]["said again"], mark[n]["resting"], mark[n]["waiting"],
                notes[n]["Possible incohering"], notes[n]["An explaining"], notes[n]["Possible exploring"], aim[n]]
               + [cites[s][n] for s in sessions])
sys.stderr.write(f"the head's notes, at no group: {dict(pile)}\n")
