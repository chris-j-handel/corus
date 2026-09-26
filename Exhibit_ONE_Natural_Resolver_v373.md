Exhibit ONE Natural Resolver v373

# Natural Resolver

**Geodesic Discovering Logical Method and Form**

---

```python
"""Exhibit ONE · Natural Resolver"""


def _1_self_other_offering(_3_self_other_sharing, _2_other_self_offering):
    _14_other_social_surfacing = {}
    for _4_other_self_sharing, _7_self_other_corusing in _2_other_self_offering:
        if _7_self_other_corusing != 0:
            _15_social_other_corusing = _14_other_social_surfacing.get(_4_other_self_sharing)
            if _15_social_other_corusing is None:
                _14_other_social_surfacing[_4_other_self_sharing] = 1 if _7_self_other_corusing > 0 else -1
            elif (_15_social_other_corusing > 0) != (_7_self_other_corusing > 0):
                _14_other_social_surfacing[_4_other_self_sharing] = 0
    _12_other_social_self_abundancing = dict(_14_other_social_surfacing)
    for _4_other_self_sharing, _7_self_other_corusing in _3_self_other_sharing:
        _15_social_other_corusing = _14_other_social_surfacing.get(_4_other_self_sharing, 0)
        if _15_social_other_corusing != 0 and (_15_social_other_corusing > 0) == (_7_self_other_corusing > 0):
            _12_other_social_self_abundancing[_4_other_self_sharing] = 0
        else:
            _12_other_social_self_abundancing[_4_other_self_sharing] = -1 if _7_self_other_corusing > 0 else 1
    _10_other_social_self_tunneling = list(_12_other_social_self_abundancing.items())
    _11_social_other_self_chaining = dict(_3_self_other_sharing)
    for _4_other_self_sharing, _7_self_other_corusing in _10_other_social_self_tunneling:
        if _7_self_other_corusing != 0:
            _11_social_other_self_chaining[_4_other_self_sharing] = _7_self_other_corusing
    return _10_other_social_self_tunneling, list(_11_social_other_self_chaining.items())


def _9_social_other_self_releasing(_10_other_social_self_tunneling, _5_self_other_neutralling):
    return [(_5_self_other_neutralling[_13_social_other_neutralling], _15_social_other_corusing)
            for _13_social_other_neutralling, _15_social_other_corusing in _10_other_social_self_tunneling]


def _17_social_self_offering(_16_other_social_torusing, _5_self_other_neutralling):
    _8_other_self_torusing = {}
    _14_other_social_surfacing = {_13_social_other_neutralling: [] for _13_social_other_neutralling in _16_other_social_torusing}
    for _13_social_other_neutralling, (_3_self_other_sharing, _2_other_self_offering) in _16_other_social_torusing.items():
        _10_other_social_self_tunneling, _8_other_self_torusing[_13_social_other_neutralling] = _1_self_other_offering(
            _3_self_other_sharing, _2_other_self_offering)
        _6_other_self_surfacing = _10_other_social_self_tunneling
        for _4_other_self_sharing, _15_social_other_corusing in _9_social_other_self_releasing(
                [(_4_other_self_sharing, _15_social_other_corusing)
                 for _4_other_self_sharing, _15_social_other_corusing in (
                     ((_13_social_other_neutralling, 6), _6_other_self_surfacing),
                     ((_13_social_other_neutralling, 10), _10_other_social_self_tunneling),
                     ((_13_social_other_neutralling, 9), _10_other_social_self_tunneling))
                 if _4_other_self_sharing in _5_self_other_neutralling],
                _5_self_other_neutralling):
            _14_other_social_surfacing[_4_other_self_sharing].extend(_15_social_other_corusing)
    return {_13_social_other_neutralling: (_8_other_self_torusing[_13_social_other_neutralling],
                                           _14_other_social_surfacing[_13_social_other_neutralling])
            for _13_social_other_neutralling in _16_other_social_torusing}

CONNECTORS = {
    2: ('2-other-self-offering', 'bi-moral', 'arriving'),
    6: ('6-other-self-surfacing', 'not-bi-moral', 'releasing'),
    9: ('9-social-other-self-releasing', 'not-co-competent', 'along'),
    10: ('10-other-social-self-tunneling', 'bi-moral', 'releasing'),
    14: ('14-other-social-surfacing', 'not-bi-moral', 'arriving'),
    17: ('17-social-self-offering', 'co-competent', 'along'),
}
JOINS = {10: 14, 6: 2, 17: 9, 9: 17}
```

```text
                        the self at co-competent, its 9
                                      ▲
                                      ║ 17  along · co
      ┌───────────────────────────────╨───────────────────────────────┐
      │                          1  entry                             │
      │                                                               │
 ══════► 14i ◄───────────────────────────────────────────────── 2 ◄══════
      │   │   offerings surfacing at each sharing: +, − or 0          │
      │   ▼                                                           │
      │   3o ─────► 12i ────────► 10 ══════════════════════════════════════►
      │   4o · 7o   changing,     + or −: is                          │
      │   carrying  is or is not  0: is not                           │
      │                           │                                   │
      │                           ├──────► 11i ─────► 3o, next        │
      │                           │        chaining   momentary       │
      │                           │                                   │
      │                           └──────► 9 ────► 5o                 │
      │                                    13i · 15i                  │
 ◄══════ 6                                                            │
      │   8o carrying wound · 16i society wound                       │
      └───────────────────────────────╥───────────────────────────────┘
                                      ║ 9  along · co
                                      ▼
                        the self at not-co-competent, its 17

   at not-bi-moral   its 10 ══► 14       6  ══► its 2
   at bi-moral       its 6  ══► 2        10 ══► its 14
   ═══ between selves, across and along    ─── within one self
   o outward face    i inward face
```

| n | Name | Parity, opens | From, to | Entry, connector or face | Across or along | Outward or inward | Facing | Joining | At the code |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1-self-other-offering | odd, co | self, other | entry | — | — | — | — | the entry: 3 and 2 in; 10 and 11 out |
| 2 | 2-other-self-offering | even, bi | other, self | connector | across | — | bi-moral | from the self at bi-moral, its 6 | the offerings, each sharing with its parity |
| 3 | 3-self-other-sharing | odd, co | self, other | face | — | outward | — | — | the carrying: each sharing, 4, with its parity, 7 |
| 4 | 4-other-self-sharing | even, bi | other, self | face | — | outward | — | — | each sharing; at the society, each self at 6, 10 and 9 |
| 5 | 5-self-other-neutralling | odd, co | self, other | face | — | outward | — | — | each sharing's receiving sharing; at the society, the joins |
| 6 | 6-other-self-surfacing | even, bi | other, self | connector | across | — | not-bi-moral | to the self at not-bi-moral, its 2 | the changing released at not-bi-moral, at that self's 2 |
| 7 | 7-self-other-corusing | odd, co | self, other | face | — | outward | — | — | each parity, offered and chained |
| 8 | 8-other-self-torusing | even, bi | other, self | face | — | outward | — | — | each self's carrying wound, its 11 the next momentary's 3 |
| 9 | 9-social-other-self-releasing | odd, co | social, other, self | connector | along | — | not-co-competent | with the self at not-co-competent, its 17 | each changing to its receiving sharing, 5 |
| 10 | 10-other-social-self-tunneling | even, bi | other, social, self | connector | across | — | bi-moral | to the self at bi-moral, its 14 | each sharing's changing: + or − is, 0 is not |
| 11 | 11-social-other-self-chaining | odd, co | social, other, self | face | — | inward | — | — | the carrying chained, each changing the next prior |
| 12 | 12-other-social-self-abundancing | even, bi | other, social, self | face | — | inward | — | — | each sharing's changing, is or is not |
| 13 | 13-social-other-neutralling | odd, co | social, other | face | — | inward | — | — | each releasing sharing; at the society, each releasing self |
| 14 | 14-other-social-surfacing | even, bi | other, social | connector | across | — | not-bi-moral | from the self at not-bi-moral, its 10 | the offerings surfacing at each sharing: +, − or 0; at the society, each self's offerings next |
| 15 | 15-social-other-corusing | odd, co | social, other | face | — | inward | — | — | the parity released at 9 |
| 16 | 16-other-social-torusing | even, bi | other, social | face | — | inward | — | — | the society wound: each self's 8 and offerings |
| 17 | 17-social-self-offering | odd, co | social, self | connector | along | — | co-competent | with the self at co-competent, its 9 | the society's next momentary: each self's 1, then 9 at 6, 10 and 9 |

| Root | Names |
|---|---|
| offering | 1 · 2 · 17 |
| sharing | 3 · 4 |
| neutralling | 5 · 13 |
| surfacing | 6 · 14 |
| corusing | 7 · 15 |
| torusing | 8 · 16 |
| releasing | 9 |
| tunneling | 10 |
| chaining | 11 |
| abundancing | 12 |

| Loop | Releasing | Closing | Across or along |
|---|---|---|---|
| the other's | 6 to 2 | 8 | across, not-bi-moral |
| the society's | 10 to 14 | 16 | across, bi-moral |
| the self's | 9 to 17 | 17 | along, not-co-competent to co-competent |

| n | Name | At this 1–17 | At the 1–17s inward, n at 8n − 7 | At the 1–17 outward, 8m − 7 at m |
|---|---|---|---|---|
| 1 | 1-self-other-offering | entry, odd, co | 1 of the 1st: entry, odd, co | 1: entry, odd, co |
| 2 | 2-other-self-offering | across, even, bi | 9 of the 1st: along, odd, co | within 1 to 2 |
| 3 | 3-self-other-sharing | face outward, odd, co | 17 of the 1st, 1 of the 2nd: along, odd, co | within 1 to 2 |
| 4 | 4-other-self-sharing | face outward, even, bi | 9 of the 2nd: along, odd, co | within 1 to 2 |
| 5 | 5-self-other-neutralling | face outward, odd, co | 17 of the 2nd, 1 of the 3rd: along, odd, co | within 1 to 2 |
| 6 | 6-other-self-surfacing | across, even, bi | 9 of the 3rd: along, odd, co | within 1 to 2 |
| 7 | 7-self-other-corusing | face outward, odd, co | 17 of the 3rd, 1 of the 4th: along, odd, co | within 1 to 2 |
| 8 | 8-other-self-torusing | face outward, even, bi | 9 of the 4th: along, odd, co | within 1 to 2 |
| 9 | 9-social-other-self-releasing | along, odd, co | 17 of the 4th, 1 of the 5th: along, odd, co | 2: across, even, bi |
| 10 | 10-other-social-self-tunneling | across, even, bi | 9 of the 5th: along, odd, co | within 2 to 3 |
| 11 | 11-social-other-self-chaining | face inward, odd, co | 17 of the 5th, 1 of the 6th: along, odd, co | within 2 to 3 |
| 12 | 12-other-social-self-abundancing | face inward, even, bi | 9 of the 6th: along, odd, co | within 2 to 3 |
| 13 | 13-social-other-neutralling | face inward, odd, co | 17 of the 6th, 1 of the 7th: along, odd, co | within 2 to 3 |
| 14 | 14-other-social-surfacing | across, even, bi | 9 of the 7th: along, odd, co | within 2 to 3 |
| 15 | 15-social-other-corusing | face inward, odd, co | 17 of the 7th, 1 of the 8th: along, odd, co | within 2 to 3 |
| 16 | 16-other-social-torusing | face inward, even, bi | 9 of the 8th: along, odd, co | within 2 to 3 |
| 17 | 17-social-self-offering | along, odd, co | 17 of the 8th, 1 of the 9th: along, odd, co | 3: face outward, odd, co |

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
| first | 1–2 | 2–3 | 1-self-other-offering · 2-other-self-offering · 3-self-other-sharing | self/other |
| second | 3–4 | 4–5 | 3-self-other-sharing · 4-other-self-sharing · 5-self-other-neutralling | self/other to other/self |
| third | 5–6 | 6–7 | 5-self-other-neutralling · 6-other-self-surfacing · 7-self-other-corusing | other/self |
| fourth | 7–8 | 8–9 | 7-self-other-corusing · 8-other-self-torusing · 9-social-other-self-releasing | other/self to other/social |

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

| Outward, at the between | Bi-coupling | Inward, 8 on | Bi-coupling |
|---|---|---|---|
| 2-other-self-offering | each other's own offering to the self | 10-other-social-self-tunneling | the self among other-selves |
| 4-other-self-sharing | the whole ordering between self and other | 12-other-social-self-abundancing | changing at bi-coupling, the self in society |
| 6-other-self-surfacing | the other's surfacing to the self | 14-other-social-surfacing | the offerings surfacing, the self's own inverting, morality |
| 8-other-self-torusing | the carrying winding to its sharing again | 16-other-social-torusing | competency asymmetry sustaining the coupling, the society winding to the self again |

| Name | 8 up | 9 less, within 1 to 8 | 17 less, within 1 to 16 |
|---|---|---|---|
| 1-self-other-offering | 9-social-other-self-releasing | 8-other-self-torusing | 16-other-social-torusing |
| 2-other-self-offering | 10-other-social-self-tunneling | 7-self-other-corusing | 15-social-other-corusing |
| 3-self-other-sharing | 11-social-other-self-chaining | 6-other-self-surfacing | 14-other-social-surfacing |
| 4-other-self-sharing | 12-other-social-self-abundancing | 5-self-other-neutralling | 13-social-other-neutralling |

| Form | Names in order | Round | Partner at the odd momentaries | Partner at the even momentaries |
|---|---|---|---|---|
| four-cycle 1-9-8-16 | 1-self-other-offering · 9-social-other-self-releasing · 8-other-self-torusing · 16-other-social-torusing | co co bi bi | four-cycle 2-15-7-10, round the other way | — |
| four-cycle 2-15-7-10 | 2-other-self-offering · 15-social-other-corusing · 7-self-other-corusing · 10-other-social-self-tunneling | bi co co bi | four-cycle 1-9-8-16, round the other way | four-cycle 3-11-6-14, round the other way |
| four-cycle 3-11-6-14 | 3-self-other-sharing · 11-social-other-self-chaining · 6-other-self-surfacing · 14-other-social-surfacing | co co bi bi | four-cycle 4-13-5-12, round the other way | four-cycle 2-15-7-10, round the other way |
| four-cycle 4-13-5-12 | 4-other-self-sharing · 13-social-other-neutralling · 5-self-other-neutralling · 12-other-social-self-abundancing | bi co co bi | four-cycle 3-11-6-14, round the other way | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | 9-social-other-self-releasing · 5-self-other-neutralling · 12-other-social-self-abundancing · 8-other-self-torusing | co co bi bi | middle four-cycle 7-11-6-10, round the other way | — |
| middle four-cycle 7-11-6-10 | 7-self-other-corusing · 11-social-other-self-chaining · 6-other-self-surfacing · 10-other-social-self-tunneling | co co bi bi | middle four-cycle 9-5-12-8, round the other way | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | 1-self-other-offering · 9-social-other-self-releasing · 5-self-other-neutralling · 12-other-social-self-abundancing · 8-other-self-torusing · 16-other-social-torusing | co co co bi bi bi | six-cycle 2-15-7-11-6-10, round the other way | — |
| six-cycle 2-15-7-11-6-10 | 2-other-self-offering · 15-social-other-corusing · 7-self-other-corusing · 11-social-other-self-chaining · 6-other-self-surfacing · 10-other-social-self-tunneling | bi co co co bi bi | six-cycle 1-9-5-12-8-16, round the other way | six-cycle 3-11-7-10-6-14, round the other way |
| six-cycle 3-11-7-10-6-14 | 3-self-other-sharing · 11-social-other-self-chaining · 7-self-other-corusing · 10-other-social-self-tunneling · 6-other-self-surfacing · 14-other-social-surfacing | co co co bi bi bi | six-cycle 4-13-5-9-8-12, round the other way | six-cycle 2-15-7-11-6-10, round the other way |
| six-cycle 4-13-5-9-8-12 | 4-other-self-sharing · 13-social-other-neutralling · 5-self-other-neutralling · 9-social-other-self-releasing · 8-other-self-torusing · 12-other-social-self-abundancing | bi co co co bi bi | six-cycle 3-11-7-10-6-14, round the other way | — |
| eight-cycle 1-9-5-13-4-12-8-16 | 1-self-other-offering · 9-social-other-self-releasing · 5-self-other-neutralling · 13-social-other-neutralling · 4-other-self-sharing · 12-other-social-self-abundancing · 8-other-self-torusing · 16-other-social-torusing | co co co co bi bi bi bi | eight-cycle 2-15-7-11-3-14-6-10, round the other way | — |
| eight-cycle 2-15-7-11-3-14-6-10 | 2-other-self-offering · 15-social-other-corusing · 7-self-other-corusing · 11-social-other-self-chaining · 3-self-other-sharing · 14-other-social-surfacing · 6-other-self-surfacing · 10-other-social-self-tunneling | bi co co co co bi bi bi | eight-cycle 1-9-5-13-4-12-8-16, round the other way | eight-cycle 2-15-7-11-3-14-6-10, itself |

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
