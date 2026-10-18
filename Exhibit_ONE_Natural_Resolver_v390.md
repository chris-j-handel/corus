Exhibit ONE Natural Resolver v390

# Natural Resolver

**Stable Forms of the Discovering Method**

---

```python
"""Exhibit ONE · Natural Resolver · at the numbered names"""


def _1_now(_3_now_co_prioring, _2_now_possibling):
    _14_next_possibling = {}
    for _4_now_co_still_possibling, _7_now_prioring in _2_now_possibling:
        if _7_now_prioring != 0:
            _15_next_prioring = _14_next_possibling.get(_4_now_co_still_possibling)
            if _15_next_prioring is None:
                _14_next_possibling[_4_now_co_still_possibling] = 1 if _7_now_prioring > 0 else -1
            elif (_15_next_prioring > 0) != (_7_now_prioring > 0):
                _14_next_possibling[_4_now_co_still_possibling] = 0
    _12_next_co_still_possibling = dict(_14_next_possibling)
    for _4_now_co_still_possibling, _7_now_prioring in _3_now_co_prioring:
        _15_next_prioring = _14_next_possibling.get(_4_now_co_still_possibling, 0)
        if _15_next_prioring != 0 and (_15_next_prioring > 0) == (_7_now_prioring > 0):
            _12_next_co_still_possibling[_4_now_co_still_possibling] = 0
        else:
            _12_next_co_still_possibling[_4_now_co_still_possibling] = -1 if _7_now_prioring > 0 else 1
    _10_next_co_possibling = list(_12_next_co_still_possibling.items())
    _11_next_co_prioring = dict(_3_now_co_prioring)
    for _4_now_co_still_possibling, _7_now_prioring in _10_next_co_possibling:
        if _7_now_prioring != 0:
            _11_next_co_prioring[_4_now_co_still_possibling] = _7_now_prioring
    return _10_next_co_possibling, list(_11_next_co_prioring.items())


def _9_next_co_changing(_10_next_co_possibling, _5_now_co_changing):
    return [(_5_now_co_changing[_13_next], _15_next_prioring)
            for _13_next, _15_next_prioring in _10_next_co_possibling]


def _17_next_now(_16_next_still_possibling, _5_now_co_changing):
    _8_now_still_possibling = {}
    _14_next_possibling = {_13_next: [] for _13_next in _16_next_still_possibling}
    for _13_next, (_3_now_co_prioring, _2_now_possibling) in _16_next_still_possibling.items():
        _10_next_co_possibling, _8_now_still_possibling[_13_next] = _1_now(
            _3_now_co_prioring, _2_now_possibling)
        _6_now_co_possibling = _10_next_co_possibling
        for _4_now_co_still_possibling, _15_next_prioring in _9_next_co_changing(
                [(_4_now_co_still_possibling, _15_next_prioring)
                 for _4_now_co_still_possibling, _15_next_prioring in (
                     ((_13_next, 6), _6_now_co_possibling),
                     ((_13_next, 10), _10_next_co_possibling),
                     ((_13_next, 9), _10_next_co_possibling))
                 if _4_now_co_still_possibling in _5_now_co_changing],
                _5_now_co_changing):
            _14_next_possibling[_4_now_co_still_possibling].extend(_15_next_prioring)
    return {_13_next: (_8_now_still_possibling[_13_next],
                       _14_next_possibling[_13_next])
            for _13_next in _16_next_still_possibling}

```

```text
                another self's 9-next-co-changing, released along to the self
                                      ▲
                                      ║ 17-next-now · along
     ┌────────────────────────────────╨────────────────────────────────┐
     │                              1-now                              │
     │  14-next-possibling ◄────────────────── 2-now-possibling ◄═══════  another self's 6 and 10
     │      │                                                          │
     │      ▼                                                          │
     │  3-now-co-prioring ──► 12-next-co-still-possibling ──► 10-next-co-possibling, with 6-now-co-possibling
     │  4-now-co-still-possibling · 7-now-prioring       │             │
     │                                                   ├──► 11-next-co-prioring ──► 3, at next
     │                                                   └──► 9-next-co-changing ──► 5-now-co-changing
     │                                         13-next · 15-next-prioring          │
 ◄════════ 6 and 10, to another self's 2 and 14                                   │
     │  8-now-still-possibling · 16-next-still-possibling                          │
     └────────────────────────────────╥────────────────────────────────┘
                                      ║ 9-next-co-changing · along
                                      ▼
                another self's 17-next-now, the self releasing to it
   sharing side, co          6-now-co-possibling ══► another self's 2-now-possibling
                             10-next-co-possibling ══► another self's 14-next-possibling
   arriving side, one        another self's 6 and 10 ══► 2 and 14
   ═══ between selves, across and along      ─── within one self
```

**At a drawing.** Prior at 3 couples with surfacing at 14 at each sharing at 12; changings at 10, same at 6, go across to another self's 2 and 14; next prior goes to 11 and on to 3 at next; and 9 releases along by 5 to another self's 17. At 6 to 2, 10 to 14 and 9 to 17 its sharing side is a self and its arriving side another self, each a self, and a society is its selves.

**At 1-now, now given and next made.** At 1-now a self is given two now names, 3-now-co-prioring and 2-now-possibling, each sharing in them at 4-now-co-still-possibling and each parity at 7-now-prioring, and each name 1-now makes is a next name, 14-next-possibling, 15-next-prioring, 12-next-co-still-possibling, 10-next-co-possibling and 11-next-co-prioring: an entry is given a self's span and makes a society's.

**Seventeen names.**

| n | Name | Momentary | Parity | Co | At the resolver |
|---|---|---|---|---|---|
| 1 | **1-now** | now, a self's span | odd, existing | one | each self's momentary, entered at a society's 17 |
| 2 | **2-now-possibling** | now, a self's span | even, possibling | one | offerings arriving at a self, each sharing with its parity |
| 3 | **3-now-co-prioring** | now, a self's span | odd, existing | between two | prior at its sharings, each sharing with its parity |
| 4 | **4-now-co-still-possibling** | now, a self's span | even, possibling | between two | each sharing at which offerings and prior couple, and at a society each self at its names 6, 10 and 9 |
| 5 | **5-now-co-changing** | now, a self's span | odd, existing | between two | releasings, each releasing sharing with a self it arrives at |
| 6 | **6-now-co-possibling** | now, a self's span | even, possibling | between two | each sharing's changing shared across, to another self's 2 |
| 7 | **7-now-prioring** | now, a self's span | odd, existing | one | each parity prioring: an offering's, a prior's and a changing's |
| 8 | **8-now-still-possibling** | now, a self's span | even, possibling | one | each self's next prior, beside other selves' |
| 9 | **9-next-co-changing** | next, a society's span | odd, existing | between two | each changing released, along at 9 and across at 6 and 10, to a self of 5's releasings |
| 10 | **10-next-co-possibling** | next, a society's span | even, possibling | between two | each sharing's changing, + or − is and 0 is not, shared across to another self's 14 |
| 11 | **11-next-co-prioring** | next, a society's span | odd, existing | between two | next prior: prior with each changing at its sharing |
| 12 | **12-next-co-still-possibling** | next, a society's span | even, possibling | between two | each sharing's changing, is or is not, prior and offerings coupling |
| 13 | **13-next** | next, a society's span | odd, existing | one | each self at a society, and each sharing a changing releases from |
| 14 | **14-next-possibling** | next, a society's span | even, possibling | one | offerings surfacing at each sharing, same one parity and parting 0; at 17 each self's next offerings |
| 15 | **15-next-prioring** | next, a society's span | odd, existing | one | each parity surfacing, and each parity released |
| 16 | **16-next-still-possibling** | next, a society's span | even, possibling | one | a society: each self with its prior and its offerings |
| 17 | **17-next-now** | next now | odd, existing | one | a society's next momentary, each self's 1-now again |

**Each name is its number and its naming, one hyphenation.** Its number is its place and its parity, odd existing and even possibling; *now* is a self's span, 1 to 8, and *next* a society's, 9 to 16, 17-next-now a society's next arriving as each self's 1-now; a name with *co* is at a sharing between two, and a name without it is at one. Six names between selves are odd and even by their numbers: 2, 6, 10 and 14, even, across, possibling, a changing shared at 6-now-co-possibling and 10-next-co-possibling another self's possibling at its 2-now-possibling and 14-next-possibling; 9 and 17, odd, along, existing, 9-next-co-changing a next prior released and 17-next-now a next now. Each self's existing is another self's possibling, one changing at a sharing across and no second thing.

**Four momentaries and their gaps.** Each span's names are two momentaries of four, each opening at an odd existing name, a possibling and a prioring within it, and completing at an even still-possibling name; between each completing and its next opening is a gap, both its sides visible, and 17-next-now is next 1-now.

| Momentary | Opening, odd, existing | Within, even, possibling | Within, odd, prioring | Completing, even, still-possibling | Gap |
|---|---|---|---|---|---|
| first | 1-now | 2-now-possibling | 3-now-co-prioring | 4-now-co-still-possibling | 4 )( 5 |
| second | 5-now-co-changing | 6-now-co-possibling | 7-now-prioring | 8-now-still-possibling | 8 )( 9 |
| third | 9-next-co-changing | 10-next-co-possibling | 11-next-co-prioring | 12-next-co-still-possibling | 12 )( 13 |
| fourth | 13-next | 14-next-possibling | 15-next-prioring | 16-next-still-possibling | 16 )( 17 |

**Co, between two or at one.** Each kind of name stands with co at a sharing between two, and without it at one.

| Kind | With co, at a sharing between two | Without co, at one |
|---|---|---|
| prioring | 3-now-co-prioring · 11-next-co-prioring, prior at its sharings | 7-now-prioring · 15-next-prioring, a parity |
| possibling | 6-now-co-possibling · 10-next-co-possibling, changing at its sharing side | 2-now-possibling · 14-next-possibling, changing at its arriving side |
| changing | 5-now-co-changing · 9-next-co-changing, between two | — |
| still-possibling | 4-now-co-still-possibling · 12-next-co-still-possibling, at each sharing | 8-now-still-possibling · 16-next-still-possibling, a self and a society |
| now and next | — | 1-now · 13-next · 17-next-now |

**Sharing between selves.** At 6 to 2, 10 to 14 and 9 to 17 co is its sharing side and its absence its arriving side: a self shares its changing, and nothing of its prior crosses to another self.

| Sharing side, co | Arriving side, one | Between selves |
|---|---|---|
| 6-now-co-possibling | 2-now-possibling | across, even, possibling |
| 10-next-co-possibling | 14-next-possibling | across, even, possibling |
| 9-next-co-changing | 17-next-now | along, odd, existing |

**Four binaries at the lines.** A universe is or is not existing, all, now and same, and at a self's span each binary is one pair of names, its *is* at an odd name and its *is not* at an even, its *is not* an other's side of a self's *is*; binaries are names' explaining, now at each name as its momentary, and existing, same and all enter no name.

| Binary | *Is*, odd | At the resolver | *Is not*, even | At the resolver |
|---|---|---|---|---|
| now | 1-now | a self's momentary entered | 2-now-possibling | offerings arriving, others' changings of their prior momentary |
| existing | 3-now-co-prioring | prior at its sharings, each with its parity | 4-now-co-still-possibling | each sharing as a place, no parity at it |
| same | 5-now-co-changing | each releasing to a self receiving it at its same sharing | 6-now-co-possibling | changings shared across, + or − at a changing and 0 at none, another self's offerings |
| all | 7-now-prioring | each parity prioring at every entry | 8-now-still-possibling | each self's own next prior, one beside others |

**At a society's span four stand with now and same exchanged**: now between two at 9-next-co-changing and 10-next-co-possibling, one now shared by selves, and same at one at 13-next and 14-next-possibling, each self's sameness its own.

**A now-self at one line.** At 12-next-co-still-possibling a line `if _15_next_prioring != 0 and (_15_next_prioring > 0) == (_7_now_prioring > 0)` is 14-next-possibling's surfacing, as 15, agreeing or not with 7-now-prioring at each sharing of 3-now-co-prioring: now-self, now-prioring and next-possibling, at one line, at 0, a between, its prior kept, or at ±, a sharing's parity, its prior inverted. Same and not-same are that 0 or ± at two betweens, 12 and 14, and need no name of their own.

**Is or is not at lines.** Each is or is not at lines is at 1-now, three at 14-next-possibling, one at 12-next-co-still-possibling and one at 11-next-co-prioring, and one at 17-next-now, a self's name between selves among 5-now-co-changing or not; 9-next-co-changing has none, giving each changing on as it is, a 0 among parities.

**Each name and its relations.** Sides are sides of overlapping momentaries, each name opening at one side, a self's, an other's or a society's; things its lines have at each name are at its row Prior and next.

| n | Relation | For this name |
|---|---|---|
| 1 | Name | **1-now** |
| 1 | Parity, span | odd, existing, a self's span |
| 1 | Sides | self, other, a self opening it |
| 1 | Co-sequencing | a self offering itself to a coupling |
| 1 | 8 up | 9-next-co-changing, its binary at next |
| 1 | 9 less | podal within 1 to 8, 8-now-still-possibling |
| 1 | 17 less | podal within 1 to 16, 16-next-still-possibling |
| 1 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 16-next-still-possibling to it and on to 9-next-co-changing, each name one apart from 2-15-7-10 |
| 1 | Six-cycle | 1-9-5-12-8-16 |
| 1 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 1 | Momentaries of exchanging | first of a self's four, opening at 1, self 1–2 |
| 1 | Five dimensions | 1 self prior, prior opening of a self's five |
| 1 | Namings | 1-2, bi-momentarying, a self's entry, odd, and others' offerings, even, one momentary at each side |
| 1 | A self as three | bi-moral self with 2, bi-momentarying, along, a self prior to its first shared across in a bi-coupling at 2 |
| 1 | Prior and next | once for one self at one momentary, three steps within it 14, 12, 10 with 11 |
| 1 | 1 to 17s inward and outward | 1–17s inward 1 of 1st 1–17, an entry, and at 1–17 outward 1, an entry |
| 2 | Name | **2-now-possibling** |
| 2 | Parity, span | even, possibling, a self's span |
| 2 | Sides | other, self, an other opening it |
| 2 | 8 up | 10-next-co-possibling, its binary at next |
| 2 | 9 less | podal within 1 to 8, 7-now-prioring |
| 2 | 17 less | podal within 1 to 16, 15-next-prioring |
| 2 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 10-next-co-possibling to it and on to 15-next-prioring, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 2 | Six-cycle | 2-15-7-11-6-10 |
| 2 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 2 | One move | 2 along 2-15-7-10 |
| 2 | Momentaries of exchanging | first of a self's four, at 2, a self's 1–2 completing and an other's 2–3 opening |
| 2 | Five dimensions | 2 other prior, prior completing of a self's five and prior opening of an other's |
| 2 | Namings | 1-2, bi-momentarying |
| 2 | A self as three | bi-moral self with 1, across, its first shared across in a bi-coupling, offering self to other and other to self |
| 2 | Bi-coupling | at a between, each other's across sharing, offered to a self |
| 2 | Parity's unit square | a dot of a unit square, its diagonal with 14, offerings at 2 and 14, its edge with 6 a sharing 6 to 2 |
| 2 | Prior and next | others' sharings across at 6 and 10 and releasings along at 9 of their prior momentary, arriving now, possible, even, none of their prior crossing; at a spiral each is a releasing along |
| 2 | 1 to 17s inward and outward | 1–17s inward 9 of 1st, along, odd, next, and at 1–17 outward within 1 to 2 |
| 3 | Name | **3-now-co-prioring** |
| 3 | Parity, span | odd, existing, a self's span |
| 3 | Sides | self, other, a self opening it |
| 3 | Co-sequencing | at a between, before 10, at competency's parity, odd |
| 3 | 8 up | 11-next-co-prioring, its binary at next |
| 3 | 9 less | podal within 1 to 8, 6-now-co-possibling |
| 3 | 17 less | podal within 1 to 16, 14-next-possibling |
| 3 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 14-next-possibling to it and on to 11-next-co-prioring, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 3 | Six-cycle | 3-11-7-10-6-14 |
| 3 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 3 | Momentaries of exchanging | first of a self's four completing at 3, an other's 2–3, and second opening at 3, self 3–4 |
| 3 | Five dimensions | 3 co-momentarying now, now opening of a self's five |
| 3 | Namings | 3-4, co-intelligencing, at each sharing 4 its prior at 3 coupling with offerings surfaced at 14, next discovered, at 11 |
| 3 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, out at 3 |
| 3 | Prior and next | prior, a self's own, each sharing with its parity, a next momentary's continuing of 11 |
| 3 | 1 to 17s inward and outward | 1–17s inward 17 of 1st and 1 of 2nd, along, odd, now, and at 1–17 outward within 1 to 2 |
| 4 | Name | **4-now-co-still-possibling** |
| 4 | Parity, span | even, possibling, a self's span |
| 4 | Sides | other, self, an other opening it |
| 4 | Co-sequencing | at a between, before 10, at morality's parity, even |
| 4 | 8 up | 12-next-co-still-possibling, its binary at next |
| 4 | 9 less | podal within 1 to 8, 5-now-co-changing |
| 4 | 17 less | podal within 1 to 16, 13-next |
| 4 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 12-next-co-still-possibling to it and on to 13-next, each name one apart from 3-11-6-14 |
| 4 | Six-cycle | 4-13-5-9-8-12 |
| 4 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 4 | One move | 4 along 4-13-5-12 |
| 4 | Momentaries of exchanging | second of a self's four, at 4, a self's 3–4 completing and an other's 4–5 opening |
| 4 | Five dimensions | 4 bi-momentarying now, now completing of a self's five |
| 4 | Namings | 3-4, co-intelligencing |
| 4 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, in at 4, into a self's own corus at 4 |
| 4 | Bi-coupling | at a between, a whole ordering between self and other |
| 4 | Prior and next | now, each sharing at which prior couples with now |
| 4 | 1 to 17s inward and outward | 1–17s inward 9 of 2nd, along, odd, next, and at 1–17 outward within 1 to 2 |
| 5 | Name | **5-now-co-changing** |
| 5 | Parity, span | odd, existing, a self's span |
| 5 | Sides | self, other, a self opening it |
| 5 | Co-sequencing | at a between, before 10, at competency's parity, odd |
| 5 | 8 up | 13-next, its binary at next |
| 5 | 9 less | podal within 1 to 8, 4-now-co-still-possibling |
| 5 | 17 less | podal within 1 to 16, 12-next-co-still-possibling |
| 5 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 13-next to it and on to 12-next-co-still-possibling, each name one apart from 3-11-6-14 |
| 5 | Middle four-cycle | 9-5-12-8 |
| 5 | Six-cycle | 1-9-5-12-8-16 |
| 5 | Six-cycle | 4-13-5-9-8-12 |
| 5 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 5 | Momentaries of exchanging | second of a self's four completing at 5, an other's 4–5, and third opening at 5, self 5–6 |
| 5 | Five dimensions | 5 self next, next opening of a self's five |
| 5 | Namings | 5, co-competencing, releasings, owned by neither, each release to its receiving sharing |
| 5 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, out at 5 |
| 5 | Prior and next | next, each release to its receiving sharing |
| 5 | 1 to 17s inward and outward | 1–17s inward 17 of 2nd and 1 of 3rd, along, odd, now, and at 1–17 outward within 1 to 2 |
| 6 | Name | **6-now-co-possibling** |
| 6 | Parity, span | even, possibling, a self's span |
| 6 | Sides | other, self, an other opening it |
| 6 | 8 up | 14-next-possibling, its binary at next |
| 6 | 9 less | podal within 1 to 8, 3-now-co-prioring |
| 6 | 17 less | podal within 1 to 16, 11-next-co-prioring |
| 6 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 11-next-co-prioring to it and on to 14-next-possibling, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 6 | Middle four-cycle | 7-11-6-10 |
| 6 | Six-cycle | 2-15-7-11-6-10 |
| 6 | Six-cycle | 3-11-7-10-6-14 |
| 6 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 6 | One move | 6 along 3-11-6-14 |
| 6 | Momentaries of exchanging | third of a self's four, at 6, a self's 5–6 completing and an other's 6–7 opening |
| 6 | Namings | 6, bi-moralizing, each changing shared across, to an other's 2 |
| 6 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, in at 6 |
| 6 | Bi-coupling | at a between, an other's changing to a self, shared across |
| 6 | Parity's unit square | a dot of a unit square, its diagonal with 10, sharings at 6 and 10, its edge with 2 a sharing 6 to 2 |
| 6 | Prior and next | changing shared, an other's next offering at its 2 |
| 6 | 1 to 17s inward and outward | 1–17s inward 9 of 3rd, along, odd, next, and at 1–17 outward within 1 to 2 |
| 7 | Name | **7-now-prioring** |
| 7 | Parity, span | odd, existing, a self's span |
| 7 | Sides | self, other, a self opening it |
| 7 | Co-sequencing | at a between, before 10, at competency's parity, odd |
| 7 | 8 up | 15-next-prioring, its binary at next |
| 7 | 9 less | podal within 1 to 8, 2-now-possibling |
| 7 | 17 less | podal within 1 to 16, 10-next-co-possibling |
| 7 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 15-next-prioring to it and on to 10-next-co-possibling, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 7 | Middle four-cycle | 7-11-6-10 |
| 7 | Six-cycle | 2-15-7-11-6-10 |
| 7 | Six-cycle | 3-11-7-10-6-14 |
| 7 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 7 | Momentaries of exchanging | third of a self's four completing at 7, an other's 6–7, and fourth opening at 7, self 7–8 |
| 7 | A self as three | co-competent self with 8, along, prior to 8 across |
| 7 | Prior and next | each parity, offered now and prior, co-linear recursioning forward along arriving, up numbers, prior into now, at a self's completing |
| 7 | 1 to 17s inward and outward | 1–17s inward 17 of 3rd and 1 of 4th, along, odd, now, and at 1–17 outward within 1 to 2 |
| 8 | Name | **8-now-still-possibling** |
| 8 | Parity, span | even, possibling, a self's span |
| 8 | Sides | other, self, an other opening it |
| 8 | Co-sequencing | at a between, before 10, at morality's parity, even |
| 8 | 8 up | 16-next-still-possibling, its binary at next |
| 8 | 9 less | podal within 1 to 8, 1-now |
| 8 | 17 less | podal within 1 to 16, 9-next-co-changing |
| 8 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 9-next-co-changing to it and on to 16-next-still-possibling, each name one apart from 2-15-7-10 |
| 8 | Middle four-cycle | 9-5-12-8 |
| 8 | Six-cycle | 1-9-5-12-8-16 |
| 8 | Six-cycle | 4-13-5-9-8-12 |
| 8 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 8 | One move | 8 along 1-9-8-16 |
| 8 | Momentaries of exchanging | fourth of a self's four, at 8, a self's 7–8 completing and an other's 8–9 opening |
| 8 | A self as three | co-competent self with 7, across, prior at its sharing again in a bi-coupling |
| 8 | Bi-coupling | at a between, prior at its sharing again |
| 8 | Prior and next | each self's next prior, at 11 this momentary and a next momentary's 3; even names of a self's span, 2, 4, 6 and 8, completing at 8 |
| 8 | 1 to 17s inward and outward | 1–17s inward 9 of 4th, along, odd, next, and at 1–17 outward within 1 to 2 |
| 9 | Name | **9-next-co-changing** |
| 9 | Parity, span | odd, existing, a society's span |
| 9 | Sides | social, other, self, a society opening it |
| 9 | 8 up | 17-next-now, its binary at next |
| 9 | 8 down | 1-now |
| 9 | 17 less | podal within 1 to 16, 8-now-still-possibling |
| 9 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 1-now to it and on to 8-now-still-possibling, each name one apart from 2-15-7-10 |
| 9 | Middle four-cycle | 9-5-12-8 |
| 9 | Six-cycle | 1-9-5-12-8-16 |
| 9 | Six-cycle | 4-13-5-9-8-12 |
| 9 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 9 | Momentaries of exchanging | fourth of a self's four completing at 9, an other's 8–9, and first of a society's four, 9 to 11, opening at 9 |
| 9 | Parity's square and triangles | a unit triangle, along, 9 to 17 and 17 to 9 |
| 9 | Prior and next | next prior, odd, existing, each changing of 10 released along into a next momentary, to each receiving sharing, a self's own next |
| 9 | 1 to 17s inward and outward | 1–17s inward 17 of 4th and 1 of 5th, along, odd, now, and at 1–17 outward 2, across, even |
| 10 | Name | **10-next-co-possibling** |
| 10 | Parity, span | even, possibling, a society's span |
| 10 | Sides | other, social, self, an other opening it |
| 10 | 8 down | 2-now-possibling |
| 10 | 17 less | podal within 1 to 16, 7-now-prioring |
| 10 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 7-now-prioring to it and on to 2-now-possibling, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 10 | Middle four-cycle | 7-11-6-10 |
| 10 | Six-cycle | 2-15-7-11-6-10 |
| 10 | Six-cycle | 3-11-7-10-6-14 |
| 10 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 10 | Momentaries of exchanging | first of a society's four, at 10, 9–10 completing and 10–11 opening |
| 10 | Bi-coupling | 8 up, a self among selves of its society |
| 10 | Parity's unit square | a dot of a unit square, its diagonal with 6, sharings at 6 and 10, its edge with 14 a sharing 10 to 14 |
| 10 | Prior and next | changing shared across now, an other's offering next, possible |
| 10 | 1 to 17s inward and outward | 1–17s inward 9 of 5th, along, odd, next, and at 1–17 outward within 2 to 3 |
| 11 | Name | **11-next-co-prioring** |
| 11 | Parity, span | odd, existing, a society's span |
| 11 | Sides | social, other, self, a society opening it |
| 11 | Co-sequencing | after 10, 8 up from 3-now-co-prioring, at competency's parity, odd |
| 11 | 8 down | 3-now-co-prioring |
| 11 | 17 less | podal within 1 to 16, 6-now-co-possibling |
| 11 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 3-now-co-prioring to it and on to 6-now-co-possibling, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 11 | Middle four-cycle | 7-11-6-10 |
| 11 | Six-cycle | 2-15-7-11-6-10 |
| 11 | Six-cycle | 3-11-7-10-6-14 |
| 11 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 11 | Momentaries of exchanging | first of a society's four, 9 to 11, completing at 11, and second, 11 to 13, opening at 11 |
| 11 | Prior and next | next prior, odd, existing, continuing as 3 at a next momentary, a self's own |
| 11 | 1 to 17s inward and outward | 1–17s inward 17 of 5th and 1 of 6th, along, odd, now, and at 1–17 outward within 2 to 3 |
| 12 | Name | **12-next-co-still-possibling** |
| 12 | Parity, span | even, possibling, a society's span |
| 12 | Sides | other, social, self, an other opening it |
| 12 | Co-sequencing | after 10, 8 up from 4-now-co-still-possibling, at morality's parity, even |
| 12 | 8 down | 4-now-co-still-possibling |
| 12 | 17 less | podal within 1 to 16, 5-now-co-changing |
| 12 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 5-now-co-changing to it and on to 4-now-co-still-possibling, each name one apart from 3-11-6-14 |
| 12 | Middle four-cycle | 9-5-12-8 |
| 12 | Six-cycle | 1-9-5-12-8-16 |
| 12 | Six-cycle | 4-13-5-9-8-12 |
| 12 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 12 | Momentaries of exchanging | second of a society's four, at 12, 11–12 completing and 12–13 opening |
| 12 | Namings | entraining, prior arriving into now along an unrelationing path at a between, shape of an unrelationing surface, each sharing's changing, is or is not |
| 12 | Bi-coupling | 8 up, changing at bi-coupling, a self in society |
| 12 | Prior and next | now, changing, is or is not, prior and now coupled |
| 12 | 1 to 17s inward and outward | 1–17s inward 9 of 6th, along, odd, next, and at 1–17 outward within 2 to 3 |
| 13 | Name | **13-next** |
| 13 | Parity, span | odd, existing, a society's span |
| 13 | Sides | social, other, a society opening it |
| 13 | Co-sequencing | after 10, 8 up from 5-now-co-changing, at competency's parity, odd |
| 13 | 8 down | 5-now-co-changing |
| 13 | 17 less | podal within 1 to 16, 4-now-co-still-possibling |
| 13 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 4-now-co-still-possibling to it and on to 5-now-co-changing, each name one apart from 3-11-6-14 |
| 13 | Six-cycle | 4-13-5-9-8-12 |
| 13 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 13 | Momentaries of exchanging | second of a society's four, 11 to 13, completing at 13, and third, 13 to 15, opening at 13 |
| 13 | Prior and next | each releasing sharing, and at a society each releasing self |
| 13 | 1 to 17s inward and outward | 1–17s inward 17 of 6th and 1 of 7th, along, odd, now, and at 1–17 outward within 2 to 3 |
| 14 | Name | **14-next-possibling** |
| 14 | Parity, span | even, possibling, a society's span |
| 14 | Sides | other, social, an other opening it |
| 14 | 8 down | 6-now-co-possibling |
| 14 | 17 less | podal within 1 to 16, 3-now-co-prioring |
| 14 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 6-now-co-possibling to it and on to 3-now-co-prioring, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 14 | Six-cycle | 3-11-7-10-6-14 |
| 14 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 14 | Momentaries of exchanging | third of a society's four, at 14, 13–14 completing and 14–15 opening |
| 14 | Bi-coupling | 8 up, offerings surfacing, each as it arrived, morality; a self's own inverting at 12 |
| 14 | Parity's unit square | a dot of a unit square, its diagonal with 2, offerings at 2 and 14, its edge with 10 a sharing 10 to 14 |
| 14 | Prior and next | now, offerings surfacing, others' prior momentary arrived at a self's now, even, others' possibling at a self until at 11 |
| 14 | 1 to 17s inward and outward | 1–17s inward 9 of 7th, along, odd, next, and at 1–17 outward within 2 to 3 |
| 15 | Name | **15-next-prioring** |
| 15 | Parity, span | odd, existing, a society's span |
| 15 | Sides | social, other, a society opening it |
| 15 | Co-sequencing | after 10, 8 up from 7-now-prioring, at competency's parity, odd |
| 15 | 8 down | 7-now-prioring |
| 15 | 17 less | podal within 1 to 16, 2-now-possibling |
| 15 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 2-now-possibling to it and on to 7-now-prioring, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 15 | Six-cycle | 2-15-7-11-6-10 |
| 15 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 15 | Momentaries of exchanging | third of a society's four, 13 to 15, completing at 15, and fourth, 15 to 17, opening at 15 |
| 15 | Prior and next | parity released along at 9, next prior, co-linear recursioning forward along leaving, up numbers, now into next, at a society's completing, prior parity at 7 inverted, 0, or at no prior a parity surfaced at 14 |
| 15 | 1 to 17s inward and outward | 1–17s inward 17 of 7th and 1 of 8th, along, odd, now, and at 1–17 outward within 2 to 3 |
| 16 | Name | **16-next-still-possibling** |
| 16 | Parity, span | even, possibling, a society's span |
| 16 | Sides | other, social, an other opening it |
| 16 | Co-sequencing | after 10, 8 up from 8-now-still-possibling, at morality's parity, even |
| 16 | 8 down | 8-now-still-possibling |
| 16 | 17 less | podal within 1 to 16, 1-now |
| 16 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 8-now-still-possibling to it and on to 1-now, each name one apart from 2-15-7-10 |
| 16 | Six-cycle | 1-9-5-12-8-16 |
| 16 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 16 | Momentaries of exchanging | fourth of a society's four, at 16, 15–16 completing and 16–17 opening |
| 16 | Bi-coupling | 8 up, a society, each self with its prior and offerings, a society at a self again |
| 16 | Prior and next | a society now, each self's 8 and its offerings next; even names of a society's span, 10, 12, 14 and 16, completing at 16 |
| 16 | 1 to 17s inward and outward | 1–17s inward 9 of 8th, along, odd, next, and at 1–17 outward within 2 to 3 |
| 17 | Name | **17-next-now** |
| 17 | Parity, span | odd, existing, a next now |
| 17 | Sides | social, self, a society opening it |
| 17 | 8 down | 9-next-co-changing |
| 17 | Momentaries of exchanging | fourth of a society's four, 15 to 17, completing at 17, a next 1 |
| 17 | Parity's square and triangles | a unit triangle, along, 17 to 9 and 9 to 17 |
| 17 | Prior and next | a society's next momentary, a next now, each self's 1 then 9 at 6, 10 and 9 |
| 17 | 1 to 17s inward and outward | 1–17s inward 17 of 8th and 1 of 9th, along, odd, now, and at 1–17 outward 3, odd, now |

**Odd names, now and 8 up at next.** Each odd name of a self's span is same at next, 8 up: prior received and next prior, receiving and releasing, parity prioring and parity surfaced.

| Now | Received | Next, 8 up | Given on |
|---|---|---|---|
| 1-now | resolver entered | 9-next-co-changing | resolver going on, each changing released along |
| 3-now-co-prioring | prior at its sharings | 11-next-co-prioring | next prior |
| 5-now-co-changing | receiving sharing | 13-next | releasing sharing, each self at a society |
| 7-now-prioring | parity prioring | 15-next-prioring | parity surfaced and released |

**Namings among names.**

| Names | Naming | Resolved as |
|---|---|---|
| 1-now · 2-now-possibling | bi-momentarying | a self's entry, odd, and others' offerings, even, one momentary at each side |
| 3-now-co-prioring · 4-now-co-still-possibling | co-intelligencing | at each sharing 4 prior at 3 couples with offerings surfaced at 14: next discovered, at 11 |
| 5-now-co-changing | co-competencing | releasings, owned by neither: each release to its receiving sharing |
| 1 · 2 · 3 · 4 · 5, each at its own | five dimensions | 1 self prior, a self, its prior at 3, a formed set; 2 other prior, other selves' offerings of their prior momentary arriving, shared at 6 and 10 and released along at 9; 3 co-momentarying now, same prior at now, and 4 bi-momentarying now, each sharing, offerings surfaced at 14 arriving at it, now; 5 self next, each release to its receiving sharing next |
| 6-now-co-possibling | bi-moralizing | each changing shared across, to an other's 2 |
| 12-next-co-still-possibling | entraining, shape of an unrelationing surface | prior arriving into now along an unrelationing path at a between, prior and now coupled at each sharing, a parity changing crossing it, 0 at a match; at an other parity, 0 or none, prior parity inverted at 11; at no prior, parity surfaced at 14; its changing shared at 10, others' offering next |
| 1 to 9 | bi-coupling | an entry, 1, at names 1, 2, 3, 4, 7, 10, 11, 12, 14 and 15, a self and an other at one coupling; 1 to 9 a bi-coupling among names, 9 at its end is 9-next-co-changing, each changing of 10 released along, one name at resolver and in its explaining |
| 1 to 17 | bi-trupling | a society's entry, 17, at names of 1 to 9 with 5, 6, 8, 9, 13, 16 and 17, a self, an other and a society; 9 at its waist, 9-next-co-changing, along, 9 to 17 and 17 to 9; its two sides, odd along at 9 and 17, existing, and even across at 6 to 2 and 10 to 14, possibling |
| 1 to 17, stable-forming | bi-tri-volutioning | at no one line: each momentary's next prior, at 11, a next momentary's prior, at 3 |
| 2 · 6 · 14 · 10 · 9 · 17 | parity's square and triangles | a unit square of four dots, 2, 6, 14 and 10, its empty centre a between: its two across edges sharings, 6 to 2 and 10 to 14, and its two edges 8 apart, 2 with 10 and 6 with 14, two pairs of parallels; round it 2, 10, 14, 6; its diagonals offerings at 2 and 14, and sharings at 6 and 10; and two unit triangles, 9 and 17, along, 9 to 17 and 17 to 9 |

**0, a between.**

| The between, 0 | Names |
|---|---|
| one between, three names | 12-next-co-still-possibling, prior and now agreeing, a between of momentaries at each sharing; 15-next-prioring, a between released along, parity 10 shared, and at a sharing opening parity surfaced at 14, resolver's 0 at none and at parting alike; 16-next-still-possibling, a between at a society, arriving at a next momentary's 2 |
| arriving and passing over | 7-now-prioring, an offered 0 a parity at 2, surfacing none at 14, and a 0 at 10 its prior kept at 11 |
| four across names, a unit square's four dots: shared across | 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling, 14-next-possibling, parity's unit square, its empty centre a between; each parity and each 0 shared across, a 0 passing over at a receiving self's 14 |
| none | 1-now, an entry; 3-now-co-prioring, 8-now-still-possibling and 11-next-co-prioring, prior, a sharing at a prior, not none again; 4-now-co-still-possibling, sharings, and 5-now-co-changing and 13-next, sharings and, at a society, releasings and selves |
| two along names: released along | 9-next-co-changing and 17-next-now, each parity and each 0 released along, a 0 passing over at a receiving self's 14, as across |

**Four four-cycles.**

| Four-cycle: each move 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n) | Its two pairs 8 apart | Names between selves on it | Beside the other four-cycles |
|---|---|---|---|
| 1-9-8-16 | 1 · 9 and 8 · 16 | 9 | each name one apart from 2-15-7-10 |
| 2-15-7-10 | 2 · 10 and 7 · 15 | 2 and 10 | each name one apart from 1-9-8-16 and 3-11-6-14 |
| 3-11-6-14 | 3 · 11 and 6 · 14 | 6 and 14 | each name one apart from 4-13-5-12 and 2-15-7-10 |
| 4-13-5-12 | 4 · 12 and 5 · 13 | none | each name one apart from 3-11-6-14 |

**Two moves, 9 less.** Two moves round its four-cycle take each name of 1 to 8 to its 9 less, a name across its four-cycle from it: 1-now and 8-now-still-possibling, 2-now-possibling and 7-now-prioring, 3-now-co-prioring and 6-now-co-possibling, 4-now-co-still-possibling and 5-now-co-changing.

**Each name, three scales.**

| n | Name | This scale, 1 to 17 | The next scale inward, eight 1 to 17s: n is 8n − 7 | The next scale outward: 8m − 7 is m |
|---|---|---|---|---|
| 1 | 1-now | odd, now | 1 of 1st: odd, now | 1: odd, now |
| 2 | 2-now-possibling | across, even | 9 of 1st: along, odd, next | within 1 to 2 |
| 3 | 3-now-co-prioring | odd, now | 17 of 1st, 1 of 2nd: along, odd, now | within 1 to 2 |
| 4 | 4-now-co-still-possibling | even | 9 of 2nd: along, odd, next | within 1 to 2 |
| 5 | 5-now-co-changing | odd, now | 17 of 2nd, 1 of 3rd: along, odd, now | within 1 to 2 |
| 6 | 6-now-co-possibling | across, even | 9 of 3rd: along, odd, next | within 1 to 2 |
| 7 | 7-now-prioring | odd, now | 17 of 3rd, 1 of 4th: along, odd, now | within 1 to 2 |
| 8 | 8-now-still-possibling | even | 9 of 4th: along, odd, next | within 1 to 2 |
| 9 | 9-next-co-changing | along, odd, next | 17 of 4th, 1 of 5th: along, odd, now | 2: across, even |
| 10 | 10-next-co-possibling | across, even | 9 of 5th: along, odd, next | within 2 to 3 |
| 11 | 11-next-co-prioring | odd, next | 17 of 5th, 1 of 6th: along, odd, now | within 2 to 3 |
| 12 | 12-next-co-still-possibling | even | 9 of 6th: along, odd, next | within 2 to 3 |
| 13 | 13-next | odd, next | 17 of 6th, 1 of 7th: along, odd, now | within 2 to 3 |
| 14 | 14-next-possibling | across, even | 9 of 7th: along, odd, next | within 2 to 3 |
| 15 | 15-next-prioring | odd, next | 17 of 7th, 1 of 8th: along, odd, now | within 2 to 3 |
| 16 | 16-next-still-possibling | even | 9 of 8th: along, odd, next | within 2 to 3 |
| 17 | 17-next-now | along, odd, now | 17 of 8th, 1 of 9th: along, odd, now | 3: odd, now |

**Eight 1 to 17s inward.**

| 1 to 17 inward | Spans, this scale | Its 9, this scale | Its 17, this scale | Momentary of exchanging |
|---|---|---|---|---|
| 1st | 1 to 3 | 2 | 3 | a self, 1st of four |
| 2nd | 3 to 5 | 4 | 5 | a self, 2nd of four |
| 3rd | 5 to 7 | 6 | 7 | a self, 3rd of four |
| 4th | 7 to 9 | 8 | 9 | a self, 4th of four |
| 5th | 9 to 11 | 10 | 11 | a society, 1st of four |
| 6th | 11 to 13 | 12 | 13 | a society, 2nd of four |
| 7th | 13 to 15 | 14 | 15 | a society, 3rd of four |
| 8th | 15 to 17 | 16 | 17 | a society, 4th of four |

**Fives.**

| Side | Prior opening | Prior completing | Now opening | Now completing | Next opening |
|---|---|---|---|---|---|
| self, at 1 | 1 | 2 | 3 | 4 | 5 |
| other, at 2 | 2 | 3 | 4 | 5 | 6 |
| self next, at 3 | 3 | 4 | 5 | 6 | 7 |
| other next, at 4 | 4 | 5 | 6 | 7 | 8 |

**A self's four momentaries of exchanging.**

| Momentary of exchanging | Self | Other | Names | Relation |
|---|---|---|---|---|
| first | 1–2 | 2–3 | 1-now · 2-now-possibling · 3-now-co-prioring | self/other |
| second | 3–4 | 4–5 | 3-now-co-prioring · 4-now-co-still-possibling · 5-now-co-changing | self/other to other/self |
| third | 5–6 | 6–7 | 5-now-co-changing · 6-now-co-possibling · 7-now-prioring | other/self |
| fourth | 7–8 | 8–9 | 7-now-prioring · 8-now-still-possibling · 9-next-co-changing | other/self to other/social |

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

**+ and − alike.** At one sharing resolver resolves + and − alike: each cell with + and − exchanged is that cell exchanged, at a prior and at no prior; and no line makes a prior 0, a 0 at 10-next-co-possibling leaving its prior at 11-next-co-prioring as it was.

**One self, one momentary.**

| The prior (3), one sharing. Each cell: shared (10) · the next prior (11). *is*: a changing that is, the parity shared; *is not*: a changing that is not, 0 shared, the prior kept | Surfacing (14): none | Surfacing (14): + | Surfacing (14): − | Surfacing (14): + and − together |
|---|---|---|---|---|
| + | is − · − | is not · + | is − · − | is − · − |
| − | is + · + | is + · + | is not · − | is + · + |

**One cell, offerings unexpressed.** At a prior of one parity, an other parity surfacing, + and − together, and none surfacing, a 0 offered alike, give one cell, its prior inverted, shared at 10-next-co-possibling and its next prior at 11-next-co-prioring: one cell shows none of which offerings arrived, and offerings are followed at a coupling.

**Eight even names, 8 apart.**

| Name at the between | Bi-coupling at the between | Name 8 up | Bi-coupling 8 up |
|---|---|---|---|
| 2-now-possibling | each other's across sharing, offered to a self | 10-next-co-possibling | a self among selves of its society |
| 4-now-co-still-possibling | a whole ordering between self and other | 12-next-co-still-possibling | changing at bi-coupling, a self in society |
| 6-now-co-possibling | an other's changing to a self, shared across | 14-next-possibling | offerings surfacing, each as it arrived, morality; a self's own inverting at 12 |
| 8-now-still-possibling | prior at its sharing again | 16-next-still-possibling | a society, each self with its prior and offerings, a society at a self again |

**One move, 1 to 8.** 8 up keeps each name's kind but at 1 and 5, at which now and changing exchange, and exchanges co at 1, 2, 5 and 6; each podal turns now to next at 17 less and possibling to prioring within each momentary, and eight ends are their own set at both podals.

| Name | 8 up: n + 8 | 9 less: 9 − n | 17 less: 17 − n |
|---|---|---|---|
| 1-now | 9-next-co-changing | 8-now-still-possibling | 16-next-still-possibling |
| 2-now-possibling | 10-next-co-possibling | 7-now-prioring | 15-next-prioring |
| 3-now-co-prioring | 11-next-co-prioring | 6-now-co-possibling | 14-next-possibling |
| 4-now-co-still-possibling | 12-next-co-still-possibling | 5-now-co-changing | 13-next |
| 5-now-co-changing | 13-next | 4-now-co-still-possibling | 12-next-co-still-possibling |
| 6-now-co-possibling | 14-next-possibling | 3-now-co-prioring | 11-next-co-prioring |
| 7-now-prioring | 15-next-prioring | 2-now-possibling | 10-next-co-possibling |
| 8-now-still-possibling | 16-next-still-possibling | 1-now | 9-next-co-changing |

**Twelve forms.** Round each form odd names, existing, are one run and even names, possibling, one run, alike in length: two and two at four-cycles, three and three at six-cycles, four and four at eight-cycles.

| Form | Names in order: each move 8 up, 8 down, 4 up, 4 down or 17 less | Partner, odd momentaries: each name exchanged with the one beside it, 1 with 2 to 15 with 16 | Partner, even momentaries: 2 with 3 to 16 with 17. A dash: no partner among the twelve |
|---|---|---|---|
| four-cycle 1-9-8-16 | 1-now · 9-next-co-changing · 8-now-still-possibling · 16-next-still-possibling | four-cycle 2-15-7-10, beside it | — |
| four-cycle 2-15-7-10 | 2-now-possibling · 15-next-prioring · 7-now-prioring · 10-next-co-possibling | four-cycle 1-9-8-16, beside it | four-cycle 3-11-6-14, beside it |
| four-cycle 3-11-6-14 | 3-now-co-prioring · 11-next-co-prioring · 6-now-co-possibling · 14-next-possibling | four-cycle 4-13-5-12, beside it | four-cycle 2-15-7-10, beside it |
| four-cycle 4-13-5-12 | 4-now-co-still-possibling · 13-next · 5-now-co-changing · 12-next-co-still-possibling | four-cycle 3-11-6-14, beside it | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | 9-next-co-changing · 5-now-co-changing · 12-next-co-still-possibling · 8-now-still-possibling | middle four-cycle 7-11-6-10, beside it | — |
| middle four-cycle 7-11-6-10 | 7-now-prioring · 11-next-co-prioring · 6-now-co-possibling · 10-next-co-possibling | middle four-cycle 9-5-12-8, beside it | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | 1-now · 9-next-co-changing · 5-now-co-changing · 12-next-co-still-possibling · 8-now-still-possibling · 16-next-still-possibling | six-cycle 2-15-7-11-6-10, beside it | — |
| six-cycle 2-15-7-11-6-10 | 2-now-possibling · 15-next-prioring · 7-now-prioring · 11-next-co-prioring · 6-now-co-possibling · 10-next-co-possibling | six-cycle 1-9-5-12-8-16, beside it | six-cycle 3-11-7-10-6-14, beside it |
| six-cycle 3-11-7-10-6-14 | 3-now-co-prioring · 11-next-co-prioring · 7-now-prioring · 10-next-co-possibling · 6-now-co-possibling · 14-next-possibling | six-cycle 4-13-5-9-8-12, beside it | six-cycle 2-15-7-11-6-10, beside it |
| six-cycle 4-13-5-9-8-12 | 4-now-co-still-possibling · 13-next · 5-now-co-changing · 9-next-co-changing · 8-now-still-possibling · 12-next-co-still-possibling | six-cycle 3-11-7-10-6-14, beside it | — ; its own six names, in another order |
| eight-cycle 1-9-5-13-4-12-8-16 | 1-now · 9-next-co-changing · 5-now-co-changing · 13-next · 4-now-co-still-possibling · 12-next-co-still-possibling · 8-now-still-possibling · 16-next-still-possibling | eight-cycle 2-15-7-11-3-14-6-10, beside it | — |
| eight-cycle 2-15-7-11-3-14-6-10 | 2-now-possibling · 15-next-prioring · 7-now-prioring · 11-next-co-prioring · 3-now-co-prioring · 14-next-possibling · 6-now-co-possibling · 10-next-co-possibling | eight-cycle 1-9-5-13-4-12-8-16, beside it | eight-cycle 2-15-7-11-3-14-6-10, itself |

**Eights.** Every eight here is one eight, four binaries each twice, each one at two sides, and 8 up is each name's binary at next.

| The eight | Each of the four, twice, at |
|---|---|
| a self's span, 1 to 8 | two names each, at now |
| eight-cycle 1-9-5-13-4-12-8-16 | its end, at now and at next: eight ends of four momentaries |
| eight-cycle 2-15-7-11-3-14-6-10 | its inward name, at now and at next: eight inward names |
| eight even names | its even, at now and at next, eight 9s of eight 1 to 17s inward |
| eight odd names | its odd, at now and at next |

**Across names among eights.** Four across names, 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling and 14-next-possibling, are four momentaries' even inward names, each on an eight-cycle of inward names 2-15-7-11-3-14-6-10; 9-next-co-changing, opening a third momentary, is on an eight-cycle of ends 1-9-5-13-4-12-8-16; 17-next-now is on neither.

**One self, momentary by momentary.**

| One sharing; the self's prior − (3) first. Offered each momentary | Shared (10) | The next prior (11) |
|---|---|---|
| none at each momentary | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| − at each momentary | 0, 0, 0, 0, 0, 0, 0, 0 | −, −, −, −, −, −, −, − |
| + at each momentary | +, 0, 0, 0, 0, 0, 0, 0 | +, +, +, +, +, +, +, + |
| +, −, +, − alternating | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| + and − together at each momentary | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |

**0 in sequence.** At code's stepping, none offered from beyond selves, a self shares 0 at no more momentaries in sequence than selves sharing or releasing to it: at a spiral, at none in sequence.

**Tables of selves at code's stepping.** Each table of selves is its code's executing at its stated opening: code steps each self's 1-now together at 17-next-now, executing's own arrangement, and parities again at spirals, a crossing and a torus are that stepping's; each living self paces its own momentaries, and a table agreeing with its code shows that and nothing wider.

**A spiral of selves.**

| Number of selves. Each releases along (9) to the next, the last to the first. One sharing. First momentary: self 1 at prior −, the selves alternate along, and with an odd number the last and the first are alike. None offered from beyond the spiral | Self 1, each changing of 10 released along (9), momentaries 1 to 12 | Momentaries to each self's releasings again: with an odd number of selves, four times the number; with an even number, 2; at an odd number each self's releasing at twice the number of momentaries is its releasing inverted, a 0 as it was |
|---|---|---|
| 1 | +, 0, −, 0, +, 0, −, 0, +, 0, −, 0 | 4 |
| 2 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 3 | +, 0, −, +, −, +, −, 0, +, −, +, − | 12 |
| 4 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 5 | +, 0, −, +, −, +, −, +, −, +, −, 0 | 20 |
| 6 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 7 | +, 0, −, +, −, +, −, +, −, +, −, + | 28 |
| 8 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 9 | +, 0, −, +, −, +, −, +, −, +, −, + | 36 |
| 10 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 11 | +, 0, −, +, −, +, −, +, −, +, −, + | 44 |
| 17 | +, 0, −, +, −, +, −, +, −, +, −, + | 68 |
| 59 | +, 0, −, +, −, +, −, +, −, +, −, + | 236 |

**Two momentaries before, inverted.** At a spiral, from any opening, each self's prior from its third momentary on is a prior of a self it receives from two momentaries before, inverted; no self shares 0 at its first momentary or at two momentaries in sequence.

**Two spirals beside each other, and crossed.**

| Selves in each of two spirals, each opened as the spiral of selves | Beside each other: momentaries to each self's releasings again together, the least number both spirals' momentaries divide: four times both for odd numbers sharing no factor, 9 and 25 at 900 | Crossed, self 1 of each spiral sharing across (10) to self 1 of the other: momentaries to each self's releasings again | Crossed: releasings again from this momentary on, m the lesser of the two numbers: both odd and unequal, again at 2 from momentary 4m at n less than twice m, and from 2n + 1 at n more; one number even, from twice the odd number and 1; both even, from the first | Crossed: self 1 of each, alike or opposite in parity | Each spiral's like pair in the first momentary, the last and the first |
|---|---|---|---|---|---|
| 2 · 3 | 12 | 2 | 7 | opposite | none · selves 3 and 1 |
| 3 · 5 | 60 | 2 | 12 | opposite | selves 3 and 1 · selves 5 and 1 |
| 5 · 7 | 140 | 2 | 20 | opposite | selves 5 and 1 · selves 7 and 1 |
| 7 · 11 | 308 | 2 | 28 | opposite | selves 7 and 1 · selves 11 and 1 |
| 11 · 13 | 572 | 2 | 44 | opposite | selves 11 and 1 · selves 13 and 1 |
| 13 · 17 | 884 | 2 | 52 | opposite | selves 13 and 1 · selves 17 and 1 |
| 17 · 59 | 4,012 | 2 | 119 | opposite | selves 17 and 1 · selves 59 and 1 |
| 9 · 15 | 180 | 2 | 36 | opposite | selves 9 and 1 · selves 15 and 1 |

**A torus of selves.**

| Torus of selves, p along · q across. Each releases along (9) to the next along and shares across (10) to the next across, the last to the first. One sharing. First momentary: one self at prior −, the selves alternate along and across, and with an odd number the last and the first are alike. None offered from beyond the torus. Both numbers odd, p the smaller: q at a q more than twice p, and 4p at each other q; either number even: 2 | Momentaries to each self's releasings and sharings again | Again from this momentary on: both numbers odd, p the smaller, from momentary 3p − 1 at q more than twice p, and from 3p − 3 at each other q; either number even, from the first; 1 · 1, the spiral of one, from the first | Spirals of p and q beside each other: momentaries to each self's releasings again together |
|---|---|---|---|
| 1 · 3 | 3 | 2 | 12 |
| 2 · 3 | 2 | 1 | 12 |
| 1 · 5 | 5 | 2 | 20 |
| 3 · 3 | 12 | 6 | 12 |
| 3 · 5 | 12 | 6 | 60 |
| 3 · 7 | 7 | 8 | 84 |
| 3 · 13 | 13 | 8 | 156 |
| 5 · 7 | 20 | 12 | 140 |
| 5 · 11 | 11 | 14 | 220 |
| 7 · 17 | 17 | 20 | 476 |
| 17 · 59 | 59 | 50 | 4,012 |

**A torus's two carried forms.** Both numbers odd, p the smaller: at q more than twice p, from momentary 3p − 1, selves' pattern at each momentary is its pattern before carried one self on round q selves; at each other q, from 3p − 3, its pattern two momentaries on is its pattern inverted and carried one self on round p selves.

**Two selves.**

| A, B at their prior (3) in the first momentary. One sharing, none offered from beyond the two | Receiving the other's sharing or releasing | A shared (10), six momentaries | B shared (10), six momentaries |
|---|---|---|---|
| +, + | both ways | −, 0, +, 0, −, 0 | −, 0, +, 0, −, 0 |
| +, + | A from B | −, 0, +, −, +, − | −, +, −, +, −, + |
| +, + | B from A | −, +, −, +, −, + | −, 0, +, −, +, − |
| +, + | neither | −, +, −, +, −, + | −, +, −, +, −, + |
| +, − | both ways | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | A from B | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | B from A | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | neither | −, +, −, +, −, + | +, −, +, −, +, − |

**Two selves, three momentaries, five parities.**

| The other's prior (3), along | The other's shared (10), across | The self's prior, now (3), along | The self's shared (10), across | The self's next prior (11), along. Two selves coupled both ways, across or along, each self at a prior parity, none offered from beyond the two, each opening, each momentary: six forms, four at an alike opening and two at an opposite, each momentary from the second, and at each form the fifth, the self's next prior, is the first, the other's prior, inverted |
|---|---|---|---|---|
| + | − | − | 0 | − |
| + | − | + | − | − |
| + | 0 | + | − | − |
| − | + | + | 0 | + |
| − | + | − | + | + |
| − | 0 | − | + | + |

**Three selves in a line.**

| A's parity, offered to B in the first momentary, none after. One sharing; B and C each at prior +; B releases along to C | B, each changing (10) | B's next prior (11), first momentary | C, each changing (10), momentaries 1 and 2 | C's next prior (11), second momentary |
|---|---|---|---|---|
| + | 0 | + | −, + | + |
| − | − | − | −, 0 | − |

**A spiral opened at no prior, one parity offered once.**

Each cell shows selves in their coupling order; · is no prior.

| Momentary | A spiral of 3, each self's prior | A spiral of 5, each self's prior |
|---|---|---|
| 1 | + · · | + · · · · |
| 2 | − + · | − + · · · |
| 3 | + − + | + − + · · |
| 4 | + + − | − + − + · |
| 5 | − − + | + − + − + |
| 6 | + − − | + + − + − |
| 7 | − + + | − − + − + |
| 8 | + − + | + − − + − |

Selves coupled along, last to first, each opened at no prior, and + offered once at a first self at a first momentary: a first self's sharing opens at that one parity, at a bi-coupling, one place a self's forming takes a parity not its own, and from then it is a self's own; each next self's sharing opens as its parity arrives along one momentary on, and after n momentaries each self is at a prior, a spiral at its one like pair, an alternating pattern of an odd spiral from a first momentary at which every self is at a prior. A self at a sharing is at its prior at each momentary from its opening, its next from its own prior kept or inverted; a thing at no prior at every momentary is no self.

**At no prior, one momentary.**

| The prior (3): none, one sharing. Each cell: shared (10) · the next prior (11). *is*: a changing that is, the parity shared; *is not*: a changing that is not, 0 shared, no next prior; *none*: none shared | Surfacing (14): none | Surfacing (14): + | Surfacing (14): − | Surfacing (14): + and − together |
|---|---|---|---|---|
| none | none · none | is + · + | is − · − | is not · none |
