body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns)
O=ns['_1_co_bi_offering']; F=ns['_17_tri_co_offering']
print("1. at 14 and 12, empty carrying:")
for offs in [[('s',1)],[('s',1),('s',1)],[('s',1),('s',-1)],[('s',1),('s',1),('s',-1)],[]]:
    print("  offered",[p for _,p in offs],"->",O([],offs))
print("   carrying +, offered +:",O([('s',1)],[('s',1)]),"; offered -:",O([('s',1)],[('s',-1)]),"; none:",O([('s',1)],[]))
def state(soc,ks): return tuple(dict(soc[k][0]).get('s',0) for k in ks)
def period(seq,start):
    # smallest p with seq[t]==seq[t+p] for all t>=start in window
    for p in range(1,len(seq)//3):
        if all(seq[t]==seq[t+p] for t in range(start,len(seq)-p)): return p
def ring(n,steps=None,seed=None):
    steps=steps or 12*n+40
    ks=list(range(n)); comp={(i,9):(i+1)%n for i in ks}
    soc={i:([('s',1)] if i==0 else [],[]) if seed is None else ([('s',seed[i])],[]) for i in ks}
    seq=[]
    for t in range(steps): soc=F(soc,comp); seq.append(state(soc,ks))
    return seq
print("2. rings of n, + once at self 0, others none; round:")
for n in [2,3,4,5,6,7,9,11]:
    seq=ring(n); p=period(seq,n+2); z=sum(1 for x in seq[-1] if x==0)
    print(f"  n={n} round {p} zeros-at-end {z}")
print("3. ring of 1 joined to itself:",ring(1,8))
# receding society: 1024 members, pairs at an empty carrying each loop
m=[1]*1024; hist=[len(m)]
while len(m)>1:
    nxt=[]
    for a,b in zip(m[0::2],m[1::2]):
        t,_=O([],[('s',a),('s',b)]); v=dict(t)['s']
        if v!=0: nxt.append(v)
    m=nxt; hist.append(len(m))
print("4. pairs at an empty carrying, alike, no others joining:",hist)
m=[1,-1]*512; t=[]
for a,b in zip(m[0::2],m[1::2]): t.append(dict(O([],[('s',a),('s',b)])[0])['s'])
print("   alternating members after one loop:",sum(1 for v in t if v!=0))
print("5. odd ring: adjacent like pairs in the carrying at each momentary (after settling):")
for n in [3,5,7,4,6]:
    seq=ring(n,60)
    likes=[sum(1 for i in range(n) if s[i]==s[(i+1)%n] and s[i]!=0) for s in seq[20:28]]
    print("  n",n,likes, seq[20])
# two rings joined across at one self each, both ways (10->14), along 9 in each ring
import itertools,random
def two_rings(a,b,seedA,seedB,steps=80):
    A=[('A',i) for i in range(a)]; B=[('B',i) for i in range(b)]
    comp={}
    for i in range(a): comp[(('A',i),9)]=('A',(i+1)%a)
    for i in range(b): comp[(('B',i),9)]=('B',(i+1)%b)
    comp[(('A',0),10)]=('B',0); comp[(('B',0),10)]=('A',0)
    soc={}
    for i in range(a): soc[('A',i)]=([('s',seedA[i])] if seedA[i] else [],[])
    for i in range(b): soc[('B',i)]=([('s',seedB[i])] if seedB[i] else [],[])
    rel=[]
    for t in range(steps):
        soc=F(soc,comp)
        x=dict(soc[('A',0)][0]).get('s',0); y=dict(soc[('B',0)][0]).get('s',0)
        rel.append('alike' if x==y and x else ('opposite' if x==-y and x else 'none'))
    return rel
random.seed(1); res={}
for a in range(2,7):
  for b in range(2,7):
    outs=set()
    for trial in range(30):
        sa=[random.choice([1,-1]) for _ in range(a)]; sb=[random.choice([1,-1]) for _ in range(b)]
        r=two_rings(a,b,sa,sb); tail=set(r[40:]); outs.add(tuple(sorted(tail)))
    res[(a,b)]=outs
print("6. two rings joined across at one self each; the joined selves' relation after settling:")
for k,v in res.items(): print(" ",k,v)
print("7. pairs at an empty carrying with k joining alike after each pairing, an unpaired member continuing:")
for k in [64,512]:
    m=[1]*1024; hist=[]
    for loop in range(14):
        nxt=[]
        for a,b in zip(m[0::2],m[1::2]):
            v=dict(O([],[('s',a),('s',b)])[0])['s']
            if v: nxt.append(v)
        if len(m)%2: nxt.append(m[-1])
        hist.append(len(nxt)); m=nxt+[1]*k
    print("  k",k,"after each pairing",hist)
