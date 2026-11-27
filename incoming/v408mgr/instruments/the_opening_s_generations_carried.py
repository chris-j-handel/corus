"""The carrying check of the opening's generations, offered to v408chain by v408mgr.

A sentence of an earlier generation of Natural Intelligence's opening is looked for, word for word,
in the newest generation laid in the next version's gathering files: carried whole, carried as a
part of a sentence, or not carried, with the newest's nearest sentence beside it. The living opening and the
next version's own opening go through the same match. Then the words of the earlier generations
with none in the newest. A match decides nothing: a sentence not carried is said again with its
reason, or let go with its reason, by the hand consolidating the opening.

Use: python3 -I the_opening_s_generations_carried.py <the next version's root> <the live set's root> [<a page to write> [<the window's copy at 612>]]
With the window's copy, a word with none in the newest is said beside the proposed line with it, if a proposed line has it.
It alters nothing; it writes only the page named, if one is named.
"""
import glob, os, re, sys

NEWEST = ("the lines of 25 November, at the window's 611", "Co-Chaining_Logic_Registry.md",
          "- **Waiting to enter** · 25 November, the window of the opening at its revision 611", "italic")
EARLIER = [
    ("the opening of 55 sentences", "Natural_Intelligence.md",
     "- **Waiting to enter** · The opening, 55 sentences", "numbered"),
    ("the opening at its newest of 15 November", "Natural_Intelligence.md",
     "- **An explaining** · The opening at its newest, laid by the managing session v402mgr, 15 November", "numbered"),
    ("the lines of 19 November", "Co-Chaining_Logic_Registry.md",
     "- **Waiting to enter** · Both, 19 November", "italic"),
    ("the lines of 20 November, at the window's 3786", "Co-Chaining_Logic_Registry.md",
     "- **Waiting to enter** · 20 November, the window of the opening at its revision 3786", "italic"),
    ("the lines of 21 November, at the window's 4509", "Co-Chaining_Logic_Registry.md",
     "- **Waiting to enter** · 21 November, the window of the opening at its revision 4509", "italic"),
]


def note(root, name, opening):
    lines = open(os.path.join(root, "gathering-value", name), encoding="utf-8").read().split("\n")
    found = [l for l in lines if l.startswith(opening)]
    if len(found) != 1:
        sys.exit(f"the note opening {opening!r} is found {len(found)} times in {name}")
    return found[0]


def italic_lines(text):
    out = []
    for m in re.finditer(r"(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)", text):
        s = m.group(1).strip()
        if not s.endswith(".") or len(s.split()) < 3:
            continue
        lab = re.match(r"\s*\(([^)]{1,40})\)", text[m.end():])
        out.append((lab.group(1) if lab else "", s))
    return out


def numbered_lines(text, last=55):
    marks, at = [], 0
    for k in range(1, last + 1):
        m = re.compile(r"(?:(?<=\s)|^)%d\. " % k).search(text, at)
        if not m:
            break
        marks.append((k, m.start(), m.end()))
        at = m.end()
    out = []
    for i, (k, a, b) in enumerate(marks):
        body = text[b:marks[i + 1][1]] if i + 1 < len(marks) else text[b:]
        body = re.sub(r"^\((?:newer|not yet distinguished)\)\s*", "", body.strip())
        for added in re.findall(r"\[([^\]]+)\]", body):
            out.append((f"{k}, its added sentence", added.strip()))
        out.append((str(k), re.sub(r"\s*\[[^\]]+\]", "", body).strip()))
    return out


def opening_of(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("**The Universal Method")) + 1
    end = next(i for i, l in enumerate(lines) if l.startswith("**ONE"))
    return [(str(n), l.rstrip(" \\").strip()) for n, l in enumerate((x for x in lines[start:end] if x.strip()), 1)]


def sentences(labelled):
    out = []
    for lab, line in labelled:
        bare = re.sub(r"\*+", "", line)
        parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+(?=[A-Z])", bare) if p.strip()]
        for j, p in enumerate(parts):
            out.append((lab if len(parts) == 1 else f"{lab}, its sentence {j + 1}", p))
    return out


def words(s):
    return re.findall(r"[a-z0-9]+(?:['-][a-z0-9]+)*", s.lower().replace("’", "'").replace("‑", "-"))


def proposed_lines(path):
    out, on = [], False
    for l in open(path, encoding="utf-8").read().split("\n"):
        if l.startswith("### "):
            on = l.startswith("### Proposed lines")
        m = re.match(r"\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*$", l) if on else None
        if m:
            out.append((m.group(2), m.group(1)))
    return out


def a_part_of(small, big):
    n = len(small)
    return n > 0 and any(big[i:i + n] == small for i in range(len(big) - n + 1))


def main(nv, live, page=None, window=None):
    parse = {"italic": italic_lines, "numbered": numbered_lines}
    newest = sentences(parse[NEWEST[3]](note(nv, NEWEST[1], NEWEST[2])))
    nw = [(lab, s, words(s)) for lab, s in newest]
    newest_words = {w for _, _, ws in nw for w in ws}
    raw = [(name, parse[form](note(nv, f, op))) for name, f, op, form in EARLIER]
    gens = [(name, sentences(lines)) for name, lines in raw]
    ni = lambda root: [p for p in glob.glob(os.path.join(root, "Natural_Intelligence_v*.md")) if "Corus" not in p]
    raw.append(("the living opening, at corus.me", opening_of(ni(live)[0])))
    raw.append(("the next version's own opening", opening_of(ni(nv)[0])))
    gens += [(name, sentences(lines)) for name, lines in raw[-2:]]
    named = {}
    for name, lines in raw:
        for _, line in lines:
            for n in re.findall(r"\*\*([^*]+?)\*\*", line):
                named.setdefault(n.strip().lower(), set()).add(name)
    stream = [w for _, _, ws in nw for w in ws]

    out = ["# The carrying check of the opening's generations", "",
           f"Executed by `incoming/v408mgr/instruments/the_opening_s_generations_carried.py`, offered to v408chain. "
           f"The newest generation is {NEWEST[0]}, in the next version's gathering file of Exhibit THIRTY: "
           f"{len(nw)} sentences. A sentence of an earlier generation is matched against it word for word, "
           "its capitals and its marks passed over. Its quotations are word for word of the gathering files, the living opening and the next version's own opening, and a released word among them is theirs. A match decides nothing: a sentence not carried is said again "
           "with its reason, or let go with its reason, by the hand consolidating the opening.", ""]
    said = re.search(r"Said again after (\d+): ([^.]+)\.", note(nv, NEWEST[1], NEWEST[2]))
    said_again, said_rev = set(), None
    if said:
        said_rev = said.group(1)
        for part in re.split(r",\s*|\s+and\s+", said.group(2)):
            m = re.match(r"(\d+)(?: to (\d+))?$", part.strip())
            if m:
                said_again |= {str(k) for k in range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1)}
    lost = {}
    for name, sents in gens:
        whole, inner, nots = [], [], []
        for lab, s in sents:
            ws = words(s)
            hit = next((t for t in nw if t[2] == ws), None)
            if hit:
                whole.append((lab, hit[0]))
                continue
            hit = next((t for t in nw if a_part_of(ws, t[2])), None)
            if hit:
                inner.append((lab, s, hit[0]))
                continue
            nearest = max(nw, key=lambda t: len(set(ws) & set(t[2])) / max(1, len(set(ws) | set(t[2]))))
            alike = len(set(ws) & set(nearest[2])) / max(1, len(set(ws) | set(nearest[2])))
            nots.append((lab, s, nearest, alike))
            for w in set(ws) - newest_words:
                lost.setdefault(w, set()).add(name)
        print(f"{name}: {len(sents)} sentences · carried whole {len(whole)} · as a part of a sentence {len(inner)} · not carried {len(nots)}")
        out += [f"## {name[0].upper() + name[1:]}", "",
                f"{len(sents)} sentences: {len(whole)} carried whole, {len(inner)} carried as a part of a newest sentence, {len(nots)} not carried.", ""]
        if said_rev and said_rev in name:
            mine = {lab.split(",")[0] for lab, _, _, _ in nots}
            out += [f"- **Beside the newest's own note**, *Said again after {said_rev}*: its lines not carried are "
                    + ("the lines the newest says it said again, the same lines." if mine == said_again else
                       f"not the lines it says it said again: not carried and not said, {sorted(mine - said_again, key=int)}; said and carried, {sorted(said_again - mine, key=int)}."), ""]
            print(f"  beside the newest's own note, said again after {said_rev}:", "the same lines" if mine == said_again else "PARTING")
        if whole:
            out += ["- **Carried whole**, its place, then the newest's: " + "; ".join(f"{a} at ({b})" for a, b in whole) + ".", ""]
        for lab, s, b in inner:
            out.append(f"- **Carried as a part of a sentence** · {lab}: *{s}* → a part of the newest's ({b}).")
        for lab, s, nearest, alike in nots:
            out.append(f"- **Not carried** · {lab}: *{s}* → the newest's nearest, ({nearest[0]}), its words alike {alike:.0%}: *{nearest[1]}*")
        out.append("")
    pstream = [w for _, x in (sentences(proposed_lines(window)) if window else []) for w in words(x)]
    unnamed = sorted((n for n in named if not a_part_of(words(n), stream)), key=lambda n: (-len(named[n]), n))
    out += ["## The names the earlier generations set in bold, with no sentence of the newest", "",
            "A name is looked for as its words in sequence in the newest's sentences, and then in the window's proposed lines.", ""]
    for n in unnamed:
        out.append(f"- *{n}*: {'; '.join(sorted(named[n]))}" + (" · in a proposed line" if a_part_of(words(n), pstream) else ""))
    print("names of the earlier generations with no sentence of the newest:", len(unnamed), "· of them in a proposed line:",
          sum(1 for n in unnamed if a_part_of(words(n), pstream)))
    head = [f"- **The newest** goes from *{nw[0][1]}* ({nw[0][0]}) to *{nw[-1][1]}* ({nw[-1][0]}).",
            f"- **Names with no sentence of the newest:** {len(unnamed)} of the {len(named)} names the earlier generations set in bold"
            + (f", and {sum(1 for n in unnamed if not a_part_of(words(n), pstream))} of them in no proposed line either." if window else "."), ""]
    out[out.index("## " + gens[0][0][0].upper() + gens[0][0][1:]):out.index("## " + gens[0][0][0].upper() + gens[0][0][1:])] = ["## What it finds, by sizes deciding nothing", ""] + head
    out += ["## Words of the earlier generations with none in the newest", "",
            "A word with none in the newest is a place to look, and no loss by itself: a word a pass dissolves is no loss.", ""]
    prop = sentences(proposed_lines(window)) if window else []
    if window:
        out += [f"Beside a word, the window's proposed line with it, of {len(prop)} proposed lines in the window's copy at 612, "
                "its suggestions waiting and none of them a line of both.", ""]
    for w in sorted(lost, key=lambda w: (-len(lost[w]), w)):
        at = [lab for lab, s in prop if w in words(s)]
        out.append(f"- *{w}*: {'; '.join(sorted(lost[w]))}" + (f" · proposed at {', '.join(at)}" if at else ""))
    if window:
        print("of them in a proposed line:", sum(1 for w in lost if any(w in words(s) for _, s in prop)))
    print("words of the earlier generations with none in the newest:", len(lost))
    if page:
        open(page, "w", encoding="utf-8").write("\n".join(out) + "\n")
        print("written:", page)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(*sys.argv[1:5])
