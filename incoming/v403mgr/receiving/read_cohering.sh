#!/bin/bash
# One of three, the managing session's receiving, as v403mgr executed it with each returning of 16 November.
# Copy the three to a folder outside the clone and execute the copies: a script changing branches is not read
# out of the clone it changes. Say your own session's lines first, each all or none:
#   export COMMIT_LINES="Co-Authored-By: ...\nClaude-Session: ..."     the two lines a commit of yours ends with
#   export PR_LINES="... Generated with ...\n\nhttps://..."            the lines a pull request of yours ends with
#   export MGR=v403mgr     your session's name;   ROOT, the clone, and RUN, a scratch folder, have their own values
ROOT="${ROOT:-/home/claude/corus}"; RUN="${RUN:-/tmp/run}"; MGR="${MGR:-v403mgr}"; HERE="$(cd "$(dirname "$0")" && pwd)"; DAY="$(date '+%-d %B')"; mkdir -p "$RUN"
# bash read_cohering.sh <PR number> : reads a v403cohering pull request for harm and merges nothing.
PR=$1; cd "$ROOT" || exit 1
git checkout -q main && git pull -q --depth=100 origin main
BR=$(gh api repos/chris-j-handel/corus/pulls/$PR --jq '.head.ref'); TITLE=$(gh api repos/chris-j-handel/corus/pulls/$PR --jq '.title'); echo "PR $PR · $BR · $TITLE"
git fetch -q --depth=80 origin "$BR:refs/remotes/pr/$PR" || exit 1
FILES=$(git diff --name-only main...pr/$PR); echo "$FILES" | sed 's/^/  /'
OUT=$(echo "$FILES" | grep -v '^gathering-value/[A-Za-z_-]*\.md$\|^incoming/v403cohering/'); [ -z "$OUT" ] && echo "each file a gathering file or its own folder's" || echo "OUTSIDE: $OUT"
s=$(gh api repos/chris-j-handel/corus/pulls/$PR --jq '.head.sha'); echo "its checks: $(gh api repos/chris-j-handel/corus/commits/$s/check-runs --jq '[.check_runs[] | .conclusion // "-"] | join(" ")')"
echo "-- lines of its instruments added, reading, writing or importing:"; git diff main...pr/$PR -- incoming/v403cohering/ | grep "^+" | grep "^+import\|^+from\|subprocess\|os\.system\|open(\|urllib\|socket\|eval(\|exec(\|write(\|remove\|shutil\|__import__" | cut -c1-200
git checkout -q -b tmp/read-$PR main && git merge -q --no-ff --no-edit pr/$PR 2>&1 | tail -2
python3 -I - "$RUN" <<'EOF'
import subprocess, glob, os, collections, sys
RUN = sys.argv[1]
def at(ref, p):
    r = subprocess.run(['git', 'show', f'{ref}:{p}'], capture_output=True, text=True); return r.stdout if r.returncode == 0 else ''
was = collections.Counter(); now = collections.Counter(); heads = True; ch = []
for p in sorted(glob.glob('gathering-value/*.md')):
    a = at('main', p).split('\n'); b = open(p, encoding='utf-8').read().split('\n')
    was.update(l for l in a if l.strip()); now.update(l for l in b if l.strip())
    heads = heads and [l for l in a if l.startswith('#')] == [l for l in b if l.startswith('#')]
    if a != b: ch.append(os.path.basename(p)[:-3])
gone = list((was - now).elements()); new = list((now - was).elements())
print(f"on a trial merge · gathering files changed: {' '.join(ch) or 'none'} · each heading the same and in order: {heads} · lines gone {len(gone)} · lines new {len(new)}")
for g in gone[:12]: print('   gone:', g[:150])
for n in new[:12]: print('   new: ', n[:150])
open(RUN + '/read_changed.txt', 'w').write(' '.join(ch))
EOF
K=kits/Living_File_Registry_TWENTY-SIX_Improving_Kit; echo "check_set: $(python3 -I $K/check_set.py . | tail -1) · carry: $(python3 -I $K/carry_check.py . | tail -1 | cut -c1-40)"
echo "reader check, added words against main: $(python3 -I $K/reader_checks.py . main | sed -n '/^3\./,/^4\./p' | grep '" in "\|added words' | cut -c1-160 | tr '\n' ' ')"
for g in $(cat $RUN/read_changed.txt); do n=$(python3 -I kits/Gathering_Value_Kit/gathering_check.py $g main | tail -1); git stash -q 2>/dev/null; git checkout -q main; w=$(python3 -I kits/Gathering_Value_Kit/gathering_check.py $g main | tail -1); git checkout -q tmp/read-$PR; echo "  $g: $n (at main: $w)"; done
git checkout -q main && git branch -q -D tmp/read-$PR
