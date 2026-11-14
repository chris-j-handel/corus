"""Tri's places in each name's three, and the same-existing names' threes, by Exhibit ONE's table. All or none.

Reads Exhibit ONE's table, and changes none. A name's three is in the order next, now, prior, by Exhibit ONE's own sentence.
Run: python3 incoming/V401atom/instruments/tri_places_check.py Exhibit_ONE_Natural_Resolver_v401mgr.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([^|]+)\| [^|]+\| [^|]+\| ([a-z-]+) \|", src, re.M)
three = {int(n): t.split("-") for n, _name, _root, t in rows}
root = {int(n): r.strip().split(",")[0] for n, _name, r, _t in rows}
print("the order of a name's three is next, now, prior, Exhibit ONE's own sentence:", "in the order next, now, prior" in src)
same = [n for n in sorted(three) if root[n] == "same-existing"]
print("1 the same-existing names:", same, "· each four-cycling's fourth:", same == [4, 8, 12, 16])
print("  each has bi at its next and at its prior:", all(three[n][0] == "bi" and three[n][2] == "bi" for n in same))
print("  its now is co by 4 and 12, and tri by 8 and 16:", [three[n][1] for n in same] == ["co", "tri", "co", "tri"])
has = {n: three[n].index("tri") for n in sorted(three) if "tri" in three[n]}
slot = ("next", "now", "prior")
print("2 tri's places:", ", ".join(f"{n} its {slot[i]}" for n, i in has.items()))
print("  tri is a name's next at 7 and 15; a name's now at 8 and 16, and at no other name; a name's prior at 9, 17 and 1:",
      [n for n, i in has.items() if i == 0] == [7, 15] and [n for n, i in has.items() if i == 1] == [8, 16] and [n for n, i in has.items() if i == 2] == [1, 9, 17])
print("  each name having no tri has co and bi only:", all(set(three[n]) == {"co", "bi"} for n in three if n not in has))
print("3 co is a name's now at each even name but 8 and 16:", [n for n in sorted(three) if n % 2 == 0 and three[n][1] == "co"] == [2, 4, 6, 10, 12, 14])
print("  bi is a name's now at each odd name:", all(three[n][1] == "bi" for n in three if n % 2 == 1))
