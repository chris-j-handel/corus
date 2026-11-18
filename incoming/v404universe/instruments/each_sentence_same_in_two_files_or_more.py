"""Each living sentence that is word for word the same in two living files or more; and each saying of one concept.

Reads each living file at the root; executes; writes no file; decides nothing.

Said in the session: each sentence in our living files can be written as a cohering and co-chaining natural
naming and explaining, and the same sentence would begin appearing all over the files.

Use: python3 -I incoming/v404universe/instruments/each_sentence_same_in_two_files_or_more.py <root>
         the number of living sentences of six words or longer, the number of them word for word the same
         in two living files or more, each set of files having some, and each sentence of three files or more
     python3 -I incoming/v404universe/instruments/each_sentence_same_in_two_files_or_more.py <root> having <words>
         each living sentence having the words, no case: a same sentence once, with each file having it,
         and each other saying after it

What it reads. A living file is a file at the root with a version in its name, *_v*.md. A sentence is a line
divided after a full stop, a question mark or an exclaiming mark; a line of a table, of code or a heading is
passed over; bold and italic marks, a list's mark and a line's closing mark are passed over.

Its own check: each sentence it names the same in two files or more is found again, word for word, in each
of those files' plain words. It closes with its fails.

Returned at main, Merge #975, 18 November 2026:
  33 living files, 36,904 living sentences of six words or longer.
  The same word for word in two living files or more: 666.
  571 of them are of Exhibit ONE Natural Resolver and Natural Intelligence alone, Exhibit ONE written whole in it.
  643 of them are with one of Exhibit ONE, Exhibit THIRTY, Natural Intelligence or Exhibit THREE.
  In three living files or more: eleven, each of them with both Exhibit THIRTY and Natural Intelligence.
  In six living files, one sentence: The universe is the set of all now-existing things.
  having 'it is the same-existing set of all': three sayings in three living files, none the same.
"""
import collections, glob, os, re, sys

R = sys.argv[1]
plain = lambda t: re.sub(r'\*\*|\*', '', t)
squeeze = lambda t: re.sub(r'\s+', ' ', t).strip()


def title(f):
    return re.sub(r'_v\d+\w*\.md$', '', os.path.basename(f)).replace('_', ' ')


def sents(t):
    out = []
    for l in t.split('\n'):
        l = plain(l).strip().rstrip(' \\').strip()
        if not l or l.startswith(('|', '```', '#')):
            continue
        l = re.sub(r'^(?:[-•]|\d+\.)\s+', '', l)
        out += [squeeze(s) for s in re.split(r'(?<=[.?!])\s+(?=[A-Z0-9"“(`+−])', l) if s.strip()]
    return out


files = sorted(glob.glob(os.path.join(R, '*_v*.md')))
text = {title(f): open(f, encoding='utf-8').read() for f in files}
each = {t: sents(x) for t, x in text.items()}

if len(sys.argv) > 2 and sys.argv[2] == 'having':
    words = squeeze(' '.join(sys.argv[3:])).lower()
    at = collections.OrderedDict()
    for t, ss in each.items():
        for s in ss:
            if words in s.lower():
                at.setdefault(s, [])
                if t not in at[s]:
                    at[s].append(t)
    same = [(s, w) for s, w in at.items() if len(w) > 1]
    print(f"having '{words}': {len(at)} sayings in {len({t for w in at.values() for t in w})} living files; "
          f"{len(same)} of them the same in two files or more")
    for s, w in sorted(at.items(), key=lambda x: -len(x[1])):
        print(f"\n  in {len(w)}: {' · '.join(w)}\n    {s}")
    sys.exit(0)

six = {t: [s for s in ss if len(s.split()) >= 6] for t, ss in each.items()}
where = collections.defaultdict(list)
for t, ss in six.items():
    for s in ss:
        if t not in where[s]:
            where[s].append(t)
same = {s: w for s, w in where.items() if len(w) > 1}
print(f"{len(files)} living files, {sum(len(v) for v in six.values()):,} living sentences of six words or longer")
print(f"the same word for word in two living files or more: {len(same):,}")

sets = collections.Counter(' · '.join(sorted(w)) for w in same.values())
print("\neach set of files, with its number of same sentences:")
for k, v in sets.most_common():
    print(f"  {v:>4}  {k}")

core = ('Exhibit ONE Natural Resolver', 'Exhibit THIRTY Co-Chaining Logic Registry', 'Natural Intelligence',
        'Exhibit THREE Natural Numbers')
print(f"\nwith one of Exhibit ONE, Exhibit THIRTY, Natural Intelligence or Exhibit THREE: "
      f"{sum(1 for w in same.values() if set(w) & set(core)):,}")
print(f"Exhibit ONE's and Natural Intelligence's alone: "
      f"{sum(1 for w in same.values() if set(w) == {'Exhibit ONE Natural Resolver', 'Natural Intelligence'}):,}")

print("\neach sentence the same in three living files or more:")
for s, w in sorted(same.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(w) >= 3:
        print(f"  in {len(w)}: {s}\n        {' · '.join(w)}")

three = [w for w in same.values() if len(w) >= 3]
both = [w for w in three if 'Exhibit THIRTY Co-Chaining Logic Registry' in w and 'Natural Intelligence' in w]
print(f"\nin three living files or more: {len(three)}; with both Exhibit THIRTY and Natural Intelligence: {len(both)}")

fails = 0
flat = {t: squeeze(plain(x)) for t, x in text.items()}
for s, w in same.items():
    for t in w:
        if s not in flat[t]:
            fails += 1
print(f"\nits own check, each same sentence found again word for word in each of its files: fails: {fails}")
