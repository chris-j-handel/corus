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

print(f"\n{places} places for a next draft, a suggestion apiece.")
