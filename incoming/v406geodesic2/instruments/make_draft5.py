"""Draft 5 · the co-linear of the bi-folding, and its two cones (session v406geodesic2).

From the second drawing: its two folds' great circles cross at two opposite intersections, at its far side and at its own side.
The line through the two, through the sphere's 0, is the co-linear. Four quarter spheres go from the far side to the own
about it, in turn of one hand and of its other, and all eight triangles are with it. A cone of a right angle
from the far intersection and one from the own side's cross in the circle between the two.
One figure, drawn twice: across the co-linear, and along it from its own side.
Geometry is computed; check_the_co-linear_and_its_two_cones.py is its check.

Usage: python3 -I make_draft5.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1200, 1000
SLATE = "#475569"
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
OWN, FAR, O = B, -B, np.zeros(3)
across = Cam(az_deg=68, el_deg=20, cx=345, cy=400, scale=270)      # seen across the co-linear
along = Cam(az_deg=0, el_deg=0, cx=965, cy=400, scale=200)          # seen along it, from its own side: C at its right, A above


def visible_part(cam, corners):
    """A triangle's part facing the viewer: its boundary sampled, its hidden runs set on the sphere's edge."""
    ring = np.concatenate([slerp(corners[i], corners[(i + 1) % 3], 48)[:-1] for i in range(3)])
    keep = [cam.depth(p) >= -1e-12 for p in ring]
    if not any(keep): return None
    if all(keep): return ring
    out, n = [], len(ring)
    for i in range(n):
        p, q = ring[i], ring[(i + 1) % n]
        if keep[i]: out.append(p)
        if keep[i] != keep[(i + 1) % n]:
            t = cam.depth(p) / (cam.depth(p) - cam.depth(q))
            x = p + t * (q - p); x = x - (x @ cam.d) * cam.d; out.append(x / np.linalg.norm(x))
    filled = []
    for i, p in enumerate(out):
        filled.append(p); q = out[(i + 1) % len(out)]
        if abs(cam.depth(p)) < 1e-9 and abs(cam.depth(q)) < 1e-9 and 1e-6 < np.linalg.norm(p - q) < 1.999:
            filled.extend(slerp(p, q, 24)[1:-1])
    return np.array(filled)


def ball(cam, key):
    R = cam.s
    return (f'<radialGradient id="ball5{key}" cx="{cam.cx - 0.38 * R:.0f}" cy="{cam.cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop></radialGradient>')


def quarters(cam):
    """The four quarter spheres between the two folds' circles, of one hand and of its other in turn."""
    out = []
    for sy in (1, -1):
        for sz in (1, -1):
            col, op = (ACC, 0.22) if sy * sz > 0 else (SLATE, 0.18)
            for sx in (1, -1):
                part = visible_part(cam, [sx * B, sy * C, sz * A])
                if part is not None and len(part) > 2:
                    out.append(f'<path d="{cam.path(part, True)}" fill="{col}" fill-opacity="{op}" stroke="none"></path>')
    return "".join(out)


def circles(cam, which):
    out = []
    for nrm, w in which:
        pts = great_circle(nrm, 721)
        f, b = runs(pts, [cam.depth(p) >= 0 for p in pts])
        out.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.28" stroke-width="{w * 0.7:.1f}" stroke-dasharray="5 6">{paths([cam.path(r) for r in b])}</g>')
        out.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.66" stroke-width="{w}">{paths([cam.path(r) for r in f])}</g>')
    return "".join(out)


def hull(points):
    pts = sorted(map(tuple, points))
    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 0: h.pop()
            h.append(p)
        return h
    lo, up = half(pts), half(list(reversed(pts)))
    return lo[:-1] + up[:-1]


def cone(cam, apex, dash):
    """A cone of a right angle at its vertex, to the circle between the two intersections."""
    ring_xy = [cam.proj(np.array([0, np.cos(t), np.sin(t)])) for t in np.linspace(0, 2 * np.pi, 361)]
    ax = cam.proj(apex)
    h = hull(ring_xy + [ax])
    i = min(range(len(h)), key=lambda k: (h[k][0] - ax[0]) ** 2 + (h[k][1] - ax[1]) ** 2)
    t1, t2 = h[i - 1], h[(i + 1) % len(h)]
    d_fill = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in h) + " Z"
    d_line = f"M{t1[0]:.1f},{t1[1]:.1f} L{ax[0]:.1f},{ax[1]:.1f} L{t2[0]:.1f},{t2[1]:.1f}"
    return (f'<path d="{d_fill}" fill="{INK}" fill-opacity="0.07" stroke="none"></path>'
            f'<path d="{d_line}" fill="none" stroke="{INK}" stroke-opacity="0.85" stroke-width="1.8" stroke-linejoin="round"{dash}></path>')


def dot(cam, V, kind):
    x, y = cam.proj(V)
    if kind == "own":   return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{ACC}" stroke="#ffffff" stroke-width="2.5"></circle>'
    if kind == "far":    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="#ffffff" fill-opacity="0.9" stroke="{INK}" stroke-width="2.2" stroke-dasharray="3 3"></circle>'
    if kind == "nought": return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#ffffff" fill-opacity="0.95" stroke="{INK}" stroke-width="2"></circle>'
    if kind == "front":  return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>'
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#ffffff" fill-opacity="0.7" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.6"></circle>'


def arrow_head(p1, p0, size=14):
    a = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [(p1[0] + size * np.cos(a), p1[1] + size * np.sin(a)),
           (p1[0] + 0.6 * size * np.cos(a + 2.25), p1[1] + 0.6 * size * np.sin(a + 2.25)),
           (p1[0] + 0.6 * size * np.cos(a - 2.25), p1[1] + 0.6 * size * np.sin(a - 2.25))]
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{INK}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"></path>'


s = ['<defs>' + ball(across, "a") + ball(along, "b") +
     '<radialGradient id="floor5" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#1f2430" stop-opacity="0.2"></stop><stop offset="1" stop-color="#1f2430" stop-opacity="0"></stop></radialGradient></defs>']

# ================= across the co-linear =================
cam = across; R = cam.s
s.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 26}" rx="{R * 0.85:.0f}" ry="{R * 0.09:.0f}" fill="url(#floor5)"></ellipse>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball5a)"></circle>')
s.append(quarters(cam))
s.append(circles(cam, (((0, 1, 0), 2.0), ((0, 0, 1), 2.0), ((1, 0, 0), 1.4))))
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"></circle>')
s.append(cone(cam, FAR, ' stroke-dasharray="6 5"'))
s.append(cone(cam, OWN, ''))
T0 = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in T0])}</g>')
P = lambda t: cam.proj(t * B)
seg = lambda t0, t1: f"M{P(t0)[0]:.1f},{P(t0)[1]:.1f} L{P(t1)[0]:.1f},{P(t1)[1]:.1f}"
edge = 1.0 / np.hypot(B @ cam.right, B @ cam.up)
REACH = 1.27
s.append(f'<path d="{seg(1.0, REACH)}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(f'<path d="{seg(-1.0, 1.0)}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-dasharray="2 7" stroke-linecap="round"></path>')
s.append(f'<path d="{seg(-REACH, -max(edge, 1.0))}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(arrow_head(P(REACH), P(REACH - 0.1)))
for V, k in ((A, "front"), (C, "front"), (-A, "back"), (-C, "back"), (FAR, "far"), (O, "nought"), (OWN, "own")):
    s.append(dot(cam, V, k))

# ================= along the co-linear, from its own side =================
cam = along; R = cam.s
s.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 24}" rx="{R * 0.85:.0f}" ry="{R * 0.09:.0f}" fill="url(#floor5)"></ellipse>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball5b)"></circle>')
for sy in (1, -1):
    for sz in (1, -1):
        col, op = (ACC, 0.22) if sy * sz > 0 else (SLATE, 0.18)
        ex, ey = cam.cx + sy * R, cam.cy - sz * R
        sweep = 0 if sy * sz > 0 else 1
        s.append(f'<path d="M{cam.cx},{cam.cy} L{ex},{cam.cy} A{R},{R} 0 0 {sweep} {cam.cx},{ey} Z" fill="{col}" fill-opacity="{op}" stroke="none"></path>')
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.66" stroke-width="2">'
         f'<path d="M{cam.cx - R},{cam.cy} L{cam.cx + R},{cam.cy}"></path><path d="M{cam.cx},{cam.cy - R} L{cam.cx},{cam.cy + R}"></path></g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"></circle>')
s.append(f'<path d="M{cam.cx},{cam.cy - R} L{cam.cx},{cam.cy} L{cam.cx + R},{cam.cy} A{R},{R} 0 0 0 {cam.cx},{cam.cy - R} Z" fill="none" stroke="{ACC}" stroke-width="4" stroke-linejoin="round"></path>')
# a step round the co-linear, from a quarter to its next: four of them, the one way
for k in range(4):
    mid = np.radians(90 + 90 * k)                      # over the fold between a quarter and its next
    ts = np.linspace(mid - np.radians(13), mid + np.radians(13), 24)
    rr = 0.82 * R
    pts = [(cam.cx + rr * np.cos(t), cam.cy - rr * np.sin(t)) for t in ts]
    s.append(f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"></path>')
    s.append(arrow_head(pts[-1], pts[-3], 10))
for V, k in ((A, "front"), (C, "front"), (-A, "front"), (-C, "front"), (OWN, "own")):
    s.append(dot(cam, V, k))

ARIA = ("One figure drawn twice. Across: a sphere with three great circles, a line through its centre and two opposite intersections of the circles, "
        "one at its far side, behind the sphere, and one at its own side, before it, and two cones, their vertices at those two intersections, facing one another and crossing in the circle between. "
        "Along the line, from its own side: a disc of four quarters about its centre, tinted two and two in turn, and four arrows going round.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

# ---------------- words, retypable on the canvas ----------------
SANS = "font-family: Inter, system-ui, sans-serif"
def chip(cx, cy, text, filled, w=38, h=30):
    look = (f"background: {INK}; color: #ffffff; border: 2px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 2px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 4}px; text-align: center; {SANS}; font-weight: 600; font-size: 15px; {look}">{text}</div>')
def word(x, cy, w, text, align, weight=400, size=17, h=24, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{text}</div>')

over = []
cam = across
nx, ny = cam.proj(OWN); fx, fy = cam.proj(FAR); ox, oy = cam.proj(O); ax_, ay_ = cam.proj(A); cx_, cy_ = cam.proj(C)
over.append(html_box(ax_, ay_ - 28, 40, 40, VSTYLE, "A"))
over.append(html_box(cx_ + 24, cy_ + 20, 40, 40, VSTYLE, "C"))
over.append(html_box(nx + 12, ny - 34, 40, 40, VSTYLE, "B"))
over.append(chip(nx + 50, ny + 34, "own side · 25", True, w=128))
over.append(chip(fx - 40, fy - 36, "far side · 23", False, w=118))
over.append(chip(ox, oy - 34, "24 · a 0", False, w=88))
over.append(word(nx + 112, ny - 52, 200, "co-recursioning", "center", 600, 16, 22))
over.append(word(nx + 112, ny - 30, 200, "cone", "center", 600, 16, 22))
over.append(word(fx - 62, fy + 36, 200, "bi-inversioning", "center", 600, 16, 22))
over.append(word(fx - 62, fy + 58, 200, "universal cone", "center", 600, 16, 22))
over.append(word(across.cx, across.cy + across.s + 58, 400, "across the co-linear", "center", 600, 15, 22, "#4a5160", "letter-spacing: 1px"))

cam = along; R = cam.s
over.append(html_box(cam.cx, cam.cy - R - 26, 40, 40, VSTYLE, "A"))
over.append(html_box(cam.cx + R + 24, cam.cy, 40, 40, VSTYLE, "C"))
QW = dict(weight=600, size=16, h=22)
q = 0.46 * R
over.append(word(cam.cx + q, cam.cy - q, 150, "possibling", "center", **QW))
over.append(word(cam.cx - q, cam.cy - q, 150, "co-possibling", "center", **QW))
over.append(word(cam.cx - q, cam.cy + q, 150, "possibling", "center", **QW))
over.append(word(cam.cx + q, cam.cy + q, 150, "co-possibling", "center", **QW))
over.append(chip(cam.cx - 76, cam.cy + 26, "own side · 25", True, w=128))
over.append(word(cam.cx, cam.cy + R + 58, 400, "along it, from its own side: 24 and 23 behind 25", "center", 600, 15, 22, "#4a5160", "letter-spacing: 1px"))

title = (f'<div style="position: absolute; left: 60px; top: 770px; width: 1080px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'The co-linear of the bi-folding, and its two cones</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 822px; width: 1080px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: #4a5160">'
           f'Two folds cross at two opposite intersections. The line through the two, through the 0, is the co-linear.<br>'
           f'Four quarter spheres go from its far side to its own side, possibling and co-possibling in turn: eight triangles, all with it.<br>'
           f'Its far side, 23, the vertex of the bi-inversioning universal cone. Its own side, 25, the co-recursioning cone.<br>'
           f'The two cones cross in the circle between the two, about 24, a 0.<br>'
           f'A turning about the co-linear rests at its two ends alone. Opened along it, the sphere is a torus: a going at no rest.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The co-linear of the bi-folding, and its two cones", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft5.dc.html"), "w", encoding="utf-8").write(html)

pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft5_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft5_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
