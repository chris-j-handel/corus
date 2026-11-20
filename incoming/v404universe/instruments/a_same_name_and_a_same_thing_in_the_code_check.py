"""A same name and a same thing in Exhibit ONE's code: by which of the two a prior and a now are found together.

Reads Exhibit ONE Natural Resolver at the root given, takes its code as it is in the living file, and executes
it with five small givings; writes no file; decides nothing.

For the window of the opening's open question, lines 9 and 10 with the same thing and lines 11 and 12 with the
same name: how the two co-chain.

Use: python3 -I incoming/v404universe/instruments/a_same_name_and_a_same_thing_in_the_code_check.py <root>

In the code a self's priors and its now are two lists of a name with a direction, the name 4-now-co-same-existing
and the direction 7-now-observing, +1 or -1. Its giving back is a self's next by name and its next priors by name.

Five checks, all or none at all:
  1  one name with a prior and with a now, their directions same: its next is 0
  2  one name with a prior and with a now, their directions not same: its next is the now's direction
  3  a now with a name of no prior is found with no prior: the prior of an other name is not its prior
  4  a name goes on from a self's priors to its next priors, in the four givings with a prior
  5  under one name going on, its direction is as it was with 1, and other-than it was with 2
It closes with its fails.

Returned at main, 19 November 2026: the five as said; fails: 0.
"""
import glob, os, re, sys

R = sys.argv[1]
f = sorted(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')))[0]
code = max(re.findall(r'```(?:python)?\n(.*?)```', open(f, encoding='utf-8').read(), flags=re.S), key=len)
ns = {}
exec(code, ns)
now_existing = ns['_1_now_existing']

fails = 0
def check(n, said, ok):
    global fails
    fails += 0 if ok else 1
    print(f"  {n}  {said}: {'is' if ok else 'IS NOT'}")

nxt, pri = now_existing([('a', 1)], [('a', 1)])
check(1, "one name, a prior and a now of the same direction: its next is 0", dict(nxt)['a'] == 0)
same_prior = dict(pri)['a']
nxt, pri = now_existing([('a', 1)], [('a', -1)])
check(2, "one name, a prior and a now not same: its next is the now's direction", dict(nxt)['a'] == -1)
other_prior = dict(pri)['a']
nxt, pri = now_existing([('a', 1)], [('b', -1)])
check(3, "a now with a name of no prior is found with no prior", dict(nxt)['b'] == -1 and dict(nxt)['a'] == -1)
goes_on = all('a' in dict(now_existing([('a', 1)], g)[1]) for g in ([('a', 1)], [('a', -1)], [('b', -1)], []))
check(4, "a name goes on from a self's priors to its next priors", goes_on)
check(5, "under one name its direction is as it was, or other-than it was", same_prior == 1 and other_prior == -1)
print(f"fails: {fails}")
