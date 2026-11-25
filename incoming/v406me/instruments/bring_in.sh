#!/bin/bash
# usage, from the set's root: incoming/v406me/instruments/bring_in.sh N "its title"
# brings offer N into main, then brings the next version current with the live set.
# TRAILERS, in the environment, is the session's own lines for the end of a commit's saying.
cd "$(git rev-parse --show-toplevel)" || exit 1
gh api repos/chris-j-handel/corus/pulls/$1/merge -X PUT -f merge_method=merge -f commit_title="Merge #$1: $2" -q '"brought in: \(.merged)"' 2>&1 | tail -1
git checkout -q main && git pull -q --ff-only origin main
B=working/natural-intelligence-with-exhibit-one-its-next-version-v403mgr
git fetch -q origin "+$B:refs/remotes/origin/copy"
git checkout -q -B copy-local refs/remotes/origin/copy && git merge -q --no-ff origin/main -m "The next version's copy brought current with main

$TRAILERS" 2>&1 | tail -2
K=kits/Living_File_Registry_TWENTY-SIX_Improving_Kit
echo "the next version's checks: $(python3 -I $K/check_set.py . | tail -1); files other-than incoming moved: $(git diff --name-only refs/remotes/origin/copy HEAD -- . ':!incoming' | wc -l)"
git -c push.negotiate=true push -q origin copy-local:$B 2>&1 | grep -v '^remote:' | tail -1
git checkout -q main
