"""A between surrounded by the living, and one with a non-living side, at Exhibit ONE's code: what passes across it. Run from the repository root."""
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read(); ns={}
exec(body.split('```python',1)[1].split('```',1)[0],ns); F=ns['_17_tri_co_offering']; O=ns['_1_co_bi_offering']
sym=lambda v:{1:'+',-1:'-',0:'0',None:'.'}[v]
arrivals=[[1],[],[],[],[-1],[],[],[1,-1],[],[]]   # what arrives at X from beside: +, then nothing, then -, then a parting, then nothing
print('what arrives at X, momentary by momentary:', [a for a in arrivals])
for label,joins in (('along, X to B at 9',{('X',9):'B'}),('across, X to B at 6',{('X',6):'B'})):
    for living in (True,False):
        soc={'X':([],[]),'B':([],[])}; xs=[]; bs=[]
        for t,a in enumerate(arrivals):
            soc['X']=(soc['X'][0] if living else [], [('s',p) for p in a])
            rx,_=O(*soc['X']); rb,_=O(*soc['B']); xs.append(dict(rx).get('s')); bs.append(dict(rb).get('s'))
            soc=F(soc,joins)
        print(f"  {label}; X {'living, carrying its prior' if living else 'non-living, carrying nothing'}: X releases {''.join(sym(x) for x in xs)} | B releases {''.join(sym(b) for b in bs)}")
