"""The opening's fifty-five waiting sentences, read by their own order: each name before its first using. All or none.

Reads Natural Intelligence's gathering, its droplet *Waiting to enter · The opening, 55 sentences*, and changes none.
Volunteered by v401atom for stage 2 of v401mgr's plan, which opens by the opening's groups, 14 November 2026.
Run: python3 incoming/V401atom/instruments/opening_order_check.py gathering-value/Natural_Intelligence.md

A name is a word a sentence has in bold: that sentence is its naming sentence.
A using is the name whole in a sentence, by its words' bounds, a hyphen a letter of a word, capitals passed over,
its last word as one or as more than one.
A sentence's connector, here: each sentence before it naming a name it uses.
A word having a hyphen is read as a name by its form: its naming sentence is the first having it in bold.
"""
import re, sys, collections
line = [l for l in open(sys.argv[1], encoding="utf-8").read().split("\n") if l.startswith("- **Waiting to enter** · The opening, 55 sentences")]
assert len(line) == 1
body = line[0]
S, pos = {}, body.index(" 1. ")
for n in range(1, 56):
    nxt = body.index(f" {n + 1}. ", pos + 1) if n < 55 else len(body)
    S[n] = body[pos + len(f" {n}. "):nxt].strip()
    pos = nxt
plain = {n: s.replace("*", "") for n, s in S.items()}

def pattern(name):
    stem, end = name, ''
    if re.search(r'[a-z]self$', ' ' + name, re.I):
        stem, end = name[:-1], '(?:f|ves)'
    elif re.search(r'[^aeiou]y$', name, re.I):
        stem, end = name[:-1], '(?:y|ies)'
    elif re.search(r'[a-z]{3}s$', name, re.I) and not name.lower().endswith('ss'):
        stem, end = name[:-1], 's?'
    elif re.search(r'[a-z]$', name, re.I):
        end = 's?'
    return re.compile(r'(?<![A-Za-z0-9-])' + re.escape(stem) + end + r'(?![A-Za-z0-9-])', re.I)

names = {}
for n, s in S.items():
    for b in re.findall(r'\*\*([^*]+)\*\*', s):
        names.setdefault(b, n)
pat = {b: pattern(b) for b in names}
print("The opening's waiting sentences, read by their own order")
print("sentences:", len(S), "· names in bold:", len(names), "· sentences naming one or more:", len(set(names.values())),
      "· sentences naming none:", ", ".join(str(n) for n in S if n not in names.values()))

print()
print("1 Each name's naming sentence is before its first using")
early = [(b, n, [m for m in S if m < n and pat[b].search(plain[m])]) for b, n in names.items()]
early = [e for e in early if e[2]]
print(f"  names first used at their naming sentence or after it: {len(names) - len(early)} · used before it: {len(early)}")
for b, n, before in early:
    print(f"    {b} · named by sentence {n} · used before it by sentence " + ", ".join(str(x) for x in before))
unused = [(b, n) for b, n in names.items() if not [m for m in S if m > n and pat[b].search(plain[m])]]
print(f"  names used by no sentence after their naming sentence: {len(unused)}")
for b, n in unused:
    print(f"    {b} · named by sentence {n}")

print()
print("2 Each word having a hyphen, a name by its form, and its naming sentence")
hy = collections.OrderedDict()
for n in S:
    for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)+", plain[n]):
        hy.setdefault(w.lower(), []).append(n)
low = {b.lower(): n for b, n in names.items()}
def naming(w):
    for b, n in low.items():
        if pattern(b).fullmatch(w):
            return n
    return None
no_name = [(w, ns) for w, ns in hy.items() if naming(w) is None]
print(f"  words having a hyphen: {len(hy)} · having a naming sentence: {len(hy) - len(no_name)} · having none: {len(no_name)}")
for w, ns in no_name:
    print(f"    {w} · in sentence " + ", ".join(str(x) for x in sorted(set(ns))))

print()
print("3 Each sentence's connector: each sentence before it naming a name it uses")
none = []
for n in S:
    used = sorted({m for b, m in names.items() if m < n and pat[b].search(plain[n])})
    if not used:
        none.append(n)
    print(f"  {n} · " + (", ".join(str(x) for x in used) if used else "none") + " · " + " ".join(plain[n].split()[:9]))
print("  sentences using no name named before them:", ", ".join(str(n) for n in none))
