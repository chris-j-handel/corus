"""v402code · sentences of Natural Intelligence's resolving and Natural Naming's resolver names, read by executing.
Deciding nothing. Run, R the set's folder: python3 -I sentences_by_code_check.py R"""
import importlib.util, os, random, itertools
here = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('L', os.path.join(here, 'tables_check_lib.py'))
L = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(L)
S = L.S
def report(name, same, detail=""): print(("SAME      " if same else "NOT SAME  ") + name + ((" :: " + detail) if detail else ""))

# "A sharing at 0 is 0 with each further parity."  "A surfacing is of any number."  each order
ok0 = True; okorder = True
for n in range(0, 7):
    for inc in itertools.product([1, -1, 0], repeat=n):
        nz = [v for v in inc if v]
        want = "empty" if not nz else (nz[0] if len(set(nz)) == 1 else 0)
        if L.surfacing(list(inc)) != want: ok0 = False
report("Parities surfacing: agreeing, one parity; parting, 0, and 0 with each further parity; an empty set, an empty set; a 0 passing over (each receiving to six parities, each order)", ok0)

# "Selves with 17 are same with each order of them."
random.seed(17)
def canon(soc): return {k: (sorted(v[0]), sorted(v[1])) for k, v in soc.items()}
ok = True
for trial in range(300):
    n = random.randint(2, 7)
    selves = list(range(n))
    routes = {}
    for i in selves:
        for nm in (6, 10, 9):
            if random.random() < 0.5: routes[(i, nm)] = random.choice(selves)
    soc = {i: ([(S, random.choice([1, -1]))] if random.random() < 0.8 else [], [(S, random.choice([1, -1, 0])) for _ in range(random.randint(0, 3))]) for i in selves}
    a = dict(soc); b = {k: soc[k] for k in random.sample(selves, n)}
    for _ in range(12):
        a = L.SEVENTEEN(a, routes); b = L.SEVENTEEN(b, routes)
        if canon(a) != canon(b): ok = False
report("Selves with 17-next-existing are same with each order of them (300 same-existing-societies by chance, 12 momentaries each)", ok)

# "With code, 6 is 10, one list with two names": a route by 6, by 10 or by 9 gives the receiving self the same list
ok = True
for nm in (6, 10, 9):
    out = L.SEVENTEEN({"A": ([(S, 1)], []), "B": ([(S, 1)], [])}, {("A", nm): "B"})
    if out["B"][1] != [(S, -1)]: ok = False
report("6 is 10, one list with two names; with 9 the same list goes along", ok)
# all three names routed to one receiving self: the one list three times
out = L.SEVENTEEN({"A": ([(S, 1)], []), "B": ([(S, 1)], [])}, {("A", 6): "B", ("A", 10): "B", ("A", 9): "B"})
print("          a self with 6, 10 and 9 each to one receiving self: that self receives", out["B"][1])

# "Once with a prior, a sharing is with a prior each momentary"
ok = True
for trial in range(2000):
    prior = random.choice([1, -1]); 
    for _ in range(10):
        inc = [random.choice([1, -1, 0]) for _ in range(random.randint(0, 4))]
        _, prior = L.one(prior, inc)
        if prior not in (1, -1): ok = False
report("Once with a prior, a sharing is with a prior each momentary (2,000 selves by chance, 10 momentaries each)", ok)

# a prior of 0, which the code's own 11-next-co-observing forms with no executing: what the lines have of it
print("          a prior given as 0 by a caller: empty surfacing ->", L.one(0, []), "; + surfacing ->", L.one(0, [1]), "; − surfacing ->", L.one(0, [-1]))
