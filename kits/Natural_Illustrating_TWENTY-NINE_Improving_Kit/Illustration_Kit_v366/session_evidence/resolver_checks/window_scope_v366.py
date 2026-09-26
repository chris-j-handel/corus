"""v366: exact scope check for the inherited ring conservation identity.
Runs against the inherited reduced step; it does not change the resolver.
"""
from ring_window_v366 import ST, step, density, joint, NAME
from itertools import product
pairs = {((1,1),(1,1)), ((-1,-1),(-1,-1)),
         ((1,1),(-1,-1)), ((-1,-1),(1,1)),
         ((1,1),(0,-1)), ((-1,-1),(0,1)),
         ((0,1),(1,1)), ((0,-1),(-1,-1)),
         ((0,1),(0,1)), ((0,-1),(0,-1))}
windows=[(a,b,c) for a,b,c in product(ST,repeat=3) if (a,b) in pairs and (b,c) in pairs]
assert len(windows)==26
assert all(((s,s),(t,t)) in pairs for s,t in product((1,-1),repeat=2))
assert all((step(a,b),step(b,c)) in pairs for a,b,c in windows)
assert all(density(step(a,b),step(b,c))-density(b,c)==joint(a,b)-joint(b,c) for a,b,c in windows)
print('26 windows: initial inclusion, closure and local conservation all hold.')
D=lambda x:sum(density(x[i],x[(i+1)%len(x)]) for i in range(len(x)))
x=[(1,1)]*3
y=x.copy(); y[0]=step(x[-1],x[0])
assert all((x[i],x[(i+1)%3]) in pairs for i in range(3))
assert D(x)==3 and D(y)==2
print('Single-node update:', [NAME[a] for a in x], '->', [NAME[a] for a in y], 'D:',D(x),'->',D(y))
parallel=[step(x[i-1],x[i]) for i in range(3)]
assert D(parallel)==3
print('Parallel update:', [NAME[a] for a in parallel], 'D:',D(parallel))
print('The inherited D is conserved by the specified parallel ring update; arbitrary one-node updates do not preserve it.')
