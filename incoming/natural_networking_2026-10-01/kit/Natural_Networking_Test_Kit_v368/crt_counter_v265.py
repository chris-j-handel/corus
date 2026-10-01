# The CRT counter at scale — odd primes as coprime ring-registers on the pure binary resolver
# (the resolver emanated from "alternating right spiral sequencing binary co-offering").
# 438 sign-only nodes count to ~3.85e21; the count reads back from the ring phases.
from math import lcm, prod

from resolver import _1_self_coupling

class Ring:
    def __init__(self,N): self.N=N; self.stands={i:(1 if i%2==0 else -1) for i in range(N)}; self.carry=[]
    def step(self):
        acc=[(i,self.stands[(i-1)%self.N]) for i in range(self.N) if self.stands.get((i-1)%self.N)]
        seq,self.carry=_1_self_coupling(self.carry,acc)
        self.stands={i:m for i,m in seq if 0<=i<self.N}       # only what stands
    def state(self): return (tuple(sorted(self.stands.items())),tuple(self.carry))

def run(primes,beats):
    rings=[Ring(p) for p in primes]; out=[]
    for _ in range(beats):
        for r in rings: r.step()
        out.append(tuple(r.state() for r in rings))
    return out

if __name__=="__main__":
    for primes in [[3,5],[3,5,7],[3,5,7,11,13]]:
        period=lcm(*[4*p for p in primes]); k=min(period,2000)
        distinct=len(set(run(primes,k)))
        print(f"rings {primes} ({sum(primes)} nodes): period {period:,}  first {k} all-distinct: {distinct==k}")
    odd=[3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
    period=lcm(*[4*p for p in odd])
    print(f"\nfull register: {len(odd)} rings, {sum(odd)} sign-only nodes -> {period:,} counts (~{period:.3e})")
    # decode small case
    primes=[3,5,7]; period=lcm(*[4*p for p in primes]); st=run(primes,period); idx={s:b for b,s in enumerate(st)}
    print("decode [3,5,7]:", all(idx[st[b]]==b for b in range(period)), "(count reads back from ring phases)")
