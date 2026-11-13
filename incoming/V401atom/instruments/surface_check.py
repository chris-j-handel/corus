"""The names as a surface: 1 to 16 four by four, and 1 to 256 sixteen by sixteen, each sixteen a surface inside one name's place.

A check of a reading: a pair's full around as one step forward of the pair outward of it, as a surface; each name
beside names one parity apart; and a surface growing by each name's place growing a surface inside it.
Each name's parities by cycling, from n - 1 in binary, each digit is-or-is-not the same as the digit one up.
Exhibit ONE's table and its twelve forms, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/surface_check.py Exhibit_ONE_Natural_Resolver_v<version>.md [a drawing's file]
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
forms = [(kind, [int(x) for x in seq.split("-")]) for kind, seq in re.findall(r"^- \*\*Form: ([a-z -]+?) ([\d-]+)\*\*", src, re.M)]
bifoldings = [set(q) for k, q in forms if k == "bi-folding"]

def parities(n, k):
    m = n - 1
    return tuple(((m >> i) ^ (m >> (i + 1))) & 1 for i in range(k))
apart = lambda a, b, k: sum(x != y for x, y in zip(parities(a, k), parities(b, k)))
ORDER = [(0, 0), (1, 0), (1, 1), (0, 1)]          # a pair's four forms in their turn: + +, - +, - -, + -
place = lambda pair: ORDER.index(pair)

# 1 to 16, four by four: along, a name's inner pair; across, its outer pair
def cell16(n):
    p = parities(n, 4)
    return place(p[0:2]), place(p[2:4])
grid = {cell16(n): n for n in range(1, 17)}
print("1  1 to 16, four by four; each line a four-cycling, and each second line read from its other end:")
for r in range(4):
    print("     ", " ".join(f"{grid[(c, r)]:2}" for c in range(4)))
cols = [{grid[(c, r)] for r in range(4)} for c in range(4)]
print("   each line down is one of Exhibit ONE's four bi-foldings:", all(c in bifoldings for c in cols), [sorted(c) for c in cols])
def beside(c, r, size):
    return [((c + 1) % size, r), ((c - 1) % size, r), (c, (r + 1) % size), (c, (r - 1) % size)]
ok = all(apart(grid[(c, r)], grid[x], 4) == 1 for c in range(4) for r in range(4) for x in beside(c, r, 4))
allof = all({grid[x] for x in beside(c, r, 4)} == {m for m in range(1, 17) if apart(grid[(c, r)], m, 4) == 1} for c in range(4) for r in range(4))
print("   each two names beside each other, along or across, full around both ways, one parity apart:", ok)
print("   a name's four beside it are each of its names one parity apart, and no other:", allof)

# 1 to 256, sixteen by sixteen: a sixteen inside each place of the four by four, each beside its bi-folding
def cell256(n):
    p = parities(n, 8)
    c, r, C, R = place(p[0:2]), place(p[2:4]), place(p[4:6]), place(p[6:8])
    return 4 * C + (c if C % 2 == 0 else 3 - c), 4 * R + (r if R % 2 == 0 else 3 - r)
big = {cell256(n): n for n in range(1, 257)}
print("2  1 to 256, sixteen by sixteen; each place filled once:", len(big) == 256)
patch = lambda n: (cell256(n)[0] // 4, cell256(n)[1] // 4)
print("   each sixteen, 1 to 16, 17 to 32 and on, is one four by four inside one place:", all(len({patch(n) for n in range(16 * j + 1, 16 * j + 17)}) == 1 for j in range(16)))
print("   the sixteen sixteens, by their first names 1, 17, 33 and on, are placed as 1 to 16 are:", all(patch(16 * j + 1) == cell16(j + 1) for j in range(16)))
okb = all(apart(big[(c, r)], big[x], 8) == 1 for c in range(16) for r in range(16) for x in beside(c, r, 16))
print("   each two names beside each other, along or across, full around both ways, one parity apart:", okb)
within = lambda n: n - 16 * ((n - 1) // 16)          # a name's number within its sixteen, 1 to 16
facing = []                                          # each two places facing each other across a heavy line, along and across
for C in range(4):
    for R in range(4):
        for c in range(4):
            for r in range(4):
                facing.append((big[(4 * C + c, 4 * R + r)], big[(4 * ((C + 1) % 4) + 3 - c, 4 * R + r)]))
                facing.append((big[(4 * C + c, 4 * R + r)], big[(4 * C + c, 4 * ((R + 1) % 4) + 3 - r)]))
print("   each sixteen is placed as the bi-folding of each sixteen beside it: each two places facing each other have names with one same inner two pairs:",
      all(parities(a, 8)[:4] == parities(b, 8)[:4] for a, b in facing), "; their numbers within their sixteens are 17 together:", all(within(a) + within(b) == 17 for a, b in facing))
n_apart = {n: [m for m in range(1, 257) if apart(n, m, 8) == 1] for n in range(1, 257)}
inv = {v: k for k, v in big.items()}
near = lambda n: sum(1 for m in n_apart[n] if inv[m] in beside(*inv[n], 16))
print("   a name's names one parity apart:", sorted({len(v) for v in n_apart.values()}), "; of them beside it on the surface:", sorted({near(n) for n in range(1, 257)}))
firsts = [inv[16 * j + 1] for j in range(16)]
gap = lambda a, b: min(abs(a[0] - b[0]), 16 - abs(a[0] - b[0])) + min(abs(a[1] - b[1]), 16 - abs(a[1] - b[1]))
print("   the sixteen first names, 1, 17, 33 and on: two of them beside each other, along or across:", any(gap(a, b) == 1 for a in firsts for b in firsts if a != b))
print("   a sixteen's last name and the next sixteen's first, one parity apart:", all(apart(16 * j, 16 * j + 1, 8) == 1 for j in range(1, 16)),
      "; beside each other on the surface:", sum(1 for j in range(1, 16) if gap(inv[16 * j], inv[16 * j + 1]) == 1), "of 15")

# three pairs, 1 to 64: a name's six
six = {n: [m for m in range(1, 65) if apart(n, m, 6) == 1] for n in range(1, 65)}
def kind(n, m):
    a, b = parities(n, 6), parities(m, 6)
    s = next(i for i in range(3) if a[2 * i:2 * i + 2] != b[2 * i:2 * i + 2])
    return "right" if place(b[2 * s:2 * s + 2]) == (place(a[2 * s:2 * s + 2]) + 1) % 4 else "back"
print("3  1 to 64, three pairs: a name's names one parity apart:", sorted({len(v) for v in six.values()}),
      "; with each name three by a pair's step forward and three by that step backward:", all(sorted(kind(n, m) for m in six[n]) == ["back"] * 3 + ["right"] * 3 for n in six))

if len(sys.argv) > 2:                               # a drawing: the sixteen by sixteen, each sixteen with its path from its first name
    u, pad = 34, 30
    W = 16 * u + 2 * pad
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W + 62}" font-family="sans-serif">',
           f'<rect width="{W}" height="{W + 62}" fill="#ffffff"/>']
    xy = lambda n: (pad + inv[n][0] * u + u / 2, pad + inv[n][1] * u + u / 2)
    for j in range(16):
        pts = " ".join("%.1f,%.1f" % xy(n) for n in range(16 * j + 1, 16 * j + 17))
        out.append(f'<polyline points="{pts}" fill="none" stroke="#9aa7b5" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>')
        x, y = xy(16 * j + 1)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10.5" fill="#1f2a36"/>')
    for n in range(1, 257):
        x, y = xy(n)
        out.append(f'<text x="{x:.1f}" y="{y + 3.5:.1f}" font-size="9.5" text-anchor="middle" fill="{"#ffffff" if (n - 1) % 16 == 0 else "#1f2a36"}">{n}</text>')
    for i in range(17):
        w = 2.2 if i % 4 == 0 else 0.4
        out.append(f'<line x1="{pad + i * u}" y1="{pad}" x2="{pad + i * u}" y2="{pad + 16 * u}" stroke="#1f2a36" stroke-width="{w}"/>')
        out.append(f'<line x1="{pad}" y1="{pad + i * u}" x2="{pad + 16 * u}" y2="{pad + i * u}" stroke="#1f2a36" stroke-width="{w}"/>')
    for i, line in enumerate(("1 to 256, sixteen by sixteen. Each heavy square is one sixteen, its path from its first name, a dot.",
                              "Each sixteen is the bi-folding of each sixteen beside it.",
                              "Each two names beside each other are one parity apart.")):
        out.append(f'<text x="{pad}" y="{W + 6 + 17 * i}" font-size="11.5" fill="#1f2a36">{line}</text>')
    out.append("</svg>")
    open(sys.argv[2], "w", encoding="utf-8").write("\n".join(out))
    print("a drawing is written:", sys.argv[2].split("/")[-1])
