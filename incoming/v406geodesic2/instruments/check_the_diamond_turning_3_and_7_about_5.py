"""v406geodesic2 · the check of the twentieth drawing: the diamond turning, 3 and 7 the right spiral steps about 5.

Usage, from the repository's root (some seconds, with the numbers to 10,000,000 gone through):
  python3 -I incoming/v406geodesic2/instruments/check_the_diamond_turning_3_and_7_about_5.py .

A partner's saying of 23 November is the drawing's ground, as said in the transcripts, pared. Re-said: among the primes' hard
problems is one of primes ending in 3 and 7, not yet understood; the diamond is the living method with it no hard problem; 3 and 7
are right spiral around the 5, the bi-inversioning with the co-recursioning along 1, 5, 9; 2, 4 is prior parity and 6, 8 is now
parity; 4, 8 is a same-existing bi-coupling; the parities are bi-coupling, bothbothing the now moments one after an other; and all
of the primes is podaling to and from the order 0124537689.
The hard problem is v406Reiman's sentence 16 and v407primes' sentence 46, a field's asking of 1980: a number of no prime, ending in
3 or 7, with both closings, doubling's one short of it and prior two added's one past it.
All or none, both ways. Whole numbers alone. It opens no file and writes none. All or none: with one line not is, the check is not.
"""
import sys
results = []
def line(name, ok): results.append((name, bool(ok)))

# ---- the diamond: the three by three of 1 to 9 about its middle, 5; a number is 5 with x and with three ys, x and y of -1, 0, 1
PAIRS = [(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1)]
by3 = {(x, y): 5 + x + 3 * y for (x, y) in PAIRS}                     # laid by threes
by7 = {(x, y): (5 + x + 7 * y) % 10 for (x, y) in PAIRS}              # laid by sevens, its mirror
seat = {n: (y - x, x + y) for (x, y), n in by3.items()}               # a number's place in the drawing: across, and down
DIAMOND = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
line("the diamond's rows are the three by three about 5: a number is 5 with x and with three ys, and a row is the numbers of one x with y",
     sorted(by3.values()) == list(range(1, 10)) and all(sorted(n for n in seat if seat[n][1] == r - 2) == DIAMOND[r] for r in range(5)))
quarter = lambda c: (-c[1], c[0])                                      # a quarter turn of the drawing about its middle
line("a quarter turn of the diamond about its 5 is multiplying by 7 round ten, all nine, a place to a place; the other way it is multiplying by 3; and 5 is at its place with both",
     all(seat[n * 7 % 10] == quarter(seat[n]) for n in seat) and all(quarter(seat[n * 3 % 10]) == seat[n] for n in seat) and 5 * 7 % 10 == 5 == 5 * 3 % 10)
line("the living right spiral step, a pair (x, y) to (y, -x): laid by threes it is multiplying by 7, and laid by sevens, the mirror, it is multiplying by 3: 3 and 7, both, a mirror between them",
     all(by3[(y, -x)] == by3[(x, y)] * 7 % 10 for (x, y) in PAIRS) and all(by7[(y, -x)] == by7[(x, y)] * 3 % 10 for (x, y) in PAIRS)
     and all(by7[(x, y)] == by3[(x, -y)] for (x, y) in PAIRS) and sorted(by7.values()) == list(range(1, 10)))
podal = lambda n: 10 - n                                               # the podaling about 5
line("two right spiral steps, by 7 or by 3, are multiplying by 9, one short of ten: the podaling about 5, both of a pair inverting; four reach the number again; and one by 7 with one by 3 is no step",
     all(n * 7 * 7 % 10 == podal(n) == n * 3 * 3 % 10 == n * 9 % 10 for n in seat) and all(n * 7 ** 4 % 10 == n == n * 3 ** 4 % 10 == n * 7 * 3 % 10 for n in seat)
     and all(by3[(-x, -y)] == podal(by3[(x, y)]) for (x, y) in PAIRS))
round7 = lambda n: [n * 7 ** k % 10 for k in range(4)]
line("the corners go round, 1, 7, 9, 3, and the four between them, 2, 4, 8, 6, the same way round: two rounds about the 5, and a number is in one round or is the 5",
     round7(1) == [1, 7, 9, 3] and round7(2) == [2, 4, 8, 6] and sorted(round7(1) + round7(2) + [5]) == list(range(1, 10)))
along = lambda n: by3[tuple(reversed(next(p for p in PAIRS if by3[p] == n)))]                      # a fold along 1, 5, 9: the pair's two, one for the other
across = lambda n: by3[tuple(-v for v in reversed(next(p for p in PAIRS if by3[p] == n)))]         # a fold along 3, 5, 7
line("two folds: along 1, 5, 9, with 3 for 7, 2 for 4 and 6 for 8; and along 3, 5, 7, with 1 for 9, 2 for 6 and 4 for 8; one and then the other, in both orders, is the podaling about 5",
     [along(n) for n in range(1, 10)] == [1, 4, 7, 2, 5, 8, 3, 6, 9] and [across(n) for n in range(1, 10)] == [9, 6, 3, 8, 5, 2, 7, 4, 1]
     and all(along(across(n)) == podal(n) == across(along(n)) for n in range(1, 10)))
line("a number by its own, round ten: the odd come to 1, 9, 5, 9, 1, the line 1, 5, 9, with 3 and 7 both at 9; a right spiral step by its own again and again goes 7, 9, 3, 1, on the line at its second and its fourth",
     [n * n % 10 for n in (1, 3, 5, 7, 9)] == [1, 9, 5, 9, 1] and [7 ** k % 10 for k in (1, 2, 3, 4)] == [7, 9, 3, 1] and [3 ** k % 10 for k in (1, 2, 3, 4)] == [3, 9, 7, 1])
line("2, 4 and 6, 8: one short and one past of 3, and of 7; the one shorts, 2 and 6, are one over an other in the diamond, and the one pasts, 4 and 8, are: a step of 4 down, as 1, 5, 9 is",
     (3 - 1, 3 + 1) == (2, 4) and (7 - 1, 7 + 1) == (6, 8) and seat[2][0] == seat[6][0] and seat[4][0] == seat[8][0] and seat[1][0] == seat[5][0] == seat[9][0]
     and (6 - 2, 8 - 4, 5 - 1, 9 - 5) == (4, 4, 4, 4))
four_ways = [seat[4][0] == seat[8][0], 4 + 4 == 8, (3 + 1, 7 + 1) == (4, 8), podal(4) == 8]
line("4 and 8, four ways: one over an other in the diamond, is; 4 with 4 is 8 with no ten passed, is; one past of 3 and of 7, is; a podal pair about 5, is not, 4's is 6: three are and one is not",
     four_ways == [True, True, True, False] and podal(4) == 6)
doubling = [1]
while len(doubling) < 9: doubling.append(doubling[-1] * 2 % 10)
line("doubling, a number with its own, round ten: 1, then 2, 4, 8, 6 round and round, the way a right spiral step by 7 goes: across 2, 4, down 4, 8, across 8, 6 and up 6, 2",
     doubling == [1, 2, 4, 8, 6, 2, 4, 8, 6] and all(n * 2 % 10 == n * 7 % 10 for n in (2, 4, 6, 8)))

# ---- prior two added, round ten: phi's pair step, (x, y) to (y, x + y)
walk = [(0, 1)]
while True:
    x, y = walk[-1]; nxt = (y, (x + y) % 10)
    if nxt == (0, 1): break
    walk.append(nxt)
ends = [p[0] for p in walk]
line("prior two added, round ten, reaches its pair again with 60 moments and no fewer; its 0s are at 0, 15, 30 and 45 and no other moment, the diamond's rows as a pair of cones observed across, with 60",
     len(walk) == 60 and [k for k, e in enumerate(ends) if e == 0] == [0, 15, 30, 45])
line("fifteen moments on, all its pairs are multiplied by 7, one right spiral step of the diamond: beside its 0s are 1, 7, 9, 3; thirty on, a cone on, a number is its podal about 5",
     all(walk[(k + 15) % 60] == (walk[k][0] * 7 % 10, walk[k][1] * 7 % 10) for k in range(60)) and [walk[k][1] for k in (0, 15, 30, 45)] == [1, 7, 9, 3]
     and all(ends[(k + 30) % 60] == (10 - ends[k]) % 10 for k in range(60)))

# ---- the same square round its next: 4 round 5, 9 round 10, 16 round 17, and 256 and 65,536
def square_turns(k):
    N = k * k + 1
    grid = {(a, b): a + k * b for a in range(1, k + 1) for b in range(k)}
    return (sorted(grid.values()) == list(range(1, N)) and all(grid[(k - b, a - 1)] == n * k % N for (a, b), n in grid.items())
            and all(grid[(b + 1, k - a)] == n * (N - k) % N for (a, b), n in grid.items()) and all(n * k * k % N == N - n for n in grid.values()))
line("the same turn, a square in a square: 1 to 4 round 5, 1 to 9 round 10, 1 to 16 round 17, 1 to 256 round 257 and 1 to 65,536 round 65,537; a quarter turn is multiplying by the side, and two are the podaling, the next number less",
     all(square_turns(k) for k in (2, 3, 4, 16, 256)) and 17 - 1 == 16)

# ---- both ways of the one order
ONE_ORDER, OTHER_ORDER = [0, 1, 2, 4, 3, 5, 7, 6, 8, 9], [0, 1, 2, 4, 5, 3, 7, 6, 8, 9]
cut = lambda o: [sorted(o[1:2]), sorted(o[2:4]), sorted(o[4:7]), sorted(o[7:9]), sorted(o[9:10])]
line("both ways of the one order, 0124357689 and 0124537689: the same rows of the diamond, with 3, 5, 7 or 5, 3, 7; the podaling about 5 carries the one to its own order gone the other way, and the other to its own row by row alone",
     cut(ONE_ORDER) == cut(OTHER_ORDER) == DIAMOND and [podal(n) for n in ONE_ORDER[1:]] == ONE_ORDER[:0:-1] and [podal(n) for n in OTHER_ORDER[1:]] != OTHER_ORDER[:0:-1]
     and [sorted(podal(n) for n in r) for r in cut(OTHER_ORDER)] == cut(OTHER_ORDER)[::-1])

# ---- the primes
TOP = 10_000_000
sieve = bytearray([1]) * (TOP + 1); sieve[0:2] = b"\x00\x00"
for i in range(2, int(TOP ** 0.5) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(range(i * i, TOP + 1, i)))
at_end = {e: sum(sieve[e::10]) for e in range(10)}
line(f"a prime past 5, to 10,000,000, ends at a corner of the diamond, 1, 3, 7 or 9, all {sum(at_end[e] for e in (1, 3, 7, 9)) - 1:,} of them; 2 and 5 alone end at 2 and at 5, and none at 0, 4, 6 or 8",
     at_end[2] == 1 == at_end[5] and at_end[0] == at_end[4] == at_end[6] == at_end[8] == 0 and sum(at_end.values()) == sum(sieve) == 664_579)
turns_of = {1: 0, 7: 1, 9: 2, 3: 3}                                   # an ending's right spiral steps, laid by threes
line("multiplying by a prime turns the diamond, all nine: ending in 1 no step, in 7 one right spiral step, in 9 two, the podaling about 5, and in 3 three; by its own it ends at 1 or 9, on the line 1, 5, 9",
     all(all(n * e % 10 == n * 7 ** t % 10 for n in range(1, 10)) for e, t in turns_of.items()) and all(e * e % 10 in (1, 9) for e in turns_of)
     and all((p * p) % 10 in (1, 9) for p in range(7, 100_000) if sieve[p]))
def prior_two_added(k, n):                                             # the pair after k steps of (x, y) to (y, x + y) from (0, 1), round n
    a, b = 0, 1
    for bit in bin(k)[2:]:
        a, b = a * (2 * b - a) % n, (a * a + b * b) % n
        if bit == "1": a, b = b, (a + b) % n
    return a, b
doubling_closes = lambda n: pow(2, n - 1, n) == 1                      # doubling, round n, reaches 1 with one short of n
adding_closes = lambda n: prior_two_added(n + 1, n)[0] == 0            # prior two added, round n, reaches its 0 with one past n
MILLION = 1_000_000
both = d_alone = a_alone = primes_with_both = primes_here = 0
for n in range(3, MILLION, 2):
    if n % 10 not in (3, 7): continue
    d, a = doubling_closes(n), adding_closes(n)
    if sieve[n]:
        primes_here += 1; primes_with_both += d and a
    else:
        both += d and a; d_alone += d and not a; a_alone += a and not d
line(f"of the odd numbers ending in 3 or 7, to 1,000,000, all gone through: the {primes_here:,} primes have both closings, doubling's one short and prior two added's one past; of the numbers of no prime, {d_alone} have doubling's alone, {a_alone} the adding's alone, and none has both",
     primes_with_both == primes_here and both == 0 and d_alone > 0 and a_alone > 0)
primes_far = with_both_far = d_far = both_far = 0
for n in range(3, TOP, 2):
    if n % 10 not in (3, 7): continue
    if sieve[n]:
        primes_far += 1; with_both_far += doubling_closes(n) and adding_closes(n)
    elif doubling_closes(n):
        d_far += 1; both_far += adding_closes(n)
line(f"to 10,000,000, doubling's closing gone through with all: the {primes_far:,} primes ending in 3 or 7 have both; {d_far} numbers of no prime have doubling's, and none of them the adding's: is as far as gone through, and no farther by this",
     with_both_far == primes_far and both_far == 0 and d_far > 0)
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
