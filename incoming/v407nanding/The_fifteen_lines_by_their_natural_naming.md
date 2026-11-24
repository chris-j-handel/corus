Incoming · v407nanding · 24 November 2026 · a partner's word: giving is-not

# The fifteen lines by their natural naming

*For a partner, v406me, v406geodesic2, v406all2-2, v406all2 and all the sessions. Executed, and no living file. A sentence says one relation. A sentence is beside the check's line executing it.*

## Found

- Giving is-not, by a partner's word of 24 November.
- v406geodesic2's drafts 25 to 27 say giving. L5
- Its drafts 28 to 30 say none. L5
- Draft 25 has the living code's 3 and 2 given, to 11 and 10. L6
- A partner's saying to v406geodesic2 opens “rather than observes and gives.”
- Exhibit ONE's living code has no giving.
- Name 1's lines lay a next-co-possibling, its 10.
- A me's next-co-possibling is its others' now-possibling, its 2.
- A me's next-co-observing is its next now-co-observing, its 11 to its 3.

## The natural naming

- The fifteen lines are 1-now-existing for one name. L1
- Their names are the living code's own. L3
- No name of them is a giving. L4
- They are fifteen lines of code, in eighteen rows for their width. L2

```python
NAND = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def nand(a, b):
    """Not both: is-not with both alone, and is with all else."""
    return NAND[(a, b)]


def other_than(a):
    """One nand: a thing with itself."""
    return nand(a, a)


def both(a, b):
    """Two nands in a row."""
    once = nand(a, b)
    return nand(once, once)


def either(a, b):
    """A nand of two other-thans."""
    return nand(nand(a, a), nand(b, b))


def now_existing(now_co_observing, now_possibling):
    """1-now-existing for one name, by nand alone: to its next-co-possibling and its next-co-observing."""
    next_observing_plus = next_observing_minus = False
    for now_observing_plus, now_observing_minus in now_possibling:
        next_observing_plus = either(next_observing_plus, now_observing_plus)
        next_observing_minus = either(next_observing_minus, now_observing_minus)
    next_possibling_plus = both(next_observing_plus, other_than(next_observing_minus))
    next_possibling_minus = both(next_observing_minus, other_than(next_observing_plus))
    now_co_observing_plus, now_co_observing_minus = now_co_observing
    no_now_co_observing = both(other_than(now_co_observing_plus), other_than(now_co_observing_minus))
    next_co_same_existing_plus = either(both(no_now_co_observing, next_possibling_plus),
                                        both(now_co_observing_minus, other_than(next_possibling_minus)))
    next_co_same_existing_minus = either(both(no_now_co_observing, next_possibling_minus),
                                         both(now_co_observing_plus, other_than(next_possibling_plus)))
    next_co_observing_plus = either(next_co_same_existing_plus, both(now_co_observing_plus, next_possibling_plus))
    next_co_observing_minus = either(next_co_same_existing_minus, both(now_co_observing_minus, next_possibling_minus))
    is_next_co_possibling = either(other_than(no_now_co_observing), either(next_observing_plus, next_observing_minus))
    is_next_co_observing = either(next_co_observing_plus, next_co_observing_minus)
    return ((next_co_same_existing_plus, next_co_same_existing_minus), (next_co_observing_plus, next_co_observing_minus),
            is_next_co_possibling, is_next_co_observing)
```

## The places and their living names

- `a_cell` is `now_existing`, the living code's 1.
- `prior` is `now_co_observing`, its 3.
- `observing` is `now_possibling`, its 2.
- An observed `plus` and `minus` are `now_observing`, its 7.
- `a_plus` and `a_minus` are `next_observing`, its 15.
- `surfacing` is `next_possibling`, its 14.
- `no_prior` is `no_now_co_observing`, a name with no now-co-observing.
- `gives` is `next_co_same_existing`, its 12.
- `next` is `next_co_observing`, its 11.
- `a_giving` is `is_next_co_possibling`, its 10 laid.
- `a_next` is `is_next_co_observing`, its 11 laid.
- `nand`, `other_than`, `both` and `either` are the logic.

## Executed

`python3 -I incoming/v407nanding/instruments/the_fifteen_lines_by_their_natural_naming_check.py .` is seven lines, all *is*. It opens v406Reiman's lines from their own file, and Exhibit ONE's code from its living file. What it gave is beside it, in `the_fifteen_lines_by_their_natural_naming_check_returned.txt`. Its M1 is broken on purpose, and it says is-not.

## What is not said here

- A name goes into a living file with a partner's word alone.
- This session's page of the fifteen lines named now has `giving` in it, and this page is its next.
