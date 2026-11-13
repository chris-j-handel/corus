"""Each name's three, of Exhibit ONE's table of seventeen names: bi with each name, and the slot it is with.

A check of a reading: bi-parity now, bi-parity prior and bi-parity next in turn, with co-parity betweens along,
and a bi with each name 1 to 17. And of a moment as an odd name then its even name: four moments with 1 to 8,
four with 9 to 16, and four in 1 to 17. Beside it, two selves of one bi-coupling with co-parity and with bi-parity,
a self's prior with its next, with each 1 to 17.
Exhibit ONE's table and code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/bi_in_each_name_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()

# the table: | n | **name** | root | n - 1 in four binary digits | Co | Its three |
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([^|]+) \| ([^|]+) \| (\w+) \| ([\w-]+) \|$", src, re.M)
three = {int(n): t.split("-") for n, _name, _root, _bits, _co, t in rows}   # each name's three, in the order next, now, prior
names = sorted(three)
print("names read from the table:", len(names), "; each with a three:", all(len(three[n]) == 3 for n in names))
print("the order of a three, as Exhibit ONE has it: next, now, prior:", "in the order next, now, prior" in src)
print("each slot's parity, as Exhibit ONE has it: co me-parity, bi other-parity, tri all-parity:", "co me-parity, bi other-parity, tri all-parity" in src)
for n in names:
    print(f"  {n:2}  {'odd ' if n % 2 else 'even'}  next {three[n][0]:3}  now {three[n][1]:3}  prior {three[n][2]:3}")

odd = [n for n in names if n % 2]; even = [n for n in names if not n % 2]
print("1  a bi with each name, 1 to 17:", all("bi" in three[n] for n in names))
print("2  with each odd name, bi is its now, and neither its next nor its prior:",
      all(three[n][1] == "bi" and three[n][0] != "bi" and three[n][2] != "bi" for n in odd))
print("3  with each even name, bi is its next and its prior, and not its now:",
      all(three[n][0] == "bi" and three[n][2] == "bi" and three[n][1] != "bi" for n in even))
print("   the now of each even name:", " ".join(f"{n}:{three[n][1]}" for n in even))
print("4  each name's now and prior are the name before's next and now, 2 to 17:",
      all(three[n][1:] == three[n - 1][:2] for n in names if n > 1), "; and 1's are 16's:", three[1][1:] == three[16][:2])
print("5  each bi is next with an even name, now with the odd name after it, and prior with the even name after that:",
      all(three[n][0] == "bi" and three[n + 1][1] == "bi" and (three[n + 2][2] if n + 2 <= 17 else three[2][2]) == "bi" for n in even))
print("   bis entering within 1 to 16:", sum(1 for n in even if three[n][0] == "bi"), "; each even name with two, one entering and one leaving:",
      all(three[n].count("bi") == 2 for n in even))
print("6  each co or tri is next with an odd name, now with the even name after it, and prior with the odd name after that:",
      all(three[n][0] in ("co", "tri") and three[n + 1][1] == three[n][0] and three[n + 2][2] == three[n][0] for n in odd if n + 2 <= 17))
print("7  the first prefixes, 1 to 8:", " ".join(three[n][0] for n in range(1, 9)), "; 9 to 16:", " ".join(three[n][0] for n in range(9, 17)),
      "; the same eight:", [three[n][0] for n in range(1, 9)] == [three[n][0] for n in range(9, 17)])
print("8  each three the same read from its prior to its next: of the even names", sum(1 for n in even if three[n] == three[n][::-1]), "of", len(even),
      "; of the odd names", sum(1 for n in odd if three[n] == three[n][::-1]), "of", len(odd),
      "; the others:", " ".join(f"{n}:{'-'.join(three[n])}" for n in names if three[n] != three[n][::-1]))

# a moment: an odd name then its even name; four with 1 to 8 and four with 9 to 16
root = {int(n): r.strip() for n, _name, r, _bits, _co, _t in rows}
print("11 four moments, each an odd name then its even name, with 1 to 8 and with 9 to 16, 8 up")
for m in range(1, 5):
    a, b = 2 * m - 1, 2 * m
    print(f"    moment {m}: {a}-{b}  {'-'.join(three[a])} then {'-'.join(three[b])}  {root[a]}, {root[b]}   |   {a + 8}-{b + 8}  {'-'.join(three[a + 8])} then {'-'.join(three[b + 8])}  {root[a + 8]}, {root[b + 8]}")
print("   each moment's two threes, the same with 1 to 8 and with 9 to 16:", all(three[n] == three[n + 8] for n in range(1, 9)))
print("   each moment's two roots, the same with 1 to 8 and with 9 to 16:", [m for m in range(1, 5) if (root[2*m-1], root[2*m]) == (root[2*m+7], root[2*m+8])], "of moments 1 to 4")
print("12 within each moment, its odd name's next is its even name's now, a co or a tri:", all(three[n][0] == three[n + 1][1] and three[n][0] != "bi" for n in range(1, 17, 2)))
print("13 each bi is next with a moment's even name, and now and prior with the odd name and the even name of the moment after it:",
      all(three[n][0] == "bi" and three[n + 1][1] == "bi" and (three[n + 2] if n + 2 <= 17 else three[2])[2] == "bi" for n in range(2, 17, 2)))
ex = re.search(r"\*\*A self's four momentaries of exchanging\.\*\*(.*?)\n\*\*", src, re.S).group(1)
print("14 Exhibit ONE's table of a self's four of exchanging, its self and its other:",
      " ; ".join(f"self {a} other {b}" for a, b in zip(re.findall(r"\*Self\*: ([\d–]+)", ex), re.findall(r"\*Other\*: ([\d–]+)", ex))))

# names on from 17, by Exhibit ONE's own rule: a first prefix by the eight, then the name before's first two one slot on
eight = [three[n][0] for n in range(1, 9)]
by_rule = {1: three[1]}
for n in range(2, 65):
    by_rule[n] = [eight[(n - 1) % 8]] + by_rule[n - 1][:2]
print("15 the rule gives the table's seventeen threes again:", all(by_rule[n] == three[n] for n in names))
print("   17 to 24, its four moments' threes the same as 1 to 8 and as 9 to 16:", all(by_rule[n + 16] == three[n] for n in range(2, 9)) and by_rule[17] == three[1])
print("   25, a next 1 by its three, as 9 and 17:", "-".join(by_rule[25]), by_rule[25] == three[1] == three[9] == three[17])
print("   each eight on to 64 the same threes as 1 to 8:", all(by_rule[n] == by_rule[n - 8] for n in range(10, 65)), "; 64:", "-".join(by_rule[64]))
fn = sorted(int(x) for x in re.findall(r"^def _(\d+)_", re.search(r"```python\n(.*?)```", src, re.S).group(1), re.M))
print("16 the code's functions:", fn, "; each the first name of an eight, 1 of 1 to 8, 9 of 9 to 16 and 17 of 17 to 24:", fn == [1, 9, 17])
print("17 four moments, three sides with each, an odd name then its even name with each side:", 4 * 3 * 2, "names, 1 to 24; with each moment", 3 * 2)
print("   24 to 60:", 60 - 24, "; six sixes:", 6 * 6, "; three of two sixes:", 3 * 12, "; 60 to 64:", 64 - 60, "; 25 to 64, names:", 64 - 25 + 1, ", five eights:", 5 * 8)

# Exhibit ONE's twelve forms: along each, its odd names one run and its even names one run
forms = [(kind, [int(x) for x in seq.split("-")]) for kind, seq in re.findall(r"^- \*\*Form: ([a-z -]+?) ([\d-]+)\*\*", src, re.M)]
def runs(seq):                       # around a form, the changes of odd to even and even to odd
    return sum(1 for i in range(len(seq)) if seq[i] % 2 != seq[(i + 1) % len(seq)] % 2)
print("18 forms read:", len(forms), "; around each, its odd names one run and its even names one run:", all(runs(q) == 2 for _k, q in forms))
six = [q for k, q in forms if k == "six-cycle"]
def from_odd(q):                     # a six-cycle said from the first name of its odd run
    i = next(i for i in range(6) if q[i] % 2 and not q[i - 1] % 2)
    return q[i:] + q[:i]
for q in six:
    r = from_odd(q)
    print("   six-cycle", "-".join(map(str, q)), ": odd then even", r[:3], r[3:], "; with 1 to 8", sorted(n for n in q if n <= 8), "; with 9 to 16", sorted(n for n in q if n > 8))
print("   each six-cycle three odd names then three even names:", all(all(n % 2 for n in from_odd(q)[:3]) and not any(n % 2 for n in from_odd(q)[3:]) for q in six),
      "; each with three names of 1 to 8 and three of 9 to 16:", all(sum(1 for n in q if n <= 8) == 3 for q in six))
move = lambda a, b: "17 less" if a + b == 17 else ("%d up" % (b - a) if b > a else "%d down" % (a - b))
mv = [[move(q[i], q[(i + 1) % 6]) for i in range(6)] for q in six]
back = lambda m: [x.replace("up", "DOWN").replace("down", "up").replace("DOWN", "down") for x in m[::-1]]
turn = lambda m, n: any(m[i:] + m[:i] == n for i in range(6))
print("   the moves of the first:", ", ".join(mv[0]))
print("   six-cycles with the same moves as the first:", sum(1 for m in mv if turn(m, mv[0])), "; with those moves backward:", sum(1 for m in mv if turn(m, back(mv[0]))))
pairs = [(i, j) for i in range(len(six)) for j in range(i + 1, len(six)) if len(set(six[i]) & set(six[j])) == 4]
print("   each a path with a path backward having four of its names:", [("-".join(map(str, six[i])), "-".join(map(str, six[j])), sorted(set(six[i]) & set(six[j]))) for i, j in pairs])
print("   steps of the four:", 4 * 6, "; of six cycles of six:", 6 * 6, "; of three, each a path with its path backward:", 3 * 12)

# the code: two selves of one bi-coupling, each sharing across with 10 to its other
ns = {}
exec(re.search(r"```python\n(.*?)```", src, re.S).group(1), ns)
step = ns["_17_next_existing"]
S = "s"; say = lambda v: "." if v is None else "+" if v > 0 else "-" if v < 0 else "0"
net = {("self", 10): "other", ("other", 10): "self"}
for title, a, b in [("co-parity, a self + and its other +", 1, 1), ("bi-parity, a self + and its other -", 1, -1)]:
    soc = {"self": ([(S, a)], []), "other": ([(S, b)], [])}
    line = {"self": [], "other": []}
    for t in range(18):
        for k in soc: line[k].append(dict(soc[k][0]).get(S))
        soc = step(soc, net)
    L = {k: line[k][2:] for k in line}      # from a third 1 to 17, each self with a parity or a 0 arriving
    along = ["bi" if L["self"][t] != L["self"][t + 1] else "co" for t in range(15)]
    across = ["bi" if L["self"][t] != L["other"][t] else "co" for t in range(16)]
    print("9 " if a == b else "10", title)
    print("    a self's priors :", "".join(say(v) for v in L["self"]))
    print("    its other's     :", "".join(say(v) for v in L["other"]))
    print("    along, a self's prior with its next, inverting bi and going on co:", " ".join(along))
    print("    across, a self's prior with its other's, not same-as bi and same-as co:", " ".join(across))
    print("    1 to 17s with a bi along or across:", sum(1 for t in range(15) if along[t] == "bi" or across[t] == "bi"), "of 15")
