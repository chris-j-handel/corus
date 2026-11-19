"""Now and me, together and separately, in Exhibit ONE's seventeen names and in its code executed.

Reads Exhibit ONE Natural Resolver at the root given, takes its table of seventeen names and its code as they are
in the living file, and executes the code with small givings; writes no file; decides nothing.

For a partner's two sayings of 19 November, with v404universe: "a parity does not exist other than now." and
"now-and-same-existing does not exist other than now."; and the asking after them, of now and me living together
and separately inside the resolver.

Use: python3 -I incoming/v404universe/instruments/now_and_me_together_and_separately_in_the_code_check.py <root>

By Exhibit ONE, co is me-parity. In its code a self's entry, 1-now-existing, is given two lists of a name with a
direction: a self's prior parities, 3-now-co-observing, co; and the parities arriving now, 2-now-possibling, one.
It gives back a self's next by name, 10-next-co-possibling, and its next priors by name, 11-next-co-observing.

Seven checks, all or none at all:
  1  the seventeen names: now with co, 3 4 5 6; now with one, 1 2 7 8; next with co, 9 10 11 12; next with one,
     13 14 15 16 17; and prior is a word of no name
  2  the entry is given two lists, and both are of now names: 3-now-co-observing and 2-now-possibling
  3  separately, a prior of no now: its next is the prior inverting, and no 0
  4  separately, a now of no prior: its next is the now's direction, and its name goes on as a next prior
  5  together, agreeing: its next is 0, and its prior goes on as it was
  6  together, parting: its next is the now's direction, and its next prior is the now's
  7  in all givings of two names, a 0 is written for a name of a now, and for no name of a prior alone
It closes with its fails.

Returned at main and in the next version, 19 November 2026: the seven as said; 225 givings, 104 with a 0, a 0
for no name of a prior alone; fails: 0.
"""
import glob, inspect, itertools, os, re, sys

R = sys.argv[1]
f = sorted(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')))[0]
text = open(f, encoding='utf-8').read()
code = max(re.findall(r'```(?:python)?\n(.*?)```', text, flags=re.S), key=len)
ns = {}
exec(code, ns)
entry = ns['_1_now_existing']

fails = 0
def check(n, said, ok):
    global fails
    fails += 0 if ok else 1
    print(f"  {n}  {said}: {'is' if ok else 'IS NOT'}")

# 1: the table of seventeen names, as it is in the living file
rows = re.findall(r'^\| (\d+) \| \*\*([0-9a-z-]+)\*\* \| [^|]+ \| [^|]+ \| (co|one) \|', text, flags=re.M)
groups = {}
for n, name, co in rows:
    groups.setdefault(('now' if '-now-' in name else 'next', co), []).append(int(n))
said = {('now', 'co'): [3, 4, 5, 6], ('now', 'one'): [1, 2, 7, 8],
        ('next', 'co'): [9, 10, 11, 12], ('next', 'one'): [13, 14, 15, 16, 17]}
no_prior = all('prior' not in name for _, name, _ in rows)
for k in said:
    print(f"     {k[0]} with {k[1]}: {' '.join(map(str, groups.get(k, [])))}")
check(1, "the seventeen names by now or next and by co or one, and prior a word of no name",
      len(rows) == 17 and groups == said and no_prior)

# 2: the entry's two givings
givings = list(inspect.signature(entry).parameters)
print(f"     the entry's givings: {', '.join(g.strip('_').replace('_', '-') for g in givings)}")
check(2, "the entry is given two lists, both of now names",
      givings == ['_3_now_co_observing', '_2_now_possibling'])

# 3 to 6: separately and together
nxt, pri = entry([('a', 1)], [])
check(3, "separately, a prior of no now: its next is the prior inverting, and no 0",
      dict(nxt)['a'] == -1 and dict(pri)['a'] == -1)
nxt, pri = entry([], [('b', 1)])
check(4, "separately, a now of no prior: its next is the now's direction, and it is a next prior",
      dict(nxt)['b'] == 1 and dict(pri)['b'] == 1)
nxt, pri = entry([('a', 1)], [('a', 1)])
check(5, "together, agreeing: its next is 0, and its prior goes on as it was",
      dict(nxt)['a'] == 0 and dict(pri)['a'] == 1)
nxt, pri = entry([('a', 1)], [('a', -1)])
check(6, "together, parting: its next is the now's direction, and its next prior is the now's",
      dict(nxt)['a'] == -1 and dict(pri)['a'] == -1)

# 7: all givings of two names, a prior of +, - or none, and nows of none, +, -, + and -, or + and +
priors = [None, 1, -1]
nows = [[], [1], [-1], [1, -1], [1, 1]]
count = with_0 = prior_alone_0 = 0
for pa, na, pb, nb in itertools.product(priors, nows, priors, nows):
    count += 1
    p = [(k, v) for k, v in (('a', pa), ('b', pb)) if v is not None]
    n = [('a', d) for d in na] + [('b', d) for d in nb]
    nxt = dict(entry(p, n)[0])
    zeros = [k for k, v in nxt.items() if v == 0]
    with_0 += 1 if zeros else 0
    has_now = {'a': bool(na), 'b': bool(nb)}
    prior_alone_0 += sum(1 for k in zeros if not has_now[k])
print(f"     givings: {count}; with a 0: {with_0}; a 0 for a name of a prior alone: {prior_alone_0}")
check(7, "in all givings a 0 is written for a name of a now, and for no name of a prior alone",
      count == 225 and with_0 > 0 and prior_alone_0 == 0)
print(f"fails: {fails}")
