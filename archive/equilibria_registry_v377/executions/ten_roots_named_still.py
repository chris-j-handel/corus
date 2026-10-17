"""Each of Exhibit ONE's ten roots with its -ing taken out: the term named still from one momentary on, and whether the resolving stops. Run from the repository root."""
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read(); ns={}
exec(body.split('```python',1)[1].split('```',1)[0],ns)
O=ns['_1_co_bi_offering']; M=ns['_9_tri_bi_co_momentarying']; F=ns['_17_tri_co_offering']

# The code's own society step, written out with one hook per name, so each term can be named still from momentary K on.
def step(soc, comp, frozen, memo, t, K):
    def hold(name, key, val):
        if name in frozen and t>=K:
            if (name,key) not in memo: memo[(name,key)]=val
            return memo[(name,key)]
        return val
    wound8={}; offer14={i:[] for i in soc}
    for i,(c3,o2) in soc.items():
        c3=hold('3',i,c3); o2=hold('2',i,o2)
        # _1_co_bi_offering, its terms at their names
        s14={}
        for k,p in o2:
            if p!=0:
                q=s14.get(k)
                if q is None: s14[k]=1 if p>0 else -1
                elif (q>0)!=(p>0): s14[k]=0
        s14=hold('14',i,s14)
        c12=dict(s14)
        for k,p in c3:
            q=s14.get(k,0)
            c12[k]=0 if (q!=0 and (q>0)==(p>0)) else (-1 if p>0 else 1)
        c12=hold('12',i,c12)
        r10=list(c12.items()); r10=hold('10',i,r10)
        ch11=dict(c3)
        for k,p in r10:
            if p!=0: ch11[k]=p
        ch11=list(ch11.items()); ch11=hold('11',i,ch11)
        ch11=hold('7',i,ch11)            # each parity chained, 7, named still
        wound8[i]=hold('8',i,ch11)       # the carrying wound, 8
        r6=hold('6',i,r10); r9=hold('9',i,r10); r15=hold('15',i,r10)
        for (a,b),val in (((i,6),r6),((i,10),r10),((i,9),r9 if '15' not in frozen else r15)):
            j=comp.get((a,b))
            j=hold('5',(a,b),j); j=hold('13',(a,b),j)
            if j is not None: offer14[j].extend(val)
    new={i:(wound8[i],offer14[i]) for i in soc}
    new=hold('16','soc',new)             # the society wound, 16
    if '17' in frozen and t>=K: return soc   # the society's next momentary named still
    if '1' in frozen and t>=K: return hold('1','soc',new)
    return new

def run(frozen=(), K=12, T=60, n=5):
    comp={}
    for i in range(n):
        comp[(i,9)]=(i+1)%n; comp[(i,6)]=(i+2)%n
    soc={i:([],[('s',1)] if i==0 else []) for i in range(n)}
    memo={}; pat=[]
    for t in range(T):
        soc=step(soc,comp,set(frozen),memo,t,K)
        pat.append(tuple(dict(soc[i][0]).get('s',0) for i in range(n)))
    last=max((t for t in range(1,T) if pat[t]!=pat[t-1]),default=None)
    return pat,last

# the written-out step equals the code's own when nothing is named still
comp={}
for i in range(5): comp[(i,9)]=(i+1)%5; comp[(i,6)]=(i+2)%5
a={i:([],[('s',1)] if i==0 else []) for i in range(5)}; b=dict(a); memo={}
same=True
for t in range(60):
    a=F(a,comp); b=step(b,comp,set(),memo,t,99)
    same &= all(dict(a[i][0])==dict(b[i][0]) and sorted(a[i][1])==sorted(b[i][1]) for i in a)
print('the written-out step equals Exhibit ONE\'s _17_tri_co_offering at 60 momentaries:',same)
pat,last=run(())
print('nothing named still: the chained parities last change at momentary',last+1 if last is not None else None,'of 60')
ROOTS=[('offering','1, 2, 17',['2']),('sharing','3, 4',['3']),('competencing','5, 13',['5','13']),('moralizing','6, 14',['14','6']),
       ('corusing','7, 15',['7','15']),('torusing','8, 16',['8','16']),('momentarying','9',['9']),('tunneling','10',['10']),
       ('chaining','11',['11']),('parity-changing','12',['12'])]
print('each root with its -ing taken out, its terms named still from momentary 13 on:')
for root,names,fr in ROOTS:
    for f in fr:
        pat,last=run((f,),K=12)
        stop = 'continues to momentary 60' if last==59 else f'stops: no chained parity changes after momentary {last+1}'
        print(f'  {root:16} at {f:>2}: {stop}')
for f in ['1','17']:
    pat,last=run((f,),K=12); print(f'  offering         at {f:>2}:', 'continues' if last==59 else f'stops after momentary {last+1}')
print('what each continuing term was named still at, and which selves keep changing:')
for f in ['2','14','6','9','15','5','13']:
    comp={}
    for i in range(5): comp[(i,9)]=(i+1)%5; comp[(i,6)]=(i+2)%5
    soc={i:([],[('s',1)] if i==0 else []) for i in range(5)}; memo={}; pats=[]
    for t in range(60):
        soc=step(soc,comp,{f},memo,t,12); pats.append(tuple(dict(soc[i][0]).get('s',0) for i in range(5)))
    held={k[1]:v for k,v in memo.items()}
    moving=[i for i in range(5) if len(set(p[i] for p in pats[20:]))>1]
    shown={k:(v if not isinstance(v,list) else [p for _,p in v]) for k,v in list(held.items())[:5]}
    print(f'  at {f:>2}: held at {shown}; selves still changing after momentary 20: {moving}')
