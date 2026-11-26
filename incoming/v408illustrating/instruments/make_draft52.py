"""Draft 52 · a me-parity living in a seam: even, odd, even (session v408illustrating).

v408primes' sentences 172 to 187, said to this session at the exchange for drawing, executed apart and drawn: eleven
me-parities, a row a me-parity, its prior, itself and its next, three cells; its even that is a seam of 4, its aim; its
even that is a seam of 6, the seam it lives in; a seam of all primes to r with its -1 and its +1; and twins, a seam with
a me-parity at both its sides. check_a_me-parity_living_in_a_seam.py is its check, and the numbers drawn here are its own.

Its placings, no execution says them: a row a me-parity; a cell a number; the tint, the dark, the accent and the mark of a seam.

Usage: python3 -I make_draft52.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("the_check", os.path.join(HERE, "check_a_me-parity_living_in_a_seam.py"))
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#c9ced8", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
d = c.the_numbers(); sieve, two = d["sieve"], d["two"]
n_ = lambda k: f"{k:,}"
MES = [p for p in range(2, 32) if sieve[p]]
assert MES == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
aim = lambda p: next((e for e in (p - 1, p + 1) if e % 4 == 0), None) if p > 2 else None
seam = lambda p: next((e for e in (p - 1, p + 1) if e % 6 == 0), None) if p > 3 else None
def agains(p):
    return next(((a * a, p - a * a) for a in range(1, p) if a * a < p and c.isqrt(p - a * a) ** 2 == p - a * a and a * a <= p - a * a), None)
# executed here again, ahead of a mark: the rows' own numbers by the check's own lists
assert all((aim(p) == p - 1) == (p in d["prior"][:12]) and (seam(p) is None or seam(p) == d["seam"][p]) and (agains(p) is not None) == bool(two[p]) for p in MES if p > 2)
assert all((agains(p) is not None) == (aim(p) == p - 1) for p in MES if p > 2) and agains(5) == (1, 4) and agains(13) == (4, 9)
s, over = [], []
def text(x, y, t, size=13, weight=600, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def cell(x, yc, w, n, dark=False, aimed=False, of6=False):
    fill = INK if dark else (TINT if n % 2 == 0 else "#ffffff")
    s.append(f'<rect x="{x + 1.5}" y="{yc - 15}" width="{w - 3}" height="30" rx="6" fill="{fill}" stroke="{ACC if aimed else (INK if dark else RAY)}" stroke-width="{2.6 if aimed else 1.2}"></rect>')
    if of6: s.append(f'<polygon points="{x + 10},{yc - 12} {x + 14.5},{yc - 7.5} {x + 10},{yc - 3} {x + 5.5},{yc - 7.5}" fill="{INK}"></polygon>')
    s.append(text(x + w / 2, yc + 4.5, n_(n), 13, 600, "#ffffff" if dark else INK))
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=670: word(x, y, w, t, "left", 400, 13.5, 20, GREY, "white-space: nowrap")
item = lambda x, y, t, w=670: word(x, y, w, t, "left", 600, 14.5, 20, extra="white-space: nowrap")
val = lambda cx, y, t, w=120, weight=600, color=INK: word(cx - w / 2, y, w, t, "center", weight, 12.5, 18, color)
CX, CW, RP, Y0 = 96, 56, 45, 352
COLS = (322, 420, 536, 652, 762)
for k, p in enumerate(MES):
    yc = Y0 + RP * k
    for j, n in enumerate((p - 1, p, p + 1)): cell(CX + CW * j, yc, CW, n, dark=(j == 1), aimed=(n == aim(p)), of6=(n == seam(p)))
    if p == 2:
        over.append(word(290, yc, 500, "odd, even, odd · <i>the one me-parity shaped as all-parity</i>, v408primes' 173", weight=600, size=12.5, h=18)); continue
    side = lambda e: "its prior" if e == p - 1 else "its next"
    over.append(val(COLS[0], yc, f"{(p - 1) // 2} · {(p + 1) // 2}"))
    over.append(val(COLS[1], yc, f"{aim(p)}, {side(aim(p))}"))
    over.append(val(COLS[2], yc, f"{agains(p)[0]} and {agains(p)[1]}" if agains(p) else "none", color=INK if agains(p) else GREY))
    over.append(val(COLS[3], yc, f"{seam(p)}, {side(seam(p))}" if seam(p) else "none", color=INK if seam(p) else GREY))
    over.append(val(COLS[4], yc, ("one even" if aim(p) == seam(p) else "its two evens") if seam(p) else "·", color=INK if seam(p) and aim(p) == seam(p) else GREY))
for j, t in enumerate(("its prior", "itself", "its next")): over.append(val(CX + CW * j + CW / 2, 318, t, 60, 600, GREY))
for cx, (a, b) in zip(COLS, (("its two evens,", "by 2"), ("its aim,", "a seam of 4"), ("two me agains", "added"), ("its seam", "of 6"), ("its aim and", "its seam"))):
    over.append(val(cx, 304, a, 120, 600, GREY)); over.append(val(cx, 319, b, 120, 600, GREY))
# a seam of all primes to r, with its -1 and its +1, by the check's own lines
TX, TY = 840, 592
table = []
for i, r in enumerate((2, 3, 5, 7, 11, 13)):
    sm = c.a_seam_of_all_primes_to(r, sieve); row = [str(r), n_(sm)]
    for side_ in (sm - 1, sm + 1):
        ps = c.parts(side_); assert all(q > r for q in ps)
        row.append(n_(side_) + ("" if len(ps) < 2 else ", " + " by ".join(n_(q) for q in ps)))
    table.append(row)
    for x, w, t in zip((TX, TX + 70, TX + 190, TX + 400), (60, 110, 200, 200), row): over.append(word(x, TY + 19 * i, w, t, weight=600, size=12.5, h=18))
assert table[2] == ["5", "30", "29", "31"] and table[3][2] == "209, 11 by 19" and table[5] == ["13", "30,030", "30,029", "30,031, 59 by 509"]
for x, w, t in zip((TX, TX + 70, TX + 190, TX + 400), (60, 110, 200, 200), ("r", "the seam", "its −1", "its +1")): over.append(word(x, TY - 21, w, t, weight=600, size=12.5, h=18, color=GREY))
# twins: a seam with a me-parity at both its sides, five cells
past = [p for p in d["twins"] if p > 3]; together = sum((p + 1) % 12 == 0 for p in past); apart = len(past) - together
for x0, lo in ((840, 10), (1170, 4)):
    for j in range(5):
        n = lo + j; cell(x0 + 44 * j, 812, 44, n, dark=bool(sieve[n]), aimed=(n in (aim(lo + 1), aim(lo + 3))), of6=(n == lo + 2))
assert sieve[11] and sieve[13] and aim(11) == aim(13) == 12 and sieve[5] and sieve[7] and (aim(5), aim(7)) == (4, 8)
ARIA = ("A drawing with no moving part. Eleven rows of three boxes with a number in a box, the middle box dark, the boxes of even numbers tinted, a box in a row with an accent edge, "
        "and a small dark mark in the corner of a box; beside a row, short words in five columns. Beside them a table of numbers in four columns and six rows, "
        "two rows of five boxes, and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
top = [word(60, 40, 1400, "52 · a figure, three cells · it is for v408primes' co-chain, a me-parity's three parts and its seam · its prior, 46", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A me-parity is three cells: even, odd, even.", "Its even that is a seam of 4 is its aim.", "Past 3, its even that is a seam of 6 is the seam it lives in.")):
    top.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
top.append(note(840, 100, "v408primes' co-chain, its sentences 172, 175 and 178, word for word:", 640))
top.append(note(840, 124, "<i>A me-parity is three parts: its prior, even; itself, odd; its next, even.</i>", 640))
top.append(note(840, 144, "<i>With all three, a me-parity aims: to its even that is a seam of 4, at one side.</i>", 640))
top.append(note(840, 164, "<i>A me-parity past 3 lives in a seam of 6, its prior or its next.</i>", 640))
top.append(head(60, 252, "the eleven me-parities to 31, a row a me-parity", 700))
top.append(note(60, 276, "tinted, an even number · dark, the me-parity · an accent edge, its aim · ◆ a seam of 6 · a me again, a number by itself", 760))
top.append(item(60, 862, f"○ a me-parity at one side of a seam of 6 alone: the least is 24, with 25, 5 by 5 · {n_(len(d['sides'][1]))} seams", 760))
top.append(item(60, 886, f"○ a me-parity at no side of a seam of 6: the least is 120, with 7 by 17 and 11 by 11 · {n_(len(d['sides'][0]))} seams", 760))
top.append(head(840, 222, "with all numbers, and stepped to 4,000,000"))
top.append(item(840, 252, f"● even, odd, even: all {n_(len(d['mes']))} me-parities past 2 · it is with all odd numbers"))
top.append(item(840, 276, f"● aiming prior, {n_(len(d['prior']))}: all are two me agains added · stepped"))
top.append(item(840, 300, f"● aiming next, {n_(len(d['nxt']))}: two me agains added at none · stepped"))
top.append(item(840, 324, f"● past 3, all {n_(len(d['past3']))} live in a seam of 6, a +1 apart · it is with all numbers:"))
top.append(note(840, 346, "of the six mes of a path of 6 closing, two alone are uncrossed by 2 and by 3:"))
top.append(note(840, 364, "the me one on and the me one back"))
top.append(head(840, 400, "a seam and its me-parity"))
top.append(item(840, 430, "● a +1 apart, and no prime crosses both"))
top.append(item(840, 454, "● round 6, 7 is one step on; round 7, 6 is one step back · 6 and 5, the other way"))
top.append(note(840, 476, "v408primes' namings of the three: <i>co-chaining, bi-co-unrelationing and bi-tunneling</i>"))
top.append(head(840, 536, "a seam of all primes to r, with its −1 and its +1"))
top.append(note(840, 714, "crossed by all primes to r, its −1 and its +1 by none of them: their parts are past r · executed, r to 31"))
top.append(head(840, 772, "twins: a seam with a me-parity at both its sides"))
top.append(note(840, 842, f"aiming together, at a seam of 12 · {n_(together)}", 320)); top.append(note(1170, 842, f"aiming apart · {n_(apart)}", 300))
top.append(note(840, 866, f"found by drawing it: a me-parity's aim and its seam are one even, a seam of 12, at {n_(len(d['one']))} past 3,"))
top.append(note(840, 884, f"and its two evens at {n_(len(d['past3']) - len(d['one']))} · twins aim together with both twins' one even, and at no other seam"))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A me-parity living in a seam: even, odd, even</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A me-parity is three cells: its prior, even; itself, odd; its next, even. Its even that is a seam of 4 is its aim.<br>'
           f'Past 3, its prior or its next is a seam of 6, a +1 apart: a me-parity lives in a seam. No prime crosses both.<br>'
           f'A seam of all primes to r has its −1 and its +1 crossed by none of them. Twins are a seam with a me-parity at both its sides.<br>'
           f'A candidate, of v408primes\' sentences 172 to 187, executed apart to 4,000,000.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(top + over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("A me-parity living in a seam: even, odd, even", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft52.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft52_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft52_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; the seams' table:", table, "; twins together and apart:", together, apart)
