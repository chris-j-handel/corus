# v408primes · DNA as stable form inherited, RNA as living form, beside this session's primes.
# The bases, their pairing, the reading frames and the standard genetic code, run with whole numbers and letters.
# Execute: python3 -I dna_and_rna_beside_the_primes.py
import random
from itertools import product

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

PAIR = {"A": "U", "U": "A", "G": "C", "C": "G"}
def other(s):            # the pairing strand, read its own way
    return "".join(PAIR[b] for b in reversed(s))

# 1. Pairing is an other-than, and pairing twice is a me again: a strand's other-than's other-than is the strand.
random.seed(408)
strands = ["".join(random.choice("AUGC") for _ in range(random.randint(1, 300))) for _ in range(20000)]
say("a strand's pairing strand's pairing strand is the strand again, 20,000 strands", all(other(other(s)) == s for s in strands))

# 2. A base is located by three parity pairs, two free: purine or pyrimidine, strong or weak, amino or keto.
R = {"A": 1, "G": 1, "C": 0, "U": 0}     # purine
S = {"G": 1, "C": 1, "A": 0, "U": 0}     # strong, three bonds
M = {"A": 1, "C": 1, "G": 0, "U": 0}     # amino
say("every base is one place of the three parity pairs, the third their otherness",
    all(M[b] == (1 if R[b] != S[b] else 0) for b in "AUGC") and len({(R[b], S[b]) for b in "AUGC"}) == 4)

# 3. The three inversions of the bases each invert two of the three parities and hold one.
pairing = PAIR
transition = {"A": "G", "G": "A", "C": "U", "U": "C"}
rumer = {"U": "G", "G": "U", "C": "A", "A": "C"}
def held(f):
    return [name for name, P in (("purine", R), ("strong", S), ("amino", M)) if all(P[b] == P[f[b]] for b in "AUGC")]
say("the three inversions of the bases hold one parity apiece and invert two: pairing holds %s, transition %s, the third %s"
    % (held(pairing), held(transition), held(rumer)), (held(pairing), held(transition), held(rumer)) == (["strong"], ["purine"], ["amino"]))

# 4. The reading frame is the loop of 3, a prime length; two strands by three frames are six, the torus of 2 and 3.
say("two strands by three frames are six reading frames, the torus of 2 and 3: the +1 winds through all six",
    len({(n % 2, n % 3) for n in range(6)}) == 6)

# 5. The standard code: 64 codons, 4 by 4 by 4, a cube of 4.
CODE = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
B = "UCAG"
code = {a + b + c: CODE[16 * B.index(a) + 4 * B.index(b) + B.index(c)] for a, b, c in product(B, B, B)}
say("the code is 64 codons, a cube of 4, to %d amino acids and the stop" % (len(set(code.values())) - 1),
    len(code) == 64 and len(set(code.values())) == 21)

# 6. A codon fractures into its box, its two leading bases, and its third, a parity: U and C at the third are alike
#    in all 16 boxes; all four thirds are alike in 8 boxes, the third's parity exhausted; in 8 the third's parity lives.
boxes = ["".join(p) for p in product(B, B)]
uc_alike = all(code[x + "U"] == code[x + "C"] for x in boxes)
exhausted = [x for x in boxes if len({code[x + c] for c in B}) == 1]
living = [x for x in boxes if x not in exhausted]
say("a codon's third: U and C alike in all 16 boxes; the third's parity exhausted in 8 boxes %s and living in 8 %s" % (exhausted, living),
    uc_alike and len(exhausted) == 8)

# 7. Strong boxes exhaust the third, weak boxes keep it living, and in a mixed box the second base decides.
def strength(x):
    return S[x[0]] + S[x[1]]
ok = all((x in exhausted) == (strength(x) == 2 or (strength(x) == 1 and R[x[1]] == 0)) for x in boxes)
say("both leading bases strong, the third exhausted; both weak, the third living; one of each, exhausted when the second is a pyrimidine", ok)

# 8. A bi-folding of the code: the third inversion, held amino, laid on a box's two leading bases, carries the 8 boxes
#    with the third exhausted onto the 8 with it living, and back.
image = sorted(rumer[x[0]] + rumer[x[1]] for x in exhausted)
say("the inversion holding amino, on the two leading bases, carries the 8 exhausted boxes onto the 8 living ones: %s" % image,
    image == sorted(living))

# 9. A hairpin is a strand folding onto its own pairing: position i pairs with position n + 1 - i, podal about its loop.
hp = "GGCAUCGAAAGAUGCC"
stem = 6
say("a hairpin %s pairs its places podal about its loop: i with n + 1 - i, %d pairs" % (hp, stem),
    all(PAIR[hp[i]] == hp[len(hp) - 1 - i] for i in range(stem)))

# 10. Counts alike, forms not shown: codons with a given base are 4 cubed less 3 cubed, 37; sense codons are 61,
#     and 5 cubed less 4 cubed is 61, while 61 sense codons are the cube of 4 less 3 stops.
with_u = sum(1 for c in code if "U" in c)
sense = sum(1 for v in code.values() if v != "*")
say("codons with a U are %d, 4 cubed less 3 cubed; sense codons are %d, 64 less 3 stops, the same count as 5 cubed less 4 cubed" % (with_u, sense),
    with_u == 4 ** 3 - 3 ** 3 == 37 and sense == 61 == 5 ** 3 - 4 ** 3)

print("All is." if all(results) else "A line is-not.")
