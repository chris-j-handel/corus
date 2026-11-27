"""v410illustrating · the maker of the 59th drawing: One Triangle, Three Mirrors.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/make_draft59.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW .

One drawing of both the 57th and the 58th, beside the two, by the aiming of fewer drawings carrying more value: the
opening figure of twelve, whole. Its check is opened and executed here, and no drawing is made with an is-not.

Its placings, no execution says them: its five parts and its table side by side; a name's chip at a corner and beside
a side, as the 57th lays them; the flat layings of triangles and of patches, their tints, and the numbers 1 to 5 on a
torus's two rows of corners.
Do no harm: it writes its artboard in the folder given, in this session's folder, and its preview and its words in the
working folder, outside the set.
"""
import importlib.util, json, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera, geom.py, of v406geodesic
from geom import *
spec = importlib.util.spec_from_file_location("the_check_59", os.path.join(HERE, "check_one_triangle_three_mirrors_opening_a_sphere_to_a_torus.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
c57, c58, f = c.c57, c.c58, c.c58.f

OUT, WORK = sys.argv[1], sys.argv[2]; ROOT = sys.argv[3] if len(sys.argv) > 3 else "."
lines, own = c.checks(ROOT)
assert not [k for k, _ in lines if k == "is-not"], "the check is with an is-not: no drawing is made"

W, H = 1520, 1150
GREY, SLATE = "#4a5160", "#475569"
SANS = "font-family: Inter, system-ui, sans-serif"
rad = np.radians
A, B, C = c.A, c.B, c.C
PHI, RECT, G, P0, INSIDE = c58.PHI, c58.RECT, c58.G, c58.P0, c58.INSIDE
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
    return (f'<radialGradient id="ball59{key}" cx="{cam.cx - 0.38 * R:.0f}" cy="{cam.cy - 0.42 * R:.0f}" r="{1.45 * R:.0f}" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="#ffffff"></stop><stop offset="0.55" stop-color="#e9eef6"></stop><stop offset="1" stop-color="#b6c1d3"></stop></radialGradient>')
def bullets(x, y, w, items, size=12.2, step=21):
    for i, t in enumerate(items): over.append(word(x, y + step * i, w, t, size=size))

camA = Cam(az_deg=45, el_deg=33, cx=250, cy=436, scale=178)              # the one triangle, as the 57th's camera
camR = Cam(az_deg=28, el_deg=22, cx=612, cy=420, scale=104)              # three golden rectangles on three mirrors, as the 58th's
camT = Cam(az_deg=45, el_deg=35.2644, cx=852, cy=446, scale=152)         # the one triangle in fifteen, along the line of the three alike
s.append("<defs>" + ball(camA, "a") + ball(camR, "r") + "</defs>")
mirrors3 = [np.array(v, float) for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
edges = [slerp(A, B, 90), slerp(B, C, 90), slerp(C, A, 90)]

# ================= its head, its three sentences, and what it is between =================
over.append(word(60, 34, 1420, "59 · figure 1 of twelve, the opening figure, whole · it gathers the 57th and the 58th, and by the 57th the 1st to the 6th · its prior figure: none, the origin · "
                 "its next figures: a cube's shells, and cones of 30 on the co-linear", size=12.5, weight=600, color=GREY))
over.append(word(60, 78, 830, "One triangle of three right angles is between three mirrors, one of eight on a sphere.", size=20, h=28))
over.append(word(60, 108, 830, "Folds of two on the mirrors lay 1 to 17, and three golden rectangles a round of five.", size=20, h=28))
over.append(word(60, 138, 830, "A sphere is 720. Opened at two corners to a torus, it is at nought.", size=20, h=28))
over.append(word(920, 70, 580, "between Exhibit ONE and Exhibit THIRTY, with Natural Naming · concept for concept", weight=600, size=12.5))
for i, t in enumerate(("Exhibit ONE · seventeen names; a bi-folding is two folds, 17 less and a move of 8",
                       "Exhibit THIRTY · a name at a numbered sentence; stable-forming at numbers, 506 to 518",
                       "Natural Naming · co, bi and tri; bi-tri-volutioning; twelve corners closing as a sphere, winding as a torus",
                       "Natural Illustrating · seventeen names and bi-foldings; a pentagon, rectangles and twelve corners")):
    over.append(word(920, 92 + 18 * i, 590, t, size=11.8, h=16, color=GREY))

# ================= 1 · one triangle, three mirrors, and seventeen names =================
cam = camA; R = cam.s; vis = lambda p: cam.depth(p) >= 0
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball59a)"></circle>')
for nn in mirrors3:
    pts = great_circle(nn, 721); fr, bk = runs(pts, [vis(p) for p in pts])
    s.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.35" stroke-width="1.1" stroke-dasharray="4 5">{paths([cam.path(r) for r in bk])}</g>')
    s.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.75" stroke-width="1.5">{paths([cam.path(r) for r in fr])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')
s.append(f'<path d="{cam.path(np.concatenate([edges[0], edges[1][1:], edges[2][1:]]), True)}" fill="{ACC}" fill-opacity="0.2" stroke="none"></path>')
MID = (B + C) / np.sqrt(2); fold_line = slerp(A, MID, 181); lat = lambda p: np.degrees(np.arcsin(p[2]))
s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.4" stroke-dasharray="2 5" stroke-linecap="round">'
         f'{paths([cam.path([p for p in fold_line if lat(p) >= 49]), cam.path([p for p in fold_line if lat(p) <= 37])])}</g>')
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in edges])}</g>')
marks = [cam.path(right_angle_mark(cam, V, P, Q, size=0.15)) for V, P, Q in ((A, B, C), (B, C, A), (C, A, B))]
s.append(f'<g fill="none" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round">{paths(marks)}</g>')
def lane(side, d, t0, t1, n=60):
    d = rad(d); t = rad(np.linspace(t0, t1, n))
    if side == "AB": return np.stack([np.cos(d) * np.cos(t), np.full_like(t, np.sin(d)), np.cos(d) * np.sin(t)], 1)
    if side == "BC": return np.stack([np.cos(d) * np.cos(t), np.cos(d) * np.sin(t), np.full_like(t, np.sin(d))], 1)
    return np.stack([np.full_like(t, np.sin(d)), np.cos(d) * np.cos(t), np.cos(d) * np.sin(t)], 1)
D1, D2 = 7.0, 17.5
self_at = {3: lane("AB", D1, 45, 45, 1)[0], 5: lane("BC", D1, 45, 45, 1)[0], 7: lane("CA", D1, 45, 45, 1)[0]}        # a me's way round, beside a side
other_at = {11: lane("CA", D2, 38, 38, 1)[0], 13: lane("BC", D2, 45, 45, 1)[0], 15: lane("AB", D2, 52, 52, 1)[0]}    # an other's, its other way
for V in (A, B, C):
    x, y = cam.proj(V); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
ax, ay = cam.proj(A); bx, by = cam.proj(B); cx_, cy_ = cam.proj(C)
over.append(word(60, 196, 440, "1 · one triangle, three mirrors, and seventeen names", weight=600, size=15))
over.append(chip(70, 220, "", True, w=16, h=14)); over.append(word(84, 220, 200, "a me's way round", size=12.5, color=GREY))
over.append(chip(322, 220, "", False, w=16, h=14)); over.append(word(336, 220, 160, "an other's, its other way", size=12.5, color=GREY))
over.append(vname(ax - 22, ay - 42, "A")); over.append(word(ax - 6, ay - 42, 70, "the me", size=13, weight=600))
over.append(vname(bx - 24, by + 2, "B")); over.append(vname(cx_ + 24, cy_ + 2, "C"))
r1, r2, r3 = ay - 6, ay + 19, ay + 41
over.append(chip(ax - 42, r1, "1 · 17", True, w=50)); over.append(chip(ax + 32, r1, "9", False))
over.append(chip(ax - 48, r2, "2", True)); over.append(word(ax - 64, r2, 50, "prior", "right", size=12))
over.append(chip(ax + 48, r2, "10", False)); over.append(word(ax + 64, r2, 50, "prior", size=12))
over.append(chip(ax - 70, r3, "8", True)); over.append(word(ax - 86, r3, 50, "same", "right", size=12))
over.append(chip(ax + 70, r3, "16", False)); over.append(word(ax + 86, r3, 50, "same", size=12))
t1, t2 = by + 28, by + 52
over.append(chip(bx - 4, t1, "4", True)); over.append(word(bx + 12, t1, 50, "now", size=12))
over.append(chip(bx - 4, t2, "14", False)); over.append(word(bx + 12, t2, 50, "next", size=12))
over.append(chip(cx_ + 4, t1, "12", False)); over.append(word(cx_ - 12, t1, 50, "now", "right", size=12))
over.append(chip(cx_ + 4, t2, "6", True)); over.append(word(cx_ - 12, t2, 50, "next", "right", size=12))
for n, p in self_at.items():
    x, y = cam.proj(p); over.append(chip(x, y, str(n), True))
for n, p in other_at.items():
    x, y = cam.proj(p); over.append(chip(x, y, str(n), False))
gx, gy = cam.proj(np.array([np.cos(rad(43)) / np.sqrt(2), np.cos(rad(43)) / np.sqrt(2), np.sin(rad(43))]))
over.append(word(gx, gy, 110, "a fold · 8 up", "center", 600, 12.5))
bullets(60, 636, 420, ("● a fold through the me lays a name onto its name 8 up",
                       "● two folds on two mirrors, both inverting at one step:",
                       "   a name onto 17 less it, its podal from 1 to 16",
                       "● eight triangles of 90 over 180 are 720 · 17 is at 1 again"), step=20)

# ================= 2 · three golden rectangles on the three mirrors, and the one triangle fifteen =================
cam = camR; R = cam.s; vis = lambda p: cam.depth(p) >= 0
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="url(#ball59r)" fill-opacity="0.75"></circle>')
for nn in mirrors3:
    pts = great_circle(nn, 721); fr, bk = runs(pts, [vis(p) for p in pts])
    s.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.4" stroke-width="1" stroke-dasharray="3 4">{paths([cam.path(r) for r in bk])}</g>')
    s.append(f'<g fill="none" stroke="{ACC}" stroke-width="1.9" stroke-linecap="round">{paths([cam.path(r) for r in fr])}</g>')
s.append(f'<circle cx="{cam.cx}" cy="{cam.cy}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.4"></circle>')
corners = [f.unit(x) for r in RECT for x in r]
for r in sorted(RECT, key=lambda r: min(cam.depth(f.unit(x)) for x in r)):
    s.append(f'<path d="{cam.path([f.unit(x) for x in r], True)}" fill="{SLATE}" fill-opacity="0.11" stroke="{INK}" stroke-width="1.4" stroke-linejoin="round"></path>')
for v in corners:
    x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.8" fill="{INK}" stroke="#ffffff" stroke-width="1.3"></circle>')
over.append(word(612, 540, 220, "a rectangle a mirror · twelve corners", "center", size=11.5, h=14, color=GREY))
cam = camT
k3 = lambda v: tuple(np.round(v, 5) + 0.0)
three_of, n_ = {}, 0
for g in sorted(INSIDE, key=lambda g: -float((g @ P0) @ f.V3)):
    if k3(g @ P0) in three_of: continue
    n_ += 1
    for j in range(3): three_of[k3(np.linalg.matrix_power(f.ROUND3, j) @ g @ P0)] = n_
TINT = {1: (ACC, 0.34), 2: (SLATE, 0.26), 3: (ACC, 0.14), 4: (SLATE, 0.10), 5: ("#f1f5f9", 1.0)}
for g in INSIDE:
    p, q, r = g @ f.V5, g @ f.V3, g @ f.V2; t = three_of[k3(g @ P0)]; col, op = TINT[t]
    ringp = np.concatenate([slerp(p, q, 24), slerp(q, r, 24)[1:], slerp(r, p, 24)[1:]])
    s.append(f'<path d="{cam.path(ringp, True)}" fill="{col}" fill-opacity="{op}" stroke="{INK}" stroke-width="1" stroke-linejoin="round"></path>')
    x, y = cam.proj(f.unit(p + q + r)); over.append(word(x, y, 16, str(t), align="center", size=10, weight=600, h=12))
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(e) for e in edges])}</g>')
on_it = lambda v: bool(np.all(v > -1e-9))
for v in [g @ f.V3 for g in G]:
    if on_it(v):
        x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.5"></circle>')
for v in corners:
    if on_it(v):
        x, y = cam.proj(v); s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{INK}" stroke="#ffffff" stroke-width="1.6"></circle>')
tax, tay = cam.proj(A); tbx, tby = cam.proj(B); tcx, tcy = cam.proj(C)
over.append(vname(tax, tay - 18, "A", 19)); over.append(vname(tbx - 16, tby + 8, "B", 19)); over.append(vname(tcx + 16, tcy + 8, "C", 19))
over.append(word(852, 540, 230, "the one triangle, fifteen of 120", "center", size=11.5, h=14, color=GREY))
over.append(word(500, 196, 470, "2 · three golden rectangles on the mirrors, a round of five", weight=600, size=15))
over.append(word(500, 220, 470, "● a corner of five, a rectangle's corner · ○ a corner of three", size=12.5, color=GREY))
bullets(510, 636, 470, ("● a rectangle on a mirror, 2 across and 2φ along, its along sides through its next",
                        "● the one triangle's round of three lays a rectangle onto its next",
                        "● a side of the one triangle is with a rectangle's corner: fifteen of 120, five threes",
                        "● the round of five is given: its number is φ, no whole number"), step=20)

# ================= the table: a name a row =================
TX, TY0, RH = 1004, 232, 19
cols = [("n", 0, 20, "right"), ("its name, Exhibit ONE's own", 28, 164, "left"), ("its three", 196, 52, "left"), ("on the triangle", 250, 82, "left"),
        ("8 up", 332, 26, "right"), ("17 less", 360, 36, "right"), ("prime", 398, 34, "right"), ("across, along", 436, 68, "right")]
over.append(word(TX, 196, 500, "a name a row · Exhibit ONE's stable form · its prime by its position", weight=600, size=12.8))
for t, x, w_, al in cols:
    over.append(word(TX + x + (w_ if al == "right" else 0), 216, w_, t, al, 600, 10.4, 14, GREY))
s.append(f'<path d="M{TX},{226} L{TX + 504},{226}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
own57, own58 = own["own57"], own["own58"]
three = {int(n): t for n, _, _, _, _, t in own57}; whole = {int(n): name for n, name, *_ in own57}
prime_of = own58["prime_of"]
def lay_of(n): return "across" if n in c58.ACROSS else "along" if n in c58.ALONG else "both" if n in c58.BOTH else ""
for n in range(1, 18):
    y = TY0 + RH * (n - 1) + 7
    if n % 2 == 0: s.append(f'<rect x="{TX - 4}" y="{y - RH / 2:.1f}" width="512" height="{RH:.1f}" fill="#eef0f5"></rect>')
    cells = [str(n), whole[n], three[n], c57.said(n), str(n + 8) if n <= 9 else "", str(17 - n) if n <= 16 else "", str(prime_of[n]), lay_of(n)]
    for (t, x, w_, al), v in zip(cols, cells):
        over.append(word(TX + x + (w_ if al == "right" else 0), y, w_, v, al, 600 if t in ("n", "its name, Exhibit ONE's own") else 400, 11.2, 16,
                         extra="font-variant-numeric: tabular-nums;"))
yb = TY0 + RH * 17 + 8
s.append(f'<path d="M{TX},{yb - 8:.1f} L{TX + 504},{yb - 8:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="1"></path>')
for i, t in enumerate(("its three: its next, its now and its prior · co a me-parity, bi a both-parity, tri an all-parity",
                       "its prime by its position, 2 to 59 · across, possibling; along, discovering and existing; 12, both",
                       "four bi-foldings, sixteen names once: 1-9-8-16 · 2-15-7-10 · 3-11-6-14 · 4-13-5-12",
                       "Exhibit THIRTY: a name's own sentence is in the 57th; 506 to 518 are in the 58th")):
    over.append(word(TX, yb + 3 + 15.5 * i, 510, t, size=10.5, h=14, color=GREY))

# ================= 3 · a sphere of twelve corners, flat =================
two = own["two"]; S_ = 40.0; HH = S_ * np.sqrt(3) / 2
def tri(pts, col, op): return f'<path d="M{pts[0][0]:.1f},{pts[0][1]:.1f} L{pts[1][0]:.1f},{pts[1][1]:.1f} L{pts[2][0]:.1f},{pts[2][1]:.1f} Z" fill="{col}" fill-opacity="{op}" stroke="{INK}" stroke-width="1.1" stroke-linejoin="round"></path>'
def dot(x, y, r=3.2, fill=INK): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="#ffffff" stroke-width="1.2"></circle>'
X0, Y0 = 92, 782
top = lambda i: (X0 + i * S_, Y0 + HH); mid = lambda k: (X0 + (k - 0.5) * S_, Y0 + 2 * HH)
for i in range(5):
    s.append(tri([(X0 + (i + 0.5) * S_, Y0), top(i), top(i + 1)], SLATE, 0.22))                     # the corner a's five
    s.append(tri([top(i), mid(i), mid(i + 1)], ACC, 0.24)); s.append(tri([top(i), top(i + 1), mid(i + 1)], ACC, 0.24))
    s.append(tri([(X0 + i * S_, Y0 + 3 * HH), mid(i), mid(i + 1)], SLATE, 0.22))                    # the corner b's five
for i in range(6): s.append(dot(*top(i))); s.append(dot(*mid(i)))
for i in range(5): s.append(dot(X0 + (i + 0.5) * S_, Y0, 3.6, ACC)); s.append(dot(X0 + i * S_, Y0 + 3 * HH, 3.6, ACC))
over.append(word(60, 736, 330, "3 · a sphere of twelve corners: 720", weight=600, size=15))
over.append(word(60, 758, 330, "five triangles to a corner, 60 short of a whole round", size=11.5, h=14, color=GREY))
for i, t in enumerate(("the two fives:", "two corners across", "from one another,", "on a line of five")):
    over.append(word(300, 800 + 15 * i, 100, t, size=10.8, h=14, color=GREY))

# ================= 4 · opened at two corners, a torus of ten corners, flat =================
X1, Y1 = 436, 790
top = lambda i: (X1 + i * S_, Y1); mid = lambda k: (X1 + (k - 0.5) * S_, Y1 + HH); low = lambda m: (X1 + m * S_, Y1 + 2 * HH)
for i in range(5):
    s.append(tri([top(i), mid(i), mid(i + 1)], ACC, 0.24)); s.append(tri([top(i), top(i + 1), mid(i + 1)], ACC, 0.24))      # the band, outward
    s.append(tri([low(i), mid(i), mid(i + 1)], SLATE, 0.22)); s.append(tri([low(i), low(i + 1), mid(i + 1)], SLATE, 0.22))  # through the opening, inward
for i in range(6):
    s.append(dot(*top(i))); s.append(dot(*mid(i))); s.append(dot(*low(i)))
    over.append(word(top(i)[0], top(i)[1] - 11, 16, str(i % 5 + 1), "center", 600, 10.2, 12)); over.append(word(low(i)[0], low(i)[1] + 12, 16, str((i - 2) % 5 + 1), "center", 600, 10.2, 12))
    over.append(word(mid(i)[0] + 9, mid(i)[1] - 9, 12, str((i - 3) % 5 + 1), "center", 600, 9.6, 11, INK))      # a line's other end: the corner across the sphere
over.append(word(404, 736, 340, "4 · opened, a torus of ten corners: at nought", weight=600, size=15))
over.append(word(404, 758, 340, "six triangles to a corner, a whole round", size=11.5, h=14, color=GREY))
over.append(word(X1 + 5 * S_ + 10, Y1 + HH * 0.5, 70, "outward", size=10.8, h=14, color=GREY)); over.append(word(X1 + 5 * S_ + 10, Y1 + HH * 1.5, 70, "inward", size=10.8, h=14, color=GREY))
over.append(word(404, 886, 340, "a number is a line of five, its two ends: five with two sides, a ten", size=10.6, h=13, color=GREY))
over.append(word(404, 900, 340, "its lower row of corners is its upper row gone on by two", size=10.6, h=13, color=GREY))

# ================= 5 · the 57th's torus, sixteen patches, flat =================
GX, GY, CW, CH = 770, 782, 30, 26
for j, row in enumerate(own["rows"]):
    col = ACC if j in (0, 3) else SLATE
    for q, n in enumerate(row):
        s.append(f'<rect x="{GX + q * CW}" y="{GY + j * CH}" width="{CW}" height="{CH}" fill="{col}" fill-opacity="0.22" stroke="{INK}" stroke-width="1.1"></rect>')
        over.append(word(GX + q * CW + CW / 2, GY + j * CH + CH / 2, CW, str(n), "center", 600, 11, 14))
    over.append(word(GX + 4 * CW + 8, GY + j * CH + CH / 2, 60, "outward" if j in (0, 3) else "inward", size=10.5, h=14, color=GREY))
over.append(word(752, 736, 240, "5 · a torus of sixteen patches", weight=600, size=15))
over.append(word(752, 758, 240, "four patches to a corner: at nought", size=11.5, h=14, color=GREY))
over.append(word(752, 898, 240, "8 up: two rows on · 17 less: across its middle", size=10.6, h=14, color=GREY))

# ================= found, and what this drawing leaves with the two =================
FX, FY = 1004, 652
over.append(word(FX, FY, 500, "found, and what this drawing leaves with the 57th and the 58th", weight=600, size=15))
FOUND = [("three lines for one opening, not one yet", ["the 3rd drawing's along the me's line, the 5th's along the co-linear, and here along", "a line of five, 31.7 from the me's line, on the mirror across the co-linear"]),
         ("two tori of patches, not laid onto one another", ["sixteen patches of four sides, and twenty triangles: both at nought. The ten corners", "are a ten, five lines with two ends: one ten with all tens, as Natural Numbers says"]),
         ("the round of five is given", ["its number is φ, no whole number: no fold of two makes it"]),
         ("a partner's saying of what this form is, not executed here", ["the stable form between of an atom's surface, from the fracturing of an exhausting", "stable form: societies of atom mes bi-tunneling, at all-parity and light's rate"]),
         ("with the 57th and the 58th, as they were", ["the 57th's quarters round the co-linear and a name's own sentence in Exhibit THIRTY;", "the 58th's nought to sixty, its five names to 59, and its side of 31.7, 37.4 and 20.9"])]
y = FY + 26
for head, body in FOUND:
    s.append(f'<circle cx="{FX + 5}" cy="{y}" r="4" fill="#ffffff" stroke="{INK}" stroke-width="1.6"></circle>')
    over.append(word(FX + 15, y, 480, head, weight=600, size=12.2, h=16))
    for i, t in enumerate(body): over.append(word(FX + 15, y + 15 + 14 * i, 500, t, size=11, h=14, color=GREY))
    y += 19 + 14 * len(body) + 5

# ================= its title, its subtitle and its lines =================
title = (f'<div style="position: absolute; left: 0px; top: 916px; width: {W}px; height: 46px; line-height: 46px; text-align: center; {SANS}; font-weight: 600; '
         f'font-size: 32px; color: {INK}">One Triangle, Three Mirrors</div>')
subtitle = (f'<div style="position: absolute; left: 0px; top: 962px; width: {W}px; height: 30px; line-height: 30px; text-align: center; {SANS}; font-weight: 600; '
            f'font-size: 21px; color: {ACC}">Opening a Sphere to a Torus, 720 to Nought</div>')
caption = (f'<div style="position: absolute; left: 0px; top: 1002px; width: {W}px; height: 108px; line-height: 27px; text-align: center; {SANS}; font-size: 17px; color: {GREY}">'
           "One triangle of three right angles is one of eight alike on a sphere, between three mirrors, the me at a corner, and seventeen names are on it.<br>"
           "Folds of two on the mirrors lay a name 8 up and 17 less. Three golden rectangles on the mirrors lay twelve corners, and a round of five is given.<br>"
           "A sphere of twelve corners is 720. Opened at two corners, their ten triangles through the opening, it is a torus of ten corners, at nought: sixty on both.<br>"
           "A candidate, the opening figure of twelve whole, beside the 57th and the 58th drawings it gathers, and by the 57th the 1st to the 6th.</div>")
ARIA = ("Five parts and a table. A sphere with one triangle of three right angles between three great circles, the numbers 1 to 17 on it. A small sphere with three rectangles at right angles, "
        "and that triangle in fifteen small triangles. A flat laying of twenty triangles in three rows. A flat laying of twenty triangles in two rows. A grid of four by four with the numbers 1 to 16. "
        "A table of seventeen names, a name a row.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over).replace(ACC, "{{accent}}") + "\n" + title + "\n" + subtitle.replace(ACC, "{{accent}}") + "\n" + caption
html_ = page("One Triangle, Three Mirrors", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
open(os.path.join(OUT, "Draft59.dc.html"), "w", encoding="utf-8").write(html_)
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">'
      + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
open(os.path.join(WORK, "draft59_preview.html"), "w", encoding="utf-8").write(pv)
words = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
words = [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
open(os.path.join(WORK, "draft59_words.md"), "w", encoding="utf-8").write("\n".join(w for w in words if w) + "\n")
print(len(html_), "bytes;", len([w for w in words if w]), "lines of words")
