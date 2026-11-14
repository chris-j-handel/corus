"""1-now-existing is a line inside 17-next-existing, one by each self; no line of the code executes 17. All or none.

Reads Exhibit ONE's code by its own lines, and executes it by each case.
Run: python3 incoming/V401atom/instruments/one_in_seventeen_check.py Exhibit_ONE_Natural_Resolver_v401mgr.md
"""
import re, sys, itertools

src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)

# the code's lines, by each function's own body
body = {}
for m in re.finditer(r"^def (_\d+_\w+)\(.*?(?=^def |\Z)", code, re.S | re.M):
    body[m.group(1)] = m.group(0).split("\n", 1)[1]
F1, F9, F17 = "_1_now_existing", "_9_next_co_discovering", "_17_next_existing"
calls = {f: {g: len(re.findall(re.escape(g) + r"\(", body[f])) for g in body} for f in body}
print("the code's functions:", sorted(body, key=lambda s: int(s.split("_")[1])) == [F1, F9, F17], "· 1, 9 and 17")
print("1 the code's one line executing 1-now-existing is a line of 17-next-existing:",
      calls[F17][F1] == 1 and calls[F1][F1] == 0 and calls[F9][F1] == 0)
print("2 no line of the code executes 17-next-existing:", all(calls[f][F17] == 0 for f in body))
print("3 the code's one line executing 9-next-co-discovering is a line of 17-next-existing:",
      calls[F17][F9] == 1 and calls[F1][F9] == 0 and calls[F9][F9] == 0)

# executed: one 1 and one 2 by each self, each executing
count = {"1": [], "9": 0}
one, nine = ns[F1], ns[F9]
def one_counted(p, q):
    count["1"].append((tuple(p), tuple(q)))
    return one(p, q)
def nine_counted(a, b):
    count["9"] += 1
    return nine(a, b)
ns[F1], ns[F9] = one_counted, nine_counted
step = ns[F17]
S = "s"
ok_each, ok_two, cases = True, True, 0
for k in (1, 2, 3, 4):
    selves = list(range(k))
    for priors in itertools.product((1, -1), repeat=k):
        for ring in (True, False):
            five = {}
            for a in selves:
                b = (a + 1) % k if ring else a + 1
                if b in selves and b != a:
                    five[(a, 6)] = b
            sixteen = {a: ([(S, priors[a])], []) for a in selves}
            for _ in range(5):
                count["1"], count["9"] = [], 0
                sixteen = step(sixteen, five)
                cases += 1
                ok_each = ok_each and len(count["1"]) == k and count["9"] == k
                # each 1 has one 3, its prior, and one 2, its possibling: two given, and no third
                ok_two = ok_two and all(len(c) == 2 for c in count["1"])
print(f"4 executed, {cases} executings of one to four selves: each executing has one 1 by each self, and one 9 by each self:", ok_each)
print("5 each 1 has two given, a 3 and a 2, and no third:", ok_two)
