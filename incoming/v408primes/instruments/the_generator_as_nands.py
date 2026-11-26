# v408primes · the prime generator as a fractal set of nands: a loop gives a crossing bit, and all the logic is one gate,
# nand. The 1 to 17 block of gates finds the skeleton round 510,510; the same block, again at the primes past 17, aimed
# from their own me agains, finds all the me-parities. Whole numbers and one gate.
# Execute: python3 -I the_generator_as_nands.py
from math import isqrt

gates = 0
def nand(a, b):
    global gates
    gates += 1
    return 1 - (a & b)
def other_than(a):                 # one inversion: a nand with itself
    return nand(a, a)
def both(a, b):                    # both: the other-than of their nand
    return other_than(nand(a, b))

def crossed(n, p):                 # the loop of p lands on n: one bit
    return 1 if n % p == 0 else 0

def uncrossed_by_all(n, loops):    # the nand of all crossings: uncrossed by all the loops given
    bit = 1
    for p in loops:
        bit = both(bit, other_than(crossed(n, p)))
    return bit

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

FRACTAL = [2, 3, 5, 7, 11, 13, 17]
SEAM = 510510
gates = 0
skeleton = [r for r in range(1, SEAM + 1) if uncrossed_by_all(r, FRACTAL)]
per_place = gates // SEAM
say("the 1 to 17 block, %d nands a place, finds the skeleton round 510,510: %s living places" % (per_place, f"{len(skeleton):,}"),
    len(skeleton) == 92160 and per_place == 3 * len(FRACTAL))

# The same block again, at the primes past 17, each aimed from its own me again: a place past 17 on the skeleton is a
# me-parity at the nand of the crossings of the me-parities whose me again it has reached.
N = 200000
found = list(FRACTAL)
aimed = []                          # me-parities past 17 whose loops are aimed: their me again reached
nxt = 0                             # the next me-parity past 17 to aim
k = 0
while True:
    c = (k // len(skeleton)) * SEAM + skeleton[k % len(skeleton)]
    k += 1
    if c == 1:
        continue
    if c > N:
        break
    while nxt < len(found) and found[nxt] > 17 and found[nxt] * found[nxt] <= c:
        aimed.append(found[nxt]); nxt += 1
    while nxt < len(found) and found[nxt] <= 17:
        nxt += 1
    if uncrossed_by_all(c, aimed):
        found.append(c)

full = [n for n in range(2, N + 1) if all(n % q for q in range(2, isqrt(n) + 1))]
say("the same block again at the me-parities past 17, aimed from their own me agains, generates all %s me-parities to %s"
    % (f"{len(found):,}", f"{N:,}"), found == full)
say("one gate alone, nand: other-than is a nand with itself, both is the other-than of a nand", other_than(0) == 1 and other_than(1) == 0 and both(1, 1) == 1 and both(1, 0) == 0)
print("All is." if all(results) else "A line is-not.")
