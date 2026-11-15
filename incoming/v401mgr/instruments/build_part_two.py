"""build_part_two · v401mgr · 14 Nov
Part two, a podal and no less: each rule is living words and their next words, word for word.
It reads the living files and changes none. It says each rule's places by file, and that no *17 less* or *9 less* is after the rules, in each file it has rules for.
Usage: python3 -I build_part_two.py <the set's root> [each]
"""
import sys, re
R = sys.argv[1]; EACH = len(sys.argv) > 2
P16, P8 = "podal within 1 to 16", "podal within 1 to 8"
rules = [
 ("- *9 less*: podal within 1 to 8, ", "- *Its "+P8+"*: "),
 ("- *17 less*: podal within 1 to 16, ", "- *Its "+P16+"*: "),
 ("  - *9 less: 9 − n*: ", "  - *Its "+P8+"*: "),
 ("  - *17 less: 17 − n*: ", "  - *Its "+P16+"*: "),
 ("going 17 less first from ", "going by a "+P16+" first from "),
 ("Each goes two folds in turn, 17 less and a move of 8", "Each goes two folds in turn, a "+P16+" and a move of 8"),
 ("8 down (n − 8) or 17 less (17 − n).", "8 down (n − 8) or a "+P16+" (17 − n)."),
 ("**Two moves, 9 less.**", "**Two moves, a "+P8+".**"),
 ("to its 9 less. Its 9 less is a name across", "to its "+P8+". Its "+P8+" is a name across"),
 ("Each name and its 9 less:", "Each name and its "+P8+":"),
 ("with 8 up, 9 less and 17 less.", "with 8 up, its "+P8+" and its "+P16+"."),
 ("move 8 up, 4 down, 17 less, 4 down, 8 up and 17 less,", "move 8 up, 4 down, a "+P16+", 4 down, 8 up and a "+P16+","),
 ("4 up, 4 down or 17 less", "4 up, 4 down or a "+P16),
 ("17 less, podal within 1 to 16; and 9 less, podal within 1 to 8, two together.", "a "+P16+"; and a "+P8+", two together."),
 ("each time with 17 less, podal within 1 to 16.", "each time with a "+P16+"."),
 ("17 less exchanges now and next.", "The "+P16+" exchanges now and next."),
 ("9 less within a self's span, 1 to 8.", "the podal within a self's span, 1 to 8."),
]
TH="Exhibit_THIRTY_Co-Chaining_Logic_Registry_v401mgr.md"; NN="Exhibit_TWENTY_Natural_Naming_v401mgr.md"; NU="Exhibit_THREE_Natural_Numbers_v401mgr.md"; NW="Exhibit_TWO_Natural_Networking_v401mgr.md"; EQ="Exhibit_TWENTY-EIGHT_Equilibria_Registry_v401mgr.md"; MA="Exhibit_FOUR_Natural_Mathematics_v391.md"; IL="Exhibit_TWENTY-NINE_Natural_Illustrating_v401mgr.md"; LF="Exhibit_TWENTY-SIX_Living_File_Registry_v401mgr.md"; ME="Exhibit_ELEVEN_Natural_Medicine_v391.md"
own = {
 TH: [
  ("each number pairs with its podal, 9 less: 1 with 8", "each number pairs with its podal: 1 with 8"),
  ("one move as three, 8 up, 17 less and 9 less, and only one move", "one move as three, 8 up, a "+P16+" and a "+P8+", and only one move"),
  ("2-15-7-10 and 4-13-5-12 going 17 less first, round other way", "2-15-7-10 and 4-13-5-12 going by a "+P16+" first, round other way"),
  ("its one move is 4 up and 9 less, a podal within 1 to 8.", "its one move is 4 up and a "+P8+"."),
  ("move is 8 up and 17 less: 3-7-2-6 opens", "move is 8 up and a "+P16+": 3-7-2-6 opens"),
  ("keeping odd or even, beside 17 less, and six-cycles", "keeping odd or even, beside a "+P16+", and six-cycles"),
  ("9-5-12-8 and 7-11-6-10 by 4 and 17 less, twice;", "9-5-12-8 and 7-11-6-10 by 4 and a "+P16+", twice;"),
  ("by two of 8, two of 4 and two of 17 less;", "by two of 8, two of 4 and two podals within 1 to 16;"),
  ("by 8, 4, 8 and 17 less, twice.", "by 8, 4, 8 and a "+P16+", twice."),
  ("are exactly two, each with a 17 less, steps 343 and 356", "are exactly two, each with a "+P16+", steps 343 and 356"),
  ("and 3 and 5 are 17 less as 14 and 12, odd to even", "and 3 and 5 are podal within 1 to 16 with 14 and 12, odd to even"),
  ("with 1 to 16, 17 less its fourth parity; with 1 to 8, 9 less its third; with 1 to 4, 5 less its second; with 1 to 2, 3 less its first, 1 and 2.", "with 1 to 16, its podal its fourth parity; with 1 to 8, its third; with 1 to 4, its second; with 1 to 2, its first, 1 and 2."),
  ("third and fourth parities inverting, 9 less and 17 less in sequence,", "third and fourth parities inverting, a "+P8+" and a "+P16+" in sequence,"),
  ("8 up and 17 less in sequence are 9 less, 1 to 9 to 8 of step 333; with 9 to 16, 17 less and 9 less in sequence are 8 down,", "8 up and a "+P16+" in sequence are a "+P8+", 1 to 9 to 8 of step 333; with 9 to 16, a "+P16+" and a "+P8+" in sequence are 8 down,"),
  ("each move, 8 up or 17 less, going between", "each move, 8 up or a "+P16+", going between"),
 ],
 NN: [
  ("With 9 less, a podal within 1 to 8, and with 17 less, a podal within 1 to 16, eight ends", "With a "+P8+", and with a "+P16+", eight ends"),
  ("k one way and 17 less its other way", "k one way and its "+P16+" its other way"),
  ("Bi-foldings step 8 up and 17 less, two names", "Bi-foldings step 8 up and by a "+P16+", two names"),
  ("a pair is a podal, 17 less within 1 to 16, and an even number's", "a pair is a "+P16+", and an even number's"),
  ("9 to 8 and 16 to 1, each with 17 less, and 1 to 9", "9 to 8 and 16 to 1, each a "+P16+", and 1 to 9"),
  ("each by 4 up and 9 less, round each other's way", "each by 4 up and a "+P8+", round each other's way"),
 ],
 NU: [
  ("17 less, podal within 1 to 16, exchanging odd and even; and 9 less, podal within 1 to 8, 17 less and 8 down together, exchanging odd and even.", "a "+P16+", exchanging odd and even; and a "+P8+", a "+P16+" and 8 down together, exchanging odd and even."),
  ("one move, 8 and 17 less one and then the other, after four.", "one move, 8 and a "+P16+" one and then the other, after four."),
  ("| 9 less, within 1 to 8 | 17 less, within 1 to 16 |", "| Podal within 1 to 8 | Podal within 1 to 16 |"),
  ("**8 up or down and 17 less one and then the other, each row is a bi-folding**", "**8 up or down and a "+P16+" one and then the other, each row is a bi-folding**"),
  ("with 9 less, 3-now-co-observing and 6-now-co-possibling, 9 less 3 being 6, are six over three", "with a "+P8+", 3-now-co-observing and 6-now-co-possibling, 3's podal being 6, are six over three"),
  ("With 9 less, now pairs with all and existing with same", "With a "+P8+", now pairs with all and existing with same"),
  ("**With one move's 8 up and 17 less, primes add to their own numbers.**", "**With one move's 8 up and "+P16+", primes add to their own numbers.**"),
  ("six prime pairs' distances from thirty. 17 less: 2 and 53", "six prime pairs' distances from thirty. A "+P16+": 2 and 53"),
  ("8 up and then 17 less is 9 less, 17 − (n + 8) = 9 − n", "8 up and then a "+P16+" is a "+P8+", 17 − (n + 8) = 9 − n"),
 ],
 NW: [
  ("**A fold has local relation whole.** 9 less pairs 1-now-existing", "**A fold has local relation whole.** A "+P8+" pairs 1-now-existing"),
  ("| Name | Podal within 1 to 8, 9 less |", "| Name | Podal within 1 to 8 |"),
  ("Within 1–16, 17 less pairs each name with 17 minus that name. Eight up or down and 17 less, one and then the other,", "Within 1–16, a podal pairs each name with 17 minus that name. Eight up or down and a "+P16+", one and then the other,"),
  ("*a* Podal pair, 9 less, one odd and one even", "*a* Podal pair within 1 to 8, one odd and one even"),
  ("keeping odd or even, and 17 less, exchanging them", "keeping odd or even, and a "+P16+", exchanging them"),
  ("9 less pairs three with six.", "A "+P8+" pairs three with six."),
  ("17 less pairs 11 with 6 and 14 with 3.", "A "+P16+" pairs 11 with 6 and 14 with 3."),
  ("with both sides forward.** 9 less pairs 1 with 8", "with both sides forward.** A "+P8+" pairs 1 with 8"),
 ],
 EQ: [
  ("exchange with its two steps of 17 less, changing:", "exchange with its two steps of a "+P16+", changing:"),
  ("2-15-7-10 and 4-13-5-12 going 17 less first:", "2-15-7-10 and 4-13-5-12 going by a "+P16+" first:"),
 ],
 MA: [
  ("and a podal within 1 to 16, 17 less, fixes none", "and a "+P16+" fixes none"),
  ("with its podal within 1 to 8, 9 less, an odd number with an even;", "with its "+P8+", an odd number with an even;"),
 ],
 IL: [
  ("three ways, 8 up, 17 less and 9 less, and with its 2.4", "three ways, 8 up, a "+P16+" and a "+P8+", and with its 2.4"),
 ],
}
# places of a number's own arithmetic, or a record: as they are, each said by its line's own words
asis = {
 TH: ["a podal, k to N less k,", "and names' podal, 17 less, 17 odd,", "8s + 1 less changes it", "4 up and 9 less with s one and 8 up and 17 less with s two."],
 NU: ["its odd centre squared less n**: within 1 to 8 it is 9 less n, within 1 to 24 it is 25 less n, and within 1 to 48 it is 49 less n,", "Within 1 to 16 its podal is 17 less n,", "8s + 1 less exchanges odd and even", "4s + 1 less within a lower half and 12s + 1 less within an upper", "With s two they are 8 up and 17 less, 3 to 11 to 6 to 14 to 3; with s one they are 4 up and 9 less,", "B + 1 less going to Br + 1 less"],
 EQ: ["17 less (9 less n) being **n + 8**."],
 NN: ["*a podal within 1 to 16* for 17 less"],
 ME: ["36 less its diagonal"],
 LF: ["17 less and 9 less twice an involution each", "4 down or 17 less, worked at each of the twelve", "8 down or 17 less; the six-cycle", "9 less as 9 − n and 17 less as 17 − n", "15 less, the citations"],
}
names = {TH:"Exhibit THIRTY Co-Chaining Logic Registry", NN:"Exhibit TWENTY Natural Naming", NU:"Exhibit THREE Natural Numbers", NW:"Exhibit TWO Natural Networking", EQ:"Exhibit TWENTY-EIGHT Equilibria Registry", MA:"Exhibit FOUR Natural Mathematics", IL:"Exhibit TWENTY-NINE Natural Illustrating", LF:"Exhibit TWENTY-SIX Living File Registry", ME:"Exhibit ELEVEN Natural Medicine"}
any_less = re.compile(r"\b(\d+|n|k) less\b|\+ 1 less\b|squared less\b")
files = {"Exhibit ONE Natural Resolver": "Exhibit_ONE_Natural_Resolver_v401mgr.md", "Natural Intelligence": "Natural_Intelligence_v401mgr.md"}
pat = re.compile(r"\b(17|9) less\b")
rows = []; total = {}
for name, f in files.items():
    t = open(R + "/" + f).read(); before = len(pat.findall(t)); n_rules = 0
    for old, new in rules:
        c = t.count(old)
        if c:
            rows.append((name, old, new, c, 0))
            n_rules += c * len(pat.findall(old))
        t = t.replace(old, new)
    left = pat.findall(t)
    assert not left, (name, len(left))
    assert n_rules == before, (name, n_rules, before)
    total[name] = before
rows2 = []; asis_rows = []; total2 = {}; left_all = {}
for f in (TH, NN, NU, NW, EQ, MA, IL, LF, ME):
    t = open(R + "/" + f).read(); before = len(pat.findall(t))
    for old, new in own.get(f, []):
        c = t.count(old); assert c == 1, (f, old, c)
        rows2.append((names[f], old, new, c)); t = t.replace(old, new)
    for s in asis.get(f, []):
        assert t.count(s) >= 1, (f, s); asis_rows.append((names[f], s)); t = t.replace(s, "")
    left = pat.findall(t)
    assert not left, (f, len(left), [m.group(0) for m in re.finditer(r".{40}\b(?:17|9) less\b.{30}", t)])
    total2[names[f]] = before
print("| The living file | The living words | The next words | Places |\n|---|---|---|---|")
for name, old, new, c, _ in rows:
    print(f"| {name} | {old.strip().replace('|','\\|')} | {new.strip().replace('|','\\|')} | {c} |")
print()
for name in total: print(f"**{name}:** each place of *17 less* and of *9 less* has its next words; none is after them.")
print()
print("| The living file | The living words | The next words |\n|---|---|---|")
for name, old, new, c in rows2: print(f"| {name} | {old.strip().replace('|','\\|')} | {new.strip().replace('|','\\|')} |")
print()
print("| The living file | The living words, as they are |\n|---|---|")
for name, s in asis_rows: print(f"| {name} | {s.strip().replace('|','\\|')} |")
print("places: " + ", ".join(f"{k} {v}" for k, v in {**total, **total2}.items()) + f"; rules of the nine {len(rows2)}; as they are {len(asis_rows)}", file=sys.stderr)
