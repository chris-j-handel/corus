"""v408illustrating · a view of an artboard: a drawing's PNG from its working preview.

Usage, from the repository's root:
  python3 -I incoming/v408illustrating/instruments/make_draft56.py incoming/v408illustrating/illustrations/artboards A_WORKING_FOLDER
  python3 -I incoming/v408illustrating/instruments/a_view_of_an_artboard.py A_WORKING_FOLDER/draft56_preview.html A_VIEW.png

A maker lays its artboard in the set and a working preview beside its words in a working folder. This instrument opens the
preview in a browser with no window, 1520 by 1150, and writes its view. It was this session's own tool from its opening
drawing on, laid in the folder at the wrap. It needs playwright with its chromium.
"""
import os, sys
from playwright.sync_api import sync_playwright

src, out = os.path.abspath(sys.argv[1]), sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1520, "height": 1150}, device_scale_factor=1)
    pg.goto("file://" + src); pg.wait_for_timeout(300)
    pg.screenshot(path=out, clip={"x": 0, "y": 0, "width": 1520, "height": 1150}); b.close()
