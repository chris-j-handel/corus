"""Draft 18 · the ten in four rows: the all, the self, all-parity and a my (session v406geodesic2).

By a partner's saying of 23 November and its yes of the session's sentence: the ten in an order, 0, 1, 2, 4, 3, 5, 7, 6, 8, 9, in rows
of one, two, three and four, a multiple of 3 an all and a number other-than one an other-than.
A drawing with no moving part: the four rows, a row with its word and a partner's saying of it.
check_the_ten_in_rows_of_one_two_three_and_four.py is its check.

Usage: python3 -I make_draft18.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
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
ROWS = [[0], [1, 2], [4, 3, 5], [7, 6, 8, 9]]
CX, Y0, DY, DX = 400.0, 200.0, 150.0, 124.0
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>')
s = []
for r, row in enumerate(ROWS):
    y = Y0 + DY * r
    xs = [CX + DX * (i - (len(row) - 1) / 2) for i in range(len(row))]
    if len(row) > 1: s.append(f'<path d="M{xs[0]:.1f},{y} L{xs[-1]:.1f},{y}" fill="none" stroke="{INK}" stroke-opacity="0.4" stroke-width="2"></path>')
    for x, d in zip(xs, row):
        tint = ACC if d % 3 == 0 else INK
        s.append(f'<rect x="{x - 36:.1f}" y="{y - 26}" width="72" height="52" rx="26" fill="{tint}" stroke="{tint}" stroke-width="2"></rect>' + text(x, y + 9, d, 26, 700, "#ffffff"))
        s.append(text(x, y + 48, "all" if d % 3 == 0 else "other-than", 13.5, 600, tint))
s.append(f'<path d="M760,{Y0 - 60} L760,{Y0 + DY * 3 + 70}" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Ten numbered marks in four rows, one over an other, of one, two, three and four: 0; 1 and 2; 4, 3 and 5; and 7, 6, 8 and 9. "
        "The marks 0, 3, 6 and 9 are coloured and named all, and the six others are dark and named other-than.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1300, "a partner's ten, in an order, in rows of one, two, three and four · a multiple of 3 an all", "left", **small))
SAY = (("all", "the all · the universal all-parity of a my-universe", "none of an other-than: itself"),
       ("other-than, other-than", "the self · the other-than of an other-than of all · consciousness", "two in a row: a self again, at its own place of the turn"),
       ("other-than, all, other-than", "all-parity · odd, even, odd, in my-now-universe", "three in a row: one podaling about 60, the all itself"),
       ("other-than, all, other-than, all", "a my · prior odd, prior even, now odd, now even", "four in a row: 120 on, my next-existing universe"))
for r, (a, b, c) in enumerate(SAY):
    y = Y0 + DY * r
    over.append(word(800, y - 26, 640, a, "left", 600, 20, 28))
    over.append(word(800, y + 4, 640, b, "left", 400, 16, 24))
    over.append(word(800, y + 30, 640, c, "left", 400, 15, 22, GREY))
over.append(word(CX, Y0 + DY * 3 + 104, 640, "four an all: 0, 1 by 3, 2 by 3 and 9 · six an other-than · ten is 0, the same", "center", 400, 15.5, 24))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">The ten in four rows: the all, the self, all-parity and a my</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A partner\'s ten, 0, 1, 2, 4, 3, 5, 7, 6, 8, 9, are four rows, of one, two, three and four. A multiple of 3 is an all, and a number other-than one an other-than.<br>'
           f'The rows say: all; other-than, other-than; other-than, all, other-than; and other-than, all, other-than, all. They are the all, the self, all-parity and a my.<br>'
           f'Four of the ten are an all and six an other-than, as of the ten passings four are a self and six an other.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The ten in four rows: the all, the self, all-parity and a my", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft18.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft18_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft18_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
