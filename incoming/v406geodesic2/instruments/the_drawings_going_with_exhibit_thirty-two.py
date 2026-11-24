"""v406geodesic2 · the drawings going with Exhibit THIRTY-TWO Natural Prime Numbering, on its draft as it is.

Usage, from the repository's root:
  python3 -I incoming/v406geodesic2/instruments/the_drawings_going_with_exhibit_thirty-two.py \
      incoming/v407primes/Exhibit_THIRTY-TWO_Natural_Prime_Numbering_first_draft.md

The concerns of all sessions are one table, v406me's, and its row 36 is this session's: the drawings going with the draft's
opening and its 3.2 to 3.5, named, with their checks executed on the draft as it is.
It opens the draft and writes nothing. A place of the draft: its sentences a drawing lays, word for word in the draft as it is, and
their numbers executed, whole numbers alone. With a draft renewed, a sentence gone from it is said by its opening words.
All or none: with one line not is, the going through is not. The drawings' own checks are named with a place, and executed apart.
"""
import sys
from math import gcd
draft = open(sys.argv[1], encoding="utf-8").read()
results, gone = [], []
def line(name, sentences, ok):
    here = [q for q in sentences if q not in draft]
    gone.extend(here); results.append((name, bool(ok) and not here))
prime = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
primes = [n for n in range(2, 62) if prime(n)]
about = lambda st: (lambda n: 2 * st - n)

line("its opening: the twelve primes 2 to 37 in three rounds of four, closing at 7, 19 and 37, the shells 2 cubed less 1, 3 cubed less 2 cubed and 4 cubed less 3 cubed; a fourth round closing at 53; and 61, 5 cubed less 4 cubed, past it · no drawing yet, this session's next",
     ["Its three rounds are the twelve primes 2 to 37, and they close at 7, 19 and 37, the shells of a cube about its corner: 2 cubed less 1, 3 cubed less 2 cubed, and 4 cubed less 3 cubed.",
      "Its fourth round, 41, 43, 47 and 53, closes at 53, and the next shell, 61, 5 cubed less 4 cubed, is past it, a next 1."],
     primes[:12][-1] == 37 and [primes[k] for k in (3, 7, 11)] == [7, 19, 37] == [2 ** 3 - 1, 3 ** 3 - 2 ** 3, 4 ** 3 - 3 ** 3] and primes[12:16] == [41, 43, 47, 53] and 61 == 5 ** 3 - 4 ** 3 and prime(61))
shell = [(x, y, z) for x in range(4) for y in range(4) for z in range(4) if min(x, y, z) == 0]
line("its 3.2: 37 a self and three rounds of six, 1, 6, 12 and 18, 4 cubed less 3 cubed; observed along (1, 1, 1) the shell's 37 are 37 places, a hexagon, the corner its centre · the seventh drawing, check_the_rounds_of_six_at_prime_scale_37.py",
     ["**37 is a self and three rounds of six, 1, 6, 12 and 18, and 4 cubed less 3 cubed.**", "**Observed along (1, 1, 1), the shell is the hexagon of 37, the corner its centre.**"],
     len(shell) == 37 == 1 + 6 + 12 + 18 == 4 ** 3 - 3 ** 3 and len({(x - z, y - z) for x, y, z in shell}) == 37 and [sum(max(c) == k for c in shell) for k in range(4)] == [1, 6, 12, 18])
places = [n for n in range(1, 60) if gcd(n, 30) == 1]
line("its 3.3, the sixteen places of a pair of cones, the names 1 to 16, 0 its vertex and 61 a next 1; a podaling about 30 and about 90 · the tenth and the fourteenth drawings, check_a_me-now_podaling_about_30_and_about_90.py and check_a_my_the_sixteen_names_on_a_pair_of_cones.py",
     ["a pair of cones, 0 to 60, has the sixteen places no spiral of 2, 3 or 5 crosses: 1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53 and 59, the names 1 to 16, with 0 its vertex and 61 a next 1.**",
      "A podaling about 30 is n to 60 less n, same-existing; about 90, n to 180 less n, next-universing."],
     places == [1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59] and len(places) == 16 and about(30)(37) == 60 - 37 and about(90)(37) == 180 - 37 and gcd(61, 30) == 1)
me = [37]
for st in (30, 60, 90, 120): me.append(about(st)(me[-1]))
fours = [[k, 60 - k, 60 + k, 120 - k] for k in places[:8]]
line("its 3.3, a me-now at 37 by four moments, to 23, 97, 83 and 157; the eight fours of 0 to 120, 32 places, four of them all primes · the eleventh drawing, check_a_me-now_four_moments_other-than_all_other-than_all.py",
     ["**A me-now at 37 goes by four moments, a cone on with a moment: about 30 to 23, an other-than; about 60 to 97, an all; about 90 to 83, an other-than; about 120 to 157, an all, next-universing.**",
      "The eight fours of 0 to 120, n, 60 less n, 60 and n and 120 less n, are its 32 uncrossed places; four of them are all primes: 7, 53, 67 and 113; 13, 47, 73 and 107; 19, 41, 79 and 101; 23, 37, 83 and 97."],
     me == [37, 23, 97, 83, 157] and sorted(n for f in fours for n in f) == [n for n in range(1, 120) if gcd(n, 30) == 1] and len(fours) * 4 == 32
     and [f for f in fours if all(map(prime, f))] == [[7, 53, 67, 113], [13, 47, 73, 107], [19, 41, 79, 101], [23, 37, 83, 97]])
line("its 3.3, prior, now and next as three pairs of cones; a me at 37 passing through as 37, 97 and 157, three primes, with 23, 83 and 143, 11 by 13 · the thirteenth drawing, check_prior_now_next_the_podalings_passing_through.py",
     ["**Prior, now and next are three pairs of cones, 0 to 60, 60 to 120 and 120 to 180**", "A me at 37 passes through as 37, 97 and 157, three primes, with 23, 83 and 143, 143 being 11 by 13."],
     all(map(prime, (37, 97, 157))) and (97 - 37, 157 - 97) == (60, 60) and [about(30)(37), about(90)(97), about(150)(157)] == [23, 83, 143] and 143 == 11 * 13 and prime(23) and prime(83))
line("its 3.4, ten as three, six and one, 3 by 3 and 1; ten by three by four, 120; and six orders of three · the seventeenth drawing's ten are four, three, two and one, check_ten_rows_of_the_four_moments.py; the nineteenth's diamond is the 3 by 3 with 0 the one, and the 21st's are the six orders",
     ["1 of 3 is three, 2 of 3 is six, and 3 of 3 is one, all-parity: 3 by 3 and 1, ten.**", "Ten other-thans by three me-nows by four moments is 120.", "3 of 3 is the corner's line, its six orders all ending at one"],
     3 + 3 * 2 + 1 == 10 == 3 * 3 + 1 == 4 + 3 + 2 + 1 and 10 * 3 * 4 == 120 and 3 * 2 * 1 == 6)
line("its 3.5, 120 as 4 by 5 by 6, the selves of a cube of 5 about its line; a cube of n about its line n cubed less n, 24, 60 and 120 · the eighth drawing, check_the_cube_of_5_and_its_line.py",
     ["**120 is 4 by 5 by 6: five's prior, now and next multiplied, the selves of a cube of 5 about its (1, 1, 1) line.**", "A cube of n about its line is n cubed less n: 3 gives 24, the fold; 4 gives 60; 5 gives 120."],
     4 * 5 * 6 == 120 == 5 ** 3 - 5 and [n ** 3 - n for n in (3, 4, 5)] == [24, 60, 120] and sum(1 for x in range(5) for y in range(5) for z in range(5) if not x == y == z) == 120)
line("its 1.6, 2.4 and 4.1, numbers' own quarter turn round ten, a crossed number ending in 3 or 7 passing both closings, and phi's closings by a prime's ending · the twentieth drawing, check_the_diamond_turning_3_and_7_about_5.py",
     ["round ten, multiplying by 3 steps 3, 9, 7, 1", "**A crossed number ending in 3 or 7 passing both is a field's asking**", "Round a prime ending in 1 or 9 φ closes by one short of it, and round a prime ending in 3 or 7 by twice one past it."],
     [3 ** k % 10 for k in (1, 2, 3, 4)] == [3, 9, 7, 1])
for name_, ok in results: print(("is       " if ok else "is not   ") + name_)
for q in gone: print("gone from the draft as it is: " + q[:90])
print(f"\n{sum(ok for _, ok in results)} of {len(results)} are is" + ("" if all(ok for _, ok in results) else ": the going through is not, all or none"))
sys.exit(0 if all(ok for _, ok in results) else 1)
