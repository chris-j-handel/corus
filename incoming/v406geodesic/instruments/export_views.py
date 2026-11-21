"""Standalone views of the three artboards, for seeing them on GitHub or in any browser.

Reads ../illustrations/artboards/<name>.dc.html and writes ../illustrations/<view>.svg
(drawing, torus body and words in one file), and a PNG beside it when rsvg-convert is installed.
The words are set in the fonts the machine has; the canvas sets them in Inter and STIX Two Text.
"""
import base64, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "..", "illustrations", "artboards")
OUTD = os.path.join(HERE, "..", "illustrations")
ACCENT = "#c2410c"
VIEWS = [("Main", "draft_1_the_three_right_angle_triangle"),
         ("Draft2", "draft_2_bi-folding_the_triangle"),
         ("Draft3", "draft_3_1_to_17_on_a_torus")]


def style_of(s):
    return {k.strip(): v.strip() for k, v in (p.split(":", 1) for p in s.split(";") if ":" in p)}


def px(v):
    return float(v.replace("px", ""))


def text_el(st, text):
    left, top, width = px(st["left"]), px(st["top"]), px(st["width"])
    lh = px(st.get("line-height", st.get("height", "20px")))
    fam = st.get("font-family", "sans-serif").replace('"', "'")
    size = px(st.get("font-size", "16px"))
    attrs = (f'font-family="{fam}" font-size="{size:g}" font-weight="{st.get("font-weight", "400")}" '
             f'fill="{st.get("color", "#1f2430")}"')
    if st.get("font-style") == "italic":
        attrs += ' font-style="italic"'
    align = st.get("text-align", "center")
    x, anchor = {"center": (left + width / 2, "middle"), "right": (left + width, "end")}.get(align, (left, "start"))
    lines = [t.strip() for t in re.split(r"<br\s*/?>", text)]
    out = []
    for i, line in enumerate(lines):
        y = top + lh * i + lh / 2 + size * 0.35
        out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" {attrs}>{line}</text>')
    return "".join(out)


def export(stem, view):
    src = open(os.path.join(ART, stem + ".dc.html"), encoding="utf-8").read()
    root = re.search(r'<div style="position: relative; width: (\d+)px; height: (\d+)px', src)
    W, H = int(root.group(1)), int(root.group(2))
    parts = []
    for m in re.finditer(r'<svg (?P<a>[^>]*)>(?P<b>.*?)</svg>|<img src="(?P<src>[^"]+)"[^>]*style="(?P<ist>[^"]+)"'
                         r'|<div style="(?P<st>position: absolute;[^"]+)">(?P<t>.*?)</div>', src, re.S):
        if m.group("b") is not None:
            parts.append(m.group("b"))
        elif m.group("src") is not None:
            st = style_of(m.group("ist"))
            png = os.path.join(ART, "torus_body@2x.png")
            b64 = base64.b64encode(open(png, "rb").read()).decode()
            parts.append(f'<image href="data:image/png;base64,{b64}" x="{px(st["left"]):g}" y="{px(st["top"]):g}" '
                         f'width="{px(st["width"]):g}" height="{px(st["height"]):g}"></image>')
        else:
            parts.append(text_el(style_of(m.group("st")), m.group("t")))
    body = "".join(parts).replace("{{accent}}", ACCENT).replace("&#39;", "’")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
           f'<rect width="{W}" height="{H}" fill="#ffffff"></rect>{body}</svg>')
    out = os.path.join(OUTD, view + ".svg")
    open(out, "w", encoding="utf-8").write(svg)
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", str(W), out, "-o", os.path.join(OUTD, view + ".png")], check=True)
    print(view, W, H)


for stem, view in VIEWS:
    export(stem, view)
