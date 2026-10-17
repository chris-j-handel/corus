"""Where the ten named still sit at Exhibit ONE's code, from its own tables and the six forward recursionings. Run from the repository root."""
import re
body=open('Exhibit_ONE_Natural_Resolver_v376.md').read()
rows=re.findall(r'^\| (\d+) \| (\d+-[a-z-]+) \| (odd|even), (co|bi) \| ([a-z]+), ([a-z]+(?:, [a-z]+)?) \|',body,re.M)
name={int(n):nm for n,nm,*_ in rows}; parity={int(n):p for n,nm,p,*_ in rows}
print('1. the six forward recursionings, Co-Chaining Logic Registry step 69: the self 1 to 3 to 5 to 7, the other 2 to 4 to 6 to 8, each step two momentaries of its side')
steps=[('self',1,3),('self',3,5),('self',5,7),('other',2,4),('other',4,6),('other',6,8)]
for n in range(1,9):
    joint=[f'{s} {a}→{b} {"opens" if n==a else "completes"}' for s,a,b in steps if n in (a,b)]
    mid=[f'{s} {a}→{b}, its first momentary {a}–{a+1} completing' for s,a,b in steps if a<n<b]
    print(f'  {n}: at a step joint: {"; ".join(joint)}' + (f' | inside a step: {"; ".join(mid)}' if mid else ''))
both=[n for n in range(1,9) if any(n in (a,b) for s,a,b in steps) and any(a<n<b for s,a,b in steps)]
print('   the numbers at which one side is at a step joint and the other inside its step:',both)
print('2. at the code each number is its name, Exhibit ONE\'s table of the momentaries of exchanging; the name opens at its parity, odd at the self and even at the other')
for n in range(2,7):
    opens='self' if parity[n]=='odd' else 'other'; comp='other' if opens=='self' else 'self'
    print(f'  {n} {name[n]}: opens at the {opens}, completes at the {comp}; its 8 up {n+8} {name[n+8]}')
print('3. the five pairs of the ten at the numbers 2 to 6, Resolving the Hard Problem Registry line 35 and the Equilibria Registry 3.3, the entering face the self\'s, along, the surfacing the other\'s, across')
PAIRS={2:('an arriving named from behind','an opening named as a place'),3:('a completing named as a last','a carry named as a store'),4:('a middle named as an end','a parity named as a magnitude'),5:('a sequencing named to one beat','a rate named as a value'),6:('a two-way named to one side','the between named as a cut')}
code={}
for n,(e,s_) in PAIRS.items():
    selfface='opening' if parity[n]=='odd' else 'completing'; otherface='completing' if selfface=='opening' else 'opening'
    code[e]={n,n+8}; code[s_]={n,n+8}
    print(f'  {n}: {e}, at the self\'s {selfface} of {name[n]}; {s_}, at the other\'s {otherface}')
print('4. against the Equilibria Registry\'s own table of the two faces, lines 195 to 201')
eq=open('Exhibit_TWENTY-EIGHT_Equilibria_Registry_v377.md').read()
for n in range(2,7):
    m=re.search(r'^\| '+str(n)+r' \| ([^|]+) \|',eq,re.M); print(f'  {n}: the registry says "{m.group(1).strip()}"; the code\'s parity gives self {"opening" if parity[n]=="odd" else "completing"}, other {"completing" if parity[n]=="odd" else "opening"}')
print('5. the three seatings the files give, against the code\'s')
T22={'an arriving named from behind':{10,2},'an opening named as a place':{14,6},'a completing named as a last':{12,4},'a carry named as a store':{16,8},'a middle named as an end':{13,5},'a parity named as a magnitude':{12,4},'a sequencing named to one beat':{16,8},'a rate named as a value':{13,5},'a two-way named to one side':{11,3},'the between named as a cut':{15,7}}
NN={'an opening named as a place':{1},'an arriving named from behind':{2},'a completing named as a last':{6},'a carry named as a store':{8},'a two-way named to one side':{3},'the between named as a cut':{5},'a middle named as an end':{5},'a parity named as a magnitude':{7},'a rate named as a value':{7},'a sequencing named to one beat':{4}}
T28={'an arriving named from behind':{3,2},'an opening named as a place':{16,3},'a completing named as a last':{11,16},'a carry named as a store':{12,6},'a middle named as an end':{10,11},'a parity named as a magnitude':{6,10},'a sequencing named to one beat':{4,1},'a rate named as a value':{14,12},'a two-way named to one side':{1,14},'the between named as a cut':{2,4}}
cyc_of={}
for c in ([1,9,8,16],[2,15,7,10],[3,11,6,14],[4,13,5,12]):
    for x in c: cyc_of[x]=tuple(c)
for label,T in (('Resolving the Hard Problem Registry, line 740, two names each',T22),('Natural Naming 4.9 and the Co-Chaining Logic Registry step 380, one name each',NN),("this file's naming ring before, at the archive, an edge of two names each",T28)):
    same=[k for k in code if T[k]==code[k]]
    share=[k for k in code if T[k]&code[k]]
    oncyc=[k for k in code if any(cyc_of[x]==cyc_of[min(code[k])] for x in T[k])]
    print(f'  {label}: the same two names as the code at {len(same)}; a name shared with the code\'s two at {len(share)} {share}; on the code\'s four-cycling at {len(oncyc)} {oncyc}')
