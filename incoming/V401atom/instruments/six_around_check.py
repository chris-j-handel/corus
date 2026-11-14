"""The six names between selves: a self's names to its others, its names from its others, and their pairs. All or none.

Reads Exhibit ONE's code by its own lines, and changes none.
Run: python3 incoming/V401atom/instruments/six_around_check.py Exhibit_ONE_Natural_Resolver_v401mgr.md
"""
import re, sys, itertools
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
b17 = code[code.index("def _17_next_existing"):]
to = sorted(int(n) for n in re.findall(r"\(\(_13_next_discovering, (\d+)\)", b17))
print("1 the names 17-next-existing's lines have from a self to an other:", to)
frm = [2, 14, 17]
print("  the names a self has from its others: 2, given to 1-now-existing:", "_2_now_possibling" in code.split("def _1_now_existing(")[1].split(")")[0],
      "; 14, each other's co-possibling added to it in 17:", "_14_next_possibling[_4_now_co_same_existing].extend" in b17,
      "; 17, returning each self's next:", "return {" in b17)
six = sorted(to + frm)
print("  the six names between selves:", six, "· Exhibit ONE's own six:", "six names between selves" in src)
pairs = [(a, b) for a, b in itertools.combinations(six, 2) if b - a == 8]
print("2 its pairs 8 apart:", pairs, "· three, each of the six in one:", len(pairs) == 3 and sorted(x for p in pairs for x in p) == six)
print("  each pair has one name to an other and one name from an other:", all((a in to) != (b in to) for a, b in pairs))
print("  a name and its name 8 apart are a now name and its next name:", all(a < 9 <= b or (a, b) == (9, 17) for a, b in pairs))
code_pairs = [(6, 2), (10, 14), (9, 17)]
print("3 Exhibit ONE's own pairs, a self's name to its other's name:", ", ".join(f"{a} to {b}" for a, b in code_pairs),
      "· in its lines:", all(f"{a} ══► {b}" in src for a, b in code_pairs))
print("  each is one name to an other and one name from an other; 6 to 2 by two now names, 10 to 14 by two next names, 9 to 17 along:",
      all(a in to and b in frm for a, b in code_pairs))
