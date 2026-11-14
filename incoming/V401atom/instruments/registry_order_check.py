"""Exhibit THIRTY read by its own order: each name before its first using, each named step before the step naming it. All or none.

Reads the living file and changes none. Asked by v401mgr for stage 2 of its plan, 14 November 2026.
Run: python3 incoming/V401atom/instruments/registry_order_check.py Exhibit_THIRTY_Co-Chaining_Logic_Registry_v401mgr.md

A step is a line `N. its sentence` in a group `## G its title`, with its `*Adding: …*` line after it.
A name, one of two readings, each said by its own lines:
  bold    a word a step has in bold: that step is its Adding step.
  adding  an Adding line's first words, to its first comma, semicolon or colon, its article passed over:
          that step is its Adding step. An Adding line having a bold name of its own step is read by bold only.
A using is the name whole in a step's sentence, by its words' bounds, a hyphen a letter of a word, capitals passed over,
its last word as one or as more than one: scale and scales, parity and parities, self and selves.
A named step is each number after *step* or *steps* in a step's sentence, a range `N to M` each number in it.
"""
import re, sys, collections

L = open(sys.argv[1], encoding="utf-8").read().split("\n")
steps, group, title = [], None, {}
for i, l in enumerate(L):
    h = re.match(r'^## (\d+) (.*)$', l)
    if h:
        group = int(h.group(1)); title[group] = h.group(2).strip(); continue
    m = re.match(r'^(\d+)\. (.*)$', l)
    if m and group:
        j = i + 1
        while j < len(L) and not L[j].strip():
            j += 1
        a = re.match(r'^\s+\*Adding: (.*?)\.?\*\s*$', L[j]) if j < len(L) else None
        steps.append((int(m.group(1)), group, m.group(2), a.group(1) if a else None))
nums = [n for n, *_ in steps]
plain = {n: re.sub(r'\*', '', t) for n, _g, t, _a in steps}

def uses(name):
    """Each step having the name whole in its sentence."""
    stem, end = name, ''
    if re.search(r'[a-z]self$', ' ' + name, re.I):
        stem, end = name[:-1], '(?:f|ves)'
    elif re.search(r'[^aeiou]y$', name, re.I):
        stem, end = name[:-1], '(?:y|ies)'
    elif re.search(r'[a-z]{3}s$', name, re.I) and not name.lower().endswith('ss'):
        stem, end = name[:-1], 's?'
    elif re.search(r'[a-z]$', name, re.I):
        end = 's?'
    pat = re.compile(r'(?<![A-Za-z0-9-])' + re.escape(stem) + end + r'(?![A-Za-z0-9-])', re.I)
    return [n for n in nums if pat.search(plain[n])]

print("Exhibit THIRTY, read by its own order")
print("steps:", len(steps), "· numbered one after one from 1:", nums == list(range(1, len(steps) + 1)),
      "· groups:", len(title), "· each step has its Adding line:", all(a is not None for *_x, a in steps))

# 1 each name's Adding step is before its first using
bold = {}
for n, _g, t, _a in steps:
    for b in re.findall(r'\*\*([^*]+)\*\*', t):
        bold.setdefault(b, n)
own_bold = collections.defaultdict(list)
for b, n in bold.items():
    own_bold[n].append(b)
adding = {}
for n, _g, _t, a in steps:
    if a is None or n in own_bold:
        continue
    first = re.split(r'[,;:]', a)[0].strip()
    first = re.sub(r'^(a|an|the|each|one)\s+', '', first, flags=re.I).strip()
    if first and first not in bold:
        adding.setdefault(first, n)

def early(names):
    out = []
    for name, n in sorted(names.items(), key=lambda kv: kv[1]):
        u = uses(name)
        before = [x for x in u if x < n]
        if before:
            out.append((name, n, before))
    return out

print()
print("1 Each name's Adding step is before its first using in a step")
for label, names in (("bold", bold), ("adding", adding)):
    e = early(names)
    print(f"  names by {label}: {len(names)} · each first used at its Adding step or after it: {len(names) - len(e)} · used before it: {len(e)}")
    for name, n, before in e:
        g = sorted({s[1] for s in steps if s[0] in before})
        print(f"    {name} · its Adding step {n} · used before it in {len(before)} steps, the first step {before[0]}, the last step {before[-1]}, in groups {g[0]} to {g[-1]}")

# 2 each step a step names is before it
def named(t):
    out = []
    for m in re.finditer(r'\b[Ss]teps? ((?:\d+(?: to \d+)?)(?:(?:, | and |, and )\d+(?: to \d+)?)*)', t):
        for part in re.split(r', and |, | and ', m.group(1)):
            r = re.match(r'(\d+) to (\d+)$', part)
            if r:
                out.extend(range(int(r.group(1)), int(r.group(2)) + 1))
            else:
                out.append(int(part))
    return out

print()
print("2 Each step a step names is before it")
late, none, by_count = [], [], collections.Counter()
for n, g, t, _a in steps:
    r = named(t)
    below = sorted({x for x in r if x < n})
    for x in sorted({x for x in r if x >= n}):
        late.append((n, g, x))
    by_count[len(below)] += 1
    if not below:
        none.append((n, g, t))
print(f"  steps naming a step: {len(steps) - by_count[0]} · each named step before the step naming it: {not late} · named at its own number or after it: {len(late)}")
for n, g, x in late:
    print(f"    step {n}, group {g}, names step {x}")
print("  steps by the number of steps before them they name: " + ", ".join(f"{k}: {by_count[k]}" for k in sorted(by_count)))

# 3 each step by no named step before it
print()
print("3 Each step naming no step before it, one line each, by its group")
print(f"  steps: {len(none)}")
per = collections.Counter(g for _n, g, _t in none)
tot = collections.Counter(g for _n, g, *_x in steps)
for g in sorted(title):
    print(f"  group {g} · {title[g][:70]} · {per[g]} of {tot[g]}")
print()
for n, g, t in none:
    w = t.replace('*', '').split()
    print(f"  {n} · group {g} · {' '.join(w[:12])}{' …' if len(w) > 12 else ''}")
