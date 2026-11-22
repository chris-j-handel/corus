"""Build the Design-canvas artboard (Main.dc.html) for the sphere illustration.

Trirectangular spherical triangle = the octant x, y, z >= 0 of the unit sphere:
A = north pole, B and C on the equator 90 degrees of longitude apart.
Orthographic projection; geometry is exact (great-circle arcs via slerp).
"""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "illustrations", "artboards")   # the artboards and the torus body
WORK = os.environ.get("TMPDIR", "/tmp")                          # working previews, not kept

W, H = 900, 900
CX, CY, R = 450, 390, 290
AZ, EL = np.radians(45), np.radians(33)

d = np.array([np.cos(EL) * np.cos(AZ), np.cos(EL) * np.sin(AZ), np.sin(EL)])
right = np.cross([0, 0, 1], d); right /= np.linalg.norm(right)
up = np.cross(d, right)

INK = "#1f2430"
GRID = "#7b8494"
ACC = "@@ACCENT@@"          # replaced by the {{accent}} hole
DEFAULT_ACCENT = "#c2410c"


def proj(p):
    p = np.asarray(p, float)
    return CX + R * p @ right, CY - R * p @ up


def vis(p):
    return np.asarray(p, float) @ d >= 0


def slerp(a, b, n=60):
    om = np.arccos(np.clip(a @ b, -1, 1))
    t = np.linspace(0, 1, n)
    return (np.sin((1 - t) * om)[:, None] * a + np.sin(t * om)[:, None] * b) / np.sin(om)


def pd(pts, close=False):
    xy = [proj(p) for p in pts]
    s = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in xy)
    return s + (" Z" if close else "")


def split_visible(pts):
    front, back, cur, cv = [], [], [], None
    for p in pts:
        v = vis(p)
        if cv is None or v == cv:
            cur.append(p)
        else:
            cur.append(p)
            (front if cv else back).append(cur)
            cur = [p]
        cv = v
    if len(cur) > 1:
        (front if cv else back).append(cur)
    return front, back


def latitude(lat, n=181):
    t = np.linspace(0, 2 * np.pi, n); c = np.cos(lat)
    return np.stack([c * np.cos(t), c * np.sin(t), np.full_like(t, np.sin(lat))], 1)


def meridian(lon, n=91):
    t = np.linspace(-np.pi / 2, np.pi / 2, n)
    return np.stack([np.cos(t) * np.cos(lon), np.cos(t) * np.sin(lon), np.sin(t)], 1)


def paths(ds, attrs):
    return "".join(f'<path d="{x}"{attrs}></path>' for x in ds)


s = []
s.append(f'''<defs>
<radialGradient id="ball" cx="{CX - 0.38 * R:.0f}" cy="{CY - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop>
</radialGradient>
<radialGradient id="floor" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#1f2430" stop-opacity="0.2"></stop><stop offset="1" stop-color="#1f2430" stop-opacity="0"></stop>
</radialGradient>
</defs>''')
s.append(f'<ellipse cx="{CX}" cy="{CY + R + 34}" rx="{R * 0.85:.0f}" ry="{R * 0.11:.0f}" fill="url(#floor)"></ellipse>')
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#ball)"></circle>')

# graticule every 30 degrees, front hemisphere only
grid = []
for lat in (-60, -30, 30, 60):
    grid += [pd(r) for r in split_visible(latitude(np.radians(lat)))[0]]
for lon in range(0, 360, 30):
    grid += [pd(r) for r in split_visible(meridian(np.radians(lon)))[0]]
s.append(f'<g fill="none" stroke="{GRID}" stroke-width="1" stroke-opacity="0.35">{paths(grid, "")}</g>')

# equator: hidden half dashed, visible half solid
fe, be = split_visible(latitude(0))
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.28" stroke-width="1.2" stroke-dasharray="5 6">{paths([pd(r) for r in be], "")}</g>')
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.5">{paths([pd(r) for r in fe], "")}</g>')
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"></circle>')

# the triangle
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
edges = [slerp(A, B), slerp(B, C), slerp(C, A)]
boundary = np.concatenate([edges[0], edges[1][1:], edges[2][1:]])
s.append(f'<path d="{pd(boundary, True)}" fill="{ACC}" fill-opacity="0.26" stroke="none"></path>')
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{paths([pd(e) for e in edges], "")}</g>')

# right-angle marks: small spherical squares in each corner
SQ = 0.17
corners = ((A, B, C), (B, C, A), (C, A, B))
marks, tag_xy = [], []
for V, P, Q in corners:
    t1 = P - (P @ V) * V; t1 /= np.linalg.norm(t1)
    t2 = Q - (Q @ V) * V; t2 /= np.linalg.norm(t2)
    p1, p2, p3 = V + SQ * t1, V + SQ * (t1 + t2), V + SQ * t2
    seg = np.concatenate([np.linspace(p1, p2, 12), np.linspace(p2, p3, 12)[1:]])
    seg /= np.linalg.norm(seg, axis=1)[:, None]
    marks.append(pd(seg))
    m = V + 0.36 * (t1 + t2) / np.sqrt(2); m /= np.linalg.norm(m)
    tag_xy.append(proj(m))
s.append(f'<g fill="none" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round">{paths(marks, "")}</g>')

vert_xy = [proj(V) for V in (A, B, C)]
for x, y in vert_xy:
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')

svg = (f'<svg role="img" aria-label="A sphere with a shaded triangle whose corners are the north pole and two points on the equator a quarter-turn apart; every corner is a right angle." '
       f'width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>")
svg = svg.replace(ACC, "{{accent}}")

# ---- HTML text overlays (retypable on the canvas)
def box(cx, cy, w, h, style, text):
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; '
            f'line-height: {h}px; text-align: center; {style}">{text}</div>')

VSTYLE = f"font-family: 'STIX Two Text', Georgia, serif; font-style: italic; font-weight: 500; font-size: 32px; color: {INK}"
TSTYLE = f"font-family: Inter, system-ui, sans-serif; font-weight: 600; font-size: 18px; color: {INK}"
offsets = [(0, -26), (-28, 22), (28, 22)]
labels = [box(x + ox, y + oy, 40, 40, VSTYLE, n) for (x, y), (ox, oy), n in zip(vert_xy, offsets, "ABC")]
tags = [box(x, y, 48, 24, TSTYLE, "90°") for x, y in tag_xy]

title = (f'<div style="position: absolute; left: 64px; top: 766px; width: 772px; text-align: center; '
         f'font-family: Inter, system-ui, sans-serif; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'A geodesic triangle with three right angles</div>')
caption = (f'<div style="position: absolute; left: 64px; top: 814px; width: 772px; text-align: center; '
           f'font-family: Inter, system-ui, sans-serif; font-weight: 400; font-size: 19px; line-height: 28px; color: #4a5160">'
           f'90° + 90° + 90° = 270° · it covers exactly 1/8 of the sphere</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT,
                    "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Sphere with a three-right-angle triangle</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&amp;family=STIX+Two+Text:ital,wght@1,500&amp;display=swap">
<style>
body{{margin:0}}
a{{color:#1d4ed8}}a:hover{{color:#1e3a8a}}
</style>
</helmet>
<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; font-family: Inter, system-ui, sans-serif; color: {INK}">
{svg}
{"".join(labels)}
{"".join(tags)}
{title}
{caption}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props, ensure_ascii=False)}'>
class Component extends DCLogic {{
renderVals() {{
return {{ accent: this.props.accent ?? '{DEFAULT_ACCENT}' }};
}}
}}
</script>
</body>
</html>
'''

root = OUT
os.makedirs(root, exist_ok=True)
open(f"{root}/Main.dc.html", "w").write(html)

# preview copy with the default accent filled in, for a local render
open(os.path.join(WORK, "preview.svg"), "w").write(
    svg.replace("{{accent}}", DEFAULT_ACCENT).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1))
print(len(html), "bytes")
