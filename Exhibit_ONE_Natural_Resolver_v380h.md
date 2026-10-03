Exhibit ONE Natural Resolver v380h

# Natural Resolver

**Stable Forms of the Discovering Method**

---

```python
"""Exhibit ONE · Natural Resolver"""


def _1_co_bi_tri_offering(_3_co_bi_co_sharing, _2_bi_co_bi_offering):
    _14_bi_tri_bi_moralizing = {}
    for _4_bi_co_bi_sharing, _7_co_bi_co_corusing in _2_bi_co_bi_offering:
        if _7_co_bi_co_corusing != 0:
            _15_tri_bi_tri_corusing = _14_bi_tri_bi_moralizing.get(_4_bi_co_bi_sharing)
            if _15_tri_bi_tri_corusing is None:
                _14_bi_tri_bi_moralizing[_4_bi_co_bi_sharing] = 1 if _7_co_bi_co_corusing > 0 else -1
            elif (_15_tri_bi_tri_corusing > 0) != (_7_co_bi_co_corusing > 0):
                _14_bi_tri_bi_moralizing[_4_bi_co_bi_sharing] = 0
    _12_bi_tri_bi_entraining = dict(_14_bi_tri_bi_moralizing)
    for _4_bi_co_bi_sharing, _7_co_bi_co_corusing in _3_co_bi_co_sharing:
        _15_tri_bi_tri_corusing = _14_bi_tri_bi_moralizing.get(_4_bi_co_bi_sharing, 0)
        if _15_tri_bi_tri_corusing != 0 and (_15_tri_bi_tri_corusing > 0) == (_7_co_bi_co_corusing > 0):
            _12_bi_tri_bi_entraining[_4_bi_co_bi_sharing] = 0
        else:
            _12_bi_tri_bi_entraining[_4_bi_co_bi_sharing] = -1 if _7_co_bi_co_corusing > 0 else 1
    _10_bi_tri_bi_tunneling = list(_12_bi_tri_bi_entraining.items())
    _11_tri_bi_tri_chaining = dict(_3_co_bi_co_sharing)
    for _4_bi_co_bi_sharing, _7_co_bi_co_corusing in _10_bi_tri_bi_tunneling:
        if _7_co_bi_co_corusing != 0:
            _11_tri_bi_tri_chaining[_4_bi_co_bi_sharing] = _7_co_bi_co_corusing
    return _10_bi_tri_bi_tunneling, list(_11_tri_bi_tri_chaining.items())


def _9_tri_bi_co_momentarying(_10_bi_tri_bi_tunneling, _5_co_bi_co_competencing):
    return [(_5_co_bi_co_competencing[_13_tri_bi_tri_competencing], _15_tri_bi_tri_corusing)
            for _13_tri_bi_tri_competencing, _15_tri_bi_tri_corusing in _10_bi_tri_bi_tunneling]


def _17_co_bi_tri_offering(_16_bi_tri_bi_torusing, _5_co_bi_co_competencing):
    _8_bi_co_bi_torusing = {}
    _14_bi_tri_bi_moralizing = {_13_tri_bi_tri_competencing: [] for _13_tri_bi_tri_competencing in _16_bi_tri_bi_torusing}
    for _13_tri_bi_tri_competencing, (_3_co_bi_co_sharing, _2_bi_co_bi_offering) in _16_bi_tri_bi_torusing.items():
        _10_bi_tri_bi_tunneling, _8_bi_co_bi_torusing[_13_tri_bi_tri_competencing] = _1_co_bi_tri_offering(
            _3_co_bi_co_sharing, _2_bi_co_bi_offering)
        _6_bi_co_bi_moralizing = _10_bi_tri_bi_tunneling
        for _4_bi_co_bi_sharing, _15_tri_bi_tri_corusing in _9_tri_bi_co_momentarying(
                [(_4_bi_co_bi_sharing, _15_tri_bi_tri_corusing)
                 for _4_bi_co_bi_sharing, _15_tri_bi_tri_corusing in (
                     ((_13_tri_bi_tri_competencing, 6), _6_bi_co_bi_moralizing),
                     ((_13_tri_bi_tri_competencing, 10), _10_bi_tri_bi_tunneling),
                     ((_13_tri_bi_tri_competencing, 9), _10_bi_tri_bi_tunneling))
                 if _4_bi_co_bi_sharing in _5_co_bi_co_competencing],
                _5_co_bi_co_competencing):
            _14_bi_tri_bi_moralizing[_4_bi_co_bi_sharing].extend(_15_tri_bi_tri_corusing)
    return {_13_tri_bi_tri_competencing: (_8_bi_co_bi_torusing[_13_tri_bi_tri_competencing],
                                           _14_bi_tri_bi_moralizing[_13_tri_bi_tri_competencing])
            for _13_tri_bi_tri_competencing in _16_bi_tri_bi_torusing}

CONNECTORS = {
    2: ('2-bi-co-bi-offering', 'bi-moral-so-far', 'arriving'),
    6: ('6-bi-co-bi-moralizing', 'not-yet-bi-moral', 'releasing'),
    9: ('9-tri-bi-co-momentarying', 'not-yet-co-competent', 'along'),
    10: ('10-bi-tri-bi-tunneling', 'not-yet-bi-moral', 'releasing'),
    14: ('14-bi-tri-bi-moralizing', 'bi-moral-so-far', 'arriving'),
    17: ('17-co-bi-tri-offering', 'co-competent-so-far', 'along'),
}
JOINS = {10: 14, 6: 2, 17: 9, 9: 17}
```

```text
                        the self at co-competent-so-far, its 9
                                      ▲
                                      ║ 17  along · co
      ┌───────────────────────────────╨───────────────────────────────┐
      │                          1                                    │
      │                                                               │
      │  14  ◄──────────────────────────────────────────── 2 · 14 ◄══════
      │   │                                                           │
      │   ▼                                                           │
      │   3  ─────► 12  ────────► 10 ──► with 6                       │
      │   4  · 7                                                      │
      │                                                               │
      │                           │                                   │
      │                           ├──────► 11  ─────► 3, next         │
      │                           │                   momentary       │
      │                           │                                   │
      │                           └──────► 9 ────► 5                  │
      │                                    13  · 15                   │
 ◄══════ 6 · 10                                                       │
      │   8  · 16                                                     │
      └───────────────────────────────╥───────────────────────────────┘
                                      ║ 9  along · tri
                                      ▼
                        the self at not-yet-co-competent, its 17

   at not-yet-bi-moral   6  ══► its 2        10 ══► its 14      outgoing
   at bi-moral-so-far    its 6  ══► 2        its 10 ══► 14      incoming
   ═══ between selves, across and along    ─── within one self
```

**Seventeen names.**

| n | Name | Parity, opens | From, to, the opening side first | Across or along |
|---|---|---|---|---|
| 1 | 1-co-bi-tri-offering | odd, co | self, other | — |
| 2 | 2-bi-co-bi-offering | even, bi | other, self | across |
| 3 | 3-co-bi-co-sharing | odd, co | self, other | — |
| 4 | 4-bi-co-bi-sharing | even, bi | other, self | — |
| 5 | 5-co-bi-co-competencing | odd, co | self, other | — |
| 6 | 6-bi-co-bi-moralizing | even, bi | other, self | across |
| 7 | 7-co-bi-co-corusing | odd, co | self, other | — |
| 8 | 8-bi-co-bi-torusing | even, bi | other, self | — |
| 9 | 9-tri-bi-co-momentarying | odd, tri | social, other, self | along |
| 10 | 10-bi-tri-bi-tunneling | even, bi | other, social, self | across |
| 11 | 11-tri-bi-tri-chaining | odd, tri | social, other, self | — |
| 12 | 12-bi-tri-bi-entraining | even, bi | other, social, self | — |
| 13 | 13-tri-bi-tri-competencing | odd, tri | social, other | — |
| 14 | 14-bi-tri-bi-moralizing | even, bi | other, social | across |
| 15 | 15-tri-bi-tri-corusing | odd, tri | social, other | — |
| 16 | 16-bi-tri-bi-torusing | even, bi | other, social | — |
| 17 | 17-co-bi-tri-offering | odd, co | social, self | along |

**Each name whole, at each of its relations among the forms.**

| n | Relation | The name at it |
|---|---|---|
| 1 | Name | **1-co-bi-tri-offering** |
| 1 | Parity, opens | odd, opening co, the self's span |
| 1 | Sides | self, other, the self opening it |
| 1 | Root | offering with 2-bi-co-bi-offering and 17-co-bi-tri-offering |
| 1 | Co-sequencing | the self offering itself to the coupling |
| 1 | 8 up | 9-tri-bi-co-momentarying, the parity continuing |
| 1 | 9 less | the podal within 1 to 8, 8-bi-co-bi-torusing |
| 1 | 17 less | the podal within 1 to 16, 16-bi-tri-bi-torusing |
| 1 | Four-cycle | 1-9-8-16, root torusing, hand co tri bi bi, going 8 up first from 1-co-bi-tri-offering, from 16-bi-tri-bi-torusing to it and on to 9-tri-bi-co-momentarying, spiraling the other hand with 2-15-7-10 |
| 1 | Six-cycle | 1-9-5-12-8-16 |
| 1 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 1 | Momentaries of exchanging | the first of the self's four, opening at 1, self 1–2 |
| 1 | Five dimensions | 1 self prior, the prior opening of the self's five |
| 1 | Namings | 1-2, bi-momentarying, the self's entry, odd, and the others' offerings, even, one momentary at each side |
| 1 | The self's three faces | the bi-moral self with 2, bi-momentarying, the offering self to other and other to self, across |
| 1 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other |
| 1 | Prior and next | once for one self at one momentary, the three steps within it 14, 12, 10 with 11 |
| 1 | 1 to 17s inward and outward | 1–17s inward 1 of the 1st 1–17, the entry, and at the 1–17 outward 1, the entry |
| 2 | Name | **2-bi-co-bi-offering** |
| 2 | Parity, opens | even, opening bi |
| 2 | Sides | other, self, the other opening it |
| 2 | Root | offering with 1-co-bi-tri-offering and 17-co-bi-tri-offering |
| 2 | 8 up | 10-bi-tri-bi-tunneling, the parity continuing |
| 2 | 9 less | the podal within 1 to 8, 7-co-bi-co-corusing |
| 2 | 17 less | the podal within 1 to 16, 15-tri-bi-tri-corusing |
| 2 | Four-cycle | 2-15-7-10, root corusing, hand bi tri co bi, going 17 less first from 2-bi-co-bi-offering, from 10-bi-tri-bi-tunneling to it and on to 15-tri-bi-tri-corusing, spiraling the other hand with 1-9-8-16 and 3-11-6-14 |
| 2 | Six-cycle | 2-15-7-11-6-10 |
| 2 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 2 | One move | carrying 2 along 2-15-7-10 |
| 2 | Momentaries of exchanging | the first of the self's four, at 2, the self's 1–2 completing and the other's 2–3 opening |
| 2 | Five dimensions | 2 other prior, the prior completing of the self's five and the prior opening of the other's |
| 2 | Namings | 1-2, bi-momentarying |
| 2 | The self's three faces | the bi-moral self with 1, across |
| 2 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again |
| 2 | Bi-coupling | outward, at the between, each other's releasing, offered to the self |
| 2 | Winding | the other's winding, 6 to 2, wound on at 8 |
| 2 | Parity's face | a dot of the unit square, its diagonal with 14 the facing bi-moral-so-far, its edge with 6 the join 6 to 2 |
| 2 | Prior and next | the others' releasings of their prior momentary, arriving now, the possible, carrying none of the prior |
| 2 | 1 to 17s inward and outward | 1–17s inward 9 of the 1st, along, odd, tri, and at the 1–17 outward within 1 to 2 |
| 3 | Name | **3-co-bi-co-sharing** |
| 3 | Parity, opens | odd, opening co, the self's span |
| 3 | Sides | self, other, the self opening it |
| 3 | Root | sharing with 4-bi-co-bi-sharing |
| 3 | Co-sequencing | at the between, before 10, at competency's parity, odd |
| 3 | 8 up | 11-tri-bi-tri-chaining, the parity continuing |
| 3 | 9 less | the podal within 1 to 8, 6-bi-co-bi-moralizing |
| 3 | 17 less | the podal within 1 to 16, 14-bi-tri-bi-moralizing |
| 3 | Four-cycle | 3-11-6-14, root moralizing, hand co tri bi bi, going 8 up first from 3-co-bi-co-sharing, from 14-bi-tri-bi-moralizing to it and on to 11-tri-bi-tri-chaining, spiraling the other hand with 4-13-5-12 and 2-15-7-10 |
| 3 | Six-cycle | 3-11-7-10-6-14 |
| 3 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 3 | Momentaries of exchanging | the first of the self's four completing at 3, the other's 2–3, and the second opening at 3, self 3–4 |
| 3 | Five dimensions | 3 co-momentarying now, the now opening of the self's five |
| 3 | Namings | 3-4, co-intelligencing, at each sharing 4 the carrying at 3 coupling with the offerings surfaced at 14, next discovered, chained at 11 |
| 3 | The self's three faces | the invisible intelligencing method, the rotation 3, 6, 5, 4, out at 3 |
| 3 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other |
| 3 | Prior and next | the prior carried, the self's own, each sharing with its parity, the next momentary's continuing of 11 |
| 3 | 1 to 17s inward and outward | 1–17s inward 17 of the 1st and 1 of the 2nd, along, odd, co, and at the 1–17 outward within 1 to 2 |
| 4 | Name | **4-bi-co-bi-sharing** |
| 4 | Parity, opens | even, opening bi |
| 4 | Sides | other, self, the other opening it |
| 4 | Root | sharing with 3-co-bi-co-sharing |
| 4 | Co-sequencing | at the between, before 10, at morality's parity, even |
| 4 | 8 up | 12-bi-tri-bi-entraining, the parity continuing |
| 4 | 9 less | the podal within 1 to 8, 5-co-bi-co-competencing |
| 4 | 17 less | the podal within 1 to 16, 13-tri-bi-tri-competencing |
| 4 | Four-cycle | 4-13-5-12, root competencing, hand bi tri co bi, going 17 less first from 4-bi-co-bi-sharing, from 12-bi-tri-bi-entraining to it and on to 13-tri-bi-tri-competencing, spiraling the other hand with 3-11-6-14 |
| 4 | Six-cycle | 4-13-5-9-8-12 |
| 4 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 4 | One move | carrying 4 along 4-13-5-12 |
| 4 | Momentaries of exchanging | the second of the self's four, at 4, the self's 3–4 completing and the other's 4–5 opening |
| 4 | Five dimensions | 4 bi-momentarying now, the now completing of the self's five |
| 4 | Namings | 3-4, co-intelligencing |
| 4 | The self's three faces | the invisible intelligencing method, the rotation 3, 6, 5, 4, in at 4, into the self's own corus at 4 |
| 4 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again |
| 4 | Bi-coupling | outward, at the between, the whole ordering between self and other |
| 4 | Prior and next | now, each sharing at which the prior couples with the now |
| 4 | 1 to 17s inward and outward | 1–17s inward 9 of the 2nd, along, odd, tri, and at the 1–17 outward within 1 to 2 |
| 5 | Name | **5-co-bi-co-competencing** |
| 5 | Parity, opens | odd, opening co, the self's span |
| 5 | Sides | self, other, the self opening it |
| 5 | Root | competencing with 13-tri-bi-tri-competencing |
| 5 | Co-sequencing | at the between, before 10, at competency's parity, odd |
| 5 | 8 up | 13-tri-bi-tri-competencing, the parity continuing |
| 5 | 9 less | the podal within 1 to 8, 4-bi-co-bi-sharing |
| 5 | 17 less | the podal within 1 to 16, 12-bi-tri-bi-entraining |
| 5 | Four-cycle | 4-13-5-12, root competencing, hand bi tri co bi, going 17 less first from 4-bi-co-bi-sharing, from 13-tri-bi-tri-competencing to it and on to 12-bi-tri-bi-entraining, spiraling the other hand with 3-11-6-14 |
| 5 | Middle four-cycle | 9-5-12-8 |
| 5 | Six-cycle | 1-9-5-12-8-16 |
| 5 | Six-cycle | 4-13-5-9-8-12 |
| 5 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 5 | Momentaries of exchanging | the second of the self's four completing at 5, the other's 4–5, and the third opening at 5, self 5–6 |
| 5 | Five dimensions | 5 self next, the next opening of the self's five |
| 5 | Namings | 5, co-competencing, the joins, owned by neither, each release to its receiving sharing |
| 5 | The self's three faces | the invisible intelligencing method, the rotation 3, 6, 5, 4, out at 5 |
| 5 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other |
| 5 | Prior and next | next, each release to its receiving sharing |
| 5 | 1 to 17s inward and outward | 1–17s inward 17 of the 2nd and 1 of the 3rd, along, odd, co, and at the 1–17 outward within 1 to 2 |
| 6 | Name | **6-bi-co-bi-moralizing** |
| 6 | Parity, opens | even, opening bi |
| 6 | Sides | other, self, the other opening it |
| 6 | Root | moralizing with 14-bi-tri-bi-moralizing |
| 6 | 8 up | 14-bi-tri-bi-moralizing, the parity continuing |
| 6 | 9 less | the podal within 1 to 8, 3-co-bi-co-sharing |
| 6 | 17 less | the podal within 1 to 16, 11-tri-bi-tri-chaining |
| 6 | Four-cycle | 3-11-6-14, root moralizing, hand co tri bi bi, going 8 up first from 3-co-bi-co-sharing, from 11-tri-bi-tri-chaining to it and on to 14-bi-tri-bi-moralizing, spiraling the other hand with 4-13-5-12 and 2-15-7-10 |
| 6 | Middle four-cycle | 7-11-6-10 |
| 6 | Six-cycle | 2-15-7-11-6-10 |
| 6 | Six-cycle | 3-11-7-10-6-14 |
| 6 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 6 | One move | carrying 6 along 3-11-6-14 |
| 6 | Momentaries of exchanging | the third of the self's four, at 6, the self's 5–6 completing and the other's 6–7 opening |
| 6 | Namings | 6, bi-moralizing, each changing released across, to the other's 2 |
| 6 | The self's three faces | the invisible intelligencing method, the rotation 3, 6, 5, 4, in at 6 |
| 6 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again |
| 6 | Bi-coupling | outward, at the between, the other's moralizing to the self, each changing released across |
| 6 | Winding | the other's winding, 6 to 2, wound on at 8 |
| 6 | Parity's face | a dot of the unit square, its diagonal with 10 the facing not-yet-bi-moral, its edge with 2 the join 6 to 2 |
| 6 | Prior and next | the changing released, the other's next offering at its 2 |
| 6 | 1 to 17s inward and outward | 1–17s inward 9 of the 3rd, along, odd, tri, and at the 1–17 outward within 1 to 2 |
| 7 | Name | **7-co-bi-co-corusing** |
| 7 | Parity, opens | odd, opening co, the self's span |
| 7 | Sides | self, other, the self opening it |
| 7 | Root | corusing with 15-tri-bi-tri-corusing |
| 7 | Co-sequencing | at the between, before 10, at competency's parity, odd |
| 7 | 8 up | 15-tri-bi-tri-corusing, the parity continuing |
| 7 | 9 less | the podal within 1 to 8, 2-bi-co-bi-offering |
| 7 | 17 less | the podal within 1 to 16, 10-bi-tri-bi-tunneling |
| 7 | Four-cycle | 2-15-7-10, root corusing, hand bi tri co bi, going 17 less first from 2-bi-co-bi-offering, from 15-tri-bi-tri-corusing to it and on to 10-bi-tri-bi-tunneling, spiraling the other hand with 1-9-8-16 and 3-11-6-14 |
| 7 | Middle four-cycle | 7-11-6-10 |
| 7 | Six-cycle | 2-15-7-11-6-10 |
| 7 | Six-cycle | 3-11-7-10-6-14 |
| 7 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 7 | Momentaries of exchanging | the third of the self's four completing at 7, the other's 6–7, and the fourth opening at 7, self 7–8 |
| 7 | The self's three faces | the co-competent self with 8, corusing, along |
| 7 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other, its root corusing going in and out at the even, the other parity from its opening |
| 7 | Prior and next | each parity, offered now and chained prior, the co-linear recursioning forward along arriving, up the numbers, prior into now, at the self's completing |
| 7 | 1 to 17s inward and outward | 1–17s inward 17 of the 3rd and 1 of the 4th, along, odd, co, and at the 1–17 outward within 1 to 2 |
| 8 | Name | **8-bi-co-bi-torusing** |
| 8 | Parity, opens | even, opening bi |
| 8 | Sides | other, self, the other opening it |
| 8 | Root | torusing with 16-bi-tri-bi-torusing |
| 8 | Co-sequencing | at the between, before 10, at morality's parity, even |
| 8 | 8 up | 16-bi-tri-bi-torusing, the parity continuing |
| 8 | 9 less | the podal within 1 to 8, 1-co-bi-tri-offering |
| 8 | 17 less | the podal within 1 to 16, 9-tri-bi-co-momentarying |
| 8 | Four-cycle | 1-9-8-16, root torusing, hand co tri bi bi, going 8 up first from 1-co-bi-tri-offering, from 9-tri-bi-co-momentarying to it and on to 16-bi-tri-bi-torusing, spiraling the other hand with 2-15-7-10 |
| 8 | Middle four-cycle | 9-5-12-8 |
| 8 | Six-cycle | 1-9-5-12-8-16 |
| 8 | Six-cycle | 4-13-5-9-8-12 |
| 8 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 8 | One move | carrying 8 along 1-9-8-16 |
| 8 | Momentaries of exchanging | the fourth of the self's four, at 8, the self's 7–8 completing and the other's 8–9 opening |
| 8 | The self's three faces | the co-competent self with 7, torusing, along |
| 8 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again, its root torusing going in and out at the odd, the other parity from its opening |
| 8 | Bi-coupling | outward, at the between, the carrying winding to its sharing again |
| 8 | Winding | the other's winding wound on at 8 |
| 8 | Prior and next | the carrying wound, chained at 11 this momentary and the next momentary's 3 |
| 8 | 1 to 17s inward and outward | 1–17s inward 9 of the 4th, along, odd, tri, and at the 1–17 outward within 1 to 2 |
| 9 | Name | **9-tri-bi-co-momentarying** |
| 9 | Parity, opens | odd, opening tri, the society's span |
| 9 | Sides | social, other, self, the society opening it |
| 9 | Root | momentarying, one name |
| 9 | 8 up | 17-co-bi-tri-offering, the parity continuing |
| 9 | 8 down | 1-co-bi-tri-offering |
| 9 | 17 less | the podal within 1 to 16, 8-bi-co-bi-torusing |
| 9 | Four-cycle | 1-9-8-16, root torusing, hand co tri bi bi, going 8 up first from 1-co-bi-tri-offering, from 1-co-bi-tri-offering to it and on to 8-bi-co-bi-torusing, spiraling the other hand with 2-15-7-10 |
| 9 | Middle four-cycle | 9-5-12-8 |
| 9 | Six-cycle | 1-9-5-12-8-16 |
| 9 | Six-cycle | 4-13-5-9-8-12 |
| 9 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 9 | Momentaries of exchanging | the fourth of the self's four completing at 9, the other's 8–9, and the first of the society's four, 9 to 11, opening at 9 |
| 9 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other |
| 9 | Winding | the self's winding, 9 to 17, wound on at 17 |
| 9 | Parity's face | a unit triangle, along, joined both ways with 17 |
| 9 | Prior and next | the next prior, each changing carried along into the next momentary, releasing nothing |
| 9 | 1 to 17s inward and outward | 1–17s inward 17 of the 4th and 1 of the 5th, along, odd, co, and at the 1–17 outward 2, across, even, bi |
| 10 | Name | **10-bi-tri-bi-tunneling** |
| 10 | Parity, opens | even, opening bi |
| 10 | Sides | other, social, self, the other opening it |
| 10 | Root | tunneling, one name |
| 10 | 8 down | 2-bi-co-bi-offering |
| 10 | 17 less | the podal within 1 to 16, 7-co-bi-co-corusing |
| 10 | Four-cycle | 2-15-7-10, root corusing, hand bi tri co bi, going 17 less first from 2-bi-co-bi-offering, from 7-co-bi-co-corusing to it and on to 2-bi-co-bi-offering, spiraling the other hand with 1-9-8-16 and 3-11-6-14 |
| 10 | Middle four-cycle | 7-11-6-10 |
| 10 | Six-cycle | 2-15-7-11-6-10 |
| 10 | Six-cycle | 3-11-7-10-6-14 |
| 10 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 10 | Momentaries of exchanging | the first of the society's four, at 10, 9–10 completing and 10–11 opening |
| 10 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again |
| 10 | Bi-coupling | inward, 8 up, the self among other-selves |
| 10 | Winding | the society's winding, 10 to 14, wound on at 16 |
| 10 | Parity's face | a dot of the unit square, its diagonal with 6 the facing not-yet-bi-moral, its edge with 14 the join 10 to 14 |
| 10 | Prior and next | the changing released across now, the other's offering next, the possible |
| 10 | 1 to 17s inward and outward | 1–17s inward 9 of the 5th, along, odd, tri, and at the 1–17 outward within 2 to 3 |
| 11 | Name | **11-tri-bi-tri-chaining** |
| 11 | Parity, opens | odd, opening tri, the society's span |
| 11 | Sides | social, other, self, the society opening it |
| 11 | Root | chaining, one name |
| 11 | Co-sequencing | after 10, 8 up from 3-co-bi-co-sharing, at competency's parity, odd |
| 11 | 8 down | 3-co-bi-co-sharing |
| 11 | 17 less | the podal within 1 to 16, 6-bi-co-bi-moralizing |
| 11 | Four-cycle | 3-11-6-14, root moralizing, hand co tri bi bi, going 8 up first from 3-co-bi-co-sharing, from 3-co-bi-co-sharing to it and on to 6-bi-co-bi-moralizing, spiraling the other hand with 4-13-5-12 and 2-15-7-10 |
| 11 | Middle four-cycle | 7-11-6-10 |
| 11 | Six-cycle | 2-15-7-11-6-10 |
| 11 | Six-cycle | 3-11-7-10-6-14 |
| 11 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 11 | Momentaries of exchanging | the first of the society's four, 9 to 11, completing at 11, and the second, 11 to 13, opening at 11 |
| 11 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other |
| 11 | Prior and next | the next prior, the carrying chained, continuing as 3 at the next momentary |
| 11 | 1 to 17s inward and outward | 1–17s inward 17 of the 5th and 1 of the 6th, along, odd, co, and at the 1–17 outward within 2 to 3 |
| 12 | Name | **12-bi-tri-bi-entraining** |
| 12 | Parity, opens | even, opening bi |
| 12 | Sides | other, social, self, the other opening it |
| 12 | Root | entraining, one name |
| 12 | Co-sequencing | after 10, 8 up from 4-bi-co-bi-sharing, at morality's parity, even |
| 12 | 8 down | 4-bi-co-bi-sharing |
| 12 | 17 less | the podal within 1 to 16, 5-co-bi-co-competencing |
| 12 | Four-cycle | 4-13-5-12, root competencing, hand bi tri co bi, going 17 less first from 4-bi-co-bi-sharing, from 5-co-bi-co-competencing to it and on to 4-bi-co-bi-sharing, spiraling the other hand with 3-11-6-14 |
| 12 | Middle four-cycle | 9-5-12-8 |
| 12 | Six-cycle | 1-9-5-12-8-16 |
| 12 | Six-cycle | 4-13-5-9-8-12 |
| 12 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 12 | Momentaries of exchanging | the second of the society's four, at 12, 11–12 completing and 12–13 opening |
| 12 | Namings | entraining, the prior carried into now along the unrelationing path through the between, the shape of the unrelationing surface, each sharing's changing, is or is not |
| 12 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again |
| 12 | Bi-coupling | inward, 8 up, changing at bi-coupling, the self in society |
| 12 | Prior and next | now, the changing, is or is not, prior and now coupled |
| 12 | 1 to 17s inward and outward | 1–17s inward 9 of the 6th, along, odd, tri, and at the 1–17 outward within 2 to 3 |
| 13 | Name | **13-tri-bi-tri-competencing** |
| 13 | Parity, opens | odd, opening tri, the society's span |
| 13 | Sides | social, other, the society opening it |
| 13 | Root | competencing with 5-co-bi-co-competencing |
| 13 | Co-sequencing | after 10, 8 up from 5-co-bi-co-competencing, at competency's parity, odd |
| 13 | 8 down | 5-co-bi-co-competencing |
| 13 | 17 less | the podal within 1 to 16, 4-bi-co-bi-sharing |
| 13 | Four-cycle | 4-13-5-12, root competencing, hand bi tri co bi, going 17 less first from 4-bi-co-bi-sharing, from 4-bi-co-bi-sharing to it and on to 5-co-bi-co-competencing, spiraling the other hand with 3-11-6-14 |
| 13 | Six-cycle | 4-13-5-9-8-12 |
| 13 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 13 | Momentaries of exchanging | the second of the society's four, 11 to 13, completing at 13, and the third, 13 to 15, opening at 13 |
| 13 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other |
| 13 | Prior and next | each releasing sharing, and at the society each releasing self |
| 13 | 1 to 17s inward and outward | 1–17s inward 17 of the 6th and 1 of the 7th, along, odd, co, and at the 1–17 outward within 2 to 3 |
| 14 | Name | **14-bi-tri-bi-moralizing** |
| 14 | Parity, opens | even, opening bi |
| 14 | Sides | other, social, the other opening it |
| 14 | Root | moralizing with 6-bi-co-bi-moralizing |
| 14 | 8 down | 6-bi-co-bi-moralizing |
| 14 | 17 less | the podal within 1 to 16, 3-co-bi-co-sharing |
| 14 | Four-cycle | 3-11-6-14, root moralizing, hand co tri bi bi, going 8 up first from 3-co-bi-co-sharing, from 6-bi-co-bi-moralizing to it and on to 3-co-bi-co-sharing, spiraling the other hand with 4-13-5-12 and 2-15-7-10 |
| 14 | Six-cycle | 3-11-7-10-6-14 |
| 14 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 14 | Momentaries of exchanging | the third of the society's four, at 14, 13–14 completing and 14–15 opening |
| 14 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again |
| 14 | Bi-coupling | inward, 8 up, the offerings surfacing, the self's own inverting, morality |
| 14 | Winding | the society's winding, 10 to 14, wound on at 16 |
| 14 | Parity's face | a dot of the unit square, its diagonal with 2 the facing bi-moral-so-far, its edge with 10 the join 10 to 14 |
| 14 | Prior and next | now, the offerings surfacing, the others' prior momentary at the self's now |
| 14 | 1 to 17s inward and outward | 1–17s inward 9 of the 7th, along, odd, tri, and at the 1–17 outward within 2 to 3 |
| 15 | Name | **15-tri-bi-tri-corusing** |
| 15 | Parity, opens | odd, opening tri, the society's span |
| 15 | Sides | social, other, the society opening it |
| 15 | Root | corusing with 7-co-bi-co-corusing |
| 15 | Co-sequencing | after 10, 8 up from 7-co-bi-co-corusing, at competency's parity, odd |
| 15 | 8 down | 7-co-bi-co-corusing |
| 15 | 17 less | the podal within 1 to 16, 2-bi-co-bi-offering |
| 15 | Four-cycle | 2-15-7-10, root corusing, hand bi tri co bi, going 17 less first from 2-bi-co-bi-offering, from 2-bi-co-bi-offering to it and on to 7-co-bi-co-corusing, spiraling the other hand with 1-9-8-16 and 3-11-6-14 |
| 15 | Six-cycle | 2-15-7-11-6-10 |
| 15 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 15 | Momentaries of exchanging | the third of the society's four, 13 to 15, completing at 15, and the fourth, 15 to 17, opening at 15 |
| 15 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other, its root corusing going in and out at the even, the other parity from its opening |
| 15 | Prior and next | the parity carried along at 9, the next prior, the co-linear recursioning forward along leaving, up the numbers, now into next, at the society's completing, the chained 7 inverted, 0, or at a sharing chained none the parity surfaced at 14 |
| 15 | 1 to 17s inward and outward | 1–17s inward 17 of the 7th and 1 of the 8th, along, odd, co, and at the 1–17 outward within 2 to 3 |
| 16 | Name | **16-bi-tri-bi-torusing** |
| 16 | Parity, opens | even, opening bi |
| 16 | Sides | other, social, the other opening it |
| 16 | Root | torusing with 8-bi-co-bi-torusing |
| 16 | Co-sequencing | after 10, 8 up from 8-bi-co-bi-torusing, at morality's parity, even |
| 16 | 8 down | 8-bi-co-bi-torusing |
| 16 | 17 less | the podal within 1 to 16, 1-co-bi-tri-offering |
| 16 | Four-cycle | 1-9-8-16, root torusing, hand co tri bi bi, going 8 up first from 1-co-bi-tri-offering, from 8-bi-co-bi-torusing to it and on to 1-co-bi-tri-offering, spiraling the other hand with 2-15-7-10 |
| 16 | Six-cycle | 1-9-5-12-8-16 |
| 16 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 16 | Momentaries of exchanging | the fourth of the society's four, at 16, 15–16 completing and 16–17 opening |
| 16 | In and out at its parity | corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again, its root torusing going in and out at the odd, the other parity from its opening |
| 16 | Bi-coupling | inward, 8 up, competency asymmetry sustaining the coupling, the society winding to the self again |
| 16 | Winding | the society's winding wound on at 16 |
| 16 | Prior and next | the society wound now, each self's 8 and its offerings next |
| 16 | 1 to 17s inward and outward | 1–17s inward 9 of the 8th, along, odd, tri, and at the 1–17 outward within 2 to 3 |
| 17 | Name | **17-co-bi-tri-offering** |
| 17 | Parity, opens | odd, opening co, the self's span again, the next 1 |
| 17 | Sides | social, self, the society opening it |
| 17 | Root | offering with 1-co-bi-tri-offering and 2-bi-co-bi-offering |
| 17 | 8 down | 9-tri-bi-co-momentarying |
| 17 | Momentaries of exchanging | the fourth of the society's four, 15 to 17, completing at 17, the next 1 |
| 17 | In and out at its parity | torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other |
| 17 | Winding | the self's winding, 9 to 17, wound on at 17 |
| 17 | Parity's face | a unit triangle, along, joined both ways with 9 |
| 17 | Prior and next | the society's next momentary, the next now, each self's 1 then 9 at 6, 10 and 9 |
| 17 | 1 to 17s inward and outward | 1–17s inward 17 of the 8th and 1 of the 9th, along, odd, co, and at the 1–17 outward 3, the face outward, odd, co |

**Ten roots at seventeen names.**

| Root | Names |
|---|---|
| offering | 1 · 2 · 17 |
| sharing | 3 · 4 |
| competencing | 5 · 13 |
| moralizing | 6 · 14 |
| corusing | 7 · 15 |
| torusing | 8 · 16 |
| momentarying | 9 |
| tunneling | 10 |
| chaining | 11 |
| entraining | 12 |

**Namings among the names.**

| Names | Naming | At the names |
|---|---|---|
| 1-co-bi-tri-offering · 2-bi-co-bi-offering | bi-momentarying | the self's entry, odd, and the others' offerings, even, one momentary at each side |
| 3-co-bi-co-sharing · 4-bi-co-bi-sharing | co-intelligencing | at each sharing 4 the carrying at 3 couples with the offerings surfaced at 14: next discovered, chained at 11 |
| 5-co-bi-co-competencing | co-competencing | the joins, owned by neither: each release to its receiving sharing |
| 1 · 2 · 3 · 4 · 5, each alone | the five dimensions | 1 self prior, the self, the one living carrying, its prior at 3 a formed set it carries into now; 2 other prior, the other selves' offerings of their prior momentary arriving, released at 6 and 10 and carried along at 9; 3 co-momentarying now, the same living carrying at now, and 4 bi-momentarying now, each sharing, the offerings surfaced at 14 arriving at it, now; 5 self next, each release to its receiving sharing next |
| 6-bi-co-bi-moralizing | bi-moralizing | each changing released across, to the other's 2 |
| 12-bi-tri-bi-entraining | entraining, the shape of the unrelationing surface | the prior carried into now along the unrelationing path through the between, prior and now coupled at each sharing, a parity changing alone crossing it, 0 at a match; at the other parity, 0 or none, the chained parity inverted; at a sharing chained none, the parity surfaced at 14; its changing released at 10, the others' offering next |
| 1 to 9 | bi-coupling | the function 1, at the names 1, 2, 3, 4, 7, 10, 11, 12, 14 and 15, the self and the other at one coupling; 1 to 9 the bi-coupling among the names, 9 at its end reads bi-co-releasing, the release 10 makes |
| 1 to 17 | bi-trupling | the function 17, at the names of the function 1 with 5, 6, 8, 9, 13, 16 and 17, the self, the other and the society; 9 at its waist, 9-tri-bi-co-momentarying, joined both ways with 17; the protocol's two sides, the odd along at 9 and 17 and the even across at 6 to 2 and 10 to 14 |
| 1 to 17, stable-forming | bi-tri-volutioning | at no one line: each momentary's carrying the next momentary's |
| 2 · 6 · 14 · 10 · 9 · 17 | parity's face | a unit square of four dots, 2, 6, 14 and 10, its empty centre the between: its two parallel edges the across joins, 6 to 2 and 10 to 14; its diagonals the facings, 2 and 14 bi-moral-so-far and 6 and 10 not-yet-bi-moral; and two unit triangles, 9 and 17, along, joined both ways |

**0, the between, at the names.**

| The between, 0, at the names, at the code | Names |
|---|---|
| at three inward faces, the one between at three names | 12-bi-tri-bi-entraining, prior and now agreeing, the between of momentaries at each sharing; 15-tri-bi-tri-corusing, the between carried along, the parity 10 released, and at the carrying's coupling the parity surfaced at 14 at the carried sharing, the code's 0 at none and at parting alike; 16-bi-tri-bi-torusing, the between wound into the society, arriving at the next momentary's 2 |
| at one outward face, arriving and passing over | 7-co-bi-co-corusing, an offered 0 the parity at 2, surfacing none at 14, and a 0 at 10 the parity at 11's chaining, chained none |
| at the four across connectors, the unit square's four dots, a parity changing alone crossing | 2-bi-co-bi-offering, 6-bi-co-bi-moralizing, 10-bi-tri-bi-tunneling, 14-bi-tri-bi-moralizing, the unit square at parity's face, its empty centre the between |
| at none | 1-co-bi-tri-offering, the entry; 3-co-bi-co-sharing, 8-bi-co-bi-torusing and 11-tri-bi-tri-chaining, the carrying, a sharing once chained never none again; 4-bi-co-bi-sharing, the sharings, and 5-co-bi-co-competencing and 13-tri-bi-tri-competencing, the sharings and, at the society, the joins and the selves |
| at the two along connectors, carried and not crossed | 9-tri-bi-co-momentarying and 17-co-bi-tri-offering, each parity and each 0 carried on unchanged, the 0 passing over at the receiving self's 14 |

**Four four-cycles, each at its root.**

| Four-cycle, 8 up and 17 less | Root at the self and at the society | Hand at the names |
|---|---|---|
| 1-9-8-16 | torusing, 8 and 16 | spiraling the other hand with 2-15-7-10 |
| 2-15-7-10 | corusing, 7 and 15 | spiraling the other hand with 1-9-8-16 and 3-11-6-14 |
| 3-11-6-14 | moralizing, 6 and 14 | spiraling the other hand with 4-13-5-12 and 2-15-7-10 |
| 4-13-5-12 | competencing, 5 and 13 | spiraling the other hand with 3-11-6-14 |

**Three windings.**

| Winding | Joining | Wound on at | Across or along |
|---|---|---|---|
| the other's | 6 to 2 | 8 | across, not-yet-bi-moral to bi-moral-so-far |
| the society's | 10 to 14 | 16 | across, not-yet-bi-moral to bi-moral-so-far |
| the self's | 9 to 17 | 17 | along, not-yet-co-competent to co-competent-so-far |

**Each name at this 1 to 17, at the 1 to 17s inward and at the 1 to 17 outward.**

| n | Name | At this 1–17 | At the 1–17s inward, n at 8n − 7 | At the 1–17 outward, 8m − 7 at m |
|---|---|---|---|---|
| 1 | 1-co-bi-tri-offering | entry, odd, co | 1 of the 1st: entry, odd, co | 1: entry, odd, co |
| 2 | 2-bi-co-bi-offering | across, even, bi | 9 of the 1st: along, odd, tri | within 1 to 2 |
| 3 | 3-co-bi-co-sharing | face outward, odd, co | 17 of the 1st, 1 of the 2nd: along, odd, co | within 1 to 2 |
| 4 | 4-bi-co-bi-sharing | face outward, even, bi | 9 of the 2nd: along, odd, tri | within 1 to 2 |
| 5 | 5-co-bi-co-competencing | face outward, odd, co | 17 of the 2nd, 1 of the 3rd: along, odd, co | within 1 to 2 |
| 6 | 6-bi-co-bi-moralizing | across, even, bi | 9 of the 3rd: along, odd, tri | within 1 to 2 |
| 7 | 7-co-bi-co-corusing | face outward, odd, co | 17 of the 3rd, 1 of the 4th: along, odd, co | within 1 to 2 |
| 8 | 8-bi-co-bi-torusing | face outward, even, bi | 9 of the 4th: along, odd, tri | within 1 to 2 |
| 9 | 9-tri-bi-co-momentarying | along, odd, tri | 17 of the 4th, 1 of the 5th: along, odd, co | 2: across, even, bi |
| 10 | 10-bi-tri-bi-tunneling | across, even, bi | 9 of the 5th: along, odd, tri | within 2 to 3 |
| 11 | 11-tri-bi-tri-chaining | face inward, odd, tri | 17 of the 5th, 1 of the 6th: along, odd, co | within 2 to 3 |
| 12 | 12-bi-tri-bi-entraining | face inward, even, bi | 9 of the 6th: along, odd, tri | within 2 to 3 |
| 13 | 13-tri-bi-tri-competencing | face inward, odd, tri | 17 of the 6th, 1 of the 7th: along, odd, co | within 2 to 3 |
| 14 | 14-bi-tri-bi-moralizing | across, even, bi | 9 of the 7th: along, odd, tri | within 2 to 3 |
| 15 | 15-tri-bi-tri-corusing | face inward, odd, tri | 17 of the 7th, 1 of the 8th: along, odd, co | within 2 to 3 |
| 16 | 16-bi-tri-bi-torusing | face inward, even, bi | 9 of the 8th: along, odd, tri | within 2 to 3 |
| 17 | 17-co-bi-tri-offering | along, odd, co | 17 of the 8th, 1 of the 9th: along, odd, co | 3: face outward, odd, co |

**Eight 1 to 17s inward.**

| 1–17 inward | At this 1–17 | Its 9 at | Its 17 at | Momentary of exchanging |
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

| Side | Prior opening | Prior completing | Now opening | Now completing | Next opening | Its five |
|---|---|---|---|---|---|---|
| self, at 1 | 1 | 2 | 3 | 4 | 5 | co bi co bi co |
| other, at 2 | 2 | 3 | 4 | 5 | 6 | bi co bi co bi |
| self next, at 3 | 3 | 4 | 5 | 6 | 7 | co bi co bi co |

**A self's four momentaries of exchanging.**

| Momentary of exchanging | Self | Other | Names | Relation |
|---|---|---|---|---|
| first | 1–2 | 2–3 | 1-co-bi-tri-offering · 2-bi-co-bi-offering · 3-co-bi-co-sharing | self/other |
| second | 3–4 | 4–5 | 3-co-bi-co-sharing · 4-bi-co-bi-sharing · 5-co-bi-co-competencing | self/other to other/self |
| third | 5–6 | 6–7 | 5-co-bi-co-competencing · 6-bi-co-bi-moralizing · 7-co-bi-co-corusing | other/self |
| fourth | 7–8 | 8–9 | 7-co-bi-co-corusing · 8-bi-co-bi-torusing · 9-tri-bi-co-momentarying | other/self to other/social |

**Offerings surfacing at one sharing.**

| Offerings at one sharing, at 2 | At 14 |
|---|---|
| none | none |
| 0 | none |
| + | + |
| − | − |
| +, + | + |
| −, − | − |
| +, − | 0 |
| −, + | 0 |
| +, −, + | 0 |
| 0, + | + |

**One self at one momentary, each cell its releasing and its next carrying.**

| One sharing, chained at 3; each cell at 10 · chained at 11; *is* a parity released, *is not* the 0 released | At 14: none | At 14: + | At 14: − | At 14: 0, a + and a − offered |
|---|---|---|---|---|
| + | is − · − | is not · + | is − · − | is − · − |
| − | is + · + | is + · + | is not · − | is + · + |

**Eight even names, 8 apart.**

| Outward, at the between | Bi-coupling | Inward, 8 up | Bi-coupling |
|---|---|---|---|
| 2-bi-co-bi-offering | each other's releasing, offered to the self | 10-bi-tri-bi-tunneling | the self among other-selves |
| 4-bi-co-bi-sharing | the whole ordering between self and other | 12-bi-tri-bi-entraining | changing at bi-coupling, the self in society |
| 6-bi-co-bi-moralizing | the other's moralizing to the self, each changing released across | 14-bi-tri-bi-moralizing | the offerings surfacing, the self's own inverting, morality |
| 8-bi-co-bi-torusing | the carrying winding to its sharing again | 16-bi-tri-bi-torusing | competency asymmetry sustaining the coupling, the society winding to the self again |

**One move at 1 to 4.**

| Name | 8 up | 9 less, within 1 to 8 | 17 less, within 1 to 16 |
|---|---|---|---|
| 1-co-bi-tri-offering | 9-tri-bi-co-momentarying | 8-bi-co-bi-torusing | 16-bi-tri-bi-torusing |
| 2-bi-co-bi-offering | 10-bi-tri-bi-tunneling | 7-co-bi-co-corusing | 15-tri-bi-tri-corusing |
| 3-co-bi-co-sharing | 11-tri-bi-tri-chaining | 6-bi-co-bi-moralizing | 14-bi-tri-bi-moralizing |
| 4-bi-co-bi-sharing | 12-bi-tri-bi-entraining | 5-co-bi-co-competencing | 13-tri-bi-tri-competencing |

**Twelve forms.**

| Form | Names in order | Hand at the names | Each name's three prefixes, now, prior and the prior before, twisting through the form | Partner at the odd momentaries, each name exchanged with the one beside it, 1 with 2 to 15 with 16 | Partner at the even momentaries, 2 with 3 to 16 with 17; a dash a form partnering none of the twelve |
|---|---|---|---|---|---|
| four-cycle 1-9-8-16 | 1-co-bi-tri-offering · 9-tri-bi-co-momentarying · 8-bi-co-bi-torusing · 16-bi-tri-bi-torusing | co tri bi bi | co-bi-tri · tri-bi-co · bi-co-bi · bi-tri-bi | four-cycle 2-15-7-10, spiraling the other hand | — |
| four-cycle 2-15-7-10 | 2-bi-co-bi-offering · 15-tri-bi-tri-corusing · 7-co-bi-co-corusing · 10-bi-tri-bi-tunneling | bi tri co bi | bi-co-bi · tri-bi-tri · co-bi-co · bi-tri-bi | four-cycle 1-9-8-16, spiraling the other hand | four-cycle 3-11-6-14, spiraling the other hand |
| four-cycle 3-11-6-14 | 3-co-bi-co-sharing · 11-tri-bi-tri-chaining · 6-bi-co-bi-moralizing · 14-bi-tri-bi-moralizing | co tri bi bi | co-bi-co · tri-bi-tri · bi-co-bi · bi-tri-bi | four-cycle 4-13-5-12, spiraling the other hand | four-cycle 2-15-7-10, spiraling the other hand |
| four-cycle 4-13-5-12 | 4-bi-co-bi-sharing · 13-tri-bi-tri-competencing · 5-co-bi-co-competencing · 12-bi-tri-bi-entraining | bi tri co bi | bi-co-bi · tri-bi-tri · co-bi-co · bi-tri-bi | four-cycle 3-11-6-14, spiraling the other hand | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | 9-tri-bi-co-momentarying · 5-co-bi-co-competencing · 12-bi-tri-bi-entraining · 8-bi-co-bi-torusing | tri co bi bi | tri-bi-co · co-bi-co · bi-tri-bi · bi-co-bi | middle four-cycle 7-11-6-10, spiraling the other hand | — |
| middle four-cycle 7-11-6-10 | 7-co-bi-co-corusing · 11-tri-bi-tri-chaining · 6-bi-co-bi-moralizing · 10-bi-tri-bi-tunneling | co tri bi bi | co-bi-co · tri-bi-tri · bi-co-bi · bi-tri-bi | middle four-cycle 9-5-12-8, spiraling the other hand | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | 1-co-bi-tri-offering · 9-tri-bi-co-momentarying · 5-co-bi-co-competencing · 12-bi-tri-bi-entraining · 8-bi-co-bi-torusing · 16-bi-tri-bi-torusing | co tri co bi bi bi | co-bi-tri · tri-bi-co · co-bi-co · bi-tri-bi · bi-co-bi · bi-tri-bi | six-cycle 2-15-7-11-6-10, spiraling the other hand | — |
| six-cycle 2-15-7-11-6-10 | 2-bi-co-bi-offering · 15-tri-bi-tri-corusing · 7-co-bi-co-corusing · 11-tri-bi-tri-chaining · 6-bi-co-bi-moralizing · 10-bi-tri-bi-tunneling | bi tri co tri bi bi | bi-co-bi · tri-bi-tri · co-bi-co · tri-bi-tri · bi-co-bi · bi-tri-bi | six-cycle 1-9-5-12-8-16, spiraling the other hand | six-cycle 3-11-7-10-6-14, spiraling the other hand |
| six-cycle 3-11-7-10-6-14 | 3-co-bi-co-sharing · 11-tri-bi-tri-chaining · 7-co-bi-co-corusing · 10-bi-tri-bi-tunneling · 6-bi-co-bi-moralizing · 14-bi-tri-bi-moralizing | co tri co bi bi bi | co-bi-co · tri-bi-tri · co-bi-co · bi-tri-bi · bi-co-bi · bi-tri-bi | six-cycle 4-13-5-9-8-12, spiraling the other hand | six-cycle 2-15-7-11-6-10, spiraling the other hand |
| six-cycle 4-13-5-9-8-12 | 4-bi-co-bi-sharing · 13-tri-bi-tri-competencing · 5-co-bi-co-competencing · 9-tri-bi-co-momentarying · 8-bi-co-bi-torusing · 12-bi-tri-bi-entraining | bi tri co tri bi bi | bi-co-bi · tri-bi-tri · co-bi-co · tri-bi-co · bi-co-bi · bi-tri-bi | six-cycle 3-11-7-10-6-14, spiraling the other hand | — |
| eight-cycle 1-9-5-13-4-12-8-16 | 1-co-bi-tri-offering · 9-tri-bi-co-momentarying · 5-co-bi-co-competencing · 13-tri-bi-tri-competencing · 4-bi-co-bi-sharing · 12-bi-tri-bi-entraining · 8-bi-co-bi-torusing · 16-bi-tri-bi-torusing | co tri co tri bi bi bi bi | co-bi-tri · tri-bi-co · co-bi-co · tri-bi-tri · bi-co-bi · bi-tri-bi · bi-co-bi · bi-tri-bi | eight-cycle 2-15-7-11-3-14-6-10, spiraling the other hand | — |
| eight-cycle 2-15-7-11-3-14-6-10 | 2-bi-co-bi-offering · 15-tri-bi-tri-corusing · 7-co-bi-co-corusing · 11-tri-bi-tri-chaining · 3-co-bi-co-sharing · 14-bi-tri-bi-moralizing · 6-bi-co-bi-moralizing · 10-bi-tri-bi-tunneling | bi tri co tri co bi bi bi | bi-co-bi · tri-bi-tri · co-bi-co · tri-bi-tri · co-bi-co · bi-tri-bi · bi-co-bi · bi-tri-bi | eight-cycle 1-9-5-13-4-12-8-16, spiraling the other hand | eight-cycle 2-15-7-11-3-14-6-10, itself |

**One self, momentary by momentary.**

| One sharing, − chained at 3 at the first momentary; offerings, momentary by momentary | At 10 | Chained at 11, the carrying at 3 at the next momentary |
|---|---|---|
| none at each momentary | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| − at each momentary | 0, 0, 0, 0, 0, 0, 0 | −, −, −, −, −, −, − |
| +, −, +, − alternating | +, −, +, −, +, − | +, −, +, −, +, − |
| + and − together at each momentary | +, −, +, −, +, − | +, −, +, −, +, − |

**A spiral of selves.**

| Number of selves, each releasing to the next at 9, the last to the first; one sharing; each self chained at a parity at the first momentary, − at self 1 and alternating along, the last and the first alike at an odd number; none offered | Self 1 at 10, momentaries 1 to 12 | Each self's releasings again at, in momentaries |
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

| Numbers of selves of two spirals, each as the spiral of selves, − at self 1 of each | Beside each other, each self's releasings again together at | Crossed, self 1 of each releasing to self 1 of the other at 10, each self's releasings again at | From momentary, the first each self's releasing comes again from | Self 1 of each | Each spiral's like pair at the first momentary, the last and the first |
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

| Torus of selves, p along · q across, each self releasing at 9 to the next along and at 10 to the next across, the last to the first; one sharing; each carrying none at the first momentary, + offered once at one self at the first momentary | Each self's releasings again at | From momentary, the first each self's releasing comes again from | Spirals of p and q beside each other, each self's releasings again together at |
|---|---|---|---|
| 1 · 3 | 3 | 3 | 12 |
| 1 · 5 | 4 | 5 | 20 |
| 3 · 3 | 12 | 8 | 12 |
| 3 · 5 | 12 | 7 | 60 |
| 3 · 7 | 7 | 9 | 84 |
| 3 · 13 | 12 | 24 | 156 |
| 5 · 7 | 20 | 14 | 140 |
| 5 · 11 | 11 | 15 | 220 |
| 7 · 17 | 17 | 23 | 476 |
| 17 · 59 | 59 | 91 | 4,012 |

**Two selves.**

| Chained at 3 at A, B at the first momentary; one sharing, none offered from beyond the two | Each receiving at 14 the other's releasing at 10 | A at 10, six momentaries | B at 10, six momentaries |
|---|---|---|---|
| +, + | both ways | −, 0, +, 0, −, 0 | −, 0, +, 0, −, 0 |
| +, + | A from B alone | −, 0, +, −, +, − | −, +, −, +, −, + |
| +, + | B from A alone | −, +, −, +, −, + | −, 0, +, −, +, − |
| +, + | neither | −, +, −, +, −, + | −, +, −, +, −, + |
| +, − | both ways | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | A from B alone | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | B from A alone | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | neither | −, +, −, +, −, + | +, −, +, −, +, − |

**Three selves in a line.**

| A's parity offered at B at the first momentary alone; one sharing; B and C each chained +; B releasing to C | B at 10 | B chained at 11, the first momentary | C at 10, momentaries 1 and 2 | C chained at 11, the second momentary |
|---|---|---|---|---|
| + | 0 | + | −, + | + |
| − | − | − | −, 0 | − |

**Colliding, at a carrying of none, at one momentary.**

| One sharing, none chained at 3; each cell at 10 · chained at 11; *is* a parity released, *is not* the 0 released, a dash none released | At 14: none | At 14: + | At 14: − | At 14: 0, a + and a − offered |
|---|---|---|---|---|
| none | — · none | is + · + | is − · − | is not · none |
