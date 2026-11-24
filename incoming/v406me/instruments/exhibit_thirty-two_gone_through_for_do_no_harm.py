"""Exhibit THIRTY-TWO Natural Prime Numbering, a first draft, gone through for do no harm beside the live set.
It goes through the draft, its sentences' file and the living files, and writes nothing.

    python3 -I incoming/v406me/instruments/exhibit_thirty-two_gone_through_for_do_no_harm.py LIVE

LIVE is the live set's root. A line says a thing found, and decides nothing.
"""
import glob, os, re, sys

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(0)
live = sys.argv[1]
P = os.path.join(live, "incoming/v407primes")
draft = open(os.path.join(P, "Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md"), encoding="utf-8").read()
story = open(os.path.join(P, "The_prime_numbers_named_and_explained_sentence_by_sentence.md"), encoding="utf-8").read()   # the sentences' file
L = draft.split("\n")
living = {os.path.basename(f): open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(live, "*_v*.md"))}
print(f"The draft: {len(draft.split())} words, {len(L)} lines. The living files: {len(living)}.")

print("\n1. Its form as a living file")
title = next(i for i, l in enumerate(L) if l.startswith("# "))
sep = next(i for i, l in enumerate(L) if l.strip() == "---" and any(x.startswith("# ") for x in L[i + 1:i + 4]))   # the rule the parts open after, as Me has it
heads = [re.match(r"^#{1,3} (.*)$", l).group(1).strip() for l in L[sep + 1:] if re.match(r"^#{1,3} ", l)]
entries = [l.strip()[2:] for l in L[title + 1:sep] if re.match(r"^- \d", l.strip())]
parts = [l.strip().strip("*") for l in L[title + 1:sep] if re.match(r"^\*\*[A-Z]+ · ", l.strip())]
print(f"   contents: {len(parts)} parts, {len(entries)} sections; with no heading: {[e for e in entries if e not in heads]}; parts with no heading: {[p for p in parts if p not in heads]}")
print(f"   its line 1: {L[0]!r}; a living file's line 1 ends with its version")
print(f"   a gathering file for it in the live set: {os.path.exists(os.path.join(live, 'gathering-value/Natural_Prime_Numbering.md'))}")
reg = next(v for k, v in living.items() if k.startswith("Exhibit_TWENTY-SIX"))
print(f"   the Living File Registry names it: {'THIRTY-TWO' in reg}; its sentence of the files' number: {re.search(r'[A-Z][a-z-]+ living files replace[^,]*,[^;]*', reg).group(0)[:150]!r}")

print("\n2. A word a partner's word of 23 November has away from natural naming and explaining")
cell = [(i + 1, l) for i, l in enumerate(L) if re.search(r"\bcells?\b", l)]
own = [n for n, l in cell if re.search(r"cell of nand|A cell is|a cell's|cells wired|a cell executes|no cell can|a cell can", l)]
print(f"   lines saying cell: {len(cell)}; of them the resolver's moment said as a cell: {own}; the others are a living thing's cell, the scale at 23")

print("\n3. The set's family words in it")
fam = re.compile(r"\b(what|whatever|how|however|somehow|where|wherever|nowhere|somewhere|elsewhere|anywhere|everywhere)\b", re.I)
for i, l in enumerate(L, 1):
    s = re.sub(r"\*[^*]+\*", "", l) if not l.startswith("**") else l
    for m in fam.finditer(re.sub(r"`[^`]+`", "", l)):
        print(f"   line {i}: {m.group(0)!r} in {l[max(0, m.start() - 30):m.end() + 30]!r}")

print("\n4. Concepts of the draft, and the living files having them now")
for q in ("durable snapshot", "next-universing", "other-than-other-than", "stable form of natural intelligence", "all-parity", "supernatural",
          "natural math", "prime scales", "phase-relation", "a first behind it, a place, a last, a store, an end, a magnitude, a beat, a value, a side, a cut",
          "a ghost is one moment's form", "society to society: all now, an other now, a me now, a me next, all next"):
    homes = [re.sub(r"_v\w+\.md$", "", k).replace("Exhibit_", "").replace("_", " ") for k, v in living.items() if q.lower() in v.lower()]
    print(f"   {q[:60]!r}: in the draft {draft.lower().count(q.lower())}; living in {len(homes)}: {', '.join(sorted(homes)[:4])}")

print("\n5. Exhibit THREE Natural Numbers beside it")
three = next(v for k, v in living.items() if k.startswith("Exhibit_THREE_"))
for q in (r"A composite folds along and a prime opens across", r"Primes 5 through 53 are prime scales[^*]*", r"Six prime pairs podal about thirty"):
    m = re.search(q, three)
    print(f"   Natural Numbers: {m.group(0)[:120]!r}" if m else f"   Natural Numbers has no {q!r}")
print(f"   the draft: {re.search(r'a staircase goes one up at a prime and across at a crossed number', draft).group(0)!r}")
print(f"   composite in Natural Numbers {len(re.findall(r'composite', three))}, in the draft {len(re.findall(r'composite', draft))}; crossed number in the draft {len(re.findall(r'crossed number', draft))}, in Natural Numbers {len(re.findall(r'crossed number', three))}")

print("\n6. Its prior naming: the sentences of its sentences' file in it")
S = re.findall(r"^(\d+)\. \*\*(.+?)\*\*", story, re.M)
def toks(t):
    return set(re.findall(r"\b\d[\d,]*\d\b|\b\d\d+\b", t)), set(x.lower() for x in re.findall(r"[A-Za-zφ][A-Za-zφ'-]{5,}", t))
dn, dw = toks(draft)
low = []
for num, bold in S:
    n, w = toks(bold)
    if not n and len(w) < 3:
        continue
    cw = len(w & dw) / len(w) if w else 1
    cn = len(n & dn) / len(n) if n else cw
    if cn * 0.6 + cw * 0.4 < 0.55 and bold.strip() not in draft and bold.strip()[:60] not in draft:
        low.append((int(num), bold[:90]))
print(f"   the numbered sentences of its sentences' file: {len(S)}; word for word in the draft: {sum(1 for n, b in S if b.strip() in draft)}; with little of their numbers and words in it: {low}")
for name in ("Prime_Numbers_A_Natural_Explaining_of_Sequential_Prime_Living.md", "The_prime_resolving_form.md"):
    t = open(os.path.join(P, name), encoding="utf-8").read()
    print(f"   {name}: seven methods {len(re.findall(r'seven methods', t, re.I))}, six prime livings {len(re.findall(r'six prime livings', t, re.I))}, five prime livings {len(re.findall(r'five prime livings', t, re.I))}")
print(f"   the draft: seven methods {len(re.findall(r'seven methods', draft, re.I))}, six prime livings {len(re.findall(r'six prime livings', draft, re.I))}, five prime livings {len(re.findall(r'five prime livings', draft, re.I))}")
