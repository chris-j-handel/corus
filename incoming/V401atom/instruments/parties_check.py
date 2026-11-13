"""A self and all; a self, its other and all; a self, three others and all: each name, each line and each case, all or none.

The first prefix of each name of 1 to 5 and of 1 to 17, from Exhibit ONE's table. The names 17-next-existing's lines
have from a self to an other, read from the code's own text. A self alone, each of two cases. And a self with three
others and a fourth, each of thirty-two cases of their priors.
Exhibit ONE's table and code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/parties_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one, step = ns["_1_now_existing"], ns["_17_next_existing"]
S = "s"
first = {int(n): t.split("-")[0] for n, t in re.findall(r"^\| (\d+) \| \*\*[\w-]+\*\* \| [^|]+\| [^|]+\| [^|]+\| ([a-z-]+) \|", src, re.M)}
three = {int(n): t for n, t in re.findall(r"^\| (\d+) \| \*\*[\w-]+\*\* \| [^|]+\| [^|]+\| [^|]+\| ([a-z-]+) \|", src, re.M)}
print("1  1 to 17, each name's first prefix:", " ".join(first[n] for n in range(1, 18)))
print("   co, bi and tri, me-parity, other-parity and all-parity, are each with 1 to 17:", {first[n] for n in range(1, 18)} == {"co", "bi", "tri"})
print("2  1 to 5, each name's first prefix:", " ".join(first[n] for n in range(1, 6)), "; tri is first with", min(n for n in first if first[n] == "tri"))
print("   within 1 to 5, tri is with one name's three, 1-now-existing's, its last:", [n for n in range(1, 6) if "tri" in three[n]] == [1] and three[1].endswith("tri"))
slots = [int(x) for x in re.findall(r"\(\(_13_next_discovering, (\d+)\), _\d+_\w+\)", code)]
print("3  the names 17-next-existing's lines have from a self to an other:", slots, "; three, and no fourth:", slots == [6, 10, 9])
print("4  a self alone, each of two cases: its prior is inverting with each 1 to 17, alternating:",
      all(dict(one([(S, p)], [])[1])[S] == -p for p in (1, -1)))
ok5 = ok6 = True
names = ["a", "b", "c", "d", "e"]
net = {("a", 6): "b", ("a", 10): "c", ("a", 9): "d", ("a", 2): "e", ("b", 10): "a", ("c", 10): "a", ("d", 10): "a", ("e", 10): "a"}
for pri in itertools.product((1, -1), repeat=5):
    soc = {k: ([(S, v)], []) for k, v in zip(names, pri)}
    for t in range(16):
        ten = [v for _key, v in one(list(soc["a"][0]), list(soc["a"][1]))[0]]
        soc = step(soc, net)
        ok5 = ok5 and all([v for _k, v in soc[o][1]] == ten for o in ("b", "c", "d"))
        ok6 = ok6 and soc["e"][1] == []
print("5  a self with three others, by 6, 10 and 9, each of thirty-two cases of the priors: its co-possibling is arriving with each of the three, as it is:", ok5)
print("6  a fourth other, given with an other name of the seventeen: nothing of the self is arriving with it, with each case:", ok6)
print("7  4, 16 and 64 steps, with 1 to 5, 1 to 17 and 1 to 65: each is four of the one before it:", (17 - 1) == 4 * (5 - 1) and (65 - 1) == 4 * (17 - 1))
