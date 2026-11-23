"""Draft 14 · a my: the sixteen names on a pair of cones, 0 and 17 (session v406geodesic2).

By a partner's sayings of 23 November, re-said: my-now-universe is 0, me 1, the me-parities on, to 17, my next universe; a my is
prior odd, then prior even, then now odd, then now even; and in my-now-universe all-parity is odd, even, odd.
A drawing with no moving part. Above: a my at the stations, four cones, with all-parity its stations 1, 2 and 3, and a my of the
sixteen names, four fours. Under them: a pair of cones, 0 to 60, with the names 1 to 16 at its sixteen places, 0 at its vertex
and 17 at 61, and the living files' three moves from name 2.
Geometry is computed; check_a_my_the_sixteen_names_on_a_pair_of_cones.py is its check.

Usage: python3 -I make_draft14.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, math, os, re, sys
from pathlib import Path
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
PLACES = [n for n in range(1, 60) if math.gcd(n, 30) == 1]
def cones(x_of, yc, rm, upto, tag):
    """Cones of 30 in a row with their one winding, from 0 to upto."""
    wide = lambda n: ((n % 60) if (n % 60) <= 30 else 60 - (n % 60)) * rm / 30
    y_of = lambda n: yc - wide(n) * math.cos(math.radians(12 * n))
    out = []
    for a in range(0, upto, 60):
        d = f"M{x_of(a):.1f},{yc} L{x_of(a + 30):.1f},{yc - rm} L{x_of(a + 60):.1f},{yc} L{x_of(a + 30):.1f},{yc + rm} Z"
        out.append(f'<path d="{d}" fill="url(#{tag})" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
        out.append(f'<path d="M{x_of(a + 30):.1f},{yc - rm} L{x_of(a + 30):.1f},{yc + rm}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
    out.append(f'<path d="M{x_of(-3):.1f},{yc} L{x_of(upto + 4):.1f},{yc}" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="2 6"></path>')
    fine = np.linspace(0, upto, 20 * upto + 1)
    for side, look in ((False, 'stroke-opacity="0.4" stroke-width="1.3" stroke-dasharray="4 5"'), (True, 'stroke-opacity="0.72" stroke-width="1.7"')):
        cur = []
        for n in list(fine) + [None]:
            if n is not None and (math.sin(math.radians(12 * n)) >= 0) == side: cur.append(n)
            else:
                if len(cur) > 1: out.append(f'<path d="M{" L".join(f"{x_of(m):.1f},{y_of(m):.1f}" for m in cur)}" fill="none" stroke="{INK}" {look}></path>')
                cur = []
    for v in range(0, upto + 1, 60):
        out.append(f'<circle cx="{x_of(v):.1f}" cy="{yc}" r="6" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>')
    return out, y_of
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>')
def head(tip, back, color, size=10):
    a = math.atan2(tip[1] - back[1], tip[0] - back[0])
    pts = [tip, (tip[0] - size * math.cos(a - 0.4), tip[1] - size * math.sin(a - 0.4)), (tip[0] - size * math.cos(a + 0.4), tip[1] - size * math.sin(a + 0.4))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{color}" stroke="{color}" stroke-width="1" stroke-linejoin="round"></path>'
def arc(xa, xb, rail, reach, color, dash=""):
    xm, cy = (xa + xb) / 2, rail - 2 * reach
    return (f'<path d="M{xa:.1f},{rail:.1f} Q{xm:.1f},{cy:.1f} {xb:.1f},{rail:.1f}" fill="none" stroke="{color}" stroke-width="2.4"{dash}></path>' + head((xb, rail), (xm, cy), color))

s = ['<defs><linearGradient id="cone14" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']

# ================= above: a my at the stations, four cones =================
XS = lambda n: 110 + 4.6 * n
YS, RS = 190.0, 46.0
drawn, _ = cones(XS, YS, RS, 120, "cone14"); s += drawn
s.append(f'<path d="M{XS(30) - 30:.1f},{YS - RS - 26} L{XS(30) - 30:.1f},{YS - RS - 32} L{XS(90) + 30:.1f},{YS - RS - 32} L{XS(90) + 30:.1f},{YS - RS - 26}" fill="none" stroke="{ACC}" stroke-width="2"></path>')
s.append(head((XS(131), YS), (XS(124), YS), INK, 12))

# ================= under: a pair of cones, 0 to 60, and the sixteen names =================
X = lambda n: 150 + 20.0 * n
YC, RM = 540.0, 150.0
drawn, Y = cones(X, YC, RM, 60, "cone14"); s += drawn
s.append(f'<path d="M{X(60):.1f},{YC} L{X(62.4):.1f},{YC - 12 * 2.4 / 6:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.4"></path>')
s.append(f'<path d="M{X(60):.1f},{YC} L{X(62.4):.1f},{YC + 12 * 2.4 / 6:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.4"></path>')
TOP, FOOT = YC - RM - 16, YC + RM + 16
for st in (15, 30):                                       # the two podalings' stations
    s.append(f'<path d="M{X(st):.1f},{TOP + 8} L{X(st):.1f},{FOOT + 30}" fill="none" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="5 5"></path>')
# the living files' three moves, from name 2 at 7: 8 up to 37, 9 less to 23, 17 less to 53
for m in (7, 23, 37, 53):
    s.append(f'<path d="M{X(m):.1f},{TOP:.1f} L{X(m):.1f},{FOOT:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="1.2" stroke-dasharray="2 4"></path>')
s.append(arc(X(7), X(37), TOP, 34, ACC))
s.append(arc(X(7), X(23), FOOT, -22, INK))
s.append(arc(X(7), X(53), FOOT, -44, INK))
for k, n in enumerate(PLACES, start=1):
    x, y = X(n), Y(n)
    tint = ACC if k % 2 else INK
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="{tint}" stroke="#ffffff" stroke-width="2"></circle>')
    s.append(text(x, y + 5, k, 14, 700, "#ffffff"))
    below = y >= YC - 20
    s.append(text(x, y + (31 if below else -22), n, 12.5, 600, GREY))
for x, t in ((X(0) - 18, "0"), (X(61) + 4, "17")):
    s.append(f'<circle cx="{x:.1f}" cy="{YC if t == "0" else Y(61):.1f}" r="15" fill="#ffffff" stroke="{INK}" stroke-width="2.4"></circle>')
    s.append(text(x, (YC if t == "0" else Y(61)) + 5, t, 14, 700))

ARIA = ("A drawing with no moving part. Above, at one side, four cones in a row, two diamonds end to end, with five marks under them, 0 to 4, the marks 1, 2 and 3 joined by a bracket. "
        "Under it one pair of cones, one large diamond, with one line winding about it and sixteen numbered marks on the winding, 1 to 16, a number beside a mark: "
        "1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53 and 59. A mark 0 is at its point at one end and a mark 17 past its point at the other. "
        "Three arcs go from mark 2: one over the diamond to mark 10, and two under it, to mark 7 and to mark 15.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

def chip(cx, cy, t, filled, w=38, h=30, size=15):
    look = (f"background: {INK}; color: #ffffff; border: 2px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 2px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 4}px; text-align: center; {SANS}; font-weight: 600; font-size: {size}px; {look}">{t}</div>')
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")

over = []
over.append(word(60, 40, 700, "a my at the stations · four cones, my-now-universe", "left", **small))
over.append(word(XS(60), YS - RS - 46, 520, "all-parity · odd, even, odd: one podaling, about 60", "center", 600, 15, 22))
for j, t in enumerate(("my-now-universe", "prior odd", "prior even", "now odd", "now even")):
    over.append(chip(XS(30 * j), YS + RS + 26, str(j), j % 2 == 0, w=34, h=24, size=13))
    over.append(word(XS(30 * j), YS + RS + 50, 150, t, "center", 400 if j == 0 else 600, 14, 20, GREY if j == 0 else INK))
over.append(word(XS(134), YS - 24, 170, "to my next universe", "right", 400, 14, 20, GREY))

TX, TY = 900, 40
over.append(word(TX, TY, 600, "a my of the names · prior or now, odd or even", "left", **small))
for r, (t, names, nums) in enumerate((("prior odd", "1, 3, 5, 7", "1, 11, 17, 23"), ("prior even", "2, 4, 6, 8", "7, 13, 19, 29"), ("now odd", "9, 11, 13, 15", "31, 41, 47, 53"), ("now even", "10, 12, 14, 16", "37, 43, 49, 59"))):
    y = TY + 36 + 30 * r
    over.append(word(TX, y, 130, t, "left", 600, 16, 24))
    over.append(word(TX + 140, y, 170, "names " + names, "left", 400, 15, 24))
    over.append(word(TX + 330, y, 200, "at " + nums, "left", 400, 15, 24, GREY))
for r, t in enumerate(("8 up · 30 on · the other-than of prior or now alone", "9 less · about 15 · the other-than of odd or even alone", "17 less · about 30 · the other-than of both")):
    over.append(word(TX, TY + 168 + 26 * r, 600, t, "left", 400, 15, 22))

over.append(word(X(30), 310, 1100, "a pair of cones, 0 to 60 · its sixteen places, the names 1 to 16, with 0 and 17", "center", **small))
over.append(word(X(37) + 16, TOP - 6, 240, "8 up · 30 on", "left", 600, 15, 22))
over.append(word(X(15) - 6, FOOT + 60, 240, "9 less · about 15", "right", 600, 15, 22))
over.append(word(X(30) + 8, FOOT + 100, 240, "17 less · about 30", "left", 600, 15, 22))
over.append(word(X(0) - 18, YC - 34, 150, "my-now-universe", "center", 400, 14, 20, GREY))
over.append(word(X(61) + 22, YC - 36, 210, "a next 1 · my next universe", "right", 400, 14, 20, GREY))
over.append(word(X(15), 846, 420, "prior · the cone opening, names 1 to 8", "center", 600, 15, 22))
over.append(word(X(45), 846, 420, "now · the cone closing, names 9 to 16", "center", 600, 15, 22))
over.append(word(X(30), 876, 900, "names 7, 8, 9 and 10, at 23, 29, 31 and 37: prior odd, prior even, now odd, now even", "center", 400, 15, 22, GREY))
over.append(word(X(30), 902, 900, "an odd name coloured, an even name dark · a name's place beside it", "center", 400, 14, 20, GREY))

title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'A my: the sixteen names on a pair of cones, 0 and 17</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A my is prior odd, then prior even, then now odd, then now even. At the stations it is four cones, and its all-parity, odd, even, odd, is one podaling, about 60.<br>'
           f'A pair of cones, 0 to 60, is sixteen places no spiral of 2, 3 or 5 crosses: in their order, the names 1 to 16. 0 is its vertex, and 17 is 61, a next 1.<br>'
           f'The living files\' three moves are the figure\'s own on them: 8 up is 30 on, 9 less a podaling about 15, and 17 less a podaling about 30.<br>'
           f'They are the three other-thans of a my\'s two, prior or now and odd or even. Names 7, 8, 9 and 10 are at 23, 29, 31 and 37, a my in its order.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A my: the sixteen names on a pair of cones, 0 and 17", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft14.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft14_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft14_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
