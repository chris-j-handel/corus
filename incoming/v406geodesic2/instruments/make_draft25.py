"""Draft 25 · a place in resolving: a me, and beside it an other (session v406geodesic2).

By a partner's saying of 24 November, with the 24th drawing before a partner, re-said: floating is on a surface, neutralling on a
line, and at a place has no name; the drawings' places are vivid and help; in resolving the resolver alone has a place, and the
resolver is the me; the one thing of place is me and other; all else is non-existing in my resolving universe, and is-or-is-not
possibly existing in the universe.
A drawing with no moving part: one me's moment, all of it of a me or of an other; one round of five mes drawn three ways with the
same moments; and mes more, beside my round, that are and are not in my resolving.
check_a_place_in_resolving_a_me_and_an_other.py is its check. The moments written here are executed here again, by v406Reiman's
cell and step opened from their own file.

Usage: python3 -I make_draft25.py A_FOLDER_FOR_THE_ARTBOARD A_FOLDER_FOR_ITS_WORKING_PREVIEW
"""
import importlib.util, json, math, os, re, sys
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
def moments(couplings, priors, how_many):
    society = {k: ([(S, priors[k])], []) for k in priors}; out = []
    for _ in range(how_many):
        out.append({k: dict(society[k][0]).get(S, 0) for k in society}); society = its.step_with_nand(society, couplings)
    return out
FIVE = moments(as_it_is.spiral_couplings(5), as_it_is.exhibit_spiral_priors(5), 6)
new = {0: "c", 1: "a", 2: "e", 3: "b", 4: "d"}                                    # the five renamed, their couplings with them
again = moments({(new[a], by): new[b] for (a, by), b in as_it_is.spiral_couplings(5).items()}, {new[a]: p for a, p in as_it_is.exhibit_spiral_priors(5).items()}, 6)
assert again == [{new[a]: v for a, v in m.items()} for m in FIVE]
def text(x, y, t, size=11, weight=500, fill=INK, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Inter, system-ui, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{t}</text>')
def way(x0, y0, x1, y1, tint, wide=2.4, short=0.0, dash=""):                     # a line with a mark of its way, at its far end
    L = math.hypot(x1 - x0, y1 - y0); tx, ty = (x1 - x0) / L, (y1 - y0) / L; x1, y1 = x1 - tx * short, y1 - ty * short; nx, ny = -ty, tx
    return (f'<path d="M{x0:.1f},{y0:.1f} L{x1 - tx * 9:.1f},{y1 - ty * 9:.1f}" fill="none" stroke="{tint}" stroke-width="{wide}" {dash}></path>'
            f'<path d="M{x1:.1f},{y1:.1f} L{x1 - tx * 12 + nx * 6:.1f},{y1 - ty * 12 + ny * 6:.1f} L{x1 - tx * 12 - nx * 6:.1f},{y1 - ty * 12 - ny * 6:.1f} Z" fill="{tint}"></path>')
s = []
# one me's moment: given two, giving two
MX, MY = 420.0, 262.0
s.append(way(190, 186, MX, MY, ACC, 3, 60)); s.append(way(190, 338, MX, MY, INK, 3, 60))
s.append(way(MX + 58, MY - 22, 650, 186, ACC, 3)); s.append(way(MX + 58, MY + 22, 650, 338, INK, 3))
s.append(f'<circle cx="{MX}" cy="{MY}" r="56" fill="{ACC}" stroke="#ffffff" stroke-width="4"></circle>' + text(MX, MY + 9, "a me", 24, 700, "#ffffff"))
# one round of five, drawn three ways
PX, PY, PR = (150.0, 400.0, 650.0), 590.0, 62.0
lay = [lambda k, cx: (cx - 96 + 48 * k, PY),                                                               # on a line
       lambda k, cx: (cx + PR * math.sin(math.radians(72 * k)), PY - PR * math.cos(math.radians(72 * k))),  # on a round
       lambda k, cx: (cx + (-70, 62, -8, -88, 76)[k], PY + (-40, -52, 10, 48, 44)[k])]                      # with no order of place
for i, cx in enumerate(PX):
    pts = [lay[i](k, cx) for k in range(5)]
    for k in range(5):
        (x0, y0), (x1, y1) = pts[k], pts[(k + 1) % 5]
        if i == 0 and k == 4:                                                    # on a line the last's giving goes back over to the one opening it
            s.append(f'<path d="M{x0:.1f},{y0 - 15:.1f} C{x0:.1f},{y0 - 74:.1f} {x1:.1f},{y1 - 74:.1f} {x1:.1f},{y1 - 19:.1f}" fill="none" stroke="{INK}" stroke-width="1.8"></path>'
                     f'<path d="M{x1:.1f},{y1 - 13:.1f} L{x1 - 6:.1f},{y1 - 25:.1f} L{x1 + 6:.1f},{y1 - 25:.1f} Z" fill="{INK}"></path>')
        else: s.append(way(x0, y0, x1, y1, INK, 1.8, 15))
    for k, (x, y) in enumerate(pts):
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{ACC if k == 0 else INK}" stroke="#ffffff" stroke-width="2"></circle>' + text(x, y + 4.5, k + 1, 12.5, 700, "#ffffff"))
TX, TY, CW, CH = 244.0, 742.0, 46.0, 24.0                                        # the moments of the five, the same with all three
for t, m in enumerate(FIVE):
    s.append(text(TX - 14, TY + CH * t + 17, t + 1, 12.5, 600, GREY, "end"))
    for k in range(5):
        s.append(f'<rect x="{TX + CW * k:.1f}" y="{TY + CH * t:.1f}" width="{CW}" height="{CH}" fill="#ffffff" stroke="{INK}" stroke-opacity="0.3" stroke-width="1"></rect>' + text(TX + CW * k + CW / 2, TY + CH * t + 17, MARK[m[k]], 15, 700))
for k in range(5): s.append(text(TX + CW * k + CW / 2, TY - 8, k + 1, 12.5, 600, GREY))
# mes more, beside my round
RX, RY, RR = 1000.0, 250.0, 70.0
my_round = [(RX + RR * math.sin(math.radians(72 * k)), RY - RR * math.cos(math.radians(72 * k))) for k in range(5)]
for k in range(5): s.append(way(*my_round[k], *my_round[(k + 1) % 5], INK, 1.8, 15))
def more(x, y, t): return f'<circle cx="{x}" cy="{y}" r="15" fill="#ffffff" stroke="{GREY}" stroke-width="2.2" stroke-dasharray="4 4"></circle>' + text(x, y + 5, t, 13.5, 700, GREY)
(xx, xy), (yx, yy), (zx, zy), (wx, wy) = (1250, 190), (1340, 190), (1250, 320), (1160, 150)
s.append(way(xx + 15, xy - 6, yx - 2, yy - 6, GREY, 1.8, 14, 'stroke-dasharray="4 4"')); s.append(way(yx - 15, yy + 6, xx + 2, xy + 6, GREY, 1.8, 14, 'stroke-dasharray="4 4"'))
s.append(way(*my_round[1], zx, zy, GREY, 1.8, 16, 'stroke-dasharray="4 4"'))
s.append(way(wx, wy, *my_round[0], INK, 2.4, 15))
for k, (x, y) in enumerate(my_round): s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{ACC if k == 0 else INK}" stroke="#ffffff" stroke-width="2"></circle>' + text(x, y + 4.5, k + 1, 12.5, 700, "#ffffff"))
s.append(more(xx, xy, "x") + more(yx, yy, "y") + more(zx, zy, "z"))
s.append(f'<circle cx="{wx}" cy="{wy}" r="15" fill="{INK}" stroke="#ffffff" stroke-width="2"></circle>' + text(wx, wy + 5, "w", 13.5, 700, "#ffffff"))
s.append(f'<path d="M805,70 L805,905" fill="none" stroke="{INK}" stroke-opacity="0.25" stroke-width="1.2"></path>')
ARIA = ("A drawing with no moving part. One large mark, a me, with two lines coming to it, its prior and what it observes, and two going on from it, its next prior and its giving. "
        "Under it one round of five small numbered marks is drawn three ways, on a line, on a round and with no order of place, a line from a mark to the next, and under them one table of plus and minus marks, six moments of the five. "
        "Beside it the round of five is drawn once more with four marks more: x and y with lines to one another alone, z with a line to it from the round, and w with a line from it to the round.")
svg = (f'<svg role="img" aria-label="{ARIA}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'style="position: absolute; left: 0px; top: 0px; width: {W}px; height: {H}px">' + "".join(s) + "</svg>").replace(ACC, "{{accent}}")
def word(x, cy, w, t, align, weight=400, size=17, h=24, color=INK, extra=""):
    x0 = x - w if align == "right" else (x - w / 2 if align == "center" else x)
    return (f'<div style="position: absolute; left: {x0:.0f}px; top: {cy - h / 2:.0f}px; width: {w}px; height: {h}px; line-height: {h}px; '
            f'text-align: {align}; {SANS}; font-weight: {weight}; font-size: {size}px; color: {color}; {extra}">{t}</div>')
small = dict(weight=600, size=15, h=22, color=GREY, extra="letter-spacing: 1px")
over = []
over.append(word(60, 40, 1400, "a partner's saying of a place · in resolving the resolver has a place, and the resolver is the me · me, and other", "left", **small))
over.append(word(60, 84, 730, "one me's moment: all of it is of a me, or of an other", "left", 600, 17, 24))
over.append(word(60, 108, 730, "given two and giving two, the living code's 3 and 2, to 11 and 10 · with nothing of place in its lines", "left", 400, 14, 20, GREY))
over.append(word(182, 176, 190, "its prior", "right", 600, 15, 22, "{{accent}}")); over.append(word(182, 197, 190, "a me", "right", 400, 14, 20, GREY))
over.append(word(182, 328, 190, "what it observes", "right", 600, 15, 22)); over.append(word(182, 349, 190, "an other", "right", 400, 14, 20, GREY))
over.append(word(662, 176, 190, "its next prior", "left", 600, 15, 22, "{{accent}}")); over.append(word(662, 197, 190, "a me", "left", 400, 14, 20, GREY))
over.append(word(662, 328, 190, "its giving", "left", 600, 15, 22)); over.append(word(662, 349, 190, "to an other", "left", 400, 14, 20, GREY))
over.append(word(MX, 352, 300, "is-or-is-not same-existing", "center", 600, 14.5, 20))
over.append(word(MX, 374, 420, "what it observes: the same in all orders, with all repeats", "center", 400, 14, 20, GREY))
over.append(word(60, 452, 730, "one round of five mes, drawn three ways: one resolving", "left", 600, 17, 24))
over.append(word(60, 476, 730, "a place of a me is its couplings, a me and its others · a line, a round and no order of place are a drawing's", "left", 400, 14, 20, GREY))
for cx, t in zip(PX, ("on a line", "on a round", "with no order of place")): over.append(word(cx, 686, 220, t, "center", 400, 13.5, 20, GREY))
over.append(word(TX + CW * 5 + 18, TY + 36, 300, "six moments of the five", "left", 600, 14, 20)); over.append(word(TX + CW * 5 + 18, TY + 58, 300, "the same with all three, and with", "left", 400, 13.5, 20, GREY))
over.append(word(TX + CW * 5 + 18, TY + 77, 300, "the five renamed, their couplings", "left", 400, 13.5, 20, GREY)); over.append(word(TX + CW * 5 + 18, TY + 96, 300, "renamed with them", "left", 400, 13.5, 20, GREY))
over.append(word(840, 84, 640, "mes more, beside my round: in the society, and in my resolving", "left", 600, 17, 24))
over.append(word(840, 108, 640, "an other is a me whose giving a me of mine observes", "left", 400, 14, 20, GREY))
RP = [("x and y, coupled to one another alone · z, given to by mine", "all moments of mine are the same as with none of them: non-existing in my resolving",
       "in the society x and y are · from my moments alone their is-or-is-not is not said"),
      ("w, giving to a me of mine", "the moments of mine are other than with none of it: an other", ""),
      ("a place, by the living code's own lines", "the names saying which me are 5, 13 and 16, in its going on, and in no line of a me's own moment",
       "of the nine names 5 alone, the bi-couplings, a me and its others: in all three of a partner's fours"),
      ("a drawing's places", "the diamonds, the cones and the sphere of the fourth to the 24th drawings are a drawing's places",
       "under them are numbers, and a me with its others: the checks execute those, and no place")]
y = 410.0
for a, b, c in RP:
    over.append(word(840, y, 640, a, "left", 600, 16, 22)); over.append(word(840, y + 23, 650, b, "left", 400, 14, 20))
    if c: over.append(word(840, y + 44, 650, c, "left", 400, 13.5, 20, GREY))
    y += 98 if c else 72
over.append(word(840, 800, 640, "floating on a surface, neutralling on a line, and at a place", "left", 600, 16, 22))
over.append(word(840, 823, 650, "<i>A corus is a self's own inverting, + to −, and neither is its place.</i>", "left", 400, 14, 20))
over.append(word(840, 842, 650, "Exhibit FOUR Natural Mathematics", "left", 400, 13.5, 20, GREY))
over.append(word(840, 867, 650, "<i>Corusing reaches a corus from a surface, and torusing reaches a surface from a corus</i>", "left", 400, 14, 20))
over.append(word(840, 886, 650, "Natural Intelligence", "left", 400, 13.5, 20, GREY))
title = (f'<div style="position: absolute; left: 60px; top: 938px; width: {W - 120}px; text-align: center; '
         f'{SANS}; font-weight: 600; font-size: 30px; line-height: 38px; color: {INK}">A place in resolving: a me, and beside it an other</div>')
caption = (f'<div style="position: absolute; left: 60px; top: 988px; width: {W - 120}px; text-align: center; '
           f'{SANS}; font-weight: 400; font-size: 18px; line-height: 28px; color: {GREY}">'
           f'A me\'s moment is given two, its prior and what it observes, and gives two, its next prior and its giving: a me, and an other, all through.<br>'
           f'Mes renamed, their couplings with them, have the same moments: a place of a me is its couplings, and a line, a round and a diamond are a drawing\'s.<br>'
           f'A me that is neither mine nor an other of mine is non-existing in my resolving, and in the society it is: from my moments alone it is an is-or-is-not.<br>'
           f'Of the nine names 5 alone says which me and which other, the bi-couplings. A partner has it in all three fours.</div>')
props = {"accent": {"editor": "color", "default": DEFAULT_ACCENT, "options": [DEFAULT_ACCENT, "#1d4ed8", "#0f766e", "#7c3aed"]}, "$preview": {"width": W, "height": H}}
body = svg + "\n" + "\n".join(over) + "\n" + title + "\n" + caption
html = page("A place in resolving: a me, and beside it an other", W, H, body, json.dumps(props, ensure_ascii=False))
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
Path(OUT, "Draft25.dc.html").write_text(html, encoding="utf-8")
pv = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>'
      f'<div style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: #ffffff; {SANS}; color: {INK}">' + body.replace("{{accent}}", DEFAULT_ACCENT) + '</div></body></html>')
Path(WORK, "draft25_preview.html").write_text(pv, encoding="utf-8")
words = re.sub(r"</?i>", "*", re.sub(r"<svg.*?</svg>", "", body, flags=re.S))                # a living sentence in italics, as a page has it
words = [ARIA] + [re.sub(r"<[^>]+>", "", w).strip() for w in re.sub(r"<br>", "\n", re.sub(r"</div>", "\n", words)).split("\n")]
Path(WORK, "draft25_words.md").write_text("\n".join(w for w in words if w) + "\n", encoding="utf-8")
print(len(html), "bytes;", len([w for w in words if w]), "lines of words;", "the five's moments:", " | ".join("".join(MARK[m[k]] for k in range(5)) for m in FIVE))
