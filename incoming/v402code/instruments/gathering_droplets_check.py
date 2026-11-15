"""v402code · two droplets of Natural Resolver's gathering, read by executing. Deciding nothing.
Run, R the set's folder: python3 -I gathering_droplets_check.py R"""
import importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
_sp = importlib.util.spec_from_file_location('L', os.path.join(here, 'tables_check_lib.py'))
L = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(L)
S = L.S
def report(name, same, detail=""): print(("SAME      " if same else "NOT SAME  ") + name + ((" :: " + detail) if detail else ""))

# droplet at 'A torus of selves': the second reading, one self only with a prior: 1 · 5 is 4 and 3 · 13 is 12
def torus_one_prior(p, q, T=400):
    selves = [(i, j) for i in range(p) for j in range(q)]
    priors = {k: None for k in selves}; priors[(0, 0)] = -1
    routes = {}
    for (i, j) in selves:
        routes[((i, j), 9)] = ((i + 1) % p, j); routes[((i, j), 10)] = (i, (j + 1) % q)
    sh, pri = L.run(priors, routes, T)
    seq = [tuple(s[k] for k in sorted(s)) for s in sh]
    return L.eventual(seq, maxp=4 * max(p, q) + 4)
got = {(1, 5): torus_one_prior(1, 5), (3, 13): torus_one_prior(3, 13)}
report("Droplet, a torus's opening by its second reading, one self only with a prior: 1 · 5 is 4 and 3 · 13 is 12",
       got[(1, 5)][1] == 4 and got[(3, 13)][1] == 12, "found (from momentary less one, again by): " + str(got))
table3 = {(1, 3): 3, (2, 3): 2, (1, 5): 5, (3, 3): 12, (3, 5): 12, (3, 7): 7, (3, 13): 13, (5, 7): 20, (5, 11): 11, (7, 17): 17}
second = {k: torus_one_prior(*k)[1] for k in table3}
print("          the table's rows by the second reading (17 · 59 aside): table", table3)
print("                                                               found", second)
print("          rows where the second reading has the table's cell:", sorted(k for k in table3 if table3[k] == second[k]))

# droplet at 'A spiral opening with an empty prior': self 1 with prior −, each other self with no prior, and no + from no self
want3 = ["+··", "−+·", "+−+", "++−", "−−+", "+−−", "−++", "+−+"]
want5 = ["+····", "−+···", "+−+··", "−+−+·", "+−+−+", "++−+−", "−−+−+", "+−−+−"]
bad = []
for n, want in ((3, want3), (5, want5)):
    pr = {("", i): None for i in range(n)}; pr[("", 0)] = -1
    ro = {(("", i), 9): ("", (i + 1) % n) for i in range(n)}
    _, pri = L.run(pr, ro, 8)
    got = ["".join(L.sym(x[("", i)]) for i in range(n)) for x in pri]
    if got != want: bad.append((n, got))
report("Droplet, a spiral opening with self 1's prior − and each other self with no prior: each row of the table as it is (3 and 5)", not bad, str(bad))

# v402mgr's reading, read again: 'A spiral of selves' by self 1 only having a prior
a_rows = {1: "+0−0+0−0+0−0", 2: "+−+−+−+−+−+−", 3: "+0−+−+−0+−+−", 4: "+−+−+−+−+−+−", 5: "+0−+−+−+−+−0",
          6: "+−+−+−+−+−+−", 7: "+0−+−+−+−+−+", 8: "+−+−+−+−+−+−", 9: "+0−+−+−+−+−+", 10: "+−+−+−+−+−+−",
          11: "+0−+−+−+−+−+", 17: "+0−+−+−+−+−+", 59: "+0−+−+−+−+−+"}
same_rows, other_rows = [], []
for n, want in a_rows.items():
    pr = {("", i): None for i in range(n)}; pr[("", 0)] = -1
    ro = {(("", i), 9): ("", (i + 1) % n) for i in range(n)}
    sh, _ = L.run(pr, ro, 12)
    got = "".join(L.sym(s[("", 0)]) for s in sh)
    (same_rows if got == want else other_rows).append(n)
report("v402mgr's reading: by self 1 only having a prior, each row of an odd number of selves past one is not same-as",
       all(n in other_rows for n in a_rows if n % 2 and n > 1), "rows same-as by self 1 only: %s; not same-as: %s" % (same_rows, other_rows))
