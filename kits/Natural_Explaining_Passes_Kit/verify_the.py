import sys,re,difflib
f,s,e,o=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
L=open(f).read().split('\n')[s-1:e]; N=open(o).read().split('\n')
if N and N[-1]=='' and len(N)==len(L)+1: N=N[:-1]
if len(N)!=len(L): print('LINECOUNT',len(L),len(N)); sys.exit(1)
ALLOW={'a','an','each','its','their','one'}
infence=False; bad=0
# fence state must be computed from file start
full=open(f).read().split('\n')
fence=False
for i in range(s-1): 
    if full[i].lstrip().startswith('```'): fence=not fence
first_part=next((i for i,l in enumerate(full) if l.startswith('## ')),len(full))
for k,(a,b) in enumerate(zip(L,N)):
    ln=s+k
    prot = fence or a.lstrip().startswith('```') or a.startswith('#') or a.lstrip().startswith((' ','*Adding:','*Entering:')) and ('*Adding:' in a or '*Entering:' in a) or re.match(r'^\|?\s*-{3}',a) or (ln-1<first_part and re.match(r'^- \d',a))
    if a.lstrip().startswith('```'): fence=not fence
    if a==b: continue
    if prot: print('PROTECTED line',ln); bad+=1; continue
    if len(a)-len(a.lstrip())!=len(b)-len(b.lstrip()) or a[:len(a)-len(a.lstrip())]!=b[:len(b)-len(b.lstrip())]: print('INDENT',ln); bad+=1; continue
    ta=re.findall(r"\S+",a.lower()); tb=re.findall(r"\S+",b.lower())
    for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,ta,tb,autojunk=False).get_opcodes():
        if op=='equal': continue
        A=[re.sub(r'^[\*\(\[_"]+','',x) for x in ta[i1:i2]]; B=[re.sub(r'^[\*\(\[_"]+','',x) for x in tb[j1:j2]]
        if op=='delete' and all(x=='the' for x in A): continue
        if op=='replace' and len(A)==len(B) and all(x=='the' and y in ALLOW for x,y in zip(A,B)): continue
        if op=='replace' and len(A)==len(B) and all((x==y) or (x=='the' and y in ALLOW) for x,y in zip(A,B)): continue
        # deletion of 'the' with neighbour punctuation moving, e.g. '**the' -> '**'
        if op=='replace' and all(x.replace('the','')==y for x,y in zip(ta[i1:i2],tb[j1:j2])) and len(A)==len(B): continue
        print('CHANGE line',ln,op,ta[i1:i2],'->',tb[j1:j2]); bad+=1; break
    if 'the universe' in a.lower() and a.lower().count('the universe')!=b.lower().count('the universe'): print('UNIVERSE line',ln); bad+=1
print('OK' if bad==0 else f'REFUSED {bad}')
