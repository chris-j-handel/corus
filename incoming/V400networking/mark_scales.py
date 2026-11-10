"""Pass-one marking instrument: mark each sentence of Exhibit TWO at its scale.

Scales (from the gathering-value head's explaining): me-parity, self, society, surface.
A sentence naming none of the four is listed for hand review (a scale unsaid being a finding).
Also marks 'instrument' register (a working, an instrument, a study, an inquiry, a diagnostic)
and 'number/name-form' sentences, each a bound question for pass two, kept apart here.

Usage: python3 -I mark_scales.py <path-to-exhibit>

Recorded result, at Exhibit TWO Natural Networking v392: 1,465 sentences split;
self 567, society 128, surface 139, each sentence at each scale its words say;
me-parity 0; 761 at no scale word, 262 of them at the numbers or instrument
register alone; the full accounting at marking_returned.txt beside this file.
A count this instrument returns is an accounting of the reading and not the reading.
"""
import re, sys, json

path = sys.argv[1]
text = open(path, encoding="utf-8").read()

# Split into sections by headings; skip the contents block before PART ONE.
body = text[text.index("# PART ONE"):]
section_re = re.compile(r"^(#{1,3} .+)$", re.M)
parts = section_re.split(body)
sections = []  # (heading, body)
for i in range(1, len(parts), 2):
    sections.append((parts[i].lstrip("# ").strip(), parts[i + 1]))

SELF = re.compile(r"\b(self|selves|self's|resolver|resolvers|resolver's|receiver|receiving self|source|source's|joiner|a me\b)\b", re.I)
SOCIETY = re.compile(r"\b(same-existing-society|same-existing-societies|society|societies|society's|team)\b", re.I)
SURFACE = re.compile(r"\b(surface|surfaces|surface's|network|networking|network's|grid)\b", re.I)
MEPARITY = re.compile(r"\bme-parit\w*|\bmes\b|\ba me\b|\bits me\b", re.I)
INSTR = re.compile(r"\b(working|instrument|study|studies|inquiry|diagnostic|comparison|caller|kit|code|Python|executing|accounting|ledger|record|window|clock|schedule|observing apparatus|test)\b", re.I)
NUMFORM = re.compile(r"\b(eight on|nine less|9 less|17 less|seventeen less|odd|even|prime|composite|number|numbers|spiral step|map|pair|pairs|fold|podal)\b", re.I)

def sentences(block: str):
    out = []
    for raw_line in block.split("\n"):
        line = raw_line.strip()
        if not line or line.startswith(("|", "-", "Each entry:", "&nbsp;")) or re.match(r"^\d+\.", line):
            continue  # tables, list entries, numbered lists: marked apart (bound: pass two)
        line = line.replace("**", "")
        # naive sentence split on '. ' keeping abbreviations rare in this corpus
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9*])", line):
            s = s.strip()
            if len(s) > 1:
                out.append(s)
    return out

marked = []
for heading, block in sections:
    if heading.startswith("PART"):
        sec = heading
    else:
        sec = heading
    for s in sentences(block):
        scales = []
        if MEPARITY.search(s) and not re.search(r"same-parit", s, re.I):
            scales.append("me-parity")
        if SELF.search(s):
            scales.append("self")
        if SOCIETY.search(s):
            scales.append("society")
        if SURFACE.search(s):
            scales.append("surface")
        reg = []
        if INSTR.search(s):
            reg.append("instrument")
        if NUMFORM.search(s):
            reg.append("number-form")
        marked.append({"section": sec, "sentence": s, "scales": scales, "registers": reg})

counts = {}
unplaced = []
for m in marked:
    key = ",".join(m["scales"]) if m["scales"] else ("(" + "/".join(m["registers"]) + " only)" if m["registers"] else "NONE")
    counts[key] = counts.get(key, 0) + 1
    if not m["scales"]:
        unplaced.append(m)

print("sentences marked:", len(marked))
for k in sorted(counts, key=counts.get, reverse=True):
    print(f"{counts[k]:5d}  {k}")
print("\nunplaced (scale unsaid) by section:")
bysec = {}
for u in unplaced:
    bysec.setdefault(u["section"], []).append(u["sentence"])
for sec, ss in bysec.items():
    print(f"\n== {sec} ({len(ss)})")
    for s in ss:
        print("  -", s)

json.dump(marked, open("marking.json", "w"), indent=0)
