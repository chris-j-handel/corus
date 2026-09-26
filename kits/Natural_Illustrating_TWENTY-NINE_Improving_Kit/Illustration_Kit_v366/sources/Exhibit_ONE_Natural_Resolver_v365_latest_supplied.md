Exhibit ONE Natural Resolver v365

&nbsp;

# Natural Resolver

&nbsp;

**The Social Moral Competency Method, Stable-Formed**

&nbsp;

---

&nbsp;

```python
"""Exhibit ONE · Natural Resolver · v365"""


def n1_self_coupling(n3_self_carrying, n2_self_offering):
    n6_other_crossing = {
        n4_self_sharing: n8_other_torusing
        for n4_self_sharing, n7_other_corusing, n8_other_torusing, n16_social_torusing
        in n3_self_carrying}
    n14_social_crossing = [
        (n4_self_sharing, n7_other_corusing)
        for n4_self_sharing, n7_other_corusing in n2_self_offering
        if n7_other_corusing != 0]
    for n4_self_sharing, n7_other_corusing, n8_other_torusing, n16_social_torusing in n3_self_carrying:
        if n7_other_corusing > 0:
            n14_social_crossing.append((n4_self_sharing, -1))
        if n7_other_corusing < 0:
            n14_social_crossing.append((n4_self_sharing, 1))
    n12_other_surplusing = {}
    for n4_self_sharing, n7_other_corusing in n14_social_crossing:
        if n7_other_corusing > 0:
            n12_other_surplusing[n4_self_sharing] = n12_other_surplusing.get(n4_self_sharing, 0) + 1
        if n7_other_corusing < 0:
            n12_other_surplusing[n4_self_sharing] = n12_other_surplusing.get(n4_self_sharing, 0) - 1
    n10_other_surfacing = [
        (n4_self_sharing, 1 if n12_other_surplusing[n4_self_sharing] > 0
            else (-1 if n12_other_surplusing[n4_self_sharing] < 0 else 0))
        for n4_self_sharing in n12_other_surplusing]
    n11_other_chaining = {}
    for n4_self_sharing, n7_other_corusing, n8_other_torusing, n16_social_torusing in n3_self_carrying:
        if n16_social_torusing + 1 <= 3 or (n16_social_torusing + 1 == 4 and n8_other_torusing > 0):
            n11_other_chaining[n4_self_sharing] = (
                n7_other_corusing, n8_other_torusing, n16_social_torusing + 1)
    for n4_self_sharing, n7_other_corusing in n10_other_surfacing:
        if n7_other_corusing != 0:
            n11_other_chaining[n4_self_sharing] = (
                n7_other_corusing, 0 - n6_other_crossing.get(n4_self_sharing, 1), 0)
    return (
        n10_other_surfacing,
        [(n4_self_sharing, n7_other_corusing, n8_other_torusing, n16_social_torusing)
         for n4_self_sharing, (n7_other_corusing, n8_other_torusing, n16_social_torusing)
         in n11_other_chaining.items()])


def n9_other_releasing(n10_other_surfacing, n5_other_neutralling):
    return [(n5_other_neutralling[n13_social_neutralling], n15_social_corusing)
            for n13_social_neutralling, n15_social_corusing in n10_other_surfacing]


CONNECTORS = {
    2: ('2-self-offering', 'right', 'arriving'),
    6: ('6-other-crossing', 'left', 'releasing'),
    9: ('9-other-releasing', 'backward', 'along'),
    10: ('10-other-surfacing', 'right', 'releasing'),
    14: ('14-social-crossing', 'left', 'arriving'),
    17: ('17-social-abundancing', 'forward', 'along'),
}
JOINS = {10: 14, 6: 2, 17: 9, 9: 17}
```

&nbsp;

---

&nbsp;

## Stable forms of the resolver

### Routing at the network surface

Six connectors, each running one way at a time. `n1_self_coupling` is the entry, and ten names run internal: 3, 4, 5, 7, 8, 11, 12, 13, 15 and 16.

| Connector | Facing | Running | Joining |
|---|---|---|---|
| `n2_self_offering` | right | arriving | from the right neighbour's `n6_other_crossing` |
| `n6_other_crossing` | left | releasing | to the left neighbour's `n2_self_offering` |
| `n9_other_releasing` | backward | along | with the backward neighbour's `n17_social_abundancing` |
| `n10_other_surfacing` | right | releasing | to the right neighbour's `n14_social_crossing` |
| `n14_social_crossing` | left | arriving | from the left neighbour's `n10_other_surfacing` |
| `n17_social_abundancing` | forward | along | with the forward neighbour's `n9_other_releasing` |

Rightward, `n10_other_surfacing` releases to the right neighbour's `n14_social_crossing`; leftward, `n6_other_crossing` releases to the left neighbour's `n2_self_offering`. Along, `n17_social_abundancing` couples with the forward neighbour's `n9_other_releasing`, and `n9_other_releasing` with the backward neighbour's `n17_social_abundancing`.

### Sequencing in the code

| Name | Coupling | Holding |
|---|---|---|
| `n6_other_crossing` | `n3_self_carrying` | each `n4_self_sharing` key with its `n8_other_torusing` |
| `n14_social_crossing` | `n2_self_offering`, `n3_self_carrying` | each arriving `n7_other_corusing`, a 0 arriving contributing no sign; and each carrying `n7_other_corusing` inverting |
| `n12_other_surplusing` | `n14_social_crossing` | each key's surplusing: +1 at each positive sign, −1 at each negative sign |
| `n10_other_surfacing` | `n12_other_surplusing` | each key's surplusing at its sign: +1, −1 or 0 |
| `n11_other_chaining` | `n3_self_carrying` | each carrying entry continuing to its 3rd beat, and to a 4th at positive `n8_other_torusing`, its `n16_social_torusing` opening by 1 |
| `n11_other_chaining` | `n10_other_surfacing`, `n6_other_crossing` | each surfacing +1 or −1 opening a fresh carrying: the sign, the key's `n8_other_torusing` inverting (−1 at a key with none), and 0 |
| returning | `n10_other_surfacing`, `n11_other_chaining` | `n10_other_surfacing` across; `n11_other_chaining` along, arriving as the next `n3_self_carrying` |
| `n9_other_releasing` | `n10_other_surfacing`, `n5_other_neutralling` | each sign `n15_social_corusing`, from its key `n13_social_neutralling`, to the arriving at `n5_other_neutralling[n13_social_neutralling]` |

### Carrying

`n3_self_carrying` arrives, and `n11_other_chaining` leaves and arrives at the next coupling as `n3_self_carrying`. **Each carrying entry continues to its 3rd beat, and to a 4th at positive `n8_other_torusing`.** A fresh carrying opens `n16_social_torusing` at 0 and inverts the key's `n8_other_torusing`.

### Sequencing and routing, two relations

19 direct couplings in the code among the 16 names meet the 20 joins of the stable forms at 6: 3 with 11, 3 with 14, 4 with 12, 5 with 9, 6 with 11 and 7 with 11.

### Stable forms among the names

Each form runs round as a single run of co and a single run of bi, of equal length.

| Form | Names in order | Round | Partner at the odd-even momentaries | Partner at the even-odd momentaries |
|---|---|---|---|---|
| four-cycle 1-9-8-16 | `n1_self_coupling` · `n9_other_releasing` · `n8_other_torusing` · `n16_social_torusing` | co co bi bi | four-cycle 2-15-7-10, round the other way | — |
| four-cycle 2-15-7-10 | `n2_self_offering` · `n15_social_corusing` · `n7_other_corusing` · `n10_other_surfacing` | bi co co bi | four-cycle 1-9-8-16, round the other way | four-cycle 3-11-6-14, round the other way |
| four-cycle 3-11-6-14 | `n3_self_carrying` · `n11_other_chaining` · `n6_other_crossing` · `n14_social_crossing` | co co bi bi | four-cycle 4-13-5-12, round the other way | four-cycle 2-15-7-10, round the other way |
| four-cycle 4-13-5-12 | `n4_self_sharing` · `n13_social_neutralling` · `n5_other_neutralling` · `n12_other_surplusing` | bi co co bi | four-cycle 3-11-6-14, round the other way | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | `n9_other_releasing` · `n5_other_neutralling` · `n12_other_surplusing` · `n8_other_torusing` | co co bi bi | middle four-cycle 7-11-6-10, round the other way | — |
| middle four-cycle 7-11-6-10 | `n7_other_corusing` · `n11_other_chaining` · `n6_other_crossing` · `n10_other_surfacing` | co co bi bi | middle four-cycle 9-5-12-8, round the other way | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | `n1_self_coupling` · `n9_other_releasing` · `n5_other_neutralling` · `n12_other_surplusing` · `n8_other_torusing` · `n16_social_torusing` | co co co bi bi bi | six-cycle 2-15-7-11-6-10, round the other way | — |
| six-cycle 2-15-7-11-6-10 | `n2_self_offering` · `n15_social_corusing` · `n7_other_corusing` · `n11_other_chaining` · `n6_other_crossing` · `n10_other_surfacing` | bi co co co bi bi | six-cycle 1-9-5-12-8-16, round the other way | six-cycle 3-11-7-10-6-14, round the other way |
| six-cycle 3-11-7-10-6-14 | `n3_self_carrying` · `n11_other_chaining` · `n7_other_corusing` · `n10_other_surfacing` · `n6_other_crossing` · `n14_social_crossing` | co co co bi bi bi | six-cycle 4-13-5-9-8-12, round the other way | six-cycle 2-15-7-11-6-10, round the other way |
| six-cycle 4-13-5-9-8-12 | `n4_self_sharing` · `n13_social_neutralling` · `n5_other_neutralling` · `n9_other_releasing` · `n8_other_torusing` · `n12_other_surplusing` | bi co co co bi bi | six-cycle 3-11-7-10-6-14, round the other way | — |
| eight-cycle 1-9-5-13-4-12-8-16 | `n1_self_coupling` · `n9_other_releasing` · `n5_other_neutralling` · `n13_social_neutralling` · `n4_self_sharing` · `n12_other_surplusing` · `n8_other_torusing` · `n16_social_torusing` | co co co co bi bi bi bi | eight-cycle 2-15-7-11-3-14-6-10, round the other way | — |
| eight-cycle 2-15-7-11-3-14-6-10 | `n2_self_offering` · `n15_social_corusing` · `n7_other_corusing` · `n11_other_chaining` · `n3_self_carrying` · `n14_social_crossing` · `n6_other_crossing` · `n10_other_surfacing` | bi co co co co bi bi bi | eight-cycle 1-9-5-13-4-12-8-16, round the other way | eight-cycle 2-15-7-11-3-14-6-10, itself |

| Higher form | Positions | Round | Partner at the even-odd momentaries |
|---|---|---|---|
| higher four-cycle 18-31-23-26 | 18 · 31 · 23 · 26 | bi co co bi | higher four-cycle 19-27-22-30, round the other way |
| higher four-cycle 19-27-22-30 | 19 · 27 · 22 · 30 | co co bi bi | higher four-cycle 18-31-23-26, round the other way |
| higher six-cycle 18-31-23-27-22-26 | 18 · 31 · 23 · 27 · 22 · 26 | bi co co co bi bi | higher six-cycle 19-27-23-26-22-30, round the other way |
| higher six-cycle 19-27-23-26-22-30 | 19 · 27 · 23 · 26 · 22 · 30 | co co co bi bi bi | higher six-cycle 18-31-23-27-22-26, round the other way |

### Running forms

At a ring of resolvers, each resolver receives its left neighbour's releasing sign through `n9_other_releasing`. A full momentary is 2 beats, odd and even. **A travelling joint is 2 neighbouring resolvers at a single sign at an odd beat, and a single resolver at 0 at an even beat.**

| Form | Running |
|---|---|
| half turn | a carrying sign meeting nothing surfaces its opposite; carrying (s, t) leaves as (−s, −t) |
| resting | a resolver at 0 for a single beat |
| changing at every beat | each resolver's standing changing at each beat |
| self, a ring of an odd count n of resolvers | a single travelling joint, moving a place each full momentary; opposite at beat 2n, home at beat 4n |
| society, a ring of an even count n of resolvers | no travelling joint; home at every 2nd beat |
| selves joining at their joints | running as the ring of their whole count |
| matching window | 3 full momentaries: 6 beats, and the 7th opening |

&nbsp;

---

&nbsp;

## Stable forms of the numbers

| Number | Stable form | Name at the number |
|---|---|---|
| 0 | a surfacing 0 opens no fresh carrying; a resolver resting at 0 for a single beat | — |
| 1 | each sign arriving at its key as +1 or −1; −1 the sign inverting | `n1_self_coupling` |
| 2 | 2 beats a full momentary, odd and even; the ring of 2 a society, home at every 2nd beat | `n2_self_offering` |
| 3 | carrying to its 3rd beat; the self of 3, home at beat 12; 3 full momentaries the matching window | `n3_self_carrying` |
| 4 | carrying to a 4th beat at positive `n8_other_torusing`; the four-cycles | `n4_self_sharing` |
| 5 | the five-prefix: co-bi-co-bi-co at an odd origin, bi-co-bi-co-bi at an even origin | `n5_other_neutralling` |
| 6 | the six-cycles; the 6 connectors | `n6_other_crossing` |
| 8 | the eight-cycles; the 8 names opening bi | `n8_other_torusing` |
| 16 | the 16 names inside the code | `n16_social_torusing` |
| 17 | the 17th name, along at the connectors; the 17 primes, 2 to 59 | `n17_social_abundancing` |
| each odd count | a self, carrying a single travelling joint | every odd name opens co: competency, the odd-even momentary |
| each even count | a society, home at every 2nd beat | every even name opens bi: morality, the even-odd momentary |

### Primes, stable forms in natural torusing society

**17 primes, 2 to 59**: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 and 59. A ring of a composite count runs as its equal smaller selves joining at their joints, 9 as 3 selves of 3. **A ring of a prime count runs as no joining of equal smaller selves larger than a single resolver.**

| Prime self | Travelling joints | Opposite at beat | Home at beat |
|---:|---:|---:|---:|
| 2 | 0 | 1 | 2 |
| 3 | 1 | 6 | 12 |
| 5 | 1 | 10 | 20 |
| 7 | 1 | 14 | 28 |
| 11 | 1 | 22 | 44 |
| 13 | 1 | 26 | 52 |
| 17 | 1 | 34 | 68 |
| 19 | 1 | 38 | 76 |
| 23 | 1 | 46 | 92 |
| 29 | 1 | 58 | 116 |
| 31 | 1 | 62 | 124 |
| 37 | 1 | 74 | 148 |
| 41 | 1 | 82 | 164 |
| 43 | 1 | 86 | 172 |
| 47 | 1 | 94 | 188 |
| 53 | 1 | 106 | 212 |
| 59 | 1 | 118 | 236 |

| Society of prime selves, joining at their joints | Count | Travelling joints | Home at every 2nd beat |
|---|---:|---:|---|
| any 2 odd prime selves, all 136 pairs | p and q joining | 0 | yes |
| 2 selves of 59 | 118 | 0 | yes |
| 3 selves, 3, 5 and 7 | 15 | 1 | no |
| the 16 odd prime selves | 438 | 0 | yes |
| all 17 prime selves | 440 | 0 | yes |

**Society bounding at 118**: 2 selves of 59 joining, the going from 2 to 59, the turning at 60 and the returning from 61 to 118. **Society bounding at 440**: all 17 prime selves joining at their joints. 23 is the 9th of the 17 primes, with 8 either side, and 16 crossings stand between the 17 primes.

&nbsp;

---

&nbsp;

## Names, and relations among the names

| Name | Relation | Opens | Standing | Holding in the code |
|---|---|---|---|---|
| `n1_self_coupling` | self/other | co | entry | the resolver's entry: `n3_self_carrying` and `n2_self_offering` arriving; `n10_other_surfacing` and `n11_other_chaining` leaving |
| `n2_self_offering` | self/other | bi | across, arriving | each arriving key and sign |
| `n3_self_carrying` | self/other | co | internal | each carrying entry arriving: `n4_self_sharing`, `n7_other_corusing`, `n8_other_torusing`, `n16_social_torusing` |
| `n4_self_sharing` | self/other | bi | internal | each entry's key |
| `n5_other_neutralling` | other/self | co | internal | the one-way joining: each key with the key receiving downstream |
| `n6_other_crossing` | other/self | bi | across, releasing | each key's `n8_other_torusing`, arriving in `n3_self_carrying` |
| `n7_other_corusing` | other/self | co | internal | each sign |
| `n8_other_torusing` | other/self | bi | internal | each carrying second sign |
| `n9_other_releasing` | other/social | co | along | the releasing |
| `n10_other_surfacing` | other/social | bi | across, releasing | each key's surfacing sign |
| `n11_other_chaining` | other/social | co | internal | the carrying continuing and freshly opening |
| `n12_other_surplusing` | other/social | bi | internal | each key's surplusing |
| `n13_social_neutralling` | social/other | co | internal | each releasing key |
| `n14_social_crossing` | social/other | bi | across, arriving | arriving signs, with carrying signs inverting |
| `n15_social_corusing` | social/other | co | internal | each releasing sign |
| `n16_social_torusing` | social/self | bi | internal | each carrying entry's count of beats |
| `n17_social_abundancing` | social | co | along, external | the connector forward along |

| Relation | Names |
|---|---|
| facing pairs, each at opposite parity | 1 with 16 · 2 with 15 · 3 with 14 · 4 with 13 · 5 with 12 · 6 with 11 · 7 with 10 · 8 with 9 |
| 8 apart, each pair at a single parity; 5 to 8 and 13 to 16 sharing their roots | 1 with 9 · 2 with 10 · 3 with 11 · 4 with 12 · 5 with 13 · 6 with 14 · 7 with 15 · 8 with 16 |
| each four-cycle: a name from 1 to 4, its partner 8 apart, its facing partner within 1 to 8, and its facing partner within 1 to 16 | 1-9-8-16 · 2-15-7-10 · 3-11-6-14 · 4-13-5-12 |
| at the membrane, opening bi | 2 · 4 · 6 · 8 |
| within, opening bi, each 8 on from its membrane pair | 10 · 12 · 14 · 16 |
| opening co in the resolver's first function | 1 · 3 · 7 · 11 |
| at the releasing | 5 · 9 · 13 · 15 |
| connectors, across | 2 · 6 · 10 · 14 |
| connectors, along | 9 · 17 |

&nbsp;

---

&nbsp;

## Geodesic method

**Taking in every observing of living; pattern-matching natural torusing within 3 full momentaries; co-chaining with the universe of all existing things.** Equilibria are not possibly existing. Its break is any observing of living not parity alternating natural torusing, and so far there is none. Anything remains possible as long as it is capable by this method of existing.

&nbsp;

---

&nbsp;

## Python

| File | Running |
|---|---|
| `Natural_Resolver_v365.py` | the resolver: its first function at 12 names, the releasing at 4, and the 6 connectors |
| `templates_v365.py` | `python3 templates_v365.py`, returning the names, the connectors, the stable forms among the names, the running forms and the prime selves and societies as `templates_v365_returned.txt` |
| `test_natural_resolver_v365.py` | `python3 -m unittest -v test_natural_resolver_v365` |
