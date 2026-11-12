"""own_turn_check.py · Exhibit ONE's code, executed as it is, with selves stepping
together, as 17 has it, and with each self with its own turn, one after an other.

Use: python3 own_turn_check.py <path to Exhibit_ONE_Natural_Resolver_v###.md>
It reads the code from the living file and changes no line of it. An executing is a
check of a reading and decides nothing. Its returned lines are in
own_turn_check_returned.txt, executed with Exhibit ONE v391.
"""
import re, sys

src = open(sys.argv[1], encoding="utf-8").read()
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"  # one sharing
sym = lambda v: {1: "+", -1: "-", 0: "0", None: "."}[v]


def run(priors, net, T, order=None):
    soc = {k: ([(S, p)], []) for k, p in priors.items()}
    hist = {k: [] for k in priors}
    for _ in range(T):
        if order is None:  # each self stepping together
            for k, (pr, inc) in soc.items():
                hist[k].append(dict(one(pr, inc)[0]).get(S))
            soc = step(soc, net)
        else:  # each self with its own turn
            for k in order:
                pr, inc = soc[k]
                out, nxt = one(pr, inc)
                hist[k].append(dict(out).get(S))
                soc[k] = (nxt, [])
                for route in ((k, 6), (k, 10), (k, 9)):
                    if route in net:
                        r = net[route]
                        soc[r] = (soc[r][0], soc[r][1] + out)
    return "   ".join("%s: %s" % (k, " ".join(sym(v) for v in h)) for k, h in hist.items())


print("One self, one sharing, one momentary: prior, receiving -> sharing . next prior")
for prior in (1, -1):
    for inc, lab in (([], "nothing"), ([(S, 1)], "+"), ([(S, -1)], "-"),
                     ([(S, 1), (S, -1)], "+ and -"), ([(S, 0)], "0")):
        o, n = one([(S, prior)], inc)
        print("  %s  %-8s -> %s . %s" % (sym(prior), lab, sym(dict(o)[S]), sym(dict(n)[S])))

pair = {("A", 10): "B", ("B", 10): "A"}
ring = {("A", 10): "B", ("B", 10): "C", ("C", 10): "A"}
each = {("A", 10): "B", ("A", 6): "C", ("B", 10): "A", ("B", 6): "C", ("C", 10): "A", ("C", 6): "B"}
print("Each self's sharing, momentary by momentary")
for lab, pri, net, order in (
    ("two alike, together", {"A": 1, "B": 1}, pair, None),
    ("two alike, own turn", {"A": 1, "B": 1}, pair, ["A", "B"]),
    ("two one parity apart, together", {"A": 1, "B": -1}, pair, None),
    ("two one parity apart, own turn", {"A": 1, "B": -1}, pair, ["A", "B"]),
    ("three along, together", {"A": 1, "B": 1, "C": 1}, ring, None),
    ("three along, own turn", {"A": 1, "B": 1, "C": 1}, ring, ["A", "B", "C"]),
    ("three, each to both others, alike, together", {"A": 1, "B": 1, "C": 1}, each, None),
    ("three, each to both others, +,+,-, together", {"A": 1, "B": 1, "C": -1}, each, None),
    ("three, each to both others, +,+,-, own turn", {"A": 1, "B": 1, "C": -1}, each, ["A", "B", "C"]),
):
    print("  %-46s %s" % (lab, run(pri, net, 12, order)))
