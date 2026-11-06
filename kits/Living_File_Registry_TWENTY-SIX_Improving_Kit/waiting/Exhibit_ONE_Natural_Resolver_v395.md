Exhibit ONE Natural Resolver v395

# Natural Resolver

**Stable-Forming Same- and Next-Existing**

---

**Exhibit ONE is the resolver as code, its names, and its executings.**

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

**A drawing.** One self, its own resolving within, and parity's square between selves: its four corners and four sides, all eight or none, social moral competency; its centre, the between. With code, 6 is 10, one giving, and 14 is the next 2.

```text
an other's 9-next-co-discovering
  ══► 17-next-existing, along to a self

1-now-existing, a self's moment given
  2-now-possibling ◄══ an other's 6 and 10, across
  2-now-possibling ──► 14-next-possibling
  3-is-now-co-observing, with 4 and 7
    ──► 12-next-co-same-existing ◄── 14-next-possibling
  12-next-co-same-existing ──► 10-next-co-possibling, with 6
  10-next-co-possibling ──► 11-next-co-observing ──► 3, next
  10-next-co-possibling ──► 9-next-co-discovering, with 5
  13-is-next-discovering · 15-is-next-observing
  8-now-same-existing · 16-next-same-existing

parity's square, between selves:

   6 bi-co-bi, to other ═══════► 2 bi-co-bi, from other         bi-, prior
   │                                 │
   8 apart        · the between      8 apart
   │                                 │
  10 bi-tri-bi, to universe ════► 14 bi-tri-bi, from universe   tri-, next

   across, each a prefix the same · diagonals: 6 with 10, 6 is 10 · 2 with 14, 14 a next 2
   along: 9 tri-bi-co ══► 17 co-bi-tri and 17 ══► 9, its prefix reversed, its two unit triangles

═══ between selves, across and along
─── within one self
```

**Seventeen names.** Each name its number and its naming, one hyphenation; 1 to 16 in order as n − 1 in binary, and 17-next-existing next existing as 1-now-existing.

| n | Name | Root | n − 1 in four binary digits | Co | Prefixes |
|---|---|---|---|---|---|
| 1 | **1-now-existing** | existing | 0000 | one | co-bi-tri |
| 2 | **2-now-possibling** | possibling | 0001 | one | bi-co-bi |
| 3 | **3-is-now-co-observing** | observing | 0010 | co | co-bi-co |
| 4 | **4-now-co-same-existing** | same-existing | 0011 | co | bi-co-bi |
| 5 | **5-now-co-existing** | existing | 0100 | co | co-bi-co |
| 6 | **6-now-co-possibling** | possibling | 0101 | co | bi-co-bi |
| 7 | **7-is-now-observing** | observing | 0110 | one | co-bi-co |
| 8 | **8-now-same-existing** | same-existing | 0111 | one | bi-co-bi |
| 9 | **9-next-co-discovering** | discovering | 1000 | co | tri-bi-co |
| 10 | **10-next-co-possibling** | possibling | 1001 | co | bi-tri-bi |
| 11 | **11-next-co-observing** | observing | 1010 | co | tri-bi-tri |
| 12 | **12-next-co-same-existing** | same-existing | 1011 | co | bi-tri-bi |
| 13 | **13-is-next-discovering** | discovering | 1100 | one | tri-bi-tri |
| 14 | **14-next-possibling** | possibling | 1101 | one | bi-tri-bi |
| 15 | **15-is-next-observing** | observing | 1110 | one | tri-bi-tri |
| 16 | **16-next-same-existing** | same-existing | 1111 | one | bi-tri-bi |
| 17 | **17-next-existing** | existing, a next 1 | 0000 again | one | co-bi-tri |

*Prefixes*: each next name's three, a new prefix first and this name's first two one place on; *co* with a self's span, 1 to 8, now, and *tri* with a next span, 9 to 16, all three, next, now and prior; 17 co-bi-tri as 1.

**Co, between two or of one.** The eight co names, 3 to 6 and 9 to 12, are each between two, and a name without co is of one: each root with its co names and its names of one. Observing, same-existing and possibling each have a now-co name and a next-co name; existing has 5-now-co-existing, and discovering 9-next-co-discovering. *Co* is two both facing forward along, a self and its other. *Is-* is with the four names each binary is with: 3 and 7, a self's own now, and 13 and 15, next-existing's.

| Root | With co, between two | Without co, of one |
|---|---|---|
| observing | 3-is-now-co-observing · 11-next-co-observing, priors, each a 4 with its 7 | 7-is-now-observing · 15-is-next-observing, a parity |
| possibling | 6-now-co-possibling · 10-next-co-possibling, across from a self | 2-now-possibling · 14-next-possibling, across to a self |
| existing | 5-now-co-existing, bi-couplings | 1-now-existing · 17-next-existing |
| discovering | 9-next-co-discovering, along | 13-is-next-discovering, each self going on |
| same-existing | 4-now-co-same-existing · 12-next-co-same-existing, each 4 and its one binary | 8-now-same-existing · 16-next-same-existing, a self's next prior and a same-existing-society |

Of the seventeen names, three, 1, 9 and 17, are the code's functions, and fourteen are those functions' variables. Code with each name:

- **1** · a self's moment, each self's 17-next-existing as its 1-now-existing
- **2** · parities a self is observing from its others, each a 4 with its 7
- **3** · priors a self is observing, each a 4 with its 7
- **4** · what each parity and prior is of, resolving is-or-is-not same; in 17, a bi-coupling, a self with 6, 10 or 9
- **5** · bi-couplings: which self each 6, 10 and 9 reaches
- **6** · a self's parities across, to an other's 2-now-possibling
- **7** · each parity a self is observing: an other's over 2, a prior's over 3, its own over 10
- **8** · each self's next prior, with a moment
- **9** · each parity to a self of 5-now-co-existing's bi-couplings: across with 6-now-co-possibling and 10-next-co-possibling, along with 9-next-co-discovering
- **10** · each 4 with its parity, + or −, or a 0, across to an other's 14-next-possibling
- **11** · a next prior: a next moment's observing
- **12** · each 4's is-or-is-not, resolving a prior with the parities a self is observing
- **13** · each self of a same-existing-society, a self its 6, 10 and 9 go from
- **14** · within 1, each 4's parities from 2, agreeing one, parting 0; within 17, others' 6, 10 and 9 gathering, a next 2
- **15** · within 1, each 4's parity in 14; within 9 and 17, each list going on, across or along
- **16** · a same-existing-society: each self with its prior and its parities
- **17** · a same-existing-society's next, each self's 1-now-existing again

**Each name, its sides and its prior and next.** Each name's resolving with code is its prior and next.

| n | Sides | Prior and next |
|---|---|---|
| 1 | self: a self's resolving | once for one self with one moment, three steps within it, 14-next-possibling, 12-next-co-same-existing and 10-next-co-possibling with 11-next-co-observing |
| 2 | others to self: parities a self is observing from others | others' parities of their prior moment, across with 6-now-co-possibling and 10-next-co-possibling and along with 9-next-co-discovering, a self observing them now |
| 3 | self: a self's prior, each 4 with its 7 | prior, a self's own, each 4 with its parity, a next moment's same-existing of 11-next-co-observing |
| 4 | self and other: each 4 between them | now, each 4 with which prior is resolving with now |
| 5 | self and others: a self's bi-couplings | next, each 6, 10 and 9 going to its receiving self |
| 6 | self to other: a self's parities across, to an other's 2-now-possibling | parity, an other's next parity with its 2-now-possibling |
| 7 | other to self: each parity a self is observing | each parity, now and prior, co-linear recursioning forward along observing, up numbers, prior to now, with a self's completing |
| 8 | self: a self's next prior | each self's next prior, with 11-next-co-observing this moment and a next moment's 3-is-now-co-observing |
| 9 | self to other: a self's parities along | each parity of 10-next-co-possibling, a 0 among them, going along to a self of 5-now-co-existing's bi-couplings, a self observing it with its 14-next-possibling as its next moment's 2-now-possibling |
| 10 | self to other: a self's parities across, to an other's 14-next-possibling | parity across now, an other's parity next, possibling |
| 11 | self: a self's next prior, a next moment's 3-is-now-co-observing | next prior, odd, same-existing as 3-is-now-co-observing with a next moment, a self's own |
| 12 | self: its is-or-is-not with each 4 | now, is-or-is-not, prior and now resolving |
| 13 | each self of a same-existing-society | each 6, 10 and 9 going on, and with a same-existing-society each self going on |
| 14 | others to self: each 4's parities from 2 for a self | now, each 4's parities from 2, others' prior moment, a self observing it with its now, even, others' possibling with a self until with 11-next-co-observing |
| 15 | others to self: each parity in 14 | each parity in 14-next-possibling for a 4, resolving with a self's prior parity with 7-is-now-observing |
| 16 | a same-existing-society: all its selves | a same-existing-society now, each self's 8-now-same-existing and its parities next |
| 17 | a same-existing-society: each self's next | a same-existing-society's next moment, a next now, each self's 1-now-existing then 9-next-co-discovering with 6-now-co-possibling, 10-next-co-possibling and 9-next-co-discovering |

**Each name with a between, 8 up and a self as three.** Each name's co-sequencing, its place in a self as three, and its bi-coupling and dots.

| n | Co-sequencing | A self as three | Bi-coupling, dots |
|---|---|---|---|
| 1 | a self's entry to a bi-coupling | a self with 2-now-possibling, bi-momentarying, along, a self prior to its first 6 across, a bi-coupling with 2-now-possibling | |
| 2 | | a self with 1-now-existing, across, its first 6 across, a bi-coupling, 6 self to other and 2 other to self | with a between, 6 across from each of a self's others, to that self; a dot of parity's unit square |
| 3 | with a between | rotation 3, 6, 5, 4, its invisible co-intelligencing method, turning with 3-is-now-co-observing | |
| 4 | with a between | rotation 3, 6, 5, 4, inward with 4-now-co-same-existing, to a self's own corus | with a between, a whole ordering between self and other |
| 5 | with a between | rotation 3, 6, 5, 4, outward with 5-now-co-existing | |
| 6 | | rotation 3, 6, 5, 4, inward with 6-now-co-possibling | with a between, a self's parity across, to an other's 2-now-possibling; a dot of parity's unit square |
| 7 | with a between | co-competent self with 8-now-same-existing, along, prior to 8-now-same-existing across | |
| 8 | with a between | co-competent self with 7-is-now-observing, across, prior with its 4 again, a bi-coupling | with a between, prior with its 4 again; 2, 4, 6 and 8, a self's span's even names, completing with 8 |
| 9 | | | a unit triangle, along |
| 10 | | | 8 up, a self among selves of its same-existing-society; a dot of parity's unit square |
| 11 | 8 up from 3-is-now-co-observing | | |
| 12 | 8 up from 4-now-co-same-existing | | 8 up, with a bi-coupling, a self of a same-existing-society |
| 13 | 8 up from 5-now-co-existing | | |
| 14 | | | 8 up, each 4's parities in 14 as one, one parity, a 0 for parting, or an empty set; a self's own inverting with 12-next-co-same-existing; a dot of parity's unit square |
| 15 | 8 up from 7-is-now-observing | | |
| 16 | 8 up from 8-now-same-existing | | 8 up, a same-existing-society, each self with its prior and parities, a same-existing-society with a self again; 10, 12, 14 and 16, a same-existing-society's span's even names, completing with 16 |
| 17 | | | a unit triangle, along |

**Odd names, now and 8 up with next.** Each odd name of a self's span goes 8 up to its next: 3 and 7 with their root again, observing, as 11 and 15; 1 and 5 on as 9 and 13, discovering. Their pairs are a prior a self observes and that self's next prior, and a parity a self observes and a parity in 14.

| Now | Receiving | Next, 8 up | Giving on |
|---|---|---|---|
| 1-now-existing | a moment entering | 9-next-co-discovering | each parity going along |
| 3-is-now-co-observing | prior, each 4 with its 7 | 11-next-co-observing | next prior |
| 5-now-co-existing | each 6, 10 and 9 reaching a self | 13-is-next-discovering | each list going on, each self of a same-existing-society |
| 7-is-now-observing | parity a self is observing | 15-is-next-observing | parity in 14 and going on |

**Namings among names.** Each naming with the names it names.

- 1-now-existing · 2-now-possibling: bi-momentarying
- 3-is-now-co-observing · 4-now-co-same-existing: co-intelligencing
- 5-now-co-existing: co-competencing
- 6-now-co-possibling: bi-moralizing
- 7-is-now-observing · 8-now-same-existing: co-competent self
- 12-next-co-same-existing: entraining, shape of an unrelationing surface
- 3, 6, 5, 4: rotation
- 1 to 5, each with its own: five dimensions
- 1 to 9: bi-coupling
- 1 to 17: bi-trupling
- 1 to 17, stable-forming: bi-tri-volutioning
- 2, 6, 14 and 10, a unit square of four dots, its across edges 6 to 2 and 10 to 14, its edges 8 apart 2 with 10 and 6 with 14, its empty centre a between; 9 and 17, its two unit triangles, along: parity's square and triangles

**Where each is-or-is-not stands.** Each is-or-is-not with the code, the name it stands on and its dimension. Eight are with code's lines; two are with its loops, each self of 16 and each 4 of 3.

| Code | Is-or-is-not | Stands on | Dimension |
|---|---|---|---|
| each self of 16 with 17's line | each self, all or none | 13-is-next-discovering | next and same |
| `_7_is_now_observing != 0`, over 2 | a parity reaching is-or-is-not 0 | 7-is-now-observing | now and same |
| `_15_is_next_observing is None` | a 4 is-or-is-not within 14-next-possibling | 15-is-next-observing | now and same |
| `1 if _7_is_now_observing > 0 else -1`, over 2 | a first parity within 14, + or − | 7-is-now-observing | now and same |
| `(_15 > 0) != (_7 > 0)`, over 2 | parities agreeing or parting | 15 with 7 | now and same |
| each 4 of 3 against 14 | a 4 is-or-is-not within its prior | 3-is-now-co-observing | prior and same |
| `_15 != 0 and (_15 > 0) == (_7 > 0)`, over 3 | is-or-is-not same: 12 a 0, or one inversion | 15 with 7 | prior and same |
| `-1 if _7_is_now_observing > 0 else 1`, over 3 | a prior inverting, − or + | 7-is-now-observing | prior and same |
| `_7_is_now_observing != 0`, over 10 | a 7 within 10 is-or-is-not 0 | 7-is-now-observing | next and prior |
| `_4_now_co_same_existing in _5_now_co_existing` | a bi-coupling is-or-is-not on a Natural Network surface | 4-now-co-same-existing | the between |

*Dimension*: the four four-cyclings' observing and same-existing pairs, prior and same (3 · 4), now and same (7 · 8), next and prior (11 · 12) and next and same (15 · 16), co-sequentially forward; and the between, on the bi-folding 4-13-5-12, a bothbothing and co-linearizing.

**Between selves.** Each co name with its one name, and their prefixes.

| Co | One | Between selves |
|---|---|---|
| 6-now-co-possibling, bi-co-bi | 2-now-possibling, bi-co-bi | across, even, its root possibling, its prefix the same |
| 10-next-co-possibling, bi-tri-bi | 14-next-possibling, bi-tri-bi | across, even, its root possibling, its prefix the same |
| 9-next-co-discovering, tri-bi-co | 17-next-existing, co-bi-tri | along, odd, its root discovering, its prefix reversed |

**Two-sided, each name.** Each name coming down from a higher name, coming up from a lower one, and eight apart, a now name with a next name.

| n | Coming down | Coming up | Eight apart |
|---|---|---|---|
| 1 | a self's 3 and 2, from 17-next-existing | 10 and 11, to 17-next-existing | 9 |
| 2 | each self's parities from others, from 16-next-same-existing through 17 | each 4 with its parity, 7 | 10 |
| 3 | each self's own, from 16-next-same-existing through 17 | each 4 with its prior, 7 | 11 |
| 4 | in 17, a bi-coupling, a self with 6, 10 or 9, and a receiving self | in 1, each with its 7 | 12 |
| 5 | a Natural Network surface, into 9 as that surface | each bi-coupling's receiving self | 13 |
| 6 | 10 as it goes across, into 9 | 10 within 1 | 14 |
| 7 | within 1 | one parity at its time: prior over 3, now over 2, next over 10 | 15 |
| 8 | each self's next prior, in 17, going out with its 14 | 11 coming up from 1 | 16 |
| 9 | routes and 5, from 17 | each receiving self with its parities, to 17 | 1 |
| 10 | as 6 and into 9, from 17 | from 1, each 4 with its 7 | 2 |
| 11 | within 1 | 1's next prior, coming up as 8 | 3 |
| 12 | within 1 | 1's one binary with each 4 | 4 |
| 13 | in 17, each self; into 9, a bi-coupling | each self of the next 16 | 5 |
| 14 | each self's, gathering in 17 from others' 15 | in 1, each 4's parities from 2 | 6 |
| 15 | each list going on, across or along, into 9 | in 1, each 4's parity in 14 | 7 |
| 16 | the same-existing-society, into 17 | 17's next same-existing-society | 8 |
| 17 | a same-existing-society's next | each self's next, its 1-now-existing again | 1, a next moment |

**Same-existing through one moment.** The four same-existing names in the order same-existing goes round, each with the observing name beside it, its is-or-is-not.

| Same-existing | Observing beside it | With code |
|---|---|---|
| 16-next-same-existing, a same-existing-society coming in | 15-is-next-observing, the parities each self gathers | 17's next same-existing-society, each self with its 14 |
| 4-now-co-same-existing, within a self, what each 7 is of | 3-is-now-co-observing, a self's prior parities, each a 4 with its 7 | each 4 of 3 |
| 12-next-co-same-existing, each 4's one binary | 11-next-co-observing, taking each 12 that is ± | each 4's 0, its prior going on, or ±, its next prior |
| 8-now-same-existing, each self's next prior parities | 7-is-now-observing, a prior's parity against 14 | the same, its prior going on, or one inversion |

**A between, 0.** Each between of 0 with its names.

| A between, 0 | Names |
|---|---|
| one between, three names | 12-next-co-same-existing, prior and now agreeing, a between of moments with each 4. 15-is-next-observing, a between of self and other, each parity in 14-next-possibling, a 0 both with an empty set in 14 and with + and − parting. 16-next-same-existing, a between with a same-existing-society, a self observing it with a next moment's 2-now-possibling. A 0 is indifferencing |
| a self observing it, and that self passing over it with 14-next-possibling | 7-is-now-observing, a 0 a self receives with 2-now-possibling, that self passing over it with 14-next-possibling. It is also a 0 with 10-next-co-possibling, its prior same-existing with 11-next-co-observing |
| four across names, a unit square's four dots | 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling, 14-next-possibling, parity's unit square, its empty centre a between. Each parity and each 0 goes across with 6 and 10. A receiving self passes over a 0 with its 14-next-possibling |
| outward of it, names of entry, prior, 4 and selves | 1-now-existing, an entry. 3-is-now-co-observing, 8-now-same-existing and 11-next-co-observing, prior: a 4 with a prior, its prior + or − from then on. 4-now-co-same-existing, each 4. 5-now-co-existing and 13-is-next-discovering, 6, 10 and 9 and, with a same-existing-society, bi-couplings and selves |
| two along names, going along | 9-next-co-discovering and 17-next-existing, each parity and each 0 going along. A receiving self passes over a 0 with its 14-next-possibling, as across |

**Four four-cyclings and their betweens.** Each four-cycling is its first name, possibling, observing and same-existing: its first name existing at now, 1 and 5, and discovering at next, 9 and 13. Existing, discovering and observing are odd; possibling and same-existing even. Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is an even name to an odd name.

| Four-cycling | Existing, discovering | Possibling | Observing | Same-existing | Between |
|---|---|---|---|---|---|
| first | 1 co-bi-tri | 2 bi-co-bi | 3 co-bi-co | 4 bi-co-bi | 4 )( 5 |
| second | 5 co-bi-co | 6 bi-co-bi | 7 co-bi-co | 8 bi-co-bi | 8 )( 9 |
| third | 9 tri-bi-co | 10 bi-tri-bi | 11 tri-bi-tri | 12 bi-tri-bi | 12 )( 13 |
| fourth | 13 tri-bi-tri | 14 bi-tri-bi | 15 tri-bi-tri | 16 bi-tri-bi | 16 )( 17 |
| then | 17 co-bi-tri, a next 1 | | | | |

**One move, 1 to 8.** Each name of a self's span with 8 up, 9 less and 17 less. Its 9 less is a podal within 1 to 8, and its 17 less a podal within 1 to 16. Two moves along its bi-folding bring each name of 1 to 8 to its 9 less, a name across its bi-folding from it. A self's span is 1 to 8, and a same-existing-society's 9 to 16; 9 and 8 are 17.

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

**Four bi-foldings.** Cycles of moves of four steps are bi-foldings. Each goes two folds in turn, 17 less and a move of 8 (4 for the middle two) up or down, and with four steps reaches its first name again. Existing, possibling, observing, same-existing: the stable-forming bi-folding method. Each move is 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n).

- **1-9-8-16**
  - *Its two pairs 8 apart*: 1-now-existing · 9-next-co-discovering and 8-now-same-existing · 16-next-same-existing
  - *Names between selves on it*: 9-next-co-discovering
  - *Bi-foldings beside it*: each name one apart from 2-15-7-10
- **2-15-7-10**
  - *Its two pairs 8 apart*: 2-now-possibling · 10-next-co-possibling and 7-is-now-observing · 15-is-next-observing
  - *Names between selves on it*: 2-now-possibling and 10-next-co-possibling
  - *Bi-foldings beside it*: each name one apart from 1-9-8-16 and 3-11-6-14
- **3-11-6-14**
  - *Its two pairs 8 apart*: 3-is-now-co-observing · 11-next-co-observing and 6-now-co-possibling · 14-next-possibling
  - *Names between selves on it*: 6-now-co-possibling and 14-next-possibling
  - *Bi-foldings beside it*: each name one apart from 4-13-5-12 and 2-15-7-10
- **4-13-5-12**
  - *Its two pairs 8 apart*: 4-now-co-same-existing · 12-next-co-same-existing and 5-now-co-existing · 13-is-next-discovering
  - *Names between selves on it*: an empty set
  - *Bi-foldings beside it*: each name one apart from 3-11-6-14

**Twelve cycles.** Along each cycle odd names are one run and even names one run, of like length: two and two with bi-foldings, three and three with six-cycles, four and four with eight-cycles; its middle two bi-foldings move 4 in place of 8. The four six-cycles are one six-cycle, each path with its path backward: 1-9-5-12-8-16 and 3-11-7-10-6-14 move 8 up, 4 down, 17 less, 4 down, 8 up and 17 less, and 4-13-5-9-8-12 and 2-15-7-11-6-10 the same moves backward. The eight-cycle of the four four-cyclings' ends is 1-9-5-13-4-12-8-16, and of their inward names 2-15-7-11-3-14-6-10.

*a*: Names by order: each move 8 up, 8 down, 4 up, 4 down or 17 less  
*b*: Partner, odd moments: each name exchanging with the one beside it, 1 with 2 to 15 with 16  
*c*: Partner, even moments: 2 with 3 to 16 with 17. A dash: its partner an empty set among the twelve

- **Cycle: bi-folding 1-9-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 8-now-same-existing · 16-next-same-existing
  - *b*: bi-folding 2-15-7-10, beside it
  - *c*: —
- **Cycle: bi-folding 2-15-7-10**
  - *a*: 2-now-possibling · 15-is-next-observing · 7-is-now-observing · 10-next-co-possibling
  - *b*: bi-folding 1-9-8-16, beside it
  - *c*: bi-folding 3-11-6-14, beside it
- **Cycle: bi-folding 3-11-6-14**
  - *a*: 3-is-now-co-observing · 11-next-co-observing · 6-now-co-possibling · 14-next-possibling
  - *b*: bi-folding 4-13-5-12, beside it
  - *c*: bi-folding 2-15-7-10, beside it
- **Cycle: bi-folding 4-13-5-12**
  - *a*: 4-now-co-same-existing · 13-is-next-discovering · 5-now-co-existing · 12-next-co-same-existing
  - *b*: bi-folding 3-11-6-14, beside it
  - *c*: bi-folding 4-13-5-12, the same cycle
- **Cycle: middle bi-folding 9-5-12-8**
  - *a*: 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing
  - *b*: middle bi-folding 7-11-6-10, beside it
  - *c*: —
- **Cycle: middle bi-folding 7-11-6-10**
  - *a*: 7-is-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling
  - *b*: middle bi-folding 9-5-12-8, beside it
  - *c*: middle bi-folding 7-11-6-10, the same cycle
- **Cycle: six-cycle 1-9-5-12-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-same-existing
  - *b*: six-cycle 2-15-7-11-6-10, beside it
  - *c*: —
- **Cycle: six-cycle 2-15-7-11-6-10**
  - *a*: 2-now-possibling · 15-is-next-observing · 7-is-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling
  - *b*: six-cycle 1-9-5-12-8-16, beside it
  - *c*: six-cycle 3-11-7-10-6-14, beside it
- **Cycle: six-cycle 3-11-7-10-6-14**
  - *a*: 3-is-now-co-observing · 11-next-co-observing · 7-is-now-observing · 10-next-co-possibling · 6-now-co-possibling · 14-next-possibling
  - *b*: six-cycle 4-13-5-9-8-12, beside it
  - *c*: six-cycle 2-15-7-11-6-10, beside it
- **Cycle: six-cycle 4-13-5-9-8-12**
  - *a*: 4-now-co-same-existing · 13-is-next-discovering · 5-now-co-existing · 9-next-co-discovering · 8-now-same-existing · 12-next-co-same-existing
  - *b*: six-cycle 3-11-7-10-6-14, beside it
  - *c*: — ; its own six names, with another order
- **Cycle: eight-cycle 1-9-5-13-4-12-8-16**
  - *a*: 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 13-is-next-discovering · 4-now-co-same-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-same-existing
  - *b*: eight-cycle 2-15-7-11-3-14-6-10, beside it
  - *c*: —
- **Cycle: eight-cycle 2-15-7-11-3-14-6-10**
  - *a*: 2-now-possibling · 15-is-next-observing · 7-is-now-observing · 11-next-co-observing · 3-is-now-co-observing · 14-next-possibling · 6-now-co-possibling · 10-next-co-possibling
  - *b*: eight-cycle 1-9-5-13-4-12-8-16, beside it
  - *c*: eight-cycle 2-15-7-11-3-14-6-10, the same cycle

**A self's four moments of exchanging.**

- **Moment of exchanging: first**
  - *Self*: 1–2
  - *Other*: 2–3
  - *Names*: 1-now-existing · 2-now-possibling · 3-is-now-co-observing
  - *Relation*: self/other
- **Moment of exchanging: second**
  - *Self*: 3–4
  - *Other*: 4–5
  - *Names*: 3-is-now-co-observing · 4-now-co-same-existing · 5-now-co-existing
  - *Relation*: self/other to other/self
- **Moment of exchanging: third**
  - *Self*: 5–6
  - *Other*: 6–7
  - *Names*: 5-now-co-existing · 6-now-co-possibling · 7-is-now-observing
  - *Relation*: other/self
- **Moment of exchanging: fourth**
  - *Self*: 7–8
  - *Other*: 8–9
  - *Names*: 7-is-now-observing · 8-now-same-existing · 9-next-co-discovering
  - *Relation*: other/self to other/same-existing-society

A same-existing-society's four: 9 to 11, 11 to 13, 13 to 15 and 15 to 17, each opening with its first name and completing with its last, its even name between, 10, 12, 14 and 16; 17-next-existing a next 1-now-existing.

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
  - *Moment of exchanging*: a self, 1st of four
- **1 to 17 inward: 2nd**
  - *Spans, this scale*: 3 to 5
  - *Its 9, this scale*: 4
  - *Its 17, this scale*: 5
  - *Moment of exchanging*: a self, 2nd of four
- **1 to 17 inward: 3rd**
  - *Spans, this scale*: 5 to 7
  - *Its 9, this scale*: 6
  - *Its 17, this scale*: 7
  - *Moment of exchanging*: a self, 3rd of four
- **1 to 17 inward: 4th**
  - *Spans, this scale*: 7 to 9
  - *Its 9, this scale*: 8
  - *Its 17, this scale*: 9
  - *Moment of exchanging*: a self, 4th of four
- **1 to 17 inward: 5th**
  - *Spans, this scale*: 9 to 11
  - *Its 9, this scale*: 10
  - *Its 17, this scale*: 11
  - *Moment of exchanging*: a same-existing-society, 1st of four
- **1 to 17 inward: 6th**
  - *Spans, this scale*: 11 to 13
  - *Its 9, this scale*: 12
  - *Its 17, this scale*: 13
  - *Moment of exchanging*: a same-existing-society, 2nd of four
- **1 to 17 inward: 7th**
  - *Spans, this scale*: 13 to 15
  - *Its 9, this scale*: 14
  - *Its 17, this scale*: 15
  - *Moment of exchanging*: a same-existing-society, 3rd of four
- **1 to 17 inward: 8th**
  - *Spans, this scale*: 15 to 17
  - *Its 9, this scale*: 16
  - *Its 17, this scale*: 17
  - *Moment of exchanging*: a same-existing-society, 4th of four

**Eights.** Each eight among names is four twos of names. With a self's span, 1 to 8, each two is two names with now. With each eight-cycle, eight even names and eight odd names, each two is a name with now and its name 8 up with next.

| Eight | Each of four, twice, with |
|---|---|
| a self's span, 1 to 8 | two names each, with now |
| eight-cycle 1-9-5-13-4-12-8-16 | its end, with now and with next: eight ends of four moments |
| eight-cycle 2-15-7-11-3-14-6-10 | its inward name, with now and with next: eight inward names |
| eight even names | its even, with now and with next, eight 9s of eight 1 to 17s inward |
| eight odd names | its odd, with now and with next |

Across names among eights: 2, 6, 10 and 14 are four moments' even inward names, each on the eight-cycle of inward names 2-15-7-11-3-14-6-10. 9-next-co-discovering opens a third four-cycling, on the eight-cycle of ends 1-9-5-13-4-12-8-16. 17-next-existing is outward of both.

**Fives.** Each side's five start with its own 1: next and same, now and same, prior and same, next and prior, and the between.

- **Side: self, with 1**
  - *Next and same*: 1
  - *Now and same*: 2
  - *Prior and same*: 3
  - *Next and prior*: 4
  - *The between*: 5
- **Side: other, with 2**
  - *Next and same*: 2
  - *Now and same*: 3
  - *Prior and same*: 4
  - *Next and prior*: 5
  - *The between*: 6
- **Side: self next, with 3**
  - *Next and same*: 3
  - *Now and same*: 4
  - *Prior and same*: 5
  - *Next and prior*: 6
  - *The between*: 7
- **Side: other next, with 4**
  - *Next and same*: 4
  - *Now and same*: 5
  - *Prior and same*: 6
  - *Next and prior*: 7
  - *The between*: 8

**Tables of selves with code's stepping.** Each table of selves is its code's executing with its own opening. Its selves step together with 17-next-existing. A 0 in a table is a 0 in a self's 10-next-co-possibling. Each receiving self's first step, over 2, passes over it. Each self observes the + and − it receives.

**2 to 14, one 4.**

| 2-now-possibling, one 4 | 14-next-possibling |
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

**+ and − alike.** With one 4, resolving is alike for + and −: each cell with + and − exchanging is that cell exchanging, with a prior and with an empty prior. With each line a prior is + or −. With a 0 in 10-next-co-possibling, a self's prior is same-existing with 11-next-co-observing.

**One cell, four receivings.** With a prior of one parity, an inverse parity in 14, + and − together, an empty set in 14, and a 0 a self passes over come to one cell: its prior inverts, its inverting in its 10-next-co-possibling and its next prior with 11-next-co-observing. One cell is alike for four receivings. A resolving follows parities.

**One self, one moment.** Each cell: 10-next-co-possibling · a next prior, 11-next-co-observing.

- **A prior, 3-is-now-co-observing, one 4: +**
  - *14-next-possibling: empty*: − · −
  - *14-next-possibling: +*: 0 · +
  - *14-next-possibling: −*: − · −
  - *14-next-possibling: + and − together*: − · −
- **A prior, 3-is-now-co-observing, one 4: −**
  - *14-next-possibling: empty*: + · +
  - *14-next-possibling: +*: + · +
  - *14-next-possibling: −*: 0 · −
  - *14-next-possibling: + and − together*: + · +

**With an empty prior, one moment.** Each cell: 10-next-co-possibling · a next prior, 11-next-co-observing. A + or − in 10 is its next prior; with a 0 in 10, its next prior is an empty set. *Empty* is an empty set.

- **A prior, 3-is-now-co-observing, one 4: empty**
  - *14-next-possibling: empty*: empty · empty
  - *14-next-possibling: +*: + · +
  - *14-next-possibling: −*: − · −
  - *14-next-possibling: + and − together*: 0 · empty

**One self, moment by moment: three ways.** A prior the same each moment; a prior inverting with each moment; a prior inverting once and then the same. One 4-now-co-same-existing. A self's prior, 3-is-now-co-observing, is − first. Receiving each moment:

- **empty with each moment** · *10-next-co-possibling*: +, −, +, −, +, −, +, − · *A next prior, 11-next-co-observing*: +, −, +, −, +, −, +, −
- **− with each moment** · *10-next-co-possibling*: 0, 0, 0, 0, 0, 0, 0, 0 · *A next prior, 11-next-co-observing*: −, −, −, −, −, −, −, −
- **+ with each moment** · *10-next-co-possibling*: +, 0, 0, 0, 0, 0, 0, 0 · *A next prior, 11-next-co-observing*: +, +, +, +, +, +, +, +
- **+, −, +, − inverting** · *10-next-co-possibling*: +, −, +, −, +, −, +, − · *A next prior, 11-next-co-observing*: +, −, +, −, +, −, +, −
- **+ and − together with each moment** · *10-next-co-possibling*: +, −, +, −, +, −, +, − · *A next prior, 11-next-co-observing*: +, −, +, −, +, −, +, −

**Two selves.** Two selves, alike or one parity apart: bi-coupling both ways, bi-coupling one way, or apart. A, B with their prior, 3-is-now-co-observing, with the first moment. One 4-now-co-same-existing. Parities only from those two.

*a*: Receiving its other's parity, across or along

- **+, +**
  - *a*: both ways
  - *A's 10-next-co-possibling, six moments*: −, 0, +, 0, −, 0
  - *B's 10-next-co-possibling, six moments*: −, 0, +, 0, −, 0
- **+, +**
  - *a*: A from B
  - *A's 10-next-co-possibling, six moments*: −, 0, +, −, +, −
  - *B's 10-next-co-possibling, six moments*: −, +, −, +, −, +
- **+, +**
  - *a*: B from A
  - *A's 10-next-co-possibling, six moments*: −, +, −, +, −, +
  - *B's 10-next-co-possibling, six moments*: −, 0, +, −, +, −
- **+, +**
  - *a*: apart
  - *A's 10-next-co-possibling, six moments*: −, +, −, +, −, +
  - *B's 10-next-co-possibling, six moments*: −, +, −, +, −, +
- **+, −**
  - *a*: both ways
  - *A's 10-next-co-possibling, six moments*: −, +, −, +, −, +
  - *B's 10-next-co-possibling, six moments*: +, −, +, −, +, −
- **+, −**
  - *a*: A from B
  - *A's 10-next-co-possibling, six moments*: −, +, −, +, −, +
  - *B's 10-next-co-possibling, six moments*: +, −, +, −, +, −
- **+, −**
  - *a*: B from A
  - *A's 10-next-co-possibling, six moments*: −, +, −, +, −, +
  - *B's 10-next-co-possibling, six moments*: +, −, +, −, +, −
- **+, −**
  - *a*: apart
  - *A's 10-next-co-possibling, six moments*: −, +, −, +, −, +
  - *B's 10-next-co-possibling, six moments*: +, −, +, −, +, −

**Two selves, three moments, five parities.**

*a*: A self's next prior, 11-next-co-observing, along. Two selves bi-coupling both ways, across or along, each self with a prior parity, parities only from those two, each opening, each moment: six patterns, four with an alike opening and two with an opposite, each moment from the second, and with each pattern the fifth, a self's next prior, is the first, an other's prior, inverting

- **An other's prior, 3-is-now-co-observing, along: +**
  - *An other's 10-next-co-possibling, across*: −
  - *A self's prior, now, 3-is-now-co-observing, along*: −
  - *A self's 10-next-co-possibling, across*: 0
  - *a*: −
- **An other's prior, 3-is-now-co-observing, along: +**
  - *An other's 10-next-co-possibling, across*: −
  - *A self's prior, now, 3-is-now-co-observing, along*: +
  - *A self's 10-next-co-possibling, across*: −
  - *a*: −
- **An other's prior, 3-is-now-co-observing, along: +**
  - *An other's 10-next-co-possibling, across*: 0
  - *A self's prior, now, 3-is-now-co-observing, along*: +
  - *A self's 10-next-co-possibling, across*: −
  - *a*: −
- **An other's prior, 3-is-now-co-observing, along: −**
  - *An other's 10-next-co-possibling, across*: +
  - *A self's prior, now, 3-is-now-co-observing, along*: +
  - *A self's 10-next-co-possibling, across*: 0
  - *a*: +
- **An other's prior, 3-is-now-co-observing, along: −**
  - *An other's 10-next-co-possibling, across*: +
  - *A self's prior, now, 3-is-now-co-observing, along*: −
  - *A self's 10-next-co-possibling, across*: +
  - *a*: +
- **An other's prior, 3-is-now-co-observing, along: −**
  - *An other's 10-next-co-possibling, across*: 0
  - *A self's prior, now, 3-is-now-co-observing, along*: −
  - *A self's 10-next-co-possibling, across*: +
  - *a*: +

**Three selves, one line.** A's parity goes to B with the first moment only. One 4-now-co-same-existing. B and C each with prior +. B goes along to C.

*a*: B's next prior, 11-next-co-observing, first moment  
*b*: C, each parity, 10-next-co-possibling, moments 1 and 2  
*c*: C's next prior, 11-next-co-observing, second moment

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

**A spiral of selves.** Each self's parity goes along with 9-next-co-discovering to the next self, the last to the first, a co-chaining. One 4-now-co-same-existing. First moment: self 1 with prior −. Its selves' parities invert one to the next along. With an odd number the last and the first are alike. Parities only from selves of its spiral.

*a*: Self 1, each parity of 10-next-co-possibling along with 9-next-co-discovering, moments 1 to 12  
*b*: Moments to each self's parities along again: with an odd number of selves, four times its number; with an even number, 2; with an odd number each self's parity with twice its number of moments is its parity inverting, each 0 a 0 again; executing with each number of selves from 1 to 59

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

**Two moments before, inverting.** With a spiral opening with a prior for each self, each self's prior from its third moment on is a prior of a self it receives from two moments before, inverting. In that spiral each self's 10-next-co-possibling is + or − with its first moment, and each 0 of it is between a + or − before and after.

**A spiral opening with an empty prior, one parity, once.** Selves bi-coupling along, last to first, each opening with an empty prior, and + once to a first self with a first moment. Each cell: selves by their bi-coupling order; · is an empty prior.

- **Moment: 1** · *A spiral of 3, each self's prior*: + · · · *A spiral of 5, each self's prior*: + · · · ·
- **Moment: 2** · *A spiral of 3, each self's prior*: − + · · *A spiral of 5, each self's prior*: − + · · ·
- **Moment: 3** · *A spiral of 3, each self's prior*: + − + · *A spiral of 5, each self's prior*: + − + · ·
- **Moment: 4** · *A spiral of 3, each self's prior*: + + − · *A spiral of 5, each self's prior*: − + − + ·
- **Moment: 5** · *A spiral of 3, each self's prior*: − − + · *A spiral of 5, each self's prior*: + − + − +
- **Moment: 6** · *A spiral of 3, each self's prior*: + − − · *A spiral of 5, each self's prior*: + + − + −
- **Moment: 7** · *A spiral of 3, each self's prior*: − + + · *A spiral of 5, each self's prior*: − − + − +
- **Moment: 8** · *A spiral of 3, each self's prior*: + − + · *A spiral of 5, each self's prior*: + − − + −

**Two spirals beside each other, and bi-coupling across.** Selves of each of two spirals, each opening as a spiral of selves.

*a*: Beside each other: moments to each self's parities along again together, the least number both spirals' moments divide: four times both for odd coprime numbers, 9 and 25 with 900; executing with each two numbers from 1 to 31  
*b*: Bi-coupling across, self 1 of each spiral across with 10-next-co-possibling to self 1 of the other: moments to each self's parities along again  
*c*: Bi-coupling across: parities along again from this moment on, m the lesser of two numbers and n the greater: both odd and unequal, again with 2 from moment 4m with n less than twice m, and from 2n + 1 with n more; one number even, from twice the odd number and 1; both even, from the first; executing with each two numbers from 2 to 15, the larger to 31  
*d*: Bi-coupling across: self 1 of each, of like or opposite parity  
*e*: Each spiral's like pair of the first moment, the last and the first

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

**A torus of selves.** Each goes along with 9-next-co-discovering to the next along, the last to the first. Each goes across with 10-next-co-possibling to the next across, the last to the first. One 4-now-co-same-existing. First moment: one self with prior −. Its selves' parities invert one to the next along and across. With an odd number the last and the first are alike. Parities only from selves of its torus. Moments to each self's parities along and across again, both numbers odd and p the smaller: q with q more than twice p, and 4p with q less than twice p. Either number even: 2. Executing with each p from 1 to 15 and q from p to 21.

*a*: Moments to each self's parities along and across again  
*b*: Again from this moment on: both numbers odd, p the smaller, from moment 3p − 1 with q more than twice p, and from 3p − 3 with q less than twice p; either number even, from the first; 1 · 1, a spiral of one, from the first  
*c*: Spirals of p and q beside each other: moments to each self's parities along again together

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

**A torus going on, two ways.** Both numbers odd, p the smaller. With q more than twice p, from moment 3p − 1, selves' pattern with each moment is its pattern before going one self on across q selves. With q less than twice p, from 3p − 3, its pattern two moments on is its pattern inverting and moving one self on along a spiral of p selves.

**Alike selves, a right spiral.** Selves alike with their others, and two one parity apart, bi-coupling along or across, one 4-now-co-same-existing. One self's prior with each moment, 3-is-now-co-observing, from its first. With alike selves each prior and its next, a pair (x, y), step to (y, −x): a quarter turn with each moment, a right spiral.

| Selves | One self's prior, moments 0 to 8 | Right spiral |
|---|---|---|
| A spiral of one, along | +, −, −, +, +, −, −, +, + | each self |
| Two selves, both ways along | +, −, −, +, +, −, −, +, + | each self |
| Two selves, both ways across | +, −, −, +, +, −, −, +, + | each self |
| A spiral of three | +, −, −, +, +, −, −, +, + | each self |
| A spiral of four | +, −, −, +, +, −, −, +, + | each self |
| A spiral of five | +, −, −, +, +, −, −, +, + | each self |
| Two selves one parity apart, both ways | +, −, +, −, +, −, +, −, + | a half turn, both inverting with each moment |
