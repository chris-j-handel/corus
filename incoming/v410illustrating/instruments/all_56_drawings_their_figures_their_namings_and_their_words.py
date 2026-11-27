"""v410illustrating · all 56 drawings gone through for their figures, their namings of one another and their words.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/all_56_drawings_their_figures_their_namings_and_their_words.py . THE_ROOT_WITH_V408ILLUSTRATING [THE_NEXT_VERSION] [--lay]

The 40th to the 56th drawings are v408illustrating's, in its offer #1294. Until that offer is brought in, the second
path is a worktree of its head, and with it brought in the second path is the root again:
  git fetch --depth=60 origin refs/pull/1294/head:refs/remotes/pull/1294
  git worktree add ../v408illustrating_at_its_wrap refs/remotes/pull/1294
The third path is a worktree of the next version, for its files' words; with none, that column is not said.

Do no harm: it opens the drawings' artboards, v408illustrating's table and the living files, and writes in none of
them. With --lay it writes two tables in this session's folder alone, a drawing a row and a word a row.

Executed here, at all 56 drawings, from a drawing's own text, found as v408illustrating's maker of its table finds it:
  where a drawing's own text names an other drawing, and the parts the set falls into by those namings;
  numbers said by more than one drawing, executed apart and found in the texts;
  one thing said by more than one name, the names found in the texts;
  the words a partner asked of, numbered; and the drawings' words that are in no living file.
Judged by this session on 27 November, by looking at all 56 views, and laid below as it was judged:
  a drawing's figure, the thing drawn. A drawing is in one figure. A figure's name is this session's placing.
A line is an is, executed here; or found, a thing found and laid whole; or judged, and said as judged.
"""
import csv, html, re, sys
from collections import Counter
from pathlib import Path

G1, G2, G3 = "incoming/v406geodesic/", "incoming/v406geodesic2/", "incoming/v408illustrating/"
MINE = "incoming/v410illustrating/"

# judged on 27 November, by looking at all 56 views: a drawing's figure, the thing drawn
FIGURES = [
    ("the one triangle on a sphere, bi-folding, and 1 to 17 on a torus", [1, 2, 3, 4, 5, 6]),
    ("rounds of six about a 0, a cube's shells 1, 7, 19, 37 and 61", [7, 8, 40, 41, 50]),
    ("cones of 30 on the co-linear, 0, 30, 60, 90 and 120", [9, 10, 11, 12, 13, 14, 15, 16, 17]),
    ("the diamond of nine, and 3, 5 and 7", [18, 19, 20, 21, 22, 23, 24]),
    ("a me, its prior and its other, at one moment", [25, 26]),
    ("a path of mes closing, a row a moment", [27, 28, 32, 33, 34, 47, 51]),
    ("nand, and a parity two wires", [29, 30, 35]),
    ("the staircase, and the between going through", [36, 37, 39]),
    ("rows of 30, and their eight", [38, 46, 56]),
    ("two primes, a number round the one and round the other", [43, 45, 48]),
    ("a seam, even, odd, even", [49, 52, 53, 54, 55]),
    ("a table of the work itself", [31, 42, 44]),
]
FIGURE_OF = {n: name for name, ns in FIGURES for n in ns}

def folder(n): return G1 if n <= 3 else G2 if n <= 39 else G3
def session(n): return "v406geodesic" if n <= 3 else "v406geodesic2" if n <= 39 else "v408illustrating"
def root_of(n): return ROOT if n <= 39 else V408

def text_of(n):
    if n <= 3: f = sorted((root_of(n) / (G1 + "illustrations")).glob(f"draft_{n}_*.svg"))[0]
    else: f = root_of(n) / (folder(n) + f"illustrations/artboards/Draft{n}.dc.html")
    t = f.read_text(encoding="utf-8")
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return "\n".join(l for l in (re.sub(r"\s+", " ", x).strip() for x in t.splitlines()) if l)
def name_of(n):
    f = sorted((root_of(n) / (folder(n) + "illustrations")).glob(f"draft_{n}_*.png"))[0].stem
    return f.split("_", 2)[2].replace("_", " ")

# ---- where a drawing's own text names an other drawing
ORD = {w: i + 1 for i, w in enumerate("first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth "
       "fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth".split())}
OW = "|".join(ORD)
def named_in(n, t):
    out = {}
    def add(k, line):
        if 1 <= k <= 56 and k != n: out.setdefault(k, line[:100])
    for l in t.splitlines():
        for m in re.finditer(r"\b(\d{1,2})(?:st|nd|rd|th) drawing", l): add(int(m.group(1)), l)          # the 32nd drawing
        m = re.search(r"((?:\d{1,2}(?:st|nd|rd|th)(?:, | and (?:the )?)?)+) drawings", l)                # the 52nd, 53rd and 54th drawings
        if m:
            for k in re.findall(r"\d+", m.group(1)): add(int(k), l)
        m = re.search(r"drawings (\d{1,2}) to (\d{1,2})", l)                                             # drawings 32 to 34
        if m:
            for k in range(int(m.group(1)), int(m.group(2)) + 1): add(k, l)
        for m in re.finditer(r"\bthe (\d{1,2})(?:st|nd|rd|th)'s", l): add(int(m.group(1)), l)            # the 47th's five mes
        for m in re.finditer(r"\b(?:beside|of|at|by) the (\d{1,2})(?:st|nd|rd|th)\b(?! prime| of)", l): add(int(m.group(1)), l)
        for m in re.finditer(r"\b(%s) drawing" % OW, l, re.I): add(ORD[m.group(1).lower()], l)           # the eighteenth drawing
        m = re.search(r"\bthe (%s) and the (%s) drawings" % (OW, OW), l, re.I)                           # the tenth and the eleventh drawings
        if m: add(ORD[m.group(1).lower()], l); add(ORD[m.group(2).lower()], l)
        m = re.search(r"\bthe (%s) to the (\d{1,2})(?:st|nd|rd|th) drawings" % OW, l, re.I)              # the fourth to the 24th drawings
        if m:
            for k in range(ORD[m.group(1).lower()], int(m.group(2)) + 1): add(k, l)
        for m in re.finditer(r"\bDrafts? (\d{1,2})(?: (to|and) (\d{1,2}))?", l):                         # Draft 20
            a = int(m.group(1)); add(a, l)
            if m.group(3):
                for k in (range(a, int(m.group(3)) + 1) if m.group(2) == "to" else [int(m.group(3))]): add(k, l)
        for m in re.finditer(r"\b(?:its prior|beside it now)[, ·]+((?:\d{1,2}(?:, | and )?)+)", l):       # a head line: its prior, 55
            for k in re.findall(r"\d+", m.group(1)): add(int(k), l)
    return out
def parts_of(links):
    adj = {n: set() for n in range(1, 57)}
    for n, ks in links.items():
        for k in ks: adj[n].add(k); adj[k].add(n)
    seen, parts = set(), []
    for n in range(1, 57):
        if n in seen: continue
        part, stack = [], [n]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x); part.append(x); stack.extend(adj[x] - seen)
        parts.append(sorted(part))
    return parts

# ---- the words
WORD = re.compile(r"[A-Za-z][A-Za-z'’\-]*[A-Za-z]|[A-Za-z]")
def words(t): return [w.lower().replace("’", "'") for w in WORD.findall(t)]
def bare(w): return re.sub(r"'s$", "", w)
def words_of_files(files):
    c = Counter()
    for f in files: c.update(words(f.read_text(encoding="utf-8")))
    return c
# v408illustrating's eight, by its own lines
EIGHT = [("twin", r"\btwins?\b"), ("loop", r"\bloops?\b"), ("room", r"\brooms?\b"), ("vault", r"\bvaults?\b"), ("rule", r"\brules?\b"),
         ("distance", r"\bdistances?\b"), ("apart", r"\bapart\b"), ("direction", r"\bdirections?\b")]
# a partner's askings of 25 and 26 November: a number's place, what is a turn, what is a self
THREE = [("turn", r"(?<![\w])turn(?:s|ed|ing|ings)?(?![\w])"), ("place", r"(?<![\w-])places?(?![\w-])"), ("self", r"(?<![\w-])sel(?:f|ves)(?![\w-])")]
# judged: the kind of a word that is in no living file, said for the words in three drawings or more, and for a session's names
KIND = {}
for w in "accent coloured dashed tinted dotted ink shaded ringed".split(): KIND[w] = "a word of a drawing's own marks"
for w in ("nand nands nanding nand-nanding nandnanding me-now me-nows me-now's other-thans next-universing universal-me-now my-prior my-next "
          "my-now-universe my-universe me-universe me-next me-prior all-parities all-parity-ing other-than-other-than other-than-other-thans "
          "all-other-than all-other-than-all other-than-all-other-than other-than-all-other-than-all next-prior-now prior-sequence same-named "
          "co-observing co-observing's bi-neutralling bi-planar bi-inversionings agains").split():
    KIND[w] = "a name or a name's form newer than the living files"
for w in ("nanding's reiman's reiman rigorized transcripts canvas's card's leanest").split(): KIND[w] = "a word of the sessions' work"
for w in ("brun brun's euclid's germain hardy landau's littlewood littlewood's polignac schinzel sophie ulam's artin bertrand carmichael "
          "chebyshev's cram dirichlet's erd kac lya's mersenne mertens montgomery pseudoprimes wieferich xi cicadas").split():
    KIND[w] = "a field's name"

def nth(n): return f"{n}{'th' if 10 < n % 100 < 14 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"
def primes_to(n):
    s = [True] * (n + 1); s[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = [False] * len(s[i * i::i])
    return [i for i, b in enumerate(s) if b]
def least_part(n): return next(p for p in range(2, n + 1) if n % p == 0)
def crossed_in(t, pat):
    """A number's line, and the line after it saying by what it is crossed."""
    ls, out = t.splitlines(), {}
    for a, b in zip(ls, ls[1:]):
        m = re.fullmatch(pat, b)
        if a.isdigit() and m: out[int(a)] = tuple(int(x) for x in m.groups())
    return out

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--lay"]; LAY = "--lay" in sys.argv
    ROOT = Path(args[0]); V408 = Path(args[1]) if len(args) > 1 else ROOT; NEXT = Path(args[2]) if len(args) > 2 else None
    if not (V408 / G3).is_dir():
        sys.exit("v408illustrating's folder is not at " + str(V408) + ": give the root with it as the second path, by this instrument's own usage")
    T = {n: text_of(n) for n in range(1, 57)}; low = {n: t.lower() for n, t in T.items()}
    said = Counter()
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")

    print("1 · All 56, and a drawing's figure")
    line("is", len(T) == 56 and all(T.values()), f"a text of its own is found at all 56 drawings: {sum(len(t.split()) for t in T.values())} words")
    ns = sorted(n for _, group in FIGURES for n in group)
    line("is", ns == list(range(1, 57)), f"a drawing is in one figure, and no drawing in two: 56 drawings in {len(FIGURES)} figures")
    for name, group in FIGURES: line("judged", True, f"{len(group)} · {name}: {', '.join(map(str, group))}")
    pairs = [(7, 41), (8, 50), (9, 43), (46, 49), (47, 51)]          # v408illustrating's five pairs, two drawings of one figure
    one = [pr for pr in pairs if FIGURE_OF[pr[0]] == FIGURE_OF[pr[1]]]; two = [pr for pr in pairs if pr not in one]
    line("judged", True, f"of v408illustrating's five pairs of one figure, {len(one)} are in one figure here, and {len(two)} are in two by the thing drawn: "
         + " and ".join(f"the {nth(x)} with the {nth(y)}" for x, y in two))

    print("\n2 · A drawing's own text naming an other drawing")
    links = {n: named_in(n, T[n]) for n in range(1, 57)}
    naming_none = [n for n in links if not links[n]]; named = {k for n in links for k in links[n]}
    named_by_none = [n for n in range(1, 57) if n not in named]; neither = [n for n in naming_none if n not in named]
    head = [n for n in range(1, 57) if re.search(r"\bits prior[, ·]+\d", T[n])]
    line("is", head == list(range(44, 57)), f"a head line says a drawing's prior at {len(head)} drawings, the {nth(head[0])} to the {nth(head[-1])}, and at no drawing ahead of them")
    early = [n for n in naming_none if n <= 24]
    line("found", True, f"of the 1st to the 24th, {len(early)} name no other drawing; of the 25th to the 56th, {len(naming_none) - len(early)}")
    line("found", True, f"{len(naming_none)} drawings name no other drawing: {', '.join(map(str, naming_none))}")
    line("found", True, f"{len(named_by_none)} drawings are named by no other: {', '.join(map(str, named_by_none))}")
    line("found", True, f"{len(neither)} drawings neither name nor are named: {', '.join(map(str, neither))}")
    parts = parts_of(links)
    line("found", True, f"by all namings the set is {len(parts)} parts: one of {max(map(len, parts))}, and {', '.join(str(p[0]) for p in parts if len(p) == 1)} a part apiece")
    span = [k for k in links[25] if 4 <= k <= 24]
    less = {n: {k: v for k, v in ks.items() if not (n == 25 and k in span)} for n, ks in links.items()}
    parts_less = parts_of(less)
    line("is", len(span) == 21, "one line of the 25th names the 4th to the 24th together, 21 drawings in one saying")
    line("found", True, f"with that one line set by, the set is {len(parts_less)} parts, {sum(len(p) == 1 for p in parts_less)} of them a drawing apiece; "
         f"the parts of more than one: " + "; ".join(", ".join(map(str, p)) for p in parts_less if len(p) > 1))

    print("\n3 · Numbers said by more than one drawing, executed apart")
    P = primes_to(400)
    by_rounds = [sum(a < p <= b for p in P) for a, b in ((0, 24), (24, 60), (60, 96), (96, 120))]
    by_cones = [sum(a < p <= b for p in P) for a, b in ((0, 30), (30, 60), (60, 90), (90, 120))]
    line("is", by_rounds == [9, 8, 7, 6] and "nine, eight, seven and six" in low[8], "the 8th: the primes of 0 to 120 by its four rounds are nine, eight, seven and six")
    line("is", by_cones == [10, 7, 7, 6] and "10, 7, 7 and 6" in low[9], "the 9th: the primes of 0 to 120 by its four cones are 10, 7, 7 and 6")
    line("is", sum(by_rounds) == sum(by_cones) == 30, "the 8th and the 9th part 0 to 120 two ways, and both are with all 30 primes")
    carried = {"23": 60 - 37, "83": 120 - 37, "97": 37 + 60, "143": 180 - 37, "157": 37 + 120}
    line("is", all(int(k) == v for k, v in carried.items()), "37 is podal about 30 with 23, about 60 with 83 and about 90 with 143; 60 on it is 97 and 120 on it is 157")
    for n in (10, 11, 12, 13, 15, 17):
        got = [k for k in carried if re.search(r"(?<!\d)%s(?!\d)" % k, T[n])]
        line("is", re.search(r"(?<!\d)37(?!\d)", T[n]) is not None and len(got) >= 3, f"the {nth(n)} is with 37 and {', '.join(got)}")
    shells = [n ** 3 - (n - 1) ** 3 for n in range(1, 6)]
    line("is", shells == [1, 7, 19, 37, 61], "a cube less the cube one smaller is 1, 7, 19, 37 and 61, at the cubes of 1 to 5")
    for n in (7, 8, 40, 41):
        got = [s for s in shells[1:] if re.search(r"(?<![\d,])%d(?![\d,]\d)" % s, T[n])]
        line("is", len(got) >= 3, f"the {nth(n)} is with the shells {', '.join(map(str, got))}")
    free = [n for n in range(1, 120) if n % 2 and n % 3 and n % 5]; pairs = [(k, 120 - k) for k in free if k < 60]
    both_prime = [pr for pr in pairs if pr[0] in P and pr[1] in P]; crossed = sorted(x for pr in pairs for x in pr if x > 1 and x not in P)
    line("is", (len(free), len(pairs), len(both_prime), crossed) == (32, 16, 12, [49, 77, 91, 119])
         and "of sixteen stations no spiral of 2, 3 or 5 crosses, twelve are a prime with a prime" in low[7]
         and "the 32 places of 0 to 120 no spiral of 2, 3 or 5 crosses" in low[11] and "91 and 77 crossed by the spiral of 7" in low[8],
         "the 7th, the 8th and the 11th: of 0 to 120, 32 numbers are crossed by none of 2, 3 and 5, sixteen podal pairs, twelve a prime with a prime, and four with 49, 77, 91 or 119")
    c38 = crossed_in(T[38], r"by (\d+)"); c56 = crossed_in(T[56], r"(\d+) by (\d+)")
    both = sorted(set(c38) & set(c56))
    line("is", all(least_part(n) == c38[n][0] for n in c38), f"the 38th: all {len(c38)} crossed numbers of its rows of 30 are crossed by their least part, as it says")
    line("is", all(a * b == n and a == least_part(n) for n, (a, b) in c56.items()), f"the 56th: all {len(c56)} crossed numbers of its rows of 30 are their two parts multiplied, the least ahead")
    line("is", len(both) == len(c56) and all(c38[n][0] == c56[n][0] for n in both), f"the 38th and the 56th say the same least part at all {len(both)} crossed numbers they are both with, to 299")
    eight = [1, 7, 11, 13, 17, 19, 23, 29]; in210 = [n for n in range(1, 211) if n % 30 in eight]
    by7 = [n for n in in210 if n % 7 == 0]
    line("is", (len(in210), len(by7), len(in210) - len(by7)) == (56, 8, 48) and "56 numbers of 210, 8 crossed by 7 and 48 places" in low[38]
         and "56 numbers: eight crossed by 7, one a column, and 48" in low[46], "the 38th and the 46th: the eight of 30 to 210 are 56 numbers, 8 crossed by 7 and 48 not")

    print("\n4 · One thing said by more than one name")
    def has(n, phrase): return phrase in low[n]
    line("found", has(8, "five selves on its line") and has(50, "five cells are still on one line"),
         "the five on the line of the cube of 5 are selves at the 8th and cells at the 50th")
    line("found", has(13, "a me at 37: 37, 97 and 157") and has(15, "its selves 97 and 157") and has(17, "a self, 60 on"),
         "37 carried 60 on and 120 on, 97 and 157, is a me at the 13th, its selves at the 15th and a self at the 17th")
    line("found", has(9, "a cone's turn of 30 is eight places") and has(38, "a turn of 30, its eight places") and has(46, "the turn of 30's eight places")
         and has(56, "a path of 30 mes: eight living"),
         "the eight of 30 are a turn's places at the 9th, the 38th and the 46th, and a path's living mes at the 56th")

    print("\n5 · The words a partner asked of, numbered in a drawing's own text")
    eight_in = {n: {w: len(re.findall(p, low[n])) for w, p in EIGHT if re.search(p, low[n])} for n in T}
    three_in = {n: {w: len(re.findall(p, low[n])) for w, p in THREE if re.search(p, low[n])} for n in T}
    with_eight = [n for n in T if eight_in[n]]
    line("is", len(with_eight) == 22, f"v408illustrating's eight words are in {len(with_eight)} drawings, as its page says")
    for w, _ in THREE:
        ds = [n for n in T if w in three_in[n]]
        line("found", True, f"{w}: {sum(three_in[n][w] for n in ds)} places in {len(ds)} drawings")
    standing = {}
    table = V408 / (G3 + "The_set_of_all_56_drawings_a_drawing_a_row.csv")
    for r in csv.DictReader(open(table, encoding="utf-8")): standing[int(r["Drawing"])] = r["Its standing"]
    fourteen = sorted(n for n, s in standing.items() if s.startswith("ready") or s.startswith("clean"))
    line("is", len(fourteen) == 14, f"v408illustrating's table is with 1 ready and 13 clean: {', '.join(map(str, fourteen))}")
    none_of_three = [n for n in fourteen if not three_in[n]]
    line("found", True, f"of the 14, {len(fourteen) - len(none_of_three)} are with turn, place or self, and {len(none_of_three)} with none: {', '.join(map(str, none_of_three)) or 'none'}")
    with_none = [n for n in T if not three_in[n] and not eight_in[n]]
    line("found", True, f"of all 56, {len(with_none)} are with none of the eleven words: {', '.join(map(str, with_none)) or 'none'}")

    print("\n6 · A drawing's words that are in no living file")
    living = words_of_files(f for f in sorted(ROOT.glob("*.md")) if f.name != "README.md")
    n_living = sum(1 for f in ROOT.glob("*.md") if f.name != "README.md")
    in_drawing = {}
    for n in T:
        for w in words(T[n]): in_drawing.setdefault(w, Counter())[n] += 1
    new = {w: c for w, c in in_drawing.items() if not living[w] and not living[bare(w)]}
    line("is", n_living == 33, f"the living files at the root are {n_living}, with {len(living)} words of their own")
    line("found", True, f"of the drawings' {len(in_drawing)} words, {len(new)} are in no living file, at {sum(sum(c.values()) for c in new.values())} places")
    nxt = {}
    if NEXT is not None:
        nl = words_of_files(f for f in sorted(NEXT.glob("*.md")) if f.name != "README.md"); ng = words_of_files(sorted((NEXT / "gathering-value").glob("*.md")))
        nxt = {w: (nl[w] + (nl[bare(w)] if bare(w) != w else 0), ng[w] + (ng[bare(w)] if bare(w) != w else 0)) for w in new}
        line("found", True, f"of the {len(new)}, {sum(1 for a, b in nxt.values() if a)} are in a living file of the next version, {sum(1 for a, b in nxt.values() if b and not a)} in its gathering files alone, and {sum(1 for a, b in nxt.values() if not a and not b)} in neither")
    for kind in sorted(set(KIND.values())):
        ws = sorted((w for w in new if KIND.get(w) == kind), key=lambda w: (-len(new[w]), w))
        line("judged", True, f"{kind}: {len(ws)} words, the most drawn {', '.join(ws[:6])}")
    rest = sorted((w for w in new if w not in KIND), key=lambda w: (-len(new[w]), w))
    line("judged", True, f"not yet judged: {len(rest)} words, the most drawn {', '.join(rest[:8])}")
    for w in ("nand", "me-now"):
        line("found", True, f"{w} is in {len(new[w])} drawings and in no living file" + (f"; in the next version it is at {nxt[w][0]} places of its living files and {nxt[w][1]} of its gathering files" if nxt else ""))

    if LAY:
        out = ROOT / MINE
        named_by = {n: sorted(k for k in links if n in links[k]) for n in T}
        with open(out / "All_56_drawings_a_drawing_a_row_its_figure_its_namings_and_its_words.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Drawing", "Its session", "Its name", "Its figure, judged on 27 November", "The drawings its own text names", "The drawings whose text names it",
                        "turn, place and self in its text, places", "v408illustrating's eight words in its text, places", "Its words in no living file",
                        "Its standing in v408illustrating's table"])
            for n in range(1, 57):
                w.writerow([n, session(n), name_of(n), FIGURE_OF[n], "; ".join(map(str, sorted(links[n]))), "; ".join(map(str, named_by[n])),
                            "; ".join(f"{k} {v}" for k, v in three_in[n].items()), "; ".join(f"{k} {v}" for k, v in eight_in[n].items()),
                            "; ".join(sorted(x for x in new if n in new[x])), standing[n]])
        with open(out / "The_words_of_all_56_drawings_that_are_in_no_living_file_a_word_a_row.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["A word", "Its drawings", "Its places", "The drawings", "In the next version's living files, places", "In the next version's gathering files, places",
                        "Its kind, judged on 27 November"])
            for x in sorted(new, key=lambda x: (-len(new[x]), -sum(new[x].values()), x)):
                w.writerow([x, len(new[x]), sum(new[x].values()), "; ".join(map(str, sorted(new[x]))), nxt.get(x, ("", ""))[0], nxt.get(x, ("", ""))[1], KIND.get(x, "not yet judged")])
        print("\nlaid: two tables in " + MINE)

    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['judged']} are judged, and said as judged" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
