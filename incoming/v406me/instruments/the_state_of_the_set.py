#!/usr/bin/env python3
"""The state of the set, executed: one page, written again whole at a sitting's end.

Usage:  python3 -I incoming/v406me/instruments/the_state_of_the_set.py LIVE NEXT [DATE]

LIVE is a checkout of the live set, main. NEXT is a checkout of the next version, in a clone
with main fetched as origin/main: the gathering check asks git for a gathering file as it is
live. DATE is the day said at the page's opening.

It executes the set's own checks and instruments, each with -I, and says what each said:
  1 check_set.py, with LIVE and with NEXT: the living files' contents, tables, version lines,
    Exhibit ONE one with Natural Intelligence, and the code executing
  2 gathering_check.py, for all the gathering files of NEXT, against origin/main
  3 NEXT beside LIVE: the living files of another version, and the incoming folders and pages
    that LIVE has and NEXT has not
  4 the_main_list_of_incoherings.py, with NEXT
  5 words_of_no_natural_naming_in_a_page.py --set, with LIVE and with NEXT
  6 the notes of NEXT's gathering files that name a page of incoming, by the folder named:
    a folder LIVE has, or a folder gone to the set's history
  7 all the living files by the set's four roots, as the Living File Registry's gathering file
    places them at its PART THREE, a living file with its live version, its next draft and
    the notes in its gathering file

It writes the page to standard output. It writes no file, reaches no network and decides
nothing. The open offers and the thread are not in it: they are gone through at the exchange.
"""
import collections
import glob
import os
import re
import subprocess
import sys

K = "kits/Living_File_Registry_TWENTY-SIX_Improving_Kit"
G = "kits/Gathering_Value_Kit"
V = "incoming/v404mgr/instruments"


ROOTS = [
    ("Same-existing, through all: the one method, its code, its co-chaining and a me",
     ["Natural_Intelligence", "Exhibit_ONE_Natural_Resolver", "Exhibit_THIRTY_Co-Chaining_Logic_Registry", "Exhibit_THIRTY-ONE_Me"]),
    ("Observing, prior-existing, along: a self and the universe",
     ["Exhibit_THREE_Natural_Numbers", "Exhibit_FOUR_Natural_Mathematics", "Exhibit_EIGHTEEN_Natural_Physics",
      "Exhibit_SIXTEEN_Natural_Chemistry", "Exhibit_SEVENTEEN_Natural_Biology", "Exhibit_NINETEEN_Natural_Philosophy",
      "Exhibit_TWENTY-FIVE_Living_Society_Registry", "Exhibit_TWENTY-ONE_Hard_Problem_Registry",
      "Exhibit_TWENTY-SEVEN_Living_Ghost_Registry", "Exhibit_TWENTY-EIGHT_Equilibria_Registry"]),
    ("Possibling, now-existing, across: a self and an other",
     ["Exhibit_SIX_Natural_Transmissioning", "Exhibit_TWO_Natural_Networking", "Exhibit_FIVE_Natural_Engineering",
      "Exhibit_TEN_Natural_Health", "Exhibit_SEVEN_Natural_Societies", "Exhibit_NINE_Natural_Human_Society",
      "Exhibit_TWENTY-THREE_Natural_Values", "Exhibit_FOURTEEN", "Natural_Intelligence_Corus"]),
    ("Discovering, next-existing, along",
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


def last(text):
    lines = [l for l in text.split("\n") if l.strip()]
    return lines[-1].strip() if lines else "no answer"


def living_files(root):
    return sorted(os.path.basename(f) for f in glob.glob(os.path.join(root, "*_v*.md")))


def title_of(name):
    return re.sub(r"_v\d+\w*\.md$", "", name)


def pages(root):
    out = {}
    for d, _, fs in os.walk(os.path.join(root, "incoming")):
        for f in fs:
            p = os.path.join(d, f)
            out[os.path.relpath(p, root)] = open(p, "rb").read()
    return out


def words(live, root):
    text = ex([os.path.join(live, V, "words_of_no_natural_naming_in_a_page.py"), "--set", root])
    rows = {}
    for l in text.split("\n"):
        m = re.match(r"\s+(.+?)\s{2,}(\d+) places in\s+(\d+) files", l)
        if m:
            rows[m.group(1)] = int(m.group(2))
    return rows


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    live, nxt = os.path.abspath(argv[1]), os.path.abspath(argv[2])
    date = argv[3] if len(argv) > 3 else "a sitting's end"
    say = []

    say.append(f"Incoming · the state of the set, executed · {date}")
    say.append("")
    say.append("# The state of the set, executed")
    say.append("")
    say.append(f"*Written by `incoming/v406me/instruments/the_state_of_the_set.py` on {date}, out of the live set and the next version as they are. A line here is what an instrument said. The page is written again whole, and no line of it is brought from an earlier page. No word here is an authority over the living files.*")
    say.append("")

    say.append("## The set's checks")
    say.append("")
    for name, root in (("the live set", live), ("the next version", nxt)):
        say.append(f"- With {name}, `check_set.py` says: {last(ex([os.path.join(root, K, 'check_set.py'), root]))}")
    say.append("")

    say.append("## The gathering check, with the next version")
    say.append("")
    found, clear = [], 0
    for g in sorted(glob.glob(os.path.join(nxt, "gathering-value", "*.md"))):
        t = os.path.basename(g)[:-3]
        answer = last(ex([os.path.join(nxt, G, "gathering_check.py"), t], cwd=nxt))
        if answer == "nothing found":
            clear += 1
        else:
            found.append(f"{t.replace('_', ' ')}, {answer}")
    say.append(f"- Nothing found: {clear} gathering files.")
    say.append(f"- With findings: {len(found)}" + (": " + "; ".join(found) + "." if found else "."))
    say.append("")

    say.append("## The next version beside the live set")
    say.append("")
    lf, nf = living_files(live), living_files(nxt)
    other = [f"{title_of(a).replace('_', ' ')}, live {a[len(title_of(a)) + 1:-3]}, next {b[len(title_of(b)) + 1:-3]}"
             for a in lf for b in nf if a != b and title_of(a) == title_of(b)]
    lone_live = [a for a in lf if title_of(a) not in {title_of(b) for b in nf}]
    lone_next = [b for b in nf if title_of(b) not in {title_of(a) for a in lf}]
    resaid = [a for a in lf if a in nf and open(os.path.join(live, a), "rb").read() != open(os.path.join(nxt, a), "rb").read()]
    say.append(f"- The live set has {len(lf)} living files, and the next version {len(nf)}.")
    if other:
        say.append("- A living file of another version in the next version: " + "; ".join(other) + ".")
    if lone_live or lone_next:
        say.append("- A living file of another title: live, " + (", ".join(lone_live) or "none") + "; next, " + (", ".join(lone_next) or "none") + ".")
    say.append(f"- A living file of one same version name with sentences re-said in the next version: {len(resaid)}" + (": " + ", ".join(title_of(a).replace("_", " ") for a in resaid) + "." if resaid else "."))
    lp, np_ = pages(live), pages(nxt)
    folders_live = sorted({p.split(os.sep)[1] for p in lp})
    folders_next = sorted({p.split(os.sep)[1] for p in np_})
    behind = [f for f in folders_live if f not in folders_next]
    apart = sorted(p for p in lp if p in np_ and lp[p] != np_[p])
    lone = sorted(p for p in np_ if p not in lp)
    say.append("- Folders of incoming the live set has and the next version has not: " + (", ".join(behind) if behind else "none") + ".")
    say.append(f"- Pages of incoming in both and not the same: {len(apart)}" + (": " + ", ".join("`" + p + "`" for p in apart[:12]) + "." if apart else "."))
    say.append(f"- Pages of incoming the next version has and the live set has not: {len(lone)}" + (": " + ", ".join("`" + p + "`" for p in lone[:12]) + "." if lone else "."))
    say.append("")

    say.append("## The main list, with the next version")
    say.append("")
    sizing = ex([os.path.join(live, V, "the_main_list_of_incoherings.py"), nxt])
    say.append("- " + (sizing.split("\n")[0].strip() if sizing else "no answer"))
    for l in sizing.split("\n")[1:5]:
        m = re.match(r"\s+(.+?)\s{2,}(\d+)\s+(.*)$", l)
        if m:
            say.append(f"- {m.group(1).strip()}: {m.group(2)} lines; {m.group(3).strip()}")
    say.append("")

    say.append("## The words of the one list, in the living files")
    say.append("")
    wl, wn = words(live, live), words(live, nxt)
    say.append(f"- In the live set: {sum(wl.values())} places. In the next version: {sum(wn.values())} places.")
    moved = [f"*{w}*, {wl[w]} to {wn.get(w, 0)}" for w in wl if wl[w] != wn.get(w, 0)]
    say.append("- A word with another number of places in the next version: " + ("; ".join(moved) if moved else "none") + ".")
    say.append("- The words with the most places, live: " + "; ".join(f"*{w}*, {n}" for w, n in sorted(wl.items(), key=lambda x: -x[1])[:6]) + ".")
    say.append("")

    say.append("## Notes of the next version's gathering files naming a page of incoming")
    say.append("")
    here, gone, notes_here, notes_gone = collections.Counter(), collections.Counter(), 0, 0
    for g in sorted(glob.glob(os.path.join(nxt, "gathering-value", "*.md"))):
        for line in open(g, encoding="utf-8"):
            if not line.startswith("- "):
                continue
            named = set(re.findall(r"incoming/([A-Za-z0-9_.-]+)/", line))
            notes_here += any(n in folders_live for n in named)
            notes_gone += any(n not in folders_live for n in named)
            for n in named:
                (here if n in folders_live else gone)[n] += 1
    say.append(f"- Notes naming a folder the live set has: {notes_here}" + (", by the folder named: " + ", ".join(f"{n} {c}" for n, c in here.most_common()) + "." if here else "."))
    say.append(f"- Notes naming a folder gone to the set's history: {notes_gone}" + (", by the folder named: " + ", ".join(f"{n} {c}" for n, c in gone.most_common()) + "." if gone else "."))
    say.append("")

    say.append("## All the living files, by the set's four roots")
    say.append("")
    say.append("*The roots are as the Living File Registry's gathering file places the files at its PART THREE. A next draft is a living file of the next version: of another version, with lines re-said, or the same as live.*")
    say.append("")
    for root, stems in ROOTS:
        say.append(f"**{root}**")
        say.append("")
        say.append("| A living file | Live | Its next draft | Notes in its gathering file |")
        say.append("|---|---|---|---|")
        for stem in stems:
            a, b = of_stem(live, stem), of_stem(nxt, stem)
            if not a or not b:
                say.append(f"| {stem.replace('_', ' ')} | not found | | |")
                continue
            na, nb = os.path.basename(a), os.path.basename(b)
            va, vb = re.search(r"_v(\d+\w*)\.md$", na).group(1), re.search(r"_v(\d+\w*)\.md$", nb).group(1)
            la, lb = open(a, encoding="utf-8").read().split("\n"), open(b, encoding="utf-8").read().split("\n")
            if na != nb:
                draft = f"another version, v{vb}" + ("" if title_of(na) == title_of(nb) else ", as " + re.sub(r"^Exhibit [A-Z-]+ ", "", title_of(nb).replace("_", " ")))
            elif la != lb:
                seen = collections.Counter(la)
                more = 0
                for l in lb:
                    if seen[l] > 0:
                        seen[l] -= 1
                    else:
                        more += 1
                draft = f"{more} line re-said" if more == 1 else f"{more} lines re-said"
            else:
                draft = "the same as live"
            g = os.path.join(nxt, "gathering-value", re.sub(r"^Exhibit_[A-Z-]+_", "", title_of(nb)) + ".md")
            notes = sum(1 for l in open(g, encoding="utf-8") if l.startswith("- ")) if os.path.exists(g) else "no gathering file found"
            say.append(f"| {title_of(na).replace('_', ' ')} | v{va} | {draft} | {notes} |")
        say.append("")
    print("\n".join(say))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
