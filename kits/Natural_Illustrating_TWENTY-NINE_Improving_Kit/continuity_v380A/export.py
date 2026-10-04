"""v380A: put the editable concept into its existing standalone wrapper."""

from html import escape, unescape
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
START = "<!-- v380A editable concept begins -->"
END = "<!-- v380A editable concept ends -->"


def export():
    page = HERE / "index.html"
    outer = page.read_text()
    match = re.search(r'data-srcdoc="([^"]*)"', outer, re.S)
    if match is None:
        raise ValueError("The standalone wrapper's data-srcdoc is missing")
    inner = unescape(match[1])
    fragment = (HERE / "v380A_Following_1_Into_3.fragment.html").read_text().strip()
    region = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if len(region.findall(inner)) != 1:
        raise ValueError("The editable concept markers must occur once")
    inner = region.sub(lambda _: START + "\n" + fragment + "\n" + END, inner)
    page.write_text(outer[:match.start(1)] + escape(inner, quote=True) + outer[match.end(1):])
    print("v380A concept exported to index.html")


if __name__ == "__main__":
    export()
