"""Draft 3: 1 to 17 resolving on a torus's outside surface.

Placement (checked by instruments/check_bifolding_and_torus.py):
  name n, n - 1 = b3 b2 b1 b0
  b3 b2 -> band round the small opening: 00 outer-top, 01 inner-top, 10 inner-bottom, 11 outer-bottom
  b1 b0 -> quarter round the large opening, theta in [90 Q, 90 Q + 90]
  17 is 0000 again: the winding closes on name 1.
Body is ray-traced to a PNG at 2x; every line, dot and label is vector over it, same camera.
"""
import json, os, sys
import numpy as np
from PIL import Image
import sys as _sys
_sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # geom.py beside this file, also under python3 -I
from geom import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "illustrations", "artboards")   # the artboards and the torus body
WORK = os.environ.get("TMPDIR", "/tmp")                          # working previews, not kept

W, H = 1200, 1000
RR, rr = 1.0, 0.42
cam = Cam(az_deg=45, el_deg=40, cx=600, cy=420, scale=318)
d, right, up = cam.d, cam.right, cam.up


def sdf(p):
    q = np.sqrt(p[..., 0] ** 2 + p[..., 1] ** 2) - RR
    return np.sqrt(q ** 2 + p[..., 2] ** 2) - rr


def surf(theta, phi):
    return np.stack([(RR + rr * np.cos(phi)) * np.cos(theta), (RR + rr * np.cos(phi)) * np.sin(theta),
                     rr * np.sin(phi)], -1)


def occluded(P, start=0.012):
    """True where the ray from P towards the viewer meets the torus (P on or off the surface)."""
    P = np.atleast_2d(P)
    t = np.full(len(P), start)
    hit = np.zeros(len(P), bool); alive = np.ones(len(P), bool)
    for _ in range(200):
        q = P[alive] + t[alive, None] * d
        f = sdf(q)
        h = f < 1e-4
        idx = np.where(alive)[0]
        hit[idx[h]] = True
        t[idx] += np.maximum(f, 2e-4)
        alive[idx[h]] = False
        alive &= t < 6
        if not alive.any():
            break
    return hit


def visible_surface(theta, phi):
    P = surf(theta, phi)
    n = np.stack([np.cos(phi) * np.cos(theta), np.cos(phi) * np.sin(theta), np.sin(phi)], -1)
    front = n @ d > 0.0
    return front & ~occluded(P + 0.004 * n)


# ---------------------------------------------------------------- raster body
def render_body(path_png):
    SS = 2
    x0, x1, y0, y1 = 120, 1080, 0, 860           # artboard px region to render
    xs = (np.arange((x1 - x0) * SS) + 0.5) / SS + x0
    ys = (np.arange((y1 - y0) * SS) + 0.5) / SS + y0
    X, Y = np.meshgrid(xs, ys)
    a = (X - cam.cx) / cam.s; b = -(Y - cam.cy) / cam.s
    O = a[..., None] * right + b[..., None] * up + 3.0 * d
    O = O.reshape(-1, 3)
    t = np.zeros(len(O)); hit = np.zeros(len(O), bool); alive = np.ones(len(O), bool)
    for _ in range(160):
        idx = np.where(alive)[0]
        p = O[idx] - t[idx, None] * d
        f = sdf(p)
        h = f < 2e-4
        hit[idx[h]] = True
        alive[idx[h]] = False
        t[idx[~h]] += f[~h] * 0.95
        alive &= t < 6.5
        if not alive.any():
            break
    P = O - t[:, None] * d
    xy = np.sqrt(P[:, 0] ** 2 + P[:, 1] ** 2) + 1e-9
    core = np.stack([P[:, 0] / xy * RR, P[:, 1] / xy * RR, np.zeros_like(xy)], 1)
    n = (P - core) / rr
    L = -0.5 * right + 0.7 * up + 0.55 * d; L /= np.linalg.norm(L)
    Hh = L + d; Hh /= np.linalg.norm(Hh)
    lam = np.clip(n @ L, 0, 1)
    spec = np.clip(n @ Hh, 0, 1) ** 36 * 0.22
    c = 0.28 + 0.72 * lam
    dark = np.array([0x9f, 0xab, 0xc0]) / 255; mid = np.array([0xe6, 0xeb, 0xf4]) / 255; light = np.ones(3)
    u = np.clip((c - 0.28) / 0.72, 0, 1)[:, None]
    col = np.where(u < 0.68, dark + (mid - dark) * (u / 0.68), mid + (light - mid) * ((u - 0.68) / 0.32))
    col = np.clip(col + spec[:, None], 0, 1)
    hgt, wid = X.shape
    hitm = hit.reshape(hgt, wid); tm = np.where(hit, t, 99).reshape(hgt, wid)
    rgb = col.reshape(hgt, wid, 3)
    # outline: silhouette and depth breaks
    edge = np.zeros_like(hitm)
    for dy, dx in ((0, 1), (1, 0), (1, 1), (1, -1)):
        h2 = np.roll(np.roll(hitm, dy, 0), dx, 1); t2 = np.roll(np.roll(tm, dy, 0), dx, 1)
        e = (hitm != h2) | (hitm & h2 & (np.abs(tm - t2) > 0.06))
        edge |= e | np.roll(np.roll(e, -dy, 0), -dx, 1)
    alpha = hitm.astype(float)
    ink = np.array([0x1f, 0x24, 0x30]) / 255
    rgb = np.where(edge[..., None], ink, rgb)
    alpha = np.where(edge, 1.0, alpha)
    img = np.concatenate([rgb, alpha[..., None]], -1)
    Image.fromarray((img * 255 + 0.5).astype(np.uint8), "RGBA").save(path_png, optimize=True)
    return x0, y0, x1 - x0, y1 - y0


# ---------------------------------------------------------------- vector overlay
s = []
s.append('''<defs>
<radialGradient id="floor3" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#1f2430" stop-opacity="0.2"></stop><stop offset="1" stop-color="#1f2430" stop-opacity="0"></stop>
</radialGradient>
</defs>''')
floor_y = cam.cy + 1.262 * cam.s + 30
s.append(f'<ellipse cx="{cam.cx}" cy="{floor_y:.0f}" rx="{1.3 * cam.s:.0f}" ry="{0.13 * cam.s:.0f}" fill="url(#floor3)"></ellipse>')
svg_floor = "".join(s); s = []

deg = np.radians
# the 16 patches' boundaries: four circles round the tube, four round the ring
grid = []
for ph in (0, 90, 180, 270):
    th = np.linspace(0, 2 * np.pi, 721); phv = np.full_like(th, deg(ph))
    pts = surf(th, phv); v = visible_surface(th, phv)
    grid += [cam.path(r) for r in runs(pts, v)[0]]
for tq in (0, 90, 180, 270):
    phv = np.linspace(0, 2 * np.pi, 361); th = np.full_like(phv, deg(tq))
    pts = surf(th, phv); v = visible_surface(th, phv)
    grid += [cam.path(r) for r in runs(pts, v)[0]]
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.32" stroke-width="1.2">{paths(grid)}</g>')

# name 1's patch: its normals are draft 1's triangle
m = 40
edge_t = np.concatenate([np.linspace(0, 90, m), np.full(m, 90), np.linspace(90, 0, m), np.zeros(m)])
edge_p = np.concatenate([np.zeros(m), np.linspace(0, 90, m), np.full(m, 90), np.linspace(90, 0, m)])
pts = surf(deg(edge_t), deg(edge_p))
assert visible_surface(deg(edge_t), deg(edge_p)).all(), "patch 1 must be fully in view"
s.append(f'<path d="{cam.path(pts, True)}" fill="{ACC}" fill-opacity="0.30" stroke="{ACC}" stroke-opacity="0.55" stroke-width="1.5"></path>')

# the winding 1 -> 17
def smooth(u):
    u = np.clip(u, 0, 1); return u * u * (3 - 2 * u)
T = np.linspace(0, 16, 3201)
th_w = deg(45 + 90 * T)
ph_w = deg(45 + 90 * (np.floor(np.minimum(T, 15.9999) / 4) + smooth(np.mod(np.minimum(T, 15.9999), 4) - 3)))
ph_w[-1] = deg(45 + 360)
wp = surf(th_w, ph_w); wv = visible_surface(th_w, ph_w)
f, b = runs(wp, wv)
s.append(f'<g fill="none" stroke="{ACC}" stroke-opacity="0.32" stroke-width="1.4" stroke-dasharray="4 6">{paths([cam.path(r) for r in b])}</g>')
s.append(f'<g fill="none" stroke="{ACC}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">{paths([cam.path(r) for r in f])}</g>')

# arrowheads at visible half-steps
heads = []
for k in range(16):
    i = int(round((k + 0.5) / 16 * (len(T) - 1)))
    if wv[max(i - 3, 0): i + 4].all():
        (xa, ya), (xb, yb) = cam.proj(wp[i - 3]), cam.proj(wp[i + 3])
        ang = np.arctan2(yb - ya, xb - xa); xm, ym = cam.proj(wp[i])
        tip = (xm + 7 * np.cos(ang), ym + 7 * np.sin(ang))
        l = (xm + 7 * np.cos(ang + 2.5), ym + 7 * np.sin(ang + 2.5))
        r_ = (xm + 7 * np.cos(ang - 2.5), ym + 7 * np.sin(ang - 2.5))
        heads.append(f'M{tip[0]:.1f},{tip[1]:.1f} L{l[0]:.1f},{l[1]:.1f} L{r_[0]:.1f},{r_[1]:.1f} Z')
s.append(f'<g fill="{ACC}">' + "".join(f'<path d="{h}"></path>' for h in heads) + '</g>')

# axes through the empty 0
def axis_runs(p0, p1, n=600):
    tt = np.linspace(0, 1, n)[:, None]
    P = p0 + tt * (p1 - p0)
    inside = sdf(P) < 0
    v = ~inside & ~occluded(P, start=0.002)
    return runs(P, v)
zf, _ = axis_runs(np.array([0, 0, -1.25]), np.array([0, 0, 1.52]))
xf, _ = axis_runs(np.array([-1.78, 0, 0]), np.array([1.95, 0, 0]))
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.5" stroke-dasharray="7 6">{paths([cam.path(r) for r in zf])}</g>')
s.append(f'<g fill="none" stroke="{INK}" stroke-opacity="0.8" stroke-width="1.8" stroke-dasharray="2 5" stroke-linecap="round">{paths([cam.path(r) for r in xf])}</g>')

# the me at the 0
O = np.zeros(3)
o_vis = not occluded(O[None], start=0.002)[0]
ox, oy = cam.proj(O)
s.append(f'<circle cx="{ox:.1f}" cy="{oy:.1f}" r="6.5" fill="{INK}" fill-opacity="{1 if o_vis else 0.35}" stroke="#ffffff" stroke-width="2"></circle>')

# name dots
names_xy, names_vis = {}, {}
for n in range(1, 17):
    k = n - 1; j, q = k >> 2, k & 3
    th, ph = deg(45 + 90 * q), deg(45 + 90 * j)
    P = surf(th, ph); v = bool(visible_surface(np.array([th]), np.array([ph]))[0])
    x, y = cam.proj(P); names_xy[n] = (x, y); names_vis[n] = v
    if v:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{ACC}" stroke="#ffffff" stroke-width="2"></circle>')
    else:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#ffffff" fill-opacity="0.7" stroke="{ACC}" stroke-opacity="0.6" stroke-width="1.8" stroke-dasharray="3 2"></circle>')

svg = (f'<svg role="img" aria-label="A torus with its surface cut into sixteen patches, four around its hole and four around its tube. '
       f'A winding runs from name 1 through 16 round the hole four times, outer top, inner top, inner bottom, outer bottom, and comes back to 1 as 17. '
       f'Name 1&#39;s patch is shaded; a dotted line through the empty centre is the half-turn that carries each name n onto 17 less n." '
       f'width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
       + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
svg_floor = (f'<svg aria-hidden="true" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">'
             + svg_floor + "</svg>")

if __name__ == "__main__":
    png = os.path.join(OUT, "torus_body@2x.png")
    bx, by, bw, bh = render_body(png)
    blob = sys.argv[1] if len(sys.argv) > 1 else "/_blob/f85c1701f5031cf94c3b94a0b3f05b78"   # the canvas's upload of torus_body@2x.png; a new canvas gives its own
    img = f'<img src="{blob}" alt="" style="position: absolute; left: {bx}px; top: {by}px; width: {bw}px; height: {bh}px">'

    NUM = "font-family: Inter, system-ui, sans-serif; font-weight: 600; font-size: 17px"
    labels = []
    for n, (x, y) in names_xy.items():
        col = INK if names_vis[n] else "#7d8494"
        txt = "1 · 17" if n == 1 else str(n)
        w = 62 if n == 1 else 30
        dx = 14 + w / 2 if n != 1 else -(14 + w / 2)
        labels.append(html_box(x + dx, y - 13, w, 22, f"{NUM}; color: {col}", txt))
    NOTE = "font-family: Inter, system-ui, sans-serif; font-weight: 400; font-size: 15px; color: #4a5160"
    labels.append(html_box(ox + 40, oy + 2, 60, 22, f"{NUM}; color: {INK}", "me · 0"))
    zt = cam.proj(np.array([0, 0, 1.52])); xt = cam.proj(np.array([1.95, 0, 0]))
    labels.append(html_box(zt[0] - 96, zt[1] + 4, 170, 20, NOTE + "; text-align: right", "the line of the turn"))
    labels.append(html_box(1000, 790, 300, 20, NOTE + "; text-align: right",
                           "shaded: name 1&#39;s patch, facing as + + +"))
    labels.append(html_box(xt[0] - 70, xt[1] + 18, 200, 20, NOTE, "17 less: a half-turn"))

    title = (f'<div style="position: absolute; left: 64px; top: 846px; width: {W - 128}px; text-align: center; '
             f'font-family: Inter, system-ui, sans-serif; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">'
             f'1 to 17 resolving on a torus&#39;s outside surface</div>')
    caption = (f'<div style="position: absolute; left: 64px; top: 894px; width: {W - 128}px; text-align: center; '
               f'font-family: Inter, system-ui, sans-serif; font-weight: 400; font-size: 19px; line-height: 28px; color: #4a5160">'
               f'Each name is n − 1 in four parities: two round the tube, two round the hole. The winding closes at 17, the next 1.<br>'
               f'Outside +720°, the sphere&#39;s eight right-angle triangles; inside −720°: a torus at nought.</div>')

    props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT,
                        "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]},
             "$preview": {"width": W, "height": H}}
    body = svg_floor + "\n" + img + "\n" + svg + "\n" + "".join(labels) + "\n" + title + "\n" + caption
    html = page("1 to 17 on a torus", W, H, body, json.dumps(props, ensure_ascii=False))
    root = OUT
    open(f"{root}/Draft3.dc.html", "w").write(html)

    # working preview of the drawing (body + lines + label places), for drafting
    pv = svg.replace("{{accent}}", DEFAULT_ACCENT).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" ', 1)
    pv = pv.replace("</svg>", "")
    import re, base64
    b64 = base64.b64encode(open(png, "rb").read()).decode()
    pv = pv.replace('<defs>', f'<image href="data:image/png;base64,{b64}" x="{bx}" y="{by}" width="{bw}" height="{bh}"></image><defs>', 1) if '<defs>' in pv else \
        pv.replace('">', f'"><image href="data:image/png;base64,{b64}" x="{bx}" y="{by}" width="{bw}" height="{bh}"></image>', 1)
    for mm in re.finditer(r'left: (-?\d+)px; top: (-?\d+)px; width: (\d+)px; height: (\d+)px;[^>]*color: (#[0-9a-f]+)[^>]*>([^<]*)</div>', "".join(labels)):
        l, t, w, h, c, txt = mm.groups()
        pv += f'<text x="{int(l) + int(w) / 2}" y="{int(t) + int(h) / 2 + 6}" font-size="16" font-weight="600" text-anchor="middle" font-family="sans-serif" fill="{c}">{txt}</text>'
    open(os.path.join(WORK, "preview3.svg"), "w").write(pv + "</svg>")
    print("png", os.path.getsize(png), "html", len(html), "| visible names:", [n for n in names_vis if names_vis[n]], "| 0 visible:", o_vis)
