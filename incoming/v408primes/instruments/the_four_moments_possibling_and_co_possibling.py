# v408primes · other-than-is and other-than-is-not, other-than-other-than-is and other-than-other-than-is-not:
# possibling and co-possibling, with same-existing as 0, linear aiming. Whole numbers and bits. Execute:
# python3 -I the_four_moments_possibling_and_co_possibling.py

results = []
def say(sentence, ok):
    results.append(ok)
    print(("is     " if ok else "is-not ") + sentence)

IS, ISNOT = 1, 0
def other_than(x):
    return 1 - x

# 1. A self's parity from prior to next has four moments, and two inversions are a same.
four = {
    "other-than-is": (IS, other_than(IS)),
    "other-than-is-not": (ISNOT, other_than(ISNOT)),
    "other-than-other-than-is": (IS, other_than(other_than(IS))),
    "other-than-other-than-is-not": (ISNOT, other_than(other_than(ISNOT))),
}
say("the four are the four moments of a self from prior to next: %s" % four, sorted(four.values()) == [(0, 0), (0, 1), (1, 0), (1, 1)])

# 2. The two other-thans are next other-than prior; the two other-than-other-thans are next same as prior.
change = {k: (a ^ b) for k, (a, b) in four.items()}
say("the other-thans change by 1 and the other-than-other-thans by 0, same-existing as 0: %s" % change,
    change == {"other-than-is": 1, "other-than-is-not": 1, "other-than-other-than-is": 0, "other-than-other-than-is-not": 0})

# 3. Changes add round 2: other-than then other-than is other-than-other-than, 1 + 1 = 0. Linear.
say("changes over two moments add round 2: 1 then 1 is 0, 1 then 0 is 1, 0 then 0 is 0, every prior",
    all(((x ^ a) ^ b) == x ^ ((a + b) % 2) for x in (0, 1) for a in (0, 1) for b in (0, 1)))

# 4. Added round 2 along, the changes are the parities multiplied across: a change of 0 is +1, a me again; of 1, −1.
say("a change added round 2 is its parities multiplied: (−1) to the a + b round 2 is (−1)^a by (−1)^b, all four",
    all((-1) ** ((a + b) % 2) == (-1) ** a * (-1) ** b for a in (0, 1) for b in (0, 1)))

# 5. Co-possibling: two selves' changes together, added round 2, are 0 when both are other-than or both same: aiming at 0.
say("two selves' changes added round 2 are 0 when both are other-than or both same-existing, and 1 when one is",
    all(((a + b) % 2 == 0) == (a == b) for a in (0, 1) for b in (0, 1)))

# 6. Co-possiblings about a between: their steps from it, −1 and +1, added are 0; podal about a turn's fold, n and the
#    turn less n, added are 0 round the turn.
say("co-possiblings' steps from their between, −1 and +1, add to 0; podal places n and 30 − n add to 0 round 30",
    -1 + 1 == 0 and all((n + (30 - n)) % 30 == 0 for n in range(30)))

# 7. A linear resolver: a ring of 11 selves, every next the xor of two priors. From two openings added round 2, its moments
#    are their moments added: linear aiming.
def ring(state, steps, n=11, taps=(10, 8)):
    out, mask = [], (1 << n) - 1
    for _ in range(steps):
        bit = ((state >> taps[0]) ^ (state >> taps[1])) & 1
        state = ((state << 1) | bit) & mask
        out.append(state)
    return out
ok = all([x ^ y for x, y in zip(ring(a, 300), ring(b, 300))] == ring(a ^ b, 300) for a in range(0, 2048, 37) for b in range(0, 2048, 53))
say("a ring of 11 selves, every next the xor of two priors: from two openings added, its moments are their moments added", ok)

# 8. Its one still place is the all-0, same-existing as 0: it goes to itself, and no other opening reaches it.
loop = ring(1, 2 ** 11 - 1)
say("the ring's one still place is the all-0: it goes to itself, and the loop from 1 passes all %d other places and never it" % (2 ** 11 - 1),
    ring(0, 5) == [0] * 5 and len(set(loop)) == 2 ** 11 - 1 and 0 not in loop)

print("All is." if all(results) else "A line is-not.")
