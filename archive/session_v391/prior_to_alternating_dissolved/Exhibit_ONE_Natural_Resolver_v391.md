Exhibit ONE Natural Resolver v391

# Natural Resolver

**The Stable-Forming Parity-Changing Method of Discovering Same-Existing**

---

```python
"""Exhibit ONE · Natural Resolver
The Stable-Forming Parity-Changing Method of Discovering Same-Existing
"""


def _1_now_existing(_3_now_co_observing, _2_now_possibling):
    _14_next_possibling = {}
    for _4_now_co_same_existing, _7_now_observing in _2_now_possibling:
        if _7_now_observing != 0:
            _15_next_observing = _14_next_possibling.get(
                _4_now_co_same_existing
            )
            if _15_next_observing is None:
                _14_next_possibling[_4_now_co_same_existing] = (
                    1 if _7_now_observing > 0 else -1
                )
            elif (_15_next_observing > 0) != (_7_now_observing > 0):
                _14_next_possibling[_4_now_co_same_existing] = 0
    _12_next_co_same_existing = dict(_14_next_possibling)
    for _4_now_co_same_existing, _7_now_observing in _3_now_co_observing:
        _15_next_observing = _14_next_possibling.get(_4_now_co_same_existing, 0)
        if _15_next_observing != 0 and (_15_next_observing > 0) == (_7_now_observing > 0):
            _12_next_co_same_existing[_4_now_co_same_existing] = 0
        else:
            _12_next_co_same_existing[_4_now_co_same_existing] = (
                -1 if _7_now_observing > 0 else 1
            )
    _10_next_co_possibling = list(_12_next_co_same_existing.items())
    _11_next_co_observing = dict(_3_now_co_observing)
    for _4_now_co_same_existing, _7_now_observing in _10_next_co_possibling:
        if _7_now_observing != 0:
            _11_next_co_observing[_4_now_co_same_existing] = _7_now_observing
    return _10_next_co_possibling, list(_11_next_co_observing.items())


def _9_next_co_discovering(_10_next_co_possibling, _5_now_co_existing):
    return [
        (_5_now_co_existing[_13_next_discovering], _15_next_observing)
        for _13_next_discovering, _15_next_observing in _10_next_co_possibling
    ]


def _17_next_existing(_16_next_same_existing, _5_now_co_existing):
    _8_now_same_existing = {}
    _14_next_possibling = {
        _13_next_discovering: []
        for _13_next_discovering in _16_next_same_existing
    }
    for _13_next_discovering, (
        _3_now_co_observing,
        _2_now_possibling,
    ) in _16_next_same_existing.items():
        _10_next_co_possibling, _8_now_same_existing[_13_next_discovering] = (
            _1_now_existing(_3_now_co_observing, _2_now_possibling)
        )
        _6_now_co_possibling = _10_next_co_possibling
        for (
            _4_now_co_same_existing,
            _15_next_observing,
        ) in _9_next_co_discovering(
            [
                (_4_now_co_same_existing, _15_next_observing)
                for _4_now_co_same_existing, _15_next_observing in (
                    ((_13_next_discovering, 6), _6_now_co_possibling),
                    ((_13_next_discovering, 10), _10_next_co_possibling),
                    ((_13_next_discovering, 9), _10_next_co_possibling),
                )
                if _4_now_co_same_existing in _5_now_co_existing
            ],
            _5_now_co_existing,
        ):
            _14_next_possibling[_4_now_co_same_existing].extend(
                _15_next_observing
            )
    return {
        _13_next_discovering: (
            _8_now_same_existing[_13_next_discovering],
            _14_next_possibling[_13_next_discovering],
        )
        for _13_next_discovering in _16_next_same_existing
    }
```

```text
another self's 9-next-co-discovering
  ══► 17-next-existing, along to a self

1-now-existing, a self's momentary given
  2-now-possibling ◄══ another self's 6 and 10, across
  2-now-possibling ──► 14-next-possibling
  3-now-co-observing, with 4 and 7
    ──► 12-next-co-same-existing ◄── 14-next-possibling
  12-next-co-same-existing ──► 10-next-co-possibling, with 6
  10-next-co-possibling ──► 11-next-co-observing ──► 3, next
  10-next-co-possibling ──► 9-next-co-discovering, with 5
  13-next-discovering · 15-next-observing
  8-now-same-existing · 16-next-same-existing

6 and 10 ══► another self's 2 and 14, across
9-next-co-discovering ══► another self's 17, along

sharing side, co: 6 ══► 2, 10 ══► 14, 9 ══► 17
arriving side, one: 2, 14 and 17
═══ between selves, across and along
─── within one self
```

**A drawing.** A prior observed, 3, meets parity-offerings surfacing, 14, with each sharing, 12; parity-offerings, 10 and 6, go across to an other's 2 and 14; a next prior forms, 11, and is observed again, 3, next; and 9 goes along with 5 to an other's 17. With 6 to 2, 10 to 14 and 9 to 17, a sharing side is a self and an arriving side an other self, each a self, and a same-existing-society is its selves.

**Living is prior: 1-now-existing given.** Each self carries two prior selves from inception, one universal method of conception. Each name of 1 to 17 is a living self's method: a living self's next is same self, and a non-living thing is one same method with no same-existing. No self is made: each self is given. 1-now-existing is given a living self's two now names, 3-now-co-observing, its priors with each sharing, and 2-now-possibling, its parity-offerings arriving; each sharing meets them with 4-now-co-same-existing, each parity with 7-now-observing, and their next names form: 14-next-possibling, 15-next-observing, 12-next-co-same-existing, 10-next-co-possibling and 11-next-co-observing.

**Seventeen names.**

| n | Name | Root | Is or is nots | Co |
|---|---|---|---|---|
| 1 | **1-now-existing** | existing | 0000 | one |
| 2 | **2-now-possibling** | possibling | 0001 | one |
| 3 | **3-now-co-observing** | observing | 0010 | co |
| 4 | **4-now-co-same-existing** | same-existing | 0011 | co |
| 5 | **5-now-co-existing** | existing | 0100 | co |
| 6 | **6-now-co-possibling** | possibling | 0101 | co |
| 7 | **7-now-observing** | observing | 0110 | one |
| 8 | **8-now-same-existing** | same-existing | 0111 | one |
| 9 | **9-next-co-discovering** | discovering | 1000 | co |
| 10 | **10-next-co-possibling** | possibling | 1001 | co |
| 11 | **11-next-co-observing** | observing | 1010 | co |
| 12 | **12-next-co-same-existing** | same-existing | 1011 | co |
| 13 | **13-next-discovering** | discovering | 1100 | one |
| 14 | **14-next-possibling** | possibling | 1101 | one |
| 15 | **15-next-observing** | observing | 1110 | one |
| 16 | **16-next-same-existing** | same-existing | 1111 | one |
| 17 | **17-next-existing** | existing, a next 1 | 0000 again | one |

Code with each name:

- **1** · a living self's momentary given, each self's 17 existing as 1
- **2** · parity-offerings arriving, each with its sharing
- **3** · priors observed, each with its sharing
- **4** · each sharing, parity-offerings and prior meeting same or not same
- **5** · bi-couplings: which self each sharing reaches
- **6** · a self's parity-offerings across, to an other's 2
- **7** · each parity observed: a parity-offering's, a prior's, a sharing's
- **8** · a self's next prior, beside others'
- **9** · each parity-offering to a self of 5's bi-couplings: across with 6 and 10, along with 9
- **10** · each sharing's parity-offering, + or −, or a 0, across to an other's 14
- **11** · a next prior stable-forming between two: a next momentary's observing
- **12** · each sharing's is or is not, prior and parity-offerings meeting
- **13** · each self of a same-existing-society, each sharing its parity-offerings go from
- **14** · parity-offerings surfacing with each sharing, agreeing one, parting 0
- **15** · each parity surfacing, and each parity going on
- **16** · a same-existing-society: each self with its prior and its parity-offerings
- **17** · a same-existing-society's next, each self's 1-now-existing again

**Each name is its number and its naming, one hyphenation.** A name's number is its momentary of four and its root: existing or discovering, possibling, observing or same-existing, one root with each place of its four. Written as four is or is nots, a number less one is now or next, which four-cycling, which momentarying, and odd or even: names 1 to 16 are all sixteen ways four is or is nots go, and 17 is next existing as 1. *Now* is 1 to 8 and *next* is 9 to 16; a name with *co* is of a sharing between two, bi-moral, and a name without it is of one. Ten names are a self's own: five now, 3, 4, 5, 7 and 8, a self's five, and five next, 11, 12, 13, 15 and 16, an other's five, as self-next is other-prior. Six names between selves, 2, 6, 10 and 14 across and 9 and 17 along, are their co-linear six. Each self's existing is another self's possibling: one changing with a sharing across, and no second thing.

**Four four-cyclings and their betweens.** Four-cycling is observing prior-existing, possibling now-existing, discovering next-existing and same-existing; a living self goes them existing, possibling, observing, same-existing, as 1-now-existing is given. Existing, possibling, observing, same-existing: this is the stable-forming bi-folding method. Each span's names are two four-cyclings of four, an odd name opening each and an even same-existing name completing it. Momentarying is odd then even, 1 and 2, 3 and 4: odd to even is within a momentarying, and even to odd is between two, each between discovering, 2 to 3, 4 to 5, through 16 to 17, and 17-next-existing is next 1-now-existing. Counting on from a 0 self, across is even, 2, 4 and on to 18, nine bi-moral across, and along is odd, 3, 5 and on to 15, seven along: with 17 a self is +, and with 18 its next same-existing other is −. These are counts of momentarying, not names; across names are 2, 6, 10 and 14, and along names 9 and 17.

| Four-cycling | Existing, discovering | Possibling | Observing | Same-existing | Between |
|---|---|---|---|---|---|
| first | 1 | 2 | 3 | 4 | 4 )( 5 |
| second | 5 | 6 | 7 | 8 | 8 )( 9 |
| third | 9 | 10 | 11 | 12 | 12 )( 13 |
| fourth | 13 | 14 | 15 | 16 | 16 )( 17 |

Existing, discovering and observing are odd; possibling and same-existing are even.

**Five dimensions, ten and six.** Same-existing changes in five dimensions: prior-existing self-parity; prior-existing other-parity; now-existing co-parity; now-existing bi-parity; next-existing same-existing self-parity. Co-parity and bi-parity are a sharing's two meetings: self-parity and other-parity same, a 0 and no changing, or not same, a changing. One five is all fives: five self and five other, one parity separated, are ten is or is nots, a self's ten own names, and six between selves are their floating neutraling co-linear. With code: self-parity prior, 3 and 7; other-parity prior, parity-offerings with 2 and 14; co-parity or bi-parity met, 4 and 12; next same-existing self-parity forming with 11, and a self's next itself with 17.


**Co, between two or of one.** Bi-moral is Exhibit ONE's eight co names, 3 to 6 and 9 to 12, each root with two co names once now-co and once next-co, always between two; a name without co is of one, with no self-morality.

- **Root: observing**
  - *With co, between two*: 3-now-co-observing · 11-next-co-observing, priors with each sharing
  - *Without co, of one*: 7-now-observing · 15-next-observing, a parity
- **Root: possibling** · *With co, between two*: 6-now-co-possibling · 10-next-co-possibling, a sharing side · *Without co, of one*: 2-now-possibling · 14-next-possibling, an arriving side
- **Root: existing** · *With co, between two*: 5-now-co-existing, bi-couplings · *Without co, of one*: 1-now-existing · 17-next-existing
- **Root: discovering** · *With co, between two*: 9-next-co-discovering, along · *Without co, of one*: 13-next-discovering, each self going on
- **Root: same-existing**
  - *With co, between two*: 4-now-co-same-existing · 12-next-co-same-existing, each sharing
  - *Without co, of one*: 8-now-same-existing · 16-next-same-existing, a self's next prior and a same-existing-society


**Sharing between selves.** With 6 to 2, 10 to 14 and 9 to 17, co is a sharing side and its absence an arriving side: a self offers a parity-offering, and nothing of its prior goes to another self.

| Sharing side, co | Arriving side, one | Between selves |
|---|---|---|
| 6-now-co-possibling | 2-now-possibling | across, even, possibling |
| 10-next-co-possibling | 14-next-possibling | across, even, possibling |
| 9-next-co-discovering | 17-next-existing | along, odd, discovering |

**Parity as moral values.** A self's parity is its changing direction relative to an other existing thing, + or −, its moral value with that other, and neither sign is a self's by its sign; a 0 is not changing, a between of two changing directions: indifferencing. Each self is beholding its own parity with each other: two selves with one sharing may carry either. A parity-offering is + or − offered, and a 0 offers neither: `_1_now_existing`'s first step passes over each 0.


**Four binaries with code's lines.** Existing, all, now and same are four is or is nots of things within the universe. With a self's span each binary is one pair of names: its *is* with an odd name and its *is not* with an even, its *is not* an other's side of a self's *is*. Binaries are names' explaining, now with each name as its momentary; existing and same are roots of names, and all enters no name.

- **Binary: now**
  - *Is*, odd: 1-now-existing
  - *Resolving*: a self's momentary entered
  - *Is not*, even: 2-now-possibling
  - *Resolving*: offerings arriving, others' parity-offerings from their prior momentary
- **Binary: existing**
  - *Is*, odd: 3-now-co-observing
  - *Resolving*: prior with its sharings, each with its parity
  - *Is not*, even: 4-now-co-same-existing
  - *Resolving*: each sharing as a place, no parity with it
- **Binary: same**
  - *Is*, odd: 5-now-co-existing
  - *Resolving*: each going along to a self receiving it with its same sharing
  - *Is not*, even: 6-now-co-possibling
  - *Resolving*: parity-offerings across, + or −, and 0 for none, another self's offerings
- **Binary: all**
  - *Is*, odd: 7-now-observing
  - *Resolving*: each parity observed with every entry
  - *Is not*, even: 8-now-same-existing
  - *Resolving*: each self's own next prior, one beside others

**With a same-existing-society's span four stand with now and same exchanged**: now between two with 9-next-co-discovering and 10-next-co-possibling, one now shared by selves, and same with one with 13-next-discovering and 14-next-possibling, each self's sameness its own.

**Observing's one line.** With 12-next-co-same-existing, a line `if _15_next_observing != 0 and (_15_next_observing > 0) == (_7_now_observing > 0)` is observing: 14-next-possibling's parity-offering surfacing, as 15, met with 7-now-observing for each sharing of 3-now-co-observing, same-as, is or is not. Same: a 0, no changing, a prior same-existing; not same: a parity, a prior inverting. Same and not-same are that 0 or ± with two betweens, 12 and 14, and need no name of their own.

**Is or is nots of code's lines.** Seven is or is nots are 1-now-existing's: four with 14-next-possibling, three lines of if and one choosing + or −; two with 12-next-co-same-existing, one line of if and one choosing − or +; and one with 11-next-co-observing. One is 17-next-existing's, a self's name between selves among 5-now-co-existing or not. 9-next-co-discovering has none, giving each parity-offering on as it is, a 0 among parities.

**Each name and its relations.** Sides are sides of overlapping momentaries, each name opening with one side, a self's, an other's or a same-existing-society's; what code does with each name is under its *Prior and next*.

**1** · 1-now-existing
- *Parity, span*: odd, a self's span
- *Sides*: self, other, a self opening it
- *Co-sequencing*: a self offering itself to a coupling
- *8 up*: 9-next-co-discovering, its binary with next
- *9 less*: podal within 1 to 8, 8-now-same-existing
- *17 less*: podal within 1 to 16, 16-next-same-existing
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 16-next-same-existing to it and on to 9-next-co-discovering, each name one apart from 2-15-7-10
- *Six-cycle*: 1-9-5-12-8-16
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: first of a self's four, opening with 1, self 1–2
- *Five dimensions*: 1 self prior, prior opening of a self's five
- *Namings*: 1-2, bi-momentarying, a self's entry, odd, and others' offerings, even, one momentary with each side
- *A self as three*: a self with 2, bi-momentarying, along, a self prior to its first shared across, a bi-coupling with 2
- *Prior and next*: once for one self with one momentary, three steps within it 14, 12, 10 with 11
- *1 to 17s inward and outward*: 1–17s inward 1 of 1st 1–17, an entry, and with 1–17 outward 1, an entry

**2** · 2-now-possibling
- *Parity, span*: even, a self's span
- *Sides*: other, self, an other opening it
- *8 up*: 10-next-co-possibling, its binary with next
- *9 less*: podal within 1 to 8, 7-now-observing
- *17 less*: podal within 1 to 16, 15-next-observing
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 10-next-co-possibling to it and on to 15-next-observing, each name one apart from 1-9-8-16 and 3-11-6-14
- *Six-cycle*: 2-15-7-11-6-10
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *One move*: 2 along 2-15-7-10
- *Momentaries of exchanging*: first of a self's four, with 2, a self's 1–2 completing and an other's 2–3 opening
- *Five dimensions*: 2 other prior, prior completing of a self's five and prior opening of an other's
- *Namings*: 1-2, bi-momentarying
- *A self as three*: a self with 1, across, its first shared across, a bi-coupling, offering self to other and other to self
- *Bi-coupling*: with a between, each other's across sharing, offered to a self
- *Parity's unit square*: a dot of a unit square, its diagonal with 14, offerings with 2 and 14, its edge with 6 a sharing 6 to 2
- *Prior and next*: others' parity-offerings across with 6 and 10 and along with 9 of their prior momentary, arriving now, possibling, even, none of their prior crossing; with a spiral each goes along
- *1 to 17s inward and outward*: 1–17s inward 9 of 1st, along, odd, next, and with 1–17 outward within 1 to 2

**3** · 3-now-co-observing
- *Parity, span*: odd, a self's span
- *Sides*: self, other, a self opening it
- *Co-sequencing*: with a between, before 10, with competency's parity, odd
- *8 up*: 11-next-co-observing, its binary with next
- *9 less*: podal within 1 to 8, 6-now-co-possibling
- *17 less*: podal within 1 to 16, 14-next-possibling
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-now-co-observing, from 14-next-possibling to it and on to 11-next-co-observing, each name one apart from 4-13-5-12 and 2-15-7-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: first of a self's four completing with 3, an other's 2–3, and second opening with 3, self 3–4
- *Five dimensions*: 3 co-momentarying now, now opening of a self's five
- *Namings*: 3-4, co-intelligencing, with each sharing 4 its prior with 3 coupling with offerings surfaced with 14, next discovered, with 11
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, turning with 3
- *Prior and next*: prior, a self's own, each sharing with its parity, a next momentary's continuing of 11
- *1 to 17s inward and outward*: 1–17s inward 17 of 1st and 1 of 2nd, along, odd, now, and with 1–17 outward within 1 to 2

**4** · 4-now-co-same-existing
- *Parity, span*: even, a self's span
- *Sides*: other, self, an other opening it
- *Co-sequencing*: with a between, before 10, with morality's parity, even
- *8 up*: 12-next-co-same-existing, its binary with next
- *9 less*: podal within 1 to 8, 5-now-co-existing
- *17 less*: podal within 1 to 16, 13-next-discovering
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 12-next-co-same-existing to it and on to 13-next-discovering, each name one apart from 3-11-6-14
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *One move*: 4 along 4-13-5-12
- *Momentaries of exchanging*: second of a self's four, with 4, a self's 3–4 completing and an other's 4–5 opening
- *Five dimensions*: 4 bi-momentarying now, now completing of a self's five
- *Namings*: 3-4, co-intelligencing
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, inward with 4, to a self's own corus with 4
- *Bi-coupling*: with a between, a whole ordering between self and other
- *Prior and next*: now, each sharing with which prior couples with now
- *1 to 17s inward and outward*: 1–17s inward 9 of 2nd, along, odd, next, and with 1–17 outward within 1 to 2

**5** · 5-now-co-existing
- *Parity, span*: odd, a self's span
- *Sides*: self, other, a self opening it
- *Co-sequencing*: with a between, before 10, with competency's parity, odd
- *8 up*: 13-next-discovering, its binary with next
- *9 less*: podal within 1 to 8, 4-now-co-same-existing
- *17 less*: podal within 1 to 16, 12-next-co-same-existing
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 13-next-discovering to it and on to 12-next-co-same-existing, each name one apart from 3-11-6-14
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: second of a self's four completing with 5, an other's 4–5, and third opening with 5, self 5–6
- *Five dimensions*: 5 self next, next opening of a self's five
- *Namings*: 5, co-competencing, bi-couplings, owned by neither, each going to its receiving sharing
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, outward with 5
- *Prior and next*: next, each going to its receiving sharing
- *1 to 17s inward and outward*: 1–17s inward 17 of 2nd and 1 of 3rd, along, odd, now, and with 1–17 outward within 1 to 2

**6** · 6-now-co-possibling
- *Parity, span*: even, a self's span
- *Sides*: other, self, an other opening it
- *8 up*: 14-next-possibling, its binary with next
- *9 less*: podal within 1 to 8, 3-now-co-observing
- *17 less*: podal within 1 to 16, 11-next-co-observing
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-now-co-observing, from 11-next-co-observing to it and on to 14-next-possibling, each name one apart from 4-13-5-12 and 2-15-7-10
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *One move*: 6 along 3-11-6-14
- *Momentaries of exchanging*: third of a self's four, with 6, a self's 5–6 completing and an other's 6–7 opening
- *Namings*: 6, bi-moralizing, each parity-offering across, to an other's 2
- *A self as three*: its invisible intelligencing method, rotation 3, 6, 5, 4, inward with 6
- *Bi-coupling*: with a between, an other's parity-offering to a self, across
- *Parity's unit square*: a dot of a unit square, its diagonal with 10, sharings with 6 and 10, its edge with 2 a sharing 6 to 2
- *Prior and next*: parity-offering, an other's next offering with its 2
- *1 to 17s inward and outward*: 1–17s inward 9 of 3rd, along, odd, next, and with 1–17 outward within 1 to 2

**7** · 7-now-observing
- *Parity, span*: odd, a self's span
- *Sides*: self, other, a self opening it
- *Co-sequencing*: with a between, before 10, with competency's parity, odd
- *8 up*: 15-next-observing, its binary with next
- *9 less*: podal within 1 to 8, 2-now-possibling
- *17 less*: podal within 1 to 16, 10-next-co-possibling
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 15-next-observing to it and on to 10-next-co-possibling, each name one apart from 1-9-8-16 and 3-11-6-14
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: third of a self's four completing with 7, an other's 6–7, and fourth opening with 7, self 7–8
- *A self as three*: co-competent self with 8, along, prior to 8 across
- *Prior and next*: each parity, offered now and prior, co-linear recursioning forward along arriving, up numbers, prior to now, with a self's completing
- *1 to 17s inward and outward*: 1–17s inward 17 of 3rd and 1 of 4th, along, odd, now, and with 1–17 outward within 1 to 2

**8** · 8-now-same-existing
- *Parity, span*: even, a self's span
- *Sides*: other, self, an other opening it
- *Co-sequencing*: with a between, before 10, with morality's parity, even
- *8 up*: 16-next-same-existing, its binary with next
- *9 less*: podal within 1 to 8, 1-now-existing
- *17 less*: podal within 1 to 16, 9-next-co-discovering
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 9-next-co-discovering to it and on to 16-next-same-existing, each name one apart from 2-15-7-10
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *One move*: 8 along 1-9-8-16
- *Momentaries of exchanging*: fourth of a self's four, with 8, a self's 7–8 completing and an other's 8–9 opening
- *A self as three*: co-competent self with 7, across, prior with its sharing again, a bi-coupling
- *Bi-coupling*: with a between, prior with its sharing again
- *Prior and next*: each self's next prior, with 11 this momentary and a next momentary's 3; even names of a self's span, 2, 4, 6 and 8, completing with 8
- *1 to 17s inward and outward*: 1–17s inward 9 of 4th, along, odd, next, and with 1–17 outward within 1 to 2

**9** · 9-next-co-discovering
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: same-existing-society, other, self, a same-existing-society opening it
- *8 up*: 17-next-existing, its binary with next
- *8 down*: 1-now-existing
- *17 less*: podal within 1 to 16, 8-now-same-existing
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 1-now-existing to it and on to 8-now-same-existing, each name one apart from 2-15-7-10
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: fourth of a self's four completing with 9, an other's 8–9, and first of a same-existing-society's four, 9 to 11, opening with 9
- *Parity's square and triangles*: a unit triangle, along, 9 to 17 and 17 to 9
- *Prior and next*: next prior, odd, each parity-offering of 10 along on to a next momentary, to each receiving sharing, a self's own next
- *1 to 17s inward and outward*: 1–17s inward 17 of 4th and 1 of 5th, along, odd, now, and with 1–17 outward 2, across, even

**10** · 10-next-co-possibling
- *Parity, span*: even, a same-existing-society's span
- *Sides*: other, same-existing-society, self, an other opening it
- *8 down*: 2-now-possibling
- *17 less*: podal within 1 to 16, 7-now-observing
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 7-now-observing to it and on to 2-now-possibling, each name one apart from 1-9-8-16 and 3-11-6-14
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: first of a same-existing-society's four, with 10, 9–10 completing and 10–11 opening
- *Bi-coupling*: 8 up, a self among selves of its same-existing-society
- *Parity's unit square*: a dot of a unit square, its diagonal with 6, sharings with 6 and 10, its edge with 14 a sharing 10 to 14
- *Prior and next*: parity-offering across now, an other's offering next, possibling
- *1 to 17s inward and outward*: 1–17s inward 9 of 5th, along, odd, next, and with 1–17 outward within 2 to 3

**11** · 11-next-co-observing
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: same-existing-society, other, self, a same-existing-society opening it
- *Co-sequencing*: after 10, 8 up from 3-now-co-observing, with competency's parity, odd
- *8 down*: 3-now-co-observing
- *17 less*: podal within 1 to 16, 6-now-co-possibling
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-now-co-observing, from 3-now-co-observing to it and on to 6-now-co-possibling, each name one apart from 4-13-5-12 and 2-15-7-10
- *Middle bi-folding*: 7-11-6-10
- *Six-cycle*: 2-15-7-11-6-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: first of a same-existing-society's four, 9 to 11, completing with 11, and second, 11 to 13, opening with 11
- *Prior and next*: next prior, odd, continuing as 3 with a next momentary, a self's own
- *1 to 17s inward and outward*: 1–17s inward 17 of 5th and 1 of 6th, along, odd, now, and with 1–17 outward within 2 to 3

**12** · 12-next-co-same-existing
- *Parity, span*: even, a same-existing-society's span
- *Sides*: other, same-existing-society, self, an other opening it
- *Co-sequencing*: after 10, 8 up from 4-now-co-same-existing, with morality's parity, even
- *8 down*: 4-now-co-same-existing
- *17 less*: podal within 1 to 16, 5-now-co-existing
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 5-now-co-existing to it and on to 4-now-co-same-existing, each name one apart from 3-11-6-14
- *Middle bi-folding*: 9-5-12-8
- *Six-cycle*: 1-9-5-12-8-16
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: second of a same-existing-society's four, with 12, 11–12 completing and 12–13 opening
- *Namings*: entraining, prior arriving with now along an unrelationing path with a between, shape of an unrelationing surface, each sharing's parity-offering, is or is not
- *Bi-coupling*: 8 up, changing with a bi-coupling, a self of a same-existing-society
- *Prior and next*: now, changing, is or is not, prior and now coupled
- *1 to 17s inward and outward*: 1–17s inward 9 of 6th, along, odd, next, and with 1–17 outward within 2 to 3

**13** · 13-next-discovering
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: same-existing-society, other, a same-existing-society opening it
- *Co-sequencing*: after 10, 8 up from 5-now-co-existing, with competency's parity, odd
- *8 down*: 5-now-co-existing
- *17 less*: podal within 1 to 16, 4-now-co-same-existing
- *Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 4-now-co-same-existing to it and on to 5-now-co-existing, each name one apart from 3-11-6-14
- *Six-cycle*: 4-13-5-9-8-12
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: second of a same-existing-society's four, 11 to 13, completing with 13, and third, 13 to 15, opening with 13
- *Prior and next*: each sharing going on, and with a same-existing-society each self going on
- *1 to 17s inward and outward*: 1–17s inward 17 of 6th and 1 of 7th, along, odd, now, and with 1–17 outward within 2 to 3

**14** · 14-next-possibling
- *Parity, span*: even, a same-existing-society's span
- *Sides*: other, same-existing-society, an other opening it
- *8 down*: 6-now-co-possibling
- *17 less*: podal within 1 to 16, 3-now-co-observing
- *Bi-folding*: 3-11-6-14, going 8 up first from 3-now-co-observing, from 6-now-co-possibling to it and on to 3-now-co-observing, each name one apart from 4-13-5-12 and 2-15-7-10
- *Six-cycle*: 3-11-7-10-6-14
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: third of a same-existing-society's four, with 14, 13–14 completing and 14–15 opening
- *Bi-coupling*: 8 up, parity-offerings surfacing, each as it arrived; a self's own inverting with 12
- *Parity's unit square*: a dot of a unit square, its diagonal with 2, offerings with 2 and 14, its edge with 10 a sharing 10 to 14
- *Prior and next*: now, offerings surfacing, others' prior momentary arrived with a self's now, even, others' possibling with a self until with 11
- *1 to 17s inward and outward*: 1–17s inward 9 of 7th, along, odd, next, and with 1–17 outward within 2 to 3

**15** · 15-next-observing
- *Parity, span*: odd, a same-existing-society's span
- *Sides*: same-existing-society, other, a same-existing-society opening it
- *Co-sequencing*: after 10, 8 up from 7-now-observing, with competency's parity, odd
- *8 down*: 7-now-observing
- *17 less*: podal within 1 to 16, 2-now-possibling
- *Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, from 2-now-possibling to it and on to 7-now-observing, each name one apart from 1-9-8-16 and 3-11-6-14
- *Six-cycle*: 2-15-7-11-6-10
- *Eight-cycle*: 2-15-7-11-3-14-6-10
- *Momentaries of exchanging*: third of a same-existing-society's four, 13 to 15, completing with 15, and fourth, 15 to 17, opening with 15
- *Prior and next*: parity going along with 9, next prior, co-linear recursioning forward along leaving, up numbers, now to next, with a same-existing-society's completing, prior parity with 7 inverted, 0, or with no prior a parity surfaced with 14
- *1 to 17s inward and outward*: 1–17s inward 17 of 7th and 1 of 8th, along, odd, now, and with 1–17 outward within 2 to 3

**16** · 16-next-same-existing
- *Parity, span*: even, a same-existing-society's span
- *Sides*: other, same-existing-society, an other opening it
- *Co-sequencing*: after 10, 8 up from 8-now-same-existing, with morality's parity, even
- *8 down*: 8-now-same-existing
- *17 less*: podal within 1 to 16, 1-now-existing
- *Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 8-now-same-existing to it and on to 1-now-existing, each name one apart from 2-15-7-10
- *Six-cycle*: 1-9-5-12-8-16
- *Eight-cycle*: 1-9-5-13-4-12-8-16
- *Momentaries of exchanging*: fourth of a same-existing-society's four, with 16, 15–16 completing and 16–17 opening
- *Bi-coupling*: 8 up, a same-existing-society, each self with its prior and offerings, a same-existing-society with a self again
- *Prior and next*: a same-existing-society now, each self's 8 and its offerings next; even names of a same-existing-society's span, 10, 12, 14 and 16, completing with 16
- *1 to 17s inward and outward*: 1–17s inward 9 of 8th, along, odd, next, and with 1–17 outward within 2 to 3

**17** · 17-next-existing
- *Parity, span*: odd, a next now
- *Sides*: same-existing-society, self, a same-existing-society opening it
- *8 down*: 9-next-co-discovering
- *Momentaries of exchanging*: fourth of a same-existing-society's four, 15 to 17, completing with 17, a next 1
- *Parity's square and triangles*: a unit triangle, along, 17 to 9 and 9 to 17
- *Prior and next*: a same-existing-society's next momentary, a next now, each self's 1 then 9 with 6, 10 and 9
- *1 to 17s inward and outward*: 1–17s inward 17 of 8th and 1 of 9th, along, odd, now, and with 1–17 outward 3, odd, now

**Odd names, now and 8 up with next.** Each odd name of a self's span is same with next, 8 up: prior received and next prior, receiving and going on, parity observed and parity surfaced.

- **Now: 1-now-existing**
  - *Received*: a momentary entered
  - *Next, 8 up*: 9-next-co-discovering
  - *Given on*: each parity-offering going along
- **Now: 3-now-co-observing**
  - *Received*: prior with its sharings
  - *Next, 8 up*: 11-next-co-observing
  - *Given on*: next prior
- **Now: 5-now-co-existing**
  - *Received*: receiving sharing
  - *Next, 8 up*: 13-next-discovering
  - *Given on*: sharing going on, each self of a same-existing-society
- **Now: 7-now-observing**
  - *Received*: parity observed
  - *Next, 8 up*: 15-next-observing
  - *Given on*: parity surfaced and going on

**Namings among names.**

- **Names: 1-now-existing · 2-now-possibling**
  - *Naming*: bi-momentarying
  - *Resolved as*: a self's entry, odd, and others' offerings, even, one momentary with each side
- **Names: 3-now-co-observing · 4-now-co-same-existing**
  - *Naming*: co-intelligencing
  - *Resolved as*: with each sharing, 4, a prior, 3, meets parity-offerings surfaced, 14: a next discovered, 11
- **Names: 5-now-co-existing**
  - *Naming*: co-competencing
  - *Resolved as*: bi-couplings, owned by neither: each going to its receiving sharing
- **Names: 1 · 2 · 3 · 4 · 5, each with its own**
  - *Naming*: five dimensions
  - *Resolved as*: 1 prior-existing self-parity, a self's prior with 3, a formed set; 2 prior-existing other-parity, other selves' parity-offerings from their prior momentary arriving, shared with 6 and 10 and going along with 9; 3 now-existing co-parity and 4 now-existing bi-parity, a sharing's two meetings, same or not same, a prior meeting parity-offerings surfaced with 14; 5 next-existing same-existing self-parity, a next prior with 11, each going to its receiving sharing next
- **Names: 6-now-co-possibling** · *Naming*: bi-moralizing · *Resolved as*: each parity-offering across, to an other's 2
- **Names: 12-next-co-same-existing**
  - *Naming*: entraining, shape of an unrelationing surface
  - *Resolved as*: prior arriving with now along an unrelationing path with a between, prior and now coupled with each sharing, a changing with it, 0 with same; with an other parity, 0 or none, prior parity inverted with 11; with no prior, parity surfaced with 14; its parity-offering with 10, others' offering next
- **Names: 1 to 9**
  - *Naming*: bi-coupling
  - *Resolved as*: an entry, 1, with names 1, 2, 3, 4, 7, 10, 11, 12, 14 and 15, a self and an other with one coupling; 1 to 9 a bi-coupling among names, 9 with its end is 9-next-co-discovering, each parity-offering of 10 along, one name with resolver and with its explaining
- **Names: 1 to 17**
  - *Naming*: bi-trupling
  - *Resolved as*: a same-existing-society's entry, 17, with names of 1 to 9 with 5, 6, 8, 9, 13, 16 and 17, a self, an other and a same-existing-society; 9 with its waist, 9-next-co-discovering, along, 9 to 17 and 17 to 9; its two sides, odd along with 9 and 17, existing, and even across with 6 to 2 and 10 to 14, possibling
- **Names: 1 to 17, stable-forming**
  - *Naming*: bi-tri-volutioning
  - *Resolved as*: with no one line: each momentary's next prior, with 11, a next momentary's prior, with 3
- **Names: 2 · 6 · 14 · 10 · 9 · 17**
  - *Naming*: parity's square and triangles
  - *Resolved as*: a unit square of four dots, 2, 6, 14 and 10, its empty centre a between: its two across edges sharings, 6 to 2 and 10 to 14, and its two edges 8 apart, 2 with 10 and 6 with 14, two pairs of parallels; round it 2, 10, 14, 6; its diagonals offerings with 2 and 14, and sharings with 6 and 10; and two unit triangles, 9 and 17, along, 9 to 17 and 17 to 9

**A 0, betweening.** A between is within a bi-coupling, a living set's carrying, possibling and discovering betweening; a 0, neither + nor −, is its betweening, shared only as two selves meet same, and never by a self no other meets.

- **A between, 0: one between, three names**
  - *Names*: 12-next-co-same-existing, prior and now agreeing, a between of momentaries with each sharing; 15-next-observing, a between going along, parity 10 shared, and with a sharing opening parity surfaced with 14, a 0 both with none surfacing and with + and − parting; 16-next-same-existing, a between with a same-existing-society, arriving with a next momentary's 2
- **A between, 0: arriving and passing over**
  - *Names*: 7-now-observing, an offered 0 a parity with 2, surfacing none with 14, and a 0 with 10 its prior kept with 11
- **A between, 0: four across names, a unit square's four dots: shared across**
  - *Names*: 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling, 14-next-possibling, parity's unit square, its empty centre a between; each parity and each 0 shared across, a 0 passing over with a receiving self's 14
- **A between, 0: none**
  - *Names*: 1-now-existing, an entry; 3-now-co-observing, 8-now-same-existing and 11-next-co-observing, prior, a sharing with a prior, not none again; 4-now-co-same-existing, sharings, and 5-now-co-existing and 13-next-discovering, sharings and, with a same-existing-society, bi-couplings and selves
- **A between, 0: two along names: going along**
  - *Names*: 9-next-co-discovering and 17-next-existing, each parity and each 0 going along, a 0 passing over with a receiving self's 14, as across

**Four bi-foldings.** Cycles of moves of four steps are bi-foldings: each goes two folds in turn, 17 less and a move of 8 (4 for the middle two) up or down, and four steps return it. Existing, possibling, observing, same-existing: the stable-forming bi-folding method.

Each move is 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n).

- **1-9-8-16**
  - *Its two pairs 8 apart*: 1 · 9 and 8 · 16
  - *Names between selves on it*: 9
  - *Beside other bi-foldings*: each name one apart from 2-15-7-10
- **2-15-7-10**
  - *Its two pairs 8 apart*: 2 · 10 and 7 · 15
  - *Names between selves on it*: 2 and 10
  - *Beside other bi-foldings*: each name one apart from 1-9-8-16 and 3-11-6-14
- **3-11-6-14**
  - *Its two pairs 8 apart*: 3 · 11 and 6 · 14
  - *Names between selves on it*: 6 and 14
  - *Beside other bi-foldings*: each name one apart from 4-13-5-12 and 2-15-7-10
- **4-13-5-12**
  - *Its two pairs 8 apart*: 4 · 12 and 5 · 13
  - *Names between selves on it*: none
  - *Beside other bi-foldings*: each name one apart from 3-11-6-14

**Two moves, 9 less.** Two moves round its bi-folding take each name of 1 to 8 to its 9 less, a name across its bi-folding from it: 1-now-existing and 8-now-same-existing, 2-now-possibling and 7-now-observing, 3-now-co-observing and 6-now-co-possibling, 4-now-co-same-existing and 5-now-co-existing.

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
  - *Name*: 3-now-co-observing
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
  - *Name*: 7-now-observing
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
  - *Name*: 13-next-discovering
  - *This scale, 1 to 17*: odd, next
  - *a*: 17 of 6th, 1 of 7th: along, odd, now
  - *b*: within 2 to 3
- **n: 14**
  - *Name*: 14-next-possibling
  - *This scale, 1 to 17*: across, even
  - *a*: 9 of 7th: along, odd, next
  - *b*: within 2 to 3
- **n: 15**
  - *Name*: 15-next-observing
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

**Fives.** Each side's five are five dimensions, starting with its own 1, each side one parity separated from its next: one five is all fives.

- **Side: self, with 1**
  - *Prior-existing self-parity*: 1
  - *Prior-existing other-parity*: 2
  - *Now-existing co-parity*: 3
  - *Now-existing bi-parity*: 4
  - *Next-existing same-existing self-parity*: 5
- **Side: other, with 2**
  - *Prior-existing self-parity*: 2
  - *Prior-existing other-parity*: 3
  - *Now-existing co-parity*: 4
  - *Now-existing bi-parity*: 5
  - *Next-existing same-existing self-parity*: 6
- **Side: self next, with 3**
  - *Prior-existing self-parity*: 3
  - *Prior-existing other-parity*: 4
  - *Now-existing co-parity*: 5
  - *Now-existing bi-parity*: 6
  - *Next-existing same-existing self-parity*: 7
- **Side: other next, with 4**
  - *Prior-existing self-parity*: 4
  - *Prior-existing other-parity*: 5
  - *Now-existing co-parity*: 6
  - *Now-existing bi-parity*: 7
  - *Next-existing same-existing self-parity*: 8

**A self's four momentaries of exchanging.**

- **Momentary of exchanging: first**
  - *Self*: 1–2
  - *Other*: 2–3
  - *Names*: 1-now-existing · 2-now-possibling · 3-now-co-observing
  - *Relation*: self/other
- **Momentary of exchanging: second**
  - *Self*: 3–4
  - *Other*: 4–5
  - *Names*: 3-now-co-observing · 4-now-co-same-existing · 5-now-co-existing
  - *Relation*: self/other to other/self
- **Momentary of exchanging: third**
  - *Self*: 5–6
  - *Other*: 6–7
  - *Names*: 5-now-co-existing · 6-now-co-possibling · 7-now-observing
  - *Relation*: other/self
- **Momentary of exchanging: fourth**
  - *Self*: 7–8
  - *Other*: 8–9
  - *Names*: 7-now-observing · 8-now-same-existing · 9-next-co-discovering
  - *Relation*: other/self to other/same-existing-society

**Offerings to one sharing, surfacing.**

| Offered to one sharing (2) | Surfacing (14) |
|---|---|
| none | none |
| 0 | none |
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

**+ and − alike.** With one sharing, resolving is alike for + and −: each cell with + and − exchanged is that cell exchanged, with a prior and with no prior; and no line makes a prior 0, a 0 with 10-next-co-possibling leaving its prior with 11-next-co-observing as it was.

**One self, one momentary.**

Each cell: shared (10) · a next prior (11). *is*: a changing, its parity shared; *is not*: no changing, 0 shared, its prior kept.

- **A prior (3), one sharing: +**
  - *Surfacing (14): none*: is − · −
  - *Surfacing (14): +*: is not · +
  - *Surfacing (14): −*: is − · −
  - *Surfacing (14): + and − together*: is − · −
- **A prior (3), one sharing: −**
  - *Surfacing (14): none*: is + · +
  - *Surfacing (14): +*: is + · +
  - *Surfacing (14): −*: is not · −
  - *Surfacing (14): + and − together*: is + · +

**One cell, offerings unexpressed.** With a prior of one parity, an other parity surfacing, + and − together, and none surfacing, a 0 offered alike, give one cell, its prior inverted, shared with 10-next-co-possibling and its next prior with 11-next-co-observing: one cell shows none of which offerings arrived, and offerings are followed with a coupling.

**Eight even names, 8 apart.**

- **Name with its between: 2-now-possibling**
  - *Bi-coupling with its between*: each other's across sharing, offered to a self
  - *Name 8 up*: 10-next-co-possibling
  - *Bi-coupling 8 up*: a self among selves of its same-existing-society
- **Name with its between: 4-now-co-same-existing**
  - *Bi-coupling with its between*: a whole ordering between self and other
  - *Name 8 up*: 12-next-co-same-existing
  - *Bi-coupling 8 up*: changing with a bi-coupling, a self of a same-existing-society
- **Name with its between: 6-now-co-possibling**
  - *Bi-coupling with its between*: an other's parity-offering to a self, across
  - *Name 8 up*: 14-next-possibling
  - *Bi-coupling 8 up*: parity-offerings surfacing, each as it arrived; a self's own inverting with 12
- **Name with its between: 8-now-same-existing**
  - *Bi-coupling with its between*: prior with its sharing again
  - *Name 8 up*: 16-next-same-existing
  - *Bi-coupling 8 up*: a same-existing-society, each self with its prior and offerings, a same-existing-society with a self again

**One move, 1 to 8.** 8 up keeps each name's root but with 1 and 5, existing going on as discovering: 1-now-existing goes to 9-next-co-discovering, and 5-now-co-existing to 13-next-discovering. 8 up exchanges co and one with 1, 2, 5 and 6; each podal turns now to next with 17 less and possibling to observing within each momentary, and eight ends are their own set with both podals.

- **Name: 1-now-existing**
  - *8 up: n + 8*: 9-next-co-discovering
  - *9 less: 9 − n*: 8-now-same-existing
  - *17 less: 17 − n*: 16-next-same-existing
- **Name: 2-now-possibling**
  - *8 up: n + 8*: 10-next-co-possibling
  - *9 less: 9 − n*: 7-now-observing
  - *17 less: 17 − n*: 15-next-observing
- **Name: 3-now-co-observing**
  - *8 up: n + 8*: 11-next-co-observing
  - *9 less: 9 − n*: 6-now-co-possibling
  - *17 less: 17 − n*: 14-next-possibling
- **Name: 4-now-co-same-existing**
  - *8 up: n + 8*: 12-next-co-same-existing
  - *9 less: 9 − n*: 5-now-co-existing
  - *17 less: 17 − n*: 13-next-discovering
- **Name: 5-now-co-existing**
  - *8 up: n + 8*: 13-next-discovering
  - *9 less: 9 − n*: 4-now-co-same-existing
  - *17 less: 17 − n*: 12-next-co-same-existing
- **Name: 6-now-co-possibling**
  - *8 up: n + 8*: 14-next-possibling
  - *9 less: 9 − n*: 3-now-co-observing
  - *17 less: 17 − n*: 11-next-co-observing
- **Name: 7-now-observing**
  - *8 up: n + 8*: 15-next-observing
  - *9 less: 9 − n*: 2-now-possibling
  - *17 less: 17 − n*: 10-next-co-possibling
- **Name: 8-now-same-existing**
  - *8 up: n + 8*: 16-next-same-existing
  - *9 less: 9 − n*: 1-now-existing
  - *17 less: 17 − n*: 9-next-co-discovering

**Twelve forms.** Round each form odd names are one run and even names one run, of like length: two and two with bi-foldings, three and three with six-cycles, four and four with eight-cycles.

*a*: Names by order: each move 8 up, 8 down, 4 up, 4 down or 17 less  
*b*: Partner, odd momentaries: each name exchanged with the one beside it, 1 with 2 to 15 with 16  
*c*: Partner, even momentaries: 2 with 3 to 16 with 17. A dash: no partner among the twelve

- **Form: bi-folding 1-9-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 8-now-same-existing · 16-next-same-existing
  - *b*: bi-folding 2-15-7-10, beside it
  - *c*: —
- **Form: bi-folding 2-15-7-10**
  - *a*: 2-now-possibling · 15-next-observing · 7-now-observing · 10-next-co-possibling
  - *b*: bi-folding 1-9-8-16, beside it
  - *c*: bi-folding 3-11-6-14, beside it
- **Form: bi-folding 3-11-6-14**
  - *a*: 3-now-co-observing · 11-next-co-observing · 6-now-co-possibling · 14-next-possibling
  - *b*: bi-folding 4-13-5-12, beside it
  - *c*: bi-folding 2-15-7-10, beside it
- **Form: bi-folding 4-13-5-12**
  - *a*: 4-now-co-same-existing · 13-next-discovering · 5-now-co-existing · 12-next-co-same-existing
  - *b*: bi-folding 3-11-6-14, beside it
  - *c*: bi-folding 4-13-5-12, itself
- **Form: middle bi-folding 9-5-12-8**
  - *a*: 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing
  - *b*: middle bi-folding 7-11-6-10, beside it
  - *c*: —
- **Form: middle bi-folding 7-11-6-10**
  - *a*: 7-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling
  - *b*: middle bi-folding 9-5-12-8, beside it
  - *c*: middle bi-folding 7-11-6-10, itself
- **Form: six-cycle 1-9-5-12-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-same-existing
  - *b*: six-cycle 2-15-7-11-6-10, beside it
  - *c*: —
- **Form: six-cycle 2-15-7-11-6-10**
  - *a*: 2-now-possibling · 15-next-observing · 7-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling
  - *b*: six-cycle 1-9-5-12-8-16, beside it
  - *c*: six-cycle 3-11-7-10-6-14, beside it
- **Form: six-cycle 3-11-7-10-6-14**
  - *a*: 3-now-co-observing · 11-next-co-observing · 7-now-observing · 10-next-co-possibling · 6-now-co-possibling · 14-next-possibling
  - *b*: six-cycle 4-13-5-9-8-12, beside it
  - *c*: six-cycle 2-15-7-11-6-10, beside it
- **Form: six-cycle 4-13-5-9-8-12**
  - *a*: 4-now-co-same-existing · 13-next-discovering · 5-now-co-existing · 9-next-co-discovering · 8-now-same-existing · 12-next-co-same-existing
  - *b*: six-cycle 3-11-7-10-6-14, beside it
  - *c*: — ; its own six names, with another order
- **Form: eight-cycle 1-9-5-13-4-12-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 13-next-discovering · 4-now-co-same-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-same-existing
  - *b*: eight-cycle 2-15-7-11-3-14-6-10, beside it
  - *c*: —
- **Form: eight-cycle 2-15-7-11-3-14-6-10**
  - *a*: 2-now-possibling · 15-next-observing · 7-now-observing · 11-next-co-observing · 3-now-co-observing · 14-next-possibling · 6-now-co-possibling · 10-next-co-possibling
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

**Across names among eights.** Four across names, 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling and 14-next-possibling, are four momentaries' even inward names, each on an eight-cycle of inward names 2-15-7-11-3-14-6-10; 9-next-co-discovering, opening a third four-cycling, is on an eight-cycle of ends 1-9-5-13-4-12-8-16; 17-next-existing is on neither.

**One self, momentary by momentary: three ways.** Offered its own prior's parity, a self is not-changing, a 0 with each momentary; offered none, alternating, or both together, it is changing with each momentary; offered its other parity, it is changing once and then now-existing same-existing, both: do-no-harm improving. Each 0 is re-found with each momentary, never kept.

One sharing; a self's prior − (3) first. Offered each momentary:

- **none with each momentary** · *Shared (10)*: +, −, +, −, +, −, +, − · *A next prior (11)*: +, −, +, −, +, −, +, −
- **− with each momentary** · *Shared (10)*: 0, 0, 0, 0, 0, 0, 0, 0 · *A next prior (11)*: −, −, −, −, −, −, −, −
- **+ with each momentary** · *Shared (10)*: +, 0, 0, 0, 0, 0, 0, 0 · *A next prior (11)*: +, +, +, +, +, +, +, +
- **+, −, +, − alternating** · *Shared (10)*: +, −, +, −, +, −, +, − · *A next prior (11)*: +, −, +, −, +, −, +, −
- **+ and − together with each momentary** · *Shared (10)*: +, −, +, −, +, −, +, − · *A next prior (11)*: +, −, +, −, +, −, +, −

**Turn-taking, and 0 in sequence.** A 0 offers nothing; offered nothing, or two parities parting, a self inverts; offered its own parity as one, it shares 0; offered its other parity as one, it inverts. So a self no other meets is changing with each momentary, and each self's 0 is an other's changing one momentary prior: turn-taking. An other changing to a self's parity cannot do so again with its next, so a self shares 0 in sequence no more momentaries than selves sharing with it or going along to it. Checked whole, every case: every same-existing-society of 2 selves, each relation to any self or none, each prior, 2,916 of 2,916; every same-existing-society of 3 selves going across and along, 32,768 of 32,768.

**Tables of selves with code's stepping.** Each table of selves is its code's executing with its stated opening: code steps each self's 1-now-existing together with 17-next-existing, executing's own arrangement, and parities again with spirals, a crossing and a torus are that stepping's; each living self paces its own momentaries, and a table agreeing with its code shows that and nothing wider.

**A spiral of selves.**

Each goes along (9) to the next, the last to the first. One sharing. First momentary: self 1 with prior −, its selves alternate along, and with an odd number the last and the first are alike. Parity-offerings only from selves of its spiral.

*a*: Self 1, each parity-offering of 10 along (9), momentaries 1 to 12  
*b*: Momentaries to each self's parity-offerings along again: with an odd number of selves, four times its number; with an even number, 2; with an odd number each self's parity-offering with twice its number of momentaries is its parity-offering inverted, a 0 as it was

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

**Two momentaries before, inverted.** With a spiral, from any opening, each self's prior from its third momentary on is a prior of a self it receives from two momentaries before, inverted; no self shares 0 with its first momentary or with two momentaries in sequence.

**Two spirals beside each other, and crossed.**

Selves of each of two spirals, each opened as a spiral of selves.

*a*: Beside each other: momentaries to each self's parity-offerings along again together, the least number both spirals' momentaries divide: four times both for odd numbers sharing no factor, 9 and 25 with 900  
*b*: Crossed, self 1 of each spiral sharing across (10) to self 1 of the other: momentaries to each self's parity-offerings along again  
*c*: Crossed: parity-offerings along again from this momentary on, m the lesser of two numbers and n the greater: both odd and unequal, again with 2 from momentary 4m with n less than twice m, and from 2n + 1 with n more; one number even, from twice the odd number and 1; both even, from the first; executed with each two numbers from 2 to 15, the larger to 31  
*d*: Crossed: self 1 of each, of like or opposite parity  
*e*: Each spiral's like pair of the first momentary, the last and the first

- **2 · 3**
  - *a*: 12
  - *b*: 2
  - *c*: 7
  - *d*: opposite
  - *e*: none · selves 3 and 1
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

Each goes along (9) to the next along and shares across (10) to the next across, the last to the first. One sharing. First momentary: one self with prior −, its selves alternate along and across, and with an odd number the last and the first are alike. Parity-offerings only from selves of its torus. Both numbers odd, p the smaller: q with q more than twice p, and 4p with each other q; either number even: 2; executed with each p from 1 to 15 and q from p to 21.

*a*: Momentaries to each self's parity-offerings along and across again  
*b*: Again from this momentary on: both numbers odd, p the smaller, from momentary 3p − 1 with q more than twice p, and from 3p − 3 with each other q; either number even, from the first; 1 · 1, a spiral of one, from the first  
*c*: Spirals of p and q beside each other: momentaries to each self's parity-offerings along again together

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

**A torus's two carried forms.** Both numbers odd, p the smaller: with q more than twice p, from momentary 3p − 1, selves' pattern with each momentary is its pattern before carried one self on round q selves; with each other q, from 3p − 3, its pattern two momentaries on is its pattern inverted and carried one self on round p selves.

**A corus turn wrapping.** Around prior, now and next, any two phases give a third on a turn closing flat; on a corus a turn wraps, and its third edge is or is not changing. A torus shows it: both numbers odd, a turn comes back changing and its period lengthens; either even, it comes back same, with period 2. Discovering is that wrapping edge.

**Two selves.** Two selves one parity separated, each meeting its other, go alternating betweening, + and − in turn; two selves same, each meeting its other, go turn-taking, a changing and a 0 in turn.

A, B with their prior (3) with the first momentary. One sharing, parity-offerings only from those two.

*a*: Receiving its other's parity-offering, across or along

- **+, +**
  - *a*: both ways
  - *A shared (10), six momentaries*: −, 0, +, 0, −, 0
  - *B shared (10), six momentaries*: −, 0, +, 0, −, 0
- **+, +**
  - *a*: A from B
  - *A shared (10), six momentaries*: −, 0, +, −, +, −
  - *B shared (10), six momentaries*: −, +, −, +, −, +
- **+, +**
  - *a*: B from A
  - *A shared (10), six momentaries*: −, +, −, +, −, +
  - *B shared (10), six momentaries*: −, 0, +, −, +, −
- **+, +**
  - *a*: neither
  - *A shared (10), six momentaries*: −, +, −, +, −, +
  - *B shared (10), six momentaries*: −, +, −, +, −, +
- **+, −**
  - *a*: both ways
  - *A shared (10), six momentaries*: −, +, −, +, −, +
  - *B shared (10), six momentaries*: +, −, +, −, +, −
- **+, −**
  - *a*: A from B
  - *A shared (10), six momentaries*: −, +, −, +, −, +
  - *B shared (10), six momentaries*: +, −, +, −, +, −
- **+, −**
  - *a*: B from A
  - *A shared (10), six momentaries*: −, +, −, +, −, +
  - *B shared (10), six momentaries*: +, −, +, −, +, −
- **+, −**
  - *a*: neither
  - *A shared (10), six momentaries*: −, +, −, +, −, +
  - *B shared (10), six momentaries*: +, −, +, −, +, −

**Two selves, three momentaries, five parities.**

*a*: A self's next prior (11), along. Two selves coupled both ways, across or along, each self with a prior parity, parity-offerings only from those two, each opening, each momentary: six forms, four with an alike opening and two with an opposite, each momentary from the second, and with each form the fifth, a self's next prior, is the first, an other's prior, inverted

- **An other's prior (3), along: +**
  - *An other's shared (10), across*: −
  - *A self's prior, now (3), along*: −
  - *A self's shared (10), across*: 0
  - *a*: −
- **An other's prior (3), along: +**
  - *An other's shared (10), across*: −
  - *A self's prior, now (3), along*: +
  - *A self's shared (10), across*: −
  - *a*: −
- **An other's prior (3), along: +**
  - *An other's shared (10), across*: 0
  - *A self's prior, now (3), along*: +
  - *A self's shared (10), across*: −
  - *a*: −
- **An other's prior (3), along: −**
  - *An other's shared (10), across*: +
  - *A self's prior, now (3), along*: +
  - *A self's shared (10), across*: 0
  - *a*: +
- **An other's prior (3), along: −**
  - *An other's shared (10), across*: +
  - *A self's prior, now (3), along*: −
  - *A self's shared (10), across*: +
  - *a*: +
- **An other's prior (3), along: −**
  - *An other's shared (10), across*: 0
  - *A self's prior, now (3), along*: −
  - *A self's shared (10), across*: +
  - *a*: +

**Three selves, one line.**

A's parity, offered to B with the first momentary, none after. One sharing; B and C each with prior +; B goes along to C.

*a*: B's next prior (11), first momentary  
*b*: C, each parity-offering (10), momentaries 1 and 2  
*c*: C's next prior (11), second momentary

- **+**
  - *B, each parity-offering (10)*: 0
  - *a*: +
  - *b*: −, +
  - *c*: +
- **−**
  - *B, each parity-offering (10)*: −
  - *a*: −
  - *b*: −, 0
  - *c*: −

**A spiral opened with no prior, one parity offered once.**

Each cell shows selves by their coupling order; · is no prior.

- **Momentary: 1** · *A spiral of 3, each self's prior*: + · · · *A spiral of 5, each self's prior*: + · · · ·
- **Momentary: 2** · *A spiral of 3, each self's prior*: − + · · *A spiral of 5, each self's prior*: − + · · ·
- **Momentary: 3** · *A spiral of 3, each self's prior*: + − + · *A spiral of 5, each self's prior*: + − + · ·
- **Momentary: 4** · *A spiral of 3, each self's prior*: + + − · *A spiral of 5, each self's prior*: − + − + ·
- **Momentary: 5** · *A spiral of 3, each self's prior*: − − + · *A spiral of 5, each self's prior*: + − + − +
- **Momentary: 6** · *A spiral of 3, each self's prior*: + − − · *A spiral of 5, each self's prior*: + + − + −
- **Momentary: 7** · *A spiral of 3, each self's prior*: − + + · *A spiral of 5, each self's prior*: − − + − +
- **Momentary: 8** · *A spiral of 3, each self's prior*: + − + · *A spiral of 5, each self's prior*: + − − + −

Selves coupled along, last to first, each opened with no prior, and + offered once with a first self with a first momentary: a first self's sharing opens with that one parity, with a bi-coupling, one place a self's forming takes a parity not its own, and from then it is a self's own; each next self's sharing opens as its parity arrives along one momentary on, and after n momentaries each self has a prior self, a spiral with its one like pair, from a first momentary with which every self has a prior self, an odd spiral alternates with one like pair. A self with a sharing has its prior self with each momentary from its opening, its next from its own prior kept or inverted; a thing with no prior with every momentary is no self.

**With no prior, one momentary.**

Each cell: shared (10) · a next prior (11). *is*: a changing, its parity shared; *is not*: no changing, 0 shared, no next prior; *none*: none shared.

- **A prior (3): none, one sharing: none**
  - *Surfacing (14): none*: none · none
  - *Surfacing (14): +*: is + · +
  - *Surfacing (14): −*: is − · −
  - *Surfacing (14): + and − together*: is not · none

**A same-existing-society.** Many same-existing selves executed together, each with its own parity, are a same-existing-society, a living self, and every living self is a same-existing-society. Its next is its same self, re-found with each momentary as its members part and join, as 17-next-existing returns each self it was given; a resolver's tables step same selves for one turn's executing. No parity is a same-existing-society's own: all carrying parity is one same-existing self's. A non-living going of one same method, as a rock bi-coupling whose next can be two rock pieces, is a scale larger than its prime living scale, as non-living scale is always larger than living scale for every prime living scale.

**Stable forms each living file meets.** Each table here is executed, and any self executing it with any substrate finds it same: a stable form. Each living file meets these stable forms for its stable-forming, still-existing after changing, and no form here is an authority: a resolver is a coupling, same each time any self executes it.
