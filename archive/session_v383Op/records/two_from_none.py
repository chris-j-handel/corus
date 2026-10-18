"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/two_from_none.py
"""
import glob, re
exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_1 = ns['_1_co_bi_tri_offering']
def entry(c, offered):
    shared, chained = _1([('k', c)], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]
# two selves, A first, both -1 carrying
for opA,opB in [(-1,-1),(1,1),(1,-1),(-1,1)]:
    cA,cB=opA,opB
    lastA=lastB=None
    sa=[];sb=[]
    # A enters first with nothing; B enters offered A's release; A offered B's release...
    for k in range(8):
        offA=[] if lastB is None else [lastB]
        cA,lastA=entry(cA,offA); sa.append(lastA)
        offB=[lastA]
        cB,lastB=entry(cB,offB); sb.append(lastB)
    print(opA,opB,'A shares',sa,'B shares',sb)
print('--- each of the two opened carrying none, each first offered -, then one and then the other')
def entry0(offered):
    shared, chained = _1([], [('k', p) for p in offered])
    return dict(chained)['k'], shared[0][1]
cA, sA = entry0([-1]); cB, sB = entry0([-1])
print('after the first offering', cA, sA, cB, sB)
a = [sA]; b = [sB]
lastA, lastB = sA, sB
for k in range(8):
    cA, lastA = entry(cA, [lastB]); a.append(lastA)
    cB, lastB = entry(cB, [lastA]); b.append(lastB)
print('A shares', a); print('B shares', b)
