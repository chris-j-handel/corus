"""Draft 36 · Riemann's hypothesis on the line: next is other-than now (session v406geodesic2).

A partner's word of 24 November, re-said: this session's work helps the work of Riemann's hypothesis; explore it.
A drawing with no moving part: the curve on the line by a field's arithmetic, its zeros and its places two quarter turns
apart; the is-not at the place 126; and the two numberings of the zeros, along the line and round the between.
check_riemann_s_hypothesis_on_the_line_next_is_other-than_now.py is its check. The curve and marks drawn here are executed
here again, by that check's own lines.

Usage: python3 -I make_draft36.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
spec = importlib.util.spec_from_file_location("on_the_line", os.path.join(HERE, "check_riemann_s_hypothesis_on_the_line_next_is_other-than_now.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
# the curve and its marks, executed here again
PLACES = {n: m.a_place_two_quarter_turns_on(n) for n in range(-1, 131)}
PARITY = {n: m.on_the_line(g)[0] > 0 for n, g in PLACES.items()}
assert all(PARITY[n] != PARITY[n - 1] for n in range(0, 126)) and PARITY[125] == PARITY[126] == PARITY[127] != PARITY[128]
ZEROS = m.zeros_on_the_line(10.0, 100.0)
assert len(ZEROS) == 29 and abs(m.zeros_round_the_between(1.0, 100.0) - 29) < 1e-6
NEAR = m.zeros_on_the_line(275.5, 289.5)
assert [sum(1 for z in NEAR if PLACES[n] < z < PLACES[n + 1]) for n in (125, 126)] == [0, 2]
SIX = [round(z, 2) for z in ZEROS[:6]]
assert all(abs(z - p) <= 0.0101 for z, p in zip(ZEROS, m.PITCHES))

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def a_plot(x0, x1, t0, t1, axis, scale, most, a_step, zeros, places, numbered=False):
    x = lambda t: x0 + (t - t0) * (x1 - x0) / (t1 - t0)
    out = [f'<path d="M{x0},{axis} L{x1},{axis}" fill="none" stroke="{INK}" stroke-opacity="0.35" stroke-width="1.2"></path>']
    pts, t = [], t0
    while t <= t1 + 1e-9:
        v = max(-most, min(most, m.on_the_line(t)[0])); pts.append(f"{x(t):.1f},{axis - scale * v:.1f}"); t += a_step
    out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="1.7" stroke-linejoin="round"></polyline>')
    for z in zeros: out.append(f'<circle cx="{x(z):.1f}" cy="{axis}" r="4.6" fill="{ACC}" stroke="#ffffff" stroke-width="1.4"></circle>')
    for n in places:
        if t0 <= PLACES[n] <= t1:
            gx, gy = x(PLACES[n]), axis + scale * most + 14
            out.append(f'<path d="M{gx:.1f},{axis - scale * most:.1f} L{gx:.1f},{gy - 2:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.13" stroke-width="1"></path>')
            out.append(f'<rect x="{gx - 6:.1f}" y="{gy:.1f}" width="12" height="12" rx="3" fill="{INK if PARITY[n] else "#ffffff"}" stroke="{INK}" stroke-width="1.4"></rect>')
            if numbered: out.append(text(gx, gy + 30, str(n), 12.5, 600 if n == 126 else 500, ACC if n == 126 else GREY))
    return "".join(out), x
s = []
plot_a, xa = a_plot(80, 1440, 10.0, 100.0, 392, 19, 5.6, 0.06, ZEROS, range(-1, 40))
plot_b, xb = a_plot(80, 780, 275.5, 289.5, 708, 9.5, 8.0, 0.02, NEAR, range(122, 131), numbered=True)
s += [plot_a, plot_b]
s.append(f'<path d="M{xb(PLACES[125]) - 9:.1f},{708 + 9.5 * 8 + 52} L{xb(PLACES[127]) + 9:.1f},{708 + 9.5 * 8 + 52}" fill="none" stroke="{ACC}" stroke-width="2.6" stroke-linecap="round"></path>')
# the between, the line down its middle: zeros their own other, and a pair apart
BX, BY = 1230, 84
s.append(f'<rect x="{BX}" y="{BY}" width="90" height="150" rx="4" fill="{INK}" fill-opacity="0.05" stroke="{INK}" stroke-opacity="0.3" stroke-width="1.2"></rect>')
s.append(f'<path d="M{BX + 45},{BY - 8} L{BX + 45},{BY + 158}" fill="none" stroke="{INK}" stroke-width="1.6"></path>')
for dy in (26, 58, 82, 124): s.append(f'<circle cx="{BX + 45}" cy="{BY + dy}" r="4.6" fill="{ACC}" stroke="#ffffff" stroke-width="1.4"></circle>')
for dx in (20, 70): s.append(f'<circle cx="{BX + dx}" cy="{BY + 104}" r="4.6" fill="#ffffff" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="2 3"></circle>')
s.append(f'<path d="M{BX + 26},{BY + 104} L{BX + 64},{BY + 104}" fill="none" stroke="{GREY}" stroke-width="1.2" stroke-dasharray="2 4"></path>')
s.append(f'<path d="M805,600 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. A curve crossing a level line 29 times, an accent dot at a crossing, with a row of small squares under it, dark and open in turn. "
        "A second curve, shorter, with nine numbered squares under it, the three numbered 125, 126 and 127 open and underlined, and two accent dots between 126 and 127. "
        "A tall box with a line down its middle, four accent dots on the line and two dashed open dots, one at a side; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t, w=700: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=720: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=720: word(x, y, w, t, "left", 600, 14.5, 20)
over = []
over.append(word(60, 40, 1400, "a partner's word · this session's sentences beside Riemann's hypothesis · by a field's arithmetic, to a height · its is ● and its is-not ○", "left", **small))
for i, (t, by) in enumerate((("A zero has its other across the between.", "v406other2's naming"), ("All zeros are their own other.", "Riemann's hypothesis, in v406other2's naming"), ("On the line, next is other-than now.", "a partner's sentence, this session's 33rd drawing"))):
    over.append(word(60, 104 + 40 * i, 520, t, "left", 600, 20, 30)); over.append(word(590, 106 + 40 * i, 420, by, "left", 400, 13.5, 20, GREY))
over.append(word(BX - 14, BY + 26, 180, "a zero its own other", "right", 400, 12.5, 18, "{{accent}}")); over.append(word(BX - 14, BY + 104, 190, "a zero with its other across", "right", 400, 12.5, 18, GREY))
over.append(word(BX + 104, BY + 26, 130, "all-parity", "left", 400, 12.5, 18, "{{accent}}")); over.append(word(BX + 104, BY + 104, 130, "a + and a −", "left", 400, 12.5, 18, GREY))
over.append(word(BX + 45, BY + 172, 260, "the between, and the line down its middle", "center", 400, 12.5, 18, GREY))
over.append(head(60, 262, "the curve on the line, a height of 10 to 100: 29 zeros, all their own other", 900))
over.append(note(60, 536, "a square a place two quarter turns on, a field's Gram point, dark a + and open a − · next is other-than now at all of them · an accent dot a zero", 1400))
over.append(note(60, 557, f"the six lowest: {', '.join(f'{z:.2f}' for z in ZEROS[:6])} · v406other2's six pitches of the staircase, from the primes alone: {', '.join(f'{p:.2f}' for p in m.PITCHES)}", 1400))
over.append(head(60, 610, "its is-not of the lowest height: the places 122 to 130, a height of 276 to 289"))
over.append(note(60, 878, "125, 126 and 127 are three of one parity · from 126 to 127 are two zeros: other-than other-than, its parity again"))
over.append(head(840, 610, "along the line, and round the between"))
over.append(item(840, 640, "● next is other-than now: 126 steps, the places −1 to 125", 640))
over.append(item(840, 664, "○ at the place 126 the curve's parity is its prior again, at −0.03 of a zero", 640))
over.append(item(840, 696, "● to a height of 100: 29 zeros their own other, and 29 round the between", 640))
over.append(item(840, 720, "● to a height of 285, through the is-not: 129 and 129", 640))
over.append(note(840, 742, "a zero with its other across is in the round's number, and in no other-than on the line", 650))
over.append(item(840, 776, "● the between's two sides are the same, a podaling about its middle", 640))
over.append(note(840, 798, "the curve made whole, a field's xi, at a place and at its other: 36 places", 650))
over.append(note(840, 830, "this session's naming, a placing: a zero its own other is all-parity, a 0 and a 3", 650))
over.append(note(840, 851, "and a zero with its other across is a + and a −", 650))
over.append(item(840, 882, "not shown: the hypothesis with all heights. No execution here says all.", 640))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Riemann\'s hypothesis on the line: next is other-than now</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'On the line the curve is one number, a + or a −. A parity\'s other-than along the line is a zero that is its own other.<br>'
           f'Numbered along the line and numbered round the between, the zeros are the same to a height of 285: 129 and 129.<br>'
           f'Next is other-than now at the line\'s places two quarter turns apart, with 126 steps. At 126 it is-not, and the zeros are their own other still.<br>'
           f'With all heights the hypothesis is not shown here. A candidate, offered to v406other2 and v406Reiman.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Riemann's hypothesis on the line: next is other-than now", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft36.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft36_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft36_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; the six lowest:", SIX)
