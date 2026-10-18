"""Session v385M: the claims of Natural Intelligence 2.4, 3.5 and 4.13 and of Exhibit ONE's tables that held when
recomputed, and one finding about when a self keeps its value (part G).
Run from the repository root:  python3 incoming/v385M/tables_check.py
It executes the python block of the newest Natural_Intelligence_v*.md at the root and changes nothing."""
import glob, itertools, re

path = sorted(p for p in glob.glob("Natural_Intelligence_v*.md"))[-1]
code = re.search(r"```python\n(.*?)```", open(path, encoding="utf-8").read(), re.S).group(1)
ns = {}
exec(code, ns)
entry, step = ns["_1_co_bi_tri_offering"], ns["_17_co_bi_tri_offering"]
print("read:", path)
V = (1, -1)
SYM = {1: "+", -1: "-", 0: "0"}

print("\nA. 2.4: the sixteen ways to name a next from (prior, now)")
states = [(p, n) for p in V for n in V]
whole = 0
for outs in itertools.product(V, repeat=4):
    f = dict(zip(states, outs))
    m = {s: (s[1], f[s]) for s in states}
    if len(set(m.values())) < 4:
        continue
    whole += 1
    seen, cycles = set(), []
    for s in states:
        length, t = 0, s
        while t not in seen:
            seen.add(t); t = m[t]; length += 1
        if length:
            cycles.append(length)
    uses_now = any(f[(p, 1)] != f[(p, -1)] for p in V)
    print("   next for (++,+-,-+,--) = %s  cycles %s  stills %d  next changes with now: %s"
          % ("".join(SYM[o] for o in outs), sorted(cycles), cycles.count(1), uses_now))
print("   carrying the prior whole: %d of 16 (said: 4); losing it: %d (said: 12)" % (whole, 16 - whole))

print("\nB. 2.4: of 256 maps of the four joint forms, one cycle of four changing one parity a step")
count = 0
for outs in itertools.product(states, repeat=4):
    m = dict(zip(states, outs))
    if any(sum(a != b for a, b in zip(s, m[s])) != 1 for s in states):
        continue
    t, seen = states[0], []
    while t not in seen:
        seen.append(t); t = m[t]
    count += len(seen) == 4 and t == states[0]
print("   found %d (said: 2)" % count)

def key(st):
    return tuple(sorted((k, tuple(sorted(c)), tuple(sorted(o))) for k, (c, o) in st.items()))

def run(st, rel, limit=40000):
    seen = {key(st): 0}
    for t in range(1, limit):
        st = step(st, rel)
        k = key(st)
        if k in seen:
            return t - seen[k], seen[k], st
        seen[k] = t
    return None, None, st

def alt(i):
    return -1 if i % 2 == 0 else 1

print("\nC. Exhibit ONE, a spiral of selves: momentaries to the releasings again (said: 4n at odd n, 2 at even)")
bad = []
for n in list(range(1, 12)) + [17, 59]:
    st = {i: ([("s", alt(i))], []) for i in range(n)}
    got = run(st, {(i, 9): (i + 1) % n for i in range(n)})[0]
    said = 4 * n if n % 2 else 2
    if got != said:
        bad.append((n, said, got))
print("   13 rows recomputed, rows parting from the table:", bad)

def torus(p, q):
    st = {(i, j): ([("s", alt(i + j))], []) for i in range(p) for j in range(q)}
    rel = {}
    for i in range(p):
        for j in range(q):
            rel[((i, j), 9)] = ((i + 1) % p, j)
            rel[((i, j), 10)] = (i, (j + 1) % q)
    return run(st, rel)[:2]

print("\nD. Exhibit ONE, a torus of selves (said, both odd, p the smaller: q at q more than twice p, 4p at each other q)")
rows = [(1,3,3,2),(2,3,2,1),(1,5,5,2),(3,3,12,6),(3,5,12,6),(3,7,7,8),(3,13,13,8),(5,7,20,12),(5,11,11,14),(7,17,17,20),(17,59,59,50)]
bad = [(p, q, torus(p, q)) for p, q, per, frm in rows if torus(p, q) != (per, frm)]
print("   11 table rows recomputed, rows parting:", bad)
bad, pairs = [], 0
for p in range(1, 16, 2):
    for q in range(p, 34, 2):
        if p == q == 1:
            continue
        pairs += 1
        said = q if q > 2 * p else 4 * p
        if torus(p, q)[0] != said:
            bad.append((p, q))
print("   the rule at %d further pairs of odd p to 15 and q to 33, pairs parting: %s" % (pairs, bad))

def crossed(p, q, pa=None, pb=None):
    pa = pa or [alt(i) for i in range(p)]
    pb = pb or [alt(i) for i in range(q)]
    st = {("A", i): ([("s", pa[i])], []) for i in range(p)}
    st.update({("B", i): ([("s", pb[i])], []) for i in range(q)})
    rel = {(("A", i), 9): ("A", (i + 1) % p) for i in range(p)}
    rel.update({(("B", i), 9): ("B", (i + 1) % q) for i in range(q)})
    rel[(("A", 0), 10)] = ("B", 0)
    rel[(("B", 0), 10)] = ("A", 0)
    return run(st, rel)

print("\nE. Exhibit ONE, two spirals crossed (said: releasings again at 2, from the momentary listed)")
rows = [(2,3,7),(3,5,12),(5,7,20),(7,11,28),(11,13,44),(13,17,52),(17,59,119),(9,15,36)]
bad = [(p, q) for p, q, frm in rows if crossed(p, q)[:2] != (2, frm)]
print("   8 rows recomputed, rows parting:", bad)

print("\nF. 4.13: from any carried patterns but all selves at one parity, two crossed spirals of 2 to 6 selves,")
print("   different numbers and one odd, come to each self alternating, the crossing selves opposite")
tried = failed = 0
for p in range(2, 7):
    for q in range(2, 7):
        if p == q or (p % 2 == 0 and q % 2 == 0):
            continue
        for pat in itertools.product(V, repeat=p + q):
            if len(set(pat)) == 1:
                continue
            tried += 1
            per, _, st = crossed(p, q, list(pat[:p]), list(pat[p:]))
            failed += per != 2 or dict(st[("A", 0)][0])["s"] == dict(st[("B", 0)][0])["s"]
print("   opening patterns tried: %d, patterns parting from the saying: %d" % (tried, failed))

print("\nG. When does one self keep the value it carries? each list of up to three offerings, carrying + or -")
kept = set()
for c in V:
    for length in range(4):
        for offs in itertools.product((1, -1, 0), repeat=length):
            _, nxt = entry([("s", c)], [("s", o) for o in offs])
            if dict(nxt)["s"] == c:
                kept.add((SYM[c], "".join(sorted({SYM[o] for o in offs}))))
print("   kept only at (carried, values offered):", sorted(kept))
print("   so a self keeps its value only when its own value arrives, and at each other arrival, none included, it changes")
