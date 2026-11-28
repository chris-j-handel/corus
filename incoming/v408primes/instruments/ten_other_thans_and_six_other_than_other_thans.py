# v408primes · for v408 illustrating: 10 other-thans as stable prime forming, 6 other-than-other-thans geodesically
# locating the prime surface crossings, on natural torusing. Whole numbers alone. Writes the places for drawing.
# Execute: python3 -I ten_other_thans_and_six_other_than_other_thans.py [--write out_dir]   (the set's root as argument writes nothing)
import sys, csv, os
from math import isqrt, gcd

def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

# 1. The six: the loop of 6, the torus of 2 and 3. Every number sits at one of its six places; the crossings of 2 and 3
#    take 0, 2, 3 and 4, and every prime past 3 sits at 1 or 5.
say("round 6, the torus of 2 and 3, the crossings take 0, 2, 3, 4 and every prime past 3 sits at 1 or 5, to 100,000",
    all(p % 6 in (1, 5) for p in range(5, 100000) if is_prime(p)) and sorted({n % 6 for n in range(100) if n % 2 == 0 or n % 3 == 0}) == [0, 2, 3, 4])

# 2. The six as three by two: three pairs of moments, in sequence two of them, are the torus of 3 and 2.
pairs = ["self", "other", "all"]
seqs = [(a, b) for a in pairs for b in pairs if a != b]
say("two of three pairs of moments in sequence are six, laid three by two: %s" % seqs,
    len(seqs) == 6 and len({(pairs.index(a), sorted(set(range(3)) - {pairs.index(a)}).index(pairs.index(b))) for a, b in seqs}) == 6)

# 3. The ten: the loop of 10, the torus of 2 and 5. The crossings of 2 and 5 take 0, 2, 4, 5, 6, 8, and every prime past 5
#    sits at 1, 3, 7 or 9.
say("round 10, the torus of 2 and 5, every prime past 5 sits at 1, 3, 7 or 9, to 100,000",
    all(p % 10 in (1, 3, 7, 9) for p in range(7, 100000) if is_prime(p)))

# 4. The six and the ten together locate every number round 30 by its two places, and the primes past 5 sit only where the
#    six's places 1 and 5 and the ten's places 1, 3, 7 and 9 are together: the eight skeleton places.
locate = {}
for n in range(30):
    locate.setdefault((n % 6, n % 10), []).append(n)
together = sorted(n for n in range(30) if n % 6 in (1, 5) and n % 10 in (1, 3, 7, 9))
say("the six and the ten locate every number round 30 by its two places, one number a pair; the primes' places are where both are uncrossed: %s" % together,
    all(len(v) == 1 for v in locate.values()) and len(locate) == 30 and together == [1, 7, 11, 13, 17, 19, 23, 29])

# 5. On the torus of 6 and 10, the +1 is a twisted loop through 30 of its 60 places, five times round the six and three
#    times round the ten, closing at 30.
cells, x, y, steps = set(), 0, 0, 0
while True:
    cells.add((x, y)); steps += 1
    x, y = (x + 1) % 6, (y + 1) % 10
    if (x, y) == (0, 0):
        break
say("on the torus of 6 and 10, the +1 winds a twisted loop through %d of its 60 places, %d times round the six and %d round the ten" % (len(cells), steps // 6, steps // 10),
    len(cells) == 30 and steps == 30)

# 6. The ten primes of the turn of 30 are 3 + 6 + 1: 2, 3, 5, the turn's three directions; 7 with 23, 11 with 19, 13 with 17,
#    three podal pairs about 15; and 29, the turn less 1, the podal of the me.
ten = [p for p in range(30) if is_prime(p)]
say("the primes of the turn of 30 are ten: %s: 2, 3, 5 its three directions; 7 + 23, 11 + 19, 13 + 17, three podal pairs making 30; and 29, 30 less 1" % ten,
    len(ten) == 10 and ten[:3] == [2, 3, 5] and [(a, 30 - a) for a in (7, 11, 13)] == [(7, 23), (11, 19), (13, 17)] and ten[-1] == 29)

# 7. The form is the turn of 30's own: round 210, the turn less 1, 209, is 11 x 19, crossed.
say("the 3 + 6 + 1 is the turn of 30's own: round 210 the turn less 1 is 209 = 11 x 19, crossed", 209 == 11 * 19)

# 8. On natural torusing, the small direction 24 is 4 by 6 and the large 60 is 6 by 10 by 2 round the six's 2: round 60 the
#    sixteen skeleton places sit where the six's 1, 5 and the ten's 1, 3, 7, 9 are together.
sixteen = sorted(n for n in range(60) if n % 6 in (1, 5) and n % 10 in (1, 3, 7, 9))
say("round 60, the large direction, the sixteen skeleton places are where the six's and the ten's uncrossed places are together: %s" % sixteen,
    sixteen == [n for n in range(60) if gcd(n, 60) == 1])

# Places for drawing: the torus of 6 and 10, a row a place of the +1's loop.
out = sys.argv[sys.argv.index("--write") + 1] if "--write" in sys.argv[:-1] else None   # the set's root as argument writes nothing
if out:
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "the_six_and_the_ten_round_30.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n round 30", "place round 6", "place round 10", "uncrossed by 2, 3 and 5", "a prime below 30", "podal round 30"])
        for n in range(30):
            w.writerow([n, n % 6, n % 10, "yes" if n % 6 in (1, 5) and n % 10 in (1, 3, 7, 9) else "", "yes" if is_prime(n) else "", (30 - n) % 30])
    print("        places for drawing written to", os.path.join(out, "the_six_and_the_ten_round_30.csv"))

print("All is." if all(results) else "A line is-not.")
