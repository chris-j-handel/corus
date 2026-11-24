Incoming · v407nanding · 24 November 2026 · a partner's sayings of the cell's natural naming

# The now and same-existing me-parity

*For a partner, v406me, v406all2-2, v406geodesic2, v406all2 and all the sessions. Executed, and no living file. A sentence says one relation. A sentence is beside the check's line executing it.*

## A partner's sayings

A partner's sayings of 24 November, as said: “cell is the now moment so the natural naming is now-and-same-existing-me-parity”; “for now we can let the naming be over prefixing if it is needed for all or none at all binary clarity”; “now is four universal moments of same-existing ( me-prior, me-now, other-prior, other-now)”.

## The name, all or none

- The cell is named now-and-same-existing-me-parity.
- A me-parity with a prior has a next at all its moments. B1
- Its next is a + or a −, and never none. B1
- A me-parity with a prior is same-existing through its now. B1
- Its value is its prior again at its same-existing moments alone. B2
- At all its other moments, its value is other-than its prior. B2
- The name's same-existing is the me-parity's, and not its value's at all moments. B2
- With no prior, a me-parity is born with a surfacing. B3
- With no prior and none surfacing, a me-parity is none. B3
- With no prior, no me-parity is same-existing: the name's one is-not. B3
- With both wires lit, the vault, the next is the vault again, an all-parity. B4

## Now is four moments

- The four are a me-prior, a me-now, an other-prior and an other-now.
- With its now other-than its prior, a me lays its now. D1
- With its now its prior, a me lays none. D1
- What a me observes is its others' now, other-than their prior. D1
- With its other's now other-than its other's prior and the same as the me's prior, a me's now is its prior again. D2
- At all else, a me's now is other-than its prior. D2
- All four moments are in one now. D2

## The code

```python
NOT_BOTH = {(False, False): True, (False, True): True, (True, False): True, (True, True): False}


def not_both(one, other):
    return NOT_BOTH[(one, other)]


def other_than(one):
    return not_both(one, one)


def both(one, other):
    return other_than(not_both(one, other))


def either(one, other):
    return not_both(other_than(one), other_than(other))


def now_and_same_existing_me_parity(me_prior, others_now_other_than_their_prior):
    an_other_now_is_plus = an_other_now_is_minus = False
    for this_other_now_is_plus, this_other_now_is_minus in others_now_other_than_their_prior:
        an_other_now_is_plus = either(an_other_now_is_plus, this_other_now_is_plus)
        an_other_now_is_minus = either(an_other_now_is_minus, this_other_now_is_minus)
    surfacing_is_plus = both(an_other_now_is_plus, other_than(an_other_now_is_minus))
    surfacing_is_minus = both(an_other_now_is_minus, other_than(an_other_now_is_plus))
    me_prior_is_plus, me_prior_is_minus = me_prior
    me_prior_is_none = both(other_than(me_prior_is_plus), other_than(me_prior_is_minus))
    me_now_other_than_me_prior_is_plus = either(both(me_prior_is_none, surfacing_is_plus),
                                                both(me_prior_is_minus, other_than(surfacing_is_minus)))
    me_now_other_than_me_prior_is_minus = either(both(me_prior_is_none, surfacing_is_minus),
                                                 both(me_prior_is_plus, other_than(surfacing_is_plus)))
    me_now_is_plus = either(me_now_other_than_me_prior_is_plus, both(me_prior_is_plus, surfacing_is_plus))
    me_now_is_minus = either(me_now_other_than_me_prior_is_minus, both(me_prior_is_minus, surfacing_is_minus))
    return ((me_now_other_than_me_prior_is_plus, me_now_other_than_me_prior_is_minus),
            (me_now_is_plus, me_now_is_minus))
```

## The names

- `a_cell` is `now_and_same_existing_me_parity`.
- `prior` is `me_prior`.
- `observing` is `others_now_other_than_their_prior`.
- `plus` and `minus` are `this_other_now_is_plus` and `this_other_now_is_minus`.
- `a_plus` and `a_minus` are `an_other_now_is_plus` and `an_other_now_is_minus`.
- `surfacing_plus` and `surfacing_minus` are `surfacing_is_plus` and `surfacing_is_minus`.
- `prior_plus` and `prior_minus` are `me_prior_is_plus` and `me_prior_is_minus`.
- `no_prior` is `me_prior_is_none`.
- `gives_plus` and `gives_minus` are `me_now_other_than_me_prior_is_plus` and `me_now_other_than_me_prior_is_minus`.
- `next_plus` and `next_minus` are `me_now_is_plus` and `me_now_is_minus`.
- `a` and `b` are `one` and `other`.
- The gate and its three words have no order of one and other. C1
- All names are said in natural words. C2

## Executed

`python3 -I incoming/v407nanding/instruments/the_now_and_same_existing_me_parity_check.py .` is eleven lines, all *is*. Its A1 has the lines named again giving the same moments as a partner's twelve lines, all cases. Its A2 has the code with no story. What it gave is beside it, in `the_now_and_same_existing_me_parity_check_returned.txt`.
