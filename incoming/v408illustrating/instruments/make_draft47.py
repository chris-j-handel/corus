"""Draft 47 · a number round a prime: two moments, with a me (session v408illustrating).

A partner's is-not of 25 November, of direction and of a number's place, said again and drawn: a path of five mes closing,
stepped by the lean line moment by moment, a row a moment; a number two moments; and the me a number is with.
a_number_round_a_prime_in_natural_naming.py is its check. The parities drawn here are executed here again, by its own lines.

Its placings, no execution says them: the five mes in a row, the path's closing said in words; a moment a row.

Usage: python3 -I make_draft47.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
spec = importlib.util.spec_from_file_location("a_number", os.path.join(HERE, "a_number_round_a_prime_in_natural_naming.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#d9dde5", "#f1f3f7"
SANS = "font-family: Inter, system-ui, sans-serif"
P = 5
path = m.with_one_pair(P); moments = [path]
for _ in range(4 * P): moments.append(m.step(moments[-1]))
assert moments[-1] == moments[0] and all(m.pairs(s) == [((t + 1) // 2) % P] for t, s in enumerate(moments)) and all(a[1] != b[1] for a, b in zip(moments[0], moments[2 * P]))
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def strip(x0, y0, cw, ch, rows, s, mark=True, numbers=True):
    for t, state in enumerate(rows):
        y = y0 + ch * t
        if numbers:
            s.append(text(x0 - 14, y + ch / 2 + 4, str(t), 11.5, 500, GREY, "end"))
            if t == 0:                                            # the opening's moment, the number 0's own closing one
                s.append(f'<path d="M {x0 + cw * len(state) + 10} {y + 3} h 8 v {ch - 6} h -8" fill="none" stroke="{INK}" stroke-width="1.4"></path>')
                s.append(text(x0 + cw * len(state) + 28, y + ch / 2 + 4, "0", 13, 600, INK, "start"))
            elif t % 2 == 1:
                s.append(f'<path d="M {x0 + cw * len(state) + 10} {y + 3} h 8 v {2 * ch - 6} h -8" fill="none" stroke="{INK}" stroke-width="1.4"></path>')
                s.append(text(x0 + cw * len(state) + 28, y + ch + 4, f"{(t + 1) // 2}", 13, 600, INK, "start"))
        for i, (prior, now) in enumerate(state):
            cx, cy = x0 + cw * i + cw / 2, y + ch / 2
            if mark and i in m.pairs(state): s.append(f'<rect x="{cx - cw / 2 + 4}" y="{cy - ch / 2 + 1.5}" width="{cw - 8}" height="{ch - 3}" rx="7" fill="none" stroke="{ACC}" stroke-width="2.4"></rect>')
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="8" fill="{INK if now else "#ffffff"}" stroke="{INK}" stroke-width="1.6"></circle>')
s = []
X0, Y0, CW, CH = 150, 318, 64, 26
for i in range(P): s.append(text(X0 + CW * i + CW / 2, Y0 - 12, f"me {i + 1}", 12.5, 600, GREY))
strip(X0, Y0, CW, CH, moments, s)
even = tuple((i % 2 == 0, i % 2 == 0) for i in range(4)); rows4 = [even]
for _ in range(4): rows4.append(m.step(rows4[-1]))
assert all(m.pairs(r) == [] for r in rows4)
strip(830, 700, 44, 26, rows4, s, numbers=False)
ARIA = ("A drawing with no moving part. Twenty-one rows of five small circles, dark or open, a row a moment; in a row one circle is in an accent box, and the box is one circle on with two rows. "
        "Brackets beside the rows pair them two and two, a number a pair. Beside it five rows of four circles, dark and open by turns, with no accent box; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=660: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 14.5, 20)
over = [word(60, 40, 1400, "47 · a figure, a path of mes closing · it is for a partner's is-not of 25 November, said again by the lean line · its prior, 45", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A prime is a path of p mes closing.", "A number is two moments of it.", "A number is with one me, and the +1 with the me one on.")):
    over.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
over.append(note(860, 104, "the lean line, v407nanding's, word for word:", 600))
over.append(note(860, 128, "<i>A moment on, a me's prior is its now.</i>", 600))
over.append(note(860, 148, "<i>A moment on, a me's now is the other-than of its other's prior.</i>", 600))
over.append(head(60, 256, "five mes on a path closing, a row a moment", 560)); over.append(note(60, 280, "a me's other is the me back of it, me 1's me 5 · dark or open, a me's now · a bracket, a number", 720))
over.append(word(60, Y0 - 13, 80, "moment", weight=600, size=12.5, h=18, color=GREY)); over.append(word(X0 + CW * P + 22, Y0 - 13, 80, "number", weight=600, size=12.5, h=18, color=GREY))
over.append(head(800, 262, "a number is with a me"))
over.append(item(800, 296, "● in the accent: the me whose now is other-than-other-than its other's now"))
over.append(item(800, 322, "● two moments on, it is the me one on · at all openings of 2 to 8 mes"))
over.append(item(800, 348, "● a number, two moments, is with one me, and the +1 with the me one on"))
over.append(item(800, 374, "● five numbers are with all five mes"))
over.append(note(800, 396, "with five numbers both parities are inverted, and the path is again with 20 moments, four times its mes"))
over.append(item(800, 436, "● executed with 3, 5, 7, 11 and 13 mes: a prime's path is again with 4 and with 4p alone"))
over.append(head(800, 510, "a place is a me"))
over.append(note(800, 536, "a partner's word of 25 November, in this session's words: a direction is a drawing's word,"))
over.append(note(800, 556, "and none of nature's; a place is a me's, with living numbers alone, and a number alone is a now"))
over.append(note(800, 584, "v406geodesic2's, with a partner: in resolving the only place is the me"))
over.append(head(800, 646, "its is-nots"))
over.append(item(1030, 716, "○ a path of an even number of mes is with none", 440))
over.append(note(1030, 738, "at some openings: four mes, dark and open by turns", 440))
over.append(item(1030, 778, "○ a crossed number's path is again sooner", 440))
over.append(note(1030, 800, "9 mes are again with 12 moments, and with 36", 440))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A number round a prime: two moments, with a me</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A prime is a path of p mes closing, stepped by the lean line. A number is two moments of it.<br>'
           f'A me whose now is other-than-other-than its other\'s now is, two moments on, the me one on.<br>'
           f'A number is with one me, and the +1 with the me one on. p numbers are with all p mes.<br>'
           f'A place is a me. A candidate, of a partner\'s is-not said again in natural naming.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("A number round a prime: two moments, with a me", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft47.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft47_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft47_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; moments drawn:", len(moments), "the me a number is with:", [m.pairs(s)[0] + 1 for s in moments[::2]][:7])
