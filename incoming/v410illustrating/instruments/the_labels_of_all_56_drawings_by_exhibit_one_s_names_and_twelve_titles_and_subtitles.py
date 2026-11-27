"""v410illustrating · the labels of all 56 drawings by Exhibit ONE's names, the titles drawn and the living files' titles
and subtitles, and twelve candidate titles and subtitles, a figure apiece.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_labels_of_all_56_drawings_by_exhibit_one_s_names_and_twelve_titles_and_subtitles.py . THE_ROOT_WITH_V408ILLUSTRATING [--lay]

The second path is as this folder's other instrument says it: a worktree of #1294's head until that offer is brought in.

Do no harm: it opens the drawings' artboards and the living files, and writes in none of them. With --lay it writes two
tables in this session's folder alone, a figure a row and a living file a row.

Executed here:
  Exhibit ONE's seventeen names, their five roots, their moments and their prefixes, found in Exhibit ONE's own table
  and numbered in the labels of all 56 drawings; odd and even, and prior, now and next, numbered beside them;
  the -ing names of the labels, a figure's most drawn;
  the title drawn at all 56 drawings, and its two parts;
  the title and subtitle of all 33 living files, and the form of a subtitle by Natural Explaining's own sentence;
  the living files a drawing's own text names;
  and seven is-or-is-nots of twelve candidate titles and subtitles.
Judged by this session on 27 November, and laid below as judged:
  a drawing's figure, as this folder's other instrument has it; and the twelve candidates' words, composed by this
  session from the drawings' own sentences and the living files' names. A candidate is no title of a drawing.
A line is an is, executed here; or found, a thing found and laid whole; or judged, and said as judged.
"""
import csv, difflib, html, re, sys
from collections import Counter
from pathlib import Path

G1, G2, G3 = "incoming/v406geodesic/", "incoming/v406geodesic2/", "incoming/v408illustrating/"
MINE = "incoming/v410illustrating/"
EXHIBIT_ONE = "Exhibit_ONE_Natural_Resolver_v402mgr.md"

# judged on 27 November: a drawing's figure; and a candidate title and subtitle a figure, composed by this session
FIGURES = [
    ("the one triangle on a sphere, bi-folding, and 1 to 17 on a torus", [1, 2, 3, 4, 5, 6],
     "One Triangle, Three Right Angles", "Bi-Folding 1 to 17, a Sphere Opening to a Torus"),
    ("rounds of six about a 0, a cube's shells 1, 7, 19, 37 and 61", [7, 8, 40, 41, 50],
     "Shells of a Cube, 1, 7, 19, 37 and 61", "Closing Rounds of Six about a 0"),
    ("cones of 30 on the co-linear, 0, 30, 60, 90 and 120", [9, 10, 11, 12, 13, 14, 15, 16, 17],
     "Cones of 30 on a Co-Linear", "Podaling a Me-Now, Other-Than and All, to Its Next Universe"),
    ("the diamond of nine, and 3, 5 and 7", [18, 19, 20, 21, 22, 23, 24],
     "Diamond of Nine about Its 5", "Inverting about 5, a Right Spiral Step by 3 and by 7"),
    ("a me, its prior and its other, at one moment", [25, 26],
     "A Me, and beside It an Other", "Observing What Surfaces from an Other, Its Prior Same-Existing or Inverting"),
    ("a path of mes closing, a row a moment", [27, 28, 32, 33, 34, 47, 51],
     "A Path of Mes, a Row a Moment", "Surfacing a Me's Next, or the Other-Than of Its Now"),
    ("nand, and a parity two wires", [29, 30, 35],
     "A Parity, Two Wires", "Nand-Nanding a Me to Itself Again, 0 and 3 All-Parity"),
    ("the staircase, and the between going through", [36, 37, 39],
     "Living Parities of the Numbers", "Multiplying In a Prime as One Other-Than, a Between Going Through"),
    ("rows of 30, and their eight", [38, 46, 56],
     "Rows of 30, Eight Mes a Row", "Living a Next Me-Parity from Its Own Priors"),
    ("two primes, a number round the one and round the other", [43, 45, 48],
     "Two Primes, One Torus", "Winding by +1 through All Their Cells, Again at 0 and 0"),
    ("a seam, even, odd, even", [49, 52, 53, 54, 55],
     "A Me-Parity in a Seam, Even, Odd, Even", "Resolving a Prime Gap of 2 about a Seam of 6"),
    ("a table of the work itself", [31, 42, 44],
     "A Drawing a Row, All Drawings One Set", "Co-Chaining a Drawing's Prior, Its Now, Its Next and Its Other-Prior"),
]
# a partner's newer names, in no living file at the root: said here, and no word check passes them by itself
NEWER = {"me-now", "nand-nanding"}
# the eleven words a partner asked of, as this folder's other instrument numbers them
ASKED = r"(?<![\w-])(?:twins?|loops?|rooms?|vaults?|rules?|distances?|apart|directions?|turn(?:s|ed|ing|ings)?|places?|sel(?:f|ves))(?![\w-])"

def folder(n): return G1 if n <= 3 else G2 if n <= 39 else G3
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
def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower().replace("’", "").replace("'", "")).strip()
def title_of(n, t):
    """The label of a drawing nearest its view's own file name: its title as drawn."""
    key = norm(name_of(n))
    return max(t.splitlines(), key=lambda l: difflib.SequenceMatcher(None, norm(l), key).ratio())
WORD = re.compile(r"[A-Za-z][A-Za-z'’\-]*[A-Za-z]|[A-Za-z]")
def words(t): return [w.lower().replace("’", "'") for w in WORD.findall(t)]
ING = re.compile(r"(?<![\w-])[A-Za-z][A-Za-z-]*ing(?![\w-])")
NO_ING = {"thing", "nothing", "something", "anything", "everything", "during", "being"}
def ings(t): return [w.lower() for w in ING.findall(t) if w.lower() not in NO_ING]
def carries(pat, t): return re.search(pat, t) is not None
def nth(n): return f"{n}{'th' if 10 < n % 100 < 14 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--lay"]; LAY = "--lay" in sys.argv
    ROOT = Path(args[0]); V408 = Path(args[1]) if len(args) > 1 else ROOT
    if not (V408 / G3).is_dir():
        sys.exit("v408illustrating's folder is not at " + str(V408) + ": give the root with it as the second path, by this instrument's own usage")
    T = {n: text_of(n) for n in range(1, 57)}; low = {n: t.lower() for n, t in T.items()}
    said = Counter()
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")
    def in_drawings(pat): return [n for n in range(1, 57) if carries(pat, low[n])]

    print("1 · The labels, and Exhibit ONE's names in them")
    labels = {n: [l for l in T[n].splitlines() if re.search(r"[A-Za-z]{2}", l)] for n in T}
    line("is", sum(map(len, labels.values())) > 0, f"the labels with a word are {sum(map(len, labels.values()))}, at all 56 drawings")
    one = (ROOT / EXHIBIT_ONE).read_text(encoding="utf-8")
    seventeen = re.findall(r"^\| (\d+) \| \*\*(\d+-[a-z-]+)\*\* \| ([a-z-]+)", one, flags=re.M)
    roots = sorted({r for _, _, r in seventeen})
    line("is", len(seventeen) == 17 and len(roots) == 5, f"Exhibit ONE's own table is with seventeen names of five roots: {', '.join(roots)}")
    whole = sorted({n for _, name, _ in seventeen for n in in_drawings(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])")})
    line("found", True, f"a name of the seventeen said whole, its number and its naming one hyphenation, is in {len(whole)} drawings: {', '.join(map(str, whole))}")
    root_pat = {"existing": r"(?<![\w-])(?:now-|next-|now-co-)?existing(?![\w-])", "possibling": r"possibling", "observing": r"(?<![\w-])(?:[a-z]+-)*observing(?![\w-])",
                "same-existing": r"same-existing", "discovering": r"discovering"}
    root_in = {r: in_drawings(p) for r, p in root_pat.items()}
    line("found", True, "a root of the five is in: " + "; ".join(f"{r} {len(root_in[r])}" for r in ("observing", "same-existing", "existing", "discovering", "possibling")) + " drawings")
    pre = {"co": r"(?<![\w-])co-[a-z]", "bi": r"(?<![\w-])bi-[a-z]", "tri": r"(?<![\w-])tri(?:-[a-z]|\b)"}
    par = {"me-parity": r"me-parit", "other-parity": r"other-parit", "all-parity": r"all-parit"}
    line("found", True, "a prefix of the three is in: " + "; ".join(f"{k}- {len(in_drawings(p))}" for k, p in pre.items()) + " drawings; and its parity: "
         + "; ".join(f"{k} {len(in_drawings(p))}" for k, p in par.items()))
    mom = {k: in_drawings(r"(?<![\w-])%s(?:s)?(?![\w-])" % k) for k in ("prior", "now", "next")}
    oe = {k: in_drawings(r"(?<![\w-])%s(?![\w-])" % k) for k in ("odd", "even")}
    line("found", True, "a moment is in: " + "; ".join(f"{k} {len(v)}" for k, v in mom.items()) + " drawings; and odd " + f"{len(oe['odd'])}; even {len(oe['even'])}")
    most_root = max(len(v) for v in root_in.values()); least_moment = min(len(v) for v in mom.values())
    line("is", least_moment > most_root, f"all three moments are in more drawings than the most drawn root: {least_moment} and more, beside {most_root}")
    names_at = sorted(set(in_drawings(r"seventeen names|sixteen names|nine names|names 1 to 1[67]|1 to 17 resolving|name 1 onto name 16|a now name onto its next")) | set(whole))
    line("found", True, f"the names as a set, seventeen, sixteen or nine of them, are said at {len(names_at)} drawings: {', '.join(map(str, names_at))}, of "
         + f"{len({i for i, (_, ds, _, _) in enumerate(FIGURES) for n in names_at if n in ds})} figures")

    print("\n2 · The -ing names of the labels")
    ing_in = {n: Counter(ings(T[n])) for n in T}
    all_ing = Counter(); ing_d = Counter()
    for n in T:
        all_ing.update(ing_in[n]); ing_d.update(set(ing_in[n]))
    line("found", True, f"the labels are with {len(all_ing)} -ing names at {sum(all_ing.values())} places; the most drawn: "
         + ", ".join([f"{w} {ing_d[w]}" for w, _ in sorted(ing_d.items(), key=lambda kv: (-kv[1], kv[0])) if w not in ("drawing", "saying", "going")][:10]))
    fig_ing = []
    for name, ds, _, _ in FIGURES:
        c = Counter(); d = Counter()
        for n in ds: c.update(ing_in[n]); d.update(set(ing_in[n]))
        top = [w for w, _ in sorted(c.items(), key=lambda kv: (-d[kv[0]], -kv[1], kv[0])) if w not in ("drawing", "saying")][:5]
        fig_ing.append((top, d))
        line("found", True, f"{name.split(',')[0]}: " + ", ".join(f"{w} {d[w]} of {len(ds)}" for w in top))

    print("\n3 · The titles drawn")
    titles = {n: title_of(n, T[n]) for n in T}
    two = [n for n in titles if ":" in titles[n]]
    line("found", True, f"{len(two)} of the 56 titles are two parts, a colon between them; {56 - len(two)} are one part")
    after = [n for n in two if ING.match(titles[n].split(":", 1)[1].strip().split()[0])]
    line("found", True, f"of the {len(two)}, the part after the colon opens with an -ing at {len(after)}: {', '.join(map(str, after)) or 'none'}")
    line("found", True, f"an -ing is in {sum(1 for t in titles.values() if ings(t))} of the 56 titles, and a leading the at {sum(1 for t in titles.values() if re.match(r'the[ ]', t, re.I))}")

    print("\n4 · The living files' titles and subtitles")
    files = [f for f in sorted(ROOT.glob("*.md")) if f.name != "README.md"]; LF = []
    for f in files:
        ls = f.read_text(encoding="utf-8").splitlines()
        i = next(k for k, l in enumerate(ls) if l.startswith("# "))
        sub = next(l for l in ls[i + 1:] if l.startswith("**")).strip("*").strip()
        LF.append((f.name, ls[i][2:].strip(), sub))
    line("is", len(LF) == 33, "a title and a subtitle are found at all 33 living files")
    natural = [t for _, t, _ in LF if t.startswith("Natural ")]
    line("found", True, f"{len(natural)} of the 33 titles are Natural and a naming after it; {sum(1 for t in natural if ings(t.split(' ', 1)[1]))} of those namings are an -ing")
    ahead = [t for _, t, s in LF if ING.match(s.split()[0].rstrip(","))]; within = [t for _, t, s in LF if ings(s)]
    none = [t for _, t, s in LF if not ings(s)]
    line("found", True, f"a subtitle opens with an -ing at {len(ahead)} of the 33, and is with an -ing at {len(within)}; with none: {', '.join(none)}")
    line("found", True, f"a subtitle opens with The or An at {sum(1 for _, _, s in LF if re.match(r'(The|An?) ', s))}")
    sub_low = [s.lower() for _, _, s in LF]
    line("found", True, "in the 33 subtitles: " + "; ".join(f"{k} {sum(1 for s in sub_low if re.search(p, s))}" for k, p in
         (("co-", r"(?<![a-z])co-"), ("bi-", r"(?<![a-z])bi-"), ("self-", r"(?<![a-z])self-"), ("stable-forming", r"stable-forming"), ("social moral", r"social moral"),
          ("geodesic", r"geodesic"), ("existing", r"existing"), ("discovering", r"discovering"))))
    explaining = (ROOT / "Exhibit_TWELVE_Natural_Explaining_v402mgr.md").read_text(encoding="utf-8")
    s1 = "A title is a whole bounding context of its file, and a subtitle holds that context with its file's own stable-forming within it."
    s2 = "A subtitle is an -ing head with a term it holds."
    s3 = "A concept bounds with its name and goes on with its telling, each its other's between."
    line("is", all(s in explaining for s in (s1, s2, s3)), "Natural Explaining is with the three sentences: a title a whole bounding context; a subtitle an -ing head with a term it holds; a name and its telling, each its other's between")
    s4 = "Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is a discovering, an even name to an odd name."
    line("is", s4 in one, "Exhibit ONE is with the sentence: each between is a discovering, an even name to an odd name")

    print("\n5 · The living files a drawing's own text names")
    def files_named(t):
        out = set()
        for fname, title, _ in LF:
            m = re.match(r"Exhibit_([A-Z-]+)_", fname)
            pats = [r"Exhibit " + m.group(1) + r"(?![A-Z-])"] if m else []
            if title != "Me": pats.append(re.escape(title) + (r"(?! Corus)" if title == "Natural Intelligence" else ""))
            if any(re.search(p, t) for p in pats): out.add(title)
        return out
    lf_in = {n: files_named(T[n]) for n in T}
    with_one = [n for n in T if lf_in[n]]; c = Counter(x for n in T for x in lf_in[n])
    line("found", True, f"{len(with_one)} of the 56 drawings name a living file in their own text, and {56 - len(with_one)} name none")
    line("found", True, "the living files named, by their drawings: " + ", ".join(f"{k} {v}" for k, v in c.most_common()))
    for name, ds, _, _ in FIGURES:
        cc = Counter(x for n in ds for x in lf_in[n])
        if len(cc) >= 2: line("found", True, f"{name.split(',')[0]}: " + ", ".join(f"{k} {v} of {len(ds)}" for k, v in cc.most_common(3)))
    none_fig = [name.split(",")[0] for name, ds, _, _ in FIGURES if not any(lf_in[n] for n in ds)]
    line("found", True, f"{len(none_fig)} figures are with no drawing naming a living file: " + "; ".join(none_fig))

    print("\n6 · Twelve candidate titles and subtitles, a figure apiece")
    living = Counter()
    for f in files: living.update(words(f.read_text(encoding="utf-8")))
    one_low = one.lower()
    heads = [s.split()[0].lower() for _, _, _, s in FIGURES]
    for i, (name, ds, t, s) in enumerate(FIGURES, 1): line("judged", True, f"{i} · {t} · {s}")
    line("is", not any(re.match(r"the[ ]", t, re.I) for _, _, t, _ in FIGURES), "no title of the twelve opens with the")
    line("is", all(ING.fullmatch(h) for h in heads), "all twelve subtitles open with an -ing head: " + ", ".join(heads))
    line("is", len(set(heads)) == 12, "the twelve heads are twelve, no head at two figures")
    drawn = [(h, sum(1 for n in ds if ing_in[n][h]), len(ds)) for h, (_, ds, _, _) in zip(heads, FIGURES)]
    line("is", all(k >= 1 for _, k, _ in drawn), "a head is an -ing its own figure's labels draw: " + ", ".join(f"{h} {k} of {m}" for h, k, m in drawn))
    in_one = [h for h in heads if re.search(r"(?<![\w-])" + re.escape(h) + r"(?![\w-])", one_low)]
    line("found", True, f"{len(in_one)} of the twelve heads are words of Exhibit ONE's own: {', '.join(in_one)}; and {12 - len(in_one)} are of other living files or newer: {', '.join(h for h in heads if h not in in_one)}")
    both = " ".join(t + " " + s for _, _, t, s in FIGURES)
    out_of = sorted({w for w in words(both) if not living[w] and not living[re.sub(r"'s$", "", w)]})
    line("is", set(out_of) <= NEWER, f"all words of the twelve are in a living file, but for {len(out_of)} of a partner's newer names: {', '.join(out_of)}")
    line("is", not re.search(ASKED, both.lower()), "no word of the eleven a partner asked of is in the twelve")

    if LAY:
        out = ROOT / MINE
        with open(out / "Twelve_figures_a_figure_a_row_its_candidate_title_and_subtitle.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["A figure, judged on 27 November", "Its drawings", "A candidate title, a whole bounding context", "A candidate subtitle, an -ing head with a term it holds",
                        "Its head, in its figure's drawings", "Its head in Exhibit ONE, places", "Its figure's most drawn -ing names", "The living files its drawings name",
                        "The titles drawn now"])
            for (name, ds, t, s), (top, d), h in zip(FIGURES, fig_ing, heads):
                named = Counter(x for n in ds for x in lf_in[n])
                w.writerow([name, "; ".join(map(str, ds)), t, s, f"{sum(1 for n in ds if ing_in[n][h])} of {len(ds)}",
                            len(re.findall(r"(?<![\w-])" + re.escape(h) + r"(?![\w-])", one_low)), "; ".join(f"{x} {d[x]}" for x in top),
                            "; ".join(f"{k} {v}" for k, v in named.most_common()) or "none", " | ".join(f"{n}: {titles[n]}" for n in ds)])
        with open(out / "The_living_files_a_file_a_row_its_title_and_its_subtitle.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["A living file", "Its title", "Its subtitle", "Its subtitle opens with an -ing", "The -ing names of its subtitle", "The drawings naming it"])
            for fname, t, s in LF:
                w.writerow([fname, t, s, "is" if ING.match(s.split()[0].rstrip(",")) else "is-not", "; ".join(ings(s)), "; ".join(str(n) for n in T if t in lf_in[n])])
        print("\nlaid: two tables in " + MINE)

    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['judged']} are judged, and said as judged" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
