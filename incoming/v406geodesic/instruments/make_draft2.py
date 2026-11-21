"""Draft 2: bi-folding the three-right-angle triangle.

Two folds, across the equator edge and then across the meridian edge AB, are a half-turn
about the axis through B and the centre: the triangle +++ turns onto +--, with no mirror.
"""
import json, os
import numpy as np
import sys as _sys
_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # geom.py beside this file, also under python3 -I
from geom import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "illustrations", "artboards")   # the artboards and the torus body
WORK = os.environ.get("TMPDIR", "/tmp")                          # working previews, not kept

W, H = 900, 900
cam = Cam(az_deg=17, el_deg=16, cx=450, cy=390, scale=290)
R = cam.s
vis = lambda p: cam.depth(p) >= 0

A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
S_ = -A; Cn = -C           # the bi-folded vertices A' (south pole) and C'

s = []
s.append(f'''<defs>
<radialGradient id="ball2" cx="{cam.cx - 0.38 * R:.0f}" cy="{cam.cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop>
</radialGradient>
<radialGradient id="floor2" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#1f2430" stop-opacity="0.2"></stop><stop offset="1" stop-color="#1f2430" stop-opacity="0"></stop>
</radialGradient>
</defs>''')
s.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 34}" rx="{R * 0.85:.0f}" ry="{R * 0.11:.0f}" fill="url(#floor2)"></ellipse>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball2)"></circle>')

# faint graticule, front only
grid = []
for lat in (-60, -30, 30, 60):
    pts = latitude(np.radians(lat)); grid += [cam.path(r) for r in runs(pts, [vis(p) for p in pts])[0]]
for lon in range(0, 360, 30):
    if lon in (0, 90, 180, 270):
        continue
    pts = meridian(np.radians(lon)); grid += [cam.path(r) for r in runs(pts, [vis(p) for p in pts])[0]]
s.append(f'<g fill="none" stroke="{GRID}" stroke-width="1" stroke-opacity="0.3">{paths(grid)}</g>')

# the three great circles that cut the sphere into its eight right-angle triangles
front, back = [], []
for nrm in ((0, 0, 1), (0, 1, 0), (1, 0, 0)):
    pts = great_circle(nrm, 721)
    f, b = runs(pts, [vis(p) for p in pts]); front += f; back += b
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.26" stroke-width="1.2" stroke-dasharray="5 6">{paths([cam.path(r) for r in back])}</g>')
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.4">{paths([cam.path(r) for r in front])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"></circle>')


def tri_fill_and_edges(P, Q, Rr, fill_op, edge_w, dashed_front=False):
    edges = [slerp(P, Q), slerp(Q, Rr), slerp(Rr, P)]
    boundary = np.concatenate([edges[0], edges[1][1:], edges[2][1:]])
    out = []
    if fill_op:
        # fill only the visible part: clip the boundary to the front hemisphere by pushing hidden points to the limb
        bp = []
        for p in boundary:
            if vis(p):
                bp.append(p)
            else:
                q = p - cam.depth(p) * cam.d; bp.append(q / np.linalg.norm(q))
        out.append(f'<path d="{cam.path(bp, True)}" fill="{ACC}" fill-opacity="{fill_op}" stroke="none"></path>')
    f, b = [], []
    for e in edges:
        ff, bb = runs(e, [vis(p) for p in e]); f += ff; b += bb
    dash = ' stroke-dasharray="9 7"' if dashed_front else ''
    out.append(f'<g fill="none" stroke="{ACC}" stroke-width="{edge_w}" stroke-linecap="round" stroke-linejoin="round"{dash}>{paths([cam.path(r) for r in f])}</g>')
    if b:
        out.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.45" stroke-width="2" stroke-dasharray="4 6">{paths([cam.path(r) for r in b])}</g>')
    return out


# one fold alone, across the equator edge: a mirror image (dashed, no fill)
s += tri_fill_and_edges(np.array([0, 0, -1.0]), B, C, 0.09, 2.2, dashed_front=True)
# the triangle, and the triangle bi-folded onto +--
s += tri_fill_and_edges(A, B, C, 0.28, 4)
s += tri_fill_and_edges(S_, B, Cn, 0.28, 4)

# right-angle marks: visible corners of both triangles
marks = []
for V, P, Q in ((A, B, C), (B, C, A), (C, A, B), (B, Cn, S_), (S_, B, Cn), (Cn, S_, B)):
    seg = right_angle_mark(cam, V, P, Q)
    if all(vis(p) for p in seg):
        marks.append(cam.path(seg))
s.append(f'<g fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round">{paths(marks)}</g>')

# the half-turn: an arc round B on the sphere, from the +++ quarter to the +-- quarter
rho = 0.34
psi = np.radians(np.linspace(52, 218, 80))   # angle about the x axis, measured from +y towards +z
arc = np.stack([np.full_like(psi, np.cos(rho)), np.sin(rho) * np.cos(psi), np.sin(rho) * np.sin(psi)], 1)
s.append(f'<path d="{cam.path(arc)}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
(x1, y1), (x0, y0) = cam.proj(arc[-1]), cam.proj(arc[-4])
ang = np.arctan2(y1 - y0, x1 - x0)
head = [(x1 + 13 * np.cos(ang), y1 + 13 * np.sin(ang)),
        (x1 + 7 * np.cos(ang + 2.4), y1 + 7 * np.sin(ang + 2.4)),
        (x1 + 7 * np.cos(ang - 2.4), y1 + 7 * np.sin(ang - 2.4))]
s.append(f'<path d="M{head[0][0]:.1f},{head[0][1]:.1f} L{head[1][0]:.1f},{head[1][1]:.1f} L{head[2][0]:.1f},{head[2][1]:.1f} Z" fill="{INK}"></path>')

# vertex dots
verts = {"A": A, "B": B, "C": C, "A′": S_, "C′": Cn}
for name, V in verts.items():
    if vis(V) or name in ("A′", "C′"):
        x, y = cam.proj(V)
        if vis(V):
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
        else:   # behind the sphere: hollow
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#ffffff" fill-opacity="0.6" stroke="{ACC}" stroke-width="2" stroke-dasharray="3 2"></circle>')

svg = (f'<svg role="img" aria-label="The sphere seen nearly along the axis through B. The triangle A B C, all right angles, and its image after two folds, '
       f'turned half way round B onto the opposite quarter below and to the left; one fold alone gives a dashed mirror image." '
       f'width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

# ---- text overlays
def at(V, dx, dy):
    x, y = cam.proj(V); return x + dx, y + dy

labels = []
for name, V, (dx, dy) in (("A", A, (0, -30)), ("B", B, (24, -22)), ("C", C, (26, 0)),
                          ("A′", S_, (0, 26)), ("C′", Cn, (-30, 0))):
    x, y = at(V, dx, dy)
    labels.append(html_box(x, y, 48, 40, VSTYLE, name))

SIGN = f"font-family: Inter, system-ui, sans-serif; font-weight: 600; font-size: 22px; letter-spacing: 2px; color: {INK}"
def centroid(P, Q, Rr):
    c = P + Q + Rr; return c / np.linalg.norm(c)
for (P, Q, Rr), txt in (((A, B, C), "+ + +"), ((S_, B, Cn), "+ − −")):
    x, y = cam.proj(centroid(P, Q, Rr))
    labels.append(html_box(x, y, 90, 30, SIGN, txt))

NOTE = f"font-family: Inter, system-ui, sans-serif; font-weight: 400; font-size: 16px; color: #4a5160"
x, y = cam.proj(centroid(np.array([0, 0, -1.0]), B, C))
labels.append(html_box(x + 12, y + 8, 150, 22, NOTE, "one fold: a mirror"))
xa, ya = cam.proj(arc[len(arc) // 2])
labels.append(html_box(xa - 40, ya - 52, 180, 22, NOTE, "two folds: a half-turn"))

title = (f'<div style="position: absolute; left: 64px; top: 766px; width: 772px; text-align: center; '
         f'font-family: Inter, system-ui, sans-serif; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'Bi-folding the triangle</div>')
caption = (f'<div style="position: absolute; left: 64px; top: 814px; width: 772px; text-align: center; '
           f'font-family: Inter, system-ui, sans-serif; font-weight: 400; font-size: 19px; line-height: 28px; color: #4a5160">'
           f'Two folds on edges at right angles are a half-turn about B: no mirror.<br>+ + + turns onto + − −, as 17 less carries name 1 onto name 16.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT,
                    "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
html = page("Bi-folding the triangle", W, H, svg + "\n" + "".join(labels) + "\n" + title + "\n" + caption,
            json.dumps(props, ensure_ascii=False))
root = OUT
os.makedirs(root, exist_ok=True)
open(f"{root}/Draft2.dc.html", "w").write(html)
open(os.path.join(WORK, "preview2.svg"), "w").write(
    svg.replace("{{accent}}", DEFAULT_ACCENT).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1))
# a rough preview of the labels' places, for drafting only
pv = open(os.path.join(WORK, "preview2.svg")).read().replace("</svg>", "")
import re
for m in re.finditer(r'left: (\d+)px; top: (\d+)px; width: (\d+)px; height: (\d+)px;[^>]*>([^<]*)</div>', "".join(labels)):
    l, t, w, h, txt = m.groups()
    pv += f'<text x="{int(l) + int(w) / 2}" y="{int(t) + int(h) / 2 + 6}" font-size="18" text-anchor="middle" font-family="sans-serif" fill="#000">{txt}</text>'
open(os.path.join(WORK, "preview2_labels.svg"), "w").write(pv + "</svg>")
print(len(html), "bytes")
