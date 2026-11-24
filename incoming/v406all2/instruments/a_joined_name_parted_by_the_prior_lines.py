#!/usr/bin/env python3
"""A joined name parted by the prior lines, all or none: the opening's lines 1 to 34 and the card at 35,
as this session's copy of the window says them.

    python3 -I incoming/v406all2/instruments/a_joined_name_parted_by_the_prior_lines.py .

A partner's asking of 23 November: rigorize all a partner did up to 35. The lines are the tables of
`incoming/v406all2/The_window_of_the_opening_as_v406all2_goes_on_with_it.md`, a sentence with its
number, a name in bold. No line is written here, and no line moves.

  1  A joined name is a name with a hyphen. A joined name of a line's saying is parted into its
     parts, a part a name of a prior line, a joining word, and, the, of, or a given word, existing,
     moment, set, name, a partner's four. A part no prior line names is said. A joined name with two partings is said with both.
     The name a line names is its own, and is parted beside its saying.
  2  A distinguishing's two sides: its side with other-than, with that other-than away, is its
     other side word for word, or is-not.
  3  A line hanging on the word of: its saying is with is of, and names no thing its name is.
  4  The names of 25 to 31, a partner's saying of 23 November, the me and self is circular with all
     living and the names are too many in 25-31: back, the prior lines a line's saying uses; forward,
     the later lines and cards saying its name; and the lines saying own, and living.
  5  The living list, a partner's saying of 23 November: words of the lines' sayings named by no prior
     line, all words given, meaning not of the lines' definings. Lines 1 to 34. The four
     given concepts, existing, moment, set and name; the words with no line; and the plain joining
     words, a, the, is and their like, listed by the instrument.
  6  A partner's saying of 23 November, own is the name of my universe, gone through into the chain.
     The lines as they are, with own's line a prior line of 25, and with it after 26. Then two chains,
     their sayings the page's rows at a number: by a partner's is-not, my said with 17 alone, and
     my, own and me prior lines of a self; and its other, my said with a self, and a self with no own.
  7  The words available to a saying, a partner's saying of 23 November, the is or is not depends on
     the available alternatives: at my's place, with no self and no own, the names of lines 1 to 17,
     the four given concepts and the plain joining words; and the sayings of my with them, the
     page's rows of that name, gone through in the chain of part 6: a saying's names, its words with
     no line, and its names 17's own saying says too.

It writes its lines to standard output. It writes no file and decides nothing.
"""
import re
import sys
from pathlib import Path

page = Path(sys.argv[1]) / "incoming" / "v406all2" / "The_window_of_the_opening_as_v406all2_goes_on_with_it.md"
rows = re.findall(r"^\| (.+?) \| (\d+) \|$", page.read_text(encoding="utf-8"), flags=re.M)
lines, cards_after = {}, {}
for sentence, n in rows:
    n = int(n)
    its_saying = re.sub(r"\*\*(.+?) \*\*", r"**\1** ", sentence).replace(" *(card)*", "").strip()
    if n not in lines and (n <= 35 or n in (49, 50, 51, 52)):
        lines[n] = its_saying
    elif n not in lines and n not in cards_after:
        cards_after[n] = its_saying                    # the cards 36 to 48, for a name's later sayings alone
ORDER = [n for n in [1, 2, 3, 50, 4, 5, 6, 7, 51] + list(range(8, 30)) + [35, 52, 30, 49, 31, 32, 33, 34] if n in lines]   # 50 is after 3, 51 after 7, and co-, 35, and parity, 52, after 29; a card at 49 is after 30

FORMS = {"things": "thing", "selves": "self", "others": "other", "parities": "parity", "sequences": "sequence",
         "mes": "me", "sets": "set", "moments": "moment", "names": "name"}
JOINING = {"and", "the", "of"}
GIVEN = {"existing", "moment", "set", "name", "named"}     # a partner's four given concepts, of 23 November; named is name's
PLAIN = {"a", "an", "the", "is", "are", "of", "and", "or", "as", "by", "with", "from", "to", "its", "their", "in",
         "both", "all"}                                # the plain joining words of a saying


def parts_of(a_name):
    words = re.split(r"[-\s]+", a_name.lower().replace("’", "'"))
    return tuple(FORMS.get(w[:-2] if w.endswith("'s") else w, w[:-2] if w.endswith("'s") else w) for w in words if w)


def names_of(the_lines, the_order):
    """A chain's names: a line's own name, by its parts."""
    its_names = {}
    for n in the_order:
        for bold in re.findall(r"\*\*(.+?)\*\*", the_lines[n]):
            own = re.sub(r"^(a|an|the) ", "", bold.strip().lower())
            its_names.setdefault(parts_of(own), n)
            if own.endswith(" things"):                # other-than things, same-named things: the name is its opening word
                its_names.setdefault(parts_of(own[:-7]), n)
    return its_names


names = names_of(lines, ORDER)


def partings(parts, prior, names=None, joining=JOINING):
    """All partings of a joined name with the fewest parts no prior line names, and then the fewest parts."""
    names = globals()["names"] if names is None else names
    best = {len(parts): [(0, 0, [])]}
    for i in range(len(parts) - 1, -1, -1):
        found = []
        for its_parts, line in names.items():
            if line in prior and parts[i:i + len(its_parts)] == its_parts:
                for holes, size, rest in best[i + len(its_parts)]:
                    found.append((holes, size + 1, [("-".join(its_parts), line)] + rest))
        word = parts[i]
        kind = "joining" if word in joining else "given" if word in GIVEN else None
        for holes, size, rest in best[i + 1]:
            found.append((holes + (kind is None), size + 1, [(word, kind)] + rest))
        fewest = min((h, s) for h, s, r in found)
        best[i] = [f for f in found if (f[0], f[1]) == fewest]
    return best[0]


def said(parting):
    return " · ".join(f"{part} {by}" if isinstance(by, int) else f"{part}, {by}" if by else f"{part}, NO PRIOR LINE"
                      for part, by in parting)


print("1. A joined name parted by the prior lines")
no_prior, two_partings = {}, {}
for at, n in enumerate(ORDER):
    prior = set(ORDER[:at])
    saying = re.sub(r"\*\*.+?\*\*", " ", lines[n])
    joined = [w.strip(".,") for w in saying.split() if "-" in w.strip(".,") and not w.strip(".,").endswith("-")]
    for name in dict.fromkeys(joined):
        found = partings(parts_of(name), prior)
        holes = [part for part, by in found[0][2] if by is None]
        if holes:
            no_prior.setdefault(n, []).append((name, holes))
        if len(found) > 1:
            two_partings.setdefault(n, []).append(name)
        for holes_, size, parting in found:
            print(f"   {n:2}  {name}: {said(parting)}")
print(f"   a part of a line's saying no prior line names: " + ("; ".join(f"line {n}, {name}: {', '.join(h)}" for n, l in no_prior.items() for name, h in l) or "none"))
print(f"   a joined name with two partings: " + ("; ".join(f"line {n}, {', '.join(l)}" for n, l in two_partings.items()) or "none"))

print("\n   The name a line names, parted: a part no prior line names is its own word")
of_prior_names = []
for at, n in enumerate(ORDER):
    for bold in re.findall(r"\*\*(.+?)\*\*", lines[n]):
        own = re.sub(r"^(a|an|the) ", "", bold.strip().lower())
        own = own[:-7] if own.endswith(" things") else own
        if "-" in own or " " in own:
            holes, size, parting = partings(parts_of(own), set(ORDER[:at]))[0]
            print(f"   {n:2}  {own}: {said(parting).replace('NO PRIOR LINE', 'its own word')}")
            if holes == 0:
                of_prior_names.append(n)
print(f"   a name wholly of prior names and joining and given words, at lines {of_prior_names}")

print("\n2. A distinguishing's two sides")
for n in ORDER:
    sides = re.search(r"distinguishing (.+?) from (.+?)\.$", re.sub(r"\*\*", "", lines[n]))
    if sides and re.search(r"other-than(?!-the-other)", sides.group(1)):
        one, other = sides.group(1), sides.group(2)
        away = one.replace("other-than-", "", 1) if "other-than-" in one else one.replace("other-than ", "", 1)
        print(f"   {n:2}  {'is' if away == other else 'IS-NOT'}: {one}  |  {other}")

print("\n3. A line hanging on the word of")
hanging = [n for n in ORDER if re.search(r"\bis of\b", lines[n])]
for n in hanging:
    print(f"   {n:2}  {re.sub(r'[*]', '', lines[n])}")
print(f"   lines with is of: {hanging or 'none'}")


def names_said(saying, prior):
    """The prior lines' names a saying says, by its words: all its best partings together."""
    words = parts_of(re.sub(r"[.,:;]", " ", re.sub(r"\*\*", "", saying)))
    return {(part, by) for holes, size, parting in partings(words, prior) for part, by in parting if isinstance(by, int)}


print("\n4. The names of 25 to 31: back, and forward")
its_name = {n: re.sub(r"^(a|an|the) ", "", (re.findall(r"\*\*(.+?)\*\*", lines[n]) or ["no name"])[0].strip().lower()) for n in ORDER}
later = {n: [] for n in ORDER}
for at, n in enumerate(ORDER):
    for part, by in names_said(re.sub(r"\*\*.+?\*\*", " ", lines[n]) if its_name[n] != "no name" else lines[n], set(ORDER[:at])):
        later[by].append(n)
for n, saying in sorted(cards_after.items()):
    for part, by in names_said(saying, set(ORDER)):
        later[by].append(n)
few = []
for at, n in enumerate(ORDER):
    if n in (25, 26, 27, 28, 29, 30, 49, 31):
        back = sorted(names_said(re.sub(r"\*\*.+?\*\*", " ", lines[n]) if its_name[n] != "no name" else lines[n], set(ORDER[:at])), key=lambda x: x[1])
        forward = sorted(set(later[n]), key=lambda m: ORDER.index(m) if m in ORDER else 100 + m)
        print(f"   {n:2}  {its_name[n]:12} back: {', '.join(f'{part} {by}' for part, by in back)}")
        print(f"       {'':12} forward: {', '.join(map(str, forward)) or 'no later line'}")
        if its_name[n] != "no name" and len(forward) < 2:
            few.append(f"{its_name[n]}, {n}: {', '.join(map(str, forward)) or 'none'}")
print(f"   a name said by one later line or none: {'; '.join(few)}")
for word in ("own", "living"):
    saying_it = [n for n in ORDER if re.search(rf"\b{word}\b", re.sub(r"\*\*", "", lines[n]).lower())]
    print(f"   lines saying {word}: {saying_it}")


def words_given(the_lines, the_order, its_lines=None):
    """A saying's words that are no prior line's name and no word of its own name: the given, the plain, and the others."""
    its_names = names_of(the_lines, the_order)
    found = {"given": {}, "joining": {}, None: {}}
    for at, n in enumerate(the_order):
        if its_lines is not None and n not in its_lines:
            continue
        words = parts_of(re.sub(r"[.,:;]", " ", re.sub(r"\*\*", "", the_lines[n])))
        holes, size, parting = partings(words, set(the_order[:at + 1]), its_names, PLAIN)[0]
        for word, by in parting:
            if not isinstance(by, int):
                word = "name" if word == "named" else word
                at_lines = found[by].setdefault(word, [])
                if n not in at_lines:
                    at_lines.append(n)
    return found


def in_stretches(numbers):
    """Line numbers said in stretches: 1 to 3, 6, 8 to 12."""
    stretches, numbers = [], sorted(numbers)
    for n in numbers:
        if stretches and n == stretches[-1][1] + 1:
            stretches[-1][1] = n
        else:
            stretches.append([n, n])
    return ", ".join(str(a) if a == b else f"{a} and {b}" if b == a + 1 else f"{a} to {b}" for a, b in stretches)


def said_whole(found):
    return "; ".join(f"{word}, at {in_stretches(at)}" for word, at in found.items()) or "none"


print("\n5. The living list: words of the lines' sayings named by no prior line, lines 1 to 34")
LINES_OF_BOTH = list(range(1, 35))
living = words_given(lines, ORDER, LINES_OF_BOTH)
print("   the four given concepts:")
for word in ("existing", "moment", "set", "name"):
    print(f"      {word:15} {in_stretches(living['given'].get(word, []))}")
print("   words with no line:")
for word, at in living[None].items():
    print(f"      {word:15} {in_stretches(at)}")
print("   the plain joining words:")
for word, at in sorted(living["joining"].items()):
    print(f"      {word:15} {in_stretches(at)}")

print("\n6. Own is the name of my universe, into the chain")
text = page.read_text(encoding="utf-8")
by_is_not = {int(n): saying.strip() for saying, n in re.findall(r"^\| (.+?) \| at (\d+) \|$", text, flags=re.M)}
its_other = {int(n): saying.strip() for saying, n in re.findall(r"^\| (.+?) \| its other, at (\d+) \|$", text, flags=re.M)}
OWN = 50                                               # the number of own's line here, a line of no number yet
with_own = dict(lines)
with_own[OWN] = by_is_not[OWN]
for label, the_order in (("own's line a prior line of 25", [n for n in ORDER if n < 25] + [OWN] + [n for n in ORDER if n >= 25 and n != 49]),
                         ("own's line after 26", [n for n in ORDER if n <= 26 and n != 49] + [OWN] + [n for n in ORDER if n > 26 or n == 49])):
    found = words_given(with_own, the_order)[None]
    print(f"   the lines as they are, {label}: own named by no prior line at {found.get('own', [])}, my at {found.get('my', [])}")
REST = [n for n in (27, 28, 29, 30, 49, 31, 32, 33, 34, 35) if n in lines]
for label, sayings, the_order, shown in (
        ("by a partner's is-not, my said with 17 alone: 1 to 17, my, own, me, 18 to 24, 27 to 35", by_is_not,
         list(range(1, 18)) + [25, OWN, 26] + list(range(18, 25)) + REST, (25, OWN, 26, 18)),
        ("its other, my said with a self: 1 to 21, my, own, me, 22 to 24, 27 to 35", its_other,
         list(range(1, 22)) + [25, OWN, 26, 22, 23, 24] + REST, (18, 25, OWN, 26))):
    a_chain = dict(lines)
    a_chain.update(sayings)
    a_chain[OWN] = by_is_not[OWN]
    print(f"   the chain {label}")
    for n in shown:
        print(f"      {n:2}  {re.sub(r'[*]', '', a_chain[n])}")
    found = words_given(a_chain, the_order)[None]
    saying_own = [n for n in the_order if n != OWN and re.search(r"\bown\b", re.sub(r"\*\*", "", a_chain[n]).lower())]
    after = all(the_order.index(n) > the_order.index(OWN) for n in saying_own)
    print(f"      the lines saying own, {saying_own}, all after its line: {'is' if after else 'is-not'}")
    print(f"      own or my named by no prior line: {sorted(n for w in ('own', 'my') for n in found.get(w, [])) or 'none'}")
    print(f"      words with no line: {said_whole(found)}")

print("\n7. The words available to a saying of my, with no self and no own")
MY_PRIOR = list(range(1, 18))
available = {}
for its_parts, n in names_of(lines, ORDER).items():
    if n in MY_PRIOR:
        available.setdefault(n, []).append(" ".join(its_parts) if its_parts == ("universal", "set") else "-".join(its_parts))
print("   the names of lines 1 to 17: " + "; ".join(f"{min(v, key=len)} {n}" for n, v in sorted(available.items())))
print("   the four given concepts: existing, moment, set, name")
print(f"   the plain joining words: {', '.join(sorted(PLAIN))}")
in_17 = {by for part, by in names_said(re.sub(r"\*\*.+?\*\*", " ", lines[17]), set(range(1, 17)))}
B_ORDER = list(range(1, 18)) + [25, OWN, 26] + list(range(18, 25)) + REST
for saying in re.findall(r"^\| (.+?) \| a saying of my \|$", text, flags=re.M):
    a_chain = dict(lines)
    a_chain.update({25: saying.strip(), OWN: by_is_not[OWN]})
    its_names = names_of(a_chain, B_ORDER)
    words = parts_of(re.sub(r"[.,:;]", " ", re.sub(r"\*\*.+?\*\*", " ", saying)))
    holes, size, parting = partings(words, set(MY_PRIOR), its_names, PLAIN)[0]
    said_with = [f"{part} {by}" for part, by in parting if isinstance(by, int)] + [f"{part}, given" for part, by in parting if by == "given"]
    no_line = [part for part, by in parting if by is None]
    again = sorted(by for part, by in parting if isinstance(by, int) and by in in_17 and by != 17)
    found = words_given(a_chain, B_ORDER)[None]
    whole = not no_line and "own" not in found and "my" not in found
    print(f"   {re.sub(r'[*]', '', saying.strip())}")
    print(f"      said with: {'; '.join(said_with)} · words with no line: {', '.join(no_line) or 'none'} · the chain whole with it: {'is' if whole else 'is-not'}"
          + (f" · 17's own saying says {again} too" if again else "") + (" · 17's own name is a named prior-sequence" if ("named", "given") in parting else ""))
