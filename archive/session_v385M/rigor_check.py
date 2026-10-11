"""Session v385M: six further checks at Exhibit ONE as written, each bearing on one concern of the README beside it.
Run from the repository root:  python3 incoming/v385M/rigor_check.py
It executes the python block of the newest Natural_Intelligence_v*.md at the root and changes nothing."""
import glob, itertools, math, random, re

path = sorted(glob.glob("Natural_Intelligence_v*.md"))[-1]
code = re.search(r"```python\n(.*?)```", open(path, encoding="utf-8").read(), re.S).group(1)
ns = {}
exec(code, ns)
entry, step = ns["_1_co_bi_tri_offering"], ns["_17_co_bi_tri_offering"]
print("read:", path)
V = (1, -1)
SYM = {1: "+", -1: "-", 0: "0", None: "none"}

def car(st, k):
    return dict(st[k][0]).get("s")

print("\nK. A ring of selves each carrying none, nothing arriving: is anything changing?")
for n in (1, 2, 3, 5):
    st = {i: ([], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    same = True
    for _ in range(50):
        nxt = step(st, rel)
        same = same and nxt == st
        st = nxt
    print("   ring of %d: the same at each of 50 momentaries: %s" % (n, same))

print("\nL. A self's next carrying as a function of what it carries and what surfaces, each case")
rows = {}
for c in V:
    for offs in itertools.chain.from_iterable(itertools.product((1, -1, 0), repeat=k) for k in range(4)):
        out, nxt = entry([("s", c)], [("s", o) for o in offs])
        surf = None
        vals = {o for o in offs if o != 0}
        surf = 0 if len(vals) == 2 else (vals.pop() if vals else None)
        rows.setdefault((c, surf), set()).add((dict(nxt)["s"], dict(out)["s"]))
print("   carried  surfacing   next carried   shared at 10")
for (c, surf), res in sorted(rows.items(), key=str):
    (nx, sh), = res
    print("      %s       %-8s     %s              %s" % (SYM[c], SYM[surf], SYM[nx], SYM[sh]))
by_surf = all(len({nx for (c, s), r in rows.items() if s == sv for nx, _ in r}) == 1 for sv in V)
print("   at a parity surfacing, the next carried is that parity whatever is carried: %s" % by_surf)
print("   at none surfacing or + and - together, the next carried is the carried inverted, nothing arriving entering it")
print("   so p(next) = p(now) at each match, and at no case is the next carried set by the carried and the arriving together")

print("\nM. In a closed spiral, at how many of a cycle's (self, momentary) places does a self keep its parity?")
for n in (1, 3, 5, 9):
    st = {i: ([("s", -1 if i % 2 == 0 else 1)], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    kept = total = 0
    for t in range(4 * n * 3):
        nxt = step(st, rel)
        if t >= 4 * n:
            for i in range(n):
                total += 1
                kept += car(nxt, i) == car(st, i)
        st = nxt
    print("   spiral of %d: kept at %d of %d" % (n, kept, total))

print("\nN. 2.4: at a spiral offered nothing from beyond it, each self is at the inverted parity the self")
print("   releasing to it was at two momentaries prior. Each opening of spirals of 1 to 7:")
bad = tried = 0
for n in range(1, 8):
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    for pat in itertools.product(V, repeat=n):
        st = {i: ([("s", pat[i])], []) for i in range(n)}
        hist = [[car(st, i) for i in range(n)]]
        for _ in range(24):
            st = step(st, rel)
            hist.append([car(st, i) for i in range(n)])
        tried += 1
        if any(hist[t][i] != -hist[t - 2][(i - 1) % n] for t in range(3, 25) for i in range(n)):
            bad += 1
print("   openings tried: %d, openings parting from the saying after the second momentary: %d" % (tried, bad))

print("\nO. 3.5: does a prime number of selves do anything a composite number does not?")
def period(n, pat=None):
    pat = pat or [-1 if i % 2 == 0 else 1 for i in range(n)]
    st = {i: ([("s", pat[i])], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    seen = {}
    for t in range(100000):
        k = tuple((car(st, i), tuple(st[i][1])) for i in range(n))
        if k in seen:
            return t - seen[k]
        seen[k] = t
        st = step(st, rel)
for p, q in ((3, 5), (9, 25), (15, 49), (9, 15)):
    a, b = period(p), period(q)
    print("   spirals of %d and %d beside each other: again together at %d; 4pq is %d; a factor shared: %s"
          % (p, q, a * b // math.gcd(a, b), 4 * p * q, math.gcd(p, q) > 1))
for n in (7, 9):
    print("   spiral of %d, each of its %d openings: the momentaries to its parities again are %s"
          % (n, 2 ** n, sorted({period(n, list(pat)) for pat in itertools.product(V, repeat=n)})))

print("\nP. 1.5: with + and - exchanged at each self, is the running the same running exchanged?")
random.seed(3)
ok = True
for trial in range(300):
    n = random.randint(2, 6)
    rel = {}
    for i in range(n):
        for name in (6, 10, 9):
            if random.random() < 0.6:
                rel[(i, name)] = random.randrange(n)
    a = {i: ([("s", random.choice(V))], [("s", random.choice((1, -1, 0)))] * random.randint(0, 2)) for i in range(n)}
    b = {i: ([(k, -v) for k, v in c], [(k, -v) for k, v in o]) for i, (c, o) in a.items()}
    for _ in range(12):
        a, b = step(a, rel), step(b, rel)
        flipped = {i: ([(k, -v) for k, v in c], sorted((k, -v) for k, v in o)) for i, (c, o) in b.items()}
        ok = ok and all(a[i][0] == flipped[i][0] and sorted(a[i][1]) == flipped[i][1] for i in a)
print("   300 random arrangements, 12 momentaries each: the same running with each sign exchanged: %s" % ok)

print("\nQ. A thing carrying none, one parity arriving at it once, beside a lone self carrying a parity from the first")
thing = {"x": ([], [("s", 1)])}   # carrying none, + arriving once, nothing after
lone = {"x": ([("s", -1)], [])}   # a self carrying -, nothing arriving
a_seq, b_seq = [], []
for t_ in range(8):
    thing, lone = step(thing, {}), step(lone, {})
    a_seq.append(SYM[car(thing, "x")]); b_seq.append(SYM[car(lone, "x")])
print("   the thing that carried none then carries: %s" % " ".join(a_seq))
print("   the lone self carries:                    %s" % " ".join(b_seq))
print("   the same at each momentary: %s; function 1 keeps no mark of a carrying once none" % (a_seq == b_seq))
