"""A draft gone through beside the living files: Exhibit THIRTY-TWO Natural Prime Numbering's.

A partner's word of 23 November: all sessions help the cohering, the co-chaining, the natural naming and the
natural explaining of v407primes's report before it is a living file. This page executes the going through
and lists places for a next draft. It decides nothing: a place is a suggestion, and v407primes carries it or not.

    python3 -I incoming/v406all2/instruments/a_draft_gone_through_beside_the_living_files.py . [a page]

It writes no file and reaches no network. It executes two of the set's own instruments as they are.
"""
import glob
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve()
PAGE = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md"
sys.path.insert(0, str(ROOT / "incoming/v406Reiman/instruments"))
import the_resolver_with_nand_alone as with_nand

lines = PAGE.read_text(encoding="utf-8").split("\n")
body_opens = next(i for i, line in enumerate(lines) if line.startswith("# ") and i > 10)
living = {Path(f).name.split("_v402mgr")[0].replace("_", " "): Path(f).read_text(encoding="utf-8") for f in sorted(glob.glob(str(ROOT / "*_v402mgr.md")))}
places = 0


def said(pattern, text):
    return len(re.findall(pattern, text, re.I))


def numbers(found):
    return ", ".join(str(n + 1) for n in found) if found else "none"


print(f"The page: {PAGE.name}, {len(lines)} lines, its body opening at line {body_opens + 1}")

print("\n1. A name said with no prior line naming it")
NAMING = [("crossed", r"\*\*A number is crossed"), ("a turn", r"come again together with a turn of"), ("a quarter turn", r"\*\*A quarter turn is"),
          ("the fold", r"\*\*At the fold, 24"), ("a cone", r"a cone's widest an other-than and a vertex an all"), ("horizon", r"its side is its horizon"),
          ("a me-parity", r"is a me-parity"), ("prime scale", r"are prime scales"), ("a staircase", r"a staircase goes one up")]
USE = {"a turn": r"\bturn of \d", "the fold": r"\bfold\b", "a cone": r"\bcones?\b", "a me-parity": r"me-parit", "a staircase": r"staircase", "a quarter turn": r"quarter turn"}
for name, naming in NAMING:
    at = next((i for i in range(body_opens, len(lines)) if re.search(naming, lines[i])), None)
    before = [i for i in range(body_opens, at or body_opens) if re.search(USE.get(name, re.escape(name)), lines[i], re.I)]
    places += len(before) > 0
    if before:
        print(f"   {name}: its line at {numbers([at])}; said at {numbers(before[:8])} with no prior line naming it")

print("\n2. Cell, two things with one word")
cells = [i for i in range(len(lines)) if re.search(r"\bcells?\b", lines[i], re.I)]
opens = next(i for i in range(body_opens, len(lines)) if lines[i].startswith("## 1.1"))
closes = next(i for i in range(opens + 1, len(lines)) if lines[i].startswith("## "))
of_code = [i for i in cells if opens <= i < closes or re.search(r"nand|logic|execute", lines[i], re.I)]
of_living = [i for i in cells if i not in of_code]
places += len(of_code) > 0 and len(of_living) > 0
print(f"   cell said with nand, logic or executing: lines {numbers(of_code)}")
print(f"   cell said as a living thing's, with tissue, organelle and organism: lines {numbers(of_living)}")
print(f"   the living files: nand at {sum(said(r'\bnand\b', t) for t in living.values())} places, a cell of nand at {sum(said(r'cell of nand', t) for t in living.values())} places, "
      f"and cell at {sum(said(r'\bcells?\b', t) for t in living.values())} places")

print("\n3. Nand and a self's moment, one thing or two")
calls = []
plain = with_nand.nand
with_nand.nand = lambda a, b: (calls.append(1), plain(a, b))[1]
givings = set()
for prior in (1, -1):
    for observed in ([1], [-1], []):
        gives, its_next, a_giving, a_next = with_nand.a_cell(with_nand.TWO[prior], [with_nand.TWO[v] for v in observed])
        givings.add(with_nand.ONE[gives])
        same = bool(observed) and observed[0] == prior
        assert with_nand.ONE[gives] == (0 if same else -prior) and with_nand.ONE[its_next] == (prior if same else -prior)
one_observed = len(calls)
calls.clear()
with_nand.a_cell(with_nand.TWO[1], [with_nand.TWO[-1]])
with_nand.nand = plain
no_prior = [with_nand.ONE[with_nand.a_cell(with_nand.TWO[0], [with_nand.TWO[v]])[0]] for v in (1, -1)]
gate = [i for i in range(len(lines)) if "this one gate nand" in lines[i]]
places += len(gate) > 0
print(f"   a self with a prior, observing the same, gives a 0 and its prior goes on; observing its other, or none, its prior inverts: is, six cases")
print(f"   a moment's giving is one of {len(givings)}, a +, a - and a 0, and nand's is one of two; a moment with one observed is {len(calls)} nands, in fifteen lines")
print(f"   a self with no prior gives what it observes, {no_prior}: no 0 and no inversion, a case the page's sentence passes over")
print(f"   the page says a moment's is-or-is-not and then *this one gate nand* at line {numbers(gate)}: two things said as one")

print("\n4. Words of the one list, a living file's own names apart")
out = subprocess.run([sys.executable, "-I", str(ROOT / "incoming/v404mgr/instruments/words_of_no_natural_naming_in_a_page.py"), str(PAGE)], capture_output=True, text=True).stdout
found = re.findall(r":(\d+): ([a-z ]+): ", out)
hard = living["Exhibit TWENTY-TWO Resolving the Hard Problem Registry"]
its_own, the_pages = [], []
for n, word in found:
    line = lines[int(n) - 1]
    a_living_name = (word == "first" and "first behind" in line and said("a first behind", hard)) or (word == "changing" and "unchangeable" in line and said("changing fixing unchangeable", hard))
    (its_own if a_living_name else the_pages).append(f"{word} at {n}")
places += len(the_pages)
print(f"   {len(found)} places; {len(its_own)} are Exhibit TWENTY-TWO's own names, a first behind it and a changing unchangeable")
print(f"   the page's own: {'; '.join(the_pages)}")

print("\n5. A saying of a living file, with its living file named or not")
HOMES = [("the ten a snapshot fixes", "Exhibit TWENTY-TWO Resolving the Hard Problem Registry", r"a first behind it, a place, a last, a store, an end, a magnitude, a beat, a value, a side"),
         ("fourteen prime scales and the fold at 24", "Exhibit SEVEN Natural Societies", r"Fourteen rungs at fourteen primes, and the fold at twenty-four"),
         ("five dimensions, society to society", "Exhibit THIRTY-ONE Me", r"society to society: all now, an other now, a me now, a me next, all next"),
         ("a spiral of selves stepped by the resolver", "Exhibit ONE Natural Resolver", r"spiral"),
         ("co-parity, the same or one inversion", "Exhibit ONE Natural Resolver", r"the same or one inversion"),
         ("a ghost", "Exhibit TWENTY-SEVEN Living Ghost Registry", r"\bghost\b"),
         ("bi-tunneling", "Exhibit TWO Natural Networking", r"bi-tunneling"),
         ("prime, a number", "Exhibit THREE Natural Numbers", r"\bprimes?\b")]
text = "\n".join(lines[body_opens:])
for saying, home, pattern in HOMES:
    named = len(re.findall(re.escape(" ".join(home.split(" ")[:2])), text))
    places += named == 0
    print(f"   {saying}: {home}, its places in it {said(pattern, living[home])}; the living file's namings in the page's body {named}")
print(f"   all namings of a living file in the page's body: {len(re.findall(r'Exhibit [A-Z]', text))}")

print("\n6. A section pointing at itself, the sources' years, and the kit's rigorizer")
section, own = None, []
for i in range(body_opens, len(lines)):
    head = re.match(r"## (\d\.\d) ", lines[i])
    section = head.group(1) if head else section
    if section and not head and re.search(rf", {re.escape(section)}[;.,]", lines[i]):
        own.append(i)
sources = next(i for i, line in enumerate(lines) if line.startswith("## Sources"))
years = [(i, int(m.group(0))) for i in range(sources, len(lines)) for m in [re.search(r"\b(1[5-9]|20)\d\d\b", lines[i])] if lines[i].startswith("- ") and m]
turning = [i for (i, y), (j, z) in zip(years[1:], years) if y < z]
seated = subprocess.run([sys.executable, "-I", str(ROOT / "kits/Living_File_Registry_TWENTY-SIX_Improving_Kit/rigorize.py"), "beside", str(PAGE)], capture_output=True, text=True).stdout
released = sorted({word for group in re.findall(r"released words: ([a-z, ]+)", seated) for word in group.split(", ")})
places += len(own) + len(turning) + len(released)
print(f"   a pointer at its own section: lines {numbers(own)}")
print(f"   a source with a year earlier than its prior line's: lines {numbers(turning)}")
print(f"   the kit's rigorizer: {seated.strip().splitlines()[-1].split(':', 1)[-1].strip()}; its released words in the page: {', '.join(released) or 'none'}")

print("\n7. The page's joined names by the opening's lines, 1 to 34, and four names v406me asked of")
import contextlib
import importlib.util
import io
from collections import Counter
spec = importlib.util.spec_from_file_location("joined", ROOT / "incoming/v406all2/instruments/a_joined_name_parted_by_the_prior_lines.py")
joined = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv, [sys.argv[0], str(ROOT)]
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(joined)
sys.argv = argv
the_lines = set(joined.LINES_OF_BOTH)


def no_line(a_name):
    holes, size, parting = joined.partings(joined.parts_of(a_name), the_lines)[0]
    return [word for word, kind in parting if kind is None]


found = Counter(m.lower() for m in re.findall(r"\b[A-Za-z]+(?:-[A-Za-z]+)+\b", text))
whole = sorted(name for name in found if not no_line(name))
parts = Counter(word for name in found for word in set(no_line(name)))
print(f"   {len(found)} joined names; {len(whole)} are said whole by the lines' names and the four given: {', '.join(whole)}")
print(f"   parts named by no line, with their joined names: {', '.join(f'{w} {n}' for w, n in parts.most_common(14))}")
whole_text = " ".join(living.values())
print(f"   durable snapshot: parts with no line {no_line('durable snapshot')}; the page's places {said('durable snapshot', text)}, the living files' {said('durable snapshot', whole_text)};"
      f" beside it Exhibit TWENTY-SEVEN's *a ghost is one moment's form, installing it as an existing thing*, {said('a ghost is one moment.s form, installing it as an existing thing', whole_text)} found")
beside_same = [i for i in range(body_opens, len(lines)) if "next-universing" in lines[i] and "same-existing" in lines[i]]
print(f"   next-universing: parts with no line {no_line('next-universing')}; the page's places {said('next-universing', text)}, the living files' {said('universing', whole_text)};"
      f" said beside same-existing, 12, at {numbers(beside_same)}, and next-existing, 11, is the lines' name beside 12")
print(f"   other-than-other-than: parts with no line {no_line('other-than-other-than') or 'none'}; the page's *other-than-other-than parity* {said('other-than-other-than parity', text)} found, a 0;"
      f" the lines' own name *other-than-other-parity*, 33, same-existing, in the page {said('other-than-other-parity', text)}; and the page's 1.1 says a 0 with same-existing, {said('a 0, its prior same-existing', text)} found")
stable = [i for i in range(body_opens, len(lines)) for m in re.finditer(r"[^.:;]*stable form[^.:;]*", lines[i])]
non_living = sum("non-living" in m.group(0) for i in range(body_opens, len(lines)) for m in re.finditer(r"[^.;]*stable form[^.;]*", lines[i]))
print(f"   a prime as the stable form of natural intelligence living: {said('A prime is the stable form of natural intelligence living', text)} found; stable form in the page {len(stable)} places,"
      f" {non_living} of them with non-living; Natural Naming's *a non-living existing form with no same-existing for stable-forming*, {said('non-living existing form with no same-existing for stable-forming', whole_text)} found;"
      f" and the page's *A prime lives five ways*, {said('A prime lives five ways', text)} found")
places += 4

print(f"\n{places} places for a next draft, a suggestion apiece.")
