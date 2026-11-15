"""v403mgr: each open sentence of Natural Intelligence's living opening, gathered with why it is open, into
Natural Intelligence's gathering file, its opening's part, in the opening's own order. From v402mgr's page of the
seventy sentences by the three. All or none: with the page not as it was read, nothing is written.

Use: python3 -I incoming/v403mgr/instruments/gather_the_opening_by_three.py <root> [--dry]

Applied at main after Merge #714, 15 November 2026: 51 droplets entered, each a living sentence with why it is open.
Of the page's fifty-two, one is an is of both partners after it, By observing, the universe is a same-existing set,
and is entered as none; three have why they are open re-said by an is after the page.
The page it read is dissolved with it, and is in the set's history: this instrument is its record.
"""
import re, sys
R = sys.argv[1]; DRY = '--dry' in sys.argv
rated = open(R + '/incoming/v402mgr/Natural_Intelligence_rated_by_three.md', encoding='utf-8').read()
rows = re.findall(r'^\| (\d+) \| (.*?) \| (is|is-or-is-not\?|is-not) \| (.*?) \|$', rated, re.M)
assert len(rows) == 70 and sum(1 for r in rows if r[2] == 'is-or-is-not?') == 52
plain = lambda s: re.sub(r'\*\*', '', s)
newer = {   # why it is open, re-said by an is after the page
    9: "one universe, or each one's own; the sentence it is after, of the universe as a same-existing set by observing, is an is",
    22: "the universe is a same-existing set by observing, an is; the universe as non-living is not yet read by it",
    3: "one universe, or each one's own, as the sentence it is after",
}
out = []
for n, s, r, why in rows:
    n = int(n)
    if r != 'is-or-is-not?' or n == 8: continue
    w = newer.get(n, why)
    if w in ('as the sentence before it', 'by the sentence before it'): w = 'as the sentence it is after, in this part'
    w = w.replace('as the sentence before it', 'as the sentence it is after')
    out.append(f'- **Possible exploring** · is-or-is-not? {plain(s)} Why it is open: {w}. — at "{plain(s)}"')
assert len(out) == 51
p = R + '/gathering-value/Natural_Intelligence.md'
L = open(p, encoding='utf-8').read().split('\n')
assert not any(l.startswith('- **Possible exploring** · is-or-is-not? One universe is now-existing. Why it is open:') for l in L), 'entered already'
z = [i for i, l in enumerate(L) if l == '## ONE · NATURAL']; assert len(z) == 1
k = z[0] - 1
while not L[k].startswith('- '): k -= 1
L[k + 1:k + 1] = out
if not DRY: open(p, 'w', encoding='utf-8').write('\n'.join(L))
print(len(out), 'droplets', 'entered' if not DRY else 'to enter, --dry')
for o in out[:3]: print('  ', o[:200])
