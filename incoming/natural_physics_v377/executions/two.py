"""Natural Physics 3.3 at Exhibit ONE v376's code: two selves joined across both ways, chained + and none, both +, and opposite; the two parities at each momentary. Run from the repository root."""
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
ns={};exec(body.split('```python',1)[1].split('```',1)[0],ns)
f=ns['_17_tri_co_offering']
comp={('A',10):'B',('B',10):'A'}
for start in [({'A':([('s',1)],[]),'B':([],[])}),({'A':([('s',1)],[]),'B':([('s',1)],[])}),({'A':([('s',1)],[]),'B':([('s',-1)],[])})]:
    soc=start; rows=[]
    for m in range(8):
        soc=f(soc,comp)
        rows.append(tuple(dict(soc[k][0]).get('s',0) for k in 'AB'))
    print(rows)
