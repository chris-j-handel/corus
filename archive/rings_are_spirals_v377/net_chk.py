import itertools
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']
def st(soc,keys): return tuple(dict(soc[k][0]).get('s',0) for k in keys)
def ring(n,s0,steps=200):
    comp={((i),9):(i+1)%n for i in range(n)}
    soc={i:([('s',s0[i])],[]) for i in range(n)}
    keys=list(range(n)); hist=[st(soc,keys)]
    for t in range(steps):
        soc=F(soc,comp); hist.append(st(soc,keys))
    return hist
def period(h,start=20):
    for p in range(1,len(h)//3):
        if all(h[i]==h[i+p] for i in range(start,len(h)-p)): return p
for n in []:
    ps=set()
    for s0 in itertools.product([1,-1],repeat=n):
        h=ring(n,s0,160); ps.add(period(h))
    print('ring',n,'periods',sorted(ps,key=str), 'first', ring(n,(1,)*n,6)[:6] if n<6 else '')
# two separate prime rings together
def two(p,q,steps):
    comp={}
    for i in range(p): comp[(('A',i),9)]=('A',(i+1)%p)
    for i in range(q): comp[(('B',i),9)]=('B',(i+1)%q)
    soc={('A',i):([('s',1)],[]) for i in range(p)}; soc.update({('B',i):([('s',1 if i else -1)],[]) for i in range(q)})
    keys=sorted(soc); h=[st(soc,keys)]
    for t in range(steps): soc=F(soc,comp); h.append(st(soc,keys))
    return h
for p,q in [(3,5),(3,7),(5,7)]:
    print('two',p,q,period(two(p,q,4*p*q*3+40),20),4*p*q)
print('---')
def two2(p,q,steps):
    comp={}
    for i in range(p): comp[(('A',i),9)]=('A',(i+1)%p)
    for i in range(q): comp[(('B',i),9)]=('B',(i+1)%q)
    soc={('A',i):([('s',1 if i else -1)],[]) for i in range(p)}; soc.update({('B',i):([('s',1 if i else -1)],[]) for i in range(q)})
    keys=sorted(soc); h=[st(soc,keys)]
    for t in range(steps): soc=F(soc,comp); h.append(st(soc,keys))
    return h
for p,q in [(3,5),(3,7),(5,7)]:
    print('two',p,q,period(two2(p,q,4*p*q*3+40),20),4*p*q)
h=ring(5,(-1,1,1,1,1),45)
for t,x in enumerate(h[:42]): print(t,x)
