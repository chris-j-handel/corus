# v408primes · bi-foldings: about a between a, two co-possiblings a − b and a + b multiplied are a's me again less b's me
# again. A number is crossed when it folds so with a − b past 1; a me-parity folds so only at its far end. The quarter
# turns 90 to 450 and the numbers across from one another about them. Whole numbers and me agains, no adding along.
# Execute: python3 -I folding_across_the_quarter_turns.py
# The folding of a me-parity is seen only at its far end: to see it so, all betweens from its side to its far end are folded.
from math import isqrt

def foldings(n):                      # all (a, b): n is a's me again less b's me again, a from n's side to its far end
    out = []
    for a in range(isqrt(n), (n + 1) // 2 + 1):
        d = a * a - n
        if d >= 0 and isqrt(d) ** 2 == d:
            out.append((a, isqrt(d)))
    return out
def me_parity(n):
    return n > 1 and all(n % q for q in range(2, isqrt(n) + 1))

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

say("360 is 18 by 20, the co-possiblings of 19 multiplied: 19's me again less 1, and 361 is 19's me again, 19 by 19", 18 * 20 == 360 and 19 * 19 == 361)
say("361 folds about its between 19 with nothing between, 19 and 19; 359 folds only at its far end, 180 and 179: %s, %s" % (foldings(361), foldings(359)),
    foldings(361)[0] == (19, 0) and foldings(359) == [(180, 179)])
ok = all((len(foldings(n)) == 1) == me_parity(n) for n in range(3, 20001, 2))
say("an odd number is a me-parity when its one folding is at its far end, and crossed when it folds about a nearer between: all odd numbers to 20,000", ok)
quarters = {}
for k in range(1, 6):
    c = 90 * k
    quarters[c] = ["%d %s" % (n, "a me-parity" if me_parity(n) else "%d by %d" % (foldings(n)[0][0] - foldings(n)[0][1], foldings(n)[0][0] + foldings(n)[0][1])) for n in (c - 1, c + 1)]
say("about the quarter turns 90 to 450, across from one another: %s" % "; ".join("%d: %s" % (c, ", ".join(v)) for c, v in quarters.items()), True)
say("440 is 20 by 22, the co-possiblings of 21 multiplied, 21's me again less 1, and 439 across is a me-parity", 20 * 22 == 440 and me_parity(439))
say("seeing 359 a me-parity by folding, the betweens 18 to 180 are folded, 163 of them; by crossing, the loops 2 to 17, 7 of them", len(range(isqrt(359), 181)) == 163)
print("All is." if all(results) else "A line is-not.")
