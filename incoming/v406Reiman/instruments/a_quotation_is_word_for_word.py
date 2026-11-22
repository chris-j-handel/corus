"""A quotation in italics of a page, set beside the set: is it word for word in a page of the set.

    python3 -I incoming/v406Reiman/instruments/a_quotation_is_word_for_word.py . PAGE [PAGE ...]

A span in italics of five words or more is taken as a quotation. A span found in
no page of the set is printed, for the session's own going through: a title or a
session's own saying in italics is no quotation.
"""
import re
import sys
from pathlib import Path

root, pages = Path(sys.argv[1]), sys.argv[2:]
own = {Path(p).resolve() for p in pages}
texts = []
for p in list(root.glob("*.md")) + list(root.glob("gathering-value/*.md")) + list(root.glob("incoming/**/*.md")):
    if p.resolve() not in own and "v406Reiman" not in p.parts:
        texts.append(re.sub(r"\*\*", "", p.read_text(encoding="utf-8")))
for page in pages:
    text = Path(page).read_text(encoding="utf-8")
    spans = re.findall(r"(?<!\*)\*(?!\*)([^*\n]{3,}?)(?<!\*)\*(?!\*)", text)
    found = missing = 0
    for s in spans:
        if len(s.split()) < 5:
            continue
        if any(s in t for t in texts):
            found += 1
        else:
            missing += 1
            print("  in no page of the set:", s[:150])
    print(f"{page}: {found} quotations word for word in the set, {missing} spans in italics in no page of it")
