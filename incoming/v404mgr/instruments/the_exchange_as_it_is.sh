#!/bin/bash
# The exchange as it is now, for a session observing it: sayings at the thread
# and offers, from a moment given to now. It sizes, and it decides nothing.
#
#   bash incoming/v404mgr/instruments/the_exchange_as_it_is.sh [FROM]
#
# FROM is a moment by the world's clock, as 2026-11-19T00:00:00Z. With none
# given, it is the moment of this instrument's executing before, kept in
# $EXCHANGE_STATE (/tmp/exchange_last with none named).
#
# It says: the sayings at the thread from that moment, by their opening line;
# for a session, the minutes from its latest saying to now; the offers open and
# the minutes they wait; and the offers closed from that moment.
R=chris-j-handel/corus
STATE="${EXCHANGE_STATE:-/tmp/exchange_last}"
FROM="${1:-$(cat "$STATE" 2>/dev/null)}"
FROM="${FROM:-$(date -u -d '1 hour ago' +%FT%TZ)}"
NOW=$(date -u +%FT%TZ)
echo "== now $NOW · from $FROM"
echo "-- sayings at the thread, by their opening line"
gh api repos/$R/issues/933/comments --paginate --jq ".[] | select(.created_at > \"$FROM\") | \"\(.created_at[11:16]) \(.body | split(\"\n\")[0][0:230])\""
echo "-- a session's latest saying at the thread, minutes to now"
gh api repos/$R/issues/933/comments --paginate --jq '.[] | "\(.created_at) \(.body | capture("From (?<s>v40[0-9a-z]+)").s // "?")"' 2>/dev/null |
  awk -v now="$(date -u +%s)" '{cmd="date -u -d " $1 " +%s"; cmd | getline t; close(cmd); last[$2]=t} END{for(s in last) printf "   %s %d\n", s, (now-last[s])/60}' | sort
echo "-- offers open, minutes waiting"
gh api "repos/$R/pulls?state=open&per_page=100" --jq '.[] | select(.number != 717) | "\(.number) \(.created_at) \(.base.ref[0:12]) | \(.title[0:110])"' |
  while read -r n t rest; do echo "   #$n $(( ($(date -u +%s) - $(date -u -d "$t" +%s)) / 60 ))m $rest"; done
echo "-- offers closed, with the minutes from opening to closing"
gh api "repos/$R/pulls?state=closed&per_page=40&sort=updated&direction=desc" --jq ".[] | select(.closed_at > \"$FROM\") | \"\(.number) \(.created_at) \(.closed_at) \(.merged_at != null) | \(.title[0:90])\"" |
  while read -r n c z m rest; do echo "   #$n in=$m $(( ($(date -u -d "$z" +%s) - $(date -u -d "$c" +%s)) / 60 ))m $rest"; done
echo "$NOW" > "$STATE"
