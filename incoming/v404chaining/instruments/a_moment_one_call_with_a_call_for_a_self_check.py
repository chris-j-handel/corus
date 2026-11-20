"""Exhibit ONE's code executed: a moment is one call of 17-next-existing, with one call of 1-now-existing for a
self of the society. Executes the code block of the Exhibit ONE file given; writes no file; decides nothing.

Use: python3 -I incoming/v404chaining/instruments/a_moment_one_call_with_a_call_for_a_self_check.py <Exhibit ONE file>
         with Exhibit_ONE_Natural_Resolver_v403mgr.md of the next version, 19 November 2026, three selves for
         four moments: a moment, one 17-next-existing call, three 1-now-existing calls, fails 0
"""
import re, sys

src = open(sys.argv[1], encoding='utf-8').read()
code = re.search(r'```python\n(.*?)```', src, re.S).group(1)
g = {}
exec(code, g)
calls = []
now_existing = g['_1_now_existing']
def counted(a, b):
    calls.append(1)
    return now_existing(a, b)
g['_1_now_existing'] = counted
selves = ['a', 'b', 'c']
state = {s: ([(o, 1 if o < s else -1) for o in selves if o != s], [(o, 1) for o in selves if o != s]) for s in selves}
co = {(s, k): s for s in selves for k in (6, 9, 10)}
fails = 0
for m in range(4):
    before = len(calls)
    state = g['_17_next_existing'](state, co)
    n = len(calls) - before
    fails += n != len(selves)
    print('moment', m + 1, ': one 17-next-existing call,', n, '1-now-existing calls, for', len(selves), 'selves')
print('fails', fails)
