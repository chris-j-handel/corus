import sys,re
f=sys.argv[1]; L=open(f).read().split('\n')
first=next((i for i,l in enumerate(L) if l.startswith('## ') or l.startswith('# ') and i>3),len(L))
heads=[re.sub(r'^#+\s*','',l).strip() for l in L if l.startswith('#')]
ents=[l[2:].strip() for l in L[:first] if l.startswith('- ')]
hs=set(heads)
print(sum(1 for e in ents if e in hs),'of',len(ents),'contents entries match a heading')
