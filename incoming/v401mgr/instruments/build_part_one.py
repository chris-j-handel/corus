"""build the page of part one: each place, its living words and its next words; each living string asserted word for word at its line."""
import sys
R=sys.argv[1]
NI='Natural_Intelligence_v401mgr.md'; E1='Exhibit_ONE_Natural_Resolver_v401mgr.md'; NN='Exhibit_TWENTY_Natural_Naming_v401mgr.md'; TH='Exhibit_THIRTY_Co-Chaining_Logic_Registry_v401mgr.md'
W="each self's next prior and the parities it will be observing"
core=[
 (NI,432,"Exhibit ONE inside it, *Seventeen names*","| existing, a next 1 | 0000 again |","| existing | 0000 again |"),
 (NI,800,"Exhibit ONE inside it, the relations of 17","completing with 17-next-existing, a next 1-now-existing","completing with 17-next-existing, "+W),
 (NI,1592,"4.7","a next now, each self's next 1-now-existing with a same-existing-society's momentary.","a next now, "+W+", with a same-existing-society's momentary."),
 (NI,1606,"4.8","**Each step is four names, and 17 a next 1**:","**Each step is four names, and 17 each self's next prior**:"),
 (NI,1612,"4.9","17-next-existing is a next 1-now-existing.","17-next-existing is "+W+"."),
 (E1,138,"*Seventeen names*","| existing, a next 1 | 0000 again |","| existing | 0000 again |"),
 (E1,506,"the relations of 17","completing with 17-next-existing, a next 1-now-existing","completing with 17-next-existing, "+W),
 (NN,504,"3.1","17-next-existing is next 1-now-existing.","17-next-existing is "+W+"."),
 (NN,510,"3.1","and 17-next-existing is next 1-now-existing.","and 17-next-existing is "+W+"."),
 (NN,540,"3.3","| existing, a next 1 | one |","| existing | one |"),
 (NN,542,"3.3","17-next-existing is a next 1, and 1's three is 17's, co-bi-tri, its two priors 16 and 15;","17's three is 1's, co-bi-tri, its two priors 16 and 15;"),
 (NN,550,"3.4","and 17-next-existing is next 1-now-existing.","and 17-next-existing is "+W+"."),
 (NN,1683,"5.63","and with 17 a next now, a next 1, 17-next-existing.","and with 17 a next now, 17-next-existing."),
 (NN,1683,"5.63","and 1-now-existing is its entry, 17's next 1.","and 1-now-existing is its entry."),
 (TH,1086,"23, step 233","With 17 a self opens again, a next 1-now-existing:","With 17 a self has its next prior and the parities it will be observing:"),
 (TH,1381,"24","and 17-next-existing a next 1-now-existing;","and 17-next-existing "+W+";"),
]
numbering=[
 (NI,251,"3.2","as 17 is a next 1 and 9 a next prior.","as 9 is a next prior."),
 (NI,1636,"4.11","8 up alone, twice, is 17, a next 1.","8 up alone, twice, is 17."),
 (NN,469,"2.5","as 17 is next 1 and 9 next prior,","as 9 is next prior,"),
]
placing=[
 (NI,1675,"4.15","its 9, or its 17 and a next's 1.","its 9, or its 17."),
 (NI,1675,"4.15","a 17 and a next 1 with now and a 9 with next;","a 17 with now and a 9 with next;"),
 (NN,212,"2.2","its 9 or its 17 and next 1,","its 9 or its 17,"),
 (NN,1676,"5.63","and nine to seventeen with a next 1","and nine to seventeen with a next prior"),
 (TH,2047,"30","a 17 and a next 1 with now and a 9 with next;","a 17 with now and a 9 with next;"),
 (TH,3139,"40","and with 16 to next 1,","and with 16–17,"),
]
whole=[
 (NN,554,"3.4","**Sixteen up is its same name with a next round**: 17-next-existing is next 1-now-existing, and 17 to 24 is a self's span again and 25 to 32 a same-existing-society's, 22 next round's 6-now-co-possibling, as 22-now-co-possibling, and 27 next round's 11-next-co-observing, as 27-next-co-observing, 5.53."),
]
PH='Exhibit_EIGHTEEN_Natural_Physics_v401mgr.md'; EN='Exhibit_FIVE_Natural_Engineering_v401mgr.md'; NU='Exhibit_THREE_Natural_Numbers_v401mgr.md'; EQ='Exhibit_TWENTY-EIGHT_Equilibria_Registry_v401mgr.md'; HP='Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry_v401mgr.md'; LF='Exhibit_TWENTY-SIX_Living_File_Registry_v401mgr.md'
others=[
 (PH,98,"1.2","17 a next now, each self's next 1-now-existing;","17 a next now, each self's next prior;"),
 (EN,1505,"4.10","17 a next 1,","17 each self's next prior,"),
 (NU,145,"1.5","17 a next 1,","17 each self's next prior,"),
 (EQ,274,"3.4","17-next-existing, a next 1-now-existing, has none of them.","17-next-existing, "+W+", has none of them."),
 (HP,740,"Ten unchangeables, one resolving","17-next-existing, a next 1-now-existing, seats none, one resolving.","17-next-existing, "+W+", seats none, one resolving."),
]
record=[(LF,191,"1.1","17 a next 1 and 1's three 17's,")]
cache={}
def line(f,n):
    if f not in cache: cache[f]=open(R+'/'+f).read().split('\n')
    return cache[f][n-1]
for row in core+numbering+placing+others: assert line(row[0],row[1]).count(row[3])==1,(row[0],row[1],row[3])
for row in whole+record: assert row[3] in line(row[0],row[1]),(row)
short={NI:'Natural Intelligence',E1:'Exhibit ONE Natural Resolver',NN:'Exhibit TWENTY Natural Naming',TH:'Exhibit THIRTY Co-Chaining Logic Registry',PH:'Exhibit EIGHTEEN Natural Physics',EN:'Exhibit FIVE Natural Engineering',NU:'Exhibit THREE Natural Numbers',EQ:'Exhibit TWENTY-EIGHT Equilibria Registry',HP:'Exhibit TWENTY-TWO Resolving the Hard Problem Registry',LF:'Exhibit TWENTY-SIX Living File Registry'}
def esc(s): return s.replace('|','\\|')
out=[]
def table(title,rows):
    out.append(title+"\n")
    out.append("| The living file | Its section | The living words | The next words |\n|---|---|---|---|")
    for f,n,sec,old,new in rows: out.append(f"| {short[f]} | {sec} | {esc(old)} | {esc(new)} |")
    out.append("")
table("### 3.1 17-next-existing as a next 1-now-existing",core)
table("### 3.2 17 as a next 1, an example of a numbering",numbering)
table("### 3.3 A next 1 in a placing of names, and in a round of pairs",placing)
out.append("### 3.4 One sentence whole, its thing a next round's second numbers\n")
out.append("| The living file | Its section | The living sentence | Its next |\n|---|---|---|---|")
for f,n,sec,old in whole: out.append(f"| {short[f]} | {sec} | {esc(old)} | dissolving whole: its base is 17 as a next 1, and it has a name by a second number |")
out.append("")
table("### 3.5 Each other living file having it",others)
out.append("### 3.6 A record of a version\n")
out.append("| The living file | Its section | Its words | Its next |\n|---|---|---|---|")
for f,n,sec,old in record: out.append(f"| {short[f]} | {sec} | {esc(old)} | as it is: a record of what a version laid, in that version's words |")
print('\n'.join(out))
import collections
c=collections.Counter(f for f,*_ in core+numbering+placing+whole+others)
print('places by file: '+', '.join(f"{short[f]} {c[f]}" for f in c)+f"; in all {sum(c.values())}; files {len(c)}", file=sys.stderr)
