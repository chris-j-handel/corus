Exhibit ONE Natural Resolver v389

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

CONNECTORS = {
    2: ('2-now-possibling', 'arriving'),
    6: ('6-now-co-possibling', 'sharing'),
    9: ('9-next-co-changing', 'along'),
    10: ('10-next-co-possibling', 'sharing'),
    14: ('14-next-possibling', 'arriving'),
    17: ('17-next-now', 'along'),
}
JOINS = {10: 14, 6: 2, 17: 9, 9: 17}
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

**At the drawing.** The prior at 3 meets the surfacing at 14 at each sharing at 12; the changings at 10, the same at 6, go across to another self's 2 and 14; the next prior goes to 11 and on to 3 at next; and 9 releases along by 5 to another self's 17. At each join the sharing side is the self and the arriving side another self, each a self, and the society is its selves.

**Seventeen names.**

| n | Name | Momentary | Parity | Co | At the resolver |
|---|---|---|---|---|---|
| 1 | **1-now** | now, the self's span | odd, existing | one | each self's momentary, entered at the society's 17 |
| 2 | **2-now-possibling** | now, the self's span | even, possibling | one | the offerings arriving at the self, each sharing with its parity |
| 3 | **3-now-co-prioring** | now, the self's span | odd, existing | between two | the prior at its sharings, each sharing with its parity |
| 4 | **4-now-co-still-possibling** | now, the self's span | even, possibling | between two | each sharing at which the offerings and the prior meet |
| 5 | **5-now-co-changing** | now, the self's span | odd, existing | between two | the releasings, each releasing sharing with the self it arrives at |
| 6 | **6-now-co-possibling** | now, the self's span | even, possibling | between two | each sharing's changing shared across, to another self's 2 |
| 7 | **7-now-prioring** | now, the self's span | odd, existing | one | each parity read: an offering's, the prior's and a changing's |
| 8 | **8-now-still-possibling** | now, the self's span | even, possibling | one | each self's next prior, beside the other selves' |
| 9 | **9-next-co-changing** | next, the society's span | odd, existing | between two | each changing released along, to the self 5 names |
| 10 | **10-next-co-possibling** | next, the society's span | even, possibling | between two | each sharing's changing, + or − is and 0 is not, shared across to another self's 14 |
| 11 | **11-next-co-prioring** | next, the society's span | odd, existing | between two | the next prior: the prior with each changing at its sharing |
| 12 | **12-next-co-still-possibling** | next, the society's span | even, possibling | between two | each sharing's changing, is or is not, the prior and the offerings meeting |
| 13 | **13-next** | next, the society's span | odd, existing | one | each self at the society, and each sharing a changing releases from |
| 14 | **14-next-possibling** | next, the society's span | even, possibling | one | the offerings surfacing at each sharing, same one parity and parting 0; at 17 each self's next offerings |
| 15 | **15-next-prioring** | next, the society's span | odd, existing | one | each parity surfacing, and each parity released |
| 16 | **16-next-still-possibling** | next, the society's span | even, possibling | one | the society: each self with its prior and its offerings |
| 17 | **17-next-now** | next now | odd, existing | one | the society's next momentary, each self's 1-now again |

**Each name is its number and its naming, one hyphenation.** The number says its place and its parity, odd existing and even possibling; *now* says the self's span, 1 to 8, and *next* the society's, 9 to 16, 17-next-now the society's next arriving as each self's 1-now; *co* says a name at a sharing between two, and a name without it is at one. The six names between selves say odd and even by their numbers: 2, 6, 10 and 14, even, across, possibling, the changing shared at 6-now-co-possibling and 10-next-co-possibling another self's possibling at its 2-now-possibling and 14-next-possibling; 9 and 17, odd, along, existing, 9-next-co-changing the next prior released and 17-next-now the next now. Each self's existing is another self's possibling, one changing at a sharing across and no second thing.

**Four momentaries and their gaps.** Each span's names are two momentaries of four, each opening at an odd existing name, a possibling and a prioring inside it, and completing at an even still-possibling name; between each completing and the next opening is a gap, both its sides named, and 17-next-now is the next 1-now.

| Momentary | Opening, odd, existing | Inside, even, possibling | Inside, odd, prioring | Completing, even, still-possibling | Gap |
|---|---|---|---|---|---|
| first | 1-now | 2-now-possibling | 3-now-co-prioring | 4-now-co-still-possibling | 4 )( 5 |
| second | 5-now-co-changing | 6-now-co-possibling | 7-now-prioring | 8-now-still-possibling | 8 )( 9 |
| third | 9-next-co-changing | 10-next-co-possibling | 11-next-co-prioring | 12-next-co-still-possibling | 12 )( 13 |
| fourth | 13-next | 14-next-possibling | 15-next-prioring | 16-next-still-possibling | 16 )( 17 |

**Co, between two or at one.** Each kind of name stands with co at a sharing between two, and without it at one.

| Kind | With co, at a sharing between two | Without co, at one |
|---|---|---|
| prioring | 3-now-co-prioring · 11-next-co-prioring, the prior at its sharings | 7-now-prioring · 15-next-prioring, a parity |
| possibling | 6-now-co-possibling · 10-next-co-possibling, the changing at its sharing side | 2-now-possibling · 14-next-possibling, the changing at its arriving side |
| changing | 5-now-co-changing · 9-next-co-changing, between two | — |
| still-possibling | 4-now-co-still-possibling · 12-next-co-still-possibling, at each sharing | 8-now-still-possibling · 16-next-still-possibling, a self and the society |
| now and next | — | 1-now · 13-next · 17-next-now |

**The joins between selves.** At each join co is the sharing side and its absence the arriving side: a self shares its changing, and nothing of its prior crosses to another self.

| Sharing side, co | Arriving side, one | Between selves |
|---|---|---|
| 6-now-co-possibling | 2-now-possibling | across, even, possibling |
| 10-next-co-possibling | 14-next-possibling | across, even, possibling |
| 9-next-co-changing | 17-next-now | along, odd, existing |

**The four binaries at the lines.** A universe is or is not existing, all, now and same, and at the self's span each binary is one bi-coupling, its *is* at the odd name and its *is not* at the even, the *is not* the other's side of the self's *is*; the binaries are the names' explaining and enter no name.

| Binary | *Is*, odd | At the resolver | *Is not*, even | At the resolver |
|---|---|---|---|---|
| now | 1-now | the self's momentary entered | 2-now-possibling | the offerings arriving, the others' prior |
| existing | 3-now-co-prioring | the prior at its sharings, each with its parity | 4-now-co-still-possibling | each sharing as a place, no parity at it |
| same | 5-now-co-changing | each releasing to the self receiving it at the same sharing | 6-now-co-possibling | the changings shared across, each a prior inverted |
| all | 7-now-prioring | each parity read at every entry | 8-now-still-possibling | each self's own next prior, one beside the others |

**At the society's span the four stand with now and same exchanged**: now between two at 9-next-co-changing and 10-next-co-possibling, one now shared by selves, and same at one at 13-next and 14-next-possibling, each self's sameness its own.

**The now-self at one line.** At 12-next-co-still-possibling the line `if _15_next_prioring != 0 and (_15_next_prioring > 0) == (_7_now_prioring > 0)` reads 14-next-possibling's surfacing, as 15, against 7-now-prioring at each sharing of 3-now-co-prioring: the now-self, now-prioring and next-possibling, at one line, its sign 0, the prior kept, or ±, the prior inverted. Same and not-same are that sign at the two betweens, 12 and 14, and need no name of their own.

**Each name and its relations.**

| n | Relation | For this name |
|---|---|---|
| 1 | Name | **1-now** |
| 1 | Parity, span | odd, existing, the self's span |
| 1 | Sides | self, other, the self opening it |
| 1 | Co-sequencing | the self offering itself to the coupling |
| 1 | 8 up | 9-next-co-changing, its binary at next |
| 1 | 9 less | the podal within 1 to 8, 8-now-still-possibling |
| 1 | 17 less | the podal within 1 to 16, 16-next-still-possibling |
| 1 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 16-next-still-possibling to it and on to 9-next-co-changing, each name one apart from 2-15-7-10 |
| 1 | Six-cycle | 1-9-5-12-8-16 |
| 1 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 1 | Momentaries of exchanging | the first of the self's four, opening at 1, self 1–2 |
| 1 | Five dimensions | 1 self prior, the prior opening of the self's five |
| 1 | Namings | 1-2, bi-momentarying, the self's entry, odd, and the others' offerings, even, one momentary at each side |
| 1 | The self as three | the bi-moral self with 2, bi-momentarying, the offering self to other and other to self, across |
| 1 | Prior and next | once for one self at one momentary, the three steps within it 14, 12, 10 with 11 |
| 1 | 1 to 17s inward and outward | 1–17s inward 1 of the 1st 1–17, the entry, and at the 1–17 outward 1, the entry |
| 2 | Name | **2-now-possibling** |
| 2 | Parity, span | even, possibling, the self's span |
| 2 | Sides | other, self, the other opening it |
| 2 | 8 up | 10-next-co-possibling, its binary at next |
| 2 | 9 less | the podal within 1 to 8, 7-now-prioring |
| 2 | 17 less | the podal within 1 to 16, 15-next-prioring |
| 2 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 10-next-co-possibling to it and on to 15-next-prioring, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 2 | Six-cycle | 2-15-7-11-6-10 |
| 2 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 2 | One move | 2 along 2-15-7-10 |
| 2 | Momentaries of exchanging | the first of the self's four, at 2, the self's 1–2 completing and the other's 2–3 opening |
| 2 | Five dimensions | 2 other prior, the prior completing of the self's five and the prior opening of the other's |
| 2 | Namings | 1-2, bi-momentarying |
| 2 | The self as three | the bi-moral self with 1, across |
| 2 | Bi-coupling | at the between, each other's across sharing, offered to the self |
| 2 | Parity's unit square | a dot of the unit square, its diagonal with 14, the offerings at 2 and 14, its edge with 6 the sharing 6 to 2 |
| 2 | Prior and next | the others' sharings across at 6 and 10 and releasings along at 9 of their prior momentary, arriving now, the possible, even, none of their prior crossing; at a spiral each is a releasing along |
| 2 | 1 to 17s inward and outward | 1–17s inward 9 of the 1st, along, odd, next, and at the 1–17 outward within 1 to 2 |
| 3 | Name | **3-now-co-prioring** |
| 3 | Parity, span | odd, existing, the self's span |
| 3 | Sides | self, other, the self opening it |
| 3 | Co-sequencing | at the between, before 10, at competency's parity, odd |
| 3 | 8 up | 11-next-co-prioring, its binary at next |
| 3 | 9 less | the podal within 1 to 8, 6-now-co-possibling |
| 3 | 17 less | the podal within 1 to 16, 14-next-possibling |
| 3 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 14-next-possibling to it and on to 11-next-co-prioring, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 3 | Six-cycle | 3-11-7-10-6-14 |
| 3 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 3 | Momentaries of exchanging | the first of the self's four completing at 3, the other's 2–3, and the second opening at 3, self 3–4 |
| 3 | Five dimensions | 3 co-momentarying now, the now opening of the self's five |
| 3 | Namings | 3-4, co-intelligencing, at each sharing 4 the prior at 3 coupling with the offerings surfaced at 14, next discovered, at 11 |
| 3 | The self as three | the invisible intelligencing method, the rotation 3, 6, 5, 4, out at 3 |
| 3 | Prior and next | the prior, the self's own, each sharing with its parity, the next momentary's continuing of 11 |
| 3 | 1 to 17s inward and outward | 1–17s inward 17 of the 1st and 1 of the 2nd, along, odd, now, and at the 1–17 outward within 1 to 2 |
| 4 | Name | **4-now-co-still-possibling** |
| 4 | Parity, span | even, possibling, the self's span |
| 4 | Sides | other, self, the other opening it |
| 4 | Co-sequencing | at the between, before 10, at morality's parity, even |
| 4 | 8 up | 12-next-co-still-possibling, its binary at next |
| 4 | 9 less | the podal within 1 to 8, 5-now-co-changing |
| 4 | 17 less | the podal within 1 to 16, 13-next |
| 4 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 12-next-co-still-possibling to it and on to 13-next, each name one apart from 3-11-6-14 |
| 4 | Six-cycle | 4-13-5-9-8-12 |
| 4 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 4 | One move | 4 along 4-13-5-12 |
| 4 | Momentaries of exchanging | the second of the self's four, at 4, the self's 3–4 completing and the other's 4–5 opening |
| 4 | Five dimensions | 4 bi-momentarying now, the now completing of the self's five |
| 4 | Namings | 3-4, co-intelligencing |
| 4 | The self as three | the invisible intelligencing method, the rotation 3, 6, 5, 4, in at 4, into the self's own corus at 4 |
| 4 | Bi-coupling | at the between, the whole ordering between self and other |
| 4 | Prior and next | now, each sharing at which the prior couples with the now |
| 4 | 1 to 17s inward and outward | 1–17s inward 9 of the 2nd, along, odd, next, and at the 1–17 outward within 1 to 2 |
| 5 | Name | **5-now-co-changing** |
| 5 | Parity, span | odd, existing, the self's span |
| 5 | Sides | self, other, the self opening it |
| 5 | Co-sequencing | at the between, before 10, at competency's parity, odd |
| 5 | 8 up | 13-next, its binary at next |
| 5 | 9 less | the podal within 1 to 8, 4-now-co-still-possibling |
| 5 | 17 less | the podal within 1 to 16, 12-next-co-still-possibling |
| 5 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 13-next to it and on to 12-next-co-still-possibling, each name one apart from 3-11-6-14 |
| 5 | Middle four-cycle | 9-5-12-8 |
| 5 | Six-cycle | 1-9-5-12-8-16 |
| 5 | Six-cycle | 4-13-5-9-8-12 |
| 5 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 5 | Momentaries of exchanging | the second of the self's four completing at 5, the other's 4–5, and the third opening at 5, self 5–6 |
| 5 | Five dimensions | 5 self next, the next opening of the self's five |
| 5 | Namings | 5, co-competencing, the releasings, owned by neither, each release to its receiving sharing |
| 5 | The self as three | the invisible intelligencing method, the rotation 3, 6, 5, 4, out at 5 |
| 5 | Prior and next | next, each release to its receiving sharing |
| 5 | 1 to 17s inward and outward | 1–17s inward 17 of the 2nd and 1 of the 3rd, along, odd, now, and at the 1–17 outward within 1 to 2 |
| 6 | Name | **6-now-co-possibling** |
| 6 | Parity, span | even, possibling, the self's span |
| 6 | Sides | other, self, the other opening it |
| 6 | 8 up | 14-next-possibling, its binary at next |
| 6 | 9 less | the podal within 1 to 8, 3-now-co-prioring |
| 6 | 17 less | the podal within 1 to 16, 11-next-co-prioring |
| 6 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 11-next-co-prioring to it and on to 14-next-possibling, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 6 | Middle four-cycle | 7-11-6-10 |
| 6 | Six-cycle | 2-15-7-11-6-10 |
| 6 | Six-cycle | 3-11-7-10-6-14 |
| 6 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 6 | One move | 6 along 3-11-6-14 |
| 6 | Momentaries of exchanging | the third of the self's four, at 6, the self's 5–6 completing and the other's 6–7 opening |
| 6 | Namings | 6, bi-moralizing, each changing shared across, to the other's 2 |
| 6 | The self as three | the invisible intelligencing method, the rotation 3, 6, 5, 4, in at 6 |
| 6 | Bi-coupling | at the between, the other's changing to the self, shared across |
| 6 | Parity's unit square | a dot of the unit square, its diagonal with 10, the sharings at 6 and 10, its edge with 2 the sharing 6 to 2 |
| 6 | Prior and next | the changing shared, the other's next offering at its 2 |
| 6 | 1 to 17s inward and outward | 1–17s inward 9 of the 3rd, along, odd, next, and at the 1–17 outward within 1 to 2 |
| 7 | Name | **7-now-prioring** |
| 7 | Parity, span | odd, existing, the self's span |
| 7 | Sides | self, other, the self opening it |
| 7 | Co-sequencing | at the between, before 10, at competency's parity, odd |
| 7 | 8 up | 15-next-prioring, its binary at next |
| 7 | 9 less | the podal within 1 to 8, 2-now-possibling |
| 7 | 17 less | the podal within 1 to 16, 10-next-co-possibling |
| 7 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 15-next-prioring to it and on to 10-next-co-possibling, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 7 | Middle four-cycle | 7-11-6-10 |
| 7 | Six-cycle | 2-15-7-11-6-10 |
| 7 | Six-cycle | 3-11-7-10-6-14 |
| 7 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 7 | Momentaries of exchanging | the third of the self's four completing at 7, the other's 6–7, and the fourth opening at 7, self 7–8 |
| 7 | The self as three | the co-competent self with 8, along |
| 7 | Prior and next | each parity, offered now and prior, the co-linear recursioning forward along arriving, up the numbers, prior into now, at the self's completing |
| 7 | 1 to 17s inward and outward | 1–17s inward 17 of the 3rd and 1 of the 4th, along, odd, now, and at the 1–17 outward within 1 to 2 |
| 8 | Name | **8-now-still-possibling** |
| 8 | Parity, span | even, possibling, the self's span |
| 8 | Sides | other, self, the other opening it |
| 8 | Co-sequencing | at the between, before 10, at morality's parity, even |
| 8 | 8 up | 16-next-still-possibling, its binary at next |
| 8 | 9 less | the podal within 1 to 8, 1-now |
| 8 | 17 less | the podal within 1 to 16, 9-next-co-changing |
| 8 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 9-next-co-changing to it and on to 16-next-still-possibling, each name one apart from 2-15-7-10 |
| 8 | Middle four-cycle | 9-5-12-8 |
| 8 | Six-cycle | 1-9-5-12-8-16 |
| 8 | Six-cycle | 4-13-5-9-8-12 |
| 8 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 8 | One move | 8 along 1-9-8-16 |
| 8 | Momentaries of exchanging | the fourth of the self's four, at 8, the self's 7–8 completing and the other's 8–9 opening |
| 8 | The self as three | the co-competent self with 7, along |
| 8 | Bi-coupling | at the between, the prior at its sharing again |
| 8 | Prior and next | each self's next prior, at 11 this momentary and the next momentary's 3; the even names of the self's span, 2, 4, 6 and 8, completing at 8 |
| 8 | 1 to 17s inward and outward | 1–17s inward 9 of the 4th, along, odd, next, and at the 1–17 outward within 1 to 2 |
| 9 | Name | **9-next-co-changing** |
| 9 | Parity, span | odd, existing, the society's span |
| 9 | Sides | social, other, self, the society opening it |
| 9 | 8 up | 17-next-now, its binary at next |
| 9 | 8 down | 1-now |
| 9 | 17 less | the podal within 1 to 16, 8-now-still-possibling |
| 9 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 1-now to it and on to 8-now-still-possibling, each name one apart from 2-15-7-10 |
| 9 | Middle four-cycle | 9-5-12-8 |
| 9 | Six-cycle | 1-9-5-12-8-16 |
| 9 | Six-cycle | 4-13-5-9-8-12 |
| 9 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 9 | Momentaries of exchanging | the fourth of the self's four completing at 9, the other's 8–9, and the first of the society's four, 9 to 11, opening at 9 |
| 9 | Parity's square and triangles | a unit triangle, along, 9 to 17 and 17 to 9 |
| 9 | Prior and next | the next prior, odd, existing, each changing of 10 released along into the next momentary, to each receiving sharing, the self's own next |
| 9 | 1 to 17s inward and outward | 1–17s inward 17 of the 4th and 1 of the 5th, along, odd, now, and at the 1–17 outward 2, across, even |
| 10 | Name | **10-next-co-possibling** |
| 10 | Parity, span | even, possibling, the society's span |
| 10 | Sides | other, social, self, the other opening it |
| 10 | 8 down | 2-now-possibling |
| 10 | 17 less | the podal within 1 to 16, 7-now-prioring |
| 10 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 7-now-prioring to it and on to 2-now-possibling, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 10 | Middle four-cycle | 7-11-6-10 |
| 10 | Six-cycle | 2-15-7-11-6-10 |
| 10 | Six-cycle | 3-11-7-10-6-14 |
| 10 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 10 | Momentaries of exchanging | the first of the society's four, at 10, 9–10 completing and 10–11 opening |
| 10 | Bi-coupling | 8 up, the self among the selves of its society |
| 10 | Parity's unit square | a dot of the unit square, its diagonal with 6, the sharings at 6 and 10, its edge with 14 the sharing 10 to 14 |
| 10 | Prior and next | the changing shared across now, the other's offering next, the possible |
| 10 | 1 to 17s inward and outward | 1–17s inward 9 of the 5th, along, odd, next, and at the 1–17 outward within 2 to 3 |
| 11 | Name | **11-next-co-prioring** |
| 11 | Parity, span | odd, existing, the society's span |
| 11 | Sides | social, other, self, the society opening it |
| 11 | Co-sequencing | after 10, 8 up from 3-now-co-prioring, at competency's parity, odd |
| 11 | 8 down | 3-now-co-prioring |
| 11 | 17 less | the podal within 1 to 16, 6-now-co-possibling |
| 11 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 3-now-co-prioring to it and on to 6-now-co-possibling, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 11 | Middle four-cycle | 7-11-6-10 |
| 11 | Six-cycle | 2-15-7-11-6-10 |
| 11 | Six-cycle | 3-11-7-10-6-14 |
| 11 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 11 | Momentaries of exchanging | the first of the society's four, 9 to 11, completing at 11, and the second, 11 to 13, opening at 11 |
| 11 | Prior and next | the next prior, the next prior, odd, existing, continuing as 3 at the next momentary, the self's own |
| 11 | 1 to 17s inward and outward | 1–17s inward 17 of the 5th and 1 of the 6th, along, odd, now, and at the 1–17 outward within 2 to 3 |
| 12 | Name | **12-next-co-still-possibling** |
| 12 | Parity, span | even, possibling, the society's span |
| 12 | Sides | other, social, self, the other opening it |
| 12 | Co-sequencing | after 10, 8 up from 4-now-co-still-possibling, at morality's parity, even |
| 12 | 8 down | 4-now-co-still-possibling |
| 12 | 17 less | the podal within 1 to 16, 5-now-co-changing |
| 12 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 5-now-co-changing to it and on to 4-now-co-still-possibling, each name one apart from 3-11-6-14 |
| 12 | Middle four-cycle | 9-5-12-8 |
| 12 | Six-cycle | 1-9-5-12-8-16 |
| 12 | Six-cycle | 4-13-5-9-8-12 |
| 12 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 12 | Momentaries of exchanging | the second of the society's four, at 12, 11–12 completing and 12–13 opening |
| 12 | Namings | entraining, the prior arriving into now along the unrelationing path at the between, the shape of the unrelationing surface, each sharing's changing, is or is not |
| 12 | Bi-coupling | 8 up, changing at bi-coupling, the self in society |
| 12 | Prior and next | now, the changing, is or is not, prior and now coupled |
| 12 | 1 to 17s inward and outward | 1–17s inward 9 of the 6th, along, odd, next, and at the 1–17 outward within 2 to 3 |
| 13 | Name | **13-next** |
| 13 | Parity, span | odd, existing, the society's span |
| 13 | Sides | social, other, the society opening it |
| 13 | Co-sequencing | after 10, 8 up from 5-now-co-changing, at competency's parity, odd |
| 13 | 8 down | 5-now-co-changing |
| 13 | 17 less | the podal within 1 to 16, 4-now-co-still-possibling |
| 13 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-still-possibling, from 4-now-co-still-possibling to it and on to 5-now-co-changing, each name one apart from 3-11-6-14 |
| 13 | Six-cycle | 4-13-5-9-8-12 |
| 13 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 13 | Momentaries of exchanging | the second of the society's four, 11 to 13, completing at 13, and the third, 13 to 15, opening at 13 |
| 13 | Prior and next | each releasing sharing, and at the society each releasing self |
| 13 | 1 to 17s inward and outward | 1–17s inward 17 of the 6th and 1 of the 7th, along, odd, now, and at the 1–17 outward within 2 to 3 |
| 14 | Name | **14-next-possibling** |
| 14 | Parity, span | even, possibling, the society's span |
| 14 | Sides | other, social, the other opening it |
| 14 | 8 down | 6-now-co-possibling |
| 14 | 17 less | the podal within 1 to 16, 3-now-co-prioring |
| 14 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-prioring, from 6-now-co-possibling to it and on to 3-now-co-prioring, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 14 | Six-cycle | 3-11-7-10-6-14 |
| 14 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 14 | Momentaries of exchanging | the third of the society's four, at 14, 13–14 completing and 14–15 opening |
| 14 | Bi-coupling | 8 up, the offerings surfacing, each as it arrived, morality; the self's own inverting at 12 |
| 14 | Parity's unit square | a dot of the unit square, its diagonal with 2, the offerings at 2 and 14, its edge with 10 the sharing 10 to 14 |
| 14 | Prior and next | now, the offerings surfacing, the others' prior momentary arrived at the self's now, even, the others' possibling at the self until at 11 |
| 14 | 1 to 17s inward and outward | 1–17s inward 9 of the 7th, along, odd, next, and at the 1–17 outward within 2 to 3 |
| 15 | Name | **15-next-prioring** |
| 15 | Parity, span | odd, existing, the society's span |
| 15 | Sides | social, other, the society opening it |
| 15 | Co-sequencing | after 10, 8 up from 7-now-prioring, at competency's parity, odd |
| 15 | 8 down | 7-now-prioring |
| 15 | 17 less | the podal within 1 to 16, 2-now-possibling |
| 15 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 2-now-possibling to it and on to 7-now-prioring, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 15 | Six-cycle | 2-15-7-11-6-10 |
| 15 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 15 | Momentaries of exchanging | the third of the society's four, 13 to 15, completing at 15, and the fourth, 15 to 17, opening at 15 |
| 15 | Prior and next | the parity released along at 9, the next prior, the co-linear recursioning forward along leaving, up the numbers, now into next, at the society's completing, the prior parity at 7 inverted, 0, or at no prior the parity surfaced at 14 |
| 15 | 1 to 17s inward and outward | 1–17s inward 17 of the 7th and 1 of the 8th, along, odd, now, and at the 1–17 outward within 2 to 3 |
| 16 | Name | **16-next-still-possibling** |
| 16 | Parity, span | even, possibling, the society's span |
| 16 | Sides | other, social, the other opening it |
| 16 | Co-sequencing | after 10, 8 up from 8-now-still-possibling, at morality's parity, even |
| 16 | 8 down | 8-now-still-possibling |
| 16 | 17 less | the podal within 1 to 16, 1-now |
| 16 | Four-cycle | 1-9-8-16, going 8 up first from 1-now, from 8-now-still-possibling to it and on to 1-now, each name one apart from 2-15-7-10 |
| 16 | Six-cycle | 1-9-5-12-8-16 |
| 16 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 16 | Momentaries of exchanging | the fourth of the society's four, at 16, 15–16 completing and 16–17 opening |
| 16 | Bi-coupling | 8 up, competency asymmetry sustaining the coupling, the society winding to the self again |
| 16 | Prior and next | the society now, each self's 8 and its offerings next; the even names of the society's span, 10, 12, 14 and 16, completing at 16 |
| 16 | 1 to 17s inward and outward | 1–17s inward 9 of the 8th, along, odd, next, and at the 1–17 outward within 2 to 3 |
| 17 | Name | **17-next-now** |
| 17 | Parity, span | odd, existing, the next now |
| 17 | Sides | social, self, the society opening it |
| 17 | 8 down | 9-next-co-changing |
| 17 | Momentaries of exchanging | the fourth of the society's four, 15 to 17, completing at 17, the next 1 |
| 17 | Parity's square and triangles | a unit triangle, along, 17 to 9 and 9 to 17 |
| 17 | Prior and next | the society's next momentary, the next now, each self's 1 then 9 at 6, 10 and 9 |
| 17 | 1 to 17s inward and outward | 1–17s inward 17 of the 8th and 1 of the 9th, along, odd, now, and at the 1–17 outward 3, odd, now |

**The odd names, now and 8 up at next.** Each odd name of the self's span is the same at next, 8 up: the prior received and the next prior, the receiving and the releasing, the parity read and the parity surfaced.

| Now | Received | Next, 8 up | Given on |
|---|---|---|---|
| 1-now | the resolver entered | 9-next-co-changing | the resolver going on, each changing released along |
| 3-now-co-prioring | the prior at its sharings | 11-next-co-prioring | the next prior |
| 5-now-co-changing | the receiving sharing | 13-next | the releasing sharing, each self at the society |
| 7-now-prioring | the parity read | 15-next-prioring | the parity surfaced and released |

**Namings among the names.**

| Names | Naming | Resolved as |
|---|---|---|
| 1-now · 2-now-possibling | bi-momentarying | the self's entry, odd, and the others' offerings, even, one momentary at each side |
| 3-now-co-prioring · 4-now-co-still-possibling | co-intelligencing | at each sharing 4 the prior at 3 couples with the offerings surfaced at 14: next discovered, at 11 |
| 5-now-co-changing | co-competencing | the releasings, owned by neither: each release to its receiving sharing |
| 1 · 2 · 3 · 4 · 5, each alone | the five dimensions | 1 self prior, the self, its prior at 3, a formed set; 2 other prior, the other selves' offerings of their prior momentary arriving, shared at 6 and 10 and released along at 9; 3 co-momentarying now, the same prior at now, and 4 bi-momentarying now, each sharing, the offerings surfaced at 14 arriving at it, now; 5 self next, each release to its receiving sharing next |
| 6-now-co-possibling | bi-moralizing | each changing shared across, to the other's 2 |
| 12-next-co-still-possibling | entraining, the shape of the unrelationing surface | the prior arriving into now along the unrelationing path at the between, prior and now coupled at each sharing, a parity changing alone crossing it, 0 at a match; at the other parity, 0 or none, the prior parity inverted at 11; at no prior, the parity surfaced at 14; its changing shared at 10, the others' offering next |
| 1 to 9 | bi-coupling | the entry, 1, at the names 1, 2, 3, 4, 7, 10, 11, 12, 14 and 15, the self and the other at one coupling; 1 to 9 the bi-coupling among the names, 9 at its end is 9-next-co-changing, each changing of 10 released along, one name at the resolver and in the explaining |
| 1 to 17 | bi-trupling | the society's entry, 17, at the names of 1 to 9 with 5, 6, 8, 9, 13, 16 and 17, the self, the other and the society; 9 at its waist, 9-next-co-changing, along, 9 to 17 and 17 to 9; its two sides, the odd along at 9 and 17, existing, and the even across at 6 to 2 and 10 to 14, possibling |
| 1 to 17, stable-forming | bi-tri-volutioning | at no one line: each momentary's next prior, at 11, the next momentary's prior, at 3 |
| 2 · 6 · 14 · 10 · 9 · 17 | parity's square and triangles | a unit square of four dots, 2, 6, 14 and 10, its empty centre the between: its two across edges the sharings, 6 to 2 and 10 to 14, and its two edges 8 apart, 2 with 10 and 6 with 14, two pairs of parallels; round it 2, 10, 14, 6; its diagonals the offerings at 2 and 14, and the sharings at 6 and 10; and two unit triangles, 9 and 17, along, 9 to 17 and 17 to 9 |

**0, the between.**

| The between, 0 | Names |
|---|---|
| the one between, three names | 12-next-co-still-possibling, prior and now agreeing, the between of momentaries at each sharing; 15-next-prioring, the between released along, the parity 10 shared, and at a sharing opening the parity surfaced at 14, the resolver's 0 at none and at parting alike; 16-next-still-possibling, the between at the society, arriving at the next momentary's 2 |
| arriving and passing over | 7-now-prioring, an offered 0 the parity at 2, surfacing none at 14, and a 0 at 10 the prior kept at 11 |
| the four across names, the unit square's four dots: shared across | 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling, 14-next-possibling, parity's unit square, its empty centre the between; each parity and each 0 shared across, the 0 passing over at the receiving self's 14 |
| none | 1-now, the entry; 3-now-co-prioring, 8-now-still-possibling and 11-next-co-prioring, the prior, a sharing at a prior never none again; 4-now-co-still-possibling, the sharings, and 5-now-co-changing and 13-next, the sharings and, at the society, the releasings and the selves |
| the two along names: released along | 9-next-co-changing and 17-next-now, each parity and each 0 released along, the 0 passing over at the receiving self's 14, as across |

**Four four-cycles.**

| Four-cycle: each move 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n) | Its two pairs 8 apart | Names between selves on it | Beside the other four-cycles |
|---|---|---|---|
| 1-9-8-16 | 1 · 9 and 8 · 16 | 9 | each name one apart from 2-15-7-10 |
| 2-15-7-10 | 2 · 10 and 7 · 15 | 2 and 10 | each name one apart from 1-9-8-16 and 3-11-6-14 |
| 3-11-6-14 | 3 · 11 and 6 · 14 | 6 and 14 | each name one apart from 4-13-5-12 and 2-15-7-10 |
| 4-13-5-12 | 4 · 12 and 5 · 13 | none | each name one apart from 3-11-6-14 |

**Each name, three scales.**

| n | Name | This scale, 1 to 17 | The next scale inward, eight 1 to 17s: n is 8n − 7 | The next scale outward: 8m − 7 is m |
|---|---|---|---|---|
| 1 | 1-now | odd, now | 1 of the 1st: odd, now | 1: odd, now |
| 2 | 2-now-possibling | across, even | 9 of the 1st: along, odd, next | within 1 to 2 |
| 3 | 3-now-co-prioring | odd, now | 17 of the 1st, 1 of the 2nd: along, odd, now | within 1 to 2 |
| 4 | 4-now-co-still-possibling | even | 9 of the 2nd: along, odd, next | within 1 to 2 |
| 5 | 5-now-co-changing | odd, now | 17 of the 2nd, 1 of the 3rd: along, odd, now | within 1 to 2 |
| 6 | 6-now-co-possibling | across, even | 9 of the 3rd: along, odd, next | within 1 to 2 |
| 7 | 7-now-prioring | odd, now | 17 of the 3rd, 1 of the 4th: along, odd, now | within 1 to 2 |
| 8 | 8-now-still-possibling | even | 9 of the 4th: along, odd, next | within 1 to 2 |
| 9 | 9-next-co-changing | along, odd, next | 17 of the 4th, 1 of the 5th: along, odd, now | 2: across, even |
| 10 | 10-next-co-possibling | across, even | 9 of the 5th: along, odd, next | within 2 to 3 |
| 11 | 11-next-co-prioring | odd, next | 17 of the 5th, 1 of the 6th: along, odd, now | within 2 to 3 |
| 12 | 12-next-co-still-possibling | even | 9 of the 6th: along, odd, next | within 2 to 3 |
| 13 | 13-next | odd, next | 17 of the 6th, 1 of the 7th: along, odd, now | within 2 to 3 |
| 14 | 14-next-possibling | across, even | 9 of the 7th: along, odd, next | within 2 to 3 |
| 15 | 15-next-prioring | odd, next | 17 of the 7th, 1 of the 8th: along, odd, now | within 2 to 3 |
| 16 | 16-next-still-possibling | even | 9 of the 8th: along, odd, next | within 2 to 3 |
| 17 | 17-next-now | along, odd, now | 17 of the 8th, 1 of the 9th: along, odd, now | 3: odd, now |

**Eight 1 to 17s inward.**

| 1 to 17 inward | Spans, this scale | Its 9, this scale | Its 17, this scale | Momentary of exchanging |
|---|---|---|---|---|
| 1st | 1 to 3 | 2 | 3 | the self, 1st of four |
| 2nd | 3 to 5 | 4 | 5 | the self, 2nd of four |
| 3rd | 5 to 7 | 6 | 7 | the self, 3rd of four |
| 4th | 7 to 9 | 8 | 9 | the self, 4th of four |
| 5th | 9 to 11 | 10 | 11 | the society, 1st of four |
| 6th | 11 to 13 | 12 | 13 | the society, 2nd of four |
| 7th | 13 to 15 | 14 | 15 | the society, 3rd of four |
| 8th | 15 to 17 | 16 | 17 | the society, 4th of four |

**Fives.**

| Side | Prior opening | Prior completing | Now opening | Now completing | Next opening |
|---|---|---|---|---|---|
| self, at 1 | 1 | 2 | 3 | 4 | 5 |
| other, at 2 | 2 | 3 | 4 | 5 | 6 |
| self next, at 3 | 3 | 4 | 5 | 6 | 7 |

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

**One self, one momentary.**

| The prior (3), one sharing. Each cell: shared (10) · the next prior (11). *is*: a changing that is, the parity shared; *is not*: a changing that is not, 0 shared, the prior kept | Surfacing (14): none | Surfacing (14): + | Surfacing (14): − | Surfacing (14): + and − together |
|---|---|---|---|---|
| + | is − · − | is not · + | is − · − | is − · − |
| − | is + · + | is + · + | is not · − | is + · + |

**Eight even names, 8 apart.**

| Name at the between | Bi-coupling at the between | Name 8 up | Bi-coupling 8 up |
|---|---|---|---|
| 2-now-possibling | each other's across sharing, offered to the self | 10-next-co-possibling | the self among the selves of its society |
| 4-now-co-still-possibling | the whole ordering between self and other | 12-next-co-still-possibling | changing at bi-coupling, the self in society |
| 6-now-co-possibling | the other's changing to the self, shared across | 14-next-possibling | the offerings surfacing, each as it arrived, morality; the self's own inverting at 12 |
| 8-now-still-possibling | the prior at its sharing again | 16-next-still-possibling | the society, each self with its prior and offerings, the society at the self again |

**One move, 1 to 8.** 8 up keeps each name's kind but at 1 and 5, at which now and changing exchange, and exchanges co at 1, 2, 5 and 6; each podal turns now to next at 17 less and possibling to prioring inside each momentary, and the eight ends are their own set at both podals.

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

**Twelve forms.**

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

**The eights.** Every eight here is the one eight, the four binaries each twice, met at a face, and 8 up is each name's binary at next.

| The eight | Each of the four, twice, at |
|---|---|
| the self's span, 1 to 8 | two names each, at now |
| the eight-cycle 1-9-5-13-4-12-8-16 | its end, at now and at next: the eight ends of the four momentaries |
| the eight-cycle 2-15-7-11-3-14-6-10 | its inside, at now and at next: the eight insides |
| the eight even names | its even, at now and at next, the eight 9s of the eight 1 to 17s inward |
| the eight odd names | its odd, at now and at next |

**One self, momentary by momentary.**

| One sharing; the self's prior − (3) first. Offered each momentary | Shared (10) | The next prior (11) |
|---|---|---|
| none at each momentary | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| − at each momentary | 0, 0, 0, 0, 0, 0, 0, 0 | −, −, −, −, −, −, −, − |
| +, −, +, − alternating | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| + and − together at each momentary | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |

**A spiral of selves.**

| Number of selves. Each releases along (9) to the next, the last to the first. One sharing. First momentary: self 1 at prior −, the selves alternate along, and with an odd number the last and the first are alike. None offered from beyond the spiral | Self 1, each changing of 10 released along (9), momentaries 1 to 12 | Momentaries to each self's releasings again |
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

**Two spirals beside each other, and crossed.**

| Selves in each of two spirals, each opened as the spiral of selves | Beside each other: momentaries to each self's releasings again together | Crossed, self 1 of each spiral sharing across (10) to self 1 of the other: momentaries to each self's releasings again | Crossed: releasings again from this momentary on | Crossed: self 1 of each, alike or opposite in parity | Each spiral's like pair in the first momentary, the last and the first |
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

| Torus of selves, p along · q across. Each releases along (9) to the next along and shares across (10) to the next across, the last to the first. One sharing. First momentary: one self at prior −, the selves alternate along and across, and with an odd number the last and the first are alike. None offered from beyond the torus. Both numbers odd, p the smaller: q at a q more than twice p, and 4p at each other q; either number even: 2 | Momentaries to each self's releasings and sharings again | Again from this momentary on | Spirals of p and q beside each other: momentaries to each self's releasings again together |
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

**Two selves.**

| A, B at their prior (3) in the first momentary. One sharing, none offered from beyond the two | Receiving the other's sharing or releasing | A shared (10), six momentaries | B shared (10), six momentaries |
|---|---|---|---|
| +, + | both ways | −, 0, +, 0, −, 0 | −, 0, +, 0, −, 0 |
| +, + | A from B alone | −, 0, +, −, +, − | −, +, −, +, −, + |
| +, + | B from A alone | −, +, −, +, −, + | −, 0, +, −, +, − |
| +, + | neither | −, +, −, +, −, + | −, +, −, +, −, + |
| +, − | both ways | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | A from B alone | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | B from A alone | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | neither | −, +, −, +, −, + | +, −, +, −, +, − |

**Two selves, three momentaries, five parities.**

| The other's prior (3), along | The other's shared (10), across | The self's prior, now (3), along | The self's shared (10), across | The self's next prior (11), along. Two selves coupled both ways, across or along, each self at a prior parity, none offered from beyond the two, each opening, each momentary: six forms, four at an alike opening and two at an opposite, each momentary from the second |
|---|---|---|---|---|
| + | − | − | 0 | − |
| + | − | + | − | − |
| + | 0 | + | − | − |
| − | + | + | 0 | + |
| − | + | − | + | + |
| − | 0 | − | + | + |

**Three selves in a line.**

| A's parity, offered to B in the first momentary alone. One sharing; B and C each at prior +; B releases along to C | B, each changing (10) | B's next prior (11), first momentary | C, each changing (10), momentaries 1 and 2 | C's next prior (11), second momentary |
|---|---|---|---|---|
| + | 0 | + | −, + | + |
| − | − | − | −, 0 | − |

**A spiral opened at no prior, one parity offered once.**

Each cell shows the selves in their coupling order; · is no prior.

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

Selves coupled along, the last to the first, each opened at no prior, and + offered once at the first self at the first momentary: the first self's sharing opens at that one parity, at the bi-coupling, the one place a self's forming takes a parity not its own, and from then it is the self's own; each next self's sharing opens as the parity arrives along one momentary on, and after n momentaries each self is at a prior, the spiral at its one like pair, the alternating pattern of an odd spiral from the first momentary at which every self is at a prior. A self at a sharing is at its prior at each momentary from its opening, its next from its own prior kept or inverted; a thing at no prior at every momentary is no self.

**At no prior, one momentary.**

| The prior (3): none, one sharing. Each cell: shared (10) · the next prior (11). *is*: a changing that is, the parity shared; *is not*: a changing that is not, 0 shared, no next prior; *none*: none shared | Surfacing (14): none | Surfacing (14): + | Surfacing (14): − | Surfacing (14): + and − together |
|---|---|---|---|---|
| none | none · none | is + · + | is − · − | is not · none |
