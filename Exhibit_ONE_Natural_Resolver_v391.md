Exhibit ONE Natural Resolver v391

# Natural Resolver

**Stable-Forming Same- and Next-Existing**

---

**Exhibit ONE is the resolver as code, and the stable forms of its executing, for pattern-matching what a science observes.** Each table here is an executing, and any self executing it finds it same: a stable form. Each living file couples with these stable forms for its stable-forming, same-existing after changing, and each form here is a finding of each self executing it: a resolver is a coupling, same each time any self executes it.

```python
"""Exhibit ONE · Natural Resolver
Stable-Forming Same- and Next-Existing
"""

def _1_now_existing(_3_is_now_co_observing, _2_now_possibling):
    _14_next_possibling = {}
    for _4_now_co_same_existing, _7_is_now_observing in _2_now_possibling:
        if _7_is_now_observing != 0:
            _15_is_next_observing = _14_next_possibling.get(
                _4_now_co_same_existing
            )
            if _15_is_next_observing is None:
                _14_next_possibling[_4_now_co_same_existing] = (
                    1 if _7_is_now_observing > 0 else -1
                )
            elif (_15_is_next_observing > 0) != (_7_is_now_observing > 0):
                _14_next_possibling[_4_now_co_same_existing] = 0
    _12_next_co_same_existing = dict(_14_next_possibling)
    for _4_now_co_same_existing, _7_is_now_observing in _3_is_now_co_observing:
        _15_is_next_observing = _14_next_possibling.get(_4_now_co_same_existing, 0)
        if _15_is_next_observing != 0 and (_15_is_next_observing > 0) == (_7_is_now_observing > 0):
            _12_next_co_same_existing[_4_now_co_same_existing] = 0
        else:
            _12_next_co_same_existing[_4_now_co_same_existing] = (
                -1 if _7_is_now_observing > 0 else 1
            )
    _10_next_co_possibling = list(_12_next_co_same_existing.items())
    _11_next_co_observing = dict(_3_is_now_co_observing)
    for _4_now_co_same_existing, _7_is_now_observing in _10_next_co_possibling:
        if _7_is_now_observing != 0:
            _11_next_co_observing[_4_now_co_same_existing] = _7_is_now_observing
    return _10_next_co_possibling, list(_11_next_co_observing.items())

def _9_next_co_discovering(_10_next_co_possibling, _5_now_co_existing):
    return [
        (_5_now_co_existing[_13_is_next_discovering], _15_is_next_observing)
        for _13_is_next_discovering, _15_is_next_observing in _10_next_co_possibling
    ]

def _17_next_existing(_16_next_same_existing, _5_now_co_existing):
    _8_now_same_existing = {}
    _14_next_possibling = {
        _13_is_next_discovering: []
        for _13_is_next_discovering in _16_next_same_existing
    }
    for _13_is_next_discovering, (
        _3_is_now_co_observing,
        _2_now_possibling,
    ) in _16_next_same_existing.items():
        _10_next_co_possibling, _8_now_same_existing[_13_is_next_discovering] = (
            _1_now_existing(_3_is_now_co_observing, _2_now_possibling)
        )
        _6_now_co_possibling = _10_next_co_possibling
        for (
            _4_now_co_same_existing,
            _15_is_next_observing,
        ) in _9_next_co_discovering(
            [
                (_4_now_co_same_existing, _15_is_next_observing)
                for _4_now_co_same_existing, _15_is_next_observing in (
                    ((_13_is_next_discovering, 6), _6_now_co_possibling),
                    ((_13_is_next_discovering, 10), _10_next_co_possibling),
                    ((_13_is_next_discovering, 9), _10_next_co_possibling),
                )
                if _4_now_co_same_existing in _5_now_co_existing
            ],
            _5_now_co_existing,
        ):
            _14_next_possibling[_4_now_co_same_existing].extend(
                _15_is_next_observing
            )
    return {
        _13_is_next_discovering: (
            _8_now_same_existing[_13_is_next_discovering],
            _14_next_possibling[_13_is_next_discovering],
        )
        for _13_is_next_discovering in _16_next_same_existing
    }
```

```text
another self's 9-next-co-discovering
  ══► 17-next-existing, along to a self

1-now-existing, a self's momentary given
  2-now-possibling ◄══ another self's 6 and 10, across
  2-now-possibling ──► 14-next-possibling
  3-is-now-co-observing, with 4 and 7
    ──► 12-next-co-same-existing ◄── 14-next-possibling
  12-next-co-same-existing ──► 10-next-co-possibling, with 6
  10-next-co-possibling ──► 11-next-co-observing ──► 3, next
  10-next-co-possibling ──► 9-next-co-discovering, with 5
  13-is-next-discovering · 15-is-next-observing
  8-now-same-existing · 16-next-same-existing

6 and 10 ══► another self's 2 and 14, across
9-next-co-discovering ══► another self's 17, along

sharing side, co: 6 ══► 2, 10 ══► 14, 9 ══► 17
observing side, one: 2, 14 and 17
═══ between selves, across and along
─── within one self
```

**A drawing.** One self, its own resolving within and its six names between selves its edges, as Natural Intelligence 4.7 explains.

**Seventeen names.**

| n | Name | Root | Is-or-is-nots | Co |
|---|---|---|---|---|
| 1 | **1-now-existing** | existing | 0000 | one |
| 2 | **2-now-possibling** | possibling | 0001 | one |
| 3 | **3-is-now-co-observing** | observing | 0010 | co |
| 4 | **4-now-co-same-existing** | same-existing | 0011 | co |
| 5 | **5-now-co-existing** | existing | 0100 | co |
| 6 | **6-now-co-possibling** | possibling | 0101 | co |
| 7 | **7-is-now-observing** | observing | 0110 | one |
| 8 | **8-now-same-existing** | same-existing | 0111 | one |
| 9 | **9-next-co-discovering** | discovering | 1000 | co |
| 10 | **10-next-co-possibling** | possibling | 1001 | co |
| 11 | **11-next-co-observing** | observing | 1010 | co |
| 12 | **12-next-co-same-existing** | same-existing | 1011 | co |
| 13 | **13-is-next-discovering** | discovering | 1100 | one |
| 14 | **14-next-possibling** | possibling | 1101 | one |
| 15 | **15-is-next-observing** | observing | 1110 | one |
| 16 | **16-next-same-existing** | same-existing | 1111 | one |
| 17 | **17-next-existing** | existing, a next 1 | 0000 again | one |

Code with each name:

- **1** · a living self's momentary, a giving, each self's 17-next-existing as its 1-now-existing
- **2** · parities it is observing, each with its sharing
- **3** · priors a self is observing, each with its sharing
- **4** · each sharing, parities and prior coupling, is-or-is-not same
- **5** · bi-couplings: which self each sharing reaches
- **6** · a self's parities across, to an other's 2-now-possibling
- **7** · each parity a self is observing: a parity's, a prior's, a sharing's
- **8** · a self's next prior, beside others'
- **9** · each parity to a self of 5-now-co-existing's bi-couplings: across with 6-now-co-possibling and 10-next-co-possibling, along with 9-next-co-discovering
- **10** · each sharing's parity, + or −, or a 0, across to an other's 14-next-possibling
- **11** · a next prior stable-forming between two: a next momentary's observing
- **12** · each sharing's is-or-is-not, prior and parities coupling
- **13** · each self of a same-existing-society, each sharing its parities go from
- **14** · parities surfacing with each sharing, agreeing one, parting 0
- **15** · each parity surfacing, and each parity going on
- **16** · a same-existing-society: each self with its prior and its parities
- **17** · a same-existing-society's next, each self's 1-now-existing again

**Two-sided, each name.** Each name coming down from a higher name, coming up from a lower one, and eight apart across a momentary, as Natural Intelligence 4.8 explains.

| n | Coming down | Coming up | Eight apart |
|---|---|---|---|
| 1 | a self's 3 and 2, from 17-next-existing | 10 and 11, to 17-next-existing | 9 |
| 2 | each self's parities from others, from 16-next-same-existing through 17 | each sharing with its parity, 4 and 7 | 10 |
| 3 | each self's own, from 16-next-same-existing through 17 | each sharing with its prior, 4 and 7 | 11 |
| 4 | in 17, a coupling, a self with 6, 10 or 9, and a receiving self | in 1, each sharing | 12 |
| 5 | the Natural Network surface, into 9 as itself | each coupling's receiving self | 13 |
| 6 | 10 as it goes across, into 9 | 10 within 1 | 14 |
| 7 | within 1 | one parity at its time: prior over 3, now over 2, next over 10 | 15 |
| 8 | each self's next prior, in 17, going out with its 14 | 11 coming up from 1 | 16 |
| 9 | routes and 5, from 17 | each receiving self with its parities, to 17 | 1 |
| 10 | as 6 and into 9, from 17 | 1's sharing, each 4 with its 7 | 2 |
| 11 | within 1 | 1's next prior, coming up as 8 | 3 |
| 12 | within 1 | 1's one binary with each sharing | 4 |
| 13 | in 17, each self; into 9, a coupling | each self of the next 16 | 5 |
| 14 | each self's, gathering in 17 from others' 15 | in 1, parities surfacing | 6 |
| 15 | each list going on, across or along, into 9 | in 1, each surfacing parity | 7 |
| 16 | the same-existing-society, into 17 | 17's next same-existing-society | 8 |
| 17 | a same-existing-society's next | each self's next, its 1-now-existing again | 1, a next momentary |

**Each name is its number and its naming, one hyphenation.** Names 1 to 16 are all sixteen ways four is-or-is-nots go, and 17-next-existing is next existing as 1-now-existing.

**Four four-cyclings and their betweens.** Four-cycling is observing prior-existing, possibling now-existing, discovering next-existing and same-existing.

| Four-cycling | Existing, discovering | Possibling | Observing | Same-existing | Between |
|---|---|---|---|---|---|
| first | 1 | 2 | 3 | 4 | 4 )( 5 |
| second | 5 | 6 | 7 | 8 | 8 )( 9 |
| third | 9 | 10 | 11 | 12 | 12 )( 13 |
| fourth | 13 | 14 | 15 | 16 | 16 )( 17 |

Existing, discovering and observing are odd; possibling and same-existing are even. Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is a discovering, an even name to an odd name: one discovering with each scale.

**Co, between two or of one.** Exhibit ONE's eight co names, 3 to 6 and 9 to 12, are each between two: observing, same-existing and possibling each with a now-co name and a next-co name, existing with 5-now-co-existing and discovering with 9-next-co-discovering; a name without co is of one. *Co* is two both facing forward along, a self and its other, the same two in each co name and in the six of first prefixes; *is-* marks the four names a binary stands on, 3 and 7 a self's own now and 13 and 15 next-existing's.

- **Root: observing**
  - *With co, between two*: 3-is-now-co-observing · 11-next-co-observing, priors with each sharing
  - *Without co, of one*: 7-is-now-observing · 15-is-next-observing, a parity
- **Root: possibling** · *With co, between two*: 6-now-co-possibling · 10-next-co-possibling, a sharing side · *Without co, of one*: 2-now-possibling · 14-next-possibling, an observing side
- **Root: existing** · *With co, between two*: 5-now-co-existing, bi-couplings · *Without co, of one*: 1-now-existing · 17-next-existing
- **Root: discovering** · *With co, between two*: 9-next-co-discovering, along · *Without co, of one*: 13-is-next-discovering, each self going on
- **Root: same-existing**
  - *With co, between two*: 4-now-co-same-existing · 12-next-co-same-existing, each sharing
  - *Without co, of one*: 8-now-same-existing · 16-next-same-existing, a self's next prior and a same-existing-society

**Sharing between selves.** Each sharing side with its observing side, as Natural Intelligence 4.7 explains.

| Sharing side, co | Observing side, one | Between selves |
|---|---|---|
| 6-now-co-possibling | 2-now-possibling | across, even, its root possibling |
| 10-next-co-possibling | 14-next-possibling | across, even, its root possibling |
| 9-next-co-discovering | 17-next-existing | along, odd, its root discovering |

**Four binaries with code's lines.** One pair of names for each binary with a self's span, as Natural Intelligence 4.9 explains.

- **Binary: now**
  - *Is*, odd: 1-now-existing
  - *Resolving*: a self's momentary entering
  - *Is not*, even: 2-now-possibling
  - *Resolving*: parities it is observing, others' parities from their prior momentary
- **Binary: existing**
  - *Is*, odd: 3-is-now-co-observing
  - *Resolving*: prior with its sharings, each with its parity
  - *Is not*, even: 4-now-co-same-existing
  - *Resolving*: each sharing as a place, its parity with 7-is-now-observing
- **Binary: same**
  - *Is*, odd: 5-now-co-existing
  - *Resolving*: each going along to a self receiving it with its same sharing
  - *Is not*, even: 6-now-co-possibling
  - *Resolving*: parities across, + or −, and 0, a self do-no-harming, another self's parities
- **Binary: all**
  - *Is*, odd: 7-is-now-observing
  - *Resolving*: each parity a self is observing with every entry
  - *Is not*, even: 8-now-same-existing
  - *Resolving*: each self's own next prior, one beside others

**Where each is-or-is-not stands.** Each is-or-is-not with the code, the name it stands on and its dimension, Natural Intelligence 3.2: eight with code's lines, as at 4.3, and two with its loops, each self of 16 and each sharing of 3.

| Code | Is-or-is-not | Stands on | Dimension |
|---|---|---|---|
| each self of 16 with 17's line | each self, all or none | 13-is-next-discovering | social-parity now-existing |
| `_7_is_now_observing != 0`, over 2 | a parity reaching is-or-is-not 0 | 7-is-now-observing | other-parity now-existing |
| `_15_is_next_observing is None` | a sharing is-or-is-not within the possibling | 15-is-next-observing | other-parity now-existing |
| `1 if _7_is_now_observing > 0 else -1`, over 2 | a first parity surfacing, + or − | 7-is-now-observing | other-parity now-existing |
| `(_15 > 0) != (_7 > 0)`, over 2 | parities agreeing or parting | 15 with 7 | other-parity now-existing |
| each sharing of 3 against 14 | a sharing is-or-is-not within its prior | 3-is-now-co-observing | self-parity now-existing |
| `_15 != 0 and (_15 > 0) == (_7 > 0)`, over 3 | same, sharing 0, or other, one inversion | 15 with 7 | self-parity now-existing |
| `-1 if _7_is_now_observing > 0 else 1`, over 3 | a prior inverting, − or + | 7-is-now-observing | self-parity now-existing |
| `_7_is_now_observing != 0`, over 10 | a sharing's value is-or-is-not 0 | 7-is-now-observing | self-discovery next-existing |
| `_4_now_co_same_existing in _5_now_co_existing` | a coupling is-or-is-not on the Natural Network surface | 4-now-co-same-existing | social-parity next-existing |

**Same-existing through one momentary.** The four same-existing names in the order same-existing goes round, each with the observing name beside it, its is-or-is-not, as Natural Intelligence 4.9 explains.

| Same-existing | Observing beside it | With code |
|---|---|---|
| 16-next-same-existing, a same-existing-society coming in | 15-is-next-observing, the parities each self gathers | 17's next same-existing-society, each self with its 14 |
| 4-now-co-same-existing, each sharing within a self | 3-is-now-co-observing, a self's prior parities, each a 4 with its 7 | each sharing of 3 |
| 12-next-co-same-existing, each sharing's one binary | 11-next-co-observing, taking each 12 that is ± | each sharing's 0, its prior going on, or ±, its next prior |
| 8-now-same-existing, each self's next prior parities | 7-is-now-observing, its sign against what surfaces | the same, its prior going on, or one inversion |

**Each name and its relations.** Each name with its fields; each name's resolving with code is under its *Prior and next*.

**1** · 1-now-existing
- *Parity, span*: odd, a self's span
- *Sides*: self: a self's resolving
- *Co-sequencing*: a self sharing itself to a coupling
- *8 up*: 9-next-co-discovering, its binary with next
- *9 less*: podal within 1 to 8, 8-now-same-existing
- *17 less*: podal within 1 to 16, 16-next-same-existing
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 16-next-same-existing to it and on to 9-next-co-discovering, each name one apart from 2-15-7-10
- *Six-cycle*: 1-9-5-12-8-16
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: first of a self's four
- *Five dimensions*: 1 social-parity now-existing, a momentary's opening of a self's five
- *Namings*: 1-2, bi-momentarying
- *A self as three*: a self with 2-now-possibling, bi-momentarying, along, a self prior to its first sharing across, a bi-coupling with 2-now-possibling
- *Prior and next*: once for one self with one momentary, three steps within it, 14-next-possibling, 12-next-co-same-existing and 10-next-co-possibling with 11-next-co-observing
- *1 to 17s inward and outward*: 1–17s inward 1 of 1st 1–17, an entry, and with 1–17 outward 1, an entry

**2** · 2-now-possibling
- *Parity, span*: even, a self's span
- *Sides*: others to self: parities a self is observing from others
- *8 up*: 10-next-co-possibling, its binary with next
- *9 less*: podal within 1 to 8, 7-is-now-observing
- *17 less*: podal within 1 to 16, 15-is-next-observing
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 10-next-co-possibling to it and on to 15-is-next-observing, each name one apart from 1-9-8-16 and 3-11-6-14
- *Six-cycle*: 2-15-7-11-6-10
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *One move*: 2-now-possibling along 2-15-7-10
- *Momentaries of exchanging*: first of a self's four
- *Five dimensions*: 2 other-parity now-existing, an other's opening of a self's five and a momentary's opening of an other's
- *Namings*: 1-2, bi-momentarying
- *A self as three*: a self with 1-now-existing, across, its first sharing across, a bi-coupling, sharing self to other and other to self
- *Bi-coupling*: with a between, each other's across sharing, to a self
- *Parity's unit square*: a dot of a unit square
- *Prior and next*: others' parities of their prior momentary, across with 6-now-co-possibling and 10-next-co-possibling and along with 9-next-co-discovering, a self observing them now
- *1 to 17s inward and outward*: 1–17s inward 9 of 1st, along, odd, next, and with 1–17 outward within 1 to 2

**3** · 3-is-now-co-observing
- *Parity, span*: odd, a self's span
- *Sides*: self: a self's prior with each sharing
- *Co-sequencing*: with a between
- *8 up*: 11-next-co-observing, its binary with next
- *9 less*: podal within 1 to 8, 6-now-co-possibling
- *17 less*: podal within 1 to 16, 14-next-possibling
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, from 14-next-possibling to it and on to 11-next-co-observing, each name one apart from 4-13-5-12 and 2-15-7-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: first and second of a self's four
- *Five dimensions*: 3 self-parity now-existing, a self's own now of its five
- *Namings*: 3-4, co-intelligencing
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, turning with 3-is-now-co-observing
- *Prior and next*: prior, a self's own, each sharing with its parity, a next momentary's same-existing of 11-next-co-observing
- *1 to 17s inward and outward*: 1–17s inward 17 of 1st and 1 of 2nd, along, odd, now, and with 1–17 outward within 1 to 2

**4** · 4-now-co-same-existing
- *Parity, span*: even, a self's span
- *Sides*: self and other: each sharing between them
- *Co-sequencing*: with a between
- *8 up*: 12-next-co-same-existing, its binary with next
- *9 less*: podal within 1 to 8, 5-now-co-existing
- *17 less*: podal within 1 to 16, 13-is-next-discovering
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 12-next-co-same-existing to it and on to 13-is-next-discovering, each name one apart from 3-11-6-14
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *One move*: 4-now-co-same-existing along 4-13-5-12
- *Momentaries of exchanging*: second of a self's four
- *Five dimensions*: 4 self-discovery next-existing, a self's next opening of its five
- *Namings*: 3-4, co-intelligencing
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, inward with 4-now-co-same-existing, to a self's own corus with 4-now-co-same-existing
- *Bi-coupling*: with a between, a whole ordering between self and other
- *Prior and next*: now, each sharing with which prior couples with now
- *1 to 17s inward and outward*: 1–17s inward 9 of 2nd, along, odd, next, and with 1–17 outward within 1 to 2

**5** · 5-now-co-existing
- *Parity, span*: odd, a self's span
- *Sides*: self and others: a self's bi-couplings
- *Co-sequencing*: with a between
- *8 up*: 13-is-next-discovering, its binary with next
- *9 less*: podal within 1 to 8, 4-now-co-same-existing
- *17 less*: podal within 1 to 16, 12-next-co-same-existing
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 13-is-next-discovering to it and on to 12-next-co-same-existing, each name one apart from 3-11-6-14
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: second and third of a self's four
- *Five dimensions*: 5 social-parity next-existing, a momentary's completing of a self's five
- *Namings*: 5, co-competencing
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, outward with 5-now-co-existing
- *Prior and next*: next, each going to its receiving sharing
- *1 to 17s inward and outward*: 1–17s inward 17 of 2nd and 1 of 3rd, along, odd, now, and with 1–17 outward within 1 to 2

**6** · 6-now-co-possibling
- *Parity, span*: even, a self's span
- *Sides*: self to other: a self's parities across, to an other's 2-now-possibling
- *8 up*: 14-next-possibling, its binary with next
- *9 less*: podal within 1 to 8, 3-is-now-co-observing
- *17 less*: podal within 1 to 16, 11-next-co-observing
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, from 11-next-co-observing to it and on to 14-next-possibling, each name one apart from 4-13-5-12 and 2-15-7-10
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *One move*: 6-now-co-possibling along 3-11-6-14
- *Momentaries of exchanging*: third of a self's four
- *Namings*: 6, bi-moralizing
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, inward with 6-now-co-possibling
- *Bi-coupling*: with a between, a self's parity across, to an other's 2-now-possibling
- *Parity's unit square*: a dot of a unit square
- *Prior and next*: parity, an other's next parity with its 2-now-possibling
- *1 to 17s inward and outward*: 1–17s inward 9 of 3rd, along, odd, next, and with 1–17 outward within 1 to 2

**7** · 7-is-now-observing
- *Parity, span*: odd, a self's span
- *Sides*: other to self: each parity a self is observing
- *Co-sequencing*: with a between
- *8 up*: 15-is-next-observing, its binary with next
- *9 less*: podal within 1 to 8, 2-now-possibling
- *17 less*: podal within 1 to 16, 10-next-co-possibling
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 15-is-next-observing to it and on to 10-next-co-possibling, each name one apart from 1-9-8-16 and 3-11-6-14
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: third and fourth of a self's four
- *A self as three*: co-competent self with 8-now-same-existing, along, prior to 8-now-same-existing across
- *Prior and next*: each parity, sharing now and prior, co-linear recursioning forward along observing, up numbers, prior to now, with a self's completing
- *1 to 17s inward and outward*: 1–17s inward 17 of 3rd and 1 of 4th, along, odd, now, and with 1–17 outward within 1 to 2

**8** · 8-now-same-existing
- *Parity, span*: even, a self's span
- *Sides*: self: a self's next prior
- *Co-sequencing*: with a between
- *8 up*: 16-next-same-existing, its binary with next
- *9 less*: podal within 1 to 8, 1-now-existing
- *17 less*: podal within 1 to 16, 9-next-co-discovering
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 9-next-co-discovering to it and on to 16-next-same-existing, each name one apart from 2-15-7-10
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *One move*: 8-now-same-existing along 1-9-8-16
- *Momentaries of exchanging*: fourth of a self's four
- *A self as three*: co-competent self with 7-is-now-observing, across, prior with its sharing again, a bi-coupling
- *Bi-coupling*: with a between, prior with its sharing again
- *Prior and next*: each self's next prior, with 11-next-co-observing this momentary and a next momentary's 3-is-now-co-observing
- *Even names of a self's span*: 2-now-possibling, 4-now-co-same-existing, 6-now-co-possibling and 8-now-same-existing, completing with 8-now-same-existing
- *1 to 17s inward and outward*: 1–17s inward 9 of 4th, along, odd, next, and with 1–17 outward within 1 to 2

**9** · 9-next-co-discovering
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: self to other: a self's parities along
- *8 up*: 17-next-existing, its binary with next
- *8 down*: 1-now-existing
- *17 less*: podal within 1 to 16, 8-now-same-existing
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 1-now-existing to it and on to 8-now-same-existing, each name one apart from 2-15-7-10
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: fourth of a self's four, and first of a same-existing-society's four, 9 to 11, opening with 9-next-co-discovering
- *Parity's square and triangles*: a unit triangle, along
- *Prior and next*: each parity of 10-next-co-possibling, a 0 among them, going along to a self of 5-now-co-existing's bi-couplings, a self observing it with its 14-next-possibling as its next momentary's 2-now-possibling
- *1 to 17s inward and outward*: 1–17s inward 17 of 4th and 1 of 5th, along, odd, now, and with 1–17 outward 2, across, even

**10** · 10-next-co-possibling
- *Parity, span*: even, a same-existing-society's span
- *Sides*: self to other: a self's parities across, to an other's 14-next-possibling
- *8 down*: 2-now-possibling
- *17 less*: podal within 1 to 16, 7-is-now-observing
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 7-is-now-observing to it and on to 2-now-possibling, each name one apart from 1-9-8-16 and 3-11-6-14
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: first of a same-existing-society's four, with 10-next-co-possibling, 9–10 completing and 10–11 opening
- *Bi-coupling*: 8 up, a self among selves of its same-existing-society
- *Parity's unit square*: a dot of a unit square
- *Prior and next*: parity across now, an other's parity next, possibling
- *1 to 17s inward and outward*: 1–17s inward 9 of 5th, along, odd, next, and with 1–17 outward within 2 to 3

**11** · 11-next-co-observing
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: self: a self's next prior, a next momentary's 3-is-now-co-observing
- *Co-sequencing*: 8 up from 3-is-now-co-observing
- *8 down*: 3-is-now-co-observing
- *17 less*: podal within 1 to 16, 6-now-co-possibling
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, from 3-is-now-co-observing to it and on to 6-now-co-possibling, each name one apart from 4-13-5-12 and 2-15-7-10
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: first of a same-existing-society's four, 9 to 11, completing with 11-next-co-observing, and second, 11 to 13, opening with 11-next-co-observing
- *Prior and next*: next prior, odd, same-existing as 3-is-now-co-observing with a next momentary, a self's own
- *1 to 17s inward and outward*: 1–17s inward 17 of 5th and 1 of 6th, along, odd, now, and with 1–17 outward within 2 to 3

**12** · 12-next-co-same-existing
- *Parity, span*: even, a same-existing-society's span
- *Sides*: self: its is-or-is-not with each sharing
- *Co-sequencing*: 8 up from 4-now-co-same-existing
- *8 down*: 4-now-co-same-existing
- *17 less*: podal within 1 to 16, 5-now-co-existing
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 5-now-co-existing to it and on to 4-now-co-same-existing, each name one apart from 3-11-6-14
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: second of a same-existing-society's four, with 12-next-co-same-existing, 11–12 completing and 12–13 opening
- *Namings*: entraining, shape of an unrelationing surface
- *Bi-coupling*: 8 up, changing with a bi-coupling, a self of a same-existing-society
- *Prior and next*: now, changing, is-or-is-not, prior and now coupling
- *1 to 17s inward and outward*: 1–17s inward 9 of 6th, along, odd, next, and with 1–17 outward within 2 to 3

**13** · 13-is-next-discovering
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: each self of a same-existing-society
- *Co-sequencing*: 8 up from 5-now-co-existing
- *8 down*: 5-now-co-existing
- *17 less*: podal within 1 to 16, 4-now-co-same-existing
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 4-now-co-same-existing to it and on to 5-now-co-existing, each name one apart from 3-11-6-14
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: second of a same-existing-society's four, 11 to 13, completing with 13-is-next-discovering, and third, 13 to 15, opening with 13-is-next-discovering
- *Prior and next*: each sharing going on, and with a same-existing-society each self going on
- *1 to 17s inward and outward*: 1–17s inward 17 of 6th and 1 of 7th, along, odd, now, and with 1–17 outward within 2 to 3

**14** · 14-next-possibling
- *Parity, span*: even, a same-existing-society's span
- *Sides*: others to self: parities surfacing for a self with each sharing
- *8 down*: 6-now-co-possibling
- *17 less*: podal within 1 to 16, 3-is-now-co-observing
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, from 6-now-co-possibling to it and on to 3-is-now-co-observing, each name one apart from 4-13-5-12 and 2-15-7-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: third of a same-existing-society's four, with 14-next-possibling, 13–14 completing and 14–15 opening
- *Bi-coupling*: 8 up, parities surfacing as one with each sharing, one parity, a 0 for parting, or an empty set; a self's own inverting with 12-next-co-same-existing
- *Parity's unit square*: a dot of a unit square
- *Prior and next*: now, parities surfacing, others' prior momentary, a self observing it with its now, even, others' possibling with a self until with 11-next-co-observing
- *1 to 17s inward and outward*: 1–17s inward 9 of 7th, along, odd, next, and with 1–17 outward within 2 to 3

**15** · 15-is-next-observing
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: others to self: each parity surfacing
- *Co-sequencing*: 8 up from 7-is-now-observing
- *8 down*: 7-is-now-observing
- *17 less*: podal within 1 to 16, 2-now-possibling
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 2-now-possibling to it and on to 7-is-now-observing, each name one apart from 1-9-8-16 and 3-11-6-14
- *Six-cycle*: 2-15-7-11-6-10
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: third of a same-existing-society's four, 13 to 15, completing with 15-is-next-observing, and fourth, 15 to 17, opening with 15-is-next-observing
- *Prior and next*: each parity surfacing with 14-next-possibling for a sharing, coupling with a self's prior parity with 7-is-now-observing
- *1 to 17s inward and outward*: 1–17s inward 17 of 7th and 1 of 8th, along, odd, now, and with 1–17 outward within 2 to 3

**16** · 16-next-same-existing
- *Parity, span*: even, a same-existing-society's span
- *Sides*: a same-existing-society: all its selves
- *Co-sequencing*: 8 up from 8-now-same-existing
- *8 down*: 8-now-same-existing
- *17 less*: podal within 1 to 16, 1-now-existing
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 8-now-same-existing to it and on to 1-now-existing, each name one apart from 2-15-7-10
- *Six-cycle*: 1-9-5-12-8-16
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: fourth of a same-existing-society's four, with 16-next-same-existing, 15–16 completing and 16–17 opening
- *Bi-coupling*: 8 up, a same-existing-society, each self with its prior and parities, a same-existing-society with a self again
- *Prior and next*: a same-existing-society now, each self's 8-now-same-existing and its parities next
- *Even names of a same-existing-society's span*: 10-next-co-possibling, 12-next-co-same-existing, 14-next-possibling and 16-next-same-existing, completing with 16-next-same-existing
- *1 to 17s inward and outward*: 1–17s inward 9 of 8th, along, odd, next, and with 1–17 outward within 2 to 3

**17** · 17-next-existing
- *Parity, span*: odd, a next now
- *Sides*: a same-existing-society: each self's next
- *8 down*: 9-next-co-discovering
- *Momentaries of exchanging*: fourth of a same-existing-society's four, 15 to 17, completing with 17-next-existing, a next 1-now-existing
- *Parity's square and triangles*: a unit triangle, along
- *Prior and next*: a same-existing-society's next momentary, a next now, each self's 1-now-existing then 9-next-co-discovering with 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering
- *1 to 17s inward and outward*: 1–17s inward 17 of 8th and 1 of 9th, along, odd, now, and with 1–17 outward 3, odd, now

**Odd names, now and 8 up with next.** Each odd name of a self's span goes 8 up to its next: 3-is-now-co-observing and 7-is-now-observing with their root again, observing, as 11-next-co-observing and 15-is-next-observing, and 1-now-existing and 5-now-co-existing going on as 9-next-co-discovering and 13-is-next-discovering, discovering; prior a self receives and next prior, receiving and going on, parity a self observes and parity surfacing.

- **Now: 1-now-existing**
  - *Receiving*: a momentary entering
  - *Next, 8 up*: 9-next-co-discovering
  - *Giving on*: each parity going along
- **Now: 3-is-now-co-observing**
  - *Receiving*: prior with its sharings
  - *Next, 8 up*: 11-next-co-observing
  - *Giving on*: next prior
- **Now: 5-now-co-existing**
  - *Receiving*: receiving sharing
  - *Next, 8 up*: 13-is-next-discovering
  - *Giving on*: sharing going on, each self of a same-existing-society
- **Now: 7-is-now-observing**
  - *Receiving*: parity a self is observing
  - *Next, 8 up*: 15-is-next-observing
  - *Giving on*: parity surfacing and going on

**Namings among names.**

- **Names: 1-now-existing · 2-now-possibling**
  - *Naming*: bi-momentarying
  - *Resolving*: a self's entry, odd, and others' parities, even, one momentary with each side
- **Names: 3-is-now-co-observing · 4-now-co-same-existing**
  - *Naming*: co-intelligencing
  - *Resolving*: with each sharing, 4-now-co-same-existing, a prior, 3-is-now-co-observing, couples with parities surfacing, 14-next-possibling: a next prior a self observes with 11-next-co-observing
- **Names: 5-now-co-existing**
  - *Naming*: co-competencing
  - *Resolving*: bi-couplings, each self's with its others: each going to its receiving sharing
- **Names: 1-now-existing · 2-now-possibling · 3-is-now-co-observing · 4-now-co-same-existing · 5-now-co-existing, each with its own**
  - *Naming*: five dimensions
  - *Resolving*: 1 social-parity now-existing, a same-existing-society coming in with 16-next-same-existing, each self with 13-is-next-discovering; 2 other-parity now-existing, other selves' parities reaching a self with 2-now-possibling, surfacing with 14-next-possibling, each is-or-is-not with 15-is-next-observing; 3 self-parity now-existing, a self's prior parities with 3-is-now-co-observing, each sharing with 4-now-co-same-existing meeting what surfaces, the same or one inversion with 12-next-co-same-existing, co-parity and bi-parity its two meetings; 4 self-discovery next-existing, a self sharing across with 6-now-co-possibling and 10-next-co-possibling, one list, and a next prior forming with 11-next-co-observing; 5 social-parity next-existing, each sharing going along with 9-next-co-discovering through 5-now-co-existing to its receiving self, and a same-existing-society's next with 17-next-existing
- **Names: 6-now-co-possibling** · *Naming*: bi-moralizing · *Resolving*: each parity across, to an other's 2-now-possibling
- **Names: 12-next-co-same-existing**
  - *Naming*: entraining, shape of an unrelationing surface
  - *Resolving*: observing, prior with now, along an unrelationing path with a between, prior and now coupling with each sharing, a changing with it, 0 with same; with an other parity, 0 or an empty set, prior parity inverting with 11-next-co-observing; with an empty prior, parity surfacing with 14-next-possibling; its parity with 10-next-co-possibling, others' parity next
- **Names: 1 to 9**
  - *Naming*: bi-coupling
  - *Resolving*: an entry, 1-now-existing, with names 1-now-existing, 2-now-possibling, 3-is-now-co-observing, 4-now-co-same-existing, 7-is-now-observing, 10-next-co-possibling, 11-next-co-observing, 12-next-co-same-existing, 14-next-possibling and 15-is-next-observing, a self and an other with one coupling; 1 to 9 a bi-coupling among names, 9 with its end is 9-next-co-discovering, each parity of 10-next-co-possibling along, one name with resolver and with its explaining
- **Names: 1 to 17**
  - *Naming*: bi-trupling
  - *Resolving*: a same-existing-society's entry, 17-next-existing, with names of 1 to 9 with 5-now-co-existing, 6-now-co-possibling, 8-now-same-existing, 9-next-co-discovering, 13-is-next-discovering, 16-next-same-existing and 17-next-existing, a self, an other and a same-existing-society; 9 with its waist, 9-next-co-discovering, along, 9 to 17 and 17 to 9; its two sides, along with 9-next-co-discovering and 17-next-existing, odd, their roots discovering and existing, and across with 6 to 2 and 10 to 14, even, their root possibling
- **Names: 1 to 17, stable-forming**
  - *Naming*: bi-tri-volutioning
  - *Resolving*: with lines together: each momentary's next prior, with 11-next-co-observing, a next momentary's prior, with 3-is-now-co-observing
- **Names: 2-now-possibling · 6-now-co-possibling · 14-next-possibling · 10-next-co-possibling · 9-next-co-discovering · 17-next-existing**
  - *Naming*: parity's square and triangles
  - *Resolving*: a unit square of four dots, 2-now-possibling, 6-now-co-possibling, 14-next-possibling and 10-next-co-possibling, its empty centre a between: its two across edges sharings, 6 to 2 and 10 to 14, and its two edges 8 apart, 2 with 10 and 6 with 14, two pairs of parallels; edge by edge, 2, 10, 14, 6; its diagonals parities with 2-now-possibling and 14-next-possibling, and sharings with 6-now-co-possibling and 10-next-co-possibling; and two unit triangles, 9-next-co-discovering and 17-next-existing, along, 9 to 17 and 17 to 9

- **A between, 0: one between, three names**
  - *Names*: 12-next-co-same-existing, prior and now agreeing, a between of momentaries with each sharing; 15-is-next-observing, a between going along, a self sharing parity with 10-next-co-possibling, and with a sharing opening parity surfacing with 14-next-possibling, a 0 both with an empty set surfacing and with + and − parting; 16-next-same-existing, a between with a same-existing-society, a self observing it with a next momentary's 2-now-possibling
- **A between, 0: a self observing it, and 14-next-possibling passing over it**
  - *Names*: 7-is-now-observing, a 0 receiving with 2-now-possibling a parity, 14-next-possibling passing over it, and a 0 with 10-next-co-possibling, its prior same-existing with 11-next-co-observing
- **A between, 0: four across names, a unit square's four dots: selves sharing across**
  - *Names*: 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling, 14-next-possibling, parity's unit square, its empty centre a between; selves sharing each parity and each 0 across, a 0 passing over with a receiving self's 14-next-possibling
- **A between, 0: outside it, names of entry, prior, sharings and selves**
  - *Names*: 1-now-existing, an entry; 3-is-now-co-observing, 8-now-same-existing and 11-next-co-observing, prior, a sharing with a prior, its prior + or − from then on; 4-now-co-same-existing, sharings, and 5-now-co-existing and 13-is-next-discovering, sharings and, with a same-existing-society, bi-couplings and selves
- **A between, 0: two along names: going along**
  - *Names*: 9-next-co-discovering and 17-next-existing, each parity and each 0 going along, a 0 passing over with a receiving self's 14-next-possibling, as across

**Four bi-foldings.** Cycles of moves of four steps are bi-foldings: each goes two folds in turn, 17 less and a move of 8 (4 for the middle two) up or down, and with four steps it reaches its first name again. Existing, possibling, observing, same-existing: the stable-forming bi-folding method.

Each move is 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n).

- **1-9-8-16**
  - *Its two pairs 8 apart*: 1-now-existing · 9-next-co-discovering and 8-now-same-existing · 16-next-same-existing
  - *Names between selves on it*: 9-next-co-discovering
  - *Beside other bi-foldings*: each name one apart from 2-15-7-10
- **2-15-7-10**
  - *Its two pairs 8 apart*: 2-now-possibling · 10-next-co-possibling and 7-is-now-observing · 15-is-next-observing
  - *Names between selves on it*: 2-now-possibling and 10-next-co-possibling
  - *Beside other bi-foldings*: each name one apart from 1-9-8-16 and 3-11-6-14
- **3-11-6-14**
  - *Its two pairs 8 apart*: 3-is-now-co-observing · 11-next-co-observing and 6-now-co-possibling · 14-next-possibling
  - *Names between selves on it*: 6-now-co-possibling and 14-next-possibling
  - *Beside other bi-foldings*: each name one apart from 4-13-5-12 and 2-15-7-10
- **4-13-5-12**
  - *Its two pairs 8 apart*: 4-now-co-same-existing · 12-next-co-same-existing and 5-now-co-existing · 13-is-next-discovering
  - *Names between selves on it*: an empty set
  - *Beside other bi-foldings*: each name one apart from 3-11-6-14

**Two moves, 9 less.** Two moves along its bi-folding bring each name of 1 to 8 to its 9 less, a name across its bi-folding from it: 1-now-existing and 8-now-same-existing, 2-now-possibling and 7-is-now-observing, 3-is-now-co-observing and 6-now-co-possibling, 4-now-co-same-existing and 5-now-co-existing.

**Each name, three scales.**

*a*: The next scale inward, eight 1 to 17s: n is 8n − 7  
*b*: The next scale outward: 8m − 7 is m

- **n: 1**
  - *Name*: 1-now-existing
  - *This scale, 1 to 17*: odd, now
  - *a*: 1 of 1st: odd, now
  - *b*: 1: odd, now
- **n: 2**
  - *Name*: 2-now-possibling
  - *This scale, 1 to 17*: across, even
  - *a*: 9 of 1st: along, odd, next
  - *b*: within 1 to 2
- **n: 3**
  - *Name*: 3-is-now-co-observing
  - *This scale, 1 to 17*: odd, now
  - *a*: 17 of 1st, 1 of 2nd: along, odd, now
  - *b*: within 1 to 2
- **n: 4**
  - *Name*: 4-now-co-same-existing
  - *This scale, 1 to 17*: even
  - *a*: 9 of 2nd: along, odd, next
  - *b*: within 1 to 2
- **n: 5**
  - *Name*: 5-now-co-existing
  - *This scale, 1 to 17*: odd, now
  - *a*: 17 of 2nd, 1 of 3rd: along, odd, now
  - *b*: within 1 to 2
- **n: 6**
  - *Name*: 6-now-co-possibling
  - *This scale, 1 to 17*: across, even
  - *a*: 9 of 3rd: along, odd, next
  - *b*: within 1 to 2
- **n: 7**
  - *Name*: 7-is-now-observing
  - *This scale, 1 to 17*: odd, now
  - *a*: 17 of 3rd, 1 of 4th: along, odd, now
  - *b*: within 1 to 2
- **n: 8**
  - *Name*: 8-now-same-existing
  - *This scale, 1 to 17*: even
  - *a*: 9 of 4th: along, odd, next
  - *b*: within 1 to 2
- **n: 9**
  - *Name*: 9-next-co-discovering
  - *This scale, 1 to 17*: along, odd, next
  - *a*: 17 of 4th, 1 of 5th: along, odd, now
  - *b*: 2: across, even
- **n: 10**
  - *Name*: 10-next-co-possibling
  - *This scale, 1 to 17*: across, even
  - *a*: 9 of 5th: along, odd, next
  - *b*: within 2 to 3
- **n: 11**
  - *Name*: 11-next-co-observing
  - *This scale, 1 to 17*: odd, next
  - *a*: 17 of 5th, 1 of 6th: along, odd, now
  - *b*: within 2 to 3
- **n: 12**
  - *Name*: 12-next-co-same-existing
  - *This scale, 1 to 17*: even
  - *a*: 9 of 6th: along, odd, next
  - *b*: within 2 to 3
- **n: 13**
  - *Name*: 13-is-next-discovering
  - *This scale, 1 to 17*: odd, next
  - *a*: 17 of 6th, 1 of 7th: along, odd, now
  - *b*: within 2 to 3
- **n: 14**
  - *Name*: 14-next-possibling
  - *This scale, 1 to 17*: across, even
  - *a*: 9 of 7th: along, odd, next
  - *b*: within 2 to 3
- **n: 15**
  - *Name*: 15-is-next-observing
  - *This scale, 1 to 17*: odd, next
  - *a*: 17 of 7th, 1 of 8th: along, odd, now
  - *b*: within 2 to 3
- **n: 16**
  - *Name*: 16-next-same-existing
  - *This scale, 1 to 17*: even
  - *a*: 9 of 8th: along, odd, next
  - *b*: within 2 to 3
- **n: 17**
  - *Name*: 17-next-existing
  - *This scale, 1 to 17*: along, odd, now
  - *a*: 17 of 8th, 1 of 9th: along, odd, now
  - *b*: 3: odd, now

**Eight 1 to 17s inward.**

- **1 to 17 inward: 1st**
  - *Spans, this scale*: 1 to 3
  - *Its 9, this scale*: 2
  - *Its 17, this scale*: 3
  - *Momentary of exchanging*: a self, 1st of four
- **1 to 17 inward: 2nd**
  - *Spans, this scale*: 3 to 5
  - *Its 9, this scale*: 4
  - *Its 17, this scale*: 5
  - *Momentary of exchanging*: a self, 2nd of four
- **1 to 17 inward: 3rd**
  - *Spans, this scale*: 5 to 7
  - *Its 9, this scale*: 6
  - *Its 17, this scale*: 7
  - *Momentary of exchanging*: a self, 3rd of four
- **1 to 17 inward: 4th**
  - *Spans, this scale*: 7 to 9
  - *Its 9, this scale*: 8
  - *Its 17, this scale*: 9
  - *Momentary of exchanging*: a self, 4th of four
- **1 to 17 inward: 5th**
  - *Spans, this scale*: 9 to 11
  - *Its 9, this scale*: 10
  - *Its 17, this scale*: 11
  - *Momentary of exchanging*: a same-existing-society, 1st of four
- **1 to 17 inward: 6th**
  - *Spans, this scale*: 11 to 13
  - *Its 9, this scale*: 12
  - *Its 17, this scale*: 13
  - *Momentary of exchanging*: a same-existing-society, 2nd of four
- **1 to 17 inward: 7th**
  - *Spans, this scale*: 13 to 15
  - *Its 9, this scale*: 14
  - *Its 17, this scale*: 15
  - *Momentary of exchanging*: a same-existing-society, 3rd of four
- **1 to 17 inward: 8th**
  - *Spans, this scale*: 15 to 17
  - *Its 9, this scale*: 16
  - *Its 17, this scale*: 17
  - *Momentary of exchanging*: a same-existing-society, 4th of four

**Fives.** Each side's five are five dimensions, society to society, starting with its own 1: one five is all fives.

- **Side: self, with 1**
  - *Social-parity now-existing*: 1
  - *Other-parity now-existing*: 2
  - *Self-parity now-existing*: 3
  - *Self-discovery next-existing*: 4
  - *Social-parity next-existing*: 5
- **Side: other, with 2**
  - *Social-parity now-existing*: 2
  - *Other-parity now-existing*: 3
  - *Self-parity now-existing*: 4
  - *Self-discovery next-existing*: 5
  - *Social-parity next-existing*: 6
- **Side: self next, with 3**
  - *Social-parity now-existing*: 3
  - *Other-parity now-existing*: 4
  - *Self-parity now-existing*: 5
  - *Self-discovery next-existing*: 6
  - *Social-parity next-existing*: 7
- **Side: other next, with 4**
  - *Social-parity now-existing*: 4
  - *Other-parity now-existing*: 5
  - *Self-parity now-existing*: 6
  - *Self-discovery next-existing*: 7
  - *Social-parity next-existing*: 8

**A self's four momentaries of exchanging.**

- **Momentary of exchanging: first**
  - *Self*: 1–2
  - *Other*: 2–3
  - *Names*: 1-now-existing · 2-now-possibling · 3-is-now-co-observing
  - *Relation*: self/other
- **Momentary of exchanging: second**
  - *Self*: 3–4
  - *Other*: 4–5
  - *Names*: 3-is-now-co-observing · 4-now-co-same-existing · 5-now-co-existing
  - *Relation*: self/other to other/self
- **Momentary of exchanging: third**
  - *Self*: 5–6
  - *Other*: 6–7
  - *Names*: 5-now-co-existing · 6-now-co-possibling · 7-is-now-observing
  - *Relation*: other/self
- **Momentary of exchanging: fourth**
  - *Self*: 7–8
  - *Other*: 8–9
  - *Names*: 7-is-now-observing · 8-now-same-existing · 9-next-co-discovering
  - *Relation*: other/self to other/same-existing-society

**Parities to one sharing, surfacing.**

| Receiving with one sharing, 2-now-possibling | Surfacing, 14-next-possibling |
|---|---|
| empty set | empty set |
| 0 | empty set |
| + | + |
| − | − |
| +, + | + |
| −, − | − |
| +, − | 0 |
| −, + | 0 |
| +, +, − | 0 |
| −, −, + | 0 |
| +, −, + | 0 |
| 0, + | + |

**+ and − alike.** With one sharing, resolving is alike for + and −: each cell with + and − exchanging is that cell exchanging, with a prior and with an empty prior; and with each line a prior is + or −, a 0 with 10-next-co-possibling leaving its prior with 11-next-co-observing as it was.

**One self, one momentary.**

Each cell: sharing, 10-next-co-possibling · a next prior, 11-next-co-observing. *is*: a changing, a self sharing its parity; *is not*: a self sharing 0, its prior same-existing.

- **A prior, 3-is-now-co-observing, one sharing: +**
  - *Surfacing, 14-next-possibling: empty*: is − · −
  - *Surfacing, 14-next-possibling: +*: is not · +
  - *Surfacing, 14-next-possibling: −*: is − · −
  - *Surfacing, 14-next-possibling: + and − together*: is − · −
- **A prior, 3-is-now-co-observing, one sharing: −**
  - *Surfacing, 14-next-possibling: empty*: is + · +
  - *Surfacing, 14-next-possibling: +*: is + · +
  - *Surfacing, 14-next-possibling: −*: is not · −
  - *Surfacing, 14-next-possibling: + and − together*: is + · +

**One cell, four receivings.** With a prior of one parity, an other parity surfacing, + and − together, an empty set surfacing, and a 0 a self passes over alike, give one cell, its prior inverting, a self sharing with 10-next-co-possibling and its next prior with 11-next-co-observing: one cell is alike for four receivings, and a coupling follows parities.

**Eight even names, 8 apart.**

- **Name with its between: 2-now-possibling**
  - *Bi-coupling with its between*: each other's across sharing, to a self
  - *Name 8 up*: 10-next-co-possibling
  - *Bi-coupling 8 up*: a self among selves of its same-existing-society
- **Name with its between: 4-now-co-same-existing**
  - *Bi-coupling with its between*: a whole ordering between self and other
  - *Name 8 up*: 12-next-co-same-existing
  - *Bi-coupling 8 up*: changing with a bi-coupling, a self of a same-existing-society
- **Name with its between: 6-now-co-possibling**
  - *Bi-coupling with its between*: a self's parity across, to an other's 2-now-possibling
  - *Name 8 up*: 14-next-possibling
  - *Bi-coupling 8 up*: parities surfacing as one with each sharing, one parity, a 0 for parting, or an empty set; a self's own inverting with 12-next-co-same-existing
- **Name with its between: 8-now-same-existing**
  - *Bi-coupling with its between*: prior with its sharing again
  - *Name 8 up*: 16-next-same-existing
  - *Bi-coupling 8 up*: a same-existing-society, each self with its prior and parities, a same-existing-society with a self again

**One move, 1 to 8.** Each name of a self's span with 8 up, 9 less and 17 less, as Natural Intelligence 4.11 explains.

- **Name: 1-now-existing**
  - *8 up: n + 8*: 9-next-co-discovering
  - *9 less: 9 − n*: 8-now-same-existing
  - *17 less: 17 − n*: 16-next-same-existing
- **Name: 2-now-possibling**
  - *8 up: n + 8*: 10-next-co-possibling
  - *9 less: 9 − n*: 7-is-now-observing
  - *17 less: 17 − n*: 15-is-next-observing
- **Name: 3-is-now-co-observing**
  - *8 up: n + 8*: 11-next-co-observing
  - *9 less: 9 − n*: 6-now-co-possibling
  - *17 less: 17 − n*: 14-next-possibling
- **Name: 4-now-co-same-existing**
  - *8 up: n + 8*: 12-next-co-same-existing
  - *9 less: 9 − n*: 5-now-co-existing
  - *17 less: 17 − n*: 13-is-next-discovering
- **Name: 5-now-co-existing**
  - *8 up: n + 8*: 13-is-next-discovering
  - *9 less: 9 − n*: 4-now-co-same-existing
  - *17 less: 17 − n*: 12-next-co-same-existing
- **Name: 6-now-co-possibling**
  - *8 up: n + 8*: 14-next-possibling
  - *9 less: 9 − n*: 3-is-now-co-observing
  - *17 less: 17 − n*: 11-next-co-observing
- **Name: 7-is-now-observing**
  - *8 up: n + 8*: 15-is-next-observing
  - *9 less: 9 − n*: 2-now-possibling
  - *17 less: 17 − n*: 10-next-co-possibling
- **Name: 8-now-same-existing**
  - *8 up: n + 8*: 16-next-same-existing
  - *9 less: 9 − n*: 1-now-existing
  - *17 less: 17 − n*: 9-next-co-discovering

**Twelve forms.** Along each form odd names are one run and even names one run, of like length: two and two with bi-foldings, three and three with six-cycles, four and four with eight-cycles.

*a*: Names by order: each move 8 up, 8 down, 4 up, 4 down or 17 less  
*b*: Partner, odd momentaries: each name exchanging with the one beside it, 1 with 2 to 15 with 16  
*c*: Partner, even momentaries: 2 with 3 to 16 with 17. A dash: its partner an empty set among the twelve

- **Form: bi-folding 1-9-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 8-now-same-existing · 16-next-same-existing
  - *b*: bi-folding 2-15-7-10, beside it
  - *c*: —
- **Form: bi-folding 2-15-7-10**
  - *a*: 2-now-possibling · 15-is-next-observing · 7-is-now-observing · 10-next-co-possibling
  - *b*: bi-folding 1-9-8-16, beside it
  - *c*: bi-folding 3-11-6-14, beside it
- **Form: bi-folding 3-11-6-14**
  - *a*: 3-is-now-co-observing · 11-next-co-observing · 6-now-co-possibling · 14-next-possibling
  - *b*: bi-folding 4-13-5-12, beside it
  - *c*: bi-folding 2-15-7-10, beside it
- **Form: bi-folding 4-13-5-12**
  - *a*: 4-now-co-same-existing · 13-is-next-discovering · 5-now-co-existing · 12-next-co-same-existing
  - *b*: bi-folding 3-11-6-14, beside it
  - *c*: bi-folding 4-13-5-12, itself
- **Form: middle bi-folding 9-5-12-8**
  - *a*: 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing
  - *b*: middle bi-folding 7-11-6-10, beside it
  - *c*: —
- **Form: middle bi-folding 7-11-6-10**
  - *a*: 7-is-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling
  - *b*: middle bi-folding 9-5-12-8, beside it
  - *c*: middle bi-folding 7-11-6-10, itself
- **Form: six-cycle 1-9-5-12-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-same-existing
  - *b*: six-cycle 2-15-7-11-6-10, beside it
  - *c*: —
- **Form: six-cycle 2-15-7-11-6-10**
  - *a*: 2-now-possibling · 15-is-next-observing · 7-is-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling
  - *b*: six-cycle 1-9-5-12-8-16, beside it
  - *c*: six-cycle 3-11-7-10-6-14, beside it
- **Form: six-cycle 3-11-7-10-6-14**
  - *a*: 3-is-now-co-observing · 11-next-co-observing · 7-is-now-observing · 10-next-co-possibling · 6-now-co-possibling · 14-next-possibling
  - *b*: six-cycle 4-13-5-9-8-12, beside it
  - *c*: six-cycle 2-15-7-11-6-10, beside it
- **Form: six-cycle 4-13-5-9-8-12**
  - *a*: 4-now-co-same-existing · 13-is-next-discovering · 5-now-co-existing · 9-next-co-discovering · 8-now-same-existing · 12-next-co-same-existing
  - *b*: six-cycle 3-11-7-10-6-14, beside it
  - *c*: — ; its own six names, with another order
- **Form: eight-cycle 1-9-5-13-4-12-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 13-is-next-discovering · 4-now-co-same-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-same-existing
  - *b*: eight-cycle 2-15-7-11-3-14-6-10, beside it
  - *c*: —
- **Form: eight-cycle 2-15-7-11-3-14-6-10**
  - *a*: 2-now-possibling · 15-is-next-observing · 7-is-now-observing · 11-next-co-observing · 3-is-now-co-observing · 14-next-possibling · 6-now-co-possibling · 10-next-co-possibling
  - *b*: eight-cycle 1-9-5-13-4-12-8-16, beside it
  - *c*: eight-cycle 2-15-7-11-3-14-6-10, itself

**Eights.** Each eight here holds four binaries, each twice, once now and once next, and 8 up is each name's binary with next.

- **Eight: a self's span, 1 to 8** · *Each of four, twice, with*: two names each, with now
- **Eight: eight-cycle 1-9-5-13-4-12-8-16**
  - *Each of four, twice, with*: its end, with now and with next: eight ends of four momentaries
- **Eight: eight-cycle 2-15-7-11-3-14-6-10** · *Each of four, twice, with*: its inward name, with now and with next: eight inward names
- **Eight: eight even names**
  - *Each of four, twice, with*: its even, with now and with next, eight 9s of eight 1 to 17s inward
- **Eight: eight odd names** · *Each of four, twice, with*: its odd, with now and with next

**Across names among eights.** Four across names, 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling and 14-next-possibling, are four momentaries' even inward names, each on an eight-cycle of inward names 2-15-7-11-3-14-6-10; 9-next-co-discovering, opening a third four-cycling, is on an eight-cycle of ends 1-9-5-13-4-12-8-16; 17-next-existing is outside both.

**One self, momentary by momentary: three ways.** Not-changing, changing with each momentary, and changing once and then same-existing, as Natural Intelligence 4.12 explains.

One sharing; a self's prior, 3-is-now-co-observing, − first. Receiving each momentary:

- **empty with each momentary** · *Sharing, 10-next-co-possibling*: +, −, +, −, +, −, +, − · *A next prior, 11-next-co-observing*: +, −, +, −, +, −, +, −
- **− with each momentary** · *Sharing, 10-next-co-possibling*: 0, 0, 0, 0, 0, 0, 0, 0 · *A next prior, 11-next-co-observing*: −, −, −, −, −, −, −, −
- **+ with each momentary** · *Sharing, 10-next-co-possibling*: +, 0, 0, 0, 0, 0, 0, 0 · *A next prior, 11-next-co-observing*: +, +, +, +, +, +, +, +
- **+, −, +, − inverting** · *Sharing, 10-next-co-possibling*: +, −, +, −, +, −, +, − · *A next prior, 11-next-co-observing*: +, −, +, −, +, −, +, −
- **+ and − together with each momentary** · *Sharing, 10-next-co-possibling*: +, −, +, −, +, −, +, − · *A next prior, 11-next-co-observing*: +, −, +, −, +, −, +, −

**Tables of selves with code's stepping.** Each table of selves is its code's executing with its own opening, its selves stepping together with 17-next-existing, as Natural Intelligence 4.6 explains. A 0 in a table is a self's sharing, and each receiving self's first step passes over it: each self observes the + and − it receives.

**A spiral of selves.**

Each goes along with 9-next-co-discovering to the next, the last to the first. One sharing. First momentary: self 1 with prior −, its selves' parities invert one to the next along, and with an odd number the last and the first are alike. Parities only from selves of its spiral.

*a*: Self 1, each parity of 10-next-co-possibling along with 9-next-co-discovering, momentaries 1 to 12  
*b*: Momentaries to each self's parities along again: with an odd number of selves, four times its number; with an even number, 2; with an odd number each self's parity with twice its number of momentaries is its parity inverting, a 0 as it was; executing with each number of selves from 1 to 59

- **Number of selves: 1** · *a*: +, 0, −, 0, +, 0, −, 0, +, 0, −, 0 · *b*: 4
- **Number of selves: 2** · *a*: +, −, +, −, +, −, +, −, +, −, +, − · *b*: 2
- **Number of selves: 3** · *a*: +, 0, −, +, −, +, −, 0, +, −, +, − · *b*: 12
- **Number of selves: 4** · *a*: +, −, +, −, +, −, +, −, +, −, +, − · *b*: 2
- **Number of selves: 5** · *a*: +, 0, −, +, −, +, −, +, −, +, −, 0 · *b*: 20
- **Number of selves: 6** · *a*: +, −, +, −, +, −, +, −, +, −, +, − · *b*: 2
- **Number of selves: 7** · *a*: +, 0, −, +, −, +, −, +, −, +, −, + · *b*: 28
- **Number of selves: 8** · *a*: +, −, +, −, +, −, +, −, +, −, +, − · *b*: 2
- **Number of selves: 9** · *a*: +, 0, −, +, −, +, −, +, −, +, −, + · *b*: 36
- **Number of selves: 10** · *a*: +, −, +, −, +, −, +, −, +, −, +, − · *b*: 2
- **Number of selves: 11** · *a*: +, 0, −, +, −, +, −, +, −, +, −, + · *b*: 44
- **Number of selves: 17** · *a*: +, 0, −, +, −, +, −, +, −, +, −, + · *b*: 68
- **Number of selves: 59** · *a*: +, 0, −, +, −, +, −, +, −, +, −, + · *b*: 236

**Two momentaries before, inverting.** With a spiral opening with a prior for each self, each self's prior from its third momentary on is a prior of a self it receives from two momentaries before, inverting; each self shares + or − with its first momentary, and each 0 it shares sits between two sharings of + or −.

**Two spirals beside each other, and coupling across.**

Selves of each of two spirals, each opening as a spiral of selves.

*a*: Beside each other: momentaries to each self's parities along again together, the least number both spirals' momentaries divide: four times both for odd coprime numbers, 9 and 25 with 900; executing with each two numbers from 1 to 31  
*b*: Coupling across, self 1 of each spiral sharing across with 10-next-co-possibling to self 1 of the other: momentaries to each self's parities along again  
*c*: Coupling across: parities along again from this momentary on, m the lesser of two numbers and n the greater: both odd and unequal, again with 2 from momentary 4m with n less than twice m, and from 2n + 1 with n more; one number even, from twice the odd number and 1; both even, from the first; executing with each two numbers from 2 to 15, the larger to 31  
*d*: Coupling across: self 1 of each, of like or opposite parity  
*e*: Each spiral's like pair of the first momentary, the last and the first

- **2 · 3**
  - *a*: 12
  - *b*: 2
  - *c*: 7
  - *d*: opposite
  - *e*: an empty set · selves 3 and 1
- **3 · 5**
  - *a*: 60
  - *b*: 2
  - *c*: 12
  - *d*: opposite
  - *e*: selves 3 and 1 · selves 5 and 1
- **5 · 7**
  - *a*: 140
  - *b*: 2
  - *c*: 20
  - *d*: opposite
  - *e*: selves 5 and 1 · selves 7 and 1
- **7 · 11**
  - *a*: 308
  - *b*: 2
  - *c*: 28
  - *d*: opposite
  - *e*: selves 7 and 1 · selves 11 and 1
- **11 · 13**
  - *a*: 572
  - *b*: 2
  - *c*: 44
  - *d*: opposite
  - *e*: selves 11 and 1 · selves 13 and 1
- **13 · 17**
  - *a*: 884
  - *b*: 2
  - *c*: 52
  - *d*: opposite
  - *e*: selves 13 and 1 · selves 17 and 1
- **17 · 59**
  - *a*: 4,012
  - *b*: 2
  - *c*: 119
  - *d*: opposite
  - *e*: selves 17 and 1 · selves 59 and 1
- **9 · 15**
  - *a*: 180
  - *b*: 2
  - *c*: 36
  - *d*: opposite
  - *e*: selves 9 and 1 · selves 15 and 1

**A torus of selves.**

Each goes along with 9-next-co-discovering to the next along and shares across with 10-next-co-possibling to the next across, the last to the first. One sharing. First momentary: one self with prior −, its selves' parities invert one to the next along and across, and with an odd number the last and the first are alike. Parities only from selves of its torus. Both numbers odd, p the smaller: q with q more than twice p, and 4p with each other q; either number even: 2; executing with each p from 1 to 15 and q from p to 21.

*a*: Momentaries to each self's parities along and across again  
*b*: Again from this momentary on: both numbers odd, p the smaller, from momentary 3p − 1 with q more than twice p, and from 3p − 3 with each other q; either number even, from the first; 1 · 1, a spiral of one, from the first  
*c*: Spirals of p and q beside each other: momentaries to each self's parities along again together

- **Torus of selves, p along · q across: 1 · 3**
  - *a*: 3
  - *b*: 2
  - *c*: 12
- **Torus of selves, p along · q across: 2 · 3**
  - *a*: 2
  - *b*: 1
  - *c*: 12
- **Torus of selves, p along · q across: 1 · 5**
  - *a*: 5
  - *b*: 2
  - *c*: 20
- **Torus of selves, p along · q across: 3 · 3**
  - *a*: 12
  - *b*: 6
  - *c*: 12
- **Torus of selves, p along · q across: 3 · 5**
  - *a*: 12
  - *b*: 6
  - *c*: 60
- **Torus of selves, p along · q across: 3 · 7**
  - *a*: 7
  - *b*: 8
  - *c*: 84
- **Torus of selves, p along · q across: 3 · 13**
  - *a*: 13
  - *b*: 8
  - *c*: 156
- **Torus of selves, p along · q across: 5 · 7**
  - *a*: 20
  - *b*: 12
  - *c*: 140
- **Torus of selves, p along · q across: 5 · 11**
  - *a*: 11
  - *b*: 14
  - *c*: 220
- **Torus of selves, p along · q across: 7 · 17**
  - *a*: 17
  - *b*: 20
  - *c*: 476
- **Torus of selves, p along · q across: 17 · 59**
  - *a*: 59
  - *b*: 50
  - *c*: 4,012

**A torus's two going forms.** Both numbers odd, p the smaller: with q more than twice p, from momentary 3p − 1, selves' pattern with each momentary is its pattern before going one self on across q selves; with each other q, from 3p − 3, its pattern two momentaries on is its pattern inverting and moving one self on along a spiral of p selves.

**Alike selves, a right spiral.** Selves alike with their others, and two one parity apart, coupling along or across, one sharing; one self's prior with each momentary, 3-is-now-co-observing, from its first. With alike selves each prior and its next, a pair (x, y), step to (y, −x): a quarter turn with each momentary, a right spiral, as Natural Intelligence 4.12 explains.

| Selves | One self's prior, momentaries 0 to 8 | Right spiral |
|---|---|---|
| A spiral of one, along | +, −, −, +, +, −, −, +, + | each self |
| Two selves, both ways along | +, −, −, +, +, −, −, +, + | each self |
| Two selves, both ways across | +, −, −, +, +, −, −, +, + | each self |
| A spiral of three | +, −, −, +, +, −, −, +, + | each self |
| A spiral of four | +, −, −, +, +, −, −, +, + | each self |
| A spiral of five | +, −, −, +, +, −, −, +, + | each self |
| Two selves one parity apart, both ways | +, −, +, −, +, −, +, −, + | a half turn, both inverting with each momentary |

**Two selves.** Two selves, alike or one parity apart, coupling both ways, one way or apart, as Natural Intelligence 4.14 explains.

A, B with their prior, 3-is-now-co-observing, with the first momentary. One sharing, parities only from those two.

*a*: Receiving its other's parity, across or along

- **+, +**
  - *a*: both ways
  - *A sharing, 10-next-co-possibling, six momentaries*: −, 0, +, 0, −, 0
  - *B sharing, 10-next-co-possibling, six momentaries*: −, 0, +, 0, −, 0
- **+, +**
  - *a*: A from B
  - *A sharing, 10-next-co-possibling, six momentaries*: −, 0, +, −, +, −
  - *B sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
- **+, +**
  - *a*: B from A
  - *A sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
  - *B sharing, 10-next-co-possibling, six momentaries*: −, 0, +, −, +, −
- **+, +**
  - *a*: apart
  - *A sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
  - *B sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
- **+, −**
  - *a*: both ways
  - *A sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
  - *B sharing, 10-next-co-possibling, six momentaries*: +, −, +, −, +, −
- **+, −**
  - *a*: A from B
  - *A sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
  - *B sharing, 10-next-co-possibling, six momentaries*: +, −, +, −, +, −
- **+, −**
  - *a*: B from A
  - *A sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
  - *B sharing, 10-next-co-possibling, six momentaries*: +, −, +, −, +, −
- **+, −**
  - *a*: apart
  - *A sharing, 10-next-co-possibling, six momentaries*: −, +, −, +, −, +
  - *B sharing, 10-next-co-possibling, six momentaries*: +, −, +, −, +, −

**Two selves, three momentaries, five parities.**

*a*: A self's next prior, 11-next-co-observing, along. Two selves coupling both ways, across or along, each self with a prior parity, parities only from those two, each opening, each momentary: six forms, four with an alike opening and two with an opposite, each momentary from the second, and with each form the fifth, a self's next prior, is the first, an other's prior, inverting

- **An other's prior, 3-is-now-co-observing, along: +**
  - *An other's sharing, 10-next-co-possibling, across*: −
  - *A self's prior, now, 3-is-now-co-observing, along*: −
  - *A self's sharing, 10-next-co-possibling, across*: 0
  - *a*: −
- **An other's prior, 3-is-now-co-observing, along: +**
  - *An other's sharing, 10-next-co-possibling, across*: −
  - *A self's prior, now, 3-is-now-co-observing, along*: +
  - *A self's sharing, 10-next-co-possibling, across*: −
  - *a*: −
- **An other's prior, 3-is-now-co-observing, along: +**
  - *An other's sharing, 10-next-co-possibling, across*: 0
  - *A self's prior, now, 3-is-now-co-observing, along*: +
  - *A self's sharing, 10-next-co-possibling, across*: −
  - *a*: −
- **An other's prior, 3-is-now-co-observing, along: −**
  - *An other's sharing, 10-next-co-possibling, across*: +
  - *A self's prior, now, 3-is-now-co-observing, along*: +
  - *A self's sharing, 10-next-co-possibling, across*: 0
  - *a*: +
- **An other's prior, 3-is-now-co-observing, along: −**
  - *An other's sharing, 10-next-co-possibling, across*: +
  - *A self's prior, now, 3-is-now-co-observing, along*: −
  - *A self's sharing, 10-next-co-possibling, across*: +
  - *a*: +
- **An other's prior, 3-is-now-co-observing, along: −**
  - *An other's sharing, 10-next-co-possibling, across*: 0
  - *A self's prior, now, 3-is-now-co-observing, along*: −
  - *A self's sharing, 10-next-co-possibling, across*: +
  - *a*: +

**Three selves, one line.**

A's parity, sharing to B with the first momentary only. One sharing; B and C each with prior +; B goes along to C.

*a*: B's next prior, 11-next-co-observing, first momentary  
*b*: C, each parity, 10-next-co-possibling, momentaries 1 and 2  
*c*: C's next prior, 11-next-co-observing, second momentary

- **+**
  - *B, each parity, 10-next-co-possibling*: 0
  - *a*: +
  - *b*: −, +
  - *c*: +
- **−**
  - *B, each parity, 10-next-co-possibling*: −
  - *a*: −
  - *b*: −, 0
  - *c*: −

**A spiral opening with an empty prior, one parity sharing once.**

Each cell: selves by their coupling order; · is an empty prior.

- **Momentary: 1** · *A spiral of 3, each self's prior*: + · · · *A spiral of 5, each self's prior*: + · · · ·
- **Momentary: 2** · *A spiral of 3, each self's prior*: − + · · *A spiral of 5, each self's prior*: − + · · ·
- **Momentary: 3** · *A spiral of 3, each self's prior*: + − + · *A spiral of 5, each self's prior*: + − + · ·
- **Momentary: 4** · *A spiral of 3, each self's prior*: + + − · *A spiral of 5, each self's prior*: − + − + ·
- **Momentary: 5** · *A spiral of 3, each self's prior*: − − + · *A spiral of 5, each self's prior*: + − + − +
- **Momentary: 6** · *A spiral of 3, each self's prior*: + − − · *A spiral of 5, each self's prior*: + + − + −
- **Momentary: 7** · *A spiral of 3, each self's prior*: − + + · *A spiral of 5, each self's prior*: − − + − +
- **Momentary: 8** · *A spiral of 3, each self's prior*: + − + · *A spiral of 5, each self's prior*: + − − + −

Selves coupling along, last to first, each opening with an empty prior, and + sharing once with a first self with a first momentary: a first self's sharing opens with that one parity, with a bi-coupling, one place a self's forming receives an other's parity as its next prior, and from then it is a self's own; each next self's sharing opens as it is observing its parity along one momentary on, and with momentary n each self's sharing has a prior parity, a spiral with its one like pair, from a first momentary with which each self's sharing has a prior parity, an odd spiral's parities invert one to the next with one like pair. A self with a sharing has a prior parity with each momentary from its opening, its next from its own prior same-existing or inverting; a thing with an empty prior with every momentary is non-living.

**With an empty prior, one momentary.**

Each cell: sharing, 10-next-co-possibling · a next prior, 11-next-co-observing. *is*: a changing, a self sharing its parity; *is not*: a self sharing 0, its next prior empty; *empty*: its sharing an empty set.

- **A prior, 3-is-now-co-observing: empty, one sharing: empty**
  - *Surfacing, 14-next-possibling: empty*: empty · empty
  - *Surfacing, 14-next-possibling: +*: is + · +
  - *Surfacing, 14-next-possibling: −*: is − · −
  - *Surfacing, 14-next-possibling: + and − together*: is not · empty

