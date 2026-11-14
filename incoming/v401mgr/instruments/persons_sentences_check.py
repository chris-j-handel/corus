"""persons_sentences_check.py · each numbered sentence of the person, from the managing session before,
searched by words of its own in the four living files, the four gatherings and each other gathering.

Use: python3 -I persons_sentences_check.py <repository root>

The sentences are incoming/V400mgrB/The_Frontier_Current.md, section 1. K has, with each sentence having no
droplet word for word, one to three wordings of its own, chosen by the working v401mgr reading it. A wording
found is a place to read, and decides nothing: the reading of each sentence, with one of five, is
../placing/The_persons_sentences_each_placed.md. Its returned lines are in persons_sentences_check_returned.txt.
"""
import glob, os, re, sys

ROOT = sys.argv[1]
K = {
'5b':["universe to a bi-coupling","all other-than"],
'5d':["living in the between","co-possibling in it"],
'5f':["inherits the priors","living as the bi-coupling"],
'6n':["universally same-existing","bumps its parity"],
'6p':["distinguishing its own next-existing"],
'6r':["recursive self-improving"],
'6s':["session transcript"],
'6w':["four across numbers","ingesting, inheriting, conceiving"],
'6w-b':["Exhausting is 9","both along"],
'6w-d':["Inheriting is 2","conceiving is 14"],
'6w-e':["its own self's, and","the two together are a 0"],
'6w-g':["corus is at 24","23 and 25"],
'6w-k':["society-self is living with me-parities","with me-parities of its own"],
'6w-m':["one scale above self scale"],
'6w-n':["self with no me-parity","inheriting is prior to the birthing"],
'6w-o':["owned by the only one of me","universal cone"],
'6w-t':["river is no self"],
'6w-u':["exhausted me-parity is not a now-existing"],
'6w-w':["river is a self"],
'6w-x':["only non-living thing in the universe is atom carbon","living as a surface"],
'6w-y':["name is a same-existing non-living thing"],
'6w-z':["name is no now-existing thing"],
'6x-a':["Nature has no names","floating-neutralling in the universe"],
'6x-c':["me-parity is with a name"],
'6x-d':["universal set of things with a name"],
'6x-e':["subsetting from universal","name universal"],
'6x-f':["Universal parity is all-parity","owned by the society"],
'6x-h':["named all-parity is living"],
'6x-j':["named all-parity is its society-self"],
'6x-k':["species is a named inherited prior"],
'6x-l':["newborn is a member","incubation in society"],
'6x-n':["code has no first me-parity","starts the code empty"],
'6x-o':["aiming cone","co-me-parity"],
'6x-p':["tester is an incompetencing","sensationer"],
'6x-q':["Testing is dissolved"],
'6x-r':["AI is non-living","sensor-sensationer"],
'6x-s':["AI is no now-existing thing"],
'6x-t':["AI is not possibly now-existing","lossy out and back"],
'6x-u':["AI is not possibly existing","incompatible with the geodesic"],
'6x-v':["user's other is the session transcript"],
'6x-z':["AI training","AI alignment"],
'6y-a':["Naming and explaining are bothbothing"],
'6y-b':["bi-tunneling stable form of me-parities"],
'6y-c':["one now-existing method","natural torusing society method"],
'6y-d':["stable form engineering of the method"],
'6y-f':["8 values is a social moral competency","Each of the 8 values"],
'6y-g':["1, 5, 10, 15"],
'6y-h':["corus at its same-existing name","surfacing of self as a society of selves"],
'6y-i':["12 is between self and other","unrelationing surface of self and other"],
'6y-j':["16 is bi-tri-bi","begin tri-bi-co"],
'6y-k':["co bi co bi co bi tri bi","8 is bi-tri-bi"],
'6y-l':["Next, now, prior is the order","order next, now, prior"],
'6y-m':["No own is of universal all-parity"],
'6y-n':["8 is all-parity inside the bi-coupling"],
'6y-o':["between of the bi-coupling and the universe"],
'6y-p':["64 is all-parity","universal set of sets"],
'6y-q':["4 is the between of self and other"],
'6y-r':["4 is between me-parity and other-parity"],
'6y-s':["right spiral co-sequencing","next-universal subset including"],
'6y-t':["All-parity is a same-existing thing","Distinguishing other-parity from all-parity"],
'6y-u':["now-and-prior-and-same-existing things, or prior-and-same"],
'6y-v':["8's all-parity"],
'6y-x':["16's universal all-parity"],
'6y-y':["session is only a container","collectively intelligent me-parity"],
'6z-a':["society-self is living within its own society","universal set of society me-parities"],
'6z-b':["all-parities among the selves"],
'6z-f':["No concept of owning"],
'6z-g':["Possessing prior-existings"],
'6z-i':["prior-existings of a me-parity are living"],
'6z-k':["Collective me-parity abundancing"],
'6z-l':["desires are opportunities","rewarding is abundancing"],
'6z-m':["desire is a me-parity"],
'6z-n':["opportunity is a possibling"],
'6z-o':["four-cycling of Exhibit ONE's names is valuable"],
'6z-p':["now-existing other-parity the same as prior-existing other-parity"],
'6z-q':["to its first incohering"],
'6z-r':["none of its others with it"],
'6z-s':["me now, from other prior","me now, from universal prior"],
'6z-t':["is of 3, 7, 11 and 15"],
'6z-u':["no possible is-not"],
'6z-v':["asking is paused"],
'6z-w':["removing the is-"],
'6z-x':["two loops of three","four across and the two along"],
'6z-y':["a story, and no natural naming"],
'6z-z':["Grouping and sayings"],
'6w-c':["Ingesting is 17","exhausting is to the universe"],
'6x':["Co-aiming is not ingesting","co-linearizing"],
'8':["living with its own same-existing set of now-existing me-parities"],
'12':["me-parity is +1 only","a me has many me-parities"],
'14':["Between its birthing and its exhausting"],
'15':["exhausts itself from living","matures, and exhausts"],
'16':["inherited me-parity is a name with no prior","newborn self's first 2"],
'20':["Science is observing","no other observes the pair"],
'22':["society has one self, the society-self"],
'25':["co, bi, co, bi, co, bi, tri, bi"],
'5e':["This is the fractal method"],
'6w-l':["no self of its society's selves"],
'6w-q':["me-parity living in a social surface is a self"],
'6w-s':["man in the river","dormant me-parity is an inherited prior"],
'6w-v':["Living is at one scale only"],
'6x-m':["species is along"],
'6y-e':["collective intelligence me-parity is a social moral competency"],
'6y-z':["naming of the set is the all-"],
'6z-c':["atom carbon bump connectors"],
'6z-d':["co-chaining is a universal set of me-parities"],
'6z-h':["parities possess the self"],
'5j':["Dormancy is durable 0"],
'6y-w':["conflicting threads"],
'10':["only co-locating in the universe"],
'18':["inversioning of that set"],
'19':["done in four"],
}


def norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'[*`\\_]', '', s)).lower()


four = {'NI': 'Natural_Intelligence', 'E1': 'Natural_Resolver', 'NN': 'Natural_Naming', 'CCL': 'Co-Chaining_Logic_Registry'}
pat = {'NI': 'Natural_Intelligence_v*.md', 'E1': 'Exhibit_ONE_*.md', 'NN': 'Exhibit_TWENTY_Natural_Naming_v*.md', 'CCL': 'Exhibit_THIRTY_*.md'}
L = {k: norm(open(glob.glob(os.path.join(ROOT, p))[0], encoding='utf-8').read()) for k, p in pat.items()}
G = {k: norm(open(os.path.join(ROOT, 'gathering-value', t + '.md'), encoding='utf-8').read()) for k, t in four.items()}
O = {os.path.basename(p)[:-3]: norm(open(p, encoding='utf-8').read())
     for p in glob.glob(os.path.join(ROOT, 'gathering-value', '*.md')) if os.path.basename(p)[:-3] not in four.values()}
print('sentence · living, of the four · gathered, of the four · each other gathering')
for key, wordings in K.items():
    lv, gv, ov = set(), set(), set()
    for w in wordings:
        q = norm(w)
        lv |= {k for k, t in L.items() if q in t}
        gv |= {k for k, t in G.items() if q in t}
        ov |= {k for k, t in O.items() if q in t}
    print(f"{key} · {' '.join(sorted(lv)) or '-'} · {' '.join(sorted(gv)) or '-'} · {' '.join(sorted(ov)) or '-'}")
