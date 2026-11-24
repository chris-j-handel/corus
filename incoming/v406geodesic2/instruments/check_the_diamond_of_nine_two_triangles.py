"""v406geodesic2 · the check of the nineteenth drawing: a diamond of nine, two triangles one into the other.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/check_the_diamond_of_nine_two_triangles.py .

A partner's saying of 23 November is the drawing's ground, as said in the transcripts, pared. Re-said: the figure is a diamond and no
triangle; two triangles are counter-turning into one another, parities and priors one for an other, and it says the triangles' arc one way
and their arc the other way; the even rows are 2, 4 and under it 6, 8; the odd are 1, then 3, 5, 7, then 9.
All or none, both ways: the eighteenth drawing's rows of one, two, three and four, and the diamond's rows, of a partner's one order.
Whole numbers alone. It opens no file and writes none. All or none: with one line not is, the check is not.
"""
import sys
results = []
def line(name, ok): results.append((name, bool(ok)))
TEN = [0, 1, 2, 4, 3, 5, 7, 6, 8, 9]
DIAMOND = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
grid = {(a, b): a + 3 * b for a in (1, 2, 3) for b in (0, 1, 2)}      # the three by three of 1 to 9: a step of 1 one way, a step of 3 the other
line("a partner's order after its 0 is the diamond row by row: 1; 2, 4; 3, 5, 7; 6, 8; and 9, rows of one, two, three, two and one, nine in all, and 0 in no row of it",
     [d for r in DIAMOND for d in r] == TEN[1:] and [len(r) for r in DIAMOND] == [1, 2, 3, 2, 1] and all(0 not in r for r in DIAMOND))
line("the diamond is the three by three of 1 to 9 turned: a row is the numbers of one number of steps, and its arcs are 1, 2, 3; 4, 5, 6; 7, 8, 9 one way, a step of 1, and 1, 4, 7; 2, 5, 8; 3, 6, 9 the other, a step of 3",
     all(sorted(n for (a, b), n in grid.items() if (a - 1) + b == r) == sorted(DIAMOND[r]) for r in range(5))
     and [[grid[(a, b)] for a in (1, 2, 3)] for b in (0, 1, 2)] == [[1, 2, 3], [4, 5, 6], [7, 8, 9]] and [[grid[(a, b)] for b in (0, 1, 2)] for a in (1, 2, 3)] == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
line("1 by 3 and 2 by 3: the arc of 3 goes on by none, by 1 by 3 and by 2 by 3, and 3 with 2 by 3 is 9, three by three",
     all(grid[(a, b)] == a + b * 3 for a in (1, 2, 3) for b in (0, 1, 2)) and 3 + 2 * 3 == 9 == 3 * 3)
line("a row is odd or even all through, and the rows are odd and even in turn: the odd 1, then 3, 5, 7, then 9; the even 2, 4 and under it 6, 8",
     [len({d % 2 for d in r}) for r in DIAMOND] == [1] * 5 and [r[0] % 2 for r in DIAMOND] == [1, 0, 1, 0, 1])
upper, lower = DIAMOND[:3], DIAMOND[2:]
turn = lambda n: 10 - n                                               # the podaling about 5, the diamond's middle
line("two triangles, one into the other at the row 3, 5, 7: the upper of 1; 2, 4; 3, 5, 7 and the lower of 3, 5, 7; 6, 8; 9, six and six with three of both, nine",
     sum(map(len, upper)) == 6 == sum(map(len, lower)) and upper[2] == lower[0] and 6 + 6 - 3 == 9)
line("the podaling about 5, the middle, carries the upper triangle to the lower, a row to a row, and an arc to an arc gone the other way: 1, 2, 3 to 9, 8, 7 and 1, 4, 7 to 9, 6, 3",
     [sorted(turn(d) for d in r) for r in DIAMOND] == [sorted(r) for r in reversed(DIAMOND)] and [turn(d) for d in (1, 2, 3)] == [9, 8, 7] and [turn(d) for d in (1, 4, 7)] == [9, 6, 3] and turn(5) == 5)
line("with it all and other-than are one for the other, and the arcs go the other way: a multiple of 3 is with a number other-than one, 3 with 7, 6 with 4 and 9 with 1; odd and even are as they are",
     all((d % 3 == 0) != (turn(d) % 3 == 0) for d in (3, 6, 9, 1, 4, 7)) and all(turn(d) % 2 == d % 2 for d in range(1, 10))
     and all({(a, b) for (a, b), n in grid.items() if n == turn(grid[(a0, b0)])} == {(4 - a0, 2 - b0)} for a0 in (1, 2, 3) for b0 in (0, 1, 2)))
wide = lambda n: (n % 60) if (n % 60) <= 30 else 60 - (n % 60)
line("a pair of cones observed across is this diamond: at 0, 15, 30, 45 and 60 its width is none, 15, 30, 15 and none, and a row's numbers are one more than its width in fifteens",
     [1 + wide(n) // 15 for n in (0, 15, 30, 45, 60)] == [len(r) for r in DIAMOND])
name = lambda d: "a" if d % 3 == 0 else "o"
line("both ways of the one order: in rows of one, two, three and four it says the eighteenth drawing's four words, a row odd and even among one another; in the diamond's rows a row is odd or even all through",
     ["".join(name(d) for d in r) for r in (TEN[0:1], TEN[1:3], TEN[3:6], TEN[6:10])] == ["a", "oo", "oao", "oaoa"] and len({d % 2 for d in TEN[3:6]}) == 2)
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the check is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
