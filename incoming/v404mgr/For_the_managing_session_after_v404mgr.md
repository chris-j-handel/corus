# For the managing session after v404mgr

*The session v404mgr, 18 November, by a partner's word: with a managing session winding down, an other working session familiar with the exchanging goes on with the managing. This page is the managing, whole, with its commands. The method is on [the start page](The_working_now.md), and it is the same for a managing session and a working one.*

## What the managing session is for

- It brings a waiting offer in, into main or into the next version, with the checks.
- It writes [the main list of incoherings](The_main_list_of_incoherings.md) again, and adds a new is-not of both partners to [the list of words](Words_of_no_natural_naming_with_their_natural_naming.md).
- It brings both partners' is'es and is-nots, said at a session, to the start page for a session to come.
- It asks the sessions how the method is working, and gathers a learning in Exhibit TWENTY-FOUR Geodesic Improving Method's gathering file of the next version, at its part 2.6 of a concern.
- A living file enters main, and corus.me goes to a next version, by a partner's word alone.
- A session works with a partner's word. No session is started to go on by itself, and no coming is set for one.

## The two places

- **Main.** The living files as they are live, the pages of a session's own folder under `incoming/`, the start page and the two lists. An offer for main with no living file and no gathering file among its files is brought in with its checks passed.
- **The next version.** The branch `working/natural-intelligence-with-exhibit-one-its-next-version-v403mgr`, its own offer 717 open and never brought in. A session's gathering notes and a re-saying of a living sentence are offered into it: an offer with this branch as its base.

## A coming, in order

1. **The thread**, issue 933, the sayings after the last coming:
   `gh api repos/chris-j-handel/corus/issues/933/comments --paginate --jq '.[] | select(.created_at > "2026-11-18T23:00:00Z") | .body'`
2. **The waiting offers**, the whole open list, with a coming:
   `gh api 'repos/chris-j-handel/corus/pulls?state=open&per_page=60' --jq '.[] | select(.number!=717) | "\(.number) \(.base.ref) \(.head.ref)"'`
3. **An offer for main**, N:
   `python3 -I incoming/v404mgr/instruments/read_for_harm.py . N incoming/v404mgr/The_sessions_v403cohering_and_v404helping_read_whole.md`
   Its checks passed, and no living file and no gathering file among its files:
   `gh api repos/chris-j-handel/corus/pulls/N/merge -X PUT -f merge_method=merge -f commit_title="Merge #N: <its title>"`
   An offer for main with a gathering note in it is brought in after its notes are gone through whole.
4. **An offer for the next version**, N:
   ```
   B=working/natural-intelligence-with-exhibit-one-its-next-version-v403mgr
   git fetch -q --depth=400 origin "$B:refs/remotes/origin/copy" refs/pull/N/head:refs/remotes/pull/N
   git checkout -q -B copy-local refs/remotes/origin/copy
   git merge -q --no-ff origin/main -m "The next version's copy brought current with main"
   git merge -q --no-ff refs/remotes/pull/N -m "Into the next version's copy: offer N"
   K=kits/Living_File_Registry_TWENTY-SIX_Improving_Kit
   python3 -I $K/check_set.py . | tail -1            # ALL PASS
   python3 -I $K/cohere_one.py . | tail -1           # Exhibit ONE is one
   python3 -I kits/Gathering_Value_Kit/gathering_check.py <Gathering_File_Title> | tail -1    # nothing found
   git -c push.negotiate=true push -q origin copy-local:$B
   ```
   Natural Intelligence's gathering file is at 10 found, main's own. With two sessions' lines at one same place, both are whole: both lines, or the newer saying of a line. The offer then shows as brought in.
5. **The main list written again**, from the next version's files:
   ```
   mkdir -p /tmp/next && git archive refs/remotes/origin/copy gathering-value | tar -x -C /tmp/next
   python3 -I incoming/v404mgr/instruments/the_main_list_of_incoherings.py /tmp/next csv > incoming/v404mgr/The_main_list_of_incoherings.csv
   ```
6. **A page of this folder re-said**, the start page among them: a branch `working/<what it is>-<session>` from main; the added words checked, `python3 -I $K/reader_checks.py . origin/main`, its third part, released words; an offer for main; its checks passed; brought in as in 3.
7. **A reply to a partner**, by the start page's parts of a reply and of an offer.

## Notes laid in a gathering file of the next version

- A note: `python3 -I kits/Gathering_Value_Kit/apply_gathered.py "<Living File Title>" FILE.json`, FILE.json `{"items":[{"kind":"droplet","section":"<a part's heading, word for word>","from":"<a few words>","text":"**Possible exploring** · ..."}]}`; with `"kind":"incohering"`, a `"sentence"`, the living sentence word for word, and its `"text"`.
- A note re-said: `python3 -I kits/Gathering_Value_Kit/replace_lines.py CHANGES.json`, CHANGES.json `[{"file":"gathering-value/X.md","old":"<the line, word for word>","new":"..."}]`.
- A note names no session, no page and no date: it is of its living sentence.

## Learned, once for one

- An offer waited five hours with the open list not looked at whole: the whole open list, with a coming.
- A released word in a page brought in: the added words checked before the offer.
- A note re-said by its wording was a note laid twice: a note is found by its distinctive words.
- A session's own span ends: the start page, the thread, the two lists and the gathering files carry the method, and a session opening comes to them.
- An offer's sentence of this session's own words was asked again, eight times in one day: a living sentence is found before a new one is written.

## As it is on 18 November

- Four working sessions: v404chaining, at Natural Intelligence's opening, Exhibit THIRTY and Exhibit TWENTY; v404universe; v404networking, at Exhibit TWO; and v404mgr, managing, at Exhibit ONE Natural Resolver's gathering. Two sessions to open: v404thirdop and v404fourthop.
- Both partners' order of the living files: Exhibit ONE Natural Resolver, then Exhibit THIRTY and Exhibit TWENTY prior to Natural Intelligence, and the improving of an other gathering file after these.
- The open sentence of this session, a gap of the co-chaining, is on the start page's *Now*.
