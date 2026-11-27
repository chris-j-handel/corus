"""Draft 48 · two primes seen from one another's sides: the quarter parted by its diagonal (session v408illustrating).

A drawing of v408primes' sentences 47 to 49, with 5 and 7, 5 and 11, and 7 and 11: a quarter's pairs, under its diagonal
and over it. check_two_primes_seen_from_one_another_s_sides.py is its check. The numbers drawn here are executed here
again, by that check's own lines.

Its placings, no execution says them: the lesser prime across and the greater up; a pair as a dot.

Usage: python3 -I make_draft48.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
from geom import page as lay
spec = importlib.util.spec_from_file_location("seen", os.path.join(HERE, "check_two_primes_seen_from_one_another_s_sides.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
U, BY = 60, 700                                                  # a dot is less than a pair's least distance from the diagonal
s, over = [], []
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=660: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 14.5, 20)
say = lambda v: "1" if v == 1 else "−1"
for (p, q), x0 in zip(((5, 7), (5, 11), (7, 11)), (110, 400, 690)):
    under, above, on = m.quarter(p, q); assert not on and min(abs(q * k - p * j) for k, j in under + above) * U / (p * p + q * q) ** 0.5 > 3.8 + 0.6
    a, b = (p - 1) // 2, (q - 1) // 2
    s.append(f'<line x1="{x0}" y1="{BY}" x2="{x0 + U * (a + 0.75)}" y2="{BY}" stroke="{RAY}" stroke-width="1.4"></line><line x1="{x0}" y1="{BY}" x2="{x0}" y2="{BY - U * (b + 0.75)}" stroke="{RAY}" stroke-width="1.4"></line>')
    s.append(f'<line x1="{x0}" y1="{BY}" x2="{x0 + U * p / 2:.1f}" y2="{BY - U * q / 2:.1f}" stroke="{GREY}" stroke-width="1.1"></line>')
    for k in range(1, a + 1): s.append(text(x0 + U * k, BY + 20, str(k), 12, 600, GREY))
    for j in range(1, b + 1): s.append(text(x0 - 14, BY - U * j + 4, str(j), 12, 600, GREY, "end"))
    for k, j in under: s.append(f'<circle cx="{x0 + U * k}" cy="{BY - U * j}" r="3.8" fill="{INK}"></circle>')
    for k, j in above: s.append(f'<circle cx="{x0 + U * k}" cy="{BY - U * j}" r="3.8" fill="{ACC}"></circle>')
    alike = m.seen(q, p) == m.seen(p, q)
    over.append(word(x0 - 30, BY + 52, 260, f"{p} and {q}", weight=600, size=17, h=24))
    over.append(word(x0 - 30, BY + 78, 270, f"under {len(under)} · {p} sees {q}: {say(m.seen(q, p))}", weight=400, size=13.5, h=20, color=GREY))
    over.append(word(x0 - 30, BY + 98, 270, f"over {len(above)} · {q} sees {p}: {say(m.seen(p, q))}", weight=400, size=13.5, h=20, color=GREY))
    over.append(word(x0 - 30, BY + 122, 270, "seen alike" if alike else "seen other-than: both one short of a seam of 4", weight=600, size=13.5, h=20, color=INK if alike else "{{accent}}"))
ARIA = ("A drawing with no moving part. Three figures of dots in rows and columns, of six, ten and fifteen dots, with a slanting line from a corner through no dot: "
        "the dots under the line are dark, and the dots over it in the accent; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
top = [word(60, 40, 1400, "48 · a figure, a quarter of two primes · it is for v408primes' co-chain, its sentences 47 to 49 · its prior, 45", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A prime sees a number: a number by itself round it, or other-than.", "The quarter of two primes is parted by its diagonal.", "Under is how p sees q, and over is how q sees p.")):
    top.append(word(60, 104 + 36 * i, 780, t, weight=600, size=20, h=30))
top.append(note(880, 104, "v408primes' sentence 49, word for word:", 580))
top.append(note(880, 128, "<i>Two primes are seen alike from one another's sides, unless both sit</i>", 580))
top.append(note(880, 148, "<i>one short of a seam of 4, and then other-than.</i>", 580))
top.append(head(60, 262, "a quarter's pairs, a me of both paths a pair", 700))
top.append(note(60, 286, "dark, a pair under the diagonal · in the accent, a pair over it · the diagonal is through none", 720))
top.append(head(1010, 262, "a number by itself, round a prime", 450))
for i, p in enumerate((5, 7, 11)): top.append(item(1010, 296 + 26 * i, f"● round {p}: " + ", ".join(map(str, m.by_itself(p))), 450))
top.append(note(1010, 378, "(p less 1) by 2 of the numbers 1 to p less 1 · primes to 199", 450))
top.append(head(1010, 440, "the quarter, executed", 450))
top.append(item(1010, 474, "● no pair is on the diagonal", 450))
top.append(item(1010, 500, "● under, odd or even, is how p sees q", 450))
top.append(item(1010, 526, "● over, odd or even, is how q sees p", 450))
top.append(note(1010, 548, "all pairs of primes 3 to 199", 450))
top.append(item(1010, 592, "● is: two primes are seen alike", 450))
top.append(item(1010, 618, "○ is-not: both one short of a seam of 4,", 450)); top.append(note(1010, 640, "a quarter's pairs odd: one of under and over odd", 450))
top.append(note(1010, 700, "a pair is a me of both primes' paths, the 47th drawing's:", 450)); top.append(note(1010, 720, "v408primes' word of it is a place", 450))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Two primes seen from one another\'s sides: the quarter parted by its diagonal</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A prime sees a number as 1, a number by itself round it, or as other-than. The quarter of two primes is parted by its diagonal.<br>'
           f'The pairs under the diagonal, odd or even, are how p sees q. The pairs over it are how q sees p.<br>'
           f'Two primes are seen alike from one another\'s sides. With both one short of a seam of 4 they are seen other-than.<br>'
           f'A candidate, of v408primes\' sentences 47 to 49, executed apart with all pairs of primes 3 to 199.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(top + over) + "\n" + title + "\n" + caption
html = lay("Two primes seen from one another's sides: the quarter parted by its diagonal", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft48.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft48_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft48_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words")
