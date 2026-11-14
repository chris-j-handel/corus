"""The page of discoveries, its co-chaining: each sentence from the ones before it, or having its base. All or none.

Reads incoming/V401atom/The_Value_Droplets.md. Each numbered sentence of its parts A to K.
Run: python3 incoming/V401atom/instruments/sequence_check.py incoming/V401atom/The_Value_Droplets.md
"""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
body = t[t.index("## A Parity"):t.index("## L Meeting")]
items = re.findall(r"^(\d+)\. (.*)$", body, re.M)
nums = [int(n) for n, _ in items]
print("sentences:", len(items), "; numbered 1 and on, each one after the one before it:", nums == list(range(1, len(nums) + 1)))
forward = []; no_ground = []; bases = {"the opening": [], "a name's is": [], "the table": [], "executed": [], "the set": []}
for n, text in items:
    n = int(n)
    refs = [int(x) for b in re.findall(r"\[([\d, ]+)\]", text) for x in b.split(",")]
    forward += [(n, r) for r in refs if r >= n]
    low = text.lower()
    marks = [k for k, key in (("the opening", "the opening's"), ("a name's is", "a name's is"), ("the table", "exhibit one's table"), ("executed", "executed"), ("the set", "exhibit twenty's")) if key in low]
    for k in marks:
        bases[k].append(n)
    if not refs and not marks:
        no_ground.append(n)
print("each number in brackets is of a sentence before its own:", not forward, forward)
print("each sentence has the sentences it is from, or its base:", not no_ground, no_ground)
for k, v in bases.items():
    print("  ", k, ":", len(v), "sentences")
from_only = [int(n) for n, text in items if re.search(r"\[[\d, ]+\]", text) and not any(key in text.lower() for key in ("the opening's", "a name's is", "exhibit one's table", "executed", "exhibit twenty's"))]
print("   from the sentences before it only:", len(from_only), "sentences")
