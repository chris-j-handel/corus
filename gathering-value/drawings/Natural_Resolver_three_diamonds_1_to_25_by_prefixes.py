"""Three diamonds of the names' numbers, 1 to 25, each number with its three prefixes only.

A candidate drawing for Exhibit ONE Natural Resolver, deciding nothing.
- Nine numbers on a square, three by three in their order, turned with 1 and 9 its two tips:
  1 aiming forward, 3 its right point, 7 its left point, 5 its centre.
- Each diamond's last is its next diamond's first: 9 and 17.
- Each number's first prefix is of the eight, co bi co bi co bi tri bi, going on.
  Its three is its own first prefix, then the first prefix of the number before it, then of the one before that:
  next, now, prior. Co is me, bi is both, tri is all.
- Each is-or-is-not of Exhibit ONE's code is marked on the name it is on: 3, 4, 7, 13 and 15.
  What they give is marked on 14 and 12: from 7 and 15, over 2, into 14; from 3, with 15 and 7, into 12.
Run: python3 -I gathering-value/drawings/Natural_Resolver_three_diamonds_1_to_25_by_prefixes.py > gathering-value/drawings/Natural_Resolver_three_diamonds_1_to_25_by_prefixes.svg
     python3 -I gathering-value/drawings/Natural_Resolver_three_diamonds_1_to_25_by_prefixes.py check
"""
import sys

PANELS = 3
LAST = 8 * PANELS + 1
EIGHT = ["co", "bi", "co", "bi", "co", "bi", "tri", "bi"]


def prefix(n):
    return EIGHT[(n - 1) % 8]


def three(n):
    return "-".join(prefix(n - k) for k in range(3))


def place(n):
    """along, forward, and across, right as +, of n."""
    d = min((n - 1) // 8, PANELS - 1)
    k = n - 8 * d
    r, c = divmod(k - 1, 3)
    return 4 * d + r + c, c - r


U, CX, W2, H2 = 60, 340, 34, 19          # unit, centre line, half width and half height of a mark
TOP = 70
Y0 = TOP + U * 4 * PANELS + H2
HEIGHT = Y0 + H2 + 150
COL = {"co": ("#E1F5EE", "#0F6E56", "#085041"), "bi": ("#FAECE7", "#993C1D", "#712B13"), "tri": ("#EEEDFE", "#534AB7", "#3C3489")}
IS_OR_IS_NOT = [3, 4, 7, 13, 15]
GIVEN = [12, 14]


def xy(n):
    a, s = place(n)
    return CX + U * s, Y0 - U * a


def build():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 {HEIGHT}" font-family="sans-serif">',
         '<title>Three diamonds, 1 to 25, by prefixes</title>',
         '<desc>Twenty-five numbers going forward as three squares of nine, each turned as a diamond and joined tip to tip. '
         'Each number has its three prefixes, next, now, prior: co is me, bi is both, tri is all. '
         'Each is-or-is-not of the code is marked on the name it is on.</desc>',
         f'<rect x="0" y="0" width="680" height="{HEIGHT}" fill="#FFFFFF"/>',
         '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         '<path d="M0 0 L10 5 L0 10 z" fill="#B4530A"/></marker></defs>']
    for d in range(PANELS):
        b = 8 * d
        for p, q in [(1, 2), (2, 3), (3, 6), (6, 9), (1, 4), (4, 7), (7, 8), (8, 9), (1, 5), (5, 9), (3, 5), (5, 7)]:
            (x1, y1), (x2, y2) = xy(b + p), xy(b + q)
            dash = ' stroke-dasharray="4 4"' if (p, q) in [(3, 5), (5, 7)] else ''
            o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#B4B2A9" stroke-width="1"{dash}/>')
    for n in range(1, LAST + 1):
        x, y = xy(n)
        p = prefix(n)
        f, s, t = COL[p]
        sw = 2.5 if p == "tri" else 1
        rx = 4 if p == "bi" else H2
        if n in IS_OR_IS_NOT:
            o.append(f'<rect x="{x - W2 - 5}" y="{y - H2 - 5}" width="{2 * W2 + 10}" height="{2 * H2 + 10}" rx="{rx + 5}" fill="none" stroke="#B4530A" stroke-width="2" stroke-dasharray="5 3"/>')
        if n in GIVEN:
            o.append(f'<rect x="{x - W2 - 5}" y="{y - H2 - 5}" width="{2 * W2 + 10}" height="{2 * H2 + 10}" rx="{rx + 5}" fill="none" stroke="#B4530A" stroke-width="2"/>')
        o.append(f'<rect x="{x - W2}" y="{y - H2}" width="{2 * W2}" height="{2 * H2}" rx="{rx}" fill="{f}" stroke="{s}" stroke-width="{sw}"/>')
        o.append(f'<text x="{x}" y="{y - 3}" text-anchor="middle" font-size="14" font-weight="700" fill="{t}">{n}</text>')
        o.append(f'<text x="{x}" y="{y + 12}" text-anchor="middle" font-size="11" fill="{t}">{three(n)}</text>')
    g = 'font-size="13" fill="#444441"'
    x1, y1 = xy(1)
    o.append(f'<text {g} x="{x1 + W2 + 10}" y="{y1 + 5}">1, aiming forward</text>')
    x3, y3 = xy(3)
    o.append(f'<text {g} x="{x3 + W2 + 12}" y="{y3 + 5}">right point</text>')
    x7, y7 = xy(7)
    o.append(f'<text {g} x="{x7 - W2 - 12}" y="{y7 + 5}" text-anchor="end">left point</text>')
    for lab, last in [("1 to 9", 9), ("9 to 17", 17), ("17 to 25", 25)]:
        ya, yb = xy(last - 8)[1], xy(last)[1]
        o.append(f'<path d="M604 {ya} L610 {ya} L610 {yb} L604 {yb}" fill="none" stroke="#B4B2A9" stroke-width="1"/>')
        o.append(f'<text {g} x="618" y="{(ya + yb) / 2 + 4}">{lab}</text>')
    o.append(f'<text x="340" y="34" text-anchor="middle" font-size="16" font-weight="700" fill="#2C2C2A">Three diamonds, 1 to 25, by prefixes</text>')
    o.append(f'<text {g} x="340" y="54" text-anchor="middle">each number with its three: next, now, prior</text>')
    ly = Y0 + H2 + 40
    lx = 40
    for p, lab in [("co", "co, me"), ("bi", "bi, both"), ("tri", "tri, all")]:
        f, s, t = COL[p]
        sw = 2.5 if p == "tri" else 1
        rx = 4 if p == "bi" else 10
        o.append(f'<rect x="{lx}" y="{ly - 10}" width="34" height="20" rx="{rx}" fill="{f}" stroke="{s}" stroke-width="{sw}"/>')
        o.append(f'<text {g} x="{lx + 44}" y="{ly + 5}">{lab}</text>')
        lx += 118
    o.append(f'<rect x="{lx}" y="{ly - 10}" width="34" height="20" rx="10" fill="none" stroke="#B4530A" stroke-width="2" stroke-dasharray="5 3"/>')
    o.append(f'<text {g} x="{lx + 44}" y="{ly + 5}">an is-or-is-not</text>')
    lx += 150
    o.append(f'<rect x="{lx}" y="{ly - 10}" width="34" height="20" rx="4" fill="none" stroke="#B4530A" stroke-width="2"/>')
    o.append(f'<text {g} x="{lx + 44}" y="{ly + 5}">what it gives</text>')
    o.append(f'<text {g} x="40" y="{ly + 40}">An is-or-is-not is on 3, 4, 7, 13 and 15.</text>')
    o.append(f'<text {g} x="40" y="{ly + 60}">From 7 and 15, over 2, into 14. From 3, with 15 and 7, into 12.</text>')
    o.append(f'<text {g} x="40" y="{ly + 80}">The eight, co bi co bi co bi tri bi, is going on from 17, with no names of its own.</text>')
    o.append('</svg>')
    return "\n".join(o)


def check():
    living = {1: "co-bi-tri", 2: "bi-co-bi", 3: "co-bi-co", 4: "bi-co-bi", 5: "co-bi-co", 6: "bi-co-bi", 7: "tri-bi-co",
              8: "bi-tri-bi", 9: "co-bi-tri", 10: "bi-co-bi", 11: "co-bi-co", 12: "bi-co-bi", 13: "co-bi-co",
              14: "bi-co-bi", 15: "tri-bi-co", 16: "bi-tri-bi", 17: "co-bi-tri"}
    print("each three of 1 to 17 as Exhibit ONE's table has it:", all(three(n) == living[n] for n in living))
    print("each odd number has bi in its middle:", all(three(n).split("-")[1] == "bi" for n in range(1, LAST + 1, 2)))
    print("each even number has bi first and last:", all(three(n).split("-")[0] == "bi" == three(n).split("-")[2] for n in range(2, LAST + 1, 2)))
    print("along:", [n for n in range(1, LAST + 1) if place(n)[1] == 0])
    print("right points:", [n for n in range(1, LAST + 1) if place(n)[1] == 2], "left points:", [n for n in range(1, LAST + 1) if place(n)[1] == -2])
    print("right faces:", [n for n in range(1, LAST + 1) if place(n)[1] == 1], "left faces:", [n for n in range(1, LAST + 1) if place(n)[1] == -1])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        check()
    else:
        print(build())
