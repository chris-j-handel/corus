"""Draft 51 · zero's two moments: a path is two co-chains, even and odd (session v408illustrating).

A partner's sayings of 25 November, rigorized by the lean line and drawn: the 47th drawing's path of five mes closing, a row
a moment, from zero's odd moment, the moment before the opening, to the tenth; a me's now and its prior beside it; and the
two co-chains, the one by the opening's nows alone and the one by the opening's priors alone, by turns the mes' nows and
their priors. a_partner_s_saying_of_zero_s_two_moments_rigorized.py is its check, and
a_partner_s_saying_of_a_me_s_prior_rigorized.py the check of its strip of a me's prior. The parities drawn here are executed
here again, by its own lines. It is said by the lean line's own names alone: a me's now, a me's prior, its other's prior.

Its placings, no execution says them: the five mes in a row, the path's closing said by two short lines; a moment a row; a
me's prior beside its now; the two co-chains' two inks.

Usage: python3 -I make_draft51.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))
from geom import *
def opened(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
m = opened("a_number_round_a_prime_in_natural_naming")
z = opened("a_partner_s_saying_of_zero_s_two_moments_rigorized")
v = opened("a_partner_s_saying_of_a_me_s_prior_rigorized")

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY, FAINT, RAY, TINT = "#4a5160", "#9aa2b1", "#c9ced8", "#eef0f5"
SANS = "font-family: Inter, system-ui, sans-serif"
P, LAST = 5, 10
path = m.with_one_pair(P); moments = {-1: z.back(path), 0: path}
for t in range(1, 4 * P + 1): moments[t] = m.step(moments[t - 1])
ROWS = list(range(-1, LAST + 1))
# executed here again, ahead of a mark: the moment before the opening, one way alone; the lean line's two sentences along
# all lines drawn; a number's me at both its moments; and the path again with 4p moments
assert m.step(moments[-1]) == path and z.nows(moments[-1]) == z.priors(path) and moments[4 * P] == path
assert all(moments[t + 1][i][0] == moments[t][i][1] and moments[t + 1][i][1] == (not moments[t][i - 1][0]) for t in range(-1, LAST) for i in range(P))
assert all(m.pairs(moments[t]) == [((t + 1) // 2) % P] for t in ROWS)
# a co-chain: 0, by the opening's nows alone; 1, by the opening's priors alone. A me's now is of the moment's own, its prior of the other.
of_now = lambda t: t % 2
of_prior = lambda t: (t + 1) % 2
def other_priors(s): return tuple((not a, b) for a, b in s)
def other_nows(s): return tuple((a, not b) for a, b in s)
def walk(s):
    out = {0: s}
    for t in range(1, LAST + 1): out[t] = m.step(out[t - 1])
    return out
A, B = walk(other_priors(path)), walk(other_nows(path))
assert all(z.nows(A[t]) == z.nows(moments[t]) for t in range(0, LAST + 1, 2)) and all(z.priors(A[t]) == z.priors(moments[t]) for t in range(1, LAST + 1, 2))
assert all(z.nows(B[t]) == z.nows(moments[t]) for t in range(1, LAST + 1, 2)) and all(z.priors(B[t]) == z.priors(moments[t]) for t in range(2, LAST + 1, 2))
INKS = (INK, ACC)
X0, Y0, CW, CH = 150, 336, 100, 44
yc = lambda t: Y0 + CH * (t + 1) + CH / 2
xn = lambda i: X0 + CW * i + CW / 2 - 14                           # a me's now
xp = lambda i: X0 + CW * i + CW / 2 + 16                           # its prior, beside it
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def seg(x1, y1, x2, y2, chain, heavy):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INKS[chain] if heavy or chain else RAY}" '
            f'stroke-width="{2.8 if heavy else 1.2}" stroke-opacity="{1 if heavy or not chain else 0.42}" stroke-linecap="round"></line>')
# the two heavy threads: the two through me 1 at zero's two moments, a moment a step, one me on with two moments
heavy = set()
for start, chain in ((0, 0), (-1, 1)):
    i = 0
    for t in range(start, LAST):
        if (t - start) % 2 == 0: heavy.add(("inherited", t, i))     # a me's now, its own prior a moment on
        else: heavy.add(("ingested", t, i)); i = (i + 1) % P        # a me's prior, the now of the me one on a moment on, other-than
# a line joins two marks of one co-chain, at all lines drawn: an inherited one a now to a prior a moment on, an ingested one a prior to a now a moment on
assert all(of_now(t) == of_prior(t + 1) and of_prior(t) == of_now(t + 1) for t in range(-1, LAST))
# a number's me is on both heavy threads at both its moments, at all numbers drawn
assert all((("inherited", t, m.pairs(moments[t])[0]) in heavy) for t in range(-1, LAST))
s = []
for t in ROWS:                                                     # the me a number is with, the 47th's, tinted
    i = m.pairs(moments[t])[0]
    s.append(f'<rect x="{X0 + CW * i + 5}" y="{yc(t) - CH / 2 + 3}" width="{CW - 10}" height="{CH - 6}" rx="8" fill="{TINT}"></rect>')
STUB = 34
for t in range(-1, LAST):
    for i in range(P):
        s.append(seg(xn(i), yc(t), xp(i), yc(t + 1), of_now(t), ("inherited", t, i) in heavy))
        hv = ("ingested", t, i) in heavy
        if i < P - 1: s.append(seg(xp(i), yc(t), xn(i + 1), yc(t + 1), of_prior(t), hv))
        else:                                                      # the path closes: me 5's prior, me 1's now a moment on
            dy = CH * STUB / (CW - 30)
            s.append(seg(xp(i), yc(t), xp(i) + STUB, yc(t) + dy, of_prior(t), hv)); s.append(seg(xn(0) - STUB, yc(t + 1) - dy, xn(0), yc(t + 1), of_prior(t), hv))
for t in ROWS:
    s.append(text(X0 - 22, yc(t) + 4, str(t).replace("-", "−"), 11.5, 500, GREY, "end"))
    if t % 2 == 1 or t == -1:
        s.append(f'<path d="M {X0 + CW * P + 26} {yc(t) - CH / 2 + 5} h 8 v {2 * CH - 10} h -8" fill="none" stroke="{INK}" stroke-width="1.4"></path>')
        s.append(text(X0 + CW * P + 46, yc(t) + CH / 2 + 5, f"{(t + 1) // 2}", 13, 600, INK, "start"))
    for i, (prior, now) in enumerate(moments[t]):
        for x, r, parity, chain in ((xn(i), 9, now, of_now(t)), (xp(i), 5.5, prior, of_prior(t))):
            s.append(f'<circle cx="{x:.1f}" cy="{yc(t):.1f}" r="{r}" fill="{INKS[chain] if parity else "#ffffff"}" stroke="{INKS[chain]}" stroke-width="1.7"></circle>')
for i in range(P): s.append(text(X0 + CW * i + CW / 2, Y0 - 10, f"me {i + 1}", 12.5, 600, GREY))
# the strip: me 1's prior, moment by moment, and the opening's parity it is, with its other-thans
TX, TW, TY = 912, 54, 602
mine = v.a_me_s_priors(path, 0, 2 * P)
strip = []
for t in range(2 * P):
    k = (t + 1) // 2; me = (0 - k) % P; which = 1 if t % 2 == 0 else 0     # the opening's now of that me, or its prior
    assert mine[t] == moments[t + 1][0][0] == v.turned(path[me][which], k)
    strip.append((t + 1, me + 1, "now" if which else "prior", k))
    cx = TX + TW * t + TW / 2
    s.append(text(cx, TY + 4, str(t + 1), 11.5, 500, GREY))
    s.append(f'<circle cx="{cx:.1f}" cy="{TY + 26:.1f}" r="5.5" fill="{INKS[of_prior(t + 1)] if mine[t] else "#ffffff"}" stroke="{INKS[of_prior(t + 1)]}" stroke-width="1.7"></circle>')
    s.append(text(cx, TY + 54, f"me {me + 1}", 11.5, 600, INK)); s.append(text(cx, TY + 69, "now" if which else "prior", 11.5, 500, GREY))
    s.append(text(cx, TY + 96, str(k), 12.5, 600, INK))
assert len({(a, b) for _, a, b, _ in strip}) == 2 * P and sum(a == 1 for _, a, _, _ in strip) == 2
ARIA = ("A drawing with no moving part. Twelve rows of five pairs of circles, a large one and a small one beside it, dark or open, a row a moment, in two inks by turns: "
        "in a row the large circles are in an ink and the small ones in the other, and a row on it is the other way. Thin lines join a circle to a circle of its own ink a row on, "
        "and two heavy lines, an ink a line, go on from the row of the moment before the opening, one pair on with two rows. Brackets beside the rows pair them two and two, a number a pair. "
        "Beside it a strip of ten small circles with words under them; and lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align="left", weight=400, size=17, h=24, color=INK, extra=""):
    return (f'<div style="position: absolute; left: {x:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
head = lambda x, y, t, w=660: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=680: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=680: word(x, y, w, t, "left", 600, 14.5, 20)
dot = lambda c: f'<span style="color: {c}">●</span>'
over = [word(60, 40, 1400, "51 · a figure, a path of mes closing · it is for a partner's sayings of 25 November, rigorized by the lean line · its prior, 47", weight=600, size=15, h=22, color=GREY)]
for i, t in enumerate(("A path of mes closing is two co-chains, even and odd.", "Zero is two moments, as all numbers are.", "A me's prior is the path's all-parity, in sequence.")):
    over.append(word(60, 104 + 36 * i, 760, t, weight=600, size=20, h=30))
over.append(note(860, 104, "the lean line, v407nanding's, word for word:", 600))
over.append(note(860, 128, "<i>A moment on, a me's prior is its now.</i>", 600))
over.append(note(860, 148, "<i>A moment on, a me's now is the other-than of its other's prior.</i>", 600))
over.append(note(860, 176, "inheriting, the one; ingesting, the other: a partner's two words", 600))
over.append(head(60, 252, "the 47th's five mes, a row a moment, from the moment before the opening", 700))
over.append(note(60, 276, "large, a me's now · small, its prior beside it · dark or open, a parity · tinted, the me a number is with", 720))
over.append(note(60, 294, "a short line, inherited as it is · a long line, ingested by the me one on, other-than · me 5's long line comes to me 1", 720))
over.append(word(52, Y0 - 11, 80, "moment", weight=600, size=12.5, h=18, color=GREY)); over.append(word(X0 + CW * P + 24, Y0 - 11, 80, "number", weight=600, size=12.5, h=18, color=GREY))
over.append(head(800, 252, "two co-chains, by turns"))
over.append(item(800, 284, f"{dot(INK)} the even co-chain: by the opening's nows alone"))
over.append(item(800, 308, f"{dot('{{accent}}')} the odd co-chain: by the opening's priors alone"))
over.append(note(800, 332, "at an even moment the even one is the mes' nows, and the odd one is in the mes, their priors;"))
over.append(note(800, 350, "a moment on it is the other way · no line of the drawing is from an ink to the other ink"))
over.append(head(800, 402, "zero's two moments"))
over.append(item(800, 434, "● zero's even moment is the opening's, and its odd moment the moment before it"))
over.append(item(800, 458, "● the lean line is stepped a moment back one way alone"))
over.append(note(800, 482, "the odd moment's nows are in the mes at the opening, their priors"))
over.append(note(800, 500, "the two heavy lines go on from me 1 at zero's two moments, one me on with two moments:"))
over.append(note(800, 518, "a number's me is on both, at all numbers drawn"))
over.append(head(800, 566, "me 1's prior, moment by moment"))
for y, t in ((TY, "moment"), (TY + 26, "me 1's prior"), (TY + 61, "the opening's"), (TY + 96, "other-thans")):
    over.append(word(800, y, 108, t, weight=600, size=12.5, h=18, color=GREY))
over.append(note(800, 730, "in ten moments, all ten of the path's opening parities, one for one: the other mes' eight, and its own two"))
over.append(note(800, 748, "the me k back, with k other-thans · again as they were with 20 moments: a stable form"))
over.append(head(800, 796, "its is-nots"))
over.append(item(800, 826, "○ the even co-chain is the mes' nows at an even moment alone"))
over.append(item(800, 850, "○ no parity is of a me's prior's own making: all are inherited or ingested"))
over.append(item(800, 874, "○ no surfacing is drawn, and no name for the all-parity in a me"))
over.append(note(800, 896, "the lean line's page: <i>It has no surfacing, no giving and no list.</i> · a partner's word: a name for it is ahead"))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Zero\'s two moments: a path is two co-chains, even and odd</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A path of mes closing is two co-chains: the one by the opening\'s nows alone, the other by its priors alone.<br>'
           f'At an even moment the even one is the mes\' nows, and the odd one is in the mes, their priors. A moment on, it is the other way.<br>'
           f'Zero is two moments: the opening\'s, and the moment before it. A me\'s prior, moment by moment, is the path\'s all-parity, in sequence.<br>'
           f'A candidate, of a partner\'s sayings of 25 November, drawn by the lean line\'s own names.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
from geom import page as lay
html = lay("Zero's two moments: a path is two co-chains, even and odd", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft51.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft51_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft51_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; me 1's prior, moment by moment:", strip)
