"""Draft 19 · a diamond of nine: two triangles, one into the other (session v406geodesic2).

By a partner's saying of 23 November, after the eighteenth drawing, re-said: the figure is a diamond and no triangle; two triangles
are counter-turning into one another, and it says their arc one way and their arc the other way; the even rows are 2, 4 and under
it 6, 8, and the odd are 1, then 3, 5, 7, then 9.
A drawing with no moving part: the nine in the diamond's rows, its two arcs, its two triangles, and 0 apart.
check_the_diamond_of_nine_two_triangles.py is its check.

Usage: python3 -I make_draft19.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
DIAMOND = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
CX, Y0, DY, DX = 400.0, 170.0, 150.0, 150.0
at = {d: (CX + DX * (i - (len(row) - 1) / 2), Y0 + DY * r) for r, row in enumerate(DIAMOND) for i, d in enumerate(row)}
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>')
seg = lambda a, b, look: f'<path d="M{at[a][0]:.1f},{at[a][1]:.1f} L{at[b][0]:.1f},{at[b][1]:.1f}" fill="none" {look}></path>'
s = []
# the two triangles, one into the other at the row 3, 5, 7
s.append(f'<path d="M{at[1][0]:.1f},{at[1][1] - 46:.1f} L{at[7][0] + 70:.1f},{at[7][1] + 10:.1f} L{at[3][0] - 70:.1f},{at[3][1] + 10:.1f} Z" fill="{ACC}" fill-opacity="0.07" stroke="{ACC}" stroke-opacity="0.6" stroke-width="1.4"></path>')
s.append(f'<path d="M{at[9][0]:.1f},{at[9][1] + 46:.1f} L{at[7][0] + 70:.1f},{at[7][1] - 10:.1f} L{at[3][0] - 70:.1f},{at[3][1] - 10:.1f} Z" fill="{INK}" fill-opacity="0.05" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.4"></path>')
for a, b, c in ((1, 2, 3), (4, 5, 6), (7, 8, 9)):           # an arc one way, a step of 1
    s.append(seg(a, b, f'stroke="{INK}" stroke-width="2.6"')); s.append(seg(b, c, f'stroke="{INK}" stroke-width="2.6"'))
for a, b, c in ((1, 4, 7), (2, 5, 8), (3, 6, 9)):           # an arc the other way, a step of 3
    s.append(seg(a, b, f'stroke="{ACC}" stroke-width="2.6" stroke-dasharray="8 6"')); s.append(seg(b, c, f'stroke="{ACC}" stroke-width="2.6" stroke-dasharray="8 6"'))
for d, (x, y) in at.items():
    tint = ACC if d % 2 else INK
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="30" fill="{tint}" stroke="#ffffff" stroke-width="3"></circle>' + text(x, y + 9, d, 26, 700, "#ffffff"))
    if d % 3 == 0: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="37" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="3 4"></circle>')
s.append(f'<circle cx="110" cy="{Y0}" r="30" fill="#ffffff" stroke="{INK}" stroke-width="2.6"></circle>' + text(110, Y0 + 9, 0, 26, 700))
s.append(f'<path d="M800,{Y0 - 60} L800,{Y0 + DY * 4 + 60}" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
LY = 276.0
s.append(f'<path d="M840,{LY} L900,{LY}" fill="none" stroke="{INK}" stroke-width="2.6"></path><path d="M840,{LY + 100} L900,{LY + 100}" fill="none" stroke="{ACC}" stroke-width="2.6" stroke-dasharray="8 6"></path>')
ARIA = ("A drawing with no moving part. Nine numbered marks in a diamond, in five rows, one over an other: 1; 2 and 4; 3, 5 and 7; 6 and 8; and 9. The odd numbers are coloured and the even dark, "
        "and 3, 6 and 9 are ringed. Lines join 1, 2, 3; 4, 5, 6; and 7, 8, 9 one way, and dashed lines join 1, 4, 7; 2, 5, 8; and 3, 6, 9 the other way. "
        "Two triangles are drawn over them, one from 1 to the row 3, 5, 7 and one from 9 to that row. A mark 0 is apart from the diamond.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1300, "a partner's nine in a diamond, two triangles one into the other · 0 apart", "left", **small))
over.append(word(110, Y0 + 50, 160, "0 · ten, the same", "center", 400, 14, 20, GREY))
for r, t in enumerate(("odd", "even", "odd", "even", "odd")):
    over.append(word(720, Y0 + DY * r, 80, t, "left", 600, 15, 22, GREY))
R = [("the rows", "1; 2, 4; 3, 5, 7; 6, 8; 9 · a row odd or even all through, odd and even in turn", "one, two, three, two and one: a pair of cones observed across"),
     ("an arc one way, a step of 1", "1, 2, 3 · 4, 5, 6 · 7, 8, 9", "other-than, other-than, all"),
     ("an arc the other way, a step of 3", "1, 4, 7 · 2, 5, 8 · 3, 6, 9 · none, 1 by 3 and 2 by 3", "3, 6 and 9, ringed, an all: one arc of it"),
     ("two triangles, one into the other", "the upper of 1; 2, 4; 3, 5, 7 and the lower of 3, 5, 7; 6, 8; 9", "the podaling about 5 carries one to the other, an arc gone the other way"),
     ("with it", "all and other-than are one for the other: 3 with 7, 6 with 4, 9 with 1", "odd and even are as they are")]
for i, (a, b, c) in enumerate(R):
    y = 176 + 100 * i
    x = 920 if i in (1, 2) else 840
    over.append(word(x, y - 22, 560, a, "left", 600, 18, 26))
    over.append(word(x, y + 4, 600, b, "left", 400, 15, 22))
    over.append(word(x, y + 26, 600, c, "left", 400, 14.5, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A diamond of nine: two triangles, one into the other</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A partner\'s order after its 0 is a diamond, row by row: 1; 2, 4; 3, 5, 7; 6, 8; and 9. It is the three by three of 1 to 9, turned.<br>'
           f'A row is odd or even all through. One way an arc is a step of 1, and the other way a step of 3: none, 1 by 3 and 2 by 3.<br>'
           f'Two triangles are one into the other at the row 3, 5, 7, and the podaling about 5 carries one to the other, an arc to an arc gone the other way.<br>'
           f'A pair of cones observed across is this diamond. The eighteenth drawing\'s four rows are of the same order, a row odd and even among one another.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A diamond of nine: two triangles, one into the other", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft19.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft19_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft19_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
