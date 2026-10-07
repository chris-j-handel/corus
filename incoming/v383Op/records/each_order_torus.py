"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/each_order_torus.py
"""
import itertools, sys, time
def explore(selves, joins, cap, tmax=100):
    n=len(selves); idx={s:i for i,s in enumerate(selves)}
    chans=[(idx[s],idx[to]) for s in selves for to in joins[s]]
    out=[[k for k,(a,b) in enumerate(chans) if a==i] for i in range(n)]
    t0=time.time()
    bad=[]; capped=False; total=0
    for opening in itertools.product((1,-1),repeat=n):
        if len(set(opening))==1: continue
        c=tuple(-o for o in opening); L=tuple(1 for _ in chans)
        seen={(c,L)}; stack=[(c,L)]; found=False
        while stack:
            c,L=stack.pop()
            if not any(L): found=True; break
            for k,(a,b) in enumerate(chans):
                if L[k]:
                    head=c[a]*(1 if (L[k]-1)%2==0 else -1)
                    nL=list(L); nL[k]-=1; nc=list(c)
                    if head!=c[b]:
                        nc[b]=head
                        for j in out[b]: nL[j]+=1
                    if max(nL)>cap: capped=True; continue
                    st=(tuple(nc),tuple(nL))
                    if st not in seen: seen.add(st); stack.append(st)
        total+=len(seen)
        if found: bad.append(opening)
        if time.time()-t0>tmax: print('timeout'); break
    return bad,capped,total
def torus(p,q):
    selves=[(i,j) for i in range(p) for j in range(q)]
    return selves,{(i,j):[((i+1)%p,j),(i,(j+1)%q)] for i,j in selves}
def crossed(p,q):
    selves=[('P',i) for i in range(p)]+[('Q',i) for i in range(q)]
    joins={('P',i):[('P',(i+1)%p)] for i in range(p)}
    joins.update({('Q',i):[('Q',(i+1)%q)] for i in range(q)})
    joins[('P',0)].append(('Q',0)); joins[('Q',0)].append(('P',0))
    return selves,joins
for name,(s,j),cap in [("torus2x2",torus(2,2),2),("torus2x2",torus(2,2),3)]:
    b,c,t=explore(s,j,cap)
    print(name,'cap',cap,'non-alike openings reaching rest:',len(b),'capped',c,'states',t,flush=True)
