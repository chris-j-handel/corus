"""The six names between selves, and six around one on a surface: each arrangement, all or none.

Reads Exhibit ONE's code by its own lines, and changes none. By whole numbers: six steps around one, each sixty from its next.
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
print("  9 and 17 are odd, along; 2 and 6 are now names and 10 and 14 next names, across:", True)
# six around one: places 0 to 5 around, place k straight across place k + 3
ok_arr = []
for perm in itertools.permutations(six):
    across = all(abs(perm[k] - perm[k + 3]) == 8 for k in range(3))                      # 8 apart is straight across
    along = {perm[0], perm[3]} == {9, 17}                                                 # 9 and 17 the line along
    sides = {perm[1], perm[2]} in ({2, 6}, {10, 14}) and {perm[4], perm[5]} in ({2, 6}, {10, 14})   # now names one side, next names the other
    if across and along and sides:
        ok_arr.append(perm)
print("3 six around one, each straight across its pair 8 apart; 9 and 17 the line along; the now names its one side and the next names its other:")
print("  arrangements:", len(ok_arr))
turn = [p for p in ok_arr if all((p[k] in to) != (p[(k + 1) % 6] in to) for k in range(6))]
for p in ok_arr:
    print("   ", " ".join(f"{n}{'>' if n in to else '<'}" for n in p), "· to and from in turn around:", p in turn)
print("  of the eight, four have a name to an other and a name from an other in turn around, each one between two of the other kind; and four have three and three:",
      len(ok_arr) == 8 and len(turn) == 4)
