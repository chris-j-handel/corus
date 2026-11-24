"""An exhibit in its four ways, as Exhibit TWELVE Natural Explaining 1.2 has a subject four times over, with a
partner's saying of 23 November of the third and the fourth: a title and subtitle; a floating neutralling contents;
bolds, a bold co-chaining to its next and aimed at its part's opening bold; and sentences bringing one thing forward,
a paragraph with its spacing. It goes through a file, a living file or a draft with a living file's head, and writes
nothing. A line is a mark, a place for a self going through, and decides nothing, as Natural Explaining 2.2 has a length.

    python3 -I incoming/v406me/instruments/an_exhibit_in_its_four_ways.py FILE [FILE ...]
"""
import re, sys, statistics, os

STOP = set("""a an and or of with its it is are as at by to in on for from no not one two three four five six seven all
that this these those then than but so nor each other-than both into out up down be has have had was were can may will own
their his her our your more most less least again alone along across about past short whole first last next prior now""".split())

def words(t):
    t = re.sub(r"`[^`]*`", " ", t)
    out = set()
    for w in re.findall(r"[A-Za-zφ][A-Za-zφ'-]{2,}", t):
        w = w.lower().split("'")[0]
        w = re.sub(r"(ings|ing|es|s)$", "", w) if len(w) > 5 else w
        if w and w not in STOP and len(w) > 2:
            out.add(w)
    return out

def go(path):
    L = open(path, encoding="utf-8").read().split("\n")
    title_i = next(i for i, l in enumerate(L) if l.startswith("# "))
    title = L[title_i][2:].strip()
    sub = next((l.strip().strip("*") for l in L[title_i + 1:title_i + 12] if re.match(r"^\*\*.+\*\*$", l.strip())), "")
    # an exhibit whole has a head closed by a rule; a part offered alone has none, and its parts open at its title
    body_i = next((i for i, l in enumerate(L) if l.strip() == "---" and any(x.startswith("# ") for x in L[i + 1:i + 4])), title_i - 1)
    end = next((i for i, l in enumerate(L) if i > body_i and re.match(r"^## Sources|^\*\*Executed", l)), len(L))
    body = L[body_i + 1:end]
    print(f"\n=== {os.path.basename(path)}: {sum(len(l.split()) for l in body)} words in its parts")

    # 1. a title and its subtitle
    btext = " ".join(l for l in body if not l.startswith("#")).lower()
    print("1. Title and subtitle")
    print(f"   {title!r} · {sub!r}")
    print(f"   the subtitle opens with an -ing: {bool(re.match(r'^[A-Za-z-]+ing\b', sub))}; in its parts, the title's and the subtitle's words: " +
          ", ".join(f"{w} {len(re.findall(r'\b' + re.escape(w.lower()), btext))}" for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9-]{3,}", title + ' ' + sub)))

    # 2. a floating neutralling contents: its parts' and sections' titles
    heads = [(i, len(m.group(1)), m.group(2).strip()) for i, l in enumerate(body) for m in [re.match(r"^(#{1,3}) (.*)$", l)] if m]
    parts = [h for h in heads if h[1] == 1]; secs = [h for h in heads if h[1] == 2]
    bare = lambda t: re.sub(r"^(\d+(\.\d+)*|[A-Z-]+ ·)\s*", "", t).strip()
    the = [t for _, _, t in heads if re.match(r"(?i)^the\b", bare(t))]
    two = [t for _, _, t in secs if re.search(r",? and ", bare(t))]
    print("2. Contents")
    print(f"   parts {len(parts)}, sections {len(secs)}; a title opening with the: {len(the)}" + (f", as {[bare(t)[:34] for t in the[:4]]}" if the else ""))
    print(f"   a section's title joining with and: {len(two)} of {len(secs)}" + (f", as {[bare(t)[:40] for t in two[:4]]}" if two else ""))

    # paragraphs, with their bold openers
    paras, cur, part, sec = [], [], None, None
    def flush():
        if cur:
            t = " ".join(cur).strip()
            if t and t not in ("&nbsp;", "---") and not t.startswith("|") and not re.match(r"^- |^\d+\. ", t):
                paras.append((part, sec, t))
            cur.clear()
    for l in body:
        m = re.match(r"^(#{1,3}) (.*)$", l)
        if m:
            flush()
            if len(m.group(1)) == 1: part, sec = m.group(2).strip(), None
            else: sec = m.group(2).strip()
        elif not l.strip(): flush()
        else: cur.append(l.strip())
    flush()
    opener = lambda t: (re.match(r"^\*\*(.+?)\*\*", t) or [None, None])[1]
    bolds = [(p, s, opener(t)) for p, s, t in paras if opener(t)]
    covered = 0
    for _, _, t in secs:
        mine = " ".join(b for p, s, b in bolds if s == t)
        w = words(bare(t))
        if w and len(w & words(mine)) * 2 >= len(w): covered += 1
    print(f"   a section's title with one of two of its words or more in its own bolds: {covered} of {len(secs)}")

    # 3. bolds: a bold co-chaining to its next, and aimed at its part's opening bold
    print("3. Bolds")
    print(f"   paragraphs {len(paras)}; opening with a bold: {len(bolds)}; with no bold: {len(paras) - len(bolds)}")
    destiny = {}
    for p, s, b in bolds:
        destiny.setdefault(p, b)
    no_d = [p for p in dict.fromkeys(p for p, _, _ in paras) if p and not any(pp == p and s is None for pp, s, _ in bolds)]
    print(f"   parts opening with a bold ahead of their sections: {len(parts) - len(no_d)} of {len(parts)}" + (f"; with none: {[x[:30] for x in no_d]}" if no_d else ""))
    breaks, aimed, n = [], 0, 0
    for k in range(1, len(bolds)):
        (p0, s0, b0), (p1, s1, b1) = bolds[k - 1], bolds[k]
        if p0 != p1: continue
        n += 1
        w1 = words(b1)
        chained = bool(w1 & words(b0))
        aim = bool(w1 & (words(destiny[p1]) | words(p1) | words(s1 or "")))
        aimed += aim
        if not chained: breaks.append((s1 or p1, b1, aim))
    print(f"   a bold with a word of its prior bold, in one part: {n - len(breaks)} of {n}; with a word of its part's opening bold or its own titles: {aimed} of {n}")
    lost = [(s, b) for s, b, aim in breaks if not aim]
    print(f"   a bold with no word of its prior bold: {len(breaks)}; of them with no word of its part's opening bold or its titles: {len(lost)}")
    for s, b in lost[:6]: print(f"      {bare(s)[:30]!r}: {b[:86]!r}")
    prose = " ".join(t for _, _, t in paras)
    marks = re.findall(r"(?<![\d.,])\b\d{1,2}\.\d{1,2}\b(?![\d,]*\d)", prose)
    print(f"   a section's number standing for its concept in a sentence, Natural Explaining 2.7: {len(marks)}")

    # 4. sentences bringing one thing forward, and a paragraph's spacing
    print("4. Sentences and paragraphs")
    sents = [s for _, _, t in paras for s in re.split(r"(?<=[.!?])\*{0,2}\s+(?=\*{0,2}[A-Z0-9φ])", t) if len(s.split()) > 2]
    n_w = sorted(len(s.split()) for s in sents)
    many = [s for s in sents if len(re.findall(r"[,;:]", s)) >= 6]
    the_s = [s for s in sents if re.match(r"^\*{0,2}The\b", s)]
    print(f"   sentences {len(sents)}; words in one, its middle {int(statistics.median(n_w))}, nine of ten at {n_w[int(len(n_w) * .9)]} or fewer, its longest {n_w[-1]}")
    print(f"   a sentence with six joinings or more, a mark of claims asking to be one: {len(many)}; a sentence opening with The: {len(the_s)}")
    per = sorted(len([s for s in re.split(r"(?<=[.!?])\*{0,2}\s+(?=\*{0,2}[A-Z0-9φ])", t) if s.strip()]) for _, _, t in paras)
    wp = sorted(len(t.split()) for _, _, t in paras)
    print(f"   sentences in a paragraph, its middle {int(statistics.median(per))}, its most {per[-1]}; words in a paragraph, its middle {int(statistics.median(wp))}, its most {wp[-1]}")
    plain = lambda l: l.strip() and not l.startswith(("|", "-", " ", "#")) and not re.match(r"^\d+\. ", l)
    run = [i for i in range(1, len(body)) if plain(body[i]) and plain(body[i - 1])]
    ahead = sum(1 for i, lv, t in parts if any(x.strip() == "&nbsp;" for x in body[max(0, i - 3):i]))
    print(f"   a paragraph with no spacing line ahead of it: {len(run)}; a part with a spacing line of &nbsp; ahead of it, as Me has: {ahead} of {len(parts)}")

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(0)
for f in sys.argv[1:]:
    go(f)
