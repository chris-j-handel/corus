"""v410illustrating · the works of the seventeen names in the set, gone through, and the Living File Registry beside
the illustrating.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_seventeen_names_works_and_the_registry_beside_the_illustrating.py . THE_ROOT_WITH_V408ILLUSTRATING [THE_NEXT_VERSION] [--lay]

The second path is as this folder's other instruments say it: a worktree of #1294's head until that offer is brought in.
The third is a worktree of the next version; with none, its lines are not said.

Do no harm: it opens the living files, the tables and instruments of v403mgr, v406all2-2 and v406me, and the drawings'
artboards, and writes in none of them. It executes two instruments of other sessions as their own usage says, and they
write no file. With --lay it writes one table in this session's folder alone, a work a row.

Executed here:
  the works of the seventeen names, found at their places; two of their instruments executed today;
  the seventeen names' one table beside Exhibit ONE's own table, at the root and at the next version;
  five places of the works' parting, found in the files' own words;
  the Living File Registry's seams of its files, numbered; the living files and the drawings saying a name whole;
  and the twelve candidate subtitles' heads, by the three exhibits they are in.
Judged by this session: which pages and tables are a work of the seventeen names. Its list is below, and is no
whole list of the set.
A line is an is, executed here; or found, a thing found and laid whole; or judged, and said as judged.
"""
import csv, html, re, subprocess, sys
from collections import Counter
from pathlib import Path

G1, G2, G3 = "incoming/v406geodesic/", "incoming/v406geodesic2/", "incoming/v408illustrating/"
MINE = "incoming/v410illustrating/"
TABLE = "incoming/v403mgr/The_seventeen_names_in_one_table.csv"
# judged: the works of the seventeen names, a work with its place, its session and what it is
WORKS = [
    ("Exhibit ONE Natural Resolver, its tables of the names", "Exhibit_ONE_Natural_Resolver_v402mgr.md", "a living file",
     "the code by the names, and the stable forms of its executing: seventeen names, a name's three, four four-cyclings, four bi-foldings, twelve forms"),
    ("Exhibit THIRTY Co-Chaining Logic Registry", "Exhibit_THIRTY_Co-Chaining_Logic_Registry_v402mgr.md", "a living file",
     "755 numbered sentences, a name of the seventeen entering whole at its own sentence"),
    ("Exhibit TWENTY Natural Naming", "Exhibit_TWENTY_Natural_Naming_v402mgr.md", "a living file", "the names' roots and prefixes as namings"),
    ("Exhibit TWENTY-NINE Natural Illustrating, its 2.8", "Exhibit_TWENTY-NINE_Natural_Illustrating_v402mgr.md", "a living file", "seventeen names, bi-foldings, and a local nine, as drawings"),
    ("The seventeen names in one table", TABLE, "v403mgr", "a name a row by 88 columns, a column with the living file it is of, or executed, an is, or floating"),
    ("Each name in the co-chaining logic", "incoming/v403mgr/Each_name_in_the_co-chaining_logic.csv", "v403mgr",
     "a name's entering sentence in Exhibit THIRTY, and its side in Exhibit ONE, Exhibit THIRTY and Natural Illustrating"),
    ("Each living file by the names", "incoming/v403mgr/Each_living_file_by_the_names.csv", "v403mgr", "a living file a row, the names it says whole"),
    ("Each form among names by its parities", "incoming/v403mgr/Each_form_among_names_by_its_parities.csv", "v403mgr", "the twelve forms, a form a row"),
    ("Each number by its logical seventeen", "incoming/v403mgr/Each_number_by_its_logical_seventeen.csv", "v403mgr", "a number a row, its name of the seventeen sixteen on"),
    ("The co-chaining logic by the names, its instrument", "incoming/v403mgr/instruments/co_chaining_logic_by_the_names.py", "v403mgr", "executes a name's entering, its side in three files, and the twelve forms"),
    ("The window of the seventeen names", "incoming/v406all2-2/The_window_of_the_seventeen_names.md", "v406all2-2", "the opening's proposed lines 38 to 46 beside their living sentences; paused on 23 November"),
    ("The plan of the window of the seventeen names", "incoming/v406all2-2/The_plan_of_the_window_of_the_seventeen_names.md", "v406all2-2", "nine opportunities and an order of six steps"),
    ("The tables combining, gone through by the seventeen names", "incoming/v406all2-2/The_tables_combining_gone_through_by_the_seventeen_names.md", "v406all2-2", "four places found, and one sentence with a partner"),
    ("The seventeen names' checks, its instrument", "incoming/v406all2-2/instruments/seventeen_names_checks.py", "v406all2-2", "45 lines, by its own arithmetic"),
    ("The names on a pair of cones, its instrument", "incoming/v406all2-2/instruments/the_names_on_a_pair_of_cones.py", "v406all2-2", "the sixteen places of a pair of cones as the names 1 to 16"),
    ("The method by the seventeen names, a sheet", "incoming/v406me/The_managing_table_its_sheet_The_method.csv", "v406me", "the expedition's working at a name, a candidate laid for breaking"),
    ("Along and across by the living sentence of the seventeen names", "incoming/v404helping/Along_and_across_by_the_living_sentence_of_the_seventeen_names.md", "v404helping", "along and across, by the names"),
    ("The source of a future session, Exhibit ONE's stable forms", "incoming/v406me/sources/The_source_of_Exhibit_ONE_stable_form_resolver.md", "v406me", "the page a session of the seventeen names opens by; no session is risen at it"),
]

def folder(n): return G1 if n <= 3 else G2 if n <= 39 else G3
def text_of(n):
    root = ROOT if n <= 39 else V408
    if n <= 3: f = sorted((root / (G1 + "illustrations")).glob(f"draft_{n}_*.svg"))[0]
    else: f = root / (folder(n) + f"illustrations/artboards/Draft{n}.dc.html")
    t = f.read_text(encoding="utf-8")
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return "\n".join(l for l in (re.sub(r"\s+", " ", x).strip() for x in t.splitlines()) if l)
def exhibit_one_of(root): return sorted(root.glob("Exhibit_ONE_Natural_Resolver_*.md"))[0]
def names_of(one_text):
    """Exhibit ONE's own table of the seventeen names: n, name, root, four binary digits, co, its three."""
    return re.findall(r"^\| (\d+) \| \*\*(\d+-[a-z-]+)\*\* \| ([^|]+?) \| ([^|]+?) \| (\w+) \| ([a-z-]+) \|", one_text, flags=re.M)
def executed(args, cwd):
    p = subprocess.run([sys.executable, "-I"] + args, cwd=cwd, capture_output=True, text=True, timeout=600)
    return p.returncode, p.stdout
def primes(k):
    out, n = [], 2
    while len(out) < k:
        if all(n % p for p in out): out.append(n)
        n += 1
    return out

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--lay"]; LAY = "--lay" in sys.argv
    ROOT = Path(args[0]).resolve(); V408 = Path(args[1]).resolve() if len(args) > 1 else ROOT; NEXT = Path(args[2]).resolve() if len(args) > 2 else None
    if not (V408 / G3).is_dir():
        sys.exit("v408illustrating's folder is not at " + str(V408) + ": give the root with it as the second path, by this instrument's own usage")
    said = Counter()
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")

    print("1 · The works of the seventeen names, at their places")
    at = [(ROOT / p).exists() for _, p, _, _ in WORKS]
    line("is", all(at), f"all {len(WORKS)} works of this instrument's list are at their places in the set")
    by = Counter(s for _, _, s, _ in WORKS)
    line("judged", True, "a work by its hand: " + "; ".join(f"{k} {v}" for k, v in by.most_common()))
    code, out = executed(["incoming/v406all2-2/instruments/seventeen_names_checks.py", TABLE], ROOT)
    line("is", code == 0 and "45 is, 0 is-not" in out, "v406all2-2's checks of the seventeen names, executed today: 45 is, 0 is-not")
    code, out = executed(["incoming/v403mgr/instruments/co_chaining_logic_by_the_names.py", "."], ROOT)
    parts_line = "twelve are one saying in the three, and five part: 2, 5, 7, 14 and 15"
    line("is", code == 0 and parts_line in out, "v403mgr's co-chaining logic by the names, executed today at the root: all its checks is")

    print("\n2 · The one table beside Exhibit ONE's own")
    rows = list(csv.DictReader(open(ROOT / TABLE, encoding="utf-8"))); head = list(rows[0].keys())
    kinds = Counter(re.search(r"\[([^\]]+)\]$", h).group(1).split()[0] for h in head)
    line("is", len(rows) == 17 and len(head) == 88, f"the one table is seventeen names by 88 columns: {kinds['living']} of a living file, {kinds['executed']} executed, {kinds['an']} an is, {kinds['floating']} floating")
    col = {k: next(h for h in head if h.startswith(k)) for k in ("name", "root", "n − 1", "co or one", "its three", "its now, a parity", "its prime, by its position")}
    def same_as(root):
        own = names_of(exhibit_one_of(root).read_text(encoding="utf-8"))
        return len(own) == 17 and all((r[col["name"]], r[col["root"]], r[col["n − 1"]], r[col["co or one"]], r[col["its three"]]) == (o[1], o[2], o[3], o[4], o[5]) for r, o in zip(rows, own))
    line("is", same_as(ROOT), "its name, root, four binary digits, co and three are Exhibit ONE's own at the root, at all seventeen")
    if NEXT: line("is", same_as(NEXT), "and the same at the next version's Exhibit ONE, at all seventeen")

    print("\n3 · Places of the works' parting")
    line("found", parts_line in out, "a name's side is one saying in Exhibit ONE, Exhibit THIRTY and Natural Illustrating at twelve names, and parts at five: 2, 5, 7, 14 and 15, by an other and others")
    if NEXT:
        code_n, out_n = executed([str(ROOT / "incoming/v403mgr/instruments/co_chaining_logic_by_the_names.py"), "."], NEXT)
        line("found", parts_line in out_n, "the same five part at the next version")
        g = "".join((NEXT / "gathering-value" / f).read_text(encoding="utf-8") for f in ("Co-Chaining_Logic_Registry.md", "Natural_Illustrating.md"))
        line("found", "co_chaining_logic_by_the_names.py" in g and "illustrating_by_the_table.py" in g, "a note of a name's side waits at two gathering files of the next version, the co-chaining registry's and Natural Illustrating's")
    one = exhibit_one_of(ROOT).read_text(encoding="utf-8"); own = names_of(one)
    three = {int(n): t for n, _, _, _, _, t in own}
    line("is", three[1] == three[9] == three[17] == "co-bi-tri" and [n for n in three if three[n] == "tri-bi-co"] == [7, 15],
         "Exhibit ONE's table: 1, 9 and 17 are one three, co-bi-tri; and tri-bi-co is the three of 7 and 15")
    T = {n: text_of(n) for n in range(1, 57)}
    line("found", "1 · 17\ntri-bi-co\n9\nco-bi-tri" in T[4], "the 4th drawing: tri-bi-co at 1 and 17, and co-bi-tri at 9")
    asking = "The three of 9-next-co-discovering faces other-than the three of 1-now-existing and of 17-next-existing."
    line("found", asking in (ROOT / "incoming/v406me/Resuming_v406me.md").read_text(encoding="utf-8"), "the asking of it is open at v406me's page for resuming, and v406me is no session now")
    bi_root = re.search(r"co me-parity, bi ([a-z]+-parity), tri all-parity", one).group(1)
    table_now = Counter(r[col["its now, a parity"]] for r in rows)
    line("found", bi_root == "other-parity" and "both-parity" in table_now, f"a bi's parity: Exhibit ONE at the root says {bi_root}; the one table says both-parity")
    if NEXT:
        bi_next = re.search(r"co me-parity, bi ([a-z]+-parity), tri all-parity", exhibit_one_of(NEXT).read_text(encoding="utf-8")).group(1)
        line("found", bi_next == "both-parity", f"and Exhibit ONE at the next version says {bi_next}")
    line("found", "co me-parity, bi other-parity, tri all-parity" in T[26], "the 26th drawing says a bi other-parity, as the root")
    by_position = primes(17); on_cones = [n for n in range(1, 60) if n % 2 and n % 3 and n % 5]
    line("is", [int(r[col["its prime, by its position"]]) for r in rows] == by_position, "the one table: a name's prime by its position is 2, 3, 5 and on to 59, at all seventeen")
    line("is", len(on_cones) == 16 and "Names 7, 8, 9 and 10 are at 23, 29, 31 and 37" in T[14] and on_cones[6:10] == [23, 29, 31, 37],
         "the 14th drawing: the names 1 to 16 are at the sixteen numbers of 1 to 59 crossed by none of 2, 3 and 5; 7, 8, 9 and 10 at 23, 29, 31 and 37")
    differ = [n for n in range(1, 17) if by_position[n - 1] != on_cones[n - 1]]
    line("found", len(differ) == 16, f"a name is with two numbers, its prime by its position and its number on a pair of cones, other at all {len(differ)} names: the 9th is with 23 and with 31")
    line("found", not any("cone" in h for h in head), "the one table is with no column of a name's number on a pair of cones")

    print("\n4 · The Living File Registry beside the illustrating")
    reg = sorted(ROOT.glob("Exhibit_TWENTY-SIX_Living_File_Registry_*.md"))[0].read_text(encoding="utf-8")
    line("is", "Together its subtitles are its set's floating neutralling contents" in reg and "Its titles name those subjects." in reg,
         "the registry says a set's titles name its subjects, and its subtitles together are the set's floating neutralling contents")
    ls = reg.splitlines(); a = next(i for i, l in enumerate(ls) if l.startswith("## 4.2")); b = next(i for i, l in enumerate(ls) if l.startswith("## 4.3"))
    seams = [l for l in ls[a:b] if l.startswith("- **") and "⇌" in l]
    k = lambda *ws: sum(1 for l in seams if all(w in l for w in ws))
    line("found", True, f"its couplings of files are {len(seams)} seams: {k('Resolver')} with Natural Resolver, {k('Co-Chaining')} with the Co-Chaining Logic Registry, {k('Illustrating')} with Natural Illustrating, {k('Naming')} with Natural Naming")
    line("found", k("Resolver", "Co-Chaining") == 0 and k("Illustrating", "Co-Chaining") == 0,
         "no seam is with Natural Resolver and the Co-Chaining Logic Registry both, and none with Natural Illustrating and the Co-Chaining Logic Registry both")
    line("found", k("Resolver", "Naming", "Illustrating") == 1, "one seam is with Natural Resolver, Natural Naming and Natural Illustrating, Natural Intelligence ahead of them")
    files = [f for f in sorted(ROOT.glob("*.md")) if f.name != "README.md"]; seventeen = [n for _, n, _, _, _, _ in own]
    whole = {f.name: sum(1 for n in seventeen if re.search(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", f.read_text(encoding="utf-8"))) for f in files}
    all17 = [f for f, c in whole.items() if c == 17]; none17 = [f for f, c in whole.items() if c == 0]
    line("found", True, f"of the 33 living files, {len(all17)} say all seventeen names whole, {33 - len(all17) - len(none17)} say some, and {len(none17)} say none")
    line("is", any("Natural_Illustrating" in f for f in all17) and any("Co-Chaining" in f for f in all17) and any("Natural_Naming" in f for f in all17),
         "Natural Illustrating, the Co-Chaining Logic Registry and Natural Naming are among the files saying all seventeen")
    d_whole = [n for n in T if any(re.search(r"(?<![\w-])" + re.escape(x) + r"(?![\w-])", T[n]) for x in seventeen)]
    line("found", True, f"of the 56 drawings, {len(d_whole)} say a name of the seventeen whole: {', '.join(map(str, d_whole))}")
    line("found", len(list((ROOT / "gathering-value" / "drawings").glob("*.svg"))) == 1, "the set's own folder of drawings is with one drawing; all 56 are candidates in three sessions' folders")

    print("\n5 · The twelve candidate subtitles' heads, by the three exhibits")
    cand = list(csv.DictReader(open(ROOT / MINE / "Twelve_figures_a_figure_a_row_its_candidate_title_and_subtitle.csv", encoding="utf-8")))
    heads = [r["A candidate subtitle, an -ing head with a term it holds"].split()[0].lower() for r in cand]
    three_files = {"Exhibit ONE": one.lower(), "Exhibit THIRTY": sorted(ROOT.glob("Exhibit_THIRTY_Co-Chaining_*.md"))[0].read_text(encoding="utf-8").lower(),
                   "Natural Naming": sorted(ROOT.glob("Exhibit_TWENTY_Natural_Naming_*.md"))[0].read_text(encoding="utf-8").lower()}
    inn = {name: [h for h in heads if re.search(r"(?<![\w-])" + re.escape(h) + r"(?![\w-])", t)] for name, t in three_files.items()}
    line("found", True, "of the twelve heads: " + "; ".join(f"{len(v)} are in {k}" for k, v in inn.items()))
    all_three = [h for h in heads if all(h in v for v in inn.values())]; none_three = [h for h in heads if not any(h in v for v in inn.values())]
    line("found", True, f"{len(all_three)} are in all three: {', '.join(all_three)}; and {len(none_three)} in none of the three: {', '.join(none_three) or 'none'}")

    if LAY:
        with open(ROOT / MINE / "The_works_of_the_seventeen_names_a_work_a_row.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["A work of the seventeen names", "Its place", "Its hand", "What it is"])
            for row in WORKS: w.writerow(row)
        print("\nlaid: one table in " + MINE)

    print(f"\n{said['is']} are is; {said['found']} are found, whole; {said['judged']} are judged, and said as judged" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
