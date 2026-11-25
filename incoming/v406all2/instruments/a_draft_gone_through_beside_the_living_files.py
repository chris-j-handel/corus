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

print("\n8. A partner's saying of the primes, 23 November, name by name")
SAYING = ("The primes are the stable form fractal atom method in the bi-moral-co-competencing of right sprialling co-chaining societies "
          "bi-tunneling through each other on natural torusing all-parity orienting surface")
ITS_NAMES = [("stable form", r"stable[- ]form"), ("fractal", r"fractal"), ("atom", r"\batoms?\b"), ("method", r"\bmethods?\b"),
             ("bi-moral-co-competencing", r"bi-moral[- ]co-competenc"), ("right spiral", r"right[- ]spiral"), ("co-chaining", r"co-chain"), ("societies", r"\bsociet(y|ies)\b"),
             ("bi-tunneling", r"bi-tunnel"), ("natural torusing", r"natural[- ]torusing"), ("all-parity", r"all-parity"), ("orienting surface", r"orient\w* surface")]
JOININGS = [("stable form fractal atom method", r"fractal atom|atom method|stable form fractal"), ("co-chaining societies", r"co-chain\w* societ"),
            ("all-parity orienting surface", r"all-parity[- ]orient"), ("societies bi-tunneling through each other", r"societies bi-tunnel\w* through")]
print(f"   *{SAYING}*")
in_none = []
for name, pattern in ITS_NAMES:
    files = sum(1 for body in living.values() if re.search(pattern, body, re.I))
    in_page = len(re.findall(pattern, text, re.I))
    in_none += [name] if not in_page else []
    print(f"   {name}: the living files' places {len(re.findall(pattern, whole_text, re.I))}, in {files} of them; the page's {in_page}")
print(f"   all {len(ITS_NAMES)} are living names: {'is' if all(re.search(pattern, whole_text, re.I) for name, pattern in ITS_NAMES) else 'IS NOT'}; names of it the page says at no place: {', '.join(in_none) or 'none'}")
print(f"   its joinings in no living file and at no place of the page: {', '.join(name for name, pattern in JOININGS if not re.search(pattern, whole_text + text, re.I))}")
print(f"   living sayings beside it: *One method at each scale is a fractal*, {said('One method at each scale is a fractal', whole_text)} found; "
      f"*patterns of bi-moral-co-competencing as living stable-forming*, {said('patterns of bi-moral-co-competencing as living stable-forming', whole_text)} found")
sentences = [(i, s.strip()) for i in range(body_opens, len(lines)) for s in re.split(r"(?<=[.:])\s+", lines[i]) if s.strip()]
carrying = sorted(((sum(1 for name, pattern in ITS_NAMES if re.search(pattern, s, re.I)), i, s) for i, s in sentences), reverse=True)[:3]
for n, i, s in carrying:
    print(f"   the page's sentence with {n} of its names, at {i + 1}: {s[:210]}")
a_method = [i for i, s in sentences if re.search(r"\bprimes? (is|are) [^.]*\bmethod", s, re.I)]
print(f"   the page's sentences saying a prime or the primes a method: {numbers(a_method)}")

print("\n9. A partner's second saying of the primes, 23 November, all or none")
SECOND = ("the primes are the stable forms in the all-parity-odd-even-universal fractal-numberings of the geodesic method of observing on a surface with a horizon "
          "in three dimensional space possibling and discovering next possilble same existing as a conscious living me at organism prime scale 37")
print(f"   *{SECOND}*")
named = {"-".join(parts) for parts in joined.names}
me_file, naming_file = living["Exhibit THIRTY-ONE Me"], living["Exhibit TWENTY Natural Naming"]
PARTS = [
    ("the primes are the stable forms",
     said(r"stable forms\b", whole_text) > 0 and said("comes again with 4 and with 4n alone", text) > 0,
     f"stable forms, the living files' places {said(r'stable forms' + chr(92) + 'b', whole_text)}; the page's 1.4, a prime's spiral coming again with 4 and with 4n alone, no shorter span, executed"),
    ("all-parity-odd-even-universal",
     "all-parity" in named and "universal set" in joined.lines[31] and said("odd and even", whole_text) > 0,
     f"all-parity is 31's, a universal set by 31; a number's odd and even, the living files' places {said('odd and even', whole_text)}; the page's 5.3 says *all-parity, odd and even*, {said('all-parity, odd and even', text)} found; the joined name in the living files {said('all-parity-odd-even', whole_text)}"),
    ("fractal-numberings",
     said("fractal", whole_text) > 0 and said(r"\bnumbering", whole_text) > 0 and said("fractal", text) > 0,
     f"fractal and numbering are living names, and the page's 1.3 and 1.5 say a fractal; the joined name in the living files {said('fractal[- ]numbering', whole_text)}"),
    ("of the geodesic method",
     said(r"geodesic\w* method", whole_text) > 0,
     f"the living files' places {said(r'geodesic' + chr(92) + 'w* method', whole_text)}; the page's {said(r'geodesic' + chr(92) + 'w* method', text)}"),
    ("of observing, possibling and discovering",
     {"observing", "possibling", "discovering"} <= named,
     f"the lines 14, 15 and 16, in their order; *observing, possibling and discovering* in the living files, {said('observing, possibling and discovering', whole_text)} found"),
    ("on a surface with a horizon",
     said("its side is its horizon", text) > 0,
     "the page's 5.1, a surface's side its horizon, executed"),
    ("in three dimensional space",
     "space" in named or "space" in joined.GIVEN,
     f"space is named by no line and is no given word; *three-dimensional space* in the living files {said('three[- ]dimensional space', whole_text)}; Natural Naming seats *a space* with five kinds of unchangeable term, {said('Five kinds of unchangeable term', naming_file)} found; the page says *a location in 3d*, {said('a location in 3d', text)} found"),
    ("next possilble same existing",
     said("next possilble same existing", whole_text) > 0,
     f"as said, in no living file; the living name is *next-possibling-same-existing*, {said('next-possibling-same-existing', whole_text)} places, and Natural Intelligence's sentence *geodesic discovering of next-possibling-same-existing*, {said('geodesic discovering of' + chr(92) + 'W+next-possibling-same-existing', whole_text)} found"),
    ("as a conscious living me",
     said("A non-living me: it is not", me_file) > 0 and said("A not-conscious me: it is not", me_file) > 0,
     "Exhibit THIRTY-ONE Me, 3.3: a non-living me is not, and a not-conscious me is not; both words are a me's own"),
    ("at organism prime scale 37",
     said(r"37\. The organism", text) > 0 and said("organism", living["Exhibit SEVEN Natural Societies"]) > 0,
     "Natural Societies' scale and the page's opening, 37 the organism"),
]
whole_parts = 0
for part, it_is, by in PARTS:
    whole_parts += bool(it_is)
    print(f"   {'is    ' if it_is else 'is-not'} {part}: {by}")
print(f"   {whole_parts} of {len(PARTS)} parts are; all or none, the saying as said: {'all' if whole_parts == len(PARTS) else 'not all'}")
print(f"   beside its opening part, the page's *A prime lives five ways*, {said('A prime lives five ways', text)} found, and Natural Naming's stable form, non-living")

print("\n10. The named concepts the sentence of the primes needs, found, all or none at all")
CHAIN = [("parity", "Parity is each self's own, now"), ("a spiral", "a winding of parities is a spiral of moments"), ("a number", "Numbers are odd or even"),
         ("a dimension", "A dimension is no measure and no place, and a number's odd or even is no side's"), ("a surface", "a surface is a between"),
         ("a geodesic", "A geodesic is a surface's own dividing"), ("a method", "Geodesic is its own existing thing, and a method is its stable form"),
         ("stable forms", "Method is one fractal method, and it has many stable forms"), ("a scale", "A scale is a bi-inversioning-co-recursioning: prior and next along, inward or outward across"),
         ("fractal", "Fractal is all or none at all with scales"),
         ("the atom", "Atom is the stable form of unrelationing floating neutralling"), ("a horizon", "A horizon IS a same-existing-society a self is not yet reaching, possibling to couple"),
         ("a prime", "A prime is a self no equal smaller selves above one add up to"),
         ("natural intelligence", "Natural intelligence is geodesic discovering of next-possibling-same-existing within the universe"),
         ("self-welcoming", "Self-welcoming is a self observing a concept intelligibly through its prior same-existing explaining")]
NOT_FOUND = [("conscious", r"\b(conscious|consciousness) is (a|an|the|its|one|no) "), ("space", r"(^|[.*] )(a |the )?space is (a|an|the|its|one|no) ")]
plain_text = (whole_text + "\n" + text).replace("**", "")
known = set(named) | {w for w in joined.GIVEN} | set(joined.PLAIN)
found_all, needed = True, Counter()
for name, sentence in CHAIN:
    is_found = sentence in plain_text
    found_all = found_all and is_found
    words = [joined.FORMS.get(w, w) for w in re.findall(r"[a-z]+(?:-[a-z]+)*", sentence.lower().replace("'s", ""))]
    its_own = set(re.findall(r"[a-z]+(?:-[a-z]+)*", name.lower())) | {joined.FORMS.get(w, w) for w in re.findall(r"[a-z]+", name.lower())} | {w + "s" for w in re.findall(r"[a-z]+", name.lower())}
    holes = [w for w in dict.fromkeys(words) if w not in known and w not in its_own and no_line(w)]
    needed.update(holes)
    print(f"   {'is    ' if is_found else 'is-not'} found: {sentence}. Its words with no prior line: {', '.join(holes) or 'none'}")
    known |= set(re.findall(r"[a-z]+(?:-[a-z]+)*", name.lower())) - {"a", "the"} | {name.replace("a ", "").replace("the ", "")}
    known |= {w + "s" for w in re.findall(r"[a-z]+", name.lower())}
for name, pattern in NOT_FOUND:
    n = len(re.findall(pattern, plain_text, re.I | re.M))
    found_all = found_all and n > 0
    print(f"   {'is    ' if n else 'is-not'} found: a direct sentence of {name}, {n}")
print(f"   all or none at all: {'all' if found_all and not needed else 'not all'}; {len(CHAIN)} concepts found with a direct sentence, {sum(1 for name, pattern in NOT_FOUND if not re.search(pattern, plain_text, re.I | re.M))} with none; "
      f"{len(needed)} words of the found sentences are named by no prior line")

print("\n11. The language resolving: prime-numberings, form, and a universe between co-chainings")
AS_SAID = "The primes are the many stable forms of the one fractal method, with numbers"
SAID_AGAIN = "A prime-numbering is a stable form of the one fractal method, and prime-numberings is its named universal set"
DISSOLVING = ["primes", "many", "forms"]
for word in DISSOLVING:
    print(f"   {word}: in the sentence as said {said(rf'\b{word}\b', AS_SAID)}, said again {said(rf'\b{word}\b', SAID_AGAIN)}; "
          f"the living files' places {said(rf'\b{word}\b', whole_text)}, the page's {said(rf'\b{word}\b', text)}")
print(f"   the sentence as said, with a dissolving word: {'is-not' if any(said(rf'\b{w}\b', AS_SAID) for w in DISSOLVING) else 'is'}; said again, with none: {'is' if not any(said(rf'\b{w}\b', SAID_AGAIN) for w in DISSOLVING) else 'is-not'}")
for n in (5, 6, 7, 12, 17):
    print(f"   {n}: {joined.lines[n]}")
for a_name in ("prime-numberings", "bi-co-universing", "floating-neutralling", "co-chainings"):
    print(f"   {a_name}: the living files' places {said(a_name.rstrip('s').replace('-n', '[- ]n'), whole_text)}; its parts named by no line: {', '.join(no_line(a_name)) or 'none'}")
for name, sentence in [("sequencing", "Sequencing is each coupling's own momentarying"), ("floating-neutralling", "Floating-neutralling is co-changing between sides, each with its own bounding and its own letting go"),
                       ("floating-neutralling", "Floating-neutralling is bounding-zeroing, each self's own with its coupling"), ("resolving", "Resolving is a self's momentarying, 1-now-existing"),
                       ("co-chaining", "Co-chaining is one sequence of steps from one opening sentence")]:
    print(f"   {'is    ' if sentence in plain_text else 'is-not'} found: {sentence}")
for name, pattern in [("numbering", r"(^|[.:] )(a )?numbering is "), ("a universe between co-chainings", r"univers\w+ [^.\n]{0,40}between [^.\n]{0,30}co-chain"), ("universing", r"universing")]:
    n = len(re.findall(pattern, whole_text.replace("**", ""), re.I | re.M))
    print(f"   {'is    ' if n else 'is-not'} found: a direct sentence of {name}, {n}")
print("   by the code, part 3's six cases: a self observing the same as its prior is same-existing and gives a 0, and a 0 is between its prior self and its next: is")

print("\n12. A sentence of the natural primes as a method, its named concepts found or found at no place")
THIRD = ("The natural primes are the universal stable-forming geodesic fractal-fracturing method of bi-co-intelligencing bi-folding surfaces "
         "as prime-podalings through sequential numberings of surface nows")
AGAIN = ("Natural prime numbering is the universal stable-forming geodesic fractal method of co-intelligencing bi-folding surfaces, "
         "as podalings through sequential numberings of a surface's moments")
print(f"   *{THIRD}*")
living_plain = whole_text.replace("**", "")
CONCEPTS = [("natural primes", r"natural primes\b", None), ("universal", r"\buniversal\b", joined.lines[6]),
            ("stable-forming", r"stable[- ]forming", "Stable-forming is fractal, with each scale by one method"),
            ("geodesic", r"geodesic", "Geodesic is its own existing thing, and a method is its stable form"),
            ("fractal-fracturing", r"fractal[- ]fractur", None), ("method", r"\bmethod\b", "Method is a relation, each self stable-forming with it"),
            ("bi-co-intelligencing", r"bi-co-intelligenc", None),
            ("co-intelligencing", r"co-intelligenc", "Co-intelligencing is selves observing, possibling and discovering within a universal set"),
            ("bi-folding", r"bi-fold", "each row is a bi-folding"), ("a surface", r"\bsurfaces?\b", "a surface is a between"),
            ("prime-podalings", r"prime[- ]podal", None), ("podaling", r"\bpodal", "Bi-co-podaling is going out and going back with one ring station"),
            ("sequential numberings", r"sequential numbering", None), ("a sequence", r"prior-sequence", joined.lines[17]),
            ("surface nows", r"surface nows?\b", None), ("now", r"\bnow\b", "Now is one, and each now-existing thing is with it")]
found_n = 0
for name, pattern, sentence in CONCEPTS:
    n = len(re.findall(pattern, living_plain, re.I))
    a_line = sentence is not None and sentence in joined.lines.values()
    is_found = sentence is not None and (a_line or (n > 0 and sentence in living_plain))
    found_n += is_found
    print(f"   {'is    ' if is_found else 'is-not'} found: {name}, " + ("a line of the opening" if a_line else f"the living files' places {n}") + (f": {sentence.replace('**', '')}" if is_found else ""))
none_of_it = [name for name, pattern, sentence in CONCEPTS if sentence is None]
print(f"   all or none at all, as said: not all; found at no place with a direct sentence: {', '.join(none_of_it)}")
print(f"   said again, its names found but for numbering and its own subject: *{AGAIN}*")
print(f"   its subject is the page's own title: {'is' if 'Natural Prime Numbering' in ' '.join(lines[:3]) else 'is-not'}; a dissolving word in it: {'is' if any(said(rf'\b{w}\b', AGAIN) for w in DISSOLVING) else 'is-not'}; "
      f"a name of it found at no place, numbering and its subject apart: {'is' if any(said(pattern, AGAIN) for name, pattern, sentence in CONCEPTS if sentence is None and name != 'sequential numberings') else 'is-not'}; "
      f"natural prime numbering, the living files' places {said('natural prime numbering', living_plain)}, the page's {said('natural prime numbering', text)}")

print("\n13. The sentence said again, explored for incohering, pair by pair")
RIGORIZED = ("Natural prime numbering is the universal stable-forming geodesic fractal method of selves co-intelligencing with bi-folding surfaces, "
             "as podalings through sequential numberings of their moments")
PAIRS = [("universal, a method", ["A universal set is the bounding method with no boundary"], True),
         ("stable-forming, fractal, a method", ["Stable-forming is fractal, with each scale by one method", "Method is one fractal method"], True),
         ("geodesic, a method, bi-folding surfaces", ["Geodesic is its own existing thing, and a method is its stable form", "A geodesic is a surface's own dividing"], True),
         ("a stable form and a stable-forming method, by scale", ["each a living method, stable-forming, with its own scale, and a stable form one scale outward"], True),
         ("co-intelligencing, and the sentence ahead of it with observing, possibling and discovering", ["Co-intelligencing is selves observing, possibling and discovering within a universal set"], True),
         ("co-intelligencing with a surface", ["Co-intelligencing is with a between", "a surface is a between"], True),
         ("a method living or non-living, in the living files", ["A method is non-living with each scale, each self stable-forming its own", "each a living method, stable-forming, with its own scale"], False)]
for name, sentences, cohering in PAIRS:
    all_found = all(s in living_plain for s in sentences)
    print(f"   {'cohering  ' if cohering else 'incohering'}: {name}; found: {'is' if all_found else 'IS NOT'}: " + " | ".join(sentences))
    assert all_found
turns, folded = [6, 30, 210, 2310], 0
for turn in turns:
    primes_of = [q for q in (2, 3, 5, 7, 11) if turn % q == 0]
    uncrossed = {n for n in range(1, turn) if all(n % q for q in primes_of)}
    assert all((turn - n) in uncrossed for n in uncrossed)
    folded += len(uncrossed)
print(f"   cohering  : bi-folding surfaces as podalings, in numbers: a turn of 6, 30, 210 and 2,310 folded about its middle lays its uncrossed places on its uncrossed places, {folded} places: is")
no_self = not re.search(r"\b(self|selves|me)\b", AGAIN)
print(f"   incohering: the sentence names no self and no me, {'is' if no_self else 'is-not'}; co-intelligencing is selves'; said with selves: {'is' if re.search(r'selves co-intelligencing with', RIGORIZED) else 'is-not'}")
print(f"   incohering: *a surface's moments*: a sequence of moments is a self's own, by 17 and 18, {'is' if 'its own prior-sequence' in joined.lines[18] else 'is-not'}; said as *their moments*: {'is' if 'their moments' in RIGORIZED else 'is-not'}")
print(f"   forward, the page's places of the sentence's names: stable-forming {said('stable-forming', text)}, co-intelligencing {said('co-intelligenc', text)}, bi-folding {said('bi-fold', text)}, podal {said('podal', text)}, geodesic {said('geodesic', text)}, fractal {said('fractal', text)}")
print(f"   rigorized: *{RIGORIZED}*")

print("\n14. Two sentences of the method, pair by pair: a stable-forming bi-folding method, 440, and a universal set or a thing")
FOUND = [("a bi-folding method, a stable-forming method", "the stable-forming bi-folding method", True),
         ("nothing surfaces in betweens", "a surface is a between: a nothing its other two places are either side of", True),
         ("the method, atom fractal stable form", "Atom is the stable form of unrelationing floating neutralling, in society and in selves and free of both, non-living in the universal set", True),
         ("all or none at all", "Fractal is all or none at all with scales", True),
         ("440 binary", "440 binary gates structuring as natural form's metabological resolver", True),
         ("the method, non-living", "A method is non-living with each scale, each self stable-forming its own", True),
         ("non-living and same-existing", "The universe is a non-living same-existing set", True),
         ("non-living and same-existing", "is non-living, step 20, same-existing with its prior, step 4", True),
         ("a stable form and same-existing, in words", "a non-living existing form with no same-existing for stable-forming", False),
         ("the method, living", "each a living method, stable-forming, with its own scale", False)]
for name, sentence, cohering in FOUND:
    assert sentence in living_plain, sentence
    print(f"   {'cohering  ' if cohering else 'incohering'}: {name}; found: {sentence}")
first = [q for q in range(2, 60) if all(q % d for d in range(2, q))]
count = []
plain_nand = with_nand.nand
with_nand.nand = lambda a, b: (count.append(1), plain_nand(a, b))[1]
with_nand.other_than(True)
an_other_than = len(count)
per = []
for k in range(4):
    count.clear()
    with_nand.a_cell(with_nand.TWO[1], [with_nand.TWO[-1]] * k)
    per.append(len(count))
with_nand.nand = plain_nand
ways = [(selves, (440 - per[0] * selves) // (per[1] - per[0])) for selves in range(1, 10) if (440 - per[0] * selves) >= 0 and (440 - per[0] * selves) % (per[1] - per[0]) == 0]
print(f"   440 is the seventeen primes 2 to 59 added: {'is' if len(first) == 17 and sum(first) == 440 else 'is-not'}; an other-than by the code is {an_other_than} nand, a binary gate")
print(f"   by the code a self's moment is {per[0]} nands and {per[1] - per[0]} more with a thing observed; 440 nands a moment by selves and things observed among them: {ways}; a self alone at 440: is-not")
ghost = sum(open(f, encoding="utf-8").read().count("A ghost is a universal") for f in glob.glob(str(ROOT / "incoming/*/*.md")))
print(f"   incohering: a universal same-named now-existing thing, beside *A ghost is a universal broken into a same-named now-existing thing*, laid at {ghost} places of the sessions' pages and in no living file; "
      f"6 has universal as a set's, and 7 the universe as a set")
print(f"   found at no place: fractured, the living files' places {said('fractured', living_plain)}; a bi-coupling of bi-couplings, {said(r'bi-coupl\w+ (of )?bi-couplings', living_plain)}")

print("\n15. A sensor and its sensationer, and an atom stable form: a universal bi-coupling explored as method")
BESIDE = [("a sensor and a sensationer, two sides", "A sensor and its sensationer have these two sides", True),
          ("a sensor-sensationer, a bi-coupling", "sensor-sensationer bi-coupling transmissioning", True),
          ("sensationing, a parity given, a + or a - alone", "it sensations, sharing a parity a body's couplings tip on, sign-only and taken or not", True),
          ("binary sequential, backward to 440 binary sequential other-thans", "binary co-sequential sensor-sensationing: an observing with a between of two", True),
          ("a bi-coupling", "A bi-coupling is two selves sharing possibling", True),
          ("a method, a relation", "Method is a relation, each self stable-forming with it", True),
          ("a method with a bi-coupling, non-living", "living's own condition with each bi-coupling at each scale", True),
          ("an atom stable form", "An atom is a non-living stable form a molecule's sharing winds round", True)]
for name, sentence, cohering in BESIDE:
    assert sentence in living_plain, sentence
    print(f"   cohering  : {name}; found: {sentence}")
moments, givings = 0, set()
for prior_a in (1, -1):
    for prior_b in (1, -1):
        give_a = give_b = None
        for moment in range(12):
            observed_a = [] if give_b is None else [with_nand.TWO[give_b]]
            observed_b = [] if give_a is None else [with_nand.TWO[give_a]]
            ga, next_a, a_gives, a_next = with_nand.a_cell(with_nand.TWO[prior_a], observed_a)
            gb, next_b, b_gives, b_next = with_nand.a_cell(with_nand.TWO[prior_b], observed_b)
            assert a_gives and b_gives and (moment == 0 or (observed_a and observed_b))
            give_a, give_b, prior_a, prior_b = with_nand.ONE[ga], with_nand.ONE[gb], with_nand.ONE[next_a], with_nand.ONE[next_b]
            givings |= {give_a, give_b}
            moments += 1
print(f"   by the code, two selves bi-coupled, four openings, {moments} moments: a self observes the other's giving and gives at all moments, a sensor and a sensationer both; "
      f"a giving is one of {sorted(givings)}, a parity alone and no magnitude: is")
print(f"   found at no place: a universal bi-coupling, the living files' places {said('universal bi-coupl', living_plain)}; fractured-fractal, {said('fractured[- ]fractal', living_plain)}; fractured, {said('fractured', living_plain)}")
print(f"   28: {joined.lines[28]}")
print("   incohering, to explore: 28 has a bi-coupling as both of two selves; an atom stable form is non-living, and 18 has a self with its own prior-sequence")

print("\n16. The method as a universal set of same-existing relations, and four names of a relation")
SET = [("the method, a universal set", "A universal set is the bounding method with no boundary", True),
       ("a universal set of same-existing", "A universal set is a set of same-existing things", True),
       ("a same-existing relation", "arising as living is a self's own same-existing relation establishing", True),
       ("a relation, a thing of a set, by 18", "A bi-coupling is a self", True),
       ("a relation and a set of relations, by scale", "One method at each scale is a fractal", True),
       ("co-chaining", "Co-chaining is one sequence of steps from one opening sentence", True),
       ("cohering", "Cohering is discovering next existing", True),
       ("co-chaining with cohering, the method's", "Chaining and not cohering is method's one break", True),
       ("bothbothing, a bi-coupling's", "IS bothboth with a between of two observings of one activity", True)]
for name, sentence, cohering in SET:
    assert sentence in living_plain, sentence
    print(f"   cohering  : {name}; found: {sentence}")
count = []
with_nand.nand = lambda a, b: (count.append(1), plain_nand(a, b))[1]
table = {(a, b): with_nand.both(a, b) for a in (True, False) for b in (True, False)}
count.clear()
with_nand.both(True, True)
nands_of_both = len(count)
with_nand.nand = plain_nand
print(f"   nandnanding: the living files' places {said('nandnand', living_plain)}, and nand's {said(r'\bnand\b', living_plain)}; by the code both is {nands_of_both} nands in a row, "
      f"and it is with both alone: {'is' if nands_of_both == 2 and all(v == (a and b) for (a, b), v in table.items()) else 'is-not'}")
print(f"   6: {joined.lines[6]}")
print(f"   the four names are four, and 6 has a set's things same-named: both is in 28, {'is' if 'both of two selves' in joined.lines[28] else 'is-not'}; "
      f"in the code's two nands, is; in bothbothing by its name; and co- in co-chaining and cohering waits at the card 35")

print("\n17. Resolved by cohering alone, a side with all and its other with not all")
import itertools
from functools import reduce
count = []
with_nand.nand = lambda a, b: (count.append(1), plain_nand(a, b))[1]
cases, nands = 0, {}
for n in (2, 4, 8):
    for things in itertools.product((True, False), repeat=n):
        count.clear()
        halves = things
        while len(halves) > 1:
            halves = [with_nand.both(halves[i], halves[i + 1]) for i in range(0, len(halves), 2)]
        in_a_row = reduce(with_nand.both, things)
        assert halves[0] == in_a_row == all(things)
        cases += 1
    nands[n] = len(count) // 2
with_nand.nand = plain_nand
print(f"   both of two is two nands; both of boths, of {', '.join(str(n) for n in nands)} things, and both in a row, link after link: with all alone, and with none of its other cases, {cases} cases: is; "
      f"its nands, {nands}, two less than twice its things")
print("   the four as one same-named relation, both, at four scales: with the code, is; with *Fractal is all or none at all with scales*, is; with *Method is one fractal method*, is; with 6, same-named, is; with 28, *both of two selves*, is: all")
assert "Method is one fractal method" in living_plain and "Fractal is all or none at all with scales" in living_plain and "same-named" in joined.lines[6]
print("   its other, four other-than relations in a set: with 6, is-not, by 4 things of four names are other-than things; with *Method is one fractal method*, is-not: not all")
print("   a bi-coupling's two as selves, a sensor and a sensationer both: with 28 as it is, is; with part 15's 48 moments, is; with *a method is its stable form* and an atom stable form non-living, is: all")
print("   its other, a sensor-sensationer with an atom stable form: with 28 as it is, is-not: not all")
RESOLVED = [("nandnanding", "both, two nands in a row", "the code, this part"),
            ("bothbothing", "both selves, a sensor and a sensationer both", "part 15, 48 moments"),
            ("a universal bi-coupling", "the universal set of same-existing bi-couplings", "part 16, and *A bi-coupling is a self*"),
            ("bi-co-intelligencing", "co-intelligencing both ways, a self observing and giving", "part 15, and bi-co- of *Bi-co-podaling is going out and going back with one ring station*"),
            ("prime-podaling", "a turn folded about its middle, its uncrossed places on its uncrossed places", "part 13, 538 places"),
            ("fractured-fractal", "a fractal with its break", f"the page's *120's fracture is the staircase's geodesic's last*, {said('fracture is the staircase', text)} found"),
            ("numbering", "a sequence's moments by twos", f"17, and the page's *A number is two moments*, {said('A number is two moments', text)} found")]
for name, resolving, by in RESOLVED:
    print(f"   {name}: {resolving}; by {by}")

print("\n18. The method going in two directions: 1x2, 2x3, 3x2, 2x4, 4x5, and on")
GIVEN = [(1, 2), (2, 3), (3, 2), (2, 4), (4, 5)]


def going(on, to=17):
    steps, at = [(1, 2)], 2
    while at < to:
        steps += [(at, at + 1), (at + 1, at), (at, on(at))]
        at = on(at)
    return steps


doubling, by_two = going(lambda h: 2 * h), going(lambda h: h + 2)
to_17 = doubling[:doubling.index((16, 17)) + 1]
its_numbers = sorted({n for step in to_17 for n in step})
print(f"   doubling, and one more and back: {', '.join(f'{a}x{b}' for a, b in to_17)}")
print(f"   its opening five are the five: {'is' if doubling[:5] == GIVEN else 'is-not'}; its other, on by two, and one more and back: {', '.join(f'{a}x{b}' for a, b in by_two[:8])}, its opening five the five: {'is' if by_two[:5] == GIVEN else 'is-not'}")
print(f"   doubling's opening step 1x2 is its own going on, 1 doubled, and at 1 the two directions are one, 1 and one more, and 1 doubled: {'is' if 1 + 1 == 2 * 1 else 'is-not'}; on by two's opening step is of its going on: {'is' if 1 + 2 == 2 else 'is-not'}")
count = []
with_nand.nand = lambda a, b: (count.append(1), plain_nand(a, b))[1]
cases = 0
for things in its_numbers[1:]:
    for case in itertools.product((True, False), repeat=things):
        count.clear()
        assert reduce(with_nand.both, case) == all(case) and len(count) == 2 * (things - 1)
        cases += 1
with_nand.nand = plain_nand
print(f"   by nand alone, both of {', '.join(str(n) for n in its_numbers[1:])} things is with all alone, {cases:,} cases: is; a thing more is two nands more, and its things doubled are its nands doubled and two more")
print(f"   to 17 it is {len(to_17)} steps and {len(its_numbers)} numbers, {its_numbers}; 1, 9 and 17 are among them, and the bi-folding's row 1-9-8-16 whole: {'is' if {1, 9, 17, 8, 16} <= set(its_numbers) else 'is-not'}")
for sentence in ["One, two, four and eight, the doubling that divides", "Across and along go alike by two directions", "1, 2 and 3 of one scale are 1, 9 and 17 of next",
                 "Bi-co-podaling is going out and going back with one ring station", "one more other, a co-chaining of bi-couplings", "bi-folding 1-9-8-16"]:
    assert sentence in living_plain, sentence
    print(f"   found beside it: {sentence}")
print("   resolved by cohering: doubling, with its opening step its own, the two folds of part 17, and the found sentences: all; on by two, with its opening step apart and no fold of part 17: not all")

print("\n19. The two directions cohering into the numbering: doubling, and one more or not")
to = 100_000
for n in range(1, to + 1):
    at = 1
    for one_more in bin(n)[3:]:
        at = 2 * at + (one_more == "1")
    assert at == n
for steps in range(12):
    assert len({int("1" + "".join(c), 2) for c in itertools.product("01", repeat=steps)}) == 2 ** steps
print(f"   a number is one sequence from 1 of doubling, with one more or not at a step, and a sequence is one number: 1 to {to:,}, and all sequences of 0 to 11 steps: is")


def uncrossed(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))


for prime in (q for q in range(3, 10_000) if uncrossed(q)):
    again = next(k for k in range(1, prime) if pow(2, k, prime) == 1)
    assert (prime - 1) % again == 0 and pow(2, prime - 1, prime) == 1
passing = [n for n in range(3, 2_048, 2) if not uncrossed(n) and pow(2, n - 1, n) == 1]
print(f"   round a prime, one more comes again with the prime's own steps, and doubling comes to 1 again by one short of it, primes 3 to 10,000: is; "
      f"crossed numbers passing doubling's closing, to 2,047: {passing}")
one_more_primes = [k for k in range(1, 33) if uncrossed(2 ** k + 1)]
print(f"   one more than a doubling, of 1 to 32 doublings, is uncrossed with {one_more_primes} doublings alone, a doubling's own number of them: "
      f"{'is' if all(k & (k - 1) == 0 for k in one_more_primes) else 'is-not'}; with 32, crossed by 641")
for sentence in ["Doubling round a prime above two closes by one short of it, by Fermat", "341 and 2,047 pass doubling's", "A number is two moments"]:
    assert sentence in text.replace("**", ""), sentence
    print(f"   the page's own, beside it: {sentence}")
print(f"   found beside it: Numbers are odd or even: {'is' if 'Numbers are odd or even' in living_plain else 'is-not'}; one more or not is a number's odd or even at a step")

print("\n20. A method living or non-living, in the living files: by scale, or non-living with all scales")
BY_SCALE = ["each a living method, stable-forming, with its own scale, and a stable form one scale outward",
            "A same-existing-society, a moment and the universe are three living sets",
            "The universe is a non-living same-existing set",
            "Atom is the stable form of unrelationing floating neutralling, in society and in selves and free of both, non-living in the universal set"]
WITH_ALL_SCALES = ["3.3 A method, a non-living existing thing", "A method is non-living with each scale, each self stable-forming its own"]
for sentence in BY_SCALE:
    assert sentence in living_plain, sentence
    print(f"   with by scale, living with its own scale and a non-living stable form one scale outward: {sentence}")
for sentence in WITH_ALL_SCALES:
    assert sentence in living_plain, sentence
    print(f"   with non-living with all scales, Natural Intelligence's own section: {sentence}")
print("   the living files part here, two files; by scale is with four sentences and both sayings of the universe, and non-living with all scales with its one section")

print("\n21. c, an atom's size matched with its moment; all or none at all with all-parity; and Natural Transmissioning")
six_path = next(iter(glob.glob(str(ROOT / "Exhibit_SIX_Natural_Transmissioning_*.md"))))
six = Path(six_path).read_text(encoding="utf-8").replace("**", "")
light, bond, turns = 299_792_458.0, 0.741e-10, 1.32e14
crossing = bond / light
print(f"   light's crossing of a hydrogen molecule, two atoms, 0.741 of a ten-billionth of a metre: {crossing * 1e21:.0f} zeptoseconds; a field's shortest measured moment, 2020, is 247")
print(f"   the molecule's own vibrating, 132 million million turns a second: a turn is {1 / turns / crossing:,.0f} crossings of light; the vibrating is not the shortest moment, and the crossing is")
for where, sentence in [(living_plain, "c is a ledger's space-to-time conversion, not a rate going across a gap"),
                        (living_plain, "A constant with a unit is a fixing, an exact value by a definition: speed of light from 1983"),
                        (six, "A transmissioning is sequencing and not timing"),
                        (six, "order has no rate"),
                        (living_plain, "each now-existing thing is-or-is-not within each universal set"),
                        (living_plain, "All-parity is with observing only, 7 and 15"),
                        (living_plain, "their stable form one scale outward is a bi-tri-involution of betweening"),
                        (living_plain, "said *ingesting* and *exhausting*")]:
    assert sentence in where, sentence
    print(f"   found: {sentence}")
print(f"   Natural Transmissioning's file is {Path(six_path).name}, a version's name behind the living files'; its places of all-parity {said('all-parity', six)}, light {said(chr(92) + 'blight' + chr(92) + 'b', six)}, "
      f"atom {said(chr(92) + 'batoms?' + chr(92) + 'b', six)}, stable form {said('stable form', six)}, nand {said(chr(92) + 'bnand' + chr(92) + 'b', six)}, rate {said(chr(92) + 'brates?' + chr(92) + 'b', six)}")
print(f"   found at no place of the living files: inhaling, {said('inhal', living_plain)}; a bump connector, {said('bump[- ]connector', living_plain)}")

print("\n22. Less than cohering, resolved farther: three moments, and the two numbers between them")
import math
radius, fine, proton = 0.529177e-10, 137.035999, 0.84e-15
a_crossing = radius / light
a_turn = 2 * math.pi * radius * fine / light
print(f"   light's crossing of an atom's radius: {a_crossing * 1e21:.0f} zeptoseconds; the atom's own turn: {a_turn * 1e18:.0f} attoseconds, {a_turn / a_crossing:.0f} crossings, a turn's 2 pi multiplied by {fine:.3f}")
print(f"   the molecule's vibrating turn: {1 / turns / a_turn:.1f} of the atom's turns, {1 / turns / a_crossing:,.0f} crossings of the radius")
print(f"   c matches the atom's size with light's crossing; the atom's own turn is matched with its size by c over {fine:.3f}: {'is' if abs(a_turn / a_crossing - 2 * math.pi * fine) < 1e-6 else 'is-not'}")
print(f"   137, the number's whole part, is uncrossed: {'is' if all(137 % q for q in range(2, 12)) else 'is-not'}; the number is not whole")
for where, sentence in [(living_plain, "A dimensionless constant, fine-structure constant first, is measured and defined by none"), (living_plain + text, "A nucleus is below five")]:
    assert sentence in where, sentence
    print(f"   found: {sentence}")
print(f"   below five: a nucleus's crossing is {2 * proton / light:.1e} seconds, and the atom's radius is {radius / proton:,.0f} of its; the fourteen prime scales open at 5, and 2 and 3 are at no rung")
print(f"   at no place of the living files: 1,836, {said('1,?836', living_plain)}, a field's weight of a nucleus's part over an electron's, the second number")

print("\n23. If c is at 61: the three moments' slowing, a rung by a rung, by prime scale numbering and by phi")
phi = (1 + 5 ** 0.5) / 2
inward, a_rung = a_turn / a_crossing, 1 / turns / a_turn
RUNGS = [(5, "atom"), (7, "molecule"), (11, "macromolecule"), (13, "protein-fold"), (17, "gene"), (19, "organelle"), (23, "cell"), (29, "tissue"), (31, "organ"), (37, "organism"),
         (41, "colony"), (43, "population"), (47, "community"), (53, "biosphere"), (59, "59"), (61, "61")]
print(f"   the two slowings: {inward:.1f}, light's crossing to the atom's turn; {a_rung:.1f}, the atom's turn to its molecule's, hydrogen's")
print(f"   by phi: {inward:.1f} is phi multiplied by itself {math.log(inward) / math.log(phi):.2f} times, and {a_rung:.1f} is {math.log(a_rung) / math.log(phi):.2f} times; "
      f"phi by 14 is {phi ** 14:.1f} and by 8 is {phi ** 8:.2f}: near, and not the same")
print(f"   by phi's turn, the golden angle of a turn's 360, {360 / phi ** 2:.3f}: 2 pi multiplied by it is {2 * math.pi * 360 / phi ** 2:.1f}, beside {inward:.1f}: {abs(2 * math.pi * 360 / phi ** 2 / inward - 1) * 100:.2f} of a hundred apart: near, and not the same")
print(f"   inward, by the rung's own slowing: light's crossing is {math.log(inward) / math.log(a_rung):.2f} rungs below the atom, at the place of 3 and 2, below five")
for steps, (prime, name) in enumerate(RUNGS):
    moment = a_turn * a_rung ** steps
    if prime in (7, 23, 37, 53, 59, 61):
        said_as = f"{moment:.2e} seconds" if moment < 1e-2 else f"{moment:.2f} seconds" if moment < 60 else f"{moment / 86400:.1f} days" if moment < 86400 * 365 else f"{moment / 86400 / 365.25:.0f} years"
        print(f"   outward, {steps} rungs, {prime} {name}: {said_as}")
print(f"   c at 61 by the rung's slowing: 61 is the slowest moment of the sixteen, and light's crossing the fastest, below 5: is-not at 61; 61 is one more than 60, a next turn's opening: {'is' if 61 == 60 + 1 else 'is-not'}")
for name, per_second in [("hydrogen's", 1.32e14), ("nitrogen's", 7.07e13), ("iodine's", 6.43e12)]:
    print(f"   a molecule's turn in its atom's turns, {name}: {1 / per_second / a_turn:,.0f}", end=";")
print(" the rung's slowing is no one number")

print(f"\n{places} places for a next draft, a suggestion apiece.")
