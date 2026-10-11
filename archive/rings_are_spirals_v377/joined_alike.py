"""Two spirals joined across at one self each, every pattern at two to five selves: the joined selves' relation, and whether they change at each momentary. Run from the repository root."""
import itertools
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']
def run(a,b,sa,sb,steps=60):
    comp={}
    for i in range(a): comp[(('A',i),9)]=('A',(i+1)%a)
    for i in range(b): comp[(('B',i),9)]=('B',(i+1)%b)
    comp[(('A',0),10)]=('B',0); comp[(('B',0),10)]=('A',0)
    soc={('A',i):([('s',sa[i])],[]) for i in range(a)}; soc.update({('B',i):([('s',sb[i])],[]) for i in range(b)})
    xs=[]
    for t in range(steps):
        soc=F(soc,comp); xs.append((dict(soc[('A',0)][0])['s'],dict(soc[('B',0)][0])['s']))
    tail=xs[30:]
    rel='alike' if tail[0][0]==tail[0][1] else 'opposite'
    ch=[(tail[i][0]!=tail[i+1][0], tail[i][1]!=tail[i+1][1]) for i in range(len(tail)-1)]
    return rel, all(c==(True,True) for c in ch), all(c[0]==c[1] for c in ch)
out={}
for a in range(2,6):
  for b in range(a,6):
    for sa in itertools.product([1,-1],repeat=a):
      for sb in itertools.product([1,-1],repeat=b):
        r=run(a,b,sa,sb); out[r]=out.get(r,0)+1
for (rel,each,together),c in sorted(out.items()): print(f"{rel}: {c} patterns, changing together {together}, at each momentary {each}")
