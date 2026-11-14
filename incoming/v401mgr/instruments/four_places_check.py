"""four_places_check.py · one bi-coupling of one self, each case, by Exhibit ONE's code as it is.

Use: python3 -I four_places_check.py <repository root>

A partner's sentence, 14 November 2026, said in natural naming: three 1s by each parity; the fourth a 1 or a 0;
the 0 in one of three places, and in the same-existing fourth place in no case.

Read here, by the code's lines, each case: a self's prior, + or − or none; and none to three parities arriving
by one 4 from its others. Four places of that one 4: its prior, 3-now-co-observing; its possibling,
14-next-possibling, none read as a 0 as the code's own line reads it; its co-possibling, 10-next-co-possibling;
and its same-existing, 8-now-same-existing, its next prior. A place is a 1 by a parity, + or −, and a 0 by a 0
or by nothing. It decides nothing. Its returned lines are in four_places_check_returned.txt.
"""
import glob, importlib.util, itertools, os, re, sys, tempfile

ROOT = sys.argv[1]
text = open(glob.glob(os.path.join(ROOT, 'Exhibit_ONE_Natural_Resolver_v*.md'))[0], encoding='utf-8').read()
code = re.search(r'```python\n(.*?)\n```', text, re.S).group(1)
with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as f:
    f.write(code)
spec = importlib.util.spec_from_file_location('e1', f.name)
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)

K = ('other', 0)


def possibling(arriving):
    v = None
    for p in arriving:
        if v is None:
            v = p
        elif (v > 0) != (p > 0):
            v = 0
    return 0 if v is None else v


rows = {}
for prior in (None, 1, -1):
    for n in range(0, 4):
        for arriving in itertools.product((1, -1), repeat=n):
            three = [(K, prior)] if prior else []
            ten, eight = e._1_now_existing(three, [(K, p) for p in arriving])
            ten, eight = dict(ten), dict(eight)
            places = (
                1 if prior else 0,
                1 if possibling(arriving) else 0,
                1 if ten.get(K, 0) else 0,
                1 if eight.get(K, 0) else 0,
            )
            rows.setdefault(('a prior' if prior else 'no prior', places), 0)
            rows[('a prior' if prior else 'no prior', places)] += 1

print('cases: a prior of + or of − or none, and none to three parities arriving by one 4:', sum(rows.values()))
print('four places: prior · possibling · co-possibling · same-existing; a 1 by a parity, a 0 by a 0 or by nothing')
for (kind, places), n in sorted(rows.items(), key=lambda x: (x[0][0], [-y for y in x[0][1]])):
    print(f"   {kind} · {' '.join(str(p) for p in places)} · {n} cases")
with_prior = [p for (k, p) in rows if k == 'a prior']
print('a self having a prior, each case: three 1s or four:', all(sum(p) >= 3 for p in with_prior))
print('a self having a prior, each case: same-existing a 1:', all(p[3] == 1 for p in with_prior))
print('a self having a prior, each case: its prior a 1:', all(p[0] == 1 for p in with_prior))
print('a self having a prior: a 0 by possibling in some case:', any(p[1] == 0 for p in with_prior),
      '· by co-possibling in some case:', any(p[2] == 0 for p in with_prior),
      '· by both in one case:', any(p[1] == 0 and p[2] == 0 for p in with_prior))
no_prior = [p for (k, p) in rows if k == 'no prior']
print('no prior: three 1s, its 0 by its prior, in some case:', any(p == (0, 1, 1, 1) for p in no_prior),
      '· same-existing a 0 in some case:', any(p[3] == 0 for p in no_prior))
