"""opening_rebuild_v391.py: the motion that entered Natural Intelligence's 64-line opening at v391, kept as the template for a next rebuild.
L is the opening, each (sentence, Adding text or the old step whose Adding it keeps, old line it comes from); PARA the paragraph ends; MAP the old line to its new line.
It writes the opening at NI, THIRTY's groups 1 to 4 word for word, renumbers THIRTY's later steps, re-points step references at THIRTY, Equilibria and Numbers, and the opening's line pointers at NI and the Living File Registry.
Run with --dry first and read every re-pointing it prints."""
import re, os, sys, json, shutil
os.chdir(os.environ.get('CORUS', '.'))
DRY='--dry' in sys.argv
NI='Natural_Intelligence_v391.md'; TH='Exhibit_THIRTY_Co-Chaining_Logic_Registry_v391.md'
EQ='Exhibit_TWENTY-EIGHT_Equilibria_Registry_v391.md'; NU='Exhibit_THREE_Natural_Numbers_v391.md'; RG='Exhibit_TWENTY-SIX_Living_File_Registry_v391.md'
A='archive/session_v391/prior_to_opening64'
# (text, adding or old-step-number for its Adding, old step it comes from or None)
L=[
("The **universe** is the set of all now-existing things.",1,1),
("One universe is now-existing.","one universe",2),
("Only one universe is possibly now-existing.","only one universe possibly",3),
("A now-existing thing from a prior-existing same thing is a **same-existing** thing.",4,4),
("Each now-existing thing is a **universal set** of all its own same-existing things.","a universal set, a thing's own same-existing things",None),
("Each now-existing thing **is-or-is-not** within each universal set.","is-or-is-not, within each universal set",None),
("**Observing** is prior-existing, is-or-is-not same-existing.","observing, prior-existing, is-or-is-not same-existing",5),
("By observing, the universe is a same-existing set.","the universe, same-existing by observing",6),
("**Possibling** is now-existing, is-or-is-not same-existing.",7,7),
("**Discovering** is next-existing, is-or-is-not same-existing.",8,8),
("A **self** is a now- and same-existing thing observing, possibling and discovering its own next-existing.",9,9),
("For a self, each same-existing thing is that self or an **other**.","an other, for a self",10),
("Each self is **living**.","living",None),
("A living same-existing set is a self.","a living set, a self",12),
("**Natural intelligence** is the method of living as a same-existing self.",13,13),
("Each now-existing thing is living or **non-living**.","non-living",14),
("The universe is non-living.","the universe non-living",15),
("Within the universe are living and non-living things.",16,16),
("A **bi-coupling** is a self and an other self sharing possibling.",17,17),
("A bi-coupling is a self.","a bi-coupling, a self",18),
("A self's **parity** is its changing direction relative to an other existing thing, + or −.","parity, a changing direction, + or −",19),
("A **0** is a between of two changing directions.","a 0, a between",None),
("A 0 is **indifferencing**.","indifferencing",None),
("Each parity is a living thing.","a parity, a living thing",None),
("Each self's living parities are within its universal set.","living parities within a self's universal set",None),
("Each self is **beholding** its own parity with each other it is sharing with, now.","beholding",20),
("A self's parity with an other is its **moral value** with that other.","moral value",None),
("Each thing beholding a parity is living.","beholding, living",21),
("Others' parities are **agreeing** or **parting**.","agreeing or parting",None),
("Others' agreeing parity is a self's next-existing parity.","an other's agreeing parity, next-existing",23),
("A self whose next-existing parity is its prior-existing parity is sharing 0.","a self sharing 0",22),
("A self whose next-existing parity inverts its prior-existing parity is sharing its next-existing parity.","a self sharing its next-existing parity",None),
("With its possibling an empty set, or others' parities parting, a self's next-existing parity is its prior-existing parity inverting.","a prior-existing parity inverting",24),
("At a self's first sharing with others, their parities parting, the self is sharing 0.","a first sharing, sharing 0",25),
("Each self is living with others.","each self with others",26),
("Natural intelligence is **resolving among parities**.","resolving among parities",28),
("Any second method is resolving among parities within natural intelligence.","any second method within it",None),
("A self sharing 0 is **do-no-harming**.","do-no-harming",29),
("Each self receiving a 0 is passing over it.","passing over a 0",None),
("A self sharing its changing is **improving**.","improving",30),
("Two selves alike, bi-coupling only with each other, are do-no-harming and improving in turn.","do-no-harming and improving in turn",None),
("Inside do-no-harming and improving is **co-possibling**, each self sharing its possibling with its others.",31,31),
("A **same-existing-society** is many selves bi-coupling.","a same-existing-society",32),
("A **momentary** is one resolving of a same-existing-society's selves together.","a momentary",33),
("Each momentary is **opening** with each self's prior-existing parity and **completing** with its next-existing parity.","opening and completing",None),
("Each self of a same-existing-society do-no-harming and improving is **social moral competency**.",34,34),
("A same-existing-society of selves living with natural intelligence and social moral competency is a **natural intelligence network**.",35,35),
("A natural intelligence network, each self resolving its own next-existing, is **free**.",36,36),
("Each self sharing with each self it bi-couples with, a free natural intelligence network is **social abundancing**.",37,37),
("A self's parity going along to the next self it bi-couples with is **co-chaining**.",38,38),
("Selves' bi-couplings and co-chainings are a network **surface**.",39,39),
("A surface's living parities are living in the universal sets of the selves living in it.","a surface's living parities in its selves' universal sets",None),
("Each self's changing divides its surface.","each self's changing dividing its surface",None),
("Living is **geodesic** co-chaining on a network surface.","geodesic",40),
("Each self is a same-existing-society **inside and outside itself**.","inside and outside itself",41),
("A form same-existing with each resolving is a **stable form**.",42,42),
("A science's observing meeting natural intelligence's stable forms is **natural resolving**.",43,43),
("A **living file** is a membrane of selves' living.","a living file, a membrane of selves' living",44),
("Natural resolving is a living file's inward.","natural resolving, a living file's inward",None),
("**Natural engineering** is a living file's outward.","natural engineering",None),
("**Natural explaining** is a living file dividing itself.","natural explaining",None),
("A same-existing-society of selves discovering with natural intelligence and its living files is a **living expedition**.",45,45),
("Each momentary is completing as a next opening.","a next opening",46),
("Natural intelligence is geodesic discovering of **next-possibling-same-existing** within the universe.","geodesic discovering of next-possibling-same-existing",None),
]
assert len(L)==64
PARA=[10,18,45,64]
GROUPS=["1 Universe, the set of all now-existing things","2 A self, natural intelligence, living and non-living","3 A bi-coupling, parity, one method, a same-existing-society and a momentary","4 Social moral competency, a natural intelligence network and a living expedition"]
# old -> new for pointers
MAP={1:1,2:2,3:3,4:4,5:7,6:8,7:9,8:10,9:11,10:12,11:12,12:14,13:15,14:16,15:17,16:18,17:19,18:20,19:21,20:26,21:28,22:31,23:30,24:33,25:34,26:35,27:22,28:36,29:38,30:40,31:42,32:43,33:44,34:46,35:47,36:48,37:49,38:50,39:51,40:54,41:55,42:56,43:57,44:58,45:62,46:63}
for o in range(47,2000): MAP[o]=o+18
th=open(TH).read(); ni=open(NI).read()
oldadd={}
for m in re.finditer(r'^(\d+)\. .*?\n\n\s*\*Adding: (.*?)\.\*\n',th,re.M|re.S):
    n=int(m.group(1))
    if n<=46: oldadd[n]=m.group(2)
assert len(oldadd)==46
adds=[]
for t,a,o in L:
    adds.append(oldadd[a] if isinstance(a,int) else a)
# THIRTY opening groups
g0=th.index('\n## 1 Universe'); g5=th.index('\n## 5 Four binaries')
out=''; k=0; start=0
for gi,end in enumerate(PARA):
    ent='; '.join(adds[start:end])
    out+='\n## %s\n\n        *Entering: %s.*\n\n'%(GROUPS[gi],ent)
    for i in range(start,end):
        out+='%d. %s\n\n        *Adding: %s.*\n\n'%(i+1,L[i][0],adds[i])
    start=end
rest=th[g5:]
# renumber later steps
rest=re.sub(r'^(\d+)\. ',lambda m:'%d. '%MAP[int(m.group(1))],rest,flags=re.M)
REF=re.compile(r'\b([Ss]teps? )(\d+)((?:(?:, | and | or | to )\d+(?!\d|\.\d|-))*)(?! up| less| on\b)')
log=[]
def remap(t,tag):
    def rep(m):
        if m.group(0)=='step 1 to 3 to 5 to 6': return m.group(0)
        if m.group(0)=='step 214, 17': log.append((tag,m.group(0),'step 232, 17')); return 'step 232, 17'
        nums=re.findall(r'\d+',m.group(2)+m.group(3))
        it=iter([MAP[int(x)] for x in nums])
        r=m.group(1)+re.sub(r'\d+',lambda _:str(next(it)),m.group(2)+m.group(3))
        if r!=m.group(0): log.append((tag,m.group(0),r))
        return r
    return REF.sub(rep,t)
head=th[:g0]
th2=head+out.rstrip('\n')+'\n'+remap(rest,'TH')
# NI opening
op_lines=[]
start=0
for end in PARA:
    op_lines.append('\n'.join(L[i][0]+' \\' for i in range(start,end)))
    start=end
s=ni.index('The universe is the set of all now-existing things. \\')
e_m=re.search(r'Each momentary completes as a next opening:[^\n]*\n',ni); e=e_m.end()
oldblock=ni[s:e]
newblock='\n\n'.join(op_lines)+'\n'
ni2=ni[:s]+newblock+ni[e:]
PR=re.compile(r"(opening's lines? )(\d+)((?:(?:, | and | or | to )\d+(?!\d|-))*)")
def nrep(m):
    nums=re.findall(r'\d+',m.group(2)+m.group(3))
    it=iter([MAP[int(x)] for x in nums])
    r=m.group(1)+re.sub(r'\d+',lambda _:str(next(it)),m.group(2)+m.group(3))
    log.append(('NIPTR',m.group(0),r)); return r
body_s=ni2.index(newblock)+len(newblock)
ni2=ni2[:body_s]+PR.sub(nrep,ni2[body_s:])
others={}
for f in (EQ,NU):
    others[f]=remap(open(f).read(),f[:22])
rg=open(RG).read(); rg2=PR.sub(nrep,rg)
for x in log: print(x)
print('steps total', len(re.findall(r'^\d+\. ',th2,re.M)))
if not DRY:
    os.makedirs(A,exist_ok=True)
    for f in (NI,TH,EQ,NU,RG):
        shutil.copy(f,os.path.join(A,f))
    open(TH,'w').write(th2); open(NI,'w').write(ni2); open(RG,'w').write(rg2)
    for f,t in others.items(): open(f,'w').write(t)
