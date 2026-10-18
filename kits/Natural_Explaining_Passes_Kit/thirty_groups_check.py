import re,sys
t=sys.stdin.read()
for g in re.split(r'\n(?=## )',t):
    m=re.search(r'\*Entering: (.*?)\.\*',g)
    if not m: continue
    ent=m.group(1).split('; ')
    add=[a for x in re.findall(r'\*Adding: (.*?)\.\*',g) for a in x.split('; ')]
    bad=[a for a in add if a not in ent]+[x for x in ent if x not in add]
    if bad: print(' ', g[:30].strip(), bad)
