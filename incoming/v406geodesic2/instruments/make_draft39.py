"""Draft 39 · longer co-chaining gives wider co-observing and faster progressing: the bothboth of out and in (session v406geodesic2).

A partner's word of 24 November, re-said: a destiny close and a destiny far are one destiny at two depths, the depth the
length of the co-chain; a longer co-chain gives wider co-observing and co-possibling and faster progressing universes.
A drawing with no moving part: the out-fold, the staircase the primes build; the in-fold gathering it back from the zeros,
a zero a link, at co-chains of 1, 5, 20 and 50 links; the error narrowing with the chain; and the finest scale narrowing.
check_longer_co-chaining_wider_co-observing_and_faster_progressing_executed.py is its check, its marks executed here again.

Usage: python3 -I make_draft39.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.dont_write_bytecode = True                                                   # a file opened by its path is laid nowhere again
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
spec = importlib.util.spec_from_file_location("the_chain", os.path.join(HERE, "check_longer_co-chaining_wider_co-observing_and_faster_progressing_executed.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
rh_spec = importlib.util.spec_from_file_location("rh", os.path.join(HERE, "check_riemann_s_hypothesis_on_the_line_next_is_other-than_now.py"))
rh = importlib.util.module_from_spec(rh_spec); rh_spec.loader.exec_module(rh)

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
# the marks drawn, executed here again
gammas = rh.zeros_on_the_line(10.0, 145.0)
rise = m.von_mangoldt_to(100)
assert len(gammas) == 50
X0, X1 = 12.0, 90.0
stair = lambda x: m.the_staircase(x, rise)
gather = lambda x, k: m.gathered_from_links(x, gammas, k)
ERRS = {k: max(abs(gather(x, k) - stair(x)) for x in m.WINDOW) for k in (1, 5, 10, 20, 50)}
assert abs(ERRS[1] - 3.08) < 0.01 and abs(ERRS[50] - 1.485) < 0.01 and ERRS[1] > ERRS[5] > ERRS[10] > ERRS[20] > ERRS[50]
FINE = {k: 2 * math.pi * 90 / gammas[k - 1] for k in (1, 50)}
assert abs(FINE[1] - 40.0) < 0.1 and abs(FINE[50] - 3.95) < 0.05
# the plot frame
PL, PR, PT, PB = 80, 1030, 320, 690
VLO, VHI = 8.0, 92.0
sx = lambda x: PL + (x - X0) * (PR - PL) / (X1 - X0)
sy = lambda v: PB - (v - VLO) * (PB - PT) / (VHI - VLO)
def curve(k, step=0.25):
    xs, pts = X0, []
    while xs <= X1 + 1e-9: pts.append(f"{sx(xs):.1f},{sy(gather(xs, k)):.1f}"); xs += step
    return " ".join(pts)
def staircase():
    powers = [n for n in range(int(X0) + 1, int(X1) + 1) if rise[n]]
    pts, v, x = [], stair(X0), X0
    pts.append(f"{sx(x):.1f},{sy(v):.1f}")
    for pw in powers:
        pts.append(f"{sx(pw):.1f},{sy(v):.1f}"); v += rise[pw]; pts.append(f"{sx(pw):.1f},{sy(v):.1f}")
    pts.append(f"{sx(X1):.1f},{sy(v):.1f}")
    return " ".join(pts)
s = []
s.append(f'<rect x="{PL}" y="{PT}" width="{PR - PL}" height="{PB - PT}" rx="6" fill="{INK}" fill-opacity="0.02" stroke="{INK}" stroke-opacity="0.18" stroke-width="1.1"></rect>')
for v in range(10, 91, 10): s.append(f'<path d="M{PL},{sy(v):.1f} L{PR},{sy(v):.1f}" fill="none" stroke="{INK}" stroke-opacity="0.07" stroke-width="1"></path>' + __import__("geom").__dict__.get("_x", lambda: "")() if False else f'<text x="{PL - 8:.1f}" y="{sy(v) + 4:.1f}" text-anchor="end" font-family="Inter, system-ui, sans-serif" font-size="10.5" fill="{GREY}">{v}</text>')
# the in-fold gatherings, short to long
for k, op, wdt in ((1, 0.33, 1.4), (5, 0.5, 1.4), (20, 0.72, 1.6)):
    s.append(f'<polyline points="{curve(k)}" fill="none" stroke="{ACC}" stroke-opacity="{op}" stroke-width="{wdt}" stroke-linejoin="round"></polyline>')
s.append(f'<polyline points="{curve(50)}" fill="none" stroke="{ACC}" stroke-width="2.4" stroke-linejoin="round"></polyline>')
# the out-fold staircase, over them
s.append(f'<polyline points="{staircase()}" fill="none" stroke="{INK}" stroke-width="2.0" stroke-linejoin="round" stroke-linecap="round"></polyline>')
# the fuzzy spot at a prime: the band between the short and long gathering, narrowing
FP = 83
band1 = [gather(FP - d / 2, 1) for d in range(0, 16)]; band50 = [gather(FP - d / 2, 50) for d in range(0, 16)]
s.append(f'<circle cx="{sx(FP):.1f}" cy="{sy(stair(FP + 0.3)):.1f}" r="5" fill="none" stroke="{INK}" stroke-width="1.6"></circle>')
# the error bars, a bar a co-chain length
BX, BW, BTOP, BBOT = 1150, 48, 470, 660
for i, k in enumerate((1, 5, 10, 20, 50)):
    h = (BBOT - BTOP) * ERRS[k] / ERRS[1]
    s.append(f'<rect x="{BX + 66 * i}" y="{BBOT - h:.1f}" width="{BW}" height="{h:.1f}" rx="3" fill="{ACC}"></rect>')
s.append(f'<path d="M805,250 L805,905" fill="none" stroke="{INK}" stroke-opacity="0" stroke-width="1"></path>')
ARIA = ("A drawing with no moving part. A rising staircase in ink, and over it four accent curves from faint to bold that hug the staircase more tightly as they go, the boldest tracking its steps. "
        "To one side five accent bars going down along, 3.08 to 1.485. Lines of words.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
head = lambda x, y, t, w=720: word(x, y, w, t, "left", 600, 17, 24)
note = lambda x, y, t, w=720: word(x, y, w, t, "left", 400, 13.5, 20, GREY)
item = lambda x, y, t, w=720: word(x, y, w, t, "left", 600, 14.5, 20)
over = []
over.append(word(60, 40, 1400, "a partner's word · a destiny close and a destiny far are one destiny · the depth is the co-chain's length · executed, the bothboth", "left", **small))
for i, t in enumerate(("The out-fold is the staircase the primes build.", "The in-fold gathers it back from the zeros, a zero a link.", "A longer co-chain gathers wider and faster.")):
    over.append(word(60, 106 + 34 * i, 900, t, "left", 600, 20, 30))
over.append(head(60, 236, "the staircase, and the co-chain gathering it: 1, 5, 20 and 50 links"))
over.append(note(60, 260, "the out-fold in ink · the in-fold in the accent, faint at one link, bold at fifty · no curve is fitted", 900))
over.append(word(sx(28) + 6, sy(stair(28)) - 22, 170, "the staircase, out", "left", 600, 13, 18, INK))
over.append(word(sx(FP) - 168, sy(stair(FP)) - 30, 160, "a prime: the fuzzy spot", "left", 400, 12, 18, GREY))
over.append(head(1120, 418, "the error, a bar a chain", 360))
over.append(note(1120, 440, "the most it strays, the window 12.5 to 89.5", 400))
for i, k in enumerate((1, 5, 10, 20, 50)):
    over.append(word(1150 + 66 * i, 676, 48, str(k), "center", 600, 12, 18, GREY))
    over.append(word(1150 + 66 * i, (BBOT - (BBOT - BTOP) * ERRS[k] / ERRS[1]) - 10, 48, f"{ERRS[k]:.2f}", "center", 600, 11.5, 16, "{{accent}}"))
over.append(word(1150, 700, 360, "links of the co-chain", "left", 400, 12.5, 18, GREY))
over.append(item(60, 740, "● a longer co-chain gives a smaller error: 3.08 at one link, 1.485 at fifty, smaller as the chain lengthens", 920))
over.append(note(60, 762, "wider co-observing: the gathering strays less from the staircase the longer the chain", 920))
over.append(item(60, 792, "● faster progressing: the finest scale it resolves about 90 is 40.0 at one link, 3.95 at fifty, the fuzzy spot narrowing", 920))
over.append(item(1120, 740, "● one destiny, two depths", 380))
over.append(note(1120, 762, "a short chain tracks the coarse trend, the close destiny · a long chain the sharp steps, the far", 400))
over.append(note(60, 834, "○ its is-not: a finite co-chain never closes the fuzzy spot · at fifty links it still strays 1.485 and overshoots at a step · only all the zeros, with all numbers, close it to the staircase, not shown", 1400))
over.append(note(60, 864, "the zeros are the far destinies over the horizon, gathered geodesically inward · the links are a co-chaining of cones, this session's 26th and 27th drawings", 1400))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Longer co-chaining: wider co-observing, faster progressing</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'The primes build the staircase out; the zeros gather it in, a zero a link of the co-chain. No curve is fitted.<br>'
           f'A longer co-chain strays less and resolves finer: wider co-observing, the fuzzy spot narrowing, faster progressing.<br>'
           f'A destiny close and a destiny far are one destiny, gathered at two depths — the depth the length of the chain.<br>'
           f'With a finite chain the fuzz never closes; only all the zeros close it. A candidate, offered for the work of the hypothesis.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Longer co-chaining: wider co-observing, faster progressing", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft39.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft39_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).replace("&nbsp;", " ").strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft39_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; errs", {k: round(v, 3) for k, v in ERRS.items()})
