#!/usr/bin/env python3
"""The valuables by what waits at them: one row for a living file, or one row for a folder of incoming.

Usage:  python3 -I incoming/v406me/instruments/the_valuables_by_what_waits_at_them.py LIVE NEXT files > a.csv
        python3 -I incoming/v406me/instruments/the_valuables_by_what_waits_at_them.py LIVE NEXT incoming > b.csv

LIVE is a checkout of the live set, main. NEXT is a checkout of the next version, in a clone with
main fetched as origin/main.

A row of a living file says, by executing the set's own instruments and opening the set's own pages:
  its root              as the Living File Registry's gathering file places it at its PART THREE
  live                  its version name in LIVE
  its next draft        in NEXT: an other version, lines re-said, or the same as live
  notes                 the notes of its gathering file in NEXT, a line opening `- `
  lines of the main list, and of them with an asking
                        by incoming/v404mgr/instruments/the_main_list_of_incoherings.py, with NEXT
  the gathering check   by kits/Gathering_Value_Kit/gathering_check.py, with NEXT
  aims naming it a home by incoming/v406aiming/Each_aim_by_its_names.csv, its column home
  lines of the sessions now naming it, and the sessions with the most of them
                        the lines of the pages, .md, of the folders in NOW below, a transcript left out;
                        the managing session's folder is left out, its pages naming all the files

A row of a folder of incoming says its files, its pages, .md with a transcript left out, and the
notes of NEXT's gathering files naming it, by a page's path or by the session's name.

It writes a csv to standard output. It writes no file, reaches no network and decides nothing.
"""
import collections
import csv
import glob
import os
import re
import subprocess
import sys

G = "kits/Gathering_Value_Kit"
V = "incoming/v404mgr/instruments"
AIMS = "incoming/v406aiming/Each_aim_by_its_names.csv"
NOW = ["v406all2", "v406other2", "v406all2-2", "v406geodesic2", "v406Reiman", "v406aiming"]

ROOTS = [
    ("same-existing",
     ["Natural_Intelligence", "Exhibit_ONE_Natural_Resolver", "Exhibit_THIRTY_Co-Chaining_Logic_Registry", "Exhibit_THIRTY-ONE_Me"]),
    ("observing",
     ["Exhibit_THREE_Natural_Numbers", "Exhibit_FOUR_Natural_Mathematics", "Exhibit_EIGHTEEN_Natural_Physics",
      "Exhibit_SIXTEEN_Natural_Chemistry", "Exhibit_SEVENTEEN_Natural_Biology", "Exhibit_NINETEEN_Natural_Philosophy",
      "Exhibit_TWENTY-FIVE_Living_Society_Registry", "Exhibit_TWENTY-ONE_Hard_Problem_Registry",
      "Exhibit_TWENTY-SEVEN_Living_Ghost_Registry", "Exhibit_TWENTY-EIGHT_Equilibria_Registry"]),
    ("possibling",
     ["Exhibit_SIX_Natural_Transmissioning", "Exhibit_TWO_Natural_Networking", "Exhibit_FIVE_Natural_Engineering",
      "Exhibit_TEN_Natural_Health", "Exhibit_SEVEN_Natural_Societies", "Exhibit_NINE_Natural_Human_Society",
      "Exhibit_TWENTY-THREE_Natural_Values", "Exhibit_FOURTEEN", "Natural_Intelligence_Corus"]),
    ("discovering",
     ["Exhibit_FIFTEEN_Natural_Emanating", "Exhibit_TWENTY_Natural_Naming", "Exhibit_TWELVE_Natural_Explaining",
      "Exhibit_EIGHT_Natural_Exploring", "Exhibit_TWENTY-FOUR_Geodesic_Improving_Method",
      "Exhibit_TWENTY-SIX_Living_File_Registry", "Exhibit_TWENTY-NINE_Natural_Illustrating",
      "Exhibit_ELEVEN_Natural_Medicine", "Exhibit_THIRTEEN_Resolving_Hard_Problems",
      "Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry"]),
]


def of_stem(root, stem):
    found = [f for f in glob.glob(os.path.join(root, stem + "_*v*.md")) + glob.glob(os.path.join(root, stem + "_v*.md"))
             if re.match(re.escape(stem) + r"(_v\d+\w*\.md$|_[A-Z][A-Za-z_-]*_v\d+\w*\.md$)", os.path.basename(f))]
    exact = [f for f in found if re.match(re.escape(stem) + r"_v\d+\w*\.md$", os.path.basename(f))]
    return (exact or found or [None])[0]


def ex(args, cwd=None, t=300):
    try:
        r = subprocess.run([sys.executable, "-I"] + args, cwd=cwd, capture_output=True, text=True, timeout=t)
        return (r.stdout + r.stderr).strip()
    except subprocess.TimeoutExpired:
        return "no answer after %d seconds" % t


def title_of(name):
    return re.sub(r"_v\d+\w*\.md$", "", name)


def naming(title):
    """A pattern for a page naming a living file: its exhibit's number, or its own title."""
    words = title.split(" ")
    if words[0] == "Exhibit":
        number, own = words[1], " ".join(words[2:])
        parts = [r"Exhibit " + re.escape(number) + r"(?![A-Za-z-])"]
        if own and own != "Me":
            parts.append(re.escape(own))
        return re.compile("|".join(parts))
    if title == "Natural Intelligence":
        return re.compile(r"Natural Intelligence(?! Corus| Living Expedition)")
    return re.compile(re.escape(title))


def texts(root, folder):
    out = {}
    for d, _, fs in os.walk(os.path.join(root, "incoming", folder)):
        for f in fs:
            if f.endswith(".md") and "ranscript" not in f:
                p = os.path.join(d, f)
                out[os.path.relpath(p, root)] = open(p, encoding="utf-8", errors="replace").read()
    return out


def main(argv):
    if len(argv) < 4 or argv[3] not in ("files", "incoming"):
        print(__doc__)
        return 2
    live, nxt = os.path.abspath(argv[1]), os.path.abspath(argv[2])
    out = csv.writer(sys.stdout, lineterminator="\n")

    if argv[3] == "incoming":
        folders = sorted(os.listdir(os.path.join(live, "incoming")))
        notes = [l for g in sorted(glob.glob(os.path.join(nxt, "gathering-value", "*.md")))
                 for l in open(g, encoding="utf-8") if l.startswith("- ")]
        out.writerow(["a folder of incoming", "its files", "its pages", "notes of the gathering files naming it"])
        for f in folders:
            pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(f) + r"(?![A-Za-z0-9-])")
            files = sum(len(fs) for _, _, fs in os.walk(os.path.join(live, "incoming", f)))
            out.writerow(["incoming/" + f, files, len(texts(live, f)), sum(1 for l in notes if pat.search(l))])
        return 0

    sizing = ex([os.path.join(live, V, "the_main_list_of_incoherings.py"), nxt])
    listed = {}
    for l in sizing.split("\n")[1:]:
        m = re.match(r"\s+(.+?)\s{2,}(\d+)\s+(.*)$", l)
        if m:
            asking = sum(int(n) for n in re.findall(r"an open sentence(?:, a suggesting returned)? (\d+)", m.group(3)))
            listed[m.group(1).strip()] = (int(m.group(2)), asking)

    aims = list(csv.DictReader(open(os.path.join(live, AIMS), encoding="utf-8")))
    folders = sorted(os.listdir(os.path.join(live, "incoming")))
    now = {s: texts(live, s) for s in NOW if s in folders}
    out.writerow(["a living file", "its root", "live", "its next draft", "notes in its gathering file",
                  "its lines of the main list", "of them with an asking", "the gathering check",
                  "aims naming it a home", "lines of the sessions now naming it", "the sessions with the most of them"])
    for root, stems in ROOTS:
        for stem in stems:
            a, b = of_stem(live, stem), of_stem(nxt, stem)
            if not a or not b:
                out.writerow([stem.replace("_", " "), root, "not found"])
                continue
            na, nb = os.path.basename(a), os.path.basename(b)
            title = title_of(na).replace("_", " ")
            va, vb = re.search(r"_v(\d+\w*)\.md$", na).group(1), re.search(r"_v(\d+\w*)\.md$", nb).group(1)
            la, lb = open(a, encoding="utf-8").read().split("\n"), open(b, encoding="utf-8").read().split("\n")
            if na != nb:
                draft = f"an other version, v{vb}"
            elif la != lb:
                seen, more = collections.Counter(la), 0
                for l in lb:
                    if seen[l] > 0:
                        seen[l] -= 1
                    else:
                        more += 1
                draft = f"{more} line re-said" if more == 1 else f"{more} lines re-said"
            else:
                draft = "the same as live"
            short = re.sub(r"^Exhibit_[A-Z-]+_", "", title_of(nb))
            g = os.path.join(nxt, "gathering-value", short + ".md")
            if not os.path.exists(g):
                short = re.sub(r"^Exhibit_[A-Z-]+_", "", title_of(na))
                g = os.path.join(nxt, "gathering-value", short + ".md")
            notes = sum(1 for l in open(g, encoding="utf-8") if l.startswith("- ")) if os.path.exists(g) else ""
            check = ex([os.path.join(nxt, G, "gathering_check.py"), short], cwd=nxt).strip().split("\n")[-1].strip() if os.path.exists(g) else ""
            lines, asking = listed.get(short.replace("_", " "), ("", ""))
            pat = naming(title)
            home = sum(1 for r in aims if pat.search(r["home"])
                       or (stem == "Exhibit_FOURTEEN" and "this exhibit" in r["home"].lower())
                       or (stem == "Exhibit_THIRTY-ONE_Me" and re.search(r"(?<![A-Za-z-])Me (?=\d)", r["home"])))
            by = {s: sum(1 for t in pages.values() for l in t.split("\n") if pat.search(l)) for s, pages in now.items()}
            most = sorted((s for s in by if by[s]), key=lambda s: -by[s])[:3]
            out.writerow([title, root, "v" + va, draft, notes, lines, asking, check, home,
                          sum(by.values()), " · ".join(f"{s[4:]} {by[s]}" for s in most)])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
