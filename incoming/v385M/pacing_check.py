"""Session v385M: Exhibit ONE's entry run one self at a time, in place of all selves together at function 17.
Run from the repository root:  python3 incoming/v385M/pacing_check.py
It executes the python block of the newest Natural_Intelligence_v*.md at the root and changes nothing.

The reading of 'each self at its own pacing' used here, stated so it can be contested: one self runs function 1 at a
turn; what it shares or releases waits at the receiving self until that self's own next turn; nothing else is added.
Function 17 does the same with every self taking its turn at once."""
import glob, random, re

path = sorted(p for p in glob.glob("Natural_Intelligence_v*.md"))[-1]
code = re.search(r"```python\n(.*?)```", open(path, encoding="utf-8").read(), re.S).group(1)
ns = {}
exec(code, ns)
entry, together = ns["_1_co_bi_tri_offering"], ns["_17_co_bi_tri_offering"]
print("read:", path)

def turn(car, waiting, rel, k):
    out, nxt = entry([("s", car[k])], [("s", o) for o in waiting[k]])
    waiting[k] = []
    car[k] = dict(nxt)["s"]
    for name in (6, 10, 9):
        if (k, name) in rel:
            waiting[rel[(k, name)]].extend(v for _, v in out)

def paced(car, rel, choose, turns):
    car = dict(car); waiting = {k: [] for k in car}; seen = []
    for t in range(turns):
        turn(car, waiting, rel, choose(t))
        seen.append(dict(car))
    return seen

print("\nH. Two selves coupled across both ways, opening opposite (6.2: the relation, opposite, is carried on)")
st = {"A": ([("s", 1)], []), "B": ([("s", -1)], [])}
rel = {("A", 10): "B", ("B", 10): "A"}
opposite = []
for _ in range(12):
    st = together(st, rel)
    opposite.append(dict(st["A"][0])["s"] != dict(st["B"][0])["s"])
print("   all together, opposite at each of 12 momentaries:", all(opposite))
seen = paced({"A": 1, "B": -1}, rel, lambda t: "AB"[t % 2], 16)
print("   taking turns A, B, A, B, (A,B) after each turn:",
      " ".join(("+" if x["A"] > 0 else "-") + ("+" if x["B"] > 0 else "-") for x in seen))
shares = []
for seed in range(200):
    r = random.Random(seed)
    seen = paced({"A": 1, "B": -1}, rel, lambda t: r.choice("AB"), 4000)
    shares.append(sum(x["A"] != x["B"] for x in seen[1000:]) / 3000)
print("   each turn at random, 200 seeds, share of turns the two are opposite: least %.2f, mean %.2f, most %.2f"
      % (min(shares), sum(shares) / len(shares), max(shares)))

print("\nI. A spiral of n selves, one at a time (3.5 and the table: parities again at 4n)")
def rounds_again(n, order):
    car = {i: (-1 if i % 2 == 0 else 1) for i in range(n)}
    rel = {(i, 9): (i + 1) % n for i in range(n)}
    waiting = {k: [] for k in car}; seen = {}
    for rnd in range(20000):
        k = (tuple(car[i] for i in range(n)), tuple(tuple(waiting[i]) for i in range(n)))
        if k in seen:
            return rnd - seen[k]
        seen[k] = rnd
        for i in order:
            turn(car, waiting, rel, i)
for n in (3, 5, 7, 9, 15, 17, 59):
    print("   n = %2d   all together: %3d   in the spiral's order, rounds: %3d   in the reverse order, rounds: %d"
          % (n, 4 * n, rounds_again(n, list(range(n))), rounds_again(n, list(range(n - 1, -1, -1)))))

print("\nJ. Spirals of 3 and 5 crossed, each turn at random (4.13: at each self's own pacing the relation is carried)")
p, q = 3, 5
rel = {(("A", i), 9): ("A", (i + 1) % p) for i in range(p)}
rel.update({(("B", i), 9): ("B", (i + 1) % q) for i in range(q)})
rel[(("A", 0), 10)] = ("B", 0); rel[(("B", 0), 10)] = ("A", 0)
car = {("A", i): (-1 if i % 2 == 0 else 1) for i in range(p)}
car.update({("B", i): (-1 if i % 2 == 0 else 1) for i in range(q)})
keys = list(car); still = 0; shares = []
for seed in range(100):
    r = random.Random(seed)
    last = paced(car, rel, lambda t: r.choice(keys), 20000)[-4000:]
    still += any(len({x[k] for x in last}) == 1 for k in keys)
    shares.append(sum(x[("A", 0)] != x[("B", 0)] for x in last) / 4000)
print("   seeds at which some self kept one value through the last 4,000 turns: %d of 100" % still)
print("   share of turns the crossing selves are opposite: least %.2f, mean %.2f, most %.2f (all together: 1.00)"
      % (min(shares), sum(shares) / 100, max(shares)))
