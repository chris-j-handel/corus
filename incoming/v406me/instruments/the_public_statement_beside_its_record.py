#!/usr/bin/env python3
"""The public statement beside its record: its sentences by their standings, and a bump at a sentence the record has not.

    python3 -I incoming/v406me/instruments/the_public_statement_beside_its_record.py ROOT

The statement is v406other2's, for all sessions to pare. Its record is the managing session's, a row a sentence:
its standing, its showing with all numbers, a second observing apart, the parings and addings offered, its place
beside the draft and the one table, and a going through. The statement is living, and a sentence said again is a
bump here: a row of the record at no place of the statement now, or a sentence of the statement with no row.
It writes no file.
"""
import csv, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
S = os.path.join(root, "incoming/v406other2/For_the_public_Riemann_s_hypothesis_and_the_living_prime_numbering_a_statement_to_pare.md")
R = os.path.join(root, "incoming/v406me/The_public_statement_of_Riemann_s_hypothesis_and_the_living_prime_numbering_its_record.csv")
now = []
part = None
for l in open(S, encoding="utf-8").read().split("\n"):
    if l.startswith("**All of prime numbering"):
        now.append(("Its one sentence", l.strip("*"), ""))
    elif l.startswith("## "):
        part = l[3:]
    elif l.startswith("- ") and part and not part.startswith("To the sessions"):
        m = re.search(r"\(([^()]*)\)\s*$", l)
        now.append((part, (l[2:m.start()] if m else l[2:]).strip(), m.group(1) if m else ""))
rec = list(csv.reader(open(R, newline="")))[1:]
kinds = {}
for _, _, st in now:
    k = "no standing" if not st else st.split(";")[0].split(",")[0].strip()
    kinds[k] = kinds.get(k, 0) + 1
print(f"The public statement now: {len(now)} sentences, {sum(len(s.split()) for _, s, _ in now)} words.")
for k, n in sorted(kinds.items(), key=lambda x: -x[1]):
    print(f"  {n:3d}  {k}")
print(f"Its record: {len(rec)} rows. A second observing apart at {sum(1 for r in rec if r[5])}. "
      f"A paring or an adding offered at {sum(1 for r in rec if r[6])}. A going through said at {sum(1 for r in rec if r[8])}.")
said = set(s for _, s, _ in now)
rows = set(r[2] for r in rec)
bumps = 0
for r in rec:
    if r[2] not in said:
        bumps += 1
        print(f"a bump: the record's row {r[0]} is at no place of the statement now: {r[2][:90]}")
for p, s, _ in now:
    if s not in rows:
        bumps += 1
        print(f"a bump: a sentence of the statement with no row of the record, at {p}: {s[:90]}")
print("No bump: the record and the statement are a row a sentence." if not bumps else f"{bumps} bumps.")
