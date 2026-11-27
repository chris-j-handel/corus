"""Draft 45 · two primes are a torus: the +1 winding through all their places (session v408illustrating).

A drawing of v408primes' sentence 41, with 5 and 7: a table of five by seven, thirty-five numbers at all thirty-five cells,
the +1 a slanting line; and beside it the six and the ten, the tori of 2 and 3 and of 2 and 5.
check_two_primes_are_a_torus.py is its check. The numbers drawn here are executed here again, by that check's own lines.

Its placings, no execution says them: 5 across and 7 down; 0 at the table's corner; a torus laid as a table.

Usage: python3 -I make_draft45.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_torus", os.path.join(HERE, "check_two_primes_are_a_torus.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
cells, again = m.the_torus(5, 7)
assert len(cells) == 35 == again
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
s = []
def table(x0, y0, cw, ch, p, q, size, lines=True):
    c, _ = m.the_torus(p, q); out = []
    for (a, b), n in c.items():
        x, y = x0 + cw * a + 3, y0 + ch * b + 3
        fill, edge, ink = (INK, INK, "#ffffff") if n == 0 else (ACC, ACC, "#ffffff") if (a == 0 or b == 0) else (TINT, RAY, INK)
        out.append(f'<rect x="{x}" y="{y}" width="{cw - 6}" height="{ch - 6}" rx="6" fill="{fill}" stroke="{edge}" stroke-width="1.2"></rect>' + text(x + cw / 2 - 3, y + ch / 2 + size * 0.2, str(n), size, 600, ink))
    if lines:
        for n in range(p * q - 1):
            a, b = n % p, n % q
            if a + 1 < p and b + 1 < q:
                out.append(f'<line x1="{x0 + cw * a + cw * 0.72:.0f}" y1="{y0 + ch * b + ch * 0.78:.0f}" x2="{x0 + cw * (a + 1) + cw * 0.28:.0f}" y2="{y0 + ch * (b + 1) + ch * 0.22:.0f}" stroke="{GREY}" stroke-width="1.2" stroke-dasharray="2 4"></line>')
    return out
X0, Y0, CW, CH = 200, 304, 100, 64
for a in range(5): s.append(text(X0 + CW * a + CW / 2, Y0 - 12, str(a), 14, 600, GREY))
for b in range(7): s.append(text(X0 - 16, Y0 + CH * b + CH / 2 + 5, str(b), 14, 600, GREY, "end"))
s += table(X0, Y0, CW, CH, 5, 7, 15)
s += table(820, 640, 46, 34, 2, 3, 12, False) + table(1060, 640, 46, 34, 2, 5, 12, False)
ARIA = ("A drawing with no moving part. A table of five columns and seven rows of numbered boxes, 0 to 34, all thirty-five with a number, with short dotted lines slanting from a box to the next. "
        "One column and one row of it are in the accent, and their corner box is dark. Beside it two small tables of numbered boxes, of six and of ten; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=660: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 14.5, 20)
box = lambda fill, edge: f'<span style="display: inline-block; width: 22px; height: 12px; border-radius: 4px; background: {fill}; border: 1.4px solid {edge}; margin: 0 7px 0 0; vertical-align: -2px"></span>'
over = [word(60, 40, 1400, "45 · a column's figure, Torus · it is for v408primes' co-chain, its sentence 41 · its prior, 43 · beside it now, 43", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("Two primes are a torus.", "The +1 winds through all their places.", "It is again at 0 and 0 at their turn, 35.")):
    over.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
over.append(note(860, 104, "v408primes' sentence 41, word for word:", 600))
over.append(note(860, 128, "<i>Two primes are a torus: the +1 winds through all their places,</i>", 600))
over.append(note(860, 148, "<i>p one way and q the other, and comes again at their turn.</i>", 600))
over.append(head(X0, 250, "its place round 5, across", 400)); over.append(word(60, 286, 120, "its place<br>round 7,<br>down", weight=600, size=13.5, h=54, color=GREY, extra="line-height: 18px"))
over.append(head(800, 262, "5 and 7, thirty-five numbers at all thirty-five cells"))
over.append(item(800, 296, "● a number is at its place round 5 and its place round 7, one for one"))
over.append(item(800, 322, "● +1 is one place on at both, the dotted lines · round the 5 seven times, round the 7 five"))
over.append(item(800, 348, "● its two primes are its two directions: a line of seven cells, and a line of five"))
over.append(note(800, 370, box("{{accent}}", "{{accent}}") + "crossed by 5, or by 7 &nbsp;&nbsp; " + box(INK, INK) + "0, at both &nbsp;&nbsp; " + box(TINT, RAY) + "of neither line, 24, four by six"))
over.append(item(800, 408, "● stepped with all pairs of two primes below 100: all cells reached, again at p by q alone"))
over.append(item(800, 446, "○ is-not: a prime with itself is no torus of two · 5 and 5 reach five of twenty-five cells"))
over.append(head(800, 520, "beside the 43rd drawing: the six and the ten"))
over.append(note(800, 546, "v408primes' saying: the six is the torus of 2 and 3, and the ten the torus of 2 and 5"))
over.append(note(800, 568, "all their cells are reached · 6 and 10 are with 2 in both, and reach thirty of their sixty"))
over.append(word(820, 620, 92, "2 and 3, six", "center", 600, 12.5, 18, GREY)); over.append(word(1060, 620, 92, "2 and 5, ten", "center", 600, 12.5, 18, GREY))
over.append(note(800, 836, "● the ten primes of the turn of 30 are 3 and 6 and 1, v408primes': 2, 3 and 5; three podal pairs; and 29"))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Two primes are a torus: the +1 winding through all their places</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A number is at its place round 5 and its place round 7, one for one. +1 is one place on at both.<br>'
           f'The +1 winds through all thirty-five cells, and is at 0 and 0 again at 35, their turn.<br>'
           f'Its two primes are its two directions: the numbers crossed by 5 are one line, and by 7 one line.<br>'
           f'A prime with itself is no torus of two. A candidate, of v408primes\' sentence 41.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Two primes are a torus: the +1 winding through all their places", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft45.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft45_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft45_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; cells reached:", len(cells), "again at", again)
