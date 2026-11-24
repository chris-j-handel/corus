#!/usr/bin/env python3
"""The notes of Exhibit THIRTY's gathering file at no group, at its head, at its opening and among its droplets: a note with
the group its sentence is of.

    python3 -I the_pile_s_notes_with_their_groups.py EXHIBIT_THIRTY.md GATHERING.md > TABLE.csv

A possible incohering opens with its living sentence in quotation marks: the sentence is found word
for word among the exhibit's sentences, and its group is the note's. An other note quotes a sentence
of the exhibit word for word, or names steps: with all of them in one group, that group is the note's. A note of several groups, or of none found, goes
on at the head. It moves nothing, sizes, and decides nothing.
"""
import csv, re, sys, collections
thirty, gathering = sys.argv[1:3]
src = open(thirty, encoding="utf-8").read()
heads = [(m.start(), int(m.group(1)), m.group(2).strip()) for m in re.finditer(r"^## (\d+) (.+)$", src, flags=re.M)]
group_of, text_of, title = {}, {}, {}
for i, (pos, n, t) in enumerate(heads):
    end = heads[i + 1][0] if i + 1 < len(heads) else len(src)
    title[n] = t
    for a, b in re.findall(r"^(\d+)\. (.*)$", src[pos:end], flags=re.M):
        group_of.setdefault(int(a), n)
        text_of.setdefault(int(a), re.sub(r"\s+", " ", b.replace("*", "")).strip())
by_text = {t: k for k, t in text_of.items()}
g = open(gathering, encoding="utf-8").read()
first_group = re.search(r"^### \d+ ", g, flags=re.M).start()
head = g[g.index("## Head, the whole file"):first_group]        # the head and the opening: at no group
if "\n## Droplets" in g:
    head += g[g.index("\n## Droplets"):]                         # the droplets after the last group
w = csv.writer(sys.stdout)
w.writerow(["at", "the note's kind", "the note's opening", "found by", "its sentences", "its group", "the group's title"])
size = collections.Counter()
at = "the head"
for line in head.split("\n"):
    if line.startswith("## Opening"):
        at = "the opening"
    if line.startswith("## Droplets"):
        at = "the droplets"
    m = re.match(r"^- \*\*([^*]+)\*\* · (.*)$", line)
    if not m:
        continue
    kind, body = m.group(1), m.group(2)
    opening = re.sub(r"\s+", " ", body)[:90]
    found, steps = "", []
    q = re.match(r'^["“](.+?)["”] →', body)
    if q:
        t = re.sub(r"\s+", " ", q.group(1).replace("*", "")).strip()
        if t in by_text:
            found, steps = "its living sentence, word for word", [by_text[t]]
        else:
            ks = [k for k, x in text_of.items() if t[:60] and x.startswith(t[:60])]
            if len(ks) == 1:
                found, steps = "its living sentence's opening words", ks
    if not steps:
        # a sentence of the exhibit quoted in italics or in quotation marks, word for word
        for seg in re.findall(r"(?<!\*)\*(?!\*)([^*]{20,}?)\*(?!\*)", body) + re.findall(r'["“]([^"”]{20,}?)["”]', body):
            t = re.sub(r"\s+", " ", seg).strip()
            k = by_text.get(t) or by_text.get(t + ".") or by_text.get(t.rstrip(".") + ".")
            if k:
                steps.append(k)
        steps = sorted(set(steps))
        if steps:
            found = "a sentence it quotes, word for word"
    if not steps:
        ks = set()
        for a, b in re.findall(r"steps? (\d+)(?: (?:to|and) (\d+))?", body):
            ks |= {int(a)} | ({int(b)} if b else set())
        steps = sorted(k for k in ks if k in group_of)
        found = "the steps it names" if steps else ""
    gs = sorted({group_of[k] for k in steps})
    if len(gs) == 1:
        place, tt = gs[0], title[gs[0]]
        size[(kind, "one group")] += 1
    elif gs:
        place, tt = "several: " + " ".join(map(str, gs)), ""
        size[(kind, "several groups")] += 1
    else:
        place, tt, found = "", "", "not found"
        size[(kind, "not found")] += 1
    w.writerow([at, kind, opening, found, " ".join(map(str, steps[:8])), place, tt])
sys.stderr.write("\n".join(f"{k[0]} | {k[1]} | {v}" for k, v in sorted(size.items())) + "\n")
