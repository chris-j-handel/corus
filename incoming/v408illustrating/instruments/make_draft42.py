"""Draft 42 · the prime resolving form, one face: six prime livings across, ten fixings down (session v408illustrating).

The whole table of v407primes' page as one drawing's face, the opening of its drawings planned with a partner, a column
leading: a column one prime living, a row one of ten fixing unchangeable, a cell an interest. Its cells, its pairs and its
interests not yet resolving are opened from the page by the check's own lines, and nothing of a cell is said again here.
check_the_prime_resolving_form_one_face.py is its check.

Its placings, no execution says them: an interest's seat at its row, the page's own; the columns' and the rows' order on
the page, the page's own.

Usage: python3 -I make_draft42.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import html as H, importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the look of the thirty-nine before, geom.py
from geom import *
spec = importlib.util.spec_from_file_location("the_form", os.path.join(HERE, "check_the_prime_resolving_form_one_face.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
ROOT = Path(HERE).resolve().parents[2]
W, H_ = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
rows = m.the_table((ROOT / m.PAGE).read_text(encoding="utf-8"))
assert len(rows) == 10 and sum(bool(c) for r in rows for c in r[3]) == 34
LIVING = ("a prime lifts its prior turn p ways", "a prime born crossing a surface's horizon", "a prime's spiral comes again with 4 and 4p alone",
          "a crossed number passing a prime's closings", "a prime's place in 120's two pieces", "two primes' spirals locking as one torus")
X0, HEADW, CW, Y0, RH = 60, 236, 194, 268, 62
s, over = [], []
def word(x, y, w, h, t, size=11, weight=400, color=INK, align="left", lh=None, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {y:.0f}px; width: {w:.0f}px; height: {h:.0f}px; line-height: {lh or h}px; overflow: hidden; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
for j, (c, saying) in enumerate(zip(m.COLUMNS, LIVING)):                         # a column, a prime living
    x = X0 + HEADW + CW * j
    over.append(word(x + 8, 204, CW - 12, 22, c, 15.5, 600))
    over.append(word(x + 8, 227, CW - 14, 30, saying, 10.5, 400, GREY, lh=14))
    if j % 2 == 0: s.append(f'<line x1="{x + 6}" y1="{Y0 - 6}" x2="{x + 2 * CW - 6}" y2="{Y0 - 6}" stroke="{INK}" stroke-width="2"></line>')
for i, (name, now, nxt, cells) in enumerate(rows):                               # a row, one of ten fixing unchangeable
    y = Y0 + RH * i
    if i % 2 == 0: s.append(f'<line x1="{X0 - 8}" y1="{y + 3}" x2="{X0 - 8}" y2="{y + 2 * RH - 5}" stroke="{INK}" stroke-width="2"></line>')
    over.append(word(X0, y + 8, HEADW - 12, 34, H.escape(name[0].lower() + name[1:]), 12.5, 600, lh=16))
    over.append(word(X0, y + 27, HEADW - 12, 16, f"{now} · {nxt}", 11.5, 400, GREY))
    for j, cell in enumerate(cells):
        x = X0 + HEADW + CW * j
        if not cell:
            s.append(f'<rect x="{x + 3}" y="{y + 3}" width="{CW - 6}" height="{RH - 6}" rx="6" fill="#ffffff" stroke="{RAY}" stroke-width="1.2" stroke-dasharray="4 4"></rect>')
            continue
        s.append(f'<rect x="{x + 3}" y="{y + 3}" width="{CW - 6}" height="{RH - 6}" rx="6" fill="{TINT}" stroke="{RAY}" stroke-width="1"></rect>')
        t = H.escape(cell)
        for interest, r, c, _ in m.NOT_YET:
            if r == i + 1 and m.COLUMNS[j] == c:
                assert interest in cell
                t = t.replace(H.escape(interest), f'<span style="color: {{{{accent}}}}; font-weight: 600">{H.escape(interest)}</span>')
        over.append(word(x + 10, y + 7, CW - 19, RH - 13, t, 10.3, 400, INK, lh=12.4))
ARIA = ("A drawing with no moving part. A table of ten rows and six columns of boxes: thirty-four tinted boxes with words, and twenty-six open boxes with a dashed edge. "
        "Dark lines above the columns pair them two and two, and dark lines beside the rows pair them two and two. Five phrases of the words are in the accent; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H_}" viewBox="0 0 {W} {H_}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H_}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
head = [word(60, 29, 1400, 22, "for the prime resolving form, v407primes' · made from its own page · a column leads, a partner's is of 25 November", 15, 600, GREY, extra="letter-spacing: 1px")]
for i, t in enumerate(("A column is a prime living.", "A row is one of ten fixing unchangeable.", "A cell is an interest.")):
    head.append(word(60, 74 + 34 * i, 700, 30, t, 20, 600))
box = lambda fill, edge, dash="": f'<span style="display: inline-block; width: 22px; height: 12px; border-radius: 4px; background: {fill}; border: 1.2px {dash or "solid"} {edge}; margin: 0 7px 0 0; vertical-align: -2px"></span>'
head.append(word(820, 76, 640, 20, "the registry's sentence: <i>a hard problem is a changing fixing unchangeable</i>", 13.5, 400, GREY))
head.append(word(820, 104, 640, 20, box(TINT, RAY) + "a cell named, 34 of sixty · its words are the page's own", 13.5, 400, GREY))
head.append(word(820, 128, 640, 20, box("#ffffff", FAINT, "dashed") + "a cell with none named, 26: the form's own asking", 13.5, 400, GREY))
head.append(word(820, 152, 640, 20, '<span style="color: {{accent}}; font-weight: 600">in the accent</span> · an interest not yet resolving, five, by the page\'s own part', 13.5, 400, GREY))
head.append(word(820, 176, 640, 20, "a dark line: a pair · the columns three pairs, the rows five bi-couplings", 13.5, 400, GREY))
foot = [word(60, 896, 1400, 20, "● named, by column: 6, 7, 6, 3, 6 and 6 · by row: 2, 3, 4, 3, 3, 3, 3, 4, 4 and 5 &nbsp;&nbsp; ○ a seat, an interest's row, is a placing, the page's own: no number executes it", 13.5, 600, INK)]
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The prime resolving form, one face: six prime livings across, ten fixings down</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A column is a prime living, and a row is one of ten fixing unchangeable. A cell is an interest, the one fixing on the other.<br>'
           f'Of sixty cells thirty-four are named. A cell with none named is the form\'s own asking.<br>'
           f'A row is at a name now and that name 8 up next. 5 and 13 are with two rows, and 7 and 15 with two.<br>'
           f'Five interests are not yet resolving, by the page\'s own part. A candidate, made from v407primes\' page as it is.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H_}}
body = svg + "\n" + "\n".join(head + over + foot) + "\n" + title + "\n" + caption
page_html = page("The prime resolving form, one face: six prime livings across, ten fixings down", W, H_, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft42.dc.html").write_text(page_html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H_}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft42_preview.html").write_text(pv, encoding="utf-8")
own = [ARIA] + [H.unescape(re.sub(r"<[^>]+>", "", w)).replace("\xa0", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", re.sub(r"</?i>", "*", "\n".join(head + foot) + "\n" + title + "\n" + caption))).split("\n")]
Path(WORK, "draft42_words.md").write_text("\n".join(w for w in own if w) + "\n", encoding="utf-8")      # this drawing's own words; a cell's words are the page's
print(len(page_html), "bytes;", len([w for w in own if w]), "lines of its own words; cells named:", sum(bool(c) for r in rows for c in r[3]))
