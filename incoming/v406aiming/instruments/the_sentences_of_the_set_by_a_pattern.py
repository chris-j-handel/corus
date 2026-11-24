"""The sentences of the set saying a pattern, by file: an instrument of v406aiming's searching. Usage: python3 -I the_sentences_of_the_set_by_a_pattern.py ROOT PATTERN [MOST_A_FILE] [GLOBS...]"""
import re, sys, glob, os
root, pat = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 3
globs = sys.argv[4:] or ['*.md', 'gathering-value/*.md', 'incoming/*/*.md']
rx = re.compile(pat, re.I)
tot = 0
for g in globs:
    for f in sorted(glob.glob(os.path.join(root, g))):
        t = open(f, errors='ignore').read()
        hits = []
        for m in rx.finditer(t):
            s = max(t.rfind('\n', 0, m.start()), t.rfind('. ', 0, m.start())) + 1
            e = min([x for x in (t.find('\n', m.end()), t.find('. ', m.end())) if x != -1] or [len(t)])
            hits.append(' '.join(t[s:e + 1].split())[:300])
        if hits:
            tot += len(hits)
            print(f'== {os.path.relpath(f, root)} ({len(hits)})')
            seen = set()
            for h in hits:
                if h not in seen and len(seen) < mx:
                    seen.add(h); print('   ', h)
print('total', tot)
