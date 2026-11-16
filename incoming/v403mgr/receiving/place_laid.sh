#!/bin/bash
# One of three, the managing session's receiving, as v403mgr executed it with each returning of 16 November.
# Copy the three to a folder outside the clone and execute the copies: a script changing branches is not read
# out of the clone it changes. Say your own session's lines first, each all or none:
#   export COMMIT_LINES="Co-Authored-By: ...\nClaude-Session: ..."     the two lines a commit of yours ends with
#   export PR_LINES="... Generated with ...\n\nhttps://..."            the lines a pull request of yours ends with
#   export MGR=v403mgr     your session's name;   ROOT, the clone, and RUN, a scratch folder, have their own values
ROOT="${ROOT:-/home/claude/corus}"; RUN="${RUN:-/tmp/run}"; MGR="${MGR:-v403mgr}"; HERE="$(cd "$(dirname "$0")" && pwd)"; DAY="$(date '+%-d %B')"; mkdir -p "$RUN"
# Inside $ROOT on a working branch: v403cohering's placing instrument, executed by a second hand,
# then read by an other reading than its own: each non-blank line of the gathering files the same lines, each
# heading the same and in order. With a parting, the gathering files are put back as they were.
cd "$ROOT" || exit 1
I=incoming/v403cohering/instruments/each_laid_is_or_is_not_to_its_section.py
[ -f $I ] || { echo "placing: no instrument"; exit 0; }
SNAP=$RUN/snap_gv; rm -rf $SNAP; cp -r gathering-value $SNAP
(cd $RUN && python3 -I $ROOT/$I $ROOT) > $RUN/place.out 2>&1; rc=$?
python3 -I - $rc "$RUN" <<'EOF'
import collections, glob, os, sys
rc = int(sys.argv[1]); RUN = sys.argv[2]; ok = rc == 0; was = collections.Counter(); now = collections.Counter(); changed = []
for p in sorted(glob.glob(RUN + '/snap_gv/*.md')):
    q = os.path.join('gathering-value', os.path.basename(p))
    a = open(p, encoding='utf-8').read().split('\n'); b = open(q, encoding='utf-8').read().split('\n') if os.path.exists(q) else []
    was.update(l for l in a if l.strip()); now.update(l for l in b if l.strip())
    ok = ok and [l for l in a if l.startswith('#')] == [l for l in b if l.startswith('#')]
    if a != b: changed.append(os.path.basename(p)[:-3])
ok = ok and was == now and len(glob.glob('gathering-value/*.md')) == len(glob.glob(RUN + '/snap_gv/*.md'))
open(RUN + '/place_changed.txt', 'w').write(' '.join(changed) if ok else '')
print(f"placing: {'each line the same lines, each heading in order' if ok else 'a parting, put back'} · files with a line placed: {' '.join(changed) or 'none'}")
sys.exit(0 if ok else 1)
EOF
if [ $? -ne 0 ]; then rm -rf gathering-value; cp -r $SNAP gathering-value; echo "placing: put back"; fi
grep "^would bring\|^brought\|^  [A-Z].* · .*: [0-9]" $RUN/place.out | head -12 | cut -c1-200
