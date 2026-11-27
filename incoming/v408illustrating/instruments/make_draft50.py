"""Draft 50 · five co-linear and ten across: the cube of 5 on its line (session v408illustrating).

A partner's saying of 25 November, rigorized and drawn: five cells still on one line; a between of two of them two planes
across; and the ten sixes about the line, a six a round on one plane, six of the ten about a central nothing.
a_partner_s_saying_of_five_co-linear_and_ten_bi-planar_rigorized.py is its check. The numbers drawn here are executed
here again, by its own lines.

Its placings, no execution says them: the cube, its line and its planes are a drawing's, and no number's; the line laid
across the page; a plane turned to the eye, a six's round drawn about the line, its six evenly round it.

Usage: python3 -I make_draft50.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
from geom import page as lay
spec = importlib.util.spec_from_file_location("five_ten", os.path.join(HERE, "a_partner_s_saying_of_five_co-linear_and_ten_bi-planar_rigorized.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
far = lambda c: 3 * sum(v * v for v in c) - sum(c) ** 2             # a cell's distance from the line, squared, by three
sixes = sorted({m.turned(c) for c in m.cells if len(m.turned(c)) == 6}, key=lambda g: (m.plane(next(iter(g))), sorted(next(iter(g)))))
rows = [(tuple(sorted(next(iter(g)))), m.plane(next(iter(g))), far(next(iter(g)))) for g in sixes]
assert len(rows) == 10 and sorted(p for _, p, _ in rows if p % 3) == [4, 5, 5, 7, 7, 8] and [m.plane(c) for c in m.on_line] == [0, 3, 6, 9, 12]
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
X0, U, LY = 130, 104, 500
px = lambda plane: X0 + U * plane
s = [f'<line x1="{px(0) - 40}" y1="{LY}" x2="{px(12) + 40}" y2="{LY}" stroke="{INK}" stroke-width="2"></line>']
for p in range(13):
    on = p % 3 == 0
    dash = "" if on else 'stroke-dasharray="4 5"'
    s.append(f'<line x1="{px(p)}" y1="{LY - 150}" x2="{px(p)}" y2="{LY + 150}" stroke="{RAY}" stroke-width="{1.4 if on else 1.1}" {dash}></line>')
    s.append(text(px(p), LY + 172, str(p), 12.5, 600, INK if on else GREY))
for three, p, f in rows:
    r, floating = 9.2 * math.sqrt(f), p % 3 != 0
    for k in range(6):
        a = math.radians(60 * k + (0 if f != 14 else 30))
        s.append(f'<circle cx="{px(p) + r * math.cos(a):.1f}" cy="{LY + r * math.sin(a):.1f}" r="5" fill="{ACC if floating else INK}"></circle>')
    s.append(f'<circle cx="{px(p)}" cy="{LY}" r="{r:.1f}" fill="none" stroke="{ACC if floating else INK}" stroke-width="1" opacity="0.45"></circle>')
for p in range(13):
    if p % 3 == 0: s.append(f'<circle cx="{px(p)}" cy="{LY}" r="7.5" fill="{INK}" stroke="#ffffff" stroke-width="1.6"></circle>')
    else: s.append(f'<circle cx="{px(p)}" cy="{LY}" r="4.2" fill="#ffffff" stroke="{GREY}" stroke-width="1.3"></circle>')
TX, TY, TW = 130, 760, 124
for j, (three, p, f) in enumerate(rows):
    floating = p % 3 != 0; x = TX + TW * j
    s.append(f'<rect x="{x + 3}" y="{TY}" width="{TW - 6}" height="30" rx="6" fill="{ACC if floating else INK}"></rect>' + text(x + TW / 2, TY + 20, " ".join(map(str, three)), 13, 600, "#ffffff"))
    pair = sorted(set(range(5)) - set(three))
    s.append(f'<rect x="{x + 3}" y="{TY + 36}" width="{TW - 6}" height="26" rx="6" fill="#ffffff" stroke="{RAY}" stroke-width="1.2"></rect>' + text(x + TW / 2, TY + 54, f"{pair[0]} {pair[1]}", 12.5, 600, GREY))
    s.append(text(x + TW / 2, TY + 82, f"plane {p}", 11.5, 500, GREY))
ARIA = ("A drawing with no moving part. A line across the page with thirteen upright lines over it, five whole and eight dashed; five dark dots on the line at the whole ones, "
        "and small open circles at the dashed ones. About the line are ten rounds of six dots, four dark about a dark dot and six in the accent about an open circle. "
        "Under them a row of ten boxes of three numbers, with ten boxes of two numbers; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=700: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=700: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=700: word(x, y, w, t, "left", 600, 14.5, 20)
dot = lambda fill, edge: f'<span style="display: inline-block; width: 10px; height: 10px; border-radius: 6px; background: {fill}; border: 1.5px solid {edge}; margin: 0 6px 0 0; vertical-align: -1px"></span>'
over = [word(60, 40, 1400, "50 · a figure, the cube of 5 on its line · it is for a partner's saying of 25 November, rigorized · its prior, 41", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("Five cells are still on one line.", "A between of two of them is two planes across.", "Six of the ten sixes are about a central nothing.")):
    over.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
over.append(note(860, 104, "a partner's saying of 25 November, in this session's words:", 600))
over.append(note(860, 126, "5 is co-linear neutralling · 10 is a bi-planar floating surface ·", 600))
over.append(note(860, 146, "the co-linear is along, through the central nothing on the plane", 600))
over.append(head(60, 250, "the cube of 5 on its line, 13 planes across it", 760))
over.append(note(60, 274, dot(INK, INK) + "a cell of the line, still by all six orders of the three ways &nbsp; " + dot("#ffffff", GREY) + "a central nothing: the line is through at no cell", 900))
over.append(note(60, 296, dot(INK, INK) + "a six about a cell of the line, four &nbsp; " + dot("{{accent}}", "{{accent}}") + "a six about a central nothing, six &nbsp; · a six is a round on one plane, all six at one distance from the line", 1100))
over.append(word(60, LY + 172 - 5, 60, "a plane", weight=600, size=12.5, h=18, color=GREY))
over.append(head(60, 722, "the ten sixes, five's choosings of three, with the pair of five a six is with none of", 900))
over.append(note(60, 870, "● the ten are 6 and 4 by the line · ○ is-not: four of the ten are about a cell of the line, at the planes 3, 6, 6 and 9", 1300))
over.append(note(60, 892, "v406geodesic2's 8th drawing is the cube of 5 on its line · v407primes' form names the ten sixes · neutralling and floating are namings", 1300))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Five co-linear and ten across: the cube of 5 on its line</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'Of the cube\'s 125 cells five are still by all six orders of the three ways, and the five are one line.<br>'
           f'A between of two of the five is two planes across the line, and the line is through them at no cell.<br>'
           f'The sixes about the line are ten, one for one with the ten pairs of five. A six is a round on one plane.<br>'
           f'Six of the ten are about a central nothing, and four about a cell of the line. A candidate, of a partner\'s saying.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = lay("Five co-linear and ten across: the cube of 5 on its line", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft50.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft50_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft50_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; the ten by their planes:", [p for _, p, _ in rows])
