#!/usr/bin/env python3
"""Minimal reproduction of the four 'fail when run' concerns in carry/Exhibit_THIRTY (v380R),
run against the living files at the repo root (v379 / v375), mirroring the verifier's
K26_probe, H24_probe, P7_probe/P28 and RH16_probe."""
import re, sys
from fractions import Fraction
from statistics import mean

REPO = __import__('os').path.abspath(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..', '..'))

print("== (1) K26: 1/x fixed set")
sample = {Fraction(a, b) for a in range(-12, 13) if a for b in range(1, 13)}
fixed = sorted(x for x in sample if 1 / x == x)
print("fixed set of x -> 1/x on nonzero p/q, |p|,q <= 12:", fixed)
print("fixed set of x -> -x on -50..50:", [x for x in range(-50, 51) if -x == x])

print("\n== (2) H24: the mean a member of no population")
for pop in ([0, 1], [1, 1], [1, 2, 3], [1, 2], [5, 5, 5]):
    m = mean(pop)
    print(f"mean{tuple(pop)} = {m}  member? {m in pop}")

print("\n== (3) P7/P28: Physics 2.5's 32 / 9 / 3 at the 5.11 register table (v379)")
NAMINGS = ['an arriving held from behind', 'an opening held as a place', 'a bound held as a last',
           'a carry held as a store', 'a middle held as an end', 'a sign held as a magnitude',
           'a sequencing held to one beat', 'a rate held to a value', 'a two-way held to one side',
           'a membrane held as a cut']
t = open(f'{REPO}/Exhibit_EIGHTEEN_Natural_Physics_v379.md', encoding='utf-8').read()
sec = t.split('## 5.11 Register')[1]
sec = sec.split('\n## ')[0]
rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in sec.split('\n')
        if l.startswith('|') and not l.startswith('|---') and '| arrival |' not in l]
own = [r for r in rows if r[1].startswith("this file's own")]
c = [sum(1 for r in rows if r[1] == n) for n in NAMINGS]
print("rows:", len(rows), " file's own:", len(own), " at the ten namings:", sum(c))
print("per naming:", dict(zip(NAMINGS, c)))
rate = c[7]; ret = c[8] + c[3]   # verifier: ret = c[3] + c[9]? see note
print("a rate held to a value:", c[7])
print("a returned sign entered as cost = carry-as-store + two-way-held? (verifier uses c[3]+c[9]):", c[3] + c[9])
print("verifier P28 groups: ref=c0+c2+c4 =", c[0]+c[2]+c[4], " rate=c6+c7 =", c[6]+c[7],
      " ret=c3+c9 =", c[3]+c[9], " mag=c5+c8 =", c[5]+c[8])
print("2.5 says (32, 9, 3); table gives", (sum(c), c[6]+c[7], c[3]+c[9]))
unknown = [r[1] for r in rows if r[1] not in NAMINGS and not r[1].startswith("this file's own")]
print("rows at no naming:", unknown)

print("\n== (4) RH16: TWENTY-TWO's resolving locator against TWENTY-ONE's entries (v375)")
hp = open(f'{REPO}/Exhibit_TWENTY-ONE_Hard_Problem_Registry_v375.md', encoding='utf-8').read()
body = hp.split('## The collection')[0]
parts = re.split(r'^## (\d+) (.+)$', body, flags=re.M)
entries = [(int(parts[i]), parts[i + 1].strip()) for i in range(1, len(parts), 3)]
print("TWENTY-ONE entries:", len(entries), " first:", entries[0], " last:", entries[-1])
rh = open(f'{REPO}/Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v375.md', encoding='utf-8').read()
loc = rh.split('**Resolving locator**')[1].split('# The given')[0]
L = re.findall(r'^(\d+) (.+?) · [\d.]+(?: and [\d.]+)?, ', loc, re.M)
name2num = {name: n for n, name in entries}
off = [int(n) - name2num[name] for n, name in L if name in name2num]
unmatched = [(n, name) for n, name in L if name not in name2num]
nums = [int(n) for n, _ in L]
print("locator lines:", len(L), " numbers run", nums[0], "to", nums[-1])
print("offset locator-number minus TWENTY-ONE number, histogram:",
      {k: off.count(k) for k in sorted(set(off))})
print("matched by name:", len(off), " unmatched names:", unmatched)
print("sample:", [(n, name, name2num.get(name)) for n, name in L[:3]], "...", [(n, name, name2num.get(name)) for n, name in L[-2:]])
print("TWENTY-ONE entries past the locator's last matched:",
      [(n, nm) for n, nm in entries if n >= 176])
