"""Do-no-harm check of Exhibit ONE v395 against v391 (Geodesic Improving Method 1.5): word-stream and line accounting."""
import re,sys,collections
S='/tmp/claude-0/-home-claude/906f769f-68f8-5342-8e15-da9cc999e269/scratchpad'
sys.argv=['x','/dev/null']; ns={}; exec(open(S+'/build_exhibit_one.py',encoding='utf-8').read().split("B = []")[0], ns)
mom,named=ns['mom'],ns['named']
W=lambda t: collections.Counter(re.findall(r"[a-z][a-z'-]*[a-z]|[a-z]", t.lower()))
L=open('Exhibit_ONE_Natural_Resolver_v391.md',encoding='utf-8').read().split('\n')
V=open(S+'/exhibit_one_best.md',encoding='utf-8').read()
ni=open('gathering-value/Natural_Intelligence.md',encoding='utf-8').read(); niE=ni[ni.find('Explaining at Exhibit ONE, leaving it'):]
nr=open('gathering-value/Natural_Resolver.md',encoding='utf-8').read()
DISSOLVED={'momentary','momentaries','sharing','sharings','shares','share','shared','surfacing','surfaces','surface','form','forms','changing','changes','change'}
v391=W('\n'.join(L)); allw=W(V)+W(niE)+W(nr)
lost=sorted(w for w in v391 if w not in allw and w not in DISSOLVED)
print('words of v391 with zero across v395, its explaining placed and Natural Resolver gathering:',lost)
placed=set(int(n) for n in re.findall(r'from Exhibit ONE v391, line (\d+)\)',ni))
Vl=set(V.split('\n')); Vw=W(V)
incode=False; out=[]
for n,s in enumerate(L,1):
    if s.startswith('```'): incode=not incode; continue
    if incode or not s.strip() or n<=10 or s.strip()=='---': continue
    if s in Vl or named(mom(s)) in Vl or n in placed: continue
    # content words of this line not in v395
    miss=[w for w in W(named(mom(s))) if w not in Vw and w not in DISSOLVED]
    out.append((n,miss,s))
print('v391 lines neither whole in v395 nor placed:',len(out),' of these with words v395 lacks:',sum(1 for o in out if o[1]))
open(S+'/left_lines2.txt','w',encoding='utf-8').write('\n'.join('%d\t%s\t%s'%(n,','.join(m),s) for n,m,s in out))
