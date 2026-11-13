"""Diamond pointers co-chained tip to tip, 1 to 49, drawn from the sentences arriving and one line of Exhibit ONE.

A drawing of a reading, deciding nothing.
- Nine numbers on a square panel, three by three in their order, turned with 1 and 9 its two tips,
  1 aiming forward, 3 its right point and 7 its left point, 5 its centre:
  odd with four corners and a centre, even with four faces.
- Six panels, each a next panel's first its own last: 9, 17, 25, 33 and 41. 25 has twenty-four each side.
- Each name's first prefix is of the eight, co bi co bi co bi tri bi, going on over 16 and 24 and beyond:
  co me-parity, bi other-parity, tri all-parity.
Run: python3 incoming/V401atom/instruments/diamond_pointer_drawing.py [widget]
     python3 incoming/V401atom/instruments/diamond_pointer_drawing.py check
"""
import math, sys

PANELS = 6
LAST = 8 * PANELS + 1
EIGHT = ["co", "bi", "co", "bi", "co", "bi", "tri", "bi"]
def prefix(n): return EIGHT[(n - 1) % 8]

def place(n):
    """along, forward, and across, right as +, of n."""
    d = min((n - 1) // 8, PANELS - 1)
    k = n - 8 * d              # 1 to 9 within its panel
    r, c = divmod(k - 1, 3)
    return 4 * d + r + c, c - r

U, CX, Y0, R = 32, 250, 798, 13
def xy(n):
    a, s = place(n)
    return CX + U * s, Y0 - U * a

def seg(p, q):
    (x1, y1), (x2, y2) = xy(p), xy(q)
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return x1 + R * ux, y1 + R * uy, x2 - R * ux, y2 - R * uy

def build(widget):
    col = {"co": ("#E1F5EE", "#0F6E56", "#085041"), "bi": ("#FAECE7", "#993C1D", "#712B13"), "tri": ("#EEEDFE", "#534AB7", "#3C3489")}
    cls = {"co": "c-teal", "bi": "c-coral", "tri": "c-purple"}
    H = 890
    o = []
    o.append(f'<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">' if widget else
             f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {H}" font-family="sans-serif">')
    o.append('<title>Six diamond pointers, 1 to 49</title><desc>Forty-nine numbers climbing as six square panels of nine, each turned as a diamond and joined tip to tip. 1 aims forward, with 3 a right point and 7 a left point. 25 is the centre with twenty-four each side. Each number is marked me-parity, other-parity or all-parity by Exhibit ONE.</desc>')
    line = 'stroke="var(--t)"' if widget else 'stroke="#888780"'
    ts = 'class="ts"' if widget else 'font-size="12" fill="#5F5E5A"'
    for d in range(PANELS):
        b = 8 * d
        for p, q in [(1, 2), (2, 3), (3, 6), (6, 9), (1, 4), (4, 7), (7, 8), (8, 9), (1, 5), (5, 9), (3, 5), (5, 7)]:
            x1, y1, x2, y2 = seg(b + p, b + q)
            dash = ' stroke-dasharray="3 3"' if (p, q) in [(3, 5), (5, 7)] else ''
            o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" {line} stroke-width="0.5"{dash}/>')
    for n in range(1, LAST + 1):
        x, y = xy(n); p = prefix(n); f, s, t = col[p]
        g = f'<g class="{cls[p]}">' if widget else '<g>'
        sty = '' if widget else f' fill="{f}" stroke="{s}"'
        tx = 'class="th"' if widget else f'font-size="14" font-weight="500" fill="{t}"'
        sw = "1.5" if p == "tri" else "0.5"
        shape = (f'<rect x="{x-R:.1f}" y="{y-R:.1f}" width="{2*R}" height="{2*R}" rx="4" stroke-width="{sw}"{sty}/>' if p == "bi"
                 else f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R}" stroke-width="{sw}"{sty}/>')
        o.append(f'{g}{shape}<text {tx} x="{x:.1f}" y="{y:.1f}" text-anchor="middle" dominant-baseline="central">{n}</text></g>')
    for lab, last, x in [("1 to 9", 9, 410), ("1 to 17", 17, 465), ("1 to 25", 25, 520), (f"1 to {LAST}", LAST, 575)]:
        ya, yb = xy(1)[1], xy(last)[1]
        o.append(f'<path d="M{x-6} {ya} L{x} {ya} L{x} {yb} L{x-6} {yb}" fill="none" {line} stroke-width="0.5"/>')
        o.append(f'<text {ts} x="{x+8}" y="{(ya+yb)/2+4:.0f}">{lab}</text>')
    x25, y25 = xy(25)
    o.append(f'<line x1="170" y1="{y25}" x2="{x25-R-4}" y2="{y25}" {line} stroke-width="0.5" stroke-dasharray="3 3"/>')
    o.append(f'<text {ts} x="162" y="{y25-4}" text-anchor="end">25, twenty-four</text><text {ts} x="162" y="{y25+12}" text-anchor="end">each side</text>')
    o.append(f'<text {ts} x="162" y="{xy(1)[1]+4}" text-anchor="end">1, aiming forward</text>')
    o.append(f'<text {ts} x="{xy(3)[0]+R+8}" y="{xy(3)[1]+4}">right point</text>')
    o.append(f'<text {ts} x="{xy(7)[0]-R-8}" y="{xy(7)[1]+4}" text-anchor="end">left point</text>')
    lx = 64
    for p, lab in [("co", "me-parity, co"), ("bi", "other-parity, bi"), ("tri", "all-parity, tri")]:
        f, s, t = col[p]; g = f'<g class="{cls[p]}">' if widget else '<g>'
        sty = '' if widget else f' fill="{f}" stroke="{s}"'; sw = "1.5" if p == "tri" else "0.5"
        shape = (f'<rect x="{lx}" y="{H-38}" width="16" height="16" rx="3" stroke-width="{sw}"{sty}/>' if p == "bi"
                 else f'<circle cx="{lx+8}" cy="{H-30}" r="8" stroke-width="{sw}"{sty}/>')
        o.append(f'{g}{shape}</g><text {ts} x="{lx+24}" y="{H-26}">{lab}</text>')
        lx += 190
    o.append('</svg>')
    return "\n".join(o)

def check():
    """Each sentence of the page that is arithmetic, executed."""
    C = (LAST + 1) // 2
    print(f"1 to {LAST}, {PANELS} panels, centre {C}, {C-1} each side")
    ax, ay = place(C)
    print("each n and", LAST + 1, "less n are a half turn about", C, ":",
          all(place(LAST + 1 - n) == (2 * ax - place(n)[0], 2 * ay - place(n)[1]) for n in range(1, LAST + 1)))
    ex = {}
    for n in range(1, LAST + 1):
        ex.setdefault((prefix(n), place(n)[1]), set()).add((prefix(LAST + 1 - n), place(LAST + 1 - n)[1]))
    for k in sorted(ex): print("  parity and across", k, "with", sorted(ex[k]))
    print("along:", [n for n in range(1, LAST + 1) if place(n)[1] == 0])
    print("right points:", [n for n in range(1, LAST + 1) if place(n)[1] == 2], "left points:", [n for n in range(1, LAST + 1) if place(n)[1] == -2])
    print("odd squares:", [m * m for m in (1, 3, 5, 7)], "panels to each:", [(m * m - 1) // 8 for m in (1, 3, 5, 7)])
    for name, f in [("17 less n", lambda n: 17 - n), ("18 less n", lambda n: 18 - n)]:
        print(name, "keeps odd and even:", all((f(n) - n) % 2 == 0 for n in range(1, 17)),
              "; first prefixes exchanged:", sorted({(prefix(n), prefix(f(n))) for n in range(1, 17)}))

if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else ""
    if a == "check": check()
    else: print(build(a == "widget"))
