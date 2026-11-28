"""v410illustrating · a breaking named by a partner on 27 November, saying 24: nothing comes again in nature.

Usage, from the repository's root:
  python3 -I incoming/v410illustrating/instruments/the_places_of_a_coming_again_in_this_session_s_drawings.py .

It finds the places in this session's own drawings saying a number, a cell, a 0 or a crossing coming again or going
back, and passes over a work's own words of a making: made again, said again, laid again. It writes in no file.
A drawing with none is an is; a drawing with a place is found, its places said.
"""
import re, sys
from collections import Counter
from pathlib import Path
WORK = r"(made|said|laid|executed|drawn|opened|checked)\s+again"
COMING = r"\b(again|back|return\w*)\b"

def words_of(path):
    t = Path(path).read_text(encoding="utf-8")
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>", " ", t, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))

def checks(root):
    root = Path(root).resolve(); lines = []; total = 0
    for n in range(57, 100):
        f = root / f"incoming/v410illustrating/illustrations/artboards/Draft{n}.dc.html"
        if not f.exists(): continue
        t = re.sub(WORK, " ", words_of(f), flags=re.I)
        t = re.sub(r"\b(the front|the back|its back|front to back|a back)\b", " ", t)      # the 23rd drawing's front and back of two diamonds: a side, no going
        places = [t[max(0, m.start() - 34):m.end() + 22].strip() for m in re.finditer(COMING, t, flags=re.I)]
        total += len(places)
        lines.append(("is" if not places else "found", f"the drawing {n}: {len(places)} places" + ("" if not places else ": " + " | ".join(places[:3]) + (" | and more" if len(places) > 3 else ""))))
    return lines, total

if __name__ == "__main__":
    lines, total = checks(sys.argv[1] if len(sys.argv) > 1 else ".")
    said = Counter(k for k, _ in lines)
    for k, w in lines: print(f"{k:7s} {w}")
    print(f"\n{total} places in all; {said['is']} drawings with none; {said['found']} with a place")
