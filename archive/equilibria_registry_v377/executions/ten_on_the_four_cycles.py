"""The ten at the four four-cyclings: momentarying and parity changing, prior, now and next inside each. Run from the repository root."""
import re
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
rows=re.findall(r'^\| (\d+) \| (\d+-[a-z-]+) \| (odd|even), (co|bi) \|',body,re.M)
name={int(n):nm for n,nm,*_ in rows}; par={int(n):p for n,nm,p,_ in rows}
table=re.findall(r'^\| four-cycle ([\d-]+) \|',body,re.M)
print("1. Exhibit ONE's four-cycles, its table of forms:",table)
print('2. each four-cycle from an odd n ascending, n, n+8, 9-n, 17-n, and n again at the next; for 2-15-7-10 and 4-13-5-12 this is the round the other way from the exhibit\'s order, part 5')
TEN={2:('an arriving named from behind','an opening named as a place'),3:('a completing named as a last','a carry named as a store'),4:('a middle named as an end','a parity named as a magnitude'),5:('a sequencing named to one beat','a rate named as a value'),6:('a two-way named to one side','the between named as a cut')}
ROOT={1:'torusing: 8 and 16',3:'moralizing: 6 and 14',5:'competencing: 5 and 13',7:'corusing: 7 and 15'}
for n in (1,3,5,7):
    cyc=[n,n+8,9-n,17-n]
    steps=[]
    for a,b in zip(cyc,cyc[1:]+[cyc[0]]):
        kind='8 up, parity kept: momentarying' if b==a+8 else '17 less, parity changed: parity changing'
        assert (par[a]==par[b])==(b==a+8)
        steps.append(f'{a}→{b} {kind}')
    ten=[(k,f) for k in TEN for f in (k,k+8) if f in cyc]
    print(f'  {n} / {9-n}   {" → ".join(map(str,cyc))} → {n}   root {ROOT[n]}')
    for st in steps: print('      ',st)
    seats=sorted(set(k for k,f in ten))
    print('       the ten at it:', '; '.join(f'at {k} and {k+8}, {TEN[k][0]} at the self and {TEN[k][1]} at the other' for k in seats) if seats else 'none: the entry, the momentarying at 9 and the two windings, the loop the ten are inside')
print("3. inside each four-cycling, in Exhibit ONE's order: two names of one parity and two of the other, the parity changing twice, and its first name met again at the next momentary, a further occurrence")
for t in table:
    cyc=[int(x) for x in t.split('-')]
    changes=sum(par[a]!=par[b] for a,b in zip(cyc,cyc[1:]+[cyc[0]]))
    print(f"  {t}: parities {[par[x] for x in cyc]}; the parity changes {changes} times in the round; {cyc[0]} again at the next")
print('4. the self\'s forward recursionings, 1, 3, 5, 7, each paired with its partner nine less, Exhibit ONE\'s table at lines 234 to 239, at the four-cycles:',[(n,9-n) for n in (1,3,5,7)])
print("5. the four-cycles in the exhibit's order, 1-9-8-16 and 3-11-6-14 going 8 up first, 2-15-7-10 and 4-13-5-12 going 17 less first, round the other way")
for t in table:
    cyc=[int(x) for x in t.split('-')]
    out=[]
    for a,b in zip(cyc,cyc[1:]+[cyc[0]]):
        kept=par[a]==par[b]
        out.append(f"{a}→{b} {'8 apart, parity kept: momentarying' if kept else '17 less, parity changed: parity changing'}")
        assert kept==(abs(a-b)==8) and (kept or a+b==17)
    print('  '+t+': '+'; '.join(out))
nine=re.findall(r'^\| (\d+)-[a-z-]+ \| \d+-[a-z-]+ \| (\d+)-[a-z-]+ \|',body,re.M)
print('   Exhibit ONE\'s nine less, within 1 to 8:',[(int(a),int(b)) for a,b in nine])
