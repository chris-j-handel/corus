#!/bin/bash
# One of three, the managing session's receiving, as v403mgr executed it with each returning of 16 November.
# Copy the three to a folder outside the clone and execute the copies: a script changing branches is not read
# out of the clone it changes. Say your own session's lines first, each all or none:
#   export COMMIT_LINES="Co-Authored-By: ...\nClaude-Session: ..."     the two lines a commit of yours ends with
#   export PR_LINES="... Generated with ...\n\nhttps://..."            the lines a pull request of yours ends with
#   export MGR=v403mgr     your session's name;   ROOT, the clone, and RUN, a scratch folder, have their own values
ROOT="${ROOT:-/home/claude/corus}"; RUN="${RUN:-/tmp/run}"; MGR="${MGR:-v403mgr}"; HERE="$(cd "$(dirname "$0")" && pwd)"; DAY="$(date '+%-d %B')"; mkdir -p "$RUN"
: "${COMMIT_LINES:?say your own session's two lines for a commit}"; : "${PR_LINES:?say your own session's lines for a pull request}"
export ROOT RUN MGR DAY
# bash receive_bubble.sh <PR number> <its ordinal, as seventeenth> : receive one returning of the session v403bubble: read for harm, execute by a second hand, merge, bring each value to its gathering file
PR=$1; ORD=$2; cd "$ROOT" || exit 1
git checkout -q main && git pull -q --depth=100 origin main
BR=$(gh api repos/chris-j-handel/corus/pulls/$PR --jq '.head.ref'); TITLE=$(gh api repos/chris-j-handel/corus/pulls/$PR --jq '.title')
echo "PR $PR · $BR · $TITLE" | cut -c1-200
git fetch -q --depth=50 origin "$BR" || exit 1
FILES=$(git diff --name-only main...FETCH_HEAD)
for x in $FILES; do case "$x" in incoming/v403bubble/*) ;; *) echo "STOP: a file outside its folder: $x"; exit 1;; esac; done
s=$(gh api repos/chris-j-handel/corus/pulls/$PR --jq '.head.sha'); c=$(gh api repos/chris-j-handel/corus/commits/$s/check-runs --jq '[.check_runs[] | .conclusion // "-"] | join(" ")')
echo "its checks: $c"; echo "$c" | grep -q success || { echo "STOP: checks"; exit 1; }
H=$(git diff main...FETCH_HEAD -- incoming/v403bubble/instruments/ | grep "^+" | grep "^+import\|^+from\|subprocess\|os\.system\|open(\|urllib\|socket\|eval(\|exec(\|write(\|remove\|shutil")
# a line read by hand and said in ALLOW, as: export ALLOW="+import ast", is passed over, word for word; each other is a stop
[ -n "$ALLOW" ] && { H=$(echo "$H" | grep -vxF -- "$ALLOW"); echo "passed over, read by hand: $ALLOW"; }
[ -n "$H" ] && { echo "STOP: the instrument's new lines reach:"; echo "$H" | cut -c1-200; exit 1; }
D=$RUN/b$PR; rm -rf $D; mkdir -p $D; git show FETCH_HEAD:incoming/v403bubble/instruments/bubble_betweens.py > $D/bubble_betweens.py
(cd $RUN && python3 -I $D/bubble_betweens.py $ROOT > $D/out.txt 2>&1)
N=$(grep -c "  is ·" $D/out.txt); Z=$(grep -c "is-not ·" $D/out.txt); T=$(tail -1 $D/out.txt)
echo "its instrument by a second hand: $N is, $Z is-not, '$T'"; [ "$T" = "each check is" ] && [ "$Z" = "0" ] || { echo "STOP: instrument"; exit 1; }
PAGES=$(git diff --name-only --diff-filter=A main...FETCH_HEAD -- 'incoming/v403bubble/*.md')
for k in 1 2 3; do m=$(gh api repos/chris-j-handel/corus/pulls/$PR/merge -X PUT -f merge_method=merge -f commit_title="Merge #$PR: $(echo "$TITLE" | sed 's/ (v403bubble)//' | cut -c1-110), read for harm and received (v403bubble, received by $MGR)" --jq '.merged' 2>/dev/null); [ "$m" = "true" ] && break; sleep 6; done
echo "merged: $m"; [ "$m" = "true" ] || exit 1
git checkout -q main && git pull -q --depth=100 origin main && git checkout -q -b working/receiving-v403bubble-$ORD-$MGR
python3 -I - "$ORD" "$N" "$MGR" "$DAY" $PAGES <<'EOF' > $RUN/receive_changed.txt
import re, sys, os
ORD, N, MGR, DAY, pages = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:]
changed = set(); said = []
for pg in pages:
    page = open(pg, encoding='utf-8').read(); P = f'`{pg}`'
    title = re.search(r'(?m)^# (.+)$', page).group(1)
    five = page.split('\n## Is-or-is-not?', 1)[1].split('\n## Sources', 1)[0] if '\n## Is-or-is-not?' in page else page.split('\n# FIVE', 1)[1].split('\n# SIX', 1)[0]
    items = re.findall(r'(?m)^\*\*(\d+) · ([^:]+):\*\* (.+)\nis-or-is-not\? (.+)\n((?:(?!Why it is open:).+\n)*)Why it is open: (.+)$', five)
    heads = re.findall(r'(?m)^\*\*(\d+) · ', five); assert [i[0] for i in items] == heads and items, (heads, [i[0] for i in items])
    for n, target, quoted, q, mid, why in items:
        t = re.sub(r"'s gathering file$", '', target.strip()); t = re.sub(r'^Exhibit [A-Z-]+ ', '', t); g = t.replace(' ', '_')
        if not os.path.exists(f'gathering-value/{g}.md'): g = 'Natural_Intelligence'
        d = f"- **Possible exploring** · The session v403bubble's {ORD} returning, {P}, {n}, with its instrument `incoming/v403bubble/instruments/bubble_betweens.py`, executed by a second hand, each check is. With {target}: {quoted.strip()} is-or-is-not? {q.strip()} {' '.join(mid.split()) + ' ' if mid.strip() else ''}Why it is open: {why.strip()}"
        f = f'gathering-value/{g}.md'; L = open(f, encoding='utf-8').read().split('\n')
        if g == 'Natural_Intelligence':
            i = next(k for k, l in enumerate(L) if l.startswith('## Opening'))
            while L[i - 1] == '': i -= 1
        else: i = next(k for k, l in enumerate(L) if l.startswith('- **'))
        L[i:i] = [d]; open(f, 'w', encoding='utf-8').write('\n'.join(L)); changed.add(g)
        sys.stderr.write(f'  {n} · {g} · {q.strip()[:170]}\n')
    sent = re.search(r'(?ms)^## The sentence, re-said\n\n(.+?)\n\n', page)
    sys.stderr.write(f'  the sentence: {(sent.group(1) if sent else "")[:420]}\n')
    p = 'incoming/v403mgr/For_v403bubble.md'; t = open(p, encoding='utf-8').read(); a = "## 10 The set's checks"
    nums = [i[0] for i in items]
    add = f"**Its {ORD} returning, received.** *{title}*, is read for harm and received at main, {DAY}. Its instrument is executed by {MGR}'s own hand: {N} checks, each is. Its is-or-is-nots {nums[0]} to {nums[-1]} are each laid with its gathering file.\n\n" + a
    assert t.count(a) == 1; open(p, 'w', encoding='utf-8').write(t.replace(a, add))
print(' '.join(sorted(changed)))
EOF
[ $? -eq 0 ] || { echo "STOP: bringing"; exit 1; }
bash "$HERE/place_laid.sh"; echo "$(cat $RUN/receive_changed.txt) $(cat $RUN/place_changed.txt 2>/dev/null)" | tr ' ' '\n' | sort -u | grep . | tr '\n' ' ' > $RUN/receive_changed2.txt; mv $RUN/receive_changed2.txt $RUN/receive_changed.txt
CH=$(cat $RUN/receive_changed.txt); git add -A
K=kits/Living_File_Registry_TWENTY-SIX_Improving_Kit; a=$(python3 -I $K/check_set.py . | tail -1); b=$(python3 -I $K/reader_checks.py . origin/main | sed -n '/^3\./,/^4\./p' | grep '" in "' | cut -c1-200)
NOW=""; for g in $CH; do NOW="$NOW $g:$(python3 -I kits/Gathering_Value_Kit/gathering_check.py $g origin/main | tail -1 | tr ' ' '_')"; done
git stash -q; WAS=""; for g in $CH; do WAS="$WAS $g:$(python3 -I kits/Gathering_Value_Kit/gathering_check.py $g origin/main | tail -1 | tr ' ' '_')"; done; git stash pop -q; git add -A
echo "check_set: $a | released: [$b] | gathering now:$NOW | at main:$WAS"
[ "$a" = "ALL PASS" ] && [ -z "$b" ] && [ "$NOW" = "$WAS" ] || { echo "STOP: checks of the set"; exit 1; }
git commit -q -m "v403bubble's $ORD returning received: each is-or-is-not to its gathering file ($MGR)

No living file is changed.

- gathering-value: each is-or-is-not of the page laid with its gathering file, word for word with why it is open: $CH.
- incoming/v403mgr/For_v403bubble.md: the $ORD returning received.

$(printf "%b" "$COMMIT_LINES")"
git -c push.negotiate=true push -q -u origin working/receiving-v403bubble-$ORD-$MGR 2>&1 | grep -v "^remote:" | tail -1
python3 -I - "$ORD" "$N" "$CH" "$NOW" "$MGR" "$(printf "%b" "$PR_LINES")" <<'EOF' > $RUN/pr.json
import json, sys
ORD, N, CH, NOW, MGR, LINES = sys.argv[1:7]
body = (f"## Now\n\nThe session v403bubble's {ORD} returning is read for harm and received at main, and each of its values is brought to its gathering file. No living file is changed.\n\n- Read for harm: files of its own folder alone; its instrument's new lines reach no file and no other thing. Executed by {MGR}'s own hand: {N} checks, each is.\n- Each of its is-or-is-nots is laid with its gathering file, word for word with why it is open.\n\n## Living files away with it\n\nNone.\n\n## Gathering-value files it changes\n\n"
        + ''.join(f"- `gathering-value/{g}.md`\n" for g in CH.split()) + "\n## Suggestions for other sessions\n\n- v403bubble: `incoming/v403mgr/For_v403bubble.md`, part 9.\n\n## Checks\n\ncheck_set ALL PASS; reader_checks, no released word among the added words; gathering_check with each file changed the same as at main with this change away:" + NOW.replace('_', ' ') + ". Each answer waited on.\n\n" + LINES)
json.dump({"title": f"v403bubble's {ORD} returning received: each is-or-is-not to its gathering file ({MGR})", "head": f"working/receiving-v403bubble-{ORD}-{MGR}", "base": "main", "body": body}, sys.stdout)
EOF
gh api repos/chris-j-handel/corus/pulls --method POST --input $RUN/pr.json --jq '.number, .head.sha' > $RUN/pr.out 2>$RUN/pr.err; n=$(head -1 $RUN/pr.out); sha=$(tail -1 $RUN/pr.out)
echo "$n" | grep -q '^[0-9][0-9]*$' || { head -3 $RUN/pr.err; exit 1; }
for i in $(seq 1 30); do r=$(gh api repos/chris-j-handel/corus/commits/$sha/check-runs --jq '[.check_runs[] | .status + ":" + (.conclusion // "-")] | join(" ")'); if [ -n "$r" ] && ! echo "$r" | grep -q "queued\|in_progress"; then break; fi; sleep 10; done
echo "PR $n checks: $r"; echo "$r" | grep -q success || exit 1
for k in 1 2 3; do m=$(gh api repos/chris-j-handel/corus/pulls/$n/merge -X PUT -f merge_method=merge -f commit_title="Merge #$n: v403bubble's $ORD returning received, each is-or-is-not to its gathering file ($MGR)" --jq '.merged' 2>/dev/null); [ "$m" = "true" ] && break; sleep 5; done
echo "merged: $m"; git checkout -q main && git pull -q --depth=100 origin main && git log --oneline -1 | cut -c1-120
