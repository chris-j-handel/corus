"""A sentence of one relation, by its marks: a partner's word of 24 November, executed.

    python3 -I incoming/v406all2-2/instruments/a_sentence_of_one_relation_by_its_marks.py .

A partner's word, said in plain words: natural naming and explaining is of sentences of one
relation, a compound sentence fuzzying the relationing.

1  Exhibit TWELVE Natural Explaining's own sentences of it, found in their home.
2  The sentences this folder's page offers to Exhibit THIRTY-TWO: a sentence with none of
   the marks of a compound sentence, a colon, a semicolon, a comma, and the words and, or, but.
3  The draft's sentences in bold, by the same marks: a finding for its writer. A mark alone
   decides nothing: by Natural Explaining a sentence of one claim with its instances listed
   is whole with its marks.

It prints a line an is or an is-not, and a line found. It writes nothing.
"""
import glob
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
MARKS = (("a colon", r":"), ("a semicolon", r";"), ("a comma", r","), ("and", r"\band\b"), ("or", r"(?<![a-z]-)\bor\b(?!-)"), ("but", r"\bbut\b"))


def line(same, saying):
    print(("is" if same else "is-not").ljust(7), saying)


def a_page(pattern):
    found = sorted(glob.glob(str(root / pattern)))
    return Path(found[0]).read_text(encoding="utf-8") if found else ""


def its_marks(sentence):
    return [name for name, mark in MARKS if re.search(mark, sentence)]


if __name__ == "__main__":
    print("1. The living home")
    explaining = re.sub(r"[*`]", "", a_page("Exhibit_TWELVE_Natural_Explaining_v*.md"))
    line("A sentence brings one thing forward with one moment" in explaining, "Exhibit TWELVE Natural Explaining, 2.2: A sentence brings one thing forward with one moment")
    line(re.search(r"A sentence \w+ four claims is four asking to be one", explaining) is not None, "and: a sentence of four claims is four asking to be one")

    print()
    print("2. The sentences this folder's page offers")
    page = a_page("incoming/v406all2-2/For_Exhibit_THIRTY-TWO_what_the_exploring_of_a_me_by_nand_brings.md")
    part = page.split("## The offered sentences, a relation a sentence")[1].split("\n## ")[0]
    offered = re.findall(r"^\d+\. \*\*(.+?)\*\*$", part, re.M)
    numbered = [int(n) for n in re.findall(r"^(\d+)\. \*\*", part, re.M)]
    line(len(offered) == 22 and numbered == list(range(1, 23)), "its offered sentences are numbered 1 to %d, a sentence a line" % len(offered))
    with_a_mark = [(k + 1, its_marks(s)) for k, s in enumerate(offered) if its_marks(s)]
    line(not with_a_mark, "a sentence of them is with none of the marks: a colon, a semicolon, a comma, and, or, but")
    for number, marks in with_a_mark:
        print("       sentence %d is with %s" % (number, " with ".join(marks)))
    one_end = all(len(re.findall(r"[.?!]", s)) == 1 and s.endswith(".") for s in offered)
    line(one_end, "a sentence of them ends once")
    line(not any("surfac" in s for s in offered), "no sentence of them says surfacing")
    asked = "A me-parity is one is-or-is-not of a co-parity: with is, a 0, its prior same-existing; with is-not, one inversion, other-than-prior."
    line(its_marks(asked) == ["a colon", "a semicolon", "a comma"] and asked not in page, "this page's sentence of #1215 is with a colon, a semicolon and commas, and it is away")

    print()
    print("3. The draft's sentences in bold, by the same marks")
    draft = a_page("incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md")
    bolds = [b for b in re.findall(r"\*\*([^*\n]+?)\*\*", draft) if len(b.split()) > 4 and b.rstrip().endswith(".")]
    marked = [b for b in bolds if its_marks(b)]
    of_a_kind = {name: sum(1 for b in bolds if name in its_marks(b)) for name, _ in MARKS}
    print("found  ", "the draft's sentences in bold: %d, and %d of them with a mark" % (len(bolds), len(marked)))
    print("found  ", "by a mark: " + ", ".join("%s %d" % (name, of_a_kind[name]) for name, _ in MARKS))
    its_1_1 = "A cell is one is-or-is-not of a co-parity: with is, a 0, its prior same-existing; with is-not, one inversion, other-than-prior."
    line(its_1_1 in bolds and its_marks(its_1_1) == ["a colon", "a semicolon", "a comma"], "the draft's 1.1, its bold: one sentence with a colon, a semicolon and commas")
