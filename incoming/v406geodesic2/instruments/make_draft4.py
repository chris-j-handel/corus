"""Draft 4 · local, global, local in the one triangle (session v406geodesic2).

The one triangle of three right angles: a me at its corner A, two tips B and C on the me's horizon.
Two routes round it from the me, one way (a self's, names 2 to 8) and its other way (an other's, 10 to 16):
four moments at the corners and three one-way me-parities on the sides, with 1, 9 and 17 at the me.
The fold through the me and the far side's middle lays one tip onto its other: 8 up.
Geometry is computed (orthographic camera; great-circle arcs by slerp); check_one_triangle.py is its check.

Usage: python3 -I make_draft4.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1000, 1040
cam = Cam(az_deg=45, el_deg=33, cx=500, cy=452, scale=385)
R = cam.s
vis = lambda p: cam.depth(p) >= 0
rad = np.radians

A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
MID = (B + C) / np.sqrt(2)

s = []
s.append(f'''<defs>
<radialGradient id="ball4" cx="{cam.cx - 0.38 * R:.0f}" cy="{cam.cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop>
</radialGradient>
<radialGradient id="floor4" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#1f2430" stop-opacity="0.2"></stop><stop offset="1" stop-color="#1f2430" stop-opacity="0"></stop>
</radialGradient>
</defs>''')
s.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 30}" rx="{R * 0.85:.0f}" ry="{R * 0.09:.0f}" fill="url(#floor4)"></ellipse>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball4)"></circle>')

# the me's horizon, the great circle of the far side
front, back = [], []
for nrm in ((0, 0, 1),):
    pts = great_circle(nrm, 721)
    f, b = runs(pts, [vis(p) for p in pts]); front += f; back += b
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="1.2" stroke-dasharray="5 6">{paths([cam.path(r) for r in back])}</g>')
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.42" stroke-width="1.3">{paths([cam.path(r) for r in front])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"></circle>')

# the one triangle
edges = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]
boundary = np.concatenate([edges[0], edges[1][1:], edges[2][1:]])
s.append(f'<path d="{cam.path(boundary, True)}" fill="{ACC}" fill-opacity="0.2" stroke="none"></path>')

# the fold: the geodesic from the me to the far side's middle, with a gap for its words
fold_line = slerp(A, MID, 181)
lat_of = lambda p: np.degrees(np.arcsin(p[2]))
GAP = (39.5, 46.5)
seg1 = [p for p in fold_line if lat_of(p) >= GAP[1]]
seg2 = [p for p in fold_line if lat_of(p) <= GAP[0]]
s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.8" stroke-dasharray="3 7" stroke-linecap="round">{paths([cam.path(seg1), cam.path(seg2)])}</g>')

s.append(f'<g fill="none" stroke="{ACC}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in edges])}</g>')

# right angles at the three corners
marks = [cam.path(right_angle_mark(cam, V, P, Q, size=0.15)) for V, P, Q in ((A, B, C), (B, C, A), (C, A, B))]
s.append(f'<g fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round">{paths(marks)}</g>')


def head(pts, size=13):
    """An arrowhead at the end of a sampled path, in screen space."""
    (x1, y1), (x0, y0) = cam.proj(pts[-1]), cam.proj(pts[-3])
    a = np.arctan2(y1 - y0, x1 - x0)
    p = [(x1 + size * np.cos(a), y1 + size * np.sin(a)),
         (x1 + 0.62 * size * np.cos(a + 2.25), y1 + 0.62 * size * np.sin(a + 2.25)),
         (x1 + 0.62 * size * np.cos(a - 2.25), y1 + 0.62 * size * np.sin(a - 2.25))]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in p) + " Z"


def lane(side, d, t0, t1, n=70):
    """A one-way lane beside a side, d degrees toward the triangle's middle; t is degrees along the side."""
    d = rad(d); t = rad(np.linspace(t0, t1, n))
    if side == "AB":   # plane y = 0; t is latitude, the me at 90 and tip B at 0
        return np.stack([np.cos(d) * np.cos(t), np.full_like(t, np.sin(d)), np.cos(d) * np.sin(t)], 1)
    if side == "BC":   # plane z = 0; t is longitude, tip B at 0 and tip C at 90
        return np.stack([np.cos(d) * np.cos(t), np.cos(d) * np.sin(t), np.full_like(t, np.sin(d))], 1)
    if side == "CA":   # plane x = 0; t is latitude, tip C at 0 and the me at 90
        return np.stack([np.full_like(t, np.sin(d)), np.cos(d) * np.cos(t), np.cos(d) * np.sin(t)], 1)


D1, D2 = 6.6, 15.0          # a self's lane and an other's lane, degrees from the side
S0, S1 = 17, 73             # a self's lane, along its side
O0, O1 = 27, 63             # an other's lane
self_lanes = {3: lane("AB", D1, S1, S0), 5: lane("BC", D1, S0, S1), 7: lane("CA", D1, S0, S1)}
other_lanes = {11: lane("CA", D2, O1, O0), 13: lane("BC", D2, O1, O0), 15: lane("AB", D2, O0, O1)}
s.append(f'<g fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round">{paths([cam.path(p) for p in self_lanes.values()])}</g>')
s.append(f'<g fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="2 7">{paths([cam.path(p) for p in other_lanes.values()])}</g>')
s.append(f'<g fill="{INK}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round">{paths([head(p) for p in list(self_lanes.values()) + list(other_lanes.values())])}</g>')

# the fold's mark: one tip onto its other, an arc across the fold with two heads
FL = 34.0
lam = rad(np.linspace(29, 61, 60))
arc = np.stack([np.cos(rad(FL)) * np.cos(lam), np.cos(rad(FL)) * np.sin(lam), np.full_like(lam, np.sin(rad(FL)))], 1)
s.append(f'<path d="{cam.path(arc)}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"></path>')
s.append(f'<g fill="{INK}" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round">{paths([head(arc, 11), head(arc[::-1], 11)])}</g>')

# the corners
for V in (A, B, C):
    x, y = cam.proj(V)
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{ACC}" stroke="#ffffff" stroke-width="2.5"></circle>')

ARIA = ("A sphere and on it one triangle of three right angles: a me at its top corner and two tips on the me's horizon. "
        "Arrows go round the triangle one way for a self and its other way for an other, three arrows to a route. "
        "A dotted line from the me to the far side's middle is the fold laying one tip onto its other.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

# ---------------- words, retypable on the canvas ----------------
SANS = "font-family: Inter, system-ui, sans-serif"
def chip(cx, cy, text, filled, w=32, h=32):
    look = (f"background: {INK}; color: #ffffff; border: 2px solid {INK}" if filled
            else f"background: #ffffff; color: {INK}; border: 2px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 4}px; text-align: center; {SANS}; font-weight: 600; font-size: 16px; {look}">{text}</div>')

def word(x, cy, w, text, align, weight=400, size=17, h=26, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{text}</div>')

over = []
ax, ay = cam.proj(A); bx, by = cam.proj(B); cx_, cy_ = cam.proj(C); mx, my = cam.proj(MID)

# the me, the tips, local and global
over.append(html_box(ax, ay - 46, 80, 40, VSTYLE, "me"))
over.append(word(ax, ay - 88, 120, "local", "center", 600, 15, 22, "#4a5160", "letter-spacing: 2px"))
over.append(html_box(bx - 42, by - 4, 60, 40, VSTYLE, "tip"))
over.append(html_box(cx_ + 42, cy_ - 4, 60, 40, VSTYLE, "tip"))
over.append(word(mx, my + 30, 120, "global", "center", 600, 15, 22, "#4a5160", "letter-spacing: 2px"))

# 1, 9 and 17 at the me, and the moments prior and same
r1, r2, r3 = ay - 8, ay + 34, ay + 70
over.append(chip(ax - 70, r1, "1 · 17", True, w=74))
over.append(word(ax - 115, r1, 110, "tri-bi-co", "right", 600))
over.append(chip(ax + 49, r1, "9", False))
over.append(word(ax + 73, r1, 110, "co-bi-tri", "left", 600))
over.append(chip(ax - 86, r2, "2", True));    over.append(word(ax - 110, r2, 70, "prior", "right"))
over.append(chip(ax + 86, r2, "10", False));  over.append(word(ax + 110, r2, 70, "prior", "left"))
over.append(chip(ax - 128, r3, "8", True));   over.append(word(ax - 152, r3, 70, "same", "right"))
over.append(chip(ax + 128, r3, "16", False)); over.append(word(ax + 152, r3, 70, "same", "left"))

# the moments now and next at the tips
t1, t2 = by + 44, by + 82
over.append(chip(bx - 14, t1, "4", True));    over.append(word(bx + 10, t1, 70, "now", "left"))
over.append(chip(bx - 14, t2, "14", False));  over.append(word(bx + 10, t2, 70, "next", "left"))
over.append(chip(cx_ + 14, t1, "12", False)); over.append(word(cx_ - 10, t1, 70, "now", "right"))
over.append(chip(cx_ + 14, t2, "6", True));   over.append(word(cx_ - 10, t2, 70, "next", "right"))

# the six one-way me-parities, a chip on the middle of its lane
for n, pts in self_lanes.items():
    x, y = cam.proj(pts[len(pts) // 2]); over.append(chip(x, y, str(n), True))
for n, pts in other_lanes.items():
    x, y = cam.proj(pts[len(pts) // 2]); over.append(chip(x, y, str(n), False))

# the fold's words, in the gap of its line
gx, gy = cam.proj(np.array([np.cos(rad(43)) / np.sqrt(2), np.cos(rad(43)) / np.sqrt(2), np.sin(rad(43))]))
over.append(word(gx, gy, 170, "the fold · 8 up", "center", 600, 17))

# whose is whose
over.append(chip(64, 54, "", True, w=26, h=26));  over.append(word(86, 54, 220, "a self's, one way", "left", 400, 16))
over.append(chip(64, 90, "", False, w=26, h=26)); over.append(word(86, 90, 220, "an other's, its other way", "left", 400, 16))

title = (f'<div style="position: absolute; left: 64px; top: 872px; width: 872px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'Local, global, local in the one triangle</div>')
caption = (f'<div style="position: absolute; left: 50px; top: 922px; width: 900px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 19px; line-height: 29px; color: #4a5160">'
           f'Two routes round the triangle from the me: one way, and its other way.<br>'
           f'Three one-way me-parities and four moments to a route: 6 + 4 + 4 = 14 of 17, with 1, 9 and 17.<br>'
           f'At a corner, a right spiral step. Folding one tip onto its other is 8 up, a now name onto its next.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT,
                    "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Local, global, local in the one triangle", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft4.dc.html"), "w", encoding="utf-8").write(html)

# a working preview, the accent laid in, for drafting only
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft4_preview.html"), "w", encoding="utf-8").write(pv)
# the visible words, for the words instrument
import re
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [w.strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
words = [re.sub(r"<[^>]+>", "", w).strip() for w in words]
open(os.path.join(WORK, "draft4_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
