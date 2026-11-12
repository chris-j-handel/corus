"""One turn of a right spiral climb, 1 to 9, in two views. A drawing of a reading, deciding nothing.

The reading: each even number is one step right across one face of a square, and each odd number one step along;
four of each are one turn, and 9 is above 1. Its centre seen along its line is a hole; seen from its side it is 5.
Each mark is by Exhibit ONE's eight, co bi co bi co bi tri bi: co me-parity, bi other-parity, tri all-parity.
Run: python3 incoming/V401atom/instruments/spiral_turn_drawing.py [widget]
"""
import sys
EIGHT = ["co", "bi", "co", "bi", "co", "bi", "tri", "bi"]
def prefix(n): return EIGHT[(n - 1) % 8]
R = 12

def build(widget):
    col = {"co": ("#E1F5EE", "#0F6E56", "#085041"), "bi": ("#FAECE7", "#993C1D", "#712B13"), "tri": ("#EEEDFE", "#534AB7", "#3C3489")}
    cls = {"co": "c-teal", "bi": "c-coral", "tri": "c-purple"}
    line = 'stroke="var(--t)"' if widget else 'stroke="#888780"'
    ts = 'class="ts"' if widget else 'font-size="12" fill="#5F5E5A"'
    H = 400
    o = [f'<svg width="100%" viewBox="0 0 680 {H}" role="img" xmlns="http://www.w3.org/2000/svg">' if widget else
         f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {H}" font-family="sans-serif">']
    o.append('<title>One turn of a right spiral climb, two views</title><desc>Nine numbers as one turn: each even number a step right across one face of a square, each odd number a step along. Seen along its line it is a square of four corners and four faces about a hole. Seen from its side, 1 is lowest, 9 highest, 3 a right point, 7 a left point and 5 its centre.</desc>')
    def ln(x1, y1, x2, y2, dash=False):
        o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {line} stroke-width="0.5"' + (' stroke-dasharray="3 3"' if dash else '') + '/>')
    def dot(n, x, y):
        p = prefix(n); f, s, t = col[p]
        g = f'<g class="{cls[p]}">' if widget else '<g>'
        sty = '' if widget else f' fill="{f}" stroke="{s}"'
        tx = 'class="th"' if widget else f'font-size="14" font-weight="500" fill="{t}"'
        sw = "1.5" if p == "tri" else "0.5"
        shape = (f'<rect x="{x-R}" y="{y-R}" width="{2*R}" height="{2*R}" rx="4" stroke-width="{sw}"{sty}/>' if p == "bi"
                 else f'<circle cx="{x}" cy="{y}" r="{R}" stroke-width="{sw}"{sty}/>')
        o.append(f'{g}{shape}<text {tx} x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central">{n}</text></g>')
    # seen along its line: four corners, four faces, a hole
    F, Rt, B, L = (160, 290), (260, 190), (160, 90), (60, 190)
    corners = [F, Rt, B, L, F]
    for i in range(4):
        (x1, y1), (x2, y2) = corners[i], corners[i + 1]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ux, uy = (x2 - x1) / 141.42, (y2 - y1) / 141.42
        ln(round(x1 + R * ux, 1), round(y1 + R * uy, 1), round(mx - 17 * ux, 1), round(my - 17 * uy, 1), dash=i in (1, 2))
        ln(round(mx + 17 * ux, 1), round(my + 17 * uy, 1), round(x2 - R * ux, 1), round(y2 - R * uy, 1), dash=i in (1, 2))
    o.append(f'<circle cx="160" cy="190" r="14" fill="none" {line} stroke-width="0.5" stroke-dasharray="3 3"/>')
    o.append(f'<text {ts} x="160" y="166" text-anchor="middle">a hole</text>')
    for n, (x, y) in [(1, F), (2, (210, 240)), (3, Rt), (4, (210, 140)), (5, B), (6, (110, 140)), (7, L), (8, (110, 240))]:
        dot(n, x, y)
    o.append(f'<text {ts} x="160" y="322" text-anchor="middle">1, with 9 above it</text>')
    o.append(f'<text {ts} x="160" y="352" text-anchor="middle">seen along its line</text>')
    # seen from its side: a step right, a step along
    ln(532, 300, 548, 300); ln(572, 300, 600, 300); ln(600, 300, 600, 257)
    ln(588, 245, 572, 245, True); ln(548, 245, 520, 245, True); ln(520, 245, 520, 202, True)
    ln(508, 190, 492, 190, True); ln(468, 190, 440, 190, True); ln(440, 190, 440, 147)
    ln(452, 135, 468, 135); ln(492, 135, 520, 135); ln(520, 135, 520, 92)
    for n, (x, y) in [(1, (520, 300)), (2, (560, 300)), (3, (600, 245)), (4, (560, 245)), (5, (520, 190)), (6, (480, 190)), (7, (440, 135)), (8, (480, 135)), (9, (520, 80))]:
        dot(n, x, y)
    o.append(f'<text {ts} x="600" y="222" text-anchor="middle">right point</text>')
    o.append(f'<text {ts} x="420" y="139" text-anchor="end">left point</text>')
    o.append(f'<text {ts} x="520" y="330" text-anchor="middle">far side dashed</text>')
    o.append(f'<text {ts} x="520" y="352" text-anchor="middle">seen from its side</text>')
    lx = 64
    for p, lab in [("co", "me-parity, co"), ("bi", "other-parity, bi"), ("tri", "all-parity, tri")]:
        f, s, t = col[p]; g = f'<g class="{cls[p]}">' if widget else '<g>'
        sty = '' if widget else f' fill="{f}" stroke="{s}"'; sw = "1.5" if p == "tri" else "0.5"
        shape = (f'<rect x="{lx}" y="{H-28}" width="16" height="16" rx="3" stroke-width="{sw}"{sty}/>' if p == "bi"
                 else f'<circle cx="{lx+8}" cy="{H-20}" r="8" stroke-width="{sw}"{sty}/>')
        o.append(f'{g}{shape}</g><text {ts} x="{lx+24}" y="{H-16}">{lab}</text>')
        lx += 190
    o.append('</svg>')
    return "\n".join(o)

if __name__ == "__main__":
    print(build(len(sys.argv) > 1 and sys.argv[1] == "widget"))
