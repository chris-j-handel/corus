"""An odd spiral of five selves, one chained + and the others at none: the 0 released at 10 and the like pair, momentary by momentary. Run from the repository root."""
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']; O=ns['_1_co_bi_offering']
n=5; ks=list(range(n)); comp={(i,9):(i+1)%n for i in ks}
soc={i:([('s',1)] if i==0 else [],[]) for i in ks}
for t in range(26):
    rel={i:dict(O(*soc[i])[0]).get('s',None) for i in ks}
    soc=F(soc,comp)
    car=[dict(soc[i][0]).get('s',0) for i in ks]
    like=[i for i in ks if car[i]==car[(i+1)%n] and car[i]!=0]
    zero=[i for i in ks if rel[i]==0]
    if t>=5: print(t+1,''.join('+' if c>0 else '-' if c<0 else '.' for c in car),"0 released at",zero,"like pair at",like)
