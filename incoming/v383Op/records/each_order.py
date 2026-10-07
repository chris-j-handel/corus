"""A record of v383Op's exploring, gathered at the session's close.

An instrument at its own arrangement: its storage and its ordering are the
instrument's, and its numbers are of that arrangement. It is at no sentence of
the method. Records.md says what it enters and what returned.

From the repository root:  python3 incoming/v383Op/records/each_order.py
"""
import itertools, sys, collections
# model the cell: arriving alone p; carrying c. match if p==c: no share. else c=p, share p.
def explore(selves, joins, cap):
    idx={s:i for i,s in enumerate(selves)}
    chans=[(s,to) for s in selves for to in joins[s]]
    cidx={ch:i for i,ch in enumerate(chans)}
    res={}
    for opening in itertools.product((1,-1),repeat=len(selves)):
        c=[-o for o in opening]  # after first momentary
        q=[() for _ in chans]
        q=list(q)
        for s in selves:
            for to in joins[s]:
                q[cidx[(s,to)]]=q[cidx[(s,to)]]+(c[idx[s]],)
        start=(tuple(c),tuple(q))
        seen={start}; stack=[start]; rest=False; capped=False
        while stack:
            c,q=stack.pop()
            if all(len(x)==0 for x in q):
                rest=True; break
            for k,ch in enumerate(chans):
                if q[k]:
                    p=q[k][0]; to=ch[1]
                    nq=list(q); nq[k]=q[k][1:]
                    nc=list(c)
                    if p!=c[idx[to]]:
                        nc[idx[to]]=p
                        for on in joins[to]:
                            j=cidx[(to,on)]; nq[j]=nq[j]+(p,)
                    if sum(len(x) for x in nq)>cap: capped=True; continue
                    st=(tuple(nc),tuple(nq))
                    if st not in seen: seen.add(st); stack.append(st)
        res[opening]=(rest,len(seen),capped)
    return res
def spiral(n): return list(range(n)),{j:[(j+1)%n] for j in range(n)}
def torus(p,q):
    selves=[(i,j) for i in range(p) for j in range(q)]
    return selves,{(i,j):[((i+1)%p,j),(i,(j+1)%q)] for i,j in selves}
def crossed(p,q):
    selves=[('P',i) for i in range(p)]+[('Q',i) for i in range(q)]
    joins={('P',i):[('P',(i+1)%p)] for i in range(p)}
    joins.update({('Q',i):[('Q',(i+1)%q)] for i in range(q)})
    joins[('P',0)].append(('Q',0)); joins[('Q',0)].append(('P',0))
    return selves,joins
for name,(s,j),cap in [('ring2',spiral(2),10),('ring3',spiral(3),10),('ring4',spiral(4),10),('ring5',spiral(5),10),('ring6',spiral(6),10),('torus2x2',torus(2,2),14)]:
    r=explore(s,j,cap)
    bad=[(o,v) for o,v in r.items() if v[0] and len(set(o))>1]
    nonrest_alike=[o for o,v in r.items() if not v[0] and len(set(o))==1]
    print(name,'openings',len(r),'non-alike that can reach rest:',len(bad),'alike that cannot reach rest',len(nonrest_alike),'capped any',any(v[2] for v in r.values()))
    if bad: print('  e.g.',bad[:3])
