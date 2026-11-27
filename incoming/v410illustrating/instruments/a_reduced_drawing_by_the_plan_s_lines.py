"""v410illustrating · a drawing of the reduced set, gone through by the plan's own lines; and the reduced set, three floating columns of the twelve figures' table.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/a_reduced_drawing_by_the_plan_s_lines.py . [--lay]

The plan is `The_plan_of_the_reducing_laid_with_an_is_of_both.md`. Its lines 2 to 5 and 7 are executed here at a drawing
of the reduced set: beside the drawings it gathers and writing in none; saying on itself its figure, its prior figure,
its next figures and the drawings it gathers; one name for one thing; a title and a subtitle, a bi-coupling; and
between Exhibit ONE and Exhibit THIRTY, with Natural Naming.

Do no harm: it opens the artboards of this session and of the drawings gathered, and writes in none. It makes the
drawing again by its maker in a folder outside the set, and executes the one list's instrument on a copy of the
drawing's own text outside the set. With --lay it writes three floating columns in the twelve figures' own table, in this
session's folder alone: one table, and not two. No cell the table had is moved.
A line is an is, executed here; or found, a thing found and laid whole.
"""
import csv, html, re, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path

MINE = "incoming/v410illustrating/"
G1, G2 = "incoming/v406geodesic/", "incoming/v406geodesic2/"
# a drawing of the reduced set: its number, its figure of the twelve, the drawings it gathers, its maker and its check
REDUCED = {57: (1, [1, 2, 3, 4, 5, 6], "make_draft57.py", "check_one_triangle_three_right_angles_bi-folding_1_to_17.py")}
ASKED = r"(?<![\w-])(?:twins?|loops?|rooms?|vaults?|rules?|distances?|apart|directions?|turn(?:s|ed|ing|ings)?|places?|sel(?:f|ves))(?![\w-])"
FILES = ("Exhibit ONE", "Exhibit THIRTY", "Natural Naming", "Natural Illustrating")

def text_of_file(f):
    t = f.read_text(encoding="utf-8")
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return "\n".join(l for l in (re.sub(r"\s+", " ", x).strip() for x in t.splitlines()) if l)
def text_of(root, n):
    if n <= 3: return text_of_file(sorted((root / (G1 + "illustrations")).glob(f"draft_{n}_*.svg"))[0])
    if n <= 39: return text_of_file(root / (G2 + f"illustrations/artboards/Draft{n}.dc.html"))
    return text_of_file(root / (MINE + f"illustrations/artboards/Draft{n}.dc.html"))
FLOATING = ["Its drawing of the reduced set, floating", "Its drawing's check, floating", "Its drawing's standing, floating"]
def names_of(root):
    one = sorted(root.glob("Exhibit_ONE_Natural_Resolver_*.md"))[0].read_text(encoding="utf-8")
    return re.findall(r"^\| \d+ \| \*\*(\d+-[a-z-]+)\*\* \|", one, flags=re.M)
def whole(name, t): return re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", t) is not None
def nth(n): return f"{n}{'th' if 10 < n % 100 < 14 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--lay"]; LAY = "--lay" in sys.argv
    ROOT = Path(args[0]).resolve()
    figures = list(csv.DictReader(open(ROOT / MINE / "Twelve_figures_a_figure_a_row_its_candidate_title_and_subtitle.csv", encoding="utf-8")))
    seventeen = names_of(ROOT)
    said = Counter(); rows = {}
    def line(kind, ok, words_):
        said[kind if ok else "is-not"] += 1; print(f"{kind if ok else 'is-not':7s} {words_}")

    for n, (fig, gathers, maker, check) in REDUCED.items():
        print(f"The {nth(n)} drawing, figure {fig} of twelve")
        t = text_of(ROOT, n); low = t.lower(); f = figures[fig - 1]
        title, subtitle = f["A candidate title, a whole bounding context"], f["A candidate subtitle, an -ing head with a term it holds"]
        line("is", len(t.split()) > 100, f"its artboard is in this session's folder, with {len(t.split())} words of its own")
        head = next((l for l in t.splitlines() if l.startswith(f"{n} · figure {fig} of twelve")), "")
        line("is", all(x in head for x in ("it gathers the 1st to the 6th drawings", "its prior figure", "its next figures")),
             "its head line says its figure, the drawings it gathers, its prior figure and its next figures")
        line("is", title in t and subtitle in t and not re.match(r"the ", title, re.I) and re.match(r"[A-Za-z-]+ing\b", subtitle),
             f"its title and its subtitle are the figure's candidates: no leading the, and an -ing head, {subtitle.split()[0].lower()}")
        line("is", all(whole(x, t) for x in seventeen), "all seventeen names of Exhibit ONE are said whole in it, a number and its naming one hyphenation")
        line("is", all(x in t for x in FILES), "it names Exhibit ONE, Exhibit THIRTY, Natural Naming and Natural Illustrating")
        line("is", not re.search(ASKED, low), "no word of the eleven a partner asked of is in it")
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / "a_drawing_s_own_text.md"; page.write_text(t + "\n", encoding="utf-8")
            o = subprocess.run([sys.executable, "-I", "incoming/v404mgr/instruments/words_of_no_natural_naming_in_a_page.py", str(page)], cwd=ROOT, capture_output=True, text=True).stdout
            m = re.search(r"^(\d+) places", o, flags=re.M)
            line("is", m is not None and m.group(1) == "0", "the one list's instrument, on its own text: 0 places")
            made = subprocess.run([sys.executable, "-I", MINE + "instruments/" + maker, tmp + "/artboard", tmp + "/working", "."], cwd=ROOT, capture_output=True, text=True)
            again = Path(tmp) / "artboard" / f"Draft{n}.dc.html"
            line("is", made.returncode == 0 and again.read_bytes() == (ROOT / MINE / f"illustrations/artboards/Draft{n}.dc.html").read_bytes(),
                 "its artboard made again by its maker is the artboard laid, byte for byte")
        c = subprocess.run([sys.executable, "-I", MINE + "instruments/" + check, "."], cwd=ROOT, capture_output=True, text=True)
        last = c.stdout.strip().splitlines()[-1]
        line("is", c.returncode == 0 and "IS-NOT" not in last, f"its check, executed here: {last}")
        G = {k: text_of(ROOT, k) for k in gathers}
        asked = {k: len(re.findall(ASKED, G[k].lower())) for k in gathers}
        line("found", True, f"the {len(gathers)} drawings it gathers are with {sum(asked.values())} places of the eleven words, in {sum(1 for v in asked.values() if v)} of them; it is with none")
        naming = [k for k in gathers if any(x in G[k] for x in FILES) or re.search(r"Exhibit [A-Z]", G[k])]
        wholes = [k for k in gathers if any(whole(x, G[k]) for x in seventeen)]
        line("found", True, f"of the {len(gathers)}, {len(naming)} name a living file and {len(wholes)} say a name of the seventeen whole; it names four files and says all seventeen")
        line("found", True, f"the {len(gathers)} are with {sum(len(G[k].split()) for k in gathers)} words of their own together; it is with {len(t.split())}")
        rows[fig] = (n, gathers, check, "laid, a candidate")

    if LAY:
        # one table, and not two: the reduced set is three floating columns of the twelve figures' own table
        base = [c for c in figures[0].keys() if c not in FLOATING]
        with open(ROOT / MINE / "Twelve_figures_a_figure_a_row_its_candidate_title_and_subtitle.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(base + FLOATING)
            for i, f in enumerate(figures, 1):
                n, gathers, check, standing = rows.get(i, ("", [], "", "ahead, no drawing made"))
                w.writerow([f[c] for c in base] + [n, check, standing])
        print("\nlaid: three floating columns in the twelve figures' table, in " + MINE)

    print(f"\n{said['is']} are is; {said['found']} are found, whole" + (f"; {said['is-not']} IS-NOT" if said["is-not"] else ""))
    sys.exit(1 if said["is-not"] else 0)
