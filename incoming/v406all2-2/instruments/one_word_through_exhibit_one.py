"""Exhibit ONE Natural Resolver, live beside its next version: the places of one word re-said, a place with its words.

Usage: python3 -I incoming/v406all2-2/instruments/one_word_through_exhibit_one.py <live file> <next version's file>
Reads two files and prints; writes nothing. A place is a line of the live file and the same line of the next version.
"""
import difflib, re, sys

live = open(sys.argv[1], encoding="utf-8").read().split("\n")
nxt = open(sys.argv[2], encoding="utf-8").read().split("\n")
tok = lambda s: re.findall(r"\w+(?:[-’']\w+)*|[^\w\s]", s)
sm = difflib.SequenceMatcher(None, live, nxt, autojunk=False)
places, other, n_within_live = [], [], sum(len(re.findall(r"\bwithin\b", l, flags=re.I)) for l in live)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    if tag != "replace" or (i2 - i1) != (j2 - j1):
        other.append((tag, live[i1:i2], nxt[j1:j2])); continue
    for k, (a, b) in enumerate(zip(live[i1:i2], nxt[j1:j2])):
        ta, tb = tok(a), tok(b)
        w = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
        for t, a1, a2, b1, b2 in w.get_opcodes():
            if t == "equal":
                continue
            was, now = " ".join(ta[a1:a2]), " ".join(tb[b1:b2])
            before = " ".join(ta[max(0, a1 - 5):a1]); after = " ".join(ta[a2:a2 + 5])
            places.append((i1 + k + 1, was, now, before, after))
kinds = {}
for line, was, now, before, after in places:
    key = "within" if was.lower() == "within" else "other"
    kinds.setdefault(key, []).append((line, was, now, before, after))
print("within, in the live file:", n_within_live, "in", sum(bool(re.search(r"\bwithin\b", l, flags=re.I)) for l in live), "lines | in the next version:", sum(len(re.findall(r"\bwithin\b", l, flags=re.I)) for l in nxt))
print("places of within re-said:", len(kinds.get("within", [])))
tally = {}
for p in kinds.get("within", []):
    tally[p[2].lower()] = tally.get(p[2].lower(), 0) + 1
print("re-said as:", ", ".join(f"{k} {v}" for k, v in sorted(tally.items(), key=lambda kv: -kv[1])))
print()
for line, was, now, before, after in kinds.get("within", []):
    print(f"{line:5d} · {before} [{was} → {now}] {after}")
print()
print("places re-said other-than the one word:", len(kinds.get("other", [])))
for line, was, now, before, after in kinds.get("other", []):
    print(f"{line:5d} · {before} [{was} → {now}] {after}")
print("lines away or new:", len(other))
for o in other:
    print("  ", o[0], "|", " / ".join(o[1])[:200], "|", " / ".join(o[2])[:200])
