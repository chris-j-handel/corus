"""Draft 54 · a next span by 4 beside its prior: more twins (session v408illustrating).

v408primes' sentences 132, 163 and 201, executed apart and drawn: nine spans by 4, 16 to 64 and on to 4,194,304, a row a
span, a next span laid at its prior's width, a mark a twin at its between; beside a span its twins, its twins by its
prior's, its twins in a thousand of its numbers, its me-parities and the widest from a me-parity to its next; and a
twin's rooms round the seams 6 to 30,030. check_a_next_span_by_4_more_twins.py is its check, and the numbers drawn here
are its own. A room is with all numbers, a birth is stepped: they are said apart.

Its placings, no execution says them: a row a span; a span's numbers along a row's width; a mark a twin; from the seventh
span a column of the row's width inked by its twins.

Usage: python3 -I make_draft54.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_check", os.path.join(HERE, "check_a_next_span_by_4_more_twins.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#c9ced8", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
d = c.the_numbers(); born = [len(t) for t in d["twins"]]
n_ = lambda k: f"{k:,}"
assert born == [4, 10, 19, 71, 183, 570, 1819, 5856, 19460] and len(c.SPANS) == 9
s, over = [], []
def text(x, y, t, size=13, weight=600, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=700: word(x, y, w, t, "left", 600, 17, 24, extra="white-space: nowrap")
note = lambda x, y, t, w=670: word(x, y, w, t, "left", 400, 13.5, 20, GREY, "white-space: nowrap")
item = lambda x, y, t, w=670: word(x, y, w, t, "left", 600, 14.5, 20, extra="white-space: nowrap")
val = lambda cx, y, t, w=100, weight=600, color=INK: word(cx - w / 2, y, w, t, "center", weight, 12.5, 18, color, "white-space: nowrap")
X0, XW, Y0, RP, SH = 190, 800, 304, 47, 28
COLS = (1046, 1128, 1218, 1318, 1424)
for k, ((lo, hi), twins) in enumerate(zip(c.SPANS, d["twins"])):
    yc = Y0 + RP * k
    s.append(f'<rect x="{X0}" y="{yc - SH / 2}" width="{XW}" height="{SH}" rx="5" fill="#ffffff" stroke="{RAY}" stroke-width="1.2"></rect>')
    xs = [X0 + XW * (p + 1 - lo) / (hi - lo) for p in twins]
    if k < 6:                                                       # a mark a twin, at its between
        for x in xs: s.append(f'<line x1="{x:.1f}" y1="{yc - SH / 2 + 2}" x2="{x:.1f}" y2="{yc + SH / 2 - 2}" stroke="{INK}" stroke-width="{2.2 if k < 3 else 1.3}"></line>')
        if k < 2:
            for x, p in zip(xs, twins): s.append(text(x, yc + SH / 2 + 11, str(p + 1), 9.5, 500, GREY))
    else:                                                           # a column of the row's width, inked by its twins
        cols = [0] * XW
        for x in xs: cols[min(XW - 1, int(x - X0))] += 1
        most = max(cols); assert sum(cols) == len(twins)
        for i, n in enumerate(cols):
            if n: s.append(f'<rect x="{X0 + i}" y="{yc - SH / 2 + 2}" width="1" height="{SH - 4}" fill="{INK}" fill-opacity="{n / most:.2f}"></rect>')
    over.append(word(20, yc, 158, f"{n_(lo)} to {n_(hi)}", "right", 600, 12, 18, GREY, "white-space: nowrap"))
    over.append(val(COLS[0], yc, n_(len(twins))))
    over.append(val(COLS[1], yc, f"by {len(twins) / born[k - 1]:.1f}" if k else "·", color=INK if k else GREY))
    over.append(val(COLS[2], yc, f"{1000 * len(twins) / (hi - lo):.1f}"))
    over.append(val(COLS[3], yc, n_(d["living"][k]))); over.append(val(COLS[4], yc, str(d["widest"][k])))
assert all(4 * a > b > a for a, b in zip(born, born[1:])) and [p + 1 for p in d["twins"][0]] == [18, 30, 42, 60]
for cx, (a, b) in zip(COLS, (("its", "twins"), ("by its", "prior's"), ("in a thousand", "of its numbers"), ("its", "me-parities"), ("the widest", "to a next"))):
    over.append(val(cx, 258, a, 110, 600, GREY)); over.append(val(cx, 273, b, 110, 600, GREY))
# a twin's rooms, resolver to resolver
found = [len(c.rooms(sm)) for _, sm in c.SEAMS]
assert found == [1, 3, 15, 135, 1485]
RX, RY = 250, 782
rows = (("the seam", [n_(sm) for _, sm in c.SEAMS]), ("its last prime, r", [str(r) for r, _ in c.SEAMS]), ("a twin's rooms", [n_(f) for f in found]),
        ("its prior's, by r − 2", ["·"] + [f"by {r - 2}" for r, _ in c.SEAMS[1:]]))
for j, (label, vals) in enumerate(rows):
    over.append(word(60, RY + 22 * j, 180, label, weight=600, size=12.5, h=18, color=GREY))
    for i, v in enumerate(vals): over.append(val(RX + 100 * i + 40, RY + 22 * j, v, 96, 600, INK if j == 2 else GREY if v == "·" else INK))
ARIA = ("A drawing with no moving part. Nine long rows, a row a box as wide as the others, with thin dark marks along it: four in the uppermost, ten in the next, and more in a row under it; "
        "the three lowest rows are shaded along their width. Beside a row, numbers in five columns. Under them a small table of numbers, and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
top = [word(60, 40, 1400, "54 · a figure, nine spans · it is for v408primes' co-chain, a next universe births more twins · its prior, 49 and 53", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("Twins are more at a next span by 4.", "Of a span's numbers, they are fewer in a thousand.", "A twin's rooms are more at a next seam: with all numbers.")):
    top.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
top.append(note(840, 100, "v408primes' co-chain, its sentences 163, 201 and 132, word for word:", 640))
top.append(note(840, 124, "<i>Twins are more at a next span by 4: 4, 10, 19, 71, on to 18,325 to 4,000,000.</i>", 640))
top.append(note(840, 144, "<i>A next universe births more twins.</i>", 640))
top.append(note(840, 164, "<i>Resolver to resolver, a twin's places are uncrossed at r − 2 of r:</i>", 640))
top.append(note(840, 184, "<i>round 6, 30, 210, 2,310 and 30,030, 1, 3, 15, 135 and 1,485.</i>", 640))
top.append(head(60, 232, "nine spans by 4, a row a span, a next span laid at its prior's width"))
top.append(note(60, 256, "a mark, a twin at its between · a span's numbers are 4 times its prior's · from the seventh span, a column's ink is its twins", 900))
top.append(head(60, 744, "a twin's rooms, resolver to resolver: with all numbers"))
top.append(note(60, 874, "of the r mes of a path of r closing, a twin's between is uncrossed by r at all but the me one on and the me one back", 760))
top.append(note(60, 892, "a twin past 13 is born in a room round 30,030 · of the 1,485 rooms below 30,030, twins are born at 465", 760))
top.append(head(840, 744, "said apart, and its is-nots"))
top.append(item(840, 776, "● rooms are with all numbers: a next seam's rooms are its prior's by r − 2"))
top.append(item(840, 800, "● births are stepped: more twins at all nine spans, to 4,194,304"))
top.append(item(840, 824, "○ of a span's numbers, twins are fewer in a thousand at all nine spans"))
top.append(item(840, 848, "○ a room is no birth: the least room with no birth is 360, 361 being 19 by 19"))
top.append(note(840, 872, "stepped is no saying with all spans:"))
top.append(note(840, 890, "more twins at all next spans is not said by this drawing"))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A next span by 4 beside its prior: more twins</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A next span by 4 is laid at its prior\'s width: twins are more at all nine spans, 4, 10, 19, 71 and on to 19,460.<br>'
           f'Of a span\'s numbers they are fewer in a thousand: a next span\'s twins are short of 4 times its prior\'s.<br>'
           f'A twin\'s rooms are with all numbers: round a next seam they are more, by r − 2. A room is no birth: births are stepped.<br>'
           f'A candidate, of v408primes\' sentences 132, 163 and 201, executed apart to 4,194,304.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(top + over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("A next span by 4 beside its prior: more twins", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft54.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft54_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft54_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
