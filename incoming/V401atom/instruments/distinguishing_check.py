"""A new self's first momentaries, each distinguishing in sequence, same-as: is, or is not. Exhibit ONE's code, no line changed.

A check of a reading: a living parity followed one distinguishing after another. Each line printed is one is-or-is-not of
Exhibit ONE's own table of its code, said for a new self with no prior and with two parities arriving together.
Run: python3 incoming/V401atom/instruments/distinguishing_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one = ns["_1_now_existing"]
S = "s"
say = lambda v: "none" if v is None else "+" if v > 0 else "-" if v < 0 else "0"
isnt = lambda b: "is" if b else "is not"

def follow(prior, arriving):
    """each is-or-is-not of one momentary, in the code's own sequence, beside what the code returns."""
    lines = []
    surfaced = None
    for v in arriving:
        lines.append(f"a parity arriving, {say(v)}: same-as 0, {isnt(v == 0)}")
        if v == 0: continue
        if surfaced is None:
            surfaced = v; lines.append(f"  a parity already surfacing with it, is not: {say(v)} surfaces")
        else:
            same = surfaced != 0 and (surfaced > 0) == (v > 0)
            lines.append(f"  same-as what surfaces, {say(surfaced)}: {isnt(same)}" + ("" if same else ": a 0"))
            if not same: surfaced = 0
    if prior is None:
        lines.append("a prior of its own: is not")
        going = surfaced
    else:
        if surfaced in (None, 0):
            going = -prior; lines.append(f"a prior of its own, {say(prior)}: is; a parity surfacing with it, is not: its prior inverts, {say(going)}")
        else:
            same = (surfaced > 0) == (prior > 0)
            going = 0 if same else -prior
            lines.append(f"a prior of its own, {say(prior)}: is; same-as what surfaces, {say(surfaced)}: {isnt(same)}: " + ("sharing 0" if same else f"one inversion, {say(going)}"))
    nxt = prior if going in (None, 0) else going
    lines.append(f"its going out, {say(going)}: same-as 0, {isnt(going == 0) if going is not None else 'none'}; its next prior, {say(nxt)}")
    out, kept = one([(S, prior)] if prior else [], [(S, v) for v in arriving])
    assert say(dict(out).get(S)) == say(going) and say(dict(kept).get(S)) == say(nxt), (prior, arriving)
    return lines, nxt

for title, seq in [("a self's parity same-as an other's, is: +, + arriving, then 0, 0, then -, -", [(1, 1), (0, 0), (-1, -1), (0, 0)]),
                   ("a self's parity same-as an other's, is not: -, + arriving, then +, -", [(-1, 1), (1, -1)])]:
    print(title)
    prior = None
    for m, arriving in enumerate(seq, 1):
        lines, prior = follow(prior, list(arriving))
        print(f"  momentary {m}")
        for l in lines: print("    " + l)
import itertools
n = 0
for prior in (None, 1, -1):
    for arriving in itertools.chain.from_iterable(itertools.product((1, -1, 0), repeat=r) for r in range(0, 4)):
        follow(prior, list(arriving)); n += 1
print(f"each of {n} cases, a prior none, + or - and none to three parities arriving: the sequence of is-or-is-nots and the code's own returning are the same")
