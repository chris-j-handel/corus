# v408primes · either parent can be odd, odd offers bi-coupling and even accepts, and from there the rest is determined.
# Whole numbers and bits; xor is four nands. Nothing simulated: every turn run whole.
# Execute: python3 -I odd_offers_even_accepts_the_rest_determined.py

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

def nand(a, b):
    return 1 - (a & b)
def xor(a, b):                      # four nands
    c = nand(a, b)
    return nand(nand(a, c), nand(b, c))

# 1. Along, with the first set odd, every next is set: odd, even, odd, even.
for first in (1, 2):
    seq = [(first + k) % 2 for k in range(12)]
    say("with the first %s, every next is set: %s" % ("odd" if first % 2 else "even", "".join("o" if x else "e" for x in seq)),
        all(seq[k] != seq[k + 1] for k in range(11)))

# 2. Odd offers and even accepts: every odd's next is an even, every even's next an odd, a bi-coupling a +1.
say("along, every odd's next is an even and every even's an odd: an offer and its accepting at every +1, to 1,000,000",
    all((n % 2 == 1) == ((n + 1) % 2 == 0) for n in range(1, 1000001)))

# 3. One odd or even alone sets two places of a turn; a parent's passing over 23 pairs is a turn of 2 to the 23.
say("one binary sets 2 places; a parent's passing over 23 pairs is a turn of %d places, set by 23 binaries" % 2 ** 23, 2 ** 23 == 8388608)

# 4. A determined stepping can pass a whole turn evenly: doubling round 11 passes all ten places, every next set by its now.
x, seen = 1, []
for _ in range(10):
    x = x * 2 % 11
    seen.append(x)
say("doubling round 11, every next set by its now, passes all ten places: %s" % seen, sorted(seen) == list(range(1, 11)))

# 5. A ring of 23 selves, every next self the xor of two of its priors, passes all 8,388,607 places of 23 binaries but
#    the all-0, every next set by its prior and now.
state, mask, steps = 1, (1 << 23) - 1, 0
while True:
    bit = xor((state >> 22) & 1, (state >> 17) & 1)
    state = ((state << 1) | bit) & mask
    steps += 1
    if state == 1:
        break
say("a ring of 23 selves, every next the xor of two priors, comes again after %d steps: all places of 23 binaries but the all-0" % steps,
    steps == 2 ** 23 - 1)

# 6. Its places pass evenly: over its whole turn, a self is 1 at 4,194,304 places and 0 at 4,194,303.
state, ones = 1, 0
for _ in range(2 ** 23 - 1):
    ones += state & 1
    bit = xor((state >> 22) & 1, (state >> 17) & 1)
    state = ((state << 1) | bit) & mask
say("over the ring's whole turn a self is 1 at %d places and 0 at %d: half and half, the all-0 the one place apart" % (ones, 2 ** 23 - 1 - ones),
    ones == 2 ** 22 and 2 ** 23 - 1 - ones == 2 ** 22 - 1)

print("All is." if all(results) else "A line is-not.")
