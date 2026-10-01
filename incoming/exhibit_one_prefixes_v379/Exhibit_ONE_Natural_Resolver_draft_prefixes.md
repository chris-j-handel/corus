Exhibit ONE Natural Resolver v379 · a draft at the rule of the prefixes, a proposal at incoming/, no living file

# Natural Resolver

**Stable Forms of the Discovering Method**

---

```python
"""Exhibit ONE · Natural Resolver"""


def _1_co_bi_co_offering(_3_co_bi_co_sharing, _2_bi_co_bi_offering):
    _14_bi_tri_bi_moralizing = {}
    for _4_bi_co_bi_sharing, _7_co_bi_co_corusing in _2_bi_co_bi_offering:
        if _7_co_bi_co_corusing != 0:
            _15_co_bi_tri_corusing = _14_bi_tri_bi_moralizing.get(_4_bi_co_bi_sharing)
            if _15_co_bi_tri_corusing is None:
                _14_bi_tri_bi_moralizing[_4_bi_co_bi_sharing] = 1 if _7_co_bi_co_corusing > 0 else -1
            elif (_15_co_bi_tri_corusing > 0) != (_7_co_bi_co_corusing > 0):
                _14_bi_tri_bi_moralizing[_4_bi_co_bi_sharing] = 0
    _12_bi_tri_bi_parity_changing = dict(_14_bi_tri_bi_moralizing)
    for _4_bi_co_bi_sharing, _7_co_bi_co_corusing in _3_co_bi_co_sharing:
        _15_co_bi_tri_corusing = _14_bi_tri_bi_moralizing.get(_4_bi_co_bi_sharing, 0)
        if _15_co_bi_tri_corusing != 0 and (_15_co_bi_tri_corusing > 0) == (_7_co_bi_co_corusing > 0):
            _12_bi_tri_bi_parity_changing[_4_bi_co_bi_sharing] = 0
        else:
            _12_bi_tri_bi_parity_changing[_4_bi_co_bi_sharing] = -1 if _7_co_bi_co_corusing > 0 else 1
    _10_bi_tri_bi_tunneling = list(_12_bi_tri_bi_parity_changing.items())
    _11_tri_bi_co_chaining = dict(_3_co_bi_co_sharing)
    for _4_bi_co_bi_sharing, _7_co_bi_co_corusing in _10_bi_tri_bi_tunneling:
        if _7_co_bi_co_corusing != 0:
            _11_tri_bi_co_chaining[_4_bi_co_bi_sharing] = _7_co_bi_co_corusing
    return _10_bi_tri_bi_tunneling, list(_11_tri_bi_co_chaining.items())


def _9_tri_bi_co_momentarying(_10_bi_tri_bi_tunneling, _5_co_bi_co_competencing):
    return [(_5_co_bi_co_competencing[_13_co_bi_tri_competencing], _15_co_bi_tri_corusing)
            for _13_co_bi_tri_competencing, _15_co_bi_tri_corusing in _10_bi_tri_bi_tunneling]


def _17_tri_bi_co_offering(_16_bi_tri_bi_torusing, _5_co_bi_co_competencing):
    _8_bi_co_bi_torusing = {}
    _14_bi_tri_bi_moralizing = {_13_co_bi_tri_competencing: [] for _13_co_bi_tri_competencing in _16_bi_tri_bi_torusing}
    for _13_co_bi_tri_competencing, (_3_co_bi_co_sharing, _2_bi_co_bi_offering) in _16_bi_tri_bi_torusing.items():
        _10_bi_tri_bi_tunneling, _8_bi_co_bi_torusing[_13_co_bi_tri_competencing] = _1_co_bi_co_offering(
            _3_co_bi_co_sharing, _2_bi_co_bi_offering)
        _6_bi_co_bi_moralizing = _10_bi_tri_bi_tunneling
        for _4_bi_co_bi_sharing, _15_co_bi_tri_corusing in _9_tri_bi_co_momentarying(
                [(_4_bi_co_bi_sharing, _15_co_bi_tri_corusing)
                 for _4_bi_co_bi_sharing, _15_co_bi_tri_corusing in (
                     ((_13_co_bi_tri_competencing, 6), _6_bi_co_bi_moralizing),
                     ((_13_co_bi_tri_competencing, 10), _10_bi_tri_bi_tunneling),
                     ((_13_co_bi_tri_competencing, 9), _10_bi_tri_bi_tunneling))
                 if _4_bi_co_bi_sharing in _5_co_bi_co_competencing],
                _5_co_bi_co_competencing):
            _14_bi_tri_bi_moralizing[_4_bi_co_bi_sharing].extend(_15_co_bi_tri_corusing)
    return {_13_co_bi_tri_competencing: (_8_bi_co_bi_torusing[_13_co_bi_tri_competencing],
                                           _14_bi_tri_bi_moralizing[_13_co_bi_tri_competencing])
            for _13_co_bi_tri_competencing in _16_bi_tri_bi_torusing}

CONNECTORS = {
    2: ('2-bi-co-bi-offering', 'bi-moral-so-far', 'arriving'),
    6: ('6-bi-co-bi-moralizing', 'not-yet-bi-moral', 'releasing'),
    9: ('9-tri-bi-co-momentarying', 'not-yet-co-competent', 'along'),
    10: ('10-bi-tri-bi-tunneling', 'not-yet-bi-moral', 'releasing'),
    14: ('14-bi-tri-bi-moralizing', 'bi-moral-so-far', 'arriving'),
    17: ('17-tri-bi-co-offering', 'co-competent-so-far', 'along'),
}
JOINS = {10: 14, 6: 2, 17: 9, 9: 17}
```

```text
                        the self at co-competent-so-far, its 9
                                      ▲
                                      ║ 17  along · co
      ┌───────────────────────────────╨───────────────────────────────┐
      │                          1  entry                             │
      │                                                               │
      │  14i ◄──────────────────────────────────────────── 2 · 14 ◄══════
      │   │   offerings surfacing at each sharing: +, − or 0          │
      │   ▼                                                           │
      │   3o ─────► 12i ────────► 10 ──► released, with 6             │
      │   4o · 7o   changing,     + or −: is                          │
      │   carrying  is or is not  0: the between                      │
      │                           │                                   │
      │                           ├──────► 11i ─────► 3o, next        │
      │                           │        chaining   momentary       │
      │                           │                                   │
      │                           └──────► 9 ────► 5o                 │
      │                                    13i · 15i                  │
 ◄══════ 6 · 10                                                       │
      │   8o carrying wound · 16i society wound                       │
      └───────────────────────────────╥───────────────────────────────┘
                                      ║ 9  along · co
                                      ▼
                        the self at not-yet-co-competent, its 17

   at not-yet-bi-moral   6  ══► its 2        10 ══► its 14      outgoing
   at bi-moral-so-far    its 6  ══► 2        its 10 ══► 14      incoming
   ═══ between selves, across and along    ─── within one self
   o outward face    i inward face
```

| n | Name | Parity, opens | From, to, the opening side first | Entry, connector or face | Across or along | Outward or inward | Facing | Joining | At the code |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1-co-bi-co-offering | odd, co | self, other | entry | — | — | — | — | the entry: 3 and 2 in; 10 and 11 out |
| 2 | 2-bi-co-bi-offering | even, bi | other, self | connector | across | — | bi-moral-so-far | from the self at bi-moral-so-far, its 6 | the offerings, each sharing with its parity |
| 3 | 3-co-bi-co-sharing | odd, co | self, other | face | — | outward | — | — | the carrying: each sharing, 4, with its parity, 7 |
| 4 | 4-bi-co-bi-sharing | even, bi | other, self | face | — | outward | — | — | each sharing; at the society, each self at 6, 10 and 9 |
| 5 | 5-co-bi-co-competencing | odd, co | self, other | face | — | outward | — | — | each sharing's receiving sharing; at the society, the joins |
| 6 | 6-bi-co-bi-moralizing | even, bi | other, self | connector | across | — | not-yet-bi-moral | to the self at not-yet-bi-moral, its 2 | the changing released at not-yet-bi-moral, at that self's 2 |
| 7 | 7-co-bi-co-corusing | odd, co | self, other | face | — | outward | — | — | each parity, offered and chained |
| 8 | 8-bi-co-bi-torusing | even, bi | other, self | face | — | outward | — | — | each self's carrying wound, its 11 the next momentary's 3 |
| 9 | 9-tri-bi-co-momentarying | odd, co | social, other, self | connector | along | — | not-yet-co-competent | with the self at not-yet-co-competent, its 17 | each changing to its receiving sharing, 5 |
| 10 | 10-bi-tri-bi-tunneling | even, bi | other, social, self | connector | across | — | not-yet-bi-moral | to the self at not-yet-bi-moral, its 14 | each sharing's changing: + or − is, 0 the between |
| 11 | 11-tri-bi-co-chaining | odd, co | social, other, self | face | — | inward | — | — | the carrying chained, each changing the next prior |
| 12 | 12-bi-tri-bi-parity-changing | even, bi | other, social, self | face | — | inward | — | — | each sharing's changing, is or is not |
| 13 | 13-co-bi-tri-competencing | odd, co | social, other | face | — | inward | — | — | each releasing sharing; at the society, each releasing self |
| 14 | 14-bi-tri-bi-moralizing | even, bi | other, social | connector | across | — | bi-moral-so-far | from the self at bi-moral-so-far, its 10 | the offerings surfacing at each sharing: +, − or 0; at the society, each self's offerings next |
| 15 | 15-co-bi-tri-corusing | odd, co | social, other | face | — | inward | — | — | the parity carried along at 9 |
| 16 | 16-bi-tri-bi-torusing | even, bi | other, social | face | — | inward | — | — | the society wound: each self's 8 and offerings |
| 17 | 17-tri-bi-co-offering | odd, co | social, self | connector | along | — | co-competent-so-far | with the self at co-competent-so-far, its 9 | the society's next momentary: each self's 1, then 9 at 6, 10 and 9 |

| n | The name whole, at each of its relations among the forms |
|---|---|
| 1 | **1-co-bi-co-offering**; odd, opening co, the self opening it, its sides self, other; the entry, once for one self at one momentary, the self offering itself to the coupling; root offering with 2-bi-co-bi-offering and 17-tri-bi-co-offering; 8 up 9-tri-bi-co-momentarying, the parity continuing; 9 less, the podal within 1 to 8, 8-bi-co-bi-torusing; 17 less, the podal within 1 to 16, 16-bi-tri-bi-torusing; on the four-cycle 1-9-8-16, root torusing, hand co co bi bi, going 8 up first from 1-co-bi-co-offering, from 16-bi-tri-bi-torusing to it and on to 9-tri-bi-co-momentarying, spiraling the other hand with 2-15-7-10; on the six-cycle 1-9-5-12-8-16; on the eight-cycle 1-9-5-13-4-12-8-16; at the momentaries of exchanging the first of the self's four, opening at 1, self 1–2; at the five dimensions 1 self prior, the prior opening of the self's five; at the namings 1-2, bi-momentarying, the self's entry, odd, and the others' offerings, even, one momentary at each side; at the self's three faces the bi-moral self with 2, bi-momentarying, the offering self to other and other to self, across; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other; prior and next: once for one self at one momentary, the three steps within it 14, 12, 10 with 11; at the 1–17s inward 1 of the 1st 1–17, the entry, and at the 1–17 outward 1, the entry; at the code the entry: 3 and 2 in; 10 and 11 out. |
| 2 | **2-bi-co-bi-offering**; even, opening bi, the other opening it, its sides other, self; a connector, across, facing bi-moral-so-far, arriving, its join from the self at bi-moral-so-far, its 6; root offering with 1-co-bi-co-offering and 17-tri-bi-co-offering; 8 up 10-bi-tri-bi-tunneling, the parity continuing; 9 less, the podal within 1 to 8, 7-co-bi-co-corusing; 17 less, the podal within 1 to 16, 15-co-bi-tri-corusing; on the four-cycle 2-15-7-10, root corusing, hand bi co co bi, going 17 less first from 2-bi-co-bi-offering, from 10-bi-tri-bi-tunneling to it and on to 15-co-bi-tri-corusing, spiraling the other hand with 1-9-8-16 and 3-11-6-14; on the six-cycle 2-15-7-11-6-10; on the eight-cycle 2-15-7-11-3-14-6-10; the one move carrying 2 along 2-15-7-10; at the momentaries of exchanging the first of the self's four, at 2, the self's 1–2 completing and the other's 2–3 opening; at the five dimensions 2 other prior, the prior completing of the self's five and the prior opening of the other's; at the namings 1-2, bi-momentarying; at the self's three faces the bi-moral self with 1, across; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again; a bi-coupling outward, at the between, each other's releasing, offered to the self; the other's winding, 6 to 2, wound on at 8; at parity's face a dot of the unit square, its diagonal with 14 the facing bi-moral-so-far, its edge with 6 the join 6 to 2; prior and next: the others' releasings of their prior momentary, arriving now, the possible, carrying none of the prior; at the 1–17s inward 9 of the 1st, along, odd, co, and at the 1–17 outward within 1 to 2; at the code the offerings, each sharing with its parity. |
| 3 | **3-co-bi-co-sharing**; odd, opening co, the self opening it, its sides self, other; a face outward, at the between, before 10 in the co-sequencing, at competency's parity, odd; root sharing with 4-bi-co-bi-sharing; 8 up 11-tri-bi-co-chaining, the parity continuing; 9 less, the podal within 1 to 8, 6-bi-co-bi-moralizing; 17 less, the podal within 1 to 16, 14-bi-tri-bi-moralizing; on the four-cycle 3-11-6-14, root moralizing, hand co co bi bi, going 8 up first from 3-co-bi-co-sharing, from 14-bi-tri-bi-moralizing to it and on to 11-tri-bi-co-chaining, spiraling the other hand with 4-13-5-12 and 2-15-7-10; on the six-cycle 3-11-7-10-6-14; on the eight-cycle 2-15-7-11-3-14-6-10; at the momentaries of exchanging the first of the self's four completing at 3, the other's 2–3, and the second opening at 3, self 3–4; at the five dimensions 3 co-momentarying now, the now opening of the self's five; at the namings 3-4, co-intelligencing, at each sharing 4 the carrying at 3 coupling with the offerings surfaced at 14, next discovered, chained at 11; at the self's three faces the invisible intelligencing method, the rotation 3, 6, 5, 4, out at 3; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other; prior and next: the prior carried, the self's own, each sharing with its parity, the next momentary's continuing of 11; at the 1–17s inward 17 of the 1st and 1 of the 2nd, along, odd, co, and at the 1–17 outward within 1 to 2; at the code the carrying: each sharing, 4, with its parity, 7. |
| 4 | **4-bi-co-bi-sharing**; even, opening bi, the other opening it, its sides other, self; a face outward, at the between, before 10 in the co-sequencing, at morality's parity, even; root sharing with 3-co-bi-co-sharing; 8 up 12-bi-tri-bi-parity-changing, the parity continuing; 9 less, the podal within 1 to 8, 5-co-bi-co-competencing; 17 less, the podal within 1 to 16, 13-co-bi-tri-competencing; on the four-cycle 4-13-5-12, root competencing, hand bi co co bi, going 17 less first from 4-bi-co-bi-sharing, from 12-bi-tri-bi-parity-changing to it and on to 13-co-bi-tri-competencing, spiraling the other hand with 3-11-6-14; on the six-cycle 4-13-5-9-8-12; on the eight-cycle 1-9-5-13-4-12-8-16; the one move carrying 4 along 4-13-5-12; at the momentaries of exchanging the second of the self's four, at 4, the self's 3–4 completing and the other's 4–5 opening; at the five dimensions 4 bi-momentarying now, the now completing of the self's five; at the namings 3-4, co-intelligencing; at the self's three faces the invisible intelligencing method, the rotation 3, 6, 5, 4, in at 4, into the self's own corus at 4; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again; a bi-coupling outward, at the between, the whole ordering between self and other; prior and next: now, each sharing at which the prior couples with the now; at the 1–17s inward 9 of the 2nd, along, odd, co, and at the 1–17 outward within 1 to 2; at the code each sharing; at the society, each self at 6, 10 and 9. |
| 5 | **5-co-bi-co-competencing**; odd, opening co, the self opening it, its sides self, other; a face outward, at the between, before 10 in the co-sequencing, at competency's parity, odd; root competencing with 13-co-bi-tri-competencing; 8 up 13-co-bi-tri-competencing, the parity continuing; 9 less, the podal within 1 to 8, 4-bi-co-bi-sharing; 17 less, the podal within 1 to 16, 12-bi-tri-bi-parity-changing; on the four-cycle 4-13-5-12, root competencing, hand bi co co bi, going 17 less first from 4-bi-co-bi-sharing, from 13-co-bi-tri-competencing to it and on to 12-bi-tri-bi-parity-changing, spiraling the other hand with 3-11-6-14; on the middle four-cycle 9-5-12-8; on the six-cycle 1-9-5-12-8-16; on the six-cycle 4-13-5-9-8-12; on the eight-cycle 1-9-5-13-4-12-8-16; at the momentaries of exchanging the second of the self's four completing at 5, the other's 4–5, and the third opening at 5, self 5–6; at the five dimensions 5 self next, the next opening of the self's five; at the namings 5, co-competencing, the joins, owned by neither, each release to its receiving sharing; at the self's three faces the invisible intelligencing method, the rotation 3, 6, 5, 4, out at 5; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other; prior and next: next, each release to its receiving sharing; at the 1–17s inward 17 of the 2nd and 1 of the 3rd, along, odd, co, and at the 1–17 outward within 1 to 2; at the code each sharing's receiving sharing; at the society, the joins. |
| 6 | **6-bi-co-bi-moralizing**; even, opening bi, the other opening it, its sides other, self; a connector, across, facing not-yet-bi-moral, releasing, its join to the self at not-yet-bi-moral, its 2; root moralizing with 14-bi-tri-bi-moralizing; 8 up 14-bi-tri-bi-moralizing, the parity continuing; 9 less, the podal within 1 to 8, 3-co-bi-co-sharing; 17 less, the podal within 1 to 16, 11-tri-bi-co-chaining; on the four-cycle 3-11-6-14, root moralizing, hand co co bi bi, going 8 up first from 3-co-bi-co-sharing, from 11-tri-bi-co-chaining to it and on to 14-bi-tri-bi-moralizing, spiraling the other hand with 4-13-5-12 and 2-15-7-10; on the middle four-cycle 7-11-6-10; on the six-cycle 2-15-7-11-6-10; on the six-cycle 3-11-7-10-6-14; on the eight-cycle 2-15-7-11-3-14-6-10; the one move carrying 6 along 3-11-6-14; at the momentaries of exchanging the third of the self's four, at 6, the self's 5–6 completing and the other's 6–7 opening; at the namings 6, bi-moralizing, each changing released across, to the other's 2; at the self's three faces the invisible intelligencing method, the rotation 3, 6, 5, 4, in at 6; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again; a bi-coupling outward, at the between, the other's moralizing to the self, each changing released across; the other's winding, 6 to 2, wound on at 8; at parity's face a dot of the unit square, its diagonal with 10 the facing not-yet-bi-moral, its edge with 2 the join 6 to 2; prior and next: the changing released, the other's next offering at its 2; at the 1–17s inward 9 of the 3rd, along, odd, co, and at the 1–17 outward within 1 to 2; at the code the changing released at not-yet-bi-moral, at that self's 2. |
| 7 | **7-co-bi-co-corusing**; odd, opening co, the self opening it, its sides self, other; a face outward, at the between, before 10 in the co-sequencing, at competency's parity, odd; root corusing with 15-co-bi-tri-corusing; 8 up 15-co-bi-tri-corusing, the parity continuing; 9 less, the podal within 1 to 8, 2-bi-co-bi-offering; 17 less, the podal within 1 to 16, 10-bi-tri-bi-tunneling; on the four-cycle 2-15-7-10, root corusing, hand bi co co bi, going 17 less first from 2-bi-co-bi-offering, from 15-co-bi-tri-corusing to it and on to 10-bi-tri-bi-tunneling, spiraling the other hand with 1-9-8-16 and 3-11-6-14; on the middle four-cycle 7-11-6-10; on the six-cycle 2-15-7-11-6-10; on the six-cycle 3-11-7-10-6-14; on the eight-cycle 2-15-7-11-3-14-6-10; at the momentaries of exchanging the third of the self's four completing at 7, the other's 6–7, and the fourth opening at 7, self 7–8; at the self's three faces the co-competent self with 8, corusing, along; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other, its root corusing going in and out at the even, the other parity from its opening; prior and next: each parity, offered now and chained prior; at the 1–17s inward 17 of the 3rd and 1 of the 4th, along, odd, co, and at the 1–17 outward within 1 to 2; at the code each parity, offered and chained. |
| 8 | **8-bi-co-bi-torusing**; even, opening bi, the other opening it, its sides other, self; a face outward, at the between, before 10 in the co-sequencing, at morality's parity, even; root torusing with 16-bi-tri-bi-torusing; 8 up 16-bi-tri-bi-torusing, the parity continuing; 9 less, the podal within 1 to 8, 1-co-bi-co-offering; 17 less, the podal within 1 to 16, 9-tri-bi-co-momentarying; on the four-cycle 1-9-8-16, root torusing, hand co co bi bi, going 8 up first from 1-co-bi-co-offering, from 9-tri-bi-co-momentarying to it and on to 16-bi-tri-bi-torusing, spiraling the other hand with 2-15-7-10; on the middle four-cycle 9-5-12-8; on the six-cycle 1-9-5-12-8-16; on the six-cycle 4-13-5-9-8-12; on the eight-cycle 1-9-5-13-4-12-8-16; the one move carrying 8 along 1-9-8-16; at the momentaries of exchanging the fourth of the self's four, at 8, the self's 7–8 completing and the other's 8–9 opening; at the self's three faces the co-competent self with 7, torusing, along; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again, its root torusing going in and out at the odd, the other parity from its opening; a bi-coupling outward, at the between, the carrying winding to its sharing again; the other's winding wound on at 8; prior and next: the carrying wound, chained at 11 this momentary and the next momentary's 3; at the 1–17s inward 9 of the 4th, along, odd, co, and at the 1–17 outward within 1 to 2; at the code each self's carrying wound, its 11 the next momentary's 3. |
| 9 | **9-tri-bi-co-momentarying**; odd, opening co, the society opening it, its sides social, other, self; a connector, along, facing not-yet-co-competent, its join with the self at not-yet-co-competent, its 17; root momentarying, one name; 8 up 17-tri-bi-co-offering, the parity continuing; 8 down 1-co-bi-co-offering; 17 less, the podal within 1 to 16, 8-bi-co-bi-torusing; on the four-cycle 1-9-8-16, root torusing, hand co co bi bi, going 8 up first from 1-co-bi-co-offering, from 1-co-bi-co-offering to it and on to 8-bi-co-bi-torusing, spiraling the other hand with 2-15-7-10; on the middle four-cycle 9-5-12-8; on the six-cycle 1-9-5-12-8-16; on the six-cycle 4-13-5-9-8-12; on the eight-cycle 1-9-5-13-4-12-8-16; at the momentaries of exchanging the fourth of the self's four completing at 9, the other's 8–9, and the first of the society's four, 9 to 11, opening at 9; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other; the self's winding, 9 to 17, wound on at 17; at parity's face a unit triangle, along, joined both ways with 17; prior and next: the next prior, each changing carried along into the next momentary, releasing nothing; at the 1–17s inward 17 of the 4th and 1 of the 5th, along, odd, co, and at the 1–17 outward 2, across, even, bi; at the code each changing to its receiving sharing, 5. |
| 10 | **10-bi-tri-bi-tunneling**; even, opening bi, the other opening it, its sides other, social, self; a connector, across, facing not-yet-bi-moral, releasing, its join to the self at not-yet-bi-moral, its 14; root tunneling, one name; 8 down 2-bi-co-bi-offering; 17 less, the podal within 1 to 16, 7-co-bi-co-corusing; on the four-cycle 2-15-7-10, root corusing, hand bi co co bi, going 17 less first from 2-bi-co-bi-offering, from 7-co-bi-co-corusing to it and on to 2-bi-co-bi-offering, spiraling the other hand with 1-9-8-16 and 3-11-6-14; on the middle four-cycle 7-11-6-10; on the six-cycle 2-15-7-11-6-10; on the six-cycle 3-11-7-10-6-14; on the eight-cycle 2-15-7-11-3-14-6-10; at the momentaries of exchanging the first of the society's four, at 10, 9–10 completing and 10–11 opening; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again; a bi-coupling inward, 8 up, the self among other-selves; the society's winding, 10 to 14, wound on at 16; at parity's face a dot of the unit square, its diagonal with 6 the facing not-yet-bi-moral, its edge with 14 the join 10 to 14; prior and next: the changing released across now, the other's offering next, the possible; at the 1–17s inward 9 of the 5th, along, odd, co, and at the 1–17 outward within 2 to 3; at the code each sharing's changing: + or − is, 0 the between. |
| 11 | **11-tri-bi-co-chaining**; odd, opening co, the society opening it, its sides social, other, self; a face inward, after 10 in the co-sequencing, 8 up from its outward face 3-co-bi-co-sharing, at competency's parity, odd; root chaining, one name; 8 down 3-co-bi-co-sharing; 17 less, the podal within 1 to 16, 6-bi-co-bi-moralizing; on the four-cycle 3-11-6-14, root moralizing, hand co co bi bi, going 8 up first from 3-co-bi-co-sharing, from 3-co-bi-co-sharing to it and on to 6-bi-co-bi-moralizing, spiraling the other hand with 4-13-5-12 and 2-15-7-10; on the middle four-cycle 7-11-6-10; on the six-cycle 2-15-7-11-6-10; on the six-cycle 3-11-7-10-6-14; on the eight-cycle 2-15-7-11-3-14-6-10; at the momentaries of exchanging the first of the society's four, 9 to 11, completing at 11, and the second, 11 to 13, opening at 11; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other; prior and next: the next prior, the carrying chained, continuing as 3 at the next momentary; at the 1–17s inward 17 of the 5th and 1 of the 6th, along, odd, co, and at the 1–17 outward within 2 to 3; at the code the carrying chained, each changing the next prior. |
| 12 | **12-bi-tri-bi-parity-changing**; even, opening bi, the other opening it, its sides other, social, self; a face inward, after 10 in the co-sequencing, 8 up from its outward face 4-bi-co-bi-sharing, at morality's parity, even; root parity-changing, one name; 8 down 4-bi-co-bi-sharing; 17 less, the podal within 1 to 16, 5-co-bi-co-competencing; on the four-cycle 4-13-5-12, root competencing, hand bi co co bi, going 17 less first from 4-bi-co-bi-sharing, from 5-co-bi-co-competencing to it and on to 4-bi-co-bi-sharing, spiraling the other hand with 3-11-6-14; on the middle four-cycle 9-5-12-8; on the six-cycle 1-9-5-12-8-16; on the six-cycle 4-13-5-9-8-12; on the eight-cycle 1-9-5-13-4-12-8-16; at the momentaries of exchanging the second of the society's four, at 12, 11–12 completing and 12–13 opening; at the namings the shape of the unrelationing surface, each sharing's changing, is or is not; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again; a bi-coupling inward, 8 up, changing at bi-coupling, the self in society; prior and next: now, the changing, is or is not, prior and now coupled; at the 1–17s inward 9 of the 6th, along, odd, co, and at the 1–17 outward within 2 to 3; at the code each sharing's changing, is or is not. |
| 13 | **13-co-bi-tri-competencing**; odd, opening co, the society opening it, its sides social, other; a face inward, after 10 in the co-sequencing, 8 up from its outward face 5-co-bi-co-competencing, at competency's parity, odd; root competencing with 5-co-bi-co-competencing; 8 down 5-co-bi-co-competencing; 17 less, the podal within 1 to 16, 4-bi-co-bi-sharing; on the four-cycle 4-13-5-12, root competencing, hand bi co co bi, going 17 less first from 4-bi-co-bi-sharing, from 4-bi-co-bi-sharing to it and on to 5-co-bi-co-competencing, spiraling the other hand with 3-11-6-14; on the six-cycle 4-13-5-9-8-12; on the eight-cycle 1-9-5-13-4-12-8-16; at the momentaries of exchanging the second of the society's four, 11 to 13, completing at 13, and the third, 13 to 15, opening at 13; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other; prior and next: each releasing sharing, and at the society each releasing self; at the 1–17s inward 17 of the 6th and 1 of the 7th, along, odd, co, and at the 1–17 outward within 2 to 3; at the code each releasing sharing; at the society, each releasing self. |
| 14 | **14-bi-tri-bi-moralizing**; even, opening bi, the other opening it, its sides other, social; a connector, across, facing bi-moral-so-far, arriving, its join from the self at bi-moral-so-far, its 10; root moralizing with 6-bi-co-bi-moralizing; 8 down 6-bi-co-bi-moralizing; 17 less, the podal within 1 to 16, 3-co-bi-co-sharing; on the four-cycle 3-11-6-14, root moralizing, hand co co bi bi, going 8 up first from 3-co-bi-co-sharing, from 6-bi-co-bi-moralizing to it and on to 3-co-bi-co-sharing, spiraling the other hand with 4-13-5-12 and 2-15-7-10; on the six-cycle 3-11-7-10-6-14; on the eight-cycle 2-15-7-11-3-14-6-10; at the momentaries of exchanging the third of the society's four, at 14, 13–14 completing and 14–15 opening; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again; a bi-coupling inward, 8 up, the offerings surfacing, the self's own inverting, morality; the society's winding, 10 to 14, wound on at 16; at parity's face a dot of the unit square, its diagonal with 2 the facing bi-moral-so-far, its edge with 10 the join 10 to 14; prior and next: now, the offerings surfacing, the others' prior momentary at the self's now; at the 1–17s inward 9 of the 7th, along, odd, co, and at the 1–17 outward within 2 to 3; at the code the offerings surfacing at each sharing: +, − or 0; at the society, each self's offerings next. |
| 15 | **15-co-bi-tri-corusing**; odd, opening co, the society opening it, its sides social, other; a face inward, after 10 in the co-sequencing, 8 up from its outward face 7-co-bi-co-corusing, at competency's parity, odd; root corusing with 7-co-bi-co-corusing; 8 down 7-co-bi-co-corusing; 17 less, the podal within 1 to 16, 2-bi-co-bi-offering; on the four-cycle 2-15-7-10, root corusing, hand bi co co bi, going 17 less first from 2-bi-co-bi-offering, from 2-bi-co-bi-offering to it and on to 7-co-bi-co-corusing, spiraling the other hand with 1-9-8-16 and 3-11-6-14; on the six-cycle 2-15-7-11-6-10; on the eight-cycle 2-15-7-11-3-14-6-10; at the momentaries of exchanging the third of the society's four, 13 to 15, completing at 15, and the fourth, 15 to 17, opening at 15; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other, its root corusing going in and out at the even, the other parity from its opening; prior and next: the parity carried along at 9, the next prior; at the 1–17s inward 17 of the 7th and 1 of the 8th, along, odd, co, and at the 1–17 outward within 2 to 3; at the code the parity carried along at 9. |
| 16 | **16-bi-tri-bi-torusing**; even, opening bi, the other opening it, its sides other, social; a face inward, after 10 in the co-sequencing, 8 up from its outward face 8-bi-co-bi-torusing, at morality's parity, even; root torusing with 8-bi-co-bi-torusing; 8 down 8-bi-co-bi-torusing; 17 less, the podal within 1 to 16, 1-co-bi-co-offering; on the four-cycle 1-9-8-16, root torusing, hand co co bi bi, going 8 up first from 1-co-bi-co-offering, from 8-bi-co-bi-torusing to it and on to 1-co-bi-co-offering, spiraling the other hand with 2-15-7-10; on the six-cycle 1-9-5-12-8-16; on the eight-cycle 1-9-5-13-4-12-8-16; at the momentaries of exchanging the fourth of the society's four, at 16, 15–16 completing and 16–17 opening; in and out at its parity, corusing, even, through the small opening, the long way round, bi-tri-exchanging, the self reaching its own side again, its root torusing going in and out at the odd, the other parity from its opening; a bi-coupling inward, 8 up, competency asymmetry sustaining the coupling, the society winding to the self again; the society's winding wound on at 16; prior and next: the society wound now, each self's 8 and its offerings next; at the 1–17s inward 9 of the 8th, along, odd, co, and at the 1–17 outward within 2 to 3; at the code the society wound: each self's 8 and offerings. |
| 17 | **17-tri-bi-co-offering**; odd, opening co, the society opening it, its sides social, self; a connector, along, facing co-competent-so-far, its join with the self at co-competent-so-far, its 9; root offering with 1-co-bi-co-offering and 2-bi-co-bi-offering; 8 down 9-tri-bi-co-momentarying; at the momentaries of exchanging the fourth of the society's four, 15 to 17, completing at 17, the next 1; in and out at its parity, torusing, odd, through the large opening, the tunnel, bi-exchanging with a particular other; the self's winding, 9 to 17, wound on at 17; at parity's face a unit triangle, along, joined both ways with 9; prior and next: the society's next momentary, the next now, each self's 1 then 9 at 6, 10 and 9; at the 1–17s inward 17 of the 8th and 1 of the 9th, along, odd, co, and at the 1–17 outward 3, the face outward, odd, co; at the code the society's next momentary: each self's 1, then 9 at 6, 10 and 9. |

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
| parity-changing | 12 |

| Names | Naming | At the code |
|---|---|---|
| 1-co-bi-co-offering · 2-bi-co-bi-offering | bi-momentarying | the self's entry, odd, and the others' offerings, even, one momentary at each side |
| 3-co-bi-co-sharing · 4-bi-co-bi-sharing | co-intelligencing | at each sharing 4 the carrying at 3 couples with the offerings surfaced at 14: next discovered, chained at 11 |
| 5-co-bi-co-competencing | co-competencing | the joins, owned by neither: each release to its receiving sharing |
| 1 · 2 · 3 · 4 · 5, each alone | the five dimensions | 1 self prior, the self, the one living carrying, its prior at 3 a formed set it carries into now; 2 other prior, the other selves' offerings of their prior momentary arriving, released at 6 and 10 and carried along at 9; 3 co-momentarying now, the same living carrying at now, and 4 bi-momentarying now, each sharing, the offerings surfaced at 14 arriving at it, now; 5 self next, each release to its receiving sharing next |
| 6-bi-co-bi-moralizing | bi-moralizing | each changing released across, to the other's 2 |
| 12-bi-tri-bi-parity-changing | the shape of the unrelationing surface | each sharing's changing, is or is not |
| 1 to 9 | bi-coupling | the function 1, at the names 1, 2, 3, 4, 7, 10, 11, 12, 14 and 15, the self and the other at one coupling; 1 to 9 the bi-coupling among the names, 9 at its end reads bi-co-releasing, the release 10 makes |
| 1 to 17 | bi-trupling | the function 17, at the names of the function 1 with 5, 6, 8, 9, 13, 16 and 17, the self, the other and the society; 9 at its waist, tri-bi-co-momentarying, joined both ways with 17; the protocol's two sides, the odd along at 9 and 17 and the even across at 6 to 2 and 10 to 14 |
| 1 to 17, stable-forming | bi-tri-volutioning | at no one line: each momentary's carrying the next momentary's |
| 2 · 6 · 14 · 10 · 9 · 17 | parity's face | a unit square of four dots, 2, 6, 14 and 10, its empty centre the between: its two parallel edges the across joins, 6 to 2 and 10 to 14; its diagonals the facings, 2 and 14 bi-moral-so-far and 6 and 10 not-yet-bi-moral; and two unit triangles, 9 and 17, along, joined both ways |

| Four-cycle, 8 up and 17 less | Root at the self and at the society | Hand at the names |
|---|---|---|
| 1-9-8-16 | torusing, 8 and 16 | spiraling the other hand with 2-15-7-10 |
| 2-15-7-10 | corusing, 7 and 15 | spiraling the other hand with 1-9-8-16 and 3-11-6-14 |
| 3-11-6-14 | moralizing, 6 and 14 | spiraling the other hand with 4-13-5-12 and 2-15-7-10 |
| 4-13-5-12 | competencing, 5 and 13 | spiraling the other hand with 3-11-6-14 |

| Winding | Joining | Wound on at | Across or along |
|---|---|---|---|
| the other's | 6 to 2 | 8 | across, not-yet-bi-moral to bi-moral-so-far |
| the society's | 10 to 14 | 16 | across, not-yet-bi-moral to bi-moral-so-far |
| the self's | 9 to 17 | 17 | along, not-yet-co-competent to co-competent-so-far |

| n | Name | At this 1–17 | At the 1–17s inward, n at 8n − 7 | At the 1–17 outward, 8m − 7 at m |
|---|---|---|---|---|
| 1 | 1-co-bi-co-offering | entry, odd, co | 1 of the 1st: entry, odd, co | 1: entry, odd, co |
| 2 | 2-bi-co-bi-offering | across, even, bi | 9 of the 1st: along, odd, co | within 1 to 2 |
| 3 | 3-co-bi-co-sharing | face outward, odd, co | 17 of the 1st, 1 of the 2nd: along, odd, co | within 1 to 2 |
| 4 | 4-bi-co-bi-sharing | face outward, even, bi | 9 of the 2nd: along, odd, co | within 1 to 2 |
| 5 | 5-co-bi-co-competencing | face outward, odd, co | 17 of the 2nd, 1 of the 3rd: along, odd, co | within 1 to 2 |
| 6 | 6-bi-co-bi-moralizing | across, even, bi | 9 of the 3rd: along, odd, co | within 1 to 2 |
| 7 | 7-co-bi-co-corusing | face outward, odd, co | 17 of the 3rd, 1 of the 4th: along, odd, co | within 1 to 2 |
| 8 | 8-bi-co-bi-torusing | face outward, even, bi | 9 of the 4th: along, odd, co | within 1 to 2 |
| 9 | 9-tri-bi-co-momentarying | along, odd, co | 17 of the 4th, 1 of the 5th: along, odd, co | 2: across, even, bi |
| 10 | 10-bi-tri-bi-tunneling | across, even, bi | 9 of the 5th: along, odd, co | within 2 to 3 |
| 11 | 11-tri-bi-co-chaining | face inward, odd, co | 17 of the 5th, 1 of the 6th: along, odd, co | within 2 to 3 |
| 12 | 12-bi-tri-bi-parity-changing | face inward, even, bi | 9 of the 6th: along, odd, co | within 2 to 3 |
| 13 | 13-co-bi-tri-competencing | face inward, odd, co | 17 of the 6th, 1 of the 7th: along, odd, co | within 2 to 3 |
| 14 | 14-bi-tri-bi-moralizing | across, even, bi | 9 of the 7th: along, odd, co | within 2 to 3 |
| 15 | 15-co-bi-tri-corusing | face inward, odd, co | 17 of the 7th, 1 of the 8th: along, odd, co | within 2 to 3 |
| 16 | 16-bi-tri-bi-torusing | face inward, even, bi | 9 of the 8th: along, odd, co | within 2 to 3 |
| 17 | 17-tri-bi-co-offering | along, odd, co | 17 of the 8th, 1 of the 9th: along, odd, co | 3: face outward, odd, co |

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

| Side | Prior opening | Prior completing | Now opening | Now completing | Next opening | Its five |
|---|---|---|---|---|---|---|
| self, at 1 | 1 | 2 | 3 | 4 | 5 | co bi co bi co |
| other, at 2 | 2 | 3 | 4 | 5 | 6 | bi co bi co bi |
| self next, at 3 | 3 | 4 | 5 | 6 | 7 | co bi co bi co |

| Momentary of exchanging | Self | Other | Names | Relation |
|---|---|---|---|---|
| first | 1–2 | 2–3 | 1-co-bi-co-offering · 2-bi-co-bi-offering · 3-co-bi-co-sharing | self/other |
| second | 3–4 | 4–5 | 3-co-bi-co-sharing · 4-bi-co-bi-sharing · 5-co-bi-co-competencing | self/other to other/self |
| third | 5–6 | 6–7 | 5-co-bi-co-competencing · 6-bi-co-bi-moralizing · 7-co-bi-co-corusing | other/self |
| fourth | 7–8 | 8–9 | 7-co-bi-co-corusing · 8-bi-co-bi-torusing · 9-tri-bi-co-momentarying | other/self to other/social |

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

| Chained at 3; each cell at 10 · chained at 11 | At 14: none | At 14: + | At 14: − | At 14: 0 |
|---|---|---|---|---|
| none | — · none | is + · + | is − · − | is not · none |
| + | is − · − | is not · + | is − · − | is − · − |
| − | is + · + | is + · + | is not · − | is + · + |

| Outward, at the between | Bi-coupling | Inward, 8 up | Bi-coupling |
|---|---|---|---|
| 2-bi-co-bi-offering | each other's releasing, offered to the self | 10-bi-tri-bi-tunneling | the self among other-selves |
| 4-bi-co-bi-sharing | the whole ordering between self and other | 12-bi-tri-bi-parity-changing | changing at bi-coupling, the self in society |
| 6-bi-co-bi-moralizing | the other's moralizing to the self, each changing released across | 14-bi-tri-bi-moralizing | the offerings surfacing, the self's own inverting, morality |
| 8-bi-co-bi-torusing | the carrying winding to its sharing again | 16-bi-tri-bi-torusing | competency asymmetry sustaining the coupling, the society winding to the self again |

| Name | 8 up | 9 less, within 1 to 8 | 17 less, within 1 to 16 |
|---|---|---|---|
| 1-co-bi-co-offering | 9-tri-bi-co-momentarying | 8-bi-co-bi-torusing | 16-bi-tri-bi-torusing |
| 2-bi-co-bi-offering | 10-bi-tri-bi-tunneling | 7-co-bi-co-corusing | 15-co-bi-tri-corusing |
| 3-co-bi-co-sharing | 11-tri-bi-co-chaining | 6-bi-co-bi-moralizing | 14-bi-tri-bi-moralizing |
| 4-bi-co-bi-sharing | 12-bi-tri-bi-parity-changing | 5-co-bi-co-competencing | 13-co-bi-tri-competencing |

| Form | Names in order | Hand at the names | Partner at the odd momentaries | Partner at the even momentaries |
|---|---|---|---|---|
| four-cycle 1-9-8-16 | 1-co-bi-co-offering · 9-tri-bi-co-momentarying · 8-bi-co-bi-torusing · 16-bi-tri-bi-torusing | co co bi bi | four-cycle 2-15-7-10, spiraling the other hand | — |
| four-cycle 2-15-7-10 | 2-bi-co-bi-offering · 15-co-bi-tri-corusing · 7-co-bi-co-corusing · 10-bi-tri-bi-tunneling | bi co co bi | four-cycle 1-9-8-16, spiraling the other hand | four-cycle 3-11-6-14, spiraling the other hand |
| four-cycle 3-11-6-14 | 3-co-bi-co-sharing · 11-tri-bi-co-chaining · 6-bi-co-bi-moralizing · 14-bi-tri-bi-moralizing | co co bi bi | four-cycle 4-13-5-12, spiraling the other hand | four-cycle 2-15-7-10, spiraling the other hand |
| four-cycle 4-13-5-12 | 4-bi-co-bi-sharing · 13-co-bi-tri-competencing · 5-co-bi-co-competencing · 12-bi-tri-bi-parity-changing | bi co co bi | four-cycle 3-11-6-14, spiraling the other hand | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | 9-tri-bi-co-momentarying · 5-co-bi-co-competencing · 12-bi-tri-bi-parity-changing · 8-bi-co-bi-torusing | co co bi bi | middle four-cycle 7-11-6-10, spiraling the other hand | — |
| middle four-cycle 7-11-6-10 | 7-co-bi-co-corusing · 11-tri-bi-co-chaining · 6-bi-co-bi-moralizing · 10-bi-tri-bi-tunneling | co co bi bi | middle four-cycle 9-5-12-8, spiraling the other hand | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | 1-co-bi-co-offering · 9-tri-bi-co-momentarying · 5-co-bi-co-competencing · 12-bi-tri-bi-parity-changing · 8-bi-co-bi-torusing · 16-bi-tri-bi-torusing | co co co bi bi bi | six-cycle 2-15-7-11-6-10, spiraling the other hand | — |
| six-cycle 2-15-7-11-6-10 | 2-bi-co-bi-offering · 15-co-bi-tri-corusing · 7-co-bi-co-corusing · 11-tri-bi-co-chaining · 6-bi-co-bi-moralizing · 10-bi-tri-bi-tunneling | bi co co co bi bi | six-cycle 1-9-5-12-8-16, spiraling the other hand | six-cycle 3-11-7-10-6-14, spiraling the other hand |
| six-cycle 3-11-7-10-6-14 | 3-co-bi-co-sharing · 11-tri-bi-co-chaining · 7-co-bi-co-corusing · 10-bi-tri-bi-tunneling · 6-bi-co-bi-moralizing · 14-bi-tri-bi-moralizing | co co co bi bi bi | six-cycle 4-13-5-9-8-12, spiraling the other hand | six-cycle 2-15-7-11-6-10, spiraling the other hand |
| six-cycle 4-13-5-9-8-12 | 4-bi-co-bi-sharing · 13-co-bi-tri-competencing · 5-co-bi-co-competencing · 9-tri-bi-co-momentarying · 8-bi-co-bi-torusing · 12-bi-tri-bi-parity-changing | bi co co co bi bi | six-cycle 3-11-7-10-6-14, spiraling the other hand | — |
| eight-cycle 1-9-5-13-4-12-8-16 | 1-co-bi-co-offering · 9-tri-bi-co-momentarying · 5-co-bi-co-competencing · 13-co-bi-tri-competencing · 4-bi-co-bi-sharing · 12-bi-tri-bi-parity-changing · 8-bi-co-bi-torusing · 16-bi-tri-bi-torusing | co co co co bi bi bi bi | eight-cycle 2-15-7-11-3-14-6-10, spiraling the other hand | — |
| eight-cycle 2-15-7-11-3-14-6-10 | 2-bi-co-bi-offering · 15-co-bi-tri-corusing · 7-co-bi-co-corusing · 11-tri-bi-co-chaining · 3-co-bi-co-sharing · 14-bi-tri-bi-moralizing · 6-bi-co-bi-moralizing · 10-bi-tri-bi-tunneling | bi co co co co bi bi bi | eight-cycle 1-9-5-13-4-12-8-16, spiraling the other hand | eight-cycle 2-15-7-11-3-14-6-10, itself |

| Offerings, momentary by momentary | At 10 | Chained at 11 |
|---|---|---|
| + once, then none | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| + at each momentary | +, 0, 0, 0, 0, 0, 0 | +, +, +, +, +, +, + |
| −, +, −, + alternating | −, +, −, +, −, + | −, +, −, +, −, + |
| + once, then + and − together | +, −, +, −, +, − | +, −, +, −, +, − |

| Selves, joined along, the last to the first, + offered once at self 1 | Self 1 at 10, momentaries 1 to 12 | Parities again at each, from momentary n | None chained again |
|---|---|---|---|
| 1 | +, 0, −, 0, +, 0, −, 0, +, 0, −, 0 | 4 | is not |
| 2 | +, −, +, −, +, −, +, −, +, −, +, − | 2 | is not |
| 3 | +, −, +, 0, −, +, −, +, −, 0, +, − | 12 | is not |
| 4 | +, −, +, −, +, −, +, −, +, −, +, − | 2 | is not |
| 5 | +, −, +, −, +, 0, −, +, −, +, −, + | 20 | is not |
| 6 | +, −, +, −, +, −, +, −, +, −, +, − | 2 | is not |
| 7 | +, −, +, −, +, −, +, 0, −, +, −, + | 28 | is not |
| 8 | +, −, +, −, +, −, +, −, +, −, +, − | 2 | is not |
| 9 | +, −, +, −, +, −, +, −, +, 0, −, + | 36 | is not |
| 10 | +, −, +, −, +, −, +, −, +, −, +, − | 2 | is not |
| 11 | +, −, +, −, +, −, +, −, +, −, +, 0 | 44 | is not |
| 17 | +, −, +, −, +, −, +, −, +, −, +, − | 68 | is not |
| 59 | +, −, +, −, +, −, +, −, +, −, +, − | 236 | is not |

| Spirals, selves, + offered once at self 1 of each | Beside each other, parities again together at | Crossed at self 1 of each both ways, parities again at | From momentary | Self 1 of each | Each spiral's like pair |
|---|---|---|---|---|---|
| 2 · 3 | 12 | 2 | 7 | opposite | none · selves 3 and 1 |
| 3 · 5 | 60 | 2 | 13 | opposite | selves 3 and 1 · selves 5 and 1 |
| 5 · 7 | 140 | 2 | 20 | opposite | selves 5 and 1 · selves 7 and 1 |
| 7 · 11 | 308 | 2 | 29 | opposite | selves 7 and 1 · selves 11 and 1 |
| 11 · 13 | 572 | 2 | 37 | opposite | selves 11 and 1 · selves 13 and 1 |
| 13 · 17 | 884 | 2 | 49 | opposite | selves 13 and 1 · selves 17 and 1 |
| 17 · 59 | 4,012 | 2 | 137 | opposite | selves 17 and 1 · selves 59 and 1 |
| 9 · 15 | 180 | 2 | 41 | opposite | selves 9 and 1 · selves 15 and 1 |

| Torus of selves, p along at 9 · q across at 10 | Parities again at, one offering at self 1 | From momentary | Spirals of p and q beside each other, parities again together at |
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

| Prior at A, B | Joining | A at 10 | B at 10 |
|---|---|---|---|
| +, + | both ways | −, 0, +, 0, −, 0 | −, 0, +, 0, −, 0 |
| +, + | A from B alone | −, 0, +, −, +, − | −, +, −, +, −, + |
| +, + | B from A alone | −, +, −, +, −, + | −, 0, +, −, +, − |
| +, + | neither | −, +, −, +, −, + | −, +, −, +, −, + |
| +, − | both ways | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | A from B alone | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | B from A alone | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | neither | −, +, −, +, −, + | +, −, +, −, +, − |

| A's parity offered at B, B and C each chained + | B at 10 | B chained | C at 10, momentaries 1 and 2 | C chained |
|---|---|---|---|---|
| + | 0 | + | −, + | + |
| − | − | − | −, 0 | − |
