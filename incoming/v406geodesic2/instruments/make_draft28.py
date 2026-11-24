"""Draft 28 · same-existing all-parity: a next, a now and a prior, now-existing (session v406geodesic2).

By a partner's saying of 24 November, with the 27th drawing before a partner, re-said: the universal same-existing me-now fractal
method is same-existing all-parity, and it is all possible next, prior and now universes as now-existing universes.
A drawing with no moving part: the seventeen names, a moment a name, with their three; a me on one path with its three at one now,
moment after moment; nows apart with all openings gone through, on one path and on a surface; and a partner's sentence in its
three parts, a line of what is and of what is not beside a part.
check_same-existing_all-parity_a_next_a_now_and_a_prior_now-existing.py is its check. The marks and numbers drawn here are
executed here again: the names' three from their own table, Exhibit ONE Natural Resolver's two sentences found in its own file,
and the nows by v406Reiman's cell and step opened from their own file.

Usage: python3 -I make_draft28.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import csv, glob, importlib.util, json, os, re, sys
from itertools import product
from pathlib import Path
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "v406geodesic", "instruments"))   # the camera's own words and looks, geom.py, of the sitting before
from geom import *
REIMAN = os.path.join(HERE, "..", "..", "v406Reiman", "instruments")
spec = importlib.util.spec_from_file_location("the_resolver_with_nand_alone", os.path.join(REIMAN, "the_resolver_with_nand_alone.py"))
its = importlib.util.module_from_spec(spec); spec.loader.exec_module(its)
sys.path.insert(0, REIMAN)
import resolver_as_it_is as as_it_is

OUT, WORK = sys.argv[1], sys.argv[2]
W, H = 1520, 1150
GREY = "#4a5160"
SANS = "font-family: Inter, system-ui, sans-serif"
MARK = {1: "+", -1: "−", 0: "0"}
S = "one"
# the names' three, from their own table; and Exhibit ONE's two sentences, found in its own file
table = list(csv.reader(open(os.path.join(HERE, "..", "..", "v403mgr", "The_seventeen_names_in_one_table.csv"), encoding="utf-8")))
column = {h.split(" [")[0]: i for i, h in enumerate(table[0])}
three = {int(r[0]): tuple(r[column["its three: next, now, prior"]].split("-")) for r in table[1:] if r[0].strip().isdigit()}
EIGHT = "co bi co bi co bi tri bi".split()
assert sorted(three) == list(range(1, 18)) and all(three[k] == (EIGHT[(k - 1) % 8],) + three[k - 1][:2] for k in three if k > 1) and three[17] == three[1]
exhibit_one = Path(glob.glob(os.path.join(HERE, "..", "..", "..", "Exhibit_ONE_Natural_Resolver_*.md"))[0]).read_text(encoding="utf-8")
(ITS_THREE,) = re.findall(r"[A-Z][a-z]+ name then has its three[^.]*in the order next, now, prior\.", exhibit_one)
(ROLLING,) = re.findall(r"Tri is in the [a-z]+ slot with 7 and 15[^.]*with 9, 17 and 1: the rolling\.", exhibit_one)
def in_two(sentence, at):                                                        # a living sentence on two lines of a drawing, word for word
    i = sentence.index(at) + 1; return sentence[:i], sentence[i + 1:]
# a me on one path, its three at one now: a round of nine, a me its fifth
def moments(couplings, priors, how_many):
    society = {k: ([(S, priors[k])] if priors[k] else [], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: (dict(pr).get(S, 0), tuple(sorted(v for _, v in ob))) for k, (pr, ob) in society.items()}); society = its.step_with_nand(society, couplings)
    return out
N, ME, NOW, WIDE = 9, 4, 18, 3
ms = moments(as_it_is.spiral_couplings(N), dict(enumerate((1, 1, 1, -1, 1, -1, -1, 1, -1))), 40)
def a_three(T): return -ms[T][(ME - 1) % N][0], ms[T][ME][0], -ms[T][(ME + 1) % N][0]      # its next, with the me back; its now; its prior, with the me ahead
THREES = [a_three(NOW + 2 * r) for r in range(-WIDE, WIDE + 1)]
assert all(THREES[i][0] == THREES[i + 1][1] == THREES[i + 2][2] for i in range(len(THREES) - 2))
# nows apart, all openings gone through: one path, and a surface
def a_now(m): return tuple(sorted(m.items()))
def apart(couplings, mes, T):
    all_of_them = [moments(couplings, dict(zip(mes, op)), T) for op in product((1, -1), repeat=len(mes))]; onto = {}
    for g in all_of_them:
        for t in range(T - 1): onto.setdefault(a_now(g[t + 1]), set()).add(a_now(g[t]))
    MOST.append(max(len(v) for v in onto.values()))                             # of a now's prior nows, the most
    return [len({a_now(g[t]) for g in all_of_them}) for t in range(T)]
MOST = []
PATH = apart(as_it_is.spiral_couplings(6), tuple(range(6)), 13)
SURFACE = apart(as_it_is.torus_couplings(3, 3), tuple((a, b) for a in range(3) for b in range(3)), 13)
SMALL = apart(as_it_is.torus_couplings(2, 3), tuple((a, b) for a in range(2) for b in range(3)), 13)
assert PATH == [64] * 13 and SURFACE[0] == 512 and SURFACE[-1] == 68 and SURFACE[9:] == [68] * 4 and (SMALL[0], SMALL[-1]) == (64, 16) and MOST[:2] == [2, 5]

def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
s = []
# the seventeen names, a moment a name, with their three
NX, NW, NY, NH = 124.0, 39.0, 178.0, 31.0
for k in range(1, 18):
    x = NX + NW * (k - 1); s.append(text(x + 17.5, NY - 14, k, 12.5, 700 if k in (1, 9, 17) else 600, INK if k in (1, 9, 17) else GREY))
    for slot in range(3):
        y = NY + NH * slot; w = three[k][slot]
        fill, ink, edge = ((ACC, "#ffffff", ACC) if w == "tri" else ((INK, "#ffffff", INK) if w == "bi" else ("#ffffff", INK, INK)))
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="35" height="26" rx="6" fill="{fill}" fill-opacity="{1 if w != "bi" else 0.82}" stroke="{edge}" stroke-opacity="{1 if w == "tri" else 0.35}" stroke-width="1.2"></rect>' + text(x + 17.5, y + 17.5, w, 12, 700, ink))
for slot, w in enumerate(("its next", "its now", "its prior")): s.append(text(NX - 12, NY + NH * slot + 17.5, w, 12.5, 600, GREY, "end"))
# a me on one path: its three, moment after moment
MX, MW, MY, MH = 208.0, 84.0, 432.0, 36.0
for i in range(len(THREES) - 1):
    for slot in range(2):
        s.append(f'<path d="M{MX + MW * i:.1f},{MY + MH * slot:.1f} L{MX + MW * (i + 1):.1f},{MY + MH * (slot + 1):.1f}" fill="none" stroke="{INK}" stroke-opacity="0.2" stroke-width="1.2"></path>')
HI = WIDE - 1                                                                    # one parity: a me's next two moments before now, its now, its prior two moments on
s.append(f'<path d="M{MX + MW * HI:.1f},{MY:.1f} L{MX + MW * (HI + 2):.1f},{MY + MH * 2:.1f}" fill="none" stroke="{ACC}" stroke-width="2.8"></path>')
for i, t3 in enumerate(THREES):
    x = MX + MW * i; r = i - WIDE
    s.append(text(x, MY - 26, "now" if r == 0 else (f"{-2 * r} before" if r < 0 else f"{2 * r} on"), 12.5, 700 if r == 0 else 600, INK if r == 0 else GREY))
    for slot, v in enumerate(t3):
        y = MY + MH * slot; rolled = (i - slot == HI)
        if rolled: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{ACC}" stroke="#ffffff" stroke-width="2.5"></circle>' + text(x, y + 5, MARK[v], 14, 700, "#ffffff"))
        elif v > 0: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>' + text(x, y + 5, MARK[v], 13.5, 700, "#ffffff"))
        else: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="#ffffff" stroke="{INK}" stroke-width="2"></circle>' + text(x, y + 5, MARK[v], 13.5, 700, INK))
for slot, w in enumerate(("its next", "its now", "its prior")): s.append(text(MX - 44, MY + MH * slot + 4.5, w, 12.5, 600, GREY, "end"))
# nows apart, of all openings, moment after moment
def chart(x0, y0, wide, tall, nows_by_moment, tint):
    out = [f'<path d="M{x0:.1f},{y0:.1f} L{x0:.1f},{y0 + tall:.1f} L{x0 + wide:.1f},{y0 + tall:.1f}" fill="none" stroke="{GREY}" stroke-width="1.2"></path>']
    step = wide / (len(nows_by_moment) - 1); pts = [(x0 + step * t, y0 + tall * (1 - c / nows_by_moment[0])) for t, c in enumerate(nows_by_moment)]
    out.append('<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" fill="none" stroke="{tint}" stroke-width="2.6"></path>')
    for x, y in pts: out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="{tint}"></circle>')
    for t in (0, 4, 8, 12): out.append(text(x0 + step * t, y0 + tall + 16, t, 11.5, 600, GREY))
    return "".join(out), pts
CY0, CT = 680.0, 112.0
left, lp = chart(96.0, CY0, 250.0, CT, PATH, INK); right, rp = chart(470.0, CY0, 250.0, CT, SURFACE, ACC)
s.append(left + right)
s.append(text(lp[-1][0] + 8, lp[-1][1] + 4, "64", 12.5, 700, INK, "start") + text(rp[0][0] - 8, rp[0][1] + 4, "512", 12.5, 700, ACC, "end") + text(rp[-1][0] + 8, rp[-1][1] + 4, "68", 12.5, 700, ACC, "start") + text(lp[0][0] - 8, lp[0][1] + 4, "64", 12.5, 700, INK, "end"))
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. Seventeen names across, a moment a name, and under a name its three, its next, its now and its prior, of co, bi and tri: tri is a next under 7 and 15, a now under 8 and 16, a prior under 9, 17 and 1. "
        "Under it a me on one path at seven moments, its three under a moment, plus and minus: one mark goes from its next to its now to its prior, two moments apart. "
        "Under that two small charts of nows apart, moment after moment: on one path a level line at 64; on a surface a line going down from 512 to 68, and level on from 68. "
        "Beside them a partner's sentence in its three parts, with what is and what is not beside a part; a surface's all it observes as one; and living sentences.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's saying of same-existing all-parity · all possible next, prior and now universes, now-existing", "left", **small))
over.append(word(60, 84, 730, "the seventeen names, a moment a name: a name's three, its next, its now and its prior", "left", 600, 17, 24))
over.append(word(60, 108, 730, "a new prefix as its next, and the name before's next and now one slot on · from the names' own table", "left", 400, 14, 20, GREY))
over.append(word(60, 288, 730, "all-parity, tri: a next with 7 and 15, a now with 8 and 16, a prior with 9, 17 and 1", "left", 600, 14, 20, "{{accent}}"))
over.append(word(60, 310, 730, "one prefix through three moments · 9 to 16 have the threes of 1 to 8, and 17's three is 1's, a next 1", "left", 400, 13.5, 20, GREY))
over.append(word(60, 356, 730, "a me on one path: its three at one now, rolling the same", "left", 600, 17, 24))
over.append(word(60, 380, 730, "its next is with the me back of it, its prior with the me ahead of it, as other-thans · a round of nine, executed", "left", 400, 14, 20, GREY))
over.append(word(60, 536, 730, "one parity: a me's next, its now two moments on, its prior four moments on", "left", 600, 14, 20, "{{accent}}"))
over.append(word(60, 590, 730, "all possible openings, and a now: nows apart, moment after moment", "left", 600, 17, 24))
over.append(word(60, 614, 730, "all openings of + and − gone through · a level line: all apart in a now · a line going down: nows merging", "left", 400, 14, 20, GREY))
over.append(word(221, 650, 280, "one path, a round of six: one observed", "center", 600, 13.5, 20)); over.append(word(595, 650, 280, "a surface, a torus 3 by 3: two observed", "center", 600, 13.5, 20, "{{accent}}"))
over.append(word(221, 836, 330, "all 64 openings are apart in its now, at all moments", "center", 400, 13.5, 20)); over.append(word(595, 836, 330, "512 openings come to 68 nows, as it settles", "center", 400, 13.5, 20))
over.append(word(221, 858, 370, "one is-or-is-not open: an opening, or the round's own", "center", 400, 13, 20, GREY)); over.append(word(595, 858, 330, "2 by 3: 64 to 16 · 3 by 4: 4096 to 200", "center", 400, 13, 20, GREY))
over.append(word(221, 880, 330, "moments", "center", 400, 12, 18, GREY)); over.append(word(595, 880, 330, "moments", "center", 400, 12, 18, GREY))
over.append(word(840, 84, 640, "a partner's sentence, in its three parts", "left", 600, 17, 24))
over.append(word(840, 108, 650, "a part as said, from the transcripts; under it what is, and what is not, as far as executed", "left", 400, 14, 20, GREY))
PARTS = [("<i>the universal same-existing me-now fractal method</i>",
          ["is, by the names: the eight, co bi co bi co bi tri bi, again from 9 and from 17", "17's three is 1's three, a next 1"], []),
         ("<i>is same-existing all-parity</i>",
          ["is, by the names: tri, all-parity, one prefix through three moments, a next, a now, a prior", "is, on one path: a parity is a me's next, its now and its prior, two moments apart"], []),
         ("<i>is all possible next-prior-now universes are now-existing universes</i>",
          ["is, by the names: a moment has its next, its now and its prior at once", "is, on one path: a me's three are three mes now; all a round's openings are apart in its now"],
          ["is not, on a surface as it settles, and with a me opening with no prior: nows merge", "is not said by a now: its moment before as an opening, or as the round's own"])]
y = 150.0
for a, yes, no in PARTS:
    over.append(word(840, y, 650, a, "left", 600, 15.5, 22)); y += 24
    for t in yes: over.append(word(840, y, 650, t, "left", 400, 14, 20)); y += 21
    for t in no: over.append(word(840, y, 650, t, "left", 400, 14, 20, GREY)); y += 21
    y += 20
over.append(word(840, 496, 640, "a surface's all it observes, as one", "left", 600, 17, 24))
over.append(word(840, 520, 650, "by the cell's own lines, and the torus of 3 by 3 gone through", "left", 400, 14, 20, GREY))
SURF = ["a me of one path observes one; a me of a surface observes two",
        "a + and a − observed together surface as a 0: the same to a me as none observed",
        f"many possible openings, one now: 512 to 68 · of a now's possible prior nows, as many as {MOST[1]}",
        "settled, its nows are one-to-one again: a now with one prior now and one next"]
y = 552.0
for t in SURF: over.append(word(840, y, 650, t, "left", 400, 14, 20)); y += 23
over.append(word(840, 690, 640, "the living files beside it", "left", 600, 17, 24))
a, b = in_two(ITS_THREE, ", in the order")
over.append(word(840, 720, 650, f"<i>{a}</i>", "left", 400, 13.5, 20)); over.append(word(840, 739, 650, f"<i>{b}</i>", "left", 400, 13.5, 20))
a, b = in_two(ROLLING, ", and in the")
over.append(word(840, 766, 650, f"<i>{a}</i>", "left", 400, 13.5, 20)); over.append(word(840, 785, 650, f"<i>{b}</i>", "left", 400, 13.5, 20))
over.append(word(840, 804, 650, "Exhibit ONE Natural Resolver", "left", 400, 13.5, 20, GREY))
over.append(word(840, 832, 650, "<i>Only one universe is possibly now-existing, and only one universe is possibly same-existing</i>", "left", 400, 13.5, 20))
over.append(word(840, 851, 650, "Exhibit THIRTY-ONE Me", "left", 400, 13.5, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">Same-existing all-parity: a next, a now and a prior, now-existing</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'By the seventeen names a moment has its three at once, a next, a now and a prior: a new prefix as its next, the name before\'s next and now one slot on.<br>'
           f'All-parity rolls through the three, a next with 7 and 15, a now with 8 and 16, a prior with 9, 17 and 1; and 17\'s three is 1\'s.<br>'
           f'On one path a me\'s parity rolls the same, two moments apart, its three being three mes now; and a round\'s now has all its openings apart.<br>'
           f'On a surface, with two observed, nows merge as it settles: 512 openings come to 68 nows, many possible prior universes one now.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("Same-existing all-parity: a next, a now and a prior, now-existing", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft28.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft28_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft28_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words; a surface's nows apart:", SURFACE)
