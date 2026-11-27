"""Draft 57 · One Triangle, Three Right Angles · Bi-Folding 1 to 17, a Sphere Opening to a Torus (session v410illustrating).

The opening figure of twelve, a candidate, laid beside the 1st to the 6th drawings it gathers; no one of the six is
written in. Its title and its subtitle are a bi-coupling: the whole bounded context, and the value of interest.
Four parts and a table: the one triangle with seventeen names on it (the 1st and the 4th); two folds and the co-linear,
across it and along it (the 2nd, the 5th and the 6th); a torus of sixteen patches, observed along the me's line from
its two sides (the 3rd); and a name a row, Exhibit ONE's own name and three with its entering sentence of Exhibit THIRTY.
check_one_triangle_three_right_angles_bi-folding_1_to_17.py is its check, and the marks drawn here are its own.

Its placings, no execution says them: the four parts side by side; a way round as a lane beside a side; a torus as
two flat views; a chip a name; the dark, the open and the accent.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft57.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .
"""
import importlib.util, json, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check", os.path.join(HERE, "check_one_triangle_three_right_angles_bi-folding_1_to_17.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own, ent = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"

W, H = 1520, 1150
GREY, FAINT, SLATE = "#4a5160", "#9aa2b1", "#475569"
SANS = "font-family: Inter, system-ui, sans-serif"
rad = np.radians
A, B, C = c.A, c.B, c.C
s, over = [], []

def word(x, cy, w, t, align="left", weight=400, size=14, h=20, color=INK, extra=""):
    left = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {left:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; white-space: nowrap; {extra}">{t}</div>')
def chip(cx, cy, t, filled, w=24, h=22, size=12, edge=INK):
    look = (f"background: {INK}; color: #ffffff; border: 1.6px solid {INK}" if filled else f"background: #ffffff; color: {INK}; border: 1.6px solid {edge}")
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; box-sizing: border-box; '
            f'border-radius: {h // 2}px; line-height: {h - 3.2:.0f}px; text-align: center; {SANS}; font-weight: 600; font-size: {size}px; {look}">{t}</div>')
def vname(cx, cy, t, size=24):
    return (f'<div style="position: absolute; left: {cx - 20:.0f}px; top: {cy - 16:.0f}px; width: 40px; height: 32px; line-height: 32px; text-align: center; '
            f"font-family: 'STIX Two Text', Georgia, serif; font-style: italic; font-weight: 500; font-size: {size}px; color: {INK}\">{t}</div>")
def ball(cam, key):
    R = cam.s
    return (f'<radialGradient id="ball57{key}" cx="{cam.cx - 0.38 * R:.0f}" cy="{cam.cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop></radialGradient>')
def head_at(p1, p0, size=9):
    a = np.arctan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [(p1[0] + size * np.cos(a), p1[1] + size * np.sin(a)), (p1[0] + 0.62 * size * np.cos(a + 2.25), p1[1] + 0.62 * size * np.sin(a + 2.25)),
           (p1[0] + 0.62 * size * np.cos(a - 2.25), p1[1] + 0.62 * size * np.sin(a - 2.25))]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"

camA = Cam(az_deg=45, el_deg=33, cx=262, cy=442, scale=200)              # the one triangle, as the 4th drawing's camera
camB = Cam(az_deg=68, el_deg=20, cx=618, cy=392, scale=118)              # across the co-linear, as the 5th's
s.append("<defs>" + ball(camA, "a") + ball(camB, "b"))
s.append('<radialGradient id="floor57" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#1f2430" stop-opacity="0.18"></stop>'
         '<stop offset="1" stop-color="#1f2430" stop-opacity="0"></stop></radialGradient></defs>')

# ================= 1 · the one triangle, and seventeen names on it =================
cam = camA; R = cam.s; vis = lambda p: cam.depth(p) >= 0
s.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 18}" rx="{R * 0.85:.0f}" ry="{R * 0.08:.0f}" fill="url(#floor57)"></ellipse>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball57a)"></circle>')
pts = great_circle((0, 0, 1), 721); f_, b_ = runs(pts, [vis(p) for p in pts])
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="1" stroke-dasharray="4 5">{paths([cam.path(r) for r in b_])}</g>')
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.42" stroke-width="1.1">{paths([cam.path(r) for r in f_])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')
edges = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]
s.append(f'<path d="{cam.path(np.concatenate([edges[0], edges[1][1:], edges[2][1:]]), True)}" fill="{ACC}" fill-opacity="0.2" stroke="none"></path>')
MID = (B + C) / np.sqrt(2); fold_line = slerp(A, MID, 181); lat = lambda p: np.degrees(np.arcsin(p[2]))
s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.4" stroke-dasharray="2 5" stroke-linecap="round">'
         f'{paths([cam.path([p for p in fold_line if lat(p) >= 47.5]), cam.path([p for p in fold_line if lat(p) <= 38.5])])}</g>')
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in edges])}</g>')
marks = [cam.path(right_angle_mark(cam, V, P, Q, size=0.15)) for V, P, Q in ((A, B, C), (B, C, A), (C, A, B))]
s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round">{paths(marks)}</g>')
def lane(side, d, t0, t1, n=60):
    d = rad(d); t = rad(np.linspace(t0, t1, n))
    if side == "AB": return np.stack([np.cos(d) * np.cos(t), np.full_like(t, np.sin(d)), np.cos(d) * np.sin(t)], 1)
    if side == "BC": return np.stack([np.cos(d) * np.cos(t), np.cos(d) * np.sin(t), np.full_like(t, np.sin(d))], 1)
    return np.stack([np.full_like(t, np.sin(d)), np.cos(d) * np.cos(t), np.cos(d) * np.sin(t)], 1)
D1, D2, S0, S1, O0, O1 = 7.0, 16.5, 19, 71, 29, 61
self_lanes = {3: lane("AB", D1, S1, S0), 5: lane("BC", D1, S0, S1), 7: lane("CA", D1, S0, S1)}        # a me's way round: the me to B, B to C, C to the me
other_lanes = {11: lane("CA", D2, O1, O0), 13: lane("BC", D2, O1, O0), 15: lane("AB", D2, O0, O1)}    # an other's, its other way
s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.9" stroke-linecap="round">{paths([cam.path(p) for p in self_lanes.values()])}</g>')
s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.9" stroke-linecap="round" stroke-dasharray="2 5">{paths([cam.path(p) for p in other_lanes.values()])}</g>')
heads = [head_at(cam.proj(p[-1]), cam.proj(p[-3])) for p in list(self_lanes.values()) + list(other_lanes.values())]
s.append(f'<g fill="{INK}" stroke="{INK}" stroke-width="1" stroke-linejoin="round">{paths(heads)}</g>')
lam = rad(np.linspace(31, 59, 50)); FL = rad(33.0)
arc = np.stack([np.cos(FL) * np.cos(lam), np.cos(FL) * np.sin(lam), np.full_like(lam, np.sin(FL))], 1)
s.append(f'<path d="{cam.path(arc)}" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round"></path>')
s.append(f'<g fill="{INK}" stroke="{INK}" stroke-width="1" stroke-linejoin="round">'
         f'{paths([head_at(cam.proj(arc[-1]), cam.proj(arc[-3]), 8), head_at(cam.proj(arc[0]), cam.proj(arc[2]), 8)])}</g>')
for V in (A, B, C):
    x, y = cam.proj(V); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
ax, ay = cam.proj(A); bx, by = cam.proj(B); cx_, cy_ = cam.proj(C)
over.append(word(60, 196, 440, "1 · one triangle, and seventeen names on it", weight=600, size=15))
over.append(chip(70, 220, "", True, w=16, h=14)); over.append(word(84, 220, 200, "a me's way round", size=12.5, color=GREY))
over.append(chip(322, 220, "", False, w=16, h=14)); over.append(word(336, 220, 160, "an other's, its other way", size=12.5, color=GREY))
over.append(vname(ax - 22, ay - 46, "A")); over.append(word(ax - 6, ay - 46, 70, "the me", size=13, weight=600))
over.append(vname(bx - 24, by + 2, "B")); over.append(vname(cx_ + 24, cy_ + 2, "C"))
r1, r2, r3 = ay - 6, ay + 20, ay + 43
over.append(chip(ax - 44, r1, "1 · 17", True, w=50)); over.append(chip(ax + 34, r1, "9", False))
over.append(chip(ax - 52, r2, "2", True)); over.append(word(ax - 68, r2, 50, "prior", "right", size=12))
over.append(chip(ax + 52, r2, "10", False)); over.append(word(ax + 68, r2, 50, "prior", size=12))
over.append(chip(ax - 76, r3, "8", True)); over.append(word(ax - 92, r3, 50, "same", "right", size=12))
over.append(chip(ax + 76, r3, "16", False)); over.append(word(ax + 92, r3, 50, "same", size=12))
t1, t2 = by + 30, by + 55
over.append(chip(bx - 4, t1, "4", True)); over.append(word(bx + 12, t1, 50, "now", size=12))
over.append(chip(bx - 4, t2, "14", False)); over.append(word(bx + 12, t2, 50, "next", size=12))
over.append(chip(cx_ + 4, t1, "12", False)); over.append(word(cx_ - 12, t1, 50, "now", "right", size=12))
over.append(chip(cx_ + 4, t2, "6", True)); over.append(word(cx_ - 12, t2, 50, "next", "right", size=12))
for n, p in self_lanes.items():
    x, y = cam.proj(p[len(p) // 2]); over.append(chip(x, y, str(n), True))
for n, p in other_lanes.items():
    k = {11: len(p) // 4, 13: len(p) // 2, 15: 3 * len(p) // 4}[n]
    x, y = cam.proj(p[k]); over.append(chip(x, y, str(n), False))
gx, gy = cam.proj(np.array([np.cos(rad(43)) / np.sqrt(2), np.cos(rad(43)) / np.sqrt(2), np.sin(rad(43))]))
over.append(word(gx, gy, 110, "a fold · 8 up", "center", 600, 12.5))

# ================= 2 · two folds, and the co-linear =================
cam = camB; R = cam.s
def visible_part(cam, corners):
    ring = np.concatenate([slerp(corners[i], corners[(i + 1) % 3], 48)[:-1] for i in range(3)])
    keep = [cam.depth(p) >= -1e-12 for p in ring]
    if not any(keep): return None
    if all(keep): return ring
    out, n = [], len(ring)
    for i in range(n):
        p, q = ring[i], ring[(i + 1) % n]
        if keep[i]: out.append(p)
        if keep[i] != keep[(i + 1) % n]:
            t = cam.depth(p) / (cam.depth(p) - cam.depth(q)); x = p + t * (q - p); x = x - (x @ cam.d) * cam.d; out.append(x / np.linalg.norm(x))
    filled = []
    for i, p in enumerate(out):
        filled.append(p); q = out[(i + 1) % len(out)]
        if abs(cam.depth(p)) < 1e-9 and abs(cam.depth(q)) < 1e-9 and 1e-6 < np.linalg.norm(p - q) < 1.999: filled.extend(slerp(p, q, 24)[1:-1])
    return np.array(filled)
s.append(f'<ellipse cx="{cam.cx}" cy="{cam.cy + R + 14}" rx="{R * 0.85:.0f}" ry="{R * 0.08:.0f}" fill="url(#floor57)"></ellipse>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball57b)"></circle>')
for sy in (1, -1):
    for sz in (1, -1):
        col, op = (ACC, 0.22) if sy * sz > 0 else (SLATE, 0.18)
        for sx in (1, -1):
            part = visible_part(cam, [sx * B, sy * C, sz * A])
            if part is not None and len(part) > 2: s.append(f'<path d="{cam.path(part, True)}" fill="{col}" fill-opacity="{op}" stroke="none"></path>')
for nrm, w_ in (((0, 1, 0), 1.6), ((0, 0, 1), 1.6), ((1, 0, 0), 1.0)):
    pts = great_circle(nrm, 721); f_, b_ = runs(pts, [cam.depth(p) >= 0 for p in pts])
    s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.28" stroke-width="{w_ * 0.7:.1f}" stroke-dasharray="4 5">{paths([cam.path(r) for r in b_])}</g>')
    s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.66" stroke-width="{w_}">{paths([cam.path(r) for r in f_])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in edges])}</g>')
P = lambda t: cam.proj(t * B)
seg = lambda t0, t1: f"M{P(t0)[0]:.1f},{P(t0)[1]:.1f} L{P(t1)[0]:.1f},{P(t1)[1]:.1f}"
edge_t = 1.0 / np.hypot(B @ cam.right, B @ cam.up); REACH = 1.3
s.append(f'<path d="{seg(1.0, REACH)}" fill="none" stroke="{INK}" stroke-width="1.9" stroke-linecap="round"></path>')
s.append(f'<path d="{seg(-1.0, 1.0)}" fill="none" stroke="{INK}" stroke-width="1.7" stroke-dasharray="2 5" stroke-linecap="round"></path>')
s.append(f'<path d="{seg(-REACH, -max(edge_t, 1.0))}" fill="none" stroke="{INK}" stroke-width="1.9" stroke-linecap="round"></path>')
s.append(f'<path d="{head_at(P(REACH), P(REACH - 0.1), 10)}" fill="{INK}" stroke="{INK}" stroke-width="1"></path>')
def dot(V, kind):
    x, y = cam.proj(V)
    if kind == "own": return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>'
    if kind == "far": return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="#ffffff" fill-opacity="0.9" stroke="{INK}" stroke-width="1.7" stroke-dasharray="3 3"></circle>'
    if kind == "nought": return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#ffffff" fill-opacity="0.95" stroke="{INK}" stroke-width="1.6"></circle>'
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.8" fill="{INK}" stroke="#ffffff" stroke-width="1.6"></circle>'
for V, k in ((A, "front"), (C, "front"), (-B, "far"), (np.zeros(3), "nought"), (B, "own")): s.append(dot(V, k))
nx, ny = cam.proj(B); fx, fy = cam.proj(-B); ox, oy = cam.proj(np.zeros(3)); a2x, a2y = cam.proj(A); c2x, c2y = cam.proj(C)
over.append(word(500, 196, 480, "2 · two folds, and the co-linear", weight=600, size=15))
over.append(word(500, 220, 480, "its two folds are on the two sides at B, at a right angle", size=12.5, color=GREY))
over.append(vname(a2x, a2y - 20, "A", 20)); over.append(vname(c2x + 16, c2y + 12, "C", 20)); over.append(vname(nx + 6, ny - 22, "B", 20))
over.append(chip(nx + 30, ny + 24, "own side · 25", True, w=96, h=20, size=11.5))
over.append(chip(fx - 22, fy - 22, "far side · 23", False, w=92, h=20, size=11.5))
over.append(chip(ox + 4, oy - 22, "24 · a 0", False, w=66, h=20, size=11.5))
over.append(word(cam.cx, cam.cy + R + 36, 240, "across the co-linear", "center", 600, 12.5, color=GREY, extra="letter-spacing: 0.6px"))
# along it, from its own side: four quarters, and a step from a quarter to its next
QX, QY, QR = 884, 392, 100
for sy in (1, -1):
    for sz in (1, -1):
        col, op = (ACC, 0.22) if sy * sz > 0 else (SLATE, 0.18)
        sweep = 0 if sy * sz > 0 else 1
        s.append(f'<path d="M{QX},{QY} L{QX + sy * QR},{QY} A{QR},{QR} 0 0 {sweep} {QX},{QY - sz * QR} Z" fill="{col}" fill-opacity="{op}" stroke="none"></path>')
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.66" stroke-width="1.6"><path d="M{QX - QR},{QY} L{QX + QR},{QY}"></path><path d="M{QX},{QY - QR} L{QX},{QY + QR}"></path></g>')
s.append(f'<circle cx="{QX}" cy="{QY}" r="{QR}" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')
s.append(f'<path d="M{QX},{QY - QR} L{QX},{QY} L{QX + QR},{QY} A{QR},{QR} 0 0 0 {QX},{QY - QR} Z" fill="none" stroke="{ACC}" stroke-width="3" stroke-linejoin="round"></path>')
for k in range(4):
    mid = rad(90 + 90 * k); ts = np.linspace(mid - rad(12), mid + rad(12), 20); rr_ = 0.86 * QR
    p_ = [(QX + rr_ * np.cos(t), QY - rr_ * np.sin(t)) for t in ts]
    s.append(f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in p_)}" fill="none" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"></path>')
    s.append(f'<path d="{head_at(p_[-1], p_[-3], 7)}" fill="{INK}" stroke="{INK}" stroke-width="1"></path>')
s.append(f'<circle cx="{QX}" cy="{QY}" r="5.5" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
q = 0.44 * QR
for dx, dy, top, under in ((q, -q, "possibling", "a +"), (-q, -q, "co-possibling", "a + and a −"), (-q, q, "possibling", "a −"), (q, q, "co-possibling", "none")):
    over.append(word(QX + dx, QY + dy - 8, 100, top, "center", 600, 11, 16)); over.append(word(QX + dx, QY + dy + 8, 100, under, "center", 400, 11, 16, GREY))
over.append(vname(QX, QY - QR - 16, "A", 20)); over.append(vname(QX + QR + 16, QY, "C", 20))
over.append(word(QX, QY + QR + 36, 240, "along it, from its own side", "center", 600, 12.5, color=GREY, extra="letter-spacing: 0.6px"))
for i, t in enumerate(("● one fold is a mirror; two folds, both inverting at one step: + + + onto + − −",
                       "● the two folds' circles are both with B and the point across from it",
                       "● the co-linear is through the two and the 0, and its two ends are as they were",
                       "● round it a step to a next quarter is one fold, one parity inverting")):
    over.append(word(500, 568 + 21 * i, 490, t, size=12.2))

# ================= 3 · a torus of sixteen patches, observed along the me's line =================
TY, RO, RM, RI = 778, 96, 63, 30
def annulus(cx, outer, inner, label):
    out = []
    for r0, r1, col, op in ((RM, RO, ACC, 0.22), (RI, RM, SLATE, 0.18)):
        out.append(f'<path d="M{cx - r1},{TY} A{r1},{r1} 0 1 0 {cx + r1},{TY} A{r1},{r1} 0 1 0 {cx - r1},{TY} Z M{cx - r0},{TY} A{r0},{r0} 0 1 1 {cx + r0},{TY} A{r0},{r0} 0 1 1 {cx - r0},{TY} Z" '
                   f'fill="{col}" fill-opacity="{op}" fill-rule="evenodd" stroke="none"></path>')
    for r_ in (RI, RM, RO): out.append(f'<circle cx="{cx}" cy="{TY}" r="{r_}" fill="none" stroke="{INK}" stroke-width="{1.6 if r_ != RM else 1.1}"></circle>')
    for a in (0, 90, 180, 270):
        out.append(f'<path d="M{cx + RI * np.cos(rad(a)):.1f},{TY - RI * np.sin(rad(a)):.1f} L{cx + RO * np.cos(rad(a)):.1f},{TY - RO * np.sin(rad(a)):.1f}" fill="none" stroke="{INK}" stroke-opacity="0.6" stroke-width="1.1"></path>')
    out.append(f'<circle cx="{cx}" cy="{TY}" r="3.6" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')
    for Q in range(4):
        a = rad(90 * Q + 45)
        for r_, n in (((RM + RO) / 2, outer(Q)), ((RI + RM) / 2, inner(Q))):
            over.append(chip(cx + r_ * np.cos(a), TY - r_ * np.sin(a), str(n), n <= 8, w=24, h=20, size=11.5))
    over.append(word(cx, TY + RO + 18, 260, label, "center", 600, 12.5, color=GREY, extra="letter-spacing: 0.4px"))
    return "".join(out)
T1X, T2X = 166, 452
# a patch's name by its quarter and band is the check's own; turned over about the co-linear a name n is onto 17 less it
by_patch = {c.patch(n): n for n in range(1, 17)}
s.append(annulus(T1X, lambda Q: by_patch[(Q, 0)], lambda Q: by_patch[(Q, 1)], "from the me's side: 1 to 8"))
s.append(annulus(T2X, lambda Q: 17 - by_patch[(Q, 0)], lambda Q: 17 - by_patch[(Q, 1)], "over, about the co-linear: 9 to 16"))
s.append(f'<path d="M{T1X - RO - 14},{TY} L{T2X + RO + 8},{TY}" fill="none" stroke="{INK}" stroke-width="1.5" stroke-dasharray="2 5" stroke-linecap="round"></path>')
s.append(f'<path d="{head_at((T2X + RO + 8, TY), (T2X + RO - 2, TY), 8)}" fill="{INK}" stroke="{INK}" stroke-width="1"></path>')
over.append(word(60, 664, 540, "3 · a torus of sixteen patches, observed along the me's line", weight=600, size=15))
over.append(word((T1X + T2X) / 2, TY - 13, 110, "the co-linear", "center", 600, 11.5, 16, GREY))
for i, t in enumerate(("● a name a patch, by its n less 1 in four binary digits:",
                       "&nbsp;&nbsp;&nbsp;two its quarter round the opening, two its band round the tube",
                       "● outward, 1 to 4 and 13 to 16: 720, a sphere's eight triangles",
                       "● inward, 5 to 12: 720 the other way · a torus is at nought",
                       "● 8 up is through the tube: one quarter, and the band across it",
                       "● two folds about the co-linear: a name onto 17 less it",
                       "● 1 to 8 on the me's side, 9 to 16 on its far side, 17 at 1 again")):
    over.append(word(584, 696 + 21 * i, 420, t, size=12.2))
over.append(chip(592, 850, "", False, w=16, h=12, edge=ACC)); over.append(word(606, 850, 200, "outward, the accent", size=11.5, color=GREY))
over.append(chip(742, 850, "", False, w=16, h=12, edge=SLATE)); over.append(word(756, 850, 200, "inward, the slate", size=11.5, color=GREY))

# ================= the table: a name a row =================
TX, TY0, RH = 1016, 232, 20
cols = [("n", 0, 22, "right"), ("its name, Exhibit ONE's own", 32, 178, "left"), ("its three", 204, 62, "left"), ("on the triangle", 270, 96, "left"),
        ("8 up", 366, 30, "right"), ("17 less", 400, 40, "right"), ("THIRTY", 448, 44, "right")]
over.append(word(TX, 196, 490, "a name a row · Exhibit ONE's stable form · its entering in Exhibit THIRTY", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.6, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 490},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
three = {int(n): t for n, _, _, _, _, t in own}; whole = {int(n): name for n, name, *_ in own}
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="498" height="{RH:.1f}" fill="#eef0f5"></rect>')
    cells = [str(n), whole[n], three[n], c.said(n), str(n + 8) if n <= 9 else "", str(17 - n) if n <= 16 else "", str(ent[n])]
    for (t, x, w_, al), v in zip(cols, cells):
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if t in ("n", "its name, Exhibit ONE's own") else 400, 11.6, 16,
                         extra="font-variant-numeric: tabular-nums;"))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 490},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
over.append(word(TX, yb + 3, 490, "a name's three is its next, its now and its prior · co a me-parity, bi a both-parity, tri an all-parity", size=10.6, h=14, color=GREY))
over.append(word(TX, yb + 19, 490, "THIRTY: the numbered sentence of Exhibit THIRTY a name is said whole at, none ahead of it", size=10.6, h=14, color=GREY))
over.append(word(TX, yb + 40, 490, "four bi-foldings, sixteen names once:", weight=600, size=11.8))
for i, b in enumerate(("1-9-8-16", "2-15-7-10", "3-11-6-14", "4-13-5-12")):
    over.append(chip(TX + 268 + 58 * i, yb + 40, b, False, w=54, h=18, size=10.2))
over.append(word(TX, yb + 58, 490, "8 up or down, and 17 less, its podal from 1 to 16: its opening name again with four", size=10.6, h=14, color=GREY))

# ================= found, and its is-nots =================
FX, FY = 1016, 672
over.append(word(FX, FY, 470, "found, and what this drawing leaves with the six", weight=600, size=15))
for i, (t, sub) in enumerate((("○ two openings, not one yet", "the 3rd opens its torus along the me's line, the co-linear across its opening; the 5th opens a sphere along the co-linear: at a right angle"),
                              ("○ 17 less, said three ways", "one fold of a bi-folding's two in Exhibit ONE; two folds on two sides at the 2nd and the 3rd; at the 4th a one-way me-parity with the corner it comes to"),
                              ("○ the three of 1 and 17", "co-bi-tri in Exhibit ONE's table, next to prior; tri-bi-co at the 4th drawing, prior to next: an asking open, and both are laid"),
                              ("○ a name's own on a drawing is a drawing's", "a corner, a side and a patch are placings; 720 and nought are a field's adding, the 3rd's. With their own drawings, as they were: the 5th's two cones, the 6th's fifteen lines by nand"))):
    over.append(word(FX, FY + 30 + 50 * i, 480, t, weight=600, size=12.6))
    over.append(word(FX + 14, FY + 30 + 50 * i + 22, 470, sub, size=11.6, h=30, color=GREY, extra="white-space: normal; line-height: 15px;"))

# ================= head, sentences, beside it, title and subtitle =================
over.append(word(60, 34, 1400, "57 · figure 1 of twelve, the opening figure · it gathers the 1st to the 6th drawings · its prior figure: none, the origin · "
                 "its next figures: a cube's shells, and cones of 30 on the co-linear", weight=600, size=13, color=GREY))
for i, t in enumerate(("One triangle is three right angles, one of eight alike on a sphere.",
                       "A fold lays a name 8 up, and two folds on two sides lay it 17 less.",
                       "A sphere opened along a line is a torus of sixteen patches, at nought.")):
    over.append(word(60, 78 + 31 * i, 780, t, weight=600, size=21, h=28))
over.append(word(900, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.6, color=GREY))
for i, t in enumerate(("Exhibit ONE · seventeen names; a bi-folding is two folds, 17 less and a move of 8",
                       "Exhibit THIRTY · a name is said whole at a numbered sentence of its own entering",
                       "Natural Naming · co, bi and tri: a me-parity, a both-parity, an all-parity",
                       "Natural Illustrating · for its part of seventeen names, bi-foldings and a local nine")):
    over.append(word(900, 92 + 19 * i, 580, t, size=12, color=GREY))
title = (f'<div style="position: absolute; left: 60px; top: 912px; width: 1400px; text-align: center; {SANS}; font-weight: 600; font-size: 32px; line-height: 40px; color: {INK}">'
         f'One Triangle, Three Right Angles</div>')
subtitle = (f'<div style="position: absolute; left: 60px; top: 956px; width: 1400px; text-align: center; {SANS}; font-weight: 600; font-size: 21px; line-height: 30px; color: {{{{accent}}}}">'
            f'Bi-Folding 1 to 17, a Sphere Opening to a Torus</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 998px; width: 1400px; text-align: center; {SANS}; font-weight: 400; font-size: 17px; line-height: 27px; color: {GREY}">'
           f'One triangle of three right angles is one of eight alike on a sphere, the me at a corner and its far side the me\'s horizon.<br>'
           f'Seventeen names are on it, a me\'s way round and an other\'s, its other way. A fold through the me lays a name onto its name 8 up.<br>'
           f'Two folds on two sides are two right spiral steps about the co-linear, both inverting at one step: a name onto 17 less it, its podal from 1 to 16.<br>'
           f'Opened along a line a sphere is a torus of sixteen patches, at nought. A candidate, the opening figure of twelve, beside the six drawings it gathers.</div>')

ARIA = ("Four parts and a table. A sphere with one triangle of three right angles, the numbers 1 to 17 on its corners and beside its sides, a me's way round and an other's. "
        "A sphere with three great circles and a line through its centre and two opposite points, and beside it a disc of four quarters. "
        "Two flat views of a torus, sixteen patches with the numbers 1 to 16. A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle + "\n" + caption
html_ = page("One Triangle, Three Right Angles", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft57.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft57_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft57_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
