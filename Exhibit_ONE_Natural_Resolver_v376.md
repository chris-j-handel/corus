Exhibit ONE Natural Resolver v376

# Natural Resolver

**Stable Forms of the Discovering Method**

---

```python
"""Exhibit ONE · Natural Resolver"""


def _1_co_bi_offering(_3_co_bi_sharing, _2_bi_co_offering):
    _14_bi_tri_moralizing = {}
    for _4_bi_co_sharing, _7_co_corusing in _2_bi_co_offering:
        if _7_co_corusing != 0:
            _15_co_bi_tri_corusing = _14_bi_tri_moralizing.get(_4_bi_co_sharing)
            if _15_co_bi_tri_corusing is None:
                _14_bi_tri_moralizing[_4_bi_co_sharing] = 1 if _7_co_corusing > 0 else -1
            elif (_15_co_bi_tri_corusing > 0) != (_7_co_corusing > 0):
                _14_bi_tri_moralizing[_4_bi_co_sharing] = 0
    _12_bi_tri_parity_changing = dict(_14_bi_tri_moralizing)
    for _4_bi_co_sharing, _7_co_corusing in _3_co_bi_sharing:
        _15_co_bi_tri_corusing = _14_bi_tri_moralizing.get(_4_bi_co_sharing, 0)
        if _15_co_bi_tri_corusing != 0 and (_15_co_bi_tri_corusing > 0) == (_7_co_corusing > 0):
            _12_bi_tri_parity_changing[_4_bi_co_sharing] = 0
        else:
            _12_bi_tri_parity_changing[_4_bi_co_sharing] = -1 if _7_co_corusing > 0 else 1
    _10_bi_tri_co_tunneling = list(_12_bi_tri_parity_changing.items())
    _11_tri_bi_co_chaining = dict(_3_co_bi_sharing)
    for _4_bi_co_sharing, _7_co_corusing in _10_bi_tri_co_tunneling:
        if _7_co_corusing != 0:
            _11_tri_bi_co_chaining[_4_bi_co_sharing] = _7_co_corusing
    return _10_bi_tri_co_tunneling, list(_11_tri_bi_co_chaining.items())


def _9_tri_bi_co_momentarying(_10_bi_tri_co_tunneling, _5_co_competencing):
    return [(_5_co_competencing[_13_co_tri_competencing], _15_co_bi_tri_corusing)
            for _13_co_tri_competencing, _15_co_bi_tri_corusing in _10_bi_tri_co_tunneling]


def _17_tri_co_offering(_16_bi_co_tri_torusing, _5_co_competencing):
    _8_bi_torusing = {}
    _14_bi_tri_moralizing = {_13_co_tri_competencing: [] for _13_co_tri_competencing in _16_bi_co_tri_torusing}
    for _13_co_tri_competencing, (_3_co_bi_sharing, _2_bi_co_offering) in _16_bi_co_tri_torusing.items():
        _10_bi_tri_co_tunneling, _8_bi_torusing[_13_co_tri_competencing] = _1_co_bi_offering(
            _3_co_bi_sharing, _2_bi_co_offering)
        _6_bi_moralizing = _10_bi_tri_co_tunneling
        for _4_bi_co_sharing, _15_co_bi_tri_corusing in _9_tri_bi_co_momentarying(
                [(_4_bi_co_sharing, _15_co_bi_tri_corusing)
                 for _4_bi_co_sharing, _15_co_bi_tri_corusing in (
                     ((_13_co_tri_competencing, 6), _6_bi_moralizing),
                     ((_13_co_tri_competencing, 10), _10_bi_tri_co_tunneling),
                     ((_13_co_tri_competencing, 9), _10_bi_tri_co_tunneling))
                 if _4_bi_co_sharing in _5_co_competencing],
                _5_co_competencing):
            _14_bi_tri_moralizing[_4_bi_co_sharing].extend(_15_co_bi_tri_corusing)
    return {_13_co_tri_competencing: (_8_bi_torusing[_13_co_tri_competencing],
                                           _14_bi_tri_moralizing[_13_co_tri_competencing])
            for _13_co_tri_competencing in _16_bi_co_tri_torusing}

CONNECTORS = {
    2: ('2-bi-co-offering', 'bi-moral-so-far', 'arriving'),
    6: ('6-bi-moralizing', 'not-yet-bi-moral', 'releasing'),
    9: ('9-tri-bi-co-momentarying', 'not-yet-co-competent', 'along'),
    10: ('10-bi-tri-co-tunneling', 'not-yet-bi-moral', 'releasing'),
    14: ('14-bi-tri-moralizing', 'bi-moral-so-far', 'arriving'),
    17: ('17-tri-co-offering', 'co-competent-so-far', 'along'),
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
      │   carrying  is or is not  0: is not                           │
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

| n | Name | Parity, opens | From, to | Entry, connector or face | Across or along | Outward or inward | Facing | Joining | At the code |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1-co-bi-offering | odd, co | self, other | entry | — | — | — | — | the entry: 3 and 2 in; 10 and 11 out |
| 2 | 2-bi-co-offering | even, bi | other, self | connector | across | — | bi-moral-so-far | from the self at bi-moral-so-far, its 6 | the offerings, each sharing with its parity |
| 3 | 3-co-bi-sharing | odd, co | self, other | face | — | outward | — | — | the carrying: each sharing, 4, with its parity, 7 |
| 4 | 4-bi-co-sharing | even, bi | other, self | face | — | outward | — | — | each sharing; at the society, each self at 6, 10 and 9 |
| 5 | 5-co-competencing | odd, co | self, other | face | — | outward | — | — | each sharing's receiving sharing; at the society, the joins |
| 6 | 6-bi-moralizing | even, bi | other, self | connector | across | — | not-yet-bi-moral | to the self at not-yet-bi-moral, its 2 | the changing released at not-yet-bi-moral, at that self's 2 |
| 7 | 7-co-corusing | odd, co | self, other | face | — | outward | — | — | each parity, offered and chained |
| 8 | 8-bi-torusing | even, bi | other, self | face | — | outward | — | — | each self's carrying wound, its 11 the next momentary's 3 |
| 9 | 9-tri-bi-co-momentarying | odd, co | social, other, self | connector | along | — | not-yet-co-competent | with the self at not-yet-co-competent, its 17 | each changing to its receiving sharing, 5 |
| 10 | 10-bi-tri-co-tunneling | even, bi | other, social, self | connector | across | — | not-yet-bi-moral | to the self at not-yet-bi-moral, its 14 | each sharing's changing: + or − is, 0 is not |
| 11 | 11-tri-bi-co-chaining | odd, co | social, other, self | face | — | inward | — | — | the carrying chained, each changing the next prior |
| 12 | 12-bi-tri-parity-changing | even, bi | other, social, self | face | — | inward | — | — | each sharing's changing, is or is not |
| 13 | 13-co-tri-competencing | odd, co | social, other | face | — | inward | — | — | each releasing sharing; at the society, each releasing self |
| 14 | 14-bi-tri-moralizing | even, bi | other, social | connector | across | — | bi-moral-so-far | from the self at bi-moral-so-far, its 10 | the offerings surfacing at each sharing: +, − or 0; at the society, each self's offerings next |
| 15 | 15-co-bi-tri-corusing | odd, co | social, other | face | — | inward | — | — | the parity carried along at 9 |
| 16 | 16-bi-co-tri-torusing | even, bi | other, social | face | — | inward | — | — | the society wound: each self's 8 and offerings |
| 17 | 17-tri-co-offering | odd, co | social, self | connector | along | — | co-competent-so-far | with the self at co-competent-so-far, its 9 | the society's next momentary: each self's 1, then 9 at 6, 10 and 9 |

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
| 1-co-bi-offering · 2-bi-co-offering | bi-momentarying | the self's entry, odd, and the others' offerings, even, one momentary at each side |
| 3-co-bi-sharing · 4-bi-co-sharing | co-intelligencing | at each sharing 4 the carrying at 3 couples with the offerings surfaced at 14: next discovered, chained at 11 |
| 5-co-competencing | co-competencing | the joins, owned by neither: each release to its receiving sharing |
| 6-bi-moralizing | bi-moralizing | each changing released across, to the other's 2 |
| 12-bi-tri-parity-changing | the shape of the unrelationing surface | each sharing's changing, is or is not |
| 1 to 9 | bi-coupling | the function 1, the self and the other at one coupling; 9 at its end reads bi-co-releasing, the release 10 makes |
| 1 to 17 | bi-trupling | the function 17, the self, the other and the society; 9 at its waist, tri-bi-co-momentarying, joined both ways with 17; the protocol's two sides, the odd along at 9 and 17 and the even across at 6 to 2 and 10 to 14 |
| 1 to 17, stable-forming | bi-tri-volutioning | at no one line: each momentary's carrying the next momentary's |

| Four-cycle, 8 up and 17 less | Root at the self and at the society | Round |
|---|---|---|
| 1-9-8-16 | torusing, 8 and 16 | round the other way with 2-15-7-10 |
| 2-15-7-10 | corusing, 7 and 15 | round the other way with 1-9-8-16 and 3-11-6-14 |
| 3-11-6-14 | moralizing, 6 and 14 | round the other way with 4-13-5-12 and 2-15-7-10 |
| 4-13-5-12 | competencing, 5 and 13 | round the other way with 3-11-6-14 |

| Loop | Joining | Closing | Across or along |
|---|---|---|---|
| the other's | 6 to 2 | 8 | across, not-yet-bi-moral to bi-moral-so-far |
| the society's | 10 to 14 | 16 | across, not-yet-bi-moral to bi-moral-so-far |
| the self's | 9 to 17 | 17 | along, not-yet-co-competent to co-competent-so-far |

| n | Name | At this 1–17 | At the 1–17s inward, n at 8n − 7 | At the 1–17 outward, 8m − 7 at m |
|---|---|---|---|---|
| 1 | 1-co-bi-offering | entry, odd, co | 1 of the 1st: entry, odd, co | 1: entry, odd, co |
| 2 | 2-bi-co-offering | across, even, bi | 9 of the 1st: along, odd, co | within 1 to 2 |
| 3 | 3-co-bi-sharing | face outward, odd, co | 17 of the 1st, 1 of the 2nd: along, odd, co | within 1 to 2 |
| 4 | 4-bi-co-sharing | face outward, even, bi | 9 of the 2nd: along, odd, co | within 1 to 2 |
| 5 | 5-co-competencing | face outward, odd, co | 17 of the 2nd, 1 of the 3rd: along, odd, co | within 1 to 2 |
| 6 | 6-bi-moralizing | across, even, bi | 9 of the 3rd: along, odd, co | within 1 to 2 |
| 7 | 7-co-corusing | face outward, odd, co | 17 of the 3rd, 1 of the 4th: along, odd, co | within 1 to 2 |
| 8 | 8-bi-torusing | face outward, even, bi | 9 of the 4th: along, odd, co | within 1 to 2 |
| 9 | 9-tri-bi-co-momentarying | along, odd, co | 17 of the 4th, 1 of the 5th: along, odd, co | 2: across, even, bi |
| 10 | 10-bi-tri-co-tunneling | across, even, bi | 9 of the 5th: along, odd, co | within 2 to 3 |
| 11 | 11-tri-bi-co-chaining | face inward, odd, co | 17 of the 5th, 1 of the 6th: along, odd, co | within 2 to 3 |
| 12 | 12-bi-tri-parity-changing | face inward, even, bi | 9 of the 6th: along, odd, co | within 2 to 3 |
| 13 | 13-co-tri-competencing | face inward, odd, co | 17 of the 6th, 1 of the 7th: along, odd, co | within 2 to 3 |
| 14 | 14-bi-tri-moralizing | across, even, bi | 9 of the 7th: along, odd, co | within 2 to 3 |
| 15 | 15-co-bi-tri-corusing | face inward, odd, co | 17 of the 7th, 1 of the 8th: along, odd, co | within 2 to 3 |
| 16 | 16-bi-co-tri-torusing | face inward, even, bi | 9 of the 8th: along, odd, co | within 2 to 3 |
| 17 | 17-tri-co-offering | along, odd, co | 17 of the 8th, 1 of the 9th: along, odd, co | 3: face outward, odd, co |

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
| first | 1–2 | 2–3 | 1-co-bi-offering · 2-bi-co-offering · 3-co-bi-sharing | self/other |
| second | 3–4 | 4–5 | 3-co-bi-sharing · 4-bi-co-sharing · 5-co-competencing | self/other to other/self |
| third | 5–6 | 6–7 | 5-co-competencing · 6-bi-moralizing · 7-co-corusing | other/self |
| fourth | 7–8 | 8–9 | 7-co-corusing · 8-bi-torusing · 9-tri-bi-co-momentarying | other/self to other/social |

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
| 2-bi-co-offering | each other's releasing, offered to the self | 10-bi-tri-co-tunneling | the self among other-selves |
| 4-bi-co-sharing | the whole ordering between self and other | 12-bi-tri-parity-changing | changing at bi-coupling, the self in society |
| 6-bi-moralizing | the other's moralizing to the self, each changing released across | 14-bi-tri-moralizing | the offerings surfacing, the self's own inverting, morality |
| 8-bi-torusing | the carrying winding to its sharing again | 16-bi-co-tri-torusing | competency asymmetry sustaining the coupling, the society winding to the self again |

| Name | 8 up | 9 less, within 1 to 8 | 17 less, within 1 to 16 |
|---|---|---|---|
| 1-co-bi-offering | 9-tri-bi-co-momentarying | 8-bi-torusing | 16-bi-co-tri-torusing |
| 2-bi-co-offering | 10-bi-tri-co-tunneling | 7-co-corusing | 15-co-bi-tri-corusing |
| 3-co-bi-sharing | 11-tri-bi-co-chaining | 6-bi-moralizing | 14-bi-tri-moralizing |
| 4-bi-co-sharing | 12-bi-tri-parity-changing | 5-co-competencing | 13-co-tri-competencing |

| Form | Names in order | Round | Partner at the odd momentaries | Partner at the even momentaries |
|---|---|---|---|---|
| four-cycle 1-9-8-16 | 1-co-bi-offering · 9-tri-bi-co-momentarying · 8-bi-torusing · 16-bi-co-tri-torusing | co co bi bi | four-cycle 2-15-7-10, round the other way | — |
| four-cycle 2-15-7-10 | 2-bi-co-offering · 15-co-bi-tri-corusing · 7-co-corusing · 10-bi-tri-co-tunneling | bi co co bi | four-cycle 1-9-8-16, round the other way | four-cycle 3-11-6-14, round the other way |
| four-cycle 3-11-6-14 | 3-co-bi-sharing · 11-tri-bi-co-chaining · 6-bi-moralizing · 14-bi-tri-moralizing | co co bi bi | four-cycle 4-13-5-12, round the other way | four-cycle 2-15-7-10, round the other way |
| four-cycle 4-13-5-12 | 4-bi-co-sharing · 13-co-tri-competencing · 5-co-competencing · 12-bi-tri-parity-changing | bi co co bi | four-cycle 3-11-6-14, round the other way | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | 9-tri-bi-co-momentarying · 5-co-competencing · 12-bi-tri-parity-changing · 8-bi-torusing | co co bi bi | middle four-cycle 7-11-6-10, round the other way | — |
| middle four-cycle 7-11-6-10 | 7-co-corusing · 11-tri-bi-co-chaining · 6-bi-moralizing · 10-bi-tri-co-tunneling | co co bi bi | middle four-cycle 9-5-12-8, round the other way | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | 1-co-bi-offering · 9-tri-bi-co-momentarying · 5-co-competencing · 12-bi-tri-parity-changing · 8-bi-torusing · 16-bi-co-tri-torusing | co co co bi bi bi | six-cycle 2-15-7-11-6-10, round the other way | — |
| six-cycle 2-15-7-11-6-10 | 2-bi-co-offering · 15-co-bi-tri-corusing · 7-co-corusing · 11-tri-bi-co-chaining · 6-bi-moralizing · 10-bi-tri-co-tunneling | bi co co co bi bi | six-cycle 1-9-5-12-8-16, round the other way | six-cycle 3-11-7-10-6-14, round the other way |
| six-cycle 3-11-7-10-6-14 | 3-co-bi-sharing · 11-tri-bi-co-chaining · 7-co-corusing · 10-bi-tri-co-tunneling · 6-bi-moralizing · 14-bi-tri-moralizing | co co co bi bi bi | six-cycle 4-13-5-9-8-12, round the other way | six-cycle 2-15-7-11-6-10, round the other way |
| six-cycle 4-13-5-9-8-12 | 4-bi-co-sharing · 13-co-tri-competencing · 5-co-competencing · 9-tri-bi-co-momentarying · 8-bi-torusing · 12-bi-tri-parity-changing | bi co co co bi bi | six-cycle 3-11-7-10-6-14, round the other way | — |
| eight-cycle 1-9-5-13-4-12-8-16 | 1-co-bi-offering · 9-tri-bi-co-momentarying · 5-co-competencing · 13-co-tri-competencing · 4-bi-co-sharing · 12-bi-tri-parity-changing · 8-bi-torusing · 16-bi-co-tri-torusing | co co co co bi bi bi bi | eight-cycle 2-15-7-11-3-14-6-10, round the other way | — |
| eight-cycle 2-15-7-11-3-14-6-10 | 2-bi-co-offering · 15-co-bi-tri-corusing · 7-co-corusing · 11-tri-bi-co-chaining · 3-co-bi-sharing · 14-bi-tri-moralizing · 6-bi-moralizing · 10-bi-tri-co-tunneling | bi co co co co bi bi bi | eight-cycle 1-9-5-13-4-12-8-16, round the other way | eight-cycle 2-15-7-11-3-14-6-10, itself |

| Offerings, momentary by momentary | At 10 | Chained at 11 |
|---|---|---|
| + once, then none | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| + at each momentary | +, 0, 0, 0, 0, 0, 0 | +, +, +, +, +, +, + |
| −, +, −, + alternating | −, +, −, +, −, + | −, +, −, +, −, + |
| + once, then + and − together | +, −, +, −, +, − | +, −, +, −, +, − |

| Selves | Self 1 at 10, momentaries 1 to 12 | Round, from momentary n | None chained again |
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

| Rings, selves | Beside each other, round | Crossed at self 1 of each both ways, round | From momentary | Self 1 of each | Each ring's pair at one parity |
|---|---|---|---|---|---|
| 2 · 3 | 12 | 2 | 7 | opposite | none · selves 3 and 1 |
| 3 · 5 | 60 | 2 | 13 | opposite | selves 3 and 1 · selves 5 and 1 |
| 5 · 7 | 140 | 2 | 20 | opposite | selves 5 and 1 · selves 7 and 1 |
| 7 · 11 | 308 | 2 | 29 | opposite | selves 7 and 1 · selves 11 and 1 |
| 11 · 13 | 572 | 2 | 37 | opposite | selves 11 and 1 · selves 13 and 1 |
| 13 · 17 | 884 | 2 | 49 | opposite | selves 13 and 1 · selves 17 and 1 |
| 17 · 59 | 4,012 | 2 | 137 | opposite | selves 17 and 1 · selves 59 and 1 |
| 9 · 15 | 180 | 2 | 41 | opposite | selves 9 and 1 · selves 15 and 1 |

| Torus of selves, p along at 9 · q across at 10 | Round, one offering at self 1 | From momentary | Rings of p and q beside each other, round |
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

| A's parity offered at B | B at 10 | B chained | C at 10, momentaries 1 and 2 | C chained |
|---|---|---|---|---|
| + | 0 | + | −, + | + |
| − | − | − | −, 0 | − |
