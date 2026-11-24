"""The seventeen names on a pair of cones, 0 to 60, by executing.

Usage: python3 -I the_names_on_a_pair_of_cones.py <a clone of the set>
   or: python3 -I the_names_on_a_pair_of_cones.py <Exhibit ONE, the living file>

Exhibit THIRTY-TWO Natural Prime Numbering, a draft of v407primes, says the
sixteen places of 0 to 60 that no spiral of 2, 3 or 5 crosses are the names
1 to 16, and 61 a next 1. This instrument goes through that saying beside
Exhibit ONE Natural Resolver's own names, moves and bi-foldings, found in
the living file as it is. It prints a line an is or an is-not, and writes
nothing.
"""
import glob
import os
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else '.'
if os.path.isdir(path):
    path = sorted(glob.glob(os.path.join(path, 'Exhibit_ONE_Natural_Resolver_v*.md')))[0]
living = re.sub(r'[*`]', '', ''.join(open(path, encoding='utf-8')))


def line(same, saying):
    print(('is' if same else 'is-not').ljust(7), saying)


def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


names = {}
for n, name in re.findall(r'^(\d+) · (\d+-[a-z-]+)$', living, re.M):
    names[int(n)] = name
folds = [tuple(int(x) for x in f.split('-')) for f in re.findall(r'^- (\d+-\d+-\d+-\d+)$', living, re.M)][:4]
places = [n for n in range(61) if n % 2 and n % 3 and n % 5]
place = {k + 1: p for k, p in enumerate(places)}
place[17] = 60 + place[1]

print("Exhibit ONE's own, as the living file says it")
line(len(names) == 17, 'seventeen names, a name with its number: %d' % len(names))
line('move is 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n).' in living, 'its sentence of a move, 8 up, 8 down or 17 less')
line(folds == [(1, 9, 8, 16), (2, 15, 7, 10), (3, 11, 6, 14), (4, 13, 5, 12)], 'its four bi-foldings: ' + ', '.join('-'.join(str(n) for n in f) for f in folds))

print()
print('The sixteen places of 0 to 60 no spiral of 2, 3 or 5 crosses')
line(len(places) == 16, ', '.join(str(p) for p in places))
line(place[17] == 61, '17 is 61, a pair of cones on from 1: a next 1')

print()
print("Exhibit ONE's moves are the cones' moves")
line(all(place[k + 8] == place[k] + 30 for k in range(1, 9)), '8 up is 30 on, a name of 1 to 8 to its next')
line(all(place[17 - k] == 60 - place[k] for k in range(1, 17)), '17 less is 60 less, a podaling about 30')
line(all(place[9 - k] == 30 - place[k] for k in range(1, 9)), '9 less is 30 less, a podaling about 15, with 1 to 8')

print()
print('A bi-folding is four places')
for f in folds:
    four = [place[n] for n in f]
    crossed = [p for p in four if not prime(p)]
    print('       ', '-'.join(str(n) for n in f).ljust(10), ', '.join(str(p) for p in four).ljust(16),
          'all primes' if not crossed else 'with ' + ' and '.join(str(p) for p in crossed) + ', no prime')
line([k for k in range(1, 17) if not prime(place[k])] == [1, 14], 'of the sixteen places two are no prime, 1 and 49: the names 1 and 14')

print()
print('A me at 37')
me = next(k for k in range(1, 17) if place[k] == 37)
line(me == 10, '37 is the place of %s' % names[me])
line(place[17 - me] == 23 and 17 - me == 7, 'its 17 less, 60 less 37, is 23, the place of %s' % names[17 - me])
walk = [37, 60 - 37, 120 - 23, 180 - 97, 240 - 83]
line(walk == [37, 23, 97, 83, 157], 'podaling about 30, 60, 90 and 120: ' + ', '.join(str(n) for n in walk))
line(all(prime(n) for n in walk), 'all five are primes')
line(all(prime(n) for n in (37, 97, 157)) and not prime(143) and 143 == 11 * 13, '37, 97 and 157 are primes; of 23, 83 and 143, 143 is 11 by 13')

print()
print('The eight fours of 0 to 120: n, 60 less n, 60 and n, 120 less n')
fours = [[n, 60 - n, 60 + n, 120 - n] for n in places if n < 30]
whole = [f for f in fours if all(prime(n) for n in f)]
line(len(fours) == 8 and sorted(n for f in fours for n in f) == [n for n in range(121) if n % 2 and n % 3 and n % 5], 'they are the 32 places of 0 to 120')
line(whole == [[7, 53, 67, 113], [13, 47, 73, 107], [19, 41, 79, 101], [23, 37, 83, 97]], 'four of them are all primes: ' + '; '.join(', '.join(str(n) for n in f) for f in whole))

print()
print("The draft's opening: rounds of four primes, by the names")
primes = [n for n in range(2, 62) if prime(n)]
rounds = [primes[0:4], primes[4:8], primes[8:12], primes[12:16]]
name_of = {p: k for k, p in place.items()}
line(rounds == [[2, 3, 5, 7], [11, 13, 17, 19], [23, 29, 31, 37], [41, 43, 47, 53]], 'four rounds of four primes: ' + '; '.join(', '.join(str(n) for n in r) for r in rounds))
line([7, 19, 37, 61] == [(k + 1) ** 3 - k ** 3 for k in range(1, 5)], "a cube's shells about its corner, 7, 19, 37 and 61; 53 is no shell")
line([1 + 6, 1 + 6 + 12, 1 + 6 + 12 + 18] == [7, 19, 37], 'a self and rounds of six: 7, 19 and 37')
for r in rounds:
    print('       ', ', '.join(str(n) for n in r).ljust(16), 'the names', ', '.join(str(name_of[n]) if n in name_of else 'a spiral' for n in r))
co = sorted(int(n) for n in re.findall(r'^- (\d+) · \d+-(?:now|next)-co-', living, re.M)) or sorted(k for k, v in names.items() if '-co-' in v)
line(co == [3, 4, 5, 6, 9, 10, 11, 12] and 'eight co names, 3 to 6 and 9 to 12' in living, "Exhibit ONE's eight co names, 3 to 6 and 9 to 12")
line([name_of[n] for n in rounds[1]] == [3, 4, 5, 6], "the round 11 to 19 is the names 3 to 6, the co names of a self's span")
line([name_of[n] for n in rounds[2]] == [7, 8, 9, 10], 'the round 23 to 37 is the names 7 to 10, closing with 10')
line([name_of[n] for n in rounds[3]] == [11, 12, 13, 15] and name_of[49] == 14, 'the round 41 to 53 is the names 11, 12, 13 and 15, passing over 14, the place 49')
line(name_of[59] == 16 and name_of[61] == 17, '59 is 16, and 61 is 17, a next 1')
turns = {2: 1, 6: 2, 30: 8, 210: 48, 510510: 92160}
line(all(sum(1 for n in range(1, t + 1) if all(n % p for p in (2, 3, 5, 7, 11, 13, 17) if t % p == 0)) == c for t, c in turns.items()) and 1 * 2 * 4 * 6 * 10 * 12 * 16 == 92160, 'the places of the turns of 2, 6, 30, 210 and 510,510: 1, 2, 8, 48 and 92,160')
line(121 == 11 * 11 and all(prime(n) or any(n % p == 0 for p in (2, 3, 5, 7)) for n in range(2, 121)), '121, 11 by 11, is the lowest crossed number that 2, 3, 5 and 7 cross not')
line(13 * 17 == 221 and 23 * 25 == 24 * 24 - 1 and primes.index(37) + 1 == 12, '13 by 17 is 221; 23 by 25 is one short of 24 by 24; 37 is the twelfth prime')
