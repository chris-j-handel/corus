#!/usr/bin/env python3
"""The sessions at their closing: a session's three pages, its commits in no offer, and its askings open.

    python3 -I incoming/v406me/instruments/the_sessions_at_their_closing.py ROOT

A session is whole for its closing with three pages in its folder and nothing of its own outside the set:
its aimings gone through with their starting place now, its page for resuming, and its transcript pared.
v406all2-2's are the three as they are laid first, 25 November. A commit on a session's branch in no offer
is said too, with the askings of the managing table's sheet that are open at the session.
It reads the set and the branches fetched. It writes no file.
"""
import csv, glob, os, subprocess, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
def git(*a):
    try:
        return subprocess.check_output(["git", "-C", root] + list(a), stderr=subprocess.DEVNULL, text=True).strip()
    except subprocess.CalledProcessError:
        return ""
def last(path):
    return git("log", "-1", "--format=%ad", "--date=format:%d %b %H:%M", "--", path)

sessions = ["v406me", "v406all2", "v406aiming", "v406other2", "v406all2-2", "v406geodesic2", "v407nanding"]
asked = list(csv.reader(open(os.path.join(root, "incoming/v406me/The_managing_table_its_sheet_Asked_of_a_session.csv"), newline="")))[1:]
refs = [r for r in git("for-each-ref", "refs/remotes/origin", "--format=%(refname:short)").split("\n") if r]
nxt = next((r for r in refs if "its-next-version" in r), None)
said_again = {"working/arriving-and-the-state-of-the-set-v406me": "its one commit of 21 November is said again by this session's later pages"}
whole = 0
for s in sessions:
    d = os.path.join(root, "incoming", s)
    pages = {
        "its aimings gone through": glob.glob(os.path.join(d, "The_aimings_of_*gone_through.md")),
        "its page for resuming": glob.glob(os.path.join(d, "Resuming_*.md")),
        "its transcript pared": glob.glob(os.path.join(d, "The_transcript_of_*pared.md")),
    }
    print(s)
    have = 0
    for name, found in pages.items():
        if found:
            have += 1
            print(f"  is      {name}, laid {last(os.path.relpath(found[0], root))}")
        else:
            print(f"  is-not  {name}")
    stray = 0
    for r in refs:
        if r.endswith("-" + s) or r.endswith("-" + s.replace("-", "")):
            n = int(git("rev-list", "--count", r, "--not", "origin/main", *( [nxt] if nxt else [] )) or 0)
            if n and r.replace("origin/", "") in said_again:
                print(f"  found   {n} commits at {r.replace('origin/', '')}: {said_again[r.replace('origin/', '')]}")
            elif n:
                stray += n
                print(f"  found   {n} commits in no offer brought in, at {r.replace('origin/', '')}")
    mine = [a for a in asked if (a[1] == s or a[1] == "all the sessions") and a[7] in ("asked", "at it", "a saying given")]
    own = [a[0] for a in mine if a[1] == s]
    print(f"  found   askings open at it: {len(own)}" + (", the askings " + ", ".join(own) if own else "") + f"; open at all the sessions: {len(mine) - len(own)}")
    if have == 3 and not stray:
        whole += 1
        print("  whole for its closing")
print(f"\n{whole} of {len(sessions)} sessions are whole for their closing.")
