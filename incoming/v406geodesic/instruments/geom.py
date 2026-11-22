"""Shared geometry for the sphere and torus drafts: orthographic camera, SVG path helpers."""
import numpy as np

INK = "#1f2430"
GRID = "#7b8494"
DEFAULT_ACCENT = "#c2410c"
ACC = "@@ACCENT@@"   # replaced by the {{accent}} hole


class Cam:
    def __init__(self, az_deg, el_deg, cx, cy, scale):
        az, el = np.radians(az_deg), np.radians(el_deg)
        self.d = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])
        r = np.cross([0, 0, 1], self.d); self.right = r / np.linalg.norm(r)
        self.up = np.cross(self.d, self.right)
        self.cx, self.cy, self.s = cx, cy, scale

    def proj(self, p):
        p = np.asarray(p, float)
        return self.cx + self.s * (p @ self.right), self.cy - self.s * (p @ self.up)

    def depth(self, p):
        return np.asarray(p, float) @ self.d

    def path(self, pts, close=False):
        xy = [self.proj(p) for p in pts]
        s = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in xy)
        return s + (" Z" if close else "")


def runs(pts, vis):
    """Split a sampled polyline into runs of equal visibility; returns (front_runs, back_runs)."""
    front, back, cur, cv = [], [], [], None
    for p, v in zip(pts, vis):
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


def slerp(a, b, n=60):
    a, b = np.asarray(a, float), np.asarray(b, float)
    om = np.arccos(np.clip(a @ b, -1, 1))
    t = np.linspace(0, 1, n)
    return (np.sin((1 - t) * om)[:, None] * a + np.sin(t * om)[:, None] * b) / np.sin(om)


def great_circle(normal, n=361):
    normal = np.asarray(normal, float); normal /= np.linalg.norm(normal)
    a = np.cross(normal, [0.3, 0.5, 0.8]); a /= np.linalg.norm(a)
    b = np.cross(normal, a)
    t = np.linspace(0, 2 * np.pi, n)
    return np.cos(t)[:, None] * a + np.sin(t)[:, None] * b


def latitude(lat, n=181):
    t = np.linspace(0, 2 * np.pi, n); c = np.cos(lat)
    return np.stack([c * np.cos(t), c * np.sin(t), np.full_like(t, np.sin(lat))], 1)


def meridian(lon, n=91):
    t = np.linspace(-np.pi / 2, np.pi / 2, n)
    return np.stack([np.cos(t) * np.cos(lon), np.cos(t) * np.sin(lon), np.sin(t)], 1)


def paths(ds):
    return "".join(f'<path d="{x}"></path>' for x in ds)


def right_angle_mark(cam, V, P, Q, size=0.17):
    """Small spherical square in the corner at V between the directions to P and Q."""
    t1 = P - (P @ V) * V; t1 /= np.linalg.norm(t1)
    t2 = Q - (Q @ V) * V; t2 /= np.linalg.norm(t2)
    p1, p2, p3 = V + size * t1, V + size * (t1 + t2), V + size * t2
    seg = np.concatenate([np.linspace(p1, p2, 12), np.linspace(p2, p3, 12)[1:]])
    return seg / np.linalg.norm(seg, axis=1)[:, None]


def html_box(cx, cy, w, h, style, text):
    return (f'<div style="position: absolute; left: {cx - w / 2:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; '
            f'line-height: {h}px; text-align: center; {style}">{text}</div>')


FONT_LINK = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600'
             '&amp;family=STIX+Two+Text:ital,wght@1,500&amp;display=swap">')
VSTYLE = f"font-family: 'STIX Two Text', Georgia, serif; font-style: italic; font-weight: 500; font-size: 32px; color: {INK}"


def page(title, w, h, body, props_json, default_accent=DEFAULT_ACCENT):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT_LINK}
<style>
body{{margin:0}}
a{{color:#1d4ed8}}a:hover{{color:#1e3a8a}}
</style>
</helmet>
<div style="position: relative; width: {w}px; height: {h}px; overflow: hidden; background: #ffffff; font-family: Inter, system-ui, sans-serif; color: {INK}">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props_json}'>
class Component extends DCLogic {{
renderVals() {{
return {{ accent: this.props.accent ?? '{default_accent}' }};
}}
}}
</script>
</body>
</html>
'''
