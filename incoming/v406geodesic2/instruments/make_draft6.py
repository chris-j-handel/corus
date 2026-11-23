"""Draft 6 · the cell by nand alone, round the co-linear (session v406geodesic2).

The fifth drawing's figure, drawn three times, with the fifteen lines of v406Reiman's cell by nand alone on it.
A parity is two is-or-is-nots, a + and a -: the two folds' circles through the co-linear, and four quarters round it.
Along the co-linear, lines 1 to 6: observing, a fold with a parity observed, and not both, through the co-linear to none.
Along it again, lines 7 to 12: with a prior +, its one is-or-is-not of four quarters, and one inversion through the co-linear.
Across it, lines 13 to 15: from its prior, of the far side, to its next prior, of its own side.
Geometry is computed; check_the_cell_by_nand_alone_round_the_co-linear.py is its check.

Usage: python3 -I make_draft6.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import json, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of the sitting before
from geom import *

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1600, 1000
SLATE = "#475569"
A = np.array([0, 0, 1.0]); B = np.array([1.0, 0, 0]); C = np.array([0, 1.0, 0])
OWN, FAR, O = B, -B, np.zeros(3)
one = Cam(az_deg=0, el_deg=0, cx=215, cy=440, scale=185)            # along the co-linear, from its own side: lines 1 to 6
two = Cam(az_deg=0, el_deg=0, cx=650, cy=440, scale=185)            # along it again: lines 7 to 12
across = Cam(az_deg=68, el_deg=20, cx=1300, cy=385, scale=240)      # across it, the fifth drawing's own view: lines 13 to 15


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
    return (f'<radialGradient id="ball6{key}" cx="{cam.cx - 0.38 * R:.0f}" cy="{cam.cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop></radialGradient>')


def quarters(cam):
    """The four quarter spheres between the two folds' circles: a parity's two, and a 0's two, in turn."""
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


def dot(cam, V, kind):
    x, y = cam.proj(V)
    if kind == "own":    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{ACC}" stroke="#ffffff" stroke-width="2.5"></circle>'
    if kind == "far":    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="#ffffff" fill-opacity="0.9" stroke="{INK}" stroke-width="2.2" stroke-dasharray="3 3"></circle>'
    if kind == "nought": return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#ffffff" fill-opacity="0.95" stroke="{INK}" stroke-width="2"></circle>'
    if kind == "front":  return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>'
    if kind == "mark":   return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="#ffffff" stroke="{INK}" stroke-width="2.2"></circle>'
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#ffffff" fill-opacity="0.7" stroke="{INK}" stroke-opacity="0.5" stroke-width="1.6"></circle>'


def arrow_head(p1, p0, size=14, opacity=1.0):
    a = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [(p1[0] + size * np.cos(a), p1[1] + size * np.sin(a)),
           (p1[0] + 0.6 * size * np.cos(a + 2.25), p1[1] + 0.6 * size * np.sin(a + 2.25)),
           (p1[0] + 0.6 * size * np.cos(a - 2.25), p1[1] + 0.6 * size * np.sin(a - 2.25))]
    return (f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)} Z" fill="{INK}" fill-opacity="{opacity}" stroke="{INK}" '
            f'stroke-opacity="{opacity}" stroke-width="1.5" stroke-linejoin="round"></path>')


def disc(cam, key, tints):
    """The figure along the co-linear, from its own side: C at its right, the me above. tints: a quarter's colour and its opacity."""
    R, out = cam.s, []
    out.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 24}" rx="{R * 0.85:.0f}" ry="{R * 0.09:.0f}" fill="url(#floor6)"></ellipse>')
    out.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball6{key})"></circle>')
    for sy in (1, -1):
        for sz in (1, -1):
            col, op = tints[(sy, sz)]
            ex, ey = cam.cx + sy * R, cam.cy - sz * R
            sweep = 0 if sy * sz > 0 else 1
            out.append(f'<path d="M{cam.cx},{cam.cy} L{ex},{cam.cy} A{R},{R} 0 0 {sweep} {cam.cx},{ey} Z" fill="{col}" fill-opacity="{op}" stroke="none"></path>')
    out.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.66" stroke-width="2">'
               f'<path d="M{cam.cx - R},{cam.cy} L{cam.cx + R},{cam.cy}"></path><path d="M{cam.cx},{cam.cy - R} L{cam.cx},{cam.cy + R}"></path></g>')
    out.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"></circle>')
    out.append(f'<path d="M{cam.cx},{cam.cy - R} L{cam.cx},{cam.cy} L{cam.cx + R},{cam.cy} A{R},{R} 0 0 0 {cam.cx},{cam.cy - R} Z" fill="none" stroke="{ACC}" stroke-width="4" stroke-linejoin="round"></path>')
    return "".join(out)


def at(cam, deg, r):
    """A place of the figure along the co-linear: degrees from C toward the me, r of its radius."""
    t = np.radians(deg)
    return cam.cx + r * cam.s * np.cos(t), cam.cy - r * cam.s * np.sin(t)


def step(cam, mid_deg, way, r=0.76):
    """One fold, over a circle: a short going round the co-linear, way +1 from C toward the me."""
    ts = np.linspace(mid_deg - way * 13, mid_deg + way * 13, 24)
    pts = [at(cam, t, r) for t in ts]
    return (f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"></path>'
            + arrow_head(pts[-1], pts[-3], 10))


def through(cam, from_deg, r0, r1, dash):
    """Two folds in a row: a going through the co-linear, from a quarter to the quarter opposite."""
    p0, p1 = at(cam, from_deg, r0), at(cam, from_deg + 180, r1)
    return (f'<path d="M{p0[0]:.1f},{p0[1]:.1f} L{p1[0]:.1f},{p1[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"{dash}></path>'
            + arrow_head(p1, p0, 12))


s = ['<defs>' + ball(one, "a") + ball(two, "b") + ball(across, "c") +
     '<radialGradient id="floor6" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#1f2430" stop-opacity="0.2"></stop><stop offset="1" stop-color="#1f2430" stop-opacity="0"></stop></radialGradient></defs>']

# ================= lines 1 to 6, along the co-linear: observing, and the parity surfacing =================
IN_TURN = {(1, 1): (ACC, 0.22), (-1, -1): (ACC, 0.22), (-1, 1): (SLATE, 0.18), (1, -1): (SLATE, 0.18)}
cam = one
s.append(disc(cam, "a", IN_TURN))
s.append(step(cam, 0, +1)); s.append(step(cam, 180, -1))        # a fold about the horizon's circle: a + observed
s.append(step(cam, 90, +1)); s.append(step(cam, 270, -1))       # a fold about its other circle: a - observed
s.append(through(cam, 135, 0.36, 0.30, ' stroke-dasharray="7 6"'))   # not both: a + and a - to none
s.append(dot(cam, OWN, "own"))
for V in (A, C, -A, -C): s.append(dot(cam, V, "front"))

# ================= lines 7 to 12, along it again: a prior +, and its one is-or-is-not =================
ONE_OF_FOUR = {(1, 1): (ACC, 0.30), (-1, -1): (SLATE, 0.13), (-1, 1): (SLATE, 0.13), (1, -1): (SLATE, 0.13)}
cam = two
s.append(disc(cam, "b", ONE_OF_FOUR))
s.append(through(cam, 45, 0.27, 0.27, ''))                      # one inversion: its prior, a +, to a -
s.append(dot(cam, OWN, "own"))
for V in (A, C, -A, -C): s.append(dot(cam, V, "front"))

# ================= lines 13 to 15, across the co-linear: from its prior to its next prior =================
cam = across; R = cam.s
s.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 26}" rx="{R * 0.85:.0f}" ry="{R * 0.09:.0f}" fill="url(#floor6)"></ellipse>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball6c)"></circle>')
s.append(quarters(cam))
s.append(circles(cam, (((0, 1, 0), 2.0), ((0, 0, 1), 2.0), ((1, 0, 0), 1.4))))
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="2"></circle>')
edges = lambda P, Q, S: [slerp(P, Q, 90), slerp(Q, S, 90), slerp(S, P, 90)]
OPPOSITE = edges(-A, B, -C)                                       # the triangle opposite the prior's, through the 0: hidden
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.45" stroke-width="2" stroke-dasharray="4 6" stroke-linecap="round">{paths([cam.path(e) for e in OPPOSITE])}</g>')
PRIOR = edges(A, -B, C)                                           # the prior's triangle: the one triangle folded about the circle between
front = lambda e: [p for p in e if cam.depth(p) >= 0]
s.append(f'<g fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(front(e)) for e in PRIOR if len(front(e)) > 1])}</g>')
T0 = edges(A, B, C)
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in T0])}</g>')
P = lambda t: cam.proj(t * B)
seg = lambda t0, t1: f"M{P(t0)[0]:.1f},{P(t0)[1]:.1f} L{P(t1)[0]:.1f},{P(t1)[1]:.1f}"
edge = 1.0 / np.hypot(B @ cam.right, B @ cam.up)
REACH = 1.27
s.append(f'<path d="{seg(1.0, REACH)}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(f'<path d="{seg(-1.0, 1.0)}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-dasharray="2 7" stroke-linecap="round"></path>')
s.append(f'<path d="{seg(-REACH, -max(edge, 1.0))}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"></path>')
s.append(arrow_head(P(REACH), P(REACH - 0.1)))
c_prior = np.array([-1, 1, 1.0]) / np.sqrt(3); c_same = np.array([1, 1, 1.0]) / np.sqrt(3); c_opposite = -c_prior
arc = slerp(c_prior, c_same, 80)[5:74]                             # with is: one fold, about the circle between
s.append(f'<path d="{cam.path(arc)}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"></path>')
s.append(arrow_head(cam.proj(arc[-1]), cam.proj(arc[-4]), 12))
q0, q1 = cam.proj(0.93 * c_prior), cam.proj(0.9 * c_opposite)      # with is-not: three folds, through the 0
s.append(f'<path d="M{q0[0]:.1f},{q0[1]:.1f} L{q1[0]:.1f},{q1[1]:.1f}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-dasharray="7 6" stroke-linecap="round"></path>')
s.append(arrow_head(q1, q0, 12, 0.7))
for V, k in ((A, "front"), (C, "front"), (-A, "back"), (-C, "back"), (FAR, "far"), (O, "nought"), (OWN, "own"), (c_prior, "mark")):
    s.append(dot(cam, V, k))

ARIA = ("One figure drawn three times: a sphere with three great circles and a line through its centre and two opposite intersections of the circles. "
        "Along the line, from its own side: a disc of four quarters about its centre, a +, a + and a −, a −, and none; four short arrows go round from none, over a circle a step, to a + and a −, "
        "and a dashed arrow goes from a + and a − through the centre to none. "
        "Along the line again: the quarter of a + apart from the three others, and an arrow from it through the centre to the quarter of a −. "
        "Across the line: from a triangle of the far side an arrow over the circle between to the triangle beside it, of its own side, and a dashed line through the centre to the triangle opposite.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")

# ---------------- words, retypable on the canvas ----------------
SANS = "font-family: Inter, system-ui, sans-serif"
def chip(cx, cy, text, filled, w=38, h=30, size=15):
    look = (f"background: {INK}; color: #ffffff; border: 2px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 2px solid {INK}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 4}px; text-align: center; {SANS}; font-weight: 600; font-size: {size}px; {look}">{text}</div>')
def word(x, cy, w, text, align, weight=400, size=17, h=24, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{text}</div>')
GREY = "#4a5160"
def under(cam, drop, head, under_it):
    return (word(cam.cx, cam.cy + cam.s + drop, 420, head, "center", 600, 15, 22, GREY, "letter-spacing: 1px")
            + word(cam.cx, cam.cy + cam.s + drop + 24, 420, under_it, "center", 400, 16, 22, GREY))

over = []
QW = dict(weight=600, size=16, h=22)
# ---- lines 1 to 6
cam = one; R = cam.s
over.append(html_box(cam.cx, cam.cy - R - 26, 40, 40, VSTYLE, "A"))
over.append(html_box(cam.cx + R + 24, cam.cy, 40, 40, VSTYLE, "C"))
for deg, text in ((45, "a +"), (135, "a + and a −"), (225, "a −"), (315, "none")):
    x, y = at(cam, deg, 0.60); over.append(word(x, y, 130, text, "center", **QW))
for deg, text in ((0, "+"), (180, "+"), (90, "−"), (270, "−")):      # a circle's parity, at its two ends
    x, y = at(cam, deg, 0.47); over.append(chip(x, y, text, False, w=24, h=24, size=15))
x, y = at(cam, 225, 0.0); over.append(word(x - 14, y + 29, 110, "not both", "right", 600, 15, 22))
over.append(under(cam, 56, "lines 1 to 6 · along the co-linear", "observing, and the parity surfacing"))
# ---- lines 7 to 12
cam = two; R = cam.s
over.append(html_box(cam.cx, cam.cy - R - 26, 40, 40, VSTYLE, "A"))
over.append(html_box(cam.cx + R + 24, cam.cy, 40, 40, VSTYLE, "C"))
for deg, name, a, b in ((45, "a +", "is", "0 · +"), (135, "a + and a −", "is-not", "− · −"), (225, "a −", "is-not", "− · −"), (315, "none", "is-not", "− · −")):
    x, y = at(cam, deg, 0.63)
    over.append(word(x, y - 23, 120, name, "center", 400, 14, 20, GREY))
    over.append(word(x, y, 120, a, "center", **QW)); over.append(word(x, y + 23, 120, b, "center", 400, 17, 22))
x, y = at(cam, 315, 0.0); over.append(word(x + 16, y + 24, 120, "one inversion", "left", 600, 15, 22))
over.append(under(cam, 56, "lines 7 to 12 · along the co-linear", "with a prior +: its giving · its next prior"))
# ---- lines 13 to 15
cam = across; R = cam.s
nx, ny = cam.proj(OWN); fx, fy = cam.proj(FAR); ox, oy = cam.proj(O); ax_, ay_ = cam.proj(A); cx_, cy_ = cam.proj(C)
over.append(html_box(ax_, ay_ - 28, 40, 40, VSTYLE, "A"))
over.append(html_box(cx_ + 24, cy_ + 20, 40, 40, VSTYLE, "C"))
over.append(html_box(nx + 12, ny - 34, 40, 40, VSTYLE, "B"))
over.append(chip(nx - 50, ny + 44, "own side · 25", True, w=128))
over.append(word(nx - 50, ny + 74, 140, "its next prior", "center", **QW))
over.append(chip(fx - 6, fy + 38, "far side · 23", False, w=118))
px, py = cam.proj(c_prior); over.append(word(px + 12, py + 40, 90, "its prior", "center", **QW))
over.append(chip(ox - 62, oy - 30, "24 · a 0", False, w=88))
mx, my = cam.proj(slerp(c_prior, c_same, 3)[1])
over.append(chip(mx - 44, my - 30, "is", False, w=40))
over.append(chip(ox - 62, oy + 37, "is-not", False, w=70))
over.append(under(cam, 56, "lines 13 to 15 · across the co-linear", "from its prior to its next prior, and the cell again"))

title = (f'<div style="position: absolute; left: 60px; top: 752px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
         f'The cell by nand alone, round the co-linear</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 804px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A parity is two is-or-is-nots, a + and a −: the two folds\' circles through the co-linear. Round it, four quarters: a +, a + and a −, a −, none.<br>'
           f'A fold is an other-than, a nand of a thing with itself. Observing is from none: a fold with a +, a fold with a −, and no fold again with the same.<br>'
           f'Not both: a + and a − go through the co-linear to none, two folds in a row. The parity surfacing is a +, a −, or none.<br>'
           f'With its prior, one is-or-is-not of four quarters. In its prior\'s own quarter, is: a 0 its giving, its prior its next prior. In the three others, is-not: one inversion.<br>'
           f'From its prior, of the far side, to its next prior, of its own side: with is one fold, about the circle between, and with is-not three, through the 0.</div>')

props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
         "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("The cell by nand alone, round the co-linear", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft6.dc.html"), "w", encoding="utf-8").write(html)

pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft6_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft6_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
