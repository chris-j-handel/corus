import importlib.util, itertools, random, collections
spec=importlib.util.spec_from_file_location('r','resolver.py'); r=importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
# 1) a self's own parity (its next prior, 11) over every case: values seen
vals=collections.Counter(); zeros_between=collections.Counter()
for prior in (1,-1,None):
    for n in range(4):
        for rec in itertools.product((1,-1,0),repeat=n):
            three=[('s',prior)] if prior is not None else []
            ten,eleven=r._1_now_existing(three,[('s',p) for p in rec])
            for k,v in eleven: vals[v]+=1
            for k,v in ten:
                if v==0: zeros_between['shared 0 with 10']+=1
print("a self's own parity (11) takes only:",dict(vals))
print(dict(zeros_between))
# 2) a spiral of one: a self receiving its own going along; its parity momentary by momentary and its joint forms
three=[('s',-1)]; two=[]; seq=[]
for m in range(8):
    ten,eleven=r._1_now_existing(three,two); seq.append(dict(eleven)['s']); three=eleven; two=ten
print("spiral of one, its parity:",seq)
print("joint forms (now, next):",sorted(set(zip(seq,seq[1:]))))
# 3) two selves bi-coupling across both ways, random priors, many momentaries: own parity values and changing / not-changing
rng=random.Random(1); own=collections.Counter(); step=collections.Counter()
for trial in range(200):
    a=[('s',rng.choice((1,-1)))]; b=[('s',rng.choice((1,-1)))]; ta=[]; tb=[]
    for m in range(12):
        na,ea=r._1_now_existing(a,tb); nb,eb=r._1_now_existing(b,ta)
        for old,new in ((a,ea),(b,eb)):
            o=dict(old)['s']; x=dict(new)['s']; own[x]+=1; step['not changing' if o==x else 'changing']+=1
        a,b,ta,tb=ea,eb,na,nb
print("two selves, own parity values:",dict(own),"| each momentarying:",dict(step))
