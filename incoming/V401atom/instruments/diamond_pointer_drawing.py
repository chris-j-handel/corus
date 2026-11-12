"""Three diamond pointers, 1 to 9, 9 to 17 and 17 to 25, drawn from one sentence and one line of Exhibit ONE.

A drawing of a reading, deciding nothing.
- Nine numbers on a square panel, three by three in their order, turned with 1 and 9 its two tips:
  odd with four corners and a centre, even with four faces.
- Each name's first prefix is of the eight, co bi co bi co bi tri bi, going on over 16 and 24:
  co me-parity, bi other-parity, tri all-parity.
Run: python3 incoming/V401atom/instruments/diamond_pointer_drawing.py [widget]
"""
import math, sys

EIGHT = ["co", "bi", "co", "bi", "co", "bi", "tri", "bi"]
def prefix(n): return EIGHT[(n - 1) % 8]

def place(n):
    """along and across of n, with three panels of nine co-chained tip to tip."""
    d = min((n - 1) // 8, 2) if n < 25 else 2
    k = n - 8 * d              # 1 to 9 within its panel
    r, c = divmod(k - 1, 3)
    return 4 * d + r + c, c - r

U, X0, CY, R = 46, 64, 140, 16
def xy(n):
    a, s = place(n)
    return X0 + U * a, CY - U * s

def seg(p, q):
    (x1, y1), (x2, y2) = xy(p), xy(q)
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return x1 + R * ux, y1 + R * uy, x2 - R * ux, y2 - R * uy

def build(widget):
    col = {"co": ("#E1F5EE", "#0F6E56", "#085041"), "bi": ("#FAECE7", "#993C1D", "#712B13"), "tri": ("#EEEDFE", "#534AB7", "#3C3489")}
    cls = {"co": "c-teal", "bi": "c-coral", "tri": "c-purple"}
    o = []
    o.append('<svg width="100%" viewBox="0 0 680 400" role="img" xmlns="http://www.w3.org/2000/svg">' if widget else
             '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 400" font-family="sans-serif">')
    o.append('<title>Three diamond pointers, 1 to 25</title><desc>Twenty-five numbers as three square panels of nine turned as diamonds and joined tip to tip with 9 and 17. Odd numbers are with corners and centres, even numbers with faces. Each is marked me-parity, other-parity or all-parity by Exhibit ONE.</desc>')
    line = 'stroke="var(--t)"' if widget else 'stroke="#888780"'
    for d in range(3):
        b = 8 * d
        for p, q in [(1, 2), (2, 3), (3, 6), (6, 9), (1, 4), (4, 7), (7, 8), (8, 9), (1, 5), (5, 9), (3, 5), (5, 7)]:
            x1, y1, x2, y2 = seg(b + p, b + q)
            dash = ' stroke-dasharray="3 3"' if (p, q) in [(3, 5), (5, 7)] else ''
            o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" {line} stroke-width="0.5"{dash}/>')
    for n in range(1, 26):
        x, y = xy(n); p = prefix(n); f, s, t = col[p]
        g = f'<g class="{cls[p]}">' if widget else '<g>'
        sty = '' if widget else f' fill="{f}" stroke="{s}"'
        tx = 'class="th"' if widget else f'font-size="14" font-weight="500" fill="{t}"'
        sw = "1.5" if p == "tri" else "0.5"
        shape = (f'<rect x="{x-R:.1f}" y="{y-R:.1f}" width="{2*R}" height="{2*R}" rx="4" stroke-width="{sw}"{sty}/>' if p == "bi"
                 else f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R}" stroke-width="{sw}"{sty}/>')
        o.append(f'{g}{shape}<text {tx} x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="central">{n}</text></g>')
    ts = 'class="ts"' if widget else 'font-size="12" fill="#5F5E5A"'
    for lab, a0, a1, y in [("1 to 9", 0, 4, 262), ("1 to 17", 0, 8, 292), ("1 to 25", 0, 12, 322)]:
        xa, xb = X0 + U * a0, X0 + U * a1
        o.append(f'<path d="M{xa} {y-6} L{xa} {y} L{xb} {y} L{xb} {y-6}" fill="none" {line} stroke-width="0.5"/>')
        o.append(f'<text {ts} x="{xb+10 if a1 < 12 else xb}" y="{y+4 if a1 < 12 else y+18}" text-anchor="{"start" if a1 < 12 else "end"}">{lab}</text>')
    lx = 64
    for p, lab in [("co", "me-parity, co"), ("bi", "other-parity, bi"), ("tri", "all-parity, tri")]:
        f, s, t = col[p]; g = f'<g class="{cls[p]}">' if widget else '<g>'
        sty = '' if widget else f' fill="{f}" stroke="{s}"'; sw = "1.5" if p == "tri" else "0.5"
        shape = (f'<rect x="{lx}" y="362" width="16" height="16" rx="3" stroke-width="{sw}"{sty}/>' if p == "bi"
                 else f'<circle cx="{lx+8}" cy="370" r="8" stroke-width="{sw}"{sty}/>')
        o.append(f'{g}{shape}</g><text {ts} x="{lx+24}" y="374">{lab}</text>')
        lx += 190
    o.append('</svg>')
    return "\n".join(o)

if __name__ == "__main__":
    w = len(sys.argv) > 1 and sys.argv[1] == "widget"
    print(build(w))
