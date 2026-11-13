"""One self with one sharing: each case of what arrives, all or none. No opening by chance, and no case left out.

A reading of the code's own lines, case by case: a self with a prior, and the code's own state of an empty prior
with a sharing, no self, with none, one, two or three others' parities arriving, each +, - or 0. And what is
inherited with one, two and three sharings, each sharing's two arriving each + or -.
And the 1 to 9 diamond's four lines through 5, each name with its first prefix from Exhibit ONE's table.
Exhibit ONE's table and code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/each_case_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one = ns["_1_now_existing"]
S = "s"

cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]      # none, one, two or three arriving
print("cases of what arrives, none to three, each +, - or 0:", len(cases))

def resolve(prior, arriving):
    out, nxt = one([(S, prior)] if prior is not None else [], [(S, v) for v in arriving])
    return dict(out).get(S), dict(nxt).get(S)

# a self with a prior
goes_on = [(p, c) for p in (1, -1) for c in cases if resolve(p, c)[1] == p]
rule = lambda p, c: any(v != 0 for v in c) and all(v == p for v in c if v != 0)
print("1  a self with a prior, each case, with + and with -:", 2 * len(cases))
print("   its prior goes on with one case only, a parity or more arriving and each same-as its prior:", all((resolve(p, c)[1] == p) == rule(p, c) for p in (1, -1) for c in cases))
print("   with each other case its prior inverts:", all(resolve(p, c)[1] == -p for p in (1, -1) for c in cases if not rule(p, c)))
print("   with its prior going on, a 0 goes out; with its prior inverting, its next prior goes out:",
      all(resolve(p, c)[0] == (0 if rule(p, c) else -p) for p in (1, -1) for c in cases))

# an empty prior with a sharing: the code's own state, and no self
alike = lambda c: len({v for v in c if v != 0}) == 1
print("2  an empty prior with a sharing, the code's own state, each case:", len(cases))
print("   a first prior with one case only, a parity or more arriving and each the same as each other; that parity as it is:",
      all((resolve(None, c)[1] is not None) == alike(c) for c in cases) and all(resolve(None, c)[1] == next(v for v in c if v != 0) for c in cases if alike(c)))
print("   with two arriving not the same, nothing is inherited, and a 0 goes out:", all(resolve(None, c) == (0, None) for c in cases if {1, -1} <= set(c)))
print("   with none arriving, or each arriving a 0, nothing is inherited, and nothing goes out:", all(resolve(None, c) == (None, None) for c in cases if not any(c)))

# what is inherited: one, two and three sharings, each sharing's two arriving each + or -
keys = "abc"
total = allbi = 0; ok = okbi = True
for k in (1, 2, 3):
    for pairs in itertools.product(((1, 1), (-1, -1), (1, -1), (-1, 1)), repeat=k):
        arriving = [(keys[i], v) for i, pr in enumerate(pairs) for v in pr]
        out, nxt = one([], arriving); nxt = dict(nxt)
        want = {keys[i]: pr[0] for i, pr in enumerate(pairs) if pr[0] == pr[1]}
        total += 1; ok = ok and nxt == want
        if not want:
            allbi += 1; okbi = okbi and nxt == {}
print("3  what is inherited, with one, two and three sharings, each sharing's two arriving each + or -, each case:", total)
print("   what is inherited is each co-parity of its two, as it is, and no other:", ok)
print("   with each bi-parity of its two,", allbi, "cases: nothing is inherited:", okbi)

# the 1 to 9 diamond: 1 2 3 / 4 5 6 / 7 8 9, 1 and 9 its two tips along, 3 and 7 its two points across
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([^|]+) \| ([^|]+) \| (\w+) \| ([\w-]+) \|$", src, re.M)
three = {int(n): t.split("-") for n, _a, _r, _b, _c, t in rows}
print("4  the 1 to 9 diamond, each of its four lines through 5, each name with its first prefix")
for name, line in (("a side's line, 4-5-6", (4, 5, 6)), ("a side's line, 2-5-8", (2, 5, 8)), ("across, 3-5-7", (3, 5, 7)), ("along, 1-5-9", (1, 5, 9))):
    print(f"   {name}: {' '.join(three[n][0] for n in line)}")
print("   each of its four faces, 2, 4, 6 and 8, its three:", " ".join("-".join(three[n]) for n in (2, 4, 6, 8)))

# each parity inverted, + for - with each one: each same-existing and each inverting the same
neg = lambda v: None if v is None else -v
print("5  each parity inverted, + for - with each one, each case")
print("   a self's sharing and its next prior are each inverted, and nothing else is changed:",
      all(resolve(neg(p), tuple(-v for v in c)) == tuple(neg(v) for v in resolve(p, c)) for p in (1, -1, None) for c in cases))
print("   a self sharing 0 with its prior same-existing, and its next prior with its prior inverting:",
      all((resolve(p, c)[0] == 0) == (resolve(p, c)[1] == p) and (resolve(p, c)[1] == p or resolve(p, c)[0] == resolve(p, c)[1]) for p in (1, -1) for c in cases))
