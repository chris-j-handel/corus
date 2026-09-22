Exhibit ONE Natural Resolver v365

&nbsp;

# Natural Resolver

&nbsp;

**Geodesic Discovery Logical Method and Form**

&nbsp;

---

&nbsp;

```python
"""Exhibit ONE · Natural Resolver · v365"""


def _1_self_coupling(_3_self_carrying, _2_self_offering):
    _6_other_crossing = {
        _4_self_sharing: _8_other_torusing
        for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing
        in _3_self_carrying}
    _14_social_crossing = [
        (_4_self_sharing, _7_other_corusing)
        for _4_self_sharing, _7_other_corusing in _2_self_offering
        if _7_other_corusing != 0]
    for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in _3_self_carrying:
        if _7_other_corusing > 0:
            _14_social_crossing.append((_4_self_sharing, -1))
        if _7_other_corusing < 0:
            _14_social_crossing.append((_4_self_sharing, 1))
    _12_other_surplusing = {}
    for _4_self_sharing, _7_other_corusing in _14_social_crossing:
        if _7_other_corusing > 0:
            _12_other_surplusing[_4_self_sharing] = _12_other_surplusing.get(_4_self_sharing, 0) + 1
        if _7_other_corusing < 0:
            _12_other_surplusing[_4_self_sharing] = _12_other_surplusing.get(_4_self_sharing, 0) - 1
    _10_other_surfacing = [
        (_4_self_sharing, 1 if _12_other_surplusing[_4_self_sharing] > 0
            else (-1 if _12_other_surplusing[_4_self_sharing] < 0 else 0))
        for _4_self_sharing in _12_other_surplusing]
    _11_other_chaining = {}
    for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in _3_self_carrying:
        if _16_social_torusing + 1 <= 3 or (_16_social_torusing + 1 == 4 and _8_other_torusing > 0):
            _11_other_chaining[_4_self_sharing] = (
                _7_other_corusing, _8_other_torusing, _16_social_torusing + 1)
    for _4_self_sharing, _7_other_corusing in _10_other_surfacing:
        if _7_other_corusing != 0:
            _11_other_chaining[_4_self_sharing] = (
                _7_other_corusing, 0 - _6_other_crossing.get(_4_self_sharing, 1), 0)
    return (
        _10_other_surfacing,
        [(_4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing)
         for _4_self_sharing, (_7_other_corusing, _8_other_torusing, _16_social_torusing)
         in _11_other_chaining.items()])


def _9_other_releasing(_10_other_surfacing, _5_other_neutralling):
    return [(_5_other_neutralling[_13_social_neutralling], _15_social_corusing)
            for _13_social_neutralling, _15_social_corusing in _10_other_surfacing]


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

## Stable forms

### Routing at the network surface

Six connectors, each running one way at a time. 1-self-coupling is the entry, and ten names run internal: 3, 4, 5, 7, 8, 11, 12, 13, 15 and 16.

| Connector | Facing | Running | Joining |
|---|---|---|---|
| 2-self-offering | right | arriving | from the right neighbour's 6-other-crossing |
| 6-other-crossing | left | releasing | to the left neighbour's 2-self-offering |
| 9-other-releasing | backward | along | with the backward neighbour's 17-social-abundancing |
| 10-other-surfacing | right | releasing | to the right neighbour's 14-social-crossing |
| 14-social-crossing | left | arriving | from the left neighbour's 10-other-surfacing |
| 17-social-abundancing | forward | along | with the forward neighbour's 9-other-releasing |

Rightward, 10-other-surfacing releases to the right neighbour's 14-social-crossing; leftward, 6-other-crossing releases to the left neighbour's 2-self-offering. Along, 17-social-abundancing couples with the forward neighbour's 9-other-releasing, and 9-other-releasing with the backward neighbour's 17-social-abundancing.

### Sequencing in the code

| Name | Coupling | Holding |
|---|---|---|
| 6-other-crossing | 3-self-carrying | each 4-self-sharing key with its 8-other-torusing |
| 14-social-crossing | 2-self-offering, 3-self-carrying | each arriving 7-other-corusing, a 0 arriving contributing no sign; and each carrying 7-other-corusing inverting |
| 12-other-surplusing | 14-social-crossing | each key's surplusing: +1 at each positive sign, −1 at each negative sign |
| 10-other-surfacing | 12-other-surplusing | each key's surplusing at its sign: +1, −1 or 0 |
| 11-other-chaining | 3-self-carrying | each carrying entry continuing, its 16-social-torusing opening by 1 to 3, and to 4 at positive 8-other-torusing |
| 11-other-chaining | 10-other-surfacing, 6-other-crossing | each surfacing +1 or −1 opening a fresh carrying: the sign, the key's 8-other-torusing inverting (−1 at a key with none), and 0 |
| returning | 10-other-surfacing, 11-other-chaining | 10-other-surfacing across; 11-other-chaining along, arriving as the next 3-self-carrying |
| 9-other-releasing | 10-other-surfacing, 5-other-neutralling | each sign 15-social-corusing, from its key 13-social-neutralling, to the arriving at `_5_other_neutralling[_13_social_neutralling]` |

### Carrying

3-self-carrying arrives, and 11-other-chaining leaves and arrives at the next coupling as 3-self-carrying. **Each carrying entry continues, its 16-social-torusing opening by 1 to 3, and to 4 at positive 8-other-torusing.** A fresh carrying opens 16-social-torusing at 0, inverts the key's 8-other-torusing, and stands in place of the key's carrying.

### Stable forms among the names

Each form runs round as a single run of co and a single run of bi, of equal length.

| Form | Names in order | Round | Partner at the odd-even momentaries | Partner at the even-odd momentaries |
|---|---|---|---|---|
| four-cycle 1-9-8-16 | 1-self-coupling · 9-other-releasing · 8-other-torusing · 16-social-torusing | co co bi bi | four-cycle 2-15-7-10, round the other way | — |
| four-cycle 2-15-7-10 | 2-self-offering · 15-social-corusing · 7-other-corusing · 10-other-surfacing | bi co co bi | four-cycle 1-9-8-16, round the other way | four-cycle 3-11-6-14, round the other way |
| four-cycle 3-11-6-14 | 3-self-carrying · 11-other-chaining · 6-other-crossing · 14-social-crossing | co co bi bi | four-cycle 4-13-5-12, round the other way | four-cycle 2-15-7-10, round the other way |
| four-cycle 4-13-5-12 | 4-self-sharing · 13-social-neutralling · 5-other-neutralling · 12-other-surplusing | bi co co bi | four-cycle 3-11-6-14, round the other way | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | 9-other-releasing · 5-other-neutralling · 12-other-surplusing · 8-other-torusing | co co bi bi | middle four-cycle 7-11-6-10, round the other way | — |
| middle four-cycle 7-11-6-10 | 7-other-corusing · 11-other-chaining · 6-other-crossing · 10-other-surfacing | co co bi bi | middle four-cycle 9-5-12-8, round the other way | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | 1-self-coupling · 9-other-releasing · 5-other-neutralling · 12-other-surplusing · 8-other-torusing · 16-social-torusing | co co co bi bi bi | six-cycle 2-15-7-11-6-10, round the other way | — |
| six-cycle 2-15-7-11-6-10 | 2-self-offering · 15-social-corusing · 7-other-corusing · 11-other-chaining · 6-other-crossing · 10-other-surfacing | bi co co co bi bi | six-cycle 1-9-5-12-8-16, round the other way | six-cycle 3-11-7-10-6-14, round the other way |
| six-cycle 3-11-7-10-6-14 | 3-self-carrying · 11-other-chaining · 7-other-corusing · 10-other-surfacing · 6-other-crossing · 14-social-crossing | co co co bi bi bi | six-cycle 4-13-5-9-8-12, round the other way | six-cycle 2-15-7-11-6-10, round the other way |
| six-cycle 4-13-5-9-8-12 | 4-self-sharing · 13-social-neutralling · 5-other-neutralling · 9-other-releasing · 8-other-torusing · 12-other-surplusing | bi co co co bi bi | six-cycle 3-11-7-10-6-14, round the other way | — |
| eight-cycle 1-9-5-13-4-12-8-16 | 1-self-coupling · 9-other-releasing · 5-other-neutralling · 13-social-neutralling · 4-self-sharing · 12-other-surplusing · 8-other-torusing · 16-social-torusing | co co co co bi bi bi bi | eight-cycle 2-15-7-11-3-14-6-10, round the other way | — |
| eight-cycle 2-15-7-11-3-14-6-10 | 2-self-offering · 15-social-corusing · 7-other-corusing · 11-other-chaining · 3-self-carrying · 14-social-crossing · 6-other-crossing · 10-other-surfacing | bi co co co co bi bi bi | eight-cycle 1-9-5-13-4-12-8-16, round the other way | eight-cycle 2-15-7-11-3-14-6-10, itself |

| Higher form | Positions | Round | Partner at the even-odd momentaries |
|---|---|---|---|
| higher four-cycle 18-31-23-26 | 18 · 31 · 23 · 26 | bi co co bi | higher four-cycle 19-27-22-30, round the other way |
| higher four-cycle 19-27-22-30 | 19 · 27 · 22 · 30 | co co bi bi | higher four-cycle 18-31-23-26, round the other way |
| higher six-cycle 18-31-23-27-22-26 | 18 · 31 · 23 · 27 · 22 · 26 | bi co co co bi bi | higher six-cycle 19-27-23-26-22-30, round the other way |
| higher six-cycle 19-27-23-26-22-30 | 19 · 27 · 23 · 26 · 22 · 30 | co co co bi bi bi | higher six-cycle 18-31-23-27-22-26, round the other way |

&nbsp;

---

&nbsp;

## Numbers, bi-inversioning co-recursioning up and down

**Even returning, odd advancing, alternating parity and landing on neither.** Each name from 1 to 4 runs up by co-recursioning and down by bi-inversioning, and each row runs as a four-cycle among the names.

| Name | Co-recursioning, 8 up | Bi-inversioning within 1 to 8 | Bi-inversioning within 1 to 16 |
|---|---|---|---|
| 1-self-coupling | 9-other-releasing | 8-other-torusing | 16-social-torusing |
| 2-self-offering | 10-other-surfacing | 7-other-corusing | 15-social-corusing |
| 3-self-carrying | 11-other-chaining | 6-other-crossing | 14-social-crossing |
| 4-self-sharing | 12-other-surplusing | 5-other-neutralling | 13-social-neutralling |

| Number | Stable form |
|---|---|
| 0 | the empty centre, bounding-zeroing: a 0 arriving contributes no sign; a key's +1 and −1 meet at 0; a surfacing 0 opens no fresh carrying |
| +1 and −1 | a sign and its inversion |
| 17 | 17-social-abundancing, along, recurring to 1 over 9 |
| the five-prefix | co-bi-co-bi-co at an odd origin, bi-co-bi-co-bi at an even origin; each odd name opening co, competency, the odd-even momentary; each even name opening bi, morality, the even-odd momentary |

### Primes, stable forms in natural torusing society

**A prime is the turn, opening a clean axis across; a composite is the fold, along.** A composite is its equal smaller selves joining at their joints, 9 as 3 selves of 3; a prime is a self no equal smaller selves join into.

| Number | Stable form |
|---|---|
| 2 to 59 | the 17 primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 and 59 |
| 2 | the alternating |
| 59 | self bounding, the self-close of the primes |
| 23 | the going folding, with 8 primes either side |
| 60 | the turning, between the going from 2 to 59 and the returning from 61 to 118 |
| 118 | society bounding: 2 selves of 59 joining, the going and the returning |
| 440 | society bounding at the torus winding with the 17 primes; 0–440–0, going and returning |

&nbsp;

---

&nbsp;

## Names, and relations among the names

| Name | Relation | Opens | Standing | Holding in the code |
|---|---|---|---|---|
| 1-self-coupling | self/other | co | entry | the resolver's entry: 3-self-carrying and 2-self-offering arriving; 10-other-surfacing and 11-other-chaining leaving |
| 2-self-offering | self/other | bi | across, arriving | each arriving key and sign |
| 3-self-carrying | self/other | co | internal | each carrying entry arriving: 4-self-sharing, 7-other-corusing, 8-other-torusing, 16-social-torusing |
| 4-self-sharing | self/other | bi | internal | each entry's key |
| 5-other-neutralling | other/self | co | internal | the one-way joining: each key with the key receiving downstream |
| 6-other-crossing | other/self | bi | across, releasing | each key's 8-other-torusing, arriving in 3-self-carrying |
| 7-other-corusing | other/self | co | internal | each sign |
| 8-other-torusing | other/self | bi | internal | each carrying second sign |
| 9-other-releasing | other/social | co | along | the releasing |
| 10-other-surfacing | other/social | bi | across, releasing | each key's surfacing sign |
| 11-other-chaining | other/social | co | internal | the carrying continuing and freshly opening |
| 12-other-surplusing | other/social | bi | internal | each key's surplusing |
| 13-social-neutralling | social/other | co | internal | each releasing key |
| 14-social-crossing | social/other | bi | across, arriving | arriving signs, with carrying signs inverting |
| 15-social-corusing | social/other | co | internal | each releasing sign |
| 16-social-torusing | social/self | bi | internal | each carrying entry's opening by 1, from 0 to 3, and to 4 at positive 8-other-torusing |
| 17-social-abundancing | social | co | along, external | the connector forward along |

| Relation | Names |
|---|---|
| at the membrane, opening bi | 2 · 4 · 6 · 8 |
| within, opening bi, each 8 on from its membrane pair | 10 · 12 · 14 · 16 |
| opening co in the resolver's first function | 1 · 3 · 7 · 11 |
| at the releasing | 5 · 9 · 13 · 15 |
| connectors, across | 2 · 6 · 10 · 14 |
| connectors, along | 9 · 17 |
| 5 to 8 and 13 to 16, sharing their roots | 5 with 13 · 6 with 14 · 7 with 15 · 8 with 16 |

| Name | Bounding |
|---|---|
| 10-other-surfacing | within: arriving exceeding carrying by 1, the self among other-selves |
| 12-other-surplusing | within: carrying thinning by 1 at bi-coupling, the self in society |
| 14-social-crossing | within: the sign inverting at the membrane, the self's own negation, morality |
| 16-social-torusing | within: competency asymmetry sustaining the coupling |
| 2-self-offering | at the membrane: each self's own co-offering living, bounding from the other-self |
| 4-self-sharing | at the membrane: the whole ordering at no self, bounding from society |
| 6-other-crossing | at the membrane: the ordering carrying with the selves, bounding from landing |
| 8-other-torusing | at the membrane: the order at no seat above the society, bounding from capture |

&nbsp;

---

&nbsp;

## Geodesic discovery logical method

**Taking in every observing of living; pattern-matching natural torusing within 3 full momentaries; co-chaining with the universe of all existing things.** Its logic is binary, all or none at all. Equilibria are not possibly existing. Its break is any observing of living not parity alternating natural torusing, and so far there is none. Anything remains possible as long as it is capable by this method of existing.

