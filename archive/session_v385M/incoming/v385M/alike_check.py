"""Session v385M: two selves opening alike and coupled both ways. Do they ever part?
Run from the repository root:  python3 incoming/v385M/alike_check.py
It executes the python block of the newest Natural_Intelligence_v*.md at the root and changes nothing.

Asked at the worm: two cells alike, either of which becomes the anchor cell, end one each, and which is which
differs from worm to worm. Here: two selves alike in what they carry and in what arrives, all together at
function 17, and one at a time (the reading of own pacing stated at the head of pacing_check.py)."""
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

sign = lambda v: "+" if v > 0 else "-"
for name in (10, 9, 6):
    rel = {("A", name): "B", ("B", name): "A"}
    print("\nCoupled both ways at name %d, both opening +" % name)
    st = {"A": ([("s", 1)], []), "B": ([("s", 1)], [])}
    row = []
    for _ in range(400):
        st = together(st, rel)
        row.append((dict(st["A"][0])["s"], dict(st["B"][0])["s"]))
    print("   all together, 400 momentaries: the two alike at %d, parted at %d;  first 12: %s"
          % (sum(a == b for a, b in row), sum(a != b for a, b in row), " ".join(sign(a) + sign(b) for a, b in row[:12])))
    seen = paced({"A": 1, "B": 1}, rel, lambda t: "AB"[t % 2], 400)
    print("   taking turns A, B, A, B, 400 turns: alike at %d, parted at %d;  first 12: %s"
          % (sum(x["A"] == x["B"] for x in seen), sum(x["A"] != x["B"] for x in seen),
             " ".join(sign(x["A"]) + sign(x["B"]) for x in seen[:12])))
    first = {"A": 0, "B": 0, "never": 0}
    for seed in range(200):
        r = random.Random(seed)
        seen = paced({"A": 1, "B": 1}, rel, lambda t: r.choice("AB"), 50)
        who = next((k for x in seen for k in "AB" if x["A"] != x["B"] and x[k] < 0), "never")
        first[who] += 1
    print("   each turn at random, 200 seeds: the first to part from + was A at %d, B at %d, neither within 50 turns at %d"
          % (first["A"], first["B"], first["never"]))
