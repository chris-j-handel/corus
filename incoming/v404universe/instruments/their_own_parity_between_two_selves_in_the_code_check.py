"""Two selves and one name between them, in Exhibit ONE's code executed.

Reads Exhibit ONE Natural Resolver at the root given, takes its code as it is in the living file, and executes it
for two selves with one name, a self's 6 going to its other; writes no file; decides nothing.

For the window's lines of 19 November: "For two different things, their own-parity is the thing between them." and
"Each of both possesses this parity."; and for Exhibit THIRTY's step 180, of a parity between two, a self and an
other, same or one inversioning between them.

Use: python3 -I incoming/v404universe/instruments/their_own_parity_between_two_selves_in_the_code_check.py <root>

Four openings, a self and its other with one name and a direction of it, + or -, and 24 moments of 17-next-existing.
Between the two, under the one name, is one of two: same, or one inversion.

Five checks, all or none at all:
  1  in all moments a self and its other both have the name, with a direction, in their own priors
  2  a self's 6 of a moment is its other's now of that moment's next, and no thing more is its other's now
  3  same or one inversion, between the two, is as it opened in all moments
  4  a 0 goes between the two from both together or from none; with one inversion between them, in no moment
  5  no direction of a self goes on as it was through two moments
It closes with its fails.

Returned at main and in the next version, 19 November 2026: the five as said; four openings, 96 moments, a 0
from both together in 24 of them; fails: 0.
"""
import glob, os, re, sys

R = sys.argv[1]
f = sorted(glob.glob(os.path.join(R, 'Exhibit_ONE_Natural_Resolver_v*.md')))[0]
text = open(f, encoding='utf-8').read()
code = max(re.findall(r'```(?:python)?\n(.*?)```', text, flags=re.S), key=len)
ns = {}
exec(code, ns)
moment = ns['_17_next_existing']
entry = ns['_1_now_existing']

fails = 0
def check(n, said, ok):
    global fails
    fails += 0 if ok else 1
    print(f"  {n}  {said}: {'is' if ok else 'IS NOT'}")

routes = {('a self', 6): 'its other', ('its other', 6): 'a self'}
both_have = sixes = as_opened = zeros_together = no_three = True
moments = zero_moments = 0
for a0, b0 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
    state = {'a self': ([('k', a0)], []), 'its other': ([('k', b0)], [])}
    opened_same = a0 == b0
    runs = {'a self': [a0], 'its other': [b0]}
    for t in range(24):
        shared = {s: entry(*state[s])[0] for s in state}          # a self's 6 of this moment
        state = moment(state, routes)
        moments += 1
        a = dict(state['a self'][0]).get('k'); b = dict(state['its other'][0]).get('k')
        both_have &= a in (1, -1) and b in (1, -1)
        sixes &= state['its other'][1] == shared['a self'] and state['a self'][1] == shared['its other']
        as_opened &= (a == b) == opened_same
        za = dict(shared['a self'])['k'] == 0; zb = dict(shared['its other'])['k'] == 0
        zeros_together &= za == zb and not (za and not opened_same)
        zero_moments += 1 if za and zb else 0
        runs['a self'].append(a); runs['its other'].append(b)
    for r in runs.values():
        no_three &= all(not (r[i] == r[i + 1] == r[i + 2]) for i in range(len(r) - 2))
    print(f"     opening {'same' if opened_same else 'one inversion'}, {a0:+d} and {b0:+d}: "
          f"a self {' '.join(f'{x:+d}' for x in runs['a self'][:9])} ...")
print(f"     moments: {moments}; a 0 from both together: {zero_moments}")
check(1, "in all moments both have the name, with a direction, in their own priors", both_have)
check(2, "a self's 6 of a moment is its other's now of the next, and no thing more", sixes)
check(3, "same or one inversion, between the two, is as it opened in all moments", as_opened)
check(4, "a 0 goes between the two from both together or from none; with one inversion, in no moment",
      zeros_together and zero_moments > 0)
check(5, "no direction of a self goes on as it was through two moments", no_three)
print(f"fails: {fails}")
