"""Session v385Q. Run from the repository root:  python3 incoming/v385Q/resolver_observings.py
It executes the python block of the newest Exhibit_ONE_Natural_Resolver_v*.md at the root and changes nothing.
One tool for one report: each observing in incoming/v385Q/README.md is a part here, A to V.
What is observed is Exhibit ONE's code at the arrangements written below. Nothing here observes a living thing.

The arrangements. A spiral of n selves: each releasing along (9) to the next, the last to the first, one
sharing, the first self carrying -, the selves alternating along, none offered from beyond: Exhibit ONE's own
published spiral. A torus of p by q selves: each releasing along (9) and sharing across (10), as published.
A colliding: at each momentary from a first to a last, one parity offered to self 1 from beyond, by a form
that is unchanging at + or at -, or returns the parity self 1 is carrying, or returns the other parity, or
alternates +, - at its own momentaries. Momentaries are numbered from 1."""
import glob, itertools, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
path = sorted(glob.glob(os.path.join(root, "Exhibit_ONE_Natural_Resolver_v*.md")))[-1]
code = re.search(r"```python\n(.*?)```", open(path, encoding="utf-8").read(), re.S).group(1)
ns = {}
exec(code, ns)
entry, step = ns["_1_co_bi_tri_offering"], ns["_17_co_bi_tri_offering"]
print("read:", os.path.basename(path))
S = {1: "+", -1: "-", 0: "0", None: "."}
V = (1, -1)
FORMS = [
    ("unchanging at +", lambda t, c: 1),
    ("unchanging at -", lambda t, c: -1),
    ("returning what it meets", lambda t, c: c),
    ("returning the other parity", lambda t, c: -c),
    ("alternating +, -", lambda t, c: 1 if t % 2 == 0 else -1),
]


def alt(i):
    return -1 if i % 2 == 0 else 1


def spiral(n, form=None, start=0, stop=None, T=400, pattern=None):
    """Shared changing (10) and carried parity (3) of each self at each momentary."""
    st = {i: ([("s", pattern[i] if pattern else alt(i))], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    sh, car = [], []
    for t in range(T):
        if form and t >= start and (stop is None or t < stop):
            c, o = st[0]
            st[0] = (c, o + [("s", form(t, dict(c)["s"]))])
        car.append([dict(st[i][0])["s"] for i in range(n)])
        sh.append(tuple(dict(entry(*st[i])[0]).get("s") for i in range(n)))
        st = step(st, rel)
    return sh, car


def torus(p, q, form=None, start=0, stop=None, T=600, quiet=None):
    """Shared changing of each self at each momentary. quiet = (a, b): self 1 releasing and sharing to none
    from momentary a + 1 until b."""
    cells = [(i, j) for i in range(p) for j in range(q)]
    st = {c: ([("s", alt(c[0] + c[1]))], []) for c in cells}
    rel = {}
    for i, j in cells:
        rel[((i, j), 9)] = ((i + 1) % p, j)
        rel[((i, j), 10)] = (i, (j + 1) % q)
    less = {k: v for k, v in rel.items() if k[0] != (0, 0)}
    sh = []
    for t in range(T):
        if form and t >= start and (stop is None or t < stop):
            c, o = st[(0, 0)]
            st[(0, 0)] = (c, o + [("s", form(t, dict(c)["s"]))])
        sh.append(tuple(dict(entry(*st[c])[0]).get("s") for c in cells))
        st = step(st, less if quiet and quiet[0] <= t < quiet[1] else rel)
    return sh


def again(rows, tail=240):
    """Momentaries to the same sharings again, read at the last `tail` momentaries."""
    s = rows[-tail:]
    for per in range(1, tail // 2):
        if all(s[i] == s[i + per] for i in range(tail - per)):
            return per
    return None


def ahead(rows, base, P, lo, hi):
    """Momentaries the arrangement is ahead of the published one, or None where it is at no displacing of it."""
    ks = [k for k in range(P) if all(rows[t] == base[t + k] for t in range(lo, hi))]
    return ks[0] if ks else None


def between_zeros(sh, i, lo, hi):
    at = [t for t in range(lo, hi) if sh[t][i] == 0]
    return sorted(set(b - a for a, b in zip(at, at[1:])))


def living_step(car, n, lo, hi):
    """At each self: momentaries t from lo to hi at which its carried parity at t + 2 is the inverse of the
    carried parity, at t, of the self releasing to it."""
    return [sum(car[t + 2][i] == -car[t][(i - 1) % n] for t in range(lo, hi)) for i in range(n)]


print("\nA. The entry at one carried sharing")
none_again = total = 0
for c in V:
    for k in range(5):
        for offs in itertools.product((1, -1, 0), repeat=k):
            total += 1
            none_again += dict(entry([("s", c)], [("s", o) for o in offs])[1]).get("s") not in V
print("   each list of up to four offerings of +, - and 0: lists %d, next carried none %d" % (total, none_again))
for c in V:
    for o in V:
        tun, nxt = entry([("s", c)], [("s", o)])
        print("   carried %s, offered %s: shared %s, next carried %s" % (S[c], S[o], S[dict(tun)["s"]], S[dict(nxt)["s"]]))

print("\nB. The living step in a spiral: each self's next the releasing self's prior inverted, two momentaries on")
tried = parting = 0
for n in range(2, 10):
    for pat in itertools.product(V, repeat=n):
        tried += 1
        parting += living_step(spiral(n, pattern=list(pat), T=60)[1], n, 0, 58) != [58] * n
print("   spirals of 2 to 9 selves, each opening pattern, none offered from beyond: patterns %d, parting %d" % (tried, parting))

print("\nC. The same relation while a form collides with self 1, momentaries 41 to 140: at each self, self 1 first,")
print("   the momentaries of 98 at which it is so; then, after the colliding has ended, of 96")
for n in (3, 5, 7, 9):
    for name, f in FORMS:
        car = spiral(n, f, start=40, stop=140, T=240)[1]
        d, a = living_step(car, n, 40, 138), living_step(car, n, 142, 238)
        print("   n = %d, %-27s self 1: %2d; each other self: %s | after: %s" % (
            n, name, d[0], sorted(set(d[1:])), sorted(set(a))))

print("\nD. The 0 of an odd spiral. Three selves, the self sharing 0 at each momentary, the colliding from 81")
base3 = spiral(3)[0]
zero_at = lambda row: "".join(str(i + 1) for i, x in enumerate(row) if x == 0) or "."
print("   momentary                    " + " ".join("%3d" % (t + 1) for t in range(77, 96)))
print("   %-28s " % "none offered" + " ".join("%3s" % zero_at(r) for r in base3[77:96]))
for name, f in FORMS:
    print("   %-28s " % name + " ".join("%3s" % zero_at(r) for r in spiral(3, f, start=80)[0][77:96]))
print("   momentaries from one 0 to the next at each self, while the colliding continues; published 2n")
for name, f in FORMS:
    row = []
    for n in (3, 5, 7, 9, 11, 13, 15):
        sh = spiral(n, f, start=80, T=500)[0]
        g = sorted(set(x for i in range(n) for x in between_zeros(sh, i, 300, 500)))
        row.append("%d: %s" % (n, g[0] if len(g) == 1 else (g or "no 0")))
    print("   %-28s %s" % (name, "; ".join(row)))
print("   the first momentary each self's sharing parts from the published spiral's, along the releasing")
for name, f in FORMS:
    row = []
    for n in (3, 5, 7, 9):
        b, sh = spiral(n)[0], spiral(n, f, start=80)[0]
        first = [next(t + 1 for t in range(400) if sh[t][i] != b[t][i]) for i in range(n)]
        row.append("n=%d from %d, each next self %s later" % (n, first[0], sorted(set(y - x for x, y in zip(first, first[1:])))))
    print("   %-28s %s" % (name, "; ".join(row)))
tried = other = 0
for n in (3, 5, 7, 9):
    for name, f in FORMS[:3]:
        for start in range(4 * n):
            tried += 1
            sh = spiral(n, f, start=start, T=360)[0]
            other += sorted(set(x for i in range(n) for x in between_zeros(sh, i, 200, 360))) != [2 * n - 1]
print("   the colliding beginning at each momentary of one whole round of 4n, the three forms with a 0: tried %d, not at 2n - 1: %d" % (tried, other))

print("\nE. Twice and one less: a spiral of n selves, a form unchanging at + colliding, its 0 again at")
row = []
for n in (3, 5, 9, 17, 33, 65):
    T = 30 * n + 300
    sh = spiral(n, FORMS[0][1], start=4 * n, T=T)[0]
    g = sorted(set(x for i in (0, n // 2, n - 1) for x in between_zeros(sh, i, T - 9 * n, T)))
    row.append("%d selves: %s" % (n, g))
print("   " + "; ".join(row))

print("\nF. After the colliding has ended, a spiral: its sharings again at 4n at each one tried; and the momentaries")
print("   it is ahead of the published spiral, by the momentaries the colliding continued, 1 to 24")
for n in (3, 5, 7):
    base = spiral(n, T=760)[0]
    inv = ahead([tuple(-x if x else x for x in r) for r in base], base, 4 * n, 300, 500)
    print("   n = %d, 4n = %d; each parity inverted is the published spiral %d ahead" % (n, 4 * n, inv))
    for name, f in FORMS:
        ks, rounds = [], set()
        for d in range(1, 25):
            sh = spiral(n, f, start=40, stop=40 + d, T=560)[0]
            rounds.add(again(sh))
            ks.append(ahead(sh, base, 4 * n, 300, 520))
        print("     %-27s again at %s; ahead %s" % (name, sorted(rounds), " ".join(str(k) for k in ks)))

print("\nG. A torus of p by q selves, the form colliding with one self. While it continues: the torus's sharings")
print("   again at; the selves whose sharing ever parts from the published torus's. After a colliding of 1 to 40")
print("   momentaries has ended: how many of the 40 leave the torus as published (=), at a displacing of the")
print("   published (d), or at its own round in a pattern that is no displacing of the published (x)")
for p, q in ((3, 5), (5, 7), (3, 7)):
    base = torus(p, q, T=1100)
    P = again(base)
    print("   torus %d by %d, %d selves, published: again at %d" % (p, q, p * q, P))
    for name, f in FORMS:
        sh = torus(p, q, f, start=100, T=700)
        parted = sum(any(sh[t][k] != base[t][k] for t in range(100, 700)) for k in range(p * q))
        kinds, steps, own = [], [], 0
        for d in range(1, 41):
            s2 = torus(p, q, f, start=100, stop=100 + d, T=800)
            own += again(s2) == P
            k = ahead(s2, base, P, 560, 760)
            kinds.append("=" if k == 0 else ("x" if k is None else "d"))
            steps.append(k)
        first = next((d + 1 for d, k in enumerate(kinds) if k != "="), None)
        runs = [((b - a) % P) for a, b in zip(steps, steps[1:]) if a is not None and b is not None and (a or b)]
        print("     %-27s while: again at %2s, selves parting %2d | after: at its own round %d of 40; = %2d, d %2d, x %2d; first not = at %s%s" % (
            name, again(sh), parted, own, kinds.count("="), kinds.count("d"), kinds.count("x"), first,
            "; each further momentary of colliding %s ahead" % sorted(set(runs)) if len(set(runs)) == 1 else ""))

print("\nH. A torus with one self releasing and sharing to none, momentaries 101 on; and given again at 201")
for p, q in ((3, 3), (3, 5), (5, 7), (3, 7)):
    base = torus(p, q, T=1100)
    P = again(base)
    a = torus(p, q, quiet=(100, 10 ** 9), T=700)
    b = torus(p, q, quiet=(100, 200), T=800)
    k = ahead(b, base, P, 560, 760)
    print("   torus %d by %d, published again at %d: with the one self to none, again at %s; given again: again at %s, %s" % (
        p, q, P, again(a), again(b), "as published" if k == 0 else ("%d ahead" % k if k else "a pattern that is no displacing of the published")))

print("\nI. Each parity inverted, on the round changing one parity at a step (Natural Mathematics 2.5)")
for k in (2, 3, 4, 5):
    r = [0, 1]
    for j in range(1, k):
        r = r + [v | (1 << j) for v in reversed(r)]
    m = len(r)
    pos = {v: i for i, v in enumerate(r)}
    on = sorted(set((pos[v ^ (m - 1)] - i) % m for i, v in enumerate(r)))
    st_ = [(pos[r[(i + 1) % m] ^ (m - 1)] - pos[r[i] ^ (m - 1)]) % m for i in range(m)]
    st_ = sorted(set(s if s <= m // 2 else s - m for s in st_))
    print("   %d parities, %2d forms: a form's opposite is %s steps on; as the round steps 1 on its opposite steps %s; the hand %s" % (
        k, m, on, st_, "kept" if k % 2 == 0 else "reversed"))
F_ = lambda v: (-v[1], v[0])
G_ = lambda v: (v[1], -v[0])
two = list(itertools.product(V, V))
print("   two parities: F then G is the form again %s; both inverted is F twice %s" % (
    all(G_(F_(v)) == v for v in two), all(F_(F_(v)) == (-v[0], -v[1]) for v in two)))

print("\nJ. Two selves coupled both ways: one self's carried parities, read as a pair two ways")
st = {"A": ([("s", 1)], []), "B": ([("s", 1)], [])}
seq = []
for t in range(10):
    seq.append(dict(st["A"][0])["s"])
    st = step(st, {("A", 10): "B", ("B", 10): "A"})
old = [(seq[i], seq[i + 1]) for i in range(9)]
new = [(y, x) for x, y in old]
print("   alike selves, A carried %s: (now, next) follows G %s; the same two written (next, now) follow F %s" % (
    " ".join(S[x] for x in seq), all(old[i + 1] == G_(old[i]) for i in range(8)), all(new[i + 1] == F_(new[i]) for i in range(8))))

print("\nK. The relation saying which self releases to which")
functions = code.split("CONNECTORS", 1)[0]
second = functions.split("def _17_co_bi_tri_offering", 1)[1]
print("   in the second function it is read at %d places and written at %d; CONNECTORS and JOINS are read by the functions at %d" % (
    len(re.findall(r"_5_co_bi_co_competencing", second)) - 1,
    len(re.findall(r"_5_co_bi_co_competencing\s*\[[^\]]*\]\s*=[^=]", second)),
    len(re.findall(r"CONNECTORS|JOINS", functions))))


print("   one releasing of a spiral left out of that relation from momentary 101, self 1 releasing to none; and given again at 201")
for n in (3, 5, 7, 9):
    rows = {}
    for label, until in (("left out", 10 ** 9), ("given again", 200)):
        st = {i: ([("s", alt(i))], []) for i in range(n)}
        whole = {(i, 9): (i + 1) % n for i in range(n)}
        less = {k: v for k, v in whole.items() if k != (0, 9)}
        sh = []
        for t in range(700):
            sh.append(tuple(dict(entry(*st[i])[0]).get("s") for i in range(n)))
            st = step(st, less if 100 <= t < until else whole)
        rows[label] = (again(sh), any(0 in r for r in sh[-240:]))
    print("     n = %d: left out, again at %s, a 0 shared %s; given again, again at %s, a 0 shared %s" % (
        n, rows["left out"][0], rows["left out"][1], rows["given again"][0], rows["given again"][1]))
print("   Exhibit ONE's published two spirals crossed, self 1 of each sharing across to self 1 of the other")
for p_, q_ in ((3, 5), (5, 7), (7, 11)):
    st = {("A", i): ([("s", alt(i))], []) for i in range(p_)}
    st.update({("B", i): ([("s", alt(i))], []) for i in range(q_)})
    rel = {(("A", i), 9): ("A", (i + 1) % p_) for i in range(p_)}
    rel.update({(("B", i), 9): ("B", (i + 1) % q_) for i in range(q_)})
    rel[(("A", 0), 10)] = ("B", 0)
    rel[(("B", 0), 10)] = ("A", 0)
    sh = []
    for t in range(700):
        sh.append(tuple(dict(entry(*st[c])[0]).get("s") for c in sorted(st)))
        st = step(st, rel)
    print("     %d and %d selves: again at %s, a 0 shared %s" % (p_, q_, again(sh), any(0 in r for r in sh[-240:])))

print("\nL. Two spirals of n selves opened alike, B opened k momentaries ahead of A, k through one whole round of 4n.")
print("   From momentary 101 to 400 self 1 of each shares across (10) to self 1 of the other; then no longer.")
print("   While crossed: each spiral's sharings again at; of 198 momentaries, those at which the crossing self's")
print("   next is the releasing self's prior inverted; whether a 0 is shared. After: the momentaries B is ahead of A.")


def state_at(n, k):
    st = {i: ([("s", alt(i))], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    for t in range(k):
        st = step(st, rel)
    return st


def twins(n, k, both, T=800):
    sa, sb = state_at(n, 0), state_at(n, k)
    st = {("A", i): sa[i] for i in range(n)}
    st.update({("B", i): sb[i] for i in range(n)})
    rel = {((x, i), 9): (x, (i + 1) % n) for x in "AB" for i in range(n)}
    crossed = dict(rel)
    crossed[(("B", 0), 10)] = ("A", 0)
    if both:
        crossed[(("A", 0), 10)] = ("B", 0)
    sh, car = {"A": [], "B": []}, {"A": [], "B": []}
    for t in range(T):
        for x in "AB":
            car[x].append([dict(st[(x, i)][0])["s"] for i in range(n)])
            sh[x].append(tuple(dict(entry(*st[(x, i)])[0]).get("s") for i in range(n)))
        st = step(st, crossed if 100 <= t < 400 else rel)
    return sh, car


for both in (True, False):
    print("   crossed %s" % ("both ways" if both else "one way, B to A alone, B receiving none from A"))
    for n in (3, 5, 7):
        groups = {}
        for k in range(4 * n):
            sh, car = twins(n, k, both)
            la = sum(car["A"][t + 2][0] == -car["A"][t][n - 1] for t in range(200, 398))
            zero = any(0 in r for r in sh["A"][200:400])
            rounds = (again(sh["A"][:400]), again(sh["B"][:400]))
            after = [d for d in range(4 * n) if all(sh["B"][t] == sh["A"][t + d] for t in range(500, 760 - 4 * n))]
            key = (rounds, "a 0 shared" if zero else "no 0 shared", after[0] if after else None)
            groups.setdefault(key, []).append((k, la))
        for (rounds, zero, after), ks in sorted(groups.items(), key=lambda g: g[1]):
            las = sorted(set(l for _, l in ks))
            kk = [k for k, _ in ks]
            print("     n = %d, k = %s: again at %s and %s, %s, A's crossing self at the living step %s of 198 | after: B %s ahead of A (each parity inverted is %d ahead)" % (
                n, kk if len(kk) <= 4 else "%d of the %d displacings" % (len(kk), 4 * n), rounds[0], rounds[1], zero,
                las[0] if len(las) == 1 else "%d to %d" % (las[0], las[-1]), after, 2 * n))

print("\nM. The torus after a longer colliding with an unchanging form has ended: ring by ring along, the momentaries")
print("   each ring of p selves is ahead of the same ring of the published torus; and the 0s shared in one round")
for p, q in ((3, 5), (5, 7)):
    base = torus(p, q, T=1100)
    P = again(base)
    cells = [(i, j) for i in range(p) for j in range(q)]
    idx = {c: k for k, c in enumerate(cells)}
    for d in (20, 40):
        s2 = torus(p, q, FORMS[0][1], start=100, stop=100 + d, T=1000)
        rings = []
        for j in range(q):
            ring = [idx[(i, j)] for i in range(p)]
            ks = [k for k in range(P) if all(tuple(s2[t][c] for c in ring) == tuple(base[t + k][c] for c in ring) for t in range(600, 900))]
            rings.append(ks[0] if ks else None)
        print("   torus %d by %d, colliding of %d momentaries: again at %s; rings along, by across place: %s ahead; 0s in one round %d, published %d; each parity inverted is %d ahead" % (
            p, q, d, again(s2), rings, sum(r.count(0) for r in s2[600:600 + P]), sum(r.count(0) for r in base[600:600 + P]), P // 2))


print("\nN. The 0 of a spiral. An alike pair: two selves beside each other along carrying one parity; its receiving")
print("   self is the one the other releases to. Spirals of 2 to 9 selves, each opening pattern, 80 momentaries")


def alike(c, n):
    return [i for i in range(n) if c[i] == c[(i - 1) % n]]


def gaps(al, n):
    al = sorted(al)
    return sorted((al[(j + 1) % len(al)] - al[j]) % n for j in range(len(al))) if al else []


tot = number = where = apart = beat = 0
for n in range(2, 10):
    for pat in itertools.product(V, repeat=n):
        sh, car = spiral(n, pattern=list(pat), T=80)
        tot += 1
        number += len(set(len(alike(car[t], n)) for t in range(80))) != 1
        where += any(not set(i for i in range(n) if sh[t][i] == 0) <= set(alike(car[t], n)) for t in range(1, 80))
        apart += len(set(tuple(gaps(alike(car[t], n), n)) for t in range(80))) != 1
        beat += len(set(t % 2 for t in range(2, 80) if 0 in sh[t])) > 1
print("   patterns %d; the number of alike pairs not the same at each momentary: %d; a 0 shared at a self that is" % (tot, number))
print("   not the receiving self of an alike pair: %d; the places between the alike pairs not kept: %d; a 0 shared at" % (where, apart))
print("   two momentaries one after the other: %d" % beat)
print("   the receiving self of the alike pair | the self sharing 0, at twelve momentaries from 121")
for name, f in [("none offered", None)] + FORMS:
    for n in (3, 5):
        sh, car = spiral(n, f, start=40, T=140)
        print("   %-27s n = %d: %s" % (name, n, " ".join(
            ("".join(str(i + 1) for i in alike(car[t], n)) or ".") + "|" + ("".join(str(i + 1) for i in range(n) if sh[t][i] == 0) or ".")
            for t in range(120, 132))))
print("   over one whole round, the momentaries at which self 1 and each self along carry one parity, less those")
print("   at which they carry the two: the whole round with one changing or its inverse, nought with neither")
for name, f, ns_ in (("an odd spiral, its 0 moving on", None, (3, 5, 7, 9)), ("an even spiral, no 0", None, (4, 6)),
                     ("a form returning the other parity colliding", FORMS[3][1], (3, 5, 7))):
    for n in ns_:
        sh, car = spiral(n, f, start=40, T=400)
        P = again(sh)
        print("   %-44s n = %d, round %2d: %s" % (name, n, P, [sum(car[t][0] * car[t][j] for t in range(200, 200 + P)) for j in range(n)]))


print("\nO. The 0's line and each self's changing. At one self, mark 1 at each momentary it shares 0 and nought at")
print("   each other. Over one whole round, add that mark times each self's carried parity, and times each self's")
print("   shared changing. Nought at each self with each self: the 0's line and the changing share nothing.")


def line_products(sh, car, n, P, lo):
    worst = 0
    has = False
    for i in range(n):
        Z = [1 if sh[t][i] == 0 else 0 for t in range(lo, lo + P)]
        has = has or any(Z)
        for j in range(n):
            worst = max(worst, abs(sum(z * car[lo + k][j] for k, z in enumerate(Z))),
                        abs(sum(z * (sh[lo + k][j] or 0) for k, z in enumerate(Z))))
    return has, worst


tally = {}
for n in range(2, 10):
    for pat in itertools.product(V, repeat=n):
        sh, car = spiral(n, pattern=list(pat), T=300)
        has, worst = line_products(sh, car, n, again(sh, 160), 120)
        if has:
            key = "odd" if n % 2 else "even"
            t = tally.setdefault(key, [0, 0])
            t[0] += 1
            t[1] += worst == 0
for key in ("odd", "even"):
    print("   spirals of an %s number of selves, 2 to 9, each opening pattern sharing a 0: patterns %d, at nought throughout %d" % (
        key, tally[key][0], tally[key][1]))
for name, f in FORMS[:3]:
    row = []
    for n in (3, 5, 7):
        sh, car = spiral(n, f, start=40, T=400)
        P = again(sh, 160)
        row.append("n=%d, round %d: %d" % (n, P, line_products(sh, car, n, P, 200)[1]))
    print("   a form %-26s colliding, the largest of those sums: %s" % (name, "; ".join(row)))


print("\nP. Beneath the alternating. Each self inverts at each momentary it shares a parity; take that out by")
print("   inverting each self's carried parity at each second momentary, and follow what still changes.")


def beneath(car, t):
    return tuple(c if t % 2 == 0 else -c for c in car[t])


tot = other = 0
for n in range(2, 10):
    for pat in itertools.product(V, repeat=n):
        sh, car = spiral(n, pattern=list(pat), T=100)
        tot += 1
        other += any({i for i in range(n) if beneath(car, t + 1)[i] != beneath(car, t)[i]} != {i for i in range(n) if sh[t][i] == 0}
                     for t in range(1, 98))
print("   spirals of 2 to 9 selves, each opening pattern: patterns %d; a momentary at which the selves changing" % tot)
print("   beneath the alternating are not exactly the selves sharing 0: %d" % other)
for n in (3, 5, 7):
    sh, car = spiral(n, T=60 + 4 * n)
    forms, who = [beneath(car, 40)], []
    for t in range(41, 41 + 4 * n):
        u = beneath(car, t)
        if u != forms[-1]:
            who.append([i + 1 for i in range(n) if u[i] != forms[-1][i]])
            forms.append(u)
    print("   n = %d, one whole round: %s" % (n, " ".join("".join(S[x] for x in f) for f in forms)))
    print("          the self changing at each step %s; forms %d, not one another %d; %d steps on each parity inverted %s; %d steps on the first form %s" % (
        " ".join("".join(map(str, w)) for w in who), len(forms) - 1, len(set(forms)), n,
        forms[n] == tuple(-x for x in forms[0]), 2 * n, forms[2 * n] == forms[0]))
for name, f in FORMS:
    row = []
    for n in (3, 5):
        car = spiral(n, f, start=40, T=200)[1]
        row.append("n=%d: %s" % (n, " ".join(
            "".join(str(i + 1) for i in range(n) if beneath(car, t + 1)[i] != beneath(car, t)[i]) or "." for t in range(120, 134))))
    print("   a form %-27s the selves changing beneath, 14 momentaries: %s" % (name + ",", "; ".join(row)))


print("\nQ. One momentary at one self, in the code's own names: carried in (3), offered and surfacing (2, 14),")
print("   changing shared (10), carried next (11). Self 1 of a spiral of 3, ten momentaries from 101")


def rows_at_self(n, form=None, start=40, T=140):
    st = {i: ([("s", alt(i))], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    out = []
    for t in range(T):
        if form and t >= start:
            c, o = st[0]
            st[0] = (c, o + [("s", form(t, dict(c)["s"]))])
        c, o = st[0]
        tun, nxt = entry(c, o)
        out.append((dict(c)["s"], " ".join(S[v] for _, v in o) or "none", dict(tun).get("s"), dict(nxt)["s"]))
        st = step(st, rel)
    return out


overlap = True
for name, f in [("none offered from beyond", None), ("a form unchanging at + colliding with this self", FORMS[0][1]),
                ("a form returning the other parity colliding with this self", FORMS[3][1])]:
    rows = rows_at_self(3, f)
    overlap = overlap and all(rows[i][3] == rows[i + 1][0] for i in range(len(rows) - 1))
    print("   " + name)
    print("     momentary   carried in   offered   changing shared   carried next")
    for t in range(100, 110):
        r = rows[t]
        print("     %9d   %10s   %7s   %15s   %s" % (t + 1, S[r[0]], r[1], S[r[2]], S[r[3]]))
print("   the carried next of each momentary is the carried in of the next, at each momentary of the three: %s" % overlap)


print("\nR. The seventeen names inside one run of the resolver's functions, from the code as written")
for part in re.split(r"\ndef ", functions)[1:]:
    print("   %-28s %s" % (part.split("(")[0], sorted(set(int(x) for x in re.findall(r"_(\d+)_[a-z_]+", part)))))
inside = sorted(set(int(x) for x in re.findall(r"_(\d+)_[a-z_]+", functions)))
print("   in the three together: %s; of 1 to 17, at none of them: %s" % (inside, [k for k in range(1, 18) if k not in inside]))
print("   Exhibit ONE's table of a self's four momentaries of exchanging has them at 1-2, 3-4, 5-6 and 7-8, and the")
print("   society's four at 9 to 11, 11 to 13, 13 to 15 and 15 to 17: each of those names is inside the one run.")


print("\nS. Two parity changings in the code: each self inverting at each 1 to 17, and the changing beneath it")


def follow(st, rel, T):
    keys = sorted(st)
    car, sh = [], []
    for t in range(T):
        car.append([dict(st[k][0])["s"] for k in keys])
        sh.append([dict(entry(*st[k])[0]).get("s") for k in keys])
        st = step(st, rel)
    return car, sh


def changes_beneath(car, lo, hi):
    return sum(beneath(car, t + 1) != beneath(car, t) for t in range(lo, hi))


car, sh = follow({0: ([("s", -1)], [])}, {}, 60)
print("   one self coupled with none: carried %s; of 40, the 1 to 17s with a changing beneath: %d; a 0 shared: %s" % (
    " ".join(S[c[0]] for c in car[:8]), changes_beneath(car, 10, 50), any(0 in r for r in sh)))
for n in (4, 6):
    car, sh = follow({i: ([("s", alt(i))], []) for i in range(n)}, {(i, 9): (i + 1) % n for i in range(n)}, 100)
    print("   the published spiral of %d: of 40, with a changing beneath: %d; a 0 shared: %s" % (n, changes_beneath(car, 40, 80), any(0 in r for r in sh[40:])))
for p_, q_ in ((3, 5), (5, 7)):
    st = {("A", i): ([("s", alt(i))], []) for i in range(p_)}
    st.update({("B", i): ([("s", alt(i))], []) for i in range(q_)})
    rel = {(("A", i), 9): ("A", (i + 1) % p_) for i in range(p_)}
    rel.update({(("B", i), 9): ("B", (i + 1) % q_) for i in range(q_)})
    rel[(("A", 0), 10)] = ("B", 0)
    rel[(("B", 0), 10)] = ("A", 0)
    car, sh = follow(st, rel, 400)
    print("   the published spirals of %d and %d crossed: with a changing beneath, the first 100: %d; 301 to 400: %d; a 0 shared after 300: %s" % (
        p_, q_, changes_beneath(car, 0, 100), changes_beneath(car, 300, 399), any(0 in r for r in sh[300:])))
for n in (3, 5, 7, 9):
    car, sh = follow({i: ([("s", alt(i))], []) for i in range(n)}, {(i, 9): (i + 1) % n for i in range(n)}, 8 * n + 40)
    at = [sum(car[t][i] == car[t][(i - 1) % n] for t in range(40, 40 + 4 * n)) for i in range(n)]
    print("   the published spiral of %d, its 4n of %d: changings beneath %d; the 1 to 17s each self is the receiving self of the alike pair: %s" % (
        n, 4 * n, changes_beneath(car, 40, 40 + 4 * n), sorted(set(at))))


print("\nT. Each entry of each self: what surfaces. A parity from carrying selves alone; a parity with a form's")
print("   among those offered; the offerings parting, + and - together; or none. At the last two the code has the")
print("   next carried as the carried inverted, whatever was offered. 200 entries of each self, after the arrangement")
print("   has come to its again.")


def what_surfaces(st, rel, T, lo, form=None, form_from=0, rel2=None, rel2_from=None):
    keys = sorted(st, key=str)
    out = {k: [0, 0, 0, 0] for k in keys}
    for t in range(T):
        formed = bool(form) and t >= form_from
        if formed:
            c, o = st[keys[0]]
            st[keys[0]] = (c, o + [("s", form(t, dict(c)["s"]))])
        if t >= lo:
            for k in keys:
                vals = [v for _, v in st[k][1] if v != 0]
                if not vals:
                    out[k][3] += 1
                elif any((v > 0) != (vals[0] > 0) for v in vals):
                    out[k][2] += 1
                elif formed and k == keys[0]:
                    out[k][1] += 1
                else:
                    out[k][0] += 1
        st = step(st, rel2 if (rel2 and t >= rel2_from) else rel)
    return out


def say(name, out):
    groups = {}
    for k, v in out.items():
        groups.setdefault(tuple(v), []).append(k)
    print("   " + name)
    for v, ks in sorted(groups.items(), key=lambda g: -len(g[1])):
        print("     %d of its selves: from carrying selves alone %3d; with a form's %3d; parting %3d; none %3d" % (len(ks), v[0], v[1], v[2], v[3]))


def ring(n):
    return {i: ([("s", alt(i))], []) for i in range(n)}, {(i, 9): (i + 1) % n for i in range(n)}


say("a self coupled with none", what_surfaces({0: ([("s", -1)], [])}, {}, 300, 100))
for n in (4, 6):
    say("the published spiral of %d" % n, what_surfaces(*ring(n), 300, 100))
for n in (3, 5, 7):
    say("the published spiral of %d" % n, what_surfaces(*ring(n), 100 + 40 * n, 100 + 40 * n - 200))
for p_, q_ in ((3, 5), (5, 7)):
    st = {("A", i): ([("s", alt(i))], []) for i in range(p_)}
    st.update({("B", i): ([("s", alt(i))], []) for i in range(q_)})
    rel = {(("A", i), 9): ("A", (i + 1) % p_) for i in range(p_)}
    rel.update({(("B", i), 9): ("B", (i + 1) % q_) for i in range(q_)})
    rel[(("A", 0), 10)] = ("B", 0)
    rel[(("B", 0), 10)] = ("A", 0)
    say("the published spirals of %d and %d crossed, at their one relation" % (p_, q_), what_surfaces(st, rel, 500, 300))
st, whole = ring(5)
say("a spiral of 5 with one releasing left out", what_surfaces(st, whole, 400, 200, rel2={k: v for k, v in whole.items() if k != (0, 9)}, rel2_from=40))
for name, f in FORMS[:1] + FORMS[2:4]:
    say("a spiral of 5, a form %s colliding with one self" % name, what_surfaces(*ring(5), 400, 200, form=f, form_from=40))


print("\nU. Each passing of the 0 at a self: the 1 to 17s from the 0 arriving among its offerings to its sharing 0;")
print("   and the parity the two alike selves carry at that sharing beside the parity of the two before, one self back")


def entries(n, pattern=None, form=None, start=40, T=200):
    st = {i: ([("s", pattern[i] if pattern else alt(i))], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    rows = []
    for t in range(T):
        if form and t >= start:
            c, o = st[0]
            st[0] = (c, o + [("s", form(t, dict(c)["s"]))])
        rows.append([(dict(st[i][0])["s"], tuple(v for _, v in st[i][1]), dict(entry(*st[i])[0]).get("s")) for i in range(n)])
        st = step(st, rel)
    return rows


def passings(rows, n, lo):
    out = []
    for t in range(lo, len(rows)):
        for i in range(n):
            if rows[t][i][2] == 0:
                t0 = next((u for u in range(t, t - 6, -1) if 0 in rows[u][i][1]), None)
                tp = next((u for u in range(t - 1, t - 8, -1) if rows[u][(i - 1) % n][2] == 0), None)
                if t0 is not None and tp is not None:
                    out.append((i, t - t0 + 1, rows[t][i][0] == -rows[tp][(i - 1) % n][0]))
    return out


total = two = inverted = 0
for n in (3, 5, 7, 9):
    for pat in itertools.product(V, repeat=n):
        for i, took, inv in passings(entries(n, pattern=list(pat), T=80), n, 20):
            total += 1
            two += took == 2
            inverted += inv
print("   published spirals of 3, 5, 7 and 9, each opening pattern: passings %d; in two 1 to 17s %d; the alike" % (total, two))
print("   pair's parity the inverse of its parity one self back %d" % inverted)
for name, f in FORMS[:3]:
    met, others = {}, {}
    for n in (3, 5, 7):
        for i, took, inv in passings(entries(n, form=f, T=300), n, 100):
            d = met if i == 0 else others
            d[took] = d.get(took, 0) + 1
    print("   a form %-24s at the self it meets, passings by 1 to 17s taken %s; at each other self %s" % (name + ":", met, others))
held = []
for n in (3, 5, 7):
    rows = entries(n, form=FORMS[3][1], T=300)
    held.append((n, sum(rows[t][0][0] == rows[t][n - 1][0] for t in range(100, 300)), sum(rows[t][i][2] == 0 for t in range(100, 300) for i in range(n))))
print("   a form returning the other parity: (n, of 200 the 1 to 17s the alike pair is at the self it meets, 0s shared) %s" % held)


print("\nV. A 0 among the offerings. The code as written hands a shared 0 on with the parities shared, and the first")
print("   function passes each offered 0 over. Tried: each arrangement again with each 0 taken out of what is offered")


def same_without_zeros(st, rel, T, form=None, form_from=0):
    a = {k: v for k, v in st.items()}
    b = {k: v for k, v in st.items()}
    first = sorted(st, key=str)[0]
    for t in range(T):
        if form and t >= form_from:
            for d in (a, b):
                c, o = d[first]
                d[first] = (c, o + [("s", form(t, dict(c)["s"]))])
        b = {k: (c, [x for x in o if x[1] != 0]) for k, (c, o) in b.items()}
        if any(entry(*a[k]) != entry(*b[k]) for k in a):
            return False
        a, b = step(a, rel), step(b, rel)
    return True


tried = parted = 0
for n in range(2, 10):
    for pat in itertools.product(V, repeat=n):
        tried += 1
        parted += not same_without_zeros({i: ([("s", pat[i])], []) for i in range(n)}, {(i, 9): (i + 1) % n for i in range(n)}, 60)
for name, f in FORMS:
    for n in (3, 5, 7):
        tried += 1
        parted += not same_without_zeros(*ring(n), 200, form=f, form_from=40)
print("   spirals of 2 to 9, each opening pattern, and spirals of 3, 5 and 7 with each form colliding: tried %d;" % tried)
print("   a 1 to 17 at which some self's shared changing or next carried is other with the 0s taken out: %d" % parted)
print("   one self, by what is offered: none, its carried inverted and shared; the parity it carries, no changing")
print("   and none shared on; the other parity, changed to it and that parity shared on")
for c in V:
    for offs in ([], [c], [-c], [c, -c]):
        tun, nxt = entry([("s", c)], [("s", o) for o in offs])
        print("     carried %s, offered %-6s shared %s, next carried %s" % (S[c], (" ".join(S[o] for o in offs) or "none") + ":", S[dict(tun)["s"]], S[dict(nxt)["s"]]))
