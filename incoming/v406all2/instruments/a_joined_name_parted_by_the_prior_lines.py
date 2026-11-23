#!/usr/bin/env python3
"""A joined name parted by the prior lines, all or none: the opening's lines 1 to 34, the card at 35 and
the card after 30, as this session's copy of the window says them.

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
  5  Four given concepts, a partner's saying of 23 November, existing, moment, set and name: a word
     of a line's saying that is no prior line's name, no word of the line's own name, none of the
     four and no plain joining word. The plain joining words are listed with it.
  6  A partner's saying of 23 November, own is the name of my universe, gone through into the chain:
     the lines as they are with own's line ahead of 25 and after 26; and a chain offered, its
     sayings the page's rows at a number, a self said with no own, my a self's, own, and me, the
     three ahead of 22.

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
    if n not in lines and (n <= 35 or n == 49):
        lines[n] = its_saying
    elif n not in lines and n not in cards_after:
        cards_after[n] = its_saying                    # the cards 36 to 48, for a name's later sayings alone
ORDER = [n for n in range(1, 31)] + [49] + [31, 32, 33, 34, 35]       # the card of a cell is after 30

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


def words_no_line_names(the_lines, the_order):
    """A word of a saying that is no prior line's name, no word of its own name, no given and no plain word."""
    its_names = names_of(the_lines, the_order)
    found = {}
    for at, n in enumerate(the_order):
        words = parts_of(re.sub(r"[.,:;]", " ", re.sub(r"\*\*", "", the_lines[n])))
        holes, size, parting = partings(words, set(the_order[:at + 1]), its_names, PLAIN)[0]
        for word, by in parting:
            if by is None:
                found.setdefault(word, [])
                if n not in found[word]:
                    found[word].append(n)
    return found


def said_whole(found):
    return "; ".join(f"{word}, at {', '.join(map(str, at))}" for word, at in found.items()) or "none"


print("\n5. Four given concepts: existing, moment, set and name")
print(f"   the plain joining words: {', '.join(sorted(PLAIN))}")
as_they_are = words_no_line_names(lines, ORDER)
print(f"   a word no prior line names and none of the four, as the lines are: {said_whole(as_they_are)}")

print("\n6. Own is the name of my universe, into the chain")
offered = {int(n): saying.strip() for saying, n in re.findall(r"^\| (.+?) \| at (\d+) \|$", page.read_text(encoding="utf-8"), flags=re.M)}
OWN = 50                                               # the number of own's line here, a line of no number yet
with_own = dict(lines)
with_own[OWN] = offered[OWN]
for label, the_order in (("own's line ahead of 25", [n for n in ORDER if n < 25] + [OWN] + [n for n in ORDER if n >= 25 and n != 49] ),
                         ("own's line after 26", [n for n in ORDER if n <= 26 and n != 49] + [OWN] + [n for n in ORDER if n > 26 or n == 49])):
    the_order = [n for n in the_order if n in with_own]
    found = words_no_line_names(with_own, the_order)
    print(f"   the lines as they are, {label}: own named by no prior line at {found.get('own', [])}, my at {found.get('my', [])}")
a_chain = dict(lines)
a_chain.update(offered)
A_CHAIN = list(range(1, 22)) + [25, OWN, 26, 22, 23, 24, 27, 28, 29, 30, 49, 31, 32, 33, 34, 35]
for n in (18, 25, OWN, 26):
    print(f"   {n:2}  {re.sub(r'[*]', '', a_chain[n])}")
found = words_no_line_names(a_chain, A_CHAIN)
saying_own = [n for n in A_CHAIN if n != OWN and re.search(r"\bown\b", re.sub(r"\*\*", "", a_chain[n]).lower())]
after = all(A_CHAIN.index(n) > A_CHAIN.index(OWN) for n in saying_own)
print(f"   the chain offered, 1 to 21, 25, own, 26, 22 to 24, 27 and on: the lines saying own, {saying_own}, all after its line: {'is' if after else 'is-not'}")
print(f"   own or my named by no prior line in it: {sorted(n for w in ('own', 'my') for n in found.get(w, [])) or 'none'}")
print(f"   a word no prior line names and none of the four, in the chain offered: {said_whole(found)}")
