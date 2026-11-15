"""v402code · column d of 'Two spirals beside each other, and bi-coupling across': self 1 of each, like or opposite."""
import importlib.util, os
_sp = importlib.util.spec_from_file_location('L', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tables_check_lib.py'))
L = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(L)
rows = [(2, 3), (3, 5), (5, 7), (7, 11), (11, 13), (13, 17), (17, 59), (9, 15)]
def d(m, n, T=None):
    pr, ro = L.two_spirals(m, n, True)
    T = T or 2 * max(m, n) + 4 * min(m, n) + 60
    sh, pri = L.run(pr, ro, T)
    seq = [tuple(s[k] for k in sorted(s)) for s in sh]
    st, p = L.eventual(seq, maxp=40)
    pri_rel = set(pri[t][("A", 0)] * pri[t][("B", 0)] for t in range(st, T))
    sh_rel = set((sh[t][("A", 0)], sh[t][("B", 0)]) for t in range(st, T))
    return st + 1, p, pri_rel, sh_rel
print("the eight rows: (from, period, product of the two self 1 priors in the going form {-1: opposite, 1: like}, their sharings)")
for m, n in rows: print(" ", m, n, d(m, n))
print("the range 2 to 15, the larger to 31: like or opposite by the kind of the two numbers")
kinds = {}
for m in range(2, 16):
    for n in range(m, 32):
        _, p, rel, shr = d(m, n)
        kind = ("even" if m % 2 == 0 else "odd") + "·" + ("even" if n % 2 == 0 else "odd") + ("" if m != n else " equal")
        kinds.setdefault(kind, {}).setdefault((p, tuple(sorted(rel))), []).append((m, n))
for k, v in kinds.items():
    for (p, rel), lst in v.items(): print(" ", k, "| period", p, "| priors product", rel, "|", len(lst), "pairs, as", lst[:4])
