import sys,re,difflib
f,o=sys.argv[1],sys.argv[2]
L=open(f).read().split('\n'); N=open(o).read().split('\n')
if len(N)!=len(L): print('LINECOUNT',len(L),len(N)); sys.exit(1)
ALLOW={'a','an','each','its','their','one'}
def norm(s): return re.sub(r'(\*\*|\*|_)(?=\w)',r'\1 ',s.lower())
fence=False; bad=0
for k,(a,b) in enumerate(zip(L,N)):
    ln=k+1
    isf=a.lstrip().startswith('```')
    prot=fence or isf
    if isf: fence=not fence
    if a==b: continue
    if prot: print('FENCE line',ln); bad+=1; continue
    cls = a.startswith('#') or a.startswith('- ') or a.lstrip().startswith('- ') or '*Adding:' in a or '*Entering:' in a or re.search(r'(\*\*|\*)the\b',a,re.I)
    if not cls: print('CLASS line',ln); bad+=1; continue
    if a[:len(a)-len(a.lstrip())]!=b[:len(b)-len(b.lstrip())]: print('INDENT',ln); bad+=1; continue
    ta=norm(a).split(); tb=norm(b).split()
    for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,ta,tb,autojunk=False).get_opcodes():
        if op=='equal': continue
        A=ta[i1:i2]; B=tb[j1:j2]
        if op=='delete' and all(x=='the' for x in A): continue
        if op=='replace' and len(A)==len(B) and all(x==y or (x=='the' and y in ALLOW) for x,y in zip(A,B)): continue
        print('CHANGE line',ln,op,A,'->',B); bad+=1; break
    for ph in ['the universe','the set of all','the changing set']:
        if a.lower().count(ph)!=b.lower().count(ph): print('KEEP-PHRASE',ln,ph); bad+=1
print('OK' if bad==0 else f'REFUSED {bad}')
