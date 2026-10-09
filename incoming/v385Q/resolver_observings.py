"""Session v385Q. Run from the repository root:  python3 incoming/v385Q/resolver_observings.py
It executes the python block of the newest Exhibit_ONE_Natural_Resolver_v*.md at the root and changes nothing.
One tool for one report: each observing in incoming/v385Q/README.md is a part here, A to Y.
What is observed is Exhibit ONE's code at the arrangements written below. Nothing here observes a living thing.

The arrangements. A spiral of n resolvers: each releasing along (9) to the next, the last to the first, one
sharing, the first resolver carrying -, the resolvers alternating along, none offered from beyond: Exhibit ONE's own
published spiral. A torus of p by q resolvers: each releasing along (9) and sharing across (10), as published.
A colliding: at each momentary from a first to a last, one parity offered to resolver 1 from beyond, by a form
that is unchanging at + or at -, or returns the parity resolver 1 is carrying, or returns the other parity, or
alternates +, - at its own momentaries. Momentaries are numbered from 1. Part X: a sequence of +, - in turn offered
from beyond to one resolver of a torus at any place along and across, one parity at each 1 to 17. Part Y runs no
resolver: it computes rows of the newest Exhibit_TWENTY-EIGHT Equilibria Registry at their own stated mathematics."""
import glob, itertools, os, random, re, sys

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


_shared_now = []


def _first_function_read(carried, offerings):
    out = entry(carried, offerings)
    _shared_now.append(out[0])
    return out


def step_reading(st, rel):
    """One 1 to 17 by Exhibit ONE's second function, unchanged; beside the next state, the shared changing that
    function's own run of the first function returned at each unit, in the order of the units."""
    del _shared_now[:]
    ns["_1_co_bi_tri_offering"] = _first_function_read
    try:
        new = step(st, rel)
    finally:
        ns["_1_co_bi_tri_offering"] = entry
    return new, [dict(tun).get("s") for tun in _shared_now]


def spiral(n, form=None, start=0, stop=None, T=400, pattern=None):
    """Shared changing (10) and carried parity (3) of each resolver at each momentary."""
    st = {i: ([("s", pattern[i] if pattern else alt(i))], []) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    sh, car = [], []
    for t in range(T):
        if form and t >= start and (stop is None or t < stop):
            c, o = st[0]
            st[0] = (c, o + [("s", form(t, dict(c)["s"]))])
        car.append([dict(st[i][0])["s"] for i in range(n)])
        st, now = step_reading(st, rel)
        sh.append(tuple(now))
    return sh, car


_torus_begun = {}


def torus(p, q, form=None, start=0, stop=None, T=600, quiet=None):
    """Shared changing of each resolver at each momentary. quiet = (a, b): resolver 1 releasing and sharing to none
    from momentary a + 1 until b. A colliding run begins from the published torus run once to the colliding's first."""
    cells = [(i, j) for i in range(p) for j in range(q)]
    st = {c: ([("s", alt(c[0] + c[1]))], []) for c in cells}
    rel = {}
    for i, j in cells:
        rel[((i, j), 9)] = ((i + 1) % p, j)
        rel[((i, j), 10)] = (i, (j + 1) % q)
    less = {k: v for k, v in rel.items() if k[0] != (0, 0)}
    sh, first = [], 0
    if form and not quiet and 0 < start <= T:
        if (p, q, start) not in _torus_begun:
            rows = []
            for t in range(start):
                st, now = step_reading(st, rel)
                rows.append(tuple(now))
            _torus_begun[(p, q, start)] = (st, rows)
        st, rows = _torus_begun[(p, q, start)]
        st, sh, first = dict(st), list(rows), start
    for t in range(first, T):
        if form and t >= start and (stop is None or t < stop):
            c, o = st[(0, 0)]
            st[(0, 0)] = (c, o + [("s", form(t, dict(c)["s"]))])
        st, now = step_reading(st, less if quiet and quiet[0] <= t < quiet[1] else rel)
        sh.append(tuple(now))
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
    """At each resolver: momentaries t from lo to hi at which its carried parity at t + 2 is the inverse of the
    carried parity, at t, of the resolver releasing to it."""
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

print("\nB. The living step in a spiral: each resolver's next the releasing resolver's prior inverted, two momentaries on")
tried = parting = 0
for n in range(2, 10):
    for pat in itertools.product(V, repeat=n):
        tried += 1
        parting += living_step(spiral(n, pattern=list(pat), T=60)[1], n, 0, 58) != [58] * n
print("   spirals of 2 to 9 resolvers, each opening pattern, none offered from beyond: patterns %d, parting %d" % (tried, parting))

print("\nC. The same relation while a form collides with resolver 1, momentaries 41 to 140: at each resolver, resolver 1 first,")
print("   the momentaries of 98 at which it is so; then, after the colliding has ended, of 96")
for n in (3, 5, 7, 9):
    for name, f in FORMS:
        car = spiral(n, f, start=40, stop=140, T=240)[1]
        d, a = living_step(car, n, 40, 138), living_step(car, n, 142, 238)
        print("   n = %d, %-27s resolver 1: %2d; each other resolver: %s | after: %s" % (
            n, name, d[0], sorted(set(d[1:])), sorted(set(a))))

print("\nD. The 0 of an odd spiral. Three resolvers, the resolver sharing 0 at each momentary, the colliding from 81")
base3 = spiral(3)[0]
zero_at = lambda row: "".join(str(i + 1) for i, x in enumerate(row) if x == 0) or "."
print("   momentary                    " + " ".join("%3d" % (t + 1) for t in range(77, 96)))
print("   %-28s " % "none offered" + " ".join("%3s" % zero_at(r) for r in base3[77:96]))
for name, f in FORMS:
    print("   %-28s " % name + " ".join("%3s" % zero_at(r) for r in spiral(3, f, start=80)[0][77:96]))
print("   momentaries from one 0 to the next at each resolver, while the colliding continues; published 2n")
for name, f in FORMS:
    row = []
    for n in (3, 5, 7, 9, 11, 13, 15):
        sh = spiral(n, f, start=80, T=500)[0]
        g = sorted(set(x for i in range(n) for x in between_zeros(sh, i, 300, 500)))
        row.append("%d: %s" % (n, g[0] if len(g) == 1 else (g or "no 0")))
    print("   %-28s %s" % (name, "; ".join(row)))
print("   the first momentary each resolver's sharing parts from the published spiral's, along the releasing")
for name, f in FORMS:
    row = []
    for n in (3, 5, 7, 9):
        b, sh = spiral(n)[0], spiral(n, f, start=80)[0]
        first = [next(t + 1 for t in range(400) if sh[t][i] != b[t][i]) for i in range(n)]
        row.append("n=%d from %d, each next resolver %s later" % (n, first[0], sorted(set(y - x for x, y in zip(first, first[1:])))))
    print("   %-28s %s" % (name, "; ".join(row)))
tried = other = 0
for n in (3, 5, 7, 9):
    for name, f in FORMS[:3]:
        for start in range(4 * n):
            tried += 1
            sh = spiral(n, f, start=start, T=360)[0]
            other += sorted(set(x for i in range(n) for x in between_zeros(sh, i, 200, 360))) != [2 * n - 1]
print("   the colliding beginning at each momentary of one whole round of 4n, the three forms with a 0: tried %d, not at 2n - 1: %d" % (tried, other))

print("\nE. Twice and one less: a spiral of n resolvers, a form unchanging at + colliding, its 0 again at")
row = []
for n in (3, 5, 9, 17, 33, 65):
    T = 30 * n + 300
    sh = spiral(n, FORMS[0][1], start=4 * n, T=T)[0]
    g = sorted(set(x for i in (0, n // 2, n - 1) for x in between_zeros(sh, i, T - 9 * n, T)))
    row.append("%d resolvers: %s" % (n, g))
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

print("\nG. A torus of p by q resolvers, the form colliding with one resolver. While it continues: the torus's sharings")
print("   again at; the resolvers whose sharing ever parts from the published torus's. After a colliding of 1 to 40")
print("   momentaries has ended: how many of the 40 leave the torus as published (=), at a displacing of the")
print("   published (d), or at its own round in a pattern that is no displacing of the published (x)")
for p, q in ((3, 5), (5, 7), (3, 7)):
    base = torus(p, q, T=1100)
    P = again(base)
    print("   torus %d by %d, %d resolvers, published: again at %d" % (p, q, p * q, P))
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
        print("     %-27s while: again at %2s, resolvers parting %2d | after: at its own round %d of 40; = %2d, d %2d, x %2d; first not = at %s%s" % (
            name, again(sh), parted, own, kinds.count("="), kinds.count("d"), kinds.count("x"), first,
            "; each further momentary of colliding %s ahead" % sorted(set(runs)) if len(set(runs)) == 1 else ""))

print("\nH. A torus with one resolver releasing and sharing to none, momentaries 101 on; and given again at 201")
for p, q in ((3, 3), (3, 5), (5, 7), (3, 7)):
    base = torus(p, q, T=1100)
    P = again(base)
    a = torus(p, q, quiet=(100, 10 ** 9), T=700)
    b = torus(p, q, quiet=(100, 200), T=800)
    k = ahead(b, base, P, 560, 760)
    print("   torus %d by %d, published again at %d: with the one resolver to none, again at %s; given again: again at %s, %s" % (
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

print("\nJ. Two resolvers coupled both ways: one resolver's carried parities, read as a pair two ways")
st = {"A": ([("s", 1)], []), "B": ([("s", 1)], [])}
seq = []
for t in range(10):
    seq.append(dict(st["A"][0])["s"])
    st = step(st, {("A", 10): "B", ("B", 10): "A"})
old = [(seq[i], seq[i + 1]) for i in range(9)]
new = [(y, x) for x, y in old]
print("   alike resolvers, A carried %s: (now, next) follows G %s; the same two written (next, now) follow F %s" % (
    " ".join(S[x] for x in seq), all(old[i + 1] == G_(old[i]) for i in range(8)), all(new[i + 1] == F_(new[i]) for i in range(8))))

print("\nK. The relation saying which resolver releases to which")
functions = code.split("CONNECTORS", 1)[0]
second = functions.split("def _17_co_bi_tri_offering", 1)[1]
print("   in the second function it is read at %d places and written at %d; CONNECTORS and JOINS are read by the functions at %d" % (
    len(re.findall(r"_5_co_bi_co_competencing", second)) - 1,
    len(re.findall(r"_5_co_bi_co_competencing\s*\[[^\]]*\]\s*=[^=]", second)),
    len(re.findall(r"CONNECTORS|JOINS", functions))))


print("   one releasing of a spiral left out of that relation from momentary 101, resolver 1 releasing to none; and given again at 201")
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
print("   Exhibit ONE's published two spirals crossed, resolver 1 of each sharing across to resolver 1 of the other")
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
    print("     %d and %d resolvers: again at %s, a 0 shared %s" % (p_, q_, again(sh), any(0 in r for r in sh[-240:])))

print("\nL. Two spirals of n resolvers opened alike, B opened k momentaries ahead of A, k through one whole round of 4n.")
print("   From momentary 101 to 400 resolver 1 of each shares across (10) to resolver 1 of the other; then no longer.")
print("   While crossed: each spiral's sharings again at; of 198 momentaries, those at which the crossing resolver's")
print("   next is the releasing resolver's prior inverted; whether a 0 is shared. After: the momentaries B is ahead of A.")


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
            print("     n = %d, k = %s: again at %s and %s, %s, A's crossing resolver at the living step %s of 198 | after: B %s ahead of A (each parity inverted is %d ahead)" % (
                n, kk if len(kk) <= 4 else "%d of the %d displacings" % (len(kk), 4 * n), rounds[0], rounds[1], zero,
                las[0] if len(las) == 1 else "%d to %d" % (las[0], las[-1]), after, 2 * n))

print("\nM. The torus after a longer colliding with an unchanging form has ended: ring by ring along, the momentaries")
print("   each ring of p resolvers is ahead of the same ring of the published torus; and the 0s shared in one round")
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


print("\nN. The 0 of a spiral. An alike pair: two resolvers beside each other along carrying one parity; its receiving")
print("   resolver is the one the other releases to. Spirals of 2 to 9 resolvers, each opening pattern, 80 momentaries")


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
print("   patterns %d; the number of alike pairs not the same at each momentary: %d; a 0 shared at a resolver that is" % (tot, number))
print("   not the receiving resolver of an alike pair: %d; the places between the alike pairs not kept: %d; a 0 shared at" % (where, apart))
print("   two momentaries one after the other: %d" % beat)
print("   the receiving resolver of the alike pair | the resolver sharing 0, at twelve momentaries from 121")
for name, f in [("none offered", None)] + FORMS:
    for n in (3, 5):
        sh, car = spiral(n, f, start=40, T=140)
        print("   %-27s n = %d: %s" % (name, n, " ".join(
            ("".join(str(i + 1) for i in alike(car[t], n)) or ".") + "|" + ("".join(str(i + 1) for i in range(n) if sh[t][i] == 0) or ".")
            for t in range(120, 132))))
print("   over one whole round, the momentaries at which resolver 1 and each resolver along carry one parity, less those")
print("   at which they carry the two: the whole round with one changing or its inverse, nought with neither")
for name, f, ns_ in (("an odd spiral, its 0 moving on", None, (3, 5, 7, 9)), ("an even spiral, no 0", None, (4, 6)),
                     ("a form returning the other parity colliding", FORMS[3][1], (3, 5, 7))):
    for n in ns_:
        sh, car = spiral(n, f, start=40, T=400)
        P = again(sh)
        print("   %-44s n = %d, round %2d: %s" % (name, n, P, [sum(car[t][0] * car[t][j] for t in range(200, 200 + P)) for j in range(n)]))


print("\nO. The 0's line and each resolver's changing. At one resolver, mark 1 at each momentary it shares 0 and nought at")
print("   each other. Over one whole round, add that mark times each resolver's carried parity, and times each resolver's")
print("   shared changing. Nought at each resolver with each resolver: the 0's line and the changing share nothing.")


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
    print("   spirals of an %s number of resolvers, 2 to 9, each opening pattern sharing a 0: patterns %d, at nought throughout %d" % (
        key, tally[key][0], tally[key][1]))
for name, f in FORMS[:3]:
    row = []
    for n in (3, 5, 7):
        sh, car = spiral(n, f, start=40, T=400)
        P = again(sh, 160)
        row.append("n=%d, round %d: %d" % (n, P, line_products(sh, car, n, P, 200)[1]))
    print("   a form %-26s colliding, the largest of those sums: %s" % (name, "; ".join(row)))


print("\nP. Beneath the alternating. Each resolver inverts at each momentary it shares a parity; take that out by")
print("   inverting each resolver's carried parity at each second momentary, and follow what still changes.")


def beneath(car, t):
    return tuple(c if t % 2 == 0 else -c for c in car[t])


tot = other = 0
for n in range(2, 10):
    for pat in itertools.product(V, repeat=n):
        sh, car = spiral(n, pattern=list(pat), T=100)
        tot += 1
        other += any({i for i in range(n) if beneath(car, t + 1)[i] != beneath(car, t)[i]} != {i for i in range(n) if sh[t][i] == 0}
                     for t in range(1, 98))
print("   spirals of 2 to 9 resolvers, each opening pattern: patterns %d; a momentary at which the resolvers changing" % tot)
print("   beneath the alternating are not exactly the resolvers sharing 0: %d" % other)
for n in (3, 5, 7):
    sh, car = spiral(n, T=60 + 4 * n)
    forms, who = [beneath(car, 40)], []
    for t in range(41, 41 + 4 * n):
        u = beneath(car, t)
        if u != forms[-1]:
            who.append([i + 1 for i in range(n) if u[i] != forms[-1][i]])
            forms.append(u)
    print("   n = %d, one whole round: %s" % (n, " ".join("".join(S[x] for x in f) for f in forms)))
    print("          the resolver changing at each step %s; forms %d, not one another %d; %d steps on each parity inverted %s; %d steps on the first form %s" % (
        " ".join("".join(map(str, w)) for w in who), len(forms) - 1, len(set(forms)), n,
        forms[n] == tuple(-x for x in forms[0]), 2 * n, forms[2 * n] == forms[0]))
for name, f in FORMS:
    row = []
    for n in (3, 5):
        car = spiral(n, f, start=40, T=200)[1]
        row.append("n=%d: %s" % (n, " ".join(
            "".join(str(i + 1) for i in range(n) if beneath(car, t + 1)[i] != beneath(car, t)[i]) or "." for t in range(120, 134))))
    print("   a form %-27s the resolvers changing beneath, 14 momentaries: %s" % (name + ",", "; ".join(row)))


print("\nQ. One momentary at one resolver, in the code's own names: carried in (3), offered and surfacing (2, 14),")
print("   changing shared (10), carried next (11). Self 1 of a spiral of 3, ten momentaries from 101")


def rows_at_resolver(n, form=None, start=40, T=140):
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
for name, f in [("none offered from beyond", None), ("a form unchanging at + colliding with this resolver", FORMS[0][1]),
                ("a form returning the other parity colliding with this resolver", FORMS[3][1])]:
    rows = rows_at_resolver(3, f)
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


print("\nS. Two parity changings in the code: each resolver inverting at each 1 to 17, and the changing beneath it")


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
print("   one resolver coupled with none: carried %s; of 40, the 1 to 17s with a changing beneath: %d; a 0 shared: %s" % (
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
    print("   the published spiral of %d, its 4n of %d: changings beneath %d; the 1 to 17s each resolver is the receiving resolver of the alike pair: %s" % (
        n, 4 * n, changes_beneath(car, 40, 40 + 4 * n), sorted(set(at))))


print("\nT. Each entry of each resolver: what surfaces. A parity from carrying resolvers alone; a parity with a form's")
print("   among those offered; the offerings parting, + and - together; or none. At the last two the code has the")
print("   next carried as the carried inverted, whatever was offered. 200 entries of each resolver, after the arrangement")
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
        print("     %d of its resolvers: from carrying resolvers alone %3d; with a form's %3d; parting %3d; none %3d" % (len(ks), v[0], v[1], v[2], v[3]))


def ring(n):
    return {i: ([("s", alt(i))], []) for i in range(n)}, {(i, 9): (i + 1) % n for i in range(n)}


say("a resolver coupled with none", what_surfaces({0: ([("s", -1)], [])}, {}, 300, 100))
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
    say("a spiral of 5, a form %s colliding with one resolver" % name, what_surfaces(*ring(5), 400, 200, form=f, form_from=40))


print("\nU. Each passing of the 0 at a resolver: the 1 to 17s from the 0 arriving among its offerings to its sharing 0;")
print("   and the parity the two alike resolvers carry at that sharing beside the parity of the two before, one resolver back")


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
print("   pair's parity the inverse of its parity one resolver back %d" % inverted)
for name, f in FORMS[:3]:
    met, others = {}, {}
    for n in (3, 5, 7):
        for i, took, inv in passings(entries(n, form=f, T=300), n, 100):
            d = met if i == 0 else others
            d[took] = d.get(took, 0) + 1
    print("   a form %-24s at the resolver it meets, passings by 1 to 17s taken %s; at each other resolver %s" % (name + ":", met, others))
held = []
for n in (3, 5, 7):
    rows = entries(n, form=FORMS[3][1], T=300)
    held.append((n, sum(rows[t][0][0] == rows[t][n - 1][0] for t in range(100, 300)), sum(rows[t][i][2] == 0 for t in range(100, 300) for i in range(n))))
print("   a form returning the other parity: (n, of 200 the 1 to 17s the alike pair is at the resolver it meets, 0s shared) %s" % held)


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
print("   a 1 to 17 at which some resolver's shared changing or next carried is other with the 0s taken out: %d" % parted)
print("   one resolver, by what is offered: none, its carried inverted and shared; the parity it carries, no changing")
print("   and none shared on; the other parity, changed to it and that parity shared on")
for c in V:
    for offs in ([], [c], [-c], [c, -c]):
        tun, nxt = entry([("s", c)], [("s", o) for o in offs])
        print("     carried %s, offered %-6s shared %s, next carried %s" % (S[c], (" ".join(S[o] for o in offs) or "none") + ":", S[dict(tun)["s"]], S[dict(nxt)["s"]]))


print("\nW. Where the 0s are on a torus, across and along together: the units sharing 0 (#) at successive 1 to 17s,")
print("   each group one place along, its marks the places across")


def torus_cells(p, q, T):
    cells = [(i, j) for i in range(p) for j in range(q)]
    st = {c: ([("s", alt(c[0] + c[1]))], []) for c in cells}
    rel = {}
    for i, j in cells:
        rel[((i, j), 9)] = ((i + 1) % p, j)
        rel[((i, j), 10)] = (i, (j + 1) % q)
    out = []
    for t in range(T):
        out.append({c: dict(entry(*st[c])[0]).get("s") for c in cells})
        st = step(st, rel)
    return out


for p, q in ((3, 7), (5, 7), (3, 5)):
    rows = torus_cells(p, q, 200)
    print("   torus of %d along by %d across" % (p, q))
    for t in range(100, 106):
        print("     %3d   %s" % (t + 1, "  ".join("".join("#" if rows[t][(i, j)] == 0 else "." for j in range(q)) for i in range(p))))
    one_each = sum(all(sum(rows[t][(i, j)] == 0 for j in range(q)) == 1 for i in range(p)) for t in range(100, 200))
    moved = sum(all((rows[t + 2][((i + 1) % p, j)] == 0) == (rows[t][(i, j)] == 0) for i in range(p) for j in range(q)) for t in range(100, 198))
    steps = set()
    for t in range(100, 200):
        at = [next((j for j in range(q) if rows[t][(i, j)] == 0), None) for i in range(p)]
        if None not in at:
            steps |= set((at[i] - at[i + 1]) % q for i in range(p - 1))
    print("     of 100, the 1 to 17s with one 0 at each place along: %d; the places across stepping back by %s from one place along" % (one_each, sorted(steps)))
    print("     to the next; of 98, the 1 to 17s after which the whole of the 0s is one place along two 1 to 17s on: %d" % moved)

print("   two spirals crossed, the published 3 and 5: the 1 to 17s at which a crossing unit shares 0, the first 100 and 301 to 400")
st = {("A", i): ([("s", alt(i))], []) for i in range(3)}
st.update({("B", i): ([("s", alt(i))], []) for i in range(5)})
rel = {(("A", i), 9): ("A", (i + 1) % 3) for i in range(3)}
rel.update({(("B", i), 9): ("B", (i + 1) % 5) for i in range(5)})
rel[(("A", 0), 10)] = ("B", 0)
rel[(("B", 0), 10)] = ("A", 0)
early = late = 0
for t in range(400):
    z = sum(dict(entry(*st[k])[0]).get("s") == 0 for k in (("A", 0), ("B", 0)))
    early += z if t < 100 else 0
    late += z if t >= 300 else 0
    st = step(st, rel)
print("     %d and %d" % (early, late))

print("\nX. A sign-changing sequence entering a torus at one resolver: +, - in turn, one at each 1 to 17, offered from")
print("   beyond to a resolver at any place along and across, begun at any 1 to 17, in either order")


_published = {}


def surface(p, q, enters=(), T=200):
    """Carried, shared and offered at each resolver of a torus at each 1 to 17. enters: (place, order, first, last),
    order 0 for +, - in turn, 1 for -, + in turn, or a function giving the parity at each 1 to 17 of the sequence.
    The published torus's first 131 1 to 17s are run once at each size and each run begins from them."""
    if (p, q) not in _published:
        cells = [(i, j) for i in range(p) for j in range(q)]
        rel = {}
        for i, j in cells:
            rel[((i, j), 9)] = ((i + 1) % p, j)
            rel[((i, j), 10)] = (i, (j + 1) % q)
        _published[(p, q)] = (cells, rel, [{c: ([("s", alt(c[0] + c[1]))], []) for c in cells}], [], [], [])
    cells, rel, states, pcar, psh, poff = _published[(p, q)]
    begin = min([first for _, _, first, _ in enters] + [T, 130])
    while len(states) <= begin:
        st = states[-1]
        poff.append({c: [v for _, v in st[c][1]] for c in cells})
        pcar.append({c: dict(st[c][0])["s"] for c in cells})
        new, now = step_reading(st, rel)
        psh.append(dict(zip(cells, now)))
        states.append(new)
    st, car, sh, off = dict(states[begin]), pcar[:begin], psh[:begin], poff[:begin]
    for t in range(begin, T):
        off.append({c: [v for _, v in st[c][1]] for c in cells})
        for at, order, first, last in enters:
            if t >= first and (last is None or t < last):
                c, o = st[at]
                st[at] = (c, o + [("s", order(t - first) if callable(order) else turn(order, t - first))])
        car.append({c: dict(st[c][0])["s"] for c in cells})
        st, now = step_reading(st, rel)
        sh.append(dict(zip(cells, now)))
    return car, sh, off


def turn(order, k):
    return 1 if (k + order) % 2 == 0 else -1


def round_of(sh, cells, tail=120):
    return again([tuple(r[c] for c in cells) for r in sh], tail)


def alike_at(car, p, q, t):
    """The receiving places of the alike pairs across and of the alike pairs along."""
    across = set((i, j) for i in range(p) for j in range(q) if car[t][(i, (j - 1) % q)] == car[t][(i, j)])
    along = set((i, j) for i in range(p) for j in range(q) if car[t][((i - 1) % p, j)] == car[t][(i, j)])
    return across, along


def opened_at(car, t1, bcar, a, b, p, q, cells, lo, span=14):
    """1 or -1 where, from lo after t1, the surface is the published one from its second 1 to 17 with place (a, b) in
    the place of resolver 1, as carried or each parity inverted; 0 where it is neither."""
    for sg in (1, -1):
        if all(car[t1 + k][(i, j)] == sg * bcar[1 + k][((i - a) % p, (j - b) % q)] for k in range(lo, lo + span) for (i, j) in cells):
            return sg
    return 0


for p, q in ((3, 7), (3, 5), (5, 7)):
    cells = [(i, j) for i in range(p) for j in range(q)]
    bcar, bsh, boff = surface(p, q, T=330)
    P = round_of(bsh, cells)
    begins = list(range(100, 100 + P)) if p * q <= 21 else list(range(100, 100 + P, 4))
    ends, wide = (begins[:3], 2) if p * q <= 21 else (begins[:1], 4)
    n = held = begun = other = before_same = 0
    lengths, passing, to_last = [], [], []
    two = no0 = carries = lines = parting_ok = 0
    ended_n = ended_same = ended_inv = 0
    each_n = each_ok = each_alt = each_pairs = 0
    shares_given = zero_there_held = zero_there_begun = zero_first_begun = 0
    for (a, b) in cells:
        for t0 in begins:
            for order in (0, 1):
                T = t0 + 2 * P + 2 * (p + q) + 14
                car, sh, off = surface(p, q, [((a, b), order, t0, None)], T)
                first = next(t for t in range(t0, T) if sh[t] != bsh[t] or car[t + 1] != bcar[t + 1])
                own, came, given = bcar[first][(a, b)], [v for v in boff[first][(a, b)] if v != 0], turn(order, first - t0)
                kind = "held" if came and all(v == own for v in came) and given == -own else ("begun" if not came and given == own else "other")
                held += kind == "held"; begun += kind == "begun"; other += kind == "other"
                n += 1
                shares_given += kind == "held" and sh[first][(a, b)] == given
                zero_first_begun += kind == "begun" and sh[first][(a, b)] == 0
                there = sum(sh[t][(a, b)] == 0 for t in range(first, T))
                zero_there_held += there if kind == "held" else 0
                zero_there_begun += there if kind == "begun" else 0
                lengths.append(first - t0 + 1)
                zs = [t for t in range(t0, first + 1) if bsh[t][(a, b)] == 0]
                passing.append(len(zs) if kind == "held" else None)
                last0 = max(t for t in range(T) if any(v == 0 for v in sh[t].values()))
                to_last.append(last0 - first)
                tail = range(T - 12, T)
                two += all(sh[t] == sh[t - 2] != sh[t - 1] for t in tail)
                no0 += last0 < T - 12
                carries += all(car[t][(i, j)] == turn(order, t - 1 - t0) * (-1) ** ((i - a) % p + (j - b) % q) for t in tail for (i, j) in cells)
                ac, al = alike_at(car, p, q, T - 1)
                lines += ac == set((i, b) for i in range(p)) and al == set((a, j) for j in range(q))
                parting_ok += all((set(off[t][c]) == {1, -1}) == ((c[0] == a or c[1] == b) and c != (a, b)) for t in tail for c in cells)
                if t0 in ends:
                    for d in (first - t0,):
                        c2, s2, _ = surface(p, q, [((a, b), order, t0, t0 + d)], t0 + d + 30) if d else (bcar, bsh, None)
                        before_same += all(c2[t] == bcar[t] for t in range(t0 + d + 30))
                    for d in (40, 41):
                        c2, s2, _ = surface(p, q, [((a, b), order, t0, t0 + d)], t0 + d + 16)
                        sg = opened_at(c2, t0 + d, bcar, a, b, p, q, cells, 0)
                        ended_n += 1; ended_same += sg == 1; ended_inv += sg == -1
                    if (a + b) % wide == 0 and t0 == begins[0]:
                        prev = None
                        for d in range(first - t0 + 1, first - t0 + 9):
                            c2, s2, _ = surface(p, q, [((a, b), order, t0, t0 + d)], t0 + d + 8 * (p + q) + 16)
                            sg = opened_at(c2, t0 + d, bcar, a, b, p, q, cells, 8 * (p + q))
                            each_n += 1; each_ok += sg != 0
                            if prev is not None:
                                each_pairs += 1; each_alt += sg and sg == -prev
                            prev = sg
    print("   torus of %d along by %d across, published again at %d: enterings %d (each place, %d beginnings, both orders)" % (p, q, P, n, len(begins)))
    print("     the first 1 to 17 the sequence changes anything: the surface offering that resolver its own parity alone and")
    print("       the sequence offering the other: %d; the surface offering it no parity and the sequence offering" % held)
    print("       its own: %d; any other: %d. The sequence's 1 to 17s counted to it: %d to %d%s" % (
        begun, other, min(lengths), max(lengths),
        "; that resolver's own-parity-alone 1 to 17 number %s" % sorted(set(x for x in passing if x)) if begun == 0 else ""))
    print("     at that 1 to 17 the entering resolver sharing the sequence's parity, at the first kind: %d; sharing 0, at the second" % shares_given)
    print("       kind: %d; the 0s shared at the entering resolver from that 1 to 17 on, with the sequence: %d at the first kind," % (zero_first_begun, zero_there_held))
    print("       %d at the second" % zero_there_begun)
    print("     ended with nothing changed: the surface as published throughout: %d of %d" % (before_same, n * len(ends) // len(begins)))
    print("     continuing: 1 to 17s from the first changing to the last 0 shared anywhere: %d to %d; then no 0 shared: %d;" % (min(to_last), max(to_last), no0))
    print("       the sharings again at 2: %d; each resolver carrying what the sequence offered the 1 to 17 before, inverted" % two)
    print("       once for each place along and across from the entering place: %d; each alike pair across received at the" % carries)
    print("       entering place across and each alike pair along at the entering place along: %d; the resolvers offered" % lines)
    print("       + and - together being those at the entering place across or along, the entering resolver apart: %d" % parting_ok)
    print("     ended after 40 or 41: the published surface from its second 1 to 17 with the entering place in the place of")
    print("       resolver 1, from the ending on: %d of %d, as carried %d, each parity inverted %d" % (ended_same + ended_inv, ended_n, ended_same, ended_inv))
    print("     ended at each of eight lengths from the first changing, read %d on: that same surface: %d of %d; each" % (8 * (p + q), each_ok, each_n))
    print("       parity inverted from one length to the next: %d of %d" % (each_alt, each_pairs))
    if (p, q) == (3, 7):
        for t0 in (100, 101):
            print("     beginning at %d, the 0s shared then with no sequence (#), and the sequence's 1 to 17s counted to the first changing at each entering place," % (t0 + 1))
            print("       order +, - | order -, +")
            rows = {}
            for (a, b) in cells:
                for order in (0, 1):
                    car, sh, off = surface(p, q, [((a, b), order, t0, None)], t0 + 3 * P)
                    rows[(a, b, order)] = next(t for t in range(t0, t0 + 3 * P) if sh[t] != bsh[t] or car[t + 1] != bcar[t + 1]) - t0 + 1
            for a in range(p):
                print("       along %d   %s   %s | %s" % (a + 1, "".join("#" if bsh[t0][(a, j)] == 0 else "." for j in range(q)),
                      " ".join("%2d" % rows[(a, j, 0)] for j in range(q)), " ".join("%2d" % rows[(a, j, 1)] for j in range(q))))

print("   the same sequence ended at a length of 1 to 29, places, beginnings and orders by a seeded choosing, read later:")
print("   the surface a published one at some place along and across, at some 1 to 17 of its round, as carried or each")
print("   parity inverted")
for p, q, tries, later in ((3, 7, 60, 100), (3, 5, 60, 100), (5, 7, 30, 300)):
    cells = [(i, j) for i in range(p) for j in range(q)]
    bcar, bsh, _ = surface(p, q, T=160)
    P = round_of(bsh, cells)
    known = set(tuple(sg * bcar[100 + dk + k][((i - da) % p, (j - db) % q)] for k in range(10) for (i, j) in cells)
                for da in range(p) for db in range(q) for dk in range(P) for sg in (1, -1))
    rnd, ok, own = random.Random(385), 0, 0
    for _ in range(tries):
        at, t0, d, order = rnd.choice(cells), 60 + rnd.randrange(P), rnd.randrange(1, 30), rnd.randrange(2)
        car, sh, _ = surface(p, q, [(at, order, t0, t0 + d)], t0 + d + later + 130)
        ok += tuple(car[t0 + d + later + k][c] for k in range(10) for c in cells) in known
        own += round_of(sh, cells) == P
    print("     torus %d by %d: tried %d, a published surface %d, at the published round %d; published surfaces by place, 1 to 17 and inverting: %d" % (p, q, tries, ok, own, len(known)))

print("   other sequences continuing at one resolver, twelve enterings each: the sharings again at 2; the 0s shared in the last 24")
for p, q in ((3, 7), (3, 5)):
    cells = [(i, j) for i in range(p) for j in range(q)]
    for name, f in (("+, - in turn", lambda k: turn(0, k)), ("two +, two -", lambda k: 1 if (k // 2) % 2 == 0 else -1),
                    ("+, +, -", lambda k: 1 if k % 3 < 2 else -1), ("unchanging at +", lambda k: 1), ("unchanging at -", lambda k: -1)):
        two, zeros = 0, []
        for at in cells[::max(1, len(cells) // 6)][:6]:
            for t0 in (100, 101):
                car, sh, _ = surface(p, q, [(at, f, t0, None)], t0 + 120)
                two += all(sh[t] == sh[t - 2] for t in range(t0 + 96, t0 + 120))
                zeros.append(sum(v == 0 for t in range(t0 + 96, t0 + 120) for v in sh[t].values()))
        print("     torus %d by %d, %-16s again at 2: %2d of 12; 0s %d to %d" % (p, q, name + ":", two, min(zeros), max(zeros)))

print("   two and three such sequences at once at different places, places, beginnings and orders by a seeded choosing")
for p, q in ((3, 7), (3, 5), (5, 7), (3, 9), (3, 11)):
    cells = [(i, j) for i in range(p) for j in range(q)]
    for N in (2, 3):
        rnd = random.Random(385 + N)
        n = two = no0 = follows = lines = 0
        for _ in range(30):
            places = rnd.sample(cells, N)
            ens = [(pl, rnd.randrange(2), 60 + rnd.randrange(24), None) for pl in places]
            T = 84 + 6 * (p + q) + 40
            car, sh, _ = surface(p, q, ens, T)
            n += 1
            two += all(sh[t] == sh[t - 2] != sh[t - 1] for t in range(T - 12, T))
            no0 += not any(v == 0 for t in range(T - 12, T) for v in sh[t].values())
            follows += sum(all(car[t][pl] == turn(order, t - 1 - t0) for t in range(T - 12, T)) for pl, order, t0, _ in ens)
            ac, al = alike_at(car, p, q, T - 1)
            lines += set(j for i, j in ac) <= set(b for a, b in places) and set(i for i, j in al) <= set(a for a, b in places)
        print("     torus %d by %2d, %d sequences, tried %d: again at 2: %d; no 0 shared: %d; each alike pair received at an entering place across" % (p, q, N, n, two, no0))
        print("       or along: %d; the entering resolvers carrying what their own sequence offered the 1 to 17 before: %d of %d" % (lines, follows, n * N))

print("   a torus with an even count along or across: the published sharings again at, its 0s in a round; one such sequence,")
print("   each place, two beginnings, both orders, 49 or 50 1 to 17s of sequence: the surface as published throughout")
for p, q in ((4, 6), (4, 7), (3, 6), (6, 5)):
    cells = [(i, j) for i in range(p) for j in range(q)]
    bcar, bsh, _ = surface(p, q, T=150)
    P = round_of(bsh, cells, 40)
    n = same = 0
    for at in cells:
        for t0 in (100, 101):
            for order in (0, 1):
                car, sh, _ = surface(p, q, [(at, order, t0, None)], 150)
                n += 1
                same += car == bcar and sh == bsh
    print("     torus %d by %d: again at %d, 0s %d; enterings %d, as published throughout %d" % (p, q, P, sum(v == 0 for t in range(100, 100 + P) for v in bsh[t].values()), n, same))

print("   where the 0 is shared on the published torus, 200 1 to 17s from 101: the 0s shared; those at a resolver receiving an")
print("   alike pair across and an alike pair along; such resolvers; those of them sharing 0")
for p, q in ((3, 7), (3, 5), (5, 7)):
    cells = [(i, j) for i in range(p) for j in range(q)]
    car, sh, _ = surface(p, q, T=300)
    zeros = at_both = both = 0
    for t in range(100, 300):
        ac, al = alike_at(car, p, q, t)
        both += len(ac & al)
        zeros += sum(sh[t][c] == 0 for c in cells)
        at_both += sum(sh[t][c] == 0 for c in ac & al)
    print("     torus %d by %d: %d; %d; %d; %d" % (p, q, zeros, at_both, both, at_both))

print("\nY. The Equilibria Registry's arrivals that state their own mathematics, each at its own stated continuing: is")
print("   what the arrival names kept (K), or is it not possible by the arrival's own requirements (N). Exact arithmetic;")
print("   each line says the reading taken. This part runs no resolver; it is of the registry's rows 4.3 to 4.12 alone.")
print("   Left out: the rows at the older resolver, the rows needing a table or a choice pair their own words do not carry,")
print("   the rows of radiation, gases and climate, and four rows whose own words leave nothing to compute.")
from fractions import Fraction as Fr


def stationary(law, moves):
    """law: {value: weight}; moves: {value: {next value: probability}}. The law after one continuing equals the law."""
    after = {}
    for v, w in law.items():
        for n, p in moves[v].items():
            after[n] = after.get(n, 0) + w * p
    return all(after.get(v, 0) == w for v, w in law.items()) and all(v in law for v in after)


def balanced(law, moves):
    return all(law[a] * moves[a].get(b, 0) == law[b] * moves[b].get(a, 0) for a in law for b in law)


arrivals = []


def arrival(name, reading, kept):
    arrivals.append((name, kept))
    print("     %-5s %s  %s" % (name, "K" if kept else "N", reading))


h = Fr(1, 2)
# mechanics, the registry's F(x, v) = (x + tau v, v)
F = lambda x, v, tau: (x + tau * v, v)
taus = [Fr(1, 3), 1, Fr(7, 2), 10]
arrival("NY23", "(x*, 0) under F(x,v) = (x + tau v, v): the pair the same at each tau tried", all(F(Fr(5, 7), 0, t) == (Fr(5, 7), 0) for t in taus))
arrival("NY24", "rest, v = 0, position free: v the same and x the same at each tau", all(F(x, 0, t) == (x, 0) for x in (0, 1, Fr(-9, 4)) for t in taus))
u = Fr(3, 5)
arrival("NY21", "v = u follows translation by tau u, u specified", all(F(x, u, t) == (x + t * u, u) for x in (0, 2) for t in taus))
arrival("NY22", "the same with some u, not specified", all(F(x, w, t) == (x + t * w, w) for w in (Fr(-1, 2), 0, 4) for x in (0, 2) for t in taus))
# dynamical systems
for name, k, note in (("NY09", Fr(-1, 2), "T(p,r) = (1-p, -r/2)"), ("NY11", Fr(-1), "T(p,r) = (1-p, -r)"), ("NY12", Fr(-2), "T(p,r) = (1-p, -2r)")):
    p, r, ok = 0, Fr(0), True
    for _ in range(12):
        p, r = 1 - p, k * r
        ok = ok and r == 0
    arrival(name, "E: r = 0 under %s: r is 0 at each of 12 occurrences, p alternating" % note, ok)
r, shrink = Fr(1, 8), True
for _ in range(12):
    r2 = Fr(-1, 2) * r
    shrink = shrink and abs(r2) < abs(r) and r2 != 0
    r = r2
arrival("NY10", "the same E and T(p,r) = (1-p, -r/2) with asymptotic stability: a departure halves at each occurrence", shrink)
dU = lambda x: x ** 3 - x ** 2 - 2 * x
U = lambda x: Fr(x) ** 4 / 4 - Fr(x) ** 3 / 3 - Fr(x) ** 2
arrival("NY13", "U = x^4/4 - x^3/3 - x^2 under x' = -U'(x): x = -1 is at rest, a minimum, and U(2) is lower", dU(-1) == 0 and U(-1) < U(Fr(-9, 10)) and U(-1) < U(Fr(-11, 10)) and U(2) < U(-1))
arrival("NY14", "the same U: x = 2 is at rest and U(2) is the least of the three resting places", dU(2) == 0 and U(2) < U(-1) and U(2) < U(0))
# laws on values
five = "ABCDE"
arrival("NY15", "the uniform law on A->B->C->D->E->A: the law the same after each continuing", stationary({c: Fr(1, 5) for c in five}, {c: {five[(i + 1) % 5]: 1} for i, c in enumerate(five)}))
arrival("NY16", "equal weights on two values exchanged: the law the same, and each passage balanced by its reverse", stationary({"A": h, "B": h}, {"A": {"B": 1}, "B": {"A": 1}}) and balanced({"A": h, "B": h}, {"A": {"B": 1}, "B": {"A": 1}}))
arrival("NY17", "A->B, B->A, X->B, weights 1/2, 1/2, 0: the law the same", stationary({"A": h, "B": h, "X": Fr(0)}, {"A": {"B": 1}, "B": {"A": 1}, "X": {"B": 1}}))
# chemistry
kf, kb = Fr(3), Fr(5)
a = kb / (kf + kb)
b = 1 - a
arrival("NY27", "A <=> B, total 1, k+ a = k- b: a' = -k+ a + k- b is 0", kf * a == kb * b and -kf * a + kb * b == 0)
f, w = Fr(2), Fr(7)
x = (f + w) / 2
arrival("NY28", "F <=> X <=> W, f and w maintained: x = (f+w)/2 gives x' = (f - x) + (w - x) = 0", (f - x) + (w - x) == 0)
K1, K2 = Fr(2), Fr(3)
K3 = 1 / (K1 * K2)
ca = Fr(1)
cb, cc = K1 * ca, K2 * K1 * ca
arrival("NY29", "A <=> B <=> C <=> A with K1 K2 K3 = 1: each of the three balanced by its own reverse", cb == K1 * ca and cc == K2 * cb and ca == K3 * cc)
k = Fr(1)
law = {0: Fr(1, 4), 1: Fr(1, 2), 2: Fr(1, 4)}
rate = {0: {1: 2 * k}, 1: {0: k, 2: k}, 2: {1: 2 * k}}
flow = all(sum(law[m] * rate[m].get(n, 0) for m in law) == law[n] * sum(rate[n].values()) for n in law)
arrival("NY31", "two molecules, A <=> B, equal constants: the law 1/4, 1/2, 1/4 on the count of B the same, each passage balanced", flow and all(law[m] * rate[m].get(n, 0) == law[n] * rate[n].get(m, 0) for m in law for n in law))
# heat
CA, CB, Utot, kappa = Fr(2), Fr(3), Fr(10), Fr(1, 7)
du = lambda uu, kap: kap * ((Utot - uu) / CB - uu / CA)
ustar = CA * Utot / (CA + CB)
arrival("NY41", "two bodies, insulated, kappa = 0: each split of U the same at each step", all(du(uu, 0) == 0 for uu in (1, 4, Fr(13, 2))))
arrival("NY42", "the same with kappa > 0: u = C_A U/(C_A + C_B) gives u' = 0, and at no other split tried", du(ustar, kappa) == 0 and all(du(uu, kappa) != 0 for uu in (1, 3, 5, 9)))
uu, nearer, reached = Fr(1), True, False
for _ in range(40):
    nxt = uu + du(uu, kappa)
    nearer = nearer and abs(nxt - ustar) < abs(uu - ustar)
    reached = reached or nxt == ustar
    uu = nxt
arrival("SA07", "the same contact approached from another split: nearer at each of 40 steps, and one resting split", nearer and du(ustar, kappa) == 0)
# populations and exchange
rr, K = Fr(2, 3), Fr(50)
logistic = lambda N: rr * N * (1 - N / K)
arrival("NY36", "N' = r N (1 - N/K): N = 0 and N = K give N' = 0", logistic(0) == 0 and logistic(K) == 0)
arrival("NY37", "the same at N = K: births r N and deaths r N^2/K equal and not 0", rr * K == rr * K * K / K and rr * K != 0)
arrival("NY38", "x' = x (1 - x): x = 0 and x = 1 give x' = 0", all(xx * (1 - xx) == 0 for xx in (0, 1)))
arrival("NY40", "each payoff 0: x' = 0 at each x tried", all(xx * (0 - 0) == 0 for xx in (0, Fr(1, 3), 1)))
clears = [q for q in (Fr(1, 3), Fr(1, 2), Fr(1), Fr(2), Fr(3)) if 1 / q == 1 and q == 1]  # good 1 asked 1/q of 1; good 2 asked q of 1
arrival("NY34", "endowments (1,0) and (0,1), each wanting the other's good, prices (q,1): of five prices both goods clear at q = 1 alone, and q(next) = 1", clears == [Fr(1)])
arrival("NY35", "the same with q(next) = 1/q: at q = 1 the next price is 1", 1 / clears[0] == clears[0])
# signs and sequences
arrival("SA04", "values -1, 0, +1, continuing exchanging -1 and +1: each next is in the collection", all(-vv in (-1, 0, 1) for vv in (-1, 0, 1)))
arrival("SA18", "self and other at opposite signs, continuing reversing both: opposite at each next", all((-c, -t)[0] == -(-c, -t)[1] for c, t in ((1, -1), (-1, 1))))
arrival("NY02", "opposition of one sign pair under joint reversal: opposite at each next", all(-c == -(-t) for c, t in ((1, -1), (-1, 1))))


def window_keeps(win, steps=24):
    win = list(win)
    for _ in range(steps):
        win = win[1:] + [-win[-1]]
        if sum(win) != 0:
            return False
    return True


keeping = [wn for n in (2, 4, 6) for wn in itertools.product(V, repeat=n) if sum(wn) == 0 and window_keeps(wn)]
arrival("SA12", "a window of signs, the oldest removed and the opposite of the latest appended, mean 0 at each next: the windows of 2, 4 and 6 keeping it are the %d alternating ones" % len(keeping), len(keeping) > 0 and all(all(wn[i] == -wn[i + 1] for i in range(len(wn) - 1)) for wn in keeping))
arrival("SA13", "a window whose next permits either sign, S(next) = S(now) + y - a: so at each of the 64 cases of four signs and y", all(sum(list(wn[1:]) + [y]) == sum(wn) + y - wn[0] for wn in itertools.product(V, repeat=4) for y in V))
joins = {(0, 1), (1, 2)}
arrival("SA15", "immediate-next joins 0 to 1 and 1 to 2 and is taken as one relation with a transitive same-form: 0 to 2 would be joined, and it is not", (0, 2) in joins)
# pi_next * 1/3 = pi * 2/3 round three values gives pi = 8 pi
p0 = Fr(1)
p1, p2 = 2 * p0, 4 * p0
arrival("SA16", "one normalized law balanced round three values, forward 2/3 and reverse 1/3: each weight twice the one before, round three, asks a weight 8 times itself", 2 * p2 == p0)
import math
arrival("SA14", "two compartments at one temperature, pressures 3 and 1, taken as no available work: the work at one temperature between them is n R T ln 3", math.log(3) == 0)

kept = [n for n, kk in arrivals if kk]
print("   arrivals computed: %d of the registry's 63; kept under its own stated continuing: %d; not possible by its own" % (len(arrivals), len(kept)))
print("   requirements: %d, %s" % (len(arrivals) - len(kept), ", ".join(n for n, kk in arrivals if not kk)))
print("   the registry's own exclusions at 5.2, computed again:")
Forb = lambda P, Q: (-Q, P)
pairs = list(itertools.product(V, repeat=2))
left = 0
proper = [set(s) for n in (1, 2, 3) for s in itertools.combinations(pairs, n)]
for sset in proper:
    for start in sset:
        cur, out = start, False
        for _ in range(3):
            cur = Forb(*cur)
            out = out or cur not in sset
        left += out
print("     F(P,Q) = (-Q,P): each of the %d nonempty proper sets of pairs is left within three advances from each pair in it: %d of %d" % (len(proper), left, sum(len(s) for s in proper)))
print("     two molecules: the passing one way and the other are alike at the count of B %s, and each passing from 1 goes to %s" % ([nB for nB in (0, 1, 2) if (2 - nB) == nB], sorted({0, 2})))
print("     so at one arrangement the count changes at each passing and the law of the counts is kept (NY31 above)")
