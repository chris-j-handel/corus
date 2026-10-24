import json, os, re, collections
ROOT = "/home/claude/corus-v392chem"
OUT = ROOT + "/incoming/v392chem/motion_atom_floor/v2"
fmap = json.load(open(OUT + "/files_map.json"))
NEG = r"\b(no|not|never|none|nothing|neither|nor|nowhere|without)\b"
BANNED = r"\b(itself|couple|couples|coupled|membrane|crossing|carrying|continuing|alternating|offering|arriving|differ\w*|keeping|holding|hold|holds|held|storing|staying|stay|stays|balance|bond|bonds|bonded|bonding|v392chem|v391|v392)\b"
ok = True
for name, f in fmap.items():
    text = open(os.path.join(ROOT, f)).read()
    pairs = json.load(open(f"{OUT}/pairs_{name}.json"))
    print(f"== {f}  ({len(pairs)} pairs)")
    for i, p in enumerate(pairs):
        o, n = p["old"], p["new"]
        c = text.count(o)
        cnt = lambda rx, s: collections.Counter(m.lower() for m in re.findall(rx, s, re.I))
        negO, negN = cnt(NEG, o), cnt(NEG, n)
        addneg = {k: negN[k] - negO[k] for k in negN if negN[k] > negO[k]}
        banO, banN = cnt(BANNED, o), cnt(BANNED, n)
        addban = {k: banN[k] - banO[k] for k in banN if banN[k] > banO[k]}
        edO = set(re.findall(r"\b\w+ed\b", o, re.I)); edN = set(re.findall(r"\b\w+ed\b", n, re.I))
        added_ed = edN - edO
        bal2 = n.count("**") % 2 == 0
        bal1 = (n.replace("**", "").count("*")) % 2 == 0
        # "bond" in new allowed only in "what chemistry calls a bond"
        bond_attr = len(re.findall(r"what chemistry calls a bond", n))
        bondN = banN.get("bond", 0)
        bond_ok = bondN <= bond_attr
        flags = []
        if c != 1: flags.append(f"COUNT={c}")
        if addneg: flags.append(f"NEG+{addneg}")
        addban.pop("bond", None)
        if addban: flags.append(f"BANNED+{addban}")
        if not bond_ok: flags.append("BOND-unattributed")
        if added_ed: flags.append(f"ED+{added_ed}")
        if not bal2: flags.append("**odd")
        if not bal1: flags.append("*odd")
        if flags: ok = False
        print(f"  [{i}] count={c} **={n.count('**')} {'OK' if not flags else 'FLAG ' + ' '.join(flags)}")
        text = text.replace(o, n, 1)
    # whole-file balance after
    print(f"  after: ** total even={text.count('**')%2==0}")
print("ALL OK" if ok else "SOME FLAGS")
