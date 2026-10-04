"""The rule of the next 0 at a torus of two odd numbers, worked as arithmetic (the Co-Chaining Logic Registry, steps 653 and 657).
From the repository root: python3 incoming/v380L/derivings/torus_rule_arithmetic.py
This is arithmetic on a rule derived by hand from the resolver's cells. It reads no file and executes no resolver. It gives, for each
row, the momentaries to the sharings again and the momentary they are from, beside Exhibit ONE's table and beside the closed forms
of steps 655 and 656. A result here is a coupling partner and decides nothing."""
def holds(p,q,K):
    tau=[[None]*(K+1) for _ in range(p)]
    for k in range(1,K+1):
        for i in range(p):
            a=tau[i][k-1] if k>1 else None
            b=tau[i-1][k] if i>=1 else (tau[p-1][k-q] if k>q else None)
            if a is None and b is None: t=2
            elif a is None: t=b+1
            elif b is None: t=a+1
            else: t=max(a,b)+1 if a!=b else a+2
            tau[i][k]=t
    return tau
def period(p,q):
    K=40*q; tau=holds(p,q,K); Tmax=min(tau[i][K] for i in range(p))-1
    H={}
    for i in range(p):
        for k in range(1,K+1): H.setdefault(tau[i][k],set()).add((i,(k-1)%q))
    # v at t=1: (-1)^(i+j) up to one sign; c(t)=v(t)*(-1)^t ; x(t)=0 at hold else c(t+1)
    v={(i,j):(-1)**(i+j) for i in range(p) for j in range(q)}
    X=[]
    for t in range(1,Tmax):
        h=H.get(t,set()); x={}
        for z in v:
            if z in h: v[z]=-v[z]; x[z]=0
            else: x[z]=v[z]*(-1)**(t+1)
        X.append(tuple(x[z] for z in sorted(x)))
    n=len(X)
    for P in range(1,6*max(p,q)+1):
        T=n-P
        while T>0 and X[T-1]==X[T-1+P]: T-=1
        if T < n-4*P-20: return P,T+1
    return None
rows=[(1,3),(1,5),(3,3),(3,5),(3,7),(3,13),(5,7),(5,11),(7,17),(17,59)]
table={(1,3):(3,2),(1,5):(5,2),(3,3):(12,6),(3,5):(12,6),(3,7):(7,8),(3,13):(13,8),(5,7):(20,12),(5,11):(11,14),(7,17):(17,20),(17,59):(59,50)}
for r in rows: print(r,period(*r),table[r], period(*r)==table[r])
for r in [(3,9),(3,11),(5,9),(5,13),(7,9),(7,15),(9,9),(7,13),(9,17),(9,19),(11,23)]:
    p,q=r; th=(q,3*p-1) if q>2*p else (4*p,3*p-3)
    print(r,period(*r),'theorem',th, period(*r)==th)
