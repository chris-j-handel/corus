"""Which of Exhibit ONE's seventeen names carry a changing from momentary to momentary, and which are the same at every momentary. Each change of a name's bound value within each frame is recorded as the code runs, in each function and in each comprehension inside it, at each momentary, and compared momentary to momentary: the set of values bound, and the sequence of those values. Run from the repository root."""
import sys, copy, types
body = open('Exhibit_ONE_Natural_Resolver_v376.md').read(); ns = {}
exec(body.split('```python', 1)[1].split('```', 1)[0], ns)
F = ns['_17_tri_co_offering']
FUN = {'_1_co_bi_offering': 1, '_9_tri_bi_co_momentarying': 9, '_17_tri_co_offering': 17}
home = {}                                   # each code object, the function it is in
def walk(c, f):
    home[c] = f
    for k in c.co_consts:
        if isinstance(k, types.CodeType): walk(k, f)
for k, f in FUN.items(): walk(ns[k].__code__, f)

def num(v):
    p = v.split('_')
    return int(p[1]) if v.startswith('_') and len(p) > 1 and p[1].isdigit() else None

cur = {}                                    # (function, name) -> bindings at this momentary
def tracer(frame, event, arg):
    if frame.f_code not in home: return None
    f = home[frame.f_code]; last = {}
    def rec(fr, ev, a):
        for k, v in fr.f_locals.items():
            n = num(k)
            if n is None or callable(v): continue
            r = repr(v)
            if last.get(k) != r:            # a change: the value differs from this name's last in this frame
                last[k] = r; cur.setdefault((f, n), []).append(r)
        return rec
    return rec

n = 5
comp = {}
for i in range(n): comp[(i, 9)] = (i + 1) % n; comp[(i, 6)] = (i + 2) % n; comp[(i, 10)] = (i + 3) % n
soc = {i: ([('s', 1 if i % 2 else -1), ('t', 1)], [('s', 1)] if i == 0 else []) for i in range(n)}
T = 40
prot_before = copy.deepcopy((ns['CONNECTORS'], ns['JOINS'], comp))
seen = {}
for t in range(T):
    cur = {}
    sys.settrace(tracer); soc = F(soc, comp); sys.settrace(None)
    for key in set(seen) | set(cur): seen.setdefault(key, [()] * t).append(tuple(cur.get(key, [])))

print(f'Python {sys.version.split()[0]}. A society of five, joined along at 9 and across at 6 and 10, two terms at each self, across {T} momentaries.')
print('1. 1, 9 and 17 are the code\'s three functions: their code is fixed, and what they carry is traced below at the other names.')
print('2. CONNECTORS, JOINS and the society\'s joins passed as 5, the same after every momentary:', prot_before == (ns['CONNECTORS'], ns['JOINS'], comp),
      '; the functions read CONNECTORS or JOINS:', any(w in ns[k].__code__.co_names for k in FUN for w in ('CONNECTORS', 'JOINS')))
print('3. Each name in each function, at each momentary compared with the momentary before: at how many momentaries the set of values bound changed, and the sequence of values; the momentaries at which either changed, when fewer than all; and the set, when it changed at none or at one:')
kinds = {}
for (f, m) in sorted(seen, key=lambda x: (x[1], x[0])):
    v = seen[(f, m)]
    cs = [t + 1 for t in range(1, T) if set(v[t]) != set(v[t - 1])]
    cq = [t + 1 for t in range(1, T) if v[t] != v[t - 1]]
    note = '' if len(cs) == T - 1 and len(cq) == T - 1 else f'; set changed at momentaries {cs}, sequence at {cq}'
    if not cs: note += f'; the set bound at every momentary: {sorted(set(v[0]))}'
    elif len(cs) == 1: note += f'; the set at momentary 1: {sorted(set(v[0]))}, from momentary 2: {sorted(set(v[1]))}'
    print(f'   {m:2d} in {f:2d}: set changed at {len(cs):2d}, sequence at {len(cq):2d} of {T-1}{note}')
    kinds.setdefault(m, []).append((len(cs), len(cq)))
same = [m for m, k in sorted(kinds.items()) if all(q == 0 for _, q in k)]
every = [m for m, k in sorted(kinds.items()) if all(q == T - 1 for _, q in k)]
other = [m for m in sorted(kinds) if m not in same and m not in every]
print('4. The same at every momentary, in every function:', same)
print('   changing at every momentary, in every function:', every)
print('   neither:', other)
