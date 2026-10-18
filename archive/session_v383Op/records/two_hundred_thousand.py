"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/two_hundred_thousand.py
"""
import sys,random
sys.argv=['x']
src=open('incoming/v383Op/no_common_now.py').read().split("print('Exhibit ONE read at'")[0]
ns={}
exec(src,ns)
r=random.Random(5)
for name,(selves,joins) in [('torus2x3',ns['torus'](2,3)),('crossed',ns['crossed'](3,5)),('spiral5',ns['spiral'](5))]:
    rest=0;n=0
    for t in range(30):
        op={s:r.choice((1,-1)) for s in selves}
        if len(set(op.values()))==1: continue
        n+=1
        how,ch,_=ns['run'](selves,joins,op,r,bound=200000)
        rest+= how=='rest'
    print(name,'non-alike openings',n,'at rest by 200000 changings:',rest)
