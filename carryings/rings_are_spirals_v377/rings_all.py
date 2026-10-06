import itertools
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']
def two_rings(a,b,sa,sb,steps=70):
    comp={}
    for i in range(a): comp[(('A',i),9)]=('A',(i+1)%a)
    for i in range(b): comp[(('B',i),9)]=('B',(i+1)%b)
    comp[(('A',0),10)]=('B',0); comp[(('B',0),10)]=('A',0)
    soc={('A',i):([('s',sa[i])],[]) for i in range(a)}
    soc.update({('B',i):([('s',sb[i])],[]) for i in range(b)})
    rel=[]
    for t in range(steps):
        soc=F(soc,comp); x=dict(soc[('A',0)][0])['s']; y=dict(soc[('B',0)][0])['s']
        rel.append('alike' if x==y else 'opposite')
    return set(rel[40:])
out={}
for a in range(2,7):
  for b in range(a,7):
    c={'alike':0,'opposite':0,'mixed':0}
    for sa in itertools.product([1,-1],repeat=a):
      for sb in itertools.product([1,-1],repeat=b):
        r=two_rings(a,b,sa,sb); c[r.pop() if len(r)==1 else 'mixed']+=1
    out[(a,b)]=c; print((a,b),c,flush=True)
