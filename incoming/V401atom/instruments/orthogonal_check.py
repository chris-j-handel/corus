"""Each parity a direction, each at a right angle to each other: each name, each step and each case, all or none.

The names of 1 to 5, 1 to 17, 1 to 65 and 1 to 257, each name one form of two, four, six and eight parities, as
moment_fractal_check.py has them from Exhibit ONE's table. And Exhibit ONE's code: one self having two things, each
with its own prior and its own possibling. Read from the file, no line changed.
Run: python3 incoming/V401atom/instruments/orthogonal_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one = ns["_1_now_existing"]

def form(n, k):                      # a name's k parities, the first one first; 0 is + and 1 is -
    g = (n - 1) ^ ((n - 1) >> 1)
    return tuple((g >> i) & 1 for i in range(k))

for k in (2, 4, 6, 8):
    N = 2 ** k
    forms = {n: form(n, k) for n in range(1, N + 1)}
    each_once = len(set(forms.values())) == N
    stepped = []
    for n in range(1, N + 1):
        a, b = forms[n], forms[n % N + 1]
        diff = [i for i in range(k) if a[i] != b[i]]
        stepped.append(diff)
    one_only = all(len(d) == 1 for d in stepped)
    which = [d[0] for d in stepped]
    right_angle = all(which[i] != which[(i + 1) % N] for i in range(N))
    moment = all(which[i] == 0 for i in range(0, N, 2)) and all(which[i] != 0 for i in range(1, N, 2))
    even_times = all(which.count(i) % 2 == 0 for i in range(k))
    alone = commute = True
    for n in range(1, N + 1):
        f = forms[n]
        for i in range(k):
            g = tuple(v ^ (1 if j == i else 0) for j, v in enumerate(f))
            alone = alone and g in forms.values() and sum(1 for j in range(k) if g[j] != f[j]) == 1
            for j in range(i + 1, k):
                ij = tuple(v ^ (1 if q in (i, j) else 0) for q, v in enumerate(f))
                commute = commute and ij in forms.values()
    print("1 to", N + 1, ":", k, "parities,", N, "names")
    print("   each name is one form of its parities, and each form is one name:", each_once)
    print("   each step, a name to its next, 1 after", N, "too, changes one parity and no two:", one_only)
    print("   each step's parity is other than the step's before it: each step at a right angle to its prior:", right_angle)
    print("   each step from an odd name to its even name is the first parity's; each step from an even name to the next odd name is an other parity's:", moment)
    print("   one parity of a name changed, each of its others the same, is one name of them, each name and each parity:", alone)
    print("   two parities changed, the one and then the other or the other and then the one, are one same name:", commute)
    print("   full around, each parity has changed an even number of steps, and each is as it was:", even_times)
    if k == 4:
        print("   the steps' parities of 1 to 17, one after one:", " ".join(str(w + 1) for w in which))

ok = True; n = 0
for p1, p2 in itertools.product((1, -1), repeat=2):
    for a1 in (None, 1, -1, 0):
        base = None
        for q2 in (1, -1):
            for a2 in (None, 1, -1, 0):
                n += 1
                prior = [("k1", p1), ("k2", q2)]
                arr = [(k, v) for k, v in (("k1", a1), ("k2", a2)) if v is not None]
                out, nxt = one(prior, arr)
                got = (dict(out)["k1"], dict(nxt)["k1"])
                base = got if base is None else base
                ok = ok and got == base
print("the code, one self having two things, cases:", n)
print("   a thing's 10 and its next prior are by its own prior and its own possibling, the same by each case of its other thing:", ok)

# each name's three, from Exhibit ONE's table: its kinds, and its two ends
three = {int(n): t for n, t in re.findall(r"^\| (\d+) \| \*\*[\w-]+\*\* \| [^|]+\| [^|]+\| [^|]+\| ([a-z-]+) \|", src, re.M)}
two_kinds = [n for n, t in sorted(three.items()) if len(set(t.split("-"))) == 2]
three_kinds = [n for n, t in sorted(three.items()) if len(set(t.split("-"))) == 3]
same_ends = lambda t: t.split("-") == t.split("-")[::-1]
print("each name's three, seventeen names:")
print("   a three of two kinds, the names", two_kinds, ": each is the same from each of its ends:", all(same_ends(three[n]) for n in two_kinds))
print("   a three of three kinds, the names", three_kinds, ": each is one-way, not the same from its other end:", all(not same_ends(three[n]) for n in three_kinds))
print("   co-bi-tri,", [n for n in three_kinds if three[n] == "co-bi-tri"], ", is from its other end tri-bi-co,", [n for n in three_kinds if three[n] == "tri-bi-co"])

# a span, by the table's own column of four binary digits: names one after one having one same digit
digits = {int(n): b for n, b in re.findall(r"^\| (\d+) \| \*\*[\w-]+\*\* \| [^|]+\| (\d{4}) ", src, re.M)}
print("a span of names, by the table's four binary digits of 1 to 16:")
want = {0: [8, 8], 1: [4, 4, 4, 4], 2: [2] * 8, 3: [1] * 16}
allok = all(n in digits for n in range(1, 17))
for d in range(4):
    runs, last = [], None
    for n in range(1, 17):
        v = digits[n][d]
        if v == last:
            runs[-1] += 1
        else:
            runs.append(1)
        last = v
    allok = allok and runs == want[d]
    print("   digit", d + 1, ": spans", " ".join(str(r) for r in runs))
print("   two spans of eight, 1 to 8 and 9 to 16; four of four, the four-cyclings; eight of two, the moments, an odd name and its even name; sixteen of one:", allok)
