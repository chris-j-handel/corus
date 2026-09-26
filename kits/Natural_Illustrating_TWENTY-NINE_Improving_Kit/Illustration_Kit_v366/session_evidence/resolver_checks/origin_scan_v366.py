#!/usr/bin/env python3
"""origin_scan_v366.py · the origin scan, carried at the ONE and TWO kit (note FF05)

Runs the published living set against the origin sentence and returns the
counts the v365 notes carry (Living Improving Value, YY01 to YY12 and ZZ01 to
ZZ07). Standard library only. Anyone can run it.

    git clone https://github.com/chris-j-handel/corus
    python3 origin_scan_v366.py corus

Every count is so far: it reads the files as they stand at the clone.
A file's retained supports (between <!-- SUPPORT BEGIN --> and
<!-- SUPPORT END -->) are counted apart from its numbered paragraphs, since
the file parts them itself (Method Improving Value, FF04).
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ORIGIN = re.compile(r"all existing things|all things that exist|all things existing", re.I)
ERROR_FORM = re.compile(r"\ban existing thing\b", re.I)
UNIVERSE_SAYS = re.compile(
    r"[^.\n]{0,160}\b(this universe|a universe|our universe|a left universe|"
    r"(?:the|this|our) universe (?:is|has|includes|contains|holds)|"
    r"(?:inside|within|in|into) (?:the|this|our|a) universe)\b[^.\n]{0,160}",
    re.I,
)
DEGREE_AT_EXISTING = re.compile(
    r"\b(partly|partially|mostly|almost|nearly|barely|hardly|more|less|somewhat|half|quasi|semi|largely)"
    r"[- ](exist\w*|real)\b|\bdegrees? of (existence|existing|being|reality)\b|"
    r"\bexist\w* (partly|partially|mostly|to some degree|in part|more or less)\b",
    re.I,
)
SPEAKER = re.compile(r"\b(the user|user|assistant|I’ll|I'll|I’m|I'm|ChatGPT|Claude)\b", re.I)
# The held face: field words that are not a speaker.
HELD_SPEAKER = re.compile(r"\beach user\b|\buser's gain\b|between user and surface|decoupling the user|couples with the user", re.I)
DEGREE_WORDS = re.compile(
    r"\b(most of|almost|nearly|usually|often|largely|mostly|partly|with few exceptions)\b", re.I
)
WORDS = ("ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE THIRTEEN FOURTEEN "
         "FIFTEEN SIXTEEN SEVENTEEN EIGHTEEN NINETEEN TWENTY").split()
WORDS += ["TWENTY-" + w for w in ("ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT")]
CITATION = re.compile(
    r"(?<![-\w])(" + "|".join(sorted(map(re.escape, WORDS), key=len, reverse=True)) + r")\s+(v\d{3,4}[a-z]?)\b"
)
SUPPORT = re.compile(r"<!-- SUPPORT BEGIN -->|<!-- SUPPORT END -->")


def faces(text):
    """The numbered paragraphs and the retained supports, as the file parts them."""
    parts = SUPPORT.split(text)
    return "".join(parts[0::2]), "".join(parts[1::2])


def lines_matching(text, pattern, skip=None):
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        if pattern.search(line) and not (skip and skip.search(line)):
            out.append((n, line.strip()[:200]))
    return out


def main(root):
    root = Path(root)
    listed = json.loads((root / "files.json").read_text(encoding="utf8"))
    md = [f for f in listed if f.endswith(".md")]
    published = {}
    for f in md:
        m = re.match(r"Exhibit_([A-Z-]+?)_[A-Z].*_(v\d+[a-z]?)\.md$", f)
        if m:
            published[m.group(1)] = m.group(2)

    print(f"Origin scan v365 · {len(md)} published files at {root}\n")

    print("1 · The origin sentence and the error's form, at the numbered paragraphs and at the supports")
    for f in md:
        text = (root / f).read_text(encoding="utf8")
        body, supports = faces(text)
        o_b, o_s = len(ORIGIN.findall(body)), len(ORIGIN.findall(supports))
        e = len(ERROR_FORM.findall(text))
        if o_b or o_s or e:
            print(f"   {f}: origin {o_b} numbered, {o_s} supports; 'an existing thing' {e}")
    print()

    print("2 · Where a file says what the universe is, counts universes, or sets it in a container")
    for f in md:
        body, _ = faces((root / f).read_text(encoding="utf8"))
        hits = [m.group(0).strip() for m in UNIVERSE_SAYS.finditer(body)]
        for h in hits:
            print(f"   {f}: …{h[:220]}…")
    print()

    print("3 · Degree words set on existing (YY11: none expected)")
    total = 0
    for f in md:
        body, supports = faces((root / f).read_text(encoding="utf8"))
        for face, s in (("numbered", body), ("supports", supports)):
            for m in DEGREE_AT_EXISTING.finditer(s):
                total += 1
                print(f"   {f} ({face}): {m.group(0)}")
    print(f"   total: {total}\n")

    print("4 · The speaker at the living voice (ZZ03, ZZ04); field words at the held face skipped")
    for f in md:
        text = (root / f).read_text(encoding="utf8")
        body, supports = faces(text)
        found = lines_matching(body, SPEAKER, HELD_SPEAKER)
        s_count = len(SPEAKER.findall(supports))
        if found or s_count:
            print(f"   {f}: {len(found)} line(s) at the numbered paragraphs; {s_count} marks at the supports")
            for n, line in found[:6]:
                print(f"      numbered line {n}: {line}")
    print()

    print("5 · Citations of versions the site does not publish (ZZ03)")
    for f in md:
        body, supports = faces((root / f).read_text(encoding="utf8"))
        for face, s in (("numbered", body), ("supports", supports)):
            c = Counter(f"{w} {v}" for w, v in CITATION.findall(s) if w in published and published[w] != v)
            if c:
                print(f"   {f} ({face}): {sum(c.values())} · " + ", ".join(f"{k} ({n})" for k, n in c.most_common()))
    print()

    print("6 · Sizes: the numbered paragraphs and the supports (ZZ03)")
    for f in md:
        raw = (root / f).read_bytes()
        body, supports = faces(raw.decode("utf8"))
        if supports:
            b, s = len(body.encode("utf8")), len(supports.encode("utf8"))
            print(f"   {f}: {len(raw):,} bytes; numbered {b:,} ({len(body.split()):,} words); "
                  f"supports {s:,} ({len(supports.split()):,} words), {100 * s / len(raw):.1f}%")
    print()

    print("7 · Degree words, raw, at the numbered paragraphs (XX05 sorts them at the held face and the living voice)")
    for f in md:
        body, _ = faces((root / f).read_text(encoding="utf8"))
        n = len(DEGREE_WORDS.findall(body))
        if n:
            print(f"   {f}: {n}")
    print()

    print("8 · The public front (ZZ05, ZZ06)")
    index = (root / "index.html").read_text(encoding="utf8") if (root / "index.html").exists() else ""
    has_origin = "yes" if ORIGIN.search(index) else "no"
    has_description = "yes" if 'name="description"' in index else "no"
    print(f"   index.html carries the origin sentence: {has_origin}")
    print(f"   index.html carries a page description: {has_description}")
    names = {p.name.lower() for p in root.iterdir()}
    print(f"   README at the repository: {'yes' if any(n.startswith('readme') for n in names) else 'no'}")
    print(f"   licence at the repository: {'yes' if any(n.startswith(('license', 'licence', 'copying')) for n in names) else 'no'}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
