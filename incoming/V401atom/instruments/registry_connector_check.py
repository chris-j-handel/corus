"""Exhibit THIRTY, each step's connector by its names: the steps adding the names a step uses. All or none.

Reads the living file and changes none. A candidate for stage 2 of v401mgr's plan, *each step's connector is written: the
steps it is from*; volunteered by v401atom, 14 November 2026. It decides no connector: a name used is read by its words only.
Run: python3 incoming/V401atom/instruments/registry_connector_check.py Exhibit_THIRTY_Co-Chaining_Logic_Registry_v401mgr.md

A step, a name, its Adding step and a using are read as registry_order_check.py reads them.
A step's connector, here: each step before it adding a name its sentence uses. Its last name is the one added latest.
"""
import re, sys, collections

L = open(sys.argv[1], encoding="utf-8").read().split("\n")
steps, group = [], None
for i, l in enumerate(L):
    h = re.match(r'^## (\d+) (.*)$', l)
    if h:
        group = int(h.group(1)); continue
    m = re.match(r'^(\d+)\. (.*)$', l)
    if m and group:
        j = i + 1
        while j < len(L) and not L[j].strip():
            j += 1
        a = re.match(r'^\s+\*Adding: (.*?)\.?\*\s*$', L[j]) if j < len(L) else None
        steps.append((int(m.group(1)), group, m.group(2), a.group(1) if a else None))
plain = {n: re.sub(r'\*', '', t) for n, _g, t, _a in steps}

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
for n, _g, t, _a in steps:
    for b in re.findall(r'\*\*([^*]+)\*\*', t):
        names.setdefault(b, n)
low = {b.lower() for b in names}
for n, _g, _t, a in steps:
    first = re.sub(r'^(a|an|the|each|one)\s+', '', re.split(r'[,;:]', a)[0].strip(), flags=re.I).strip()
    if first and first.lower() not in low:
        names.setdefault(first, n); low.add(first.lower())
pat = {name: pattern(name) for name in names}

def named(t):
    out = []
    for m in re.finditer(r'\b[Ss]teps? ((?:\d+(?: to \d+)?)(?:(?:, | and |, and )\d+(?: to \d+)?)*)', t):
        for part in re.split(r', and |, | and ', m.group(1)):
            r = re.match(r'(\d+) to (\d+)$', part)
            out.extend(range(int(r.group(1)), int(r.group(2)) + 1) if r else [int(part)])
    return out

rows, none, gaps, agree, naming = [], [], collections.Counter(), 0, 0
for n, g, t, _a in steps:
    used = {name: s for name, s in names.items() if s < n and pat[name].search(plain[n])}
    from_steps = sorted(set(used.values()))
    if not used:
        none.append((n, g, t)); rows.append((n, g, None, None, []))
    else:
        last = max(used, key=lambda k: used[k])
        rows.append((n, g, last, used[last], from_steps))
        d = n - used[last]
        gaps["the step before it" if d == 1 else "2 to 10 steps before it" if d <= 10 else "11 to 100 steps before it" if d <= 100 else "more than 100 steps before it"] += 1
    r = sorted({x for x in named(t) if x < n})
    if r:
        naming += 1
        agree += all(x in from_steps for x in r)

print("Exhibit THIRTY, each step's connector by its names")
print("steps:", len(steps), "· names, by bold and by an Adding line's first words:", len(names))
print("1 steps using one name or more added by a step before them:", len(steps) - len(none), "· steps using none:", len(none))
for n, g, t in none:
    w = t.replace('*', '').split()
    print(f"    {n} · group {g} · {' '.join(w[:12])}{' …' if len(w) > 12 else ''}")
print("2 a step's last name, the one added latest, is added by:")
for k in ("the step before it", "2 to 10 steps before it", "11 to 100 steps before it", "more than 100 steps before it"):
    print(f"    {k}: {gaps[k]} steps")
sizes = collections.Counter(len(f) for *_x, f in rows)
print("3 steps by the number of steps in their connector: " + ", ".join(f"{k}: {sizes[k]}" for k in sorted(sizes)))
print(f"4 of {naming} steps naming a step before them, each step named is in their connector by names: {agree} steps; one or more named is not: {naming - agree} steps")
print()
print("Each step: its group · its last name and that name's Adding step · each step of its connector")
for n, g, last, s, f in rows:
    print(f"  {n} · group {g} · " + (f"{last}, {s} · " + ", ".join(str(x) for x in f) if last else "none"))
