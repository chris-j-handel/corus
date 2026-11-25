"""A sentence of one relation, by its marks: a partner's word of 24 November, executed.

    python3 -I incoming/v406all2-2/instruments/a_sentence_of_one_relation_by_its_marks.py .
    python3 -I incoming/v406all2-2/instruments/a_sentence_of_one_relation_by_its_marks.py . FILE

A partner's word, said in plain words: natural naming and explaining is of sentences of one
relation, a compound sentence fuzzying the relationing.

1  Exhibit TWELVE Natural Explaining's own sentences of it, found in their home.
2  The sentences this folder's page offers to Exhibit THIRTY-TWO: a sentence with none of
   the marks of a compound sentence, a colon, a semicolon, a comma, and the words and, or, but.
3  The draft's sentences in bold, by the same marks: a finding for its writer. A mark alone
   decides nothing: by Natural Explaining a sentence of one claim with its instances listed
   is whole with its marks.

4  With a FILE after the set's place: that page's sentences, in bold and of a list, by the
   same marks, a sentence with a mark a line. A list's standing in brackets is passed over.
   A finding for its session, and no gate.

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
    line(len(offered) == 16 and numbered == list(range(1, 17)), "its offered sentences are numbered 1 to %d, a sentence a line" % len(offered))
    with_a_mark = [(k + 1, its_marks(s)) for k, s in enumerate(offered) if its_marks(s)]
    line(not with_a_mark, "a sentence of them is with none of the marks: a colon, a semicolon, a comma, and, or, but")
    for number, marks in with_a_mark:
        print("       sentence %d is with %s" % (number, " with ".join(marks)))
    one_end = all(len(re.findall(r"[.?!]", s)) == 1 and s.endswith(".") for s in offered)
    line(one_end, "a sentence of them ends once")
    away = ("co-parit", "observed", "surfac", "giving", "gives", "given")
    line(not any(word in s.lower() for s in offered for word in away), "no sentence of them says co-parity, observed, surfacing or giving")
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

    if len(sys.argv) > 2:
        print()
        print("4. A page's sentences, in bold and of a list, by the same marks:", sys.argv[2])
        its_page = Path(sys.argv[2]).read_text(encoding="utf-8")
        its_bolds = [b for b in re.findall(r"\*\*([^*\n]+?)\*\*", its_page) if len(b.split()) > 4 and b.rstrip().endswith(".")]
        of_a_list = []
        for a_line in re.findall(r"^\s*(?:-|\d+\.)\s+(.+)$", its_page, re.M):
            a_line = re.sub(r"\s*\([^()]*\)\s*$", "", re.sub(r"[*`]", "", a_line))
            of_a_list += [a for a in re.split(r"(?<=[.?!])\s+", a_line) if len(a.split()) > 2]
        for its_name, sentences in (("in bold", its_bolds), ("of a list", of_a_list)):
            its_marked = [(b, its_marks(b)) for b in sentences if its_marks(b)]
            print("found  ", "its sentences %s: %d, and %d of them with a mark" % (its_name, len(sentences), len(its_marked)))
            for b, marks in its_marked:
                print("found  ", "with %s: %s" % (" with ".join(marks), b[:90]))
