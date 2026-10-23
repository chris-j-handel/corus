import re, os, sys, shutil, json
os.chdir('/home/claude/corus')
DRY='--dry' in sys.argv
NI='Natural_Intelligence_v391.md'; TH='Exhibit_THIRTY_Co-Chaining_Logic_Registry_v391.md'
EQ='Exhibit_TWENTY-EIGHT_Equilibria_Registry_v391.md'; NU='Exhibit_THREE_Natural_Numbers_v391.md'
PREV="**Natural intelligence** is the method of living as a same-existing self."
NEW=sys.argv[1] if len(sys.argv)>1 and not sys.argv[1].startswith('--') else "Living is **co-intelligencing** within a universal set."
NEW_ADD="co-intelligencing, living within a universal set"
K=15
MAP={o:(o if o<=K else o+1) for o in range(1,3000)}
ni=open(NI).read(); th=open(TH).read()
assert ni.count(PREV+' \\\n')==1
ni=ni.replace(PREV+' \\\n', PREV+' \\\n'+NEW+' \\\n')
m=re.search(r'^%d\. '%K+re.escape(PREV)+r'\n\n(\s*)\*Adding: .*?\*\n\n',th,re.M|re.S); ind=m.group(1)
th=th[:m.end()]+'NEWSTEP. '+NEW+'\n\n'+ind+'*Adding: '+NEW_ADD+'.*\n\n'+th[m.end():]
cnt=[0]
def seq(m): cnt[0]+=1; return '%d. '%cnt[0]
th=re.sub(r'^(NEWSTEP|\d+)\. ',seq,th,flags=re.M)
REF=re.compile(r'\b([Ss]teps? )(\d+)((?:(?:, | and | or | to )\d+(?!\d|\.\d|-))*)(?! up| less| on\b)')
log=[]
def remap(t,tag):
    def rep(m):
        g=m.group(0)
        if g=='step 1 to 3 to 5 to 6': return g
        mm=re.match(r'step (\d+), 17$',g)
        if mm and int(mm.group(1))>200: r='step %d, 17'%MAP[int(mm.group(1))]; log.append((tag,g,r)); return r
        nums=re.findall(r'\d+',m.group(2)+m.group(3)); it=iter([MAP[int(x)] for x in nums])
        r=m.group(1)+re.sub(r'\d+',lambda _:str(next(it)),m.group(2)+m.group(3))
        if r!=g: log.append((tag,g,r))
        return r
    return REF.sub(rep,t)
g0=th.index('\n## 5 '); th=th[:g0]+remap(th[g0:],'TH')
parts=re.split(r'(\n## \d+ [^\n]*\n)',th); out=[parts[0]]
for k in range(1,len(parts),2):
    head,body=parts[k],parts[k+1]
    al=[x for y in re.findall(r'\*Adding: (.*?)\.\*',body) for x in y.split('; ')]
    if re.search(r'\*Entering: (.*?)\.\*',body) and al: body=re.sub(r'\*Entering: (.*?)\.\*',lambda m:'*Entering: '+'; '.join(al)+'.*',body,count=1)
    out+=[head,body]
th=''.join(out)
others={f:remap(open(f).read(),f[:20]) for f in (EQ,NU)}
print('steps',cnt[0],'refs re-pointed',len(log))
for x in log[:12]: print(x)
if not DRY:
    A='archive/session_v391/prior_to_opening64_cointelligencing'; os.makedirs(A,exist_ok=True)
    for f in (NI,TH,EQ,NU): shutil.copy(f,os.path.join(A,f))
    open(NI,'w').write(ni); open(TH,'w').write(th)
    for f,t in others.items(): open(f,'w').write(t)
