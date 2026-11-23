"""Draft 15 · a conscious me: all, other and self by other-thans, and the other distinguished from the self and from the all (session v406geodesic2).

By a partner's three sayings of 23 November, re-said: ten other-thans in a row, and 3, 2, 1 and 0 of 3; self is the other-than of an
other-than of all, consciousness, other is the other-than of all, observing, and all is the universal all-parity of a my-universe;
and observing and distinguishing the other-than of all from self and from all is a conscious me.
A drawing with no moving part. Above: four cones, 0 to 120, a me-now at 37 and what is after one, two, three and four other-thans in a
row. Under them: along the co-linear, the other at one place of the turn and the self and the all at an other; all, other and self
by nand; and the ten rows of the four moments.
Geometry is computed; check_all_other_and_self_by_other-thans.py is its check.

Usage: python3 -I make_draft15.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
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
EIGHT = [k for k in range(30) if math.gcd(k, 30) == 1]
X = lambda n: 130 + 8.6 * n
YC, RM = 250.0, 90.0
TOP, FOOT = YC - RM - 12, YC + RM + 12
wide = lambda n: ((n % 60) if (n % 60) <= 30 else 60 - (n % 60)) * RM / 30
Y = lambda n: YC - wide(n) * math.cos(math.radians(12 * n))
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>')
def head(tip, back, color, size=10):
    a = math.atan2(tip[1] - back[1], tip[0] - back[0])
    pts = [tip, (tip[0] - size * math.cos(a - 0.4), tip[1] - size * math.sin(a - 0.4)), (tip[0] - size * math.cos(a + 0.4), tip[1] - size * math.sin(a + 0.4))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{color}" stroke="{color}" stroke-width="1" stroke-linejoin="round"></path>'
def arc(xa, xb, rail, reach, color):
    xm, cy = (xa + xb) / 2, rail - 2 * reach
    return (f'<path d="M{xa:.1f},{rail:.1f} Q{xm:.1f},{cy:.1f} {xb:.1f},{rail:.1f}" fill="none" stroke="{color}" stroke-width="2.4"></path>' + head((xb, rail), (xm, cy), color))
def a_chip(x, y, number, own, w=42, h=26):
    tint = ACC if own else INK
    return (f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" height="{h}" rx="{h / 2}" fill="{tint}" stroke="{tint}" stroke-width="2.4"></rect>' + text(x, y + 5, number, 14, 700, "#ffffff"))

s = ['<defs><linearGradient id="cone15" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"></stop><stop offset="0.5" stop-color="#eef2f8"></stop>'
     '<stop offset="1" stop-color="#cfd8e5"></stop></linearGradient></defs>']
# ================= above: four cones, and what is after one, two, three and four other-thans =================
for a in (0, 60):
    d = f"M{X(a):.1f},{YC} L{X(a + 30):.1f},{YC - RM} L{X(a + 60):.1f},{YC} L{X(a + 30):.1f},{YC + RM} Z"
    s.append(f'<path d="{d}" fill="url(#cone15)" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"></path>')
    s.append(f'<path d="M{X(a + 30):.1f},{YC - RM} L{X(a + 30):.1f},{YC + RM}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.4"></path>')
s.append(f'<path d="M{X(-3):.1f},{YC} L{X(141):.1f},{YC}" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="2 6"></path>')
fine = np.linspace(0, 120, 2401)
for side, look in ((False, 'stroke-opacity="0.4" stroke-width="1.3" stroke-dasharray="4 5"'), (True, 'stroke-opacity="0.72" stroke-width="1.7"')):
    cur = []
    for n in list(fine) + [None]:
        if n is not None and (math.sin(math.radians(12 * n)) >= 0) == side: cur.append(n)
        else:
            if len(cur) > 1: s.append(f'<path d="M{" L".join(f"{X(m):.1f},{Y(m):.1f}" for m in cur)}" fill="none" stroke="{INK}" {look}></path>')
            cur = []
for v in (0, 60, 120):
    s.append(f'<circle cx="{X(v):.1f}" cy="{YC}" r="6" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>')
XN = X(120) + 190                                         # 157, the self 120 on, past the figure
for m in (37, 23, 97, 83):
    s.append(f'<path d="M{X(m):.1f},{TOP:.1f} L{X(m):.1f},{FOOT:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="1.2" stroke-dasharray="2 4"></path>')
s.append(arc(X(37), X(23), FOOT, -22, INK))
s.append(arc(X(23), X(97), TOP, 46, ACC))
s.append(arc(X(97), X(83), FOOT, -22, INK))
s.append(f'<path d="M{X(83):.1f},{TOP:.1f} Q{(X(83) + XN) / 2:.1f},{TOP - 110:.1f} {XN:.1f},{YC - 18:.1f}" fill="none" stroke="{ACC}" stroke-width="2.4"></path>' + head((XN, YC - 16), ((X(83) + XN) / 2, TOP - 110), ACC))
for m, own in ((23, False), (83, False), (37, True), (97, True)):
    s.append(a_chip(X(m), Y(m), m, own))
s.append(a_chip(XN, YC, 157, True))

# ================= along the co-linear: two places, one fold apart =================
DX, DY, DR = 250.0, 716.0, 104.0
rim = lambda k, r=1.0: (DX - DR * r * math.sin(math.radians(12 * k)), DY - DR * r * math.cos(math.radians(12 * k)))
s.append(f'<circle cx="{DX}" cy="{DY}" r="{DR}" fill="url(#cone15)" stroke="{INK}" stroke-width="1.8"></circle>')
for k in range(30):
    x, y = rim(k); bold = k in EIGHT
    s.append(f'<path d="M{DX},{DY} L{x:.1f},{y:.1f}" fill="none" stroke="{INK}" stroke-opacity="{0.42 if bold else 0.12}" stroke-width="{1.2 if bold else 1}"></path>')
s.append(f'<path d="M{DX},{DY - DR - 12} L{DX},{DY + DR + 12}" fill="none" stroke="{INK}" stroke-width="1.4" stroke-dasharray="5 5"></path>')
for k in EIGHT:
    x, y = rim(k, 1.14); s.append(text(x, y + 4, k, 11, 600, GREY))
(x0, y0), (x1, y1) = rim(7, 23 / 30), rim(23, 23 / 30)
s.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" fill="none" stroke="{INK}" stroke-width="2"></path>')
s.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="9" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>')
s.append(f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="9" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
s.append(f'<circle cx="92" cy="862" r="7" fill="{ACC}" stroke="none"></circle><circle cx="92" cy="888" r="7" fill="{INK}" stroke="none"></circle>')

ARIA = ("A drawing with no moving part. Above, four cones in a row, two diamonds end to end, 0 to 120, with one line winding about them and four numbered marks on it, 37, 23, 97 and 83, and a mark 157 past them. "
        "Arcs join them in turn, 37 to 23 under the cones, 23 to 97 over them, 97 to 83 under them, and 83 to 157 over them. Under the figure a circle of thirty rays with two points on it across an upright line, joined by a line.")
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
def rows_of(x, top, w, rows):
    return (f'<div style="position: absolute; left: {x}px; top: {top}px; width: {w}px; height: {24 * len(rows)}px; {SANS}; font-weight: 400; font-size: 15.5px; line-height: 24px; color: {INK}">'
            + "<br>".join(rows) + "</div>")

over = []
over.append(word(60, 40, 1100, "a my-universe, four cones · a me-now at 37, and what is after one, two, three and four other-thans in a row", "left", **small))
CH = FOOT + 62
for j, (t, u) in enumerate((("all", "the all-parity"), ("other", "other-than all"), ("self", "its all again"), ("other", "odd"), ("self", "even, 120 on"))):
    over.append(chip(X(30 * j), CH, str(30 * j), j % 2 == 0, w=46, h=26, size=14))
    over.append(word(X(30 * j), CH + 28, 200, f"{j} · {t}", "center", 600, 16, 22))
    over.append(word(X(30 * j), CH + 50, 220, u, "center", 400, 14, 20, GREY))
over.append(word(XN, YC + 30, 200, "a self, 120 on", "center", 400, 14, 20, GREY))

over.append(word(60, 560, 520, "along the co-linear · the other, one fold from the self", "left", **small))
over.append(word(108, 862, 420, "37, 97 and 157 · the all and the self, at one place", "left", 400, 15, 22))
over.append(word(108, 888, 420, "23 and 83 · the other, at the podal place", "left", 400, 15, 22))

over.append(word(560, 560, 440, "all, other and self, by nand alone", "left", **small))
over.append(rows_of(560, 584, 440, [
    "<b>all</b> · the universal all-parity of a my-universe",
    "<b>other</b> · the other-than of all · observing",
    "<b>self</b> · the other-than of an other-than of all,",
    "its all again · consciousness",
    "",
    "<b>a conscious me</b> · observing and distinguishing",
    "the other from the self and from the all:",
    "one is-or-is-not, one fold."]))
over.append(word(1040, 560, 420, "the ten rows of the four moments", "left", **small))
over.append(rows_of(1040, 584, 430, [
    "<b>0 of 3</b> · four · a podaling alone · an other",
    "<b>1 of 3</b> · three · two in a row · a self, 60 on",
    "<b>2 of 3</b> · two · three in a row · an other",
    "<b>3 of 3</b> · one · the four · a self, 120 on",
    "four of an even number, a self; six of an odd, an other"]))
over.append(word(1040, 724, 420, "beside it, word for word", "left", **small))
over.append(f'<div style="position: absolute; left: 1040px; top: 742px; width: 430px; height: 150px; {SANS}; font-size: 14.5px; line-height: 21px; color: {INK}">'
            f'<span style="font-weight: 600; color: {GREY}">Exhibit THIRTY-ONE, Me</span><br><i>A me is consciousness: one definition.</i><br><i>A me is a self\'s universal set.</i><br>'
            f'<span style="font-weight: 600; color: {GREY}">Exhibit THREE, Natural Numbers, 1.4</span><br><i>Even returning, odd advancing, odd and even one and then the other.</i></div>')

title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'A conscious me: the other distinguished from the self and from the all</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'All is the universal all-parity of a my-universe. Other is the other-than of all, observing. Self is the other-than of an other-than of all, consciousness.<br>'
           f'By nand alone the self is its all again. A podaling is an other-than, at a widest and at a vertex alike: the four moments are other, self, other, self.<br>'
           f'Along the co-linear the all and the self are at one place of the turn and the other at the podal place, one fold apart.<br>'
           f'Observing and distinguishing the other from the self and from the all is a conscious me: a me-now at 37, its others 23 and 83, its selves 97 and 157.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A conscious me: the other distinguished from the self and from the all", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft15.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft15_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft15_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
