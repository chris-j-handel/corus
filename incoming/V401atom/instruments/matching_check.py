"""The code's matchings and the table's bi-foldings: each line and each name, all or none. No opening by chance.

Each line of the code comparing two parities, the names it is with and the loop it is in. The four bi-foldings from
Exhibit ONE's own lines, each name with its root from the table. And each case of 14-next-possibling and of
12-next-co-same-existing, with none to three parities arriving, each +, - or 0, and a prior + or -.
Exhibit ONE's table and code, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/matching_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one = ns["_1_now_existing"]
S = "s"
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([\w-]+)", src, re.M)
root = {int(n): r for n, _name, r in rows}

body1 = code[code.index("def _1_now_existing"):code.index("def _9_next_co_discovering")]
compares = re.findall(r"\((_\d+_\w+) > 0\) (==|!=) \((_\d+_\w+) > 0\)", code)
print("1  each line comparing two parities:", compares)
print("   each is 15-next-observing with 7-now-observing, the two names with tri-bi-co, and each is in 1-now-existing:",
      all(a == "_15_next_observing" and b == "_7_now_observing" for a, _op, b in compares) and len(compares) == 2
      and len(re.findall(r"> 0\) (?:==|!=) \(", body1)) == 2)
loop2, loop3 = body1.index("in _2_now_possibling"), body1.index("in _3_now_co_observing")
c1, c2 = [m.start() for m in re.finditer(r"> 0\) (?:==|!=) \(", body1)]
print("2  the first is with each parity arriving with 2, before a self's prior is read; the second is with a self's prior with 3:",
      loop2 < c1 < loop3 < c2)

cases = [c for k in range(4) for c in itertools.product((1, -1, 0), repeat=k)]
def fourteen(c):
    seen = {v for v in c if v != 0}
    return None if not seen else (seen.pop() if len(seen) == 1 else 0)
ok3 = all(dict(one([], [(S, v) for v in c])[0]).get(S) == fourteen(c) for c in cases)
print("3  14-next-possibling, each case of none to three arriving,", len(cases), "cases, with no prior read: nothing with none arriving or each a 0;")
print("   the parity with each arriving the same; a 0 with two not the same:", ok3)
ok4 = True
for p in (1, -1):
    for c in cases:
        s, n = (dict(x).get(S) for x in one([(S, p)], [(S, v) for v in c]))
        m = fourteen(c)
        ok4 = ok4 and (s == 0) == (m == p) and (s == -p) == (m != p)
print("4  12-next-co-same-existing, each case with a prior + or -: a 0 with 14 the same as a self's prior, and its prior inverted with each other case:", ok4)

folds = [tuple(int(x) for x in m.split("-")) for m in re.findall(r"^- \*Bi-folding\*: (\d+-\d+-\d+-\d+),", src, re.M)]
folds = sorted(set(folds))
print("5  the four bi-foldings, from Exhibit ONE's lines, each name with its root:")
for f in folds:
    print("    ", "-".join(map(str, f)), [root[n] for n in f])
with_poss = [f for f in folds if any(root[n] == "possibling" for n in f)]
print("   two of four are with possibling names, each with two possibling and two observing; the other two with none of either:",
      len(folds) == 4 and len(with_poss) == 2
      and all(sorted(root[n] for n in f) == ["observing", "observing", "possibling", "possibling"] for f in with_poss)
      and all(not any(root[n] in ("possibling", "observing") for n in f) for f in folds if f not in with_poss))
poss = sorted(n for n in root if root[n] == "possibling"); obs = sorted(n for n in root if root[n] == "observing")
print("6  possibling names", poss, "and observing names", obs, ": each observing name is a possibling name and one:", obs == [n + 1 for n in poss])
names1 = sorted({int(n) for n in re.findall(r"_(\d+)_", body1)})
two = sorted(n for f in with_poss for n in f)
print("7  the names with 1-now-existing's lines:", names1, "; each name of the two bi-foldings but 6, and 1, 4 and 12:",
      names1 == sorted(set(two) - {6} | {1, 4, 12}))
